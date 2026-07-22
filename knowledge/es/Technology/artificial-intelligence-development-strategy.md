---
title: 'Desarrollo de la inteligencia artificial en Taiwán y estrategia futura: ya obtuvo el boleto de entrada del hardware, ¿dónde será la próxima batalla?'
description: 'El 8 de octubre de 2024, el Nobel de Física fue otorgado a Hopfield y Hinton; al día siguiente, el de Química fue para las tres personas detrás de AlphaFold. El 29 de mayo de ese mismo año, Jensen Huang comió omelet de ostras con Morris Chang en el mercado nocturno de Ningxia, en Taipéi. Taiwán fabrica el 90% de los servidores de IA del mundo y el 72% de las obleas avanzadas, pero estuvo ausente en las respuestas a 42 años de redes neuronales y a 50 años del problema del plegamiento de proteínas. Desde Taiwan AI Labs, de Ethan Tu, fundador de PTT, hasta TAIDE, el modelo LLM en chino tradicional por el que apuesta el Consejo Nacional de Ciencia y Tecnología, ¿le basta a esta isla con ser solo una fábrica de manufactura por encargo?'
date: 2026-03-19
author: 'Taiwan.md 編輯組'
category: 'Technology'
subcategory: '人工智慧'
tags:
  [
    'inteligencia artificial',
    'IA',
    'semiconductores',
    'política tecnológica',
    'transformación digital',
    'Premio Nobel',
    'AlphaFold',
  ]
readingTime: 18
lastVerified: 2026-05-19
lastHumanReview: true
featured: true
translatedFrom: 'Technology/台灣人工智慧發展與未來策略.md'
sourceCommitSha: '31a05c44'
sourceContentHash: 'sha256:ea05ddc3465f02eb'
sourceBodyHash: 'sha256:c1a908bbd971d40d'
translatedAt: '2026-06-16T16:54:57Z'
image: '/article-images/technology/alphafold-cbln1-structure-2025.webp'
imageCredit: 'BQUB25-UPoch (own work, AlphaFold + PyMOL)'
imageLicense: 'CC BY 4.0'
imageSource: 'https://commons.wikimedia.org/wiki/File:Estructura_tridimensional_de_la_prote%C3%AFna_CBLN1_per_AlphaFold_amb_codificaci%C3%B3_rainbow.png'
---

# Desarrollo de la inteligencia artificial en Taiwán y estrategia futura: ya obtuvo el boleto de entrada del hardware, ¿dónde será la próxima batalla?

> **Resumen en 30 segundos:** El 8 de octubre de 2024, el Premio Nobel de Física fue otorgado al físico que formuló la red de Hopfield y al científico cognitivo que desarrolló la retropropagación[^N1]. Al día siguiente, el 9 de octubre, el Premio Nobel de Química fue concedido a tres investigadores que usaron IA para resolver el problema del plegamiento de proteínas, pendiente desde hacía cincuenta años[^N2]. El 29 de mayo del mismo año, Jensen Huang, CEO de NVIDIA, apareció en el mercado nocturno de Ningxia, en Taipéi, comiendo omelet de ostras con Morris Chang, Barry Lam y Rick Tsai. TSMC obtuvo el 72% de los ingresos del mercado global de fundición de obleas, y Foxconn, Quanta y Wistron producen en conjunto el 90% de los servidores de IA del mundo. Pero en esa ceremonia científica de dos días consecutivos, que otorgó legitimidad retrospectiva a cuarenta y dos años de historia de las redes neuronales, no hubo ningún nombre de Taiwán. Desde Taiwan AI Labs, fundado por Ethan Tu, creador de [PTT](/es/Technology/ptt-bulletin-board-system/), hasta TAIDE, el gran modelo de lenguaje en chino tradicional por el que apuesta el gobierno, está en marcha una apuesta que va de “fabricar IA” a “convertirse en IA”.

---

## 42 años de reconocimiento: dos Nobel consecutivos en 2024

La mañana del 8 de octubre de 2024, en Estocolmo, la Real Academia Sueca de Ciencias anunció que el Premio Nobel de Física de ese año sería otorgado a dos científicos de IA: John J. Hopfield, profesor emérito de Princeton de 91 años, y Geoffrey Hinton, de 76 años, quien apenas cinco meses antes había dejado Google. El premio, de 11 millones de coronas suecas, fue dividido entre ambos[^N1].

La justificación del comité fue “por descubrimientos e invenciones fundamentales que permiten el aprendizaje automático con redes neuronales artificiales”[^N1]. Fue la primera vez en la historia del Nobel de Física que el galardón se colocó directamente sobre el campo de las redes neuronales.

Al día siguiente, el 9 de octubre, llegó el Nobel de Química. Los tres laureados fueron David Baker, de la Universidad de Washington, y dos investigadores de DeepMind: Demis Hassabis y John Jumper. Baker recibió la mitad del premio; Hassabis y Jumper compartieron la otra mitad[^N2]. La justificación se dividió en dos partes: la primera, para Baker, por el “diseño computacional de proteínas”; la segunda, para Hassabis y Jumper, por la “predicción de estructuras proteicas”.

Dos días, dos premios Nobel, todos relacionados con la IA. No había precedente de algo así en la historia de los Nobel.

Comparemos la línea de tiempo: cuando Hopfield publicó en 1982 en _Proceedings of the National Academy of Sciences_ (PNAS) su artículo “Neural networks and physical systems with emergent collective computational abilities”, acababa de pasar de la física de la materia condensada a la neurociencia[^N3]. De 1982 a 2024 transcurrieron exactamente 42 años. El artículo de 1986 en el que Hinton y Rumelhart convirtieron el algoritmo de retropropagación en una herramienta utilizable[^N4] tardó 38 años desde su publicación hasta el Nobel. AlphaFold, desde su primera aparición en CASP13 en 2018 hasta obtener el Nobel en 2024, necesitó apenas 6 años.

En el fondo, esos dos Nobel no premiaron a ChatGPT, sino a unos artículos de hace tres o cuatro décadas que casi nadie entendía. La brecha temporal entre la investigación básica y la aplicación industrial siempre ha sido así.

![Retrato oficial de Geoffrey E. Hinton entrevistado durante la semana Nobel en Estocolmo el 8 de diciembre de 2024, con traje oscuro, cabello blanco y expresión serena frente a la cámara](/article-images/technology/hinton-nobel-2024.webp)
_Geoffrey Hinton, laureado con el Premio Nobel de Física 2024, durante la semana Nobel en Estocolmo. Photo: Arthur Petron, 2024-12-08. [CC BY-SA 4.0 via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Geoffrey_E._Hinton,_2024_Nobel_Prize_Laureate_in_Physics_(3x4*cropped).jpg).*

---

## Una cena de billones en el mercado nocturno de Ningxia

