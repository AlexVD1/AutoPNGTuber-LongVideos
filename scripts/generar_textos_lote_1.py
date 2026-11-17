#!/usr/bin/env python3
"""
Lote 1: Documentales 004, 005, 006 y 007 expandidos a 7.5 - 8.5 minutos.
"""

from redactar_guiones_largos_completos import actualizar_guion


def construir_doc_004():
    capitulos = [
        {
            "id": "cap_1",
            "numero": 1,
            "titulo": "La Noche del 15 de Agosto de 1977",
            "resumen": "El radiotelescopio Big Ear y el hallazgo de Jerry Ehman en el papel continuo.",
            "escenas": [
                {
                    "id": 1,
                    "texto": "La noche del quince de agosto de mil novecientos setenta y siete, en un rincón apartado de Ohio, un radiotelescopio apodado Big Ear escaneaba pacientemente el firmamento. El observatorio no tenía pantallas a color ni procesadores modernos; todo se registraba mecánicamente sobre rollos de papel continuo mediante una impresora matricial que zumbaba en la penumbra. El joven astrónomo voluntario Jerry Ehman revisaba pilas de datos rutinarios cuando de pronto sus ojos se toparon con algo imposible: una columna vertical de seis caracteres alfanuméricos que rompía por completo la monotonía del ruido cósmico. Incapaz de contener su asombro, tomó un bolígrafo rojo, trazó un círculo tembloroso alrededor de la secuencia y escribió una sola palabra al margen: Guau.",
                    "tituloVisual": "OHIO, 15 DE AGOSTO",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "habitacion_noche",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["quince de agosto", "radiotelescopio", "impresora matricial", "Jerry Ehman"],
                    "poseId": "reading_clipboard",
                    "expresion": "shocked"
                },
                {
                    "id": 2,
                    "texto": "Para entender la conmoción de Ehman hay que mirar cómo registraba el telescopio. Cada carácter en el papel representaba la potencia de la señal recibida en intervalos de doce segundos. Un espacio en blanco era ruido mínimo, los números del uno al nueve medían potencias crecientes, y cuando la intensidad superaba la cifra nueve, el sistema pasaba a letras: la A valía diez, la B once, y así sucesivamente. La señal captada aquella noche no fue un destello errático: comenzó con un seis, escaló suavemente a la letra E, alcanzó la cúspide con una Q y una J, y volvió a descender con un cinco. Había alcanzado una potencia treinta veces superior a cualquier murmullo natural del espacio profundo.",
                    "tituloVisual": "CODIGO 6EQUJ5",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "laboratorio",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["doce segundos", "escala alfanumérica", "treinta veces", "potencia"],
                    "poseId": "explaining_pointing_up",
                    "expresion": "analytical",
                    "infografia": {
                        "tipo": "dato_clave",
                        "titulo": "Escala de Potencia",
                        "subtitulo": "Secuencia Alfanumérica 6EQUJ5",
                        "valorPrincipal": "30x",
                        "unidad": "sobre el fondo",
                        "items": [
                            {"etiqueta": "Q (Pico máximo)", "valor": "Intensidad 26", "porcentaje": 100, "color": "#FFE600"},
                            {"etiqueta": "Ruido promedio", "valor": "Intensidad 1 a 2", "porcentaje": 8, "color": "#94A3B8"}
                        ],
                        "colorAcento": "#FFE600"
                    }
                }
            ]
        },
        {
            "id": "cap_2",
            "numero": 2,
            "titulo": "La Frecuencia Sagrada: 1420 Megahercios",
            "resumen": "Por qué la señal coincidió con la línea de emisión del hidrógeno neutro.",
            "escenas": [
                {
                    "id": 3,
                    "texto": "Lo que verdaderamente heló la sangre de los astrofísicos no fue solo su asombrosa potencia, sino la frecuencia exacta en la que vibraba: mil cuatrocientos veinte megahercios. Dieciocho años antes, en mil novecientos cincuenta y nueve, los físicos Giuseppe Cocconi y Philip Morrison habían publicado un célebre artículo en la revista Nature proponiendo que si una civilización extraterrestre intentara comunicarse con otras especies a través del abismo interestelar, elegiría inevitablemente esa longitud de onda. Es la frecuencia natural a la que oscila el hidrógeno neutro, el elemento químico más abundante y ubicuo del cosmos. Emitir en mil cuatrocientos veinte megahercios era como sintonizar la radio en la única estación común que todo observador inteligente en la galaxia debería conocer.",
                    "tituloVisual": "1420 MEGAHERCIOS",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "laboratorio",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["mil cuatrocientos veinte", "hidrógeno neutro", "Cocconi y Morrison", "radio interestelar"],
                    "poseId": "holding_presentation_board",
                    "expresion": "eureka",
                    "infografia": {
                        "tipo": "tarjeta_concepto",
                        "titulo": "El Dial Cósmico",
                        "subtitulo": "Línea de Hidrógeno de 21 Centímetros",
                        "valorPrincipal": "1420.4",
                        "unidad": "MHz",
                        "items": [
                            {"etiqueta": "Elemento", "valor": "Hidrógeno Neutro (H I)", "porcentaje": 100, "color": "#38BDF8"},
                            {"etiqueta": "Propósito SETI", "valor": "Canal Universal de Transmisión", "porcentaje": 95, "color": "#FFE600"}
                        ],
                        "colorAcento": "#38BDF8"
                    }
                },
                {
                    "id": 4,
                    "texto": "Además, la transmisión era de banda extremadamente estrecha: ocupaba menos de diez kilohercios de ancho de banda. En astrofísica, las fuentes naturales como púlsares, quásares o nubes de gas emiten radiación en un espectro ancho y desordenado; es físicamente imposible que un fenómeno astrofísico conocido concentre tanta energía en un canal tan diminuto sin tecnología detrás. La señal Wow parecía una portadora pura, idéntica a una emisión de radio artificial. Durante setenta y dos segundos, el telescopio escuchó una campana resonar con una pureza electromagnética perfecta, exactamente en el centro del canal sagrado del hidrógeno.",
                    "tituloVisual": "BANDA ESTRECHA",
                    "layout": "split_screen",
                    "composicionVisual": "plano_general",
                    "escenario": "espacio_profundo",
                    "transicion": "zoom_in",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_sci_fi_beep.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["diez kilohercios", "banda estrecha", "portadora pura", "emisión artificial"],
                    "poseId": "thinking_chin_hand",
                    "expresion": "analytical"
                }
            ]
        },
        {
            "id": "cap_3",
            "numero": 3,
            "titulo": "La Ventana de 72 Segundos",
            "resumen": "Cómo el movimiento de rotación terrestre definió la forma perfecta de campana.",
            "escenas": [
                {
                    "id": 5,
                    "texto": "Muchas personas creen que la señal se apagó repentinamente a los setenta y dos segundos, pero la realidad mecánica del observatorio cuenta una historia aún más fascinante. El radiotelescopio Big Ear era un instrumento fijo: no rotaba para seguir estrellas en el cielo, sino que permanecía inmóvil mientras la rotación de nuestro planeta barría el universo de oeste a este. El campo de visión de la antena tardaba exactamente setenta y dos segundos en cruzar un punto fijo del cielo. Cualquier objeto estelar que emitiera radiación continua entraría en el haz, alcanzaría su punto máximo a los treinta y seis segundos y se desvanecería al salir.",
                    "tituloVisual": "ROTACION DE LA TIERRA",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "espacio_profundo",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["setenta y dos segundos", "rotación terrestre", "antena fija", "Big Ear"],
                    "poseId": "walking_confidently",
                    "expresion": "analytical"
                },
                {
                    "id": 6,
                    "texto": "Y eso fue exactamente lo que dibujó la secuencia 6EQUJ5: una curva gaussiana impecable, la huella dactilar geométrica de un haz de radio cruzando una antena fija en la Tierra. Esto demostró dos cosas cruciales: primero, que la fuente no provenía de un avión, un satélite en órbita baja o un transmisor terrestre cercano, los cuales habrían mostrado patrones erráticos o repetitivos; y segundo, que el origen de la señal estaba situado a una distancia infinita en el cielo profundo, en las inmediaciones de la constelación de Sagitario.",
                    "tituloVisual": "CURVA GAUSSIANA",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "laboratorio",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["curva gaussiana", "Sagitario", "distancia infinita", "huella geométrica"],
                    "poseId": "explaining_both_hands",
                    "expresion": "eureka",
                    "infografia": {
                        "tipo": "grafico_barras",
                        "titulo": "Perfil Temporal (72s)",
                        "subtitulo": "Coincidencia con el Lóbulo de la Antena",
                        "valorPrincipal": "72s",
                        "unidad": "duración exacta",
                        "items": [
                            {"etiqueta": "Entrada (0-24s)", "valor": "6 a E", "porcentaje": 40, "color": "#38BDF8"},
                            {"etiqueta": "Pico central (36s)", "valor": "Q a U", "porcentaje": 100, "color": "#FFE600"},
                            {"etiqueta": "Salida (48-72s)", "valor": "J a 5", "porcentaje": 45, "color": "#38BDF8"}
                        ],
                        "colorAcento": "#FFE600"
                    }
                }
            ]
        },
        {
            "id": "cap_4",
            "numero": 4,
            "titulo": "Las Hipótesis Terrestres Descartadas",
            "resumen": "El análisis minucioso de satélites secretos, aviones y reflejos cometarios.",
            "escenas": [
                {
                    "id": 7,
                    "texto": "Durante las décadas posteriores, la comunidad científica intentó desmontar el enigma buscando explicaciones mundanas. ¿Pudo ser un satélite espía soviético o estadounidense? No: en mil novecientos setenta y siete no existía ningún satélite en órbita transmitiendo en esa porción protegida del espectro, ya que los mil cuatrocientos veinte megahercios están reservados por tratados internacionales exclusivamente a la radioastronomía pasiva. Tampoco pudo ser una reflexión en basura espacial, porque ningún objeto orbital permaneció en esa posición durante setenta y dos segundos sin registrarse en los radares de defensa.",
                    "tituloVisual": "ESPECTRO PROTEGIDO",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "laboratorio",
                    "transicion": "zoom_in",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["satélite espía", "tratados internacionales", "radioastronomía pasiva", "basura espacial"],
                    "poseId": "confused_scratch_head",
                    "expresion": "analytical"
                },
                {
                    "id": 8,
                    "texto": "En dos mil diecisiete surgió una teoría que acaparó titulares: el astrónomo Antonio Paris sugirió que dos cometas, desconocidos en mil novecientos setenta y siete, habían cruzado esa región del cielo envueltos en gigantescas nubes de vapor de hidrógeno que pudieron generar la emisión. Sin embargo, los astrónomos del observatorio desestimaron rápidamente la idea: los cometas son fuentes difusas de emisión extraordinariamente débil, incapaces de producir un pulso tan concentrado, potente y de banda estrecha sin detectarse en el segundo receptor que el Big Ear tenía apuntando a la misma zona minutos después.",
                    "tituloVisual": "LA HIPOTESIS COMETARIA",
                    "layout": "split_screen",
                    "composicionVisual": "plano_medio",
                    "escenario": "espacio_profundo",
                    "transicion": "whip_left",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_impact.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["cometas", "Antonio Paris", "nubes de vapor", "segundo receptor"],
                    "poseId": "explaining_pointing_up",
                    "expresion": "talking"
                }
            ]
        },
        {
            "id": "cap_5",
            "numero": 5,
            "titulo": "El Silencio Ensayado de Sagitario",
            "resumen": "Las búsquedas posteriores con el telescopio de Arecibo y el Very Large Array.",
            "escenas": [
                {
                    "id": 9,
                    "texto": "Si una civilización alienígena nos envió un mensaje, ¿por qué no insistieron? Jerry Ehman y decenas de radioastrónomos apuntaron instrumentos mucho más potentes hacia las mismas coordenadas de Sagitario. El gigantesco radiotelescopio de Arecibo en Puerto Rico y el Very Large Array en Nuevo México escanearon la zona una y otra vez con una sensibilidad miles de veces mayor que la del Big Ear. El resultado fue siempre el mismo: un silencio sepulcral. Ni un solo susurro, ni una variación de tono. Aquella transmisión única pareció desvanecerse en el abismo como un faro que destelló una sola vez y se apagó para siempre.",
                    "tituloVisual": "BUSQUEDA EN ARECIBO",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "espacio_profundo",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_sci_fi_beep.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["Arecibo", "Very Large Array", "silencio sepulcral", "coordenadas de Sagitario"],
                    "poseId": "astronomy_telescope",
                    "expresion": "sad"
                },
                {
                    "id": 10,
                    "texto": "Una de las explicaciones más inquietantes sugiere el fenómeno del centelleo interestelar o la lente gravitacional transitoria: una señal que viajaba por el cosmos fue amplificada momentáneamente miles de veces al alinearse de forma milimétrica con una nube de plasma o la gravedad de una estrella intermedia. O tal vez, como argumentan los teóricos del programa SETI, no era una transmisión dirigida a nosotros, sino un radar de navegación cósmica o el barrido de un haz emisor rotatorio alienígena que barrió nuestro sistema solar durante poco más de un minuto antes de continuar su viaje hacia la inmensidad.",
                    "tituloVisual": "CENTELLEO O FARO ALIEN",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "espacio_profundo",
                    "transicion": "zoom_in",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["centelleo interestelar", "lente gravitacional", "radar de navegación", "haz rotatorio"],
                    "poseId": "thinking_chin_hand",
                    "expresion": "analytical",
                    "infografia": {
                        "tipo": "comparacion",
                        "titulo": "Modelos Teóricos",
                        "subtitulo": "Naturaleza de la Transmisión",
                        "valorPrincipal": "SETI",
                        "unidad": "candidato #1",
                        "items": [
                            {"etiqueta": "Faro interestelar rotatorio", "valor": "Haz periódico amplio", "porcentaje": 80, "color": "#FFE600"},
                            {"etiqueta": "Centelleo de plasma", "valor": "Amplificación fugaz", "porcentaje": 65, "color": "#38BDF8"}
                        ],
                        "colorAcento": "#FFE600"
                    }
                }
            ]
        },
        {
            "id": "cap_6",
            "numero": 6,
            "titulo": "El Eco de una Pregunta Abierta",
            "resumen": "La herencia del mensaje y nuestro lugar solitario en la galaxia.",
            "escenas": [
                {
                    "id": 11,
                    "texto": "Casi medio siglo después, la señal Wow permanece como el candidato más sólido y desconcertante de contacto tecnológico de toda la historia humana. En el año dos mil doce, en el trigésimo quinto aniversario del evento, la humanidad envió una respuesta desde el radiotelescopio de Arecibo: una transmisión compuesta por más de diez mil mensajes de texto y videos de ciudadanos de todo el planeta hacia las coordenadas exactas de donde provino el pulso. Esa respuesta tardará siglos en llegar a su destino, si es que alguna vez alguien está allí para escucharla.",
                    "tituloVisual": "RESPUESTA DESDE ARECIBO",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "espacio_profundo",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["medio siglo", "trigésimo quinto aniversario", "diez mil mensajes", "respuesta terrestre"],
                    "poseId": "standing_curious",
                    "expresion": "hopeful"
                },
                {
                    "id": 12,
                    "texto": "Aquella hoja de papel continuo con el círculo rojo de Jerry Ehman descansa hoy en los archivos históricos como un recordatorio poético de nuestra fragilidad. Tal vez fuimos testigos involuntarios del saludo de una civilización lejana que ya no existe, o tal vez el universo nos mostró una anomalía natural que aún no comprendemos. Pero cada vez que miramos hacia la constelación de Sagitario en una noche clara, sabemos que durante setenta y dos segundos de mil novecientos setenta y siete, la Tierra no estuvo del todo sola.",
                    "tituloVisual": "SETENTA Y DOS SEGUNDOS",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "habitacion_noche",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["círculo rojo", "constelación de Sagitario", "setenta y dos segundos", "no estuvimos solos"],
                    "poseId": "explaining_both_hands",
                    "expresion": "smile_wide"
                }
            ]
        }
    ]
    actualizar_guion("004", capitulos)


