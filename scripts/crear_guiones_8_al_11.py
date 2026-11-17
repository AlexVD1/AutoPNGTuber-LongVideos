#!/usr/bin/env python3
"""
Constructor de Guiones Largos 8 al 11 (16:9, 1920x1080)
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


def construir_doc_008_cordyceps():
    return {
        "meta": {
            "id": "doc_008_hongo_cordyceps",
            "slug": "hongo_zombi_cordyceps_control_biologico",
            "titulo": "Ophiocordyceps: La Maquinaria Celular del Hongo Zombi en la Selva",
            "premisa": "En los bosques tropicales, un hongo parásito manipula químicamente el sistema muscular de las hormigas carpinteras, convirtiéndolas en títeres biológicos para asegurar la dispersión de sus esporas letales.",
            "gancho": "¿Existe un parásito en la naturaleza capaz de secuestrar el cuerpo de otro ser vivo sin tocar su cerebro?",
            "categoria": "Science & Technology",
            "duracionObjetivo": [400, 480],
            "fps": 30,
            "dimensiones": {"width": 1920, "height": 1080},
            "idioma": "es",
            "voz": "alex.conds.pt",
            "musicaPrincipal": "bgm/bgm.mp3",
            "volumenMusica": 0.12,
            "fuentes": [
                "Hughes, D. P., et al. (2011). Behavioral mechanisms of zombie ants. BMC Ecology.",
                "Fredericksen, M. A., et al. (2017). 3D reconstruction of fungal networks in zombie ants. PNAS.",
                "Mangold, C. A., et al. (2019). Host manipulation by Ophiocordyceps unilateralis. Science Advances."
            ],
            "tags": ["biologia", "cordyceps", "parasitos", "naturaleza", "ciencia", "hormigas", "documental"]
        },
        "capitulos": [
            {
                "id": "cap_1",
                "numero": 1,
                "titulo": "La Espora Invisible en el Dosel",
                "resumen": "La caída de la espora y la penetración mecánica del exoesqueleto.",
                "escenas": [
                    {
                        "id": 1,
                        "texto": "En lo profundo de las selvas tropicales de Tailandia y Brasil, una hormiga carpintera de la especie Camponotus leonardi desciende desde la copa de los árboles para recolectar alimento en el suelo selvático.",
                        "tituloVisual": "SELVA TROPICAL",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "cielo_dia",
                        "transicion": "fundido_negro",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_dramatic_hit.wav",
                        "volumenSfx": 0.25,
                        "palabrasClave": ["selvas tropicales", "hormiga carpintera", "suelo selvático"],
                        "poseId": "standing_confident",
                        "expresion": "analytical"
                    },
                    {
                        "id": 2,
                        "texto": "Al rozar una hoja húmeda, una espora microscópica de Ophiocordyceps se adhiere a su caparazón de quitina. En cuestión de horas, la espora secreta enzimas ácidas que disuelven la armadura del insecto y penetra silenciosamente hacia su hemolinfa.",
                        "tituloVisual": "INFECCION QUIMICA",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "espacio_molecular",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["Ophiocordyceps", "caparazón de quitina", "enzimas ácidas"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka",
                        "infografia": {
                            "tipo": "dato_clave",
                            "titulo": "Invasión Cuticular",
                            "subtitulo": "Velocidad de penetración enzimática",
                            "valorPrincipal": "12 HORAS",
                            "unidad": "tiempo de entrada",
                            "items": [
                                {"etiqueta": "Diámetro de la espora", "valor": "5 a 8 micrómetros", "porcentaje": 10, "color": "#38BDF8"},
                                {"etiqueta": "Carga letal", "valor": "1 sola espora basta", "porcentaje": 100, "color": "#EF4444"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    }
                ]
            },
            {
                "id": "cap_2",
                "numero": 2,
                "titulo": "La Infiltración Muscular: El Cerebro Intacto",
                "resumen": "Cómo el hongo coloniza los músculos sin dañar el sistema nervioso.",
                "escenas": [
                    {
                        "id": 3,
                        "texto": "Durante décadas se creyó que el parásito invadía el cerebro de la hormiga para controlar sus pensamientos. Pero en dos mil diecisiete, reconstrucciones en tres dimensiones de la Universidad Estatal de Pensilvania revelaron algo mucho más escalofriante.",
                        "tituloVisual": "HALLAZGO EN 3D",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "laboratorio",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["dos mil diecisiete", "reconstrucciones en tres dimensiones", "escalofriante"],
                        "poseId": "thinking_chin_hand",
                        "expresion": "analytical"
                    },
                    {
                        "id": 4,
                        "texto": "El cerebro de la hormiga permanece intacto y consciente. El hongo prolifera formando una red celular continua que envuelve cada fibra muscular de sus patas y mandíbulas, cortando la comunicación entre el cerebro y los músculos para mover mecánicamente al insecto como una marioneta biológica.",
                        "tituloVisual": "RED MUSCULAR",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "espacio_molecular",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["cerebro intacto", "red celular continua", "marioneta biológica"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka",
                        "infografia": {
                            "tipo": "comparacion",
                            "titulo": "Colonización Anatómica del Huésped",
                            "subtitulo": "Distribución de biomasa fúngica en la hormiga",
                            "valorPrincipal": "50%",
                            "unidad": "del cuerpo es hongo",
                            "items": [
                                {"etiqueta": "Músculos y mandíbulas", "valor": "Completamente infiltrados", "porcentaje": 100, "color": "#EF4444"},
                                {"etiqueta": "Cerebro", "valor": "0% invadido (intacto)", "porcentaje": 0, "color": "#10B981"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    }
                ]
            },
            {
                "id": "cap_3",
                "numero": 3,
                "titulo": "La Marcha de la Muerte a 25 Centímetros",
                "resumen": "La precisión microclimática del comportamiento inducido.",
                "escenas": [
                    {
                        "id": 5,
                        "texto": "Bajo el control químico del invasor, la hormiga abandona a su colonia en el dosel y desciende hacia el sotobosque en una marcha torpe y descoordinada. El parásito la guía con precisión milimétrica hacia la cara inferior de una hoja orientada hacia el norte.",
                        "tituloVisual": "MARCHA FORZADA",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "habitacion_noche",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["abandona a su colonia", "sotobosque", "orientada hacia el norte"],
                        "poseId": "standing_confident",
                        "expresion": "analytical"
                    },
                    {
                        "id": 6,
                        "texto": "Y la altura elegida jamás es aleatoria: exactamente veinticinco centímetros por encima del suelo. A esa altura precisa, la humedad del noventa y cuatro por ciento y la temperatura de veinticinco grados centígrados crean la incubadora ideal para que el hongo prospere.",
                        "tituloVisual": "PRECISION DE 25 CM",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "laboratorio",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["veinticinco centímetros", "humedad del noventa y cuatro", "veinticinco grados centígrados"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka",
                        "infografia": {
                            "tipo": "dato_clave",
                            "titulo": "Microclima de Fructificación",
                            "subtitulo": "Condiciones a 25 centímetros del suelo",
                            "valorPrincipal": "94%",
                            "unidad": "humedad relativa",
                            "items": [
                                {"etiqueta": "Temperatura media", "valor": "25 grados Celsius", "porcentaje": 80, "color": "#F59E0B"},
                                {"etiqueta": "Tasa de germinación", "valor": "Máxima viabilidad", "porcentaje": 100, "color": "#10B981"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    }
                ]
            },
            {
                "id": "cap_4",
                "numero": 4,
                "titulo": "El Mordisco Final y el Bloqueo Mandibular",
                "resumen": "La contracción irreversible de las mandíbulas al mediodía solar.",
                "escenas": [
                    {
                        "id": 7,
                        "texto": "Al mediodía solar exacto, el hongo desencadena una descarga química masiva que atrofia las fibras musculares de la mandíbula, obligando a la hormiga a clavar sus tenazas con fuerza extrema en la vena principal de la hoja.",
                        "tituloVisual": "MEDIODIA SOLAR",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "cielo_dia",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_dramatic_hit.wav",
                        "volumenSfx": 0.25,
                        "palabrasClave": ["mediodía solar", "descarga química masiva", "fuerza extrema"],
                        "poseId": "standing_confident",
                        "expresion": "analytical"
                    },
                    {
                        "id": 8,
                        "texto": "Las células fúngicas disuelven el tejido conectivo de la mandíbula dejándola bloqueada de forma irreversible en un espasmo mortal. La hormiga queda anclada como una grapa metálica; horas después, el insecto muere y el parásito consume sus órganos internos.",
                        "tituloVisual": "BLOQUEO IRREVERSIBLE",
                        "layout": "primer_plano",
                        "composicionVisual": "primer_plano",
                        "escenario": "espacio_molecular",
                        "transicion": "whip_left",
                        "efectosCamara": ["punch"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["espasmo mortal", "grapa metálica", "consume sus órganos"],
                        "poseId": "thinking_chin_hand",
                        "expresion": "shocked"
                    }
                ]
            },
            {
                "id": "cap_5",
                "numero": 5,
                "titulo": "La Erupción del Estroma Fúngico",
                "resumen": "El brote que atraviesa la cabeza y dispara millones de esporas.",
                "escenas": [
                    {
                        "id": 9,
                        "texto": "Tras varios días alimentándose del cadáver desde dentro, una aguja carnosa llamada estroma brota perforando la parte posterior de la cabeza de la hormiga muerta, creciendo varios centímetros en el aire.",
                        "tituloVisual": "EL BROTE CARNOSO",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "habitacion_noche",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["estroma brota", "parte posterior de la cabeza", "hormiga muerta"],
                        "poseId": "standing_confident",
                        "expresion": "analytical"
                    },
                    {
                        "id": 10,
                        "texto": "En la punta del tallo madura una cápsula que estalla liberando una nube de millones de esporas sobre los senderos de forrajeo que cruzan las demás hormigas en el suelo, garantizando que el ciclo continúe durante miles de generaciones.",
                        "tituloVisual": "LLUVIA DE ESPORAS",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "espacio_profundo",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["nube de millones de esporas", "senderos de forrajeo", "miles de generaciones"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka",
                        "infografia": {
                            "tipo": "dato_clave",
                            "titulo": "Área de Contagio Fúngico",
                            "subtitulo": "Radio de dispersión bajo la hoja mordida",
                            "valorPrincipal": "2 M²",
                            "unidad": "zona de exterminio",
                            "items": [
                                {"etiqueta": "Esporas expulsadas", "valor": "Cientos de miles por cápsula", "porcentaje": 100, "color": "#A855F7"},
                                {"etiqueta": "Defensa de la colonia", "valor": "Entierro y aislamiento de zombis", "porcentaje": 80, "color": "#10B981"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    }
                ]
            },
            {
                "id": "cap_6",
                "numero": 6,
                "titulo": "La Sofisticación de la Guerra Biológica",
                "resumen": "Epílogo sobre la evolución molecular sin sistema nervioso central.",
                "escenas": [
                    {
                        "id": 11,
                        "texto": "Ophiocordyceps es un recordatorio demoledor de que la inteligencia en la naturaleza no requiere un cerebro: una red de células fúngicas microscópicas puede dominar con precisión robótica a un animal entero mediante pura química evolutiva destilada a lo largo de cuarenta y ocho millones de años.",
                        "tituloVisual": "LA QUIMICA EVOLUTIVA",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "vacio",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["inteligencia en la naturaleza", "precisión robótica", "cuarenta y ocho millones de años"],
                        "poseId": "standing_confident",
                        "expresion": "smile_soft"
                    }
                ]
            }
        ]
    }


def construir_doc_009_olbers():
    return {
        "meta": {
            "id": "doc_009_paradoja_olbers",
            "slug": "paradoja_olbers_oscuridad_cosmos_infinito",
            "titulo": "La Paradoja de Olbers: Por qué la Noche es Negra en un Cosmos Infinito",
            "premisa": "Si el universo tuviera infinitas estrellas en todas direcciones, cada línea de visión toparía con una superficie ardiente y la noche brillaría con la intensidad del Sol. La oscuridad nocturna es la prueba viviente del Big Bang.",
            "gancho": "¿Por qué el cielo nocturno es negro si existen incontables estrellas brillando?",
            "categoria": "Science & Technology",
            "duracionObjetivo": [400, 480],
            "fps": 30,
            "dimensiones": {"width": 1920, "height": 1080},
            "idioma": "es",
            "voz": "alex.conds.pt",
            "musicaPrincipal": "bgm/bgm.mp3",
            "volumenMusica": 0.12,
            "fuentes": [
                "Olbers, H. W. M. (1826). Über die Durchsichtigkeit des Weltraums. Astronomisches Jahrbuch.",
                "Harrison, E. (1987). Darkness at Night: A Riddle of the Universe. Harvard University Press.",
                "Wesson, P. S. (1991). Olbers's Paradox and the Spectral Intensity of the Extragalactic Background Light."
            ],
            "tags": ["astronomia", "olbers", "cosmologia", "universo", "luz", "big bang", "ciencia", "documental"]
        },
        "capitulos": [
            {
                "id": "cap_1",
                "numero": 1,
                "titulo": "La Pregunta de Heinrich Olbers",
                "resumen": "La paradoja formulada en mil ochocientos veintitrés.",
                "escenas": [
                    {
                        "id": 1,
                        "texto": "En mil ochocientos veintitrés, el médico y astrónomo alemán Heinrich Olbers planteó un dilema que desconcertó a las mentes más brillantes de su tiempo: ¿por qué la noche es oscura?",
                        "tituloVisual": "ALEMANIA, 1823",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "habitacion_noche",
                        "transicion": "fundido_negro",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_dramatic_hit.wav",
                        "volumenSfx": 0.25,
                        "palabrasClave": ["mil ochocientos veintitrés", "Heinrich Olbers", "noche es oscura"],
                        "poseId": "thinking_chin_hand",
                        "expresion": "analytical"
                    },
                    {
                        "id": 2,
                        "texto": "A primera vista parece una tontería infantil: la noche es oscura porque el Sol se oculta tras el horizonte terrestre. Pero en la cosmología clásica de Newton, que consideraba que el universo era infinito, eterno y repleto de estrellas homogéneas, esa respuesta no funciona.",
                        "tituloVisual": "LA TRAMPA DE NEWTON",
                        "layout": "primer_plano",
                        "composicionVisual": "primer_plano",
                        "escenario": "laboratorio",
                        "transicion": "zoom_in",
                        "efectosCamara": ["punch"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["Sol se oculta", "universo infinito", "estrellas homogéneas"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka"
                    }
                ]
            },
            {
                "id": "cap_2",
                "numero": 2,
                "titulo": "La Geometría de un Bosque Infinito de Estrellas",
                "resumen": "El modelo de capas esféricas concéntricas y la intensidad constante.",
                "escenas": [
                    {
                        "id": 3,
                        "texto": "Imagina que estás en el centro de un bosque interminable: mires adonde mires, tu vista siempre terminará chocando contra el tronco de un árbol. En un universo infinito lleno de estrellas, ocurriría exactamente lo mismo.",
                        "tituloVisual": "EL BOSQUE DE FOTONES",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "espacio_profundo",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["bosque interminable", "tronco de un árbol", "universo infinito"],
                        "poseId": "standing_confident",
                        "expresion": "analytical"
                    },
                    {
                        "id": 4,
                        "texto": "Cualquier rayo visual que proyectes al cielo nocturno debería toparse tarde o temprano con la superficie ardiente de una estrella. Aunque las estrellas lejanas se ven más débiles, su número aumenta en la misma proporción con la distancia, por lo que el cielo entero debería brillar con la temperatura cegadora del Sol.",
                        "tituloVisual": "BRILLO TEORICO SOLAR",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "espacio_profundo",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["superficie ardiente", "aumenta en la misma proporción", "temperatura cegadora"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka",
                        "infografia": {
                            "tipo": "dato_clave",
                            "titulo": "La Paradoja Matemática",
                            "subtitulo": "Integración de capas esféricas infinitas",
                            "valorPrincipal": "5500 °C",
                            "unidad": "brillo nocturno calculado",
                            "items": [
                                {"etiqueta": "Intensidad por estrella", "valor": "Decae con 1/R²", "porcentaje": 50, "color": "#38BDF8"},
                                {"etiqueta": "Número de estrellas", "valor": "Crece con R² (Se anulan)", "porcentaje": 100, "color": "#EF4444"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    }
                ]
            },
            {
                "id": "cap_3",
                "numero": 3,
                "titulo": "La Velocidad Finita de la Luz y el Tiempo",
                "resumen": "La resolución poética de Edgar Allan Poe y la física moderna.",
                "escenas": [
                    {
                        "id": 5,
                        "texto": "Sorprendentemente, la primera persona en intuir la verdadera solución no fue un físico, sino el escritor Edgar Allan Poe en su ensayo Eureka de mil ochocientos cuarenta y ocho: la luz de las estrellas más remotas aún no ha tenido tiempo de llegar a la Tierra.",
                        "tituloVisual": "EDGAR ALLAN POE, 1848",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "laboratorio",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["Edgar Allan Poe", "Eureka", "no ha tenido tiempo"],
                        "poseId": "thinking_chin_hand",
                        "expresion": "analytical"
                    },
                    {
                        "id": 6,
                        "texto": "El universo no es eterno hacia el pasado: nació hace trece mil ochocientos millones de años. Como la luz viaja a una velocidad finita, solo podemos ver las estrellas situadas dentro de nuestra burbuja cósmica observable; la luz de todo lo que está más allá aún viene en camino.",
                        "tituloVisual": "HORIZONTE COSMICO",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "espacio_profundo",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["trece mil ochocientos millones de años", "velocidad finita", "burbuja cósmica observable"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka",
                        "infografia": {
                            "tipo": "comparacion",
                            "titulo": "Límite del Horizonte Observable",
                            "subtitulo": "Tiempo de viaje de la luz desde el Big Bang",
                            "valorPrincipal": "13.800 M",
                            "unidad": "años de edad",
                            "items": [
                                {"etiqueta": "Volumen observable alcanzado", "valor": "46.500 millones de años luz", "porcentaje": 40, "color": "#38BDF8"},
                                {"etiqueta": "Luz que aún no llega", "valor": "Espacio infinito exterior", "porcentaje": 100, "color": "#94A3B8"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    }
                ]
            },
            {
                "id": "cap_4",
                "numero": 4,
                "titulo": "La Expansión Cósmica y el Corrimiento al Rojo",
                "resumen": "Cómo la expansión del espacio enfría y estira los fotones.",
                "escenas": [
                    {
                        "id": 7,
                        "texto": "Hay un segundo motivo crucial que descubrió Edwin Hubble: el universo se está expandiendo activamente. Conforme la luz atraviesa miles de millones de años luz de espacio en expansión, sus ondas se estiran y pierden energía.",
                        "tituloVisual": "EXPANSION DE HUBBLE",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "tunel_relativista",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_dramatic_hit.wav",
                        "volumenSfx": 0.25,
                        "palabrasClave": ["Edwin Hubble", "expandiendo activamente", "ondas se estiran"],
                        "poseId": "standing_confident",
                        "expresion": "analytical"
                    },
                    {
                        "id": 8,
                        "texto": "La luz visible emitida por las galaxias primitivas se ha estirado tanto que se ha convertido en radiación infrarroja y microondas. Nuestros ojos biológicos no pueden verla, convirtiendo el cielo en un manto negro para nuestra vista.",
                        "tituloVisual": "FOTONES ESTIRADOS",
                        "layout": "primer_plano",
                        "composicionVisual": "primer_plano",
                        "escenario": "espacio_profundo",
                        "transicion": "whip_left",
                        "efectosCamara": ["punch"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["galaxias primitivas", "radiación infrarroja", "manto negro"],
                        "poseId": "thinking_chin_hand",
                        "expresion": "analytical"
                    }
                ]
            },
            {
                "id": "cap_5",
                "numero": 5,
                "titulo": "El Eco Resplandeciente del Big Bang",
                "resumen": "El fondo cósmico de microondas que baña la noche.",
                "escenas": [
                    {
                        "id": 9,
                        "texto": "Si tus ojos pudieran percibir las ondas de radio y microondas, la noche no sería negra en absoluto: resplandecería de forma uniforme en todas direcciones con el fondo cósmico de microondas, el eco fósil de la primera luz liberada tras el Big Bang.",
                        "tituloVisual": "FONDO COSMICO",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "espacio_profundo",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["ondas de radio", "fondo cósmico de microondas", "eco fósil"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka",
                        "infografia": {
                            "tipo": "dato_clave",
                            "titulo": "Temperatura del Fondo Cósmico",
                            "subtitulo": "Luz fósil enfriada por la expansión",
                            "valorPrincipal": "2.73 K",
                            "unidad": "grados Kelvin (-270 °C)",
                            "items": [
                                {"etiqueta": "Temperatura original Big Bang", "valor": "3.000 grados Celsius", "porcentaje": 100, "color": "#EF4444"},
                                {"etiqueta": "Enfriamiento por expansión", "valor": "Factor de estiramiento 1100x", "porcentaje": 99, "color": "#38BDF8"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    },
                    {
                        "id": 10,
                        "texto": "Ese resplandor residual baña cada milímetro del cosmos día y noche. En los televisores analógicos antiguos con estática gris sin sintonizar, un uno por ciento de ese ruido blanco correspondía a fotones del Big Bang chocando contra la antena.",
                        "tituloVisual": "FOTONES EN LA ANTENA",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "galeria_diseno_retro",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["televisores analógicos", "ruido blanco", "fotones del Big Bang"],
                        "poseId": "standing_confident",
                        "expresion": "smile_soft"
                    }
                ]
            },
            {
                "id": "cap_6",
                "numero": 6,
                "titulo": "La Prueba Visible de un Universo con Principio",
                "resumen": "Epílogo sobre la oscuridad de la noche como triunfo del conocimiento.",
                "escenas": [
                    {
                        "id": 11,
                        "texto": "La próxima vez que salgas al patio y mires la oscuridad del firmamento, no veas un vacío silencioso. La noche es negra porque el universo tuvo un cumpleaños y porque no deja de expandirse: la oscuridad es la huella digital más grandiosa del origen del cosmos.",
                        "tituloVisual": "LA HUELLA DEL PRINCIPIO",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "vacio",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["oscuridad del firmamento", "tuvo un cumpleaños", "origen del cosmos"],
                        "poseId": "standing_confident",
                        "expresion": "smile_soft"
                    }
                ]
            }
        ]
    }


def main():
    print("[CREAR] Generando documentales largos 8 y 9...")
    d8 = construir_doc_008_cordyceps()
    d9 = construir_doc_009_olbers()

    with open(GUIONES_DIR / "doc_008_hongo_cordyceps.json", "w", encoding="utf-8") as f:
        json.dump(d8, f, ensure_ascii=False, indent=2)

    with open(GUIONES_DIR / "doc_009_paradoja_olbers.json", "w", encoding="utf-8") as f:
        json.dump(d9, f, ensure_ascii=False, indent=2)

    print("✅ Documentales 8 y 9 exportados exitosamente.")


if __name__ == "__main__":
    main()
