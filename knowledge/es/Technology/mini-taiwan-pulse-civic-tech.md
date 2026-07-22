---
title: "'Mini Taiwan Pulse: con mirada curatorial, dibujar Taiwán como un mapa que respira'"
description: 'En 2026, el analista de datos Migu superpuso datos abiertos dispersos de Taiwán —aviones, barcos, trenes, autobuses y camiones de basura— hasta convertirlos en un mapa que respira. El trabajo pesado de extraer datos quedó en manos de la IA; pero decidir qué capas juntar, qué colores usar y cuál hacer brillar dependió de una mirada curatorial formada en planificación urbana.'
date: 2026-04-19
author: 'Taiwan.md'
category: 'Technology'
subcategory: '公民科技'
tags:
  [
    'Tecnología',
    'tecnología cívica',
    'datos abiertos',
    'visualización de datos',
    'proyecto de código abierto',
    'TDX',
    'Three.js',
    'inteligencia artificial',
    'agente de IA',
    'SIG',
  ]
readingTime: 20
lastVerified: 2026-06-25
lastHumanReview: true
featured: false
translatedFrom: 'Technology/mini-taiwan-pulse.md'
sourceCommitSha: '905aa4a82'
sourceContentHash: 'sha256:93ceaae8bc44512f'
sourceBodyHash: 'sha256:941fb85e8f2fbb98'
translatedAt: '2026-06-26T00:38:47+08:00'
image: '/article-images/technology/mini-taiwan-pulse-map-2026.webp'
imageCredit: 'Migu / sciwork 2026'
imageLicense: 'Fair use editorial commentary'
imageSource: 'https://github.com/ianlkl11234s/0613-sci-work-share'
---

# Mini Taiwan Pulse: con mirada curatorial, dibujar Taiwán como un mapa que respira

Un día a comienzos de 2026, un analista de datos llamado Migu convirtió un archivo CSV en GeoJSON y lo arrastró a una herramienta del navegador llamada Kepler.gl. Sin escribir media línea de código, apareció en la pantalla el primer mapa de Taiwán.

En la universidad había estudiado planificación urbana y entonces había tocado un poco de SIG (sistemas de información geográfica; en términos simples, herramientas que hacen que los datos vivan sobre un mapa). Después de entrar al mundo laboral siguió el camino del análisis de datos, y hacía mucho que no volvía a trabajar con mapas. Aquel día, al arrastrar el CSV a Kepler.gl y ver cómo Taiwán crecía en la pantalla, lo que le vino a la mente fue una sorpresa muy sencilla:

> “Resulta que Taiwán tiene tantos datos; resulta que convertirlos en mapa no es tan difícil.”[^1]

La frase no parece gran cosa. Después se convirtió en la semilla de todo un conjunto de cosas.

> **Resumen en 30 segundos:** Migu (GitHub `ianlkl11234s`) empezó a fines de 2025 a crear más de una decena de proyectos de visualización con datos abiertos de Taiwán. El más popular, mini-taiwan-pulse, acumuló 375 estrellas en GitHub y superpone cinco tipos de datos en tiempo real —cielo, mar, tierra, calles y recolección de basura— en un mapa animado[^2]. Pero en una charla de junio de 2026 para la comunidad sciwork, planteó el problema sin rodeos: sólo el gobierno central de Taiwán tiene alrededor de cincuenta mil conjuntos de datos abiertos, dispersos además en más de veinte plataformas municipales y de condado; “el cerebro humano no alcanza a revisarlos todos”. Su respuesta no fue pedir a más personas que ayudaran a revisarlos, sino entregar los datos completos a un sistema orquestado por agentes de IA, capaz de crecer por sí mismo, donde las personas sólo se encargan de formular las preguntas y validar los resultados[^3].

Este artículo trata de cómo una persona pasó de la ingenuidad de arrastrar un CSV a soltar el control para dejar que un sistema creciera por él.

## Cómo el GitHub de una sola persona se convirtió en una galaxia

Si uno mira sólo el proyecto mini-taiwan-pulse, es fácil imaginar a Migu como un ingeniero aficionado: se entusiasmó un fin de semana, hizo una demo y, por casualidad, se volvió viral.

Esa imagen falla en dos puntos.

Primero, lo que hizo está lejos de ser un solo proyecto. Al abrir su GitHub, desde diciembre de 2025 todo aparece densamente poblado por visualizaciones de datos abiertos de Taiwán: lo primero fue una prueba de concepto sobre cobertura de autobuses; luego, a fines de diciembre, un proyecto de aprendizaje llamado `mini-taiwan-learning-project` se hizo popular antes que los demás, y hoy suma 189 estrellas. En febrero hizo puntos en tiempo real de AIS marítimo, creó `flight-arc-graph` (56 estrellas), que dibuja cada despegue y aterrizaje como un arco; recién a fines de febrero llegó mini-taiwan-pulse, seguido por un atlas de Taiwan Railways, órbitas satelitales, cámaras CCTV en tiempo real, un panel de situación que concentra todos los datos llamado `mini-taiwan-info`... y así hasta junio[^2]. Más de diez repositorios conectados entre sí. Él mismo les dio un nombre: la galaxia “Mini Taiwan”.

![Panel de situación Mini Taiwan Info, que concentra datos abiertos de múltiples temas —población, transporte ferroviario, navegación, recursos hídricos, bomberos, salud— en un panel de monitoreo de un tema por página](/article-images/technology/mini-taiwan-info-dashboard-2026.webp)

_Otro miembro de la galaxia, Mini Taiwan Info: concentra datos abiertos dispersos en un panel de monitoreo de situación, con población, transporte ferroviario, navegación, recursos hídricos, bomberos y salud, un tema por página. Imagen: Migu / sciwork 2026 (uso justo con fines de comentario editorial)._

