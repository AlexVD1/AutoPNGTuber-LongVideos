"""
Generador procedural de SFX en formato WAV (16-bit PCM, 44.1kHz).
No requiere dependencias externas (usa la biblioteca estándar de Python: wave, math, struct, random).

Uso:
  python scripts/generar_sfx.py <nombre_archivo> <tipo> [duracion_seg]
  python scripts/generar_sfx.py laser.wav laser 0.35
  python scripts/generar_sfx.py alarma.wav alarm 0.6
  python scripts/generar_sfx.py glitch.wav glitch 0.4
"""

import sys
import os
import wave
import struct
import math
import random

SAMPLE_RATE = 44100

def synth_laser(duration=0.35):
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        # Frecuencia cae exponencialmente de 1600 Hz a 120 Hz
        freq = 1600 * math.exp(-6 * progress) + 120
        phase = 2 * math.pi * freq * t
        env = math.pow(1 - progress, 1.5)
        val = math.sin(phase) * env
        samples.append(val)
    return samples

def synth_heartbeat(duration=0.7):
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        val = 0.0
        # Golpe 1 (t=0.0 a 0.2s)
        if 0.0 <= t < 0.2:
            p1 = t / 0.2
            freq1 = 55 + 20 * (1 - p1)
            env1 = math.sin(math.pi * p1) * (1 - p1 * 0.3)
            val += math.sin(2 * math.pi * freq1 * t) * env1 * 0.8
        # Golpe 2 (t=0.22 a 0.42s)
        elif 0.22 <= t < 0.42:
            p2 = (t - 0.22) / 0.20
            freq2 = 65 + 15 * (1 - p2)
            env2 = math.sin(math.pi * p2) * (1 - p2 * 0.2)
            val += math.sin(2 * math.pi * freq2 * (t - 0.22)) * env2 * 1.0
        samples.append(val)
    return samples

def synth_glitch(duration=0.35):
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        # Ruido modulado con onda cuadrada
        noise = random.uniform(-1, 1)
        freq = 120 + 300 * ((int(t * 40)) % 5)
        sq = 1.0 if math.sin(2 * math.pi * freq * t) > 0 else -1.0
        env = (1 - progress * 0.8) if (int(t * 60) % 2 == 0) else 0.1
        val = (noise * 0.6 + sq * 0.4) * env
        samples.append(val)
    return samples

def synth_alarm(duration=0.6):
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        # Beep alternante de dos tonos (880Hz y 660Hz)
        tone = 880 if (int(t * 8) % 2 == 0) else 660
        env = 1.0 - progress * 0.2
        val = math.sin(2 * math.pi * tone * t) * env * 0.7
        samples.append(val)
    return samples

def synth_sub_impact(duration=0.5):
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        freq = 140 * math.exp(-8 * progress) + 40
        sub = math.sin(2 * math.pi * freq * t)
        noise = random.uniform(-1, 1) * math.exp(-25 * progress) * 0.4
        env = math.pow(1 - progress, 2)
        val = (sub + noise) * env
        samples.append(val)
    return samples

def synth_sparkle(duration=0.45):
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    harmonics = [523.25, 659.25, 783.99, 1046.50, 1318.51] # Arpegio C Mayor
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        val = 0.0
        for idx, freq in enumerate(harmonics):
            start_t = idx * (duration / len(harmonics)) * 0.6
            if t >= start_t:
                dt = t - start_t
                env = math.exp(-12 * dt)
                val += math.sin(2 * math.pi * freq * dt) * env * 0.25
        samples.append(val)
    return samples

def synth_click(duration=0.08):
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        freq = 2400 * (1 - progress) + 300
        val = math.sin(2 * math.pi * freq * t) * math.exp(-40 * progress)
        samples.append(val)
    return samples

def synth_metal_clang(duration=0.6):
    """Impacto metálico duro con resonancia cristalina/acero (bala o yunque)"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        # Ruido inicial instantáneo tipo percusión
        noise = random.uniform(-1, 1) * math.exp(-60 * progress) * 0.7
        # Resonancias metálicas inarmónicas de alta frecuencia
        f1, f2, f3 = 1850.0, 2940.0, 4210.0
        ring = (
            math.sin(2 * math.pi * f1 * t) * math.exp(-9 * progress) * 0.45 +
            math.sin(2 * math.pi * f2 * t) * math.exp(-14 * progress) * 0.35 +
            math.sin(2 * math.pi * f3 * t) * math.exp(-22 * progress) * 0.20
        )
        val = noise + ring
        samples.append(val)
    return samples

def synth_boing(duration=0.55):
    """Rebote elástico estilo caricatura (barrido ascendente de frecuencia con vibrato)"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        # Frecuencia sube de 110Hz a 380Hz con oscilación de resorte
        vibrato = math.sin(2 * math.pi * 14 * t) * (1 - progress * 0.5) * 35
        freq = (110 + 260 * math.sqrt(progress)) + vibrato
        env = math.exp(-4.5 * progress)
        val = math.sin(2 * math.pi * freq * t) * env
        samples.append(val)
    return samples

def synth_thermal_hiss(duration=0.75):
    """Siseo de choque térmico intenso (vapor de vidrio al rojo sumergido en agua)"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    # Filtro paso-banda simple simulado acumulando ruido
    last_noise = 0.0
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        raw_noise = random.uniform(-1, 1)
        # Filtro de paso alto simple
        hiss = raw_noise - last_noise * 0.65
        last_noise = raw_noise
        # Burbujeo sutil de baja frecuencia modulando amplitud
        bubble = 0.7 + 0.3 * math.sin(2 * math.pi * 42 * t)
        # Envolvente con pico rápido a 0.05s y decaimiento suave
        if progress < 0.1:
            env = progress / 0.1
        else:
            env = math.exp(-3.5 * (progress - 0.1))
        val = hiss * bubble * env
        samples.append(val)
    return samples

def synth_tension_creak(duration=0.65):
    """Crujido de tensión mecánica extrema (cables o compresión molecular al límite)"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        # Armónicos chirriantes bajos con modulación lenta
        f_base = 75 + 15 * math.sin(2 * math.pi * 5 * t)
        creak_saw = (2 * ((t * f_base) % 1.0) - 1.0) * 0.4
        grit = random.uniform(-0.3, 0.3) if (int(t * 80) % 2 == 0) else 0.0
        env = math.sin(math.pi * math.pow(progress, 0.7))
        val = (creak_saw + grit) * env
        samples.append(val)
    return samples

def synth_glass_snap(duration=0.25):
    """Chasquido milimétrico seco de punta de cristal partiéndose"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        # Click ultra-rápido de fractura
        click = random.uniform(-1, 1) * math.exp(-80 * progress) * 0.8
        # Micro-resonancia aguda de cristal
        chime = math.sin(2 * math.pi * 3800 * t) * math.exp(-25 * progress) * 0.4
        val = click + chime
        samples.append(val)
    return samples

def synth_glass_shatter_boom(duration=0.85):
    """Onda de choque explosiva con pulverización masiva de cristal (Prince Rupert shockwave)"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        # Golpe sub-grave inicial (onda de choque expansiva)
        sub_freq = 120 * math.exp(-12 * progress) + 38
        sub = math.sin(2 * math.pi * sub_freq * t) * math.exp(-6 * progress) * 0.65
        # Ruido de fragmentación y polvo de cristal fino disperso
        noise = random.uniform(-1, 1) * math.exp(-4 * progress) * 0.55
        # Múltiples armónicos tintineantes de esquirlas
        tinkles = (
            math.sin(2 * math.pi * 2600 * t) * 0.25 +
            math.sin(2 * math.pi * 4400 * t) * 0.15 +
            math.sin(2 * math.pi * 6100 * t) * 0.10
        ) * math.exp(-8 * progress)
        val = sub + noise + tinkles
        samples.append(val)
    return samples

def synth_sonar_pulse(duration=0.65):
    """Burbuja subacuática ('bloop') seguida de un pulso sónico resonante con destello"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        # Parte 1: bloop de burbuja rápida (0 a 0.15s)
        bloop = 0.0
        if t < 0.18:
            bp = t / 0.18
            bfreq = 320 + 480 * math.pow(bp, 2)
            bloop = math.sin(2 * math.pi * bfreq * t) * math.sin(math.pi * bp) * 0.85
        # Parte 2: pulso sónico futurista de baja frecuencia con resonancia (t > 0.12s)
        pulse = 0.0
        if t >= 0.10:
            pt = t - 0.10
            pp = pt / (duration - 0.10)
            pfreq = 180 * math.exp(-3 * pp) + 60
            pulse = math.sin(2 * math.pi * pfreq * pt) * math.exp(-5 * pp) * 0.9
            # Brillo eléctrico
            shimmer = math.sin(2 * math.pi * 3200 * pt) * math.exp(-14 * pp) * 0.3
            pulse += shimmer
        val = bloop + pulse
        samples.append(val)
    return samples

def synth_water_splash(duration=0.55):
    """Chapoteo torpe de agua con burbujas y pop inofensivo"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    last_noise = 0.0
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        raw = random.uniform(-1, 1)
        # Filtro de agua
        fnoise = raw * 0.6 + last_noise * 0.4
        last_noise = fnoise
        bubble = math.sin(2 * math.pi * (240 + 380 * math.sin(t * 30)) * t) * 0.35
        env = math.exp(-5.5 * progress)
        pop = math.sin(2 * math.pi * 520 * t) * math.exp(-35 * progress) * 0.5
        val = (fnoise * 0.65 + bubble + pop) * env
        samples.append(val)
    return samples

def synth_ultrasound_sweep(duration=0.7):
    """Barrido senoidal de ultrasonido limpio (sube hasta frecuencias inaudibles)"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        # Frecuencia sube exponencialmente de 800 Hz a 16,000 Hz
        freq = 800 * math.pow(20, progress)
        phase = 2 * math.pi * freq * t
        env = math.sin(math.pi * math.pow(progress, 0.6))
        val = math.sin(phase) * env * 0.75
        samples.append(val)
    return samples

def synth_cavitation_thud(duration=0.6):
    """Compresión hidrodinámica violenta con golpe sordo subacuático (THUD)"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        # Vacío previo
        inrush = math.pow(progress, 3) * math.sin(2 * math.pi * 180 * t) * 0.4 if progress < 0.25 else 0.0
        # Colapso sordo contundente a t=0.22s
        thud = 0.0
        if t >= 0.20:
            dt = t - 0.20
            dp = dt / (duration - 0.20)
            thud_freq = 90 * math.exp(-8 * dp) + 35
            thud = math.sin(2 * math.pi * thud_freq * dt) * math.exp(-5.5 * dp) * 1.0
            impact_noise = random.uniform(-1, 1) * math.exp(-22 * dp) * 0.4
            thud += impact_noise
        val = inrush + thud
        samples.append(val)
    return samples

def synth_plasma_burst(duration=0.45):
    """Fogonazo de plasma luminoso con chasquido láser ultra-rápido (PZT)"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        # Descarga de plasma instantánea
        zap = (2 * ((t * 4200) % 1.0) - 1.0) * math.exp(-32 * progress) * 0.7
        # Resonancia de cavidad de cuarzo
        ring = math.sin(2 * math.pi * 5400 * t) * math.exp(-12 * progress) * 0.45
        sub = math.sin(2 * math.pi * 150 * t) * math.exp(-15 * progress) * 0.5
        val = zap + ring + sub
        samples.append(val)
    return samples

def synth_ambient_chime(duration=0.8):
    """Acorde celestial de cuarzo relajante (resolución cósmica en agua)"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    notes = [587.33, 880.0, 1174.66, 1760.0] # D5, A5, D6, A6 armónicos puros
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        val = 0.0
        for n_idx, freq in enumerate(notes):
            delay = n_idx * 0.05
            if t >= delay:
                dt = t - delay
                env = math.exp(-3.5 * dt)
                val += math.sin(2 * math.pi * freq * dt) * env * (0.28 / len(notes))
        samples.append(val)
    return samples