def construir_doc_005():
    capitulos = [
        {
            "id": "cap_1",
            "numero": 1,
            "titulo": "El Almuerzo de Los Álamos",
            "resumen": "El verano de 1950 y la pregunta desconcertante de Enrico Fermi.",
            "escenas": [
                {
                    "id": 1,
                    "texto": "En el verano de mil novecientos cincuenta, cuatro de las mentes científicas más brillantes del siglo veinte caminaban hacia el comedor del laboratorio nuclear de Los Álamos. Enrico Fermi, Edward Teller, Herbert York y Emil Konopinski charlaban animadamente sobre ovnis y una caricatura del New Yorker que culpaba a los extraterrestres por la misteriosa desaparición de botes de basura en Nueva York. Tras sentarse a comer y cambiar de tema durante varios minutos, Fermi exclamó de pronto con voz atronadora: Pero, ¿dónde están todos? Sus colegas rompieron a reír, pero comprendieron de inmediato la profunda paradoja matemática que el físico de origen italiano acababa de plantear.",
                    "tituloVisual": "LOS ALAMOS, 1950",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "laboratorio",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["mil novecientos cincuenta", "Enrico Fermi", "Los Álamos", "dónde están todos"],
                    "poseId": "explaining_both_hands",
                    "expresion": "eureka"
                },
                {
                    "id": 2,
                    "texto": "El razonamiento de Fermi era implacable: nuestra galaxia tiene más de cien mil millones de estrellas y alrededor de trece mil millones de años de antigüedad. El Sol es una estrella relativamente joven en comparación. Si solo una fracción ínfima de esos planetas albergara vida y desarrollara viajes espaciales a velocidades sublumínicas modestas, una sola civilización podría colonizar toda la Vía Láctea en apenas unos pocos millones de años. La paradoja radica en la aterradora contradicción entre la altísima probabilidad matemática de vida inteligente en el cosmos y la absoluta falta de evidencia física.",
                    "tituloVisual": "LA PARADOJA MATEMATICA",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "espacio_profundo",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["cien mil millones de estrellas", "trece mil millones de años", "colonización galáctica", "probabilidad matemática"],
                    "poseId": "thinking_chin_hand",
                    "expresion": "analytical",
                    "infografia": {
                        "tipo": "dato_clave",
                        "titulo": "Escala Temporal Galáctica",
                        "subtitulo": "Tiempo para Colonizar la Galaxia",
                        "valorPrincipal": "10M",
                        "unidad": "años",
                        "items": [
                            {"etiqueta": "Edad de la Galaxia", "valor": "13.600 millones de años", "porcentaje": 100, "color": "#38BDF8"},
                            {"etiqueta": "Expansión estelar lenta", "valor": "10 a 50 millones de años", "porcentaje": 5, "color": "#FFE600"}
                        ],
                        "colorAcento": "#FFE600"
                    }
                }
            ]
        },
        {
            "id": "cap_2",
            "numero": 2,
            "titulo": "La Ecuación de Frank Drake",
            "resumen": "El intento de cuantificar civilizaciones comunicativas en la galaxia.",
            "escenas": [
                {
                    "id": 3,
                    "texto": "Once años después del almuerzo de Fermi, el astrónomo Frank Drake formuló una ecuación probabilística para estimar el número de civilizaciones en la Vía Láctea capaces de emitir señales de radio. Multiplicando la tasa de formación de estrellas, la fracción de astros con planetas, los mundos habitables, y la probabilidad de que surja vida, inteligencia y tecnología, los cálculos más conservadores arrojaban decenas de miles de civilizaciones activas en este preciso momento. Si la galaxia es un hervidero cósmico con miles de millones de años de ventaja sobre nosotros, los cielos deberían estar saturados de transmisiones, faros térmicos y megaconstrucciones.",
                    "tituloVisual": "ECUACION DE DRAKE",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "laboratorio",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_sci_fi_beep.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["Frank Drake", "ecuación probabilística", "civilizaciones activas", "megaconstrucciones"],
                    "poseId": "holding_presentation_board",
                    "expresion": "analytical",
                    "infografia": {
                        "tipo": "tarjeta_concepto",
                        "titulo": "Variables de Drake",
                        "subtitulo": "Factores de Supervivencia Tecnológica",
                        "valorPrincipal": "N",
                        "unidad": "civilizaciones",
                        "items": [
                            {"etiqueta": "Planetas habitables", "valor": "Miles de millones", "porcentaje": 90, "color": "#38BDF8"},
                            {"etiqueta": "Vida tecnológica", "valor": "Factor L (Duración)", "porcentaje": 30, "color": "#FFE600"}
                        ],
                        "colorAcento": "#38BDF8"
                    }
                },
                {
                    "id": 4,
                    "texto": "Sin embargo, cada vez que miramos hacia el abismo con nuestros radiotelescopios más avanzados, solo encontramos el siseo monótono de la radiación cósmica de fondo. Este abrumador mutismo se conoce en astrofísica como el Gran Silencio. No detectamos señales de radio extraterrestres, no vemos naves exploradoras autorreplicantes, ni encontramos esferas de Dyson recolectando la energía de soles lejanos. El universo observable se comporta como un desierto biológico donde la Tierra parece ser el único faro encendido.",
                    "tituloVisual": "EL GRAN SILENCIO",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "espacio_profundo",
                    "transicion": "zoom_in",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["Gran Silencio", "radiación de fondo", "esferas de Dyson", "desierto biológico"],
                    "poseId": "astronomy_telescope",
                    "expresion": "confused"
                }
            ]
        },
        {
            "id": "cap_3",
            "numero": 3,
            "titulo": "El Gran Filtro: La Barrera Mortal",
            "resumen": "La hipótesis evolutiva de Robin Hanson y el dilema de nuestra supervivencia.",
            "escenas": [
                {
                    "id": 5,
                    "texto": "En mil novecientos noventa y seis, el economista y filósofo Robin Hanson propuso una respuesta aterradora para reconciliar la paradoja: la teoría del Gran Filtro. Hanson argumentó que en el largo camino evolutivo que va desde la química prebiótica elemental hasta una especie interestelar capaz de colonizar la galaxia, existe al menos una barrera casi insuperable, un cuello de botella evolutivo o tecnológico tan brutal que extermina a casi la totalidad de las especies antes de que puedan dejar una huella visible en el cosmos.",
                    "tituloVisual": "EL GRAN FILTRO",
                    "layout": "split_screen",
                    "composicionVisual": "plano_general",
                    "escenario": "espacio_profundo",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["Robin Hanson", "Gran Filtro", "barrera insuperable", "cuello de botella"],
                    "poseId": "thinking_chin_hand",
                    "expresion": "analytical"
                },
                {
                    "id": 6,
                    "texto": "La cuestión existencial decisiva es: ¿dónde se encuentra ese filtro? Si el Gran Filtro está detrás de nosotros, significa que el paso más improbable ya ocurrió: tal vez el origen de la vida celular, la invención de la fotosíntesis o la aparición de la inteligencia reflexiva son anomalías astronómicas irrepetibles, lo que nos convertiría en la primera o única especie inteligente de la galaxia. Pero si el Gran Filtro está por delante de nosotros, aguardándonos en el futuro, significa que casi todas las especies se autodestruyen al alcanzar el poder tecnológico.",
                    "tituloVisual": "¿DETRAS O DELANTE?",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "laboratorio",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["detrás de nosotros", "delante en el futuro", "origen de la vida", "autodestrucción"],
                    "poseId": "explaining_pointing_up",
                    "expresion": "shocked",
                    "infografia": {
                        "tipo": "comparacion",
                        "titulo": "Ubicación del Filtro",
                        "subtitulo": "Implicaciones para la Humanidad",
                        "valorPrincipal": "Destino",
                        "unidad": "evolutivo",
                        "items": [
                            {"etiqueta": "Filtro en el pasado", "valor": "Somos únicos y afortunados", "porcentaje": 100, "color": "#38BDF8"},
                            {"etiqueta": "Filtro en el futuro", "valor": "Extinción casi segura", "porcentaje": 10, "color": "#FFE600"}
                        ],
                        "colorAcento": "#FFE600"
                    }
                }
            ]
        },
        {
            "id": "cap_4",
            "numero": 4,
            "titulo": "La Hipótesis del Bosque Oscuro",
            "resumen": "El silencio cósmico como estrategia militar de supervivencia.",
            "escenas": [
                {
                    "id": 7,
                    "texto": "Existe una interpretación aún más escalofriante popularizada por el escritor de ciencia ficción Liu Cixin: la teoría del Bosque Oscuro. Imagina el universo como un bosque cerrado durante la noche, donde innumerables cazadores armados caminan en silencio entre los árboles. Cada civilización es un cazador que no sabe si los demás son pacíficos o letales. La velocidad de la luz impone una brecha de comunicación insalvable y el crecimiento tecnológico exponencial hace que cualquier vecino atrasado pueda convertirse mañana en una amenaza mortal.",
                    "tituloVisual": "EL BOSQUE OSCURO",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "habitacion_noche",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["Liu Cixin", "Bosque Oscuro", "cazadores armados", "brecha de comunicación"],
                    "poseId": "thinking_chin_hand",
                    "expresion": "fear"
                },
                {
                    "id": 8,
                    "texto": "Bajo las reglas implacables de la teoría de juegos del Bosque Oscuro, la conducta más racional para cualquier sociedad avanzada no es emitir saludos al cosmos, sino mantener el silencio radiofónico más absoluto. Revelar tu posición en el cielo equivale a encender una antorcha en medio de la niebla: el primer cazador que te detecte disparará por precaución para garantizar su propia supervivencia. Desde esta perspectiva, la razón por la que el cielo está mudo no es que esté vacío, sino que todas las civilizaciones adultas se esconden aterradas.",
                    "tituloVisual": "SILENCIO COMO ESCUDO",
                    "layout": "split_screen",
                    "composicionVisual": "plano_medio",
                    "escenario": "espacio_profundo",
                    "transicion": "whip_left",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["teoría de juegos", "silencio radiofónico", "antorcha en la niebla", "supervivencia"],
                    "poseId": "explaining_both_hands",
                    "expresion": "analytical"
                }
            ]
        },
        {
            "id": "cap_5",
            "numero": 5,
            "titulo": "El Zoológico Cósmico y la Brecha Temporal",
            "resumen": "Aislamiento deliberado o desajuste de civilizaciones en el tiempo.",
            "escenas": [
                {
                    "id": 9,
                    "texto": "Otras hipótesis plantean escenarios menos bélicos pero igualmente intrigantes. La Hipótesis del Zoológico, propuesta por John Ball en mil novecientos setenta y tres, sugiere que entidades alienígenas inmensamente superiores nos observan desde la distancia sin intervenir, tratándonos como una reserva natural protegida para permitir nuestro desarrollo cultural orgánico, tal como los humanos observamos a las tribus no contactadas en las profundidades del Amazonas.",
                    "tituloVisual": "LA RESERVA NATURAL",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "espacio_profundo",
                    "transicion": "zoom_in",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_sci_fi_beep.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["John Ball", "Hipótesis del Zoológico", "reserva natural", "tribus no contactadas"],
                    "poseId": "standing_curious",
                    "expresion": "talking"
                },
                {
                    "id": 10,
                    "texto": "A esto se suma la abrumadora brecha temporal. Nuestra especie apenas lleva un siglo emitiendo señales electromagnéticas al espacio, una cáscara esférica de solo cien años luz en una galaxia de cien mil años luz de diámetro. En términos cósmicos, somos una chispa efímera de milisegundos. Dos civilizaciones podrían haber florecido, construido imperios majestuosos y desaparecido en el mismo sector galáctico, separadas simplemente por una ventana temporal de cincuenta millones de años sin llegar a coincidir jamás.",
                    "tituloVisual": "DESAJUSTE TEMPORAL",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "laboratorio",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["un siglo de radio", "cien años luz", "chispa efímera", "desajuste temporal"],
                    "poseId": "explaining_pointing_up",
                    "expresion": "analytical",
                    "infografia": {
                        "tipo": "dato_clave",
                        "titulo": "La Burbuja Humana",
                        "subtitulo": "Alcance de Nuestras Señales de Radio",
                        "valorPrincipal": "100",
                        "unidad": "años luz",
                        "items": [
                            {"etiqueta": "Burbuja de radio humana", "valor": "100 años luz", "porcentaje": 0.1, "color": "#FFE600"},
                            {"etiqueta": "Diámetro de la Vía Láctea", "valor": "100.000 años luz", "porcentaje": 100, "color": "#38BDF8"}
                        ],
                        "colorAcento": "#FFE600"
                    }
                }
            ]
        },
        {
            "id": "cap_6",
            "numero": 6,
            "titulo": "La Soledad como Responsabilidad",
            "resumen": "El valor supremo de la conciencia humana en un universo silencioso.",
            "escenas": [
                {
                    "id": 11,
                    "texto": "El filósofo Nick Bostrom advertía que el mayor temor que deberíamos tener al explorar Marte o las lunas heladas de Júpiter es encontrar fósiles de vida compleja. Si descubrimos que la vida compleja surge con facilidad en cualquier charco cósmico, la conclusión lógica e implacable sería que el Gran Filtro no está en el pasado, sino en nuestro futuro inmediato: nos aguarda a la vuelta de la esquina con el colapso ecológico, la inteligencia artificial descontrolada o el armamento de destrucción masiva.",
                    "tituloVisual": "LA ADVERTENCIA DE BOSTROM",
                    "layout": "split_screen",
                    "composicionVisual": "plano_general",
                    "escenario": "superficie_marte",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["Nick Bostrom", "fósiles en Marte", "vida compleja", "armas de destrucción"],
                    "poseId": "thinking_chin_hand",
                    "expresion": "sad"
                },
                {
                    "id": 12,
                    "texto": "Como decía Arthur C. Clarke, solo existen dos posibilidades: o estamos solos en el universo, o no lo estamos; ambas son igualmente aterradoras. Si estamos solos, la Tierra no es un planeta más, sino el único santuario donde la materia inerte logró abrir los ojos y comprenderse a sí misma. La ausencia de respuestas en el firmamento no debe sumirnos en la desesperanza, sino inspirarnos una reverencia infinita: la llama de la conciencia es extraordinariamente frágil, y cuidarla es la única misión sagrada de nuestra especie.",
                    "tituloVisual": "EL SANTUARIO CONSCIENTE",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "espacio_profundo",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["Arthur C. Clarke", "materia inerte", "llama de la conciencia", "misión sagrada"],
                    "poseId": "explaining_both_hands",
                    "expresion": "smile_wide"
                }
            ]
        }
    ]
    actualizar_guion("005", capitulos)