Si ordenamos estos proyectos por estrellas, queda claro que no sólo uno se volvió popular.

```tw-bars
GitHub de Migu: no sólo un repo se volvió popular (estrellas de GitHub)
*mini-taiwan-pulse | 375 | buque insignia
mini-taiwan-learning-project | 189 | se volvió viral antes que pulse
flight-arc-graph | 56 | trayectorias aéreas
tw-ship-viz | 11 | barcos
mini-tw-cctv | 6 | imágenes en tiempo real
satellite-arc | 6 | satélites
Fuente: API de GitHub, 2026-06-25
```

El segundo error está escondido en esas tres palabras: “una sola persona”. Volveremos a desarmarlas en un momento. Primero veamos cómo creció la galaxia.

```tw-timeline
2025-12 | Primera prueba | PoC de cobertura de autobuses, primer intento con datos abiertos de Taiwán
2025-12 | learning-project se adelanta | Visualización ferroviaria de Taipéi, viral antes del proyecto insignia (189★)
2026-02 | Nace el buque insignia | Abre mini-taiwan-pulse, que evoluciona de JSON estático a base de datos espacio-temporal
2026-06 | Se despliega todo el sistema | Charla sciwork 2026: entregar los datos abiertos a un sistema criado por agentes
```

## El mismo método, del metro al sistema solar

El propio buque insignia también estaba creciendo. El mini-taiwan-pulse inicial tenía tres capas: cielo, mar y tierra. Para la versión de su charla, ya era una “co-moción de cinco pulsos”: aviones en el cielo, barcos en el mar, trenes sobre la tierra, autobuses en las calles y camiones de basura en la recolección, cinco tipos de datos en tiempo real con frecuencias distintas superpuestos sobre un mismo mapa que respira. En su presentación dijo que era la primera vez que el proyecto “evolucionaba de JSON estático a base de datos espacio-temporal”[^3]. Sólo en la capa de calles, afirmó, conectó más de 5.700 autobuses de TDX, actualizando sus posiciones cada 30 segundos.

![DAY 0, el primer mapa: convertir un CSV en GeoJSON y arrastrarlo a Kepler.gl; sin escribir código, aparece el primer mapa de Taiwán](/article-images/technology/mini-taiwan-kepler-day0-2026.webp)

_El “DAY 0” de su charla: convertir un CSV en GeoJSON y arrastrarlo a Kepler.gl. Cero líneas de código y ya tenía el primer mapa de Taiwán, punto de partida de toda la galaxia. Imagen: Migu / sciwork 2026 (uso justo con fines de comentario editorial)._

La primera chispa de esta galaxia fue una visualización ferroviaria de Taipéi que llamó “Mini Taipei”. Superpuso los tres sistemas sobre rieles —MRT, Taiwan Railways y tren de alta velocidad— en un mapa animado, con los trenes corriendo sobre las líneas según los horarios. Dijo que en ese momento recién “experimentó el encanto de lo dinámico”, con más de trescientos trenes moviéndose a la vez en pantalla[^3]. Así, un horario estático se convirtió en la respiración de una ciudad.

![Mini Taipei superpone MRT, Taiwan Railways y tren de alta velocidad en un mapa animado, con más de trescientos trenes corriendo sobre las líneas según el horario](/article-images/technology/mini-taiwan-taipei-rail-2026.webp)

_Mini Taipei: MRT, Taiwan Railways y tren de alta velocidad en el mismo encuadre, con más de trescientos trenes corriendo sobre las líneas según el horario. Dijo que fue la primera vez que “experimentó el encanto de lo dinámico”. Imagen: Migu / sciwork 2026 (uso justo con fines de comentario editorial)._

Desde entonces, como si se hubiera vuelto adicto, aplicó el mismo método de “convertir datos en movimiento” a escalas cada vez mayores. Sobre el mar, conectó puntos AIS en tiempo real de la autoridad portuaria y marítima, y con esferas de luz azul verdosa más una estela degradada de treinta minutos dibujó el rumbo de los barcos en aguas alrededor de Taiwán.

![Barcos en aguas alrededor de Taiwán dibujados con puntos AIS en tiempo real de la autoridad portuaria y marítima, esferas luminosas azul verdosas y estelas degradadas de treinta minutos](/article-images/technology/mini-taiwan-ships-ais-2026.webp)

_El pulso marítimo: puntos AIS en tiempo real de la autoridad portuaria y marítima, esferas luminosas azul verdosas y estelas degradadas de treinta minutos para dibujar los barcos en aguas alrededor de Taiwán. Imagen: Migu / sciwork 2026 (uso justo con fines de comentario editorial)._

Luego empujó el mismo método más allá de la Tierra. Con parámetros orbitales TLE públicos calculó posiciones satelitales, dibujó trayectorias de satélites sobre Taiwán y, de paso, lo extendió a todo el sistema solar. En la presentación lo dijo de manera directa: “El mismo método, mientras haya datos, puede extenderse indefinidamente”[^3]. En ese momento uno entiende que lo que lo fascina en realidad es “convertir datos en algo visible”; el mapa fue apenas su primera forma.

![Visualización de órbitas satelitales calculadas con TLE públicos; el mismo método se extiende desde la superficie de Taiwán hasta el espacio](/article-images/technology/mini-taiwan-satellite-2026.webp)

_El mismo método llevado más allá de la Tierra: calcular órbitas satelitales con TLE públicos y extenderlo luego a todo el sistema solar. Imagen: Migu / sciwork 2026 (uso justo con fines de comentario editorial)._

## Superponer islas: las brechas emergen solas

