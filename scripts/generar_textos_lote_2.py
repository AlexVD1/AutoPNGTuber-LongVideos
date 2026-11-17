#!/usr/bin/env python3
"""
Lote 2: Documentales 008, 009, 010 y 011 expandidos a 6.5 - 8.0 minutos.
"""

from redactar_guiones_largos_completos import actualizar_guion


def construir_doc_008():
    capitulos = [
        {
            "id": "cap_1",
            "numero": 1,
            "titulo": "La Infección Silenciosa en la Selva",
            "resumen": "El ataque invisible de una espora sobre la hormiga carpintera.",
            "escenas": [
                {
                    "id": 1,
                    "texto": "En las profundidades del dosel selvático de Tailandia y la cuenca del Amazonas, miles de hormigas carpinteras caminan por senderos aéreos recolectando alimento para su colonia. Pero en el suelo del bosque acecha una amenaza invisible: millones de esporas microscópicas del hongo Ophiocordyceps unilateralis suspendidas en la humedad sofocante. Basta con que una sola de estas esporas minúsculas roce la pata o la cutícula de una hormiga para que se active un mecanismo letal. La espora no busca matar de inmediato a su hospedador, sino colonizarlo lentamente desde adentro en una macabra obra de ingeniería biológica.",
                    "tituloVisual": "LA ESPORA INVISIBLE",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "cielo_dia",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["Ophiocordyceps unilateralis", "hormiga carpintera", "esporas microscópicas", "cuenca del Amazonas"],
                    "poseId": "walking_confidently",
                    "expresion": "analytical"
                },
                {
                    "id": 2,
                    "texto": "Al hacer contacto, la espora secreta un cóctel de enzimas químicas que disuelven el exoesqueleto de quitina del insecto y penetra en su hemolinfa, el equivalente a la sangre en los artrópodos. Una vez en el interior, el hongo no ataca el cerebro como se creyó durante décadas: en lugar de eso, sus células proliferan exponencialmente como levaduras individuales que se comunican entre sí mediante señales químicas. El hongo comienza a tejer una red física continua que envuelve cada fibra muscular del animal, convirtiendo el cuerpo de la hormiga en una marioneta biológica controlada desde el sistema neuromuscular.",
                    "tituloVisual": "RED NEUROMUSCULAR",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "laboratorio",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["exoesqueleto de quitina", "hemolinfa", "fibras musculares", "marioneta biológica"],
                    "poseId": "holding_presentation_board",
                    "expresion": "eureka",
                    "infografia": {
                        "tipo": "dato_clave",
                        "titulo": "Colonización Muscular",
                        "subtitulo": "Invasión Tisular del Hongo",
                        "valorPrincipal": "40%",
                        "unidad": "de biomasa fúngica",
                        "items": [
                            {"etiqueta": "Cerebro de la hormiga", "valor": "Intacto (Sin invadir)", "porcentaje": 100, "color": "#38BDF8"},
                            {"etiqueta": "Músculos manipulados", "valor": "Rodeados por micelio", "porcentaje": 80, "color": "#FFE600"}
                        ],
                        "colorAcento": "#FFE600"
                    }
                }
            ]
        },
        {
            "id": "cap_2",
            "numero": 2,
            "titulo": "La Marcha de la Marioneta",
            "resumen": "La pérdida del control motriz y el abandono forzoso de la colonia.",
            "escenas": [
                {
                    "id": 3,
                    "texto": "A los pocos días de la infección, el comportamiento de la hormiga cambia drásticamente. Deja de comunicarse con sus hermanas, ignora las órdenes químicas de la reina y comienza a sufrir convulsiones musculares erráticas que la hacen tambalearse como un sonámbulo. Sus compañeras de nido, dotadas de un estricto instinto de higiene social, detectan la anomalía química y la expulsan de inmediato del hormiguero para evitar que contamine al resto de la comunidad. Desorientada y solitaria, la hormiga zombi emprende una marcha fúnebre hacia las copas bajas de la vegetación.",
                    "tituloVisual": "EXPULSION DEL NIDO",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "cielo_dia",
                    "transicion": "zoom_in",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["convulsiones erráticas", "higiene social", "marcha fúnebre", "hormiga zombi"],
                    "poseId": "thinking_chin_hand",
                    "expresion": "fear"
                },
                {
                    "id": 4,
                    "texto": "Lo más sobrecogedor revelado por el microscopio electrónico es que el cerebro de la hormiga permanece intacto y consciente durante todo el proceso. El hongo no destruye su mente; secuestra mecánicamente sus patas y mandíbulas segregando compuestos bioactivos que imitan los neurotransmisores del insecto. La hormiga es una pasajera prisionera dentro de su propio cuerpo, obligada a caminar hacia el lugar exacto que el parásito necesita para su propia reproducción.",
                    "tituloVisual": "PRISIONERA EN SU CUERPO",
                    "layout": "split_screen",
                    "composicionVisual": "plano_medio",
                    "escenario": "laboratorio",
                    "transicion": "whip_left",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["microscopio electrónico", "pasajera prisionera", "secuestro mecánico", "neurotransmisores"],
                    "poseId": "confused_scratch_head",
                    "expresion": "shocked"
                }
            ]
        },
        {
            "id": "cap_3",
            "numero": 3,
            "titulo": "El Mordisco Mortal a las Doce del Mediodía",
            "resumen": "La sincronización solar milimétrica y la mordida en el nervio de la hoja.",
            "escenas": [
                {
                    "id": 5,
                    "texto": "El nivel de precisión geométrica que alcanza la manipulación es casi sobrenatural. El hongo obliga a la hormiga a trepar a una altura de exactamente veinticinco centímetros sobre el suelo de la selva, orientada hacia el lado norte de una planta donde la humedad relativa ronda el noventa y cinco por ciento y la temperatura es de entre veinte y veintiséis grados centígrados: las condiciones climatológicas perfectas para el crecimiento fúngico. Cualquier otra altura o inclinación significaría la muerte del hongo por desecación solar.",
                    "tituloVisual": "PRECISION GEOMETRICA",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "cielo_dia",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["veinticinco centímetros", "lado norte", "noventa y cinco por ciento", "condiciones perfectas"],
                    "poseId": "explaining_pointing_up",
                    "expresion": "eureka",
                    "infografia": {
                        "tipo": "dato_clave",
                        "titulo": "Microclima Óptimo",
                        "subtitulo": "Coordenadas Fúngicas Precisas",
                        "valorPrincipal": "25 cm",
                        "unidad": "sobre el suelo",
                        "items": [
                            {"etiqueta": "Humedad requerida", "valor": "95% constante", "porcentaje": 95, "color": "#38BDF8"},
                            {"etiqueta": "Orientación solar", "valor": "Cara norte de la hoja", "porcentaje": 100, "color": "#FFE600"}
                        ],
                        "colorAcento": "#FFE600"
                    }
                },
                {
                    "id": 6,
                    "texto": "Cerca del mediodía solar, cuando la luz alcanza su pico, el hongo desencadena el acto final: emite una señal química masiva que provoca un espasmo incontrolable en los músculos mandibulares de la hormiga. Las mandíbulas se clavan con fuerza descomunal en la nervadura principal del envés de la hoja, rompiendo los tejidos vegetales en lo que los biólogos llaman el mordisco mortal. Inmediatamente después, el parásito disuelve las fibras de los músculos mandibulares, bloqueando las mandíbulas en un cerrojo químico irreversible. La hormiga queda anclada para siempre.",
                    "tituloVisual": "EL MORDISCO MORTAL",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "cielo_dia",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["mediodía solar", "nervadura principal", "mordisco mortal", "cerrojo irreversible"],
                    "poseId": "explaining_both_hands",
                    "expresion": "talking"
                }
            ]
        },
        {
            "id": "cap_4",
            "numero": 4,
            "titulo": "La Erupción del Cuerno Fúngico",
            "resumen": "La digestión interna de los órganos y el brote del estroma.",
            "escenas": [
                {
                    "id": 7,
                    "texto": "Una vez asegurado el anclaje físico, la hormiga muere en cuestión de horas. El hongo ya no necesita mantener con vida los órganos del insecto, así que procede a digerir metódicamente todas las vísceras, músculos y grasas internas mediante enzimas proteolíticas, dejando únicamente la armadura exterior de quitina intacta como un caparazón protector contra la intemperie y los carroñeros.",
                    "tituloVisual": "DIGESTION INTERNA",
                    "layout": "split_screen",
                    "composicionVisual": "plano_medio",
                    "escenario": "laboratorio",
                    "transicion": "zoom_in",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["enzimas proteolíticas", "armadura de quitina", "caparazón protector", "vísceras digeridas"],
                    "poseId": "thinking_chin_hand",
                    "expresion": "analytical"
                },
                {
                    "id": 8,
                    "texto": "Días después, una aguja carnosa de color marrón oscuro, llamada estroma, perfora la base de la cabeza de la hormiga muerta, emergiendo detrás del cuello hacia la luz del sol. El tallo crece durante varias semanas hasta desarrollar en su extremo superior una cápsula esférica repleta de esporas sexuales. Desde esa atalaya privilegiada a veinticinco centímetros de altura, justo encima de los senderos transitados por las hormigas sanas que marchan por el suelo, el hongo está listo para detonar la siguiente generación de contagio.",
                    "tituloVisual": "BROTE DEL ESTROMA",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "cielo_dia",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_sci_fi_beep.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["estroma fúngico", "base de la cabeza", "cápsula de esporas", "atalaya privilegiada"],
                    "poseId": "holding_presentation_board",
                    "expresion": "shocked"
                }
            ]
        },
        {
            "id": "cap_5",
            "numero": 5,
            "titulo": "¿Podría Afectar a los Seres Humanos?",
            "resumen": "La ciencia real frente a la ficción cinematográfica de The Last of Us.",
            "escenas": [
                {
                    "id": 9,
                    "texto": "La aterradora biología de Cordyceps saltó a la cultura popular mundial gracias al videojuego y serie The Last of Us, donde una mutación del hongo se adapta a los mamíferos y desata una plaga zombi que destruye la civilización humana. Esto despertó una pregunta inevitable entre el público: ¿podría una mutación real de este parásito infectar y controlar el cerebro de los seres humanos?",
                    "tituloVisual": "EL MITO DE THE LAST OF US",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "habitacion_noche",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["The Last of Us", "plaga zombi", "mamíferos", "mutación real"],
                    "poseId": "standing_curious",
                    "expresion": "confused"
                },
                {
                    "id": 10,
                    "texto": "Desde el punto de vista evolutivo y médico, la respuesta es un rotundo no. Ophiocordyceps ha pasado más de cuarenta y cinco millones de años de coevolución milimétrica especializándose en el sistema nervioso de especies muy concretas de insectos. Nuestro sistema inmunológico endotérmico mantiene el cuerpo a treinta y siete grados centígrados, una temperatura letal para la inmensa mayoría de los hongos microscópicos, y nuestro cerebro posee una complejidad neuronal miles de millones de veces superior al ganglio cerebral de una hormiga.",
                    "tituloVisual": "BARRERA ENDOTERMICA",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "laboratorio",
                    "transicion": "whip_left",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["cuarenta y cinco millones de años", "sistema endotérmico", "treinta y siete grados", "barrera neuronal"],
                    "poseId": "explaining_both_hands",
                    "expresion": "smile_wide",
                    "infografia": {
                        "tipo": "comparacion",
                        "titulo": "Defensas Biológicas",
                        "subtitulo": "Hormiga Artrópoda vs Humano Endotérmico",
                        "valorPrincipal": "37°C",
                        "unidad": "escudo térmico",
                        "items": [
                            {"etiqueta": "Temperatura humana", "valor": "37°C (Letal para el hongo)", "porcentaje": 100, "color": "#38BDF8"},
                            {"etiqueta": "Temperatura insecto", "valor": "Ambiente (20-26°C)", "porcentaje": 45, "color": "#FFE600"}
                        ],
                        "colorAcento": "#38BDF8"
                    }
                }
            ]
        },
        {
            "id": "cap_6",
            "numero": 6,
            "titulo": "El Guardián Invisible del Ecosistema",
            "resumen": "La importancia ecológica del hongo para evitar plagas destructivas.",
            "escenas": [
                {
                    "id": 11,
                    "texto": "Aunque su ciclo vital parece una pesadilla de terror biológico, en la naturaleza Ophiocordyceps cumple una función ecológica indispensable: el control poblacional. Las hormigas son los animales más abundantes y dominantes de los trópicos; si una sola colonia creciera sin freno, devoraría toda la vegetación circundante provocando el colapso del bosque. El hongo actúa como un termostato natural que ataca preferentemente a las colonias superpobladas, garantizando la coexistencia de miles de especies vegetales y animales.",
                    "tituloVisual": "CONTROL POBLACIONAL",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "cielo_dia",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["control poblacional", "termostato natural", "equilibrio del bosque", "colonias superpobladas"],
                    "poseId": "explaining_pointing_up",
                    "expresion": "talking"
                },
                {
                    "id": 12,
                    "texto": "Además, la medicina moderna estudia hoy los metabolitos secundarios de estos hongos en la búsqueda de nuevos fármacos inmunosupresores, antivirales y antitumorales para curar enfermedades humanas. En el misterioso equilibrio de la vida, el mismo organismo capaz de convertir a un insecto en una marioneta sin voluntad nos recuerda la asombrosa sofisticación de la evolución y cómo la muerte de un individuo sostiene la vida eterna del ecosistema entero.",
                    "tituloVisual": "EL EQUILIBRIO PERFECTO",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "laboratorio",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["metabolitos secundarios", "fármacos antitumorales", "equilibrio de la vida", "sofisticación evolutiva"],
                    "poseId": "explaining_both_hands",
                    "expresion": "smile_wide"
                }
            ]
        }
    ]
    actualizar_guion("008", capitulos)


