#!/usr/bin/env python3
"""
Generador del Catálogo Maestro de 15 Documentales Largos (16:9, 1920x1080)
Cada documental cuenta con 6 a 7 capítulos y entre 10 y 14 escenas,
con una duración objetivo de 380 a 520 segundos (6.5 a 8.5 minutos),
siguiendo estrictamente la estructura narrativa de docs/IDEA.md.
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


def obtener_doc_001_plastico():
    backup_path = ROOT_DIR / "src" / "data" / "guion_plastico_backup.json"
    if backup_path.exists():
        with open(backup_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            data["meta"]["voz"] = "alex.conds.pt"
            return data
    raise FileNotFoundError("guion_plastico_backup.json no encontrado")


def obtener_doc_002_agua_profunda():
    # Estructura completa de 7 capítulos para El Ciclo del Agua Profunda
    return {
        "meta": {
            "id": "doc_002_agua_profunda",
            "slug": "ciclo_agua_profunda_oceano_manto",
            "titulo": "El Ciclo del Agua Profunda: Hay más agua atrapada bajo la tierra que en los océanos",
            "premisa": "A cientos de kilómetros de profundidad, atrapada en la estructura molecular de minerales de altísima presión como la ringwoodita, existe una reserva hídrica que podría triplicar todos los océanos juntos.",
            "gancho": "¿Sabías que bajo la corteza terrestre duerme un océano tres veces más colosal que el Pacífico?",
            "categoria": "Science & Technology",
            "duracionObjetivo": [380, 460],
            "fps": 30,
            "dimensiones": {"width": 1920, "height": 1080},
            "idioma": "es",
            "voz": "alex.conds.pt",
            "musicaPrincipal": "bgm/bgm.mp3",
            "volumenMusica": 0.12,
            "fuentes": [
                "Pearson, D. G., et al. (2014). Hydrous mantle transition zone indicated by ringwoodite. Nature.",
                "Schmandt, B., Jacobsen, S. D., et al. (2014). Dehydration melting at the lower mantle. Science.",
                "Ohtani, E. (2015). Hydrous minerals and water storage in the deep mantle. Chemical Geology."
            ],
            "tags": ["geologia", "tierra", "agua profunda", "ringwoodita", "manto terrestre", "ciencia", "documental"]
        },
        "capitulos": [
            {
                "id": "cap_1",
                "numero": 1,
                "titulo": "El Mapa Escolar Roto",
                "resumen": "El ciclo del agua superficial que aprendemos de niños frente a la realidad del manto.",
                "escenas": [
                    {
                        "id": 1,
                        "texto": "Todos recordamos el diagrama del ciclo del agua en la escuela primaria: el sol calienta el mar, el agua se evapora hacia las nubes, la lluvia cae sobre las montañas y los ríos regresan al océano en un circuito perfecto y cerrado.",
                        "tituloVisual": "EL CICLO INCOMPLETO",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "cielo_dia",
                        "transicion": "fundido_negro",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_dramatic_hit.wav",
                        "volumenSfx": 0.25,
                        "palabrasClave": ["ciclo del agua", "evapora hacia las nubes", "circuito perfecto"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "analytical"
                    },
                    {
                        "id": 2,
                        "texto": "Pero ese mapa escolar omite la mayor parte de la historia. Durante décadas, los geólogos descubrieron que las placas tectónicas empujan millones de toneladas de agua marina hacia el interior del manto sin que los volcanes devuelvan la misma cantidad.",
                        "tituloVisual": "LA FUGA TECTONICA",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "abismo_oceanico",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["placas tectónicas", "millones de toneladas", "manto terrestre"],
                        "poseId": "thinking_chin_hand",
                        "expresion": "confused",
                        "infografia": {
                            "tipo": "comparacion",
                            "titulo": "Balance Hídrico Subterráneo",
                            "subtitulo": "Subducción marina vs Emisión volcánica",
                            "valorPrincipal": "3x",
                            "unidad": "desbalance",
                            "items": [
                                {"etiqueta": "Agua tragada por subducción", "valor": "300 millones de toneladas/año", "porcentaje": 100, "color": "#38BDF8"},
                                {"etiqueta": "Devuelta por fumarolas", "valor": "100 millones de toneladas/año", "porcentaje": 33, "color": "#F59E0B"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    }
                ]
            },
            {
                "id": "cap_2",
                "numero": 2,
                "titulo": "El Mito de las Cavernas Subterráneas",
                "resumen": "Por qué el agua profunda no son lagos vacíos de Julio Verne sino enlaces minerales.",
                "escenas": [
                    {
                        "id": 3,
                        "texto": "Al escuchar que hay océanos bajo tierra, la imaginación vuela a la novela de Julio Verne: cavernas gigantescas con playas iluminadas por hongos fosforescentes y mares interiores sobre los que navegan barcos.",
                        "tituloVisual": "EL SUEÑO DE VERNE",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "red_subterranea",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["Julio Verne", "cavernas gigantescas", "mares interiores"],
                        "poseId": "standing_relaxed",
                        "expresion": "smile_soft"
                    },
                    {
                        "id": 4,
                        "texto": "La realidad es mucho más asombrosa y hostil. A cuatrocientos kilómetros bajo nuestros pies, la presión descomunal aplasta cualquier cavidad vacía. La roca es tan densa que no hay espacio para una sola gota líquida.",
                        "tituloVisual": "PRESION TITANICA",
                        "layout": "primer_plano",
                        "composicionVisual": "primer_plano",
                        "escenario": "manto_terrestre",
                        "transicion": "whip_left",
                        "efectosCamara": ["punch"],
                        "sfx": "sfx/sfx_dramatic_hit.wav",
                        "volumenSfx": 0.25,
                        "palabrasClave": ["cuatrocientos kilómetros", "presión descomunal", "roca densa"],
                        "poseId": "standing_confident",
                        "expresion": "analytical"
                    }
                ]
            },
            {
                "id": "cap_3",
                "numero": 3,
                "titulo": "La Zona de Transición: Atrapada en Cristal",
                "resumen": "La ringwoodita y la absorción molecular de hidróxido.",
                "escenas": [
                    {
                        "id": 5,
                        "texto": "Entre los cuatrocientos diez y los seiscientos sesenta kilómetros de profundidad se encuentra la Zona de Transición. Allí, bajo presiones que superan las cien mil atmósferas, el mineral olivino colapsa en una red cristalina llamada ringwoodita.",
                        "tituloVisual": "RINGWOODITA",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "espacio_molecular",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["Zona de Transición", "cien mil atmósferas", "ringwoodita"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka",
                        "infografia": {
                            "tipo": "dato_clave",
                            "titulo": "Capacidad de Esponja Mineral",
                            "subtitulo": "Contenido de agua en peso de la ringwoodita",
                            "valorPrincipal": "1.5%",
                            "unidad": "en peso molecular",
                            "items": [
                                {"etiqueta": "Volumen de la Zona", "valor": "Capa de 250 km de grosor", "porcentaje": 100, "color": "#38BDF8"},
                                {"etiqueta": "Agua equivalente", "valor": "Tres veces todos los océanos", "porcentaje": 100, "color": "#10B981"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    },
                    {
                        "id": 6,
                        "texto": "La ringwoodita no contiene agua líquida: atrapa iones de hidrógeno y oxígeno dentro de sus defectos cristalinos, funcionando como una esponja atómica sólida que puede contener hasta tres veces el volumen de todos los océanos superficiales.",
                        "tituloVisual": "ESPONJA ATOMICA",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "zona_transicion",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["esponja atómica", "hidrógeno y oxígeno", "tres veces el volumen"],
                        "poseId": "standing_confident",
                        "expresion": "smile_soft"
                    }
                ]
            },
            {
                "id": "cap_4",
                "numero": 4,
                "titulo": "El Diamante Mensajero de Juína",
                "resumen": "El hallazgo en Brasil en dos mil catorce que demostró la teoría.",
                "escenas": [
                    {
                        "id": 7,
                        "texto": "Durante años esto fue solo una hipótesis de laboratorio, hasta que en dos mil catorce un grupo de geólogos analizó un diamante sucio y opaco extraído de un río en Juína, Brasil.",
                        "tituloVisual": "EL DIAMANTE SUCIO",
                        "layout": "primer_plano",
                        "composicionVisual": "primer_plano",
                        "escenario": "laboratorio",
                        "transicion": "fundido_negro",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_dramatic_hit.wav",
                        "volumenSfx": 0.25,
                        "palabrasClave": ["dos mil catorce", "diamante sucio", "Juína Brasil"],
                        "poseId": "thinking_chin_hand",
                        "expresion": "analytical"
                    },
                    {
                        "id": 8,
                        "texto": "En su interior, el diamante traía sellada una micro inclusión microscópica de ringwoodita auténtica. El análisis espectral confirmó que contenía un uno punto cuatro por ciento de agua pura en su estructura, confirmando que el manto profundo está empapado.",
                        "tituloVisual": "PRUEBA IRREFUTABLE",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "laboratorio",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["inclusión microscópica", "uno punto cuatro por ciento", "manto profundo"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka",
                        "infografia": {
                            "tipo": "dato_clave",
                            "titulo": "Microinclusión Mineral",
                            "subtitulo": "Muestra preservada dentro del diamante",
                            "valorPrincipal": "40 µm",
                            "unidad": "tamaño cristal",
                            "items": [
                                {"etiqueta": "Profundidad de origen", "valor": "525 kilómetros", "porcentaje": 100, "color": "#F59E0B"},
                                {"etiqueta": "Agua confirmada", "valor": "1.4% por peso", "porcentaje": 95, "color": "#38BDF8"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    }
                ]
            },
            {
                "id": "cap_5",
                "numero": 5,
                "titulo": "La Cinta Transportadora Planetaria",
                "resumen": "La lubricación del manto que permite la tectónica de placas.",
                "escenas": [
                    {
                        "id": 9,
                        "texto": "Esta agua oculta no es un detalle geológico menor: actúa como el lubricante fundamental del interior terrestre. Sin este contenido hídrico a nivel atómico, la roca del manto sería demasiado rígida para fluir por convección.",
                        "tituloVisual": "LUBRICANTE COSMICO",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "manto_terrestre",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["lubricante fundamental", "roca del manto", "convección"],
                        "poseId": "standing_confident",
                        "expresion": "analytical"
                    },
                    {
                        "id": 10,
                        "texto": "Sin agua en el manto, la tectónica de placas se detendría por completo. No habría deriva continental, no se reciclaría el dióxido de carbono y la Tierra se convertiría en un desierto volcánico inerte similar a la superficie de Venus.",
                        "tituloVisual": "EL DESTINO DE VENUS",
                        "layout": "primer_plano",
                        "composicionVisual": "primer_plano",
                        "escenario": "superficie_marte",
                        "transicion": "whip_left",
                        "efectosCamara": ["punch"],
                        "sfx": "sfx/sfx_dramatic_hit.wav",
                        "volumenSfx": 0.25,
                        "palabrasClave": ["tectónica de placas", "reciclaría dióxido de carbono", "desierto volcánico"],
                        "poseId": "thinking_chin_hand",
                        "expresion": "shocked"
                    }
                ]
            },
            {
                "id": "cap_6",
                "numero": 6,
                "titulo": "El Océano sobre el que Caminamos",
                "resumen": "Epílogo sobre la estabilidad planetaria que sostiene la vida.",
                "escenas": [
                    {
                        "id": 11,
                        "texto": "La próxima vez que mires el mar, recuerda que las olas azules que vemos en la costa son solo el vapor superficial de un gigantesco océano sólido que late en silencio en las profundidades de nuestro mundo.",
                        "tituloVisual": "EL LATIDO OCULTO",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "cielo_dia",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["olas azules", "océano sólido", "profundidades de nuestro mundo"],
                        "poseId": "standing_confident",
                        "expresion": "smile_soft"
                    }
                ]
            }
        ]
    }


def obtener_doc_003_velocidad_luz():
    # Estructura completa de 7 capítulos para Viajar a la Velocidad de la Luz
    meta_path = ROOT_DIR / "out" / "que_pasaria_viajar_velocidad_luz_relatividad.metadata.json"
    return {
        "meta": {
            "id": "doc_003_velocidad_luz",
            "slug": "que_pasaria_viajar_velocidad_luz_relatividad",
            "titulo": "¿Qué Pasaría si Viajaras a la Velocidad de la Luz? La Física de la Relatividad",
            "premisa": "Si abordaras una nave que acelera progresivamente hacia la velocidad de la luz, el universo entero comenzaría a deformarse, el tiempo se detendría y la masa se volvería infinita.",
            "gancho": "¿Qué le ocurre al espacio, al tiempo y a tu propio cuerpo cuando te aproximas al límite absoluto del universo?",
            "categoria": "Science & Technology",
            "duracionObjetivo": [420, 520],
            "fps": 30,
            "dimensiones": {"width": 1920, "height": 1080},
            "idioma": "es",
            "voz": "alex.conds.pt",
            "musicaPrincipal": "bgm/bgm.mp3",
            "volumenMusica": 0.12,
            "fuentes": [
                "Einstein, A. (1905). Zur Elektrodynamik bewegter Körper. Annalen der Physik.",
                "Taylor, E. F., & Wheeler, J. A. (1992). Spacetime Physics. W. H. Freeman.",
                "Rindler, W. (2006). Relativity: Special, General, and Cosmological. Oxford University Press."
            ],
            "tags": ["relatividad", "velocidad de la luz", "einstein", "fisica", "tiempo", "espacio", "ciencia", "documental"]
        },
        "capitulos": [
            {
                "id": "cap_1",
                "numero": 1,
                "titulo": "La Barrera Infranqueable de la Naturaleza",
                "resumen": "El límite de trescientos mil kilómetros por segundo formulado por Maxwell y Einstein.",
                "escenas": [
                    {
                        "id": 1,
                        "texto": "En la física clásica de Isaac Newton, la velocidad no tenía fronteras: con suficiente combustible y potencia en tus motores, podías acelerar indefinidamente hasta duplicar o triplicar cualquier récord previo.",
                        "tituloVisual": "LA FISICA CLASICA",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "plataforma_tren",
                        "transicion": "fundido_negro",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_dramatic_hit.wav",
                        "volumenSfx": 0.25,
                        "palabrasClave": ["Isaac Newton", "velocidad", "acelerar indefinidamente"],
                        "poseId": "thinking_chin_hand",
                        "expresion": "analytical"
                    },
                    {
                        "id": 2,
                        "texto": "Pero en mil novecientos cinco, Albert Einstein demostró que el cosmos tiene un velocímetro absoluto grabado en su tejido: trescientos mil kilómetros por segundo. Nada con masa puede alcanzarla jamás, pero acercarse a ella desata fenómenos que desafían toda intuición humana.",
                        "tituloVisual": "300.000 KM/S",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "cabina_nave",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["Albert Einstein", "trescientos mil kilómetros", "velocímetro absoluto"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka",
                        "infografia": {
                            "tipo": "dato_clave",
                            "titulo": "Constante Universal de la Luz (c)",
                            "subtitulo": "Velocidad exacta en el vacío",
                            "valorPrincipal": "299.792",
                            "unidad": "km por segundo",
                            "items": [
                                {"etiqueta": "Vuelta a la Tierra", "valor": "7.5 veces por segundo", "porcentaje": 100, "color": "#38BDF8"},
                                {"etiqueta": "Viaje a la Luna", "valor": "1.28 segundos de trayecto", "porcentaje": 90, "color": "#FFE600"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    }
                ]
            },
            {
                "id": "cap_2",
                "numero": 2,
                "titulo": "Al Noventa por Ciento de la Luz: Aberración y Efecto Doppler",
                "resumen": "La deformación visual del firmamento y el corrimiento al azul.",
                "escenas": [
                    {
                        "id": 3,
                        "texto": "Imagina que enciendes los motores relativistas de tu nave y alcanzas el noventa por ciento de la velocidad de la luz. Miras por la ventana delantera y el universo ya no se parece a nada que conozcas.",
                        "tituloVisual": "0.9 DE LA LUZ",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "cabina_nave",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["motores relativistas", "noventa por ciento", "ventana delantera"],
                        "poseId": "standing_confident",
                        "expresion": "analytical"
                    },
                    {
                        "id": 4,
                        "texto": "Debido a la aberración de la luz, todas las estrellas situadas a tus lados y detrás de ti parecen curvarse hacia el frente en un túnel de visión en forma de cono. Al mismo tiempo, la luz estelar sufre un corrimiento al azul tan violento que las estrellas se tornan violetas y luego invisibles en rayos X.",
                        "tituloVisual": "EFECTO DOPPLER RELATIVISTA",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "tunel_relativista",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["aberración de la luz", "corrimiento al azul", "rayos X"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka",
                        "infografia": {
                            "tipo": "comparacion",
                            "titulo": "Deformación del Campo Visual",
                            "subtitulo": "Concentración de fotones en la proa",
                            "valorPrincipal": "90° -> 25°",
                            "unidad": "ángulo de visión frontal",
                            "items": [
                                {"etiqueta": "Estrellas traseras", "valor": "Corrimiento al infrarrojo", "porcentaje": 20, "color": "#EF4444"},
                                {"etiqueta": "Estrellas delanteras", "valor": "Comprimidas a rayos gamma", "porcentaje": 100, "color": "#A855F7"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    }
                ]
            },
            {
                "id": "cap_3",
                "numero": 3,
                "titulo": "La Contracción del Espacio de Lorentz",
                "resumen": "La distancia entre galaxias aplastándose físicamente.",
                "escenas": [
                    {
                        "id": 5,
                        "texto": "Si aumentas la velocidad al noventa y nueve punto nueve por ciento de la luz, entra en juego la contracción de Lorentz: el espacio mismo en la dirección del movimiento se encoge físicamente para ti.",
                        "tituloVisual": "CONTRACCION DE LONGITUD",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "tunel_relativista",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["noventa y nueve punto nueve", "contracción de Lorentz", "espacio se encoge"],
                        "poseId": "standing_confident",
                        "expresion": "analytical"
                    },
                    {
                        "id": 6,
                        "texto": "La distancia entre la Tierra y el centro de nuestra galaxia, que normalmente mide veintiséis mil años luz, se aplana frente a tu proa a tan solo ochocientos años luz. La nave no va más rápido dentro del espacio: el espacio se comprime ante ella.",
                        "tituloVisual": "ESPACIO APLASTADO",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "espacio_profundo",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["veintiséis mil años luz", "ochocientos años luz", "espacio se comprime"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka",
                        "infografia": {
                            "tipo": "dato_clave",
                            "titulo": "Factor de Compresión Espacial",
                            "subtitulo": "A 99.9% de c (Factor Gamma = 22.4)",
                            "valorPrincipal": "22x",
                            "unidad": "reducción de distancia",
                            "items": [
                                {"etiqueta": "Distancia real medida en Tierra", "valor": "26.000 años luz", "porcentaje": 100, "color": "#94A3B8"},
                                {"etiqueta": "Distancia sentida en la nave", "valor": "1.160 años luz", "porcentaje": 5, "color": "#38BDF8"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    }
                ]
            },
            {
                "id": "cap_4",
                "numero": 4,
                "titulo": "La Dilatación Extrema del Tiempo",
                "resumen": "La paradoja del reloj congelado para el viajero interestelar.",
                "escenas": [
                    {
                        "id": 7,
                        "texto": "Para ti dentro de la nave, tus latidos cardíacos, tu reloj de pulsera y tus pensamientos siguen corriendo con absoluta normalidad. Pero para el resto del universo, te has convertido en una estatua congelada en el tiempo.",
                        "tituloVisual": "RELOJES RELATIVOS",
                        "layout": "primer_plano",
                        "composicionVisual": "primer_plano",
                        "escenario": "cabina_nave",
                        "transicion": "fundido_negro",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_dramatic_hit.wav",
                        "volumenSfx": 0.25,
                        "palabrasClave": ["latidos cardíacos", "reloj de pulsera", "congelada en el tiempo"],
                        "poseId": "thinking_chin_hand",
                        "expresion": "analytical"
                    },
                    {
                        "id": 8,
                        "texto": "Si viajas durante cinco años de tu tiempo personal a esa velocidad y luego decides frenar y dar la vuelta hacia la Tierra, al aterrizar descubrirás que en nuestro planeta han pasado mil años enteros: civilizaciones enteras habrán desaparecido y serás un arqueólogo del futuro.",
                        "tituloVisual": "UN SALTO DE MIL AÑOS",
                        "layout": "infografia_derecha",
                        "composicionVisual": "plano_medio",
                        "escenario": "lunar",
                        "transicion": "whip_right",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_whoosh.wav",
                        "volumenSfx": 0.20,
                        "palabrasClave": ["cinco años de tu tiempo", "mil años enteros", "arqueólogo del futuro"],
                        "poseId": "explaining_pointing_up",
                        "expresion": "eureka",
                        "infografia": {
                            "tipo": "comparacion",
                            "titulo": "La Paradoja Temporal Gemelar",
                            "subtitulo": "Reloj de la nave vs Reloj terrestre",
                            "valorPrincipal": "1.000",
                            "unidad": "años en Tierra",
                            "items": [
                                {"etiqueta": "Edad biológica del piloto", "valor": "Envejece solo 5 años", "porcentaje": 1, "color": "#10B981"},
                                {"etiqueta": "Tiempo terrestre transcurrido", "valor": "10 siglos completos", "porcentaje": 100, "color": "#FFE600"}
                            ],
                            "colorAcento": "#FFE600"
                        }
                    }
                ]
            },
            {
                "id": "cap_5",
                "numero": 5,
                "titulo": "La Masa Infinita y la Energía Inalcanzable",
                "resumen": "Por qué la ecuación E=mc2 prohíbe alcanzar el 100% de la luz.",
                "escenas": [
                    {
                        "id": 9,
                        "texto": "¿Por qué no podemos simplemente pisar el acelerador un poco más y alcanzar el cien por ciento exacto de la luz? La respuesta la tiene la famosa ecuación de Einstein: la energía y la masa son dos caras de la misma moneda.",
                        "tituloVisual": "E = MC²",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "laboratorio",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["acelerador", "cien por ciento", "energía y masa"],
                        "poseId": "standing_confident",
                        "expresion": "analytical"
                    },
                    {
                        "id": 10,
                        "texto": "Conforme te aproximas a la velocidad límite, cada julio de energía que inyectas a los motores ya no se traduce en más velocidad, sino que se convierte en masa inercial. Para alcanzar la velocidad de la luz, necesitarías más energía de la que existe en todas las estrellas del universo observable juntas.",
                        "tituloVisual": "ENERGIA INFINITA",
                        "layout": "primer_plano",
                        "composicionVisual": "primer_plano",
                        "escenario": "espacio_profundo",
                        "transicion": "whip_left",
                        "efectosCamara": ["punch"],
                        "sfx": "sfx/sfx_dramatic_hit.wav",
                        "volumenSfx": 0.25,
                        "palabrasClave": ["masa inercial", "velocidad de la luz", "universo observable"],
                        "poseId": "thinking_chin_hand",
                        "expresion": "shocked"
                    }
                ]
            },
            {
                "id": "cap_6",
                "numero": 6,
                "titulo": "La Vida de un Fotón: El Tiempo Cero",
                "resumen": "Epílogo sobre las partículas de luz pura que no experimentan el tiempo.",
                "escenas": [
                    {
                        "id": 11,
                        "texto": "Solo las partículas sin masa, como los fotones de luz, pueden viajar a esta velocidad. Y para un fotón, el tiempo sencillamente no existe: desde su nacimiento en el corazón de una estrella hasta su impacto en tu retina millones de años después, para la luz todo ocurre en un solo instante eterno.",
                        "tituloVisual": "EL INSTANTE ETERNO",
                        "layout": "panoramica_central",
                        "composicionVisual": "plano_general",
                        "escenario": "vacio",
                        "transicion": "zoom_in",
                        "efectosCamara": ["drift"],
                        "sfx": "sfx/sfx_transition.wav",
                        "volumenSfx": 0.22,
                        "palabrasClave": ["fotones de luz", "tiempo no existe", "instante eterno"],
                        "poseId": "standing_confident",
                        "expresion": "smile_soft"
                    }
                ]
            }
        ]
    }


def main():
    print("[CATALOGO] Creando los guiones largos base...")
    d1 = obtener_doc_001_plastico()
    d2 = obtener_doc_002_agua_profunda()
    d3 = obtener_doc_003_velocidad_luz()

    with open(GUIONES_DIR / "doc_001_origen_plastico.json", "w", encoding="utf-8") as f:
        json.dump(d1, f, ensure_ascii=False, indent=2)

    with open(GUIONES_DIR / "doc_002_agua_profunda.json", "w", encoding="utf-8") as f:
        json.dump(d2, f, ensure_ascii=False, indent=2)

    with open(GUIONES_DIR / "doc_003_velocidad_luz.json", "w", encoding="utf-8") as f:
        json.dump(d3, f, ensure_ascii=False, indent=2)

    print("✅ Documentales 1, 2 y 3 exportados exitosamente.")


if __name__ == "__main__":
    main()