def synth_borehole_laser(duration=0.55):
    """Eco láser antártico por dispersión acústica en pozo de hielo (PEEEW-tsch)"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        # Barrido exponencial descendente agudo a grave (dispersión)
        freq = 4200 * math.exp(-7.5 * progress) + 160
        phase = 2 * math.pi * freq * t
        # Resonancia metálica/cristalina de pared de hielo cilíndrica
        flutter = 1.0 + 0.25 * math.sin(2 * math.pi * 95 * t)
        # Cola de siseo gélido al final
        frost_tail = random.uniform(-0.15, 0.15) * math.exp(-3 * progress) if progress > 0.3 else 0.0
        env = math.pow(1 - progress, 1.2)
        val = (math.sin(phase) * flutter + frost_tail) * env
        samples.append(val)
    return samples

def synth_tape_measure(duration=0.7):
    """Carrete de cinta métrica desenrollándose a gran velocidad con campana final"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        val = 0.0
        if progress < 0.65:
            # Ruido de engranaje / cinta zumbando (whirrr)
            ratchet_freq = 60 + 140 * (progress / 0.65)
            click = 1.0 if (int(t * ratchet_freq * 4) % 2 == 0) else -0.3
            buzz = math.sin(2 * math.pi * (450 + 100 * math.sin(t * 30)) * t) * 0.3
            val = (click * 0.4 + buzz) * (0.8 + 0.2 * math.sin(t * 50))
        else:
            # Ding de campana a 90m
            dt = t - (0.65 * duration)
            ding = math.sin(2 * math.pi * 2093.0 * dt) * math.exp(-7.0 * dt) * 0.85
            ding_harm = math.sin(2 * math.pi * 4186.0 * dt) * math.exp(-12.0 * dt) * 0.3
            val = ding + ding_harm
        samples.append(val)
    return samples

def synth_rhythmic_pews(duration=0.95):
    """Secuencia rítmica de tres disparos láser antárticos con alturas escalonadas"""
    samples = [0.0] * int(SAMPLE_RATE * duration)
    shots = [
        (0.00, 0.26, 3600, 180, 0.7),
        (0.30, 0.22, 4500, 220, 0.85),
        (0.56, 0.35, 2900, 120, 1.0)
    ]
    for start_t, shot_dur, start_f, end_f, amp in shots:
        n_shot = int(SAMPLE_RATE * shot_dur)
        start_idx = int(start_t * SAMPLE_RATE)
        for i in range(n_shot):
            idx = start_idx + i
            if idx >= len(samples):
                break
            t_shot = i / SAMPLE_RATE
            p = t_shot / shot_dur
            f = (start_f - end_f) * math.exp(-8 * p) + end_f
            env = math.pow(1 - p, 1.4) * amp
            crackle = random.uniform(-0.2, 0.2) * math.exp(-4 * p) if start_f < 3000 else 0.0
            samples[idx] += (math.sin(2 * math.pi * f * t_shot) + crackle) * env
    return samples

def synth_ice_thump_vibration(duration=0.7):
    """Golpe sordo contra hielo en el fondo con resonancia armónica de tubo"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        thump_f = 110 * math.exp(-14 * progress) + 45
        thump = math.sin(2 * math.pi * thump_f * t) * math.exp(-9 * progress) * 0.9
        impact_grit = random.uniform(-0.5, 0.5) * math.exp(-35 * progress) * 0.6
        res = (
            math.sin(2 * math.pi * 320 * t) * 0.35 +
            math.sin(2 * math.pi * 640 * t) * 0.22 +
            math.sin(2 * math.pi * 960 * t) * 0.12
        ) * math.exp(-4.5 * progress)
        val = thump + impact_grit + res
        samples.append(val)
    return samples

def synth_dispersion_glissando(duration=0.85):
    """Glissando descendente de dispersión acústica pura (frecuencias agudas a graves)"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        freq = 3800 * math.exp(-4.5 * progress) + 150
        env = math.sin(math.pi * math.pow(progress, 0.45)) * math.pow(1 - progress, 0.7)
        val = math.sin(2 * math.pi * freq * t) * env * 0.9
        samples.append(val)
    return samples

def synth_scifi_double_pew(duration=0.65):
    """Disparo láser doble estilo ciencia ficción clásica ochentera (PEW! PEW!)"""
    samples = [0.0] * int(SAMPLE_RATE * duration)
    bursts = [(0.0, 0.26), (0.28, 0.28)]
    for start_t, b_dur in bursts:
        start_idx = int(start_t * SAMPLE_RATE)
        n_burst = int(b_dur * SAMPLE_RATE)
        for i in range(n_burst):
            idx = start_idx + i
            if idx >= len(samples):
                break
            t_b = i / SAMPLE_RATE
            p = t_b / b_dur
            f = 2400 * math.exp(-9 * p) + 220
            env = math.pow(1 - p, 1.5) * 0.85
            samples[idx] += math.sin(2 * math.pi * f * t_b) * env
    return samples

def synth_colossal_laser_echo(duration=1.2):
    """Disparo láser colosal con eco reverberante largo y siseo de viento polar"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        f_main = 4600 * math.exp(-5.5 * progress) + 120
        main_pew = math.sin(2 * math.pi * f_main * t) * math.pow(1 - progress, 1.1) * 0.8
        echoes = 0.0
        for d_ms, att in [(0.08, 0.45), (0.17, 0.28), (0.28, 0.16)]:
            if t >= d_ms:
                dt = t - d_ms
                dp = dt / (duration - d_ms)
                f_echo = 3800 * math.exp(-6.0 * dp) + 130
                echoes += math.sin(2 * math.pi * f_echo * dt) * math.pow(1 - dp, 1.4) * att
        wind = random.uniform(-0.12, 0.12) * math.sin(math.pi * progress)
        val = main_pew + echoes + wind
        samples.append(val)
    return samples

def synth_empuje_fotones(duration=0.6):
    """Zumbido solar ascendente con golpe cinético suave de caricatura (shhh-wham/puff)"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        whirr = 0.0
        if progress < 0.4:
            wp = progress / 0.4
            wfreq = 120 + 350 * math.pow(wp, 2)
            whirr = math.sin(2 * math.pi * wfreq * t) * math.sin(math.pi * wp) * 0.7
        puff = 0.0
        if progress >= 0.25:
            dt = t - (0.25 * duration)
            dp = dt / (duration - 0.25 * duration)
            pfreq = 85 * math.exp(-12 * dp) + 35
            sub = math.sin(2 * math.pi * pfreq * dt) * math.exp(-7 * dp) * 0.9
            noise_puff = random.uniform(-0.35, 0.35) * math.exp(-18 * dp)
            puff = sub + noise_puff
        val = whirr + puff
        samples.append(val)
    return samples

def synth_rebote_fotones(duration=0.65):
    """Micro-impactos continuos y cristalinos de fotones rebotando (ping-ping-ping)"""
    samples = [0.0] * int(SAMPLE_RATE * duration)
    pings = [
        (0.00, 3100), (0.08, 4200), (0.16, 2800), (0.24, 4900),
        (0.32, 3600), (0.40, 5200), (0.48, 3300)
    ]
    for start_t, freq in pings:
        start_idx = int(start_t * SAMPLE_RATE)
        n_ping = int(0.12 * SAMPLE_RATE)
        for i in range(n_ping):
            idx = start_idx + i
            if idx >= len(samples):
                break
            dt = i / SAMPLE_RATE
            env = math.exp(-35 * dt)
            val = math.sin(2 * math.pi * freq * dt) * env * 0.6
            samples[idx] += val
    return samples

def synth_vacio_espacial(duration=0.85):
    """Clic mecánico apagándose seguido de acorde etéreo profundo de vacío cósmico"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        val = 0.0
        if t < 0.05:
            cp = t / 0.05
            cfreq = 2200 * (1 - cp) + 400
            val += math.sin(2 * math.pi * cfreq * t) * math.exp(-30 * cp) * 0.7
        if t >= 0.12:
            dt = t - 0.12
            dp = dt / (duration - 0.12)
            pad_env = math.sin(math.pi * math.pow(dp, 0.4)) * 0.8
            chord = (
                math.sin(2 * math.pi * 130.81 * dt) * 0.35 +
                math.sin(2 * math.pi * 196.00 * dt) * 0.28 +
                math.sin(2 * math.pi * 261.63 * dt) * 0.22 +
                math.sin(2 * math.pi * 329.63 * dt) * 0.18
            )
            val += chord * pad_env
        samples.append(val)
    return samples

def synth_despliegue_vela(duration=0.75):
    """Servomotores de mástiles retráctiles con tensión elástica de lona reflectante"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        val = 0.0
        if progress < 0.65:
            servo = (2 * ((t * 220) % 1.0) - 1.0) * 0.3
            buzz = math.sin(2 * math.pi * (340 + 60 * math.sin(t * 40)) * t) * 0.3
            val += (servo + buzz) * (0.8 + 0.2 * math.sin(t * 80))
        else:
            dt = t - (0.65 * duration)
            dp = dt / (duration - 0.65 * duration)
            clack = math.sin(2 * math.pi * 480 * dt) * math.exp(-18 * dp) * 0.85
            shimmer = random.uniform(-0.25, 0.25) * math.exp(-8 * dp)
            val += clack + shimmer
        samples.append(val)
    return samples

def synth_rebote_doble_impulso(duration=0.75):
    """Doble rebote elástico (boing-twang) con campana eureka de confirmación física"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        val = 0.0
        if t < 0.22:
            p1 = t / 0.22
            f1 = 160 + 280 * math.sqrt(p1)
            val += math.sin(2 * math.pi * f1 * t) * math.exp(-5 * p1) * 0.7
        elif 0.22 <= t < 0.44:
            dt2 = t - 0.22
            p2 = dt2 / 0.22
            f2 = 220 + 380 * math.sqrt(p2)
            val += math.sin(2 * math.pi * f2 * dt2) * math.exp(-5 * p2) * 0.85
        if t >= 0.40:
            dtc = t - 0.40
            bell = math.sin(2 * math.pi * 2349.32 * dtc) * math.exp(-6.5 * dtc) * 0.8
            bell_harm = math.sin(2 * math.pi * 4698.63 * dtc) * math.exp(-11 * dtc) * 0.3
            val += bell + bell_harm
        samples.append(val)
    return samples

def synth_aceleracion_cosmica(duration=0.9):
    """Silbido sostenido de aceleración relativista ascendente sin límite (warp whoosh)"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        freq = 220 * math.pow(12.7, progress)
        phase = 2 * math.pi * freq * t
        wind = random.uniform(-0.25, 0.25) * math.pow(progress, 1.5)
        env = math.sin(math.pi * math.pow(progress, 0.6))
        val = (math.sin(phase) * 0.75 + wind) * env
        samples.append(val)
    return samples

def synth_surf_cosmico(duration=1.1):
    """Acorde mayor espacial triunfal con arpegio estelar y destello brillante final"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    notes = [174.61, 220.00, 261.63, 329.63, 392.00, 523.25]
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        val = 0.0
        for idx, f in enumerate(notes):
            start_t = idx * 0.04
            if t >= start_t:
                dt = t - start_t
                env = math.exp(-2.2 * dt)
                val += math.sin(2 * math.pi * f * dt) * env * (0.35 / len(notes))
        if progress > 0.4:
            dt_sh = t - 0.4 * duration
            shimmer = (
                math.sin(2 * math.pi * 3135.96 * dt_sh) * 0.15 +
                math.sin(2 * math.pi * 4186.01 * dt_sh) * 0.10
            ) * math.exp(-3.0 * dt_sh)
            val += shimmer
        samples.append(val)
    return samples

def synth_gota_espacial_bloop(duration=0.6):
    """Burbuja líquida en microgravedad (glup-bloop con oscilación elástica wobble)"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        bloop = 0.0
        if progress < 0.45:
            bp = progress / 0.45
            bfreq = 180 + 340 * math.pow(bp, 1.8)
            bloop = math.sin(2 * math.pi * bfreq * t) * math.sin(math.pi * bp) * 0.8
        wobble = 0.0
        if progress >= 0.2:
            wt = t - 0.2 * duration
            wp = wt / (duration - 0.2 * duration)
            w_freq = 65 + 15 * math.sin(2 * math.pi * 9 * wt)
            wobble = math.sin(2 * math.pi * w_freq * wt) * math.exp(-4.0 * wp) * 0.75
        val = bloop + wobble
        samples.append(val)
    return samples

