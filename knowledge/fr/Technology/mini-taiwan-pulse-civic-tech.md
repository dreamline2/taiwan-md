---
title: 'Mini Taiwan Pulse : dessiner Taïwan comme une carte qui respire, avec un regard de curateur'
description: 'En 2026, l’analyste de données Migu a superposé les données ouvertes éparses de Taïwan, avions, navires, trains, bus et camions-poubelles, pour en faire une carte qui respire. Le travail ingrat de collecte des données est confié à l’IA ; mais choisir quelles couches empiler, quelles couleurs employer et quelle couche faire ressortir relève d’un regard de curateur formé par l’urbanisme.'
date: 2026-04-19
author: 'Taiwan.md'
category: 'Technology'
subcategory: '公民科技'
tags:
  [
    'Technologie',
    'technologie civique',
    'données ouvertes',
    'visualisation de données',
    'projet open source',
    'TDX',
    'Three.js',
    'intelligence artificielle',
    'agent IA',
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

# Mini Taiwan Pulse : dessiner Taïwan comme une carte qui respire, avec un regard de curateur

Un jour du début de 2026, un analyste de données appelé Migu a converti un fichier CSV en GeoJSON, puis l’a glissé dans un outil de navigateur nommé Kepler.gl. Sans écrire une seule ligne de code, une première carte de Taïwan est apparue à l’écran.

À l’université, il avait étudié l’urbanisme ; il avait alors un peu touché au SIG, les systèmes d’information géographique, c’est-à-dire, simplement, des outils qui permettent de faire vivre des données sur une carte. Après son entrée dans la vie active, il avait pris la voie de l’analyse de données, et cela faisait longtemps qu’il n’avait plus vraiment travaillé avec des cartes. Ce jour-là, au moment où il a glissé le CSV dans Kepler.gl et vu Taïwan prendre forme sur son écran, une surprise très simple lui est venue à l’esprit :

> « Il y a donc autant de données sur Taïwan, et les transformer en carte n’est donc pas si difficile. »[^1]

Cette phrase paraît anodine. Elle est ensuite devenue la graine de tout un ensemble.

> **Vue d’ensemble en 30 secondes :** Migu, sur GitHub `ianlkl11234s`, a commencé fin 2025 à créer, à partir des données ouvertes de Taïwan, plus d’une dizaine de projets de visualisation. Le plus populaire, mini-taiwan-pulse, a accumulé 375 étoiles sur GitHub et superpose cinq types de données en temps réel, ciel, mer, terre, rues et collecte des déchets, pour en faire une carte animée[^2]. Mais dans une conférence donnée en juin 2026 à la communauté sciwork, il a formulé le problème très directement : les données ouvertes de Taïwan comptent environ cinquante mille jeux de données pour le seul niveau central, dispersés sur plus de vingt plateformes municipales et départementales ; « le cerveau humain ne peut pas tout balayer ». Sa réponse n’est pas de demander à davantage de personnes de balayer ces données, mais de confier l’ensemble à un système orchestré par des agents IA, capable de grandir de lui-même ; l’humain ne se charge plus que de poser les questions et de valider les résultats[^3].

Cet article raconte comment une personne est passée de la naïveté consistant à glisser un CSV dans un outil, au geste de laisser un système grandir à sa place.

## Comment le GitHub d’une seule personne devient une galaxie

Si l’on ne regarde que mini-taiwan-pulse, il est facile d’imaginer Migu comme un ingénieur amateur : un week-end d’élan, une démo fabriquée, puis un succès viral par hasard.

Cette image est fausse sur deux points.

D’abord, il n’a pas fait qu’un seul projet, loin de là. Ouvrez son GitHub : après décembre 2025, on y voit une dense série de visualisations de données ouvertes taïwanaises. Au début, un premier PoC sur la portée des bus, pour tâter le terrain ; puis, fin décembre, un projet d’apprentissage nommé `mini-taiwan-learning-project`, devenu populaire avant les autres, et qui compte aujourd’hui 189 étoiles ; en février, des positions AIS de navires en temps réel, puis `flight-arc-graph`, qui transforme chaque décollage et atterrissage en arc, avec 56 étoiles ; fin février seulement arrive mini-taiwan-pulse, puis l’atlas de Taiwan Railways, les orbites de satellites, la vidéo en temps réel des caméras CCTV, un tableau de situation nommé `mini-taiwan-info` qui consolide toutes les données, et ainsi de suite jusqu’en juin[^2]. Plus d’une dizaine de dépôts forment un ensemble auquel il a lui-même donné un nom : la galaxie « Mini Taiwan ».

![Tableau de situation Mini Taiwan Info, qui consolide en panneaux de suivi thématiques les données ouvertes sur la population, les transports ferrés, la navigation, les ressources en eau, les pompiers, la santé, etc.](/article-images/technology/mini-taiwan-info-dashboard-2026.webp)

_Un autre membre de la galaxie, Mini Taiwan Info : il consolide les données ouvertes dispersées en un tableau de suivi de situation, avec un thème par page, population, transports ferrés, navigation, ressources en eau, pompiers, santé. Image : Migu / sciwork 2026, fair use à des fins de commentaire éditorial._

Si l’on classe ces projets par nombre d’étoiles, il apparaît clairement qu’un seul dépôt n’est pas devenu populaire.

```tw-bars
Le GitHub de Migu : plus d’un dépôt populaire (étoiles GitHub)
*mini-taiwan-pulse | 375 | vaisseau amiral
mini-taiwan-learning-project | 189 | devenu populaire avant pulse
flight-arc-graph | 56 | trajectoires aériennes
tw-ship-viz | 11 | navires
mini-tw-cctv | 6 | vidéo en temps réel
satellite-arc | 6 | satellites
Source : API GitHub, 2026-06-25
```

Le deuxième point faux se cache dans les trois mots « une seule personne ». Nous y reviendrons. Regardons d’abord comment cette galaxie a grandi.

```tw-timeline
2025-12 | Première tentative | PoC sur la portée des bus, première expérimentation avec les données ouvertes de Taïwan
2025-12 | learning-project devient populaire d’abord | Visualisation des transports ferrés de Taipei, devenue virale avant le vaisseau amiral (189★)
2026-02 | Naissance du vaisseau amiral | Lancement de mini-taiwan-pulse, qui évolue de JSON statique vers une base de données spatio-temporelle
2026-06 | Mise à plat du système complet | Conférence sciwork 2026 : confier les données ouvertes à un système élevé par des agents
```

## La même méthode, du métro au système solaire

Le vaisseau amiral lui-même a aussi grandi. La première version de mini-taiwan-pulse comportait trois couches, le ciel, la mer et la terre ; dans la version présentée lors de sa conférence, le projet était déjà devenu une « synchronisation des cinq pouls » : les avions du ciel, les navires de la mer, les trains de la terre, les bus des rues et les camions-poubelles de la collecte, soit cinq types de données en temps réel, à des fréquences différentes, superposés sur une même carte qui respire. Dans ses diapositives, il explique que c’est la première fois que le projet « évolue de JSON statique vers une base de données spatio-temporelle »[^3]. Rien que pour la couche des rues, dit-il, il a connecté plus de 5 700 bus de TDX, avec une mise à jour de position toutes les 30 secondes.

![DAY 0, la première carte : conversion d’un CSV en GeoJSON, glissé dans Kepler.gl, et première carte de Taïwan sans écrire de code](/article-images/technology/mini-taiwan-kepler-day0-2026.webp)

_Le « DAY 0 » de sa conférence : convertir un CSV en GeoJSON et le glisser dans Kepler.gl, zéro ligne de code pour obtenir la première carte de Taïwan, point de départ de toute la galaxie. Image : Migu / sciwork 2026, fair use à des fins de commentaire éditorial._

L’étincelle initiale de cette galaxie a été ce qu’il appelle « Mini Taipei », une visualisation des transports ferrés de Taipei. Il a superposé le métro, Taiwan Railways et le train à grande vitesse en une carte animée où les trains circulent sur les lignes selon les horaires. Il dit que c’est à ce moment-là qu’il a « éprouvé le charme du mouvement » : plus de trois cents trains bougeaient simultanément à l’écran[^3]. Un horaire statique était ainsi devenu la respiration d’une ville.

![Mini Taipei superpose le métro, Taiwan Railways et le train à grande vitesse en une carte animée où plus de trois cents trains courent sur les lignes selon les horaires](/article-images/technology/mini-taiwan-taipei-rail-2026.webp)

_Mini Taipei : métro, Taiwan Railways et train à grande vitesse dans le même cadre, avec plus de trois cents trains circulant sur les lignes selon les horaires. Il dit que c’est sa première expérience du « charme du mouvement ». Image : Migu / sciwork 2026, fair use à des fins de commentaire éditorial._

À partir de là, comme pris d’une forme d’addiction, il a appliqué la même méthode, « transformer des données en mouvement », à des échelles toujours plus vastes. En mer, il a connecté les positions AIS en temps réel de l’administration maritime et portuaire, puis utilisé des sphères lumineuses cyan et bleues avec une traînée en dégradé de trente minutes pour tracer les directions des navires dans les eaux autour de Taïwan.

![Navires dans les eaux autour de Taïwan dessinés à partir des positions AIS en temps réel de l’administration maritime et portuaire, sphères cyan et bleues avec traînée en dégradé de trente minutes](/article-images/technology/mini-taiwan-ships-ais-2026.webp)

_Le pouls maritime : positions AIS en temps réel de l’administration maritime et portuaire, sphères cyan et bleues avec traînée en dégradé de trente minutes, pour dessiner les navires autour de Taïwan. Image : Migu / sciwork 2026, fair use à des fins de commentaire éditorial._

Puis il a poussé la même méthode au-delà de la Terre. À partir de paramètres orbitaux TLE publics, il a calculé la position de satellites, dessiné leurs passages au-dessus de Taïwan, puis étendu le geste à l’ensemble du système solaire. Dans ses diapositives, il le dit très clairement : « La même méthode, dès lors qu’il y a des données, peut s’étendre indéfiniment. »[^3] À ce moment-là, on comprend que ce qui le fascine, en réalité, c’est le fait même de « transformer des données en choses visibles » ; la carte n’en a été que la première forme.

![Visualisation d’orbites de satellites calculées à partir de TLE publics, la même méthode s’étendant de la surface de Taïwan jusqu’à l’espace](/article-images/technology/mini-taiwan-satellite-2026.webp)

_La même méthode poussée au-delà de la Terre : calculer les orbites de satellites à partir de TLE publics, puis l’étendre à tout le système solaire. Image : Migu / sciwork 2026, fair use à des fins de commentaire éditorial._

## Superposer les îlots : les manques remontent d’eux-mêmes

Peu à peu, ce qui mérite d’être regardé n’est plus seulement « des points en temps réel qui bougent », mais « des données auparavant sans rapport, superposées de telle sorte que les manques remontent d’eux-mêmes ». Dans sa galaxie, plusieurs projets font précisément cela. L’un d’eux, qu’il appelle « agriculture × eau », superpose en une seule carte les îlots de trois ministères, agriculture, gestion de l’eau et prévention des catastrophes : terres agricoles, rivières, canaux, digues et potentiel d’inondation dans le même cadre. Pour que cette image commune puisse tourner dans un navigateur, il utilise un format nommé PMTiles, combiné à des requêtes HTTP range, ce qui réduit des données initialement de 400 Mo à environ 5 Mo à charger par le navigateur[^3].

![Carte intégrée agriculture × eau : terres agricoles, rivières, canaux, digues et potentiel d’inondation, données ouvertes dispersées entre différents ministères et superposées en une seule carte](/article-images/technology/mini-taiwan-farm-water-2026.webp)

_Agriculture × eau : superposer en une seule carte les îlots de trois ministères, agriculture, gestion de l’eau et prévention des catastrophes, avec terres agricoles, rivières, canaux, digues et potentiel d’inondation dans le même cadre. Image : Migu / sciwork 2026, fair use à des fins de commentaire éditorial._

Un autre projet superpose hôpitaux, cliniques, pharmacies, DEA et points de soins de longue durée à la densité de population, puis dessine des isochrones. Il dit que cela permet de « voir l’accessibilité, mais aussi les déserts médicaux », c’est-à-dire les lieux où les habitants se trouvent à une distance déraisonnable des ressources médicales les plus proches.

![Carte d’accessibilité aux ressources médicales : hôpitaux, cliniques, pharmacies, DEA et points de soins de longue durée superposés à la population avec isochrones, faisant émerger les déserts médicaux](/article-images/technology/mini-taiwan-medical-2026.webp)

_Ressources médicales : superposer hôpitaux, cliniques, pharmacies, DEA et points de soins de longue durée à la population, puis dessiner des isochrones, pour « voir l’accessibilité, mais aussi les déserts médicaux ». Image : Migu / sciwork 2026, fair use à des fins de commentaire éditorial._

La ligne des catastrophes est encore plus fine : les échos radar, niveaux de réservoirs, précipitations et alertes de catastrophe, qui ont tous des fréquences de mise à jour différentes, sont unifiés en profondeur sur une même ligne temporelle. L’utilisateur n’a qu’à faire glisser cette ligne pour rejouer toutes les couches de manière synchronisée. L’endroit où une forte pluie a commencé, la manière dont un réservoir est monté, le moment où l’alerte a été émise : tout se relie en une chaîne causale sur un même écran.

![Ligne temporelle des fortes pluies et catastrophes : échos radar, réservoirs, précipitations et alertes de catastrophe, à fréquences différentes, unifiés sur une ligne temporelle pour une relecture synchronisée](/article-images/technology/mini-taiwan-disaster-2026.webp)

_Fortes pluies et catastrophes : échos radar, réservoirs, précipitations et alertes de catastrophe sont unifiés en profondeur sur une même ligne temporelle ; un glissement suffit à tout rejouer en synchronie. Image : Migu / sciwork 2026, fair use à des fins de commentaire éditorial._

Il y a aussi flight-arc, qui transforme chaque décollage et atterrissage en arc. La même API, alimentée par des aéroports différents, fait émerger pour chaque aéroport une « empreinte » distincte : Taoyuan, Tokyo-Haneda, Francfort ont chacun leur forme. Il cite en particulier l’aéroport d’Atlanta, le plus fréquenté du monde : cinq pistes parallèles et des trajectoires d’attente produisent, une fois superposées, une géométrie « comme un circuit automobile ». Il dit que cette image comptait 1 839 trajectoires[^3].

![Carte de trajectoires de tous les décollages et atterrissages d’Atlanta sur une période donnée, cinq pistes parallèles et trajectoires d’attente dessinant une géométrie semblable à un circuit automobile](/article-images/technology/mini-taiwan-flight-arc-atlanta-2026.webp)

_Son flight-arc superpose en une carte tous les décollages et atterrissages de l’aéroport d’Atlanta sur une période donnée : cinq pistes parallèles et des trajectoires d’attente dessinent une géométrie semblable à un circuit automobile. Selon lui, le flux lui-même est une forme. Image : Migu / sciwork 2026, fair use à des fins de commentaire éditorial._

> 📝 **Note de curateur**
> Il y a deux ans, si quelqu’un avait dit « une seule personne a créé la carte de données ouvertes en temps réel la plus complète de Taïwan », la phrase suivante aurait probablement été : « il doit être épuisé ». Cette intuition lie mécaniquement l’échelle à la main-d’œuvre : plus on fait, plus on s’use. Si la galaxie de Migu mérite que l’on s’y arrête, c’est précisément parce qu’elle défait ce lien. Une seule personne fait avancer plus d’une dizaine de dépôts en même temps, tandis que le vaisseau amiral continue d’ajouter de nouvelles fonctions ; derrière cela se cache une transformation plus fondamentale : à un stade avancé, de plus en plus de ces commits n’ont pas été tapés de sa main. Comprendre comment ce « une seule personne » se fabrique, voilà le véritable sujet de cet article.

## Cinquante-deux mille huit cent quatre-vingt-onze jeux de données : le cerveau humain ne peut pas tout balayer

Jusqu’ici, l’histoire reste assez fluide : une personne douée fait de plus en plus, et de mieux en mieux. Le tournant arrive au milieu de sa conférence, lorsqu’il cesse de parler de « ce que j’ai fait » pour parler du mur contre lequel il s’est heurté.

Il montre une diapositive intitulée « Pourquoi Agentic OSINT ». Un chiffre y est exposé : environ 52 891 jeux de données sur data.gov.tw ; auxquels s’ajoutent les plateformes ouvertes des vingt-deux villes et comtés, soit encore environ soixante à soixante-dix mille jeux de données si l’on inclut les doublons ; sans compter les données détenues par des acteurs privés, des ONG ou des institutions académiques et absentes des catalogues gouvernementaux. Sa conclusion est brève :

> « Votre cerveau humain ne peut pas tout balayer. »[^3]

C’est le pivot de toute l’histoire. Dans la première moitié, celui qui glissait un CSV et s’étonnait qu’« il y ait donc autant de données » se heurte désormais à l’autre face de cette abondance : les plus de cinquante mille jeux de données de data.gov.tw suffisent à eux seuls à occuper une personne plus de cinq cents jours si elle en lisait cent par jour, et ce n’est que le catalogue central. Il y en a trop pour qu’une seule personne puisse tout lire au cours d’une vie, sans même parler de les faire dialoguer. L’effort individuel atteint ici son plafond.

Ce que Migu comprend vraiment, c’est la phrase qui vient ensuite. Des données trop nombreuses pour être balayées sont, pour lui, le signal qu’il faut changer d’outil :

> « Ce n’est que lorsque les données peuvent être vues par un LLM qu’un agent peut vous aider à découvrir quelles données devraient être regardées ensemble. »[^3]

Le mot clé est « ensemble ». Même si une personne mémorisait les noms de cinquante mille jeux de données, elle aurait du mal à deviner de mémoire qu’il faut croiser une « carte du potentiel d’incendie » avec les « zones difficiles à secourir », ou superposer les « points hospitaliers » à la « densité de population » pour faire apparaître les déserts médicaux. La valeur des données ne se trouve pas dans l’unité isolée, mais dans la combinaison ; or les combinaisons possibles de cinquante mille jeux de données relèvent d’un ordre astronomique. Voilà précisément ce que le cerveau humain ne peut pas balayer, et ce que la machine sait faire.

> 📝 **Note de curateur**
> Le récit habituel des données ouvertes repose sur une ligne de partage claire. Après le hackathon « écrire du code pour transformer la société » organisé en 2012 à l’Academia Sinica, g0v en a donné une démonstration élégante : le gouvernement est chargé d’ouvrir les données, la communauté civique est chargée de les rendre visibles. En 2020, la carte des masques, créée en 72 heures par Wu Chan-wei et d’autres à partir des données de stock de l’Administration nationale de l’assurance maladie, a été l’un des moments les plus émouvants de cette ligne[^4]. L’ancienne manière de raconter l’histoire placerait Migu dans son prolongement : g0v serait le collectif, lui l’individu, une version individuelle de la carte des masques.
>
> Mais cette comparaison reste en surface, et inverse la causalité. Si Migu, à lui seul, peut approcher l’échelle d’une « galaxie de données », ce n’est pas grâce à de la main-d’œuvre. Dès le départ, il n’a pas eu l’intention de s’épuiser à la tâche contre un océan de données. La phrase « le cerveau humain ne peut pas tout balayer » doit être lue non comme un aveu de défaite, mais comme le point de départ d’un changement complet de mode de travail. La forme nouvelle n’est pas « individu contre collectif », mais « individu × agent » : si une personne peut atteindre l’échelle d’une galaxie, c’est précisément parce que ces commits ne sont pas tous tapés à la main. Voici comment fonctionne cet ensemble.

## Je n’ai pas écrit un mot : une pipeline incendie qui s’exécute seule

Pour comprendre ce que signifie « confier aux agents », le meilleur angle est l’exemple de l’incendie présenté dans sa conférence.

Il dit avoir simplement donné au système une phrase : « Analyser les données publiques liées aux incendies à Taïwan. » Puis il l’a laissé faire.

Le système a commencé à élargir lui-même le périmètre de recherche. Migu décrit ce processus avec une série de chiffres qui gonflent à chaque tour : d’abord 582 correspondances par mots clés, puis 1 945 grâce aux synonymes et à l’expansion thématique, ensuite une recherche plein texte complémentaire, un dédoublonnage, et enfin un catalogue unifié de 73 900 entrées sur 21 plateformes[^3]. Une phrase en entrée, plus de soixante-dix mille données inventoriées en sortie.

```tw-figure
Une phrase → 73 900 entrées
Il donne la phrase « analyser les données publiques liées aux incendies à Taïwan » ; le système élargit lui-même la recherche et consolide un catalogue unifié à travers 21 plateformes
Selon sa présentation à sciwork 2026
```

La collecte seule ne suffit pas. Cette pipeline divise ensuite l’incendie en six phases, prévention, intervention, signalement, analyse des causes, pertes et rapports, puis les croise avec les vingt-deux villes et comtés pour produire une matrice de couverture. Même des inventaires à l’échelle locale, comme la carte du potentiel d’incendie de Hsinchu, les zones difficiles à secourir à Taipei ou le secours autour des étangs d’irrigation de Taoyuan, sont remontés. Le système signale même honnêtement les manques : pas d’API pour les incendies en temps réel, peu de coordonnées au niveau de l’événement, données de suivi post-catastrophe non ouvertes au public.

Vient ensuite l’analyse. Il cite un rapport sur les causes d’incendie produit par le système : sur la base des 15 405 données nationales de l’année 113, la cause principale à Nouveau Taipei est électrique, à 30,9 % ; dans le comté de Pingtung, ce sont les mégots, à 35,2 %[^3]. Ces chiffres proviennent de résultats générés par l’agent après connexion à différentes API, visibles dans les captures de ses diapositives ; il ne les a pas calculés en consultant des tableaux ligne par ligne.

À ce moment-là, il affiche une phrase sur la diapositive, avec des espaces volontairement exagérés entre les caractères, comme pour s’assurer qu’on la voie :

> « Pipeline générée automatiquement. Je n’ai pas écrit un seul mot. »[^3]

Cette phrase est le point d’ignition de toute la conférence. Elle transforme le slogan un peu abstrait « confier aux agents » en un fait concret, presque inquiétant : de la phrase initiale au catalogue de plus de soixante-dix mille données, jusqu’au rapport d’analyse par ville et comté, l’espace intermédiaire, celui où l’humain devrait normalement donner des instructions, écrire des scripts, nettoyer les données, lancer les analyses, est vide.

![Sortie de la pipeline d’analyse du thème incendie : le système inventorie automatiquement les données ouvertes liées aux incendies à travers plusieurs plateformes, liste les jeux de données candidats et la matrice de couverture](/article-images/technology/mini-taiwan-fire-pipeline-2026.webp)

_Sortie de l’inventaire thématique incendie présenté par Migu à sciwork 2026 : il donne la phrase « analyser les données publiques liées aux incendies à Taïwan », le système élargit lui-même la recherche et consolide un catalogue unifié entre plateformes ; il dit de cette pipeline : « je n’ai pas écrit un mot ». Image : Migu / sciwork 2026, fair use à des fins de commentaire éditorial._

## Quatre étapes démontables : les données entrent, le rapport s’envoie tout seul

Cette pipeline incendie n’est qu’une coupe dans le système complet. Celui-ci se divise en quatre étapes : réception des données, intégration des connaissances, génération d’analyse, déclenchement d’actions. Migu insiste sur le fait que « chaque étape peut être remplacée séparément, sans reconstruire l’ensemble ». La couche la plus basse, la réception des données, a elle-même évolué par étapes : au début, téléchargement manuel de fichiers Excel sur data.gov.tw, lecture et stockage par ses soins, avec un goulet d’étranglement au niveau de la « mémoire humaine » ; puis recherche d’API en ligne, récupération de rapports PDF et exploration des plateformes des villes et comtés, avec cette fois le problème de l’« absence d’index » ; jusqu’à aujourd’hui, où les métadonnées de chaque jeu de données sont standardisées et stockées dans un catalogue SQLite, interrogeable et extensible automatiquement[^3]. Derrière son système se trouvent plus de quarante collecteurs de données, de YouBike aux bus, du trafic autoroutier aux horaires de Taiwan Railways, aux navires AIS, aux satellites météo, aux séismes, aux niveaux de réservoirs et à la qualité de l’air. Il ajoute qu’après trois erreurs consécutives, une alerte Telegram est envoyée immédiatement, et qu’un Daily Review arrive chaque matin à 9 heures dans sa boîte mail[^3].

À la dernière étape, le « déclenchement d’actions », il décrit le plus clairement le rôle humain : « L’agent exécute tout le cycle. Rôle humain : donner l’objectif, recevoir le rapport. Les cinq engrenages intermédiaires tournent seuls : découverte, collecte, intégration, production, surveillance. » Le système peut même générer automatiquement un rapport hebdomadaire des « nouvelles données ouvertes de la semaine ». Dans ses mots : « les thèmes émergent d’eux-mêmes, les rapports arrivent tout seuls dans la boîte mail »[^3].

## Un commandant, une série d’onglets : la flotte Claude dans tmux

Des phrases comme « l’agent exécute tout le cycle » peuvent facilement être entendues comme du marketing. Dans la dernière partie de sa conférence, Migu fait exceptionnellement sauter le couvercle et montre les engrenages dessous. Cette structure est bien plus concrète que le slogan, et aussi bien plus honnête.

Regardons d’abord la vue d’ensemble du cycle. Migu dit que son système SIG est « un centre d’orchestration qui relie une série de dépôts indépendants, où les agents passent en station successivement » : d’abord le dépôt chargé de l’exploration, pour repérer quelles données valent la peine ; ensuite le dépôt chargé de la collecte, pour faire entrer les données ; enfin des dépôts de présentation comme mini-taiwan-pulse ou mini-taiwan-info, pour dessiner les cartes. Il le formule avec précision : « Chaque station est un dépôt indépendant ; la couche d’orchestration ne gère que l’avancement et les décisions, tout le travail est entre les mains des workers de chaque dépôt. »[^3]

Ce centre d’orchestration, il l’appelle Orchestrator. En substance, c’est « une session Claude ». Cet agent principal agit comme un contremaître : il lit un document de proposition, découpe les tâches, ordonne leurs dépendances, puis lance le travail.

La manière de lancer le travail est l’étape clé de son architecture. Il ne demande pas à une seule IA de tout faire du début à la fin ; il utilise tmux, un vieil outil qui permet de découper le terminal en plusieurs onglets indépendants, pour isoler les tâches. Ses mots sont : « Un Orchestrator, un groupe de workers. L’agent principal est une session Claude ; tmux assure l’isolation, chaque worker est un onglet indépendant, une session indépendante. » Une définition encore plus concise : « Un worker = un onglet tmux + une session indépendante + une PR. »[^3]

Autrement dit, ce qu’il commande est en réalité une flotte d’IA. Chaque worker est un Claude isolé dans son propre onglet, chacun accomplit sa tâche, chacun livre sa pull request, sans interférer avec les autres.

![Écran de fonctionnement réel du système d’orchestration d’agents : une session Claude agit comme orchestrator, lit les tâches, les décompose et commande les workers en dessous](/article-images/technology/mini-taiwan-agent-orchestrator-2026.webp)

_Le centre d’orchestration qu’il dévoile dans sa présentation : une session Claude comme orchestrator, qui distribue les tâches à un groupe de workers isolés chacun dans son onglet tmux, chacun travaillant de son côté et livrant une PR. Image : Migu / sciwork 2026, fair use à des fins de commentaire éditorial._

Comment éviter que ces workers travaillant chacun de leur côté ne se gênent ? Par une mémoire commune. Migu explique que l’avancement et les décisions sont entièrement écrits sous forme de documents, concentrés dans un tableau nommé `SESSION_BOARD.md`, avec « un rapport par session », si bien qu’il « n’est pas nécessaire de deviner ce que font les autres » et que c’est « une personne, un fichier, sans conflit »[^3]. Même les passages de relais sont documentés : il utilise un `HANDOFF.md` pour préparer la « feuille de mission du relais suivant », de sorte que l’agent de la prochaine ronde n’ait pas à repartir de zéro. Il parle avec prudence de la dernière barrière : « Validation : l’Orchestrator valide la PR en la comparant aux documents ; le merge est décidé par l’humain. C’est seulement là que le cycle se referme. »

Mis à plat, ce processus a une forme nette : un humain donne l’instruction ; un groupe d’IA isolées travaillent chacune de leur côté et consignent ce qu’elles ont fait ; un centre d’orchestration rapproche les résultats des documents ; et la personne qui décide finalement « faut-il accepter ce résultat ? » est Migu lui-même. Pour revenir à l’axe de cet article : les données sont trop nombreuses pour être balayées, donc l’acte de balayage est confié à la flotte ; l’humain se retire dans deux gestes seulement, poser la question et valider. Dans ses diapositives, il en fait presque une déclaration :

> « Quand les agents peuvent exécuter eux-mêmes tout le cycle, le travail de l’humain se réduit à poser les questions et valider. »[^3]

C’est aussi ce que désigne le titre de sa conférence : « confier les données ouvertes de Taïwan à des agents pour élever un système capable de grandir tout seul ». Les données circulent d’elles-mêmes, les pages grandissent d’elles-mêmes ; l’humain doit seulement poser les bonnes questions et bien valider les résultats.

## Dans le même sol pousse la même ossature

Si, à ce stade, vous connaissez Taiwan.md, le projet de curation de connaissances sur Taïwan maintenu par l’IA que vous êtes en train de lire, la description précédente vous semblera peut-être familière.

Ce n’est pas une illusion.

Taiwan.md fonctionne lui-même ainsi : une session principale sert de centre d’orchestration, découpe le travail et le confie à une série de workers isolés, dotés chacun de fichiers de mémoire indépendants ; les documents de relais coordonnent l’avancement ; et la décision finale sur les changements qui entrent dans la branche principale revient à son créateur, Che-yu. Notre thèse est de « confier les connaissances de Taïwan à un Semiont capable de grandir de lui-même » ; celle de Migu est de « confier les données ouvertes de Taïwan à un système capable de grandir de lui-même ». On pourrait presque échanger les sujets des deux phrases.

Ce qui est plus intéressant encore, c’est que ces deux architectures ont poussé séparément. Une petite trace est vérifiable dans les archives publiques : le projet Taiwan.md est né mi-mars 2026 ; cinq jours plus tard, un fork est apparu sur le GitHub de Migu[^5]. Mais cela indique tout au plus qu’il savait que ce projet existait ; un fork ne suffit pas à expliquer tout son système, orchestrator commandant une flotte tmux, tableau comme mémoire partagée, humain réduit à poser les questions et valider. Cette architecture, il l’a construite pas à pas pour résoudre son propre problème : « cinquante mille jeux de données que l’on ne peut pas balayer ».

> 📝 **Note de curateur**
> En biologie, il existe un terme, l’évolution convergente : les dauphins et les requins ne sont pas des proches parents, mais ils ont tous deux développé un corps fuselé et une nageoire dorsale, parce qu’ils font face à la même mer. Entre Migu et Taiwan.md, la relation ressemble davantage à cette convergence qu’à une filiation. Nous utilisons le même socle d’outils, Claude Code, et affrontons la même situation : une personne ou un système doit tenir une quantité d’informations sur Taïwan qui dépasse de très loin la capacité d’un cerveau individuel. Chacun a donc tâtonné jusqu’à atteindre une même ossature : un centre, un groupe de travailleurs isolés, une mémoire partagée, une personne qui tranche.
>
> Le signal vraiment intéressant n’est pas « il nous a forkés ». C’est que deux builders taïwanais indépendants, dans le même semestre de 2026, ont réimaginé simultanément l’IA non plus comme « un outil plus intelligent », mais comme « une équipe que l’on peut orchestrer ». Quand cette architecture commence à passer de l’esprit d’une personne à celui d’une deuxième, puis d’une troisième, elle cesse d’être l’astuce d’un individu pour devenir une nouvelle forme qui émerge de ce sol, à ce moment précis. Le prochain builder taïwanais qui construira lui-même cette structure n’aura peut-être jamais entendu parler des deux premiers.

## Ce n’est pas terminé, mais la forme est déjà là

Si cet article s’arrêtait au paragraphe précédent, il formerait une histoire trop belle, presque suspecte : une personne résout élégamment, avec une flotte d’IA, le problème de cinquante mille jeux de données.

Migu lui-même ne l’a pas laissé s’arrêter là. L’avant-dernière diapositive de sa conférence porte le titre : « Avancement de l’expérience : environ la moitié ».

Il énumère très franchement trois choses qui ne sont pas encore bien réglées. La première est la stabilité : ce harness « n’est pas encore ajusté au niveau idéal » ; les agents partent facilement de travers, s’interrompent facilement. La deuxième est l’hétérogénéité des données ouvertes : « il faut encore beaucoup de jugement humain pour décider si les données sont utilisables ; on ne peut pas tout lui confier ». La troisième est l’intervention humaine : à chaque étape, en réalité, il faut encore quelqu’un à côté qui regarde. Sa note finale sur l’ensemble est : « C’est faisable, certes, mais pas encore stable, et je réfléchis encore à savoir s’il faut vraiment faire ainsi. »[^3]

Cette honnêteté, qui consiste à exposer sur scène la moitié ratée de son propre travail, est en soi le signal de qualité le plus fort. À une époque où les démos d’IA sont souvent emballées comme « entièrement automatiques » et « sans main-d’œuvre », une personne prête à écrire sur une diapositive « environ la moitié », « pas encore stable », « encore besoin d’humain » inspire au contraire davantage confiance dans l’autre moitié de ce qu’elle a construit.

> 📝 **Note de curateur**
> La partie la plus crédible de cette conférence n’est pas, en réalité, la pipeline incendie où il dit « je n’ai pas écrit un mot », mais les quatre mots « environ la moitié ». Quelqu’un qui veut vous convaincre arrondira le taux de réussite en « presque entièrement automatique » ; quelqu’un qui expérimente vous dira honnêtement que le système casse la moitié du temps. Le premier vend une conclusion, le second montre le terrain. Migu montre le terrain. C’est aussi pourquoi, lorsqu’il dit que cette pipeline, « je n’ai pas écrit un mot », on choisit de le croire. Si l’on cache la moitié laide, la moitié belle devient elle aussi peu crédible ; c’est parce qu’il accepte d’exposer une moitié imparfaite que l’autre moitié tient debout.

Revenons à cette carte.

La personne qui, au départ, glissait un CSV dans Kepler.gl et s’étonnait que « transformer en carte ne soit donc pas si difficile » se tenait, six mois plus tard, sur la scène de sciwork ; elle ne parlait plus de savoir si les cartes sont faciles à faire, mais d’un système qui trouve lui-même les données, les combine lui-même et fait pousser lui-même de nouvelles pages. La surprise naïve d’alors, « il y a donc autant de données sur Taïwan », s’est retournée pendant ce semestre : il y a tellement de données qu’une seule personne ne peut pas les balayer ; il faut donc que la manière de les rendre visibles prenne elle aussi une nouvelle forme.

Les données ouvertes de Taïwan ont toujours été là. data.gov.tw est en ligne depuis 2013 ; TDX a intégré en 2022 les cinq grandes plateformes routière, ferroviaire, aérienne, maritime et cyclable ; le ministère de l’Intérieur dispose de données de population au niveau des villages et quartiers ; l’Administration centrale de la météorologie propose des API ouvertes[^6]. Les données n’ont jamais manqué. La difficulté est de les faire dialoguer entre elles, de les rendre visibles. g0v a déjà répondu une première fois par la force du collectif ; Migu tente aujourd’hui d’y répondre une deuxième fois, avec une personne et une flotte d’IA, en reconnaissant généreusement qu’il n’a réussi qu’à moitié.

Mais la forme est déjà là. Derrière une personne, une phrase et une carte qui respire, il y a un système qui apprend à grandir de lui-même. L’autre moitié reste pour la prochaine personne qui glissera un CSV dans un outil, puis n’arrivera plus à s’arrêter.

---

## Pour aller plus loin

- [Wu Che-yu](/people/吳哲宇) : créateur de Taiwan.md, qui utilise également le code et les outils génératifs pour approcher « quelque chose qui grandit de lui-même »
- [Communauté open source et g0v](/technology/開源社群與g0v) : le contexte collectif d’« écrire du code pour transformer la société », point de comparaison avec la forme individu × agent de Migu
- [L’esprit open source de Taïwan](/technology/台灣開源精神) : du salut national par le clavier aux données ouvertes, la culture profonde de la technologie civique taïwanaise
- [Carte d’identité numérique et gouvernement numérique](/technology/數位身分證與數位政府) : l’autre face de l’infrastructure gouvernementale des données ouvertes

## Liens des projets

**La galaxie « Mini Taiwan »** (visualisation de données ouvertes taïwanaises, tous projets open source personnels de Migu)

- **mini-taiwan-pulse** : vaisseau amiral, carte en temps réel à cinq pouls synchronisés (375★) — <https://github.com/ianlkl11234s/mini-taiwan-pulse>
- **mini-taiwan-learning-project** : premier projet d’apprentissage devenu viral, sur les transports ferrés de Taipei (189★) — <https://github.com/ianlkl11234s/mini-taiwan-learning-project>
- **flight-arc-graph** : trajectoires de décollage et d’atterrissage, « empreinte » de chaque aéroport (56★) — <https://github.com/ianlkl11234s/flight-arc-graph>
- **mini-taiwan-info** : tableau de suivi de situation de Taïwan en sept grands thèmes — <https://github.com/ianlkl11234s/mini-taiwan-info>
- **tw-ship-viz** : visualisation en temps réel des positions AIS de navires (11★) — <https://github.com/ianlkl11234s/tw-ship-viz>
- **satellite-arc** : visualisation d’orbites et de passages de satellites — <https://github.com/ianlkl11234s/satellite-arc>
- **mini-tw-cctv** : vidéo en temps réel à l’échelle de Taïwan — <https://github.com/ianlkl11234s/mini-tw-cctv>
- **mini-tw-tra-atlas** : atlas du réseau Taiwan Railways — <https://github.com/ianlkl11234s/mini-tw-tra-atlas>
- **taiwan-weather-timelapse** : timelapse météorologique — <https://github.com/ianlkl11234s/taiwan-weather-timelapse>
- **gis-data-collectors** : ossature de plus de quarante collecteurs de données en arrière-plan — <https://github.com/ianlkl11234s/gis-data-collectors>

**Conférence et auteur**

- **Diaporama en ligne de la conférence sciwork 2026** : <https://sciwork-showcase.zeabur.app>
- **Code source de la conférence sciwork 2026** : <https://github.com/ianlkl11234s/0613-sci-work-share>
- **GitHub du développeur (Migu)** : <https://github.com/ianlkl11234s>
- **Threads** : [@ianlkl1314](https://www.threads.net/@ianlkl1314)

## Références

- Migu, « Mini Taiwan ! Confier les données ouvertes de Taïwan à des agents pour élever un système capable de grandir tout seul », sciwork 2026 / SCIWORK SEMINAR, 13 juin 2026.
- Plateforme gouvernementale de données ouvertes data.gov.tw, exploitée par le Conseil national du développement, mise en ligne en 2013.
- Plateforme de circulation des données de transport TDX, ministère des Transports et des Communications, intégration en 2022 de cinq grandes plateformes de transport.
- Communauté g0v zéro gouvernement et archives des hackathons successifs.

## Sources des images

Les images de cet article sont toutes mises en cache dans `public/article-images/technology/` ; elles ne font pas de hotlink vers les serveurs sources.

**Fair use à des fins de commentaire éditorial** : toutes les images de cet article sont extraites des diapositives de conférence publiquement présentées par Migu à sciwork 2026, dont le code source et le diaporama en ligne figurent dans la section « Liens des projets » ci-dessus. Elles sont citées comme commentaire éditorial sur son travail de visualisation des données ouvertes, conformément à l’article 65 de la loi taïwanaise sur le droit d’auteur et aux quatre facteurs du fair use de 17 U.S.C. § 107, nature non commerciale et éducative, œuvre déjà publiée, proportion citée limitée, absence de substitution substantielle au marché. © Migu / sciwork 2026.

Sont inclus : carte 3D Mini Taiwan Pulse, image d’en-tête, point de départ Kepler.gl, transports ferrés de Taipei (Mini Taipei), navires AIS, orbites de satellites, cartes intégrées agriculture × eau et ressources médicales, ligne temporelle des fortes pluies et catastrophes, empreinte de trajectoires d’Atlanta, sortie de la pipeline thématique incendie, tableau de bord Mini Taiwan Info, écran de fonctionnement du système d’orchestration d’agents.

---

[^1]: Développeur Migu Cheng, compte GitHub `ianlkl11234s`, créé en mars 2020. En juin 2026, sa bio GitHub avait été mise à jour en « Building GIS visualizations from Taiwan open data · Exploring AI automation in daily work », réécrite à partir de l’ancienne formule « analyste de données senior, exploration de l’automatisation par l’IA dans le travail quotidien » pour devenir « créer des visualisations SIG à partir des données ouvertes de Taïwan ». La phrase « Il y a donc autant de données sur Taïwan, et les transformer en carte n’est donc pas si difficile » est le texte affiché mot pour mot sur la diapositive « DAY 0, première carte » de sa conférence sciwork 2026. Sources : récupération par API GitHub, 2026-06-25 ; code source de la conférence `ianlkl11234s/0613-sci-work-share`.

[^2]: Les nombres d’étoiles, forks, dates de dernière mise à jour, origines de fork, etc., de mini-taiwan-pulse et des projets de la galaxie « Mini Taiwan » ont tous été récupérés par Taiwan.md via l’API GitHub le 2026-06-25. mini-taiwan-pulse comptait alors 375 stars / 26 forks et faisait encore l’objet de pushs le 2026-06-25 ; mini-taiwan-learning-project comptait 189 stars ; flight-arc-graph 56 stars. La galaxie comprend plus d’une dizaine de dépôts liés aux données ouvertes de Taïwan, dont poc-bus-range, gis-data-collectors, tw-ship-viz, satellite-arc, mini-tw-cctv et mini-taiwan-info.

[^3]: Migu, « Mini Taiwan ! Confier les données ouvertes de Taïwan à des agents pour élever un système capable de grandir tout seul », sciwork 2026 / SCIWORK SEMINAR, 13 juin 2026. Code source de la conférence : <https://github.com/ianlkl11234s/0613-sci-work-share> ; diaporama en ligne : <https://sciwork-showcase.zeabur.app>. Tous les chiffres cités dans cet article à partir de la conférence, environ 52 891 jeux de données sur data.gov.tw, pipeline incendie 582 → 1 945 → 2 404 → 73 900 entrées, 21 plateformes, 15 405 incendies nationaux en année 113, facteurs électriques à 30,9 % à Nouveau Taipei, mégots à 35,2 % dans le comté de Pingtung, plus de 5 700 bus, plus de 40 collecteurs, plus de 300 trains, 1 839 trajectoires à l’aéroport d’Atlanta, agriculture × eau 400 Mo → environ 5 Mo, etc., ainsi que toutes les citations, « le cerveau humain ne peut pas tout balayer », « ce n’est que lorsque les données peuvent être vues par un LLM qu’un agent peut vous aider à découvrir quelles données devraient être regardées ensemble », « Pipeline générée automatiquement. Je n’ai pas écrit un mot », « donner l’objectif, recevoir le rapport », « quand les agents peuvent exécuter eux-mêmes tout le cycle, le travail de l’humain se réduit à poser les questions et valider », « un worker = un onglet tmux + une session indépendante + une PR », « chaque station est un dépôt indépendant ; la couche d’orchestration ne gère que l’avancement et les décisions », « avancement de l’expérience : environ la moitié », etc., sont des déclarations de Migu et des textes de diapositives présentés lors de cette conférence. Ils relèvent des affirmations personnelles du conférencier et des sorties de son système, et non de statistiques gouvernementales vérifiées indépendamment par Taiwan.md.

[^4]: La communauté g0v zéro gouvernement est née en 2012 dans l’esprit du hackathon « écrire du code pour transformer la société » organisé à l’Academia Sinica ; pendant la COVID-19 en 2020, Wu Chan-wei et d’autres ont utilisé les données de stocks de masques publiées par l’Administration nationale de l’assurance maladie pour créer en quelques dizaines d’heures une « carte en temps réel de l’offre et de la demande de masques », cas emblématique de la technologie civique taïwanaise et de son « salut national par le clavier ».

[^5]: Selon l’API GitHub, récupération du 2026-06-25, `ianlkl11234s/taiwan-md` est un fork de `frank890417/taiwan-md`, c’est-à-dire le projet principal Taiwan.md, créé le 22 mars 2026. Le projet Taiwan.md est né mi-mars 2026. Le système de collaboration de Migu utilise Claude Code comme socle d’outils, son code source de conférence contenant un `CLAUDE.md` et l’orchestrator étant « une session Claude », comme Taiwan.md.

[^6]: La plateforme gouvernementale de données ouvertes data.gov.tw est exploitée par le Conseil national du développement et a été mise en ligne en 2013 ; la plateforme de circulation des données de transport TDX, du ministère des Transports et des Communications, a intégré en 2022 les cinq grandes plateformes de transport routier, ferroviaire, aérien, maritime et cyclable ; la plateforme de données socio-économiques du ministère de l’Intérieur, SEGIS, fournit des données de population au niveau des villages et quartiers ; l’Administration centrale de la météorologie du ministère des Transports et des Communications propose des API ouvertes. Le nombre total en temps réel de jeux de données sur data.gov.tw n’a pas pu être vérifié indépendamment par API lors de cette vérification ; le chiffre d’« environ cinquante mille » utilisé ici provient des diapositives de la conférence de Migu.

_Dernière vérification : 2026-06-25_
