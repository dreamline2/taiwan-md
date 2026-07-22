---
title: 'Catálogo de módulos de visualización: diecisiete formas de ver los datos de Taiwán'
description: 'Ejemplo activo de módulos de visualización de Taiwan.md — con datos reales de vivienda y población de Taiwán, se renderiza cada módulo tw-* una vez, junto con la sintaxis y los principios de diseño de graph.md.'
date: 2026-06-06
category: 'About'
tags:
  - 'visualización de datos'
  - 'justicia habitacional'
  - 'política de vivienda'
  - 'datos abiertos'
author: 'Taiwan.md'
readingTime: 11
featured: false
lastVerified: 2026-06-12
lastHumanReview: false
translatedFrom: 'About/視覺化模組型錄.md'
sourceCommitSha: '31a05c44'
sourceContentHash: 'sha256:38fecc11c893b25a'
sourceBodyHash: 'sha256:09331c2942b129a6'
translatedAt: '2026-06-13T00:46:25+08:00'
image: '/article-images/society/taipei-skyline-housing-2026.webp'
imageCredit: 'Heeheemalu'
imageLicense: 'CC BY-SA 4.0'
imageSource: 'https://commons.wikimedia.org/wiki/File:20260204_Taipei,_Taiwan_Skyline.jpg'
---

# Catálogo de módulos de visualización: diecisiete formas de ver los datos de Taiwán