def synth_membrana_elastica_agua(duration=0.65):
    """Membrana de tensión superficial rebotando ante el tacto del dedo (boing acuático suave)"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        vibrato = math.sin(2 * math.pi * 12 * t) * (1 - progress * 0.5) * 20
        freq = (120 + 210 * math.sqrt(progress)) + vibrato
        env = math.sin(math.pi * math.pow(progress, 0.4)) * math.pow(1 - progress, 1.2)
        bubble_hum = math.sin(2 * math.pi * 320 * t) * math.exp(-6 * progress) * 0.25
        val = (math.sin(2 * math.pi * freq * t) + bubble_hum) * env * 0.9
        samples.append(val)
    return samples

def synth_cohesion_molecular(duration=0.65):
    """Atracción cohesiva intermolecular (chasquidos magnéticos y resonancia armónica)"""
    samples = [0.0] * int(SAMPLE_RATE * duration)
    snaps = [(0.00, 1800), (0.07, 2400), (0.14, 3100), (0.22, 3900)]
    for start_t, freq in snaps:
        start_idx = int(start_t * SAMPLE_RATE)
        n_snap = int(0.08 * SAMPLE_RATE)
        for i in range(n_snap):
            idx = start_idx + i
            if idx >= len(samples):
                break
            dt = i / SAMPLE_RATE
            samples[idx] += math.sin(2 * math.pi * freq * dt) * math.exp(-45 * dt) * 0.5
    for i in range(int(0.20 * SAMPLE_RATE), len(samples)):
        dt = (i - 0.20 * SAMPLE_RATE) / SAMPLE_RATE
        chime = (
            math.sin(2 * math.pi * 523.25 * dt) * 0.35 +
            math.sin(2 * math.pi * 659.25 * dt) * 0.25 +
            math.sin(2 * math.pi * 783.99 * dt) * 0.20
        ) * math.exp(-4.5 * dt)
        samples[i] += chime
    return samples

def synth_inmersion_pececillo(duration=0.65):
    """Inmersión suave del pececito de hule dentro de la esfera de agua (schloop acuático)"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        suck_freq = 380 * math.exp(-6 * progress) + 90
        suck = math.sin(2 * math.pi * suck_freq * t) * math.exp(-4.5 * progress) * 0.8
        pop = 0.0
        if t >= 0.22:
            dt = t - 0.22
            pop = math.sin(2 * math.pi * (440 + 200 * dt) * dt) * math.exp(-25 * dt) * 0.65
        water_gargle = math.sin(2 * math.pi * (180 + 40 * math.sin(t * 35)) * t) * math.exp(-5 * progress) * 0.25
        val = suck + pop + water_gargle
        samples.append(val)
    return samples

def synth_succion_popote_adhesion(duration=0.75):
    """Succión por popote y trepado capilar de masa de agua (slurp + reptado viscoso)"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        val = 0.0
        if progress < 0.5:
            sp = progress / 0.5
            bubble_slurp = math.sin(2 * math.pi * (280 + 350 * math.sin(t * 50)) * t) * (0.6 + 0.4 * random.uniform(-0.5, 0.5))
            val += bubble_slurp * math.sin(math.pi * sp) * 0.7
        if progress >= 0.35:
            dt = t - (0.35 * duration)
            dp = dt / (duration - 0.35 * duration)
            creep_freq = 150 + 480 * math.pow(dp, 2)
            glide = math.sin(2 * math.pi * creep_freq * dt) * math.exp(-3.5 * dp) * 0.85
            noise_whoosh = random.uniform(-0.25, 0.25) * math.sin(math.pi * dp)
            val += glide + noise_whoosh
        samples.append(val)
    return samples

def synth_mascara_agua_splat(duration=0.85):
    """Impacto húmedo elástico en la cara (SPLAT-GLOOP) y reverberación subacuática ahogada"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        splat_noise = random.uniform(-0.6, 0.6) * math.exp(-18 * progress)
        splat_thud = math.sin(2 * math.pi * (110 * math.exp(-10 * progress) + 40) * t) * math.exp(-6 * progress) * 0.8
        underwater_hum = (
            math.sin(2 * math.pi * 95 * t) * 0.4 +
            math.sin(2 * math.pi * 140 * t) * 0.25
        ) * math.pow(1 - progress, 1.2)
        val = splat_noise + splat_thud + underwater_hum
        samples.append(val)
    return samples

def synth_toalla_secado_espacial(duration=1.0):
    """Fricción suave de toalla de microfibra seguida de acorde espacial alegre de alivio"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        val = 0.0
        if progress < 0.35:
            tp = progress / 0.35
            towel = random.uniform(-0.4, 0.4) * math.sin(math.pi * tp)
            val += towel
        if progress >= 0.25:
            dt = t - (0.25 * duration)
            chime = (
                math.sin(2 * math.pi * 440.00 * dt) * 0.30 +
                math.sin(2 * math.pi * 554.37 * dt) * 0.25 +
                math.sin(2 * math.pi * 659.25 * dt) * 0.20 +
                math.sin(2 * math.pi * 880.00 * dt) * 0.15
            ) * math.exp(-2.8 * dt)
            val += chime
        samples.append(val)
    return samples

def synth_viento_misterio_penitentes(duration=0.85):
    """Viento seco de alta montaña andina con ráfaga y golpe orquestal misterioso (shhh-BOOM)"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        val = 0.0
        # Viento silbante seco en alta montaña
        wind_mod = math.sin(2 * math.pi * 3.5 * t) * 0.3
        wind_noise = random.uniform(-0.35, 0.35) * (1.0 + wind_mod) * math.sin(math.pi * progress)
        wind_whistle = math.sin(2 * math.pi * (420 + 180 * math.sin(t * 12)) * t) * 0.15 * math.sin(math.pi * progress)
        val += wind_noise + wind_whistle
        # Golpe orquestal misterioso a mitad
        if t >= 0.35:
            dt = t - 0.35
            dp = dt / (duration - 0.35)
            boom = math.sin(2 * math.pi * 65 * math.exp(-4 * dp) * dt) * math.exp(-6 * dp) * 0.8
            chime_sub = math.sin(2 * math.pi * 196.0 * dt) * math.exp(-4.5 * dp) * 0.35
            val += boom + chime_sub
        samples.append(val)
    return samples

def synth_resbalon_hielo_crack(duration=0.65):
    """Chirrido seco de hielo duro contra goma (SKRRR-CRACK) e impacto de choque"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        val = 0.0
        # Chirrido skrrr
        if progress < 0.45:
            sp = progress / 0.45
            skrr = random.uniform(-0.55, 0.55) * math.sin(2 * math.pi * (1600 + 400 * math.sin(t * 80)) * t) * math.sin(math.pi * sp)
            val += skrr * 0.8
        # Crack de hielo duro y golpe cómico
        if t >= 0.30:
            dt = t - 0.30
            dp = dt / (duration - 0.30)
            crack = math.sin(2 * math.pi * 2800 * dt) * math.exp(-40 * dp) * 0.75
            thud = math.sin(2 * math.pi * 90 * math.exp(-12 * dp) * dt) * math.exp(-8 * dp) * 0.85
            val += crack + thud
        samples.append(val)
    return samples

def synth_fosforo_sublimacion_tsss(duration=0.75):
    """Rascado de fósforo (shhh-flick) y siseo limpio de vaporización directa a gas (tsss)"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        val = 0.0
        # Fósforo raspando
        if progress < 0.25:
            fp = progress / 0.25
            flick = random.uniform(-0.6, 0.6) * math.exp(-15 * fp)
            click = math.sin(2 * math.pi * 1200 * t) * math.exp(-30 * fp) * 0.5
            val += flick + click
        # Siseo gaseoso limpio continuo (sublimación)
        if t >= 0.18:
            dt = t - 0.18
            dp = dt / (duration - 0.18)
            hiss = random.uniform(-0.35, 0.35) * math.sin(math.pi * math.pow(dp, 0.5)) * (1 - dp) * 0.85
            vapor_tone = math.sin(2 * math.pi * (3200 + 300 * math.sin(dt * 25)) * dt) * 0.12 * math.exp(-2.5 * dp)
            val += hiss + vapor_tone
        samples.append(val)
    return samples

def synth_diagrama_sublimacion_campana(duration=0.70):
    """Whoosh de cambio de fase y campana de acierto científico eureka"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        val = 0.0
        # Whoosh de flecha que cruza
        if progress < 0.40:
            wp = progress / 0.40
            whoosh = random.uniform(-0.4, 0.4) * math.sin(math.pi * wp) * 0.7
            val += whoosh
        # Campana eureka de cambio de estado
        if t >= 0.25:
            dt = t - 0.25
            dp = dt / (duration - 0.25)
            bell = (
                math.sin(2 * math.pi * 880.0 * dt) * 0.40 +
                math.sin(2 * math.pi * 1318.5 * dt) * 0.30 +
                math.sin(2 * math.pi * 1760.0 * dt) * 0.20
            ) * math.exp(-4.2 * dt)
            val += bell
        samples.append(val)
    return samples

def synth_timelapse_erosion_solar(duration=0.75):
    """Avance rápido de radiación solar tallando zanjas profundas (fast-forward sibilante)"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        # Frecuencia en barrido ascendente acelerado
        sweep_freq = 240 + 900 * math.pow(progress, 1.8)
        whir = math.sin(2 * math.pi * sweep_freq * t) * (0.35 + 0.15 * math.sin(t * 60))
        hiss_carve = random.uniform(-0.28, 0.28) * (0.5 + 0.5 * progress)
        env = math.sin(math.pi * progress)
        val = (whir + hiss_carve) * env * 0.9
        samples.append(val)
    return samples

def synth_campana_monasterio_misterio(duration=0.85):
    """Campana profunda de abadía o monasterio con eco andino místico y ráfaga gélida"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        # Acorde de campana de monasterio (Sol menor / notas graves sagradas)
        bell = (
            math.sin(2 * math.pi * 220.00 * t) * 0.45 +
            math.sin(2 * math.pi * 261.63 * t) * 0.30 +
            math.sin(2 * math.pi * 329.63 * t) * 0.25 +
            math.sin(2 * math.pi * 659.25 * t) * 0.15
        ) * math.exp(-3.2 * t)
        # Ráfaga de viento gélido de fondo
        wind = random.uniform(-0.18, 0.18) * math.sin(math.pi * progress)
        val = bell + wind
        samples.append(val)
    return samples

def synth_remate_andino_viento(duration=0.95):
    """Suspiro cómico, crujido de pasos firmes y remate melódico andino sutil de cierre"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        val = 0.0
        # Suspiro cómico inicial
        if progress < 0.30:
            sp = progress / 0.30
            fuff = random.uniform(-0.3, 0.3) * math.sin(math.pi * sp) * 0.6
            val += fuff
        # Crujido de pisada en nieve dura
        if 0.20 <= progress < 0.45:
            cp = (progress - 0.20) / 0.25
            crunch = random.uniform(-0.45, 0.45) * math.exp(-12 * cp)
            val += crunch
        # Remate pentatónico andino sutil (flauta de pan estilizada)
        if t >= 0.35:
            dt = t - 0.35
            andina = (
                math.sin(2 * math.pi * 587.33 * dt) * 0.35 + # D5
                math.sin(2 * math.pi * 659.25 * dt) * 0.28 + # E5
                math.sin(2 * math.pi * 880.00 * dt) * 0.22   # A5
            ) * math.exp(-3.5 * dt)
            air_flute = math.sin(2 * math.pi * 1760 * dt) * 0.08 * math.exp(-3.0 * dt)
            val += andina + air_flute
        samples.append(val)
    return samples

def synth_fuego_azul_presion(duration=0.85):
    """Viento nocturno grave volcánico, silbido de gas a presión (fsssshh) y acorde misterioso"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        # Viento nocturno en cráter
        wind = math.sin(2 * math.pi * 55 * t) * (0.35 + 0.15 * math.sin(t * 12)) * math.sin(math.pi * progress)
        # Silbido de gas a presión
        hiss = random.uniform(-0.3, 0.3) * math.sin(2 * math.pi * (1800 + 400 * math.sin(t * 20)) * t) * 0.4 * math.sin(math.pi * progress)
        # Acorde sintético misterioso (Re menor cósmico / volcánico)
        chord = 0.0
        if t >= 0.25:
            dt = t - 0.25
            chord = (
                math.sin(2 * math.pi * 146.83 * dt) * 0.35 + # D3
                math.sin(2 * math.pi * 220.00 * dt) * 0.25 + # A3
                math.sin(2 * math.pi * 349.23 * dt) * 0.20   # F4
            ) * math.exp(-3.5 * dt)
        val = wind + hiss + chord
        samples.append(val)
    return samples

def synth_tos_mascara_antigas(duration=0.75):
    """Toses cómicas (cof-cof), tintineo metálico de cuchara y clic hermético de máscara"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        val = 0.0
        # Dos golpes de tos (cof - cof)
        if 0.05 <= progress < 0.20:
            cp = (progress - 0.05) / 0.15
            cough1 = random.uniform(-0.5, 0.5) * math.sin(2 * math.pi * 220 * t) * math.exp(-12 * cp)
            val += cough1
        if 0.25 <= progress < 0.45:
            cp = (progress - 0.25) / 0.20
            cough2 = random.uniform(-0.6, 0.6) * math.sin(2 * math.pi * 180 * t) * math.exp(-10 * cp)
            val += cough2
        # Tintineo de cuchara metálica
        if 0.40 <= progress < 0.60:
            dt = t - 0.40 * duration
            ting = (math.sin(2 * math.pi * 3200 * dt) * 0.4 + math.sin(2 * math.pi * 4800 * dt) * 0.25) * math.exp(-25 * dt)
            val += ting
        # Clic y sello hermético de máscara (fshhh)
        if progress >= 0.55:
            dt = t - 0.55 * duration
            dp = dt / (duration - 0.55 * duration)
            click = math.sin(2 * math.pi * 850 * dt) * math.exp(-40 * dt) * 0.7
            seal_fsh = random.uniform(-0.35, 0.35) * math.sin(math.pi * dp) * math.exp(-4 * dp)
            val += click + seal_fsh
        samples.append(val)
    return samples