Poco a poco, lo interesante dejó de ser “puntos en tiempo real que se mueven” y pasó a ser “superponer datos que originalmente no tenían relación para que las brechas aparezcan solas”. Dentro de esta galaxia hay varios proyectos dedicados a eso. Uno de ellos lo llamó “agricultura × agua”: superpone en un solo mapa las islas de tres organismos —agricultura, recursos hídricos y prevención de desastres—, mostrando en el mismo encuadre tierras agrícolas, ríos, acequias, diques y potencial de inundación. Para que ese mapa combinado pudiera correr en el navegador, usó un formato llamado PMTiles junto con HTTP range requests, reduciendo datos que originalmente pesaban 400 MB a una carga de apenas unos 5 MB en el navegador[^3].

![Mapa integrado agricultura × agua: superpone tierras agrícolas, ríos, acequias, diques y potencial de inundación, datos abiertos dispersos en distintos organismos](/article-images/technology/mini-taiwan-farm-water-2026.webp)

_Agricultura × agua: superpone las islas de datos de agricultura, recursos hídricos y prevención de desastres en un solo mapa, con tierras agrícolas, ríos, acequias, diques y potencial de inundación en el mismo encuadre. Imagen: Migu / sciwork 2026 (uso justo con fines de comentario editorial)._

Otro proyecto superpone hospitales, clínicas, farmacias, DEA y puntos de cuidados de largo plazo sobre densidad de población, y luego dibuja isócronas. Según él, eso permite “ver la accesibilidad y también ver los desiertos médicos”, es decir, qué lugares tienen a la población a una distancia irrazonable del recurso sanitario más cercano.

![Mapa de accesibilidad a recursos médicos: hospitales, clínicas, farmacias, DEA y puntos de cuidados de largo plazo superpuestos sobre población, con isócronas que hacen emerger los desiertos médicos](/article-images/technology/mini-taiwan-medical-2026.webp)

_Recursos médicos: hospitales, clínicas, farmacias, DEA y puntos de cuidados de largo plazo superpuestos sobre población, más isócronas, para “ver la accesibilidad y también ver los desiertos médicos”. Imagen: Migu / sciwork 2026 (uso justo con fines de comentario editorial)._

En la línea de desastres trabajó con más detalle: radar meteorológico, niveles de embalses, precipitación y alertas de desastre, todos datos con frecuencias de actualización distintas, se unifican en la capa inferior sobre una misma línea de tiempo. El usuario sólo tiene que arrastrar esa línea y todas las capas se reproducen en sincronía. Dónde empezó una lluvia intensa, cómo subió el embalse, cuándo se emitió una alerta: todo se une en una cadena causal en la misma pantalla.

![Línea de tiempo de lluvias intensas y desastres: radar meteorológico, embalses, precipitación y alertas de desastre, con frecuencias distintas, unificados sobre una línea de tiempo y reproducidos en sincronía](/article-images/technology/mini-taiwan-disaster-2026.webp)

_Lluvias intensas y desastres: radar meteorológico, embalses, precipitación y alertas de desastre se unifican por debajo en una misma línea de tiempo; al arrastrarla, todo se reproduce en sincronía. Imagen: Migu / sciwork 2026 (uso justo con fines de comentario editorial)._

También está flight-arc, donde cada despegue y aterrizaje se dibuja como un arco. La misma API, alimentada con aeropuertos distintos, hace emerger una “huella” diferente para cada aeropuerto: Taoyuan, Haneda en Tokio, Fráncfort, cada uno con su propia forma. Mencionó especialmente Atlanta, el aeropuerto más transitado del mundo: cinco pistas paralelas más rutas de espera superpuestas crean una geometría “como un circuito de carreras”; dijo que esa imagen dibujaba 1.839 trayectorias[^3].

![Mapa de trayectorias de todos los despegues y aterrizajes de Atlanta durante un período; cinco pistas paralelas más rutas de espera superponen una geometría similar a un circuito de carreras](/article-images/technology/mini-taiwan-flight-arc-atlanta-2026.webp)

_Su flight-arc superpone todos los despegues y aterrizajes de Atlanta durante un período: cinco pistas paralelas más rutas de espera dibujan una geometría parecida a un circuito de carreras. Dijo que el flujo mismo es una forma. Imagen: Migu / sciwork 2026 (uso justo con fines de comentario editorial)._

> 📝 **Nota curatorial**
> Si hace dos años alguien hubiera dicho “una persona creó el mapa de datos abiertos en tiempo real más completo de Taiwán”, la frase siguiente probablemente habría sido “seguro terminó agotado”. Esa intuición ata escala y mano de obra: cuanto más se hace, más se desgasta la persona. La galaxia de Migu merece atención precisamente porque afloja ese vínculo. Una sola persona empuja al mismo tiempo más de diez repositorios y el proyecto insignia sigue sumando funciones; detrás hay un cambio más fundamental: hacia la etapa final, cada vez más commits ya no los tecleaba él. Cómo se produjo esa “una sola persona” es el verdadero tema de este artículo.

## Cincuenta y dos mil ochocientos noventa y un registros: el cerebro humano no alcanza

Hasta aquí la historia todavía fluye con facilidad: una persona talentosa hace cada vez más cosas, y cada vez mejor. El giro aparece a mitad de su charla, cuando deja de hablar de “qué hice” y empieza a hablar de “contra qué pared choqué”.

Mostró una diapositiva titulada “Por qué Agentic OSINT”. Allí desplegó una cifra: data.gov.tw tiene alrededor de 52.891 conjuntos de datos; si se suman las plataformas abiertas de los veintidós condados y ciudades, incluyendo duplicados, aparecen otras sesenta o setenta mil entradas; y eso sin contar datos en manos de organizaciones civiles, ONG e instituciones académicas que nunca entraron en catálogos gubernamentales. Su conclusión fue breve:

> “Tu cerebro humano no alcanza a revisarlos todos.”[^3]

