#!/usr/bin/env python3
"""
Motor Autónomo de Síntesis de Voz Clonada y Alineación de Palabras (TTS Engine).
Utiliza Chatterbox Multilingual TTS con clonación vocal (.conds.pt) en GPU/CUDA,
faster-whisper para alineación temporal a nivel de palabra y poda estricta de pausas y colas residuales.
Soporta la jerarquía completa de capítulos y escenas de AutoPNGTuber-LongVideos.
"""

import argparse
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import tempfile
import warnings
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent


def _ensure_venv_python() -> None:
    """Re-ejecuta el script automáticamente en el entorno virtual con GPU/TTS si el Python actual no tiene chatterbox."""
    if os.environ.get("AUTOPNGTUBER_VENV_ACTIVE") == "1":
        return
    try:
        import chatterbox  # noqa: F401
        import faster_whisper  # noqa: F401
        import mutagen  # noqa: F401
        import torch  # noqa: F401
        return
    except ImportError:
        pass

    candidates = [
        ROOT_DIR.parent / "AIO" / "KidsAnimationStudio" / "voice-lab" / ".venv" / "Scripts" / "python.exe",
        ROOT_DIR / ".venv" / "Scripts" / "python.exe",
        ROOT_DIR.parent / ".venv" / "Scripts" / "python.exe",
    ]
    for candidate in candidates:
        if candidate.exists() and candidate.resolve() != Path(sys.executable).resolve():
            env = os.environ.copy()
            env["AUTOPNGTUBER_VENV_ACTIVE"] = "1"
            res = subprocess.run([str(candidate), *sys.argv], env=env)
            sys.exit(res.returncode)


_ensure_venv_python()

os.environ.setdefault("TQDM_DISABLE", "1")
os.environ.setdefault("HF_HUB_DISABLE_PROGRESS_BARS", "1")
os.environ.setdefault("TRANSFORMERS_VERBOSITY", "error")
warnings.filterwarnings("ignore")

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

try:
    import truststore
    truststore.inject_into_ssl()
except Exception:
    pass

import numpy as np
import soundfile as sf
import torch
from difflib import SequenceMatcher
from faster_whisper import WhisperModel
from mutagen.mp3 import MP3

from normalizador_numeros import normalizar_cifras_espanol

GUION_PATH = ROOT_DIR / "src" / "data" / "guion.json"
AUDIOS_DIR = ROOT_DIR / "public" / "audios"
VOICES_DIR = ROOT_DIR / "public" / "voices"
CACHE_PATH = AUDIOS_DIR / ".tts_cache.json"

DEFAULT_VOICE_CONDS = "alex.conds.pt"
PAUSE_SECONDS = 0.25
EXAGGERATION = 0.55
TEMPERATURE = 0.58
WHISPER_MODEL_SIZE = "base"
PIPELINE_VERSION = "v5_verified_chunk_no_cuts"
PUNCT_STRIP = "¿?¡!.,;:()\"'«»—–-[]{}"

ANGLICISMOS_FONETICOS = [
    (r"\bhackear\b", "jaquear"),
    (r"\bhackea\b", "jaquea"),
    (r"\bhackeó\b", "jaqueó"),
    (r"\bhackeado\b", "jaqueado"),
    (r"\bhacker\b", "jáquer"),
    (r"\bhackers\b", "jáquers"),
    (r"\bsoftware\b", "sóftuer"),
    (r"\bhardware\b", "járduer"),
    (r"\bRudolph\s+Zallinger\b", "Rúdolf Zálinguer"),
    (r"\bStephen\s+Jay\s+Gould\b", "Estíven Yéi Guld"),
    (r"\bLeslie\s+Aiello\b", "Lésli Aiélo"),
    (r"\bPeter\s+Wheeler\b", "Píter Uíler"),
    (r"\bRichard\s+Wrangham\b", "Ríchard Rángam"),
    (r"\bKaren\s+Rosenberg\b", "Káren Rósenberg"),
    (r"\bWenda\s+Trevathan\b", "Uénda Trevátan"),
    (r"\bPeter\s+Godfrey[-\s]+Smith\b", "Píter Gódfri Esmít"),
    (r"\bGodfrey[-\s]+Smith\b", "Gódfri Esmít"),
    (r"\bWilder\s+Penfield\b", "Uáilder Pénfild"),
    (r"\bDoron\s+Behar\b", "Dóron Béjar"),
    (r"\bStanley\s+Ambrose\b", "Estánli Ámbrous"),
    (r"\bCharles\s+Darwin\b", "Chárls Dáruin"),
]


def fonetizar_para_tts(texto: str) -> str:
    """Adapta anglicismos al español fonético exclusivamente para el motor TTS."""
    res = texto
    for patron, fonetico in ANGLICISMOS_FONETICOS:
        res = re.sub(patron, fonetico, res, flags=re.IGNORECASE)
    return res


def resolver_archivo_condiciones(nombre_conds: str = DEFAULT_VOICE_CONDS) -> Path:
    """Busca el archivo .conds.pt en public/voices o rutas candidatas."""
    candidatos = [
        VOICES_DIR / nombre_conds,
        VOICES_DIR / (f"{nombre_conds}.conds.pt" if not nombre_conds.endswith(".conds.pt") else nombre_conds),
        VOICES_DIR / "narrador.conds.pt",
        VOICES_DIR / "alex.conds.pt",
        VOICES_DIR / "alejandro.conds.pt",
        VOICES_DIR / "voice-alex.conds.pt",
        ROOT_DIR / nombre_conds,
        ROOT_DIR.parent / "AutoPNGTuber" / "public" / "voices" / nombre_conds,
    ]
    for ruta in candidatos:
        if ruta.exists():
            return ruta.resolve()
    raise FileNotFoundError(
        f"No se encontró el archivo de condiciones de voz ({nombre_conds}) en {VOICES_DIR}"
    )