def construir_doc_009():
    capitulos = [
        {
            "id": "cap_1",
            "numero": 1,
            "titulo": "La Pregunta más Simple de la Infancia",
            "resumen": "Por qué la oscuridad del cielo nocturno desconcertó a los astrónomos.",
            "escenas": [
                {
                    "id": 1,
                    "texto": "¿Por qué la noche es oscura? Parece una pregunta infantil con una respuesta obvia: la noche es oscura porque el Sol se oculta tras el horizonte y la Tierra bloquea su luz con su propia masa. Pero en el siglo diecinueve, un médico y astrónomo aficionado alemán llamado Heinrich Wilhelm Olbers demostró que si las ideas dominantes de la ciencia sobre el cosmos fueran correctas, la noche jamás debería ser negra: el cielo entero debería arder con un resplandor abrasador, tan brillante y caluroso como la superficie misma del Sol.",
                    "tituloVisual": "¿POR QUE ES OSCURA LA NOCHE?",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "habitacion_noche",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["oscuridad de la noche", "Heinrich Wilhelm Olbers", "resplandor abrasador", "superficie del Sol"],
                    "poseId": "thinking_chin_hand",
                    "expresion": "confused"
                },
                {
                    "id": 2,
                    "texto": "Durante siglos, desde Isaac Newton hasta inicios del siglo veinte, la física asumía tres pilares fundamentales sobre el universo: primero, que era infinito en tamaño; segundo, que era estático y eterno, existiendo desde siempre sin principio ni final; y tercero, que las estrellas estaban distribuidas de manera homogénea por todo el espacio. Olbers tomó estas tres premisas indiscutibles y descubrió una paradoja matemática implacable que la física clásica no podía resolver.",
                    "tituloVisual": "LOS TRES PILARES CLASICOS",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "laboratorio",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["Isaac Newton", "universo infinito", "eterno y estático", "distribución homogénea"],
                    "poseId": "holding_presentation_board",
                    "expresion": "analytical",
                    "infografia": {
                        "tipo": "tarjeta_concepto",
                        "titulo": "Modelo Clásico",
                        "subtitulo": "Premisas de Newton y Olbers",
                        "valorPrincipal": "Infinito",
                        "unidad": "espacio y tiempo",
                        "items": [
                            {"etiqueta": "Extensión espacial", "valor": "Infinita", "porcentaje": 100, "color": "#38BDF8"},
                            {"etiqueta": "Tiempo cósmico", "valor": "Eterno (Sin Big Bang)", "porcentaje": 100, "color": "#FFE600"}
                        ],
                        "colorAcento": "#FFE600"
                    }
                }
            ]
        },
        {
            "id": "cap_2",
            "numero": 2,
            "titulo": "La Geometría del Bosque Infinito",
            "resumen": "La analogía de los troncos de árboles y las capas de estrellas esféricas.",
            "escenas": [
                {
                    "id": 3,
                    "texto": "Para comprender el dilema, imagina que estás en medio de un bosque pequeño: puedes ver espacios vacíos entre los troncos de los árboles y vislumbrar el campo abierto más allá. Pero si el bosque se extiende infinitamente en todas las direcciones, sin importar hacia dónde mires, tu línea de visión chocará inevitablemente contra el tronco de un árbol. No habrá un solo milímetro libre de corteza vegetal. Ahora reemplaza cada árbol por una estrella brillante como nuestro Sol.",
                    "tituloVisual": "EL BOSQUE DE ESTRELLAS",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "espacio_profundo",
                    "transicion": "zoom_in",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["bosque infinito", "línea de visión", "tronco de árbol", "estrella brillante"],
                    "poseId": "walking_confidently",
                    "expresion": "analytical"
                },
                {
                    "id": 4,
                    "texto": "Cualquiera podría pensar que las estrellas lejanas son más tenues y no iluminan tanto. Es verdad: el brillo aparente de una estrella disminuye con el cuadrado de la distancia. Sin embargo, el número de estrellas en una capa esférica a esa distancia aumenta exactamente con el cuadrado del radio. Ambos efectos matemáticos se cancelan con precisión perfecta: cada cascarón concéntrico del cosmos aporta exactamente la misma cantidad de luz a nuestros ojos. En un cosmos infinito y eterno, cada punto del cielo debería estar ocupado por el disco incandescente de una estrella.",
                    "tituloVisual": "CANCELACION MATEMATICA",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "laboratorio",
                    "transicion": "whip_left",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["cuadrado de la distancia", "cascarón concéntrico", "cancelación geométrica", "disco incandescente"],
                    "poseId": "explaining_pointing_up",
                    "expresion": "eureka",
                    "infografia": {
                        "tipo": "dato_clave",
                        "titulo": "Paradoja Radiativa",
                        "subtitulo": "Brillo vs Cantidad de Estrellas",
                        "valorPrincipal": "1 / r²",
                        "unidad": "vs r² (Se anulan)",
                        "items": [
                            {"etiqueta": "Atenuación por distancia", "valor": "Disminuye con r²", "porcentaje": 50, "color": "#38BDF8"},
                            {"etiqueta": "Densidad de estrellas", "valor": "Aumenta con r²", "porcentaje": 50, "color": "#FFE600"}
                        ],
                        "colorAcento": "#FFE600"
                    }
                }
            ]
        },
        {
            "id": "cap_3",
            "numero": 3,
            "titulo": "Las Falsas Soluciones del Polvo Cósmico",
            "resumen": "Por qué el polvo interestelar no puede resolver el dilema térmico.",
            "escenas": [
                {
                    "id": 5,
                    "texto": "El propio Olbers propuso una solución intuitiva: sugirió que el espacio interestelar no estaba vacío, sino lleno de nubes colosales de gas y polvo que absorbían la luz de los astros más lejanos antes de llegar a la Tierra, manteniendo el cielo oscuro. Durante décadas, muchos astrónomos aceptaron esta explicación como un alivio científico para conservar el modelo estático del universo.",
                    "tituloVisual": "LA HIPOTESIS DEL POLVO",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "espacio_profundo",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["polvo interestelar", "nubes colosales", "absorción de luz", "modelo estático"],
                    "poseId": "thinking_chin_hand",
                    "expresion": "talking"
                },
                {
                    "id": 6,
                    "texto": "Pero la termodinámica moderna echó por tierra la idea de Olbers. Por la primera ley de la conservación de la energía, el polvo no puede destruir la radiación: al absorber fotones durante eones interminables, el gas se calentaría progresivamente hasta alcanzar el equilibrio térmico con las estrellas, comenzando a brillar con la misma intensidad que la radiación que absorbía. El polvo no apagaría la luz del cielo; solo la reemitiría como un horno infrarrojo gigantesco.",
                    "tituloVisual": "EQUILIBRIO TERMODINAMICO",
                    "layout": "split_screen",
                    "composicionVisual": "plano_medio",
                    "escenario": "laboratorio",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["primera ley", "equilibrio térmico", "horno infrarrojo", "conservación de energía"],
                    "poseId": "explaining_both_hands",
                    "expresion": "analytical"
                }
            ]
        },
        {
            "id": "cap_4",
            "numero": 4,
            "titulo": "La Intuición Poética de Edgar Allan Poe",
            "resumen": "El ensayo Eureka de 1848 y la primera solución científica real.",
            "escenas": [
                {
                    "id": 7,
                    "texto": "Increíblemente, la primera persona en formular la respuesta correcta a la paradoja no fue un catedrático de física de Cambridge, sino el célebre escritor y poeta Edgar Allan Poe. En mil novecientos cuarenta y ocho, en su inclasificable ensayo cosmogónico Eureka, Poe escribió unas líneas visionarias: la única forma de que existan vacíos negros entre las estrellas es que la distancia al fondo sea tan inmensa que la luz de los astros más lejanos aún no haya tenido tiempo suficiente de viajar hasta nosotros.",
                    "tituloVisual": "EUREKA (POE, 1848)",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "habitacion_noche",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["Edgar Allan Poe", "Eureka", "tiempo de viaje de la luz", "visión poética"],
                    "poseId": "reading_clipboard",
                    "expresion": "eureka"
                },
                {
                    "id": 8,
                    "texto": "Poe había intuido dos verdades revolucionarias que la astronomía tardaría casi un siglo en formalizar: primero, que la velocidad de la luz es finita, viajando a trescientos mil kilómetros por segundo; y segundo, que el universo no ha existido desde siempre, sino que tuvo un comienzo en el tiempo. Mirar lejos en el espacio equivale a mirar atrás en el tiempo. Existe un límite temporal más allá del cual no hay estrellas porque el universo todavía no las había creado.",
                    "tituloVisual": "MIRAR LEJOS ES MIRAR AL PASADO",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "espacio_profundo",
                    "transicion": "zoom_in",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_sci_fi_beep.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["velocidad de la luz", "trescientos mil kilómetros por segundo", "universo con principio", "mirar al pasado"],
                    "poseId": "explaining_pointing_up",
                    "expresion": "talking",
                    "infografia": {
                        "tipo": "dato_clave",
                        "titulo": "Horizonte Cósmico",
                        "subtitulo": "Edad del Universo Observable",
                        "valorPrincipal": "13.800M",
                        "unidad": "años de antigüedad",
                        "items": [
                            {"etiqueta": "Velocidad de la luz", "valor": "300.000 km/s (Finita)", "porcentaje": 100, "color": "#FFE600"},
                            {"etiqueta": "Luz que aún no llega", "valor": "Más allá del horizonte", "porcentaje": 75, "color": "#38BDF8"}
                        ],
                        "colorAcento": "#FFE600"
                    }
                }
            ]
        },
        {
            "id": "cap_5",
            "numero": 5,
            "titulo": "El Big Bang y la Expansión Cósmica",
            "resumen": "El corrimiento al rojo y el enfriamiento de la radiación primigenia.",
            "escenas": [
                {
                    "id": 9,
                    "texto": "En la década de mil novecientos veinte, Edwin Hubble descubrió que las galaxias se alejan unas de otras a velocidades vertiginosas: el universo se está expandiendo. Este descubrimiento aportó la pieza definitiva que faltaba en el rompecabezas. La expansión del tejido espacio-temporal estira las ondas de luz que viajan a través de él en un fenómeno llamado corrimiento al rojo cosmológico.",
                    "tituloVisual": "EXPANSION DE HUBBLE",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "espacio_profundo",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["Edwin Hubble", "corrimiento al rojo", "expansión del espacio", "ondas de luz estiradas"],
                    "poseId": "astronomy_telescope",
                    "expresion": "analytical"
                },
                {
                    "id": 10,
                    "texto": "Sí hubo un momento en que el universo entero estuvo saturado de luz brillante: los primeros trescientos ochenta mil años tras el Big Bang, cuando el cosmos era una sopa ardiente de plasma brillante. Sin embargo, a lo largo de trece mil ochocientos millones de años de expansión ininterrumpida, esa radiación de luz visible se estiró tanto que se transformó en microondas invisibles para nuestros ojos. El cielo sí brilla en todas direcciones, pero en una frecuencia que nuestros ojos biológicos no pueden ver.",
                    "tituloVisual": "FONDO COSMICO DE MICROONDAS",
                    "layout": "split_screen",
                    "composicionVisual": "plano_medio",
                    "escenario": "laboratorio",
                    "transicion": "whip_left",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["trescientos ochenta mil años", "Fondo Cósmico de Microondas", "trece mil ochocientos millones", "microondas invisibles"],
                    "poseId": "explaining_both_hands",
                    "expresion": "eureka"
                }
            ]
        },
        {
            "id": "cap_6",
            "numero": 6,
            "titulo": "La Prueba Visible de que el Cosmos Nació",
            "resumen": "La oscuridad de la noche como el monumento visual más grandioso.",
            "escenas": [
                {
                    "id": 11,
                    "texto": "La próxima vez que salgas al patio de tu casa y mires el cielo nocturno salpicado de estrellas sobre un fondo negro profundo, comprende el asombroso secreto que tienes ante ti: la oscuridad de la noche no es la simple ausencia de luz, sino la prueba científica más rotunda y accesible de que el universo tuvo un origen y no ha existido por toda la eternidad.",
                    "tituloVisual": "EL MONUMENTO NOCTURNO",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "habitacion_noche",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["fondo negro profundo", "prueba más accesible", "origen del universo", "secreto cósmico"],
                    "poseId": "standing_curious",
                    "expresion": "hopeful"
                },
                {
                    "id": 12,
                    "texto": "Si el universo fuera estático e infinito, la vida en la Tierra sería físicamente imposible: los océanos se habrían evaporado y la superficie ardería como una estrella perpetua. La oscuridad es el escudo que nos permite existir, la huella visible del Big Bang y el recordatorio silencioso de que habitamos un cosmos joven, dinámico y en constante evolución.",
                    "tituloVisual": "EL ESCUDO OSCURO",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "espacio_profundo",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["océanos evaporados", "escudo vital", "cosmos joven", "huella del Big Bang"],
                    "poseId": "explaining_both_hands",
                    "expresion": "smile_wide"
                }
            ]
        }
    ]
    actualizar_guion("009", capitulos)