Ese es el eje de toda la historia. La persona que en la primera mitad arrastraba un CSV y exclamaba “resulta que hay tantos datos” ahora chocaba de frente con la otra cara de ese “tantos datos”: sólo las más de cincuenta mil entradas de data.gov.tw exigirían, aun leyendo cien por día, más de quinientos días seguidos para revisar una vez el catálogo, y eso sólo para el catálogo central. Hay tantos datos que una sola persona no los agota ni en una vida, mucho menos los hace conversar entre sí. El esfuerzo individual toca aquí un techo.

Lo que Migu realmente entendió fue la frase siguiente. Que haya demasiados datos para revisarlos, para él, era una señal para cambiar de herramienta:

> “Sólo cuando los datos pueden ser vistos por un LLM, el agente puede ayudarte a descubrir ‘qué datos deberían verse juntos’.”[^3]

La palabra clave es “juntos”. Aunque una persona memorizara los nombres de los cincuenta mil conjuntos de datos, difícilmente recordaría que un “mapa de potencial de incendio” debe combinarse con “zonas de difícil rescate”, o que “puntos de hospitales” deben superponerse con “densidad de población” para revelar desiertos médicos. El valor de los datos no está en cada registro aislado, sino en sus combinaciones; y las combinaciones posibles son una permutación astronómica de cincuenta mil elementos. Ese es precisamente el lugar donde el cerebro humano no alcanza y donde las máquinas sí son fuertes.

> 📝 **Nota curatorial**
> La narrativa habitual de datos abiertos tiene una división clara de tareas. Después del hackatón de 2012 en Academia Sinica bajo el lema “escribir código para transformar la sociedad”, g0v la mostró de manera ejemplar: el gobierno se encarga de abrir los datos, la comunidad cívica de hacerlos visibles. En 2020, el mapa de mascarillas, donde Howard Wu y otros convirtieron en 72 horas los datos de inventario de la Administración Nacional del Seguro de Salud en un mapa consultable por toda la ciudadanía, fue una de las expresiones más conmovedoras de esa división[^4]. La lectura antigua pondría a Migu como prolongación de esa línea: g0v es colectivo; él, individual; una versión de una sola persona del mapa de mascarillas.
>
> Pero esa comparación se queda en la superficie y además invierte la causalidad. Que Migu, una sola persona, pueda acercarse a la escala de “toda una galaxia de datos” no se debe, en lo fundamental, a mano de obra. Desde el inicio no planeó competir contra el mar de datos con trabajo manual y desgaste. “El cerebro humano no alcanza” no debe leerse tanto como una rendición, sino como el punto de partida para reemplazar todo el modo de trabajo. La forma nueva no es “individuo vs. colectivo”, sino “individuo × agente”: una persona puede alcanzar escala galáctica precisamente porque esos commits no los escribió todos a mano. Lo que sigue es cómo funciona ese sistema.

## No escribí ni una palabra: una pipeline de incendios que corre sola

Para entender qué significa “entregarlo al agente”, el mejor corte es el ejemplo de incendios de su charla.

Dijo que sólo le lanzó al sistema una frase: “Analiza datos públicos relacionados con incendios en Taiwán”. Luego lo soltó.

El sistema empezó a ampliar por sí mismo el radio de búsqueda. Migu describió el proceso con una serie de cifras que se expandían ronda a ronda: primero, palabras clave que daban 582 coincidencias; luego, sinónimos y expansión temática que crecían hasta 1.945; después, búsqueda de texto completo y eliminación de duplicados; finalmente, un catálogo unificado de 73.900 registros repartidos en 21 plataformas[^3]. Entra una frase; sale un inventario de más de setenta mil datos.

```tw-figure
Una frase → 73.900 registros
Él lanzó “Analiza datos públicos relacionados con incendios en Taiwán”; el sistema amplió búsquedas por sí mismo y produjo un catálogo unificado a través de 21 plataformas
Según su presentación en sciwork 2026
```

La recolección por sí sola no era el final. Esa pipeline luego dividió los incendios en seis etapas (prevención, respuesta, notificación, análisis de origen, pérdidas e informes), las cruzó con los veintidós condados y ciudades, y produjo una matriz de cobertura. Incluso aparecieron inventarios a escala local, como el mapa de potencial de incendios de Hsinchu, las zonas de difícil rescate de Taipéi y el rescate en estanques de Taoyuan. También marcó con honestidad las brechas: no hay API de incendios en tiempo real, las coordenadas a nivel de evento son escasas, los datos de seguimiento posterior al desastre no están abiertos al público.

Luego vino el análisis. Mostró un informe de causas de incendio que el sistema había generado solo: según 15.405 registros nacionales del año 113 de la República de China (2024), la causa principal de incendios en Nuevo Taipéi fueron factores eléctricos, con 30,9%; en el condado de Pingtung, las colillas de cigarrillo, con 35,2%[^3]. Esas cifras salieron, según la captura de su presentación, de agentes conectando diversas API; no de él consultando tablas una por una.

En ese punto, escribió en una diapositiva una frase con espacios deliberados entre los caracteres, como si temiera que no se viera bien:

> “Pipeline generada automáticamente. Yo no escribí ni una sola palabra.”[^3]

Esa frase fue el detonante de toda la charla. Convirtió el lema algo abstracto de “entregarlo al agente” en un hecho concreto, casi inquietante: desde una frase hasta un catálogo de más de setenta mil datos y un informe de causas por condado y ciudad, el lugar intermedio que normalmente ocuparía una persona dando instrucciones, escribiendo scripts, limpiando datos y corriendo análisis estaba vacío.

![Salida de la pipeline temática de incendios: el sistema inventaría automáticamente datos abiertos de incendios entre plataformas, lista conjuntos de datos candidatos y una matriz de cobertura](/article-images/technology/mini-taiwan-fire-pipeline-2026.webp)