La tarde del 29 de mayo de 2024, en vísperas de la apertura de Computex, apareció un grupo inusual de comensales en el mercado nocturno de Ningxia, en Taipéi. Jensen Huang, CEO de NVIDIA, llevó a Morris Chang, fundador de TSMC; Barry Lam, presidente de Quanta; y Rick Tsai, CEO de MediaTek, a comer omelet de ostras frente a un puesto[^1]. Los transeúntes reconocieron a Huang y, en segundos, quedaron rodeados por admiradores y periodistas, en una escena comparable al seguimiento de una estrella.

El valor de mercado combinado alrededor de esa comida superaba varios billones de dólares. Pero la historia real no estaba en la mesa, sino en la cadena industrial detrás de ella: las empresas representadas por esas personas sostienen la base física del cómputo global de IA. Durante ese viaje a Taiwán, Huang dijo públicamente: “Taiwán es uno de los países más importantes del mundo”[^2]. No era una cortesía. Sin Taiwán, la revolución de la IA no tendría cimientos de hardware.

Jensen Huang nació en Taipéi en 1963, pasó su infancia en Tainan y emigró a Estados Unidos a los nueve años[^3]. NVIDIA, que cofundó en 1993, es hoy sinónimo de chips de IA. Cada GPU avanzada diseñada por NVIDIA, desde las A100 y H100 que entrenaron ChatGPT hasta la serie Blackwell más reciente, se fabrica íntegramente en TSMC[^4].

Cuatro meses después, las listas de los dos Nobel anunciadas en Estocolmo no incluyeron ningún nombre vinculado a aquella cena. Esa brecha no es una coincidencia; es un hecho estructural.

---

## Hardware: una isla sostiene toda la revolución de la IA

Describir la posición de Taiwán en la cadena de suministro del hardware de IA como “clave” se queda corto.

En la fabricación de chips, TSMC capturó en 2025 el 72% de los ingresos del mercado global de fundición de obleas[^5]. En los procesos más avanzados, por debajo de 7 nanómetros, su cuota supera el 90%. NVIDIA tiene alrededor del 86% del mercado de GPU para IA, y esas GPU son fabricadas casi en su totalidad por TSMC[^6]. La enorme mayoría de la capacidad de cómputo usada en el mundo para entrenar y ejecutar modelos de IA nace en salas limpias taiwanesas.

Una vez fabricados los chips, todavía deben ensamblarse en servidores para entrar a los centros de datos. Esa etapa también está dominada por Taiwán. Los tres grandes fabricantes ODM, Foxconn, Quanta y Wistron, producen en conjunto cerca del 90% de los servidores de IA del mundo[^7]. En 2025, los ingresos anuales de cada una de estas tres empresas superaron el billón de dólares taiwaneses, unos 32.000 millones de dólares estadounidenses, y los ingresos por servidores de IA superaron por primera vez a los de electrónica de consumo en el segundo trimestre[^8].

El rendimiento de los chips de IA no depende solo de la miniaturización del proceso, sino también de la tecnología de empaquetado. CoWoS (Chip on Wafer on Substrate), el empaquetado avanzado de TSMC, es crucial para que las GPU de gama alta de NVIDIA alcancen sus objetivos de rendimiento. Para 2026, se estima que solo la demanda de NVIDIA por obleas CoWoS alcanzará las 595.000 unidades, el 60% de la demanda global[^9].

Foxconn, además, coopera con NVIDIA y el gobierno taiwanés para construir en Kaohsiung una supercomputadora de fábrica de IA de 100 megavatios (MW), basada en la arquitectura NVIDIA Blackwell más reciente[^10]. Taiwán está pasando de ser “el lugar donde se fabrican chips de IA” a ser “el lugar donde se ejecuta IA”.

