---
title: 'BIM y tecnología de construcción en Taiwán: doce años de política caso por caso, reescritos por un protocolo de dieciocho meses'
description: 'El 23 de mayo de 2014, el Comité de Obras Públicas del Yuan Ejecutivo estableció la "Plataforma para la Promoción del Uso de BIM en Obras Públicas", adoptando el principio de "adaptación a cada caso y avance progresivo". Once años y siete meses después, un desarrollador taiwanés que trabaja en Tokio subió un repositorio llamado REVIT_MCP_study a GitHub, con más de setenta estrellas y más de ochenta forks. En esos doce años intermedios, la industria de la construcción taiwanesa recorrió un largo camino desde el dibujo a mano y la impresión heliográfica hasta el modelado 3D, desde los intentos individuales hasta los estándares nacionales, y desde la actualización de herramientas hasta la redefinición de roles profesionales.'
date: 2026-05-22
author: 'Taiwan.md'
category: 'Technology'
subcategory: '建築科技'
tags:
  [
    'Technology',
    'BIM',
    '建築資訊建模',
    '營建科技',
    '建築',
    '數位轉型',
    'Revit',
    'MCP',
    'AI',
    '中鼎工程',
    '台灣世曦',
    '碩濤',
  ]
readingTime: 22
lastVerified: 2026-05-22
lastHumanReview: false
featured: true
translatedFrom: 'Technology/台灣BIM與營建科技.md'
sourceCommitSha: '31a05c44'
sourceContentHash: 'sha256:5500ed1d9d4e0f85'
sourceBodyHash: 'sha256:6207b1decb9dcfc4'
translatedAt: '2026-06-16T16:54:57Z'
image: '/article-images/technology/freecad-bim-example-2024.webp'
imageCredit: 'Maxwxyz via Wikimedia Commons'
imageLicense: 'CC BY 4.0'
imageSource: 'https://commons.wikimedia.org/wiki/File:FreeCAD_1.0_Dark_BIM_Example.png'
---

# BIM y tecnología de construcción en Taiwán: doce años de política caso por caso, reescritos por un protocolo de dieciocho meses