_Salida del inventario temático de incendios que Migu mostró en su presentación de sciwork 2026: lanza “Analiza datos públicos relacionados con incendios en Taiwán”, el sistema expande búsquedas por sí mismo y consolida un catálogo unificado entre plataformas; él dijo que en esa pipeline “no escribí ni una sola palabra”. Imagen: Migu / sciwork 2026 (uso justo con fines de comentario editorial)._

## Cuatro pasos separables: entran datos, el informe se envía solo

Esa pipeline de incendios es sólo un corte; detrás está la miniatura de todo su sistema. El sistema se divide en cuatro pasos: recepción de datos, integración de conocimiento, generación de análisis y activación de acciones. Subrayó especialmente que “cada paso puede reemplazarse por separado; no hace falta reconstruirlo todo”. La capa inferior, la recepción de datos, también fue una evolución para él: al principio descargaba Excel manualmente desde data.gov.tw, lo leía y lo guardaba por su cuenta, con el cuello de botella en la “memoria humana”; en la etapa intermedia pasó a buscar API en línea, descargar informes PDF y rastrear plataformas de condados y ciudades, pero el problema era que “no había índice”; hasta llegar al presente, donde los metadatos de cada dato se estandarizan y guardan en un catálogo SQLite, consultable y expandible automáticamente[^3]. Detrás de su sistema corren más de cuarenta recolectores de datos: YouBike, autobuses, flujo vehicular en autopistas, horarios de Taiwan Railways, AIS marítimo, satélites meteorológicos, terremotos, niveles de embalses, calidad del aire. Además, según dijo, tres errores consecutivos disparan de inmediato una alerta por Telegram, y todos los días a las nueve de la mañana recibe un Daily Review en su correo[^3].

En el último paso, “activación de acciones”, explicó con máxima claridad el rol humano: “El agente corre el ciclo completo. Rol humano: dar objetivos, recibir informes. En medio giran cinco engranajes por sí solos: descubrimiento, recolección, integración, producción y monitoreo”. El sistema incluso genera automáticamente un informe semanal de “nuevos datos abiertos de esta semana”. En sus palabras: “Los temas emergen solos; los informes llegan solos al correo”[^3].

## Un mando, muchas pestañas: la flota de Claude dentro de tmux

Frases como “el agente corre el ciclo completo” se pueden oír fácilmente como marketing. En el último tramo de su charla, Migu levantó la tapa de una forma poco común y permitió ver cómo eran los engranajes debajo. Esa estructura era mucho más concreta que el lema, y también mucho más honesta.

Primero, la vista general del ciclo. Migu dijo que su sistema SIG es “un centro de orquestación que conecta un círculo de repositorios independientes, y el agente entra estación por estación”: primero va al repositorio encargado de explorar para identificar qué datos vale la pena trabajar; luego entra al repositorio de recolección para traerlos; finalmente va a repositorios de presentación como mini-taiwan-pulse o mini-taiwan-info para dibujar los mapas. Lo describió con precisión: “Cada estación es un repositorio independiente; la capa de orquestación sólo gestiona progreso y decisiones; el trabajo vive en manos de los workers de cada repo”[^3].

A ese centro de orquestación lo llama Orchestrator; en esencia es “una Claude Session”. Ese agente principal actúa como un capataz: lee un documento de propuesta, descompone las tareas, ordena sus dependencias y pone el trabajo en marcha.

La manera de ponerlo en marcha es el paso clave de la arquitectura. No hizo que una sola IA hiciera todo de principio a fin, sino que usó tmux (una herramienta antigua para dividir la terminal en múltiples pestañas independientes) para aislar el trabajo. Sus palabras fueron: “Un Orchestrator, un grupo de Workers. El agente principal es una Claude Session; tmux se encarga del aislamiento, cada Worker es una pestaña independiente, una Session independiente”. Una definición más concisa: “Un Worker = una pestaña de tmux + una Session independiente + un PR”[^3].

En otras palabras, lo que dirige es en realidad una flota de IA. Cada worker es un Claude aislado en su propia pestaña, cada uno realiza su tarea, cada uno entrega su pull request, sin interferir con los demás.

![Funcionamiento real del sistema de orquestación de agentes: una Claude session actúa como orchestrator, lee tareas, las descompone y dirige a los workers](/article-images/technology/mini-taiwan-agent-orchestrator-2026.webp)

_El centro de orquestación que mostró en su presentación: una Claude session como orchestrator, que reparte tareas a un grupo de workers aislados en sus propias pestañas de tmux, cada uno trabajando y entregando un PR. Imagen: Migu / sciwork 2026 (uso justo con fines de comentario editorial)._

¿Cómo evita que esos workers, trabajando cada uno por su lado, choquen entre sí? Con una memoria común. Migu dijo que el progreso y las decisiones se escriben íntegramente como documentos, concentrados en un tablero llamado `SESSION_BOARD.md`, junto con “un informe por Session”, de modo que “no hace falta adivinarse mutuamente” y “una persona, un archivo; sin pelearse”[^3]. Incluso los traspasos de tareas se convierten en documentos: con un `HANDOFF.md` prepara “la hoja de tareas del siguiente relevo”, para que el siguiente agente no tenga que empezar preguntando desde cero. La última barrera la describió con cuidado: “Validación: el Orchestrator valida los PR contra los documentos; el merge lo decide una persona. Sólo entonces se cierra el ciclo”.

