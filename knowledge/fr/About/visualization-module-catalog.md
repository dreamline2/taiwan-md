---
title: 'Catalogue des modules de visualisation : dix‑sept méthodes pour voir les données de Taïwan'
description: "Exemple vivant des modules de visualisation d'articles de Taiwan.md — en utilisant des données réelles de logement et de population de Taïwan, chaque module tw-* est rendu une fois, accompagné de la syntaxe et des principes de conception de graph.md."
date: 2026-06-06
category: 'About'
tags:
  - 'visualisation de données'
  - 'justice du logement'
  - 'politique du logement'
  - 'données ouvertes'
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

# Catalogue des modules de visualisation : dix‑sept méthodes pour voir les données de Taïwan

> **Vue d’ensemble en 30 secondes :** cette page est le « exemple vivant » du système de visualisation de Taiwan.md — elle rend chaque l’un des dix‑sept modules de visualisation d’articles une fois, en utilisant des données réelles de Taïwan (ratio prix du logement/revenu, logements publics, vieillissement, référendums). Elle accompagne le guide d’édition [graph.md](https://github.com/frank890417/taiwan-md/blob/main/docs/editorial/graph.md) : **graph.md explique « quand utiliser quoi, comment le faire correctement, quelle syntaxe employer », cette page vous montre directement «  à quoi cela ressemble ».** Chaque module est rendu en HTML/SVG pur, de sorte que les personnes, les lecteurs d’écran, Google et les IA peuvent lire les mêmes données — c’est la raison pour laquelle nous privilégions les visualisations statiques aux graphiques interactifs.

Lorsque l’on rédige un article axé sur les chiffres, le pire est de transformer les données en une succession de nombres empilés, ce qui fait que le lecteur se désengage dès le troisième pourcentage. Le travail de visualisation consiste à transformer « un texte dense en chiffres » en « une structure lisible d’un seul coup d’œil ».

Mais la visualisation de Taiwan.md suit une discipline que les autres n’ont pas : **nous ne créons que des visualisations « compréhensibles par les LLM »**. Un graphique interactif réalisé avec D3 ou Canvas est impressionnant, mais les IA comme GPTBot, PerplexityBot ou ClaudeBot n’exécutent pas de JavaScript ; pour elles, ce graphique est une page blanche. En revanche, nos graphiques construits avec du HTML sémantique et du SVG en ligne contiennent les données dans le code source, accessibles aux IA dans les six langues supportées. **Une visualisation lisible par les LLM est une visualisation souveraine.**

Les dix‑sept modules ci‑dessous, du plus simple « un grand nombre » au « carte en briques des comtés », sont présentés dans cet ordre. La version complète de la syntaxe et des principes de conception se trouve dans graph.md ; ici nous ne donnons qu’une phrase « qu’est‑ce que c’est, quand l’utiliser ».

## Grand nombre de données tw-figure

Le type le plus simple et le plus percutant : mettre un chiffre marquant en grand, avec un contraste avant‑après pour illustrer une transformation. Idéal comme « statistique marteau ».

```tw-figure
6.7 萬 → 87 萬 / 坪
台北成功國宅 1985 年的滯銷配售價，到 2026 年的房仲均價——同一個門牌，約 13 倍
實價登錄房仲平台（成功國宅）
```

## Ensemble de données tw-stat

Lorsqu’un paragraphe contient trois ou quatre chiffres clés, il vaut mieux les disposer en rangée de cartes plutôt que de les entasser dans une longue phrase.

```tw-stat
174,891 戶 | 政府直接興建的國宅 | 1976–1999
39 萬餘戶 | 廣義國宅總量 | 至 2015 年廢止
84.4% | 全台自有住宅率 | 2024 年
```

## Carte comparative tw-versus

Deux systèmes, deux positions, ou deux états successifs comparés point par point. Couleur chaude à gauche, froide à droite, avec un « vs » central, pour lire les différences ligne par ligne.

```tw-versus
台灣國宅 | 香港居屋
政府補貼、便宜賣給住戶 | 政府補貼、便宜賣給住戶
住滿一年即可全市價轉售 | 公開市場轉售須先「補地價」
增值幾乎全歸個人 | 增值按原折扣比例回收公庫
公共存量一次性流失 | 公共讓利收得回來
```

## Barres proportionnelles tw-bars

Comparaison ou classement de quelques catégories ; la longueur des barres horizontales s’ajuste automatiquement aux valeurs, la plus grande remplissant la largeur. N’oubliez pas d’ajouter une ligne `來源：` à la fin ; elle sera transformée en annotation de source.

```tw-bars
全國 2014 | 8.41 倍
全國 2024 | 10.76 倍
台北 2024 | 16.60 倍 | 歷史峰值
來源：內政部不動產資訊平台、政大不動產研究中心
```

## Diagramme en grille tw-waffle

Proportion d’une partie par rapport au tout ; cent cases représentent cent pour cent, plus intuitif qu’un camembert — vous pouvez réellement compter les cases. Idéal pour des données dont la somme s’approche de 100 %.

```tw-waffle
維也納的住宅組成（2023）
市營社宅 | 21.9
限利潤社宅 | 21.4
自有住宅 | 20.4
私人租賃 | 36.3
來源：維也納市政府（Stadt Wien）住宅統計
```

## Axe de politique tw-timeline

Points clés d’un système ou d’une politique présentés sur une frise chronologique. Il s’agit d’un « aide visuelle », distinct des titres de section qui ne doivent pas être chronologiques.

```tw-timeline
1975 | 國宅條例上路 | 政府蓋了賣，設「買家資格」閉環，補貼跑不掉
2002 | 那道牆被拆掉 | 修法取消買家資格限制，國宅住滿一年可賣給任何人
2015 | 國宅條例廢止 | 官方理由：自有住宅率已 85%，改走只租不售的社宅
2026 | 桃園把閘門裝回 | 可負擔住宅：轉售不得超過原承購價
```

## Carte de citation tw-quote

Quand une phrase résume la tension centrale de tout l’article, on l’amplifie en carte de citation. Le module ajoute les guillemets ; la citation doit être littérale et vérifiable.

```tw-quote
市價 3000 萬元的房子，變成 6000 至 7000 萬元的房子……劫貧濟富，國家出錢幫有錢人改建房子
林智群 | 律師，2025 年批「國家出錢替成功國宅都更」提案
```

## Bande source tw-source

Regroupe les sources d’une analyse en une petite puce discrète placée à côté du paragraphe. La crédibilité fait partie de la curation — les médias numériques taïwanais oublient souvent de citer leurs sources, ce que nous pouvons corriger.

```tw-source
內政部不動產資訊平台、實價登錄、政大不動產研究中心、立法院公報、香港房屋委員會
```

## Boîte explicative tw-note

La crédibilité d’un article de données repose en partie sur « comment le calcul a été fait ». Les journalistes utilisent des blocs « explication » pour détailler les méthodes, les notes de bas de page pour les corrections. Le module suit cette convention : la première ligne indique `說明`/`方法`/`註`/`更正`/`更新`, chaque ligne suivante forme un paragraphe autonome.

```tw-note
說明
本頁「老化指數」＝65 歲以上人口 ÷ 0–14 歲人口 × 100。等於 100 代表老人和小孩一樣多，數字越高代表這個地方越「頭重腳輕」。
高齡化率與老化指數取自內政部戶政司 2025 年底統計，完整的 22 縣市分析見〈用數據看台灣 22 縣市〉。
```

## Graphique en ligne tw-line

Pour plus de quatre points temporels, on utilise une courbe tracée en SVG ; les limites supérieure et inférieure de l’axe y sont affichées pour que le lecteur perçoive l’amplitude. Le point crucial : le module génère automatiquement un tableau de données caché, lisible par les lecteurs d’écran et les IA. Le graphique sert aux humains, le tableau aux machines, les deux étant identiques en contenu.

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

Les graphiques en ligne supportent aussi des **lignes de référence** : ajoutez une ligne `基準：標籤 | 值` qui sera dessinée en pointillé, sans point d’ancrage, uniquement avec une étiquette, afin de ne pas confondre une valeur fixe avec les données mesurées.

## Diagramme de pente tw-slope

Lorsque l’on ne dispose que de « deux points temporels », le graphique en ligne gaspille l’espace intermédiaire. Le diagramme de pente relie directement les deux extrémités, montrant qui a augmenté le plus rapidement. Un `*` devant une ligne la met en évidence, les autres s’estompent.

```tw-slope
房價所得比：十年之間誰漲得兇（倍）
2014 | 2024
全國 | 8.41 | 10.76
*台北 | 12.0 | 16.60
來源：內政部不動產資訊平台、政大不動產研究中心
```

## Carte thermique tw-heatmap

Matrice région × indicateur ou année × catégorie. Chaque colonne est normalisée en intensité de couleur ; plus le nombre est grand, plus la teinte est chaude. C’est intrinsèquement un tableau HTML, donc immédiatement lisible par les IA — c’est pourquoi les cartes thermiques sont préférées aux images colorées.

```tw-heatmap
縣市 | 房價所得比（倍） | 房貸負擔率（%）
台北 | 16.60 | 63.9
新北 | 13.03 | 56.9
台中 | 11.11 | 48.0
桃園 | 9.0 | 40.0
來源：內政部不動產資訊平台
```

## Diagramme à points tw-dot

Les diagrammes à barres montrent la « quantité », le diagramme à points montre la « distribution » : chaque point représente une valeur, vous voyez qui se regroupe et qui est isolé. Une ligne unique donne une valeur, deux valeurs créent un intervalle. Le `*` fonctionne de la même façon.

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

## Barres empilées tw-stack

Le diagramme en grille convient à la composition d’un tout ; les barres empilées conviennent à la comparaison de plusieurs ensembles — chaque rangée est normalisée à 100 %, et si l’espace le permet les valeurs sont affichées directement dans les blocs colorés.

```tw-stack
三場核能公投：同意 vs 不同意（有效票占比 %）
公投 | 同意 | 不同意
2018 以核養綠 | 59 | 41
2021 重啟核四 | 47 | 53
2025 核三延役 | 74 | 26
來源：中央選舉委員會三場公投官方審定結果
```

## Pyramide tw-pyramid

Barres symétriques dos à dos, chacune représentant un camp, avec une étiquette centrale — le classique diagramme démographique. Ici il montre, pour six comtés, la proportion d’enfants versus celle des personnes âgées : à gauche les jeunes, à droite les aînés, la comparaison rend le vieillissement plus concret qu’un simple pourcentage.

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

## Carte en briques des comtés tw-tiles

Les cartes choroplèthes de Taïwan posent deux problèmes : Hualien et Taitung sont si vastes qu’ils dominent visuellement, et les IA dessinent souvent la forme de Taïwan comme « entre une olive et une pomme de terre ». La carte en briques place les 22 comtés dans des carrés de même taille (disposition codée dans le système selon la position réelle), chaque brique a le même poids visuel, le chiffre est inscrit directement sur la brique. La forme est toujours correcte, car aucune forme géographique n’est dessinée.

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

## Diagramme d’unité tw-iso

« 174 891 foyers » est un nombre difficile à appréhender ; neuf points que l’on peut compter avec les doigts le sont beaucoup plus. Le diagramme d’unité transforme un grand nombre en « un symbole = quantité », méthode utilisée dans les reportages sur la pêche hauturière : il rend le chiffre abstrait tangible. Le symbole reste entier (pas de demi‑symbole) et la valeur exacte est indiquée à côté.

```tw-iso
政府這 24 年蓋了多少國宅
單位：● = 20,000 戶
政府直接興建 | 174,891 戶 | 1976–1999
廣義國宅總量 | 390,000 餘戶 | 至 2015 年廢止
來源：行政院廢止國民住宅條例新聞稿
```

## Comment utiliser ces modules

Chaque module s’insère dans le Markdown d’un article sous la forme d’un bloc `tw-*` avec des colonnes séparées par `|`. Lors de la génération, le bloc est automatiquement transformé en la visualisation affichée ci‑dessus — l’auteur n’a pas besoin d’écrire du HTML ou du JavaScript. La syntaxe complète, les moments propices à chaque type, les palettes de couleurs et les réglages d’axes pour éviter les mauvaises interprétations, ainsi que la checklist de vérification visuelle avant publication, se trouvent dans [graph.md](https://github.com/frank890417/taiwan-md/blob/main/docs/editorial/graph.md).

Ce système s’inspire de la philosophie éditoriale de [The Pudding](https://pudding.cool/) — le problème précède les données, la conclusion doit être claire, la citation est le protagoniste — mais il a évolué pour devenir l’organe propre à Taiwan.md : statique, multilingue, lisible par l’IA. Le contexte complet de conception est détaillé dans le [rapport du système de visualisation d’articles](https://github.com/frank890417/taiwan-md/blob/main/reports/article-visualization-design-2026-06-06.md).

Pour voir comment ces modules s’intègrent dans un article approfondi, consultez [Logements publics et justice du logement](/society/國宅與居住正義) — la plupart des données de cette page proviennent de cette étude.

**Lectures complémentaires** :

- [Logements publics et justice du logement](/society/國宅與居住正義) — l’histoire complète derrière ces données : comment les logements publics sont passés d’un logement bon marché à un ascenseur d’actifs, source de la majorité des modules.
- [Voir les données de Taïwan : 22 comtés](/geography/用數據看台灣22縣市) — les données de vieillissement utilisées dans les diagrammes à points, pyramides et cartes en briques proviennent de cette analyse complète.
- [Taïwan et le débat sur le nucléaire](/society/台灣與核能的討論) — le contexte complet des trois référendums présentés dans le diagramme à barres empilées.
- [Logements sociaux et justice du logement](/society/社會住宅與居住正義) — la trajectoire « location uniquement » après 2016.
- [Crise de la faible natalité à Taïwan](/society/台灣少子化危機) — l’impossibilité d’acheter un logement et le manque de naissances, une autre facette de la justice intergénérationnelle.

## Références

[^1]: [內政部不動產資訊平台](https://pip.moi.gov.tw/Publicize/Info/E1050) — ratios prix du logement/revenu, taux d’endettement hypothécaire, taux de logement propriétaire, etc., statistiques officielles du logement.

[^2]: [政大不動產研究中心](https://rer.nccu.edu.tw/article/detail/2210058908437) — indicateurs historiques de la capacité de paiement du logement, sources des séries nationales du ratio prix/revenu dans les graphiques en ligne et les barres proportionnelles.

[^3]: [行政院廢止國民住宅條例新聞稿](https://www.ey.gov.tw/Page/9277F759E41CCD91/d4afaf10-ece5-4b4f-9482-35ce16bdc657) — données officielles sur le nombre cumulé de foyers de logements publics (environ 390 000).

[^4]: [內政部戶政司人口統計資料](https://www.ris.gov.tw/app/portal/346) — proportions de la population de 65 ans et plus et indice de vieillissement pour chaque comté à la fin de 2025, sources des diagrammes à points, pyramides, cartes en briques et boîtes explicatives ; chaîne de vérification complète dans « [Voir les données de Taïwan : 22 comtés](/geography/用數據看台灣22縣市) ».

[^5]: [中央選舉委員會 2018 年第 16 案公投結果（PDF）](https://web.cec.gov.tw/api/file/0132581c-18b5-4951-bc24-3cc083924666.pdf) — résultats officiels du CEC pour les trois référendums sur le nucléaire (59 %/47 %/74 % d’accord), chaîne de vérification dans « [Taïwan et le débat sur le nucléaire](/society/台灣與核能的討論) ».

## Sources d’images

Cette page utilise une image sous licence CC BY‑SA 4.0, stockée dans `public/article-images/society/` :

- [Silhouette résidentielle de Taipei (vue depuis Xiangshan)](https://commons.wikimedia.org/wiki/File:20260204_Taipei,_Taiwan_Skyline.jpg) — Photo : Heeheemalu, 2026, CC BY‑SA 4.0 (hero)