def synth_subsuelo_olla_presion(duration=0.75):
    """Gorgoteo de magma rojo (bloop-glup) y siseo ascendente de escape a presión (TSSSSS)"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        val = 0.0
        # Gorgoteo viscoso de lava
        if progress < 0.35:
            glup = math.sin(2 * math.pi * (110 + 90 * math.sin(t * 40)) * t) * (1 - progress / 0.35) * 0.7
            val += glup
        # Válvula de presión ascendente silbando
        if progress >= 0.20:
            dt = t - 0.20 * duration
            dp = dt / (duration - 0.20 * duration)
            whistle_freq = 1200 + 2600 * math.pow(dp, 1.8)
            whistle = math.sin(2 * math.pi * whistle_freq * dt) * 0.35 * math.sin(math.pi * dp)
            hiss_noise = random.uniform(-0.35, 0.35) * dp * 0.8
            val += whistle + hiss_noise
        samples.append(val)
    return samples

def synth_soplete_ignicion_fwoosh(duration=0.85):
    """Ignición repentina de gas (FWOOOSH) y bramido potente de soplete de oxiacetileno"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        val = 0.0
        # Estallido de ignición inicial (FWOOSH)
        if progress < 0.35:
            fp = progress / 0.35
            fwoosh = random.uniform(-0.7, 0.7) * math.sin(math.pi * fp) * 0.85
            thump = math.sin(2 * math.pi * (80 * math.exp(-8 * fp) + 35) * t) * 0.9 * math.exp(-5 * fp)
            val += fwoosh + thump
        # Bramido rugiente de soplete a presión continuo
        if progress >= 0.25:
            dt = t - 0.25 * duration
            dp = dt / (duration - 0.25 * duration)
            torch_roar = math.sin(2 * math.pi * (320 + 80 * math.sin(t * 60)) * t) * 0.4
            torch_noise = random.uniform(-0.4, 0.4) * (0.8 + 0.2 * math.sin(t * 80))
            val += (torch_roar + torch_noise) * math.sin(math.pi * math.pow(dp, 0.4)) * 0.9
        samples.append(val)
    return samples

def synth_goteo_azufre_crepitar(duration=0.80):
    """Goteo viscoso ardiente de azufre (drip-fzzzt) y chisporroteo de fuego líquido"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        val = 0.0
        # Gota viscosa cayendo
        if progress < 0.35:
            dp = progress / 0.35
            drip = math.sin(2 * math.pi * (380 + 400 * dp) * t) * math.exp(-8 * dp) * 0.75
            val += drip
        # Fzzzt / crepitar de azufre encendido
        if progress >= 0.20:
            dt = t - 0.20 * duration
            dp = dt / (duration - 0.20 * duration)
            crackle = random.uniform(-0.35, 0.35) if (int(t * 400) % 3 == 0) else 0.0
            hiss = random.uniform(-0.25, 0.25) * math.sin(math.pi * dp)
            val += crackle + hiss
        samples.append(val)
    return samples

def synth_amanecer_timelapse_fumarola(duration=0.75):
    """Aceleración de amanecer (whoosh-clock) con canto distante y siseo de fumarola"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        # Whoosh de avance rápido
        sweep = math.sin(2 * math.pi * (260 + 850 * progress) * t) * 0.3 * math.sin(math.pi * progress)
        wind = random.uniform(-0.25, 0.25) * math.sin(math.pi * progress)
        # Siseo suave de fumarola diurna
        fumarola = random.uniform(-0.15, 0.15) * (0.5 + 0.5 * progress)
        val = sweep + wind + fumarola
        samples.append(val)
    return samples

def synth_remate_volcan_azul_soplete(duration=0.95):
    """Disminución de zumbido volcánico y remate sintético etéreo de contemplación cósmica"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        # Zumbido volcánico apagándose
        hum = math.sin(2 * math.pi * 65 * t) * (1 - progress) * 0.35
        # Acorde atmosférico épico de contemplación (Mi menor / Si menor)
        pad = 0.0
        if t >= 0.20:
            dt = t - 0.20
            pad = (
                math.sin(2 * math.pi * 164.81 * dt) * 0.40 + # E3
                math.sin(2 * math.pi * 246.94 * dt) * 0.30 + # B3
                math.sin(2 * math.pi * 329.63 * dt) * 0.25 + # E4
                math.sin(2 * math.pi * 493.88 * dt) * 0.18   # B4
            ) * math.exp(-2.8 * dt)
        val = hum + pad
        samples.append(val)
    return samples

def synth_plastico_crujiente_disolucion(duration=0.85):
    """Crujido de plástico aplastándose (crinkle-crunch) y sorbo cómico de disolución (slurp)"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        val = 0.0
        # Crujido de plástico aplastándose
        if progress < 0.45:
            cp = progress / 0.45
            crinkle = (random.uniform(-0.6, 0.6) if (int(t * 800) % 4 == 0) else 0.0) * math.exp(-6 * cp)
            thud = math.sin(2 * math.pi * 120 * t) * math.exp(-12 * cp) * 0.4
            val += crinkle + thud
        # Sorbo cómico de disolución enzimática (slurp)
        if progress >= 0.35:
            dt = t - 0.35 * duration
            dp = dt / (duration - 0.35 * duration)
            slurp_freq = 280 + 350 * math.pow(dp, 1.5) + math.sin(2 * math.pi * 35 * dt) * 80
            slurp = math.sin(2 * math.pi * slurp_freq * dt) * math.sin(math.pi * dp) * 0.75
            bubble = math.sin(2 * math.pi * 600 * dt) * 0.15 * (1 - dp)
            val += slurp + bubble
        samples.append(val)
    return samples

def synth_placa_petri_hallazgo(duration=0.75):
    """Clic mecánico de microscopio (clack) y campana eureka de hallazgo biológico (ding)"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        val = 0.0
        # Clic de microscopio
        if progress < 0.25:
            cp = progress / 0.25
            clack = math.sin(2 * math.pi * 680 * t) * math.exp(-35 * cp) * 0.8
            click_hi = math.sin(2 * math.pi * 2400 * t) * math.exp(-40 * cp) * 0.4
            val += clack + click_hi
        # Campana eureka de hallazgo
        if t >= 0.18:
            dt = t - 0.18
            ding = (
                math.sin(2 * math.pi * 1046.50 * dt) * 0.45 + # C6
                math.sin(2 * math.pi * 1318.51 * dt) * 0.30 + # E6
                math.sin(2 * math.pi * 1567.98 * dt) * 0.20   # G6
            ) * math.exp(-4.5 * dt)
            val += ding
        samples.append(val)
    return samples

def synth_bacteria_chomp_plastico(duration=0.65):
    """Ladrido o gemido tierno (yip) y mordisco seco de caricatura (CHOMP)"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        val = 0.0
        # Yip tierno de mascota
        if progress < 0.35:
            yp = progress / 0.35
            yip_freq = 420 + 380 * math.sin(math.pi * yp)
            yip = math.sin(2 * math.pi * yip_freq * t) * math.sin(math.pi * yp) * 0.65
            val += yip
        # CHOMP de mordida
        if t >= 0.25:
            dt = t - 0.25
            dp = dt / (duration - 0.25)
            chomp = math.sin(2 * math.pi * (140 * math.exp(-15 * dp) + 45) * dt) * math.exp(-10 * dp) * 0.85
            crunch = (random.uniform(-0.5, 0.5) if (int(dt * 1200) % 3 == 0) else 0.0) * math.exp(-18 * dp)
            val += chomp + crunch
        samples.append(val)
    return samples

def synth_tijeras_petasa_snip(duration=0.75):
    """Adhesión con ventosa (schloop) y ráfaga de tijeras moleculares (snip-snip-snip)"""
    samples = [0.0] * int(SAMPLE_RATE * duration)
    # Ventosa inicial schloop
    schloop_len = int(0.25 * SAMPLE_RATE)
    for i in range(schloop_len):
        t = i / SAMPLE_RATE
        p = i / schloop_len
        freq = 180 + 320 * math.sin(math.pi * p)
        samples[i] += math.sin(2 * math.pi * freq * t) * math.sin(math.pi * p) * 0.7
    # 3 chasquidos de tijera metálicos
    snips = [(0.25, 2200), (0.40, 2600), (0.55, 3100)]
    for start_t, freq in snips:
        s_idx = int(start_t * SAMPLE_RATE)
        n_snip = int(0.08 * SAMPLE_RATE)
        for i in range(n_snip):
            idx = s_idx + i
            if idx >= len(samples):
                break
            dt = i / SAMPLE_RATE
            metal = (math.sin(2 * math.pi * freq * dt) + 0.4 * math.sin(2 * math.pi * (freq * 1.6) * dt)) * math.exp(-45 * dt) * 0.75
            samples[idx] += metal
    return samples

def synth_recarga_metabolica_powerup(duration=0.80):
    """Campaneo ascendente glockenspiel y sonido de subida de energía (power-up)"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        # Frecuencia en barrido ascendente limpio tipo videojuego
        power_freq = 260 + 750 * math.pow(progress, 1.4)
        synth = math.sin(2 * math.pi * power_freq * t) * math.sin(math.pi * progress) * 0.55
        # Campaneo armónico
        bell = 0.0
        if t >= 0.40:
            dt = t - 0.40
            bell = (
                math.sin(2 * math.pi * 880.00 * dt) * 0.35 +
                math.sin(2 * math.pi * 1108.73 * dt) * 0.25 +
                math.sin(2 * math.pi * 1318.51 * dt) * 0.20
            ) * math.exp(-4.0 * dt)
        val = synth + bell
        samples.append(val)
    return samples

def synth_aspiradora_enzima_vrooom(duration=0.85):
    """Zumbido láser y aspiradora industrial acelerada (VROOOOM) con destello limpio"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        val = 0.0
        # Pew-laser inicial
        if progress < 0.25:
            lp = progress / 0.25
            lf = 1400 * math.exp(-12 * lp) + 200
            laser = math.sin(2 * math.pi * lf * t) * math.exp(-8 * lp) * 0.65
            val += laser
        # VROOOM devorador acelerado
        if progress >= 0.18:
            dt = t - 0.18 * duration
            dp = dt / (duration - 0.18 * duration)
            vroom_freq = 110 + 280 * math.pow(dp, 1.6)
            whir = math.sin(2 * math.pi * vroom_freq * dt) * 0.45
            air = random.uniform(-0.35, 0.35) * (0.5 + 0.5 * dp)
            val += (whir + air) * math.sin(math.pi * math.pow(dp, 0.5)) * 0.85
        # Ting final
        if t >= 0.70:
            dt = t - 0.70
            ting = math.sin(2 * math.pi * 2093.0 * dt) * math.exp(-18 * dt) * 0.3
            val += ting
        samples.append(val)
    return samples

def synth_eructo_paseo_ecologico(duration=0.95):
    """Eructo diminuto cómico (burp-pop) y remate musical alegre con flauta"""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        val = 0.0
        # Eructito tierno con burbuja (burp - pop)
        if progress < 0.30:
            bp = progress / 0.30
            burp = math.sin(2 * math.pi * (85 + 30 * math.sin(t * 50)) * t) * math.sin(math.pi * bp) * 0.5
            pop = 0.0
            if t >= 0.15:
                dt_p = t - 0.15
                pop = math.sin(2 * math.pi * 650 * dt_p) * math.exp(-40 * dt_p) * 0.5
            val += burp + pop
        # Melodía alegre y optimista de cierre ecológico
        if t >= 0.25:
            dt = t - 0.25
            flute = (
                math.sin(2 * math.pi * 523.25 * dt) * 0.35 + # C5
                math.sin(2 * math.pi * 659.25 * dt) * 0.28 + # E5
                math.sin(2 * math.pi * 783.99 * dt) * 0.22 + # G5
                math.sin(2 * math.pi * 1046.50 * dt) * 0.15  # C6
            ) * math.exp(-3.0 * dt)
            val += flute
        samples.append(val)
    return samples