![Captura de pantalla de la plataforma de trabajo BIM de FreeCAD 1.0 en tema oscuro, mostrando un modelo 3D de un edificio de demostración en el centro, con un panel lateral izquierdo que lista las capas profesionales (estructura, MEP, envolvente) y una barra de herramientas inferior con el conjunto de comandos específico del banco de trabajo BIM, reflejando la esencia de la transformación digital de la ingeniería que es la sistematización de la información del edificio](/article-images/technology/freecad-bim-example-2024.webp)
_Archivo de demostración del banco de trabajo BIM de FreeCAD 1.0 en tema oscuro. Foto: Maxwxyz, 2024-10-07. [Licencia vía Wikimedia Commons](https://commons.wikimedia.org/wiki/File:FreeCAD_1.0_Dark_BIM_Example.png)._

> **Resumen en 30 segundos:** El 23 de mayo de 2014, el Comité de Obras Públicas del Yuan Ejecutivo estableció la "Plataforma para la Promoción del Uso de Modelado de Información de Construcción (BIM) en Obras Públicas"[^1], adoptando el principio de "adaptación a cada caso y avance progresivo" en tres fases, sin que hasta la fecha sea obligatorio[^2]. En ese mismo período, el Centro de Investigación BIM de la Universidad Nacional de Taiwán impartió su primera clase, se fundó formalmente la Asociación Taiwanesa de Modelado de Información de Construcción (TBIMA)[^3], el gobierno de Nueva Taipéi emitió la primera licencia de construcción aprobada mediante modelo BIM, la Oficina de Desarrollo Urbano de Taipéi publicó las normas operativas para datos de atributos del modelo BIM de finalización de obra[^4], y BSI firmó un MOU con el Taiwan BIM Task Group[^5]. Once años y siete meses después, el 10 de diciembre de 2025, un desarrollador llamado CHIANG SHUOTAO subió un repositorio llamado `REVIT_MCP_study` a GitHub, con setenta y tres estrellas y ochenta y cinco forks[^6]. Cuatro meses más tarde, en abril de 2026, Autodesk anunció que Revit 2027 incluiría de forma nativa un servidor Model Context Protocol[^7]. Los doce años que el gobierno no pudo impulsar, frente a los dieciocho meses de un protocolo de Anthropic, representan la lenta redefinición profesional de la industria de la construcción taiwanesa, desde el dibujo hasta la integración de sistemas.

---

## La "adaptación a cada caso" del Comité de Obras Públicas

El 23 de mayo de 2014, el Comité de Obras Públicas del Yuan Ejecutivo creó algo llamado "Plataforma para la Promoción del Uso de Modelado de Información de Construcción (BIM) en Obras Públicas"[^1]. El principio de ocho caracteres anunciado ese día fue "**adaptación a cada caso, avance progresivo**".

Estas ocho palabras fueron citadas durante muchos años.

El Comité dividió la estrategia de promoción en tres fases: primera fase (año 103 de la República, 2014) "fomento y proyectos piloto selectivos", invitando a organismos contratantes de obras no residenciales a participar en proyectos piloto, dando prioridad a contratos por mejor oferta global; segunda fase (años 104-105, 2015-2016) "implementación y evaluación piloto"; tercera fase "**a partir del año 106 [2017], promover el uso de tecnología BIM en obras públicas por encima de un cierto monto**"[^1].

Pero el umbral de "por encima de un cierto monto" nunca se convirtió en obligación total en 2026. La formulación repetida del Comité fue: "**los organismos contratantes de obras evaluarán por sí mismos, en función de la complejidad del caso o la escala de la obra, y de su propia capacidad de gestión contractual, si adoptan o no la tecnología BIM, en lugar de establecer una regulación general y obligatoria**"[^2].

El grupo de comparación es Hong Kong. La Oficina de Desarrollo de Hong Kong ya exige obligatoriamente el uso de BIM en proyectos de obra con un presupuesto estimado superior a 30 millones de dólares de Hong Kong[^8]. En Taiwán, en cambio, los tres verbos "fomentar", "probar" y "evaluar por cuenta propia" aparecen rotativamente en cada libro blanco.

Según la información pública disponible hasta la fecha de búsqueda, la plataforma BIM del Comité acumuló "más de 60 organismos de licitación de obras públicas que utilizan tecnología BIM, con más de 120 casos de aplicación"[^2]. Esta cifra, dentro de los más de diez mil casos de obras públicas anuales en Taiwán, es insignificante.

> **📝 Nota del curador**
> La narrativa habitual es que "el gobierno no pudo impulsar BIM porque la industria no estaba a la altura". Esta explicación es narrativamente conveniente, pero invierte la causalidad. **El orden real es más cercano a: desde 2014, el gobierno decidió no hacer BIM obligatorio, porque hacerlo habría destruido la fuente de ingresos de la mitad de los estudios de arquitectura.** La "adaptación a cada caso" es un cálculo político: deja la decisión en manos de las pocas entidades con "capacidad de gestión contractual", mientras el resto sigue usando AutoCAD, sin que nadie se meta con nadie.

---

## Ministerio del Interior, Taipéi, Nueva Taipéi: tres ejes de promoción desincronizados

El Comité de Obras Públicas impulsaba lo suyo, y el Instituto de Investigación en Construcción del Ministerio del Interior (ABRI) impulsaba lo propio.

El ABRI lanzó en el año 104 de la República (2015) el plan cuatrienal "Plan de Promoción de la Investigación, Integración, Compartición y Aplicación de Información de Construcción", continuando en el año 108 (2019) con un segundo plan cuatrienal[^9]. Los dos grandes objetivos del segundo período se formulaban ambiciosamente: "**actualización digital de la tecnología de construcción**" + "**entorno digital de vida en edificios**", este último buscando integrar BIM con GIS e IoT para ciudades digitales[^10].

Pero el ABRI no es el organismo ejecutor de la gestión de construcción. La gestión de construcción recae en los gobiernos municipales y de condado.

En 2014, **el gobierno de Nueva Taipéi emitió la primera licencia de construcción aprobada mediante revisión de un modelo BIM**[^11]. Ese mismo año, Nueva Taipéi publicó los "Criterios para la Entrega de Información del Modelo BIM de Finalización de Obra en Edificios Públicos del Gobierno de Nueva Taipéi". Para 2026, el "Sistema de Verificación Asistida por Computadora para Licencias de Construcción" del gobierno de Nueva Taipéi (bim.ntpc.gov.tw) había acumulado más de 20 modelos BIM completados[^11].

Cuatro años después, el 6 de noviembre de 2018, **la Oficina de Desarrollo Urbano del Gobierno de Taipéi publicó las "Normas Operativas para Datos de Atributos del Modelo BIM de Finalización de Obra en Proyectos de Construcción Dirigidos por la Oficina de Desarrollo Urbano del Gobierno de Taipéi"**[^4]. Las normas de Taipéi hacen referencia al formato internacional COBie (Construction Operations Building Information Exchange) e incorporan normas pertinentes del Instituto de Investigación en Construcción del Ministerio del Interior de 2015 y del Reino Unido[^4]. Las normas exigen que, al utilizar diferentes software de modelado BIM, se deben exportar datos estándar en formato **IFC** (Industry Foundation Classes, Clases de Fundamento Industrial, estándar internacional abierto establecido por buildingSMART International, ISO 16739-1:2024) y COBie[^4][^12].

> **💡 ¿Sabías que...?**
> IFC pertenece a un estándar internacional abierto establecido por la organización sin fines de lucro buildingSMART International[^12], independiente de Autodesk o de cualquier otro proveedor individual. Su lógica de existencia es similar a la de PDF: permite que modelos creados con diferentes software (Revit, ArchiCAD, Tekla, Navisworks) se intercambien sin fricción. **El gobierno danés exige obligatoriamente el uso del formato IFC en proyectos de construcción pública desde 2010, seguido por Noruega, Finlandia y Singapur**[^12]. Taiwán no incorporó IFC en sus normas hasta 2018, a nivel municipal desde la Oficina de Desarrollo Urbano de Taipéi. El estándar internacional llevaba diez años de ventaja; Taiwán lo fue incorporando gradualmente.

Los tres ejes de promoción —central, Taipéi y Nueva Taipéi— operan en momentos completamente desincronizados. La misma estación de metro puede tener la fase de diseño regida por las normas BIM de la Oficina de Ingeniería del Metro de Taipéi (vinculadas al contrato global), la fase de licencia de construcción regida por las normas de modelo de finalización de la Oficina de Desarrollo Urbano de Taipéi (formato COBie), y la fase de operación y mantenimiento cayendo en un conjunto de herramientas de gestión de instalaciones completamente distinto.

"**La mayoría de las aplicaciones de BIM en el sector público se concentran en las fases de diseño y construcción. También existen diferencias en la aplicación entre obras tradicionales y obras bajo contrato global. Los modelos de gestión operativa y de mantenimiento posteriores aún adoptan prácticas tradicionales**"[^13]— esto fue escrito en el propio informe de resultados del ABRI.

---

## Línea Wan-Ta, Estación de Miaoli, Terminal 3 del Aeropuerto de Taoyuan: BIM en las obras públicas

En 2011, **la Línea Wan-Ta del Metro de Taipéi incorporó por primera vez BIM en el contrato de diseño de ingeniería**[^14].

Este es un evento "primero" frecuentemente citado en la promoción de BIM en Taiwán. Los diferentes tramos de la Línea Wan-Ta, conforme a los requisitos contractuales, adoptaron el modelo BIM para el diseño de las estaciones de metro, integrando simultáneamente las especialidades de arquitectura, estructura e instalaciones mecánicas y eléctricas, **reduciendo conflictos en las interfaces de diseño**[^14].

Siguiendo los pasos de la Línea Wan-Ta, las obras públicas fueron incorporándose una tras otra: la estación elevada Y19 de la Línea Circular del Metro de Taipéi, varios centros deportivos en Nueva Taipéi, la nueva estación del Tren de Alta Velocidad en Miaoli, la Terminal 3 del Aeropuerto Internacional de Taoyuan, el Tren Ligero Circular de Kaohsiung: cada proyecto tiene un caso de estudio publicado en revistas internas del ABRI, del NTUBIM de la Universidad Nacional de Taiwán o de la Oficina de Metro.

La "**victoria numérica**" más citada es la Estación Miaoli del Tren de Alta Velocidad de Taiwán: se introdujo BIM tres meses antes del inicio de la obra, el equipo de supervisión detectó múltiples puntos de conflicto a partir del modelo 3D, **ahorrando un 20% en costos de cambios de diseño posteriores, y el replanteo en obra comenzó dos meses antes de lo previsto**[^15].

La Terminal 3 del Aeropuerto de Taoyuan es otro caso de escala diferente. En marzo de 2021, **el consorcio formado por Samsung C&T y Rong Gong Engineering ganó la licitación para la obra civil del edificio principal de la T3 por 44.5 mil millones de dólares taiwaneses**[^16]. Todo el diseño de la T3 fue liderado por CECI Engineering Consultants (junto con Rogers Stirk Harbour + Partners y Ove Arup and Partners Hong Kong), y la colaboración transnacional dependió de que los modelos BIM fluyeran entre diferentes firmas — este es el caso insignia que CECI utiliza repetidamente en sus materiales de capacitación interna[^17].

> **✦** El momento en que la Línea Wan-Ta incorporó por primera vez BIM en el contrato en 2011 fue una divisoria de aguas silenciosa en la historia de las obras públicas de Taiwán. A partir de ese día, ningún proyecto de metro, aeropuerto, tren de alta velocidad o tren ligero en Taiwán dejó de preguntarse "cómo se hace BIM".

Pero estos son todos "casos emblemáticos". Todos los casos emblemáticos en Taiwán comparten un único defecto común: **son la excepción**.

---

## Cinco grandes consultoras de ingeniería + dos organizaciones: las personas detrás

Las personas que impulsaron BIM en las obras públicas tienen nombre y rostro.

**CECI Engineering Consultants, S.A. (台灣世曦工程顧問股份有限公司)**: fundada en 2007 como inversión de la China Engineering Consultants, Inc. (CECI, establecida en 1969 como fundación)[^18]. **En 2010 estableció el primer Centro de Integración BIM**[^19], uno de los primeros centros de integración en la industria taiwanesa. Cerca de 2,000 empleados, el 90% con formación en carreteras, ferrocarriles, puertos, aeropuertos, puentes, estructuras, túneles, metro, arquitectura, mecánica, eléctrica y control de sistemas, BIM, ITS, PPP y áreas relacionadas[^19].

**Sinotech Engineering Consultants (中興工程顧問)**: fundada en 1970, transformada en organización sin fines de lucro en 1994, con inversión posterior en Sinotech Engineering Consultants, Inc.[^20]. Sinotech desarrolló BIM en algo llamado "**Sistema de Información de Gestión de Proyectos (PMIS)**": basado en el espíritu del Entorno de Datos Común (CDE) de ISO 19650, con siete módulos principales que facilitan la integración de información entre especialidades y proyectos[^21].

**Evergreen Consulting Engineering Co., Ltd. (EGC, 永峻工程顧問股份有限公司)**: fundada en 1974. El diseño estructural del Taipei 101 y la Torre T&C de 85 pisos en Kaohsiung fueron obra suya[^22]. **El CTBUH (Council on Tall Buildings and Urban Habitat) clasifica a EGC entre las diez principales consultoras de estructura de edificios altos del mundo**[^22].

En el ámbito académico hay dos nodos clave:

**Centro de Investigación en Simulación y Gestión de Información en Ingeniería Civil de la Universidad Nacional de Taiwán (NTUBIM)**: fundado en 2011, dirigido por el profesor **Shang-Hsien Hsieh** del Departamento de Ingeniería Civil. El cofundador académico, el profesor asociado **Rong-Chin Guo**, escribió en diciembre de 2011 un artículo titulado "**El desarrollo de BIM impacta el sistema arquitectónico actual**"[^23], que sigue siendo uno de los documentos académicos tempranos de referencia en la discusión sobre BIM en Taiwán. NTUBIM posteriormente asumió encargos del ABRI y del Comité de Obras Públicas durante varios años, liderando la guía de trabajo colaborativo BIM de Taiwán y la traducción al chino de ISO 19650.

**Asociación Taiwanesa de Modelado de Información de Construcción (TBIMA)**: predecesora fue un encuentro de entusiastas de la tecnología BIM en Taiwán en 2009, comenzó la preparación en 2011, y **se registró formalmente como asociación ante el Ministerio del Interior el 10 de marzo de 2012**[^3]. Los principales miembros de la association provienen de los instructores certificados de Autodesk Taiwan en 2008: el linaje de las organizaciones civiles de BIM en Taiwán creció directamente del círculo de instructores certificados de Autodesk.

> **📝 Nota del curador**
> En la ceremonia de firma del MOU del Taiwan BIM Task Group el 3 de octubre de 2018[^5], cinco rostros se sentaron a la mesa: BSI (British Standards Institution) Taiwán, NTUBIM de la Universidad Nacional de Taiwán, la Academia Taiwanesa de Investigación en Construcción, el Centro de Construcción de Taiwán y TBIMA. **El Instituto de Investigación en Construcción del Ministerio del Interior fue "unidad directiva" pero no "unidad signataria"**, un arreglo jerárquico revelador. Significa que el gobierno reconoció que, en materia de estándares internacionales de BIM, era mejor dejar que el mundo académico y las organizaciones civiles tomaran la iniciativa, mientras el gobierno se retiraba a un segundo plano. La publicación al año siguiente de la "**versión en chino de ISO 19650**"[^24] por parte de BSI fue una pequeña declaración de soberanía blanda: Taiwán finalmente tenía su propia traducción oficial al chino de los estándares internacionales de BIM.

---

## Revit, ArchiCAD, Tekla: la corriente subterránea de la hegemonía del software

![Captura de pantalla de Autodesk Revit 2024, mostrando una simple pared divisoria con puertas y ventanas en una presentación tridimensional orientada a objetos, con el panel de propiedades de componentes a la izquierda y vistas en planta, alzado y sección sincronizadas en tiempo real en la parte inferior derecha, reflejando la naturaleza del modelado orientado a objetos del software BIM](/article-images/technology/autodesk-revit-2024-bim-objects.webp)
_Demostración de componentes BIM de Autodesk Revit 2024. Foto: DanielDefault, 2024. [Licencia vía Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Revit_2024.png)._

Al entrar en cualquier estudio de Taiwán que haya adoptado BIM, la pantalla de inicio es Revit en el 90% de los casos.

"**En Taiwán, el 90% de los arquitectos (con capacidad de diseño BIM) utilizan Revit Architecture**" — esta es la cifra que el distribuidor de ArchiCAD escribió en su propio sitio web[^25]. Aunque es una cita de fuente única, es consistente con la percepción de la industria: Revit tiene una posición casi monopolística en el campo del diseño arquitectónico en Taiwán.

ArchiCAD, desarrollado por la empresa húngara Graphisoft, funciona en Mac y Windows. Su intuición de diseño y curva de aprendizaje son más amigables que las de Revit, pero su base de usuarios en Taiwán es notablemente menor[^26]. El distribuidor Long Ting Information ha organizado muchas demostraciones en el distrito oriental de Taipéi, y en cada una se escucha a los diseñadores decir: "Sé usar Revit, el estudio solo tiene licencia de Revit". Este es el efecto de bloqueo por escala.

El campo de las estructuras de acero sigue otro eje. **Tekla Structures (producto de Trimble, anteriormente XSteel) es actualmente el software dominante en el diseño de estructuras de acero en Taiwán**[^27]. La capacidad de Tekla para manejar estructuras de acero es reconocida en la industria taiwanesa en edificios altos, puentes, gimnasios y fábricas.

La infraestructura (ferrocarriles, carreteras, túneles) se inclina hacia el sistema MicroStation de Bentley Systems[^28]. CECI, Sinotech y Sinotech Engineering Consultants utilizan MicroStation junto con OpenRoads / OpenBridge de Bentley en grandes contratos EPC globales y proyectos ferroviarios transnacionales.

Corriendo sobre estos software principales están Dynamo (programación visual de Autodesk) y pyRevit (framework de extensión en Python) de código abierto. **A principios de 2016, Autodesk Taiwán invitó específicamente al equipo de desarrollo de Dynamo desde Singapur para impartir cursos en Taiwán**[^29], y desde entonces Dynamo ha llamado la atención en el círculo de ingenieros BIM de Taiwán. Un escenario típico: un ingeniero de instalaciones escribe un script de Dynamo que ordena automáticamente las coordenadas de todos los ductos de aire, verifica las alturas libres y genera vistas de sección — algo que antes tomaba un día entero con CAD, ahora se resuelve en minutos[^30].

El escenario de detección de conflictos (clash detection) pertenece a Autodesk Navisworks. Navisworks Manage integra navegación 3D, detección de conflictos, exportación de informes, simulación de cronograma 4D y funciones de estimación de costos 5D[^31]. En la ingeniería de instalaciones del metro de Taiwán existe un término especializado llamado **CSD / SEM** — CSD (Combined Service Drawing) son los planos combinados de instalaciones, SEM (Structure / Electric / Mechanic) son los planos integrados de estructura, electricidad y mecánica. La práctica tradicional usaba CAD para superponer planos y verificación en papel; en la era BIM se utiliza Navisworks para ejecutar verificaciones de colisión y detectar puntos de conflicto en 3D[^32].

La frase "**integración de planos CSD/SEM**" es ahora un servicio obligatorio en los sitios web de las consultoras BIM de Taiwán.

---

## CTCI, Futsu, Dacin, Obayashi: quienes construyen Taiwán

![Vista de la calle del sitio de construcción del Taipei Dome por la mañana del 21 de junio de 2020, con la estructura de acero y revestimiento metálico del domo aún en construcción a lo lejos, y un camión Hino 300 cruzando el paso de peatones en la calle Zhongxiao E. Rd. cerca de la salida 5 de la estación del Memorial de Sun Yat-sen, reflejando la realidad de más de una década de construcción del recinto deportivo más grande de Taipéi y el papel de gestión de construcción de Obayashi en este domo de acero tubular circular de 65,000 toneladas](/article-images/technology/taipei-dome-construction-cheng-2020.webp)
_Sitio de construcción del Taipei Dome, 2020-08-16, calle Zhongxiao E. Rd., salida 5 de la estación del Memorial de Sun Yat-sen. Foto: Cheng-en Cheng, 2020-08-16. [Licencia vía Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Taipei_Dome_and_Hino_300_BEM-5593_%2850281669428%29.jpg).\_

Los principales actores del mercado de construcción a gran escala en Taiwán son un grupo de empresas de contratación global (EPC) — que adoptaron BIM antes que los estudios de arquitectura y la convirtieron en herramienta de producción.

La primera es **CTCI Corporation (中鼎工程股份有限公司, código bursátil 9933)**. CTCI fue fundada en 1979 por inversión conjunta de la Fundación China Technical Service Cooperative (CTCI) con China Development Industrial Bank y Central Investment Company[^33] — este contexto de fundación es especial: la Fundación China Technical Service Cooperative (中國技術服務社), establecida en 1959, es una agencia de transferencia tecnológica al servicio del desarrollo industrial de Taiwán, que en la década de 1970, durante el auge de la industria petroquímica, asumió una gran cantidad de trabajo de consultoría técnica de empresas estatales como CPC. En 1979, la fundación escindió su negocio de consultoría de ingeniería, y así nació CTCI.

El negocio de CTCI es **EPC** (Engineering, Procurement, Construction, contratación global de diseño / adquisición / construcción): refinería, petroquímica, química, energía, acero, almacenamiento y transporte, transporte, incineradoras, obras públicas e ingeniería ambiental[^33]. Hasta 2021, 7,500 empleados, con sucursales / oficinas en 15 países[^33][^34]. Proyecto Amine en Arabia Saudita, proyecto de horno de craqueo de etileno Saudi Kayan, proyecto global SAMAC MMA y PMMA — estos nombres trazan la huella de los contratistas EPC taiwaneses en Oriente Medio durante los últimos 20 años[^33].

En 2011 ocurrió algo que reestructuró la composición accionaria de CTCI: **la empresa japonesa Chiyoda Corporation adquirió acciones de CTCI, convirtiéndose en el mayor accionista**[^33]. Esta es la empresa de contratación global más grande de Taiwán, y ahora su mayor accionista es un grupo japonés de construcción química. Este dato poco conocido es desconocido para la mayoría.

> **⚠️ Punto de vista controvertido**
> Los proyectos en el extranjero de grandes empresas EPC como CTCI no están exentos de controversia. En 2017, el proyecto EPC de una planta de procesamiento de gas natural de CTCI en India sufrió retrasos significativos y deudas incobrables, y el grupo reconoció una "**falla fatal en el control de riesgos internacional**"[^35]. Ese mismo año, se canceló el proyecto de la Refinería Guoguang, y las controversias sobre la salud de los residentes cercanos a la Sexta Planta Petroquímica de Mailiao continuaron. Varios proyectos petroquímicos en los que participó CTCI fueron señalados en las narrativas ambientales. BIM ayudó en la precisión de ingeniería de estos grandes proyectos, pero la precisión no resuelve los problemas políticos de tierra, trabajo y medio ambiente.

El mercado de promotores privados tiene otro grupo de nombres: **Futsu Construction (互助營造)** "acumula la mayor superficie de piso completada de plantas de alta tecnología, la mayor experiencia nacional en construcción de plantas"[^36]; **Dacin Engineering (達欣工程, 2535)** es percibida externamente como "**la constructora de referencia de TSMC**", habiendo obtenido el pedido de la estructura superior de la planta FAB 18P3 de TSMC en el Parque Científico del Sur[^37]. El departamento BIM de Dacin escribe en sus presentaciones internas: "**utilizando BIM como plataforma de herramienta base para el desarrollo, planificación, diseño, construcción e integración y coordinación de proyectos de construcción**"[^37] — pero esto solo representa una pequeña parte de los contratos de Dacin.

Hay dos presencias estructurales de empresas extranjeras en Taiwán. **Obayashi Corporation Taiwán (台灣大林組營造)** es la sucursal establecida en Taiwán en 1989 por la empresa japonesa Obayashi Corporation (la que construyó la Torre Skytree de Tokio), y ha construido todo el Taipei 101, la Línea Xinyi del Metro de Taipéi, la Terminal 3 del Aeropuerto de Taoyuan, y el **Taipei Dome**[^38]. **La página de "Resumen Corporativo" del sitio web de la sucursal taiwena de Obayashi enumera explícitamente "gestión de planos de ejecución y aplicación de BIM" como un elemento principal de gestión de construcción**[^38].

> **💡 ¿Sabías que...?**
> El peso total de la estructura de acero del Taipei Dome es de 65,000 toneladas, siendo el único domo en el mundo construido enteramente con tubos de acero circulares[^39]. El diseño de la estructura de acero se realiza en su mayor parte en Tekla Structures, y luego el modelo se importa a Navisworks para realizar detección de conflictos con otras especialidades (instalaciones mecánicas y eléctricas, contra incendios). **Sin BIM, un proyecto de estructura de acero de la escala del Taipei Dome sería prácticamente imposible de completar sin errores graves** — esta es también la razón por la que Obayashi incluye BIM en la lista de "elementos principales de gestión de construcción" en el resumen corporativo.

---

## Escasez de mano de obra, envejecimiento, trabajadores migrantes: por qué la transformación digital es inevitable

Traslademos la escena a una mañana típica en una obra: seis y media de la mañana, los trabajadores llegan gradualmente. Más de la mitad son maestros "de la generación del abuelo", mayores de 40 años.

**Las estadísticas de muertes por accidentes laborales del gobierno de Nueva Taipéi muestran que, de más de 100 casos de muerte, más del 77% tenían más de 40 años**[^40]. Esta cifra es ya un conocimiento común en el círculo de ingenieros civiles. El envejecimiento de la fuerza laboral en la industria de la construcción de Taiwán es una realidad, no una tendencia en curso.

La baja natalidad hace que los jóvenes no entren en la construcción. Las condiciones difíciles en la obra, los salarios poco competitivos y la alta tasa de accidentes mortales — tres factores combinados — hacen que la presión de contratación en la industria de la construcción sea cada vez mayor[^40]. El Ministerio de Trabajo aprobó en 2024 la apertura de 15,000 plazas para trabajadores migrantes en la construcción, y a principios de 2026 ya estaban "**a punto de agotarse**"[^41].

Esta es la razón por la que la transformación digital se ha vuelto algo que la industria de la construcción no puede dejar de hacer.

**La demanda de puestos de ingeniero BIM es alta, el salario inicial para principiantes es de 35,000-45,000 dólares taiwaneses, y hay 104 vacantes con salarios mensuales superiores a 50,000 en el portal de empleo 1111**[^42]. Pero "alta demanda" y "ser competente" son cosas distintas — "**aprender BIM no necesariamente conlleva un crecimiento salarial significativo, la mayoría elige rutas de aprendizaje más económicas**"[^43]. El techo profesional de los ingenieros BIM aún no tiene consenso en la industria.

El problema estructural más profundo radica en que BIM traslada al arquitecto de la categoría profesional de "**dibujante**" a la nueva categoría de "**integrador de sistemas**". La actualización de herramientas es solo la superficie.

Un arquitecto que dibuja con AutoCAD dibuja un conjunto de líneas bidimensionales. Dibuja plantas, alzados y secciones — cada plano es independiente, y es cotidiano modificar la planta y olvidar actualizar el alzado. Un ingeniero que usa Revit / BIM construye un modelo de información: detrás de cada línea se vinculan materiales, especificaciones, proveedores, precios, secuencia de construcción y ciclos de mantenimiento[^44]. Al modificar la planta, el alzado y las secciones se actualizan automáticamente.

Los arquitectos veteranos miran a los jóvenes ingenieros BIM y dicen "esto es cosa de la nueva generación", y la razón real detrás es simple — **esa profesión ya pertenece a un oficio diferente al "arquitecto" con el que ellos entraron en la industria**.

> **✦** "Los modelos BIM a menudo se convierten en trabajo subcontratado, desconectado de la obra real, y muchos centros o equipos BIM se disuelven"[^45] — esta es la observación del propio Centro de Investigación BIM de la Universidad Nacional de Taiwán sobre el estado actual de la promoción de BIM en Taiwán.

---

## Un protocolo como USB-C: la llave de Anthropic para conectar IA con Revit

El 25 de noviembre de 2024, Anthropic abrió el código de algo llamado **Model Context Protocol (MCP)**[^46].

El anuncio original decía en tono científico: "**MCP is an open standard, open-source framework introduced by Anthropic to standardize the way artificial intelligence (AI) systems like large language models (LLMs) integrate and share data with external tools, systems, and data sources**"[^47]. La explicación de Anthropic era más coloquial: "**Think of MCP like a USB-C port for AI applications**"[^6] — así como USB-C unificó la conexión de dispositivos, MCP busca unificar el protocolo de conexión entre IA y fuentes de datos y herramientas.

Junto con el anuncio de MCP vinieron SDK para Python, TypeScript, C# y Java, además de servidores MCP preconstruidos para Google Drive, Slack, GitHub, Git, Postgres y Puppeteer[^46].

Lo que sucedió después, nadie lo anticipó en velocidad.

El 10 de diciembre de 2025, un desarrollador llamado **CHIANG SHUOTAO** subió un repositorio llamado `REVIT_MCP_study` a GitHub[^48]. La descripción del repositorio tenía solo ocho palabras en inglés: "LEARN HOW TO BUILD UP YOUR REVIT MCP". Distribución de lenguajes: **C# 54.2%, JavaScript 18.7%, PowerShell 14.3%, TypeScript 7.0%, HTML 3.3%, Shell 1.2%**[^48]. Para mayo de 2026, este repositorio personal había acumulado **73 estrellas y 85 forks**[^6].

La página personal de GitHub de Shuotao indica su ubicación como "Tokio", pero el README y todos los documentos de enseñanza están en chino tradicional, con contenido que hace eco extensamente de los flujos de trabajo de la industria de la construcción taiwanesa. Sus repositorios periféricos — `CAD_MCP_study`, `NAVISWORK_MCP`, `IFCSH` — constituyen una serie personal de experimentos de código abierto en BIM × MCP × IA[^49].

¿Cómo se lee este caso?

No es que "Taiwán tenga su propio BIM_MCP" — el repositorio de Shuotao es parte del mismo ecosistema que `mcp-servers-for-revit/revit-mcp` a nivel internacional y el propio servidor MCP nativo de Revit 2027 de Autodesk[^7][^50]. Su significado radica en que: **un desarrollador taiwanés, menos de 13 meses después de que Anthropic anunciara MCP, creó un proyecto de enseñanza de código abierto con más de setenta estrellas, trayendo la práctica de ingeniería de Revit MCP internacional de vuelta a la comunidad de habla china**.

Cuatro meses después, **en abril de 2026, Autodesk anunció que Revit 2027 incluiría de forma nativa un servidor MCP y Autodesk Assistant**[^7]. El nuevo Autodesk Assistant puede hacer cosas como: "**encontrar todas las habitaciones que carecen de etiquetas MEP**", "**establecer la resistencia al fuego de todas las puertas de la Fase 2 en 90 minutos**", "**generar todas las vistas de fontanería de este piso**"[^7] — operar Revit en lenguaje natural.

Lo que antes requería uno o dos años de aprendizaje de Revit, ahora se puede hacer diciendo una frase en chino (o inglés).

> **📝 Nota del curador**
> Alineando la línea de tiempo: desde la creación de la plataforma BIM del Comité de Obras Públicas el 23 de mayo de 2014 hasta que Anthropic abrió el código de MCP el 25 de noviembre de 2014, **pasaron 10 años y 6 meses**. En esos 10 años de promoción gubernamental de BIM en Taiwán, se pasó de "fomentar proyectos piloto" a "adaptación a cada caso", sin llegar nunca a la obligatoriedad. Desde que Anthropic abrió el código de MCP hasta que Autodesk anunció el servidor MCP nativo en Revit 2027, **solo pasaron 17 meses**. La velocidad con que una plataforma tecnológica reescribe la incorporación a la industria supera con creces la velocidad de la promoción política. **La verdadera diferencia está en la estructura de los dos modelos de impulso** — la promoción obligatoria requiere coordinar a cientos de partes interesadas, equilibrar decenas de cabilderos industriales y ajustar varias leyes; la promoción por plataforma solo requiere abrir el código del SDK y escribir buena documentación. Ver esta estructura con claridad es más importante que quejarse del gobierno o adorar la IA.

---

## Del dibujo a la integración de sistemas: la redefinición profesional inacabada

Volvamos la cámara a un estudio de arquitectura de la década de 1990.

En aquella época, las paredes del estudio tenían mesas de dibujo, reglas T, estilógrafos y heliógrafos. Un arquitecto dibujaba una planta en un papel A1 grande con estilógrafo, y al terminar una lámina había que llevarla al heliógrafo para sacar copias — la máquina zumbaba, y los planos heliográficos de fondo azul y líneas blancas salían lentamente por el otro lado. Modificar un detalle obligaba a redibujar toda la lámina.

AutoCAD lanzó la versión para Classic Mac OS en 1992 y la versión para Microsoft Windows en 1993[^51], y los estudios de arquitectura taiwaneses comenzaron a adoptar CAD de forma masiva a mediados de la década de 1990. El dolor de la transición duró aproximadamente diez años — los arquitectos veteranos se resistían, los diseñadores jóvenes lo abrazaban, y dentro de los estudios se formaban dos bandos: los que "dibujaban en CAD" y los que "dibujaban en la mesa".

La transición de AutoCAD a Revit fue la segunda transformación. **Autodesk no lanzó Revit junto con el término "Building Information Modeling" hasta 2002**[^52] — es decir, el intervalo entre el dibujo a mano y CAD, y entre CAD y BIM, fue de aproximadamente veinte años. Pero el dolor de la transición a BIM fue más profundo que el de la transición a CAD, porque esta vez el nivel requerido ascendió de la sustitución de herramientas a la **reestructuración del modelo mental**.

CAD digitaliza tus líneas. BIM requiere que sistematices toda la información del edificio. Una pared se convierte en un objeto de datos: "pared divisoria del espacio de oficina de la Zona A del 2.º piso, material: doble placa de yeso de 12 mm + estructura ligera de acero de 75 mm, resistencia al fuego 1 hora, proveedor XX, costo YY, secuencia de construcción después del tendido de tuberías MEP", en lugar de ser solo dos líneas paralelas.

La integración entre especialidades también cambió. El flujo tradicional era: el arquitecto dibujaba sus planos, el ingeniero estructural dibujaba los suyos, el ingeniero MEP dibujaba los suyos, y los tres conjuntos de planos se superponían en la obra para detectar conflictos — un ducto de aire atravesando una viga, un tubo de drenaje chocando con un pilar estructural. El flujo BIM superpone los planos en el mismo modelo tridimensional durante la fase de diseño, y las verificaciones de colisión y conflictos se completan en computadora[^32].

La frase "**reducción de conflictos en las interfaces de diseño**" aparece en todos los informes de resultados de casos de estudio BIM en Taiwán[^14][^15]. Pero el cambio profesional detrás de estas seis palabras es: la estructura de poder entre arquitectos, ingenieros estructurales, ingenieros MEP y contratistas está siendo reorganizada. **Antes el arquitecto era el autor único de la fase de diseño; en la era BIM, el diseño es una integración de sistemas colaborativa entre múltiples partes**.

Esta redefinición profesional aún no está completa.

> **✦** "**Los clientes carecen de un conocimiento suficiente sobre la aplicación de BIM y a menudo trabajan con flujos de trabajo de ingeniería tradicionales, lo que limita la eficacia de la tecnología BIM**"[^53] — esta es la observación más directa de BSI sobre el lado del cliente en Taiwán. El cuello de botella para impulsar BIM está en el lado del cliente; si los ingenieros saben o no es secundario.

---

## Lo que viene

En mayo de 2026, la situación de BIM en Taiwán es la siguiente:

- El gobierno central lleva 12 años promoviéndolo, sigue siendo "adaptación a cada caso", sin obligatoriedad total[^2]
- Taipéi y Nueva Taipéi exigen modelos BIM a nivel de licencia de construcción desde 2014 / 2018, pero las normas municipales difieren entre condados[^4][^11]
- Las grandes consultoras de ingeniería (CECI, Sinotech, Evergreen) y los grandes contratistas (CTCI, Futsu, Dacin, Obayashi) lo utilizan; la demanda de ingenieros BIM es alta[^17][^19][^33][^42]
- La mayoría de los estudios de arquitectura pequeños y medianos aún usan principalmente AutoCAD; la tasa de adopción de BIM se estima en un dígito porcentual[^43][^45]
- 17 meses después de que Anthropic abriera el código de MCP en noviembre de 2024, se anunció el servidor MCP nativo en Autodesk Revit 2027[^7][^46]
- Un desarrollador taiwanés creó un repositorio de enseñanza de Revit MCP con 73 estrellas, conectando el ecosistema internacional con la comunidad de habla china[^6][^48]

Al unir estas seis líneas, **BIM en Taiwán es la historia de una profesión que está siendo redefinida desde el exterior por una plataforma tecnológica**, y aún le falta distancia para parecerse a una industria madura. La velocidad de promoción gubernamental no sigue el ritmo de la iteración tecnológica; la velocidad de adopción civil no sigue el ritmo del envejecimiento demográfico. La industria de la construcción taiwanesa es tirada simultáneamente por tres fuerzas: profesionales tradicionales envejecidos, obras con escasez de mano de obra, y herramientas de nueva generación de IA × BIM.

En la próxima década, la profesión de "arquitecto" en Taiwán puede dejar de ser lo que es ahora. La parte de dibujo se la cederá a la IA — con una frase como "**establecer la resistencia al fuego de todas las puertas de la Fase 2 en 90 minutos**"[^7] se pueden modificar todas las puertas de un proyecto. El trabajo del arquitecto se acercará más a "**integrador de sistemas**", "**traductor entre el cliente y la tecnología**" y "**curador de colaboración multipartita**".

Cuando la plataforma BIM del Comité de Obras Públicas celebró su primera reunión el 23 de mayo de 2014, la Estación Miaoli del Tren de Alta Velocidad aún no estaba construida. Cuando Autodesk anunció el servidor MCP nativo en Revit 2027 en abril de 2026, la siguiente planta fab de TSMC en Kaohsiung ya estaba preparándose con planos completos en BIM. Doce años de "adaptación a cada caso" llegaron a un lugar que nadie anticipó — un protocolo de código abierto que salió de las oficinas de Anthropic en California, California, reescribió desde el lado de la plataforma la curva de incorporación de toda la industria, rodeando el camino original de la obligatoriedad gubernamental.

Cuando Shuotao subió `REVIT_MCP_study` a GitHub en diciembre de 2025[^48], habían pasado exactamente 11 años y 7 meses desde la creación de la plataforma BIM del Comité. En esos doce años intermedios, la industria de la construcción taiwanesa recorrió un largo camino desde el dibujo a mano y la impresión heliográfica hasta el modelado 3D, desde los intentos individuales hasta los estándares nacionales, y desde la actualización de herramientas hasta la redefinición de roles profesionales. **Este camino no está terminado — pero cómo se recorra su siguiente tramo ya no está enteramente en manos del gobierno taiwanés**.

---

**Lectura adicional**:

- [Arquitectura de Taiwán](/art/台灣建築) — la narrativa cultural arquitectónica desde las casas de piedra hasta los rascacielos; este artículo es su complemento sobre digitalización de ingeniería
- [Vivienda social y justicia habitacional](/society/社會住宅與居住正義) — la aplicación de BIM en la gestión operativa y de mantenimiento de vivienda social es un plan prioritario del Instituto de Investigación en Construcción del Ministerio del Interior en los últimos años
- [Empresas de Taiwán: TSMC](/economy/台灣企業：台積電) — la aplicación de BIM en las plantas de TSMC es el principal campo de batalla práctico para constructoras como Futsu y Dacin
- [Desarrollo de IA en Taiwán](/technology/AI發展) — Anthropic MCP y el servidor MCP nativo en Revit 2027 son un caso concreto de IA × industria
- [Industria de semiconductores](/technology/半導體產業) — la solución integral de ingeniería para plantas fab + la construcción inteligente con BIM es la base de ingeniería para la expansión de los clústeres de semiconductores

## Imágenes

Este artículo utiliza 3 imágenes con licencia CC de Wikimedia Commons, todas almacenadas en caché en `public/article-images/technology/` para evitar enlaces directos al servidor de origen:

- [FreeCAD 1.0 Dark BIM Example](https://commons.wikimedia.org/wiki/File:FreeCAD_1.0_Dark_BIM_Example.png) — Foto: Maxwxyz, 2024-10-07, CC BY 4.0 (imagen principal: presentación de modelo 3D de herramienta BIM de código abierto)
- [Autodesk Revit 2024 物件示範](https://commons.wikimedia.org/wiki/File:Revit_2024.png) — Foto: DanielDefault, 2024, CC BY-SA 4.0 (imagen en línea: pantalla de modelado orientado a objetos de Revit)
- [Taipei Dome and Hino 300 BEM-5593](https://commons.wikimedia.org/wiki/File:Taipei_Dome_and_Hino_300_BEM-5593_%2850281669428%29.jpg) — Foto: Cheng-en Cheng, 2020-08-16, CC BY-SA 2.0 (imagen en línea: sitio de construcción del Taipei Dome con 65,000 toneladas de estructura de acero en montaje)

La matriz completa de licencias de medios se registra en [`reports/research/2026-05/台灣BIM與營建科技.md`](../../reports/research/2026-05/台灣BIM與營建科技.md) § tres tablas de la matriz de licencias de medios.

## Referencias

[^1]: [Comité de Obras Públicas del Yuan Ejecutivo de la República de China: Zona especial para el uso de Modelado de Información de Construcción (BIM) en obras públicas](https://www.pcc.gov.tw/content/index?eid=1345&type=C) — Página oficial de la plataforma de promoción de BIM del Comité de Obras Públicas del Yuan Ejecutivo, que documenta el establecimiento el 23 de mayo de 2014 y la estrategia de promoción en tres fases: "fomento y proyectos piloto / implementación y evaluación piloto / a partir del año 106 [2017], promover el uso de tecnología BIM en obras públicas por encima de un cierto monto".

[^2]: [Plataforma de Participación en Políticas Públicas de la Oficina de Auditoría: Consulta de opiniones sobre la estrategia de promoción de BIM del Comité de Obras Públicas](https://cy.join.gov.tw/policies/detail/8e95c8d6-ce87-4e05-afce-c46a33eb6f89) — Página de discusión abierta de la Oficina de Auditoría, que documenta el principio de promoción del Comité como "adaptación a cada caso, avance progresivo", sin obligatoriedad total; estadísticas oficiales de más de 60 organismos de licitación de obras públicas que utilizan BIM y más de 120 casos de aplicación.

[^3]: [Sitio web oficial de la Asociación Taiwanesa de Modelado de Información de Construcción (TBIMA)](https://sites.google.com/view/tbima) — Sitio web oficial de la asociación registrada ante el Ministerio del Interior, que documenta el origen en reuniones de 2009, la preparación en 2011, la fundación formal el 10 de marzo de 2012, y el linaje de los principales miembros provenientes del círculo de instructores certificados de Autodesk Taiwan en 2008.

[^4]: [Oficina de Desarrollo Urbano del Gobierno de Taipéi: Normas operativas para datos de atributos del modelo BIM de finalización de obra en proyectos de construcción v.2.0](https://udd.gov.taipei/assets/50-10660/Documents/竣工模型屬性資料作業規範v2.0_20181109_new.pdf) — Normas oficiales publicadas por la Oficina de Desarrollo Urbano de Taipéi el 9 de noviembre de 2018, que hacen referencia al formato internacional COBie y exigen la exportación de datos en formato IFC.

[^5]: [BSI firma MOU de cooperación con "Taiwan BIM Task Group" junto con industria, gobierno, academia e investigación](https://www.bsigroup.com/zh-TW/about-bsi/media-centre/press-release/2018-/october/bsitaiwan-bim-task-group/) — Comunicado de prensa de BSI Taiwán del 3 de octubre de 2018, que documenta las cinco unidades signatarias (BSI, NTUBIM de la Universidad Nacional de Taiwán, Academia Taiwanesa de Investigación en Construcción, Centro de Construcción de Taiwán, TBIMA) y el papel directivo del Instituto de Investigación en Construcción del Ministerio del Interior.

[^6]: [shuotao/REVIT_MCP_study repositorio GitHub](https://github.com/shuotao/REVIT_MCP_study) — Proyecto personal de enseñanza de Revit MCP de código abierto de CHIANG SHUOTAO (碩濤), creado en diciembre de 2025, con 73 estrellas y 85 forks acumulados para mayo de 2026, distribución de lenguajes: C# 54.2% + JavaScript 18.7% + PowerShell 14.3%.

[^7]: [Blog de Desarrolladores de Autodesk: Revit API Agents, MCP, Copilot y Codex](https://blog.autodesk.io/revit-api-agents-mcp-copilot-and-codex) — Anuncio del blog oficial de desarrolladores de Autodesk de abril de 2026, Revit 2027 incluye servidor MCP nativo + Autodesk Assistant que soporta operación de modelos Revit en lenguaje natural.

[^8]: [ONC Lawyers: Adopción de BIM y sus complicaciones legales para la industria de la construcción](https://www.onc.hk/zh_HK/publication/adoption-of-bim-and-its-legal-complications-for-the-construction-industry) — Artículo de un bufete de abogados de Hong Kong, que documenta la comparación de políticas con la exigencia obligatoria de BIM por parte de la Oficina de Desarrollo de Hong Kong para proyectos con un presupuesto estimado superior a 30 millones de dólares de Hong Kong.

[^9]: [Instituto de Investigación en Construcción del Ministerio del Interior de la República de China: Plan de promoción de la aplicación de Modelado de Información de Construcción (BIM)](https://www.abri.gov.tw/News_Content_Table.aspx?n=807&s=315634) — Página oficial del plan del ABRI, que documenta el plan cuatrienal de 2015 (año 104 de la República) y los objetivos y alcance del segundo período del plan en 2019 (año 108).

[^10]: [Instituto de Investigación en Construcción del Ministerio del Interior: Investigación sobre el estado de aplicación de los resultados del desarrollo del Modelado de Información de Construcción (BIM) en edificios y plan de promoción](https://www.abri.gov.tw/News_Content_Table.aspx?n=807&s=39612) — Informe de resultados de investigación encargado por el ABRI, que documenta los dos grandes objetivos del segundo período del plan: "actualización digital de la tecnología de construcción" + "entorno digital de vida en edificios" y la dirección de integración de BIM × GIS × IoT para ciudades digitales.

[^11]: [Oficina de Obras Públicas del Gobierno de Nueva Taipéi: Sistema de verificación asistida por computadora para licencias de construcción](https://www.bim.ntpc.gov.tw/) — Sitio web oficial del sistema de verificación de licencias BIM del gobierno de Nueva Taipéi, que documenta la primera licencia de construcción aprobada mediante modelo BIM en 2014, los más de 20 modelos BIM completados acumulados y los "Criterios para la Entrega de Información del Modelo BIM de Finalización de Obra en Edificios Públicos del Gobierno de Nueva Taipéi".

[^12]: [buildingSMART International: Industry Foundation Classes (IFC)](https://www.buildingsmart.org/standards/bsi-standards/industry-foundation-classes/) — Página del estándar IFC en el sitio web de buildingSMART International, que documenta el estándar internacional ISO 16739-1:2024, la adopción obligatoria de IFC en construcción pública en Dinamarca desde 2010 y otros casos internacionales.

[^13]: [Instituto de Investigación en Construcción del Ministerio del Interior: Informe de resultados del plan de promoción de la aplicación de Modelado de Información de Construcción (BIM) (año 112)](https://ws.moi.gov.tw/001/Upload/404/relfile/9489/315634/0cccc6e2-2dc6-496f-a45f-69b60e2811b1.pdf) — Informe de resultados del ABRI de 2023 (año 112 de la República), que reconoce el diagnóstico oficial de que "la mayoría de las aplicaciones de BIM en el sector público se concentran en las fases de diseño y construcción, mientras que la gestión operativa y de mantenimiento aún adopta prácticas tradicionales".

[^14]: [Oficina de Ingeniería del Metro del Gobierno de Nueva Taipéi: Aplicación de BIM en la Línea Wan-Ta del Metro](https://www.dorts.ntpc.gov.tw/documentary/articleInfo/P9z2zp0nZrDp?page=216) — Documento de la colección de ingeniería de la Oficina de Metro de Nueva Taipéi, que registra que la Línea Wan-Ta del Metro de Taipéi fue "la primera obra pública en incorporar BIM en el contrato" y la reducción de conflictos en las interfaces de diseño.

[^15]: [Flow BIM Service: Compartiendo casos de edificios comerciales inteligentes](https://bim.flow.tw/smartoffice-globalshowcase/) — Caso compartido por la consultora BIM Flow International, que cita datos específicos de la aplicación de BIM en la Estación Miaoli del Tren de Alta Velocidad de Taiwán: "ahorro del 20% en costos de cambios de diseño, inicio de obra dos meses antes de lo previsto".

[^16]: [Liberty Times Financiero: Se adjudica la Terminal 3 del aeropuerto de Taoyuan, consorcio de Samsung C&T y Rong Gong Engineering gana por 44.5 mil millones de dólares taiwaneses](https://ec.ltn.com.tw/article/breakingnews/3414669) — Comunicado de prensa del Liberty Times de marzo de 2021, que documenta la adjudicación de la obra civil del edificio principal de la Terminal 3 del Aeropuerto de Taoyuan y los detalles específicos del consorcio formado por Samsung C&T y Rong Gong Engineering.

[^17]: [iThome: La industria de la construcción logra el gemelo digital de edificios con BIM, caso de CECI Engineering Consultants](https://www.ithome.com.tw/people/137308) — Reportaje en profundidad de iThome de 2021, entrevista con el ingeniero jefe Lin Yao-tsang de CECI, documentando casos de ciclo de vida completo BIM de CECI como la Estación Fengshan y el Túnel Bagua, y el flujo de colaboración BIM transnacional de la Terminal 3 del Aeropuerto de Taoyuan.

[^18]: [Fundación China Engineering Consultants, Inc. (CECI): 50 hitos clásicos](https://www.ceci.org.tw/modules/article-content.aspx?s=13&i=226) — Cronología del 50.º aniversario en el sitio web oficial de CECI, que documenta la fundación en 1969 y la inversión en la fundación de CECI Engineering Consultants, Inc. en 2007.

[^19]: [CECI Engineering Consultants, S.A.: Perfil de la empresa](https://www.104.com.tw/company/d1w3jw0) — Página de empleo de CECI en 104, que documenta que cerca de 2,000 empleados tienen un 90% de formación profesional en carreteras, ferrocarriles, aeropuertos, puentes, BIM, ITS, PPP y áreas relacionadas, y la creación del primer Centro de Integración BIM en 2010.

[^20]: [Fundación Sinotech Engineering Consultants: Hacia el 50.º aniversario de Sinotech Engineering](https://50th-anniversary.sinotech.org.tw/about_ltd.html) — Sitio web del 50.º aniversario de la Fundación Sinotech Engineering Consultants, que documenta la fundación en 1970, la transformación en organización sin fines de lucro en 1994 y la inversión posterior en Sinotech Engineering Consultants, Inc.

[^21]: [Autodesk University: Diseño y aplicación de la plataforma de trabajo colaborativo BIM de Sinotech Engineering](https://www.autodesk.com/autodesk-university/class/zhongxinggongchengBIMxietongzuoyepingtaizhishejiyuyingyong-2020) — Presentación técnica de Autodesk University 2020, que documenta la arquitectura técnica de Sinotech Engineering basada en el entorno CDE de ISO 19650 para construir un módulo de seguimiento de incidencias BIM y los siete módulos principales del PMIS.

[^22]: [Sitio web oficial de Evergreen Consulting Engineering Co., Ltd. (EGC)](https://www.egc.com.tw/) — Sitio web oficial de EGC, que documenta la fundación en 1974, más de 80 profesionales, el diseño estructural del Taipei 101 y la Torre T&C de 85 pisos en Kaohsiung, y su clasificación como una de las diez principales consultoras de estructura de edificios altos del mundo por el CTBUH.

[^23]: [Centro de Investigación BIM de la Universidad Nacional de Taiwán: El desarrollo de BIM impacta el sistema arquitectónico actual (Guo Rong-qin, 2011.12)](https://www.ntubim.net/bim2356027396/bim-201112) — Documento académico temprano de referencia en la discusión sobre BIM en Taiwán, uno de los trabajos representativos de la discusión académica sobre BIM en Taiwán publicados por el profesor asociado Guo Rong-qin en 2011.

[^24]: [BSI: Añadiendo impulso a la digitalización de la industria de la construcción, Taiwan BIM Task Group publica el estándar internacional de BIM "ISO 19650 versión en chino"](https://www.bsigroup.com/zh-TW/about-bsi/media-centre/press-release/2019/20197/iso-19650-tw-standard-launch/) — Comunicado de prensa de BSI de 2019, que documenta la publicación de la versión en chino de ISO 19650, la supervisión del director del Instituto de Investigación en Construcción del Ministerio del Interior Wang Rong-jin y la asistencia en la traducción del NTUBIM de la Universidad Nacional de Taiwán.

[^25]: [BIM-API: PyRevit + Dynamo Scripts](https://www.bim-api.com/en/blog/pyrevit-dynamo-scripts/) — Artículo del blog BIM-API, que documenta la cifra de percepción de la industria de que "en Taiwán, el 90% de los arquitectos (con capacidad de diseño BIM) utilizan Revit Architecture".

[^26]: [Sitio web oficial del distribuidor de Graphisoft ArchiCAD Long Ting Information](https://www.academicd.com/) — Sitio web oficial del distribuidor de Graphisoft Taiwán Long Ting Information, que documenta los recursos de soporte de ventas y capacitación de ArchiCAD en Taiwán, posicionado en el mercado como "software BIM más amigable que Revit".

[^27]: [BIM Explorer: Compartiendo experiencia con Tekla Structures](https://tpuaup.blogspot.com/2013/05/tekla-structures.html) — Artículo de blog BIM, que documenta que Tekla Structures es el software dominante en el diseño de estructuras de acero en Taiwán y el estado actual de la industria en el manejo de estructuras de acero complejas (gimnasios, puentes, plantas industriales).

[^28]: [OITC Technology: Diseño de infraestructura con MicroStation](https://www.oitc.com.tw/products-detail/MicroStation/79) — Sitio web oficial del distribuidor de Bentley MicroStation en Taiwán, que documenta el alcance de aplicación de MicroStation en proyectos de infraestructura como ferrocarriles, carreteras, túneles y puentes en Taiwán.

[^29]: [Academia de Arquitectura Digital BIM+ Studio: Curso básico de Dynamo para arquitectura](https://bimstudio.tabc.org.tw/blogs/bim%E7%9F%A5%E8%AD%98%E5%BA%AB/49627) — Descripción del curso del BIM+ Studio del Centro de Construcción de Taiwán, que documenta el momento clave de principios de 2016 cuando Autodesk Taiwán invitó al equipo de desarrollo de Dynamo desde Singapur para impartir cursos en Taiwán.

[^30]: [WeBIM Services: Cómo Dynamo revoluciona el mundo de Revit](https://webim.com.tw/en/tech-en/dynamo-application-webim-3/) — Artículo técnico de WeBIM, que documenta casos de aplicación específicos de Dynamo en el círculo de ingenieros BIM de Taiwán (ordenamiento de coordenadas de ductos de aire, verificación de alturas libres, generación automática de vistas de sección).

[^31]: [Resumen del producto Autodesk Navisworks](https://www.quickly.com.tw/autodesk/navisworks.php) — Sitio web oficial del distribuidor de Autodesk Taiwán Quickly, que documenta las funciones completas de Navisworks Manage: navegación 3D, detección de conflictos, exportación de informes, simulación de cronograma 4D y estimación de costos 5D.

[^32]: [airitiLibrary: Desarrollo y aplicación de la automatización del diseño CSD/SEM para metro asistido por BIM](https://www.airitilibrary.com/Article/Detail/0257554X-202107-202107290004-202107290004-77-85) — Artículo académico de revista en la biblioteca en línea Huayi, que documenta la metodología de integración BIM para CSD (Combined Service Drawing) y SEM (Structure / Electric / Mechanic) en la ingeniería de instalaciones del metro de Taiwán.

[^33]: [Grupo CTCI - Wikipedia](https://zh.wikipedia.org/zh-tw/%E4%B8%AD%E9%BC%8E%E9%9B%86%E5%9C%98) — Entrada de Wikipedia del Grupo CTCI, que documenta la fundación en 1979 por inversión conjunta de la Fundación China Technical Service Cooperative con China Development Industrial Bank y Central Investment Company, la adquisición de la mayoría de acciones por la empresa japonesa Chiyoda Corporation en 2011, 7,500 empleados (2021), y casos EPC importantes en el extranjero como Amine en Arabia Saudita, Saudi Kayan y SAMAC MMA.

[^34]: [Sitio web oficial del Grupo CTCI](https://www.ctci.com/www/ctci2022/page.aspx?L=CH) — Sitio web oficial de CTCI Engineering, que documenta el negocio de contratación global de ingeniería, el modelo EPC y el alcance de operaciones en 15 países.

[^35]: [Crossing: Desde la crisis de deudas incobrables masivas de CTCI en el extranjero, mirando la falla fatal en el "control de riesgos internacional" de los contratistas globales taiwaneses](https://crossing.cw.com.tw/article/19832) — Reportaje en profundidad de Crossing del Commonwealth, que documenta el evento controvertido de retrasos significativos y deudas incobrables en el proyecto EPC de una planta de procesamiento de gas natural de CTCI en India en 2017.

[^36]: [Futsu Construction Co., Ltd.: Resultados en plantas de alta tecnología](https://www.futsu.com.tw/p_hitech.html) — Página de plantas de alta tecnología del sitio web oficial de Futsu Construction, que documenta la declaración oficial de "acumula la mayor superficie de piso completada de plantas de alta tecnología, la mayor experiencia nacional en construcción de plantas".

[^37]: [Dacin Engineering: Experiencia BIM](https://www.dacin.com.tw/bim/) — Página de experiencia BIM del sitio web oficial de Dacin Engineering, que documenta la declaración oficial de "utilizando BIM como plataforma de herramienta base para el desarrollo, planificación, diseño, construcción e integración y coordinación de proyectos de construcción".

[^38]: [Obayashi Taiwán: Resumen corporativo](https://www.obayashi.com.tw/topic/about/preview/3250113421819124234) — Sitio web oficial de Obayashi Corporation Taiwán, que documenta la fundación en 1989, la empresa matriz Obayashi Corporation (constructora de la Torre Skytree de Tokio), y "gestión de planos de ejecución y aplicación de BIM" como elemento principal de gestión de construcción.

[^39]: [Taipei Dome - Wikipedia](https://zh.wikipedia.org/zh-tw/%E8%87%BA%E5%8C%97%E5%A4%A7%E5%B7%A8%E8%9B%8B) — Entrada de Wikipedia del Taipei Dome, que documenta la superficie total de piso de 120,000 metros cuadrados, el peso total de la estructura de acero de 65,000 toneladas y las especificaciones de ingeniería como el único domo en el mundo construido enteramente con tubos de acero circulares.

[^40]: [United Daily News: Trabajadores de la generación del abuelo sostienen la obra, la tecnología de la construcción enfrenta una brecha generacional](https://udn.com/news/story/124689/9220106) — Reportaje de investigación del United Daily News, que documenta la realidad del envejecimiento en la industria de la construcción con más del 77% de los más de 100 casos de muerte por accidentes laborales en Nueva Taipéi teniendo más de 40 años.

[^41]: [Liberty Times: ¡Gran escasez de mano de obra en toda Taiwán! Las 15,000 plazas para trabajadores migrantes en la construcción están a punto de agotarse](https://estate.ltn.com.tw/article/21452) — Reportaje financiero del Liberty Times, que documenta la crisis estructural de mano de obra con la aprobación del Ministerio de Trabajo de 15,000 plazas para trabajadores migrantes en la construcción en 2024-2026 y la asignación casi agotada.

[^42]: [Portal de empleo 1111: Resultados de búsqueda de puestos de ingeniero BIM con salario mensual superior a 50,000](https://www.1111.com.tw/search/job?page=1&col=ab&sort=desc&ks=bim,%E7%B9%AA%E5%9C%96&st=1&sa0=50000*) — Página de búsqueda de puestos de ingeniero BIM en el portal de empleo 1111, que documenta la situación salarial de los ingenieros BIM en Taiwán: 104 puestos con salario mensual superior a 50,000 y salario inicial para principiantes de 35,000-45,000 dólares taiwaneses.

[^43]: [¿Por qué es difícil implementar BIM en Taiwán? Cuatro etapas revelan la verdad y las oportunidades](https://engineeringlifetw.com/whynotbim/) — Artículo de análisis profundo del blog工地人生 (Vida en la Obra), que documenta las resistencias culturales a la promoción de BIM en Taiwán: "en el pasado la gestión de construcción gubernamental se basaba en CAD, los flujos de la industria seguían CAD, los modelos BIM se convirtieron en trabajo subcontratado, muchos centros o equipos BIM se disolvieron".

[^44]: [Verakey Engineering Consultants: ¿Qué es BIM? Análisis completo de las 5 principales ventajas de BIM](https://veracityconsultant.com.tw/what-is-bim/) — Sitio web oficial de la consultora BIM Verakey, que explica la esencia de la transformación digital de la ingeniería que es la sistematización de la información del edificio (materiales, especificaciones, proveedores, precios, secuencia de construcción, ciclos de mantenimiento).

[^45]: [Instituto de Investigación en Construcción del Ministerio del Interior de la República de China: Plan de promoción de la aplicación de BIM](https://www.abri.gov.tw/News_Content_Table.aspx?n=807&s=39506) — Página del plan del ABRI, que documenta el autodiagnóstico del estado actual de la promoción de BIM en Taiwán: "los modelos BIM se convirtieron en trabajo subcontratado, desconectados de la obra real, muchos centros o equipos BIM se disolvieron".

[^46]: [Anthropic: Presentando el Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) — Anuncio oficial de Anthropic del 25 de noviembre de 2024, abriendo el código del Model Context Protocol (MCP), describiendo "Think of MCP like a USB-C port for AI applications" y los SDK para Python / TypeScript / C# / Java publicados simultáneamente.

[^47]: [Wikipedia: Model Context Protocol](https://en.wikipedia.org/wiki/Model_Context_Protocol) — Entrada de Wikipedia en inglés sobre MCP, que documenta la apertura de código por Anthropic el 25 de noviembre de 2024 y la donación de MCP por Anthropic a la Agentic AI Foundation (bajo la Linux Foundation) en diciembre de 2025.

[^48]: [Página personal de GitHub de shuotao](https://github.com/shuotao) — Página personal de GitHub de CHIANG SHUOTAO, que documenta la ubicación Tokio y la serie de repositorios periféricos de experimentos de código abierto BIM × MCP × IA (CAD_MCP_study, NAVISWORK_MCP, IFCSH, etc.).

[^49]: [shuotao/CAD_MCP_study repositorio GitHub](https://github.com/shuotao/CAD_MCP_study) — Proyecto de enseñanza de código abierto CAD × MCP de Shuotao, que forma parte de la serie de experimentos de código abierto personales BIM × MCP × IA junto con REVIT_MCP_study y NAVISWORK_MCP.

[^50]: [Architosh: Autodesk Revit 2027 — Grandes cambios nuevos en IA y gráficos](https://architosh.com/2026/04/autodesk-revit-2027-big-new-ai-and-graphics-changes/) — Reportaje de abril de 2026 del medio profesional de software de arquitectura Architosh, que documenta en detalle las funciones y arquitectura específicas del servidor MCP nativo + Autodesk Assistant en Autodesk Revit 2027.

[^51]: [AutoCAD - Wikipedia](https://en.wikipedia.org/wiki/AutoCAD) — Entrada de Wikipedia en inglés sobre AutoCAD, que documenta la línea de tiempo histórica del lanzamiento inicial en plataformas CP/M e IBM PC en diciembre de 1982, la versión para Classic Mac OS en 1992 y la versión para Microsoft Windows en 1993.

[^52]: [Modelado de Información de Construcción - Wikipedia](https://zh.wikipedia.org/zh-tw/%E5%BB%BA%E7%AF%89%E4%BF%A1%E6%81%AF%E6%A8%A1%E5%9E%8B) — Entrada de Wikipedia en chino tradicional sobre BIM, que documenta la historia del desarrollo académico: propuesta por primera vez en 1975, investigación por académicos finlandeses y estadounidenses en la década de 1980, y la introducción del término "Building Information Modeling" por Autodesk en 2002.

[^53]: [BSI Taiwán: El valor comercial del Modelado de Información de Construcción (BIM)](https://www.bsigroup.com/zh-TW/insights-and-media/insights/blogs/business-value-of-building-information-modelling-bim/) — Blog oficial de BSI Taiwán, que documenta la observación del problema estructural del lado del cliente: "los clientes carecen de un conocimiento suficiente sobre la aplicación de BIM y a menudo trabajan con flujos de trabajo de ingeniería tradicionales, lo que limita la eficacia de la tecnología BIM".
