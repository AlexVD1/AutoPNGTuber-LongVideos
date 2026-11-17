#!/usr/bin/env python3
"""
Lote 3: Documentales 012, 013, 014 y 015 expandidos a 6.5 - 8.0 minutos.
"""

from redactar_guiones_largos_completos import actualizar_guion


def construir_doc_012():
    capitulos = [
        {
            "id": "cap_1",
            "numero": 1,
            "titulo": "Los Monstruos Invisibles del Musgo",
            "resumen": "El descubrimiento de los osos de agua por Goeze en 1773.",
            "escenas": [
                {
                    "id": 1,
                    "texto": "Si tomas un trozo de musgo húmedo del jardín de tu casa, lo colocas bajo la lente de un microscopio óptico y agregas unas gotas de agua limpia, es casi seguro que presenciarás a uno de los seres más extraños e indestructibles de la naturaleza: un animal microscópico de ocho patas rechonchas armadas con garras afiladas que camina con la pesada parsimonia de un oso pardo en miniatura. En mil setecientos setenta y tres, el pastor y zoólogo alemán Johann August Ephraim Goeze los descubrió fascinado y los bautizó informalmente como pequeños osos de agua.",
                    "tituloVisual": "OSOS DE AGUA (1773)",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "cielo_dia",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["microscopio óptico", "oso pardo en miniatura", "Johann Goeze", "ocho patas rechonchas"],
                    "poseId": "walking_confidently",
                    "expresion": "analytical"
                },
                {
                    "id": 2,
                    "texto": "Tres años más tarde, el biólogo italiano Lazzaro Spallanzani les otorgó su nombre científico definitivo: tardígrados, que en latín significa literalmente los de paso lento. Miden apenas medio milímetro de longitud, poseen una anatomía con sistema digestivo, boca tubular succionadora y ojos primitivos, y habitan prácticamente en todos los rincones del globo: desde las cumbres heladas del Himalaya por encima de los seis mil metros hasta las fosas abisales oceánicas a más de cuatro mil metros de profundidad.",
                    "tituloVisual": "PASO LENTO (TARDIGRADA)",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "laboratorio",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["Lazzaro Spallanzani", "tardígrados", "medio milímetro", "cumbres del Himalaya"],
                    "poseId": "holding_presentation_board",
                    "expresion": "talking",
                    "infografia": {
                        "tipo": "dato_clave",
                        "titulo": "Distribución Planetaria",
                        "subtitulo": "Rango de Hábitat de los Tardígrados",
                        "valorPrincipal": "0.5 mm",
                        "unidad": "tamaño promedio",
                        "items": [
                            {"etiqueta": "Altitud máxima", "valor": "+6.000 m (Himalaya)", "porcentaje": 100, "color": "#38BDF8"},
                            {"etiqueta": "Profundidad máxima", "valor": "-4.000 m (Fosas marinas)", "porcentaje": 80, "color": "#FFE600"}
                        ],
                        "colorAcento": "#FFE600"
                    }
                }
            ]
        },
        {
            "id": "cap_2",
            "numero": 2,
            "titulo": "La Magia de la Criptobiosis",
            "resumen": "Cómo transformarse en un barril de cristal biológico.",
            "escenas": [
                {
                    "id": 3,
                    "texto": "Sin embargo, lo que eleva a los tardígrados al estatus de superorganismos indiscutibles no es su aspecto simpático, sino su respuesta ante el peligro ambiental extremo: la criptobiosis. Cuando el musgo en el que habitan se seca por completo bajo el sol abrasador, en lugar de morir por deshidratación como cualquier otro animal, el tardígrado repliega sus ocho patas hacia adentro, enrolla su cuerpo cilíndrico en forma de pequeña píldora llamada tonel o barril y expulsa más del noventa y siete por ciento del agua de sus tejidos.",
                    "tituloVisual": "EL ESTADO DE TONEL",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "laboratorio",
                    "transicion": "zoom_in",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["criptobiosis", "deshidratación extrema", "estado de tonel", "noventa y siete por ciento"],
                    "poseId": "thinking_chin_hand",
                    "expresion": "eureka"
                },
                {
                    "id": 4,
                    "texto": "En ese estado de animación suspendida, su metabolismo celular se ralentiza hasta una diezmilésima parte de su actividad normal, una cifra prácticamente indistinguible de la muerte biológica. Para evitar que sus estructuras celulares y su ADN colapsen sin agua, el tardígrado sintetiza unas proteínas exclusivas llamadas proteínas intrínsecamente desordenadas de tardígrado. Estas moléculas forman un gel biológico que se solidifica en un escudo de vidrio molecular, vitrificando el interior de la célula sin romper sus membranas.",
                    "tituloVisual": "VITRIFICACION CELULAR",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "laboratorio",
                    "transicion": "whip_left",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["animación suspendida", "diezmilésima parte", "vidrio molecular", "vitrificación"],
                    "poseId": "explaining_pointing_up",
                    "expresion": "analytical",
                    "infografia": {
                        "tipo": "comparacion",
                        "titulo": "Metabolismo en Criptobiosis",
                        "subtitulo": "Actividad Vital Activa vs Estado Tonel",
                        "valorPrincipal": "0.01%",
                        "unidad": "del metabolismo basal",
                        "items": [
                            {"etiqueta": "Estado activo", "valor": "100% de agua y funciones", "porcentaje": 100, "color": "#38BDF8"},
                            {"etiqueta": "Estado tonel (desecado)", "valor": "< 3% agua, vitrificado", "porcentaje": 3, "color": "#FFE600"}
                        ],
                        "colorAcento": "#FFE600"
                    }
                }
            ]
        },
        {
            "id": "cap_3",
            "numero": 3,
            "titulo": "Torturas de Laboratorio que Dejan en Vergüenza a la Física",
            "resumen": "Resistencia a temperaturas cercanas al cero absoluto y presiones descomunales.",
            "escenas": [
                {
                    "id": 5,
                    "texto": "Durante décadas, científicos de todo el mundo han sometido a tardígrados en estado de criptobiosis a pruebas de resistencia física que pulverizarían a cualquier otra forma de vida en la Tierra. Fueron sumergidos en helio líquido a doscientos setenta y dos grados bajo cero, a apenas un grado por encima del cero absoluto, y al calentarse y recibir agua revivieron sin daños. También fueron calentados a ciento cincuenta grados centígrados, muy por encima del punto de ebullición del agua, sobreviviendo indemnes.",
                    "tituloVisual": "-272°C A +150°C",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "laboratorio",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["helio líquido", "doscientos setenta y dos bajo cero", "ciento cincuenta grados", "cero absoluto"],
                    "poseId": "standing_curious",
                    "expresion": "shocked"
                },
                {
                    "id": 6,
                    "texto": "En experimentos de presión hidrostática, los osos de agua soportaron presiones de hasta seis mil atmósferas: seis veces la presión que reina en el fondo de la Fosa de las Marianas. A esa presión salvaje, los enlaces químicos ordinarios y las membranas de las bacterias se desintegran por compresión mecánica, pero los tardígrados permanecieron intactos gracias a la rigidez de su matriz vítrea celular.",
                    "tituloVisual": "6000 ATMOSFERAS",
                    "layout": "split_screen",
                    "composicionVisual": "plano_medio",
                    "escenario": "abismo_oceanico",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["presión hidrostática", "seis mil atmósferas", "Fosa de las Marianas", "matriz vítrea"],
                    "poseId": "explaining_both_hands",
                    "expresion": "talking"
                }
            ]
        },
        {
            "id": "cap_4",
            "numero": 4,
            "titulo": "El Paseo Espacial en el Vacío Cósmico",
            "resumen": "La misión TARDIS de la ESA en 2007 en el exterior de un satélite.",
            "escenas": [
                {
                    "id": 7,
                    "texto": "En septiembre de dos mil siete, la Agencia Espacial Europea llevó la prueba al extremo definitivo con la misión espacial FOTON-M3 y el experimento TARDIS. Miles de tardígrados desecados fueron colocados en una bandeja en el exterior de un satélite y expuestos directamente al vacío implacable del espacio exterior durante diez días seguidos, sin atmósfera, sin presión y bombardeados por radiación solar ultravioleta sin filtro.",
                    "tituloVisual": "MISION TARDIS (2007)",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "espacio_profundo",
                    "transicion": "zoom_in",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_sci_fi_beep.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["FOTON-M3", "experimento TARDIS", "diez días en el vacío", "radiación ultravioleta"],
                    "poseId": "astronomy_telescope",
                    "expresion": "eureka"
                },
                {
                    "id": 8,
                    "texto": "Al regresar a la Tierra y ser rehidratados con agua de manantial, la mayoría de los ejemplares despertaron como si nada hubiera pasado, comenzaron a caminar y produjeron descendencia sana y fértil. Se convirtieron en los primeros animales multicelulares de la historia conocidos capaces de sobrevivir a la exposición directa y prolongada al vacío y a la radiación cósmica del espacio exterior sin traje protector alguno.",
                    "tituloVisual": "SOBREVIVIENTES DEL COSMOS",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "laboratorio",
                    "transicion": "whip_left",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["rehidratados con agua", "descendencia sana", "primeros animales multicelulares", "radiación cósmica"],
                    "poseId": "explaining_pointing_up",
                    "expresion": "smile_wide",
                    "infografia": {
                        "tipo": "dato_clave",
                        "titulo": "Radiación Espacial",
                        "subtitulo": "Dosis Letal Humana vs Tardígrado",
                        "valorPrincipal": "5.000 Gy",
                        "unidad": "Dosis tolerable",
                        "items": [
                            {"etiqueta": "Dosis mortal humana", "valor": "5 a 10 Grays", "porcentaje": 1, "color": "#EF4444"},
                            {"etiqueta": "Tolerancia tardígrado", "valor": "Hasta 5.000 Grays", "porcentaje": 100, "color": "#FFE600"}
                        ],
                        "colorAcento": "#FFE600"
                    }
                }
            ]
        },
        {
            "id": "cap_5",
            "numero": 5,
            "titulo": "El Escudo Genético Dsup",
            "resumen": "La proteína que suprime el daño al ADN ante la radiación atómica.",
            "escenas": [
                {
                    "id": 9,
                    "texto": "En dos mil dieciséis, un equipo de genetistas de la Universidad de Tokio descubrió el secreto molecular de su resistencia atómica: una proteína única bautizada como Dsup, abreviatura de Damage Suppressor. Esta proteína se adhiere físicamente a la doble hélice del ADN como una vaina protectora y desvía la energía de los radicales libres generados por la radiación ionizante, evitando que los cromosomas se fragmenten.",
                    "tituloVisual": "PROTEINA DSUP",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "laboratorio",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["Universidad de Tokio", "Damage Suppressor", "doble hélice", "radicales libres"],
                    "poseId": "holding_presentation_board",
                    "expresion": "analytical"
                },
                {
                    "id": 10,
                    "texto": "En un experimento de laboratorio asombroso, los científicos introdujeron el gen de la proteína Dsup en cultivos de células humanas vivas y las expusieron a dosis letales de rayos X: las células humanas protegidas con el gen de tardígrado mostraron una reducción de más del cuarenta por ciento en el daño al ADN. Este hallazgo abre la puerta a futuras terapias para proteger a astronautas en viajes a Marte o mejorar la radioterapia contra el cáncer.",
                    "tituloVisual": "APLICACION MEDICA",
                    "layout": "split_screen",
                    "composicionVisual": "plano_medio",
                    "escenario": "laboratorio",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_sci_fi_beep.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["células humanas vivas", "cuarenta por ciento de reducción", "viajes a Marte", "radioterapia"],
                    "poseId": "explaining_both_hands",
                    "expresion": "eureka"
                }
            ]
        },
        {
            "id": "cap_6",
            "numero": 6,
            "titulo": "Los Herederos de la Tierra",
            "resumen": "Los seres que sobrevivirán al fin del mundo cuando el Sol se apague.",
            "escenas": [
                {
                    "id": 11,
                    "texto": "Un estudio astrofísico conjunto de las universidades de Oxford y Harvard calculó la probabilidad de que cataclismos cósmicos —como el impacto de un asteroide gigante, la explosión de una supernova cercana o un estallido de rayos gamma— esterilicen por completo la vida en la Tierra. La conclusión fue categórica: mientras el impacto de un asteroide de diez kilómetros extinguió a los dinosaurios en minutos, ningún evento cósmico concebible, salvo la ebullición completa de todos los océanos del planeta, tiene la capacidad de exterminar a los tardígrados.",
                    "tituloVisual": "A PRUEBA DE APOCALIPSIS",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "espacio_profundo",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["Oxford y Harvard", "cataclismos cósmicos", "supernova cercana", "ebullición de los océanos"],
                    "poseId": "thinking_chin_hand",
                    "expresion": "talking"
                },
                {
                    "id": 12,
                    "texto": "Cuando la humanidad sea solo un recuerdo fósil en los estratos geológicos y las civilizaciones del futuro hayan desaparecido, los osos de agua seguirán caminando pacientemente entre los musgos húmedos de las rocas. Son los verdaderos dueños de nuestro planeta, los supervivientes absolutos que nos demuestran que la vida, en sus formas más diminutas e ignoradas, posee una resistencia invencible capaz de desafiar al mismísimo universo.",
                    "tituloVisual": "LOS VERDADEROS AMOS",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "cielo_dia",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["recuerdo fósil", "estratos geológicos", "resistencia invencible", "supervivientes absolutos"],
                    "poseId": "explaining_both_hands",
                    "expresion": "smile_wide"
                }
            ]
        }
    ]
    actualizar_guion("012", capitulos)


