---
title: 'Visualization Module Catalog: Seventeen Ways to See Taiwan Data'
description: "Taiwan.md's live examples of visualization modules—using real Taiwan housing and population data to render each tw-* visualization module once, together with the syntax and design principles from graph.md."
date: '2026-06-06'
category: 'About'
tags:
  - 'Data Visualization'
  - 'Housing Justice'
  - 'Housing Policy'
  - 'Open Data'
author: 'Taiwan.md'
readingTime: '11'
featured: false
lastVerified: '2026-06-12'
lastHumanReview: false
translatedFrom: 'About/視覺化模組型錄.md'
sourceCommitSha: '31a05c44'
sourceContentHash: 'sha256:38fecc11c893b25a'
sourceBodyHash: 'sha256:09331c2942b129a6'
translatedAt: '2026-06-13T00:46:21+08:00'
image: '/article-images/society/taipei-skyline-housing-2026.webp'
imageCredit: 'Heeheemalu'
imageLicense: 'CC BY-SA 4.0'
imageSource: 'https://commons.wikimedia.org/wiki/File:20260204_Taipei,_Taiwan_Skyline.jpg'
---

# Visualization Module Catalog: Seventeen Ways to See Taiwan Data

> **30‑second overview:** This page is the “live example” of Taiwan.md’s visualization system—rendering each of the seventeen article‑level visualization modules once, all with real Taiwan data (price‑to‑income ratio, public housing, aging, referendums). It is the companion to the editorial guide [graph.md](https://github.com/frank890417/taiwan-md/blob/main/docs/editorial/graph.md): **graph.md explains “when to use which, how to do it well, and the syntax,” and this page shows you exactly “what it looks like.”** Each module is pure HTML/SVG, so people, screen readers, Google, and AI crawlers all read the same data—this is why we choose static visualizations over interactive charts.

When writing a data‑heavy article, the biggest fear is turning the information into a wall of numbers that makes readers tune out after the third percentage point. Visualization’s job is to turn “dense numeric prose” into “a structure readable at a glance.”

But Taiwan.md’s visualizations follow a discipline that others lack: **we only make visualizations that LLMs can also understand.** An interactive D3 or Canvas chart may look flashy, but GPTBot, PerplexityBot, ClaudeBot and similar AI crawlers do not execute JavaScript; to them the chart is a blank space. Our charts, built with semantic HTML and inline SVG, embed the data directly in the source code, so AI can read and cite Taiwan’s first‑person data in any of the six supported languages. **Visualizations that LLMs can read are sovereign visualizations.**

The seventeen modules below range from the simplest “big number” to “county‑level tile map,” displayed in order. The full syntax and design principles are in graph.md; here we only give a one‑sentence “what it is, when to use it.”

## Data‑Big‑Number `tw-figure`

The simplest and most powerful: put a dramatic figure at maximum size, with a before‑and‑after contrast that tells a transformation story. Ideal for an opening “sledgehammer stat.”

```tw-figure
6.7 萬 → 87 萬 / 坪
Taipei Chenggong Public Housing 1985’s unsold allocation price versus 2026’s average market price—same address, about 13 × increase
Real‑estate transaction platform (Chenggong Public Housing)
```

## Data‑Set `tw-stat`

When a paragraph contains three or four parallel key figures, instead of a long sentence, lay them out as a row of cards for a quick scan.

```tw-stat
174,891 households | Government‑built public housing | 1976–1999
over 390,000 units | Broad public housing total | discontinued in 2015
84.4% | Nationwide home‑ownership rate | 2024
```

## Comparison Card `tw-versus`

Side‑by‑side point‑by‑point comparison of two systems, positions, or time periods. Warm colour on the left, cool on the right, with a “vs” in the middle.

```tw-versus
Taiwan public housing | Hong Kong Home Ownership Scheme
Government subsidy, cheap sale to residents | Government subsidy, cheap sale to residents
Resell at full market price after one year of occupancy | Resell on open market only after “land price subsidy”
Appreciation almost entirely private | Appreciation reclaimed by the treasury at original discount rate
Public stock lost in one go | Public benefit recouped later
```

## Proportion Grid `tw-waffle`

Shows part‑of‑whole composition; 100 squares represent 100 %. More intuitive than a pie chart—you can actually count the squares. Good for data that sum to roughly 100 %.

```tw-waffle
Housing composition in Vienna (2023)
Municipal social housing | 21.9
Limited‑profit social housing | 21.4
Owner‑occupied housing | 20.4
Private rentals | 36.3
Source: City of Vienna (Stadt Wien) housing statistics
```

## Policy Timeline `tw-timeline`

Key policy or institutional milestones linked on a timeline. Note this is a “visual aid,” not a chronological heading in the main text.

```tw-timeline
1975 | Public Housing Act enacted | Government built and sold units, set “buyer eligibility” loop, subsidies unavoidable
2002 | The wall comes down | Legal amendment removes buyer‑eligibility restriction; public housing can be sold after one year of occupancy
2015 | Public Housing Act repealed | Official rationale: home‑ownership rate reached 85 %; shift to rental‑only public housing
2026 | Taoyuan reinstates gate | Affordable housing: resale price may not exceed original purchase price
```

## Quote Card `tw-quote`

When a single sentence captures the core tension of the article, enlarge it as a quote card. The module adds quotation marks automatically; the quote must be verbatim and verifiable.

```tw-quote
A house priced at NT$30 million becomes NT$60–70 million… enriching the rich while impoverishing the poor, the state pays to help the wealthy rebuild.
Lin Chih‑chun | Lawyer, 2025 proposal “State funds for Chenggong public housing redevelopment”
```

## Source Chip `tw-source`

Collect the sources for a paragraph into a low‑key chip placed beside the text. Credibility is part of curation—Taiwan’s digital media often forget to cite sources; this is where we can differ.

```tw-source
Ministry of the Interior Real‑Estate Information Platform, Real‑estate Transaction Registry, NCCU Real‑Estate Research Center, Legislative Yuan Gazette, Hong Kong Housing Authority
```

## Note Box `tw-note`

Half of a data article’s credibility lies in “how you calculated it.” Reporters use a **Note** block to explain methodology or issue corrections; we formalize that as a module. The first line is one of: `說明` (Explanation), `方法` (Method), `註` (Note), `更正` (Correction), `更新` (Update); each subsequent line forms its own paragraph.

```tw-note
說明
This page’s “Aging Index” = (population ≥ 65) ÷ (population 0–14) × 100. A value of 100 means equal numbers of elderly and children; higher values indicate a “top‑heavy” population.
Aging rate and aging index are from the Ministry of the Interior Household Registration Department’s 2025 year‑end statistics; the full analysis of all 22 counties and cities appears in <Using Data to View Taiwan’s 22 Counties and Cities>.
```

## Line Chart `tw-line`

For trends with four or more time points, an inline‑SVG line chart shows the shape, with explicit y‑axis limits so readers see the range. Crucially, it **automatically generates a hidden data table** that screen readers and AI crawlers can read. The chart is for humans; the table is for machines, and they share the same source.

```tw-line
Decade‑long rise in nationwide price‑to‑income ratio (×)
Year | Nationwide
2014 | 8.41
2016 | 9.32
2018 | 8.57
2020 | 9.20
2022 | 9.61
2024 | 10.76
Baseline: 2014 start | 8.41
Source: NCCU Real‑Estate Research Center, Ministry of the Interior Real‑Estate Information Platform
```

Line charts also support **baseline lines**: add a row `Baseline: label | value` to draw a dashed line without endpoints, visually separating it from the measured series.

## Slope Chart `tw-slope`

When you have only **two** time points, a line chart wastes space. A slope chart connects the two ends directly, letting the steepness speak for itself—who surged, who fell, at a glance. Prefix a label with `*` to highlight a row; other rows are automatically de‑emphasized.

```tw-slope
Price‑to‑income ratio: who surged most over ten years (×)
2014 | 2024
Nationwide | 8.41 | 10.76
*Taipei | 12.0 | 16.60
Source: Ministry of the Interior Real‑Estate Information Platform, NCCU Real‑Estate Research Center
```

## Heatmap `tw-heatmap`

A matrix of regions × indicators or years × categories. Each column is normalized to a colour intensity; larger numbers are warmer. Because it is an HTML table, it is inherently AI‑readable—this is why heatmaps are preferred over a single coloured image in our system.

```tw-heatmap
County/City | Price‑to‑income ratio (×) | Mortgage‑burden ratio (%)
Taipei | 16.60 | 63.9
New Taipei | 13.03 | 56.9
Taichung | 11.11 | 48.0
Taoyuan | 9.0 | 40.0
Source: Ministry of the Interior Real‑Estate Information Platform
```

## Dot Plot `tw-dot`

Bar charts show “quantity”; dot plots show “distribution.” All dots lie on the same scale, so you can see clusters and outliers. One value per line creates a dot strip; two values draw a “from‑to” interval. `*` can again highlight rows.

```tw-dot
Polarization of aging rates: youngest to oldest counties (percentage of population ≥ 65)
Hsinchu County | 15.08 | Youngest in Taiwan
Taoyuan | 16.72
Taichung | 17.40
New Taipei | 19.95
Tainan | 20.48
Kaohsiung | 20.79
*Chiayi County | 24.11 | Oldest in Taiwan
*Taipei | 24.18 | Oldest among the six special municipalities
Source: Ministry of the Interior Household Registration Department, 2025 year‑end
```

## Stacked Bar `tw-stack`

Waffle charts are good for a single whole; stacked bars are ideal for **comparing compositions across several rows**—each row automatically normalizes to 100 %, and if the bar is wide enough the values appear inside the colour blocks.

```tw-stack
Three nuclear‑energy referendums: Yes vs No (valid‑vote share %)
Referendum | Yes | No
2018 Keep Nuclear for Green Energy | 59 | 41
2021 Restart Nuclear Plant 4 | 47 | 53
2025 Extend Nuclear Plant 3 | 74 | 26
Source: Central Election Commission, official results of the three referendums
```

## Pyramid `tw-pyramid`

Back‑to‑back bars, one for each side, sharing a common axis—classic demographic pyramid. Here we use it to compare six counties’ “top‑heavy vs bottom‑heavy” structure: children on the left, elderly on the right. When the two sides differ, aging is no longer an abstract percentage.

```tw-pyramid
Top‑heavy vs bottom‑heavy: child vs elderly population share (%) in six counties
County | Age 0–14 | Age ≥ 65
Hsinchu County | 14.80 | 15.08
Taoyuan | 13.13 | 16.72
Taichung | 12.75 | 17.40
Taipei | 11.97 | 24.18
Keelung | 9.28 | 22.28
Chiayi County | 8.27 | 24.11
Source: Ministry of the Interior Household Registration Department, 2025 year‑end; child share derived from aging rate ÷ aging index × 100
```

## County‑Level Tile Map `tw-tiles`

Taiwan’s choropleth maps suffer from two problems: Hualien and Taitung’s large areas dominate visual weight, and AI‑generated outlines of Taiwan often look “between an olive and a potato.” Tiles arrange the 22 counties and cities into equal‑sized squares (layout hard‑coded to reflect real relative positions); each tile carries the same visual weight, and the number is written directly on the tile. The shape is always correct because we never draw the outline.

```tw-tiles
Taiwan’s 22 counties and cities – aging rate (population ≥ 65, %)
Taipei City | 24.18
New Taipei City | 19.95
Taoyuan City | 16.72
Taichung City | 17.40
Tainan City | 20.48
Kaohsiung City | 20.79
Keelung City | 22.28
Hsinchu City | 16.16
Chiayi City | 19.90
Hsinchu County | 15.08
Miaoli County | 20.23
Changhua County | 20.37
Nantou County | 22.66
Yunlin County | 21.76
Chiayi County | 24.11
Pingtung County | 21.84
Yilan County | 20.77
Hualien County | 21.52
Taitung County | 20.93
Penghu County | 21.03
Kinmen County | 19.69
Lienchiang County | 17.14
Source: Ministry of the Interior Household Registration Department, 2025 year‑end
```

## Unit Chart `tw-iso`

“174,891 households” is a number that slips away after a glance; nine hand‑countable dots stay with the reader. A unit chart converts a huge figure into “one symbol = how many,” a technique reporters use for offshore‑fishing pieces: turn an abstract large number into a tangible unit. Symbols use whole numbers only; the exact value is written beside them.

```tw-iso
How many public housing units the government built in 24 years
Unit: ● = 20,000 households
Government‑directly built | 174,891 households | 1976–1999
Broad public housing total | over 390,000 households | discontinued in 2015
Source: Executive Yuan press release on the repeal of the National Housing Act
```

## How to Use These Modules

Each module is written in an article’s Markdown as a fenced block ` ```tw-* ` with columns separated by `|`. During build, it is automatically transformed into the visual you see above—authors never need to write HTML or JavaScript. The complete syntax, guidance on when to use each type, colour‑ and axis‑design best practices, and a pre‑publication visual‑checklist are all in [graph.md](https://github.com/frank890417/taiwan-md/blob/main/docs/editorial/graph.md).

Our system draws inspiration from the visual‑storytelling outlet [The Pudding](https://pudding.cool/), whose editorial philosophy stresses “question before data, clear conclusions, and attribution as the protagonist.” It has evolved into a tool that fits Taiwan.md: static, multilingual, AI‑readable. The full design rationale is documented in the [Visualization System Design Report](https://github.com/frank890417/taiwan-md/blob/main/reports/article-visualization-design-2026-06-06.md).

To see how these modules are woven into a real in‑depth article, read [Public Housing and Housing Justice](/society/國宅與居住正義)—most of the data on this page comes from that research.

**Further Reading**

- [Public Housing and Housing Justice](/society/國宅與居住正義) — the full story behind the housing data: how public housing shifted from cheap homes to an asset ladder; source for most modules on this page
- [Using Data to View Taiwan’s 22 Counties and Cities](/geography/用數據看台灣22縣市) — all aging‑rate data for the dot plot, pyramid, and tile map come from this comprehensive analysis
- [Taiwan and Nuclear Power Debate](/society/台灣與核能的討論) — the full narrative behind the stacked‑bar referendums
- [Social Housing and Housing Justice](/society/社會住宅與居住正義) — the post‑2016 “rental‑only” public housing trajectory
- [Taiwan’s Low‑Birth‑Rate Crisis](/society/台灣少子化危機) — unaffordable housing and declining births, another facet of inter‑generational justice

## References

[^1]: [Ministry of the Interior Real‑Estate Information Platform](https://pip.moi.gov.tw/Publicize/Info/E1050) — official housing statistics such as price‑to‑income ratio, mortgage‑burden ratio, home‑ownership rate.

[^2]: [NCCU Real‑Estate Research Center](https://rer.nccu.edu.tw/article/detail/2210058908437) — historical housing affordability indicators; source for the line chart and proportion bars.

[^3]: [Executive Yuan press release on the repeal of the National Housing Act](https://www.ey.gov.tw/Page/9277F759E41CCD91/d4afaf10-ece5-4b4f-9482-35ce16bdc657) — official figures for cumulative public‑housing units (≈ 390,000).

[^4]: [Ministry of the Interior Household Registration Department population statistics](https://www.ris.gov.tw/app/portal/346) — 2025 year‑end percentages of population ≥ 65 and aging index for all counties and cities; data for dot plot, pyramid, tile map, and note box. Full verification chain in <[Using Data to View Taiwan’s 22 Counties and Cities](/geography/用數據看台灣22縣市)>.

[^5]: [Central Election Commission 2018 Referendum Result (PDF)](https://web.cec.gov.tw/api/file/0132581c-18b5-4951-bc24-3cc083924666.pdf) — official yes‑share percentages (59 %/47 %/74 %) for the three nuclear referendums; verification chain in <[Taiwan and Nuclear Power Debate](/society/台灣與核能的討論)>.

## Image Credit

The article uses one CC‑licensed image, cached in `public/article-images/society/`:

- [Taipei skyline from Xiangshan (2026)](https://commons.wikimedia.org/wiki/File:20260204_Taipei,_Taiwan_Skyline.jpg) — Photo by Heeheemalu, 2026, CC BY‑SA 4.0 (hero)
