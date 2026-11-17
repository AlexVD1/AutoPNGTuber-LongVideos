import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR / "scripts"))

from tts_engine import (
    _ensure_venv_python,
    resolver_archivo_condiciones,
    LocalClonedTTS,
    LocalWhisperAligner,
    limpiar_y_compactar_audio,
)
from normalizador_numeros import normalizar_cifras_espanol

_ensure_venv_python()


def test_normalizador_cifras():
    print("[TEST-TTS] Probando normalizador fonético de cifras grandes...")
    ejemplos = [
        ("1420 megahercios", "mil cuatrocientos veinte megahercios"),
        ("agosto de 1977", "agosto de mil novecientos setenta y siete"),
        ("30 veces", "treinta veces"),
        ("72 segundos", "setenta y dos segundos"),
        ("300.000 km/s", "trescientos mil kilómetros por segundo"),
    ]
    for entrada, esperada in ejemplos:
        res = normalizar_cifras_espanol(entrada)
        assert res == esperada, f"Fallo al normalizar '{entrada}': esperado '{esperada}', obtenido '{res}'"
    print("[TEST-TTS] ✅ Normalizador de cifras OK: todas las expresiones expandidas.")


def test_cloned_tts():
    print("[TEST-TTS] Probando motor de voz clonada Chatterbox + Faster-Whisper...")
    conds_path = resolver_archivo_condiciones("alex.conds.pt")
    assert conds_path.exists(), f"El archivo {conds_path} debe existir"

    texto_prueba = "Prueba de síntesis con voz clonada y alineación por palabra en dieciséis a nueve."

    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
        temp_audio = Path(f.name)

    tts_engine = LocalClonedTTS(conds_path=conds_path)
    whisper_aligner = LocalWhisperAligner()

    try:
        tts_engine.sintetizar_a_mp3(texto_prueba, temp_audio)
        assert temp_audio.exists(), "El archivo de audio debe haberse generado"
        assert temp_audio.stat().st_size > 5000, "El MP3 debe tener un tamaño válido"

        limpiar_y_compactar_audio(temp_audio, texto_prueba, whisper_aligner.asegurar_modelo())

        from mutagen.mp3 import MP3
        duracion = MP3(str(temp_audio)).info.length
        assert duracion > 2.0, f"La duración ({duracion}s) debe ser mayor a 2s"

        palabras = whisper_aligner.extraer_palabras(temp_audio, texto_prueba, duracion)
        assert len(palabras) >= 6, f"Se deben detectar al menos 6 palabras (detectadas: {len(palabras)})"

        prev_inicio = 0
        for p in palabras:
            assert "palabra" in p
            assert "inicioMs" in p
            assert "finMs" in p
            assert p["inicioMs"] <= p["finMs"]
            assert p["inicioMs"] >= prev_inicio
            prev_inicio = p["inicioMs"]

        print(f"[TEST-TTS] ✅ Voz clonada OK: {duracion:.2f}s, {len(palabras)} palabras alineadas con Whisper.")
    finally:
        tts_engine.liberar_vram()
        temp_audio.unlink(missing_ok=True)


if __name__ == "__main__":
    test_normalizador_cifras()
    test_cloned_tts()