def construir_doc_006():
    capitulos = [
        {
            "id": "cap_1",
            "numero": 1,
            "titulo": "La Fiebre Geológica de la Guerra Fría",
            "resumen": "La carrera secreta hacia el centro de la Tierra en la península de Kola.",
            "escenas": [
                {
                    "id": 1,
                    "texto": "Durante el apogeo de la Guerra Fría, la atención del mundo entero estaba hipnotizada por la carrera espacial: satélites en órbita, misiones lunares y sondas rumbo a Venus. Pero bajo el suelo helado de la península de Kola, cerca de la frontera soviética con Noruega, se libraba una batalla científica mucho más silenciosa y brutal: la carrera hacia el interior de nuestro propio planeta. En mayo de mil novecientos setenta, geólogos soviéticos armados con la colosal torre de perforación Uralmash montaron una operación monumental con un único objetivo: perforar la corteza continental terrestre hasta alcanzar el manto superior.",
                    "tituloVisual": "PENINSULA DE KOLA, 1970",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "habitacion_noche",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["Guerra Fría", "península de Kola", "Uralmash", "manto superior"],
                    "poseId": "walking_confidently",
                    "expresion": "analytical"
                },
                {
                    "id": 2,
                    "texto": "Sabemos más sobre la superficie de la Luna o los valles de Marte que sobre lo que yace a apenas veinte kilómetros bajo nuestros propios pies. El proyecto del Pozo Superprofundo de Kola, conocido formalmente como SG-3, no buscaba petróleo ni gas natural; era un experimento de ciencia pura concebido para comprobar si los modelos teóricos sobre las capas internas de la Tierra eran correctos. La Unión Soviética prometió descender hasta los quince mil metros de profundidad, desafiando presiones aplastantes y temperaturas que desafiaban la resistencia de cualquier aleación metálica conocida.",
                    "tituloVisual": "PROYECTO SG-3",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "laboratorio",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["veinte kilómetros", "proyecto SG-3", "quince mil metros", "aleación metálica"],
                    "poseId": "holding_presentation_board",
                    "expresion": "talking",
                    "infografia": {
                        "tipo": "dato_clave",
                        "titulo": "Objetivo de Profundidad",
                        "subtitulo": "La Perforación más Profunda de la Historia",
                        "valorPrincipal": "15.000",
                        "unidad": "metros objetivo",
                        "items": [
                            {"etiqueta": "Récord alcanzado", "valor": "12.262 metros", "porcentaje": 82, "color": "#FFE600"},
                            {"etiqueta": "Fosa de las Marianas", "valor": "10.994 metros", "porcentaje": 73, "color": "#38BDF8"}
                        ],
                        "colorAcento": "#FFE600"
                    }
                }
            ]
        },
        {
            "id": "cap_2",
            "numero": 2,
            "titulo": "El Taladro que Conquistó el Abismo",
            "resumen": "La ingeniería extrema de la broca y el peso de doce kilómetros de tubería.",
            "escenas": [
                {
                    "id": 3,
                    "texto": "Para penetrar kilómetros de granito compacto, los ingenieros tuvieron que reinventar la tecnología de perforación desde cero. En un pozo convencional, todo el tubo gira desde la superficie; pero a miles de metros, el peso y la fricción de doce kilómetros de acero habrían retorcido la tubería como un fideo húmedo. Diseñaron entonces una turbina especial en la que solo giraba la cabeza de perforación, impulsada por un flujo continuo de lodo a alta presión inyectado desde la superficie. A lo largo de dos décadas se desgastaron miles de cabezales de carburo de tungsteno y diamante.",
                    "tituloVisual": "TURBINA DE LODO",
                    "layout": "split_screen",
                    "composicionVisual": "plano_general",
                    "escenario": "red_subterranea",
                    "transicion": "zoom_in",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_impact.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["carburo de tungsteno", "diamante", "turbina de lodo", "acero retorcido"],
                    "poseId": "thinking_chin_hand",
                    "expresion": "analytical"
                },
                {
                    "id": 4,
                    "texto": "Cambiar una sola broca desgastada requería una labor titánica: había que desacoplar y sacar los doce kilómetros de tubería de perforación, sección por sección, reemplazar la punta en la superficie y volver a ensamblar los cientos de tubos hacia el fondo. Cada recambio tardaba días enteros de trabajo ininterrumpido en turnos de veinticuatro horas. Pese a los constantes derrumbes y atascos mecánicos que obligaron a ramificar el pozo en varias ocasiones, en mil novecientos ochenta y nueve la perforación alcanzó los doce mil doscientos sesenta y dos metros de profundidad vertical.",
                    "tituloVisual": "12.262 METROS",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "red_subterranea",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["doce kilómetros de tubería", "sección por sección", "veinticuatro horas", "doce mil doscientos sesenta y dos"],
                    "poseId": "explaining_both_hands",
                    "expresion": "eureka"
                }
            ]
        },
        {
            "id": "cap_3",
            "numero": 3,
            "titulo": "Las Sorpresas Científicas Bajo la Roca",
            "resumen": "El agua fósil a altísima presión y la ausencia de la transición de Conrad.",
            "escenas": [
                {
                    "id": 5,
                    "texto": "A medida que el pozo descendía, los descubrimientos hicieron pedazos los libros de texto de geología de la época. Todos los científicos esperaban encontrar la llamada discontinuidad de Conrad, una supuesta frontera sísmica donde el granito superficial daría paso a una densa capa de basalto. Para sorpresa de todos, el basalto jamás apareció: la roca continuó siendo granito metamórfico hasta el final. La señal sísmica que los geofísicos interpretaban como un cambio de roca era en realidad un cambio en la porosidad y fractura del propio granito bajo presiones descomunales.",
                    "tituloVisual": "EL MITO DEL BASALTO",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "laboratorio",
                    "transicion": "whip_left",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["discontinuidad de Conrad", "granito metamórfico", "basalto inexistente", "porosidad de la roca"],
                    "poseId": "explaining_pointing_up",
                    "expresion": "analytical",
                    "infografia": {
                        "tipo": "comparacion",
                        "titulo": "Estructura de la Corteza",
                        "subtitulo": "Teoría Previa vs Hallazgo Real de Kola",
                        "valorPrincipal": "Granito",
                        "unidad": "continuo",
                        "items": [
                            {"etiqueta": "Predicción teórica", "valor": "Capa de Basalto a 7 km", "porcentaje": 40, "color": "#94A3B8"},
                            {"etiqueta": "Descubrimiento en Kola", "valor": "Granito fracturado con agua", "porcentaje": 100, "color": "#38BDF8"}
                        ],
                        "colorAcento": "#38BDF8"
                    }
                },
                {
                    "id": 6,
                    "texto": "Pero el hallazgo más desconcertante fue encontrar agua líquida libre a más de siete kilómetros de profundidad. La teoría convencional afirmaba que a esas profundidades la roca estaría tan compactada por el peso superior que los poros se sellarían herméticamente. Sin embargo, el agua estaba allí, atrapada en fracturas microscópicas a presiones sobrehumanas. No provenía de la superficie: era agua juvenil que se había originado a partir de átomos de hidrógeno y oxígeno expulsados de los propios minerales y que no tenía forma de escapar a través de la corteza impermeable.",
                    "tituloVisual": "AGUA FOSIL PROFUNDA",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "red_subterranea",
                    "transicion": "zoom_in",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_sci_fi_beep.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["siete kilómetros", "agua juvenil", "fracturas microscópicas", "minerales hidratados"],
                    "poseId": "thinking_chin_hand",
                    "expresion": "eureka"
                }
            ]
        },
        {
            "id": "cap_4",
            "numero": 4,
            "titulo": "La Fósiles Microscópicos y el Muro Térmico",
            "resumen": "Microfósiles a seis kilómetros y el calor que derritió el acero.",
            "escenas": [
                {
                    "id": 7,
                    "texto": "A seis mil metros bajo la superficie, los geólogos extrajeron núcleos de roca que contenían microfósiles microscópicos de plancton unicelular intacto que databan de más de dos mil millones de años de antigüedad. Aquellas células primordiales habían sobrevivido a eras de presión geológica extrema envueltas en una matriz mineral protectora, revelando que la biosfera arcaica de la Tierra era mucho más resistente de lo que la ciencia imaginaba.",
                    "tituloVisual": "FOSILES DE 2000 MILLONES DE ANOS",
                    "layout": "split_screen",
                    "composicionVisual": "plano_medio",
                    "escenario": "laboratorio",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["microfósiles", "dos mil millones de años", "plancton unicelular", "biosfera arcaica"],
                    "poseId": "holding_presentation_board",
                    "expresion": "talking"
                },
                {
                    "id": 8,
                    "texto": "Sin embargo, al superar los diez kilómetros de profundidad, el pozo colisionó contra un muro infranqueable: el gradiente térmico de la Tierra. Los modelos geológicos pronosticaban que a doce kilómetros la temperatura rondaría los cien grados centígrados, un calor manejable. Pero la realidad térmica fue abrasadora: el termómetro marcó ciento ochenta grados centígrados, casi el doble de lo esperado. A esa temperatura y bajo presiones de miles de atmósferas, la roca de granito dejó de comportarse como un sólido rígido y comenzó a fluir como cera plástica.",
                    "tituloVisual": "EL MURO DE 180 GRADOS",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "red_subterranea",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["gradiente térmico", "ciento ochenta grados", "roca plástica", "presión de miles de atmósferas"],
                    "poseId": "confused_scratch_head",
                    "expresion": "sad",
                    "infografia": {
                        "tipo": "dato_clave",
                        "titulo": "Temperatura Infernal",
                        "subtitulo": "Discrepancia a 12 km de Profundidad",
                        "valorPrincipal": "180°C",
                        "unidad": "en el fondo",
                        "items": [
                            {"etiqueta": "Temperatura real medida", "valor": "180 grados centígrados", "porcentaje": 100, "color": "#FFE600"},
                            {"etiqueta": "Temperatura prevista", "valor": "100 grados centígrados", "porcentaje": 55, "color": "#38BDF8"}
                        ],
                        "colorAcento": "#FFE600"
                    }
                }
            ]
        },
        {
            "id": "cap_5",
            "numero": 5,
            "titulo": "El Mito Urbano del Pozo al Infierno",
            "resumen": "La leyenda de las grabaciones de voces y su origen mediático.",
            "escenas": [
                {
                    "id": 9,
                    "texto": "A finales de los años ochenta nació una de las leyendas urbanas más famosas de la historia de Internet: el supuesto Pozo al Infierno de Siberia. Según el bulo, los científicos soviéticos habían perforado una caverna hueca a catorce kilómetros, y al bajar un micrófono resistente al calor para registrar el movimiento de las placas tectónicas, escucharon grabaciones aterradoras con los gritos desgarradores de millones de almas atormentadas en el inframundo, provocando que los ingenieros huyeran despavoridos.",
                    "tituloVisual": "LA LEYENDA DEL INFIERNO",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "habitacion_noche",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["pozo al infierno", "gritos desgarradores", "bulo de Internet", "micrófono térmico"],
                    "poseId": "standing_curious",
                    "expresion": "fear"
                },
                {
                    "id": 10,
                    "texto": "La historia era una falsedad absoluta originada en una cadena de radio religiosa estadounidense que tomó en serio una broma de un boletín escolar finlandés. El audio no era más que un montaje cutre mezclando sonidos de la película de terror Baron Blood en bucle. En la realidad física de Kola no había cavernas huecas ni demonios: a doce kilómetros la presión geológica es tan gigantesca que cualquier cavidad se colapsaría de inmediato. El único sonido en el abismo era el siseo del lodo caliente y el crujido metálico de las brocas rompiéndose.",
                    "tituloVisual": "DESMONTANDO EL BACTERO",
                    "layout": "split_screen",
                    "composicionVisual": "plano_medio",
                    "escenario": "laboratorio",
                    "transicion": "whip_left",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["falsedad absoluta", "broma finlandesa", "montaje de audio", "sin cavernas huecas"],
                    "poseId": "explaining_both_hands",
                    "expresion": "analytical"
                }
            ]
        },
        {
            "id": "cap_6",
            "numero": 6,
            "titulo": "La Tapa Oxidada y el Legado de Kola",
            "resumen": "El cierre del proyecto en 1992 y nuestra visión de la Tierra.",
            "escenas": [
                {
                    "id": 11,
                    "texto": "En mil novecientos noventa y dos, tras el colapso de la Unión Soviética y ante la imposibilidad técnica de avanzar por las temperaturas sofocantes que derretían las brocas y cerraban el pozo cada vez que se retiraba la tubería, los trabajos se detuvieron definitivamente en los doce mil doscientos sesenta y dos metros. En dos mil ocho las instalaciones fueron abandonadas y desmanteladas. Hoy en día, la perforación más profunda jamás excavada por la especie humana está sellada con una modesta tapa circular de acero oxidado sujeta con doce pernos.",
                    "tituloVisual": "UNA TAPA DE DOCE PERNOS",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "habitacion_noche",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["colapso soviético", "doce mil doscientos sesenta y dos", "tapa de acero oxidado", "doce pernos"],
                    "poseId": "reading_clipboard",
                    "expresion": "sad"
                },
                {
                    "id": 12,
                    "texto": "Si la Tierra tuviera el tamaño de una manzana estándar, la impresionante perforación del pozo de Kola de doce kilómetros de profundidad ni siquiera habría logrado atravesar la delgada piel exterior de la fruta. Apenas rasgamos un tercio de la corteza continental. Pero las miles de muestras de roca extraídas continúan en los museos geológicos como un monumento a la curiosidad humana: el recordatorio indiscutible de que el mundo bajo nuestros pies es tan insondable, ardiente y misterioso como las profundidades del espacio sideral.",
                    "tituloVisual": "LA PIEL DE LA MANZANA",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "laboratorio",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["piel de la manzana", "un tercio de la corteza", "muestras geológicas", "curiosidad humana"],
                    "poseId": "explaining_both_hands",
                    "expresion": "smile_wide"
                }
            ]
        }
    ]
    actualizar_guion("006", capitulos)


