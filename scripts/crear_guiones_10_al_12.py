#!/usr/bin/env python3
"""
Constructor de Guiones Largos 10 al 12 (16:9, 1920x1080)
Extensión documental completa (6 capítulos, 11-12 escenas cada uno, ~400-500 segundos).
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


def construir_doc_010_color_sol():
    return {
        "meta": {
            "id": "doc_010_color_sol",
            "slug": "verdadero_color_sol_optica_cosmica",
            "titulo": "El Color Real del Sol: La Trampa Óptica de Nuestra Atmósfera",
            "premisa": "Toda la cultura humana retrata al Sol como una bola amarilla o naranja. Sin embargo, en el vacío del espacio nuestra estrella brilla con una luz blanca deslumbrante y pura.",
            "gancho": "¿De qué color es verdaderamente el Sol cuando lo observas fuera de la Tierra?",
            "categoria": "Science & Technology",
            "duracionObjetivo": [400, 480],
            "fps": 30,
            "dimensiones": {"width": 1920, "height": 1080},
            "idioma": "es",
            "voz": "alex.conds.pt",
            "musicaPrincipal": "bgm/bgm.mp3",
            "volumenMusica": 0.12,
            "fuentes": [
                "Rayleigh, Lord (1899). On the Transmission of Light through an Atmosphere. Phil. Mag.",
                "NASA Solar Physics (2020). The Sun's True White Spectrum.",
                "Minnaert, M. (1993). Light and Color in the Outdoors. Springer."
            ],
            "tags": ["ciencia", "sol", "fisica", "optica", "astronomia", "atmosfera", "documental"]
        },
        "capitulos": [
            {
                "id": "cap_1",
                "numero": 1,
                "titulo": "El Mito del Dibujo Infantil",
                "resumen": "El crayón amarillo y el consenso cultural universal.",
                "escenas": [
                    {
                        "id": 1,
                        "texto": "Pídele a cualquier niño o adulto en cualquier rincón del planeta que dibuje el Sol en una hoja de papel blanco, y casi con total seguridad elegirá un crayón amarillo o naranja brillante.",
                        "tituloVisual": "EL CRAYON AMARILLO",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "cielo_dia",
                        "transicion": "fundido_negro",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_dramatic_hit.wav",
                        "volumenSfx": 0.25,
                        "palabrasClave": ["crayón amarillo", "Sol en una hoja", "naranja brillante"],
                        "poseId": "standing_confident",
                        "expresion": "analytical"
                    },
                    {
                        "id": 2,
                        "texto": "Incluso los astrónomos lo clasifican técnicamente como una enana amarilla. Pero esa etiqueta es una trampa lingüística: si pudieras contemplar al Sol desde la ventana de la Estación Espacial Internacional sin cristales tintados, verías una luz blanca pura que te quemaría las pupilas en un instante.",
                        "tituloVisual": "BLANCO PURO",
                        "layout": "primer_plano",
                        "composicionVisual": "primer_plano",
                        "escenario": "espacio_profundo",
                        "transicion": "zoom_in",
                        "efectosCamara": ["punch"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["enana amarilla", "luz blanca pura", "quemaría las pupilas"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka"
                    }
                ]
            },
            {
                "id": "cap_2",
                "numero": 2,
                "titulo": "La Física de la Radiación de Cuerpo Negro",
                "resumen": "El espectro térmico a cinco mil quinientos grados centígrados.",
                "escenas": [
                    {
                        "id": 3,
                        "texto": "El color de cualquier estrella depende exclusivamente de la temperatura de su superficie fotosférica. La fotosfera de nuestro Sol arde a cinco mil quinientos grados centígrados, emitiendo fotones en todas las longitudes de onda del espectro electromagnético visible.",
                        "tituloVisual": "5.500 °C EN LA FOTOSFERA",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "laboratorio",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["temperatura de su superficie", "cinco mil quinientos grados", "espectro electromagnético"],
                        "poseId": "standing_confident",
                        "expresion": "analytical"
                    },
                    {
                        "id": 4,
                        "texto": "Emite luz roja, naranja, amarilla, verde, azul y violeta con intensidades casi parejas. Cuando el ojo humano recibe todos esos colores mezclados simultáneamente, nuestro cerebro interpreta la suma como un blanco deslumbrante.",
                        "tituloVisual": "SUMA DE COLORES",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "espacio_molecular",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["todos esos colores", "mezclados simultáneamente", "blanco deslumbrante"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka",
                        "infografia": {
                            "tipo": "dato_clave",
                            "titulo": "Espectro Solar Fuera de Atmósfera",
                            "subtitulo": "Emisión continua de radiación de Planck",
                            "valorPrincipal": "5500 K",
                            "unidad": "espectro blanco completo",
                            "items": [
                                {"etiqueta": "Pico de emisión", "valor": "Verde-azulado (500 nm)", "porcentaje": 100, "color": "#10B981"},
                                {"etiqueta": "Percepción humana", "valor": "Blanco neutro equilibrado", "porcentaje": 100, "color": "#F8FAFC"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    }
                ]
            },
            {
                "id": "cap_3",
                "numero": 3,
                "titulo": "La Dispersión de Rayleigh en el Aire",
                "resumen": "Cómo las moléculas de nitrógeno y oxígeno roban el azul.",
                "escenas": [
                    {
                        "id": 5,
                        "texto": "Entonces, ¿por qué desde la superficie de la Tierra lo vemos dorado? La culpable es la atmósfera: una densa envoltura de nitrógeno y oxígeno que actúa como un filtro óptico selectivo.",
                        "tituloVisual": "EL FILTRO ATMOSFERICO",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "cielo_dia",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["vemos dorado", "nitrógeno y oxígeno", "filtro óptico"],
                        "poseId": "thinking_chin_hand",
                        "expresion": "analytical"
                    },
                    {
                        "id": 6,
                        "texto": "Bajo la dispersión de Rayleigh, las ondas de luz azul, que son más cortas, chocan contra las moléculas de gas y rebotan en todas direcciones, dispersándose por todo el firmamento e iluminando el cielo con el color azul que vemos a diario.",
                        "tituloVisual": "DISPERSION DE RAYLEIGH",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "cielo_dia",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["ondas de luz azul", "moléculas de gas", "color azul"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka",
                        "infografia": {
                            "tipo": "comparacion",
                            "titulo": "Eficiencia de Dispersión por Longitud de Onda",
                            "subtitulo": "Ley de Rayleigh (proporcional a 1 / longitud⁴)",
                            "valorPrincipal": "9.4x",
                            "unidad": "más dispersión azul que roja",
                            "items": [
                                {"etiqueta": "Luz azul (400 nm)", "valor": "Dispersada por todo el cielo", "porcentaje": 100, "color": "#38BDF8"},
                                {"etiqueta": "Luz roja (700 nm)", "valor": "Pasa en línea recta", "porcentaje": 11, "color": "#EF4444"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    }
                ]
            },
            {
                "id": "cap_4",
                "numero": 4,
                "titulo": "La Sustracción Cromática: Restar Azul al Blanco",
                "resumen": "La matemática del color que produce el tono amarillo.",
                "escenas": [
                    {
                        "id": 7,
                        "texto": "Cuando tomas un haz de luz blanca pura y le quitas una buena porción de sus componentes azules y violetas, lo que continúa en línea recta directa hacia tus ojos es una mezcla dominada por los tonos amarillos, verdes y rojos.",
                        "tituloVisual": "RESTAR AZUL AL BLANCO",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "laboratorio",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_dramatic_hit.wav",
                        "volumenSfx": 0.25,
                        "palabrasClave": ["luz blanca pura", "quitas componentes azules", "tonos amarillos"],
                        "poseId": "standing_confident",
                        "expresion": "analytical"
                    },
                    {
                        "id": 8,
                        "texto": "El Sol se ve amarillo en la Tierra por el mismo motivo exacto por el que el cielo se ve azul. Si nuestra atmósfera fuera de gas metano o de vapor denso, el cielo tendría otro color y veríamos al Sol verde o turquesa.",
                        "tituloVisual": "DOS CARAS DE LA MISMA LUZ",
                        "layout": "primer_plano",
                        "composicionVisual": "primer_plano",
                        "escenario": "cielo_dia",
                        "transicion": "whip_left",
                        "efectosCamara": ["punch"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["mismo motivo exacto", "cielo se ve azul", "dos caras de la misma luz"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka"
                    }
                ]
            },
            {
                "id": "cap_5",
                "numero": 5,
                "titulo": "El Fuego Crepuscular del Atardecer",
                "resumen": "Por qué atravesar diez veces más masa de aire vuelve al Sol rojo.",
                "escenas": [
                    {
                        "id": 9,
                        "texto": "Al atardecer, el efecto óptico se multiplica de forma espectacular. Como el Sol está bajo cerca del horizonte, sus rayos deben atravesar diez veces más masa atmosférica que al mediodía para llegar a nosotros.",
                        "tituloVisual": "DIEZ VECES MAS AIRE",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "atardecer_dorado",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["al atardecer", "cerca del horizonte", "diez veces más masa"],
                        "poseId": "thinking_chin_hand",
                        "expresion": "analytical",
                        "infografia": {
                            "tipo": "dato_clave",
                            "titulo": "Grosor Atmosférico Óptico (Airmass)",
                            "subtitulo": "Trayectoria de los fotones solares",
                            "valorPrincipal": "10x",
                            "unidad": "columna de aire al crepúsculo",
                            "items": [
                                {"etiqueta": "Cenit al mediodía", "valor": "1 Airmass (100% fotones)", "porcentaje": 10, "color": "#38BDF8"},
                                {"etiqueta": "Puesta de sol", "valor": "10 Airmass (Solo rojo sobrevive)", "porcentaje": 100, "color": "#EF4444"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    },
                    {
                        "id": 10,
                        "texto": "Toda la luz azul, verde y amarilla queda dispersada y absorbida por el camino; únicamente las ondas rojas más largas logran abrirse paso, regalándonos esos ocasos encendidos que han inspirado a poetas y pintores a lo largo de los siglos.",
                        "tituloVisual": "OCASO ENCENDIDO",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "atardecer_dorado",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["luz azul dispersada", "ondas rojas más largas", "ocasos encendidos"],
                        "poseId": "standing_confident",
                        "expresion": "smile_soft"
                    }
                ]
            },
            {
                "id": "cap_6",
                "numero": 6,
                "titulo": "La Antorcha Blanca del Espacio Exterior",
                "resumen": "Epílogo sobre la perspectiva cósmica de los astronautas.",
                "escenas": [
                    {
                        "id": 11,
                        "texto": "Cuando los astronautas contemplan el Sol en el vacío exterior, ven una colosal antorcha blanca flotando en medio de una oscuridad absoluta de terciopelo negro. Nuestro Sol nunca fue amarillo: fue nuestra atmósfera la que tiñó al rey del cosmos para proteger nuestros ojos y regalarnos el cielo azul.",
                        "tituloVisual": "LA PERSPECTIVA COSMICA",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "vacio",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["antorcha blanca", "oscuridad absoluta", "nunca fue amarillo"],
                        "poseId": "standing_confident",
                        "expresion": "smile_soft"
                    }
                ]
            }
        ]
    }


def construir_doc_011_hawking():
    return {
        "meta": {
            "id": "doc_011_radiacion_hawking",
            "slug": "radiacion_hawking_evaporacion_agujeros_negros",
            "titulo": "La Radiación de Hawking: Cómo la Física Cuántica Destruye a los Agujeros Negros",
            "premisa": "Durante décadas se creyó que los agujeros negros eran tumbas eternas e indestructibles de materia. En 1974, Stephen Hawking demostró que la mecánica cuántica en el horizonte de sucesos hace que se evaporen hasta estallar.",
            "gancho": "¿Pueden morir los agujeros negros o sobrevivirán por siempre en el vacío del universo?",
            "categoria": "Science & Technology",
            "duracionObjetivo": [420, 500],
            "fps": 30,
            "dimensiones": {"width": 1920, "height": 1080},
            "idioma": "es",
            "voz": "alex.conds.pt",
            "musicaPrincipal": "bgm/bgm.mp3",
            "volumenMusica": 0.12,
            "fuentes": [
                "Hawking, S. W. (1974). Black hole explosions?. Nature.",
                "Hawking, S. W. (1975). Particle creation by black holes. Commun. Math. Phys.",
                "Page, D. N. (1976). Particle emission rates from a black hole. Physical Review D."
            ],
            "tags": ["fisica", "agujeros negros", "hawking", "cuantica", "espacio", "relatividad", "documental"]
        },
        "capitulos": [
            {
                "id": "cap_1",
                "numero": 1,
                "titulo": "La Prisión Eterna de la Relatividad",
                "resumen": "La concepción clásica de los agujeros negros como trampas de las que nada escapa.",
                "escenas": [
                    {
                        "id": 1,
                        "texto": "En la teoría de la relatividad general de Einstein, un agujero negro es el destino final y definitivo de la materia: una región donde la gravedad es tan infinitamente densa que ni siquiera los fotones de luz pueden escapar jamás.",
                        "tituloVisual": "GRAVEDAD INFINITA",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "espacio_profundo",
                        "transicion": "fundido_negro",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_dramatic_hit.wav",
                        "volumenSfx": 0.25,
                        "palabrasClave": ["relatividad general", "agujero negro", "fotones de luz"],
                        "poseId": "standing_confident",
                        "expresion": "analytical"
                    },
                    {
                        "id": 2,
                        "texto": "Cualquier estrella, planeta o rayo de luz que cruzara su frontera invisible, llamada horizonte de sucesos, quedaba condenado a desaparecer para siempre, haciendo crecer la masa del agujero en un camino de un solo sentido.",
                        "tituloVisual": "HORIZONTE DE SUCESOS",
                        "layout": "primer_plano",
                        "composicionVisual": "primer_plano",
                        "escenario": "espacio_profundo",
                        "transicion": "zoom_in",
                        "efectosCamara": ["punch"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["horizonte de sucesos", "crecer la masa", "solo sentido"],
                        "poseId": "thinking_chin_hand",
                        "expresion": "analytical"
                    }
                ]
            },
            {
                "id": "cap_2",
                "numero": 2,
                "titulo": "El Vacío Cuántico Hirviente",
                "resumen": "La fluctuación cuántica y la creación espontánea de pares.",
                "escenas": [
                    {
                        "id": 3,
                        "texto": "Pero en la física cuántica, el vacío absoluto no está vacío en absoluto. Es una sopa hirviente de fluctuaciones de energía donde nacen y mueren constantemente pares de partículas y antipartículas virtuales en billonésimas de segundo.",
                        "tituloVisual": "EL VACIO HIRVIENTE",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "espacio_molecular",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["física cuántica", "vacío absoluto", "partículas virtuales"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka"
                    },
                    {
                        "id": 4,
                        "texto": "Normalmente, estas partículas se crean de la nada, colisionan entre sí en un parpadeo y se aniquilan mutuamente devolviendo la energía prestada al universo. Pero Stephen Hawking se preguntó: ¿qué ocurre si ese par nace exactamente sobre el borde del horizonte de sucesos?",
                        "tituloVisual": "¿QUE PASA EN EL BORDE?",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "espacio_profundo",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["aniquilan mutuamente", "Stephen Hawking", "borde del horizonte"],
                        "poseId": "thinking_chin_hand",
                        "expresion": "analytical",
                        "infografia": {
                            "tipo": "dato_clave",
                            "titulo": "Fluctuaciones del Vacío",
                            "subtitulo": "Principio de incertidumbre de Heisenberg",
                            "valorPrincipal": "ΔE·Δt ≥ ℏ/2",
                            "unidad": "fórmula cuántica",
                            "items": [
                                {"etiqueta": "Creación espontánea", "valor": "Par materia-antimateria", "porcentaje": 100, "color": "#38BDF8"},
                                {"etiqueta": "Tiempo de vida", "valor": "Inapreciable (10^-21 seg)", "porcentaje": 10, "color": "#94A3B8"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    }
                ]
            },
            {
                "id": "cap_3",
                "numero": 3,
                "titulo": "El Robo Cuántico de Masa",
                "resumen": "La separación del par: una cae dentro y la otra escapa al infinito.",
                "escenas": [
                    {
                        "id": 5,
                        "texto": "En mil novecientos setenta y cuatro, Hawking calculó que las fuerzas de marea gravitatoria pueden separar al par antes de que se aniquilen: una de las partículas cae irremediablemente al interior del agujero, mientras que su compañera queda libre y escapa hacia el espacio exterior.",
                        "tituloVisual": "PARTICULA LIBERADA",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "espacio_profundo",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["mil novecientos setenta y cuatro", "fuerzas de marea", "escapa hacia el espacio"],
                        "poseId": "standing_confident",
                        "expresion": "eureka"
                    },
                    {
                        "id": 6,
                        "texto": "Para conservar la energía total del universo, la partícula que cae al agujero negro debe entrar con energía negativa neta. Como resultado matemático inevitable, cada vez que una partícula escapa, el agujero negro pierde masa física y se encoge.",
                        "tituloVisual": "ENERGIA NEGATIVA",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "laboratorio",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["energía negativa", "pierde masa física", "se encoge"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka",
                        "infografia": {
                            "tipo": "comparacion",
                            "titulo": "Mecanismo de la Radiación de Hawking",
                            "subtitulo": "Balanza energética en el horizonte",
                            "valorPrincipal": "ΔM < 0",
                            "unidad": "pérdida neta de masa",
                            "items": [
                                {"etiqueta": "Partícula exterior", "valor": "Radiación térmica emitida", "porcentaje": 100, "color": "#10B981"},
                                {"etiqueta": "Partícula atrapada", "valor": "Resta masa al agujero", "porcentaje": 100, "color": "#EF4444"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    }
                ]
            },
            {
                "id": "cap_4",
                "numero": 4,
                "titulo": "La Paradoja de la Temperatura Inversa",
                "resumen": "Cuanto más pequeño se vuelve, más caliente arde.",
                "escenas": [
                    {
                        "id": 7,
                        "texto": "Hawking descubrió una propiedad asombrosa e intuitivamente contraria a toda la termodinámica clásica: los agujeros negros tienen una capacidad calorífica negativa.",
                        "tituloVisual": "CALOR INVERSO",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "laboratorio",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_dramatic_hit.wav",
                        "volumenSfx": 0.25,
                        "palabrasClave": ["propiedad asombrosa", "termodinámica clásica", "calorífica negativa"],
                        "poseId": "thinking_chin_hand",
                        "expresion": "analytical"
                    },
                    {
                        "id": 8,
                        "texto": "Un agujero negro supermasivo es gélido, con una temperatura apenas por encima del cero absoluto. Pero conforme pierde masa y se hace diminuto, su temperatura se dispara violentamente: cuanto menos pesa, más caliente arde y más rápido se evapora en una espiral desbocada.",
                        "tituloVisual": "ESPIRAL ACELERADA",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "espacio_profundo",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["cero absoluto", "temperatura se dispara", "más rápido se evapora"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka",
                        "infografia": {
                            "tipo": "dato_clave",
                            "titulo": "Temperatura de Hawking",
                            "subtitulo": "Relación inversa absoluta: T = ℏc³ / (8πGMk)",
                            "valorPrincipal": "T ∝ 1/M",
                            "unidad": "fórmula maestra",
                            "items": [
                                {"etiqueta": "Agujero de masa solar", "valor": "0.00000006 Kelvin (Helado)", "porcentaje": 1, "color": "#38BDF8"},
                                {"etiqueta": "Último segundo de vida", "valor": "Billones de grados (Bomba)", "porcentaje": 100, "color": "#EF4444"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    }
                ]
            },
            {
                "id": "cap_5",
                "numero": 5,
                "titulo": "El Estallido Final en Rayos Gamma",
                "resumen": "El clímax catastrófico del último segundo de vida.",
                "escenas": [
                    {
                        "id": 9,
                        "texto": "Durante su último segundo de existencia, cuando el agujero negro se reduce a unas pocas toneladas de masa, la evaporación se convierte en una catástrofe luminosa: libera más energía que millones de bombas nucleares en un estallido fulminante de rayos gamma.",
                        "tituloVisual": "DETONACION FINAL",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "espacio_profundo",
                        "transicion": "zoom_in",
                        "efectosCamara": ["punch", "drift"],
                        "sfx": "sfx/sfx_dramatic_hit.wav",
                        "volumenSfx": 0.25,
                        "palabrasClave": ["último segundo", "catástrofe luminosa", "millones de bombas nucleares"],
                        "poseId": "standing_confident",
                        "expresion": "shocked"
                    },
                    {
                        "id": 10,
                        "texto": "Aunque a un agujero negro estelar le tomará diez elevado a la sesenta y siete años evaporarse por completo —un tiempo inmensamente mayor que toda la historia cósmica—, el destino final de todos ellos es la disolución total.",
                        "tituloVisual": "10^67 AÑOS",
                        "layout": "primer_plano",
                        "composicionVisual": "primer_plano",
                        "escenario": "espacio_profundo",
                        "transicion": "whip_left",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["diez elevado a la sesenta y siete", "disolución total", "historia cósmica"],
                        "poseId": "thinking_chin_hand",
                        "expresion": "analytical"
                    }
                ]
            },
            {
                "id": "cap_6",
                "numero": 6,
                "titulo": "La Paradoja de la Información y el Destino Cósmico",
                "resumen": "Epílogo sobre la reconciliación entre la relatividad y la cuántica.",
                "escenas": [
                    {
                        "id": 11,
                        "texto": "La radiación de Hawking desató la mayor revolución de la física teórica moderna: si un agujero negro se evapora por completo, ¿adónde va la información de todo lo que cayó en él? Stephen Hawking nos enseñó que incluso los monstruos más temibles del cosmos son mortales y que en sus cenizas cuánticas descansa la fórmula definitiva para comprender la realidad.",
                        "tituloVisual": "CENIZAS CUANTICAS",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "vacio",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["radiación de Hawking", "paradoja de la información", "monstruos más temibles"],
                        "poseId": "standing_confident",
                        "expresion": "smile_soft"
                    }
                ]
            }
        ]
    }


def main():
    print("[CREAR] Generando documentales largos 10 y 11...")
    d10 = construir_doc_010_color_sol()
    d11 = construir_doc_011_hawking()

    with open(GUIONES_DIR / "doc_010_color_sol.json", "w", encoding="utf-8") as f:
        json.dump(d10, f, ensure_ascii=False, indent=2)

    with open(GUIONES_DIR / "doc_011_radiacion_hawking.json", "w", encoding="utf-8") as f:
        json.dump(d11, f, ensure_ascii=False, indent=2)

    print("✅ Documentales 10 y 11 exportados exitosamente.")


if __name__ == "__main__":
    main()
