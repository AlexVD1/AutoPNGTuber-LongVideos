"""Módulo de normalización fonética de cifras y abreviaturas en español para TTS.

Convierte números arábigos, años, decimales, unidades y porcentajes a palabras
en español para garantizar una dicción perfecta y articulada en modelos de TTS neural
(Chatterbox, XTTS, etc.) y una alineación exacta palabra por palabra con Whisper.
"""

from __future__ import annotations

import re

UNIDADES = {
    0: "cero",
    1: "uno",
    2: "dos",
    3: "tres",
    4: "cuatro",
    5: "cinco",
    6: "seis",
    7: "siete",
    8: "ocho",
    9: "nueve",
}

ESPECIALES_10_29 = {
    10: "diez",
    11: "once",
    12: "doce",
    13: "trece",
    14: "catorce",
    15: "quince",
    16: "dieciséis",
    17: "diecisiete",
    18: "dieciocho",
    19: "diecinueve",
    20: "veinte",
    21: "veintiuno",
    22: "veintidós",
    23: "veintitrés",
    24: "veinticuatro",
    25: "veinticinco",
    26: "veintiséis",
    27: "veintisiete",
    28: "veintiocho",
    29: "veintinueve",
}

DECENAS = {
    30: "treinta",
    40: "cuarenta",
    50: "cincuenta",
    60: "sesenta",
    70: "setenta",
    80: "ochenta",
    90: "noventa",
}

CENTENAS = {
    100: "cien",
    200: "doscientos",
    300: "trescientos",
    400: "cuatrocientos",
    500: "quinientos",
    600: "seiscientos",
    700: "setecientos",
    800: "ochocientos",
    900: "novecientos",
}


def numero_a_palabras(n: int) -> str:
    """Convierte un entero no negativo a texto en español."""
    if n < 0:
        return f"menos {numero_a_palabras(-n)}"
    if n <= 9:
        return UNIDADES[n]
    if n in ESPECIALES_10_29:
        return ESPECIALES_10_29[n]
    if n < 100:
        d = (n // 10) * 10
        u = n % 10
        if u == 0:
            return DECENAS[d]
        return f"{DECENAS[d]} y {UNIDADES[u]}"
    if n == 100:
        return "cien"
    if n < 1000:
        c = (n // 100) * 100
        resto = n % 100
        nombre_c = "ciento" if c == 100 else CENTENAS[c]
        if resto == 0:
            return nombre_c
        return f"{nombre_c} {numero_a_palabras(resto)}"
    if n < 1_000_000:
        miles = n // 1000
        resto = n % 1000
        if miles == 1:
            texto_miles = "mil"
        else:
            texto_miles = f"{numero_a_palabras(miles)} mil"
        if resto == 0:
            return texto_miles
        return f"{texto_miles} {numero_a_palabras(resto)}"
    if n < 1_000_000_000_000:
        millones = n // 1_000_000
        resto = n % 1_000_000
        if millones == 1:
            texto_millones = "un millón"
        else:
            texto_millones = f"{numero_a_palabras(millones)} millones"
        if resto == 0:
            return texto_millones
        return f"{texto_millones} {numero_a_palabras(resto)}"
    return str(n)


UNIDADES_ABREVIADAS = [
    (r"\bMHz\b", "megahercios"),
    (r"\bmhz\b", "megahercios"),
    (r"\bGHz\b", "gigahercios"),
    (r"\bghz\b", "gigahercios"),
    (r"\bkHz\b", "kilohercios"),
    (r"\bkhz\b", "kilohercios"),
    (r"\bHz\b", "hercios"),
    (r"\bhz\b", "hercios"),
    (r"\bkm/h\b", "kilómetros por hora"),
    (r"\bkm/s\b", "kilómetros por segundo"),
    (r"\bkm\b", "kilómetros"),
    (r"\bcm³\b", "centímetros cúbicos"),
    (r"\bcm3\b", "centímetros cúbicos"),
    (r"\bmm³\b", "milímetros cúbicos"),
    (r"\bm³\b", "metros cúbicos"),
    (r"\bcm\b", "centímetros"),
    (r"\bmm\b", "milímetros"),
    (r"\bkg\b", "kilogramos"),
    (r"\bseg\b", "segundos"),
    (r"%", " por ciento"),
    (r"°C\b", " grados celsius"),
    (r"°\b", " grados"),
    (r"\bpor ciento de [cC]\b", "por ciento de la velocidad de la luz"),
    (r"\bde [cC]\b", "de la velocidad de la luz"),
]


def normalizar_cifras_espanol(texto: str) -> str:
    """Normaliza de forma integral cualquier cifra, decimal, año o abreviatura en español.

    Ejemplos:
      '1420 megahercios' -> 'mil cuatrocientos veinte megahercios'
      'agosto de 1977' -> 'agosto de mil novecientos setenta y siete'
      '30 veces' -> 'treinta veces'
      '72 segundos' -> 'setenta y dos segundos'
      '1420.4 MHz' -> 'mil cuatrocientos veinte punto cuatro megahercios'
      '100%' -> 'cien por ciento'
    """
    if not texto:
        return ""

    resultado = texto

    # 1. Expandir unidades técnicas comunes
    for patron, reemplazo in UNIDADES_ABREVIADAS:
        resultado = re.sub(patron, reemplazo, resultado)

    # 2. Números formateados con separador de miles (ej. 300.000 o 1.500.000)
    # DEBE EJECUTARSE ANTES de los decimales para evitar tratar 300.000 como decimal
    def _reemplazar_miles(match: re.Match) -> str:
        num_str = match.group(0).replace(".", "").replace(",", "")
        try:
            val = int(num_str)
            return numero_a_palabras(val)
        except ValueError:
            return match.group(0)

    resultado = re.sub(r"\b\d{1,3}(?:\.\d{3})+\b", _reemplazar_miles, resultado)

    # 3. Decimales (ej. 1420.4 o 3.14 o 0,5 o 1,5)
    def _reemplazar_decimal(match: re.Match) -> str:
        entero_str = match.group(1)
        sep = match.group(2)
        dec_str = match.group(3)
        try:
            entero_num = int(entero_str)
            entero_txt = numero_a_palabras(entero_num)
            dec_num = int(dec_str)
            dec_txt = numero_a_palabras(dec_num)
            conector = "punto" if sep == "." else "coma"
            return f"{entero_txt} {conector} {dec_txt}"
        except ValueError:
            return match.group(0)

    resultado = re.sub(r"\b(\d+)([.,])(\d+)\b", _reemplazar_decimal, resultado)

    # 4. Enteros independientes (ej. 1977, 1420, 30, 72)
    def _reemplazar_entero(match: re.Match) -> str:
        num_str = match.group(0)
        try:
            val = int(num_str)
            return numero_a_palabras(val)
        except ValueError:
            return match.group(0)

    resultado = re.sub(r"\b\d+\b", _reemplazar_entero, resultado)

    # Limpiar espacios múltiples resultantes
    resultado = re.sub(r"\s+", " ", resultado).strip()
    return resultado