def construir_doc_013():
    capitulos = [
        {
            "id": "cap_1",
            "numero": 1,
            "titulo": "El Cirujano sin Morfina en Anzio",
            "resumen": "Henry Beecher en 1944 y el nacimiento accidental del placebo moderno.",
            "escenas": [
                {
                    "id": 1,
                    "texto": "Durante la Segunda Guerra Mundial, en el sangriento desembarco aliado de Anzio en mil novecientos cuarenta y cuatro, el médico anestesiólogo estadounidense Henry Beecher se enfrentaba a una pesadilla médica: las camillas desbordaban de soldados gravemente heridos con fracturas expuestas y miembros amputados, y las reservas de morfina para calmar los dolores agónicos se habían agotado por completo. En medio de la desesperación, una enfermera militar decidió tomar una jeringa, llenarla con agua salina esterilizada e inyectársela a un soldado desgarrado, asegurándole solemnemente que se trataba de una potente dosis de morfina pura.",
                    "tituloVisual": "ANZIO, 1944",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "habitacion_noche",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["Segunda Guerra Mundial", "Henry Beecher", "desembarco de Anzio", "agua salina"],
                    "poseId": "reading_clipboard",
                    "expresion": "shocked"
                },
                {
                    "id": 2,
                    "texto": "Para estupefacción de Beecher, el milagro ocurrió: el soldado se calmó en cuestión de segundos, su respiración agitada se normalizó, el dolor desapareció de su rostro y pudo ser operado sin caer en shock quirúrgico. Aquella jeringa sin fármaco activo salvó docenas de vidas en el frente. Al regresar a los Estados Unidos, Beecher publicó en mil novecientos cincuenta y cinco un célebre artículo titulado The Powerful Placebo, dando inicio al estudio científico riguroso de una de las capacidades más enigmáticas del cerebro humano.",
                    "tituloVisual": "THE POWERFUL PLACEBO",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "laboratorio",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["shock quirúrgico", "The Powerful Placebo", "mil novecientos cincuenta y cinco", "dolor desaparecido"],
                    "poseId": "explaining_pointing_up",
                    "expresion": "eureka",
                    "infografia": {
                        "tipo": "dato_clave",
                        "titulo": "Eficacia Documentada",
                        "subtitulo": "Respuesta al Placebo de Beecher (1955)",
                        "valorPrincipal": "35%",
                        "unidad": "de pacientes con alivio real",
                        "items": [
                            {"etiqueta": "Alivio clínico significativo", "valor": "35% en 15 estudios", "porcentaje": 35, "color": "#FFE600"},
                            {"etiqueta": "Principio farmacológico activo", "valor": "0% (Agua con sal / azúcar)", "porcentaje": 0, "color": "#38BDF8"}
                        ],
                        "colorAcento": "#FFE600"
                    }
                }
            ]
        },
        {
            "id": "cap_2",
            "numero": 2,
            "titulo": "No es Sugestión Psicológica: Es Neuroquímica Pura",
            "resumen": "La producción real de endorfinas y dopamina demostrada con naloxona.",
            "escenas": [
                {
                    "id": 3,
                    "texto": "Durante décadas se consideró despectivamente que el efecto placebo era una simple debilidad psicológica de pacientes crédulos o imaginativos. Pero en mil novecientos setenta y ocho, un experimento histórico dirigido por Jon Levine en la Universidad de California demostró que el placebo es un proceso biológico real y medible. Levine administró un placebo analgésico a pacientes tras una extracción dental dolorosa, logrando un alivio notable del dolor.",
                    "tituloVisual": "EXPERIMENTO DE LEVINE",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "laboratorio",
                    "transicion": "zoom_in",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["Jon Levine", "Universidad de California", "proceso biológico real", "extracción dental"],
                    "poseId": "walking_confidently",
                    "expresion": "analytical"
                },
                {
                    "id": 4,
                    "texto": "Inmediatamente después, inyectó secretamente a los pacientes naloxona, un fármaco bloqueador que anula la acción de los opiáceos en el cerebro. Al entrar la naloxona en el torrente sanguíneo, el dolor regresó de golpe con toda su violencia. Esto demostró que cuando una persona cree firmemente que está recibiendo un analgésico, el cerebro no finge el alivio: abre sus propias compuertas neuroquímicas y sintetiza endorfinas y encefalinas reales, su propia morfina endógena.",
                    "tituloVisual": "BLOQUEO CON NALOXONA",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "laboratorio",
                    "transicion": "whip_left",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["naloxona", "bloqueador de opiáceos", "endorfinas y encefalinas", "morfina endógena"],
                    "poseId": "explaining_both_hands",
                    "expresion": "eureka",
                    "infografia": {
                        "tipo": "tarjeta_concepto",
                        "titulo": "Prueba Farmacológica",
                        "subtitulo": "El Experimento de la Naloxona",
                        "valorPrincipal": "Endorfinas",
                        "unidad": "reales en sangre",
                        "items": [
                            {"etiqueta": "Inyección Salina", "valor": "Cerebro secreta endorfinas", "porcentaje": 100, "color": "#38BDF8"},
                            {"etiqueta": "+ Naloxona", "valor": "Bloquea endorfinas (Regresa el dolor)", "porcentaje": 0, "color": "#EF4444"}
                        ],
                        "colorAcento": "#EF4444"
                    }
                }
            ]
        },
        {
            "id": "cap_3",
            "numero": 3,
            "titulo": "La Psicología del Color, el Precio y la Forma",
            "resumen": "Por qué las pastillas rojas, caras o inyectadas curan más.",
            "escenas": [
                {
                    "id": 5,
                    "texto": "El poder del placebo está íntimamente ligado a la puesta en escena y las expectativas inconscientes del paciente. Numerosos ensayos clínicos han demostrado que el color de una pastilla de azúcar modifica su efecto fisiológico: las píldoras de color rojo o amarillo funcionan mucho mejor como estimulantes o antidepresivos, mientras que las píldoras azules o verdes son dos veces más efectivas como sedantes y relajantes musculares.",
                    "tituloVisual": "EL COLOR DE LA CURA",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "laboratorio",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["expectativas inconscientes", "color de la pastilla", "sedantes azules", "estimulantes rojos"],
                    "poseId": "thinking_chin_hand",
                    "expresion": "talking"
                },
                {
                    "id": 6,
                    "texto": "Y la jerarquía no se detiene allí: dos pastillas de azúcar funcionan mejor que una sola; una cápsula grande es más potente que una pequeña; una inyección salina falsa supera ampliamente a una pastilla; y el simulacro de una cirugía compleja bajo anestesia supera a todo lo anterior. Incluso el precio influye: un placebo comercializado a dos dólares y medio calma el dolor significativamente más que la misma pastilla idéntica etiquetada con un descuento de diez centavos.",
                    "tituloVisual": "JERARQUIA DE LA EXPECTATIVA",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "laboratorio",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["inyección falsa", "cirugía simulada", "precio comercial", "diez centavos"],
                    "poseId": "explaining_pointing_up",
                    "expresion": "shocked",
                    "infografia": {
                        "tipo": "grafico_barras",
                        "titulo": "Potencia del Ritual",
                        "subtitulo": "Eficacia según Método de Administración",
                        "valorPrincipal": "Ritual",
                        "unidad": "Impacto mental",
                        "items": [
                            {"etiqueta": "Píldora blanca simple", "valor": "Efecto basal", "porcentaje": 30, "color": "#94A3B8"},
                            {"etiqueta": "Inyección con bata médica", "valor": "Efecto elevado", "porcentaje": 70, "color": "#38BDF8"},
                            {"etiqueta": "Cirugía simulada (Sham)", "valor": "Máxima respuesta", "porcentaje": 100, "color": "#FFE600"}
                        ],
                        "colorAcento": "#FFE600"
                    }
                }
            ]
        },
        {
            "id": "cap_4",
            "numero": 4,
            "titulo": "El Gemelo Oscuro: El Efecto Nocebo",
            "resumen": "Cómo la expectativa del daño puede provocar síntomas físicos reales.",
            "escenas": [
                {
                    "id": 7,
                    "texto": "La capacidad del cerebro para alterar la fisiología tiene una vertiente oscura y peligrosa: el efecto nocebo. Si un médico o el prospecto de un medicamento advierten al paciente de posibles efectos secundarios como náuseas, migrañas o mareos, hasta un tercio de las personas que reciben una pastilla de almidón inofensiva desarrollarán esos mismos síntomas físicos con una intensidad demoledora, provocada exclusivamente por el miedo anticipatorio.",
                    "tituloVisual": "EL EFECTO NOCEBO",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "laboratorio",
                    "transicion": "zoom_in",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["efecto nocebo", "prospecto de medicamento", "miedo anticipatorio", "síntomas reales"],
                    "poseId": "confused_scratch_head",
                    "expresion": "fear"
                },
                {
                    "id": 8,
                    "texto": "En la neurobiología del nocebo, la ansiedad y la expectativa del dolor disparan la liberación masiva de una molécula llamada colecistoquinina en el sistema nervioso central, la cual amplifica las señales nerviosas de dolor que viajan hacia la médula espinal. El cerebro puede enfermar físicamente al cuerpo si está convencido de que ha sido envenenado o perjudicado.",
                    "tituloVisual": "COLECISTOQUININA",
                    "layout": "split_screen",
                    "composicionVisual": "plano_medio",
                    "escenario": "laboratorio",
                    "transicion": "whip_left",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["ansiedad patológica", "colecistoquinina", "médula espinal", "amplificación del dolor"],
                    "poseId": "thinking_chin_hand",
                    "expresion": "sad"
                }
            ]
        },
        {
            "id": "cap_5",
            "numero": 5,
            "titulo": "Placebos que Funcionan Incluso Cuando Sabes la Verdad",
            "resumen": "Los revolucionarios ensayos de Ted Kaptchuk con placebos abiertos.",
            "escenas": [
                {
                    "id": 9,
                    "texto": "Uno de los hallazgos más asombrosos del siglo veintiuno fue descubierto por el investigador Ted Kaptchuk de la Escuela de Medicina de Harvard: los llamados placebos de etiqueta abierta. Durante décadas se pensó que para que el placebo funcionara era indispensable engañar al paciente haciéndole creer que recibía un medicamento real. Kaptchuk decidió probar lo impensable: administró frascos de pastillas a pacientes con colon irritable que decían claramente en la etiqueta píldoras placebo de azúcar sin principio activo.",
                    "tituloVisual": "PLACEBO DE ETIQUETA ABIERTA",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "laboratorio",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_sci_fi_beep.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["Ted Kaptchuk", "Harvard", "placebo de etiqueta abierta", "sin engaño"],
                    "poseId": "standing_curious",
                    "expresion": "talking"
                },
                {
                    "id": 10,
                    "texto": "Contra toda lógica intuitiva, los pacientes que tomaron las pastillas sabiendo perfectamente que eran de azúcar experimentaron una mejoría clínica casi idéntica a los que recibieron fármacos tradicionales. El simple ritual de levantarse por la mañana, tomar un vaso de agua e ingerir una pastilla con la atención atenta de un médico empático activa circuitos biológicos de curación condicionados a lo largo de toda nuestra vida.",
                    "tituloVisual": "EL RITUAL CURATIVO",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "laboratorio",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["ritual curativo", "condicionamiento pavloviano", "médico empático", "colon irritable"],
                    "poseId": "explaining_both_hands",
                    "expresion": "eureka",
                    "infografia": {
                        "tipo": "dato_clave",
                        "titulo": "Ensayo de Harvard (Kaptchuk)",
                        "subtitulo": "Mejora con Placebo Conocido",
                        "valorPrincipal": "59%",
                        "unidad": "de mejoría clínica",
                        "items": [
                            {"etiqueta": "Placebo con engaño", "valor": "62% de mejoría", "porcentaje": 100, "color": "#38BDF8"},
                            {"etiqueta": "Placebo honesto (Declarado)", "valor": "59% de mejoría", "porcentaje": 95, "color": "#FFE600"}
                        ],
                        "colorAcento": "#FFE600"
                    }
                }
            ]
        },
        {
            "id": "cap_6",
            "numero": 6,
            "titulo": "Los Límites de la Mente y la Farmacia Interior",
            "resumen": "La diferencia entre modular síntomas y curar patologías infecciosas.",
            "escenas": [
                {
                    "id": 11,
                    "texto": "Es fundamental trazar una frontera médica estricta: el efecto placebo es formidable para modular el dolor, la fatiga, la depresión, la ansiedad o las náuseas, porque todos estos síntomas son regulados directamente por el sistema nervioso central. Pero un placebo jamás reducirá el tamaño de un tumor maligno ni eliminará una bacteria virulenta de la sangre sin antibióticos reales. No reemplaza a la medicina científica; es el copiloto biológico de la curación.",
                    "tituloVisual": "LIMITES MEDICOS",
                    "layout": "split_screen",
                    "composicionVisual": "plano_medio",
                    "escenario": "laboratorio",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["frontera médica", "síntomas subjetivos", "tumores y bacterias", "copiloto biológico"],
                    "poseId": "thinking_chin_hand",
                    "expresion": "analytical"
                },
                {
                    "id": 12,
                    "texto": "El efecto placebo nos demuestra que el cuerpo humano no es una máquina mecánica aislada de la mente, sino una farmacia interior extraordinariamente compleja donde la esperanza, la empatía y la confianza tienen una firma molecular tangible. Cuando creemos en nuestra propia recuperación, desatamos una química ancestral que lleva millones de años esperando la señal para comenzar a sanar.",
                    "tituloVisual": "LA FARMACIA INTERIOR",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "laboratorio",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["farmacia interior", "firma molecular tangible", "química ancestral", "confianza y salud"],
                    "poseId": "explaining_both_hands",
                    "expresion": "smile_wide"
                }
            ]
        }
    ]
    actualizar_guion("013", capitulos)


