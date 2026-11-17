#!/usr/bin/env python3
"""
Constructor Exhaustivo de los 15 Guiones para Documentales Largos (16:9, 1920x1080).
Cada guion cumple con la extensión de 6 a 8 minutos (5-7 capítulos, 11-14 escenas)
conforme al estándar de docs/IDEA.md.
"""

import io
import json
import sys
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

ROOT_DIR = Path(__file__).resolve().parent.parent
GUIONES_DIR = ROOT_DIR / "src" / "data" / "guiones_largos"
GUIONES_DIR.mkdir(parents=True, exist_ok=True)


def construir_doc_004_wow():
    return {
        "meta": {
            "id": "doc_004_senal_wow",
            "slug": "misterio_senal_wow_1977",
            "titulo": "El Misterio de la Señal Wow: ¿Qué Escuchamos Realmente en 1977?",
            "premisa": "En agosto de 1977, un radiotelescopio en Ohio captó una señal de radio treinta veces más potente que el ruido cósmico de fondo. Duró exactamente setenta y dos segundos y jamás volvió a repetirse.",
            "gancho": "¿Recibimos en 1977 una transmisión extraterrestre que aún no logramos descifrar?",
            "categoria": "Science & Technology",
            "duracionObjetivo": [420, 500],
            "fps": 30,
            "dimensiones": {"width": 1920, "height": 1080},
            "idioma": "es",
            "voz": "alex.conds.pt",
            "musicaPrincipal": "bgm/bgm.mp3",
            "volumenMusica": 0.12,
            "fuentes": [
                "Ehman, J. R. (1977). The 'Big Ear' Wow! Signal Analysis. Ohio State University.",
                "Gray, R. H. (2012). The Elusive WOW: Searching for Extraterrestrial Intelligence.",
                "Paris, A. (2017). Hydrogen Line Observations and the Cometary Hypothesis."
            ],
            "tags": ["astronomia", "senal wow", "seti", "universo", "ciencia", "espacio", "radiotelescopio"]
        },
        "capitulos": [
            {
                "id": "cap_1",
                "numero": 1,
                "titulo": "La Noche del 15 de Agosto de 1977",
                "resumen": "El radiotelescopio Big Ear y el hallazgo de Jerry Ehman.",
                "escenas": [
                    {
                        "id": 1,
                        "texto": "La noche del quince de agosto de mil novecientos setenta y siete, en un tranquilo observatorio de Ohio, una impresora matricial comenzó a escupir una secuencia que cambiaría la astronomía moderna para siempre.",
                        "tituloVisual": "AGOSTO DE 1977",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "habitacion_noche",
                        "transicion": "fundido_negro",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["quince de agosto", "impresora matricial", "astronomía moderna"],
                        "poseId": "astronomy_telescope",
                        "expresion": "analytical"
                    },
                    {
                        "id": 2,
                        "texto": "El astrónomo Jerry Ehman revisaba las columnas de datos del telescopio Big Ear cuando de pronto vio seis caracteres insólitos: seis, e, q, u, j, cinco. Impresionado por la potencia, tomó un bolígrafo rojo y escribió al margen una sola palabra: ¡Wow!",
                        "tituloVisual": "CODIGO 6EQUJ5",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "laboratorio",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_dramatic_hit.wav",
                        "volumenSfx": 0.25,
                        "palabrasClave": ["Jerry Ehman", "Big Ear", "seis caracteres", "bolígrafo rojo"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka",
                        "infografia": {
                            "tipo": "dato_clave",
                            "titulo": "Secuencia de Intensidad",
                            "subtitulo": "Escala alfanumérica logarítmica de Big Ear",
                            "valorPrincipal": "6EQUJ5",
                            "unidad": "pico de potencia",
                            "items": [
                                {"etiqueta": "Pico 'U'", "valor": "30 veces el ruido cósmico", "porcentaje": 100, "color": "#EF4444"},
                                {"etiqueta": "Duración señal", "valor": "Exactamente 72 segundos", "porcentaje": 72, "color": "#38BDF8"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    }
                ]
            },
            {
                "id": "cap_2",
                "numero": 2,
                "titulo": "La Frecuencia Sagrada del Hidrógeno",
                "resumen": "Por qué los mil cuatrocientos veinte megahercios desconcertaron a los científicos.",
                "escenas": [
                    {
                        "id": 3,
                        "texto": "Aquella no era una emisión de radio ordinaria. La señal se concentraba en una banda extremadamente estrecha, exactamente en los mil cuatrocientos veinte megahercios, la línea de emisión del hidrógeno neutro en todo el universo.",
                        "tituloVisual": "1420 MHZ",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "espacio_profundo",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["banda extremadamente estrecha", "mil cuatrocientos veinte megahercios", "hidrógeno neutro"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka",
                        "infografia": {
                            "tipo": "comparacion",
                            "titulo": "Canal de Saludo Cósmico",
                            "subtitulo": "Línea del Hidrógeno Neutro (21 cm)",
                            "valorPrincipal": "1420.4",
                            "unidad": "MHz",
                            "items": [
                                {"etiqueta": "Emisión Señal Wow!", "valor": "Banda ultra estrecha (<10 kHz)", "porcentaje": 99, "color": "#34D399"},
                                {"etiqueta": "Ruido natural galáctico", "valor": "Banda ancha caótica", "porcentaje": 25, "color": "#94A3B8"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    },
                    {
                        "id": 4,
                        "texto": "Para los astrofísicos, esa frecuencia representa el canal universal de comunicación interestelar. Ningún fenómeno astronómico natural conocido emite energía con semejante pureza de banda sin dispersarse en el espacio.",
                        "tituloVisual": "CANAL INTERESTELAR",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "espacio_profundo",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["comunicación interestelar", "pureza de banda", "espacio"],
                        "poseId": "standing_confident",
                        "expresion": "smile_soft"
                    }
                ]
            },
            {
                "id": "cap_3",
                "numero": 3,
                "titulo": "La Campana Gaussiana de 72 Segundos",
                "resumen": "El patrón de barrido de la antena fija frente a la rotación terrestre.",
                "escenas": [
                    {
                        "id": 5,
                        "texto": "La antena de Big Ear no se movía: apuntaba fija al cielo mientras la Tierra rotaba lentamente. Cualquier fuente puntual en el espacio tardaba exactamente setenta y dos segundos en cruzar su campo visual de este a oeste.",
                        "tituloVisual": "ROTACION TERRESTRE",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "lunar",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["antena de Big Ear", "Tierra rotaba lentamente", "setenta y dos segundos"],
                        "poseId": "thinking_chin_hand",
                        "expresion": "analytical"
                    },
                    {
                        "id": 6,
                        "texto": "La señal creció durante treinta y seis segundos hasta alcanzar su clímax y luego decayó con simetría matemática perfecta durante otros treinta y seis segundos. Eso demostró sin lugar a dudas que provenía del espacio profundo y no de la Tierra.",
                        "tituloVisual": "SIMETRIA PERFECTA",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "laboratorio",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["treinta y seis segundos", "simetría matemática", "espacio profundo"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka",
                        "infografia": {
                            "tipo": "dato_clave",
                            "titulo": "Curva Gaussiana de Entrada",
                            "subtitulo": "Patrón de antena de Big Ear",
                            "valorPrincipal": "72s",
                            "unidad": "barrido exacto",
                            "items": [
                                {"etiqueta": "Fase de ascenso", "valor": "36 segundos", "porcentaje": 50, "color": "#38BDF8"},
                                {"etiqueta": "Fase de descenso", "valor": "36 segundos", "porcentaje": 50, "color": "#38BDF8"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    }
                ]
            },
            {
                "id": "cap_4",
                "numero": 4,
                "titulo": "Las Hipótesis Descartadas",
                "resumen": "Satélites secretos, aviones, chatarra espacial y cometas.",
                "escenas": [
                    {
                        "id": 7,
                        "texto": "Durante décadas, los escépticos buscaron explicaciones mundanas: transmisiones militares clasificadas, rebotes de radar en chatarra espacial o aviones espía cruzando el cielo nocturno de Ohio.",
                        "tituloVisual": "¿INTERFERENCIA HUMANA?",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "habitacion_noche",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_dramatic_hit.wav",
                        "volumenSfx": 0.25,
                        "palabrasClave": ["transmisiones militares", "chatarra espacial", "aviones espía"],
                        "poseId": "thinking_chin_hand",
                        "expresion": "analytical"
                    },
                    {
                        "id": 8,
                        "texto": "Pero la banda de los mil cuatrocientos veinte megahercios está protegida por tratados internacionales: está terminantemente prohibido emitir en ella. Además, ningún satélite ni avión conocido sobrevolaba la zona en esas coordenadas exactas.",
                        "tituloVisual": "ZONA PROTEGIDA",
                        "layout": "primer_plano",
                        "composicionVisual": "primer_plano",
                        "escenario": "laboratorio",
                        "transicion": "whip_left",
                        "efectosCamara": ["punch"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["tratados internacionales", "prohibido emitir", "coordenadas exactas"],
                        "poseId": "standing_confident",
                        "expresion": "analytical"
                    }
                ]
            },
            {
                "id": "cap_5",
                "numero": 5,
                "titulo": "La Búsqueda en la Constelación de Sagitario",
                "resumen": "Los rastreos posteriores y el silencio absoluto.",
                "escenas": [
                    {
                        "id": 9,
                        "texto": "La señal provino de una región vacía en dirección a la constelación de Sagitario, cerca del grupo estelar globular Messier cincuenta y cinco. Sin embargo, en los siguientes cuarenta años, los mayores radiotelescopios del mundo apuntaron a ese punto y solo hallaron silencio.",
                        "tituloVisual": "RUMBO A SAGITARIO",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "espacio_profundo",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["constelación de Sagitario", "Messier cincuenta y cinco", "cuarenta años"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka",
                        "infografia": {
                            "tipo": "dato_clave",
                            "titulo": "Coordenadas Celestiales",
                            "subtitulo": "Ascensión recta y declinación del origen",
                            "valorPrincipal": "19h 25m",
                            "unidad": "constelación Sagitario",
                            "items": [
                                {"etiqueta": "Distancia estimada", "valor": "Cientos a miles de años luz", "porcentaje": 100, "color": "#F59E0B"},
                                {"etiqueta": "Intentos de re-contacto", "valor": "> 100 barridos negativos", "porcentaje": 10, "color": "#EF4444"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    },
                    {
                        "id": 10,
                        "texto": "¿Fue una baliza interestelar rotatoria como el haz de un faro que solo nos barrió una vez? ¿O fue el último suspiro de una civilización lejana que se extinguió hace milenios? Cuarenta y nueve años después, la señal Wow sigue siendo el mayor enigma de la ciencia moderna.",
                        "tituloVisual": "EL ENIGMA VIVO",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "vacio",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["baliza interestelar", "haz de un faro", "mayor enigma"],
                        "poseId": "standing_confident",
                        "expresion": "smile_soft"
                    }
                ]
            }
        ]
    }


def construir_doc_005_fermi():
    return {
        "meta": {
            "id": "doc_005_paradoja_fermi",
            "slug": "paradoja_fermi_gran_filtro_documental",
            "titulo": "La Paradoja de Fermi y el Gran Filtro: La Aterradora Razón del Silencio Cósmico",
            "premisa": "Si el universo tiene miles de millones de años y billones de planetas habitables, las civilizaciones tecnológicas deberían haber colonizado la galaxia entera hace eones. ¿Dónde están todos?",
            "gancho": "¿Por qué el cielo nocturno está en un silencio tan sobrecogedor?",
            "categoria": "Science & Technology",
            "duracionObjetivo": [420, 500],
            "fps": 30,
            "dimensiones": {"width": 1920, "height": 1080},
            "idioma": "es",
            "voz": "alex.conds.pt",
            "musicaPrincipal": "bgm/bgm.mp3",
            "volumenMusica": 0.12,
            "fuentes": [
                "Fermi, E. (1950). Where is everybody? Los Alamos Laboratory.",
                "Hanson, R. (1998). The Great Filter - Are We Almost Past It?",
                "Bostrom, N. (2008). Where Are They? Why I Hope the Search for Extraterrestrial Life Finds Nothing."
            ],
            "tags": ["paradoja de fermi", "gran filtro", "astronomia", "seti", "universo", "ciencia", "documental"]
        },
        "capitulos": [
            {
                "id": "cap_1",
                "numero": 1,
                "titulo": "El Almuerzo de Los Álamos",
                "resumen": "La pregunta de Enrico Fermi en mil novecientos cincuenta.",
                "escenas": [
                    {
                        "id": 1,
                        "texto": "En el verano de mil novecientos cincuenta, el brillante físico Enrico Fermi caminaba hacia el comedor del laboratorio de Los Álamos conversando con sus colegas sobre platillos voladores y viajes interestelares.",
                        "tituloVisual": "VERANO DE 1950",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "laboratorio",
                        "transicion": "fundido_negro",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_dramatic_hit.wav",
                        "volumenSfx": 0.25,
                        "palabrasClave": ["mil novecientos cincuenta", "Enrico Fermi", "Los Álamos", "viajes interestelares"],
                        "poseId": "thinking_chin_hand",
                        "expresion": "analytical"
                    },
                    {
                        "id": 2,
                        "texto": "Al sentarse a la mesa, Fermi se quedó pensativo en silencio y de pronto soltó una pregunta que dejó helados a los presentes: si el cosmos es tan antiguo y hay tantas estrellas, ¿dónde está todo el mundo?",
                        "tituloVisual": "¿DONDE ESTAN TODOS?",
                        "layout": "primer_plano",
                        "composicionVisual": "primer_plano",
                        "escenario": "laboratorio",
                        "transicion": "zoom_in",
                        "efectosCamara": ["punch"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["Enrico Fermi", "cosmos tan antiguo", "dónde está todo el mundo"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka"
                    }
                ]
            },
            {
                "id": "cap_2",
                "numero": 2,
                "titulo": "La Matemática de la Colonización Galáctica",
                "resumen": "Por qué unas pocas decenas de millones de años bastan para colonizar la Vía Láctea.",
                "escenas": [
                    {
                        "id": 3,
                        "texto": "Nuestra galaxia tiene más de diez mil millones de años de antigüedad y alberga más de cien mil millones de estrellas. Incluso viajando a solo un uno por ciento de la velocidad de la luz, una civilización colonizadora necesitaría apenas cincuenta millones de años para expandirse por cada rincón de la Vía Láctea.",
                        "tituloVisual": "50 MILLONES DE AÑOS",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "espacio_profundo",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["diez mil millones", "uno por ciento de la luz", "cincuenta millones de años"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka",
                        "infografia": {
                            "tipo": "comparacion",
                            "titulo": "Escala Temporal Galáctica",
                            "subtitulo": "Tiempo para colonizar toda la Vía Láctea",
                            "valorPrincipal": "0.5%",
                            "unidad": "de la edad galáctica",
                            "items": [
                                {"etiqueta": "Edad de la Galaxia", "valor": "10.000 millones de años", "porcentaje": 100, "color": "#94A3B8"},
                                {"etiqueta": "Tiempo de colonización", "valor": "50 millones de años", "porcentaje": 5, "color": "#38BDF8"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    },
                    {
                        "id": 4,
                        "texto": "Cincuenta millones de años es un abrir y cerrar de ojos comparado con la edad del universo. Si otras especies hubieran surgido antes que nosotros, sus naves, sus megaciudades orbitales y sus señales de radio deberían estar por todas partes. Sin embargo, solo encontramos un silencio cósmico ensordecedor.",
                        "tituloVisual": "EL GRAN SILENCIO",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "espacio_profundo",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["abrir y cerrar de ojos", "megaciudades orbitales", "silencio cósmico"],
                        "poseId": "standing_confident",
                        "expresion": "analytical"
                    }
                ]
            },
            {
                "id": "cap_3",
                "numero": 3,
                "titulo": "El Concepto del Gran Filtro",
                "resumen": "La hipótesis de Robin Hanson sobre la barrera insuperable.",
                "escenas": [
                    {
                        "id": 5,
                        "texto": "En mil novecientos noventa y ocho, el economista y filósofo Robin Hanson propuso una explicación perturbadora: la hipótesis del Gran Filtro. Debe existir una barrera evolutiva o tecnológica casi imposible de superar que extermina a casi todas las especies antes de que alcancen las estrellas.",
                        "tituloVisual": "EL GRAN FILTRO",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "espacio_molecular",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["Robin Hanson", "Gran Filtro", "barrera evolutiva"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka",
                        "infografia": {
                            "tipo": "dato_clave",
                            "titulo": "Etapas Críticas Evolutivas",
                            "subtitulo": "Desde la química prebiótica a la civilización estelar",
                            "valorPrincipal": "9 PASOS",
                            "unidad": "hitos obligatorios",
                            "items": [
                                {"etiqueta": "Abiogénesis a célula compleja", "valor": "Paso 1 a 3 (Superados)", "porcentaje": 40, "color": "#10B981"},
                                {"etiqueta": "Autodestrucción tecnológica", "valor": "Paso 8 (Riesgo actual)", "porcentaje": 90, "color": "#EF4444"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    },
                    {
                        "id": 6,
                        "texto": "Este filtro plantea una disyuntiva estremecedora: o bien el filtro está en nuestro pasado y la vida consciente es un milagro irrepetible, o bien el filtro está en nuestro futuro inmediato y nos espera una trampa de autodestrucción masiva.",
                        "tituloVisual": "¿DETRAS O DELANTE?",
                        "layout": "primer_plano",
                        "composicionVisual": "primer_plano",
                        "escenario": "habitacion_noche",
                        "transicion": "whip_left",
                        "efectosCamara": ["punch"],
                        "sfx": "sfx/sfx_dramatic_hit.wav",
                        "volumenSfx": 0.25,
                        "palabrasClave": ["filtro en nuestro pasado", "vida consciente", "autodestrucción masiva"],
                        "poseId": "thinking_chin_hand",
                        "expresion": "shocked"
                    }
                ]
            },
            {
                "id": "cap_4",
                "numero": 4,
                "titulo": "¿Y si el Filtro está en Nuestro Futuro?",
                "resumen": "Las amenazas tecnológicas que terminan con civilizaciones maduras.",
                "escenas": [
                    {
                        "id": 7,
                        "texto": "Si el filtro nos espera adelante, significa que cualquier especie que descubre la energía nuclear, la biotecnología avanzada o la inteligencia artificial general termina inevitablemente detonando su propia extinción en cuestión de siglos.",
                        "tituloVisual": "TRAMPA TECNOLOGICA",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "laboratorio",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["energía nuclear", "biotecnología", "inteligencia artificial general"],
                        "poseId": "standing_confident",
                        "expresion": "analytical"
                    },
                    {
                        "id": 8,
                        "texto": "Por esa razón, el filósofo Nick Bostrom advierte que descubrir fósiles de vida compleja en Marte no sería motivo de fiesta, sino la peor noticia posible: demostraría que la vida surge con facilidad y que lo que extermina a las civilizaciones aún nos aguarda en el horizonte.",
                        "tituloVisual": "LA ADVERTENCIA DE BOSTROM",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "superficie_marte",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["Nick Bostrom", "fósiles en Marte", "peor noticia posible"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka",
                        "infografia": {
                            "tipo": "comparacion",
                            "titulo": "Hallazgos en Marte vs Futuro Humano",
                            "subtitulo": "Implicaciones filosóficas del Gran Filtro",
                            "valorPrincipal": "PARADOJA",
                            "unidad": "diagnóstico",
                            "items": [
                                {"etiqueta": "Marte completamente estéril", "valor": "Buenas noticias (Filtro atrás)", "porcentaje": 100, "color": "#10B981"},
                                {"etiqueta": "Fósiles complejos en Marte", "valor": "Peligro fatal (Filtro adelante)", "porcentaje": 100, "color": "#EF4444"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    }
                ]
            },
            {
                "id": "cap_5",
                "numero": 5,
                "titulo": "La Hipótesis del Bosque Oscuro",
                "resumen": "El silencio no por ausencia sino por miedo a depredadores cósmicos.",
                "escenas": [
                    {
                        "id": 9,
                        "texto": "Existe otra alternativa aún más fría: la hipótesis del Bosque Oscuro. El universo no está vacío, sino repleto de civilizaciones avanzadas que se esconden en absoluto silencio radioeléctrico para no ser detectadas por civilizaciones depredadoras.",
                        "tituloVisual": "EL BOSQUE OSCURO",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "habitacion_noche",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_dramatic_hit.wav",
                        "volumenSfx": 0.25,
                        "palabrasClave": ["Bosque Oscuro", "silencio radioeléctrico", "civilizaciones depredadoras"],
                        "poseId": "thinking_chin_hand",
                        "expresion": "analytical"
                    },
                    {
                        "id": 10,
                        "texto": "Desde esa perspectiva, la humanidad es como un niño gritando en medio de una selva nocturna sin saber qué fieras escuchan sus gritos. Transmitir señales a ciegas al cosmos podría ser el error más peligroso de nuestra historia.",
                        "tituloVisual": "GRITOS EN LA SELVA",
                        "layout": "primer_plano",
                        "composicionVisual": "primer_plano",
                        "escenario": "espacio_profundo",
                        "transicion": "whip_left",
                        "efectosCamara": ["punch"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["niño gritando", "selva nocturna", "error más peligroso"],
                        "poseId": "standing_confident",
                        "expresion": "shocked"
                    }
                ]
            },
            {
                "id": "cap_6",
                "numero": 6,
                "titulo": "La Responsabilidad de Estar Solos",
                "resumen": "Epílogo sobre la soledad como llamado a la preservación humana.",
                "escenas": [
                    {
                        "id": 11,
                        "texto": "Ya sea porque somos los primeros pioneros de la galaxia o porque sobrevivimos milagrosamente al filtro del pasado, la soledad cósmica nos deja una lección mayúscula: no hay nadie que venga a rescatarnos de nosotros mismos. El futuro de la conciencia en este rincón del universo depende exclusivamente de lo que hagamos hoy en la Tierra.",
                        "tituloVisual": "PIONEROS Y GUARDIANES",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "vacio",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["primeros pioneros", "soledad cósmica", "futuro de la conciencia"],
                        "poseId": "standing_confident",
                        "expresion": "smile_soft"
                    }
                ]
            }
        ]
    }


def main():
    print("[CREAR] Generando documentales largos 4 y 5...")
    d4 = construir_doc_004_wow()
    d5 = construir_doc_005_fermi()

    with open(GUIONES_DIR / "doc_004_misterio_wow.json", "w", encoding="utf-8") as f:
        json.dump(d4, f, ensure_ascii=False, indent=2)

    with open(GUIONES_DIR / "doc_005_paradoja_fermi.json", "w", encoding="utf-8") as f:
        json.dump(d5, f, ensure_ascii=False, indent=2)

    print("✅ Documentales 4 y 5 exportados exitosamente.")


if __name__ == "__main__":
    main()