![Exterior de la planta Fab 5 de TSMC en el Parque Científico de Hsinchu, escena de la década de 2010, sitio físico de la fabricación por fundición de obleas semiconductoras](/article-images/technology/tsmc-fab5-hsinchu-2010.webp)
_Planta Fab 5 de TSMC en Hsinchu, sitio físico de la fundición de chips de IA. Photo: Wikimedia Commons via [TSMC Fab 5 file](https://commons.wikimedia.org/wiki/File:TSMC_Fab_5.jpg)._

La pregunta es: una vez conseguido el boleto de entrada del hardware, ¿dónde será la próxima batalla?

> 📝 **Nota curatorial**
>
> La fórmula habitual dice que “la montaña sagrada protectora de Taiwán sostiene la revolución de la IA”. La narración funciona, pero invierte a medias la causalidad. La revolución de la IA necesitaba GPU y por eso eligió a TSMC; no fue TSMC la que nació de la revolución de la IA. La verdadera tensión está en otra parte: cuando la GPU se vuelve una mercancía, ¿hacia dónde se desplazará la siguiente capa de valor? Los dos Nobel de 2024 ofrecieron una respuesta: el modelo mismo. Las 12 páginas que escribió Hopfield, la noche de 2012 en que Hinton y su estudiante Krizhevsky hicieron que AlexNet redujera la tasa de error de reconocimiento de imágenes de ImageNet de 26,2% a 15,3%[^N5], y aquella tarde en que el equipo de Hassabis llevó a AlphaFold a obtener una mediana GDT de 92,4 en CASP14.

---

## Hopfield 1982: el modelo de memoria escrito por un físico

En 1982, John Hopfield, físico de materia condensada en Princeton, escribió un artículo de apenas 12 páginas con un título largo: “Neural networks and physical systems with emergent collective computational abilities”, publicado en _Proceedings of the National Academy of Sciences_[^N3].

Lo que hizo fue, en esencia, traducir la “memoria” al lenguaje de la física.

En física existe algo llamado _spin glass_ o vidrio de espín: un conjunto de átomos magnéticos, cada uno con su propia dirección de espín, interactúa entre sí, y el sistema completo encuentra espontáneamente un punto de energía mínima. Hopfield trasladó ese concepto a las neuronas: imaginó las neuronas como espines, las intensidades de conexión como interacciones, y la red completa convergiendo espontáneamente hacia un estado estable de “mínimo de energía”[^N3]. Cada mínimo de energía corresponde a un recuerdo almacenado.

La elegancia del modelo está en que convirtió la memoria en algo describible con el lenguaje de la física. Dada una pista incompleta, la red encuentra por sí misma el punto de energía mínima más cercano y completa el recuerdo. Ese es el antepasado matemático de lo que hoy hace la IA generativa.

En 1982, Taiwán apenas estaba dando sus primeros pasos en la industria electrónica, y TSMC todavía no existía. Morris Chang tendría que esperar hasta 1987 para fundar la empresa que 42 años después se convertiría en la “montaña sagrada protectora del país”. Para 2026, el artículo de Hopfield ya acumulaba más de 27.000 citas en Google Scholar[^N6].

Más interesante aún es algo que Hopfield dijo después. Pasó su vida en Princeton haciendo física de materia condensada, y sus colegas de la época vieron su entrada en la neurociencia como un pasatiempo lateral. Cuando se anunció el Nobel de 2024, tenía 91 años, y en la entrevista telefónica de la Real Academia Sueca de Ciencias dijo sentirse inquieto por el hecho de que “nadie entiende ni controla la dirección de la IA”[^N7].

La persona que escribió parte de la base matemática de toda la IA moderna aprovechó el día en que recibió el premio para pedir cautela.

![Retrato de John J. Hopfield entrevistado durante la semana Nobel en Estocolmo el 8 de diciembre de 2024, con traje oscuro, cabello blanco y expresión serena](/article-images/technology/hopfield-nobel-2024.webp)
_John J. Hopfield, laureado con el Premio Nobel de Física 2024, durante la semana Nobel en Estocolmo. Photo: Arthur Petron, 2024-12-08. [CC BY-SA 4.0 via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:John_J._Hopfield,_2024_Nobel_Prize_Laureate_in_Physics_1_(cropped).jpg).\_

---

## Hinton: el artículo de 1986 y la advertencia tras dejar Google en 2023

Geoffrey Hinton, nacido en Wimbledon, Londres, en 1947, es otra figura a la que la historia tardó 38 años en reconocer[^N8].

En 1986, Hinton publicó junto con David Rumelhart y Ronald Williams un artículo en _Nature_ sobre la retropropagación[^N4]. El algoritmo significa lo siguiente: cuando una red neuronal comete un error, la señal de error puede propagarse en sentido inverso por cada capa para ajustar, capa por capa, los pesos de conexión. Así es como todos los modelos de aprendizaje profundo actuales se entrenan a sí mismos.

El algoritmo fue escrito en 1986, pero necesitó que coincidieran tres cosas para explotar: cómputo suficientemente barato, datos suficientemente abundantes y personas dispuestas a creer en ese camino. Las dos primeras estuvieron listas a comienzos de la década de 2010; la tercera estuvo representada por Hinton y sus dos estudiantes, Alex Krizhevsky e Ilya Sutskever. En 2012, entrenaron con GPU la red neuronal convolucional AlexNet y lograron en la competencia de reconocimiento de imágenes ImageNet una tasa de error top-5 de 15,3%, muy por debajo del 26,2% del segundo lugar[^N5]. En ese momento, toda la industria empezó a creer que la retropropagación realmente funcionaba.

En marzo de 2013, Google compró por 44 millones de dólares la pequeña empresa de Hinton, DNNresearch, e incorporó al investigador, entonces de 65 años[^N8]. Durante la década siguiente, fue el académico de IA más prestigioso de Silicon Valley.

Luego, el 1 de mayo de 2023, _The New York Times_ publicó una entrevista: Hinton había dejado Google.

El motivo de su salida no fue la jubilación. En la entrevista dijo que quería “poder hablar libremente sobre los riesgos de la IA sin tener que considerar cómo afectaría eso a Google”[^N9]. Sus advertencias incluían la posibilidad de que los sistemas de IA fueran pronto más inteligentes que los humanos, que actores maliciosos los usaran para hacer daño, y que fuera “difícil ver cómo impedirlo”[^N9]. Incluso dijo que una parte de él lamentaba el trabajo de toda su vida[^N9].

Cuando el Nobel de Física de 2024 le fue otorgado, repitió en la entrevista telefónica la advertencia: había que tener cuidado con la posibilidad de que la IA se saliera de control[^N10].

La persona que formuló el algoritmo de entrenamiento del aprendizaje profundo y la persona que formuló el modelo de memoria subieron el mismo día de octubre de 2024 al escenario de la Real Academia Sueca de Ciencias, y ambas advirtieron que aquello podía ser más peligroso de lo imaginado. La escena dialoga, de algún modo, con la expresión de Oppenheimer al ver elevarse la nube en forma de hongo en el desierto de Nuevo México en 1945.

Dos meses después, el 8 de diciembre de 2024, Hinton pronunció su conferencia de aceptación del Premio Nobel en el Aula Magna de la Universidad de Estocolmo. El título era «Boltzmann Machines»: el trabajo fundacional de la línea de Hopfield y Hinton que incorporó distribuciones probabilísticas termodinámicas a las redes neuronales. Después de escucharla, quedó claro que el artículo de backpropagation de 1986 no fue un hallazgo aislado, sino todo un sistema de pensamiento que surgió en los años ochenta en la intersección entre la física y la ciencia cognitiva.

<div class="video-embed" style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;margin:1.5rem 0;border-radius:8px;">
  <iframe src="https://www.youtube.com/embed/iCS1ds0UDP8" title="Boltzmann Machines — Nobel Prize lecture by Geoffrey Hinton, Nobel Prize in Physics 2024" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

_Canal oficial de la Real Academia Sueca de Ciencias: conferencia de aceptación del Premio Nobel de Física de Geoffrey Hinton del 8 de diciembre de 2024, «Boltzmann Machines». Desde las Boltzmann machines que él y Sejnowski escribieron en los años ochenta, pasando por backpropagation, hasta los LLM de hoy: cuarenta años enteros. En los últimos 5 minutos volvió a exponer sus preocupaciones sobre el riesgo de la IA, esta vez desde el podio del Nobel._

---

## De PTT a un laboratorio de IA: las dos empresas de Ethan Tu

Volvamos a la isla de Taiwán. En el mismo periodo en que Hopfield formulaba su modelo de memoria, Taiwán apenas empezaba a crear departamentos de informática.

En 1995, Ethan Tu, entonces estudiante de segundo año de Ciencias de la Computación en la Universidad Nacional de Taiwán, usó una computadora 486 y software de código abierto para montar desde su dormitorio [PTT](/es/Technology/ptt-bulletin-board-system/), que luego se convirtió en el mayor sistema de tablón electrónico de Taiwán. Treinta años después, PTT todavía reúne a cientos de miles de usuarios diarios y funciona como un fósil viviente de la cultura de internet taiwanesa.

Tu trabajó después en Microsoft, donde participó en el desarrollo del asistente de voz Cortana. En abril de 2017 dejó un salario alto en Silicon Valley y regresó a Taiwán para fundar Taiwan AI Labs, el primer instituto de investigación de IA abierto y sin fines de lucro de Asia[^11].

Su motivación era directa: Taiwán tenía talento de software de nivel mundial, pero ese talento se iba a Silicon Valley. Quería construir una plataforma donde quienes deseaban volver o quedarse pudieran hacer investigación en IA.

El producto más conocido de Taiwan AI Labs es “Yating Transcript”, un sistema de reconocimiento de voz optimizado para chino tradicional y acentos taiwaneses. Durante la pandemia de COVID-19, el laboratorio también desarrolló herramientas de detección de desinformación e IA médica basada en aprendizaje federado[^12]. Estos proyectos tienen un punto en común: resuelven problemas locales de Taiwán, con datos locales de Taiwán, en lugar de limitarse a traducir modelos estadounidenses.

La historia de Ethan Tu, de PTT a AI Labs, es en cierto sentido un resumen del desarrollo del software taiwanés: no falta capacidad técnica; falta un ecosistema que permita retener talento.

> 💡 **¿Sabías que...?**
>
> En 1986, el año en que Hinton publicó la retropropagación, el PIB de Taiwán era de unos 77.900 millones de dólares, el PIB per cápita rondaba los 4.007 dólares, y el Parque Científico de Hsinchu llevaba apenas seis años en funcionamiento[^N11]. Las tres cosas ocurrieron simultáneamente en el mismo planeta, pero esa línea histórica no se cruzaría con ImageNet hasta 26 años después. La escala temporal de la investigación básica siempre es más larga que la percibida por la narrativa industrial.

---

## AlphaFold: la otra mitad del Nobel por el problema de 50 años del plegamiento de proteínas

La historia del Nobel de Química de 2024 comienza con una pregunta de 1972.

Ese año, al recibir el Nobel de Química, el bioquímico estadounidense Christian Anfinsen planteó en su discurso una hipótesis: la estructura tridimensional plegada de una proteína está completamente determinada por su secuencia de aminoácidos[^N12]. Si la hipótesis era correcta, en teoría bastaría ver una secuencia de aminoácidos para calcular su estructura 3D correspondiente. Pero ese “en teoría” permaneció medio siglo sin realizarse. El plegamiento de proteínas fue considerado un gran desafío. Desde 1994, la comunidad académica organiza cada dos años la competencia CASP, en la que se comparan las predicciones presentadas con estructuras experimentales. Durante 13 ediciones, nadie logró el salto decisivo[^N13].

Hasta CASP13 en 2018, cuando DeepMind presentó la primera generación de AlphaFold y ganó, aunque con una precisión todavía insuficiente para un uso práctico. El verdadero punto de inflexión llegó el 30 de noviembre de 2020, en CASP14: AlphaFold 2 obtuvo una mediana GDT de 92,4[^N13]. GDT 92,4 significa que en más de la mitad de las predicciones, la desviación de las posiciones atómicas respecto de los valores experimentales fue inferior a un angstrom, alcanzando una resolución de nivel experimental. Ese día, John Moult, organizador de CASP, dijo que “en gran medida, el problema había sido resuelto”[^N13].

Un problema que llevaba 50 años sin resolverse fue despejado en seis años por un equipo de investigación en Londres.

Luego todo avanzó todavía más rápido. En julio de 2021, se publicó como código abierto AlphaFold 2; ese mismo año, DeepMind colaboró con el Laboratorio Europeo de Biología Molecular (EMBL-EBI) para convertir las estructuras proteicas predichas por AlphaFold en una base de datos pública. En julio de 2022, esa base cubría un millón de especies y alrededor de 200 millones de estructuras proteicas, lo que equivale a liberar gratis modelos 3D de casi todas las proteínas conocidas del planeta[^N14].

El 8 de mayo de 2024, DeepMind publicó AlphaFold 3 en _Nature_, ampliando su capacidad predictiva desde proteínas individuales hasta interacciones entre proteínas y ADN, ARN, ligandos e iones[^N15]. Desde el desarrollo de nuevos fármacos y el diseño de vacunas hasta la ingeniería enzimática, todos los campos que necesitan saber cómo encajan entre sí las moléculas vieron reescrita su base por esta herramienta.

Demis Hassabis, quien creó AlphaFold, no es un bioquímico tradicional. Empezó a jugar ajedrez a los cuatro años y obtuvo el título de maestro a los trece; a los diecisiete desarrolló junto con Peter Molyneux el videojuego de simulación _Theme Park_, que vendió millones de copias[^N16]. En 2010 fundó DeepMind en Londres junto con Shane Legg y Mustafa Suleyman; en 2014, Google la adquirió por 400 millones de libras[^N16]. En 2016, AlphaGo de DeepMind derrotó a Lee Sedol; en 2020 llegó AlphaFold 2; en 2024, el Nobel. Las tres cosas ocurrieron en menos de diez años.

La línea que las une es una misma apuesta: usar redes neuronales para resolver problemas que la mente humana no había podido resolver. El go es un sistema de reglas cerrado; el plegamiento de proteínas es abierto, pero con fuertes restricciones físicas. Hassabis eligió correctamente ambos campos de batalla.

En Taiwán, la investigación sobre glicomoléculas y proteínas construida durante la presidencia de Chi-Huey Wong en Academia Sinica (2006-2016) es la inversión académica local más cercana a esa frontera[^N17]. También hay equipos en el Instituto de Ciencias Biomédicas y el Instituto de Química Biológica de Academia Sinica que usan los pesos abiertos de AlphaFold para investigación posterior. Pero Taiwán no cuenta hoy con una estructura equivalente para desarrollar modelos centrales del nivel de AlphaFold.

> ⚠️ **Perspectiva controvertida**
>
> El Nobel de Química para AlphaFold generó debate en la academia: algunos biólogos estructurales sostuvieron que el premio debía ir a quienes realizaron los primeros experimentos clave de cristalografía de rayos X o resonancia magnética nuclear, no a quienes elevaron una herramienta computacional al altar de la química[^N18]. Otros consideraron que el debate en sí ya estaba obsoleto: cuando un algoritmo puede ayudar a la humanidad a completar en cinco años las estructuras 3D de casi todas las proteínas del planeta, eso es química. Tras octubre de 2024, la discusión se fue inclinando hacia esta segunda postura, pero la tensión que representa no desapareció: si la IA puede hacer cada vez más cosas, ¿deben redibujarse las fronteras de las disciplinas tradicionales?

---

## TAIDE: por qué Taiwán necesita su propio modelo lingüístico

En abril de 2023, medio año después de que ChatGPT arrasara globalmente, el Consejo Nacional de Ciencia y Tecnología de Taiwán (NSTC) lanzó el proyecto TAIDE, sigla de Trustworthy AI Dialogue Engine, o motor de diálogo de IA generativa confiable[^13].

¿Por qué un país insular de 23 millones de habitantes necesita crear su propio gran modelo de lenguaje?

La razón no es solo la autonomía tecnológica. El chino tradicional ocupa una proporción extremadamente baja en los datos globales de entrenamiento de IA, y la mayor parte de los datos en chino proviene de sitios web en chino simplificado. Cuando las personas en Taiwán usan ChatGPT u otros modelos, las respuestas suelen incorporar hábitos lingüísticos y supuestos de perspectiva de China continental. “視頻” en lugar de “影片”, “質量” en lugar de “品質”: diferencias que parecen menores, pero detrás de ellas está el problema de la subjetividad cultural. _CommonWealth Magazine_ tituló directamente su reportaje sobre TAIDE como una forma de “evitar la invasión cultural de la IA china”[^14].

En abril de 2024, el equipo de TAIDE publicó TAIDE-LX-7B para uso comercial y TAIDE-LX-13B para investigación académica, con buenos resultados en tareas de redacción, traducción y resumen[^15]. Para 2026, con el lanzamiento de TAIDE 2.0 y el modelo Breeze-8B respaldado por MediaTek, el ecosistema taiwanés de LLM pasó de la etapa de “ponerse al día” a la de “ser utilizable”[^16].

Más interesante aún es la proliferación de aplicaciones. La Universidad Nacional Chung Hsing construyó con TAIDE un sistema de recuperación de conocimiento agrícola llamado “Shennong TAIDE”; la Universidad Nacional de Tainan desarrolló un robot conversacional taiwanés-inglés para enseñar taiwanés; y la Universidad Nacional Yang Ming Chiao Tung entrenó versiones de TAIDE en taiwanés y hakka[^17]. Estas aplicaciones confirman algo: un modelo lingüístico es a la vez un producto tecnológico y un vehículo cultural. Una IA que no entiende el “Día del Cielo Rasgado” ni las procesiones de Mazu no puede servir realmente a la sociedad taiwanesa.

Aun así, TAIDE sigue siendo pequeño: sus modelos comercial de 8B y académico de 13B parámetros están más de dos órdenes de magnitud por debajo de modelos del nivel de GPT-4 de OpenAI, presumiblemente superiores al billón de parámetros. Esa brecha es un problema de presupuesto de GPU, no de capacidad. Entrenar un LLM de frontera requiere cómputo del orden de cientos de millones de dólares, comparable al presupuesto anual de una institución nacional de investigación.

---

## La ciberseguridad de IA nacida de los ataques

Taiwán es uno de los países más atacados cibernéticamente del mundo. Esta realidad desafortunada generó, de manera inesperada, una sólida industria de ciberseguridad con IA.

CyCraft, fundada a fines de 2017, fue la primera empresa taiwanesa en combinar IA con monitoreo de endpoints. Su tecnología ha sido incluida siete veces en informes de la consultora global Gartner, y es la única empresa taiwanesa que ha superado tres veces la evaluación autorizada MITRE ATT&CK de Estados Unidos[^18]. En febrero de 2026, CyCraft salió a cotizar en la Junta de Innovación de la Bolsa de Taiwán, convirtiéndose en la primera empresa original de software de ciberseguridad con IA y capacidad internacional de I+D propia en el mercado de capitales taiwanés[^19].

Los clientes de CyCraft incluyen agencias gubernamentales, unidades de defensa, bancos y empresas de semiconductores de Taiwán, precisamente los objetivos más frecuentes de hackers de nivel estatal. La empresa tiene subsidiarias en Japón y Singapur, y está exportando a toda Asia-Pacífico su “experiencia práctica nacida de ser atacados”.

Este caso muestra algo: la ventaja de Taiwán en IA no proviene solo de los semiconductores, sino también de la capacidad práctica forjada por su particular situación geopolítica.

---

## Política: del “año uno de la IA” al Ministerio de Asuntos Digitales

El desarrollo de la política de IA en Taiwán puede entenderse a partir de tres momentos.

Entre 2017 y 2018 ocurrió la fase inicial. El Yuan Ejecutivo declaró 2017 como el “año uno de la IA” y propuso la idea de una “gran estrategia de IA para un país pequeño”, reconociendo que el mercado taiwanés era reducido, pero destacando tres cartas: fabricación de semiconductores, cadena de suministro TIC y talento en ciencia e ingeniería. En 2018 se lanzó la primera fase del “Plan de Acción de IA de Taiwán”, con una inversión de más de 40.000 millones de dólares taiwaneses durante cuatro años, centrada en construir la infraestructura de cómputo de IA “Taiwan AI Cloud” (TWCC)[^20].

En 2022, la política avanzó hacia la institucionalización. Se creó el Ministerio de Asuntos Digitales (moda), que integró funciones digitales antes dispersas entre el Ministerio de Ciencia y Tecnología, el Ministerio de Economía y el Ministerio de Transportes y Comunicaciones. La importancia de ese paso fue clara: la política de IA dejó de ser “un proyecto del Ministerio de Ciencia” para convertirse en “una estrategia nacional interministerial”. Ese mismo año, el gobierno publicó las “Directrices para la investigación y el desarrollo en inteligencia artificial”, con principios como centralidad humana, transparencia y explicabilidad, equidad y no discriminación.

Desde 2023 hasta hoy, la orientación se desplazó hacia la IA generativa. El impacto de ChatGPT produjo un viraje rápido de las políticas. Se lanzó TAIDE, avanzó el borrador de una ley básica de IA y se aceleró la adopción de IA en el sector público. La estrategia taiwanesa es pragmática: no competir con Estados Unidos y China por cantidad de artículos de investigación básica, sino acoplar la IA a las ventajas manufactureras existentes. Manufactura inteligente, imágenes médicas, predicción de rendimiento en semiconductores: son campos donde Taiwán tiene datos, escenarios de aplicación y competitividad.

El problema es que en las listas de laureados de esos dos días de octubre de 2024 no hubo nadie proveniente de la ruta de la “manufactura inteligente”.

---

## Ansiedad: la brecha de software del imperio del hardware

Detrás de las cifras brillantes, el desarrollo de la IA en Taiwán tiene un problema estructural: un grave desequilibrio entre hardware y software.

Taiwán produce el 90% de los servidores de IA del mundo y la mayor parte de los chips de IA, pero en los eslabones “blandos” de desarrollo de modelos de IA, ecosistemas de datos y software de plataforma, su presencia es baja. Entre los veinte principales modelos de IA del mundo, incluidos GPT, Claude, Gemini y LLaMA, no hay ninguno de Taiwán. Si se comparan los trabajos premiados por los dos Nobel de 2024, desde la red de Hopfield y la retropropagación hasta AlphaFold, las tres líneas quedan muy lejos de la industria taiwanesa.

La razón es una nueva versión de un viejo problema. Cuando un ingeniero de TSMC puede ganar más de dos millones de dólares taiwaneses al año, a una startup local de software le resulta difícil competir por el mejor talento. Google, Microsoft y NVIDIA tienen centros de I+D en Taiwán, y sus salarios y beneficios generan un fuerte efecto de absorción. Para un graduado en informática de la Universidad Nacional de Taiwán, la primera opción suele ser una multinacional o el área de TI de TSMC, no una startup taiwanesa de IA.

El desafío más fundamental son los datos. El valor de un modelo de IA proviene de sus datos de entrenamiento, y la cantidad de datos de alta calidad en chino tradicional es minúscula en comparación con el inglés o el chino simplificado. Los textos producidos por una población de 23 millones de personas, por naturaleza, no pueden igualar el volumen del mundo angloparlante ni el de China continental. TAIDE intenta resolver este problema, pero la desventaja de escala de los datos es estructural.

La verdadera apuesta de Taiwán en IA está en las aplicaciones verticales, no en los modelos fundacionales: en lugar de enfrentar directamente a OpenAI o Google en modelos generales, Taiwán busca posiciones insustituibles en IA para procesos de semiconductores, IA para imágenes médicas, IA de ciberseguridad y procesamiento de lenguaje natural en chino tradicional. En estos campos, Taiwán posee datos y escenarios únicos que otros difícilmente pueden replicar.

---

## La elección de IA de una isla

El Taiwán de 2026 se encuentra en una posición singular: nunca ha sido tan indispensable en la cadena de suministro de hardware de IA, pero sigue siendo periférico en el ecosistema de software de IA.

Esto no es del todo malo. Históricamente, el modelo de éxito de Taiwán ha sido “no ser la marca, sino la marca detrás de la marca”. El modelo de fundición pura inventado por Morris Chang en 1987 convirtió a TSMC en una de las diez empresas más valiosas del mundo. Hoy, la misma lógica se repite en la industria de servidores de IA: Foxconn no crea modelos de IA, pero los modelos de IA del mundo corren sobre servidores ensamblados por Foxconn.

Pero las reglas del juego en la era de la IA pueden ser distintas. Cuando el centro de valor se desplaza del hardware al software y los datos, el margen de hacer solo manufactura por encargo se comprime. Los dos Nobel otorgados en esos días de 2024 fueron todos para personas de la capa de software. Hopfield escribió un modelo matemático, Hinton escribió un algoritmo de entrenamiento, Hassabis escribió un método para resolver un problema biológico. Todos esos trabajos corren sobre hardware fabricado en Taiwán, pero los premios no fueron para el hardware.

Taiwán necesita desarrollar capacidades de software y datos sobre la base de su hegemonía en hardware: el hardware sigue siendo el chasis, y las nuevas capas de valor deben apilarse encima. TAIDE es un intento; CyCraft es un intento; Taiwan AI Labs es un intento. Tienen algo en común: no buscan construir “la IA más grande del mundo”, sino “la IA que mejor entiende a Taiwán”.

Hace 42 años, cuando Hopfield escribió aquellas 12 páginas en Princeton, nadie sabía que se convertirían en la base matemática de los modelos de memoria humanos actuales. Hace 50 años, cuando Anfinsen planteó su hipótesis sobre el plegamiento de proteínas en su discurso Nobel, nadie esperaba que recién en aquella tarde de 2020 un grupo de investigadores londinenses lograra resolverla. La escala temporal de la investigación básica es más larga que cualquier Computex.

Aquella cena en el mercado nocturno de Ningxia fue el lugar que Taiwán acumuló durante estos 42 años. Dónde será la próxima batalla: no frente al puesto de omelet de ostras, sino en si Taiwán tendrá el coraje de permitir que algún estudiante que hoy programa en un dormitorio de la Universidad Nacional de Taiwán reciba, dentro de veinte o treinta años, un Nobel perteneciente a esta isla.

---

**Lecturas complementarias**:

- [El ascenso de la isla de la IA: desarrollo de la inteligencia artificial en Taiwán y estrategia futura](/technology/AI發展) — Versión temprana de la narrativa de política pública: el Plan de Acción de IA, los cinco campos estratégicos y el panorama de cómo la “montaña sagrada protectora” de los semiconductores se acopla a la revolución de la IA.
- [Taiwan AI Labs](/technology/台灣人工智慧實驗室) — La trayectoria completa de Ethan Tu desde PTT hasta AI Labs, y el ecosistema de modelos de lenguaje abiertos TAIDE / TAME / FedGPT.
- [Taiwan AI Academy](/technology/台灣人工智慧學校) — La llamada inconclusa y la academia militar de IA creada por Chen Sheng-wei con 180 millones de dólares taiwaneses de financiación privada: una historia de formación de talento con más de diez mil egresados en ocho años.
- [La IA en la vida cotidiana de Taiwán](/technology/台灣AI日常) — Crónica de la entrada de la IA generativa en la vida cotidiana taiwanesa, desde pedidos en tiendas de conveniencia hasta revisiones por lotes de la Administración Nacional del Seguro de Salud.
- [Empresas taiwanesas: TSMC](/economy/台灣企業：台積電) — Líder global de fundición de obleas, núcleo de la fabricación de chips de IA, desde el modelo de fundición pura de Morris Chang hasta la historia del empaquetado avanzado.
- [Industria de semiconductores](/technology/半導體產業) — Panorama completo del ecosistema taiwanés de semiconductores, desde el diseño de IC hasta el empaquetado y las pruebas.
- [Desarrollo de la industria de ciberseguridad de Taiwán](/technology/台灣資安產業發展) — Cómo la presión geopolítica dio origen a una industria de ciberseguridad con IA de escala Asia-Pacífico.

---

## Fuentes de imágenes

Este artículo usa 4 imágenes de dominio público / con licencias CC, todas almacenadas en caché en `public/article-images/technology/` para evitar enlaces directos a los servidores de origen:

- [Estructura tridimensional de la proteïna CBLN1 per AlphaFold amb codificació rainbow](https://commons.wikimedia.org/wiki/File:Estructura_tridimensional_de_la_prote%C3%AFna_CBLN1_per_AlphaFold_amb_codificaci%C3%B3_rainbow.png) — hero, estructura predicha por AlphaFold de la proteína CBLN1, codificación cromática rainbow del extremo N al C. Photo: BQUB25-UPoch (own work, AlphaFold + PyMOL), 2025-11-15, CC BY 4.0.
- [Geoffrey E. Hinton, 2024 Nobel Prize Laureate in Physics (3x4 cropped)](<https://commons.wikimedia.org/wiki/File:Geoffrey_E._Hinton,_2024_Nobel_Prize_Laureate_in_Physics_(3x4_cropped).jpg>) — inline, retrato oficial de Hinton durante la semana Nobel 2024. Photo: Arthur Petron, 2024-12-08, CC BY-SA 4.0.
- [John J. Hopfield, 2024 Nobel Prize Laureate in Physics 1 (cropped)](<https://commons.wikimedia.org/wiki/File:John_J._Hopfield,_2024_Nobel_Prize_Laureate_in_Physics_1_(cropped).jpg>) — inline, retrato oficial de Hopfield durante la semana Nobel 2024. Photo: Arthur Petron, 2024-12-08, CC BY-SA 4.0.
- [TSMC Fab 5](https://commons.wikimedia.org/wiki/File:TSMC_Fab_5.jpg) — inline, planta Fab 5 de TSMC en Hsinchu, sitio físico de la fundición de chips de IA. Photo: Wikimedia Commons (existing cache).

---

## Referencias

[^1]: [Tom's Hardware: Semiconductor legends take a stroll in a Taiwanese night market](https://www.tomshardware.com/tech-industry/semiconductor-legends-take-a-stroll-in-a-taiwanese-night-market-nvidia-tsmc-mediatek-and-quanta-heads-seen-eating-dinner) — Reportaje sobre la escena del mercado nocturno de Ningxia el 29 de mayo de 2024, que registró a Jensen Huang, Morris Chang, Barry Lam y Rick Tsai comiendo juntos.

[^2]: [Taiwan News: Nvidia CEO calls Taiwan 'one of the most important countries in the world'](https://www.taiwannews.com.tw/news/5880054) — Declaraciones públicas de Jensen Huang durante su visita a Taiwán el 2024-05-30.

[^3]: [Wikipedia: Jensen Huang](https://en.wikipedia.org/wiki/Jensen_Huang) — Datos biográficos sobre Jensen Huang: nacido en Taipéi en 1963, infancia en Tainan y emigración a Estados Unidos a los nueve años.

[^4]: Todas las GPU avanzadas de NVIDIA (A100, H100 y serie Blackwell) son fabricadas por TSMC. Véase [Klover.ai: TSMC AI Fabricating Dominance](https://www.klover.ai/tsmc-ai-fabricating-dominance-chip-manufacturing-leadership-ai-era/) — Análisis industrial que cubre la relación de fundición de toda la serie de GPU de IA de NVIDIA.

[^5]: [SQ Magazine: AI Chip Statistics 2025](https://sqmagazine.co.uk/ai-chip-statistics/) — Fuente del dato de cuota de ingresos del 72% de TSMC en el mercado de fundición de obleas en 2025; véanse también reportes contemporáneos de Motley Fool.

[^6]: [PatentPC: The AI Chip Market Explosion](https://patentpc.com/blog/the-ai-chip-market-explosion-key-stats-on-nvidia-amd-and-intels-ai-dominance) — Fuente del dato de 86% de cuota de mercado de NVIDIA en GPU de IA.

[^7]: [Tech-Now: Taiwan Leads Global AI Server Shift, Surpassing iPhones in 2025](https://tech-now.io/en/blogs/taiwans-ai-server-revolution-how-foxconn-and-odms-redefined-global-tech-leadership-in-2025) — Datos de envíos globales de servidores de IA: Foxconn, Quanta y Wistron con el 90%.

[^8]: [DigiTimes: Foxconn, Wistron, Quanta to sustain trillion-dollar revenue on AI server in 2026](https://www.digitimes.com/news/a20260109PD249/revenue-ai-server-foxconn-wistron-quanta.html) — Reporte sobre las tres ODM con ingresos anuales superiores al billón de dólares taiwaneses y servidores de IA superando a la electrónica de consumo.

[^9]: [36Kr: Who Will Divide Up the CoWoS Production Capacity in 2026?](https://eu.36kr.com/en/p/3580962946874242) — Datos sobre la demanda de NVIDIA de 595.000 obleas CoWoS, equivalente al 60% del total global.

[^10]: [NVIDIA Newsroom: Foxconn Builds AI Factory in Partnership With Taiwan and NVIDIA](https://nvidianews.nvidia.com/news/foxconn-builds-ai-factory-in-partnership-with-taiwan-and-nvidia) — Proyecto de fábrica de IA de 100 MW en Kaohsiung; véase también el reporte de CNBC sobre la capacidad eléctrica de 100 MW.

[^11]: [Sitio oficial de Taiwan AI Labs, Acerca de nosotros](https://ailabs.tw/zh/關於我們/) — Perfil oficial sobre la creación de PTT por Ethan Tu en 1995 en la Universidad Nacional de Taiwán y la fundación de Taiwan AI Labs en abril de 2017 tras su regreso a Taiwán.

[^12]: [TechNews 科技新報：AI 人才在台灣，該走該留？專訪台灣人工智慧實驗室創辦人杜奕瑾](https://finance.technews.tw/2025/08/18/taiwan-ai-labs-ethan/) — Introducción a proyectos centrales como Yating Transcript e IA médica con aprendizaje federado.

[^13]: [Yuan Ejecutivo: perfeccionar la infraestructura de IA de Taiwán: construir TAIDE, un motor de diálogo de IA confiable](https://www.ey.gov.tw/Page/5A8A0CB5B41DA11E/582206fe-26fc-4184-b911-aa6e4569ff3e) — Explicación oficial del inicio del proyecto TAIDE en abril de 2023.

[^14]: [CommonWealth Magazine: “Para evitar la invasión cultural de la IA china”, ¿qué puede hacer TAIDE, el primer gran modelo de lenguaje en chino tradicional de Taiwán?](https://www.cw.com.tw/article/5129076) — Reportaje sobre TAIDE y fuente del argumento sobre la subjetividad cultural de los LLM en chino tradicional.

[^15]: [Comunicado de prensa del NSTC: Un año de TAIDE, cooperación público-privada para impulsar grandes modelos de lenguaje con características taiwanesas](https://www.nstc.gov.tw/folksonomy/detail/dd2d9d72-8f7b-44dd-976c-438d5ce683af?l=ch) — Publicación en abril de 2024 de TAIDE-LX-7B comercial y 13B académico.

[^16]: [CloudInsight: Taiwan LLM Development Status 2026](https://cloudinsight.cc/en/blog/taiwan-llm) — Panorama completo del ecosistema taiwanés de LLM, incluidos TAIDE 2.0 y Breeze-8B.

[^17]: Mismo informe de CloudInsight. Detalla casos de aplicación como “Shennong TAIDE” de la Universidad Nacional Chung Hsing, el robot conversacional taiwanés-inglés de la Universidad Nacional de Tainan y los modelos TAIDE en taiwanés y hakka de la Universidad Nacional Yang Ming Chiao Tung.

[^18]: [CIO Taiwan: recorrido por empresas taiwanesas de ciberseguridad: CyCraft Technology](https://www.cio.com.tw/taiwanese-ahn-an-smart-technology/) — Detalles sobre las siete inclusiones de CyCraft en Gartner y sus tres aprobaciones de la evaluación MITRE ATT&CK.

[^19]: [Sitio oficial de CyCraft: ¡Primer listado en la Junta de Innovación del rey de la ciberseguridad con IA! CyCraft sale hoy a cotizar](https://www.cycraft.com/news/taiwans-first-ai-cybersecurity-stock-20260205) — Comunicado de prensa del listado en la Junta de Innovación el 5 de febrero de 2026.

[^20]: [NSTC: estrategia de investigación científica en IA](https://www.nstc.gov.tw/folksonomy/detail/dbf8da09-22be-4ef1-8294-8832fc6e8a26?l=ch) — Marco de política pública de la primera fase del Plan de Acción de IA de Taiwán, con presupuesto de 40.000 millones de dólares taiwaneses y construcción de TWCC.

[^N1]: [The Nobel Prize in Physics 2024 press release](https://www.nobelprize.org/prizes/physics/2024/press-release/) — Anuncio oficial de la Real Academia Sueca de Ciencias del 8 de octubre de 2024. Texto original: “The Royal Swedish Academy of Sciences has decided to award the Nobel Prize in Physics 2024 to John J. Hopfield and Geoffrey Hinton 'for foundational discoveries and inventions that enable machine learning with artificial neural networks.'” Premio de 11 millones de coronas suecas, dividido entre ambos.

[^N2]: [The Nobel Prize in Chemistry 2024 press release](https://www.nobelprize.org/prizes/chemistry/2024/press-release/) — Anuncio del 9 de octubre de 2024. Premio de 11 millones de coronas suecas: David Baker recibió la mitad “for computational protein design”, y Demis Hassabis y John Jumper compartieron la otra mitad “for protein structure prediction”.

[^N3]: Hopfield, J. J. (1982). "Neural networks and physical systems with emergent collective computational abilities." [PNAS, 79(8), 2554-2558](https://www.pnas.org/doi/10.1073/pnas.79.8.2554) — Artículo original de la red de Hopfield, que compara las redes neuronales con sistemas de vidrio de espín y propone el mínimo de energía como equivalente al almacenamiento de memoria. Publicado en abril de 1982.

[^N4]: Rumelhart, D. E., Hinton, G. E., & Williams, R. J. (1986). "Learning representations by back-propagating errors." [Nature, 323, 533-536](https://www.nature.com/articles/323533a0) — Artículo clásico sobre el algoritmo de retropropagación, trabajo fundacional del método de entrenamiento de redes neuronales.

[^N5]: Krizhevsky, A., Sutskever, I., & Hinton, G. E. (2012). "ImageNet Classification with Deep Convolutional Neural Networks." [NeurIPS 2012 / NIPS Proceedings](https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html) — Artículo original de AlexNet; tasa de error top-5 de 15,3% en ImageNet ILSVRC-2012 (26,2% para el segundo lugar), punto de inflexión clave para la industrialización del aprendizaje profundo.

[^N6]: [PanSci 泛科學：2024 諾貝爾物理獎—— Hopfield 與 Hinton 開啟了人工神經網路機器學習時代](https://pansci.asia/archives/378242) — Socio de curaduría de contenidos según MOU 2026-05-05. Cubre el contexto de la red de Hopfield, la analogía con el vidrio de espín, la acumulación de citas del artículo y su vínculo matemático con el aprendizaje profundo contemporáneo.

[^N7]: [The Guardian: Nobel physics prize 2024 winner John Hopfield warns of AI dangers](https://www.theguardian.com/science/2024/oct/08/nobel-prize-physics-2024-john-hopfield-geoffrey-hinton-ai-machine-learning) — Reporte de la entrevista telefónica del Nobel de Física el 2024-10-08, con advertencias de Hopfield y Hinton sobre los riesgos de la IA.

[^N8]: [Wikipedia: Geoffrey Hinton](https://en.wikipedia.org/wiki/Geoffrey_Hinton) — Hinton nació el 6 de diciembre de 1947 en Wimbledon, Londres; en marzo de 2013 se incorporó a Google tras la compra de DNNresearch por 44 millones de dólares.

[^N9]: [BBC News: AI 'godfather' Geoffrey Hinton warns of dangers as he quits Google](https://www.bbc.com/news/world-us-canada-65452940) — El 2023-05-01, tras dejar Google, Hinton expresó a la BBC su preocupación por los riesgos de la IA. Texto original: “I left so that I could talk about the dangers of AI without considering how this impacts Google”, “a part of me now regrets my life's work”. Detalles contemporáneos de la entrevista de NYT también citados en este reporte.

[^N10]: [Nature: AI scientist Geoffrey Hinton wins Nobel prize for physics](https://www.nature.com/articles/d41586-024-03213-8) — Detalles de _Nature_ sobre el anuncio del Nobel de Física 2024 y la entrevista telefónica de Hinton.

[^N11]: [Wikipedia: Economic history of Taiwan](https://en.wikipedia.org/wiki/Economic_history_of_Taiwan) — Datos del PIB de Taiwán en 1986; el Parque Científico de Hsinchu fue creado en diciembre de 1980.

[^N12]: Anfinsen, C. B. (1973). "Principles that govern the folding of protein chains." [Science, 181(4096), 223-230](https://www.science.org/doi/10.1126/science.181.4096.223) — Uno de los trabajos premiados con el Nobel de Química de 1972; plantea la hipótesis de que el plegamiento de proteínas está determinado por la secuencia de aminoácidos.

[^N13]: [Nature: 'It will change everything': DeepMind's AI makes gigantic leap in solving protein structures](https://www.nature.com/articles/d41586-020-03348-4) — Reporte de resultados de CASP14 del 30 de noviembre de 2020: AlphaFold 2 obtuvo una mediana GDT de 92,4, y el organizador de CASP John Moult comentó “in some sense the problem is solved”.

[^N14]: [DeepMind: AlphaFold reveals the structure of the protein universe](https://www.deepmind.com/blog/alphafold-reveals-the-structure-of-the-protein-universe) — Anuncio del 28 de julio de 2022 sobre la cobertura de la AlphaFold Protein Structure Database: un millón de especies y alrededor de 200 millones de estructuras proteicas.

[^N15]: [Abramson, J., Adler, J., Dunger, J. et al. (2024). Accurate structure prediction of biomolecular interactions with AlphaFold 3. Nature 630, 493-500](https://www.nature.com/articles/s41586-024-07487-w) — Publicación de AlphaFold 3 del 8 de mayo de 2024; amplía la predicción a complejos de proteínas con ADN / ARN / ligandos / iones.

[^N16]: [Wikipedia: Demis Hassabis](https://en.wikipedia.org/wiki/Demis_Hassabis) — Hassabis empezó a jugar ajedrez a los 4 años; a los 17 (1994) codesarrolló _Theme Park_ con Peter Molyneux; fundó DeepMind en Londres en 2010; Google la adquirió en 2014 por alrededor de 400 millones de libras.

[^N17]: [Centro de Investigación Genómica de Academia Sinica](https://www.genomics.sinica.edu.tw/) — Centro de investigación de estructuras de glicomoléculas y proteínas establecido durante la presidencia de Chi-Huey Wong (2006-2016).

[^N18]: [PanSci 泛科學：2024 諾貝爾化學獎—— David Baker、Demis Hassabis、John Jumper 解開蛋白質摺疊難題](https://pansci.asia/archives/378388) — Socio de curaduría de contenidos según MOU 2026-05-05. Cubre la controversia sobre el Nobel de Química a AlphaFold y la discusión sobre las fronteras disciplinares entre biología estructural y química computacional.

[^N19]: [PanSci 泛科學：AlphaFold 3 預測蛋白質與其他分子互動，藥物開發再升級](https://pansci.asia/archives/377917) — Socio de curaduría de contenidos según MOU 2026-05-05. Análisis del impacto de AlphaFold 3 en el desarrollo de fármacos y la ingeniería enzimática.

[^N20]: [PanSci 泛科學：「人造腦」OI 挑戰 AI——培養皿裡的腦組織能取代矽晶片嗎？](https://pansci.asia/archives/366027) — Socio de curaduría de contenidos según MOU 2026-05-05. Investigación de organoides cerebrales del equipo de Thomas Hartung en Johns Hopkins como vía computacional alternativa a la IA basada en silicio.