def construir_doc_014():
    capitulos = [
        {
            "id": "cap_1",
            "numero": 1,
            "titulo": "La Tierra Púrpura y el Mar de Hierro",
            "resumen": "La atmósfera primordial anóxica y los océanos verdes ricos en hierro.",
            "escenas": [
                {
                    "id": 1,
                    "texto": "Hoy respiramos el aire sin pensarlo dos veces, dando por sentado que el oxígeno es el aliento vital indispensable para cualquier criatura del planeta. Pero hace dos mil cuatrocientos millones de años, en la era geológica del Paleoproterozoico, la Tierra era un mundo alienígena donde un humano moriría asfixiado en segundos: no había ni una sola molécula de oxígeno libre en la atmósfera. El cielo no era azul sino de un tono anaranjado pálido debido a densas concentraciones de metano, y los océanos eran de un verde turbio saturados de hierro ferroso disuelto.",
                    "tituloVisual": "LA TIERRA DE HACE 2400M",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "abismo_oceanico",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["dos mil cuatrocientos millones", "Paleoproterozoico", "metano atmosférico", "océanos de hierro verde"],
                    "poseId": "walking_confidently",
                    "expresion": "analytical"
                },
                {
                    "id": 2,
                    "texto": "Los dueños absolutos de este planeta primordial eran microorganismos anaeróbicos: arqueas y bacterias primitivas para las cuales el oxígeno elemental no era un nutriente vital, sino un gas corrosivo y altamente tóxico que destruía sus membranas celulares y quemaba sus proteínas. La vida prosperaba en la oscuridad y el silencio de un equilibrio químico que parecía destinado a durar por siempre.",
                    "tituloVisual": "REINADO ANAEROBICO",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "laboratorio",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["microorganismos anaeróbicos", "arqueas primitivas", "oxígeno como veneno", "equilibrio primordial"],
                    "poseId": "holding_presentation_board",
                    "expresion": "talking",
                    "infografia": {
                        "tipo": "dato_clave",
                        "titulo": "Atmósfera Primordial",
                        "subtitulo": "Concentración de Oxígeno Libre (O₂)",
                        "valorPrincipal": "0.001%",
                        "unidad": "anóxico total",
                        "items": [
                            {"etiqueta": "Oxígeno Arcaico", "valor": "< 0.001% (Trazas insignificantes)", "porcentaje": 1, "color": "#EF4444"},
                            {"etiqueta": "Oxígeno Actual", "valor": "21% (Sustento vital)", "porcentaje": 100, "color": "#38BDF8"}
                        ],
                        "colorAcento": "#38BDF8"
                    }
                }
            ]
        },
        {
            "id": "cap_2",
            "numero": 2,
            "titulo": "La Invención del Veneno Fotosintético",
            "resumen": "Las cianobacterias y el milagro bioenergético de romper la molécula de agua.",
            "escenas": [
                {
                    "id": 3,
                    "texto": "Todo cambió cuando un grupo diminuto de bacterias marinas dio con la mayor revolución bioquímica de la historia de la vida: la fotosíntesis oxigénica. Desarrollaron un complejo molecular capaz de hacer algo energéticamente sobrehumano: capturar la luz solar para romper las fortísimas uniones de las moléculas de agua, extrayendo átomos de hidrógeno para sintetizar azúcares y liberando el oxígeno sobrante al mar como un simple residuo metabólico tóxico. Eran las cianobacterias.",
                    "tituloVisual": "CIANOBACTERIAS",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "cielo_dia",
                    "transicion": "zoom_in",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["fotosíntesis oxigénica", "romper moléculas de agua", "cianobacterias", "residuo tóxico"],
                    "poseId": "explaining_pointing_up",
                    "expresion": "eureka"
                },
                {
                    "id": 4,
                    "texto": "Al principio, el veneno generado por las cianobacterias no se acumuló en el ambiente. El mar primitivo estaba repleto de hierro disuelto que actuó como una esponja química gigantesca: cada átomo de oxígeno liberado se unía de inmediato al hierro, oxidándolo y precipitándolo al fondo marino en forma de óxido férrico. Durante cientos de millones de años, este proceso acumuló colosales yacimientos de hierro bandeado que hoy son la principal fuente de acero de nuestra civilización industrial.",
                    "tituloVisual": "HIERRO BANDEADO",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "abismo_oceanico",
                    "transicion": "whip_left",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["esponja química", "óxido férrico", "hierro bandeado", "yacimientos industriales"],
                    "poseId": "thinking_chin_hand",
                    "expresion": "analytical",
                    "infografia": {
                        "tipo": "tarjeta_concepto",
                        "titulo": "Sumidero Oceánico",
                        "subtitulo": "Formaciones de Hierro Bandeado (BIF)",
                        "valorPrincipal": "Fe₂O₃",
                        "unidad": "Herrumbre Cósmica",
                        "items": [
                            {"etiqueta": "Hierro en solución", "valor": "Atrapa todo el oxígeno producido", "porcentaje": 100, "color": "#FFE600"},
                            {"etiqueta": "Oxígeno en atmósfera", "valor": "Cero (Retenido en el lecho marino)", "porcentaje": 0, "color": "#38BDF8"}
                        ],
                        "colorAcento": "#FFE600"
                    }
                }
            ]
        },
        {
            "id": "cap_3",
            "numero": 3,
            "titulo": "La Saturación y el Holocausto Químico",
            "resumen": "Cuando el hierro se agotó y el oxígeno envenenó los mares y el aire.",
            "escenas": [
                {
                    "id": 5,
                    "texto": "Pero llegó un momento en que el hierro de los océanos se agotó por completo. La esponja mineral se saturó y ya no pudo absorber ni una molécula más. Sin sumideros químicos donde ocultarse, el oxígeno libre comenzó a acumularse a borbotones en el agua del mar y a desbordarse hacia la atmósfera terrestre. Lo que para las cianobacterias era un subproducto de desecho se convirtió en el mayor holocausto químico de la historia planetaria.",
                    "tituloVisual": "LA SATURACION TOTAL",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "abismo_oceanico",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["esponja saturada", "oxígeno libre desbordado", "holocausto químico", "cataclismo ecológico"],
                    "poseId": "confused_scratch_head",
                    "expresion": "shocked"
                },
                {
                    "id": 6,
                    "texto": "Para los billones de organismos anaeróbicos que poblaban la Tierra, el oxígeno era un agente corrosivo letal: arrancaba electrones de sus estructuras celulares y oxidaba violentamente sus enzimas. El noventa y nueve por ciento de todas las especies vivas del planeta perecieron en una extinción masiva silenciosa. Solo sobrevivieron aquellas arqueas que huyeron hacia el lodo profundo sin oxígeno o los respiraderos hidrotermales del abismo oceánico.",
                    "tituloVisual": "EXTINCION DEL 99%",
                    "layout": "split_screen",
                    "composicionVisual": "plano_medio",
                    "escenario": "red_subterranea",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_impact.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["noventa y nueve por ciento", "extinción masiva", "respiraderos hidrotermales", "arqueas sobrevivientes"],
                    "poseId": "explaining_both_hands",
                    "expresion": "sad"
                }
            ]
        },
        {
            "id": "cap_4",
            "numero": 4,
            "titulo": "La Tierra Bola de Nieve Huroriana",
            "resumen": "La destrucción del efecto invernadero de metano y la mayor glaciación de la historia.",
            "escenas": [
                {
                    "id": 7,
                    "texto": "El cataclismo biológico desató de inmediato una catástrofe climática aún más aterradora. El clima cálido de la Tierra primitiva dependía del gas metano atmosférico, un gas de efecto invernadero treinta veces más potente que el dióxido de carbono. Cuando el oxígeno inundó la atmósfera superior, reaccionó químicamente con el metano, transformándolo en agua y dióxido de carbono y destruyendo la manta térmica que mantenía templado al planeta.",
                    "tituloVisual": "COLAPSO DEL METANO",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "cielo_dia",
                    "transicion": "zoom_in",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["gas metano", "efecto invernadero", "manta térmica destruida", "catástrofe climática"],
                    "poseId": "thinking_chin_hand",
                    "expresion": "analytical"
                },
                {
                    "id": 8,
                    "texto": "Sin el metano, las temperaturas globales cayeron en picado hacia los cincuenta grados bajo cero. Los casquetes polares avanzaron hacia el ecuador reflejando la radiación solar y sumieron al planeta en la glaciación Huroniana: trescientos millones de años durante los cuales la Tierra entera se convirtió en una gigantesca bola de nieve sólida cubierta por capas de hielo de más de un kilómetro de espesor de polo a polo.",
                    "tituloVisual": "TIERRA BOLA DE NIEVE",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "lunar",
                    "transicion": "whip_left",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["glaciación Huroniana", "cincuenta grados bajo cero", "trescientos millones de años", "bola de nieve"],
                    "poseId": "explaining_pointing_up",
                    "expresion": "shocked",
                    "infografia": {
                        "tipo": "dato_clave",
                        "titulo": "Glaciación Huroniana",
                        "subtitulo": "La Mayor Era de Hielo del Planeta",
                        "valorPrincipal": "300M",
                        "unidad": "años bajo el hielo",
                        "items": [
                            {"etiqueta": "Temperatura media global", "valor": "-50°C (Congelación total)", "porcentaje": 100, "color": "#38BDF8"},
                            {"etiqueta": "Grosor del hielo ecuatorial", "valor": "> 1.000 metros de espesor", "porcentaje": 80, "color": "#FFE600"}
                        ],
                        "colorAcento": "#38BDF8"
                    }
                }
            ]
        },
        {
            "id": "cap_5",
            "numero": 5,
            "titulo": "El Caparazón de Ozono y el Motor Mitocondrial",
            "resumen": "La creación de la capa de ozono y el salto evolutivo a la respiración aeróbica.",
            "escenas": [
                {
                    "id": 9,
                    "texto": "Tras millones de años de vulcanismo que perforó el hielo acumulando dióxido de carbono en la atmósfera, el planeta finalmente se descongeló, y el oxígeno reveló su auténtico milagro evolutivo. En la estratosfera, la radiación solar dividió las moléculas de oxígeno creando la capa de ozono, un escudo invisible que por primera vez bloqueó los letales rayos ultravioleta del Sol, permitiendo que la vida pudiera algún día abandonar el agua y colonizar la tierra firme.",
                    "tituloVisual": "NACE LA CAPA DE OZONO",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "cielo_dia",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_sci_fi_beep.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["capa de ozono", "rayos ultravioleta", "tierra firme", "descongelamiento volcánico"],
                    "poseId": "standing_curious",
                    "expresion": "eureka"
                },
                {
                    "id": 10,
                    "texto": "Y en el interior de las células ocurrió un salto gigantesco: las células que aprendieron a utilizar el oxígeno para quemar nutrientes obtuvieron una recompensa energética astronómica: la respiración aeróbica produce dieciocho veces más energía por molécula de glucosa que la fermentación anaeróbica. Esta inmensa batería metabólica impulsó la aparición de las mitocondrias, la célula eucariota y, en última instancia, toda la vida multicelular compleja.",
                    "tituloVisual": "18 VECES MAS ENERGIA",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "laboratorio",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["respiración aeróbica", "dieciocho veces más energía", "mitocondrias", "célula eucariota"],
                    "poseId": "explaining_both_hands",
                    "expresion": "talking",
                    "infografia": {
                        "tipo": "comparacion",
                        "titulo": "Eficiencia Metabólica",
                        "subtitulo": "Fermentación Anaeróbica vs Respiración con Oxígeno",
                        "valorPrincipal": "36 ATP",
                        "unidad": "vs 2 ATP por glucosa",
                        "items": [
                            {"etiqueta": "Respiración con O₂ (Aeróbica)", "valor": "36 ATP (18x más energía)", "porcentaje": 100, "color": "#FFE600"},
                            {"etiqueta": "Fermentación sin O₂ (Anaeróbica)", "valor": "2 ATP (Energía mínima)", "porcentaje": 5, "color": "#94A3B8"}
                        ],
                        "colorAcento": "#FFE600"
                    }
                }
            ]
        },
        {
            "id": "cap_6",
            "numero": 6,
            "titulo": "El Veneno que nos Regala la Vida",
            "resumen": "La paradoja final del oxígeno como motor de la existencia y el envejecimiento.",
            "escenas": [
                {
                    "id": 11,
                    "texto": "La Gran Oxidación nos recuerda la paradoja suprema de la biología terrestre: el mismo gas que envenenó al noventa y nueve por ciento de los habitantes arcaicos de la Tierra es el combustible indispensable que hoy bombea tu corazón y alimenta tus pensamientos en este preciso milisegundo. Sin aquel cataclismo primordial perpetrado por humildes bacterias acuáticas, los animales, las plantas y los seres humanos jamás habríamos existido.",
                    "tituloVisual": "EL COMBUSTIBLE DE LA MENTE",
                    "layout": "split_screen",
                    "composicionVisual": "plano_medio",
                    "escenario": "laboratorio",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["paradoja suprema", "combustible biológico", "bacterias acuáticas", "pensamiento humano"],
                    "poseId": "thinking_chin_hand",
                    "expresion": "analytical"
                },
                {
                    "id": 12,
                    "texto": "Incluso hoy, el oxígeno sigue siendo una llama de doble filo: nos da la energía para vivir, pero sus radicales libres oxidan lentamente nuestras células en el proceso inevitable del envejecimiento. Cada bocanada de aire fresco es un tributo a la catástrofe que reinventó el planeta: un recordatorio de que en la historia de la vida, los mayores desastres ecológicos son a menudo la cuna de los milagros más asombrosos.",
                    "tituloVisual": "LA LLAMA DE DOBLE FILO",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "cielo_dia",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["llama de doble filo", "envejecimiento celular", "tributo a la catástrofe", "cuna de milagros"],
                    "poseId": "explaining_both_hands",
                    "expresion": "smile_wide"
                }
            ]
        }
    ]
    actualizar_guion("014", capitulos)