def calcular_hash_escena(texto: str, conds_path: Path, silencio_extra: float = 0.0) -> str:
    """Calcula el hash SHA-256 determinista del texto normalizado, versión del pipeline y condiciones."""
    normalizado = re.sub(r"\s+", " ", texto.strip())
    sil_tag = f"::sil={silencio_extra:.2f}" if silencio_extra > 0 else ""
    payload = f"{PIPELINE_VERSION}::{conds_path.name}::{normalizado}{sil_tag}".encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def cargar_cache() -> dict:
    if CACHE_PATH.exists():
        try:
            with open(CACHE_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def guardar_cache(cache: dict) -> None:
    AUDIOS_DIR.mkdir(parents=True, exist_ok=True)
    with open(CACHE_PATH, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)


def limpiar_texto_narracion(texto: str) -> str:
    if not texto:
        return ""
    texto = re.sub(r"[*_#`~]", "", texto)
    texto = re.sub(r"\[.*?\]|\(.*?\)", "", texto)
    texto = re.sub(r"\.{2,}|…", ". ", texto)
    texto = re.sub(r"[—–-]{2,}", ", ", texto)
    texto = normalizar_cifras_espanol(texto)
    return re.sub(r"\s+", " ", texto).strip()


def dividir_en_fragmentos(texto: str, max_chars: int = 105) -> list[str]:
    """Fragmenta en cláusulas naturales cortas y garantiza cierre oracional limpio para evitar cortes de EOS en Chatterbox."""
    limpio = limpiar_texto_narracion(texto)
    if not limpio:
        return []

    raw_oraciones = [s.strip() for s in re.split(r"(?<=[.!?])\s+", limpio) if s.strip()]

    # Fusionar oraciones diminutas (ej. "¿Por qué?") con la siguiente para evitar micro-cláusulas
    partes_oracion = []
    i = 0
    while i < len(raw_oraciones):
        actual = raw_oraciones[i]
        if (len(actual.split()) <= 3 or len(actual) <= 18) and i + 1 < len(raw_oraciones):
            combinada = f"{actual} {raw_oraciones[i + 1]}"
            if len(combinada) <= max_chars + 20:
                partes_oracion.append(combinada)
                i += 2
                continue
        partes_oracion.append(actual)
        i += 1

    fragmentos = []
    for oracion in partes_oraciones_iter(partes_oracion):
        if len(oracion) <= max_chars:
            fragmentos.append(oracion)
        else:
            clausulas = [s.strip() for s in re.split(r"(?<=[,;:])\s+", oracion) if s.strip()]
            if len(clausulas) > 1:
                actual = ""
                for c in clausulas:
                    if len(c) > max_chars:
                        if actual:
                            fragmentos.append(actual)
                            actual = ""
                        palabras_c = c.split()
                        bloque_c = []
                        for p in palabras_c:
                            if bloque_c and len(" ".join(bloque_c)) + 1 + len(p) > max_chars:
                                fragmentos.append(" ".join(bloque_c))
                                bloque_c = [p]
                            else:
                                bloque_c.append(p)
                        if bloque_c:
                            actual = " ".join(bloque_c)
                    elif not actual:
                        actual = c
                    elif len(actual) + 1 + len(c) <= max_chars:
                        actual = f"{actual} {c}"
                    else:
                        fragmentos.append(actual)
                        actual = c
                if actual:
                    fragmentos.append(actual)
            else:
                palabras = oracion.split()
                bloque = []
                for p in palabras:
                    if bloque and len(" ".join(bloque)) + 1 + len(p) > max_chars:
                        fragmentos.append(" ".join(bloque))
                        bloque = [p]
                    else:
                        bloque.append(p)
                if bloque:
                    fragmentos.append(" ".join(bloque))

    # Garantizar puntuación terminal limpia (. ! ?) en cada fragmento para evitar truncamientos de EOS
    normalizados = []
    for f in (fragmentos if fragmentos else [limpio]):
        f = f.strip()
        if not f:
            continue
        if f[-1] in ",;:":
            f = f[:-1].rstrip() + "."
        elif f[-1] not in ".!?":
            f = f + "."
        normalizados.append(f)

    return normalizados if normalizados else [limpio]


def _extraer_tokens_comparables(texto: str) -> list[str]:
    expandido = normalizar_cifras_espanol(texto.lower())
    limpio = re.sub(r"[^\w\sáéíóúüñ]", " ", expandido)
    return [w for w in limpio.split() if w]


def _recortar_bordes_silencio_seguro(wav_np: np.ndarray, sr: int) -> np.ndarray:
    """Recorta únicamente silencio digital/acústico puro en los extremos conservando ataque y decaimiento natural."""
    if len(wav_np) < int(sr * 0.08):
        return wav_np
    win = max(1, int(sr * 0.015))
    n_wins = len(wav_np) // win
    if n_wins < 4:
        return wav_np
    trimmed = wav_np[: n_wins * win].reshape(n_wins, win)
    rms = np.sqrt(np.mean(trimmed * trimmed, axis=1))
    activos = np.where(rms >= 0.0055)[0]
    if len(activos) == 0:
        return wav_np

    s0 = max(0, int(activos[0] * win) - int(sr * 0.045))
    s1 = min(len(wav_np), int((activos[-1] + 1) * win) + int(sr * 0.125))
    out = wav_np[s0:s1].copy()
    if len(out) > int(sr * 0.04):
        fi = min(int(sr * 0.010), len(out))
        fo = min(int(sr * 0.028), len(out))
        out[:fi] *= np.linspace(0.0, 1.0, fi)
        out[-fo:] *= np.linspace(1.0, 0.0, fo)
    return out


def _dividir_fragmento_mitad(frag: str) -> tuple[str, str]:
    """Divide un fragmento largo en dos mitades sintácticas limpias cuando T3 trunca por longitud."""
    texto_sin_punto = frag.rstrip(".!? ").strip()
    palabras = texto_sin_punto.split()
    mid = len(palabras) // 2
    conectores = {"y", "e", "o", "u", "pero", "sino", "que", "donde", "cuando", "como", "para", "porque", "mientras", "aunque"}
    mejor_corte = mid
    for delta in range(0, min(6, mid)):
        for cand in (mid + delta, mid - delta):
            if 2 <= cand <= len(palabras) - 2:
                prev_tiene_coma = palabras[cand - 1].endswith((",", ";", ":"))
                es_conector = palabras[cand].lower().strip(PUNCT_STRIP) in conectores
                if prev_tiene_coma or es_conector:
                    mejor_corte = cand
                    break
        else:
            continue
        break
    p1 = " ".join(palabras[:mejor_corte]).rstrip(",;: ") + "."
    p2 = " ".join(palabras[mejor_corte:]).rstrip(",;: ") + "."
    return p1, p2


def partes_oraciones_iter(partes: list[str]) -> list[str]:
    return partes


class LocalClonedTTS:
    """Motor TTS local de voz clonada (.conds.pt) con Chatterbox en GPU/CUDA."""

    def __init__(self, conds_path: Path, exaggeration: float = EXAGGERATION) -> None:
        self.conds_path = conds_path
        self.exaggeration = exaggeration
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = None
        self.base_conds = None

    def asegurar_modelo(self) -> None:
        if self.model is not None:
            return

        from chatterbox import ChatterboxMultilingualTTS
        from chatterbox.mtl_tts import Conditionals, T3Cond

        print(
            f"[TTS Clonado] 🎙️  Cargando modelo de clonación en {self.device.upper()} "
            f"con voz '{self.conds_path.name}'..."
        )
        self.model = ChatterboxMultilingualTTS.from_pretrained(device=self.device)
        self._conds_cache = {}
        self.cambiar_voz(self.conds_path)

    def cambiar_voz(self, conds_path: Path) -> None:
        self.asegurar_modelo()
        if not hasattr(self, "_conds_cache"):
            self._conds_cache = {}
        key = str(conds_path.resolve())
        if key not in self._conds_cache:
            from chatterbox.mtl_tts import Conditionals, T3Cond
            loaded_conds = Conditionals.load(conds_path, map_location=self.device).to(self.device)
            t3_cond = loaded_conds.t3
            new_t3 = T3Cond(
                speaker_emb=t3_cond.speaker_emb,
                cond_prompt_speech_tokens=t3_cond.cond_prompt_speech_tokens,
                emotion_adv=float(self.exaggeration) * torch.ones(1, 1, 1, device=self.device),
            ).to(device=self.device)
            self._conds_cache[key] = Conditionals(new_t3, loaded_conds.gen)
        self.conds_path = conds_path
        self.base_conds = self._conds_cache[key]
        self.model.conds = self.base_conds

    def _evaluar_fragmento_whisper(
        self,
        wav_np: np.ndarray,
        sr: int,
        frag_tts: str,
        whisper_model: WhisperModel | None,
    ) -> tuple[bool, float]:
        if whisper_model is None or len(wav_np) < int(sr * 0.12):
            return (len(wav_np) >= int(sr * 0.25), 0.5)

        exp_tokens = _extraer_tokens_comparables(frag_tts)
        if not exp_tokens:
            return (True, 1.0)

        target_len = max(160, int(round(len(wav_np) * 16000.0 / sr)))
        x_old = np.linspace(0.0, 1.0, num=len(wav_np), endpoint=False)
        x_new = np.linspace(0.0, 1.0, num=target_len, endpoint=False)
        wav_16k = np.interp(x_new, x_old, wav_np).astype(np.float32)

        segs, _ = whisper_model.transcribe(
            wav_16k,
            language="es",
            vad_filter=False,
            condition_on_previous_text=False,
        )
        heard_raw = " ".join(s.text.strip() for s in segs)
        got_tokens = _extraer_tokens_comparables(heard_raw)
        if not got_tokens:
            return (False, 0.0)

        seq_ratio = SequenceMatcher(None, exp_tokens, got_tokens).ratio()
        len_ratio = len(got_tokens) / max(1, len(exp_tokens))

        tail_n = min(2, len(exp_tokens))
        tail_exp = " ".join(exp_tokens[-tail_n:])
        tail_window = " ".join(got_tokens[-min(len(got_tokens), tail_n + 2) :])
        tail_sim = max(
            SequenceMatcher(None, tail_exp, " ".join(got_tokens[-tail_n:])).ratio(),
            1.0 if tail_exp in tail_window else 0.0,
        )

        score = 0.45 * seq_ratio + 0.25 * min(1.0, len_ratio) + 0.30 * tail_sim
        completo = seq_ratio >= 0.78 and len_ratio >= 0.84 and tail_sim >= 0.64
        return (completo, score)

    def _sintetizar_fragmento_verificado(
        self,
        frag: str,
        sr: int,
        temperature: float,
        whisper_model: WhisperModel | None,
        depth: int = 0,
    ) -> list[np.ndarray]:
        frag_tts = fonetizar_para_tts(frag)
        intentos_cfg = [
            (temperature, 2.0),
            (min(0.82, round(temperature + 0.08, 2)), 2.15),
            (min(0.86, round(temperature + 0.14, 2)), 1.85),
        ]
        max_tries = 3 if whisper_model is not None else 1

        mejor_wav = None
        mejor_score = -1.0

        for idx in range(max_tries):
            temp_i, rep_i = intentos_cfg[idx]
            wav_tensor = self.model.generate(
                text=frag_tts,
                language_id="es",
                exaggeration=self.exaggeration,
                temperature=temp_i,
                repetition_penalty=rep_i,
            )
            if isinstance(wav_tensor, torch.Tensor):
                wav_np = wav_tensor.detach().cpu().numpy().squeeze().astype(np.float32)
            else:
                wav_np = np.asarray(wav_tensor, dtype=np.float32).squeeze()

            wav_limpio = _recortar_bordes_silencio_seguro(wav_np, sr)
            completo, score = self._evaluar_fragmento_whisper(wav_limpio, sr, frag_tts, whisper_model)
            if score > mejor_score:
                mejor_score = score
                mejor_wav = wav_limpio
            if completo:
                return [wav_limpio]

        # Si el fragmento fue truncado por EOS tras reintentos, subdividir en 2 mitades cortas
        if whisper_model is not None and depth < 2 and len(frag.split()) >= 6:
            sub1, sub2 = _dividir_fragmento_mitad(frag)
            if sub1 and sub2 and sub1 != frag:
                out1 = self._sintetizar_fragmento_verificado(sub1, sr, temperature, whisper_model, depth + 1)
                out2 = self._sintetizar_fragmento_verificado(sub2, sr, temperature, whisper_model, depth + 1)
                return out1 + out2

        return [mejor_wav if mejor_wav is not None else np.zeros(int(sr * 0.2), dtype=np.float32)]

    def sintetizar_a_mp3(
        self,
        texto: str,
        destino_mp3: Path,
        temperature: float = TEMPERATURE,
        whisper_model: WhisperModel | None = None,
    ) -> None:
        self.asegurar_modelo()
        self.model.conds = self.base_conds

        sr = self.model.sr
        pausa_corta = np.zeros(int(sr * 0.13), dtype=np.float32)
        pausa_oracion = np.zeros(int(sr * 0.20), dtype=np.float32)
        fragmentos = dividir_en_fragmentos(texto)
        segmentos_audio = []

        for frag in fragmentos:
            sub_wavs = self._sintetizar_fragmento_verificado(frag, sr, temperature, whisper_model)
            for sub_idx, wav_np in enumerate(sub_wavs):
                segmentos_audio.append(wav_np)
                es_fin_frag = sub_idx == len(sub_wavs) - 1
                segmentos_audio.append(pausa_oracion if es_fin_frag else pausa_corta)

        if segmentos_audio:
            audio_completo = np.concatenate(segmentos_audio[:-1])
        else:
            audio_completo = np.zeros(int(sr * 0.5), dtype=np.float32)

        destino_mp3.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp_file:
            tmp_wav = Path(tmp_file.name)

        try:
            sf.write(str(tmp_wav), audio_completo, sr)
            filtro_audio = "highpass=f=80,loudnorm=I=-16:TP=-1.5:LRA=11"
            cmd = [
                "ffmpeg",
                "-y",
                "-loglevel",
                "error",
                "-i",
                str(tmp_wav),
                "-af",
                filtro_audio,
                "-ar",
                "24000",
                "-ac",
                "1",
                "-codec:a",
                "libmp3lame",
                "-qscale:a",
                "2",
                str(destino_mp3),
            ]
            res = subprocess.run(cmd, capture_output=True, text=True)
            if res.returncode != 0:
                sf.write(str(destino_mp3), audio_completo, sr)
        finally:
            tmp_wav.unlink(missing_ok=True)

    def liberar_vram(self) -> None:
        if self.model is not None:
            del self.model
            self.model = None
        if self.base_conds is not None:
            del self.base_conds
            self.base_conds = None
        if torch.cuda.is_available():
            torch.cuda.empty_cache()


def limpiar_y_compactar_audio(
    audio_path: Path,
    texto_guion: str,
    whisper_model: WhisperModel,
    silencio_final_s: float = 0.0,
) -> None:
    """Compacta exclusivamente silencios acústicos reales verificados por energía RMS (nunca corta fonemas ni palabras cortas) y añade silencio final opcional."""
    try:
        audio, sr = sf.read(str(audio_path))
    except Exception as e:
        print(f"[Limpieza Audio] ⚠️ Error al leer {audio_path}: {e}")
        return

    if audio.ndim > 1:
        audio = audio.mean(axis=1)

    if len(audio) < int(sr * 0.25):
        return

    win = max(1, int(sr * 0.020))  # Ventanas de 20 ms
    n_wins = len(audio) // win
    if n_wins < 8:
        return

    frames_rms = np.sqrt(np.mean(audio[: n_wins * win].reshape(n_wins, win) ** 2, axis=1))
    umbral_silencio = 0.0045  # ~ -47 dBFS: garantiza no tocar jamás consonantes suaves ni respiraciones
    es_silencio = frames_rms < umbral_silencio

    modificado = False

    # 1. Recorte suave de silencio puro inicial dejando 55ms de margen previo al ataque
    activos = np.where(~es_silencio)[0]
    if len(activos) == 0:
        return

    s_inicio = max(0, int(activos[0] * win) - int(sr * 0.055))
    if s_inicio > int(sr * 0.08):
        audio = audio[s_inicio:]
        n_wins = len(audio) // win
        frames_rms = np.sqrt(np.mean(audio[: n_wins * win].reshape(n_wins, win) ** 2, axis=1))
        es_silencio = frames_rms < umbral_silencio
        activos = np.where(~es_silencio)[0]
        fi = min(int(sr * 0.015), len(audio))
        audio[:fi] *= np.linspace(0.0, 1.0, fi)
        modificado = True

    # 2. Compactar únicamente pausas muertas reales (> 0.48s con RMS < umbral_silencio) dejando 0.16s a cada lado
    min_wins_pausa = int(0.48 / 0.020)
    margen_wins = int(0.16 / 0.020)
    cortes = []
    idx = 0
    while idx < len(es_silencio):
        if not es_silencio[idx]:
            idx += 1
            continue
        run_start = idx
        while idx < len(es_silencio) and es_silencio[idx]:
            idx += 1
        run_end = idx
        if (run_end - run_start) >= min_wins_pausa and run_start > 0 and run_end < len(es_silencio):
            c_from = (run_start + margen_wins) * win
            c_to = (run_end - margen_wins) * win
            if c_to > c_from + int(0.06 * sr) and c_to < len(audio):
                cortes.append((c_from, c_to))

    if cortes:
        pedazos = []
        last_idx = 0
        xfade_len = int(0.022 * sr)
        for s_from, s_to in cortes:
            if s_from > last_idx:
                chunk = audio[last_idx:s_from].copy()
                if len(chunk) > xfade_len:
                    chunk[-xfade_len:] *= np.linspace(1.0, 0.0, xfade_len)
                pedazos.append(chunk)
            last_idx = s_to
            if last_idx < len(audio):
                fade_in_len = min(xfade_len, len(audio) - last_idx)
                audio[last_idx : last_idx + fade_in_len] *= np.linspace(0.0, 1.0, fade_in_len)
        if last_idx < len(audio):
            pedazos.append(audio[last_idx:])
        if pedazos:
            audio = np.concatenate(pedazos)
            modificado = True

    # 3. Poda segura de cola puramente silenciosa al final (+0.36s tras el último frame con energía acústica)
    n_wins_post = len(audio) // win
    if n_wins_post >= 4:
        rms_post = np.sqrt(np.mean(audio[: n_wins_post * win].reshape(n_wins_post, win) ** 2, axis=1))
        act_post = np.where(rms_post >= umbral_silencio)[0]
        if len(act_post) > 0:
            limite_fin = int((act_post[-1] + 1) * win) + int(0.36 * sr)
            if 0 < limite_fin < len(audio) - int(0.15 * sr):
                audio = audio[:limite_fin]
                ft = min(int(0.065 * sr), len(audio))
                audio[-ft:] *= np.linspace(1.0, 0.0, ft)
                modificado = True

    # 4. Silencio contemplativo final opcional (ej. epílogo con fundido a negro de 4 segundos)
    if silencio_final_s > 0.01:
        cola_silencio = np.zeros(int(silencio_final_s * sr), dtype=audio.dtype)
        audio = np.concatenate([audio, cola_silencio])
        modificado = True

    if modificado:
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp_file:
            tmp_wav = Path(tmp_file.name)
        try:
            sf.write(str(tmp_wav), audio, sr)
            cmd = [
                "ffmpeg",
                "-y",
                "-loglevel",
                "error",
                "-i",
                str(tmp_wav),
                "-ar",
                "24000",
                "-ac",
                "1",
                "-codec:a",
                "libmp3lame",
                "-qscale:a",
                "2",
                str(audio_path),
            ]
            subprocess.run(cmd, capture_output=True, text=True)
        finally:
            tmp_wav.unlink(missing_ok=True)


NUM_MAP = {
    "100": ["cien", "ciento"],
    "20": ["veinte"],
    "30": ["treinta"],
    "300000": ["trescientos", "mil"],
    "300.000": ["trescientos", "mil"],
    "30000": ["treinta", "mil"],
    "30.000": ["treinta", "mil"],
    "150000": ["ciento", "cincuenta", "mil"],
    "150.000": ["ciento", "cincuenta", "mil"],
    "14": ["catorce"],
    "10000": ["diez", "mil"],
    "10.000": ["diez", "mil"],
    "100000": ["cien", "mil"],
    "100.000": ["cien", "mil"],
    "15": ["quince"],
    "70": ["setenta"],
    "7": ["siete"],
    "90": ["noventa"],
    "99": ["noventa", "y", "nueve"],
    "0.5": ["cero", "coma", "cinco"],
    "0,5": ["cero", "coma", "cinco"],
    "km": ["kilómetros", "kilómetro"],
    "km/h": ["kilómetros", "por", "hora"],
    "km/s": ["kilómetros", "por", "segundo"],
    "h": ["hora", "horas"],
    "c": ["luz", "velocidad", "constante"],
    "%": ["por", "ciento"],
}


def _clean_word_for_sim(w: str) -> str:
    return w.lower().strip(PUNCT_STRIP)


def _word_similarity(g: str, w: str) -> float:
    cg = _clean_word_for_sim(g)
    cw = _clean_word_for_sim(w)
    if not cg or not cw:
        return 0.0
    if cg == cw:
        return 1.0
    if cw in NUM_MAP and cg in NUM_MAP[cw]:
        return 0.95
    if cg in NUM_MAP and cw in NUM_MAP[cg]:
        return 0.95
    return SequenceMatcher(None, cg, cw).ratio()


def align_tokens_dp(tokens_guion: list[str], whisper_words: list[dict], duracion_total_ms: int) -> list[dict]:
    M = len(tokens_guion)
    N = len(whisper_words)
    if M == 0:
        return []
    if N == 0:
        step = max(80, duracion_total_ms / M)
        return [
            {"palabra": tok, "inicioMs": round(i * step), "finMs": round((i + 1) * step)}
            for i, tok in enumerate(tokens_guion)
        ]

    max_dev = max(18, abs(M - N) + 10)
    dp = {}
    dp[(0, 0)] = (0.0, None)

    for i in range(M + 1):
        for j in range(max(0, i - max_dev), min(N + 1, i + max_dev + 1)):
            if i == 0 and j == 0:
                continue

            best_score = -1e9
            best_bp = None

            # Opción 1: Emparejar tokens_guion[i-1] con whisper_words[j-1]
            if i > 0 and j > 0 and (i - 1, j - 1) in dp:
                sim = _word_similarity(tokens_guion[i - 1], whisper_words[j - 1]["palabra"])
                match_score = (3.0 * sim - 0.5) if sim >= 0.6 else (-1.5)
                score = dp[(i - 1, j - 1)][0] + match_score
                if score > best_score:
                    best_score = score
                    best_bp = (i - 1, j - 1, "match")

            # Opción 2: Gap en Whisper (token en guion sin palabra explícita en transcripción)
            if i > 0 and (i - 1, j) in dp:
                score = dp[(i - 1, j)][0] - 0.6
                if score > best_score:
                    best_score = score
                    best_bp = (i - 1, j, "gap_w")

            # Opción 3: Gap en Guion (palabra de Whisper espuria o extra)
            if j > 0 and (i, j - 1) in dp:
                score = dp[(i, j - 1)][0] - 0.6
                if score > best_score:
                    best_score = score
                    best_bp = (i, j - 1, "gap_g")

            if best_bp is not None:
                dp[(i, j)] = (best_score, best_bp)

    # Backtrack para reconstruir la alineación óptima
    curr_i, curr_j = M, N
    if (curr_i, curr_j) not in dp:
        candidates = [(k, v[0]) for k, v in dp.items() if k[0] == M]
        if candidates:
            curr_i, curr_j = max(candidates, key=lambda x: x[1])[0]
        else:
            curr_i, curr_j = max(dp.keys(), key=lambda k: dp[k][0])

    matches_g = {}
    while (curr_i, curr_j) != (0, 0):
        if (curr_i, curr_j) not in dp:
            break
        _, bp = dp[(curr_i, curr_j)]
        if bp is None:
            break
        prev_i, prev_j, op = bp
        if op == "match":
            matches_g[prev_i] = prev_j
        curr_i = prev_i
        curr_j = prev_j

    result = []
    for i in range(M):
        if i in matches_g:
            j = matches_g[i]
            result.append({
                "palabra": tokens_guion[i],
                "inicioMs": whisper_words[j]["inicioMs"],
                "finMs": whisper_words[j]["finMs"],
            })
        else:
            result.append({
                "palabra": tokens_guion[i],
                "inicioMs": None,
                "finMs": None,
            })

    # Interpolar gaps suavemente preservando la duración natural
    last_known_end = 0
    idx = 0
    while idx < M:
        if result[idx]["inicioMs"] is not None:
            last_known_end = result[idx]["finMs"]
            idx += 1
            continue

        gap_start = idx
        while idx < M and result[idx]["inicioMs"] is None:
            idx += 1
        gap_end = idx

        next_known_start = result[gap_end]["inicioMs"] if gap_end < M else duracion_total_ms
        if next_known_start <= last_known_end:
            next_known_start = last_known_end + 250 * (gap_end - gap_start)

        gap_duration = next_known_start - last_known_end
        span = gap_duration / (gap_end - gap_start + 1)

        for k in range(gap_start, gap_end):
            rel = k - gap_start + 1
            w_start = round(last_known_end + (rel - 1) * span)
            w_end = round(last_known_end + rel * span)
            result[k]["inicioMs"] = w_start
            result[k]["finMs"] = max(w_start + 40, w_end)

        last_known_end = result[gap_end - 1]["finMs"]

    # Monotonicidad estricta y duración mínima
    prev = 0
    for r in result:
        if r["inicioMs"] < prev:
            r["inicioMs"] = prev
        if r["finMs"] <= r["inicioMs"]:
            r["finMs"] = r["inicioMs"] + 40
        prev = r["inicioMs"]

    return result


class LocalWhisperAligner:
    """Alineador local de palabras (inicioMs, finMs) con faster-whisper y Programación Dinámica."""

    def __init__(self, model_size: str = WHISPER_MODEL_SIZE) -> None:
        self.model_size = model_size
        self.model: WhisperModel | None = None

    def asegurar_modelo(self) -> WhisperModel:
        if self.model is None:
            device = "cuda" if torch.cuda.is_available() else "cpu"
            compute_type = "float16" if device == "cuda" else "int8"
            print(f"[Faster-Whisper] 🎧 Cargando modelo local '{self.model_size}' en {device.upper()} ({compute_type})...")
            self.model = WhisperModel(self.model_size, device=device, compute_type=compute_type)
        return self.model

    def extraer_palabras(
        self,
        audio_path: Path,
        texto_guion: str,
        duracion_audio_s: float,
        silencio_final_s: float = 0.0,
    ) -> list[dict]:
        model = self.asegurar_modelo()
        # Prompt neutro de dominio (NO repetir el inicio literal del guion en initial_prompt,
        # pues Whisper lo interpreta como <|startofprev|> y puede omitir la primera frase en audios >30s).
        prompt_dominio = (
            "Documental científico narrado en español claro sobre evolución biológica, "
            "cerebro, metabolismo, homínidos, paleontología y naturaleza."
        )
        segments, _ = model.transcribe(
            str(audio_path.resolve()),
            language="es",
            initial_prompt=prompt_dominio,
            word_timestamps=True,
            vad_filter=False,
            condition_on_previous_text=False,
        )

        detectadas = []
        for seg in segments:
            if not seg.words:
                continue
            for w in seg.words:
                if (w.end - w.start) < 0.015:
                    continue
                limpia = w.word.strip().strip(PUNCT_STRIP)
                if not limpia:
                    continue
                inicio_ms = max(0, round(w.start * 1000))
                fin_ms = max(inicio_ms + 20, round(w.end * 1000))

                # Si Whisper transcribe cifras/años en dígitos ("1965", "20%"), expandir a palabras
                # repartiendo proporcionalmente su ventana temporal para alineación 1:1 con el guion.
                if any(ch.isdigit() for ch in limpia):
                    expandida = normalizar_cifras_espanol(limpia)
                    sub_tokens = [
                        st.strip(PUNCT_STRIP)
                        for st in expandida.split()
                        if st.strip(PUNCT_STRIP)
                    ]
                    if len(sub_tokens) > 1:
                        total_chars = max(1, sum(len(st) for st in sub_tokens))
                        span_ms = max(20 * len(sub_tokens), fin_ms - inicio_ms)
                        cursor_ms = inicio_ms
                        for idx_st, st in enumerate(sub_tokens):
                            if idx_st == len(sub_tokens) - 1:
                                st_fin = max(cursor_ms + 20, fin_ms)
                            else:
                                st_dur = max(20, round(span_ms * (len(st) / total_chars)))
                                st_fin = cursor_ms + st_dur
                            detectadas.append({
                                "palabra": st,
                                "inicioMs": cursor_ms,
                                "finMs": st_fin,
                            })
                            cursor_ms = st_fin
                        continue
                    elif len(sub_tokens) == 1:
                        limpia = sub_tokens[0]

                detectadas.append({
                    "palabra": limpia,
                    "inicioMs": inicio_ms,
                    "finMs": fin_ms,
                })

        tokens_guion = [
            t.strip(PUNCT_STRIP)
            for t in re.findall(r"\S+", texto_guion)
            if t.strip(PUNCT_STRIP)
        ]

        dur_habla_s = max(0.3, duracion_audio_s - max(0.0, silencio_final_s))
        dur_ms = round(dur_habla_s * 1000)
        return align_tokens_dp(tokens_guion, detectadas, dur_ms)


def validar_palabras(palabras: list[dict], texto_guion: str, escena_id) -> list[dict]:
    previo = 0
    for p in palabras:
        if p["inicioMs"] < previo:
            p["inicioMs"] = previo
        if p["finMs"] <= p["inicioMs"]:
            p["finMs"] = p["inicioMs"] + 20
        previo = p["inicioMs"]
    return palabras


def procesar_escena(
    escena: dict,
    tts_engine: LocalClonedTTS,
    whisper_aligner: LocalWhisperAligner,
    cache: dict,
    force: bool = False,
) -> None:
    escena_id = escena["id"]
    texto_original = escena["texto"]

    # Normalización fonética automática de cifras, años, decimales y unidades en español
    texto = normalizar_cifras_espanol(texto_original)
    if texto != texto_original:
        print(
            f"  [TTS Dicción] 🗣️ Escena {escena_id}: Cifras expandidas fonéticamente para dicción óptima:\n"
            f"                 Original: \"{texto_original}\"\n"
            f"                 Fonético: \"{texto}\""
        )
        escena["texto"] = texto

    audio_path = AUDIOS_DIR / f"escena_{escena_id}.mp3"
    cache_key = f"escena_{escena_id}"

    # Cambio dinámico de voz si la escena especifica voz de narrador o personaje
    voz_solicitada = escena.get("voz")
    conds_escena = (
        resolver_archivo_condiciones(voz_solicitada)
        if voz_solicitada
        else tts_engine.conds_path
    )
    tts_engine.cambiar_voz(conds_escena)

    silencio_extra = float(escena.get("silencioFinalSegundos") or 0.0)
    hash_actual = calcular_hash_escena(texto, conds_escena, silencio_extra)
    entrada_cache = cache.get(cache_key, {})

    en_cache = (
        not force
        and audio_path.exists()
        and audio_path.stat().st_size > 500
        and entrada_cache.get("sha256") == hash_actual
        and bool(entrada_cache.get("palabras") or escena.get("palabras"))
    )

    if en_cache:
        mp3_info = MP3(audio_path)
        duracion_segundos = round(mp3_info.info.length + PAUSE_SECONDS, 3)
        palabras = entrada_cache.get("palabras") or escena.get("palabras", [])
        escena["duracionSegundos"] = duracion_segundos
        escena["palabras"] = palabras
        print(
            f"  [TTS] ⚡ Escena {escena_id} (en caché SHA-256): {duracion_segundos:.2f}s ({len(palabras)} palabras)"
        )
        return

    tokens_guion = [
        t.strip(PUNCT_STRIP)
        for t in re.findall(r"\S+", texto)
        if t.strip(PUNCT_STRIP)
    ]

    max_intentos = 3
    duracion_real_mp3 = 3.0
    palabras = []

    w_model = whisper_aligner.asegurar_modelo()
    for intento in range(max_intentos):
        temp_intento = round(TEMPERATURE + (intento * 0.04), 2)
        tts_engine.sintetizar_a_mp3(
            texto,
            audio_path,
            temperature=temp_intento,
            whisper_model=w_model,
        )

        limpiar_y_compactar_audio(
            audio_path,
            texto,
            w_model,
            silencio_final_s=silencio_extra,
        )

        mp3_info = MP3(audio_path)
        duracion_real_mp3 = mp3_info.info.length
        palabras = whisper_aligner.extraer_palabras(
            audio_path,
            texto,
            duracion_real_mp3,
            silencio_final_s=silencio_extra,
        )

        if tokens_guion and intento < max_intentos - 1:
            segs_chk, _ = w_model.transcribe(
                str(audio_path),
                language="es",
                vad_filter=False,
                condition_on_previous_text=False,
            )
            heard_tokens = _extraer_tokens_comparables(" ".join(s.text.strip() for s in segs_chk))
            exp_tokens = _extraer_tokens_comparables(fonetizar_para_tts(texto))
            overall_sim = SequenceMatcher(None, exp_tokens, heard_tokens).ratio()
            len_ratio = len(heard_tokens) / max(1, len(exp_tokens))

            if len_ratio < 0.88 or overall_sim < 0.82:
                print(
                    f"  [TTS] ⚠️ Escena {escena_id}: Cobertura baja (sim={overall_sim:.2f}, len={len_ratio:.2f}). "
                    f"Reintentando síntesis ({intento + 2}/{max_intentos})..."
                )
                continue

        break

    palabras = validar_palabras(palabras, texto, escena_id)
    duracion_segundos = round(duracion_real_mp3 + PAUSE_SECONDS, 3)

    escena["duracionSegundos"] = duracion_segundos
    escena["palabras"] = palabras

    cache[cache_key] = {
        "sha256": hash_actual,
        "pipelineVersion": PIPELINE_VERSION,
        "texto": texto,
        "voiceConds": tts_engine.conds_path.name,
        "duracionSegundos": duracion_segundos,
        "palabras": palabras,
    }

    print(
        f"  [TTS] ✨ Escena {escena_id} clonada con éxito: {duracion_segundos:.2f}s ({len(palabras)} palabras)"
    )


def procesar_guion(guion_path: Path, nombre_conds: str, force: bool = False) -> None:
    if not guion_path.exists():
        print(f"[TTS] ❌ No se encontró el guion en {guion_path}")
        sys.exit(1)

    with open(guion_path, "r", encoding="utf-8") as f:
        guion = json.load(f)

    meta = guion.get("meta", {})
    capitulos = guion.get("capitulos", [])

    if not capitulos:
        print("[TTS] ❌ El guion no contiene capítulos para procesar.")
        sys.exit(1)

    AUDIOS_DIR.mkdir(parents=True, exist_ok=True)
    conds_path = resolver_archivo_condiciones(nombre_conds)

    cache = cargar_cache()
    tts_engine = LocalClonedTTS(conds_path=conds_path)
    whisper_aligner = LocalWhisperAligner()

    print(f"\n[TTS Clonado] 🎙️  Procesando guion con voz clonada '{conds_path.name}'...")

    total_escenas = sum(len(c.get("escenas", [])) for c in capitulos)

    try:
        for cap in capitulos:
            num = cap.get("numero", 1)
            titulo = cap.get("titulo", "Sin título")
            print(f"\n[TTS] 📁 Capítulo {num}: \"{titulo}\"")
            duracion_cap = 0.0

            for esc in cap.get("escenas", []):
                procesar_escena(
                    escena=esc,
                    tts_engine=tts_engine,
                    whisper_aligner=whisper_aligner,
                    cache=cache,
                    force=force,
                )
                duracion_cap += esc.get("duracionSegundos", 0.0)

            cap["duracionSegundos"] = round(duracion_cap, 2)
    finally:
        tts_engine.liberar_vram()

    guardar_cache(cache)

    with open(guion_path, "w", encoding="utf-8") as f:
        json.dump(guion, f, ensure_ascii=False, indent=2)

    duracion_total = sum(c.get("duracionSegundos", 0.0) for c in capitulos)
    minutos = int(duracion_total // 60)
    segundos = duracion_total % 60

    print(f"\n[TTS] ✅ Síntesis clonada completada con éxito.")
    print(f"      Total escenas: {total_escenas}")
    print(f"      Duración total del video: {duracion_total:.2f}s (~{minutos}m {segundos:.0f}s)")

    dur_obj = meta.get("duracionObjetivo")
    if dur_obj and len(dur_obj) == 2:
        min_obj, max_obj = dur_obj
        if duracion_total < min_obj:
            print(f"      ⚠️  Alerta: Duración menor al objetivo [{min_obj}-{max_obj}s].")
        elif duracion_total > max_obj:
            print(f"      ⚠️  Alerta: Duración mayor al objetivo [{min_obj}-{max_obj}s].")
        else:
            print(f"      🎯 Duración dentro del rango objetivo [{min_obj}-{max_obj}s].")


def main():
    parser = argparse.ArgumentParser(description="Motor TTS con voz clonada para videos largos")
    parser.add_argument("--script", default=str(GUION_PATH), help="Ruta al guion JSON")
    parser.add_argument("--conds", default=DEFAULT_VOICE_CONDS, help="Archivo de condiciones vocales (.conds.pt)")
    parser.add_argument("--force", action="store_true", help="Forzar regeneración ignorando caché")
    args = parser.parse_args()

    procesar_guion(Path(args.script), args.conds, args.force)


if __name__ == "__main__":
    main()
