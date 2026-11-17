#!/usr/bin/env python3
"""
Constructor de Guiones Largos 6 al 10 (16:9, 1920x1080)
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


def construir_doc_006_kola():
    return {
        "meta": {
            "id": "doc_006_pozo_kola",
            "slug": "pozo_superprofundo_kola_infierno_terrestre",
            "titulo": "El Pozo Superprofundo de Kola: El Agujero más Hondo Excavado por la Humanidad",
            "premisa": "En 1970 la Unión Soviética inició en el Ártico la perforación más profunda jamás intentada. A doce kilómetros bajo tierra, toparon con roca hirviente que fluía como plástico y agua caliente donde debía reinar la roca seca.",
            "gancho": "¿Qué encontraron realmente los científicos soviéticos al cavar el agujero más hondo del planeta?",
            "categoria": "Science & Technology",
            "duracionObjetivo": [400, 480],
            "fps": 30,
            "dimensiones": {"width": 1920, "height": 1080},
            "idioma": "es",
            "voz": "alex.conds.pt",
            "musicaPrincipal": "bgm/bgm.mp3",
            "volumenMusica": 0.12,
            "fuentes": [
                "Kozlovsky, Y. A. (1987). The Superdeep Well of the Kola Peninsula. Springer.",
                "Smith, C. (1995). Continental Drilling and the Kola Experience.",
                "Fuchs, K., et al. (1990). Super-Deep Continental Drilling and Deep Geophysical Sounding."
            ],
            "tags": ["geologia", "pozo de kola", "tierra", "geofisica", "ciencia", "historia", "documental"]
        },
        "capitulos": [
            {
                "id": "cap_1",
                "numero": 1,
                "titulo": "La Carrera hacia el Centro de la Tierra",
                "resumen": "El inicio de la perforación en la península de Kola en mil novecientos setenta.",
                "escenas": [
                    {
                        "id": 1,
                        "texto": "Durante la Guerra Fría, la carrera entre superpotencias no solo apuntó hacia la Luna. En mayo de mil novecientos setenta, en el inhóspito Círculo Polar Ártico, ingenieros soviéticos encendieron la torre de perforación Uralmash cuatro e para conquistar las profundidades terrestres.",
                        "tituloVisual": "MAYO DE 1970",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "laboratorio",
                        "transicion": "fundido_negro",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_dramatic_hit.wav",
                        "volumenSfx": 0.25,
                        "palabrasClave": ["Guerra Fría", "Círculo Polar Ártico", "Uralmash cuatro e"],
                        "poseId": "standing_confident",
                        "expresion": "analytical"
                    },
                    {
                        "id": 2,
                        "texto": "El objetivo soviético era colosal: perforar quince kilómetros a través de la corteza continental del escudo báltico para tocar directamente la discontinuidad de Mohorovicic y tomar muestras del manto virgen.",
                        "tituloVisual": "OBJETIVO: 15 KM",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "red_subterranea",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["quince kilómetros", "escudo báltico", "Mohorovicic"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka",
                        "infografia": {
                            "tipo": "dato_clave",
                            "titulo": "Meta del Proyecto SG-3",
                            "subtitulo": "Profundidad planificada a través de la corteza",
                            "valorPrincipal": "15.000",
                            "unidad": "metros objetivo",
                            "items": [
                                {"etiqueta": "Récord alcanzado", "valor": "12.262 metros finales", "porcentaje": 82, "color": "#F59E0B"},
                                {"etiqueta": "Espesor de la corteza", "valor": "Aprox 35 kilómetros", "porcentaje": 35, "color": "#38BDF8"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    }
                ]
            },
            {
                "id": "cap_2",
                "numero": 2,
                "titulo": "El Desplome de las Teorías Geológicas",
                "resumen": "La ausencia de basalto y la presencia de granito fracturado.",
                "escenas": [
                    {
                        "id": 3,
                        "texto": "Los libros de texto de la época afirmaban con total certeza que a partir de los siete kilómetros de profundidad el granito daría paso a una capa masiva y compacta de basalto volcánico pesado.",
                        "tituloVisual": "EL MAPA TEORICO",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "red_subterranea",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["siete kilómetros", "capa masiva", "basalto volcánico"],
                        "poseId": "thinking_chin_hand",
                        "expresion": "analytical"
                    },
                    {
                        "id": 4,
                        "texto": "Pero los taladros jamás encontraron basalto. El granito continuó extendiéndose hasta los doce kilómetros, pero transformado por la presión en una roca quebradiza y porosa saturada de gas helio, hidrógeno y nitrógeno.",
                        "tituloVisual": "GRANITO FRACTURADO",
                        "layout": "primer_plano",
                        "composicionVisual": "primer_plano",
                        "escenario": "red_subterranea",
                        "transicion": "whip_left",
                        "efectosCamara": ["punch"],
                        "sfx": "sfx/sfx_dramatic_hit.wav",
                        "volumenSfx": 0.25,
                        "palabrasClave": ["jamás encontraron basalto", "doce kilómetros", "roca porosa"],
                        "poseId": "standing_confident",
                        "expresion": "shocked"
                    }
                ]
            },
            {
                "id": "cap_3",
                "numero": 3,
                "titulo": "Agua Hirviente en el Abismo Seco",
                "resumen": "El hallazgo de fluidos hidrotermales donde era físicamente imposible.",
                "escenas": [
                    {
                        "id": 5,
                        "texto": "El mayor choque para la comunidad científica ocurrió al superar los nueve kilómetros: los sensores de extracción comenzaron a bombear lodo saturado de agua caliente mineralizada.",
                        "tituloVisual": "AGUA A 9 KILOMETROS",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "red_subterranea",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["nueve kilómetros", "sensores de extracción", "agua caliente mineralizada"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka"
                    },
                    {
                        "id": 6,
                        "texto": "Esa agua no procedía de la superficie: jamás había llovido allí. Eran iones de hidrógeno y oxígeno comprimidos en los minerales que, bajo el calor extremo, se habían liberado formando una salmuera que no podía escapar debido a las capas superiores impermeables.",
                        "tituloVisual": "ORIGEN MINERAL",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "espacio_molecular",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["hidrógeno y oxígeno", "calor extremo", "salmuera"],
                        "poseId": "thinking_chin_hand",
                        "expresion": "analytical",
                        "infografia": {
                            "tipo": "dato_clave",
                            "titulo": "Fluidos Hidrotermales Profundos",
                            "subtitulo": "Presión de confinamiento a 9.000 metros",
                            "valorPrincipal": "3.000",
                            "unidad": "atmósferas",
                            "items": [
                                {"etiqueta": "Composición del agua", "valor": "Salmuera rica en minerales", "porcentaje": 100, "color": "#38BDF8"},
                                {"etiqueta": "Gases disueltos", "valor": "Metano, Helio y Nitrógeno", "porcentaje": 75, "color": "#F59E0B"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    }
                ]
            },
            {
                "id": "cap_4",
                "numero": 4,
                "titulo": "La Barrera Térmica de 180 Grados",
                "resumen": "La roca actuando como plástico fundido y destruyendo los taladros.",
                "escenas": [
                    {
                        "id": 7,
                        "texto": "Hacia mil novecientos ochenta y nueve, el pozo alcanzó doce mil doscientos sesenta y dos metros de profundidad. Pero allí los termómetros registraron un infierno inesperado: ciento ochenta grados centígrados, casi el doble de lo calculado.",
                        "tituloVisual": "180 GRADOS CENTIGRADOS",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "manto_terrestre",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_dramatic_hit.wav",
                        "volumenSfx": 0.25,
                        "palabrasClave": ["doce mil doscientos sesenta y dos metros", "ciento ochenta grados", "doble de lo calculado"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka",
                        "infografia": {
                            "tipo": "comparacion",
                            "titulo": "Gradiente Geotérmico Real vs Estimado",
                            "subtitulo": "Temperatura al fondo del pozo Kola",
                            "valorPrincipal": "180 °C",
                            "unidad": "temperatura real",
                            "items": [
                                {"etiqueta": "Pronóstico teórico soviético", "valor": "100 °C esperados", "porcentaje": 55, "color": "#38BDF8"},
                                {"etiqueta": "Temperatura real medida", "valor": "180 °C medidos al fondo", "porcentaje": 100, "color": "#EF4444"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    },
                    {
                        "id": 8,
                        "texto": "A esa temperatura y presión, la roca sólida dejó de comportarse como piedra y comenzó a fluir como goma de mascar caliente. Cada vez que extraían la broca de perforación para cambiar los diamantes desgastados, el agujero se cerraba sobre sí mismo como si fuera masa líquida.",
                        "tituloVisual": "ROCA VISCOSA",
                        "layout": "primer_plano",
                        "composicionVisual": "primer_plano",
                        "escenario": "manto_terrestre",
                        "transicion": "zoom_in",
                        "efectosCamara": ["punch"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["goma de mascar caliente", "broca de perforación", "masa líquida"],
                        "poseId": "thinking_chin_hand",
                        "expresion": "shocked"
                    }
                ]
            },
            {
                "id": "cap_5",
                "numero": 5,
                "titulo": "El Mito Urbano de los 'Sonidos del Infierno'",
                "resumen": "La leyenda del micrófono y la realidad acústica sísmica.",
                "escenas": [
                    {
                        "id": 9,
                        "texto": "En los años noventa surgió una infame leyenda urbana en medios internacionales: afirmaba que los ingenieros rusos habían bajado un micrófono térmico al pozo y habían grabado gritos agonizantes de almas condenadas en el infierno.",
                        "tituloVisual": "LA LEYENDA DEL INFIERNO",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "habitacion_noche",
                        "transicion": "fundido_negro",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_dramatic_hit.wav",
                        "volumenSfx": 0.25,
                        "palabrasClave": ["leyenda urbana", "micrófono térmico", "gritos agonizantes"],
                        "poseId": "thinking_chin_hand",
                        "expresion": "analytical"
                    },
                    {
                        "id": 10,
                        "texto": "La historia era un engaño inventado por un canal de televisión sensacionalista. Lo que realmente grabaron los geófonos sísmicos no fueron voces, sino el estremecedor gemido de la corteza terrestre sufriendo microfracturas por la colosal presión de las placas tectónicas.",
                        "tituloVisual": "ECOS TECTONICOS",
                        "layout": "primer_plano",
                        "composicionVisual": "primer_plano",
                        "escenario": "laboratorio",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["engaño inventado", "geófonos sísmicos", "gemido de la corteza"],
                        "poseId": "standing_confident",
                        "expresion": "smile_soft"
                    }
                ]
            },
            {
                "id": "cap_6",
                "numero": 6,
                "titulo": "La Tapa de Acero Olvidada",
                "resumen": "El cierre del pozo y la lección sobre los límites de la exploración.",
                "escenas": [
                    {
                        "id": 11,
                        "texto": "En mil novecientos noventa y dos las operaciones se detuvieron definitivamente. Hoy el complejo de Kola es una ruina industrial congelada en el Ártico, y sobre el agujero récord descansa una simple tapa metálica de acero atornillada al suelo.",
                        "tituloVisual": "LA TAPA DE ACERO",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "lunar",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["mil novecientos noventa y dos", "ruina industrial", "tapa metálica de acero"],
                        "poseId": "standing_confident",
                        "expresion": "analytical"
                    },
                    {
                        "id": 12,
                        "texto": "Esa pequeña tapa de veintitrés centímetros de diámetro nos recuerda una verdad humilde: hemos enviado sondas espaciales más allá de los confines del sistema solar, pero hacia el interior de nuestro propio planeta, apenas logramos arañar una tercera parte de la piel de una manzana.",
                        "tituloVisual": "LA PIEL DE LA MANZANA",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "vacio",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["veintitrés centímetros", "sondas espaciales", "piel de una manzana"],
                        "poseId": "standing_confident",
                        "expresion": "smile_soft"
                    }
                ]
            }
        ]
    }


def construir_doc_007_nemo():
    return {
        "meta": {
            "id": "doc_007_punto_nemo",
            "slug": "punto_nemo_cementerio_abismal_espacial",
            "titulo": "Punto Nemo: El Abismo más Solitario de la Tierra y Cementerio Espacial",
            "premisa": "El polo oceánico de inaccesibilidad en el Pacífico sur es el lugar más distante de cualquier tierra firme. Es tan remoto que las agencias espaciales lo eligieron como la tumba final de estaciones orbitales y satélites fuera de servicio.",
            "gancho": "¿Cuál es el rincón más aislado del planeta donde los humanos más cercanos viajan en el espacio?",
            "categoria": "Science & Technology",
            "duracionObjetivo": [400, 480],
            "fps": 30,
            "dimensiones": {"width": 1920, "height": 1080},
            "idioma": "es",
            "voz": "alex.conds.pt",
            "musicaPrincipal": "bgm/bgm.mp3",
            "volumenMusica": 0.12,
            "fuentes": [
                "Lukatela, H. (1992). Calculation of the Oceanic Pole of Inaccessibility.",
                "ESA (2018). Spacecraft Reentry and Ocean Impact Protocols.",
                "NASA Orbital Debris Program (2021). The South Pacific Oceanic Uninhabited Area."
            ],
            "tags": ["geografia", "punto nemo", "oceano", "espacio", "satelites", "ciencia", "documental"]
        },
        "capitulos": [
            {
                "id": "cap_1",
                "numero": 1,
                "titulo": "El Cálculo de la Soledad Absoluta",
                "resumen": "Cómo Hrvoje Lukatela calculó el punto más remoto en mil novecientos noventa y dos.",
                "escenas": [
                    {
                        "id": 1,
                        "texto": "En mil novecientos noventa y dos, el ingeniero croata canadiense Hrvoje Lukatela utilizó un sofisticado programa de geometría espacial para resolver una pregunta cartográfica: ¿cuál es el punto exacto del océano más alejado de cualquier costa del planeta?",
                        "tituloVisual": "HRVOJE LUKATELA, 1992",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "laboratorio",
                        "transicion": "fundido_negro",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_dramatic_hit.wav",
                        "volumenSfx": 0.25,
                        "palabrasClave": ["mil novecientos noventa y dos", "Hrvoje Lukatela", "geometría espacial"],
                        "poseId": "thinking_chin_hand",
                        "expresion": "analytical"
                    },
                    {
                        "id": 2,
                        "texto": "Las coordenadas halladas en el Pacífico sur quedaron fijadas a dos mil seiscientos ochenta y ocho kilómetros de tres islas deshabitadas idénticamente equidistantes: la isla Ducie al norte, Motu Nui al noreste y la isla Maher en la Antártida al sur.",
                        "tituloVisual": "2.688 KILOMETROS",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "abismo_oceanico",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["dos mil seiscientos ochenta y ocho kilómetros", "Pacífico sur", "tres islas deshabitadas"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka",
                        "infografia": {
                            "tipo": "dato_clave",
                            "titulo": "Polo de Inaccesibilidad Oceánica",
                            "subtitulo": "Distancia a la tierra más próxima",
                            "valorPrincipal": "2.688",
                            "unidad": "km de radio desierto",
                            "items": [
                                {"etiqueta": "Isla Ducie (Pitcairn)", "valor": "2.688 km al norte", "porcentaje": 100, "color": "#38BDF8"},
                                {"etiqueta": "Isla Maher (Antártida)", "valor": "2.688 km al sur", "porcentaje": 100, "color": "#94A3B8"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    }
                ]
            },
            {
                "id": "cap_2",
                "numero": 2,
                "titulo": "El Desierto Biológico Marino",
                "resumen": "La corriente del giro del Pacífico Sur y la ausencia de vida.",
                "escenas": [
                    {
                        "id": 3,
                        "texto": "A diferencia de las ricas costas marinas repletas de cardúmenes y algas, Punto Nemo se sitúa en el corazón del Giro del Pacífico Sur, una gigantesca corriente circular que impide la entrada de nutrientes desde los continentes.",
                        "tituloVisual": "DESIERTO BIOLOGICO",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "abismo_oceanico",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["Punto Nemo", "Giro del Pacífico Sur", "nutrientes"],
                        "poseId": "standing_confident",
                        "expresion": "analytical"
                    },
                    {
                        "id": 4,
                        "texto": "Sus aguas tienen tan poco fitoplancton que es uno de los lugares biológicamente más estériles del océano global. No hay aves marinas, apenas nadan peces y el fondo a cuatro mil metros es una llanura de lodo silencioso.",
                        "tituloVisual": "AGUAS ESTERILES",
                        "layout": "primer_plano",
                        "composicionVisual": "primer_plano",
                        "escenario": "abismo_oceanico",
                        "transicion": "whip_left",
                        "efectosCamara": ["punch"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["fitoplancton", "estériles del océano", "cuatro mil metros"],
                        "poseId": "thinking_chin_hand",
                        "expresion": "analytical"
                    }
                ]
            },
            {
                "id": "cap_3",
                "numero": 3,
                "titulo": "Los Astronautas como Vecinos más Cercanos",
                "resumen": "La paradoja de los cuatrocientos kilómetros en órbita.",
                "escenas": [
                    {
                        "id": 5,
                        "texto": "Si alguna vez navegaras en barco por el Punto Nemo, los seres humanos más cercanos a ti no estarían en ninguna isla ni en ningún puerto: serían los astronautas a bordo de la Estación Espacial Internacional cuando cruzan justo sobre tu cabeza.",
                        "tituloVisual": "VECINOS EN EL CIELO",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "espacio_profundo",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["Punto Nemo", "astronautas", "Estación Espacial Internacional"],
                        "poseId": "standing_confident",
                        "expresion": "smile_soft"
                    },
                    {
                        "id": 6,
                        "texto": "Mientras que cualquier costa terrestre dista casi dos mil setecientos kilómetros de ti, la estación espacial orbita a tan solo cuatrocientos kilómetros de altitud, haciendo que el cielo esté siete veces más próximo que la tierra firme.",
                        "tituloVisual": "400 KM VERTICALES",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "cabina_nave",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["dos mil setecientos kilómetros", "cuatrocientos kilómetros de altitud", "siete veces más próximo"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka",
                        "infografia": {
                            "tipo": "comparacion",
                            "titulo": "Proximidad Humana en Punto Nemo",
                            "subtitulo": "Distancia a la presencia humana más cercana",
                            "valorPrincipal": "7x",
                            "unidad": "más cerca del cielo",
                            "items": [
                                {"etiqueta": "Tripulación de la EEI", "valor": "400 km verticales", "porcentaje": 15, "color": "#38BDF8"},
                                {"etiqueta": "Población en tierra firme", "valor": "2.688 km horizontales", "porcentaje": 100, "color": "#F59E0B"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    }
                ]
            },
            {
                "id": "cap_4",
                "numero": 4,
                "titulo": "El Cementerio de Naves Espaciales",
                "resumen": "La caída de más de doscientas sesenta estructuras espaciales.",
                "escenas": [
                    {
                        "id": 7,
                        "texto": "Fue precisamente ese aislamiento extremo y la ausencia de rutas comerciales marinas lo que llevó a las agencias espaciales de Rusia, Europa, Japón y Estados Unidos a elegirlo como su vertedero orbital oficial.",
                        "tituloVisual": "EL DESTINO FINAL",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "cielo_dia",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_dramatic_hit.wav",
                        "volumenSfx": 0.25,
                        "palabrasClave": ["aislamiento extremo", "rutas comerciales", "agencias espaciales"],
                        "poseId": "standing_confident",
                        "expresion": "analytical"
                    },
                    {
                        "id": 8,
                        "texto": "Desde mil novecientos setenta y uno, más de doscientas sesenta naves espaciales han sido desorbitadas y dirigidas deliberadamente hacia este parche del Pacífico, incluyendo cargueros Progress, satélites espía y la famosa estación soviética Mir en dos mil uno.",
                        "tituloVisual": "+260 NAVES HUNDIDAS",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "abismo_oceanico",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["doscientas sesenta naves", "estación soviética Mir", "dos mil uno"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka",
                        "infografia": {
                            "tipo": "dato_clave",
                            "titulo": "Masa Tecnológica en el Fondo",
                            "subtitulo": "Titanio y aleaciones depositadas a 4.000 m",
                            "valorPrincipal": "140 T",
                            "unidad": "Estación Mir (2001)",
                            "items": [
                                {"etiqueta": "Fragmentos que sobreviven", "valor": "Aprox 20 a 40% de masa", "porcentaje": 30, "color": "#EF4444"},
                                {"etiqueta": "Naves quemadas en reentrada", "valor": "Desintegradas en atmósfera", "porcentaje": 70, "color": "#F59E0B"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    }
                ]
            },
            {
                "id": "cap_5",
                "numero": 5,
                "titulo": "La Caída Programada de la Estación Espacial",
                "resumen": "El retiro en dos mil treinta y uno de la mayor estructura humana orbital.",
                "escenas": [
                    {
                        "id": 9,
                        "texto": "Hacia el año dos mil treinta y uno, el mayor objeto jamás construido en el espacio llegará a su fin: la Estación Espacial Internacional, con más de cuatrocientas toneladas de peso y el tamaño de un campo de fútbol.",
                        "tituloVisual": "AÑO 2031: FIN DE LA EEI",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "espacio_profundo",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_dramatic_hit.wav",
                        "volumenSfx": 0.25,
                        "palabrasClave": ["dos mil treinta y uno", "Estación Espacial Internacional", "cuatrocientas toneladas"],
                        "poseId": "thinking_chin_hand",
                        "expresion": "analytical"
                    },
                    {
                        "id": 10,
                        "texto": "Tras encender sus últimos propulsores de frenado, la enorme estación reentrará envuelta en una bola de fuego supersónica sobre el océano y sus piezas de titanio blindado descansarán para siempre en el fondo abisal de Punto Nemo.",
                        "tituloVisual": "REENTRADA EN FUEGO",
                        "layout": "primer_plano",
                        "composicionVisual": "primer_plano",
                        "escenario": "cielo_dia",
                        "transicion": "whip_left",
                        "efectosCamara": ["punch"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["bola de fuego supersónica", "titanio blindado", "fondo abisal"],
                        "poseId": "standing_confident",
                        "expresion": "shocked"
                    }
                ]
            },
            {
                "id": "cap_6",
                "numero": 6,
                "titulo": "Donde Duerme el Metal en la Penumbra",
                "resumen": "Epílogo sobre el museo de tecnología sumergido.",
                "escenas": [
                    {
                        "id": 11,
                        "texto": "Bajo cuatro kilómetros de agua helada y en completa oscuridad descansa el museo aeroespacial más extraordinario del mundo: los restos retorcidos de la era de la exploración espacial que permitieron conectar a la humanidad sin que nadie viva cerca para contarlo.",
                        "tituloVisual": "EL MUSEO ABISAL",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "vacio",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["cuatro kilómetros de agua", "museo aeroespacial", "exploración espacial"],
                        "poseId": "standing_confident",
                        "expresion": "smile_soft"
                    }
                ]
            }
        ]
    }


def main():
    print("[CREAR] Generando documentales largos 6 y 7...")
    d6 = construir_doc_006_kola()
    d7 = construir_doc_007_nemo()

    with open(GUIONES_DIR / "doc_006_pozo_kola.json", "w", encoding="utf-8") as f:
        json.dump(d6, f, ensure_ascii=False, indent=2)

    with open(GUIONES_DIR / "doc_007_punto_nemo.json", "w", encoding="utf-8") as f:
        json.dump(d7, f, ensure_ascii=False, indent=2)

    print("✅ Documentales 6 y 7 exportados exitosamente.")


if __name__ == "__main__":
    main()
