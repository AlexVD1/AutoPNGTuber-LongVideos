#!/usr/bin/env python3
"""
Constructor de Guiones Largos 12 al 15 (16:9, 1920x1080)
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


def construir_doc_012_tardigrados():
    return {
        "meta": {
            "id": "doc_012_tardigrados",
            "slug": "tardigrados_criptobiosis_inmortalidad_biologica",
            "titulo": "Tardígrados: Los Amos de la Criptobiosis y los Límites de la Supervivencia",
            "premisa": "Los osos de agua miden menos de un milímetro, pero soportan temperaturas cercanas al cero absoluto, el vacío del espacio, radiación atómica y décadas sin una gota de agua vitrificando sus células con proteínas similares al vidrio.",
            "gancho": "¿Qué animal microscópico puede pausar su biología durante décadas y despertar intacto en una gota de agua?",
            "categoria": "Science & Technology",
            "duracionObjetivo": [400, 480],
            "fps": 30,
            "dimensiones": {"width": 1920, "height": 1080},
            "idioma": "es",
            "voz": "alex.conds.pt",
            "musicaPrincipal": "bgm/bgm.mp3",
            "volumenMusica": 0.12,
            "fuentes": [
                "Jönsson, K. I., et al. (2008). Tardigrades survive exposure to space in low Earth orbit. Current Biology.",
                "Boothby, T. C., et al. (2017). Tardigrades Use Intrinsically Disordered Proteins to Survive Desiccation. Molecular Cell.",
                "Hashimoto, T., et al. (2016). Extremotolerant tardigrade genome and its Dsup protein. Nature Communications."
            ],
            "tags": ["biologia", "tardigrados", "ciencia", "espacio", "criptobiosis", "evolucion", "documental"]
        },
        "capitulos": [
            {
                "id": "cap_1",
                "numero": 1,
                "titulo": "Los Osos de Agua Microscópicos",
                "resumen": "La anatomía y presencia ubicua de los tardígrados en la Tierra.",
                "escenas": [
                    {
                        "id": 1,
                        "texto": "Si tomas un trozo de musgo húmedo de cualquier árbol de tu vecindario y lo observas bajo una lupa de aumento, descubrirás a las criaturas más resilientes del planeta: los tardígrados u osos de agua.",
                        "tituloVisual": "LOS OSOS DE AGUA",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "laboratorio",
                        "transicion": "fundido_negro",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_dramatic_hit.wav",
                        "volumenSfx": 0.25,
                        "palabrasClave": ["trozo de musgo", "lupa de aumento", "osos de agua"],
                        "poseId": "standing_confident",
                        "expresion": "analytical"
                    },
                    {
                        "id": 2,
                        "texto": "Miden menos de medio milímetro de longitud, tienen ocho patas rechonchas armadas con garras afiladas y avanzan con un paso torpe y cómico. Pero no te dejes engañar por su aspecto tierno: han sobrevivido a las cinco extinciones masivas de la Tierra.",
                        "tituloVisual": "5 EXTINCIONES SUPERADAS",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "laboratorio",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["ocho patas rechonchas", "garras afiladas", "cinco extinciones masivas"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka",
                        "infografia": {
                            "tipo": "dato_clave",
                            "titulo": "Longevidad del Linaje",
                            "subtitulo": "Antigüedad en el registro fósil",
                            "valorPrincipal": "500 M",
                            "unidad": "años de existencia",
                            "items": [
                                {"etiqueta": "Sobrevivieron a dinosaurios", "valor": "Impacto de Chicxulub superado", "porcentaje": 100, "color": "#10B981"},
                                {"etiqueta": "Tamaño corporal", "valor": "0.3 a 0.5 milímetros", "porcentaje": 5, "color": "#38BDF8"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    }
                ]
            },
            {
                "id": "cap_2",
                "numero": 2,
                "titulo": "El Arte de la Criptobiosis",
                "resumen": "La deshidratación extrema del noventa y siete por ciento del cuerpo.",
                "escenas": [
                    {
                        "id": 3,
                        "texto": "Cuando el musgo donde habitan se seca por completo bajo el sol, la mayoría de los animales muere en cuestión de minutos. Los tardígrados hacen algo radical: apagan voluntariamente su propia vida.",
                        "tituloVisual": "APAGAR LA VIDA",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "espacio_molecular",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["musgo se seca", "apagan voluntariamente", "propia vida"],
                        "poseId": "thinking_chin_hand",
                        "expresion": "analytical"
                    },
                    {
                        "id": 4,
                        "texto": "Expulsan el noventa y siete por ciento del agua de sus tejidos, retraen la cabeza y sus ocho patas hacia el interior del caparazón y forman una esfera compacta y arrugada llamada tonel. Su metabolismo cae a menos de un cero punto cero un por ciento de lo normal: están biológicamente indistinguibles de la muerte.",
                        "tituloVisual": "ESTADO DE TONEL",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "laboratorio",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["noventa y siete por ciento", "esfera compacta", "indistinguibles de la muerte"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka",
                        "infografia": {
                            "tipo": "comparacion",
                            "titulo": "Metabolismo en Criptobiosis",
                            "subtitulo": "Tasa metabólica activa vs estado de tonel",
                            "valorPrincipal": "0.01%",
                            "unidad": "del metabolismo basal",
                            "items": [
                                {"etiqueta": "Agua corporal activa", "valor": "85% de peso en agua", "porcentaje": 100, "color": "#38BDF8"},
                                {"etiqueta": "Agua en estado de tonel", "valor": "Apenas 3% restante", "porcentaje": 3, "color": "#F59E0B"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    }
                ]
            },
            {
                "id": "cap_3",
                "numero": 3,
                "titulo": "El Escudo de Vidrio Biológico",
                "resumen": "Proteínas desordenadas TDP que vitrifican el interior celular.",
                "escenas": [
                    {
                        "id": 5,
                        "texto": "La congelación y deshidratación normal destruye las células humanas porque el agua forma cristales de hielo afilados que desgarran las membranas celulares y el ADN.",
                        "tituloVisual": "EL PELIGRO DEL HIELO",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "laboratorio",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["deshidratación normal", "cristales de hielo afilados", "membranas celulares"],
                        "poseId": "thinking_chin_hand",
                        "expresion": "analytical"
                    },
                    {
                        "id": 6,
                        "texto": "Los tardígrados sintetizan proteínas únicas en la naturaleza llamadas proteínas desordenadas de tardígrado. Al perder agua, estas moléculas no cristalizan: forman un gel vítreo amorfo similar al ámbar que inmoviliza y protege a las proteínas y cromosomas sin que se rompan.",
                        "tituloVisual": "ESCUDO DE CRISTAL",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "espacio_molecular",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["proteínas desordenadas", "gel vítreo amorfo", "inmoviliza y protege"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka",
                        "infografia": {
                            "tipo": "dato_clave",
                            "titulo": "Proteínas Vitrificantes TDP",
                            "subtitulo": "Biovidrio protector intracelular",
                            "valorPrincipal": "TDP-1",
                            "unidad": "matriz amorfa",
                            "items": [
                                {"etiqueta": "Proteína Dsup protectora", "valor": "Envuelve el ADN como armadura", "porcentaje": 100, "color": "#10B981"},
                                {"etiqueta": "Tolerancia a la desecación", "valor": "Más de 30 años en hibernación", "porcentaje": 100, "color": "#38BDF8"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    }
                ]
            },
            {
                "id": "cap_4",
                "numero": 4,
                "titulo": "Los Límites Extremos de la Física",
                "resumen": "Resistencia a menos doscientos setenta y dos grados, presión y radiación.",
                "escenas": [
                    {
                        "id": 7,
                        "texto": "En estado de criptobiosis, los tardígrados desafían las leyes de la supervivencia biológica. Científicos los han sumergido en helio líquido a doscientos setenta y dos grados centígrados bajo cero —a un solo grado del cero absoluto— y han sobrevivido.",
                        "tituloVisual": "-272 °C: CERO ABSOLUTO",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "laboratorio",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_dramatic_hit.wav",
                        "volumenSfx": 0.25,
                        "palabrasClave": ["helio líquido", "doscientos setenta y dos grados bajo cero", "cero absoluto"],
                        "poseId": "standing_confident",
                        "expresion": "analytical"
                    },
                    {
                        "id": 8,
                        "texto": "También soportan presiones de seis mil atmósferas —seis veces más aplastantes que en el fondo de la Fosa de las Marianas— y dosis de radiación ionizante mil veces superiores a las que matarían a un ser humano en segundos.",
                        "tituloVisual": "PRESION Y RADIACION",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "abismo_oceanico",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["seis mil atmósferas", "Fosa de las Marianas", "mil veces superiores"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka",
                        "infografia": {
                            "tipo": "comparacion",
                            "titulo": "Dosis Letal de Radiación Ionizante",
                            "subtitulo": "Tardígrado vs Ser Humano (en Grays)",
                            "valorPrincipal": "5.000 Gy",
                            "unidad": "dosis soportada por el tardígrado",
                            "items": [
                                {"etiqueta": "Ser humano mortal", "valor": "5 Grays (Letal en días)", "porcentaje": 1, "color": "#EF4444"},
                                {"etiqueta": "Tardígrado en tonel", "valor": "5.000 Grays (Sobrevive intacto)", "porcentaje": 100, "color": "#10B981"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    }
                ]
            },
            {
                "id": "cap_5",
                "numero": 5,
                "titulo": "El Experimento Espacial en Órbita",
                "resumen": "La misión Foton M3 de la Agencia Espacial Europea en dos mil siete.",
                "escenas": [
                    {
                        "id": 9,
                        "texto": "En dos mil siete, la Agencia Espacial Europea llevó el desafío al límite absoluto: cargó tardígrados deshidratados a bordo de la cápsula espacial FOTON eme tres y los expuso directamente al vacío exterior del espacio durante diez días enteros.",
                        "tituloVisual": "FOTON M3, 2007",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "espacio_profundo",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_dramatic_hit.wav",
                        "volumenSfx": 0.25,
                        "palabrasClave": ["dos mil siete", "Agencia Espacial Europea", "diez días enteros"],
                        "poseId": "thinking_chin_hand",
                        "expresion": "analytical"
                    },
                    {
                        "id": 10,
                        "texto": "Soportaron el vacío despresurizado y la radiación ultravioleta del Sol sin escafandra. Al regresar a la Tierra y recibir una simple gota de agua destilada, despertaron en treinta minutos, comenzaron a comer y tuvieron descendencia fértil.",
                        "tituloVisual": "EL DESPERTAR EN EL AGUA",
                        "layout": "primer_plano",
                        "composicionVisual": "primer_plano",
                        "escenario": "laboratorio",
                        "transicion": "whip_left",
                        "efectosCamara": ["punch"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["gota de agua destilada", "treinta minutos", "descendencia fértil"],
                        "poseId": "standing_confident",
                        "expresion": "smile_soft"
                    }
                ]
            },
            {
                "id": "cap_6",
                "numero": 6,
                "titulo": "La Lección de la Resiliencia de la Vida",
                "resumen": "Epílogo sobre los tardígrados y la posibilidad de vida en otros mundos.",
                "escenas": [
                    {
                        "id": 11,
                        "texto": "Los tardígrados son la prueba irrefutable de que la vida biológica es infinitamente más terca y tenaz de lo que creíamos. Nos demuestran que las semillas de la biología terrestre podrían viajar sobre meteoritos a través del vacío cósmico, recordándonos que en un universo hostil, la vida siempre encuentra un camino.",
                        "tituloVisual": "LA VIDA SIEMPRE VENCE",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "vacio",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["terca y tenaz", "semillas de la biología", "siempre encuentra un camino"],
                        "poseId": "standing_confident",
                        "expresion": "smile_soft"
                    }
                ]
            }
        ]
    }


def construir_doc_013_placebo():
    return {
        "meta": {
            "id": "doc_013_efecto_placebo",
            "slug": "efecto_placebo_farmacia_secreta_cerebro",
            "titulo": "El Efecto Placebo: Cómo tu Sistema Nervioso Fabrica Fármacos Reales por Creencia",
            "premisa": "Cuando crees firmemente que una pastilla inerte de azúcar o una inyección de agua salina es un fármaco potente, tu cerebro activa la producción bioquímica real de endorfinas, dopamina y opioides endógenos que alteran tu fisiología.",
            "gancho": "¿Cómo puede una simple pastilla de harina calmar el dolor físico y engañar a la química del cuerpo?",
            "categoria": "Science & Technology",
            "duracionObjetivo": [400, 480],
            "fps": 30,
            "dimensiones": {"width": 1920, "height": 1080},
            "idioma": "es",
            "voz": "alex.conds.pt",
            "musicaPrincipal": "bgm/bgm.mp3",
            "volumenMusica": 0.12,
            "fuentes": [
                "Beecher, H. K. (1955). The Powerful Placebo. JAMA.",
                "Benedetti, F. (2014). Placebo Effects: Understanding the Mechanisms in Health and Disease. Oxford.",
                "Wager, T. D., & Atlas, L. Y. (2015). The neuroscience of placebo effects. Nature Reviews Neuroscience."
            ],
            "tags": ["neurociencia", "medicina", "cerebro", "placebo", "psicologia", "mente", "documental"]
        },
        "capitulos": [
            {
                "id": "cap_1",
                "numero": 1,
                "titulo": "La Morfina Falsa de Henry Beecher",
                "resumen": "El descubrimiento en el frente de batalla de la Segunda Guerra Mundial.",
                "escenas": [
                    {
                        "id": 1,
                        "texto": "Durante la sangrienta batalla de Anzio en la Segunda Guerra Mundial, los hospitales militares de campaña desbordaban de soldados con heridas desgarradoras y la morfina líquida se agotó por completo.",
                        "tituloVisual": "ANZIO, 1944",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "habitacion_noche",
                        "transicion": "fundido_negro",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_dramatic_hit.wav",
                        "volumenSfx": 0.25,
                        "palabrasClave": ["batalla de Anzio", "Segunda Guerra Mundial", "morfina líquida"],
                        "poseId": "standing_confident",
                        "expresion": "analytical"
                    },
                    {
                        "id": 2,
                        "texto": "Desesperado por evitar el shock traumático, el anestesiólogo Henry Beecher llenó una jeringa con simple suero salino y le dijo al soldado herido que le inyectaba una dosis potente de analgésico. Para su asombro absoluto, el soldado se calmó y el dolor desapareció de verdad.",
                        "tituloVisual": "EL SUERO MILAGROSO",
                        "layout": "primer_plano",
                        "composicionVisual": "primer_plano",
                        "escenario": "laboratorio_neuro",
                        "transicion": "zoom_in",
                        "efectosCamara": ["punch"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["Henry Beecher", "suero salino", "dolor desapareció de verdad"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka"
                    }
                ]
            },
            {
                "id": "cap_2",
                "numero": 2,
                "titulo": "El Paper de 1955 que Sacudió la Medicina",
                "resumen": "La publicación de The Powerful Placebo en JAMA.",
                "escenas": [
                    {
                        "id": 3,
                        "texto": "Al regresar a los Estados Unidos, Beecher publicó en mil novecientos cincuenta y cinco un estudio histórico en la revista JAMA titulado El Poderoso Placebo, demostrando que un treinta y cinco por ciento de los pacientes mejoraba únicamente por la expectativa psicológica de la cura.",
                        "tituloVisual": "JAMA, 1955",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "laboratorio",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["mil novecientos cincuenta y cinco", "El Poderoso Placebo", "treinta y cinco por ciento"],
                        "poseId": "thinking_chin_hand",
                        "expresion": "analytical"
                    },
                    {
                        "id": 4,
                        "texto": "Durante décadas, la medicina tradicional descartó este fenómeno como mera imaginación o autosugestión de pacientes débiles. Pero la llegada de la resonancia magnética funcional a finales del siglo veinte destapó la verdad biológica.",
                        "tituloVisual": "NO ES IMAGINACION",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "laboratorio_neuro",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["autosugestión", "resonancia magnética funcional", "verdad biológica"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka",
                        "infografia": {
                            "tipo": "dato_clave",
                            "titulo": "Respuesta Clínica Promedio",
                            "subtitulo": "Efectividad medida en ensayos controlados ciegos",
                            "valorPrincipal": "35%",
                            "unidad": "de pacientes responden",
                            "items": [
                                {"etiqueta": "Alivio del dolor crónico", "valor": "Hasta 40% de reducción", "porcentaje": 40, "color": "#10B981"},
                                {"etiqueta": "Depresión y ansiedad", "valor": "Hasta 50% de respuesta", "porcentaje": 50, "color": "#38BDF8"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    }
                ]
            },
            {
                "id": "cap_3",
                "numero": 3,
                "titulo": "La Farmacia Bioquímica en el Tronco Encefálico",
                "resumen": "La síntesis real de endorfinas y dopamina en el sistema nervioso.",
                "escenas": [
                    {
                        "id": 5,
                        "texto": "Cuando una persona confía en que el tratamiento médico que recibe va a curarla, la corteza prefrontal del cerebro envía señales eléctricas directas hacia el área gris periacueductal del tronco encefálico.",
                        "tituloVisual": "CORTEZA PREFRONTAL",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "espacio_molecular",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["corteza prefrontal", "señales eléctricas", "tronco encefálico"],
                        "poseId": "standing_confident",
                        "expresion": "analytical"
                    },
                    {
                        "id": 6,
                        "texto": "Allí se activa una cascada de síntesis de endorfinas y encefalinas —sustancias químicas químicamente idénticas a la morfina— que bajan por la médula espinal cerrando los canales de transmisión del dolor antes de que lleguen a la conciencia.",
                        "tituloVisual": "OPIOIDES ENDOGENOS",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "laboratorio_neuro",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["endorfinas y encefalinas", "idénticas a la morfina", "canales del dolor"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka",
                        "infografia": {
                            "tipo": "comparacion",
                            "titulo": "Morfina Farmacéutica vs Endorfinas Cerebrales",
                            "subtitulo": "Afinidad por los receptores opioides Mu",
                            "valorPrincipal": "IDÉNTICA",
                            "unidad": "acción molecular",
                            "items": [
                                {"etiqueta": "Morfina externa", "valor": "Bloqueo receptores espinales", "porcentaje": 100, "color": "#EF4444"},
                                {"etiqueta": "Placebo cerebral", "valor": "Fabrica morfina interna natural", "porcentaje": 100, "color": "#10B981"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    }
                ]
            },
            {
                "id": "cap_4",
                "numero": 4,
                "titulo": "La Prueba Definitiva de la Naloxona",
                "resumen": "El experimento de Fabrizio Benedetti que silenció a los escépticos.",
                "escenas": [
                    {
                        "id": 7,
                        "texto": "El neurólogo italiano Fabrizio Benedetti realizó en los años noventa el experimento más brillante para acallar a los escépticos que seguían diciendo que el placebo era una fantasía psicológica.",
                        "tituloVisual": "FABRIZIO BENEDETTI",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "laboratorio",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_dramatic_hit.wav",
                        "volumenSfx": 0.25,
                        "palabrasClave": ["Fabrizio Benedetti", "experimento más brillante", "acallar escépticos"],
                        "poseId": "thinking_chin_hand",
                        "expresion": "analytical"
                    },
                    {
                        "id": 8,
                        "texto": "Inyectó un placebo a pacientes con dolor y confirmó el alivio. Luego, sin avisarles, les administró naloxona, un fármaco que bloquea químicamente los receptores de opioides en las neuronas. De inmediato, el efecto placebo desapareció por completo y el dolor regresó, demostrando que el cerebro estaba fabricando opioides reales.",
                        "tituloVisual": "NALOXONA: EL DETECTOR",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "espacio_molecular",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["administró naloxona", "bloquea químicamente", "opioides reales"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka",
                        "infografia": {
                            "tipo": "dato_clave",
                            "titulo": "Efecto de la Naloxona",
                            "subtitulo": "Bloqueo farmacológico del placebo",
                            "valorPrincipal": "0%",
                            "unidad": "alivio tras naloxona",
                            "items": [
                                {"etiqueta": "Placebo solo", "valor": "Dolor reducido notablemente", "porcentaje": 100, "color": "#10B981"},
                                {"etiqueta": "Placebo + Naloxona", "valor": "Dolor regresa de golpe", "porcentaje": 0, "color": "#EF4444"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    }
                ]
            },
            {
                "id": "cap_5",
                "numero": 5,
                "titulo": "La Psicología del Ritual Clínico y el Nocebo",
                "resumen": "El precio, el color de las pastillas y el lado oscuro del nocebo.",
                "escenas": [
                    {
                        "id": 9,
                        "texto": "La potencia del placebo depende fuertemente de la presentación: dos pastillas de azúcar funcionan mejor que una; las pastillas grandes curan más que las pequeñas; las inyecciones salinas son más potentes que las pastillas y las pastillas con precio caro alivian el doble que las etiquetadas como baratas.",
                        "tituloVisual": "EL PODER DEL RITUAL",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "galeria_diseno_retro",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["presentación", "inyecciones salinas", "precio caro"],
                        "poseId": "standing_confident",
                        "expresion": "analytical"
                    },
                    {
                        "id": 10,
                        "texto": "Pero el fenómeno tiene un hermano gemelo siniestro llamado nocebo: si un paciente lee la lista de efectos secundarios y cree con convicción que el medicamento le causará náuseas o mareos, su cerebro desencadenará esos síntomas físicos reales aunque la pastilla sea solo harina.",
                        "tituloVisual": "EL EFECTO NOCEBO",
                        "layout": "primer_plano",
                        "composicionVisual": "primer_plano",
                        "escenario": "habitacion_noche",
                        "transicion": "whip_left",
                        "efectosCamara": ["punch"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["efecto nocebo", "efectos secundarios", "pastilla sea solo harina"],
                        "poseId": "thinking_chin_hand",
                        "expresion": "shocked"
                    }
                ]
            },
            {
                "id": "cap_6",
                "numero": 6,
                "titulo": "El Puente entre Conciencia y Fisiología",
                "resumen": "Epílogo sobre la capacidad autocurativa del cuerpo humano.",
                "escenas": [
                    {
                        "id": 11,
                        "texto": "El efecto placebo no significa que las enfermedades sean imaginarias, sino que la mente no es un espectador pasivo de la biología celular. Poseemos dentro de nuestro cráneo la farmacia química más sofisticada del planeta, y apenas comenzamos a comprender las llaves que abren sus compuertas.",
                        "tituloVisual": "LA FARMACIA INTERNA",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "vacio",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["espectador pasivo", "farmacia química más sofisticada", "llaves que abren"],
                        "poseId": "standing_confident",
                        "expresion": "smile_soft"
                    }
                ]
            }
        ]
    }


def construir_doc_014_oxidacion():
    return {
        "meta": {
            "id": "doc_014_gran_oxidacion",
            "slug": "gran_oxidacion_cataclismo_oxigeno_tierra",
            "titulo": "La Gran Oxidación: Cuando el Oxígeno Casi Extermina toda la Vida Terrestre",
            "premisa": "Hace dos mil cuatrocientos millones de años, las primeras cianobacterias inventaron la fotosíntesis y liberaron tanto oxígeno que asfixiaron al noventa por ciento de los organismos del planeta, congelaron la Tierra entera y cambiaron la geología para siempre.",
            "gancho": "¿Sabías que el gas que hoy respiramos para vivir fue en el pasado la mayor catástrofe ambiental del planeta?",
            "categoria": "Science & Technology",
            "duracionObjetivo": [400, 480],
            "fps": 30,
            "dimensiones": {"width": 1920, "height": 1080},
            "idioma": "es",
            "voz": "alex.conds.pt",
            "musicaPrincipal": "bgm/bgm.mp3",
            "volumenMusica": 0.12,
            "fuentes": [
                "Holland, H. D. (2006). The oxygenation of the atmosphere and oceans. Phil. Trans. R. Soc. B.",
                "Lyons, T. W., et al. (2014). The rise of oxygen in Earth's early ocean and atmosphere. Nature.",
                "Kirschvink, J. L., et al. (2000). Paleoproterozoic snowball Earth: Extreme climactic and evolutionary events."
            ],
            "tags": ["paleontologia", "oxigeno", "geologia", "tierra", "evolucion", "fotosintesis", "documental"]
        },
        "capitulos": [
            {
                "id": "cap_1",
                "numero": 1,
                "titulo": "El Planeta Anaranjado y los Mares Verdes",
                "resumen": "La Tierra arcaica dominada por metano y bacterias anaerobias.",
                "escenas": [
                    {
                        "id": 1,
                        "texto": "Si pudieras viajar en el tiempo hace dos mil cuatrocientos millones de años, no reconocerías a nuestro mundo: los cielos eran anaranjados debido a una espesa bruma de metano y los océanos tenían un intenso color verde esmeralda por millones de toneladas de hierro disuelto.",
                        "tituloVisual": "HACE 2.400 MILLONES DE AÑOS",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "abismo_oceanico",
                        "transicion": "fundido_negro",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_dramatic_hit.wav",
                        "volumenSfx": 0.25,
                        "palabrasClave": ["dos mil cuatrocientos millones", "bruma de metano", "hierro disuelto"],
                        "poseId": "standing_confident",
                        "expresion": "analytical"
                    },
                    {
                        "id": 2,
                        "texto": "En ese mundo arcaico no había una sola molécula de oxígeno libre. La Tierra estaba habitada exclusivamente por colonias microscópicas de arqueas y bacterias anaerobias para quienes el oxígeno era un gas altamente corrosivo y mortal.",
                        "tituloVisual": "MUNDO ANAEROBIO",
                        "layout": "primer_plano",
                        "composicionVisual": "primer_plano",
                        "escenario": "espacio_molecular",
                        "transicion": "zoom_in",
                        "efectosCamara": ["punch"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["oxígeno libre", "bacterias anaerobias", "altamente corrosivo y mortal"],
                        "poseId": "thinking_chin_hand",
                        "expresion": "analytical"
                    }
                ]
            },
            {
                "id": "cap_2",
                "numero": 2,
                "titulo": "La Invención Letal de las Cianobacterias",
                "resumen": "La fotosíntesis oxigénica que rompió el equilibrio molecular.",
                "escenas": [
                    {
                        "id": 3,
                        "texto": "Entonces ocurrió una revolución silenciosa en las aguas poco profundas: un nuevo tipo de microbio verde azulado, las cianobacterias, desarrolló una maquinaria molecular asombrosa capaz de utilizar la luz solar para romper moléculas de agua y fabricar glucosa.",
                        "tituloVisual": "FOTOSINTESIS OXIGENICA",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "abismo_oceanico",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["cianobacterias", "maquinaria molecular", "romper moléculas de agua"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka"
                    },
                    {
                        "id": 4,
                        "texto": "Como desecho residual de esa reacción química, las cianobacterias expulsaban gas oxígeno. No lo producían para respirar: para ellas era basura química tóxica que arrojaban al agua marina en cantidades industriales cada segundo.",
                        "tituloVisual": "DESECHO QUIMICO",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "espacio_molecular",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["gas oxígeno", "basura química tóxica", "cantidades industriales"],
                        "poseId": "thinking_chin_hand",
                        "expresion": "analytical",
                        "infografia": {
                            "tipo": "dato_clave",
                            "titulo": "Reacción de la Fotosíntesis",
                            "subtitulo": "6CO₂ + 6H₂O + Luz -> Glucosa + 6O₂",
                            "valorPrincipal": "6 O₂",
                            "unidad": "oxígeno residual por molécula",
                            "items": [
                                {"etiqueta": "Energía capturada", "valor": "Luz solar abundante", "porcentaje": 100, "color": "#FFE600"},
                                {"etiqueta": "Gas venenoso emitido", "valor": "Oxígeno biatómico libre", "porcentaje": 100, "color": "#38BDF8"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    }
                ]
            },
            {
                "id": "cap_3",
                "numero": 3,
                "titulo": "La Oxidación de los Océanos y el Hierro en Bandas",
                "resumen": "El óxido que precipitó al lecho marino creando las minas de hierro actuales.",
                "escenas": [
                    {
                        "id": 5,
                        "texto": "Al principio, el oxígeno no se acumuló en el aire porque los océanos primitivos estaban repletos de hierro disuelto. El oxígeno reaccionó con el hierro oxidándolo instantáneamente y tiñendo los mares de rojo óxido.",
                        "tituloVisual": "OXIDACION SUBMARINA",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "abismo_oceanico",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["hierro disuelto", "tiñendo los mares", "rojo óxido"],
                        "poseId": "standing_confident",
                        "expresion": "analytical"
                    },
                    {
                        "id": 6,
                        "texto": "Miles de millones de toneladas de óxido de hierro se precipitaron al fondo marino durante cientos de millones de años formando las formaciones de hierro en bandas: los mismos yacimientos de mineral que la humanidad extrae hoy para fabricar todo el acero del mundo moderno.",
                        "tituloVisual": "FORMACIONES DE HIERRO",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "red_subterranea",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["toneladas de óxido", "hierro en bandas", "acero del mundo moderno"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka",
                        "infografia": {
                            "tipo": "dato_clave",
                            "titulo": "Banded Iron Formations (BIF)",
                            "subtitulo": "Origen del 90% del mineral de hierro industrial",
                            "valorPrincipal": "90%",
                            "unidad": "del acero global proviene de aquí",
                            "items": [
                                {"etiqueta": "Duración del depósito", "valor": "800 millones de años", "porcentaje": 100, "color": "#F97316"},
                                {"etiqueta": "Capas alternadas", "valor": "Hematita y sílice marina", "porcentaje": 80, "color": "#94A3B8"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    }
                ]
            },
            {
                "id": "cap_4",
                "numero": 4,
                "titulo": "La Gran Extinción y la Tierra Bola de Nieve",
                "resumen": "El colapso del metano y la glaciación huroniana de trescientos millones de años.",
                "escenas": [
                    {
                        "id": 7,
                        "texto": "Hacia hace dos mil cuatrocientos millones de años, todo el hierro marino se oxidó por completo y el sumidero se agotó. El oxígeno libre no tuvo adonde ir y comenzó a filtrarse masivamente hacia la atmósfera.",
                        "tituloVisual": "DESBORDE A LA ATMOSFERA",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "cielo_dia",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_dramatic_hit.wav",
                        "volumenSfx": 0.25,
                        "palabrasClave": ["sumidero se agotó", "filtrarse masivamente", "hacia la atmósfera"],
                        "poseId": "thinking_chin_hand",
                        "expresion": "analytical"
                    },
                    {
                        "id": 8,
                        "texto": "El resultado fue doblemente apocalíptico: el oxígeno reaccionó con el metano destruyendo el efecto invernadero que mantenía cálida a la Tierra, desatando la Glaciación Huroniana: trescientos millones de años de hielo global donde los océanos se congelaron bajo kilómetros de hielo.",
                        "tituloVisual": "TIERRA BOLA DE NIEVE",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "lunar",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["Glaciación Huroniana", "trescientos millones de años", "kilómetros de hielo"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka",
                        "infografia": {
                            "tipo": "comparacion",
                            "titulo": "El Colapso Climático Huroniano",
                            "subtitulo": "Destrucción del metano por el oxígeno libre",
                            "valorPrincipal": "-50 °C",
                            "unidad": "temperatura media global",
                            "items": [
                                {"etiqueta": "Duración de la glaciación", "valor": "300 millones de años", "porcentaje": 100, "color": "#38BDF8"},
                                {"etiqueta": "Mortalidad anaerobia", "valor": "90% de especies extintas", "porcentaje": 90, "color": "#EF4444"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    }
                ]
            },
            {
                "id": "cap_5",
                "numero": 5,
                "titulo": "La Invención de la Respiración Celular",
                "resumen": "El milagro metabólico que convirtió el veneno en combustible.",
                "escenas": [
                    {
                        "id": 9,
                        "texto": "Más del noventa por ciento de la biosfera arcaica se extinguió, pero un puñado de microbios supervivientes logró el mayor salto evolutivo de la historia: aprender a domesticar el veneno mediante la respiración celular.",
                        "tituloVisual": "DOMESTICAR EL VENENO",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "espacio_molecular",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["noventa por ciento", "respiración celular", "salto evolutivo"],
                        "poseId": "standing_confident",
                        "expresion": "analytical"
                    },
                    {
                        "id": 10,
                        "texto": "La respiración con oxígeno produce casi dieciocho veces más energía utilizable por cada molécula de glucosa que la fermentación anaerobia antigua. Esa sobredosis de energía fue el combustible obligatorio que permitió la aparición de células complejas, órganos, animales y cerebros pensantes.",
                        "tituloVisual": "18X MAS ENERGIA",
                        "layout": "primer_plano",
                        "composicionVisual": "primer_plano",
                        "escenario": "laboratorio",
                        "transicion": "whip_left",
                        "efectosCamara": ["punch"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["dieciocho veces más energía", "células complejas", "cerebros pensantes"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka"
                    }
                ]
            },
            {
                "id": "cap_6",
                "numero": 6,
                "titulo": "El Hilo Invisible que Conecta el Pasado con tus Pulmones",
                "resumen": "Epílogo sobre el equilibrio que nos permite vivir hoy.",
                "escenas": [
                    {
                        "id": 11,
                        "texto": "Cada bocanada de aire que entra a tus pulmones es el residuo tóxico de una catástrofe planetaria que casi aniquiló la Tierra. La vida no solo se adapta a los desastres de la naturaleza: transforma los venenos del pasado en el motor sagrado de su propia existencia.",
                        "tituloVisual": "EL VENENO VITAL",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "vacio",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["bocanada de aire", "catástrofe planetaria", "motor sagrado"],
                        "poseId": "standing_confident",
                        "expresion": "smile_soft"
                    }
                ]
            }
        ]
    }


def construir_doc_015_oklo():
    return {
        "meta": {
            "id": "doc_015_reactor_oklo",
            "slug": "reactor_nuclear_natural_oklo_gabon",
            "titulo": "El Reactor Nuclear Natural de Oklo: Fisión Atómica Espontánea Hace Dos Mil Millones de Años",
            "premisa": "En 1972, científicos franceses descubrieron que una mina de uranio en Gabón tenía un déficit de isótopo doscientos treinta y cinco. La Tierra había encendido por sí misma reactores nucleares de fisión natural dos mil millones de años antes de que existieran los humanos.",
            "gancho": "¿Construyó la humanidad el primer reactor atómico o la Tierra ya fabricaba energía nuclear hace eones?",
            "categoria": "Science & Technology",
            "duracionObjetivo": [400, 480],
            "fps": 30,
            "dimensiones": {"width": 1920, "height": 1080},
            "idioma": "es",
            "voz": "alex.conds.pt",
            "musicaPrincipal": "bgm/bgm.mp3",
            "volumenMusica": 0.12,
            "fuentes": [
                "Bodu, R., et al. (1972). Sur l'existence d'anomalies isotopiques dans l'uranium d'Oklo. C. R. Acad. Sci. Paris.",
                "Meshik, A. P. (2005). The Workings of an Ancient Nuclear Reactor. Scientific American.",
                "Kuroda, P. K. (1956). On the Nuclear Physical Stability of the Uranium Minerals. J. Chem. Phys."
            ],
            "tags": ["geologia", "nuclear", "oklo", "ciencia", "historia", "energia", "documental"]
        },
        "capitulos": [
            {
                "id": "cap_1",
                "numero": 1,
                "titulo": "El Misterio del Uranio Faltante en Francia",
                "resumen": "La alarma de seguridad en la planta de enriquecimiento de Pierrelatte en mil novecientos setenta y dos.",
                "escenas": [
                    {
                        "id": 1,
                        "texto": "En mayo de mil novecientos setenta y dos, inspectores de control de calidad en la planta de enriquecimiento de uranio de Pierrelatte, en Francia, descubrieron una discrepancia analítica que desató el pánico de un posible robo de material atómico.",
                        "tituloVisual": "PIERRELATTE, 1972",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "laboratorio",
                        "transicion": "fundido_negro",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_dramatic_hit.wav",
                        "volumenSfx": 0.25,
                        "palabrasClave": ["mil novecientos setenta y dos", "Pierrelatte Francia", "robo de material atómico"],
                        "poseId": "standing_confident",
                        "expresion": "analytical"
                    },
                    {
                        "id": 2,
                        "texto": "En cualquier roca de la Tierra, en la Luna y en los meteoritos, el uranio doscientos treinta y cinco fisible representa con absoluta precisión el cero punto setecientos veinte por ciento de todo el uranio. Pero el lote llegado de una mina en Oklo, Gabón, tenía solo cero punto setecientos diecisiete por ciento: faltaban doscientos kilos de uranio apto para bombas.",
                        "tituloVisual": "FALTAN 200 KILOS",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "laboratorio",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["cero punto setecientos veinte por ciento", "Oklo Gabón", "doscientos kilos de uranio"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka",
                        "infografia": {
                            "tipo": "dato_clave",
                            "titulo": "Déficit Isotópico Crítico",
                            "subtitulo": "Concentración de U-235 en el mineral de Oklo",
                            "valorPrincipal": "0.717%",
                            "unidad": "vs 0.720% estándar cósmico",
                            "items": [
                                {"etiqueta": "Uranio 235 consumido", "valor": "Aprox 200 kilogramos", "porcentaje": 100, "color": "#EF4444"},
                                {"etiqueta": "Isótopos hijos detectados", "valor": "Neodimio y Rutenio fisiles", "porcentaje": 100, "color": "#10B981"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    }
                ]
            },
            {
                "id": "cap_2",
                "numero": 2,
                "titulo": "La Hipótesis Olvidada de Paul Kuroda",
                "resumen": "La predicción teórica de mil novecientos cincuenta y seis sobre reactores fósiles.",
                "escenas": [
                    {
                        "id": 3,
                        "texto": "Temiendo un contrabando ilícito para armamento nuclear clandestino, la Comisión de Energía Atómica francesa envió una comisión científica urgente a las minas de Oklo en África occidental.",
                        "tituloVisual": "EXPEDICION A GABON",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "red_subterranea",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["contrabando ilícito", "Comisión de Energía Atómica", "África occidental"],
                        "poseId": "thinking_chin_hand",
                        "expresion": "analytical"
                    },
                    {
                        "id": 4,
                        "texto": "Allí recordaron la audaz predicción que el químico nuclear Paul Kuroda había formulado en mil novecientos cincuenta y seis: bajo condiciones geológicas muy particulares, la naturaleza podía ensamblar reactores de fisión nuclear autónomos sin ayuda humana.",
                        "tituloVisual": "PAUL KURODA, 1956",
                        "layout": "primer_plano",
                        "composicionVisual": "primer_plano",
                        "escenario": "laboratorio",
                        "transicion": "whip_left",
                        "efectosCamara": ["punch"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["Paul Kuroda", "condiciones geológicas", "sin ayuda humana"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka"
                    }
                ]
            },
            {
                "id": "cap_3",
                "numero": 3,
                "titulo": "El Enriquecimiento Natural de Hace Dos Mil Millones de Años",
                "resumen": "La abundancia del tres por ciento de uranio doscientos treinta y cinco en el pasado.",
                "escenas": [
                    {
                        "id": 5,
                        "texto": "El uranio doscientos treinta y cinco es inestable y se desintegra más rápido que el uranio doscientos treinta y ocho. Por eso, hace dos mil millones de años su concentración en la corteza terrestre era mucho mayor: rondaba el tres por ciento, exactamente la misma proporción a la que hoy enriquecemos el combustible nuclear comercial.",
                        "tituloVisual": "3% DE CONCENTRACION",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "espacio_molecular",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["dos mil millones de años", "tres por ciento", "enriquecemos el combustible"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka",
                        "infografia": {
                            "tipo": "comparacion",
                            "titulo": "Evolución Temporal del Uranio 235",
                            "subtitulo": "Desintegración radiactiva a lo largo de eones",
                            "valorPrincipal": "3%",
                            "unidad": "concentración hace 2.000 Ma",
                            "items": [
                                {"etiqueta": "Hace 2.000 millones de años", "valor": "3% (Combustible natural)", "porcentaje": 100, "color": "#10B981"},
                                {"etiqueta": "En la actualidad", "valor": "0.72% (Demasiado diluido)", "porcentaje": 24, "color": "#94A3B8"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    },
                    {
                        "id": 6,
                        "texto": "En los sedimentos fluviales de Oklo, ríos antiguos concentraron gruesas vetas de uraninita de hasta un metro de espesor en arenisca porosa, alcanzando la masa crítica requerida para encender una reacción neutrónica sostenida.",
                        "tituloVisual": "MASA CRITICA GEOLOGICA",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "red_subterranea",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["sedimentos fluviales", "uraninita", "masa crítica"],
                        "poseId": "standing_confident",
                        "expresion": "analytical"
                    }
                ]
            },
            {
                "id": "cap_4",
                "numero": 4,
                "titulo": "El Agua como Moderador Cíclico Tipo Géiser",
                "resumen": "El ciclo autorregulado de treinta minutos activo y dos horas y media de enfriamiento.",
                "escenas": [
                    {
                        "id": 7,
                        "texto": "Para que la fisión nuclear funcione, los neutrones rápidos deben desacelerarse con un moderador. En Oklo, ese moderador fue el agua subterránea que se filtraba a través de las grietas de la roca arenisca.",
                        "tituloVisual": "EL AGUA MODERADORA",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "red_subterranea",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_dramatic_hit.wav",
                        "volumenSfx": 0.25,
                        "palabrasClave": ["fisión nuclear", "moderador", "agua subterránea"],
                        "poseId": "thinking_chin_hand",
                        "expresion": "analytical"
                    },
                    {
                        "id": 8,
                        "texto": "Cuando el agua penetraba, la reacción atómica se encendía y generaba calor. Al alcanzar trescientos grados centígrados, el agua hervía convirtiéndose en vapor y escapaba como un géiser hacia la superficie. Al desaparecer el agua líquida, los neutrones ya no podían moderarse y el reactor se apagaba de forma automática hasta que la roca se enfriaba y el agua volvía a entrar.",
                        "tituloVisual": "CICLO GEISER DE 3 HORAS",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "red_subterranea",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["trescientos grados centígrados", "escapaba como un géiser", "apagaba de forma automática"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka",
                        "infografia": {
                            "tipo": "dato_clave",
                            "titulo": "Ciclo Térmico de Oklo",
                            "subtitulo": "Autorregulación hidrodinámica natural",
                            "valorPrincipal": "3 HORAS",
                            "unidad": "por ciclo completo",
                            "items": [
                                {"etiqueta": "Fase de fisión activa", "valor": "30 minutos (Calentamiento)", "porcentaje": 17, "color": "#EF4444"},
                                {"etiqueta": "Fase de enfriamiento", "valor": "150 minutos (Infiltración)", "porcentaje": 83, "color": "#38BDF8"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    }
                ]
            },
            {
                "id": "cap_5",
                "numero": 5,
                "titulo": "Cientos de Miles de Años de Energía Limpia",
                "resumen": "Dieciséis zonas de reactores operando sin fusión catastrófica.",
                "escenas": [
                    {
                        "id": 9,
                        "texto": "Se descubrieron al menos dieciséis zonas de reactores independientes en la región de Oklo. Estos reactores operaron pacíficamente durante cientos de miles de años, produciendo una potencia térmica promedio constante de unos cien kilovatios.",
                        "tituloVisual": "16 REACTORES NATURALES",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "manto_terrestre",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["dieciséis zonas", "cientos de miles de años", "cien kilovatios"],
                        "poseId": "standing_confident",
                        "expresion": "analytical"
                    },
                    {
                        "id": 10,
                        "texto": "A diferencia de Chernobyl o Fukushima, los reactores de Oklo jamás sufrieron una explosión descontrolada: el ingenioso ciclo natural de retroalimentación de vapor apagaba la reacción antes de que pudiera sobrecalentarse.",
                        "tituloVisual": "SEGURIDAD NATURAL",
                        "layout": "primer_plano",
                        "composicionVisual": "primer_plano",
                        "escenario": "laboratorio",
                        "transicion": "whip_left",
                        "efectosCamara": ["punch"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["Chernobyl o Fukushima", "jamás sufrieron una explosión", "retroalimentación de vapor"],
                        "poseId": "standing_confident",
                        "expresion": "smile_soft"
                    }
                ]
            },
            {
                "id": "cap_6",
                "numero": 6,
                "titulo": "La Lección Geológica para el Almacenamiento Nuclear",
                "resumen": "Epílogo sobre los desechos radiactivos confinados durante dos mil millones de años.",
                "escenas": [
                    {
                        "id": 11,
                        "texto": "El legado más valioso de Oklo para la ingeniería moderna es el destino de sus residuos radiactivos: elementos como el plutonio y los actínidos generados durante la fisión permanecieron inmovilizados en la estructura cristalina de la roca sin desplazarse más de unos pocos centímetros durante dos mil millones de años. La Tierra demostró que la roca profunda es el almacén nuclear más seguro y eterno del universo.",
                        "tituloVisual": "CONFINAMIENTO ETERNO",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "vacio",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["residuos radiactivos", "pocos centímetros", "almacén nuclear más seguro"],
                        "poseId": "standing_confident",
                        "expresion": "smile_soft"
                    }
                ]
            }
        ]
    }


def main():
    print("[CREAR] Generando documentales largos 12 al 15...")
    d12 = construir_doc_012_tardigrados()
    d13 = construir_doc_013_placebo()
    d14 = construir_doc_014_oxidacion()
    d15 = construir_doc_015_oklo()

    with open(GUIONES_DIR / "doc_012_tardigrados.json", "w", encoding="utf-8") as f:
        json.dump(d12, f, ensure_ascii=False, indent=2)

    with open(GUIONES_DIR / "doc_013_efecto_placebo.json", "w", encoding="utf-8") as f:
        json.dump(d13, f, ensure_ascii=False, indent=2)

    with open(GUIONES_DIR / "doc_014_gran_oxidacion.json", "w", encoding="utf-8") as f:
        json.dump(d14, f, ensure_ascii=False, indent=2)

    with open(GUIONES_DIR / "doc_015_reactor_oklo.json", "w", encoding="utf-8") as f:
        json.dump(d15, f, ensure_ascii=False, indent=2)

    print("✅ Documentales 12 al 15 exportados exitosamente.")


if __name__ == "__main__":
    main()
