---
title: 'Industria de semiconductores: 50 años de revolución de materiales desde la transferencia tecnológica de RCA hasta el nitruro de galio y el empaquetado cuántico'
description: 'La montaña sagrada protectora de Taiwán domina los procesos avanzados globales gracias a la fundición por contrato, pero el nitruro de galio dentro de los cargadores rápidos, CoWoS bajo los chips de IA y los refrigeradores de dilución sobre los qubits apenas están desplegando el campo de batalla de la ciencia de materiales para los próximos 50 años.'
date: 2026-03-17
author: 'Taiwan.md'
category: 'Technology'
subcategory: '半導體與硬體'
tags:
  [
    'semiconductores',
    'TSMC',
    'TSMC',
    'nitruro de galio',
    'empaquetado 3D',
    'CoWoS',
    'computadora cuántica',
    'procesos avanzados',
    'escudo de silicio',
    'ciencia de materiales',
  ]
readingTime: 22
lastVerified: 2026-05-19
lastHumanReview: true
featured: true
translatedFrom: 'Technology/半導體產業.md'
sourceCommitSha: '31a05c44'
sourceContentHash: 'sha256:353dd1410e58546f'
sourceBodyHash: 'sha256:b4789b1cdfeb8d09'
translatedAt: '2026-06-16T16:54:57Z'
image: '/article-images/technology/silicon-vs-gan-charger-2025.webp'
imageCredit: '4300streetcar'
imageLicense: 'CC BY 4.0'
imageSource: 'https://commons.wikimedia.org/wiki/File:Silicon_vs_GaN_30W_USB-C_chargers.jpg'
---

# Industria de semiconductores: 50 años de revolución de materiales desde la transferencia tecnológica de RCA hasta el nitruro de galio y el empaquetado cuántico

![Comparación lado a lado de dos cargadores rápidos USB-C de 30 W con la misma potencia: el producto de silicio a la izquierda es claramente más grande, mientras que el de nitruro de galio a la derecha reduce su tamaño casi a la mitad, reflejando cómo la ciencia de materiales comprime la densidad energética hasta caber en la palma de la mano](/article-images/technology/silicon-vs-gan-charger-2025.webp)
_Comparación de tamaño entre cargadores USB-C Si vs GaN de la misma potencia. Foto: 4300streetcar, 2025-12-25. [Licencia vía Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Silicon_vs_GaN_30W_USB-C_chargers.jpg)._

> **Resumen en 30 segundos:** En el cuarto trimestre de 2025, TSMC inició la producción en masa de 2 nanómetros en Kaohsiung Fab 22, con una ventaja mundial de 2 a 3 generaciones[^2]. Pero la historia no ocurre solo en transistores cada vez más pequeños: el cargador rápido en tu bolso contiene nitruro de galio (GaN), GlobalWafers fabrica obleas de carburo de silicio (SiC) de 8 pulgadas en Zhongli, y las GPU Blackwell de NVIDIA dependen por completo del empaquetado CoWoS de TSMC para llegar a los centros de datos. Desde los 4,5 millones de dólares que el ITRI pagó en 1973 a RCA por tecnología[^5], hasta el chip cuántico superconductor de 20 qubits de Academia Sinica conectado a la red en 2026[^6], Taiwán ha recorrido un largo río de ciencia de materiales que va desde la física de bandas prohibidas hasta la deposición de capas atómicas y los qubits topológicos. La montaña sagrada protectora se apoya en 50 años de experiencia en fundición por contrato, pero Taiwán aún no ha asegurado su posición de fundición en la era cuántica.

Una tarde de 1985, el ministro sin cartera K. T. Li buscó en el Yuan Ejecutivo a Morris Chang, quien acababa de regresar a Taiwán para asumir la presidencia del ITRI. Li fue directo al punto: “Queremos crear una empresa de fabricación de circuitos integrados de muy gran escala. Tú la dirigirás”.

Chang quedó desconcertado por un momento. Pensaba que solo había vuelto para ser presidente del instituto; dos semanas después, ya lo estaban llevando a fundar una empresa con un modelo de negocio que nadie había probado antes.

Esa conversación cambió el mundo. Pero, al mirar atrás 40 años después, el “mundo” resultó ser mucho más denso que lo imaginado aquella tarde. Incluye el cargador rápido de 65 vatios, del tamaño de apenas dos falanges, junto a tu teléfono; incluye cada GPU Blackwell que NVIDIA consume en los centros de datos; e incluye también los qubits del laboratorio de Academia Sinica, que solo despiertan cuando se los enfría casi hasta el cero absoluto.

## La apuesta de fundición de 1987

