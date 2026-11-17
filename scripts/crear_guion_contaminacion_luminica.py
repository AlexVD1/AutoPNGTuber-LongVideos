#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador Maestro del Guion Documental Largo:
"El día que la Tierra se quedó sin oscuridad: La contaminación lumínica global"
Formato 16:9 (1920x1080 @ 30fps) - Monetización Mid-Roll >= 8:15 min (>= 495s)
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GUION_PATH = ROOT / "src" / "data" / "guion.json"

guion = {
    "meta": {
        "id": "doc_016_contaminacion_luminica_oscuridad",
        "slug": "dia_tierra_sin_oscuridad_contaminacion_luminica",
        "titulo": "El día que la Tierra se quedó sin oscuridad: La contaminación lumínica global",
        "premisa": "Examen exhaustivo del impacto ecológico, astronómico y biológico de la iluminación artificial nocturna permanente y cómo una generación entera ha perdido el contacto visual con la Vía Láctea.",
        "gancho": "¿Sabías que más del ochenta por ciento de la humanidad jamás ha visto el cielo nocturno real debido al resplandor artificial de las ciudades?",
        "categoria": "Science & Technology",
        "duracionObjetivo": [500, 570],
        "fps": 30,
        "dimensiones": {"width": 1920, "height": 1080},
        "idioma": "es",
        "voz": "alex.conds.pt",
        "musicaPrincipal": "bgm/bgm.mp3",
        "volumenMusica": 0.12,
        "fuentes": [
            "Falchi, F., et al. (2016). The new world atlas of artificial night sky brightness. Science Advances, 2(6), e1600377.",
            "Bortle, J. E. (2001). Introducing the Bortle Dark-Sky Scale. Sky & Telescope, 101(2), 126-129.",
            "Cinzano, P., Falchi, F., & Elvidge, C. D. (2001). The first World Atlas of the artificial night sky brightness. Monthly Notices of the Royal Astronomical Society, 328(3), 689-707.",
            "Witherington, B. E., & Martin, R. E. (2003). Understanding, assessing, and resolving light-pollution problems on sea turtle nesting beaches. Florida Fish and Wildlife Research Institute.",
            "Longcore, T., & Rich, C. (2004). Ecological light pollution. Frontiers in Ecology and the Environment, 2(4), 191-198.",
            "Brainard, G. C., et al. (2001). Action spectrum for melatonin regulation in humans. Journal of Neuroscience, 21(16), 6405-6412."
        ],
        "tags": [
            "contaminacion luminica",
            "cielo nocturno",
            "via lactea",
            "astronomia",
            "escala bortle",
            "ritmo circadiano",
            "ecologia",
            "tortugas marinas",
            "luz led",
            "documental"
        ]
    },
    "capitulos": [
        {
            "id": "cap_1",
            "numero": 1,
            "titulo": "El Apagón de Los Ángeles y la Galaxia Olvidada",
            "resumen": "La madrugada de 1994 en que un terremoto reveló la Vía Láctea y aterrorizó a millones de ciudadanos.",
            "escenas": [
                {
                    "id": 1,
                    "texto": "El diecisiete de enero de mil novecientos noventa y cuatro, a las cuatro y media de la madrugada, un violento terremoto de magnitud seis punto siete sacudió la ciudad de Los Ángeles. El sismo destruyó el tendido eléctrico y sumió a millones de habitantes en una oscuridad absoluta que jamás habían experimentado. Minutos después, las líneas telefónicas de los servicios de emergencia comenzaron a colapsar con llamadas de ciudadanos aterrorizados que reportaban una gigantesca nube plateada y brillante flotando sobre sus cabezas. Aquella misteriosa estructura no era una explosión química ni una invasión espacial: era simplemente el brazo central de la Vía Láctea, visible por primera vez en décadas.",
                    "tituloVisual": "LOS ÁNGELES, 1994",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "metropoli_noche_resplandor",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["shake", "drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.28,
                    "palabrasClave": ["diecisiete de enero", "terremoto", "oscuridad absoluta", "Vía Láctea"],
                    "planos": [
                        {
                            "tipo": "general",
                            "desdePalabra": "El diecisiete",
                            "hastaPalabra": "Los Ángeles",
                            "zoom": 1.0,
                            "blurFondo": 0
                        },
                        {
                            "tipo": "sobre_hombro",
                            "desdePalabra": "El sismo destruyó",
                            "hastaPalabra": "habían experimentado",
                            "x": -160,
                            "y": 15,
                            "zoom": 1.25,
                            "blurFondo": 3.5,
                            "hombroLado": "derecha"
                        },
                        {
                            "tipo": "primer_plano",
                            "desdePalabra": "Minutos después",
                            "hastaPalabra": "sus cabezas",
                            "x": -260,
                            "y": 0,
                            "zoom": 1.38,
                            "blurFondo": 5.0
                        },
                        {
                            "tipo": "plano_medio",
                            "desdePalabra": "Aquella misteriosa",
                            "hastaPalabra": "en décadas",
                            "x": 160,
                            "y": 15,
                            "zoom": 1.18,
                            "blurFondo": 2.0
                        }
                    ],
                    "personajes": [
                        {
                            "id": "stickman_narrador",
                            "posicion": {"x": -380, "y": 50},
                            "escala": 1.05,
                            "capaZ": 22,
                            "colorRim": "#38BDF8",
                            "acciones": [
                                {
                                    "pasos": [
                                        {
                                            "desdePalabra": "El diecisiete",
                                            "hastaPalabra": "Los Ángeles",
                                            "posicion": {"x": -380, "y": 50},
                                            "poseId": "standing_confident",
                                            "expresion": "talking_enthusiastic",
                                            "orientacion": "derecha"
                                        },
                                        {
                                            "desdePalabra": "El sismo destruyó",
                                            "hastaPalabra": "habían experimentado",
                                            "posicion": {"x": -340, "y": 50},
                                            "poseId": "shocked",
                                            "expresion": "worried",
                                            "orientacion": "derecha",
                                            "procedural": "temblar"
                                        },
                                        {
                                            "desdePalabra": "Minutos después",
                                            "hastaPalabra": "en décadas",
                                            "posicion": {"x": -300, "y": 50},
                                            "poseId": "explaining_pointing_up",
                                            "expresion": "eureka",
                                            "orientacion": "derecha"
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    "objetos": [
                        {
                            "id": "cielo_revelado",
                            "propId": "cielo_milkyway_revelacion",
                            "posicion": {"x": 260, "y": 40},
                            "escala": 1.25,
                            "capaZ": 28,
                            "pasos": [
                                {
                                    "desdePalabra": "El diecisiete",
                                    "hastaPalabra": "Los Ángeles",
                                    "estado": "bruma_anaranjada_ciega"
                                },
                                {
                                    "desdePalabra": "El sismo destruyó",
                                    "hastaPalabra": "habían experimentado",
                                    "estado": "apagon_repentino_corte"
                                },
                                {
                                    "desdePalabra": "Aquella misteriosa",
                                    "hastaPalabra": "en décadas",
                                    "estado": "via_lactea_resplandeciente"
                                }
                            ]
                        }
                    ],
                    "cotasVectoriales": [
                        {
                            "id": "cota_sismo_1994",
                            "valor": "MAGNITUD 6.7 + APAGÓN TOTAL",
                            "etiqueta": "Colapso de la red metropolitana",
                            "origenX": 1180,
                            "origenY": 580,
                            "destinoX": 880,
                            "destinoY": 260,
                            "color": "#FFE600",
                            "desdePalabra": "El sismo destruyó",
                            "hastaPalabra": "habían experimentado"
                        }
                    ],
                    "emisoresParticulas": [
                        {
                            "tipo": "fotones_luz",
                            "x": 1160,
                            "y": 640,
                            "color": "#FDE047",
                            "desdePalabra": "El diecisiete",
                            "hastaPalabra": "Los Ángeles"
                        }
                    ]
                },
                {
                    "id": 2,
                    "texto": "El asombro de los habitantes de Los Ángeles reveló una verdad incómoda de nuestra civilización industrial: más del ochenta por ciento de la población mundial vive hoy bajo cielos completamente intoxicados por la luz artificial. En regiones como Europa y América del Norte, esa cifra supera el noventa y nueve por ciento. Una generación entera de seres humanos está creciendo sin haber contemplado jamás la galaxia que habitamos. Al convertir la noche en un perpetuo crepúsculo artificial, la humanidad rompió un pacto biológico y astronómico de millones de años, encendiendo un experimento descontrolado a escala global que está alterando silenciosamente la vida sobre la Tierra.",
                    "tituloVisual": "80% POBLACIÓN MUNDIAL",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_medio",
                    "escenario": "metropoli_noche_resplandor",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.22,
                    "palabrasClave": ["ochenta por ciento", "luz artificial", "noventa y nueve por ciento", "crepúsculo artificial"],
                    "planos": [
                        {
                            "tipo": "general",
                            "desdePalabra": "El asombro",
                            "hastaPalabra": "luz artificial",
                            "zoom": 1.0,
                            "blurFondo": 0
                        },
                        {
                            "tipo": "sobre_hombro",
                            "desdePalabra": "En regiones como",
                            "hastaPalabra": "que habitamos",
                            "x": 260,
                            "y": 490,
                            "zoom": 1.26,
                            "blurFondo": 4.0,
                            "hombroLado": "izquierda"
                        },
                        {
                            "tipo": "primer_plano",
                            "desdePalabra": "Al convertir la noche",
                            "hastaPalabra": "sobre la Tierra",
                            "x": 320,
                            "y": 500,
                            "zoom": 1.45,
                            "blurFondo": 6.5
                        }
                    ],
                    "personajes": [
                        {
                            "id": "stickman_narrador",
                            "posicion": {"x": 360, "y": 620},
                            "escala": 1.05,
                            "capaZ": 22,
                            "colorRim": "#FFE600",
                            "acciones": [
                                {
                                    "pasos": [
                                        {
                                            "desdePalabra": "El asombro",
                                            "hastaPalabra": "luz artificial",
                                            "posicion": {"x": 360, "y": 620},
                                            "poseId": "presenting_open",
                                            "expresion": "analytical",
                                            "orientacion": "izquierda"
                                        },
                                        {
                                            "desdePalabra": "En regiones como",
                                            "hastaPalabra": "que habitamos",
                                            "posicion": {"x": 310, "y": 620},
                                            "poseId": "thinking_hand_chin",
                                            "expresion": "worried",
                                            "orientacion": "izquierda",
                                            "esHolograma": True,
                                            "trayectoriaSuelo": {
                                                "desdeX": 310,
                                                "hastaX": -240,
                                                "etiqueta": "SATURACIÓN FOTÓNICA GLOBAL",
                                                "color": "#EF4444"
                                            }
                                        },
                                        {
                                            "desdePalabra": "Al convertir la noche",
                                            "hastaPalabra": "sobre la Tierra",
                                            "posicion": {"x": 280, "y": 620},
                                            "poseId": "standing_confident",
                                            "expresion": "determined",
                                            "orientacion": "izquierda"
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    "objetos": [
                        {
                            "id": "globo_terrestre",
                            "propId": "esfera_tierra_luces_nocturnas",
                            "posicion": {"x": -240, "y": 140},
                            "escala": 1.25,
                            "capaZ": 28,
                            "pasos": [
                                {
                                    "desdePalabra": "El asombro",
                                    "hastaPalabra": "luz artificial",
                                    "estado": "red_luces_continentes"
                                },
                                {
                                    "desdePalabra": "En regiones como",
                                    "hastaPalabra": "que habitamos",
                                    "estado": "europa_america_saturada"
                                },
                                {
                                    "desdePalabra": "Al convertir la noche",
                                    "hastaPalabra": "sobre la Tierra",
                                    "estado": "tierra_oscuridad_amenazada"
                                }
                            ]
                        }
                    ],
                    "cotasVectoriales": [
                        {
                            "id": "cota_poblacion_80",
                            "valor": "80% POBLACIÓN AFECTADA",
                            "etiqueta": "Pérdida de visión de la galaxia",
                            "origenX": 740,
                            "origenY": 540,
                            "destinoX": 940,
                            "destinoY": 260,
                            "color": "#EF4444",
                            "desdePalabra": "En regiones como",
                            "hastaPalabra": "que habitamos"
                        }
                    ]
                }
            ]
        },
        {
            "id": "cap_2",
            "numero": 2,
            "titulo": "La Invención de la Noche Artificial y la Escala Bortle",
            "resumen": "De las farolas de gas a la clasificación métrica del oscurecimiento del cielo.",
            "escenas": [
                {
                    "id": 3,
                    "texto": "Durante casi toda la historia de nuestra especie, la noche estuvo dominada por el fuego tenue de las antorchas, las velas de cera y los mecheros de gas. Pero a finales del siglo diecinueve, la invención de la bombilla incandescente por Thomas Edison y la electrificación masiva de las ciudades transformaron radicalmente el planeta. Pronto, las luminarias de vapor de mercurio y sodio de alta presión colonizaron cada avenida, autopista y fachada comercial. La luz eléctrica se convirtió en el símbolo indiscutible del progreso humano y la seguridad moderna, pero con un diseño óptico primitivo que disparaba más de la mitad de sus fotones directamente hacia las nubes.",
                    "tituloVisual": "REVOLUCIÓN ELÉCTRICA",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "metropoli_noche_resplandor",
                    "transicion": "zoom_in",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.22,
                    "palabrasClave": ["fuego tenue", "siglo diecinueve", "Thomas Edison", "vapor de mercurio", "diseño óptico"],
                    "planos": [
                        {
                            "tipo": "general",
                            "desdePalabra": "Durante casi",
                            "hastaPalabra": "radicalmente el planeta",
                            "zoom": 1.0,
                            "blurFondo": 0
                        },
                        {
                            "tipo": "plano_medio",
                            "desdePalabra": "Pronto, las luminarias",
                            "hastaPalabra": "y la seguridad moderna",
                            "x": -180,
                            "y": 500,
                            "zoom": 1.22,
                            "blurFondo": 3.0
                        },
                        {
                            "tipo": "primer_plano",
                            "desdePalabra": "pero con un diseño",
                            "hastaPalabra": "hacia las nubes",
                            "x": -260,
                            "y": 490,
                            "zoom": 1.40,
                            "blurFondo": 5.5
                        }
                    ],
                    "personajes": [
                        {
                            "id": "stickman_narrador",
                            "posicion": {"x": -360, "y": 620},
                            "escala": 1.05,
                            "capaZ": 22,
                            "colorRim": "#38BDF8",
                            "acciones": [
                                {
                                    "pasos": [
                                        {
                                            "desdePalabra": "Durante casi",
                                            "hastaPalabra": "radicalmente el planeta",
                                            "posicion": {"x": -360, "y": 620},
                                            "poseId": "walking",
                                            "expresion": "talking_enthusiastic",
                                            "orientacion": "derecha",
                                            "procedural": "caminar"
                                        },
                                        {
                                            "desdePalabra": "Pronto, las luminarias",
                                            "hastaPalabra": "hacia las nubes",
                                            "posicion": {"x": -280, "y": 620},
                                            "poseId": "explaining_pointing_up",
                                            "expresion": "eureka",
                                            "orientacion": "derecha"
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    "objetos": [
                        {
                            "id": "farola_historica",
                            "propId": "evolucion_farola_electrica",
                            "posicion": {"x": 260, "y": 140},
                            "escala": 1.25,
                            "capaZ": 28,
                            "pasos": [
                                {
                                    "desdePalabra": "Durante casi",
                                    "hastaPalabra": "mecheros de gas",
                                    "estado": "farola_gas_victoriana_1880"
                                },
                                {
                                    "desdePalabra": "Pero a finales",
                                    "hastaPalabra": "la seguridad moderna",
                                    "estado": "farola_mercurio_globo_360"
                                },
                                {
                                    "desdePalabra": "pero con un diseño",
                                    "hastaPalabra": "hacia las nubes",
                                    "estado": "farola_blindada_cero_polucion"
                                }
                            ]
                        }
                    ],
                    "cotasVectoriales": [
                        {
                            "id": "cota_fuga_fotones",
                            "valor": "60% DISPERSIÓN AL CIELO",
                            "etiqueta": "Pérdida por globo no blindado",
                            "origenX": 1180,
                            "origenY": 540,
                            "destinoX": 860,
                            "destinoY": 260,
                            "color": "#EF4444",
                            "desdePalabra": "pero con un diseño",
                            "hastaPalabra": "hacia las nubes"
                        }
                    ],
                    "emisoresParticulas": [
                        {
                            "tipo": "fotones_luz",
                            "x": 1220,
                            "y": 600,
                            "color": "#FFE600",
                            "desdePalabra": "Pronto, las luminarias",
                            "hastaPalabra": "hacia las nubes"
                        }
                    ]
                },
                {
                    "id": 4,
                    "texto": "Para cuantificar el colapso de la oscuridad celeste, el astrónomo aficionado John Bortle creó en el año dos mil uno una escala de nueve niveles que mide la degradación del firmamento. En el nivel nueve, correspondiente al corazón de megalópolis como Nueva York o Tokio, el cielo nocturno emite un resplandor lechoso y brillante donde apenas son visibles la Luna y un par de planetas luminosos. Por el contrario, en el nivel uno de cielo prístino, la atmósfera es tan oscura y transparente que la Vía Láctea proyecta sombras nítidas sobre el suelo y revela miles de estrellas sin necesidad de telescopios.",
                    "tituloVisual": "ESCALA BORTLE (1 A 9)",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "metropoli_noche_resplandor",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.22,
                    "palabrasClave": ["John Bortle", "dos mil uno", "escala de nueve niveles", "nivel nueve", "nivel uno", "Vía Láctea"],
                    "planos": [
                        {
                            "tipo": "general",
                            "desdePalabra": "Para cuantificar",
                            "hastaPalabra": "degradación del firmamento",
                            "zoom": 1.02,
                            "blurFondo": 0
                        },
                        {
                            "tipo": "plano_medio",
                            "desdePalabra": "En el nivel nueve",
                            "hastaPalabra": "planetas luminosos",
                            "x": -80,
                            "y": 510,
                            "zoom": 1.08,
                            "blurFondo": 2.0
                        },
                        {
                            "tipo": "plano_medio",
                            "desdePalabra": "Por el contrario",
                            "hastaPalabra": "de telescopios",
                            "x": -100,
                            "y": 510,
                            "zoom": 1.08,
                            "blurFondo": 2.0
                        }
                    ],
                    "personajes": [
                        {
                            "id": "stickman_narrador",
                            "posicion": {"x": -450, "y": 620},
                            "escala": 1.05,
                            "capaZ": 22,
                            "colorRim": "#38BDF8",
                            "acciones": [
                                {
                                    "pasos": [
                                        {
                                            "desdePalabra": "Para cuantificar",
                                            "hastaPalabra": "degradación del firmamento",
                                            "posicion": {"x": -450, "y": 620},
                                            "poseId": "presenting_open",
                                            "expresion": "analytical",
                                            "orientacion": "derecha"
                                        },
                                        {
                                            "desdePalabra": "En el nivel nueve",
                                            "hastaPalabra": "planetas luminosos",
                                            "posicion": {"x": -430, "y": 620},
                                            "poseId": "worried",
                                            "expresion": "worried",
                                            "orientacion": "derecha"
                                        },
                                        {
                                            "desdePalabra": "Por el contrario",
                                            "hastaPalabra": "de telescopios",
                                            "posicion": {"x": -410, "y": 620},
                                            "poseId": "standing_confident",
                                            "expresion": "eureka",
                                            "orientacion": "derecha"
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    "objetos": [
                        {
                            "id": "medidor_sqm",
                            "propId": "medidor_escala_bortle",
                            "posicion": {"x": -105, "y": 140},
                            "escala": 1.25,
                            "capaZ": 28,
                            "pasos": [
                                {
                                    "desdePalabra": "Para cuantificar",
                                    "hastaPalabra": "degradación del firmamento",
                                    "estado": "bortle_5_amarillo_suburbano"
                                },
                                {
                                    "desdePalabra": "En el nivel nueve",
                                    "hastaPalabra": "planetas luminosos",
                                    "estado": "bortle_9_rojo_critico"
                                },
                                {
                                    "desdePalabra": "Por el contrario",
                                    "hastaPalabra": "de telescopios",
                                    "estado": "bortle_1_verde_pristino"
                                }
                            ]
                        }
                    ],
                    "infografia": {
                        "tipo": "dato_clave",
                        "titulo": "Escala Bortle",
                        "subtitulo": "Nivel de brillo del cielo nocturno",
                        "valorPrincipal": "9 a 1",
                        "unidad": "CLASES",
                        "items": [
                            {"etiqueta": "Clase 9: Centro Urbano", "valor": "17.5 mag", "porcentaje": 100, "color": "#EF4444"},
                            {"etiqueta": "Clase 5: Suburbio típico", "valor": "20.2 mag", "porcentaje": 55, "color": "#F59E0B"},
                            {"etiqueta": "Clase 1: Prístino", "valor": "22.0 mag", "porcentaje": 10, "color": "#10B981"}
                        ],
                        "colorAcento": "#FFE600",
                        "compacta": True,
                        "posicion": {"x": 420, "y": 10}
                    }
                }
            ]
        },
        {
            "id": "cap_3",
            "numero": 3,
            "titulo": "La Trampa Fotónica para el Reino Animal",
            "resumen": "Cómo la luz artificial desorienta a tortugas marinas y masacra a millones de aves migratorias.",
            "escenas": [
                {
                    "id": 5,
                    "texto": "El primer impacto devastador de la noche artificial golpeó directamente al reino animal. En las playas tropicales de todo el mundo, las tortugas marinas hembra y sus pequeñas crías recién nacidas han dependido durante millones de años del horizonte oceánico más brillante, iluminado de forma natural por la Luna y las estrellas sobre las olas. Sin embargo, las luces de complejos hoteleros, farolas costeras y avenidas desorientan a las crías en sentido opuesto. Millones de tortugas diminutas avanzan hacia las autopistas y el asfalto caliente, muriendo deshidratadas, atropelladas por vehículos o devoradas por depredadores terrestres antes del amanecer.",
                    "tituloVisual": "TORTUGAS MARINAS",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "playa_costa_nocturna",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.22,
                    "palabrasClave": ["reino animal", "tortugas marinas", "horizonte oceánico", "desorientan", "autopistas"],
                    "planos": [
                        {
                            "tipo": "general",
                            "desdePalabra": "El primer impacto",
                            "hastaPalabra": "sobre las olas",
                            "zoom": 1.0,
                            "blurFondo": 0
                        },
                        {
                            "tipo": "sobre_hombro",
                            "desdePalabra": "Sin embargo, las luces",
                            "hastaPalabra": "en sentido opuesto",
                            "x": -260,
                            "y": 480,
                            "zoom": 1.25,
                            "blurFondo": 4.0,
                            "hombroLado": "derecha"
                        },
                        {
                            "tipo": "primer_plano",
                            "desdePalabra": "Millones de tortugas",
                            "hastaPalabra": "antes del amanecer",
                            "x": -320,
                            "y": 500,
                            "zoom": 1.42,
                            "blurFondo": 6.0
                        }
                    ],
                    "personajes": [
                        {
                            "id": "stickman_narrador",
                            "posicion": {"x": -360, "y": 620},
                            "escala": 1.05,
                            "capaZ": 22,
                            "colorRim": "#38BDF8",
                            "acciones": [
                                {
                                    "pasos": [
                                        {
                                            "desdePalabra": "El primer impacto",
                                            "hastaPalabra": "sobre las olas",
                                            "posicion": {"x": -360, "y": 620},
                                            "poseId": "standing_confident",
                                            "expresion": "talking_enthusiastic",
                                            "orientacion": "derecha"
                                        },
                                        {
                                            "desdePalabra": "Sin embargo, las luces",
                                            "hastaPalabra": "antes del amanecer",
                                            "posicion": {"x": -300, "y": 620},
                                            "poseId": "shocked",
                                            "expresion": "sad",
                                            "orientacion": "derecha"
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    "objetos": [
                        {
                            "id": "cria_tortuga",
                            "propId": "tortuga_marina_desorientada",
                            "posicion": {"x": 260, "y": 140},
                            "escala": 1.25,
                            "capaZ": 28,
                            "pasos": [
                                {
                                    "desdePalabra": "El primer impacto",
                                    "hastaPalabra": "sobre las olas",
                                    "estado": "cria_naciendo_arena"
                                },
                                {
                                    "desdePalabra": "Sin embargo, las luces",
                                    "hastaPalabra": "en sentido opuesto",
                                    "estado": "desorientada_hacia_farolas"
                                },
                                {
                                    "desdePalabra": "Millones de tortugas",
                                    "hastaPalabra": "antes del amanecer",
                                    "estado": "salvada_rumbo_oceano"
                                }
                            ]
                        }
                    ],
                    "cotasVectoriales": [
                        {
                            "id": "cota_trampa_tortuga",
                            "valor": "DESORIENTACIÓN FATAL 180°",
                            "etiqueta": "Atracción destructiva hacia hoteles",
                            "origenX": 1180,
                            "origenY": 540,
                            "destinoX": 860,
                            "destinoY": 260,
                            "color": "#EF4444",
                            "desdePalabra": "Sin embargo, las luces",
                            "hastaPalabra": "en sentido opuesto"
                        }
                    ]
                },
                {
                    "id": 6,
                    "texto": "La trampa mortal se repite cada noche en el cielo aéreo de las grandes metrópolis. Cientos de millones de aves migratorias, guiadas por campos magnéticos y por la posición de las constelaciones celestes, atraviesan continentes enteros durante sus viajes estacionales. Al sobrevolar núcleos urbanos resplandecientes, quedan atrapadas en conos de luz enceguecedores, girando en círculos concéntricos durante horas hasta desplomarse al suelo por agotamiento físico absoluto. En ciudades como Chicago o Toronto, decenas de miles de aves canoras colisionan a gran velocidad contra torres vidriadas iluminadas, convirtiendo los centros financieros en verdaderos cementerios de biodiversidad alada.",
                    "tituloVisual": "AVES MIGRATORIAS",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_medio",
                    "escenario": "metropoli_noche_resplandor",
                    "transicion": "whip_left",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.22,
                    "palabrasClave": ["Cientos de millones", "aves migratorias", "constelaciones celestes", "conos de luz", "Chicago o Toronto"],
                    "planos": [
                        {
                            "tipo": "general",
                            "desdePalabra": "La trampa mortal",
                            "hastaPalabra": "viajes estacionales",
                            "zoom": 1.0,
                            "blurFondo": 0
                        },
                        {
                            "tipo": "sobre_hombro",
                            "desdePalabra": "Al sobrevolar núcleos",
                            "hastaPalabra": "agotamiento físico absoluto",
                            "x": 260,
                            "y": 480,
                            "zoom": 1.25,
                            "blurFondo": 4.0,
                            "hombroLado": "izquierda"
                        },
                        {
                            "tipo": "primer_plano",
                            "desdePalabra": "En ciudades como",
                            "hastaPalabra": "biodiversidad alada",
                            "x": 320,
                            "y": 500,
                            "zoom": 1.42,
                            "blurFondo": 6.0
                        }
                    ],
                    "personajes": [
                        {
                            "id": "stickman_narrador",
                            "posicion": {"x": 360, "y": 620},
                            "escala": 1.05,
                            "capaZ": 22,
                            "colorRim": "#38BDF8",
                            "acciones": [
                                {
                                    "pasos": [
                                        {
                                            "desdePalabra": "La trampa mortal",
                                            "hastaPalabra": "viajes estacionales",
                                            "posicion": {"x": 360, "y": 620},
                                            "poseId": "presenting_open",
                                            "expresion": "analytical",
                                            "orientacion": "izquierda"
                                        },
                                        {
                                            "desdePalabra": "Al sobrevolar núcleos",
                                            "hastaPalabra": "biodiversidad alada",
                                            "posicion": {"x": 300, "y": 620},
                                            "poseId": "worried",
                                            "expresion": "sad",
                                            "orientacion": "izquierda"
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    "objetos": [
                        {
                            "id": "aves_trampa",
                            "propId": "aves_migratorias_rascacielos",
                            "posicion": {"x": -240, "y": 140},
                            "escala": 1.25,
                            "capaZ": 28,
                            "pasos": [
                                {
                                    "desdePalabra": "La trampa mortal",
                                    "hastaPalabra": "viajes estacionales",
                                    "estado": "vuelo_migratorio_estelar"
                                },
                                {
                                    "desdePalabra": "Al sobrevolar núcleos",
                                    "hastaPalabra": "agotamiento físico absoluto",
                                    "estado": "atrapadas_espiral_luz"
                                },
                                {
                                    "desdePalabra": "En ciudades como",
                                    "hastaPalabra": "biodiversidad alada",
                                    "estado": "torre_apagada_vuelo_libre"
                                }
                            ]
                        }
                    ],
                    "cotasVectoriales": [
                        {
                            "id": "cota_aves_colision",
                            "valor": "CIENTOS DE MILLONES DE AVES",
                            "etiqueta": "Colisiones nocturnas contra cristal",
                            "origenX": 740,
                            "origenY": 540,
                            "destinoX": 940,
                            "destinoY": 260,
                            "color": "#EF4444",
                            "desdePalabra": "Al sobrevolar núcleos",
                            "hastaPalabra": "agotamiento físico absoluto"
                        }
                    ]
                }
            ]
        },
        {
            "id": "cap_4",
            "numero": 4,
            "titulo": "El Espectro Azul y la Destrucción del Sueño Humano",
            "resumen": "La transición al LED blanco de 460 nm y el apagado químico de la melatonina en el cerebro.",
            "escenas": [
                {
                    "id": 7,
                    "texto": "En las últimas dos décadas, una supuesta revolución de eficiencia energética empeoró drásticamente el problema: la transición global hacia el alumbrado público con diodos emisores de luz, conocidos como diodos led. Aunque consumen mucha menos electricidad, la mayoría de estas luminarias emiten una luz blanca fría con un pico de emisión letal en los cuatrocientos sesenta nanómetros, justo en la franja del azul brillante. Esta longitud de onda precisa activa de inmediato las células ganglionares retinianas intrínsecamente fotosensibles de nuestro ojo, enviando una falsa señal de mediodía solar al reloj biológico central del organismo.",
                    "tituloVisual": "PICO AZUL: 460 NM",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "metropoli_noche_resplandor",
                    "transicion": "zoom_in",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.22,
                    "palabrasClave": ["dos décadas", "diodos led", "luz blanca fría", "cuatrocientos sesenta nanómetros", "reloj biológico"],
                    "planos": [
                        {
                            "tipo": "general",
                            "desdePalabra": "En las últimas",
                            "hastaPalabra": "diodos led",
                            "zoom": 1.0,
                            "blurFondo": 0
                        },
                        {
                            "tipo": "plano_medio",
                            "desdePalabra": "Aunque consumen mucha",
                            "hastaPalabra": "del azul brillante",
                            "x": -180,
                            "y": 500,
                            "zoom": 1.24,
                            "blurFondo": 3.0
                        },
                        {
                            "tipo": "primer_plano",
                            "desdePalabra": "Esta longitud de onda",
                            "hastaPalabra": "central del organismo",
                            "x": -260,
                            "y": 490,
                            "zoom": 1.42,
                            "blurFondo": 6.0
                        }
                    ],
                    "personajes": [
                        {
                            "id": "stickman_narrador",
                            "posicion": {"x": -360, "y": 620},
                            "escala": 1.05,
                            "capaZ": 22,
                            "colorRim": "#38BDF8",
                            "acciones": [
                                {
                                    "pasos": [
                                        {
                                            "desdePalabra": "En las últimas",
                                            "hastaPalabra": "diodos led",
                                            "posicion": {"x": -360, "y": 620},
                                            "poseId": "standing_confident",
                                            "expresion": "talking_enthusiastic",
                                            "orientacion": "derecha"
                                        },
                                        {
                                            "desdePalabra": "Aunque consumen mucha",
                                            "hastaPalabra": "central del organismo",
                                            "posicion": {"x": -280, "y": 620},
                                            "poseId": "explaining_pointing_up",
                                            "expresion": "analytical",
                                            "orientacion": "derecha"
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    "objetos": [
                        {
                            "id": "espectro_led",
                            "propId": "espectro_led_azul_460nm",
                            "posicion": {"x": 260, "y": 140},
                            "escala": 1.25,
                            "capaZ": 28,
                            "pasos": [
                                {
                                    "desdePalabra": "En las últimas",
                                    "hastaPalabra": "diodos led",
                                    "estado": "pico_azul_led_frio_460nm"
                                },
                                {
                                    "desdePalabra": "Aunque consumen mucha",
                                    "hastaPalabra": "del azul brillante",
                                    "estado": "comparacion_sodio_calido"
                                },
                                {
                                    "desdePalabra": "Esta longitud de onda",
                                    "hastaPalabra": "central del organismo",
                                    "estado": "filtro_ambar_circadiano"
                                }
                            ]
                        }
                    ],
                    "cotasVectoriales": [
                        {
                            "id": "cota_nm_460",
                            "valor": "LONGITUD DE ONDA 460 NM",
                            "etiqueta": "Pico de máxima sensibilidad biológica",
                            "origenX": 1180,
                            "origenY": 540,
                            "destinoX": 860,
                            "destinoY": 260,
                            "color": "#38BDF8",
                            "desdePalabra": "Aunque consumen mucha",
                            "hastaPalabra": "del azul brillante"
                        }
                    ]
                },
                {
                    "id": 8,
                    "texto": "Cuando el cerebro humano recibe fotones azules durante la medianoche, el núcleo supraquiasmático detiene de forma instantánea la producción de melatonina en la glándula pineal. La melatonina no solo es la hormona fundamental que induce el sueño reparador y profundo, sino también un potente antioxidante celular que regula el sistema inmunológico y combate procesos tumorales. Diversos estudios epidemiológicos demuestran que las poblaciones sometidas a polución lumínica constante sufren tasas significativamente más elevadas de insomnio crónico, trastornos metabólicos, depresión severa y un incremento preocupante en el riesgo de cáncer de mama y próstata.",
                    "tituloVisual": "BLOQUEO DE MELATONINA",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "metropoli_noche_resplandor",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.22,
                    "palabrasClave": ["fotones azules", "núcleo supraquiasmático", "melatonina", "glándula pineal", "insomnio crónico"],
                    "planos": [
                        {
                            "tipo": "general",
                            "desdePalabra": "Cuando el cerebro",
                            "hastaPalabra": "la glándula pineal",
                            "zoom": 1.02,
                            "blurFondo": 0
                        },
                        {
                            "tipo": "plano_medio",
                            "desdePalabra": "La melatonina no solo",
                            "hastaPalabra": "procesos tumorales",
                            "x": -80,
                            "y": 510,
                            "zoom": 1.08,
                            "blurFondo": 2.0
                        },
                        {
                            "tipo": "plano_medio",
                            "desdePalabra": "Diversos estudios",
                            "hastaPalabra": "mama y próstata",
                            "x": -100,
                            "y": 510,
                            "zoom": 1.08,
                            "blurFondo": 2.0
                        }
                    ],
                    "personajes": [
                        {
                            "id": "stickman_narrador",
                            "posicion": {"x": -450, "y": 620},
                            "escala": 1.05,
                            "capaZ": 22,
                            "colorRim": "#FFE600",
                            "acciones": [
                                {
                                    "pasos": [
                                        {
                                            "desdePalabra": "Cuando el cerebro",
                                            "hastaPalabra": "la glándula pineal",
                                            "posicion": {"x": -450, "y": 620},
                                            "poseId": "thinking_hand_chin",
                                            "expresion": "analytical",
                                            "orientacion": "derecha"
                                        },
                                        {
                                            "desdePalabra": "La melatonina no solo",
                                            "hastaPalabra": "mama y próstata",
                                            "posicion": {"x": -410, "y": 620},
                                            "poseId": "worried",
                                            "expresion": "worried",
                                            "orientacion": "derecha"
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    "objetos": [
                        {
                            "id": "glandula_brain",
                            "propId": "glandula_pineal_melatonina",
                            "posicion": {"x": -105, "y": 140},
                            "escala": 1.25,
                            "capaZ": 28,
                            "pasos": [
                                {
                                    "desdePalabra": "Cuando el cerebro",
                                    "hastaPalabra": "la glándula pineal",
                                    "estado": "luz_azul_bloqueo_total"
                                },
                                {
                                    "desdePalabra": "La melatonina no solo",
                                    "hastaPalabra": "procesos tumorales",
                                    "estado": "melatonina_fluyendo_noche"
                                },
                                {
                                    "desdePalabra": "Diversos estudios",
                                    "hastaPalabra": "mama y próstata",
                                    "estado": "reloj_biologico_restaurado"
                                }
                            ]
                        }
                    ],
                    "infografia": {
                        "tipo": "comparacion",
                        "titulo": "Impacto Circadiano",
                        "subtitulo": "Supresión de melatonina por longitud de onda",
                        "items": [
                            {"etiqueta": "Luz Azul 460 nm (LED)", "valor": "85% Bloqueo", "porcentaje": 85, "color": "#38BDF8"},
                            {"etiqueta": "Luz Ámbar 590 nm (Sodio)", "valor": "12% Bloqueo", "porcentaje": 12, "color": "#F59E0B"},
                            {"etiqueta": "Oscuridad Natural", "valor": "0% Bloqueo", "porcentaje": 0, "color": "#10B981"}
                        ],
                        "colorAcento": "#EF4444",
                        "compacta": True,
                        "posicion": {"x": 420, "y": 10}
                    }
                }
            ]
        },
        {
            "id": "cap_5",
            "numero": 5,
            "titulo": "El Resplandor Difuso y la Ceguera Astronómica",
            "resumen": "La física de la dispersión Rayleigh y cómo los grandes telescopios históricos quedaron ciegos.",
            "escenas": [
                {
                    "id": 9,
                    "texto": "El daño visual de la luz artificial no se limita al perímetro de las calles asfaltadas, sino que se propaga por toda la atmósfera terrestre mediante el fenómeno del resplandor celeste. Cuando las luminarias emiten haces de fotones sin blindaje hacia arriba, la radiación choca contra las moléculas de nitrógeno, oxígeno y partículas de polvo en suspensión. Siguiendo la ley de dispersión de Rayleigh, las longitudes de onda cortas se esparcen en todas las direcciones del espacio, creando una cúpula luminiscente gigante que puede viajar a más de trescientos kilómetros de distancia del núcleo urbano.",
                    "tituloVisual": "DISPERSIÓN RAYLEIGH",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "metropoli_noche_resplandor",
                    "transicion": "zoom_in",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.22,
                    "palabrasClave": ["resplandor celeste", "fotones sin blindaje", "dispersión de Rayleigh", "trescientos kilómetros"],
                    "planos": [
                        {
                            "tipo": "general",
                            "desdePalabra": "El daño visual",
                            "hastaPalabra": "del resplandor celeste",
                            "zoom": 1.0,
                            "blurFondo": 0
                        },
                        {
                            "tipo": "plano_medio",
                            "desdePalabra": "Cuando las luminarias",
                            "hastaPalabra": "polvo en suspensión",
                            "x": -180,
                            "y": 500,
                            "zoom": 1.22,
                            "blurFondo": 3.0
                        },
                        {
                            "tipo": "primer_plano",
                            "desdePalabra": "Siguiendo la ley",
                            "hastaPalabra": "del núcleo urbano",
                            "x": -260,
                            "y": 490,
                            "zoom": 1.42,
                            "blurFondo": 6.0
                        }
                    ],
                    "personajes": [
                        {
                            "id": "stickman_narrador",
                            "posicion": {"x": -360, "y": 620},
                            "escala": 1.05,
                            "capaZ": 22,
                            "colorRim": "#38BDF8",
                            "acciones": [
                                {
                                    "pasos": [
                                        {
                                            "desdePalabra": "El daño visual",
                                            "hastaPalabra": "del resplandor celeste",
                                            "posicion": {"x": -360, "y": 620},
                                            "poseId": "standing_confident",
                                            "expresion": "talking_enthusiastic",
                                            "orientacion": "derecha"
                                        },
                                        {
                                            "desdePalabra": "Cuando las luminarias",
                                            "hastaPalabra": "del núcleo urbano",
                                            "posicion": {"x": -280, "y": 620},
                                            "poseId": "explaining_pointing_up",
                                            "expresion": "analytical",
                                            "orientacion": "derecha"
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    "objetos": [
                        {
                            "id": "skyglow_physics",
                            "propId": "resplandor_atmosferico_rayleigh",
                            "posicion": {"x": 260, "y": 140},
                            "escala": 1.25,
                            "capaZ": 28,
                            "pasos": [
                                {
                                    "desdePalabra": "El daño visual",
                                    "hastaPalabra": "del resplandor celeste",
                                    "estado": "dispersion_rayleigh_haz"
                                },
                                {
                                    "desdePalabra": "Siguiendo la ley",
                                    "hastaPalabra": "del núcleo urbano",
                                    "estado": "cupula_300km_alcance"
                                }
                            ]
                        }
                    ],
                    "cotasVectoriales": [
                        {
                            "id": "cota_300km",
                            "valor": "RADIO DE 300 KM DE ALCANCE",
                            "etiqueta": "Cúpula de dispersión molecular",
                            "origenX": 1180,
                            "origenY": 540,
                            "destinoX": 860,
                            "destinoY": 260,
                            "color": "#F59E0B",
                            "desdePalabra": "Siguiendo la ley",
                            "hastaPalabra": "del núcleo urbano"
                        }
                    ],
                    "emisoresParticulas": [
                        {
                            "tipo": "fotones_luz",
                            "x": 1200,
                            "y": 620,
                            "color": "#FDE047",
                            "desdePalabra": "El daño visual",
                            "hastaPalabra": "del núcleo urbano"
                        }
                    ]
                },
                {
                    "id": 10,
                    "texto": "Esta niebla luminosa perpetua ha dejado prácticamente ciegos a los observatorios astronómicos históricos construidos cerca de las grandes poblaciones. Centros legendarios como Monte Wilson en California, donde Edwin Hubble descubrió la expansión del universo en mil novecientos veintinueve, hoy enfrentan un cielo nocturno mil veces más brillante que su valor natural. Los astrónomos contemporáneos se han visto forzados a abandonar estos telescopios gigantes y buscar refugio en cumbres remotas a miles de metros de altitud, huyendo de una civilización que borró con farolas y carteles de neón el mapa del universo profundo.",
                    "tituloVisual": "MONTE WILSON, 1929",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_medio",
                    "escenario": "observatorio_astronomico_cumbre",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.22,
                    "palabrasClave": ["observatorios astronómicos", "Monte Wilson", "Edwin Hubble", "mil novecientos veintinueve", "universo profundo"],
                    "planos": [
                        {
                            "tipo": "general",
                            "desdePalabra": "Esta niebla luminosa",
                            "hastaPalabra": "las grandes poblaciones",
                            "zoom": 1.0,
                            "blurFondo": 0
                        },
                        {
                            "tipo": "sobre_hombro",
                            "desdePalabra": "Centros legendarios como",
                            "hastaPalabra": "su valor natural",
                            "x": 260,
                            "y": 480,
                            "zoom": 1.25,
                            "blurFondo": 4.0,
                            "hombroLado": "izquierda"
                        },
                        {
                            "tipo": "primer_plano",
                            "desdePalabra": "Los astrónomos contemporáneos",
                            "hastaPalabra": "del universo profundo",
                            "x": 320,
                            "y": 500,
                            "zoom": 1.42,
                            "blurFondo": 6.0
                        }
                    ],
                    "personajes": [
                        {
                            "id": "stickman_narrador",
                            "posicion": {"x": 360, "y": 620},
                            "escala": 1.05,
                            "capaZ": 22,
                            "colorRim": "#38BDF8",
                            "acciones": [
                                {
                                    "pasos": [
                                        {
                                            "desdePalabra": "Esta niebla luminosa",
                                            "hastaPalabra": "las grandes poblaciones",
                                            "posicion": {"x": 360, "y": 620},
                                            "poseId": "presenting_open",
                                            "expresion": "analytical",
                                            "orientacion": "izquierda"
                                        },
                                        {
                                            "desdePalabra": "Centros legendarios como",
                                            "hastaPalabra": "del universo profundo",
                                            "posicion": {"x": 300, "y": 620},
                                            "poseId": "thinking_hand_chin",
                                            "expresion": "worried",
                                            "orientacion": "izquierda"
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    "objetos": [
                        {
                            "id": "telescopio_cegado",
                            "propId": "telescopio_cegado_polucion",
                            "posicion": {"x": -240, "y": 140},
                            "escala": 1.25,
                            "capaZ": 28,
                            "pasos": [
                                {
                                    "desdePalabra": "Esta niebla luminosa",
                                    "hastaPalabra": "las grandes poblaciones",
                                    "estado": "telescopio_cegado_resplandor"
                                },
                                {
                                    "desdePalabra": "Centros legendarios como",
                                    "hastaPalabra": "su valor natural",
                                    "estado": "sensor_ccd_saturado_ruido"
                                },
                                {
                                    "desdePalabra": "Los astrónomos contemporáneos",
                                    "hastaPalabra": "del universo profundo",
                                    "estado": "telescopio_remoto_cumbre"
                                }
                            ]
                        }
                    ],
                    "cotasVectoriales": [
                        {
                            "id": "cota_1000x",
                            "valor": "1.000 VECES MÁS BRILLANTE",
                            "etiqueta": "Saturación del fondo celeste histórico",
                            "origenX": 740,
                            "origenY": 540,
                            "destinoX": 940,
                            "destinoY": 260,
                            "color": "#FFE600",
                            "desdePalabra": "Centros legendarios como",
                            "hastaPalabra": "su valor natural"
                        }
                    ]
                }
            ]
        },
        {
            "id": "cap_6",
            "numero": 6,
            "titulo": "La Maqueta Urbana: Soluciones Ópticas y Blindaje",
            "resumen": "El Stickman analiza el derroche en la maqueta y aplica el blindaje Full Cut-off.",
            "escenas": [
                {
                    "id": 11,
                    "texto": "Para comprender cómo revertir esta crisis invisible, el Stickman examina una maqueta de control eléctrico que simula la distribución de energía en una metrópoli moderna. Gran parte del desperdicio proviene de luminarias esféricas o mal orientadas que dispersan más del cincuenta por ciento de sus lúmenes hacia el firmamento, iluminando las copas de los árboles y las fachadas de los edificios en lugar del suelo. El alumbrado público representa miles de millones de kilovatios hora desperdiciados anualmente, lo que se traduce en millones de toneladas de dióxido de carbono emitidas inútilmente a la atmósfera.",
                    "tituloVisual": "MAQUETA DE CONTROL",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "maqueta_urbana_interruptores",
                    "transicion": "zoom_in",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.22,
                    "palabrasClave": ["maqueta de control", "cincuenta por ciento", "firmamento", "kilovatios hora", "dióxido de carbono"],
                    "planos": [
                        {
                            "tipo": "general",
                            "desdePalabra": "Para comprender",
                            "hastaPalabra": "metrópoli moderna",
                            "zoom": 1.0,
                            "blurFondo": 0
                        },
                        {
                            "tipo": "plano_medio",
                            "desdePalabra": "Gran parte del desperdicio",
                            "hastaPalabra": "en lugar del suelo",
                            "x": -180,
                            "y": 500,
                            "zoom": 1.22,
                            "blurFondo": 3.0
                        },
                        {
                            "tipo": "primer_plano",
                            "desdePalabra": "El alumbrado público",
                            "hastaPalabra": "inútilmente a la atmósfera",
                            "x": -260,
                            "y": 490,
                            "zoom": 1.42,
                            "blurFondo": 6.0
                        }
                    ],
                    "personajes": [
                        {
                            "id": "stickman_narrador",
                            "posicion": {"x": -360, "y": 620},
                            "escala": 1.05,
                            "capaZ": 22,
                            "colorRim": "#38BDF8",
                            "acciones": [
                                {
                                    "pasos": [
                                        {
                                            "desdePalabra": "Para comprender",
                                            "hastaPalabra": "metrópoli moderna",
                                            "posicion": {"x": -360, "y": 620},
                                            "poseId": "walking",
                                            "expresion": "talking_enthusiastic",
                                            "orientacion": "derecha",
                                            "procedural": "caminar"
                                        },
                                        {
                                            "desdePalabra": "Gran parte del desperdicio",
                                            "hastaPalabra": "inútilmente a la atmósfera",
                                            "posicion": {"x": -280, "y": 620},
                                            "poseId": "explaining_pointing_up",
                                            "expresion": "analytical",
                                            "orientacion": "derecha",
                                            "procedural": "manipular"
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    "objetos": [
                        {
                            "id": "maqueta_red",
                            "propId": "maqueta_control_iluminacion",
                            "posicion": {"x": 260, "y": 140},
                            "escala": 1.25,
                            "capaZ": 28,
                            "pasos": [
                                {
                                    "desdePalabra": "Para comprender",
                                    "hastaPalabra": "metrópoli moderna",
                                    "estado": "maqueta_ciudades_encendidas"
                                },
                                {
                                    "desdePalabra": "Gran parte del desperdicio",
                                    "hastaPalabra": "en lugar del suelo",
                                    "estado": "desperdicio_lumenes_cielo"
                                },
                                {
                                    "desdePalabra": "El alumbrado público",
                                    "hastaPalabra": "inútilmente a la atmósfera",
                                    "estado": "red_optimizada_eficiente"
                                }
                            ]
                        }
                    ],
                    "cotasVectoriales": [
                        {
                            "id": "cota_50_desperdicio",
                            "valor": "> 50% LUZ MAL DIRIGIDA",
                            "etiqueta": "Pérdida energética hacia el cielo",
                            "origenX": 1180,
                            "origenY": 540,
                            "destinoX": 860,
                            "destinoY": 260,
                            "color": "#EF4444",
                            "desdePalabra": "Gran parte del desperdicio",
                            "hastaPalabra": "en lugar del suelo"
                        }
                    ]
                },
                {
                    "id": 12,
                    "texto": "La física y la ingeniería óptica demuestran que resolver la contaminación lumínica no requiere apagar las ciudades ni sumir las calles en la inseguridad. La solución radica en utilizar luminarias con blindaje total que dirijan el cien por ciento del haz luminoso hacia el suelo, evitando cualquier emisión hacia la línea del horizonte. Asimismo, sustituir los diodos led blancos de cinco mil kelvin por fuentes cálidas de dos mil doscientos kelvin reduce la dispersión atmosférica a una tercera parte, devolviendo la visibilidad al cielo nocturno sin comprometer la seguridad de peatones ni conductores.",
                    "tituloVisual": "LUMINARIAS FULL CUT-OFF",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_medio",
                    "escenario": "maqueta_urbana_interruptores",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.22,
                    "palabrasClave": ["ingeniería óptica", "blindaje total", "cien por ciento", "dos mil doscientos kelvin", "tercera parte"],
                    "planos": [
                        {
                            "tipo": "general",
                            "desdePalabra": "La física y",
                            "hastaPalabra": "en la inseguridad",
                            "zoom": 1.0,
                            "blurFondo": 0
                        },
                        {
                            "tipo": "sobre_hombro",
                            "desdePalabra": "La solución radica",
                            "hastaPalabra": "línea del horizonte",
                            "x": 260,
                            "y": 480,
                            "zoom": 1.25,
                            "blurFondo": 4.0,
                            "hombroLado": "izquierda"
                        },
                        {
                            "tipo": "primer_plano",
                            "desdePalabra": "Asimismo, sustituir",
                            "hastaPalabra": "peatones ni conductores",
                            "x": 320,
                            "y": 500,
                            "zoom": 1.42,
                            "blurFondo": 6.0
                        }
                    ],
                    "personajes": [
                        {
                            "id": "stickman_narrador",
                            "posicion": {"x": 360, "y": 620},
                            "escala": 1.05,
                            "capaZ": 22,
                            "colorRim": "#38BDF8",
                            "acciones": [
                                {
                                    "pasos": [
                                        {
                                            "desdePalabra": "La física y",
                                            "hastaPalabra": "en la inseguridad",
                                            "posicion": {"x": 360, "y": 620},
                                            "poseId": "standing_confident",
                                            "expresion": "talking_enthusiastic",
                                            "orientacion": "izquierda"
                                        },
                                        {
                                            "desdePalabra": "La solución radica",
                                            "hastaPalabra": "peatones ni conductores",
                                            "posicion": {"x": 300, "y": 620},
                                            "poseId": "explaining_pointing_up",
                                            "expresion": "eureka",
                                            "orientacion": "izquierda"
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    "objetos": [
                        {
                            "id": "optica_cutoff",
                            "propId": "luminaria_full_cutoff",
                            "posicion": {"x": -240, "y": 140},
                            "escala": 1.25,
                            "capaZ": 28,
                            "pasos": [
                                {
                                    "desdePalabra": "La física y",
                                    "hastaPalabra": "en la inseguridad",
                                    "estado": "luminaria_globo_fuga_arriba"
                                },
                                {
                                    "desdePalabra": "La solución radica",
                                    "hastaPalabra": "línea del horizonte",
                                    "estado": "diseno_full_cutoff_plano"
                                },
                                {
                                    "desdePalabra": "Asimismo, sustituir",
                                    "hastaPalabra": "peatones ni conductores",
                                    "estado": "sensor_movimiento_atenuacion"
                                }
                            ]
                        }
                    ],
                    "cotasVectoriales": [
                        {
                            "id": "cota_0_fuga",
                            "valor": "0% EMISIÓN SOBRE EL HORIZONTE",
                            "etiqueta": "Haz 100% dirigido al pavimento",
                            "origenX": 740,
                            "origenY": 540,
                            "destinoX": 940,
                            "destinoY": 260,
                            "color": "#10B981",
                            "desdePalabra": "La solución radica",
                            "hastaPalabra": "línea del horizonte"
                        }
                    ]
                }
            ]
        },
        {
            "id": "cap_7",
            "numero": 7,
            "titulo": "Reservas Starlight y los Últimos Santuarios",
            "resumen": "Viaje a Atacama y La Palma: la experiencia sensorial de un cielo prístino de Clase 1.",
            "escenas": [
                {
                    "id": 13,
                    "texto": "Para proteger lo que aún queda de la noche prístina, la comunidad científica internacional ha establecido reservas y parques de cielo oscuro en los rincones más aislados del planeta. Lugares excepcionales como el desierto de Atacama en Chile y la isla de La Palma en Canarias cuentan con leyes estrictas que prohíben luminarias contaminantes a cientos de kilómetros a la redonda. En estos santuarios protegidos, la atmósfera extremadamente seca y la ausencia total de resplandor artificial permiten que telescopios de última generación capturen fotones que viajaron durante más de trece mil millones de años cósmicos.",
                    "tituloVisual": "SANTUARIOS STARLIGHT",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "santuario_cielo_estrellado",
                    "transicion": "zoom_in",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.22,
                    "palabrasClave": ["parques de cielo oscuro", "desierto de Atacama", "La Palma en Canarias", "trece mil millones de años"],
                    "planos": [
                        {
                            "tipo": "general",
                            "desdePalabra": "Para proteger",
                            "hastaPalabra": "aislados del planeta",
                            "zoom": 1.0,
                            "blurFondo": 0
                        },
                        {
                            "tipo": "sobre_hombro",
                            "desdePalabra": "Lugares excepcionales como",
                            "hastaPalabra": "a la redonda",
                            "x": -260,
                            "y": 480,
                            "zoom": 1.25,
                            "blurFondo": 3.5,
                            "hombroLado": "derecha"
                        },
                        {
                            "tipo": "detalle_mano",
                            "desdePalabra": "En estos santuarios",
                            "hastaPalabra": "años cósmicos",
                            "zoom": 1.30,
                            "blurFondo": 6.5,
                            "accionMano": "ajustar_telescopio",
                            "etiquetaInsert": "ENFOQUE ÓPTICO ULTRA-PROFUNDO"
                        }
                    ],
                    "personajes": [
                        {
                            "id": "stickman_narrador",
                            "posicion": {"x": -360, "y": 620},
                            "escala": 1.05,
                            "capaZ": 22,
                            "colorRim": "#38BDF8",
                            "acciones": [
                                {
                                    "pasos": [
                                        {
                                            "desdePalabra": "Para proteger",
                                            "hastaPalabra": "aislados del planeta",
                                            "posicion": {"x": -360, "y": 620},
                                            "poseId": "standing_confident",
                                            "expresion": "talking_enthusiastic",
                                            "orientacion": "derecha"
                                        },
                                        {
                                            "desdePalabra": "Lugares excepcionales como",
                                            "hastaPalabra": "años cósmicos",
                                            "posicion": {"x": -280, "y": 620},
                                            "poseId": "explaining_pointing_up",
                                            "expresion": "eureka",
                                            "orientacion": "derecha"
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    "objetos": [
                        {
                            "id": "cupula_atacama",
                            "propId": "observatorio_atacama_cupula",
                            "posicion": {"x": 260, "y": 140},
                            "escala": 1.25,
                            "capaZ": 28,
                            "pasos": [
                                {
                                    "desdePalabra": "Para proteger",
                                    "hastaPalabra": "aislados del planeta",
                                    "estado": "cupula_atacama_abierta"
                                },
                                {
                                    "desdePalabra": "Lugares excepcionales como",
                                    "hastaPalabra": "a la redonda",
                                    "estado": "laser_estrella_guia"
                                },
                                {
                                    "desdePalabra": "En estos santuarios",
                                    "hastaPalabra": "años cósmicos",
                                    "estado": "cielo_profundo_cosmos"
                                }
                            ]
                        }
                    ],
                    "cotasVectoriales": [
                        {
                            "id": "cota_13000m",
                            "valor": "13.000 MILLONES DE AÑOS LUZ",
                            "etiqueta": "Observación sin ruido atmosférico",
                            "origenX": 1180,
                            "origenY": 540,
                            "destinoX": 860,
                            "destinoY": 260,
                            "color": "#38BDF8",
                            "desdePalabra": "Lugares excepcionales como",
                            "hastaPalabra": "a la redonda"
                        }
                    ],
                    "emisoresParticulas": [
                        {
                            "tipo": "polvo_estelar",
                            "x": 960,
                            "y": 280,
                            "color": "#FFE600",
                            "desdePalabra": "Para proteger",
                            "hastaPalabra": "años cósmicos"
                        }
                    ]
                },
                {
                    "id": 14,
                    "texto": "Cuando una persona se adentra en un santuario de clase uno de la escala Bortle, la experiencia sensorial redefine por completo su percepción de la realidad. En un cielo sin polución lumínica, las estrellas no titilan tímidamente: resplandecen como diamantes ardientes sobre un terciopelo oscuro, mientras las nubes oscuras de polvo interestelar dibujan la silueta completa de la Vía Láctea. Incluso es posible distinguir el suave resplandor de la luz zodiacal y las tonalidades tenues del brillo atmosférico natural, recordándonos que el universo es un espectáculo accesible para los ojos de cualquier ser humano.",
                    "tituloVisual": "BORTLE CLASE 1: COSMOS",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_medio",
                    "escenario": "santuario_cielo_estrellado",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_ambient_chime.wav",
                    "volumenSfx": 0.24,
                    "palabrasClave": ["clase uno", "escala Bortle", "Vía Láctea", "luz zodiacal", "brillo atmosférico"],
                    "planos": [
                        {
                            "tipo": "general",
                            "desdePalabra": "Cuando una persona",
                            "hastaPalabra": "de la realidad",
                            "zoom": 1.0,
                            "blurFondo": 0
                        },
                        {
                            "tipo": "sobre_hombro",
                            "desdePalabra": "En un cielo sin",
                            "hastaPalabra": "la Vía Láctea",
                            "x": 260,
                            "y": 480,
                            "zoom": 1.25,
                            "blurFondo": 3.5,
                            "hombroLado": "izquierda"
                        },
                        {
                            "tipo": "primer_plano",
                            "desdePalabra": "Incluso es posible",
                            "hastaPalabra": "cualquier ser humano",
                            "x": 320,
                            "y": 500,
                            "zoom": 1.45,
                            "blurFondo": 6.0
                        }
                    ],
                    "personajes": [
                        {
                            "id": "stickman_narrador",
                            "posicion": {"x": 360, "y": 620},
                            "escala": 1.05,
                            "capaZ": 22,
                            "colorRim": "#FFE600",
                            "acciones": [
                                {
                                    "pasos": [
                                        {
                                            "desdePalabra": "Cuando una persona",
                                            "hastaPalabra": "de la realidad",
                                            "posicion": {"x": 360, "y": 620},
                                            "poseId": "presenting_open",
                                            "expresion": "talking_enthusiastic",
                                            "orientacion": "izquierda"
                                        },
                                        {
                                            "desdePalabra": "En un cielo sin",
                                            "hastaPalabra": "cualquier ser humano",
                                            "posicion": {"x": 300, "y": 620},
                                            "poseId": "standing_confident",
                                            "expresion": "eureka",
                                            "orientacion": "izquierda"
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    "objetos": [
                        {
                            "id": "cielo_bortle_uno",
                            "propId": "cielo_milkyway_revelacion",
                            "posicion": {"x": -240, "y": 140},
                            "escala": 1.25,
                            "capaZ": 28,
                            "pasos": [
                                {
                                    "desdePalabra": "Cuando una persona",
                                    "hastaPalabra": "cualquier ser humano",
                                    "estado": "via_lactea_resplandeciente"
                                }
                            ]
                        }
                    ],
                    "cotasVectoriales": [
                        {
                            "id": "cota_bortle_1_luz",
                            "valor": "MAGNITUD LIMITE 7.6 - 8.0",
                            "etiqueta": "Miles de estrellas y luz zodiacal",
                            "origenX": 740,
                            "origenY": 540,
                            "destinoX": 940,
                            "destinoY": 260,
                            "color": "#10B981",
                            "desdePalabra": "En un cielo sin",
                            "hastaPalabra": "la Vía Láctea"
                        }
                    ],
                    "emisoresParticulas": [
                        {
                            "tipo": "polvo_estelar",
                            "x": 960,
                            "y": 280,
                            "color": "#38BDF8",
                            "desdePalabra": "Cuando una persona",
                            "hastaPalabra": "cualquier ser humano"
                        }
                    ]
                }
            ]
        },
        {
            "id": "cap_8",
            "numero": 8,
            "titulo": "El Gran Apagón Maestro: Reconquistando la Noche",
            "resumen": "El Stickman baja la palanca maestra y la Vía Láctea vuelve a iluminar la metrópoli.",
            "escenas": [
                {
                    "id": 15,
                    "texto": "De vuelta en la maqueta de control urbano, el Stickman se prepara para la acción definitiva: tirar de la palanca del interruptor maestro y cortar la iluminación desmedida de la metrópoli. Al desconectar los reflectores comerciales innecesarios, regular las farolas hacia el suelo y apagar los anuncios publicitarios nocturnos, la densa cúpula de resplandor anaranjado comienza a desvanecerse en cuestión de segundos. Una a una, las constelaciones que inspiraron a los navegantes, filósofos y científicos de la antigüedad vuelven a proyectarse con nitidez sobre los tejados y parques de la ciudad liberada.",
                    "tituloVisual": "EL INTERRUPTOR MAESTRO",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "maqueta_urbana_interruptores",
                    "transicion": "zoom_in",
                    "efectosCamara": ["shake", "drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.28,
                    "palabrasClave": ["interruptor maestro", "iluminación desmedida", "cúpula de resplandor", "constelaciones", "ciudad liberada"],
                    "planos": [
                        {
                            "tipo": "general",
                            "desdePalabra": "De vuelta en",
                            "hastaPalabra": "de la metrópoli",
                            "zoom": 1.0,
                            "blurFondo": 0
                        },
                        {
                            "tipo": "detalle_mano",
                            "desdePalabra": "Al desconectar los reflectores",
                            "hastaPalabra": "cuestión de segundos",
                            "zoom": 1.30,
                            "blurFondo": 6.5,
                            "accionMano": "bajar_interruptor",
                            "etiquetaInsert": "DESCONEXIÓN MAESTRA DE RED"
                        },
                        {
                            "tipo": "primer_plano",
                            "desdePalabra": "Una a una",
                            "hastaPalabra": "la ciudad liberada",
                            "x": -260,
                            "y": 490,
                            "zoom": 1.42,
                            "blurFondo": 6.0
                        }
                    ],
                    "personajes": [
                        {
                            "id": "stickman_narrador",
                            "posicion": {"x": -360, "y": 620},
                            "escala": 1.05,
                            "capaZ": 22,
                            "colorRim": "#38BDF8",
                            "acciones": [
                                {
                                    "pasos": [
                                        {
                                            "desdePalabra": "De vuelta en",
                                            "hastaPalabra": "de la metrópoli",
                                            "posicion": {"x": -360, "y": 620},
                                            "poseId": "standing_confident",
                                            "expresion": "determined",
                                            "orientacion": "derecha",
                                            "procedural": "esfuerzo"
                                        },
                                        {
                                            "desdePalabra": "Al desconectar los reflectores",
                                            "hastaPalabra": "la ciudad liberada",
                                            "posicion": {"x": -280, "y": 620},
                                            "poseId": "explaining_pointing_up",
                                            "expresion": "eureka",
                                            "orientacion": "derecha"
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    "objetos": [
                        {
                            "id": "switch_master",
                            "propId": "interruptor_maestro_apagon",
                            "posicion": {"x": 260, "y": 140},
                            "escala": 1.25,
                            "capaZ": 28,
                            "pasos": [
                                {
                                    "desdePalabra": "De vuelta en",
                                    "hastaPalabra": "de la metrópoli",
                                    "estado": "interruptor_conectado_alerta"
                                },
                                {
                                    "desdePalabra": "Al desconectar los reflectores",
                                    "hastaPalabra": "cuestión de segundos",
                                    "estado": "palanca_bajando_corte"
                                },
                                {
                                    "desdePalabra": "Una a una",
                                    "hastaPalabra": "la ciudad liberada",
                                    "estado": "sistema_apagado_estrellas"
                                }
                            ]
                        }
                    ],
                    "cotasVectoriales": [
                        {
                            "id": "cota_apagon_eficiente",
                            "valor": "-100% CONTAMINACIÓN INÚTIL",
                            "etiqueta": "El resplandor se extingue en segundos",
                            "origenX": 1180,
                            "origenY": 540,
                            "destinoX": 860,
                            "destinoY": 260,
                            "color": "#10B981",
                            "desdePalabra": "Al desconectar los reflectores",
                            "hastaPalabra": "cuestión de segundos"
                        }
                    ]
                },
                {
                    "id": 16,
                    "texto": "Recuperar la oscuridad de la noche no significa retroceder a la época de las cavernas, sino madurar como especie y aprender a iluminar con inteligencia y respeto por el entorno. El cielo estrellado fue la primera pantalla de cine de la humanidad, la cuna de las matemáticas, la navegación y la ciencia astronómica. Proteger la oscuridad natural del firmamento es preservar nuestro propio equilibrio biológico, proteger la vida salvaje del planeta y mantener abierta para las futuras generaciones la ventana más asombrosa y humilde que tenemos hacia la inmensidad del cosmos infinito.",
                    "tituloVisual": "NUESTRA VENTANA CÓSMICA",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_medio",
                    "escenario": "santuario_cielo_estrellado",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_ambient_chime.wav",
                    "volumenSfx": 0.24,
                    "palabrasClave": ["oscuridad de la noche", "madurar como especie", "primera pantalla de cine", "equilibrio biológico", "cosmos infinito"],
                    "planos": [
                        {
                            "tipo": "general",
                            "desdePalabra": "Recuperar la oscuridad",
                            "hastaPalabra": "respeto por el entorno",
                            "zoom": 1.0,
                            "blurFondo": 0
                        },
                        {
                            "tipo": "sobre_hombro",
                            "desdePalabra": "El cielo estrellado",
                            "hastaPalabra": "la ciencia astronómica",
                            "x": 260,
                            "y": 480,
                            "zoom": 1.25,
                            "blurFondo": 3.5,
                            "hombroLado": "izquierda"
                        },
                        {
                            "tipo": "primer_plano",
                            "desdePalabra": "Proteger la oscuridad",
                            "hastaPalabra": "del cosmos infinito",
                            "x": 320,
                            "y": 500,
                            "zoom": 1.45,
                            "blurFondo": 6.0
                        }
                    ],
                    "personajes": [
                        {
                            "id": "stickman_narrador",
                            "posicion": {"x": 360, "y": 620},
                            "escala": 1.05,
                            "capaZ": 22,
                            "colorRim": "#FFE600",
                            "acciones": [
                                {
                                    "pasos": [
                                        {
                                            "desdePalabra": "Recuperar la oscuridad",
                                            "hastaPalabra": "respeto por el entorno",
                                            "posicion": {"x": 360, "y": 620},
                                            "poseId": "standing_confident",
                                            "expresion": "talking_enthusiastic",
                                            "orientacion": "izquierda"
                                        },
                                        {
                                            "desdePalabra": "El cielo estrellado",
                                            "hastaPalabra": "del cosmos infinito",
                                            "posicion": {"x": 300, "y": 620},
                                            "poseId": "presenting_open",
                                            "expresion": "eureka",
                                            "orientacion": "izquierda"
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    "objetos": [
                        {
                            "id": "sintesis_universo",
                            "propId": "cielo_milkyway_revelacion",
                            "posicion": {"x": -240, "y": 140},
                            "escala": 1.25,
                            "capaZ": 28,
                            "pasos": [
                                {
                                    "desdePalabra": "Recuperar la oscuridad",
                                    "hastaPalabra": "del cosmos infinito",
                                    "estado": "via_lactea_resplandeciente"
                                }
                            ]
                        }
                    ],
                    "cotasVectoriales": [
                        {
                            "id": "cota_final_cosmos",
                            "valor": "LA VENTANA AL COSMOS",
                            "etiqueta": "Patrimonio universal de la humanidad",
                            "origenX": 740,
                            "origenY": 540,
                            "destinoX": 940,
                            "destinoY": 260,
                            "color": "#FFE600",
                            "desdePalabra": "Proteger la oscuridad",
                            "hastaPalabra": "del cosmos infinito"
                        }
                    ],
                    "emisoresParticulas": [
                        {
                            "tipo": "polvo_estelar",
                            "x": 960,
                            "y": 280,
                            "color": "#FFE600",
                            "desdePalabra": "Recuperar la oscuridad",
                            "hastaPalabra": "del cosmos infinito"
                        }
                    ]
                }
            ]
        }
    ]
}

def validar_palabras(guion_obj):
    total_palabras = 0
    print("\n--- AUDITORÍA DE CONTEO DE PALABRAS POR ESCENA ---")
    for cap in guion_obj["capitulos"]:
        for esc in cap["escenas"]:
            palabras = esc["texto"].split()
            count = len(palabras)
            total_palabras += count
            print(f"Cap {cap['numero']} | Esc {esc['id']:2d}: {count:3d} palabras | Inicio: {' '.join(palabras[:4])}...")
            # Verificar si contiene números en dígitos en texto
            digitos = re.findall(r'\b\d+\b', esc["texto"])
            if digitos:
                print(f"  ⚠️ ALERTA: Contiene dígitos arábigos: {digitos}")
            
            # Verificar anchor words
            texto = esc["texto"]
            if "planos" in esc:
                for pl in esc["planos"]:
                    if pl.get("desdePalabra") and pl["desdePalabra"] not in texto:
                        print(f"  ❌ Error plano desdePalabra: '{pl['desdePalabra']}' no está en texto de Esc {esc['id']}")
                    if pl.get("hastaPalabra") and pl["hastaPalabra"] not in texto:
                        print(f"  ❌ Error plano hastaPalabra: '{pl['hastaPalabra']}' no está en texto de Esc {esc['id']}")
            if "personajes" in esc:
                for p in esc["personajes"]:
                    for ac in p.get("acciones", []):
                        for paso in ac.get("pasos", []):
                            if paso.get("desdePalabra") and paso["desdePalabra"] not in texto:
                                print(f"  ❌ Error personaje desdePalabra: '{paso['desdePalabra']}' no está en texto de Esc {esc['id']}")
                            if paso.get("hastaPalabra") and paso["hastaPalabra"] not in texto:
                                print(f"  ❌ Error personaje hastaPalabra: '{paso['hastaPalabra']}' no está en texto de Esc {esc['id']}")
            if "objetos" in esc:
                for obj in esc["objetos"]:
                    for paso in obj.get("pasos", []):
                        if paso.get("desdePalabra") and paso["desdePalabra"] not in texto:
                            print(f"  ❌ Error objeto desdePalabra: '{paso['desdePalabra']}' no está en texto de Esc {esc['id']}")
                        if paso.get("hastaPalabra") and paso["hastaPalabra"] not in texto:
                            print(f"  ❌ Error objeto hastaPalabra: '{paso['hastaPalabra']}' no está en texto de Esc {esc['id']}")
            if "cotasVectoriales" in esc:
                for c in esc["cotasVectoriales"]:
                    if c.get("desdePalabra") and c["desdePalabra"] not in texto:
                        print(f"  ❌ Error cota desdePalabra: '{c['desdePalabra']}' no está en texto de Esc {esc['id']}")
                    if c.get("hastaPalabra") and c["hastaPalabra"] not in texto:
                        print(f"  ❌ Error cota hastaPalabra: '{c['hastaPalabra']}' no está en texto de Esc {esc['id']}")

    print(f"\nTOTAL PALABRAS DEL GUION: {total_palabras}")
    if total_palabras < 1400:
        raise ValueError(f"El conteo total ({total_palabras}) es inferior a 1,400 palabras requeridas.")
    print("[OK] Conteo de palabras cumple sobradamente con la regla de duracion mid-roll (>= 1,400 palabras).")

if __name__ == "__main__":
    validar_palabras(guion)
    with open(GUION_PATH, "w", encoding="utf-8") as f:
        json.dump(guion, f, ensure_ascii=False, indent=2)
    print(f"\n[OK] Guion guardado exitosamente en: {GUION_PATH}")