def construir_doc_007():
    capitulos = [
        {
            "id": "cap_1",
            "numero": 1,
            "titulo": "El Punto Más Solitario del Planeta",
            "resumen": "La definición del Polo Oceánico de Inaccesibilidad y su lejanía cósmica.",
            "escenas": [
                {
                    "id": 1,
                    "texto": "En medio del Pacífico Sur, sepultado en una inmensidad de agua que parece infinita, existe una coordenada geográfica que ostenta el título del lugar más aislado de la superficie de la Tierra: el Polo Oceánico de Inaccesibilidad, bautizado popularmente como Punto Nemo en honor al legendario capitán de Julio Verne. Para llegar a tierra firme desde este punto exacto hay que navegar dos mil seiscientos ochenta y ocho kilómetros en cualquier dirección: hacia el norte se encuentra la deshabitada isla Ducie, al noreste el islote Motu Nui de la Isla de Pascua, y hacia el sur las costas heladas de la Antártida.",
                    "tituloVisual": "PUNTO NEMO",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "abismo_oceanico",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["Punto Nemo", "Polo Oceánico de Inaccesibilidad", "dos mil seiscientos ochenta y ocho kilómetros", "Pacífico Sur"],
                    "poseId": "standing_curious",
                    "expresion": "analytical"
                },
                {
                    "id": 2,
                    "texto": "La soledad de Punto Nemo es tan abrumadora que produce una paradoja espacial asombrosa: los seres humanos más cercanos a ti cuando navegas por esas coordenadas no están en un barco ni en una isla de pescadores; son los astronautas a bordo de la Estación Espacial Internacional. Mientras la costa más próxima dista casi dos mil setecientos kilómetros, la estación espacial orbita a cuatrocientos kilómetros directamente sobre tu cabeza. Si miras hacia el cenit en una noche despejada, estás siete veces más cerca del espacio exterior que de cualquier civilización humana terrestre.",
                    "tituloVisual": "VECINOS EN ORBITA",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "espacio_profundo",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_sci_fi_beep.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["Estación Espacial Internacional", "cuatrocientos kilómetros", "siete veces más cerca", "astronautas"],
                    "poseId": "explaining_pointing_up",
                    "expresion": "eureka",
                    "infografia": {
                        "tipo": "comparacion",
                        "titulo": "Distancia a Humanos",
                        "subtitulo": "Costa más Cercana vs Estación Espacial",
                        "valorPrincipal": "400 km",
                        "unidad": "ISS en el cenit",
                        "items": [
                            {"etiqueta": "Estación Espacial (Cielo)", "valor": "400 km de distancia", "porcentaje": 15, "color": "#FFE600"},
                            {"etiqueta": "Isla Ducie (Tierra firme)", "valor": "2.688 km de distancia", "porcentaje": 100, "color": "#38BDF8"}
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
            "resumen": "El Giro del Pacífico Sur y la ausencia casi total de vida en las aguas.",
            "escenas": [
                {
                    "id": 3,
                    "texto": "Lejos de ser un vergel tropical repleto de peces y ballenas, Punto Nemo es en realidad un colosal desierto biológico oceánico. El área se encuentra situada justo en el corazón del Giro del Pacífico Sur, una gigantesca corriente marina circular que actúa como una barrera impenetrable: impide que las corrientes ricas en nutrientes de las costas sudamericanas y antárticas penetren en su interior. Sin corrientes de surgencia que eleven minerales desde el fondo, el agua permanece en una calma cristalina y estéril.",
                    "tituloVisual": "EL GIRO DEL PACIFICO",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "abismo_oceanico",
                    "transicion": "zoom_in",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["Giro del Pacífico Sur", "desierto biológico", "nutrientes minerales", "calma estéril"],
                    "poseId": "walking_confidently",
                    "expresion": "analytical"
                },
                {
                    "id": 4,
                    "texto": "Al estar tan desconectado de los continentes, el polvo de tierra acarreado por el viento apenas llega a esta región, privando al mar de hierro y fósforo, los fertilizantes químicos esenciales para el fitoplancton. Sin fitoplancton no hay algas, sin algas no hay krill, y sin krill los bancos de peces y los mamíferos marinos no pueden sobrevivir. Las aguas de Punto Nemo poseen una de las biomasas más bajas del planeta; solo sobrevive un puñado de bacterias especializadas y extraños cangrejos en respiraderos hidrotermales a cuatro mil metros de profundidad.",
                    "tituloVisual": "AGUAS HIPO-TROFICAS",
                    "layout": "split_screen",
                    "composicionVisual": "plano_medio",
                    "escenario": "abismo_oceanico",
                    "transicion": "whip_left",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_impact.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["fitoplancton", "polvo de tierra", "biomasa mínima", "cuatro mil metros"],
                    "poseId": "thinking_chin_hand",
                    "expresion": "talking"
                }
            ]
        },
        {
            "id": "cap_3",
            "numero": 3,
            "titulo": "El Cementerio Oficial de Naves Espaciales",
            "resumen": "Por qué las agencias espaciales eligen Punto Nemo como basurero orbital.",
            "escenas": [
                {
                    "id": 5,
                    "texto": "Es precisamente esta combinación de aislamiento geográfico absoluto, ausencia de rutas comerciales marítimas y escasez de vida marina lo que convirtió a Punto Nemo en el destino predilecto de las agencias espaciales de todo el planeta: la NASA, Roscosmos, la Agencia Espacial Europea y la JAXA japonesa. Es el cementerio espacial oficial del mundo. Cuando un satélite de gran tonelaje o una estación espacial concluye su vida útil, no se puede dejar en órbita a la deriva ni permitir que caiga de forma descontrolada sobre una ciudad.",
                    "tituloVisual": "BASURERO ORBITAL",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "espacio_profundo",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["cementerio espacial", "NASA y Roscosmos", "satélites desorbitados", "desecho seguro"],
                    "poseId": "explaining_both_hands",
                    "expresion": "analytical"
                },
                {
                    "id": 6,
                    "texto": "Mediante una maniobra de retrofrenado de precisión milimétrica, los ingenieros en tierra encienden los motores de la nave para reducir su velocidad orbital y dirigir su reentrada destructiva directamente hacia la caja oceánica de Punto Nemo. Al penetrar la atmósfera a más de veintisiete mil kilómetros por hora, la fricción y el plasma desintegran el noventa por ciento de la estructura; sin embargo, componentes densos de titanio, tanques de combustible de acero inoxidable y toberas de motor resisten la fundición y caen como proyectiles al agua.",
                    "tituloVisual": "REENTRADA CONTROLADA",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "abismo_oceanico",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["retrofrenado", "veintisiete mil kilómetros por hora", "titanio y acero", "proyectiles al agua"],
                    "poseId": "explaining_pointing_up",
                    "expresion": "shocked",
                    "infografia": {
                        "tipo": "dato_clave",
                        "titulo": "Velocidad de Reentrada",
                        "subtitulo": "Desintegración Atmosférica Controlada",
                        "valorPrincipal": "27.000",
                        "unidad": "km/h",
                        "items": [
                            {"etiqueta": "Masa desintegrada", "valor": "80 a 90% en la atmósfera", "porcentaje": 85, "color": "#FFE600"},
                            {"etiqueta": "Restos en el lecho marino", "valor": "Titanio y motores densos", "porcentaje": 15, "color": "#38BDF8"}
                        ],
                        "colorAcento": "#FFE600"
                    }
                }
            ]
        },
        {
            "id": "cap_4",
            "numero": 4,
            "titulo": "Los Gigantes Caídos de la Carrera Espacial",
            "resumen": "La estación Mir, los cargueros Progress y más de 300 reliquias cósmicas.",
            "escenas": [
                {
                    "id": 7,
                    "texto": "Se calcula que en el lecho marino de Punto Nemo descansan los restos de más de trescientas naves espaciales acumuladas desde mil novecientos setenta y uno. El trofeo histórico más célebre de este cementerio es la legendaria estación espacial soviética Mir. En marzo de dos mil uno, tras quince años en órbita y decenas de récords cósmicos, la colosal mole de ciento cuarenta toneladas fue desorbitada de forma controlada. Una lluvia de fragmentos incandescentes cruzó el cielo del Pacífico como una lluvia de meteoros de fuego antes de sepultarse en el abismo.",
                    "tituloVisual": "LA CAIDA DE LA MIR",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "abismo_oceanico",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["estación Mir", "trescientas naves", "ciento cuarenta toneladas", "lluvia de meteoros"],
                    "poseId": "thinking_chin_hand",
                    "expresion": "sad"
                },
                {
                    "id": 8,
                    "texto": "Junto a la Mir reposan decenas de cargueros no tripulados rusos Progress, cápsulas automatizadas ATV de la Agencia Espacial Europea, cargueros japoneses HTV y fragmentos de cohetes de etapas superiores. Repartidos a lo largo de un corredor de escombros de más de mil kilómetros de longitud y sumergidos a cuatro mil metros bajo la superficie, estos esqueletos de alta tecnología forman el museo arqueológico más inaccesible y solitario de la civilización humana.",
                    "tituloVisual": "EL MUSEO SUBMARINO",
                    "layout": "split_screen",
                    "composicionVisual": "plano_medio",
                    "escenario": "abismo_oceanico",
                    "transicion": "whip_left",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["cargueros Progress", "módulos ATV", "cuatro mil metros bajo el agua", "museo arqueológico"],
                    "poseId": "holding_presentation_board",
                    "expresion": "talking"
                }
            ]
        },
        {
            "id": "cap_5",
            "numero": 5,
            "titulo": "El Destino Final de la ISS en 2031",
            "resumen": "El adiós a la mayor estructura jamás construida fuera de la Tierra.",
            "escenas": [
                {
                    "id": 9,
                    "texto": "El futuro de Punto Nemo ya tiene fecha para su acontecimiento más dramático: el final de la Estación Espacial Internacional. Con un peso que supera las cuatrocientas cincuenta toneladas y la envergadura de un campo de fútbol americano, la mayor maravilla de la ingeniería espacial no puede dejarse a la deriva cuando concluya sus operaciones en el año dos mil treinta y uno. La NASA y sus socios internacionales ya han diseñado el plan de descenso final.",
                    "tituloVisual": "ADIEU A LA ISS (2031)",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "espacio_profundo",
                    "transicion": "zoom_in",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_sci_fi_beep.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["Estación Espacial Internacional", "cuatrocientas cincuenta toneladas", "dos mil treinta y uno", "campo de fútbol"],
                    "poseId": "explaining_both_hands",
                    "expresion": "analytical"
                },
                {
                    "id": 10,
                    "texto": "Un remolcador espacial especialmente diseñado empujará a la estación hacia la atmósfera superior en un ángulo de descenso calculado al milímetro. Los paneles solares se quebrarán en segundos, los módulos presurizados explotarán por descompresión térmica y decenas de toneladas de chatarra espacial fundida se precipitarán sobre Punto Nemo. Cuando la estación se sumerja para siempre en las profundidades gélidas, se cerrará el capítulo más brillante de la exploración espacial de nuestra era.",
                    "tituloVisual": "EL CLIMAX ACUATICO",
                    "layout": "infografia_derecha",
                    "composicionVisual": "plano_medio",
                    "escenario": "abismo_oceanico",
                    "transicion": "whip_right",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["remolcador espacial", "paneles solares", "chatarra espacial fundida", "profundidades gélidas"],
                    "poseId": "explaining_pointing_up",
                    "expresion": "sad",
                    "infografia": {
                        "tipo": "dato_clave",
                        "titulo": "La Mayor Reentrada",
                        "subtitulo": "Masa de la Estación Espacial Internacional",
                        "valorPrincipal": "450t",
                        "unidad": "en 2031",
                        "items": [
                            {"etiqueta": "Masa ISS", "valor": "450 toneladas", "porcentaje": 100, "color": "#FFE600"},
                            {"etiqueta": "Masa Mir (2001)", "valor": "140 toneladas", "porcentaje": 31, "color": "#38BDF8"}
                        ],
                        "colorAcento": "#FFE600"
                    }
                }
            ]
        },
        {
            "id": "cap_6",
            "numero": 6,
            "titulo": "La Paradoja de Lovecraft y el Silencio Eterno",
            "resumen": "La cercanía ficticia de R'lyeh y la calma infinita del océano.",
            "escenas": [
                {
                    "id": 11,
                    "texto": "Por una fascinante coincidencia literaria, décadas antes de que los oceanógrafos calcularan las coordenadas de Punto Nemo con ordenadores en mil novecientos noventa y dos, el maestro del horror cósmico H. P. Lovecraft situó en mil novecientos veintiocho la mítica ciudad sumergida de R'lyeh a apenas unos cientos de kilómetros de este mismo punto exacto. El escritor eligió intuitivamente el rincón más aislado del mapa para ocultar la morada del monstruoso Cthulhu en las tinieblas abismales.",
                    "tituloVisual": "LA COINCIDENCIA DE R'LYEH",
                    "layout": "split_screen",
                    "composicionVisual": "plano_general",
                    "escenario": "abismo_oceanico",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_whoosh.wav",
                    "volumenSfx": 0.2,
                    "palabrasClave": ["Lovecraft", "R'lyeh", "horror cósmico", "mil novecientos veintiocho"],
                    "poseId": "thinking_chin_hand",
                    "expresion": "fear"
                },
                {
                    "id": 12,
                    "texto": "Punto Nemo es el punto de encuentro definitivo entre lo más avanzado de la conquista espacial humana y lo más primitivo e impenetrable de los océanos terrestres. Allí, bajo un manto de agua quieta donde jamás arriba barco alguno, las máquinas que tocaron las estrellas duermen su sueño eterno en la oscuridad, protegidas por una soledad que ningún ser humano en la Tierra podrá experimentar jamás.",
                    "tituloVisual": "EL SUEÑO ETERNO",
                    "layout": "panoramica_central",
                    "composicionVisual": "plano_general",
                    "escenario": "abismo_oceanico",
                    "transicion": "fundido_negro",
                    "efectosCamara": ["drift"],
                    "sfx": "sfx/sfx_dramatic_hit.wav",
                    "volumenSfx": 0.25,
                    "palabrasClave": ["conquista espacial", "máquinas que tocaron estrellas", "sueño eterno", "oscuridad abismal"],
                    "poseId": "explaining_both_hands",
                    "expresion": "smile_wide"
                }
            ]
        }
    ]
    actualizar_guion("007", capitulos)


if __name__ == "__main__":
    print("Redactando Lote 1 (004, 005, 006, 007)...")
    construir_doc_004()
    construir_doc_005()
    construir_doc_006()
    construir_doc_007()
    print("Lote 1 completado.")