def construir_doc_010():
    capitulos = [
        {
            "id": "cap_1",
            "numero": 1,
            "titulo": "El Dibujo que Todos Pintamos de Niños",
            "resumen": "El Sol amarillo en el papel y la verdad científica desde el espacio exterior.",
            "escenas": [
                {
                    "id": 1,
                    "texto": "Si le pides a cualquier niño en cualquier colegio del planeta que dibuje un paisaje en un día soleado, tomará invariablemente un crayón amarillo para pintar el Sol en la esquina del papel. Es una convención cultural tan arraigada que hasta los astrónomos profesionales clasifican a nuestra estrella en los catálogos científicos bajo la etiqueta de enana amarilla. Sin embargo, si pudieras quitarte el filtro de la atmósfera terrestre y mirar al Sol desde el vacío del espacio, te encontrarías con una sorpresa deslumbrante: el Sol no es amarillo, ni naranja, ni rojo; es de un blanco inmaculado y puro.",
                    "tituloVisual": "EL CRAYON AMARILLO",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "cielo_dia",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["crayón amarillo", "enana amarilla", "espacio exterior", "blanco inmaculado"],
                    "poseId": "thinking_chin_hand",
                    "expresion": "confused"
                },
                {
                    "id": 2,
                    "texto": "Las fotografías captadas por los astronautas en la Estación Espacial Internacional confirman esta realidad a diario: contra el telón negro azabache del cosmos, el Sol brilla como una esfera de luz blanca resplandeciente, idéntica a una bombilla halógena de laboratorio encendida al máximo. Para comprender por qué la humanidad lleva milenios creyendo que nuestra estrella es amarilla, debemos desarmar la física de la luz y el engaño óptico que produce la atmósfera de nuestro propio planeta.",
                    "tituloVisual": "LUCES EN LA ESTACION ESPACIAL",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "espacio_profundo",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_sci_fi_beep.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["Estación Espacial", "telón negro", "esfera blanca", "engaño óptico"],
                    "poseId": "explaining_pointing_up",
                    "expresion": "eureka",
                    "infografia": {
                        "tipo": "comparacion",
                        "titulo": "Color Real del Sol",
                        "subtitulo": "Desde la Tierra vs Desde el Espacio",
                        "valorPrincipal": "#FFFFFF",
                        "unidad": "blanco puro",
                        "items": [
                            {"etiqueta": "Visto en el Espacio", "valor": "Blanco puro (Todas las longitudes)", "porcentaje": 100, "color": "#FFFFFF"},
                            {"etiqueta": "Visto en la Tierra", "valor": "Amarillo / Anaranjado (Dispersión)", "porcentaje": 70, "color": "#FFE600"}
                        ],
                        "colorAcento": "#FFE600"
                    }
                }
            ]
        },
        {
            "id": "cap_2",
            "numero": 2,
            "titulo": "La Física del Cuerpo Negro y el Arcoíris Solar",
            "resumen": "La emisión de todas las longitudes de onda y el pico verde del espectro.",
            "escenas": [
                {
                    "id": 3,
                    "texto": "El Sol es lo que los físicos llaman un radiador de cuerpo negro casi perfecto. Su fotosfera, la superficie visible que vemos brillar, arde a una temperatura constante de aproximadamente cinco mil quinientos grados centígrados. A esa temperatura precisa, la termodinámica dicta que el Sol emite radiación electromagnética en todas y cada una de las longitudes de onda del espectro visible de manera simultánea: emite fotones rojos, anaranjados, amarillos, verdes, cianes, azules y violetas.",
                    "tituloVisual": "EL CUERPO NEGRO SOLAR",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "laboratorio",
                    "transicion": "zoom_in",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["cuerpo negro", "fotosfera solar", "cinco mil quinientos grados", "espectro visible"],
                    "poseId": "holding_presentation_board",
                    "expresion": "analytical"
                },
                {
                    "id": 4,
                    "texto": "De hecho, si medimos con un espectrómetro de alta precisión la energía emitida por cada color, descubrimos una paradoja aún más desconcertante: el pico máximo de emisión del Sol no está en el amarillo ni en el rojo, sino en la frontera entre el color verde y el azul, alrededor de los quinientos nanómetros. ¿Por qué entonces no vemos un Sol de color verde esmeralda? Porque el Sol no emite solo en verde; emite cantidades ingentes de todos los demás colores al mismo tiempo. Cuando todos los colores del espectro visible llegan juntos a nuestros ojos, el cerebro humano los suma y procesa una única sensación visual: luz blanca perfecta.",
                    "tituloVisual": "EL PICO VERDE INVISIBLE",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "laboratorio",
                    "transicion": "whip_left",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["quinientos nanómetros", "pico verde", "suma de colores", "luz blanca perfecta"],
                    "poseId": "explaining_both_hands",
                    "expresion": "eureka",
                    "infografia": {
                        "tipo": "grafico_barras",
                        "titulo": "Espectro Solar Visible",
                        "subtitulo": "Emisión Fotométrica por Longitud de Onda",
                        "valorPrincipal": "500 nm",
                        "unidad": "pico espectral",
                        "items": [
                            {"etiqueta": "Azul y Violeta (400-480nm)", "valor": "Muy alta intensidad", "porcentaje": 88, "color": "#38BDF8"},
                            {"etiqueta": "Verde (500nm - Pico)", "valor": "Máxima intensidad", "porcentaje": 100, "color": "#22C55E"},
                            {"etiqueta": "Rojo y Naranja (600-700nm)", "valor": "Alta intensidad continua", "porcentaje": 80, "color": "#EF4444"}
                        ],
                        "colorAcento": "#22C55E"
                    }
                }
            ]
        },
        {
            "id": "cap_3",
            "numero": 3,
            "titulo": "La Dispersión de Rayleigh: El Ladrón de Color",
            "resumen": "Cómo las moléculas de nitrógeno y oxígeno roban la luz azul del disco.",
            "escenas": [
                {
                    "id": 5,
                    "texto": "Si la luz solar es blanca pura, ¿por qué desde el suelo la percibimos amarillenta durante el día? El responsable de esta ilusión es el fenómeno físico de la dispersión de Rayleigh, bautizado en honor al físico británico Lord Rayleigh. La atmósfera de la Tierra no es un cristal transparente; es un océano denso de billones de moléculas de nitrógeno y oxígeno. Cuando la luz blanca del Sol impacta contra estas partículas diminutas, los diferentes colores no reaccionan de la misma manera.",
                    "tituloVisual": "DISPERSION DE RAYLEIGH",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "cielo_dia",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["Lord Rayleigh", "dispersión de Rayleigh", "nitrógeno y oxígeno", "océano denso"],
                    "poseId": "walking_confidently",
                    "expresion": "analytical"
                },
                {
                    "id": 6,
                    "texto": "Las ondas de luz con longitudes de onda cortas, como el azul y el violeta, colisionan violentamente con los gases atmosféricos y se dispersan rebotando en todas las direcciones del firmamento; esa es la razón exacta por la que el cielo diurno es azul. Al robarle gran parte del componente azul al haz directo que llega desde el Sol, la luz remanente que continúa en línea recta hacia nuestros ojos queda desbalanceada hacia el extremo cálido del espectro: una mezcla dominante de rojo, naranja y amarillo que nuestro cerebro interpreta como un cálido tono amarillento.",
                    "tituloVisual": "EL CIELO SE ROBA EL AZUL",
                    "layout": "split_screen",
                    "composicionVisual": "plano_medio",
                    "escenario": "cielo_dia",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["cielo diurno azul", "haz directo", "extremo cálido", "desbalance cromático"],
                    "poseId": "explaining_pointing_up",
                    "expresion": "eureka"
                }
            ]
        },
        {
            "id": "cap_4",
            "numero": 4,
            "titulo": "La Tragedia Visual del Atardecer",
            "resumen": "Por qué los atardeceres tiñen el horizonte de carmesí y oro.",
            "escenas": [
                {
                    "id": 7,
                    "texto": "Al atardecer y al amanecer, el efecto de filtrado atmosférico alcanza su expresión más extrema y espectacular. Cuando el Sol desciende hacia la línea del horizonte, sus rayos deben atravesar una capa de atmósfera hasta diez veces más gruesa que cuando se encuentra en el cenit del mediodía. Esta gigantesca muralla de aire actúa como un filtro implacable que dispersa prácticamente la totalidad de los fotones azules, verdes y amarillos.",
                    "tituloVisual": "EL ATARDECER ROJO",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "cielo_dia",
                    "transicion": "zoom_in",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["diez veces más atmósfera", "línea del horizonte", "filtro implacable", "atardecer carmesí"],
                    "poseId": "standing_curious",
                    "expresion": "talking"
                },
                {
                    "id": 8,
                    "texto": "Solo las longitudes de onda más largas y resistentes, correspondientes a los rojos profundos y los naranjas oscuros, logran sortear los miles de kilómetros de gases sin dispersarse y alcanzar la retina del observador. Por eso el Sol del ocaso se transforma en una esfera de fuego roja que parece arder sin dañar la vista: no es que la estrella haya cambiado de temperatura ni de naturaleza; es que la atmósfera terrestre se ha tragado literalmente todos los demás colores.",
                    "tituloVisual": "FILTRO DE DIEZ VECES",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "cielo_dia",
                    "transicion": "whip_left",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["longitudes de onda largas", "esfera de fuego roja", "ocaso solar", "atmósfera espesa"],
                    "poseId": "thinking_chin_hand",
                    "expresion": "analytical",
                    "infografia": {
                        "tipo": "dato_clave",
                        "titulo": "Espesor Atmosférico",
                        "subtitulo": "Camino Óptico según Ángulo Solar",
                        "valorPrincipal": "10x",
                        "unidad": "masa de aire al ocaso",
                        "items": [
                            {"etiqueta": "Cenit (Mediodía)", "valor": "1 atmósfera de espesor (Blanco-amarillo)", "porcentaje": 10, "color": "#38BDF8"},
                            {"etiqueta": "Horizonte (Ocaso)", "valor": "Hasta 10 atmósferas (Rojo profundo)", "porcentaje": 100, "color": "#EF4444"}
                        ],
                        "colorAcento": "#EF4444"
                    }
                }
            ]
        },
        {
            "id": "cap_5",
            "numero": 5,
            "titulo": "La Evolución del Ojo Humano",
            "resumen": "Nuestros ojos evolucionaron calibrados para la luz solar blanca.",
            "escenas": [
                {
                    "id": 9,
                    "texto": "Hay una prueba biológica concluyente de que el Sol es blanco: nuestros propios ojos. La visión humana no evolucionó por casualidad; a lo largo de cientos de millones de años de selección natural, los fotorreceptores de la retina de nuestros ancestros marinos y terrestres se calibraron con precisión matemática para aprovechar al máximo la radiación emitida por la estrella que baña nuestro planeta.",
                    "tituloVisual": "CALIBRACION BIOLOGICA",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "laboratorio",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_sci_fi_beep.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["fotorreceptores", "retina humana", "selección natural", "visión biológica"],
                    "poseId": "explaining_both_hands",
                    "expresion": "analytical"
                },
                {
                    "id": 10,
                    "texto": "Nuestros tres tipos de conos oculares responden a las bandas roja, verde y azul. El cerebro define biológicamente el concepto de blanco como la suma equilibrada de toda la luz disponible en el ambiente diurno. Si el Sol fuera verdaderamente amarillo, todos los objetos blancos que iluminara —como la nieve fresca o una hoja de papel— se verían amarillos por defecto. La razón por la que vemos la nieve blanca bajo el Sol del mediodía es que la luz solar directa es blanca.",
                    "tituloVisual": "EL BLANCO DE LA NIEVE",
                    "layout": "split_screen",
                    "composicionVisual": "plano_medio",
                    "escenario": "cielo_dia",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["conos oculares", "nieve fresca", "hoja de papel", "luz blanca directa"],
                    "poseId": "explaining_pointing_up",
                    "expresion": "eureka"
                }
            ]
        },
        {
            "id": "cap_6",
            "numero": 6,
            "titulo": "La Lección del Prisma Cósmico",
            "resumen": "La desmitificación de los catálogos y la belleza de la realidad física.",
            "escenas": [
                {
                    "id": 11,
                    "texto": "La clasificación del Sol como enana amarilla es una simple convención astronómica nacida del sistema de clasificación de Harvard desarrollado a finales del siglo diecinueve, donde las estrellas de tipo espectral G se etiquetan tradicionalmente como amarillas para distinguirlas de las estrellas azules de tipo O y las gigantes rojas de tipo M. Pero en el cosmos real, un astrónomo extraterrestre que observara nuestro sistema solar desde Alpha Centauri vería un punto de luz blanca pura y deslumbrante.",
                    "tituloVisual": "TIPO ESPECTRAL G",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "espacio_profundo",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["enana amarilla", "tipo espectral G", "clasificación de Harvard", "Alpha Centauri"],
                    "poseId": "holding_presentation_board",
                    "expresion": "talking"
                },
                {
                    "id": 12,
                    "texto": "Saber que el Sol es blanco no le quita magia al dibujo de un niño ni a la poesía de un atardecer dorado en la playa. Al contrario: nos demuestra que nuestra atmósfera es un prisma colosal y protector que no solo nos resguarda de la radiación mortal del espacio, sino que pinta el cielo de azul y tiñe nuestra estrella de oro para regalarnos el espectáculo visual más hermoso del universo conocido.",
                    "tituloVisual": "EL PRISMA CELESTIAL",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "cielo_dia",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["prisma colosal", "atardecer dorado", "radiación mortal", "espectáculo visual"],
                    "poseId": "explaining_both_hands",
                    "expresion": "smile_wide"
                }
            ]
        }
    ]
    actualizar_guion("010", capitulos)