def synth_auto_rewind_rueda(duration=0.85):
    """Rugido de motor a velocidad + aire cortante + frenazo cómico de cinta al revés."""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        val = 0.0
        # Fase 1: Motor veloz + viento (0.0 a 0.45s)
        if t < 0.45:
            p1 = t / 0.45
            eng_freq = 90 + 70 * p1
            engine = (math.sin(2 * math.pi * eng_freq * t) * 0.4 +
                      math.sin(2 * math.pi * eng_freq * 2 * t) * 0.25 +
                      math.sin(2 * math.pi * eng_freq * 3 * t) * 0.15)
            wind = (random.random() * 2 - 1) * 0.15 * p1
            val = (engine + wind) * math.sin(math.pi * p1 * 0.9)
        # Fase 2: Frenazo / cinta en reversa skrrr-rewind (0.42 a 0.85s)
        if t >= 0.40:
            dt = t - 0.40
            p2 = dt / 0.45
            # Pitch deslizándose hacia arriba con modulaciones rápidas
            freq_tape = 900 + 1800 * math.pow(p2, 1.4) + math.sin(2 * math.pi * 35 * dt) * 350
            tape = math.sin(2 * math.pi * freq_tape * dt) * 0.45
            chatter = math.sin(2 * math.pi * (freq_tape * 0.5) * dt) * 0.2
            noise = (random.random() * 2 - 1) * 0.18 * math.exp(-3.0 * p2)
            env2 = math.sin(math.pi * math.sin(math.pi * p2 * 0.5)) * math.exp(-1.5 * p2)
            val += (tape + chatter + noise) * env2
        samples.append(val)
    return samples

def synth_pausa_proyector_cine(duration=0.80):
    """Clic de pausa + campanilla de rin + traqueteo de proyector antiguo."""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        val = 0.0
        # 1. Clic de pausa al inicio (0.0 a 0.08s)
        if t < 0.08:
            p = t / 0.08
            val += (math.sin(2 * math.pi * 320 * t) * 0.6 + (random.random() * 2 - 1) * 0.4) * math.exp(-35 * t)
        # 2. Campanilla metálica del rin (0.05 a 0.60s)
        if t >= 0.05:
            dt = t - 0.05
            ting = (math.sin(2 * math.pi * 1760 * dt) * 0.35 +
                    math.sin(2 * math.pi * 3520 * dt) * 0.18 +
                    math.sin(2 * math.pi * 5280 * dt) * 0.08) * math.exp(-7.0 * dt)
            val += ting
        # 3. Traqueteo mecánico de proyector (0.20 a 0.80s, ráfagas cada 0.08s)
        if t >= 0.20:
            dt_proj = t - 0.20
            period = 0.075
            pulse_t = dt_proj % period
            if pulse_t < 0.025:
                p_clack = pulse_t / 0.025
                clack = (math.sin(2 * math.pi * 650 * pulse_t) * 0.3 + (random.random() * 2 - 1) * 0.25) * math.exp(-60 * pulse_t)
                val += clack * (1 - dt_proj / 0.60)
        samples.append(val)
    return samples

def synth_obturador_camara_reloj(duration=0.75):
    """Disparos sucesivos de obturador réflex (chck-chck-chck) y siseo suave."""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    click_times = [0.06, 0.28, 0.50]
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        val = 0.0
        # Disparos de obturador
        for c_t in click_times:
            if c_t <= t < c_t + 0.12:
                dt = t - c_t
                # Golpe de espejo (thud bajo) + cortinilla metálica
                thud = math.sin(2 * math.pi * 140 * dt) * 0.45 * math.exp(-35 * dt)
                click = (random.random() * 2 - 1) * 0.4 * math.exp(-45 * dt)
                curtain = math.sin(2 * math.pi * 2400 * dt) * 0.2 * math.exp(-30 * dt)
                val += thud + click + curtain
        # Siseo continuo de rebobinado suave
        hiss = (random.random() * 2 - 1) * 0.04 * math.sin(math.pi * (t / duration))
        val += hiss
        samples.append(val)
    return samples

def synth_helicoptero_aspas_reversa(duration=0.90):
    """Turbina acelerando + corte de aspas + silbido descendente en reversa."""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        val = 0.0
        # Fase 1: Chop-chop acelerando (0.0 a 0.50s)
        if t < 0.55:
            p1 = t / 0.55
            mod_rate = 8 + 20 * p1 # frecuencia de corte de aspas
            blade_mod = math.pow(0.5 + 0.5 * math.sin(2 * math.pi * mod_rate * t), 3)
            rotor_rumble = math.sin(2 * math.pi * (70 + 40 * p1) * t) * 0.5
            val += rotor_rumble * blade_mod * math.sin(math.pi * p1 * 0.95)
        # Fase 2: Silbido estroboscópico en reversa (0.45 a 0.90s)
        if t >= 0.45:
            dt = t - 0.45
            p2 = dt / 0.45
            # Descenso de tono de hélice en aparente reversa
            rev_freq = 580 * math.exp(-2.2 * p2) + 160
            whistle = math.sin(2 * math.pi * rev_freq * dt) * 0.35
            harmonic = math.sin(2 * math.pi * rev_freq * 1.5 * dt) * 0.18
            slow_chop = math.pow(0.5 + 0.5 * math.sin(2 * math.pi * 4 * dt), 2)
            env2 = math.sin(math.pi * math.sin(math.pi * p2 * 0.5)) * math.exp(-0.8 * p2)
            val += (whistle + harmonic) * slow_chop * env2
        samples.append(val)
    return samples

def synth_camara_beep_congelado(duration=0.75):
    """Clic de dial + BEEP electrónico de bloqueo + zumbido irreal de aspas congeladas."""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    dial_times = [0.04, 0.11, 0.18]
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        val = 0.0
        # Diales de ajuste (tick-tick-tick)
        for d_t in dial_times:
            if d_t <= t < d_t + 0.04:
                dt = t - d_t
                val += (math.sin(2 * math.pi * 2200 * dt) * 0.25 + (random.random() * 2 - 1) * 0.2) * math.exp(-70 * dt)
        # Beep electrónico de confirmación (0.25 a 0.42s)
        if 0.25 <= t < 0.42:
            dt_beep = t - 0.25
            val += (math.sin(2 * math.pi * 950 * dt_beep) * 0.4 +
                    math.sin(2 * math.pi * 1900 * dt_beep) * 0.15) * math.sin(math.pi * (dt_beep / 0.17))
        # Zumbido irreal estático flotante (0.40 a 0.75s)
        if t >= 0.40:
            dt_hum = t - 0.40
            hum = (math.sin(2 * math.pi * 220 * dt_hum) * 0.25 +
                   math.sin(2 * math.pi * 440 * dt_hum) * 0.12) * math.exp(-2.2 * dt_hum)
            val += hum
        samples.append(val)
    return samples

def synth_parpadeo_estroboscopico(duration=0.80):
    """Aleteo veloz de pestañas + audio estroboscópico entrecortado."""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        # Efecto estroboscópico: chopper rítmico de 14 Hz (como párpados batiendo)
        blink_rate = 14
        shutter_gate = 1.0 if (math.sin(2 * math.pi * blink_rate * t) > 0.15) else 0.05
        # Sonido de aleteo veloz (sweep agudo de aire)
        flutter_freq = 500 + 400 * math.sin(2 * math.pi * blink_rate * t)
        air_flutter = math.sin(2 * math.pi * flutter_freq * t) * 0.35
        wind_noise = (random.random() * 2 - 1) * 0.2
        env = math.sin(math.pi * progress)
        val = (air_flutter + wind_noise) * shutter_gate * env
        samples.append(val)
    return samples

def synth_mareo_estrellas_thud(duration=0.95):
    """Silbido de mareo de caricatura (twinkle) + golpe acolchonado (thud) + acorde cómico."""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    notes = [784.0, 987.77, 1174.66, 1567.98, 1975.53] # G5, B5, D6, G6, B6
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        val = 0.0
        # 1. Campanitas de mareo orbitando (0.0 a 0.50s)
        if t < 0.50:
            for idx, freq in enumerate(notes):
                t_note = t - (idx * 0.08)
                if 0 <= t_note < 0.25:
                    vibrato = math.sin(2 * math.pi * 7 * t_note) * 20
                    bell = math.sin(2 * math.pi * (freq + vibrato) * t_note) * 0.22 * math.exp(-9 * t_note)
                    val += bell
        # 2. Golpe sordo acolchado thud (0.45 a 0.65s)
        if 0.45 <= t < 0.65:
            dt_thud = t - 0.45
            thud = math.sin(2 * math.pi * 72 * dt_thud) * 0.55 * math.exp(-22 * dt_thud)
            cloth = (random.random() * 2 - 1) * 0.25 * math.exp(-35 * dt_thud)
            val += thud + cloth
        # 3. Acorde cómico resolutivo (0.62 a 0.95s)
        if t >= 0.62:
            dt_chord = t - 0.62
            c_notes = [523.25, 659.25, 783.99, 1046.50] # C5, E5, G5, C6
            chord = sum(math.sin(2 * math.pi * f_c * dt_chord) * 0.15 for f_c in c_notes) * math.exp(-5.5 * dt_chord)
            val += chord
        samples.append(val)
    return samples

def synth_viento_sal_suspenso(duration=0.85):
    """Viento desolado + paso crujiente sobre costra de sal + campana de suspenso."""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        val = 0.0
        # 1. Viento desolado y aullido tenue (0.0 a 0.85s)
        wind_mod = math.sin(2 * math.pi * 3.5 * t) * 60
        wind = math.sin(2 * math.pi * (260 + wind_mod) * t) * 0.22 + (random.random() * 2 - 1) * 0.15
        val += wind * math.sin(math.pi * (t / duration))
        # 2. Paso crujiente sobre sal "crunch" (0.25 a 0.50s)
        if 0.25 <= t < 0.50:
            dt_c = t - 0.25
            crunch = (random.random() * 2 - 1) * 0.45 * math.exp(-22 * dt_c)
            gravel = math.sin(2 * math.pi * 750 * dt_c) * 0.2 * math.exp(-35 * dt_c)
            val += crunch + gravel
        # 3. Acorde sordo de suspenso con campana metálica (0.45 a 0.85s)
        if t >= 0.45:
            dt_bell = t - 0.45
            bell = (math.sin(2 * math.pi * 370 * dt_bell) * 0.35 +
                    math.sin(2 * math.pi * 740 * dt_bell) * 0.18 +
                    math.sin(2 * math.pi * 1110 * dt_bell) * 0.1) * math.exp(-4.5 * dt_bell)
            val += bell
        samples.append(val)
    return samples

def synth_golpe_ceramica_piedra(duration=0.75):
    """Golpe resonante de losa/cerámica ("CLINK-CLACK") + chillido cómico del Stickman."""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        val = 0.0
        # 1. Doble impacto cerámico "CLINK-CLACK" (t=0.04 y t=0.12)
        for clk_t in [0.04, 0.12]:
            if clk_t <= t < clk_t + 0.35:
                dt = t - clk_t
                clink = (math.sin(2 * math.pi * 2150 * dt) * 0.45 +
                         math.sin(2 * math.pi * 4300 * dt) * 0.25 +
                         (random.random() * 2 - 1) * 0.2) * math.exp(-28 * dt)
                val += clink
        # 2. Chillido ahogado de caricatura (0.32 a 0.65s, pitch deslizándose hacia arriba)
        if 0.32 <= t < 0.65:
            dt_y = t - 0.32
            p_y = dt_y / 0.33
            scream_freq = 600 + 1200 * math.pow(p_y, 2)
            scream = (math.sin(2 * math.pi * scream_freq * dt_y) * 0.35 +
                      math.sin(2 * math.pi * (scream_freq * 1.5) * dt_y) * 0.15) * math.sin(math.pi * p_y)
            val += scream
        samples.append(val)
    return samples