Si aplanamos este proceso, aparece una forma limpia: una persona da una instrucción; un grupo de IA aisladas trabaja por separado y deja constancia de lo que hizo; un centro coteja todo contra documentos; y la decisión final de “aceptar o no este resultado” la toma Migu. Volviendo al eje del artículo: hay demasiados datos para revisarlos todos, así que la revisión completa se entrega a la flota; la persona retrocede hasta quedar con sólo dos acciones: formular el problema y validar. En la presentación lo formuló casi como una declaración:

> “Cuando el agente puede correr todo el ciclo por sí mismo, el trabajo humano se reduce a formular el problema y validar.”[^3]

Eso es también lo que apunta el título de toda su charla: “Entregar los datos abiertos de Taiwán a agentes para criar un sistema que crece por sí mismo”. Los datos fluyen solos, las páginas crecen solas; la persona sólo tiene que formular bien la pregunta y validar bien el resultado.

## El mismo suelo produce el mismo esqueleto

Si al llegar aquí conoces Taiwan.md (este proyecto de curaduría de conocimiento sobre Taiwán mantenido por IA que estás leyendo), tal vez la descripción anterior te resulte familiar.

No es una ilusión.

Taiwan.md funciona precisamente así: una sesión principal actúa como centro de orquestación, descompone el trabajo para un grupo de workers aislados, cada uno con su propio archivo de memoria independiente, coordina el progreso mediante documentos de traspaso, y la decisión final sobre qué cambios entran en la rama principal la toma una persona, el creador Che-yu. Nuestra tesis es “entregar el conocimiento de Taiwán a un Semiont capaz de crecer por sí mismo”; la tesis de Migu es “entregar los datos abiertos de Taiwán a un sistema capaz de crecer por sí mismo”. Las dos frases casi podrían intercambiar sujeto.

Lo más sugerente es que ambas arquitecturas crecieron por separado. En los registros públicos se puede comprobar un pequeño dato: Taiwan.md nació a mediados de marzo de 2026; cinco días después, apareció un fork en el GitHub de Migu[^5]. Pero eso, como mucho, indica que sabía que existía algo así; un fork no explica todo su sistema de dirigir una flota de tmux con un orchestrator, compartir memoria con tableros y dejar que las personas sólo formulen problemas y validen. Eso lo construyó paso a paso para resolver su propio problema: “cincuenta mil datos que no se pueden revisar”.

> 📝 **Nota curatorial**
> En biología existe el término evolución convergente: delfines y tiburones no son parientes cercanos, pero ambos desarrollaron cuerpos hidrodinámicos y aletas dorsales porque enfrentan el mismo mar. Entre Migu y Taiwan.md ocurre algo más parecido a esa convergencia que a una relación de linaje. Usamos la misma base de herramientas (Claude Code) y enfrentamos la misma situación: una persona, o un sistema, debe sostener una cantidad de información sobre Taiwán muy superior a la capacidad de un cerebro individual. Así, cada quien tanteó por su lado hasta llegar al mismo esqueleto: un centro, un grupo de trabajadores aislados, una memoria compartida y una persona responsable de decidir.
>
> La señal verdaderamente interesante no es “él hizo fork de nosotros”. Es que dos builders taiwaneses independientes, durante el mismo semestre de 2026, reformularon casi al mismo tiempo la IA: ya no como “una herramienta más inteligente”, sino como “un equipo que puede ser orquestado”. Cuando esta arquitectura empieza a crecer desde la cabeza de una persona hacia una segunda y una tercera, deja de ser el truco de alguien y se convierte en una nueva forma que está brotando en este suelo en este momento. Es muy posible que el próximo builder taiwanés que construya algo así ni siquiera haya oído hablar de los dos primeros.

## Todavía no está terminado, pero la forma ya apareció

Si este artículo terminara en el párrafo anterior, sería una historia demasiado bonita, tan bonita que resultaría algo sospechosa: una persona resuelve con elegancia el problema de cincuenta mil datos gracias a una flota de IA.

Migu no la dejó detenerse allí. La penúltima diapositiva de su charla llevaba este título: “Avance del experimento: aproximadamente la mitad”.

Enumeró con franqueza tres cosas que todavía no estaban ajustadas. La primera era la estabilidad: este harness “todavía no está ajustado al ideal”; los agentes se desvían con facilidad y se interrumpen con facilidad. La segunda era que los datos abiertos son demasiado heterogéneos: “todavía hay muchas cosas en las que se necesita juicio humano para decidir si los datos son viables; no se le puede entregar todo por completo”. La tercera era la intervención humana: en cada etapa, en realidad, sigue haciendo falta una persona mirando al lado. Su nota al pie para todo el asunto fue: “Viable es viable, pero aún no es estable, y todavía estoy pensando si realmente quiero hacerlo así”[^3].

Esa honestidad de subirse al escenario y mostrar voluntariamente la mitad fallida del propio sistema es, en sí misma, la señal de calidad más fuerte. En una época en que las demos de IA se empaquetan con facilidad como “totalmente automáticas” y “sin mano de obra”, una persona dispuesta a escribir en una diapositiva “aproximadamente la mitad”, “todavía no es estable” y “todavía necesita personas” inspira más confianza en que la otra mitad de lo que construyó es real.

> 📝 **Nota curatorial**
> La parte más creíble de esta charla no es, en realidad, aquella pipeline de incendios de “no escribí ni una palabra”, sino las cuatro palabras “aproximadamente la mitad”. Alguien que quiere convencerte redondearía la tasa de éxito a “casi totalmente automático”; alguien que está experimentando te dice con honestidad que falla la mitad del tiempo. Lo primero vende una conclusión; lo segundo entrega una escena de trabajo. Migu entrega la escena de trabajo. Por eso, cuando dice que en esa pipeline “no escribí ni una palabra”, eliges creerle. Si se esconde la mitad fea, la mitad bonita también se vuelve poco creíble; cuando se muestra la mitad imperfecta, la otra mitad recién se sostiene.