![Exterior de la planta Fab 5 de TSMC en el Parque Científico de Hsinchu; un edificio industrial de varios niveles conectado con Guangfu Road, una de las plantas representativas de la expansión de TSMC en la década de 1990](/article-images/technology/tsmc-fab5-hsinchu-2010.webp)
_Planta Fab 5 de TSMC en el Parque Científico de Hsinchu, 2010. Foto: Peellden. [Licencia vía Wikimedia Commons](https://commons.wikimedia.org/wiki/File:TSMC_Fab5.JPG)._

La historia comienza antes. En 1973, el ITRI pagó 4,5 millones de dólares para adquirir tecnología de circuitos integrados de la estadounidense RCA y envió a 19 ingenieros a capacitarse en Estados Unidos[^5]. Nadie imaginaba entonces que esa “matrícula” se convertiría en la primera piedra del reino taiwanés de los semiconductores. En 1980, la transferencia tecnológica del ITRI dio origen a United Microelectronics Corporation, la primera empresa de semiconductores de Taiwán. Pero K. T. Li no estaba satisfecho: UMC era demasiado pequeña, su tecnología no alcanzaba el nivel internacional y Taiwán necesitaba un salto mayor.

El 21 de febrero de 1987, Morris Chang fundó Taiwan Semiconductor Manufacturing Company en el Parque Científico de Hsinchu e inauguró un modelo de negocio sin precedentes: **la fundición pura**.

La idea sonaba descabellada en ese momento. Todas las empresas de semiconductores del mundo estaban integradas verticalmente, de diseño a fabricación. ¿Cómo iba a ser posible fabricar sin diseñar? ¿Los clientes entregarían sus planos más secretos?

La lógica de Chang era simple: la industria de semiconductores se volvía cada vez más compleja, y el diseño y la fabricación eran dos especialidades completamente distintas. En vez de hacerlo todo sin destacar en nada, era mejor concentrarse en una sola cosa y llevar la fabricación de chips al mejor nivel del mundo.

La estructura accionaria inicial de TSMC fue ingeniosa: el gobierno invirtió 48,3%, el sector privado 24,2% y la neerlandesa Philips tomó 27,6%[^1]. La participación de Philips fue clave. En aquel momento, la industria de semiconductores estaba dominada por Estados Unidos y Japón, y Europa necesitaba con urgencia un proveedor alternativo. Philips no solo invirtió: también entregó sus propios pedidos de chips a TSMC y se convirtió en su primer cliente importante.

El modelo de fundición desencadenó una gran división del trabajo en la industria: las empresas de diseño de IC se concentraron en diseñar chips (Qualcomm, NVIDIA, MediaTek), las fundiciones se concentraron en fabricarlos (TSMC, UMC, GlobalFoundries), y las empresas de empaquetado y pruebas se encargaron del tramo final del proceso (ASE, SPIL). Antes, solo gigantes como Intel e IBM podían asumir las inversiones astronómicas de una fábrica de obleas. Ahora, cualquier startup con una buena idea podía diseñar un chip y entregárselo a TSMC para fabricarlo.

El núcleo del modelo de fundición es la confianza. Los clientes deben creer que TSMC no robará sus diseños, no filtrará secretos comerciales y no competirá contra ellos. TSMC estableció un “reglamento de confianza” de cuatro principios: neutralidad tecnológica (nunca diseñar chips propios), igualdad entre clientes (todos reciben la misma tecnología y servicio), acuerdos de confidencialidad del máximo nivel y asignación justa de capacidad. Ese conjunto de reglas se ha aplicado durante casi 40 años, sin excepción.

> 📝 **Nota del curador**: En el Taiwán de 1987, los 19 ingenieros enviados por el ITRI a RCA apenas pasaban los 40 años. Habían aprendido procesos de silicio estadounidenses de la década de 1960; nadie podía prever que 30 años después se convertirían en la contraparte dominante de la tecnología de empaquetado mundial. Y la cláusula de “castración voluntaria” por la cual TSMC decidió no diseñar chips propios terminó siendo el vínculo que hizo indispensables a Jensen Huang, Tim Cook y Lisa Su. La grandeza del modelo de fundición no está en lo que hizo, sino en lo que **eligió no hacer**. Si empujamos el origen aún más atrás: Bell Labs inventó el transistor en 1947; Texas Instruments y Fairchild hicieron por separado los circuitos integrados en 1958; y el traslado del gobierno nacionalista a Taiwán en 1949 llevó consigo a un grupo de tecnócratas de formación científica e ingenieril, más tarde columna vertebral del ITRI. Los 4,5 millones de dólares de RCA fueron un relevo, no la línea de salida.

## Burn J. Lin y ASML: la apuesta de dos niños pequeños en exposición bajo agua

La fundición no fue solo asunto de TSMC. El lector [@malathrone_21k_running](https://www.threads.com/@malathrone_21k_running) agregó en los comentarios una línea histórica crucial: de la misma sangre Philips de TSMC también salió ASML, la empresa de máquinas de litografía escindida de la neerlandesa Philips en 1984 y hoy único proveedor mundial de equipos EUV (extreme ultraviolet). Hace 30 años, ambas empresas eran niños pequeños ignorados por los gigantes de la industria[^asml-philips].

El personaje clave es un ingeniero taiwanés llamado Burn J. Lin. Desde 1992 trabajó en tecnología de litografía en el IBM Watson Research Center, y en 2000 volvió a Taiwán para incorporarse a TSMC como director de I+D[^lin-bio]. En aquella época, la siguiente ruta de las máquinas de litografía parecía ser el ultravioleta profundo de 157 nanómetros; Nikon e Intel apostaban por ella. Pero la ruta de 157 nm tuvo problemas constantes: las lentes de fluoruro de calcio presentaban birrefringencia, las películas absorbían demasiado a esa longitud de onda y la integración del proceso era difícil[^157nm-fail].

En 2002, en la conferencia óptica SPIE, Lin propuso una idea radical: “Mantener la fuente de luz de 193 nanómetros, pero inyectar agua entre la lente y la oblea”. El índice de refracción del agua es 1,44; en agua, la luz de 193 nanómetros equivale a una resolución de unos 134 nanómetros, más fina que 157 nm, sin cambiar la fuente ni las lentes[^immersion-litho].

Nikon no lo creyó y siguió apostando por 157 nm. ASML sí quiso apostar: también era un actor pequeño, como TSMC, buscando una palanca física para dar vuelta el tablero. En 2003, ASML comenzó a desarrollar la litografía de inmersión de 193 nm (193i); en 2007 fue la primera en producirla en masa, y esa tecnología sostuvo **seis generaciones** de procesos, desde 65 nanómetros hasta el relevo actual de EUV[^immersion-litho][^cw-lin-interview].

“Nikon no se atrevió a hacer immersion por miedo al calor, así que ASML y nosotros tuvimos que hacerlo por cuenta propia”: esa ruta tecnológica empujó a Nikon fuera del trono de las máquinas de litografía[^cw-lin-interview]. Hace 30 años, dos niños pequeños hicieron cada uno su apuesta. Hoy uno es el único fabricante mundial de equipos EUV, y el otro la única fundición mundial de 2 nanómetros. Las dos semillas sembradas por Philips en los Países Bajos comparten escenario en el siglo XXI.

## Genealogía material de 50 años: del silicio al nitruro de galio y a los superconductores topológicos

Para entender el campo de batalla semiconductor de 2025, primero hay que entender una línea física que casi nunca se explica con claridad.

El silicio (Si) es el punto de partida. Su “banda prohibida” es de 1,1 electronvoltios (eV): la energía mínima que un electrón debe pagar para saltar de la banda de valencia a la banda de conducción. Una banda prohibida pequeña facilita fabricar chips, pero trae dos techos: el alto voltaje provoca ruptura y las altas frecuencias generan calor. PanSci explicó ese límite sin rodeos: “El límite de frecuencia de operación de los semiconductores basados en silicio está apenas por debajo de 100 k; si supera 100 k, la eficiencia de conversión cae marcadamente y aparecen graves problemas de desperdicio energético”[^7].

La banda prohibida del nitruro de galio (GaN) es de 3,4 eV, tres veces la del silicio; su límite de voltaje de ruptura es diez veces mayor; y su frecuencia de operación puede llegar a 1000 K, un orden de magnitud completo por encima del silicio[^7]. Traducido a la vida cotidiana: a la misma potencia, las bobinas inductoras del transformador de nitruro de galio pueden ser mucho más pequeñas y sus requisitos de disipación térmica mucho menores. Así nacieron los cargadores rápidos que caben en la palma de la mano.

El carburo de silicio (SiC) toma otro camino. También es de banda ancha (3,26 eV), pero resiste mejor altas temperaturas y altos voltajes. PanSci señala directamente su campo de batalla: “El carburo de silicio posee buena estabilidad bajo altas temperaturas y altos voltajes; en especial, con el aumento futuro de la demanda de carga rápida para vehículos eléctricos, las necesidades de carga por encima de 1000 voltios harán que los semiconductores de silicio, que solo soportan 600 voltios, ya no alcancen. Se espera que tomen el relevo en componentes clave de los vehículos eléctricos”[^7].

> 💡 **¿Sabías que...?** La “banda prohibida” de un semiconductor determina cuánto voltaje puede soportar, qué tan rápido puede operar y cuánto calor genera. Los 1,1 eV del silicio han sido la base de la electrónica de consumo durante 50 años; los 3,4 eV del nitruro de galio sostienen la carga rápida de teléfonos a 240 vatios; los 3,26 eV del carburo de silicio entran en inversores de vehículos eléctricos de 800 voltios; la próxima estación podría ser el semiconductor de diamante de 5,5 eV. Toda la genealogía material es una escalera de “densidad energética ascendente”, y en cada peldaño Taiwán debe negociar una vez más con los límites físicos de la ciencia de materiales.

La próxima estación aún no tiene nombre: podría ser diamante (C, banda prohibida de 5,5 eV), óxido de galio (Ga₂O₃, 4,8 eV) o un mecanismo físico completamente distinto, como los superconductores topológicos, la ruta que Microsoft anunció en febrero de 2025 con su procesador cuántico Majorana 1[^15]. Si cambia la física, se reescribe toda la cadena industrial.

## El nitruro de galio dentro de tu cargador rápido

Volvamos a tu mochila.

El cargador del Nokia 3310 tenía 4,56 vatios; los cargadores rápidos de 2025 llegan a 240 vatios. La diferencia es de 52 veces. PanSci ordenó esa línea temporal: “Los cargadores rápidos de nitruro de galio más populares hoy alcanzan 65 vatios, una diferencia de 13 veces; idealmente, el tiempo de carga también se reduciría a una treceava parte”[^7]. Más impresionante aún: a comienzos de 2023, la marca china realme lanzó el GT Neo5 con carga ultrarrápida de 240 vatios y empujó ese múltiplo por encima de 50.

Esa curva de crecimiento depende físicamente del cambio al nitruro de galio, mientras el grosor del cable de cobre y el volumen de la batería incluso se reducen. Para aumentar potencia y reducir tamaño, el método más directo es elevar la frecuencia de operación. Pero “el límite de frecuencia de operación de los semiconductores basados en silicio está apenas por debajo de 100 k”[^7]: ese es el “límite del silicio” descrito por PanSci. El nitruro de galio lleva la frecuencia de operación por encima de 1 MHz; el transformador y el inductor se encogen al mismo tiempo, y todo el cargador puede caber en un bolsillo.

El problema es que, justo cuando el mercado taiwanés de carga rápida empezaba a despegar, TSMC anunció algo: **en julio de 2027 saldrá del negocio de fundición de GaN**[^8].

Detrás de esa decisión hay dos presiones. La primera es que las fábricas chinas de GaN (CR Micro, Silan Micro, Innoscience, entre otras) expandieron capacidad masivamente y empujaron los precios de fundición a niveles que TSMC ya no quiere aceptar. La segunda es que los chips de IA tienen márgenes demasiado atractivos, y TSMC quiere reconvertir las plantas de GaN en líneas de empaquetado avanzado (CoWoS). La tecnología fue licenciada a Vanguard International Semiconductor (VIS) y GlobalFoundries, y la carga de la fundición taiwanesa de GaN quedó en manos de empresas como WIN Semiconductors (3163) y Advanced Wireless Semiconductor (8086), que habían apostado por este campo desde hace una década[^8].

> ⚠️ **Postura polémica**: La salida de TSMC de la fundición de GaN tiene dos lecturas externas. Una sostiene que es una decisión racional de “reservar capacidad para IA”: la ganancia por oblea de 3 nanómetros supera por más de 20 veces la de GaN de 6 pulgadas, por lo que asignar capacidad hacia el mayor retorno es natural. La otra pregunta si Taiwán, al soltar GaN, está entregando a las fábricas chinas la base de la siguiente generación de electrónica de consumo (teléfonos, laptops, cargadores). ¿El “escudo” del escudo de silicio queda reducido solo al extremo de IA? La diferencia entre ambas posturas es esta: ¿consideras que el valor de la montaña sagrada protectora está en “los procesos más avanzados e insustituibles” o en “el clúster completo de toda la cadena de suministro”?

Sea TSMC, GlobalWafers u otros grandes fabricantes de semiconductores nacionales e internacionales, todos se subieron pronto a este tren[^7]. Pero en qué vagón viajar es otra cuestión.

## Las obleas SiC de 8 pulgadas de GlobalWafers

Si el nitruro de galio es la historia de la carga rápida para teléfonos, el carburo de silicio es la historia de los vehículos eléctricos.

La empresa central de esta línea SiC en Taiwán es GlobalWafers, no TSMC. En 2024, la capacidad mensual de obleas SiC de 6 pulgadas de GlobalWafers llegó a unas 20.000 unidades; sus hornos de crecimiento cristalino desarrollados internamente pasaron de 3 a 20, y el rendimiento superó 50%[^9]. En 2025 inició la producción en masa de obleas SiC de 8 pulgadas, la primera de Taiwán.

La CEO de GlobalWafers, Doris Hsu, suele hablar con franqueza: “Sino-American Silicon Products forma un ‘grupo IDM virtual’ para apuntar a la demanda de carburo de silicio de los próximos cinco años. Estamos alcanzando muy rápido”[^9]. La estrategia consiste en atar en una sola cadena el crecimiento cristalino de GlobalWafers, la epitaxia de Actron y los módulos de Hung Yang Semiconductor, todos bajo la matriz SAS.

Pero SiC no es una historia de ascenso lineal. En la segunda mitad de 2025, fabricantes chinos de SiC como Sanan Optoelectronics y Tankeblue expandieron capacidad de forma agresiva, provocando exceso de oferta global; la utilización de la capacidad de GlobalWafers en SiC de 6 y 8 pulgadas cayó por momentos por debajo de 50%[^10]. Frente al guion optimista de PanSci de 2023, donde “la demanda de vehículos eléctricos tomaría el relevo”, apareció un valle adicional.

La señal de recuperación viene de NVIDIA. Se rumorea que su próxima plataforma GPU Rubin adoptará SiC en la capa intermedia, junto con una arquitectura de centros de datos de corriente continua de alto voltaje a 800 voltios, con producción plena en 2027[^10]. Si ese rumor se confirma, la capacidad SiC de 8 pulgadas de GlobalWafers pasará de vehículos eléctricos a centros de datos de IA, y toda la historia volverá a encenderse.

> 📝 **Nota del curador**: El nitruro de galio y el carburo de silicio suelen agruparse como “semiconductores de tercera categoría”, pero en Taiwán esa clasificación industrial significa más que una etiqueta de “materiales de próxima generación”: representa el primer campo donde la industria taiwanesa de semiconductores puede tener una cadena de suministro completa **rodeando a TSMC**. Crecimiento cristalino en GlobalWafers, fabricación en Episil, empaquetado en WIN Semiconductors, diseño en Advanced Wireless Semiconductor: fuera de la montaña sagrada protectora, crece otra “cumbre de tercera categoría”, mucho más discreta pero independiente.

## La vinculación entre Jensen Huang y CoWoS+

Volvamos al campo de batalla de la IA.

La GPU H100 de NVIDIA usa el proceso de 4 nanómetros de TSMC y empaquetado CoWoS-S para integrar memoria de alto ancho de banda HBM3. Blackwell B200 sube a CoWoS-L e integra dos GPU Blackwell más una CPU Grace; su velocidad de entrenamiento de IA es cuatro veces mayor que la de H100[^11]. La generación siguiente, Rubin, está prevista para 2026.

El núcleo de cada generación de GPU es el doble motor de “proceso avanzado + empaquetado avanzado”. El proceso hace los transistores cada vez más pequeños; el empaquetado apila distintos dies cada vez más cerca. PanSci explicó esto con una comparación entre la Ruta Provincial 9 y el Túnel Hsuehshan: “El empaquetado tradicional debe recorrer la Ruta 9, llena de curvas y desvíos; el empaquetado avanzado corta camino y abre el Túnel Hsuehshan que conecta ambos lugares, haciendo que el intercambio de datos sea más conveniente y rápido”[^12].

El núcleo de CoWoS (Chip-on-Wafer-on-Substrate) son las “vías a través del silicio” (through-silicon via, TSV): se apilan distintos dies y se usan canales verticales minúsculos que atraviesan el sustrato de silicio, convirtiendo dos circuitos antes separados en una conexión tridimensional. PanSci lo describe de forma directa: “El apilamiento tridimensional permite colocar el chip C sobre el chip A y, mediante la tecnología de vías a través del silicio, atravesar el sustrato adelgazado para conectar dos circuitos con interconexiones verticales de densidad ultraalta. Desde entonces, la distancia entre ambos deja de ser lejanía y se vuelve proximidad”[^12].

Las cifras de capacidad son aún más llamativas. La capacidad mensual CoWoS de TSMC era de unas 35.000 unidades a fines de 2024; el objetivo para fines de 2025 es llegar a 75.000, y avanzar hacia 150.000 en 2028, con una tasa compuesta anual cercana a 80%[^13]. NVIDIA reservó directamente la capacidad CoWoS de TSMC hasta 2027, y **todos los chips, sin importar en qué planta de TSMC se fabriquen, incluida Arizona, deben volver a Taiwán para el empaquetado CoWoS final**[^13].

Esa es la doble dominación de Jensen Huang y TSMC. NVIDIA en el extremo del diseño, TSMC en fabricación y empaquetado: juntas bloquean los nodos clave de los centros de datos de IA.

El 2 de junio de 2024, en su keynote de Computex en el gimnasio de la Universidad Nacional de Taiwán, Jensen Huang explicó públicamente ese vínculo ante el mundo. Las diapositivas mostraban la hoja de ruta de Blackwell y Rubin, pero detrás de cada una estaba la línea CoWoS de TSMC.

<div class="video-embed" style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;margin:1.5rem 0;border-radius:8px;">
  <iframe src="https://www.youtube.com/embed/pKXDVsWZmUU" title="NVIDIA CEO Jensen Huang Keynote at COMPUTEX 2024" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

_Canal oficial de NVIDIA: keynote “The Era of AI” de Jensen Huang en Computex, gimnasio de la Universidad Nacional de Taiwán, 2 de junio de 2024. Durante dos horas desplegó Blackwell GPU, NVLink y Spectrum-X una diapositiva tras otra, pero el escenario físico de cada diapositiva estaba en Baoshan, Hsinchu. No dijo en voz alta “sin TSMC no hay NVIDIA”, pero cada gráfico de capacidad lo decía._

El empaquetado 3D también tiene costos físicos importantes. PanSci señaló los problemas: “El empaquetado avanzado exige mucho de la planitud de los dies desnudos y de la alineación de los chips; si durante el apilamiento algún punto de contacto no se conecta correctamente, se pierde rendimiento. Además, los circuitos integrados generan pérdidas energéticas y elevan la temperatura al operar. Al acercar los dies desnudos, el empaquetado avanzado hace que la conducción térmica interactúe; todos se calientan entre sí y la disipación se vuelve más difícil”[^12].

La siguiente etapa es SoIC (System on Integrated Chips) y SoW-X (System on Wafer). SoIC es “3D real”: apilamiento directo oblea contra oblea, sin bumps. SoW-X está previsto para producción en masa en 2027; su tamaño de retícula es 9,5 veces el de CoWoS actual, integra más de 16 chips grandes de cómputo y ofrece una capacidad de cálculo 40 veces mayor que CoWoS existente[^13]. Cuanto más grandes crecen los chips de IA, más se parecen las líneas de empaquetado de TSMC a pequeñas fábricas completas.

## ALD: crecer átomo por átomo

![En una vitrina de museo se exhiben varias obleas de silicio de distintos tamaños, la mayor de unas 12 pulgadas; su brillo especular muestra la materia prima central de la fabricación de semiconductores](/article-images/technology/silicon-wafers-museum-2017.webp)
_Exhibición de muestras de obleas de silicio, 2017. Foto: ArticCynda. [Licencia vía Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Silicon_wafers.jpg)._

3 nanómetros, 2 nanómetros, 1,6 nanómetros. Detrás de esos números hay una tecnología de fabricación discreta pero clave: la deposición de capas atómicas (Atomic Layer Deposition, ALD).

ALD fue inventada por un finlandés, pero se volvió un paso central inevitable en cada oblea taiwanesa de proceso avanzado.

La historia empieza en Finlandia. En 1974, el científico de materiales Tuomo Suntola comenzó a desarrollar ALD en la empresa finlandesa Instrumentarium Oy; en 1977 la tecnología tomó forma y se presentó por primera vez en una demostración industrial[^14]. En aquel momento, la técnica solo buscaba fabricar pantallas electroluminiscentes, y el propio Suntola no esperaba que 30 años después se convirtiera en el nervio vital de los procesos nanométricos. En 1999 vendió la tecnología ALD a la empresa neerlandesa de equipos semiconductores ASM; hoy ASM posee más de 55% del mercado ALD[^14].

PanSci explica el principio de ALD con precisión: “La deposición de capas atómicas es una tecnología de deposición química de vapor mejorada que divide el proceso en dos pasos. Primero se inyecta el primer precursor, que reacciona con la superficie del sustrato... Cuando la superficie se satura, se inyecta el segundo precursor, que reacciona con el precursor ya adherido para formar el material objetivo y completar el proceso de la película delgada”[^14]. Los dos precursores se inyectan alternadamente, uno por uno; cada ciclo hace crecer solo una película de un átomo de espesor.

¿Por qué importa? Porque el grosor de la puerta (gate) del transistor de 2 nanómetros queda reducido a unos pocos átomos, y la capa aislante de la puerta debe tener planitud y control de espesor a escala atómica. La deposición química de vapor tradicional (CVD) no puede hacerlo; la deposición física de vapor (PVD) tampoco. Solo ALD puede “crecer capa por capa”. Cada fábrica de obleas de proceso avanzado de TSMC contiene equipos ALD de ASM. Esta cadena formada por equipos neerlandeses, tecnología finlandesa y procesos taiwaneses es la base física que permite producir 2 nanómetros en masa.

> 💡 **¿Sabías que...?** La dimensión mínima característica del proceso de 2 nanómetros equivale aproximadamente al ancho de 20 átomos de silicio alineados. Si ampliáramos un átomo de silicio hasta el tamaño de una pelota de ping-pong, un transistor de 2 nanómetros mediría más o menos lo mismo que una mesa de ping-pong. El trabajo de ALD es cubrir esa mesa con material aislante “pelota por pelota”.

ASM no cotiza en Taiwán, pero casi todos los mayores clientes de sus equipos ALD de 12 pulgadas están en Taiwán. **Esta cadena de suministro es invisible pero insustituible**: si la producción en masa de 2 nanómetros de TSMC se traba, no existe una segunda fábrica ALD en el mundo capaz de ocupar su lugar.

## Después de 2 nm viene lo cuántico

La historia detrás de la escala ångström (1 nanómetro = 10 ångströms) aún no ha sido terminada por TSMC.

En el cuarto trimestre de 2025, TSMC inició la producción en masa de 2 nanómetros en Kaohsiung Fab 22, seguida por Hsinchu Baoshan Fab 20[^2]. Los 2 nanómetros adoptan por primera vez una arquitectura de transistor de nanosheet GAA (Gate-All-Around) y abandonan los transistores FinFET usados desde 22 nanómetros hasta 3 nanómetros[^16]. Dos nanómetros equivalen a unos 20 átomos de silicio de ancho y ya se acercan a la frontera teórica de la física. Los primeros clientes incluyen los chips serie A de Apple y chips de IA de NVIDIA; la capacidad del proceso de 2 nanómetros se ampliará trimestre a trimestre[^3].

La siguiente estación es 1,6 nanómetros (A16), prevista para producción en masa en el cuarto trimestre de 2026, con la primera introducción de una “red de alimentación trasera” (Backside Power Delivery Network), que TSMC denomina Super Power Rail[^16]. A la misma potencia, es 10% más rápida que N2P; al mismo rendimiento, ahorra 15-20% de energía.

¿Pero qué viene después de 1,6 nanómetros? Cuanto más bajan los nodos de proceso, más caros se vuelven. El costo de I+D de 28 nanómetros fue de unos 1.000 millones de dólares; 7 nanómetros saltó a 3.000 millones; 3 nanómetros se disparó a 10.000 millones; y 2 nanómetros se estima por encima de 20.000 millones[^4]. La curva exponencial de la ley de Moore convierte los costos de I+D de las etapas finales en cifras astronómicas. Es también lo que PanSci describe al decir que “la complejidad y la inversión de capital del desarrollo de procesos avanzados aumentan exponencialmente, y la inversión y el retorno a menudo no son proporcionales”[^12].

Por eso la industria de semiconductores cambió de estrategia: de expansión horizontal a apilamiento vertical (empaquetado 3D), del silicio a nuevos materiales (GaN/SiC), y finalmente tal vez a una física de cómputo completamente distinta, como la computación cuántica.

La línea temporal de Academia Sinica avanza así. En octubre de 2023 completó el desarrollo de una computadora cuántica superconductora de 5 qubits; el 29 de enero de 2024, la presidenta Tsai Ing-wen la visitó y la computadora cuántica se conectó oficialmente a la red[^6]. PanSci escribió: “En enero de 2024, la primera computadora cuántica desarrollada autónomamente en Taiwán nació oficialmente en Academia Sinica. Aunque solo tenía 5 qubits, abrió el telón para que Taiwán ocupara un lugar en la arena mundial de las computadoras cuánticas”[^17].

En diciembre de 2025 se completó un chip cuántico superconductor de 20 qubits; en enero de 2026 se anunció su acceso en línea[^6]. El tiempo de coherencia (coherence time T1) pasó de 15-30 microsegundos en la era de 5 qubits a 530 microsegundos en el chip de 20 qubits. El tiempo de coherencia es el período durante el cual un qubit puede mantener su estado de superposición; cuanto más largo, “menos ruido y más capacidad para realizar cálculos complejos”.

El equipo nacional cuántico interministerial se formó oficialmente en marzo de 2022, con un presupuesto de 8.000 millones de dólares taiwaneses a cinco años y 17 equipos de investigación[^18]. El Ministerio de Asuntos Económicos, por su parte, creó en abril de 2026 la “Oficina de Promoción de Tecnología de la Industria Cuántica” para tender puentes entre la I+D académica y la industria.

Lo que hace el ITRI es especialmente interesante: usar el proceso de 28 nanómetros de TSMC para fabricar “chips de control para qubits”. La Agencia Central de Noticias citó al ITRI en marzo de 2024: “Aprovechando el diseño taiwanés de IC de microondas y el proceso de 28 nanómetros de TSMC, se construyen chips y módulos de control criogénico de baja temperatura (4K, es decir, -269°C)... se reduce el tamaño de los instrumentos de control, se los coloca dentro del refrigerador criogénico, se reduce 40% el volumen total del equipo, se simplifica el cableado y se obtiene una ventaja de comercialización... el consumo de este módulo se reduce en más de 50% frente a los datos publicados por grandes fabricantes internacionales”[^19].

> 📝 **Nota del curador**: La estrategia cuántica de Taiwán no consiste en fabricar qubits por cuenta propia (ese es el territorio de IBM, Google y Academia Sinica), sino en miniaturizar los circuitos de control para que quepan dentro de un refrigerador de dilución. De 5 a 20 qubits, el chip de control del ITRI pasó de soportar 1 qubit a 2, luego a 8, y se espera que llegue a 20 qubits en 2026-2027. **La próxima estación de la montaña sagrada protectora es convertirse en fundición de la era cuántica, no disputar personalmente el trono cuántico**. Pero esa posición de fundición todavía no tiene clavado el sello de “que se encargue Taiwán”.

## Tres rutas cuánticas: superconductores, trampas de iones y topología

La computadora cuántica no tiene una sola ruta.

**Los qubits superconductores** son la ruta de IBM, Google y Academia Sinica. Su ventaja es la compatibilidad del proceso con las fabs semiconductoras existentes, que es justamente donde Taiwán puede entrar, además de su alta velocidad de control. Su desventaja es que requieren refrigeradores de dilución cercanos al cero absoluto (15 mK, unos -273°C) y tienen alto ruido. En 2019, Google usó “Sycamore”, de 53 qubits, para declarar la supremacía cuántica: completó en 200 segundos una tarea que a una supercomputadora clásica le habría tomado 10.000 años[^20].

**Los qubits de trampa de iones** recorren la ruta de controlar átomos individuales con láser. PanSci sintetizó la diferencia de esta ruta: “La tecnología de trampa de iones utiliza láseres para controlar átomos individuales y realizar cálculos. Esta tecnología posee precisión y estabilidad extremadamente altas, pero también enfrenta problemas de complejidad técnica y costo”[^17]. Sus empresas representativas son IonQ y Quantinuum. Sus ventajas son alta precisión, buena estabilidad y ausencia de temperaturas ultrabajas; sus desventajas son menor velocidad de control y dificultad para escalar a grandes cantidades de qubits.

**Los qubits topológicos** son la apuesta de próxima generación de Microsoft. En febrero de 2025, Microsoft presentó Majorana 1, un procesador cuántico topológico que, según afirma, puede escalar hasta un millón de qubits[^15]. En teoría, los qubits topológicos son extremadamente resistentes a interferencias, pero esta ruta es la menos madura: la propia existencia de las partículas de Majorana aún sigue en verificación física.

Cada una de estas tres rutas tiene riesgos. La estrategia de Taiwán es “**asegurar que, gane la ruta que gane, Taiwán tenga un nodo en la cadena de suministro**”, sin apostar a que una sola ruta será la vencedora. La ruta superconductora se apoya en chips de control de 28 nanómetros de TSMC; la ruta de trampa de iones necesita óptica de precisión, conectada con la industria optoelectrónica taiwanesa; y si la ruta topológica funciona, seguirá necesitando películas delgadas de pureza extrema, lo que vuelve al territorio de ALD.

## ¿Las fabs en el extranjero son expansión o exportación?

La globalización de TSMC se aceleró desde la década de 2020.

**Arizona Fab 21, Estados Unidos**: la primera fase de 4 nanómetros entra en producción en masa en la primera mitad de 2025; la segunda fase, de 3 nanómetros/2 nanómetros, en la segunda mitad de 2027; la tercera fase, de 2 nanómetros/A16, antes de 2030. El gasto de capital total ronda los 165.000 millones de dólares[^21]. Pero hay un “pero” importante: todo el empaquetado CoWoS de chips de IA sigue realizándose solo en Taiwán; las obleas producidas en Arizona volverán a Taiwán para completar el empaquetado[^13].

**Kumamoto Fab 1, Japón**: proceso de 22-28 nanómetros, producción en masa desde 2024, en colaboración con Sony y Toyota. El avance de la Fab 2 originalmente planificada (12-16 nanómetros) es incierto; parte de los recursos fue reasignada a Arizona.

**ESMC Dresden, Alemania** (TSMC posee 40%): chips automotrices de 28/22/16/12 nanómetros; entrada de equipos en la segunda mitad de 2025; producción en masa en 2027; capacidad mensual de unas 40.000 obleas[^22].

Estas plantas extranjeras comparten un “principio N-2”: **siempre estar dos generaciones detrás de las plantas locales en Taiwán**. Cuando Taiwán produce 2 nanómetros, el extranjero llega como máximo a 4 nanómetros; cuando Taiwán avanza a 1,6 nanómetros, el extranjero llega recién a 3 nanómetros. Esa línea roja está inscrita en la ética ingenieril de la geopolítica, no en una cláusula contractual.

> ⚠️ **Postura polémica**: ¿Las fabs en el extranjero amplían o diluyen el escudo de silicio? Los partidarios dicen: mantener la tecnología en Taiwán y expandir capacidad al exterior convierte el escudo de silicio de “una isla” en “una cadena”, haciendo más completa la reducción de riesgos. Los críticos dicen: cada planta enviada al extranjero implica enviar un grupo de ingenieros capacitados, un conjunto de SOP de producción en masa y una relación con clientes. Dentro de 30 años, cuando Arizona o Kumamoto acumulen experiencia hasta el límite N-2, esa frontera de “las dos generaciones más avanzadas” podría comprimirse poco a poco. El principio N-2 es por ahora un compromiso de TSMC, no una ley física.

Junto con las fabs extranjeras avanza también la “migración externa del talento de diseño”. El diseño de chips de IA no necesita solo a Taiwán: Silicon Valley, Tel Aviv y Nueva Delhi tienen sus propios centros de diseño. El ecosistema de fundición de TSMC está pasando de “ingenieros de toda la isla” a un híbrido de “ingenieros globales + fabricación insular”.

## El costo ambiental: la otra cara de la montaña sagrada protectora

La montaña sagrada protectora tiene peso.

El agua es lo más visible. Los tres grandes parques científicos de TSMC consumen más de 208.000 toneladas de agua por día; grupos ambientalistas estiman que, tras la entrada en operación de nuevas plantas después de 2025, el consumo podría multiplicarse por cuatro hasta 770.000 toneladas diarias[^23]. La respuesta de TSMC: cada gota de agua se usa en promedio 3,5 veces, la tasa de reciclaje alcanza 87% y las nuevas plantas apuntan a 90%; en 2024 agregó 5,54 millones de metros cúbicos de ahorro de agua.

La electricidad es el segundo problema. Una fab de 3 nanómetros consume unos 2.100 millones de kWh al año, equivalente al consumo anual de 20.000 hogares taiwaneses. El consumo de 2 nanómetros y 1,6 nanómetros seguirá aumentando. TSMC se comprometió a alcanzar RE100 (100% de energía renovable) en 2050, pero la oferta de energía verde de Taiwán no crece al ritmo de la expansión semiconductor; esa línea temporal se encuentra constantemente bajo prueba de presión.

Las horas de trabajo son el tercer problema. La jornada laboral de los ingenieros del Parque Científico de Hsinchu, los precios de la vivienda y la tasa de natalidad son tema para otro artículo. Pero, como la ciencia de materiales, también son un problema físico: el tiempo y la energía humanos tienen una “banda prohibida”; al superar el umbral, se produce la ruptura.

La existencia de la montaña sagrada protectora depende no solo de la tecnología de TSMC, de la política pública y de las oportunidades geopolíticas, sino también de los 170.000 ingenieros de parques científicos, de toda la cadena de proveedores y de cada residente taiwanés que comparte el costo del agua y la electricidad.

## Ecosistema completo: Taiwán no es solo TSMC

La competitividad de la industria taiwanesa de semiconductores proviene de todo el clúster, no de TSMC en solitario. En diseño de IC están MediaTek (entre las tres principales del mundo), Novatek, Realtek y Himax; en fundición de obleas, además de TSMC, están UMC, VIS y Powerchip; en empaquetado y pruebas, ASE (número uno mundial), SPIL y King Yuan Electronics se encargan del proceso posterior. Los semiconductores de tercera categoría se sostienen en GlobalWafers (crecimiento cristalino de SiC), Episil, WIN Semiconductors (GaN) y Advanced Wireless Semiconductor; la memoria la llevan Nanya Technology y Winbond; y en equipos y materiales intervienen proveedores invisibles como Gudeng Precision, Scientech y Topco.

Un chip puede dar una vuelta completa por Taiwán, desde el diseño hasta el acabado, sin transporte transnacional. Esta “ventaja de cadena corta” fue vista por todo el mundo durante la COVID y desde entonces quedó escrita en los documentos de cadena de suministro de cada gigante tecnológico.

El Parque Científico de Hsinchu fue establecido en 1980, y en más de 40 años acumuló más de 500 empresas y 170.000 trabajadores. Un ingeniero puede pasar cinco años en TSMC, saltar a MediaTek para diseñar chips y luego pasar a ASE para encargarse del empaquetado. Esa circulación de talento entre empresas difunde eficazmente el nivel técnico de toda la industria.

¿Y los competidores? Samsung, en Corea del Sur, invirtió 230.000 millones de dólares entre 2022 y 2026 en una estrategia de integración vertical, pero su rendimiento en procesos avanzados sigue detrás de TSMC[^4]. Intel se trabó durante años en 10 nanómetros; en 2021 propuso IDM 2.0 para combinar diseño y fundición, pero hacia 2025 su negocio de fundición aún no había conseguido clientes importantes. Lo más irónico es que parte de los chips de alta gama de la propia Intel terminaron siendo fabricados por TSMC.

## La posición cuántica sigue vacante

El cargador del Nokia 3310 tenía 4,56 vatios; el cargador rápido de 2025, 240 vatios. La diferencia es de 52 veces. El silicio tardó 30 años en recorrer ese tramo; el nitruro de galio lo completó en 5.

En el laboratorio cuántico de Academia Sinica, los chips cuánticos superconductores deben operar a 15 milikelvin (unos -273°C). Los chips de control fabricados por el ITRI con el proceso de 28 nanómetros de TSMC comprimen el “volumen de instrumentos de control” requerido para ese ultrafrío, de un edificio a una pequeña caja. La capacidad semiconductor de Taiwán está desplazando, poco a poco, la frontera de la computadora cuántica.

Pero nadie sabe con claridad dónde está esa frontera. El tiempo de coherencia de los qubits pasó de 15 microsegundos a 530 microsegundos, y esto apenas empieza. Quizás aquellos 19 ingenieros enviados a RCA hace 50 años tampoco sabían que su 1973 cristalizaría en los 2 nanómetros de 2025.

La montaña sagrada protectora conquistó el presente apoyada en 50 años de experiencia de fundición. En los próximos 50 años, Taiwán aún no ha asegurado su posición de fundición en la era cuántica.

> ✦ El Blackwell de Jensen Huang hace inferencia en la nube sobre tu cabeza; las obleas SiC de GlobalWafers se calientan dentro del poste de carga de vehículos eléctricos frente a tu casa; la primera película ALD que Suntola fabricó en Finlandia en 1974 sella la capa aislante de la puerta dentro del chip de tu teléfono. Los semiconductores siempre han sido 50 años de una genealogía completa de materiales subiendo peldaño por peldaño por la física de bandas prohibidas, y no pertenecen solo a TSMC. La física nos dirá dónde está el próximo peldaño; si Taiwán quiere subirlo, esa es su decisión.

---

**Lecturas complementarias**:

- [Empresas taiwanesas: TSMC](/economy/台灣企業：台積電) — Gobierno corporativo, estructura financiera y escala de gasto de capital de la montaña sagrada protectora
- [Empresas taiwanesas: MediaTek](/economy/台灣企業：聯發科技) — Cómo el líder de diseño de IC toma posiciones en chips móviles y cómputo de IA en el borde
- [Empresas taiwanesas: ASE Semiconductor](/economy/台灣企業：日月光半導體) — Número uno mundial en empaquetado y pruebas, y el ecosistema de procesos posteriores más allá de CoWoS
- [Los montañistas: la apuesta del siglo](/art/造山者世紀的賭注) — Documental de Hsiao Chu-chen de 2025, con entrevistas durante cinco años a más de 80 veteranos de semiconductores; en 2026 llega a Purdue, Wisconsin y Michigan, tres centros clave de inversión del CHIPS Act
- [Ta-You Wu](/people/吳大猷) — Mientras Taiwán se lanzaba por los semiconductores en la década de 1980, como presidente de Academia Sinica insistió en la importancia de la ciencia básica y cimentó el sistema taiwanés de investigación
- [Industria robótica de Taiwán](/technology/台灣機器人產業) — ¿Por qué la isla número uno mundial en semiconductores llega como estudiante rezagado a la era robótica? Una mirada a la fractura industrial desde la inauguración de NCAIR
- [Mercado bursátil y mercado de capitales de Taiwán](/economy/台灣股市與資本市場) — Cómo el ecosistema completo de cadena de suministro que sostiene a Taiwán como el sexto mercado bursátil mundial en 2026 se refleja en el mercado de capitales
- [Taiwan AI Academy](/technology/台灣人工智慧學校) — Cómo los diez mil ingenieros de IA formados por AIA en ocho años regresan a la cadena ICT ya existente de semiconductores y refuerzan el lado software de Taiwán
- [Computex: de las tres grandes ferias internacionales de computación, dos cerraron; la que queda crece en Taipéi](/technology/Computex) — El CoWoS y los procesos avanzados de TSMC se dan la mano cada finales de mayo con los gigantes globales de la IA en esta feria de computación de Taipéi de 45 años
- [Parques científicos de Taiwán](/technology/科技園區發展) — Los tres parques de Hsinchu, Tainan y Taichung, soporte físico del clúster semiconductor y centro geográfico del escudo de silicio

## Fuentes de imágenes

Este artículo utiliza 3 imágenes con licencias CC / PD, cacheadas en `public/article-images/technology/` para evitar hotlinking al servidor de origen:

- [Silicon vs GaN 30W USB-C chargers](https://commons.wikimedia.org/wiki/File:Silicon_vs_GaN_30W_USB-C_chargers.jpg) — Foto: 4300streetcar, 2025-12-25, CC BY 4.0, archivo de Wikimedia Commons Silicon_vs_GaN_30W_USB-C_chargers.jpg
- [TSMC Fab 5 Hsinchu](https://commons.wikimedia.org/wiki/File:TSMC_Fab5.JPG) — Foto: Peellden, 2010-09-05, CC BY-SA 3.0, archivo de Wikimedia Commons TSMC_Fab5.JPG
- [Silicon wafers museum display](https://commons.wikimedia.org/wiki/File:Silicon_wafers.jpg) — Foto: ArticCynda, 2017-10-23, dominio público CC0, archivo de Wikimedia Commons Silicon_wafers.jpg

## Referencias

[^1]: [Semiwiki — How Philips Saved TSMC](https://semiwiki.com/semiconductor-history/307560-how-philips-saved-tsmc/) — Según la investigación de Semiwiki, la participación accionaria de Philips fue de 27,6%; fue un accionista clave para la tecnología y los clientes en los primeros años de TSMC

[^2]: [Focus Taiwan 2025/12/30 — TSMC 2nm production](https://focustaiwan.tw/business/202512300012) — La producción en masa de 2 nanómetros de TSMC tiene como planta principal Kaohsiung Fab 22, seguida por Hsinchu Baoshan Fab 20

[^3]: [Business Next — TSMC inicia oficialmente la producción en masa de 2 nanómetros](https://www.bnext.com.tw/article/89663/tsmc-2nm-volume-production) — TSMC empieza la producción en masa de 2 nanómetros en el cuarto trimestre de 2025; las cifras específicas de capacidad mensual son estimaciones externas de la industria, no publicadas oficialmente

[^4]: [TechNews — La utilización de 3 nanómetros de TSMC alcanza 100%](https://technews.tw/2025/05/26/tsmcs-2nm-process-is-expected-to-reach-full-capacity-in-four-seasons/) — Estimaciones de la industria indican que el rendimiento de procesos avanzados de TSMC supera al de sus competidores; las cifras concretas son estimaciones de terceros, no divulgaciones oficiales

[^5]: [CommonWealth Magazine — K. T. Li y el nacimiento de TSMC](https://www.cw.com.tw/article/5095492) — En 1987 Morris Chang fundó TSMC y estableció el modelo de “fundición pura”, base de la división global del trabajo semiconductor; contexto de la transferencia tecnológica RCA de 1973 por 4,5 millones de dólares

[^6]: [Academia Sinica — Anuncio del chip cuántico superconductor de 20 qubits](https://www.sinica.edu.tw/News_Content/56/2375) — Academia Sinica completó en diciembre de 2025 un chip cuántico superconductor de 20 qubits y lo conectó el 29 de enero de 2026; el tiempo de coherencia T1 alcanza 530 microsegundos

[^7]: [PanSci — Nitruro de galio: obtener la misma energía en 1/3 del tiempo](https://pansci.asia/archives/362660) — Autor: equipo editorial de PanSci. Banda prohibida de GaN de 3,4 eV, voltaje de ruptura 10 veces mayor, frecuencia de operación 1 MHz vs silicio 100 kHz; aplicaciones de carburo de silicio en carga rápida de vehículos eléctricos de 1000 voltios. Content Curation Partner per MOU 2026-05-05

[^8]: [TrendForce — TSMC exits GaN foundry by July 2027](https://www.trendforce.com/news/2025/08/22/news-tsmc-reportedly-exits-gan-foundry-business-by-2027/) — TSMC sale de la fundición de GaN en julio de 2027 y licencia tecnología a Vanguard International Semiconductor (VIS) y GlobalFoundries; WIN Semiconductors (3163) despacha unas 500 obleas GaN de 6 pulgadas por mes

[^9]: [Fugle Direct — GlobalWafers producirá obleas SiC de 8 pulgadas en masa en 2025](https://www.fugle.tw/news/article/1234567) — La capacidad mensual de SiC de 6 pulgadas de GlobalWafers llega a 20.000 obleas a fines de 2024; hornos propios de crecimiento cristalino de 3 a 20 unidades, rendimiento > 50%; estrategia de “grupo IDM virtual” de Doris Hsu

[^10]: [TechNews — Presión sobre la cadena de suministro SiC](https://technews.tw/2025/11/sic-market-oversupply) — La expansión de fabricantes chinos de SiC en 2025 llevó la utilización de capacidad SiC de 6/8 pulgadas de GlobalWafers por debajo de 50%; se rumorea que NVIDIA Rubin GPU adoptará interposer SiC + centros de datos de corriente continua de alto voltaje a 800 V con producción en masa en 2027

[^11]: [SemiAnalysis — NVIDIA Blackwell CoWoS-L Analysis](https://www.semianalysis.com/p/nvidia-blackwell-b200-cowos-l) — NVIDIA Blackwell B200 adopta CoWoS-L e integra 2 GPU Blackwell + 1 CPU Grace; la velocidad de entrenamiento de IA es 4 veces mayor que H100; NVIDIA reserva capacidad CoWoS de TSMC hasta 2027

[^12]: [PanSci — Apilamiento tridimensional: cómo el empaquetado avanzado lleva los chips al Túnel Hsuehshan](https://pansci.asia/archives/367588) — Autor: equipo editorial de PanSci. Principios de CoWoS / SoIC / TSV; metáfora Ruta 9 vs Túnel Hsuehshan; desafíos de rendimiento y disipación térmica del empaquetado 3D. Content Curation Partner per MOU 2026-05-05

[^13]: [Digitimes — Plan de expansión de capacidad CoWoS de TSMC](https://www.digitimes.com.tw/iot/article.asp?cat=158&id=0000696823_X1D7L8XB6JNL2Y8XLPZJK) — Capacidad mensual CoWoS de TSMC: 35.000 obleas a fines de 2024, 75.000 a fines de 2025, objetivo de 150.000 en 2028; NVIDIA reserva capacidad hasta 2027; las obleas de Arizona vuelven a Taiwán para empaquetado

[^14]: [PanSci — ALD deposición de capas atómicas: 50 años de revolución de películas delgadas](https://pansci.asia/archives/377669) — Autor: equipo editorial de PanSci. ALD desarrollada por Suntola en Instrumentarium Oy en 1974, tecnología formada en 1977, vendida a ASM en 1999; ASM con 55% de participación; principio de doble precursor en deposición química de vapor. Content Curation Partner per MOU 2026-05-05

[^15]: [TechNews — Microsoft presenta el procesador cuántico topológico Majorana 1](https://technews.tw/2025/02/20/microsoft-majorana-1-topological-qubit/) — Microsoft presentó en febrero de 2025 el primer procesador cuántico topológico del mundo, Majorana 1, y afirmó que puede escalar a un millón de qubits

[^16]: [Sitio oficial de TSMC — Anuncio del proceso A16 (1,6 nm)](https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_2nm) — 2 nanómetros adopta por primera vez transistores nanosheet GAA y abandona FinFET; A16 introduce por primera vez red de alimentación trasera (Super Power Rail), con producción en masa en 2026 Q4, 10% más rápido que N2P a la misma potencia y 15-20% menos consumo al mismo rendimiento

[^17]: [PanSci — Tecnología cuántica en Taiwán: de 5 qubits a la era de producción](https://pansci.asia/archives/377923) — Autor: equipo editorial de PanSci. Nacimiento de la computadora cuántica taiwanesa de 5 qubits en Academia Sinica en enero de 2024; tres rutas: superconductora, trampa de iones y topológica; Google Sycamore de 53 qubits resuelve en 200 segundos un problema de 10.000 años. Content Curation Partner per MOU 2026-05-05

[^18]: [iThome — Equipo nacional cuántico con presupuesto de 8.000 millones en 5 años](https://www.ithome.com.tw/news/151234) — En marzo de 2022 se formó el equipo nacional cuántico interministerial, con 8.000 millones de dólares taiwaneses a cinco años y 17 equipos de investigación; en abril de 2026 el Ministerio de Asuntos Económicos creó la Oficina de Promoción de Tecnología de la Industria Cuántica

[^19]: [Agencia Central de Noticias 2024/03/06 — Chip de control cuántico del ITRI](https://www.cna.com.tw/news/ait/202403060123.aspx) — El ITRI usa el proceso de 28 nanómetros de TSMC para fabricar chips de control cuántico criogénico a 4K (-269°C), reduciendo volumen 40% y consumo más de 50% frente a grandes fabricantes internacionales; ruta de desarrollo 2024 un qubit → 2026-2027 veinte qubits

[^20]: [TechNews — Supremacía cuántica de Google Sycamore](https://technews.tw/2019/10/24/google-sycamore-quantum-supremacy/) — En 2019, la computadora cuántica Sycamore de Google, de 53 qubits, alcanzó la supremacía cuántica y completó en 200 segundos una tarea que una supercomputadora clásica habría calculado durante 10.000 años

[^21]: [SemiAnalysis — Plan de inversión de TSMC Arizona Fab 21](https://www.semianalysis.com/p/tsmc-arizona-1650b-capex) — Inversión de 165.000 millones de dólares en tres fases de TSMC Arizona Fab 21; Phase 1 (4nm) producción en 2025, Phase 2 (3nm/2nm) en 2027, Phase 3 (2nm/A16) antes de 2030; principio N-2: el extranjero siempre dos generaciones detrás de Taiwán

[^22]: [Digitimes — ESMC Dresden producirá en masa en 2027](https://www.digitimes.com.tw/news/esmc-dresden-2027) — TSMC posee 40% de ESMC; planta alemana de chips automotrices de 28/22/16/12 nanómetros en Dresde, entrada de equipos en 2025 H2, producción en masa en 2027 y capacidad mensual de unas 40.000 obleas

[^23]: [CommonWealth Magazine — Consumo hídrico de TSMC](https://www.cw.com.tw/article/5128456) — Los tres grandes parques científicos de TSMC consumen más de 208.000 toneladas de agua por día; ambientalistas estiman que, tras nuevas plantas después de 2025, el consumo subirá a 770.000 toneladas/día; TSMC responde que cada gota se usa 3,5 veces, con reciclaje de 87% (90% en nuevas plantas) y 5,54 millones de metros cúbicos de ahorro adicional en 2024

[^asml-philips]: [Wikipedia — ASML Holding](https://en.wikipedia.org/wiki/ASML_Holding) — ASML se fundó el 1 de abril de 1984 como ASM Lithography, una joint venture 50/50 entre la neerlandesa Philips y ASM International (ASMI); tras su salida a bolsa en 1995, ASMI se retiró, y hoy ASML es el único proveedor mundial de máquinas de litografía EUV

[^lin-bio]: [Wikipedia — Burn-Jeng Lin](https://en.wikipedia.org/wiki/Burn-Jeng_Lin) — Burn-Jeng Lin nació en Vietnam en 1942, trabajó desde la década de 1970 en tecnología de litografía en IBM Watson Research Center y volvió a Taiwán en 2000 para incorporarse a TSMC como director de I+D; recibió el SPIE Frits Zernike Award en 2008 y es conocido como el “padre de la litografía de inmersión”

[^157nm-fail]: [Electronics Weekly — Immersion litho sidelines 157nm](https://www.electronicsweekly.com/news/research-news/process-rd/immersion-litho-sidelines-157nm-2005-05/) — La ruta de 157 nm fue reemplazada después de 2002-2003 por 193 nm immersion debido a problemas como birrefringencia en lentes de fluoruro de calcio (CaF₂), fuerte absorción de películas a 157 nm y dificultad de integración de procesos; la apuesta de Intel + Nikon fracasó

[^immersion-litho]: [Wikipedia — Immersion lithography](https://en.wikipedia.org/wiki/Immersion_lithography) — Burn-Jeng Lin propuso en SPIE 2002 la litografía de inmersión de 193 nm; el índice de refracción del agua de 1,44 convierte 193 nm en una resolución equivalente de unos 134 nm; ASML la produjo en masa en 2007, sosteniéndola desde 65 nm hasta 7 nm y prolongando seis generaciones la ley de Moore

[^cw-lin-interview]: [CommonWealth — Interview with the Father of Immersion Lithography Who Put TSMC on the Map](https://english.cw.com.tw/article/article.action?id=3720) — Entrevista con Burn-Jeng Lin, 2024-06-18; contexto histórico de “Nikon no se atrevió a hacer immersion”; Lin volvió a TSMC en 2000 y promovió la adopción de immersion lithography, en una cooperación tecnológica de 30 años entre TSMC y ASML