def construir_doc_011():
    capitulos = [
        {
            "id": "cap_1",
            "numero": 1,
            "titulo": "Las Prisiones Eternas de la Relatividad",
            "resumen": "La visión clásica de los agujeros negros como tumbas gravitacionales irreversibles.",
            "escenas": [
                {
                    "id": 1,
                    "texto": "Durante más de medio siglo tras la formulación de la relatividad general de Albert Einstein, los agujeros negros fueron considerados las tumbas definitivas del universo: prisiones gravitacionales tan monstruosas e implacables que nada, ni siquiera la luz a trescientos mil kilómetros por segundo, podía escapar de su interior una vez cruzada la frontera del horizonte de sucesos. Eran el callejón sin salida de la física cósmica, objetos que solo podían tragar materia y crecer eternamente sin devolver jamás un solo fotón al cosmos.",
                    "tituloVisual": "EL CALLEJON SIN SALIDA",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "espacio_profundo",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["Albert Einstein", "relatividad general", "horizonte de sucesos", "tumbas gravitacionales"],
                    "poseId": "thinking_chin_hand",
                    "expresion": "analytical"
                },
                {
                    "id": 2,
                    "texto": "Esta imagen clásica planteaba una violación alarmante de una de las leyes más sagradas de la ciencia: la segunda ley de la termodinámica. Si un agujero negro fuera verdaderamente negro y frío, su temperatura debería ser el cero absoluto y su entropía debería ser nula. Pero si arrojabas un objeto caliente con alta entropía dentro de él, esa entropía parecía desvanecerse del universo sin dejar rastro, violando el principio de que el desorden cósmico siempre debe aumentar. Stephen Hawking se propuso demostrar que esta idea estaba equivocada, pero terminó descubriendo una verdad aún más revolucionaria.",
                    "tituloVisual": "LA PARADOJA TERMICA",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "laboratorio",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["segunda ley de la termodinámica", "cero absoluto", "Stephen Hawking", "entropía cósmica"],
                    "poseId": "holding_presentation_board",
                    "expresion": "eureka",
                    "infografia": {
                        "tipo": "tarjeta_concepto",
                        "titulo": "Dilema Termodinámico",
                        "subtitulo": "Relatividad vs Física Cuántica",
                        "valorPrincipal": "0 K",
                        "unidad": "¿Cero Absoluto?",
                        "items": [
                            {"etiqueta": "Relatividad Clásica", "valor": "Agujero Negro no emite nada", "porcentaje": 100, "color": "#94A3B8"},
                            {"etiqueta": "Mecánica Cuántica", "valor": "Debe poseer temperatura y radiación", "porcentaje": 100, "color": "#FFE600"}
                        ],
                        "colorAcento": "#FFE600"
                    }
                }
            ]
        },
        {
            "id": "cap_2",
            "numero": 2,
            "titulo": "El Matrimonio Imposible de Hawking (1974)",
            "resumen": "La unión entre la gravedad de Einstein y el vacío cuántico.",
            "escenas": [
                {
                    "id": 3,
                    "texto": "En mil novecientos setenta y cuatro, el joven físico teórico Stephen Hawking publicó en la revista Nature un artículo que sacudió los cimientos de la ciencia teórica: Black hole explosions?. Hawking logró por primera vez en la historia aplicar las leyes de la mecánica cuántica a los bordes del horizonte de sucesos de un agujero negro. El vacío del espacio, según la teoría cuántica de campos, no es una nada estéril e inmóvil; es un hervidero espumoso de actividad cuántica donde pares de partículas y antipartículas virtuales brotan continuamente de la nada y se aniquilan en fracciones de segundo.",
                    "tituloVisual": "EL VACIO CUANTICO",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "espacio_profundo",
                    "transicion": "zoom_in",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_sci_fi_beep.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["mil novecientos setenta y cuatro", "Stephen Hawking", "Black hole explosions", "partículas virtuales"],
                    "poseId": "walking_confidently",
                    "expresion": "eureka"
                },
                {
                    "id": 4,
                    "texto": "Pero qué sucede cuando este par de partículas virtuales brota justo en la línea divisoria del horizonte de sucesos? La gigantesca marea gravitatoria del agujero negro desgarra el par antes de que puedan aniquilarse: una de las partículas cae irremediablemente hacia el interior del abismo, mientras que su compañera queda libre en el exterior y escapa hacia el espacio profundo como una partícula real. Para un observador distante, parece que el agujero negro está emitiendo una tenue radiación térmica: la radiación de Hawking.",
                    "tituloVisual": "DESGARRO DE PARTICULAS",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "laboratorio",
                    "transicion": "whip_left",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["horizonte de sucesos", "partícula virtual", "partícula real libre", "radiación de Hawking"],
                    "poseId": "explaining_pointing_up",
                    "expresion": "analytical",
                    "infografia": {
                        "tipo": "dato_clave",
                        "titulo": "Mecanismo Cuántico",
                        "subtitulo": "Emisión en el Horizonte de Sucesos",
                        "valorPrincipal": "E = mc²",
                        "unidad": "Pérdida de masa",
                        "items": [
                            {"etiqueta": "Partícula capturada", "valor": "Energía negativa neta", "porcentaje": 50, "color": "#38BDF8"},
                            {"etiqueta": "Partícula expulsada", "valor": "Radiación térmica visible", "porcentaje": 50, "color": "#FFE600"}
                        ],
                        "colorAcento": "#FFE600"
                    }
                }
            ]
        },
        {
            "id": "cap_3",
            "numero": 3,
            "titulo": "La Pérdida de Masa y la Evaporación",
            "resumen": "Por qué la energía de la partícula que escapa se cobra de la masa del agujero.",
            "escenas": [
                {
                    "id": 5,
                    "texto": "La ley de conservación de la energía no perdona: la partícula que escapó hacia el cosmos tiene energía positiva real. Para equilibrar el balance energético del universo, la partícula que cayó al interior del agujero negro debe poseer matemáticamente energía negativa. Esto significa algo revolucionario: cada partícula capturada no engorda al agujero negro, sino que le resta masa de forma constante. Los agujeros negros no son eternos; están perdiendo masa segundo tras segundo, evaporándose lentamente en la nada.",
                    "tituloVisual": "ENERGIA NEGATIVA",
                    "layout": "split_screen",
                    "composicionVisual": "plano_medio",
                    "escenario": "espacio_profundo",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["conservación de la energía", "energía negativa", "resta de masa", "evaporación lenta"],
                    "poseId": "explaining_both_hands",
                    "expresion": "talking"
                },
                {
                    "id": 6,
                    "texto": "La velocidad de esta evaporación sigue una regla termodinámica fascinante e inversa: cuanto más masivo y gigante es un agujero negro, más frío es y más despacio se evapora. Un agujero negro supermasivo como el del centro de nuestra galaxia emite a una temperatura de fracciones infinitesimales de nanokelvin, mucho más frío que el fondo cósmico de microondas. Pero a medida que el agujero pierde masa y se hace más pequeño, su temperatura aumenta vertiginosamente, emitiendo cada vez más radiación con mayor furia.",
                    "tituloVisual": "REGLA INVERSA DE MASA",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "laboratorio",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["regla inversa", "más frío cuanto más grande", "nanokelvin", "temperatura vertiginosa"],
                    "poseId": "thinking_chin_hand",
                    "expresion": "analytical",
                    "infografia": {
                        "tipo": "comparacion",
                        "titulo": "Escala Térmica de Hawking",
                        "subtitulo": "Masa vs Temperatura y Evaporación",
                        "valorPrincipal": "T ∝ 1/M",
                        "unidad": "Inversamente proporcional",
                        "items": [
                            {"etiqueta": "Agujero Supermasivo (Sgr A*)", "valor": "0.00000000001 K (Ultragélido)", "porcentaje": 5, "color": "#38BDF8"},
                            {"etiqueta": "Micro Agujero Negro", "valor": "Billones de Grados (Explosivo)", "porcentaje": 100, "color": "#FFE600"}
                        ],
                        "colorAcento": "#FFE600"
                    }
                }
            ]
        },
        {
            "id": "cap_4",
            "numero": 4,
            "titulo": "La Explosión Final de un Monstruo en Miniatura",
            "resumen": "El final catastrófico en un destello de rayos gamma.",
            "escenas": [
                {
                    "id": 7,
                    "texto": "En los últimos segundos de vida de un agujero negro, el proceso de evaporación se transforma en una reacción nuclear desbocada. Cuando la masa desciende al equivalente a una montaña o un asteroide, la temperatura supera la de cualquier estrella del universo. El agujero comienza a emitir torrentes cegadores de rayos gamma y partículas de alta energía a un ritmo exponencial.",
                    "tituloVisual": "LA AGONIA FINAL",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "espacio_profundo",
                    "transicion": "zoom_in",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["últimos segundos", "reacción desbocada", "masa de una montaña", "rayos gamma"],
                    "poseId": "confused_scratch_head",
                    "expresion": "shocked"
                },
                {
                    "id": 8,
                    "texto": "En su último milisegundo de existencia, los últimos cientos de toneladas de masa se convierten íntegramente en radiación pura en una explosión titánica equivalente a millones de bombas termonucleares detonando al mismo instante. Aquel monstruo gravitacional que alguna vez devoró estrellas enteras se desvanece para siempre del tejido espacio-temporal en un fogonazo de luz cósmica, sin dejar tras de sí ni una sola partícula de materia.",
                    "tituloVisual": "MILLONES DE BOMBAS",
                    "layout": "split_screen",
                    "composicionVisual": "plano_medio",
                    "escenario": "espacio_profundo",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["último milisegundo", "bombas termonucleares", "fogonazo de luz", "desvanecimiento total"],
                    "poseId": "explaining_both_hands",
                    "expresion": "eureka"
                }
            ]
        },
        {
            "id": "cap_5",
            "numero": 5,
            "titulo": "La Paradoja de la Información de Hawking",
            "resumen": "¿Se destruye la historia de lo que cayó en el agujero negro?",
            "escenas": [
                {
                    "id": 9,
                    "texto": "El descubrimiento de la evaporación desató la crisis teórica más profunda de la física moderna: la paradoja de la información. La mecánica cuántica exige estrictamente que la información nunca puede destruirse: si conoces el estado final de un sistema, deberías poder reconstruir matemáticamente su pasado. Pero si arrojas una enciclopedia dentro de un agujero negro y este se evapora emitiendo radiación térmica aleatoria e indistinguible, ¿adónde fue a parar el texto de la enciclopedia?",
                    "tituloVisual": "PARADOJA DE INFORMACION",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "laboratorio",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_sci_fi_beep.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["paradoja de la información", "mecánica cuántica", "información indestructible", "texto de la enciclopedia"],
                    "poseId": "thinking_chin_hand",
                    "expresion": "confused"
                },
                {
                    "id": 10,
                    "texto": "Durante tres décadas, Hawking sostuvo que la información se perdía para siempre, lo que habría significado que las leyes de la física cuántica estaban incompletas. Sin embargo, gracias a los trabajos de Leonard Susskind y el principio holográfico formulado por Gerard 't Hooft y Juan Maldacena, hoy la mayoría de los físicos acepta que la información queda codificada de forma sutil en las fluctuaciones cuánticas del horizonte de sucesos y escapa enredada en la propia radiación de Hawking.",
                    "tituloVisual": "EL PRINCIPIO HOLOGRAFICO",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "laboratorio",
                    "transicion": "whip_left",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["Leonard Susskind", "principio holográfico", "Juan Maldacena", "enredo cuántico"],
                    "poseId": "explaining_pointing_up",
                    "expresion": "eureka",
                    "infografia": {
                        "tipo": "tarjeta_concepto",
                        "titulo": "Resolución Holográfica",
                        "subtitulo": "La Información se Conserva",
                        "valorPrincipal": "2D $\\rightarrow$ 3D",
                        "unidad": "Holograma Cuántico",
                        "items": [
                            {"etiqueta": "Horizonte de sucesos", "valor": "Codifica la información en 2D", "porcentaje": 100, "color": "#FFE600"},
                            {"etiqueta": "Radiación saliente", "valor": "Lleva la huella cuántica enredada", "porcentaje": 90, "color": "#38BDF8"}
                        ],
                        "colorAcento": "#FFE600"
                    }
                }
            ]
        },
        {
            "id": "cap_6",
            "numero": 6,
            "titulo": "El Destino del Universo y el Epitafio de Hawking",
            "resumen": "La era de los agujeros negros en el futuro remoto del cosmos.",
            "escenas": [
                {
                    "id": 11,
                    "texto": "El tiempo que tardará un agujero negro estelar en evaporarse por completo desafía la imaginación humana: un uno seguido de sesenta y siete ceros de años. Y los agujeros negros supermasivos requerirán más de un uno seguido de cien ceros de años. En ese futuro inimaginablemente remoto, todas las estrellas se habrán apagado, las galaxias se habrán disuelto y los agujeros negros serán los últimos gobernantes del universo antes de evaporarse uno tras otro en la oscuridad.",
                    "tituloVisual": "UN UNO SEGUIDO DE CIEN CEROS",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "espacio_profundo",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["sesenta y siete ceros", "cien ceros de años", "futuro remoto", "últimos gobernantes"],
                    "poseId": "astronomy_telescope",
                    "expresion": "sad"
                },
                {
                    "id": 12,
                    "texto": "Cuando Stephen Hawking falleció en dos mil dieciocho, sus cenizas fueron enterradas en la Abadía de Westminster entre las tumbas de Isaac Newton y Charles Darwin. Sobre su lápida de piedra está grabada una sola fórmula matemática: la ecuación de la temperatura de Hawking. Esa breve línea de símbolos resume la victoria intelectual más hermosa de su vida: haber demostrado que ni siquiera los abismos más oscuros y aterradores del cosmos son capaces de retener su luz para siempre.",
                    "tituloVisual": "EL EPITAFIO EN WESTMINSTER",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "laboratorio",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["Abadía de Westminster", "fórmula de Hawking", "Isaac Newton", "abismos no son eternos"],
                    "poseId": "explaining_both_hands",
                    "expresion": "smile_wide"
                }
            ]
        }
    ]
    actualizar_guion("011", capitulos)


if __name__ == "__main__":
    print("Redactando Lote 2 (008, 009, 010, 011)...")
    construir_doc_008()
    construir_doc_009()
    construir_doc_010()
    construir_doc_011()
    print("Lote 2 completado.")