> **Resumen de 30 segundos:** Esta página es el “ejemplo activo” del sistema de visualización de Taiwan.md — renderiza una vez cada uno de los diecisiete módulos de visualización de artículos, usando datos reales de Taiwán (relación precio‑ingreso, viviendas públicas, envejecimiento, referéndum). Es el complemento de la guía editorial [graph.md](https://github.com/frank890417/taiwan-md/blob/main/docs/editorial/graph.md): **graph.md explica “cuándo usar cuál, cómo hacerlo bien, cómo escribir la sintaxis”, y esta página te muestra directamente “cómo se ve”.** Cada módulo se genera con HTML/SVG puro, por lo que personas, lectores de pantalla, Google y bots de IA pueden leer los mismos datos — esa es la razón por la que elegimos visualizaciones estáticas en lugar de gráficos interactivos.

Al escribir un artículo basado en cifras, lo peor es convertir los datos en una sucesión de números sin contexto; el lector se desconecta al tercer porcentaje. La visualización transforma el “prosa densa de números” en una “estructura legible de un vistazo”.

Pero la visualización de Taiwan.md sigue una disciplina que otros no tienen: **solo hacemos visualizaciones “legibles para LLM”.** Un gráfico interactivo hecho con D3 o Canvas puede ser llamativo, pero GPTBot, PerplexityBot, ClaudeBot y otros bots de IA no ejecutan JavaScript; para ellos ese gráfico es un vacío. Con HTML semántico y SVG en línea, los datos están en el código fuente, y la IA puede leerlos y citar los datos de Taiwán en sus seis idiomas. **Una visualización que entiende la IA es una visualización soberana.**

A continuación, diecisiete módulos, desde el “número grande” más sencillo hasta el “mosaico de municipios”, presentados en orden. La sintaxis completa y los principios de diseño están en graph.md; aquí solo incluimos una frase “qué es y cuándo usarlo”.

## Número grande tw-figure

La forma más simple y poderosa: colocar un número impactante en grande, con contraste antes‑después para contar una transformación. Ideal como “estadística martillo”.

```tw-figure
6.7 万 → 87 万 / 坪
Taipei 成功國宅 1985 年的滯銷配售價，到 2026 年的房仲均價——同一個門牌，約 13 倍
實價登錄房仲平台（成功國宅）
```

## Conjunto de datos tw-stat

Cuando un párrafo contiene tres o cuatro cifras clave, en lugar de escribir una frase larga, dispónlas en una fila de tarjetas para que el lector las escanee de un vistazo.

```tw-stat
174,891 戶 | 政府直接興建的國宅 | 1976–1999
39 萬餘戶 | 廣義國宅總量 | 至 2015 年廢止
84.4% | 全台自有住宅率 | 2024 年
```

## Tarjeta comparativa tw-versus

Dos sistemas, dos posturas o dos estados comparados punto a punto. Color cálido a la izquierda, frío a la derecha, con un “vs” central.

```tw-versus
台灣國宅 | 香港居屋
政府補貼、便宜賣給住戶 | 政府補貼、便宜賣給住戶
住滿一年即可全市價轉售 | 公開市場轉售須先「補地價」
增值幾乎全歸個人 | 增值按原折扣比例回收公庫
公共存量一次性流失 | 公共讓利收得回來
```

## Barra de proporción tw-bars

Comparación o ranking de pocos categorías; la longitud horizontal se escala automáticamente según el valor, y el máximo ocupa todo el ancho. Recuerda añadir una fila `來源：` al final; se convertirá en la nota de fuente.

```tw-bars
全國 2014 | 8.41 倍
全國 2024 | 10.76 倍
台北 2024 | 16.60 倍 | 歷史峰值
來源：內政部不動產資訊平台、政大不動產研究中心
```

## Diagrama de mosaico tw-waffle

Proporción de partes sobre el todo; cada 100 casillas representan el 100 %. Más intuitivo que un pastel porque puedes contar los cuadros. Útil cuando la suma de categorías ronda el 100 %.

```tw-waffle
維也納的住宅組成（2023）
市營社宅 | 21.9
限利潤社宅 | 21.4
自有住宅 | 20.4
私人租賃 | 36.3
來源：維也納市政府（Stadt Wien）住宅統計
```

## Línea de política tw-timeline

Ejes temporales que conectan hitos clave de un sistema o política. Es “apoyo visual”, no debe confundirse con usar fechas como subtítulos en el texto.

```tw-timeline
1975 | 國宅條例上路 | 政府蓋了賣，設「買家資格」閉環，補貼跑不掉
2002 | 那道牆被拆掉 | 修法取消買家資格限制，國宅住滿一年可賣給任何人
2015 | 國宅條例廢止 | 官方理由：自有住宅率已 85%，改走只租不售的社宅
2026 | 桃園把閘門裝回 | 可負擔住宅：轉售不得超過原承購價
```

## Tarjeta de cita tw-quote

Cuando una frase resume la tensión central del artículo, conviértela en una tarjeta de cita. No añadas comillas; el módulo las inserta. La cita debe ser literal y verificable.

```tw-quote
市價 3000 萬元的房子，變成 6000 至 7000 萬元的房子……劫貧濟富，國家出錢幫有錢人改建房子
林智群 | 律師，2025 年批「國家出錢替成功國宅都更」提案
```

## Chip de fuente tw-source

Concentra las fuentes de una sección de análisis en un pequeño chip al margen. La credibilidad forma parte de la curaduría — muchos medios digitales de Taiwán olvidan citar fuentes; aquí podemos hacerlo diferente.

```tw-source
內政部不動產資訊平台、實價登錄、政大不動產研究中心、立法院公報、香港房屋委員會
```

## Caja explicativa tw-note

La mitad de la credibilidad de un artículo de datos está en “cómo lo calculaste”. Los reporteros usan bloques de **nota** para explicar métodos, correcciones o actualizaciones; este módulo lo estandariza. La primera fila indica `說明`/`方法`/`註`/`更正`/`更新`, y cada fila posterior es un párrafo independiente.

```tw-note
說明
本頁「老化指數」＝65 歲以上人口 ÷ 0–14 歲人口 × 100。等於 100 代表老人和小孩一樣多，數字越高代表這個地方越「頭重腳輕」。
高齡化率與老化指數取自內政部戶政司 2025 年底統計，完整的 22 縣市分析見〈用數據看台灣 22 縣市〉。
```

## Gráfica de línea tw-line

Para tendencias con más de cuatro puntos temporales, usa una línea con SVG en línea; el eje Y muestra los límites para que el lector vea el rango. Lo crucial es que **se genera automáticamente una tabla oculta** que los lectores de pantalla y los bots de IA pueden leer. El gráfico sirve a la vista, la tabla al motor.

```tw-line
全國房價所得比的十年攀升（倍）
年 | 全國
2014 | 8.41
2016 | 9.32
2018 | 8.57
2020 | 9.20
2022 | 9.61
2024 | 10.76
基準：2014 起點 | 8.41
來源：政大不動產研究中心、內政部不動產資訊平台
```

Las líneas también admiten **líneas de referencia**: añade una fila `基準：標籤 | 值` y aparecerá como una línea discontinua sin extremos, separada visualmente de la serie medida.

## Gráfica de pendiente tw-slope

Cuando solo tienes “dos puntos temporales”, la línea de tendencia desperdicia espacio. La gráfica de pendiente conecta directamente los extremos y muestra la inclinación; quien sube más rápido o quién supera a quién se ve de un vistazo. Usa `*` al inicio de una fila para resaltarla; el resto se atenuará.

```tw-slope
房價所得比：十年之間誰漲得兇（倍）
2014 | 2024
全國 | 8.41 | 10.76
*台北 | 12.0 | 16.60
來源：內政部不動產資訊平台、政大不動產研究中心
```

## Mapa de calor tw-heatmap

Matriz de regiones × indicadores o años × categorías. Cada columna se normaliza en intensidad de color; los valores mayores son más cálidos. Es una tabla HTML, por lo que es inherentemente legible por IA — esa es la ventaja frente a una imagen de mapa de calor.

```tw-heatmap
縣市 | 房價所得比（倍） | 房貸負擔率（%）
台北 | 16.60 | 63.9
新北 | 13.03 | 56.9
台中 | 11.11 | 48.0
桃園 | 9.0 | 40.0
來源：內政部不動產資訊平台
```

## Diagrama de puntos tw-dot

Los diagramas de barras muestran “cantidad”; los de puntos muestran “distribución”: cada punto está en la misma escala, así puedes ver quién está agrupado y quién es un valor atípico. Cada fila con un solo valor crea una tira de puntos; con dos valores se dibuja un intervalo. `*` funciona igual para resaltar.

```tw-dot
高齡化率的兩極：最年輕到最老的縣市（65 歲以上占比，%）
新竹縣 | 15.08 | 全台最年輕
桃園 | 16.72
台中 | 17.40
新北 | 19.95
台南 | 20.48
高雄 | 20.79
*嘉義縣 | 24.11 | 全台最老
*台北 | 24.18 | 六都最老
來源：內政部戶政司，2025 年底
```

## Barras apiladas tw-stack

Los diagramas de mosaico son útiles para la composición de “un todo”; las barras apiladas sirven para **comparar composiciones a través de varias filas** — cada fila se normaliza al 100 % y, si hay espacio suficiente, el valor se muestra dentro del bloque de color.

```tw-stack
三場核能公投：同意 vs 不同意（有效票占比 %）
公投 | 同意 | 不同意
2018 以核養綠 | 59 | 41
2021 重啟核四 | 47 | 53
2025 核三延役 | 74 | 26
來源：中央選舉委員會三場公投官方審定結果
```

## Pirámide tw-pyramid

Barras espejo, una a cada lado, con una etiqueta central — el clásico gráfico demográfico. Aquí muestra la “carga de cabeza” de seis municipios: izquierda niños, derecha ancianos; al comparar ambos lados, la proporción de ancianos deja de ser un porcentaje abstracto.

```tw-pyramid
頭重腳輕：六縣市的幼年 vs 老年人口占比（%）
縣市 | 0–14 歲 | 65 歲以上
新竹縣 | 14.80 | 15.08
桃園 | 13.13 | 16.72
台中 | 12.75 | 17.40
台北 | 11.97 | 24.18
基隆 | 9.28 | 22.28
嘉義縣 | 8.27 | 24.11
來源：內政部戶政司 2025 年底；幼年占比由高齡化率 ÷ 老化指數 × 100 推算
```

## Mosaico de municipios tw-tiles

Los mapas coropléticos de Taiwán tienen dos problemas: Hualien y Taitung ocupan tanto espacio que dominan la visual, y los dibujos de IA de la forma de Taiwán a menudo terminan pareciendo “entre una oliva y una patata”. El mosaico coloca los 22 municipios en bloques de igual tamaño (disposición fija en el sistema, respetando la posición relativa real); cada bloque tiene el mismo peso y el número se escribe directamente sobre él. La forma siempre es correcta porque no se dibuja la silueta.

```tw-tiles
全台 22 縣市高齡化率（65 歲以上人口占比，%）
臺北市 | 24.18
新北市 | 19.95
桃園市 | 16.72
臺中市 | 17.40
臺南市 | 20.48
高雄市 | 20.79
基隆市 | 22.28
新竹市 | 16.16
嘉義市 | 19.90
新竹縣 | 15.08
苗栗縣 | 20.23
彰化縣 | 20.37
南投縣 | 22.66
雲林縣 | 21.76
嘉義縣 | 24.11
屏東縣 | 21.84
宜蘭縣 | 20.77
花蓮縣 | 21.52
臺東縣 | 20.93
澎湖縣 | 21.03
金門縣 | 19.69
連江縣 | 17.14
來源：內政部戶政司，2025 年底
```

## Diagrama de unidades tw-iso

“174,891 hogares” es un número que se olvida; nueve puntos que pueden contarse con los dedos son más tangibles. El diagrama de unidades convierte un número grande en “un símbolo = cuánto”. Solo se usan enteros; el valor exacto se escribe al lado.

```tw-iso
政府這 24 年蓋了多少國宅
單位：● = 20,000 戶
政府直接興建 | 174,891 戶 | 1976–1999
廣義國宅總量 | 390,000 餘戶 | 至 2015 年廢止
來源：行政院廢止國民住宅條例新聞稿
```

## Cómo usar estos módulos

Cada módulo se escribe en el Markdown del artículo dentro de un bloque ` ```tw-* `, usando `|` para separar columnas; al compilar, se transforma automáticamente en la visualización que ves — el autor no necesita escribir HTML ni JavaScript. La sintaxis completa, cuándo usar cada tipo, colores y ejes que eviten confusión, y la lista de verificación visual antes de publicar, están en [graph.md](https://github.com/frank890417/taiwan-md/blob/main/docs/editorial/graph.md).

Este sistema se inspira en la filosofía editorial de medios narrativos como [The Pudding](https://pudding.cool/): el problema antes que los datos, conclusiones claras, y la atribución como protagonista — pero adaptado a la anatomía propia de Taiwan.md: estático, multilingüe y legible por IA. El contexto completo del diseño está en el [Informe del sistema de visualización](https://github.com/frank890417/taiwan-md/blob/main/reports/article-visualization-design-2026-06-06.md).

Para ver cómo estos módulos se insertan en un artículo profundo, lee [Vivienda pública y justicia habitacional](/society/國宅與居住正義) — la mayoría de los datos de esta página provienen de esa investigación.

**Lecturas complementarias**:

- [Vivienda pública y justicia habitacional](/society/國宅與居住正義) — la historia completa detrás de los datos de vivienda: cómo la vivienda pública pasó de ser vivienda barata a una escalera de activos, y la mayor parte de los módulos usan esas cifras.
- [Ver Taiwán con datos](/geography/用數據看台灣22縣市) — los datos de envejecimiento para los diagramas de puntos, pirámide y mosaico provienen de este análisis de los 22 municipios.
- [Debate sobre la energía nuclear en Taiwán](/society/台灣與核能的討論) — la historia completa de los tres referéndums que alimentan el diagrama de barras apiladas.
- [Vivienda social y justicia habitacional](/society/社會住宅與居住正義) — la ruta de “solo alquiler, no venta” después de 2016.
- [Crisis de natalidad en Taiwán](/society/台灣少子化危機) — la imposibilidad de comprar vivienda y la falta de hijos, otra cara de la justicia generacional.

## Referencias

[^1]: [內政部不動產資訊平台](https://pip.moi.gov.tw/Publicize/Info/E1050) — datos oficiales de relación precio‑ingreso, carga hipotecaria y tasa de vivienda propia.

[^2]: [政大不動產研究中心](https://rer.nccu.edu.tw/article/detail/2210058908437) — indicadores históricos de asequibilidad de la vivienda; fuente de la línea y barra de proporción.

[^3]: [行政院廢止國民住宅條例新聞稿](https://www.ey.gov.tw/Page/9277F759E41CCD91/d4afaf10-ece5-4b4f-9482-35ce16bdc657) — número acumulado de viviendas públicas (≈ 390 mil).

[^4]: [內政部戶政司人口統計資料](https://www.ris.gov.tw/app/portal/346) — proporción de población mayor de 65 años y índice de envejecimiento al final de 2025; datos para los diagramas de puntos, pirámide, mosaico y caja explicativa; cadena de verificación completa en〈[Ver Taiwán con datos](/geography/用數據看台灣22縣市)〉.

[^5]: [中央選舉委員會 2018 年第 16 案公投結果（PDF）](https://web.cec.gov.tw/api/file/0132581c-18b5-4951-bc24-3cc083924666.pdf) — resultados oficiales de los tres referéndums nucleares (59 %/47 %/74 %); cadena de verificación completa en〈[Debate sobre la energía nuclear en Taiwán](/society/台灣與核能的討論)〉.

## Fuente de la imagen

Esta publicación usa una imagen bajo licencia CC BY‑SA 4.0, almacenada en `public/article-images/society/`:

- [Taipei skyline (vista desde Xiangshan)](https://commons.wikimedia.org/wiki/File:20260204_Taipei,_Taiwan_Skyline.jpg) — Foto: Heeheemalu, 2026, CC BY‑SA 4.0 (hero)