def synth_siseo_alerta_quimica(duration=0.80):
    """Suspiro de alivio + siseo cáustico al tocar agua + alerta tóxica dual-tone."""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        val = 0.0
        # 1. Suspiro "fiuuu" cayendo de tono (0.0 a 0.30s)
        if t < 0.30:
            p_sigh = t / 0.30
            sigh_freq = 700 - 350 * p_sigh
            sigh = (math.sin(2 * math.pi * sigh_freq * t) * 0.2 + (random.random() * 2 - 1) * 0.15) * math.sin(math.pi * p_sigh)
            val += sigh
        # 2. Siseo químico cáustico "tsss" (0.28 a 0.55s)
        if 0.28 <= t < 0.55:
            dt_hiss = t - 0.28
            hiss = (random.random() * 2 - 1) * 0.45 * math.exp(-8 * dt_hiss) * (0.5 + 0.5 * math.sin(2 * math.pi * 25 * dt_hiss))
            val += hiss
        # 3. Pitido de alerta tóxica (0.50 a 0.80s, dos beeps agudos)
        for b_t in [0.52, 0.68]:
            if b_t <= t < b_t + 0.09:
                dt_b = t - b_t
                beep = math.sin(2 * math.pi * 1850 * dt_b) * 0.38 * math.sin(math.pi * (dt_b / 0.09))
                val += beep
        samples.append(val)
    return samples

def synth_retumbo_volcan_egipcio(duration=0.90):
    """Retumbo volcánico grave subterráneo + fanfarria egipcia con címbalos."""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        val = 0.0
        # 1. Retumbo volcánico sub-grave (0.0 a 0.55s)
        if t < 0.55:
            p_r = t / 0.55
            rumble_freq = 55 + math.sin(2 * math.pi * 8 * t) * 15
            rumble = (math.sin(2 * math.pi * rumble_freq * t) * 0.55 +
                      math.sin(2 * math.pi * (rumble_freq * 2) * t) * 0.25 +
                      (random.random() * 2 - 1) * 0.15) * math.sin(math.pi * p_r)
            val += rumble
        # 2. Fanfarria breve egipcia (escala frigia / doble armónica: E, F, G#, A) a partir de 0.45s
        if t >= 0.45:
            dt_eg = t - 0.45
            egypt_notes = [(0.0, 659.25), (0.10, 698.46), (0.22, 830.61), (0.33, 880.00)]
            for note_t, n_freq in egypt_notes:
                if note_t <= dt_eg < note_t + 0.20:
                    dt_n = dt_eg - note_t
                    flute = (math.sin(2 * math.pi * n_freq * dt_n) * 0.3 +
                             math.sin(2 * math.pi * n_freq * 2 * dt_n) * 0.12) * math.exp(-8 * dt_n)
                    val += flute
            # Címbalo antiguo
            cymbal = (random.random() * 2 - 1) * 0.18 * math.exp(-10 * dt_eg)
            val += cymbal
        samples.append(val)
    return samples

def synth_impacto_espejo_agua_splat(duration=0.80):
    """Impacto contra agua densa ("splat") + zumbido químico de sal + "glup" sordo."""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        val = 0.0
        # 1. Impacto amortiguado "splat" (0.02 a 0.25s)
        if 0.02 <= t < 0.25:
            dt_sp = t - 0.02
            splat = (math.sin(2 * math.pi * 120 * dt_sp) * 0.45 + (random.random() * 2 - 1) * 0.4) * math.exp(-25 * dt_sp)
            val += splat
        # 2. Zumbido de sal deshidratando (0.20 a 0.60s)
        if 0.20 <= t < 0.60:
            dt_chem = t - 0.20
            chem_hum = (math.sin(2 * math.pi * 420 * dt_chem) * 0.25 +
                        math.sin(2 * math.pi * 840 * dt_chem) * 0.12) * (0.5 + 0.5 * math.sin(2 * math.pi * 18 * dt_chem)) * math.exp(-3 * dt_chem)
            val += chem_hum
        # 3. "Glup" sordo en salmuera (0.50 a 0.78s, pitch cayendo)
        if 0.50 <= t < 0.78:
            dt_glup = t - 0.50
            glup_freq = 280 - 160 * (dt_glup / 0.28)
            glup = math.sin(2 * math.pi * glup_freq * dt_glup) * 0.45 * math.sin(math.pi * (dt_glup / 0.28))
            val += glup
        samples.append(val)
    return samples

def synth_cristalizacion_timelapse(duration=0.85):
    """Silbido de time-lapse rápido + crujido mineral cristalizándose + tono ambiental."""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        val = 0.0
        # 1. Silbido de aceleración de tiempo "shhh-tick-tick" (0.0 a 0.45s)
        if t < 0.45:
            p_tl = t / 0.45
            sweep = math.sin(2 * math.pi * (350 + 600 * p_tl) * t) * 0.25 + (random.random() * 2 - 1) * 0.15
            ticks = math.sin(2 * math.pi * 28 * t) > 0.6
            val += (sweep + (0.2 if ticks else 0.0)) * math.sin(math.pi * p_tl)
        # 2. Crujido mineral cristalizándose (0.40 a 0.75s, ráfagas crujientes)
        if 0.40 <= t < 0.75:
            dt_cr = t - 0.40
            crack = (random.random() * 2 - 1) * 0.38 * (0.5 + 0.5 * math.sin(2 * math.pi * 32 * dt_cr)) * math.exp(-4 * dt_cr)
            mineral = math.sin(2 * math.pi * 1400 * dt_cr) * 0.2 * math.exp(-15 * dt_cr)
            val += crack + mineral
        # 3. Tono ambiental envolvente (0.55 a 0.85s)
        if t >= 0.55:
            dt_amb = t - 0.55
            ambient = (math.sin(2 * math.pi * 440 * dt_amb) * 0.25 +
                       math.sin(2 * math.pi * 554.37 * dt_amb) * 0.18 +
                       math.sin(2 * math.pi * 659.25 * dt_amb) * 0.12) * math.exp(-3.5 * dt_amb)
            val += ambient
        samples.append(val)
    return samples

def synth_flamencos_orquesta_cierre(duration=0.95):
    """Graznidos de flamencos + brisa cálida + acorde orquestal emotivo de cierre."""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        val = 0.0
        # 1. Graznido cálido de flamenco menor (0.0 a 0.40s, bocinazo nasal dulce)
        if t < 0.40:
            dt_fl = t
            honk_freq = 520 + math.sin(2 * math.pi * 14 * dt_fl) * 45
            honk = (math.sin(2 * math.pi * honk_freq * dt_fl) * 0.35 +
                    math.sin(2 * math.pi * (honk_freq * 1.5) * dt_fl) * 0.2) * math.sin(math.pi * (dt_fl / 0.40))
            val += honk
        # 2. Brisa cálida (0.20 a 0.70s)
        if 0.20 <= t < 0.70:
            breeze = (random.random() * 2 - 1) * 0.12 * math.sin(math.pi * ((t - 0.20) / 0.50))
            val += breeze
        # 3. Acorde orquestal emotivo de cierre (F mayor: F4, A4, C5, F5 a partir de 0.45s)
        if t >= 0.45:
            dt_ch = t - 0.45
            f_notes = [349.23, 440.00, 523.25, 698.46]
            chord = sum(math.sin(2 * math.pi * f_n * dt_ch) * 0.18 for f_n in f_notes) * math.exp(-3.5 * dt_ch)
            val += chord
        samples.append(val)
    return samples

def synth_enjambre_patitas_suspenso(duration=0.85):
    """Murmullo continuo de miles de patas + crujido de hojarasca + redoble de suspenso."""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        val = 0.0
        # 1. Murmullo y crujido rítmico de patitas marchando (16 Hz)
        swarm_gate = 0.6 + 0.4 * math.sin(2 * math.pi * 16 * t)
        patter = (random.random() * 2 - 1) * 0.35 * swarm_gate
        rustle = math.sin(2 * math.pi * 950 * t) * 0.15 * swarm_gate
        val += (patter + rustle) * math.sin(math.pi * (t / duration))
        # 2. Redoble sordo y misterioso de timbal bajo (0.35 a 0.85s)
        if t >= 0.35:
            dt_r = t - 0.35
            timpani = (math.sin(2 * math.pi * 65 * dt_r) * 0.45 +
                       math.sin(2 * math.pi * 130 * dt_r) * 0.2) * math.exp(-3.5 * dt_r)
            val += timpani
        samples.append(val)
    return samples

def synth_patitas_motor_quejido(duration=0.75):
    """Traqueteo de patitas aceleradas tipo motor de juguete + siseo vegetal + quejido cómico."""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        val = 0.0
        # 1. Traqueteo a 22 Hz tipo motor de patitas (0.0 a 0.50s)
        if t < 0.50:
            clack = (math.sin(2 * math.pi * 22 * t) > 0.3) * (random.random() * 2 - 1) * 0.45
            buzz = math.sin(2 * math.pi * 320 * t) * 0.2
            val += (clack + buzz) * (1 - t / 0.50)
        # 2. Quejido cómico del Stickman (0.38 a 0.75s, "¡ugh-ay!")
        if t >= 0.38:
            dt_q = t - 0.38
            p_q = dt_q / 0.37
            freq_q = 550 - 220 * math.pow(p_q, 1.5)
            grunt = (math.sin(2 * math.pi * freq_q * dt_q) * 0.35 +
                     math.sin(2 * math.pi * (freq_q * 1.5) * dt_q) * 0.18) * math.sin(math.pi * p_q)
            val += grunt
        samples.append(val)
    return samples

def synth_linterna_antena_campana(duration=0.80):
    """Clic seco de linterna + zumbido elástico de antena + campana científica."""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        val = 0.0
        # 1. Clic metálico táctico de linterna (t=0.03 a 0.10s)
        if 0.03 <= t < 0.10:
            dt_c = t - 0.03
            val += (math.sin(2 * math.pi * 2400 * dt_c) * 0.45 + (random.random() * 2 - 1) * 0.3) * math.exp(-45 * dt_c)
        # 2. Zumbido elástico de antena "boing-boing" (0.12 a 0.45s)
        if 0.12 <= t < 0.45:
            dt_a = t - 0.12
            boing_freq = 460 + math.sin(2 * math.pi * 18 * dt_a) * 80
            boing = math.sin(2 * math.pi * boing_freq * dt_a) * 0.35 * math.exp(-7.0 * dt_a)
            val += boing
        # 3. Tono cristalino de campana explicativa (0.40 a 0.80s, A6 1760 Hz)
        if t >= 0.40:
            dt_b = t - 0.40
            chime = (math.sin(2 * math.pi * 1760 * dt_b) * 0.35 +
                     math.sin(2 * math.pi * 3520 * dt_b) * 0.15) * math.exp(-5.0 * dt_b)
            val += chime
        samples.append(val)
    return samples

def synth_sniff_radar_feromona(duration=0.85):
    """Dos aspiraciones de olfato ("sniff-sniff") + pitidos de radar ("blip-blip")."""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    sniff_times = [0.05, 0.26]
    radar_times = [0.48, 0.68]
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        val = 0.0
        # Aspiración de aire nasal
        for st in sniff_times:
            if st <= t < st + 0.14:
                dt_s = t - st
                sniff = (random.random() * 2 - 1) * 0.38 * math.sin(math.pi * (dt_s / 0.14))
                val += sniff
        # Radar biológico químico
        for rt in radar_times:
            if rt <= t < rt + 0.10:
                dt_r = t - rt
                blip = math.sin(2 * math.pi * 1046.50 * dt_r) * 0.35 * math.sin(math.pi * (dt_r / 0.10))
                val += blip
        samples.append(val)
    return samples

def synth_bucle_infinito_glitch(duration=0.90):
    """Cinta sin fin acelerando + bucle de software digital glitch + redoble tenso."""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        val = 0.0
        # 1. Sweep ascendente de bucle sin fin (0.0 a 0.50s)
        if t < 0.50:
            p1 = t / 0.50
            sweep_f = 280 + 1100 * math.pow(p1, 1.6)
            val += math.sin(2 * math.pi * sweep_f * t) * 0.35 * math.sin(math.pi * p1)
        # 2. Glitch digital entrecortado tipo bug de software (0.45 a 0.90s)
        if t >= 0.45:
            dt_g = t - 0.45
            glitch_clock = math.sin(2 * math.pi * 32 * dt_g) > 0.0
            glitch_tone = math.sin(2 * math.pi * (880 if glitch_clock else 440) * dt_g) * 0.35
            noise = (random.random() * 2 - 1) * 0.2 if glitch_clock else 0.0
            val += (glitch_tone + noise) * (1 - dt_g / 0.45)
        samples.append(val)
    return samples

def synth_atomizador_espuma_spray(duration=0.80):
    """Triple disparo de spray atomizador a presión ("psssht") + efervescencia de espuma."""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    spray_times = [0.06, 0.28, 0.50]
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        val = 0.0
        # 3 disparos de spray a presión
        for st in spray_times:
            if st <= t < st + 0.15:
                dt_sp = t - st
                spray = (random.random() * 2 - 1) * 0.45 * math.sin(math.pi * (dt_sp / 0.15))
                hiss = math.sin(2 * math.pi * 3200 * dt_sp) * 0.15 * math.exp(-12 * dt_sp)
                val += spray + hiss
        # Efervescencia suave de espuma jabonosa
        if t >= 0.55:
            dt_f = t - 0.55
            fizz = (random.random() * 2 - 1) * 0.18 * math.exp(-5.0 * dt_f)
            val += fizz
        samples.append(val)
    return samples