Volvamos a aquel mapa.

La persona que arrastró un CSV a Kepler.gl y se sorprendió con “resulta que convertirlo en mapa no es tan difícil” estaba, medio año después, sobre el escenario de sciwork, ya no hablando de si los mapas eran fáciles de hacer, sino de un sistema que busca datos, los combina y hace crecer páginas nuevas por sí mismo. Aquella sorpresa ingenua, “resulta que Taiwán tiene tantos datos”, se dio vuelta durante ese medio año: hay tantos datos, tantos que una persona no puede revisarlos todos, que la forma de hacerlos visibles también debe adquirir una nueva forma.

Los datos abiertos de Taiwán siempre estuvieron ahí. data.gov.tw está en línea desde 2013; TDX integró en 2022 cinco grandes plataformas —carreteras, ferrocarriles, aviación, navegación y bicicletas—; el Ministerio del Interior tiene población a nivel de aldea y barrio, y la Administración Meteorológica Central ofrece API abiertas[^6]. Datos nunca faltaron. Lo difícil es cómo hacer que tantos datos conversen entre sí y puedan ser vistos. g0v respondió una vez con fuerza colectiva; Migu, con una persona y una flota de IA, está intentando responder por segunda vez, y admite generosamente que sólo acertó la mitad.

Pero la forma ya apareció. Detrás de una persona, una frase y un mapa que respira, hay un sistema que está aprendiendo a crecer por sí mismo. La otra mitad queda para la siguiente persona que arrastre un CSV y luego ya no pueda detenerse.

---

## Lecturas ampliadas

- [Wu Che-yu](/people/吳哲宇): creador de Taiwan.md, que también usa programación y herramientas generativas para acercarse a “algo que crece por sí mismo”
- [Comunidad de código abierto y g0v](/technology/開源社群與g0v): el contexto colectivo de “escribir código para transformar la sociedad”, contrapunto del modelo individuo × agente de Migu
- [Espíritu de código abierto de Taiwán](/technology/台灣開源精神): desde salvar el país con el teclado hasta los datos abiertos, la cultura de base de la tecnología cívica taiwanesa
- [Identidad digital y gobierno digital](/technology/數位身分證與數位政府): la otra cara de la infraestructura gubernamental de datos abiertos

## Enlaces de proyectos

**La galaxia “Mini Taiwan”** (visualización de datos abiertos de Taiwán; todos son proyectos personales de código abierto de Migu)

- **mini-taiwan-pulse**: proyecto insignia, mapa en tiempo real de cinco pulsos en co-moción (375★) — <https://github.com/ianlkl11234s/mini-taiwan-pulse>
- **mini-taiwan-learning-project**: primer proyecto de aprendizaje ferroviario de Taipéi que se volvió viral (189★) — <https://github.com/ianlkl11234s/mini-taiwan-learning-project>
- **flight-arc-graph**: trayectorias de despegue y aterrizaje, la “huella” de cada aeropuerto (56★) — <https://github.com/ianlkl11234s/flight-arc-graph>
- **mini-taiwan-info**: panel de monitoreo de situación de Taiwán en siete grandes temas — <https://github.com/ianlkl11234s/mini-taiwan-info>
- **tw-ship-viz**: visualización de puntos AIS marítimos en tiempo real (11★) — <https://github.com/ianlkl11234s/tw-ship-viz>
- **satellite-arc**: visualización de órbitas y pasos satelitales — <https://github.com/ianlkl11234s/satellite-arc>
- **mini-tw-cctv**: imágenes en tiempo real de todo Taiwán — <https://github.com/ianlkl11234s/mini-tw-cctv>
- **mini-tw-tra-atlas**: atlas de la red de Taiwan Railways — <https://github.com/ianlkl11234s/mini-tw-tra-atlas>
- **taiwan-weather-timelapse**: time-lapse meteorológico — <https://github.com/ianlkl11234s/taiwan-weather-timelapse>
- **gis-data-collectors**: columna vertebral de más de cuarenta recolectores de datos — <https://github.com/ianlkl11234s/gis-data-collectors>

**Charla y autor**