def construir_doc_015():
    capitulos = [
        {
            "id": "cap_1",
            "numero": 1,
            "titulo": "La Anomalía del Uranio en Pierrelatte",
            "resumen": "Mayo de 1972 y el misterio del uranio empobrecido en Francia.",
            "escenas": [
                {
                    "id": 1,
                    "texto": "En mayo de mil novecientos setenta y dos, en la planta de enriquecimiento de combustible nuclear de Pierrelatte en Francia, un analista de laboratorio realizaba una espectrometría de masas rutinaria sobre una muestra de mineral de uranio cuando se topó con un resultado que desató todas las alarmas de seguridad atómica internacional. En cualquier roca de la corteza terrestre, en la Luna y en los meteoritos que caen del espacio, el isótopo fisionable uranio doscientos treinta y cinco existe siempre en una proporción fija y universal: exactamente el cero punto setecientos veinte por ciento.",
                    "tituloVisual": "PIERRELATTE, MAYO DE 1972",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "laboratorio",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["Pierrelatte", "espectrometría de masas", "uranio doscientos treinta y cinco", "cero punto setecientos veinte"],
                    "poseId": "reading_clipboard",
                    "expresion": "shocked"
                },
                {
                    "id": 2,
                    "texto": "Sin embargo, el cargamento examinado en Pierrelatte, procedente de la mina a cielo abierto de Oklo en la república africana de Gabón, mostraba una cifra anómala e inexplicable: apenas un cero punto setecientos diecisiete por ciento, y en algunas capas posteriores caía a un alarmante cero punto cuatro por ciento. Faltaban cientos de kilogramos de uranio doscientos treinta y cinco. El Comisariado de Energía Atómica francés temió de inmediato un robo de material nuclear o el desvío clandestino de combustible enriquecido para la fabricación de una bomba atómica secreta.",
                    "tituloVisual": "FALTAN 200 KILOS DE U-235",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "laboratorio",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["mina de Oklo", "Gabón", "bomba atómica secreta", "cero punto setecientos diecisiete"],
                    "poseId": "explaining_pointing_up",
                    "expresion": "analytical",
                    "infografia": {
                        "tipo": "comparacion",
                        "titulo": "Anomalía Isotópica U-235",
                        "subtitulo": "Concentración Natural vs Oklo",
                        "valorPrincipal": "0.720%",
                        "unidad": "estándar universal",
                        "items": [
                            {"etiqueta": "Estándar terrestre y cósmico", "valor": "0.7202% constante", "porcentaje": 100, "color": "#38BDF8"},
                            {"etiqueta": "Mina de Oklo (Gabón)", "valor": "0.7171% (Agotado)", "porcentaje": 99.5, "color": "#FFE600"},
                            {"etiqueta": "Núcleos del reactor", "valor": "Hasta 0.440% (Quemado)", "porcentaje": 61, "color": "#EF4444"}
                        ],
                        "colorAcento": "#EF4444"
                    }
                }
            ]
        },
        {
            "id": "cap_2",
            "numero": 2,
            "titulo": "La Investigación Geológica en Gabón",
            "resumen": "La expedición a África y el descarte de sabotajes modernos.",
            "escenas": [
                {
                    "id": 3,
                    "texto": "Un equipo de físicos y geólogos franceses fue enviado de urgencia a las selvas de Gabón para investigar el yacimiento in situ. Rastrearon cada lote de roca y descartaron rápidamente cualquier intervención humana moderna o fraude industrial: el mineral provenía de estratos geológicos profundos que habían permanecido completamente sellados e intactos durante cientos de millones de años. La única explicación física concebible era inconcebible para la época: aquel uranio ya había sido consumido en una reacción de fisión nuclear.",
                    "tituloVisual": "EXPEDICION A OKLO",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "cielo_dia",
                    "transicion": "zoom_in",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["selvas de Gabón", "estratos sellados", "fraude descartado", "reacción de fisión nuclear"],
                    "poseId": "walking_confidently",
                    "expresion": "analytical"
                },
                {
                    "id": 4,
                    "texto": "La confirmación irrefutable llegó al analizar los subproductos de la roca: los geólogos encontraron concentraciones anómalas de isótopos de neodimio, samario, rutenio y cesio con patrones de descomposición idénticos a las cenizas radiactivas que se producen dentro de un reactor nuclear moderno. Alguien o algo había encendido una reacción en cadena de fisión nuclear en África... hace dos mil millones de años.",
                    "tituloVisual": "CENIZAS RADIACTIVAS",
                    "layout": "split_screen",
                    "composicionVisual": "plano_medio",
                    "escenario": "laboratorio",
                    "transicion": "whip_left",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["neodimio y samario", "cenizas radiactivas", "hace dos mil millones de años", "patrones de fisión"],
                    "poseId": "holding_presentation_board",
                    "expresion": "shocked"
                }
            ]
        },
        {
            "id": "cap_3",
            "numero": 3,
            "titulo": "Las Condiciones Milagrosas de hace Dos Mil Millones de Años",
            "resumen": "Por qué la física del pasado permitió lo que hoy es imposible.",
            "escenas": [
                {
                    "id": 5,
                    "texto": "¿Cómo fue posible que la naturaleza ensamblara un reactor nuclear sin ingenieros ni computadoras? La respuesta reside en el reloj de desintegración radiactiva. El isótopo fisionable uranio doscientos treinta y cinco se desintegra mucho más rápido que el uranio doscientos treinta y ocho, con una vida media de setecientos millones de años. Esto significa que hace dos mil millones de años, la abundancia natural de uranio fisionable en el planeta no era del raquítico cero punto siete por ciento actual, sino de más del tres por ciento: exactamente la misma proporción a la que hoy enriquecemos el combustible artificial en las centrales nucleares.",
                    "tituloVisual": "EL RELOJ RADIACTIVO",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "laboratorio",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["vida media", "setecientos millones de años", "tres por ciento natural", "centrales nucleares modernas"],
                    "poseId": "explaining_pointing_up",
                    "expresion": "eureka",
                    "infografia": {
                        "tipo": "dato_clave",
                        "titulo": "Enriquecimiento Natural",
                        "subtitulo": "Concentración de U-235 hace 2.000 Millones de Años",
                        "valorPrincipal": "3.1%",
                        "unidad": "enriquecimiento fósil",
                        "items": [
                            {"etiqueta": "Hace 2.000M de años", "valor": "3.1% (Grado reactor comercial)", "porcentaje": 100, "color": "#FFE600"},
                            {"etiqueta": "Hoy en día", "valor": "0.72% (Fisión natural imposible)", "porcentaje": 23, "color": "#38BDF8"}
                        ],
                        "colorAcento": "#FFE600"
                    }
                },
                {
                    "id": 6,
                    "texto": "A esto se sumó un factor geológico providencial: el drenaje de aguas subterráneas ricas en oxígeno formadas tras la Gran Oxidación arrastró y concentró masivas vetas de óxido de uranio en areniscas porosas en Oklo, creando capas de más de un metro de espesor con la masa crítica necesaria para iniciar la fisión espontánea.",
                    "tituloVisual": "LA MASA CRITICA",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "red_subterranea",
                    "transicion": "zoom_in",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["areniscas porosas", "masa crítica", "fisión espontánea", "vetas de óxido de uranio"],
                    "poseId": "thinking_chin_hand",
                    "expresion": "analytical"
                }
            ]
        },
        {
            "id": "cap_4",
            "numero": 4,
            "titulo": "El Moderador de Agua y el Ciclo de Tres Horas",
            "resumen": "El termostato natural autorregulable que evitó una explosión nuclear.",
            "escenas": [
                {
                    "id": 7,
                    "texto": "Pero para sostener una reacción nuclear controlada y evitar que el uranio estalle como una bomba o se apague de inmediato se requiere un moderador de neutrones: una sustancia que frene la velocidad de los neutrones rápidos para que puedan partir otros núcleos atómicos. En Oklo, ese moderador fue simplemente el agua de lluvia subterránea que se filtraba a través de las fracturas de la roca arenisca.",
                    "tituloVisual": "EL MODERADOR DE AGUA",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "red_subterranea",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["moderador de neutrones", "agua de lluvia subterránea", "neutrones rápidos", "reacción controlada"],
                    "poseId": "explaining_both_hands",
                    "expresion": "talking"
                },
                {
                    "id": 8,
                    "texto": "El reactor natural funcionaba con un ciclo pulsante fascinante de tres horas idéntico a un géiser: el agua fría entraba en la veta de uranio, frenaba los neutrones e iniciaba la fisión nuclear. A medida que el calor atómico elevaba la temperatura a más de cuatrocientos grados centígrados, el agua comenzaba a hervir y se evaporaba en vapor a alta presión. Sin agua líquida como moderador, los neutrones viajaban demasiado rápido y la reacción se detenía sola de forma segura. Al enfriarse el lecho mineral horas después, el agua volvía a condensarse y el ciclo arrancaba de nuevo.",
                    "tituloVisual": "CICLO GEISER DE TRES HORAS",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "laboratorio",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["ciclo pulsante de tres horas", "cuatrocientos grados", "vapor a alta presión", "termostato natural"],
                    "poseId": "explaining_pointing_up",
                    "expresion": "eureka",
                    "infografia": {
                        "tipo": "grafico_barras",
                        "titulo": "Ciclo Térmico de Oklo",
                        "subtitulo": "Pulsos de Fisión Autorregulados",
                        "valorPrincipal": "3 Horas",
                        "unidad": "periodo del ciclo",
                        "items": [
                            {"etiqueta": "Fase de Fisión Activa", "valor": "30 minutos (Agua líquida modera)", "porcentaje": 17, "color": "#FFE600"},
                            {"etiqueta": "Fase de Enfriamiento", "valor": "150 minutos (Vapor detiene fisión)", "porcentaje": 83, "color": "#38BDF8"}
                        ],
                        "colorAcento": "#FFE600"
                    }
                }
            ]
        },
        {
            "id": "cap_5",
            "numero": 5,
            "titulo": "Cien Mil Años de Energía Atómica Silenciosa",
            "resumen": "La potencia promedio de 100 kilovatios y la contención de residuos.",
            "escenas": [
                {
                    "id": 9,
                    "texto": "Los cálculos físicos demostraron que en la región de Oklo operaron al menos dieciséis reactores nucleares naturales independientes. Juntos funcionaron de forma ininterrumpida durante cientos de miles de años, produciendo una potencia térmica continua de aproximadamente cien kilovatios, suficiente para abastecer de electricidad a una docena de hogares modernos. A lo largo de su vida útil consumieron más de cinco toneladas de uranio doscientos treinta y cinco y generaron toneladas de plutonio y residuos radiactivos altamente peligrosos.",
                    "tituloVisual": "16 REACTORES NATURALES",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "red_subterranea",
                    "transicion": "zoom_in",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["dieciséis reactores", "cien kilovatios", "cinco toneladas de uranio", "cientos de miles de años"],
                    "poseId": "standing_curious",
                    "expresion": "analytical"
                },
                {
                    "id": 10,
                    "texto": "Sin embargo, lo que verdaderamente cautiva a los ingenieros nucleares contemporáneos es cómo la naturaleza resolvió el problema del almacenamiento de residuos: a lo largo de dos mil millones de años de historia geológica, los residuos radiactivos más peligrosos, como el plutonio y los actínidos, apenas se desplazaron unos pocos centímetros de su posición original, atrapados sólidamente en la estructura mineral de arcillas de fosfato sin contaminar el agua circundante.",
                    "tituloVisual": "EL ALMACEN GEOLOGICO",
                    "layout": "split_screen",
                    "composicionVisual": "plano_medio",
                    "escenario": "laboratorio",
                    "transicion": "whip_left",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_sci_fi_beep.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["residuos radiactivos", "arcillas de fosfato", "dos mil millones de años", "pocos centímetros"],
                    "poseId": "holding_presentation_board",
                    "expresion": "eureka"
                }
            ]
        },
        {
            "id": "cap_6",
            "numero": 6,
            "titulo": "La Naturaleza nos Ganó por Dos Mil Millones de Años",
            "resumen": "La humildad científica de la humanidad frente al poder del planeta.",
            "escenas": [
                {
                    "id": 11,
                    "texto": "Cuando Enrico Fermi y su equipo lograron la primera reacción nuclear en cadena controlada por la humanidad en la Universidad de Chicago en diciembre de mil novecientos cuarenta y dos, creyeron que habían inaugurado una hazaña tecnológica exclusiva de la inteligencia humana: la era atómica.",
                    "tituloVisual": "CHICAGO PILE-1 (1942)",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "laboratorio",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["Enrico Fermi", "Chicago Pile-1", "diciembre de mil novecientos cuarenta y dos", "era atómica"],
                    "poseId": "walking_confidently",
                    "expresion": "talking"
                },
                {
                    "id": 12,
                    "texto": "El reactor fósil de Oklo nos enseñó una lección monumental de humildad cósmica: la naturaleza ya había dominado la energía nuclear, el control por moderación hidrodinámica y el aislamiento geológico de residuos atómicos dos mil millones de años antes de que el primer ser humano encendiera una fogata. La Tierra no es solo nuestro hogar; es el laboratorio científico más asombroso del universo.",
                    "tituloVisual": "HUMILDAD COSMICA",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "cielo_dia",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["humildad cósmica", "laboratorio científico", "energía nuclear natural", "aislamiento geológico"],
                    "poseId": "explaining_both_hands",
                    "expresion": "smile_wide"
                }
            ]
        }
    ]
    actualizar_guion("015", capitulos)


if __name__ == "__main__":
    print("Redactando Lote 3 (012, 013, 014, 015)...")
    construir_doc_012()
    construir_doc_013()
    construir_doc_014()
    construir_doc_015()
    print("Lote 3 completado.")