def synth_dispersion_hojarasca_triunfo(duration=0.95):
    """Dispersión viva de hojarasca + suspiro "fiuuu" + golpe sordo acolchado + acorde triunfal."""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        val = 0.0
        # 1. Hojarasca dispersándose (0.0 a 0.35s)
        if t < 0.35:
            rustle = (random.random() * 2 - 1) * 0.3 * math.sin(math.pi * (t / 0.35))
            val += rustle
        # 2. Suspiro de alivio "fiuuu" (0.15 a 0.45s)
        if 0.15 <= t < 0.45:
            dt_s = t - 0.15
            sigh_f = 650 - 320 * (dt_s / 0.30)
            val += math.sin(2 * math.pi * sigh_f * dt_s) * 0.25 * math.sin(math.pi * (dt_s / 0.30))
        # 3. Golpe sordo al sentarse thud (0.42 a 0.60s)
        if 0.42 <= t < 0.60:
            dt_th = t - 0.42
            val += math.sin(2 * math.pi * 75 * dt_th) * 0.5 * math.exp(-25 * dt_th)
        # 4. Acorde orquestal triunfal (G mayor: G4, B4, D5, G5 a partir de 0.58s)
        if t >= 0.58:
            dt_ch = t - 0.58
            g_notes = [392.00, 493.88, 587.33, 783.99]
            chord = sum(math.sin(2 * math.pi * gn * dt_ch) * 0.18 for gn in g_notes) * math.exp(-4.5 * dt_ch)
            val += chord
        samples.append(val)
    return samples

def synth_calor_tos_pulmon_ahogo(duration=0.85):
    """Calor sofocante + inhalación forzada + tos y ahogo húmedo + golpe de misterio."""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        val = 0.0
        # 1. Inhalación de aire hirviente con siseo áspero (0.0 a 0.28s)
        if t < 0.28:
            p_in = t / 0.28
            inhale = (random.random() * 2 - 1) * 0.35 * math.sin(math.pi * p_in)
            heat_drone = math.sin(2 * math.pi * 110 * t) * 0.15
            val += inhale + heat_drone
        # 2. Tos y ahogo pulmonar húmedo (0.28 a 0.65s, dos golpes de tos)
        for c_t in [0.30, 0.46]:
            if c_t <= t < c_t + 0.14:
                dt_c = t - c_t
                cough = (random.random() * 2 - 1) * 0.45 * math.exp(-25 * dt_c)
                throat = math.sin(2 * math.pi * 280 * dt_c) * 0.3 * math.exp(-20 * dt_c)
                val += cough + throat
        # 3. Sub-bajo sordo de misterio tenso (0.50 a 0.85s)
        if t >= 0.50:
            dt_sub = t - 0.50
            sub = (math.sin(2 * math.pi * 52 * dt_sub) * 0.5 +
                   math.sin(2 * math.pi * 104 * dt_sub) * 0.2) * math.exp(-4.0 * dt_sub)
            val += sub
        samples.append(val)
    return samples

def synth_cueva_eco_cristales_shimmer(duration=0.80):
    """Ecos lejanos de caverna + pasos sobre piedra mineral + brillo cristalino limpio."""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    step_times = [0.12, 0.36]
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        val = 0.0
        # Ecos de caverna ambiental
        reverb_drone = (math.sin(2 * math.pi * 85 * t) * 0.18 + (random.random() * 2 - 1) * 0.06) * math.sin(math.pi * (t / duration))
        val += reverb_drone
        # Pasos secos sobre selenita
        for st in step_times:
            if st <= t < st + 0.12:
                dt_st = t - st
                step = math.sin(2 * math.pi * 320 * dt_st) * 0.35 * math.exp(-35 * dt_st)
                val += step
        # Shimmer cristalino (2400 Hz y armónicos a partir de 0.30s)
        if t >= 0.30:
            dt_sh = t - 0.30
            shimmer = (math.sin(2 * math.pi * 2489 * dt_sh) * 0.22 +
                       math.sin(2 * math.pi * 4978 * dt_sh) * 0.12) * math.exp(-5.0 * dt_sh)
            val += shimmer
        samples.append(val)
    return samples

def synth_magma_submarino_reloj(duration=0.90):
    """Borboteo submarino + zumbido tectónico de magma + reloj mecánico acelerado."""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        val = 0.0
        # 1. Zumbido tectónico subacuático (55 Hz + modulación)
        tectonic = (math.sin(2 * math.pi * 55 * t) * 0.45 +
                    math.sin(2 * math.pi * 110 * t) * 0.2) * math.sin(math.pi * (t / duration))
        bubble = math.sin(2 * math.pi * (220 + math.sin(2 * math.pi * 12 * t) * 60) * t) * 0.15
        val += tectonic + bubble
        # 2. Reloj mecánico acelerado en time-lapse (0.30 a 0.90s, ticks cada 0.06s)
        if t >= 0.30:
            dt_cl = t - 0.30
            period = 0.065
            phase = dt_cl % period
            if phase < 0.02:
                tick = (math.sin(2 * math.pi * 1800 * phase) * 0.3 + (random.random() * 2 - 1) * 0.2) * math.exp(-80 * phase)
                val += tick * (1 - dt_cl / 0.60)
        samples.append(val)
    return samples

def synth_bomba_drenaje_vapor_alarma(duration=0.80):
    """Succión de bombas industriales masivas + siseo de vapor + alarma de calor."""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        val = 0.0
        # 1. Motor de bomba extractora y succión (0.0 a 0.55s)
        if t < 0.55:
            p_p = t / 0.55
            pump_freq = 75 + 45 * p_p
            pump = (math.sin(2 * math.pi * pump_freq * t) * 0.4 +
                    math.sin(2 * math.pi * (pump_freq * 2) * t) * 0.2) * math.sin(math.pi * p_p)
            val += pump
        # 2. Siseo de vapor a alta presión (0.25 a 0.65s)
        if 0.25 <= t < 0.65:
            dt_v = t - 0.25
            steam = (random.random() * 2 - 1) * 0.35 * math.exp(-5.0 * dt_v)
            val += steam
        # 3. Alarma industrial periódica (dos beeps de advertencia)
        for al_t in [0.45, 0.65]:
            if al_t <= t < al_t + 0.08:
                dt_a = t - al_t
                alarm = math.sin(2 * math.pi * 1350 * dt_a) * 0.4 * math.sin(math.pi * (dt_a / 0.08))
                val += alarm
        samples.append(val)
    return samples

def synth_lata_goteo_latido_pulmon(duration=0.85):
    """Apertura de lata fría ("k-tshhh") + goteo continuo + latidos cardíacos."""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    drip_times = [0.22, 0.44, 0.66]
    heart_times = [0.35, 0.42, 0.68, 0.75]
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        val = 0.0
        # 1. Apertura de lata metálica ("k-tshhh", 0.03 a 0.18s)
        if 0.03 <= t < 0.18:
            dt_can = t - 0.03
            can_snap = math.sin(2 * math.pi * 850 * dt_can) * 0.4 * math.exp(-35 * dt_can)
            fizz = (random.random() * 2 - 1) * 0.35 * math.exp(-20 * dt_can)
            val += can_snap + fizz
        # 2. Gotas cayendo ("drip, drip")
        for dt_t in drip_times:
            if dt_t <= t < dt_t + 0.12:
                dt_d = t - dt_t
                drip_freq = 950 + 400 * (dt_d / 0.12)
                drip = math.sin(2 * math.pi * drip_freq * dt_d) * 0.35 * math.exp(-28 * dt_d)
                val += drip
        # 3. Latidos del corazón "pum-pum"
        for ht in heart_times:
            if ht <= t < ht + 0.09:
                dt_h = t - ht
                thump = math.sin(2 * math.pi * 65 * dt_h) * 0.45 * math.sin(math.pi * (dt_h / 0.09))
                val += thump
        samples.append(val)
    return samples

def synth_traje_hielo_rescate_oxigeno(duration=0.90):
    """Cuenta regresiva de peligro + clic hermético + inhalación helada de alivio."""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        val = 0.0
        # 1. Beeps rápidos de cuenta regresiva límite (0.05 a 0.35s)
        for b_t in [0.06, 0.18, 0.30]:
            if b_t <= t < b_t + 0.06:
                dt_b = t - b_t
                beep = math.sin(2 * math.pi * 1600 * dt_b) * 0.3 * math.sin(math.pi * (dt_b / 0.06))
                val += beep
        # 2. Clic hermético de manguera de oxígeno ("clic-fssshh", 0.38 a 0.58s)
        if 0.38 <= t < 0.58:
            dt_c = t - 0.38
            click = math.sin(2 * math.pi * 2200 * dt_c) * 0.4 * math.exp(-50 * dt_c)
            flow = (random.random() * 2 - 1) * 0.3 * math.exp(-10 * dt_c)
            val += click + flow
        # 3. Inhalación profunda de aire frío y puro (0.55 a 0.90s)
        if t >= 0.55:
            dt_o = t - 0.55
            p_o = dt_o / 0.35
            frost_air = (random.random() * 2 - 1) * 0.25 * math.sin(math.pi * p_o)
            hum_cold = math.sin(2 * math.pi * 380 * dt_o) * 0.15 * math.exp(-2.5 * dt_o)
            val += frost_air + hum_cold
        samples.append(val)
    return samples

def synth_escotilla_mina_portazo_triunfo(duration=0.95):
    """Campanilleo mineral + portazo masivo de escotilla de acero ("CLANG-SHUT") + fanfarria orquestal."""
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        val = 0.0
        # 1. Pasos y brillo cristalino inicial (0.0 a 0.35s)
        if t < 0.35:
            shimmer = (math.sin(2 * math.pi * 2200 * t) * 0.25 +
                       math.sin(2 * math.pi * 3300 * t) * 0.12) * math.sin(math.pi * (t / 0.35))
            val += shimmer
        # 2. Portazo seco y pesado de escotilla metálica ("CLANG-SHUT", 0.32 a 0.70s)
        if 0.32 <= t < 0.70:
            dt_cl = t - 0.32
            clang = (math.sin(2 * math.pi * 180 * dt_cl) * 0.6 +
                     math.sin(2 * math.pi * 540 * dt_cl) * 0.3 +
                     (random.random() * 2 - 1) * 0.45) * math.exp(-18 * dt_cl)
            sub_reverb = math.sin(2 * math.pi * 48 * dt_cl) * 0.5 * math.exp(-8 * dt_cl)
            val += clang + sub_reverb
        # 3. Acorde orquestal triunfal dramático (D mayor: D4, F#4, A4, D5 a partir de 0.55s)
        if t >= 0.55:
            dt_ch = t - 0.55
            d_notes = [293.66, 369.99, 440.00, 587.33]
            chord = sum(math.sin(2 * math.pi * dn * dt_ch) * 0.18 for dn in d_notes) * math.exp(-3.5 * dt_ch)
            val += chord
        samples.append(val)
    return samples

def synth_radio_static(duration=1.2):
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    b0 = 0.0
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        noise = (random.random() * 2.0 - 1.0)
        # Low-pass filter for analog warmth
        b0 = 0.82 * b0 + 0.18 * noise
        # Modulated static waves
        mod = 0.5 + 0.5 * math.sin(2 * math.pi * 3.5 * t)
        # Crackles
        crackle = 2.5 if random.random() < 0.015 else 1.0
        env = math.sin(math.pi * (t / duration)) ** 0.5
        samples.append(b0 * mod * crackle * env * 0.7)
    return samples

def synth_spark_zap(duration=0.4):
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        p = t / duration
        freq = 3800 * math.exp(-12 * p) + 400 + (random.random() * 600 - 300)
        env = math.exp(-18 * p)
        spark = math.sin(2 * math.pi * freq * t) + (random.random() * 2.0 - 1.0) * 0.35
        samples.append(spark * env)
    return samples

def synth_casino_bell(duration=0.9):
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    notes = [1046.5, 1318.5, 1567.98, 2093.0] # C6, E6, G6, C7
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        val = 0.0
        for idx, freq in enumerate(notes):
            t_offset = idx * 0.08
            if t >= t_offset:
                dt = t - t_offset
                env = math.exp(-4.5 * dt)
                val += math.sin(2 * math.pi * freq * dt) * env * 0.25
        samples.append(val)
    return samples