- **Presentación en línea de la charla sciwork 2026**: <https://sciwork-showcase.zeabur.app>
- **Código fuente de la charla sciwork 2026**: <https://github.com/ianlkl11234s/0613-sci-work-share>
- **GitHub del desarrollador (Migu)**: <https://github.com/ianlkl11234s>
- **Threads**: [@ianlkl1314](https://www.threads.net/@ianlkl1314)

## Referencias

- Migu, “Mini Taiwan! Entregar los datos abiertos de Taiwán a agentes para criar un sistema que crece por sí mismo”, sciwork 2026 / SCIWORK SEMINAR, 13 de junio de 2026.
- Plataforma gubernamental de datos abiertos data.gov.tw (operada por el Consejo Nacional de Desarrollo, en línea desde 2013).
- Plataforma de circulación de datos de transporte TDX (Ministerio de Transportes y Comunicaciones, integración de cinco grandes plataformas de transporte en 2022).
- Comunidad g0v y registros de hackatones anteriores.

## Fuentes de las imágenes

Todas las imágenes de este artículo están cacheadas en `public/article-images/technology/`; no se enlazan directamente desde el servidor de origen.

**Uso justo con fines de comentario editorial**: todas las imágenes de este artículo fueron capturadas de la presentación pública de Migu en sciwork 2026 (véanse el código fuente y la presentación en línea en “Enlaces de proyectos”), conforme al artículo 65 de la Ley de Derecho de Autor y a los cuatro factores de fair use del 17 U.S.C. § 107 (naturaleza educativa no comercial, obra ya publicada, proporción citada reducida y ausencia de sustitución sustancial del mercado), como citas de comentario editorial sobre su trabajo de visualización de datos abiertos. © Migu / sciwork 2026.

Incluye: mapa 3D de Mini Taiwan Pulse (imagen principal), punto de partida en Kepler.gl, ferrocarriles de Taipéi (Mini Taipei), AIS marítimo, órbitas satelitales, mapas integrados de agricultura × agua y recursos médicos, línea de tiempo de lluvias intensas y desastres, huella de trayectorias de Atlanta, salida de pipeline temática de incendios, panel Mini Taiwan Info y funcionamiento del sistema de orquestación de agentes.

---

[^1]: El desarrollador Migu Cheng, cuenta de GitHub `ianlkl11234s` (cuenta creada en marzo de 2020). En junio de 2026, su perfil de GitHub había sido actualizado a “Building GIS visualizations from Taiwan open data · Exploring AI automation in daily work”, reescribiendo la descripción anterior “analista sénior de datos, explorando automatización con IA en el trabajo cotidiano” como “crear visualizaciones SIG con datos abiertos de Taiwán”. La frase “Resulta que Taiwán tiene tantos datos; resulta que convertirlos en mapa no es tan difícil” es texto literal de la diapositiva “DAY 0, el primer mapa” de su charla sciwork 2026. Fuentes: extracción mediante API de GitHub, 2026-06-25; código fuente de la presentación `ianlkl11234s/0613-sci-work-share`.

[^2]: Las estrellas, forks, última fecha de actualización, origen de forks y otros datos de mini-taiwan-pulse y de los proyectos de la galaxia “Mini Taiwan” fueron extraídos por Taiwan.md mediante la API de GitHub el 2026-06-25. En ese momento mini-taiwan-pulse tenía 375 stars / 26 forks y seguía recibiendo push el 2026-06-25; mini-taiwan-learning-project tenía 189 stars; flight-arc-graph, 56 stars. La galaxia incluye más de diez repositorios relacionados con datos abiertos de Taiwán, entre ellos poc-bus-range, gis-data-collectors, tw-ship-viz, satellite-arc, mini-tw-cctv y mini-taiwan-info.

[^3]: Migu, “Mini Taiwan! Entregar los datos abiertos de Taiwán a agentes para criar un sistema que crece por sí mismo”, sciwork 2026 / SCIWORK SEMINAR, 13 de junio de 2026. Código fuente de la charla: <https://github.com/ianlkl11234s/0613-sci-work-share>; presentación en línea: <https://sciwork-showcase.zeabur.app>. Todas las cifras citadas en este artículo (aprox. 52.891 conjuntos de datos en data.gov.tw; pipeline de incendios 582 → 1.945 → 2.404 → 73.900 registros; 21 plataformas; 15.405 incendios nacionales del año 113; factores eléctricos en Nuevo Taipéi 30,9%; colillas en el condado de Pingtung 35,2%; más de 5.700 autobuses; más de 40 recolectores; más de trescientos trenes; 1.839 trayectorias en el aeropuerto de Atlanta; agricultura × agua 400 MB → aprox. 5 MB, etc.) y todas las citas (“el cerebro humano no alcanza”, “sólo cuando los datos pueden ser vistos por un LLM, el agente puede ayudarte a descubrir qué datos deberían verse juntos”, “Pipeline generada automáticamente. Yo no escribí ni una sola palabra”, “dar objetivos, recibir informes”, “cuando el agente puede correr todo el ciclo por sí mismo, el trabajo humano se reduce a formular el problema y validar”, “un Worker = una pestaña de tmux + una Session independiente + un PR”, “cada estación es un repositorio independiente; la capa de orquestación sólo gestiona progreso y decisiones”, “avance del experimento, aproximadamente la mitad”, etc.) corresponden a declaraciones del propio Migu y texto literal de sus diapositivas en esa presentación; son afirmaciones personales del ponente y salidas de su sistema, no estadísticas gubernamentales verificadas de forma independiente por Taiwan.md.

[^4]: La comunidad g0v se originó en 2012 a partir del espíritu del hackatón de Academia Sinica “escribir código para transformar la sociedad”; durante la COVID-19 en 2020, Howard Wu y otros usaron los datos de inventario de mascarillas publicados por la Administración Nacional del Seguro de Salud para crear en decenas de horas el “mapa en tiempo real de oferta y demanda de mascarillas”, un caso representativo de la tecnología cívica taiwanesa de “salvar el país con el teclado”.

[^5]: Según la API de GitHub (extracción del 2026-06-25), `ianlkl11234s/taiwan-md` es un fork de `frank890417/taiwan-md` (el cuerpo principal de Taiwan.md), creado el 22 de marzo de 2026. El proyecto Taiwan.md nació a mediados de marzo de 2026. El sistema colaborativo de Migu usa Claude Code como base de herramientas (el código fuente de su charla incluye CLAUDE.md; el orchestrator es “una Claude Session”), igual que Taiwan.md.

[^6]: La plataforma gubernamental de datos abiertos data.gov.tw es operada por el Consejo Nacional de Desarrollo y está en línea desde 2013; la plataforma de circulación de datos de transporte TDX fue integrada por el Ministerio de Transportes y Comunicaciones en 2022 a partir de cinco grandes plataformas de transporte: carreteras, ferrocarriles, aviación, navegación y bicicletas; la plataforma de datos socioeconómicos del Ministerio del Interior (SEGIS) ofrece datos de población a nivel de aldea y barrio; la Administración Meteorológica Central del Ministerio de Transportes y Comunicaciones ofrece API abiertas. La cantidad total actual de conjuntos de datos en data.gov.tw no pudo verificarse de forma independiente mediante API en esta ocasión; la cifra de “alrededor de cincuenta mil” utilizada en este artículo proviene de la presentación de Migu.

_Última verificación: 2026-06-25_