def synth_oven_ding(duration=1.0):
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        env = math.exp(-3.2 * t)
        val = (math.sin(2 * math.pi * 1760 * t) * 0.6 +
               math.sin(2 * math.pi * 3520 * t) * 0.3 +
               math.sin(2 * math.pi * 5280 * t) * 0.1) * env
        samples.append(val)
    return samples

def synth_ice_drill(duration=1.2):
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        p = t / duration
        motor = math.sin(2 * math.pi * (280 + math.sin(t * 40) * 35) * t)
        crunch = (random.random() * 2.0 - 1.0) * (0.4 + 0.3 * math.sin(t * 60))
        env = min(1.0, t * 12) * min(1.0, (duration - t) * 6)
        samples.append((motor * 0.5 + crunch * 0.5) * env)
    return samples

def synth_soup_bubble(duration=0.8):
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    bubble_times = [0.05, 0.22, 0.45, 0.60]
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        val = 0.0
        for bt in bubble_times:
            if bt <= t < bt + 0.14:
                dt = t - bt
                p = dt / 0.14
                freq = 320 + 750 * (p ** 1.8)
                env = math.sin(math.pi * p)
                val += math.sin(2 * math.pi * freq * dt) * env * 0.6
        samples.append(val)
    return samples

def synth_dino_roar(duration=1.4):
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        p = t / duration
        freq = 95 + 40 * math.sin(math.pi * p) + (random.random() * 20 - 10)
        growl = math.sin(2 * math.pi * freq * t) + 0.4 * math.sin(2 * math.pi * (freq * 0.5) * t)
        distortion = math.tanh(growl * 2.5) * 0.7
        env = math.sin(math.pi * (p ** 0.65))
        samples.append(distortion * env)
    return samples

def synth_match_strike(duration=0.7):
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        val = 0.0
        # Raspado (t < 0.25)
        if t < 0.25:
            p = t / 0.25
            val += (random.random() * 2.0 - 1.0) * (1 - p * 0.5) * 0.8
        # Ignición / llama suave (t >= 0.25)
        else:
            dt = t - 0.25
            p2 = dt / 0.45
            hiss = (random.random() * 2.0 - 1.0) * math.exp(-5.0 * p2) * 0.6
            fizzle = math.sin(2 * math.pi * 420 * dt) * math.exp(-9.0 * p2) * 0.3
            val += hiss + fizzle
        samples.append(val)
    return samples

def synth_alarm_siren(duration=1.2):
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        mod = math.sin(2 * math.pi * 3.5 * t)
        freq = 650 + 280 * mod
        env = min(1.0, t * 10) * min(1.0, (duration - t) * 8)
        val = math.sin(2 * math.pi * freq * t) * env * 0.75
        samples.append(val)
    return samples

def synth_final_beeps(duration=2.5):
    samples = []
    n_samples = int(SAMPLE_RATE * duration)
    beep_starts = [0.2, 0.95, 1.7]
    beep_len = 0.24
    freq = 1420.4 # Frecuencia del hidrógeno
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        val = 0.0
        for bs in beep_starts:
            if bs <= t < bs + beep_len:
                dt = t - bs
                p = dt / beep_len
                # Ventana Hann suave sin clicks
                env = 0.5 * (1 - math.cos(2 * math.pi * p))
                val += math.sin(2 * math.pi * freq * dt) * env * 0.75
        samples.append(val)
    return samples

GENERADORES = {
    "radio_static": synth_radio_static,
    "spark_zap": synth_spark_zap,
    "casino_bell": synth_casino_bell,
    "oven_ding": synth_oven_ding,
    "ice_drill": synth_ice_drill,
    "soup_bubble": synth_soup_bubble,
    "dino_roar": synth_dino_roar,
    "match_strike": synth_match_strike,
    "alarm_siren": synth_alarm_siren,
    "final_beeps": synth_final_beeps,
    "calor_tos_pulmon_ahogo": synth_calor_tos_pulmon_ahogo,
    "cueva_eco_cristales_shimmer": synth_cueva_eco_cristales_shimmer,
    "magma_submarino_reloj": synth_magma_submarino_reloj,
    "bomba_drenaje_vapor_alarma": synth_bomba_drenaje_vapor_alarma,
    "lata_goteo_latido_pulmon": synth_lata_goteo_latido_pulmon,
    "traje_hielo_rescate_oxigeno": synth_traje_hielo_rescate_oxigeno,
    "escotilla_mina_portazo_triunfo": synth_escotilla_mina_portazo_triunfo,
    "enjambre_patitas_suspenso": synth_enjambre_patitas_suspenso,
    "patitas_motor_quejido": synth_patitas_motor_quejido,
    "linterna_antena_campana": synth_linterna_antena_campana,
    "sniff_radar_feromona": synth_sniff_radar_feromona,
    "bucle_infinito_glitch": synth_bucle_infinito_glitch,
    "atomizador_espuma_spray": synth_atomizador_espuma_spray,
    "dispersion_hojarasca_triunfo": synth_dispersion_hojarasca_triunfo,
    "viento_sal_suspenso": synth_viento_sal_suspenso,
    "golpe_ceramica_piedra": synth_golpe_ceramica_piedra,
    "siseo_alerta_quimica": synth_siseo_alerta_quimica,
    "retumbo_volcan_egipcio": synth_retumbo_volcan_egipcio,
    "impacto_espejo_agua_splat": synth_impacto_espejo_agua_splat,
    "cristalizacion_timelapse": synth_cristalizacion_timelapse,
    "flamencos_orquesta_cierre": synth_flamencos_orquesta_cierre,
    "auto_rewind_rueda": synth_auto_rewind_rueda,
    "pausa_proyector_cine": synth_pausa_proyector_cine,
    "obturador_camara_reloj": synth_obturador_camara_reloj,
    "helicoptero_aspas_reversa": synth_helicoptero_aspas_reversa,
    "camara_beep_congelado": synth_camara_beep_congelado,
    "parpadeo_estroboscopico": synth_parpadeo_estroboscopico,
    "mareo_estrellas_thud": synth_mareo_estrellas_thud,
    "plastico_crujiente_disolucion": synth_plastico_crujiente_disolucion,
    "placa_petri_hallazgo": synth_placa_petri_hallazgo,
    "bacteria_chomp_plastico": synth_bacteria_chomp_plastico,
    "tijeras_petasa_snip": synth_tijeras_petasa_snip,
    "recarga_metabolica_powerup": synth_recarga_metabolica_powerup,
    "aspiradora_enzima_vrooom": synth_aspiradora_enzima_vrooom,
    "eructo_paseo_ecologico": synth_eructo_paseo_ecologico,
    "fuego_azul_presion": synth_fuego_azul_presion,
    "tos_mascara_antigas": synth_tos_mascara_antigas,
    "subsuelo_olla_presion": synth_subsuelo_olla_presion,
    "soplete_ignicion_fwoosh": synth_soplete_ignicion_fwoosh,
    "goteo_azufre_crepitar": synth_goteo_azufre_crepitar,
    "amanecer_timelapse_fumarola": synth_amanecer_timelapse_fumarola,
    "remate_volcan_azul_soplete": synth_remate_volcan_azul_soplete,
    "viento_misterio_penitentes": synth_viento_misterio_penitentes,
    "resbalon_hielo_crack": synth_resbalon_hielo_crack,
    "fosforo_sublimacion_tsss": synth_fosforo_sublimacion_tsss,
    "diagrama_sublimacion_campana": synth_diagrama_sublimacion_campana,
    "timelapse_erosion_solar": synth_timelapse_erosion_solar,
    "campana_monasterio_misterio": synth_campana_monasterio_misterio,
    "remate_andino_viento": synth_remate_andino_viento,
    "gota_espacial_bloop": synth_gota_espacial_bloop,
    "membrana_elastica_agua": synth_membrana_elastica_agua,
    "cohesion_molecular": synth_cohesion_molecular,
    "inmersion_pececillo": synth_inmersion_pececillo,
    "succion_popote_adhesion": synth_succion_popote_adhesion,
    "mascara_agua_splat": synth_mascara_agua_splat,
    "toalla_secado_espacial": synth_toalla_secado_espacial,
    "empuje_fotones": synth_empuje_fotones,
    "rebote_fotones": synth_rebote_fotones,
    "vacio_espacial": synth_vacio_espacial,
    "despliegue_vela": synth_despliegue_vela,
    "rebote_doble_impulso": synth_rebote_doble_impulso,
    "aceleracion_cosmica": synth_aceleracion_cosmica,
    "surf_cosmico": synth_surf_cosmico,
    "borehole_laser": synth_borehole_laser,
    "eco_laser_antartida": synth_borehole_laser,
    "tape_measure": synth_tape_measure,
    "cinta_metrica": synth_tape_measure,
    "rhythmic_pews": synth_rhythmic_pews,
    "laser_ritmico": synth_rhythmic_pews,
    "ice_thump": synth_ice_thump_vibration,
    "golpe_hielo": synth_ice_thump_vibration,
    "dispersion_glissando": synth_dispersion_glissando,
    "glissando_dispersion": synth_dispersion_glissando,
    "scifi_double_pew": synth_scifi_double_pew,
    "laser_doble": synth_scifi_double_pew,
    "colossal_laser_echo": synth_colossal_laser_echo,
    "laser_colosal": synth_colossal_laser_echo,
    "laser": synth_laser,
    "heartbeat": synth_heartbeat,
    "latido": synth_heartbeat,
    "glitch": synth_glitch,
    "alarm": synth_alarm,
    "alarma": synth_alarm,
    "impact": synth_sub_impact,
    "sub_impact": synth_sub_impact,
    "sparkle": synth_sparkle,
    "destello": synth_sparkle,
    "click": synth_click,
    "clang": synth_metal_clang,
    "metal_clang": synth_metal_clang,
    "boing": synth_boing,
    "rebote": synth_boing,
    "thermal_hiss": synth_thermal_hiss,
    "siseo": synth_thermal_hiss,
    "tension_creak": synth_tension_creak,
    "tension": synth_tension_creak,
    "snap": synth_glass_snap,
    "chasquido": synth_glass_snap,
    "shatter_boom": synth_glass_shatter_boom,
    "pulverizacion": synth_glass_shatter_boom,
    "sonar_pulse": synth_sonar_pulse,
    "sonar": synth_sonar_pulse,
    "water_splash": synth_water_splash,
    "splash": synth_water_splash,
    "ultrasound_sweep": synth_ultrasound_sweep,
    "ultrasonido": synth_ultrasound_sweep,
    "cavitation_thud": synth_cavitation_thud,
    "cavitacion": synth_cavitation_thud,
    "plasma_burst": synth_plasma_burst,
    "plasma": synth_plasma_burst,
    "ambient_chime": synth_ambient_chime,
    "campana_cosmica": synth_ambient_chime,
}

def guardar_wav(ruta_wav, samples, volumen=0.8):
    os.makedirs(os.path.dirname(os.path.abspath(ruta_wav)), exist_ok=True)
    # Normalizar si hay picos
    max_val = max(abs(s) for s in samples) if samples else 1.0
    norm_factor = (32767 * volumen) / max(max_val, 1e-5)
    
    with wave.open(ruta_wav, "wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2) # 16-bit
        wav.setframerate(SAMPLE_RATE)
        frames = bytearray()
        for s in samples:
            val_int = int(max(-32767, min(32767, s * norm_factor)))
            frames.extend(struct.pack("<h", val_int))
        wav.writeframes(frames)
    print(f"[SFX GENERADO] Guardado exitosamente en: {ruta_wav} ({len(samples)/SAMPLE_RATE:.2f}s)")

def main():
    if len(sys.argv) < 3:
        print("Uso: python scripts/generar_sfx.py <nombre_archivo_o_ruta> <tipo> [duracion_seg]")
        print(f"Tipos disponibles: {', '.join(GENERADORES.keys())}")
        sys.exit(1)
        
    archivo = sys.argv[1]
    tipo = sys.argv[2].lower()
    duracion = float(sys.argv[3]) if len(sys.argv) > 3 else None
    
    if not archivo.endswith(".wav"):
        archivo += ".wav"
        
    ruta_completa = archivo if ("/" in archivo or "\\" in archivo) else os.path.join("public", "sfx", archivo)
    
    if tipo not in GENERADORES:
        print(f"Error: Tipo '{tipo}' desconocido. Opciones: {list(GENERADORES.keys())}")
        sys.exit(1)
        
    fn = GENERADORES[tipo]
    samples = fn(duracion) if duracion else fn()
    guardar_wav(ruta_completa, samples)

if __name__ == "__main__":
    main()
