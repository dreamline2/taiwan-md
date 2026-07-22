---
title: 'Développement de l’intelligence artificielle à Taïwan et stratégies d’avenir : le ticket matériel est acquis, où se jouera la prochaine bataille ?'
description: 'Le 8 octobre 2024, le prix Nobel de physique est attribué à Hopfield et Hinton ; le lendemain, celui de chimie revient aux trois chercheurs d’AlphaFold. Le 29 mai de la même année, Jensen Huang mange une omelette aux huîtres avec Morris Chang au marché nocturne de Ningxia, à Taipei. Taïwan fabrique 90 % des serveurs d’IA du monde et 72 % des wafers avancés, mais reste absent des solutions apportées à 42 ans d’histoire des réseaux neuronaux et à 50 ans d’énigme du repliement des protéines. De Taiwan AI Labs, fondé par Ethan Tu, créateur de PTT, au modèle LLM en chinois traditionnel TAIDE soutenu par le Conseil national des sciences et de la technologie, cette île peut-elle encore se contenter d’être une usine de sous-traitance ?'
date: 2026-03-19
author: 'Taiwan.md 編輯組'
category: 'Technology'
subcategory: '人工智慧'
tags:
  [
    'intelligence artificielle',
    'IA',
    'semi-conducteurs',
    'politique technologique',
    'transformation numérique',
    'prix Nobel',
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
translatedAt: '2026-06-16T16:54:51Z'
image: '/article-images/technology/alphafold-cbln1-structure-2025.webp'
imageCredit: 'BQUB25-UPoch (own work, AlphaFold + PyMOL)'
imageLicense: 'CC BY 4.0'
imageSource: 'https://commons.wikimedia.org/wiki/File:Estructura_tridimensional_de_la_prote%C3%AFna_CBLN1_per_AlphaFold_amb_codificaci%C3%B3_rainbow.png'
---

# Développement de l’intelligence artificielle à Taïwan et stratégies d’avenir : le ticket matériel est acquis, où se jouera la prochaine bataille ?

> **Aperçu en 30 secondes :** Le 8 octobre 2024, le prix Nobel de physique est attribué au physicien qui a formulé le réseau de Hopfield et au spécialiste des sciences cognitives qui a formalisé la rétropropagation[^N1]. Le lendemain, 9 octobre, le prix Nobel de chimie revient à trois chercheurs qui ont utilisé l’IA pour résoudre l’énigme du repliement des protéines, vieille de cinquante ans[^N2]. Le 29 mai de la même année, le PDG de NVIDIA Jensen Huang apparaît au marché nocturne de Ningxia, à Taipei, pour manger une omelette aux huîtres avec Morris Chang, Barry Lam et Rick Tsai. TSMC capte 72 % des revenus mondiaux de la fonderie de wafers ; Foxconn, Quanta et Wistron produisent ensemble 90 % des serveurs d’IA du monde. Mais dans cette cérémonie scientifique concentrée sur deux jours, qui a donné une légitimité rétrospective à 42 ans d’histoire des réseaux neuronaux, aucun nom ne venait de Taïwan. Du Taiwan AI Labs fondé par Ethan Tu, créateur de PTT, au grand modèle de langue en chinois traditionnel TAIDE soutenu par l’État, un pari est en cours : passer de « fabriquer l’IA » à « devenir l’IA ».

---

## 42 ans de reconnaissance : deux Nobel en deux jours en 2024

Le matin du 8 octobre 2024, à Stockholm, l’Académie royale des sciences de Suède annonce que le prix Nobel de physique de l’année est attribué à deux scientifiques de l’IA : John J. Hopfield, professeur émérite de Princeton âgé de 91 ans, et Geoffrey Hinton, 76 ans, qui venait de quitter Google cinq mois plus tôt. La dotation de 11 millions de couronnes suédoises est partagée entre les deux lauréats[^N1].

Le comité justifie le prix par leurs « découvertes et inventions fondamentales qui permettent l’apprentissage automatique avec des réseaux neuronaux artificiels »[^N1]. C’est la première fois dans l’histoire du Nobel de physique que le prix est attribué directement au champ des réseaux neuronaux.

Le lendemain, 9 octobre, c’est le prix de chimie. Trois lauréats : David Baker, de l’Université de Washington, ainsi que deux chercheurs de DeepMind, Demis Hassabis et John Jumper. Baker reçoit la moitié de la dotation ; Hassabis et Jumper se partagent l’autre moitié[^N2]. La motivation du prix est divisée en deux parties : la « conception computationnelle de protéines » pour Baker, et la « prédiction de la structure des protéines » pour Hassabis et Jumper.

Deux jours, deux prix Nobel, tous deux liés à l’IA. Il n’existe pas de précédent dans l’histoire du prix Nobel.

Un rappel chronologique permet de mesurer l’écart : lorsque Hopfield publie en 1982, dans les _Proceedings of the National Academy of Sciences_ (PNAS), son article intitulé « Neural networks and physical systems with emergent collective computational abilities », il vient tout juste de passer de la physique de la matière condensée aux neurosciences[^N3]. De 1982 à 2024 : exactement 42 ans. L’article de 1986 dans lequel Hinton et Rumelhart transforment l’algorithme de rétropropagation en outil utilisable[^N4] attendra lui aussi 38 ans avant d’être récompensé. AlphaFold, en revanche, n’aura eu besoin que de six ans entre sa première apparition à CASP13 en 2018 et le Nobel de 2024.

Au fond, ces deux Nobel ne récompensent pas ChatGPT, mais quelques articles d’il y a trente ou quarante ans que presque personne ne comprenait alors. Le décalage temporel entre recherche fondamentale et application industrielle a toujours fonctionné ainsi.

![Portrait officiel de Geoffrey E. Hinton interviewé le 8 décembre 2024 à Stockholm pendant la semaine Nobel, costume sombre, cheveux blancs, expression calme face à l’objectif](/article-images/technology/hinton-nobel-2024.webp)
_Geoffrey Hinton, lauréat du prix Nobel de physique 2024, pendant la semaine Nobel à Stockholm. Photo : Arthur Petron, 2024-12-08. [CC BY-SA 4.0 via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Geoffrey_E._Hinton,_2024_Nobel_Prize_Laureate_in_Physics_(3x4*cropped).jpg).*

---

## Le dîner à plusieurs milliers de milliards au marché nocturne de Ningxia

Le soir du 29 mai 2024, à la veille de l’ouverture du Computex, un groupe de convives inhabituel apparaît au marché nocturne de Ningxia, un night market de Taipei. Le PDG de NVIDIA Jensen Huang, accompagné du fondateur de TSMC Morris Chang, du président de Quanta Barry Lam et du PDG de MediaTek Rick Tsai, se presse devant un stand pour manger une omelette aux huîtres[^1]. Des passants reconnaissent Jensen Huang ; en quelques instants, il est entouré de fans et de journalistes, dans une scène digne d’une célébrité.

La capitalisation boursière réunie autour de cette table dépasse plusieurs milliers de milliards de dollars. Mais la véritable histoire n’est pas sur la table : elle se trouve dans la chaîne industrielle qui la soutient. Les entreprises représentées par ces hommes constituent la base matérielle du calcul IA mondial. Lors de ce séjour à Taïwan, Jensen Huang déclare publiquement : « Taïwan est l’un des pays les plus importants du monde »[^2]. Ce n’est pas une formule de courtoisie. Sans Taïwan, les fondations matérielles de la révolution de l’IA n’existeraient pas.

Jensen Huang est né à Taipei en 1963, a passé son enfance à Tainan, puis a immigré aux États-Unis à l’âge de neuf ans[^3]. NVIDIA, qu’il cofonde en 1993, est aujourd’hui synonyme de puces d’IA. Chaque GPU avancé conçu par NVIDIA, des A100 et H100 utilisés pour entraîner ChatGPT jusqu’à la dernière série Blackwell, est fabriqué par TSMC[^4].

Quatre mois plus tard, les deux listes de prix Nobel annoncées à Stockholm ne comportent aucun nom lié à ce dîner. Cet écart n’est pas un hasard : c’est un fait structurel.

---

## Le matériel : une île qui porte toute la révolution de l’IA

Qualifier la place de Taïwan dans la chaîne d’approvisionnement matérielle de l’IA de « cruciale » est presque trop faible.

Dans la fabrication de puces, TSMC capte en 2025 72 % des revenus du marché mondial de la fonderie de wafers[^5]. Dans les procédés les plus avancés, inférieurs à 7 nanomètres, sa part de marché dépasse 90 %. NVIDIA détient environ 86 % du marché des GPU d’IA, et ces GPU sont presque tous produits par TSMC[^6]. L’immense majorité de la puissance de calcul utilisée dans le monde pour entraîner et faire tourner les modèles d’IA naît dans les salles blanches de Taïwan.

Une fois les puces produites, elles doivent encore être assemblées en serveurs pour rejoindre les centres de données. Là encore, Taïwan domine. Les trois grands fabricants ODM Foxconn, Quanta et Wistron produisent ensemble environ 90 % des serveurs d’IA du monde[^7]. En 2025, le chiffre d’affaires annuel de chacune de ces trois entreprises dépasse 1 000 milliards de nouveaux dollars taïwanais, soit environ 32 milliards de dollars américains ; au deuxième trimestre, les revenus des serveurs d’IA dépassent pour la première fois ceux de l’électronique grand public[^8].

La performance d’une puce d’IA ne dépend pas seulement de la miniaturisation des procédés, mais aussi des technologies de packaging. Le CoWoS (Chip on Wafer on Substrate) de TSMC, une technologie de packaging avancé, est essentiel pour permettre aux GPU haut de gamme de NVIDIA d’atteindre leurs objectifs de performance. En 2026, la seule demande de NVIDIA en wafers CoWoS devrait atteindre 595 000 unités, soit 60 % de la demande mondiale totale[^9].

Foxconn coopère en outre avec NVIDIA et le gouvernement taïwanais pour construire à Kaohsiung un supercalculateur d’usine IA de classe 100 MW, fondé sur la dernière architecture NVIDIA Blackwell[^10]. Taïwan passe ainsi du statut de « lieu où l’on fabrique les puces d’IA » à celui de « lieu où l’on fait fonctionner l’IA ».

![Extérieur de l’usine Fab 5 de TSMC dans le parc scientifique de Hsinchu, scène des années 2010, site physique de la fonderie de wafers semi-conducteurs](/article-images/technology/tsmc-fab5-hsinchu-2010.webp)
_Usine Fab 5 de TSMC à Hsinchu, site physique de la fonderie des puces d’IA. Photo : Wikimedia Commons via [TSMC Fab 5 file](https://commons.wikimedia.org/wiki/File:TSMC_Fab_5.jpg)._

La question est donc la suivante : une fois le ticket matériel obtenu, où se jouera la prochaine bataille ?

> 📝 **Note curatoriale**
>
> La formule courante affirme que la « montagne sacrée qui protège le pays » soutient la révolution de l’IA. Elle fonctionne bien narrativement, mais inverse à moitié la causalité. C’est parce que la révolution de l’IA avait besoin de GPU qu’elle a choisi TSMC ; ce n’est pas TSMC qui est né de la révolution de l’IA. La véritable tension est ailleurs : lorsque le GPU devient une marchandise, vers où glisse la prochaine couche de valeur ? Les deux Nobel de 2024 apportent une réponse : vers le modèle lui-même. Les douze pages écrites par Hopfield, la nuit de 2012 où Hinton et son étudiant Krizhevsky font passer AlexNet de 26,2 % à 15,3 % de taux d’erreur en reconnaissance d’images sur ImageNet[^N5], et l’après-midi où l’équipe de Hassabis permet à AlphaFold d’atteindre une médiane GDT de 92,4 à CASP14.

---

## Hopfield 1982 : le modèle de mémoire écrit par un physicien

En 1982, John Hopfield, physicien de la matière condensée à Princeton, écrit un article de seulement douze pages au titre très long : « Neural networks and physical systems with emergent collective computational abilities », publié dans les _Proceedings of the National Academy of Sciences_[^N3].

Ce qu’il fait, au fond, consiste à traduire la « mémoire » en physique.

En physique, il existe un objet appelé spin glass, ou verre de spin : un ensemble d’atomes magnétiques possèdent chacun une orientation de spin, interagissent les uns avec les autres, et l’ensemble du système trouve spontanément un point d’énergie minimale. Hopfield transpose ce concept aux neurones : il imagine les neurones comme des spins, les forces de connexion comme des interactions, et le réseau entier converge spontanément vers un état stable correspondant à un « minimum d’énergie »[^N3]. Chaque minimum d’énergie est une mémoire stockée.

L’élégance du modèle tient à ce qu’il rend la mémoire descriptible dans le langage de la physique. À partir d’un indice incomplet, le réseau retrouve de lui-même le point d’énergie minimale le plus proche et complète le souvenir. C’est l’ancêtre mathématique de ce que fait aujourd’hui l’IA générative.

En 1982, à Taïwan, l’industrie électronique en est à ses débuts et TSMC n’existe pas encore. Morris Chang ne fondera qu’en 1987 l’entreprise qui, 42 ans plus tard, deviendra la « montagne sacrée qui protège le pays ». En 2026, l’article de Hopfield a déjà accumulé plus de 27 000 citations sur Google Scholar[^N6].

Plus intéressant encore : une phrase que Hopfield prononce plus tard. Il a passé sa vie à Princeton en physique de la matière condensée ; son entrée dans les neurosciences était vue par ses pairs de l’époque comme une forme de dilettantisme. Lorsqu’en 2024, à 91 ans, son nom est annoncé pour le Nobel, l’Académie royale de Suède lui demande au téléphone sa réaction. Il dit être inquiet devant le fait que « personne ne comprend ni ne contrôle la direction de l’IA »[^N7].

L’homme qui a formulé une partie des bases mathématiques de l’IA moderne rappelle, le jour même où il reçoit le prix, qu’il faut faire preuve de prudence.

![Portrait de John J. Hopfield interviewé le 8 décembre 2024 à Stockholm pendant la semaine Nobel, costume sombre, cheveux blancs, expression posée](/article-images/technology/hopfield-nobel-2024.webp)
_John J. Hopfield, lauréat du prix Nobel de physique 2024, pendant la semaine Nobel à Stockholm. Photo : Arthur Petron, 2024-12-08. [CC BY-SA 4.0 via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:John_J._Hopfield,_2024_Nobel_Prize_Laureate_in_Physics_1_(cropped).jpg).\_

---

## Hinton : l’article de 1986 et l’avertissement après son départ de Google en 2023

Né en 1947 à Wimbledon, Londres, Geoffrey Hinton est un autre chercheur que l’histoire n’a accepté de reconnaître qu’avec 38 ans de retard[^N8].

En 1986, Hinton publie avec David Rumelhart et Ronald Williams un article dans _Nature_ sur la rétropropagation[^N4]. Le principe de cet algorithme est le suivant : lorsqu’un réseau neuronal commet une erreur, le signal d’erreur peut être renvoyé en sens inverse dans chaque couche, afin d’ajuster couche par couche les poids des connexions. C’est la méthode par laquelle tous les modèles d’apprentissage profond s’entraînent aujourd’hui.

L’algorithme est formulé en 1986, mais il lui faut trois conditions pour exploser : une puissance de calcul suffisamment bon marché, une masse de données suffisamment grande et des personnes prêtes à croire dans cette voie. Les deux premières conditions sont réunies au début des années 2010. La troisième est incarnée par Hinton et ses deux étudiants, Alex Krizhevsky et Ilya Sutskever. En 2012, ils entraînent avec des GPU le réseau neuronal convolutionnel AlexNet et obtiennent, au concours de reconnaissance d’images ImageNet, un taux d’erreur top-5 de 15,3 %, très loin devant les 26,2 % du deuxième[^N5]. C’est à ce moment que l’industrie entière se convainc que la rétropropagation fonctionne réellement.

En mars 2013, Google rachète pour 44 millions de dollars la petite société de Hinton, DNNresearch, et intègre le chercheur alors âgé de 65 ans[^N8]. Pendant les dix années suivantes, il devient l’un des universitaires de l’IA les plus respectés de la Silicon Valley.

Puis, le 1er mai 2023, le _New York Times_ publie un entretien : Hinton a quitté Google.

La raison de son départ n’est pas la retraite. Il explique vouloir « pouvoir parler librement des risques de l’IA sans devoir tenir compte de l’impact sur Google »[^N9]. Ses avertissements portent notamment sur la possibilité que les systèmes d’IA deviennent rapidement plus intelligents que les humains, qu’ils soient utilisés à mauvais escient par des acteurs malveillants, et sur le fait qu’il est « difficile de voir » comment empêcher cela[^N9]. Il va jusqu’à dire qu’une partie de lui regrette le travail de toute sa vie[^N9].

Lorsque le Nobel de physique lui est attribué en 2024, il répète au téléphone le même avertissement : il faut prendre au sérieux la possibilité d’une perte de contrôle de l’IA[^N10].

Celui qui a formulé l’algorithme d’entraînement de l’apprentissage profond et celui qui a écrit le modèle de mémoire se retrouvent en octobre 2024 sur la scène de l’Académie royale des sciences de Suède pour rappeler, au même moment, que cette chose pourrait être plus dangereuse qu’on ne l’imagine. L’image résonne en contrepoint avec celle d’Oppenheimer regardant le nuage en champignon se lever dans le désert du Nouveau-Mexique en 1945.

Deux mois plus tard, le 8 décembre 2024, Hinton prononce sa conférence Nobel à l’Aula Magna de l’Université de Stockholm. Le titre : « Boltzmann Machines » — ce travail sur les machines de Boltzmann qu’il a mené avec Sejnowski dans les années 1980, qui inscrit les distributions de probabilité thermodynamiques dans les réseaux de neurones. En l’écoutant jusqu’au bout, on comprend que l’article de 1986 sur la rétropropagation n’était pas une intuition isolée, mais une pensée complète née au carrefour de la physique et des sciences cognitives des années 1980 :

<div class="video-embed" style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;margin:1.5rem 0;border-radius:8px;">
  <iframe src="https://www.youtube.com/embed/iCS1ds0UDP8" title="Boltzmann Machines — Nobel Prize lecture by Geoffrey Hinton, Nobel Prize in Physics 2024" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

_Chaîne officielle de l’Académie royale des sciences de Suède : conférence Nobel de physique 2024 de Geoffrey Hinton, le 8 décembre 2024, « Boltzmann Machines ». Des machines de Boltzmann qu’il écrit avec Sejnowski dans les années 1980, à la rétropropagation, jusqu’aux LLM d’aujourd’hui — quarante ans en entier. Dans les cinq dernières minutes, depuis le podium Nobel, il réexprime ses inquiétudes sur les risques de l’IA._

---

## De PTT au laboratoire d’IA : les deux créations d’Ethan Tu

Revenons à Taïwan. Au moment où Hopfield formule son modèle de mémoire, l’île commence à peine à ouvrir des départements d’informatique.

En 1995, Ethan Tu, alors étudiant en deuxième année au département d’informatique de l’Université nationale de Taïwan, utilise un ordinateur 486 et des logiciels open source pour mettre en place dans son dortoir [PTT](/fr/Technology/ptt-bulletin-board-system/), qui deviendra plus tard le plus grand système de bulletin board de Taïwan. Trente ans plus tard, PTT compte toujours plusieurs centaines de milliers de connexions quotidiennes et demeure un fossile vivant de la culture Internet taïwanaise.

Ethan Tu part ensuite chez Microsoft, où il participe au développement de l’assistant vocal Cortana. En avril 2017, il renonce à un salaire élevé dans la Silicon Valley pour rentrer à Taïwan et fonde Taiwan AI Labs, le premier organisme de recherche en IA à but non lucratif et ouvert d’Asie[^11].

Sa motivation est directe : Taïwan possède des talents logiciels de niveau mondial, mais ceux-ci partent dans la Silicon Valley. Il veut créer une plateforme où les personnes qui souhaitent revenir ou rester puissent faire de la recherche en IA.

Le produit le plus connu de Taiwan AI Labs est « 雅婷逐字稿 », un système de reconnaissance vocale optimisé pour le chinois traditionnel et les accents taïwanais. Pendant la pandémie de COVID-19, le laboratoire développe également des outils de détection de désinformation et des IA médicales fondées sur l’apprentissage fédéré[^12]. Ces projets ont un point commun : ils résolvent des problèmes locaux taïwanais, avec des données locales taïwanaises, au lieu de simplement traduire et réutiliser des modèles américains.

L’histoire d’Ethan Tu, de PTT à AI Labs, résume dans une certaine mesure le développement logiciel de Taïwan : les capacités techniques ne manquent pas ; ce qui manque, c’est l’écosystème capable de retenir les talents.

> 💡 **Le saviez-vous ?**
>
> En 1986, l’année où Hinton publie la rétropropagation, le PIB de Taïwan est d’environ 77,9 milliards de dollars américains, son PIB par habitant d’environ 4 007 dollars, et le parc scientifique de Hsinchu n’a que six ans d’existence[^N11]. Ces trois événements se produisent simultanément sur la même planète, mais il faudra attendre 26 ans et le jeu de données ImageNet pour que ces lignes historiques se croisent. L’échelle temporelle de la recherche fondamentale est toujours plus longue que celle ressentie par les récits industriels.

---

## AlphaFold : l’autre moitié du Nobel pour l’énigme du repliement des protéines

L’histoire du Nobel de chimie 2024 commence par une question posée en 1972.

Cette année-là, dans son discours de réception du prix Nobel de chimie, le biochimiste américain Christian Anfinsen propose une hypothèse : la structure tridimensionnelle repliée d’une protéine est entièrement déterminée par sa séquence d’acides aminés[^N12]. Si cette hypothèse est correcte, alors, en théorie, il devrait suffire de voir une séquence d’acides aminés pour calculer la structure 3D correspondante. Mais ce « devrait » reste hors d’atteinte pendant un demi-siècle. Le repliement des protéines devient un grand défi scientifique. Tous les deux ans, la communauté organise le concours CASP : les participants soumettent leurs prédictions, comparées ensuite aux structures expérimentales. De 1994 à la treizième édition, personne ne parvient à franchir le seuil décisif[^N13].

Jusqu’à CASP13, en 2018, où DeepMind engage la première génération d’AlphaFold et remporte la compétition, sans toutefois atteindre une précision pleinement utilisable. Le vrai tournant a lieu le 30 novembre 2020, à CASP14 : AlphaFold 2 obtient une médiane GDT de 92,4[^N13]. Un GDT de 92,4 signifie que, pour plus de la moitié des prédictions, l’écart entre les positions atomiques prédites et les valeurs expérimentales est inférieur à un angström, c’est-à-dire au niveau de la résolution expérimentale. John Moult, organisateur de CASP, déclare ce jour-là que, « dans une large mesure, ce problème est résolu »[^N13].

Un problème resté sans solution pendant 50 ans est résolu en six ans par une équipe de recherche londonienne.

La suite est encore plus rapide. En juillet 2021, le code source d’AlphaFold 2 est publié en open source ; la même année, DeepMind s’associe au Laboratoire européen de biologie moléculaire (EMBL-EBI) pour constituer une base de données publique des structures protéiques prédites par AlphaFold. En juillet 2022, cette base couvre un million d’espèces et environ 200 millions de structures protéiques, ce qui revient à publier gratuitement des modèles 3D de presque toutes les protéines connues sur Terre[^N14].

Le 8 mai 2024, DeepMind publie AlphaFold 3 dans _Nature_, étendant la prédiction d’une protéine isolée aux interactions entre protéines et ADN, ARN, ligands et ions[^N15]. Du développement de nouveaux médicaments à la conception de vaccins et à l’ingénierie enzymatique, tous les domaines qui ont besoin de savoir comment les molécules s’emboîtent voient leurs fondations réécrites par cet outil.

Demis Hassabis, qui a créé AlphaFold, n’est pas un biochimiste traditionnel. Il commence les échecs à quatre ans et obtient le titre de maître à 13 ans ; à 17 ans, il codéveloppe avec Peter Molyneux le jeu de simulation _Theme Park_, vendu à plusieurs millions d’exemplaires[^N16]. En 2010, il fonde DeepMind à Londres avec Shane Legg et Mustafa Suleyman ; en 2014, Google rachète l’entreprise pour 400 millions de livres sterling[^N16]. En 2016, AlphaGo bat Lee Sedol ; en 2020 arrive AlphaFold 2 ; en 2024, le Nobel. Moins de dix ans séparent ces trois événements.

La ligne qui les relie repose sur le même pari : utiliser les réseaux neuronaux pour résoudre des problèmes que le cerveau humain ne parvenait pas à résoudre. Le go est un domaine à règles fermées ; le repliement des protéines est un domaine à règles ouvertes mais fortement contraint par la physique. Dans les deux cas, Hassabis a choisi le bon champ de bataille.

À Taïwan, la recherche sur les glycomolécules et les protéines construite sous la présidence de Chi-Huey Wong à l’Academia Sinica (2006-2016) est l’investissement académique local le plus proche de cette frontière[^N17]. Des équipes de l’Institut des sciences biomédicales et de l’Institut de chimie biologique de l’Academia Sinica utilisent aussi les poids open source d’AlphaFold pour des recherches en aval. Mais Taïwan ne dispose pas aujourd’hui d’une structure équivalente pour développer un modèle de cœur de niveau AlphaFold.

> ⚠️ **Point de vue controversé**
>
> L’attribution du Nobel de chimie à AlphaFold a suscité un débat académique : certains biologistes structuraux estiment que le prix aurait dû revenir aux chercheurs ayant réalisé les premières expériences clés en cristallographie aux rayons X ou en résonance magnétique nucléaire, plutôt qu’à l’élévation d’un outil de calcul au rang de chimie nobélisée[^N18]. D’autres considèrent que ce débat est déjà dépassé : lorsqu’un algorithme peut, en cinq ans, aider l’humanité à compléter presque toutes les structures 3D des protéines de la Terre, c’est bien de la chimie. Après octobre 2024, le débat a progressivement penché vers la seconde position, mais la tension qu’il révèle n’a pas disparu : lorsque ce que l’IA sait faire s’étend, faut-il redessiner les frontières des disciplines traditionnelles ?

---

## TAIDE : pourquoi Taïwan a besoin de son propre modèle de langue

En avril 2023, six mois après que ChatGPT a conquis le monde, le Conseil national des sciences et de la technologie de Taïwan lance le projet « TAIDE », pour Trustworthy AI Dialogue Engine, un moteur de dialogue génératif fiable[^13].

Pourquoi un État insulaire de 23 millions d’habitants devrait-il développer lui-même un grand modèle de langue ?

La raison n’est pas seulement l’autonomie technologique. Le chinois traditionnel est très peu représenté dans les données mondiales d’entraînement de l’IA, et la plupart des données chinoises proviennent de sites en chinois simplifié. Lorsque les Taïwanais utilisent ChatGPT ou d’autres modèles, les réponses incorporent souvent les usages lexicaux et les présupposés de la Chine continentale. Employer « 視頻 » au lieu de « 影片 », « 質量 » au lieu de « 品質 » : ces différences apparemment mineures renvoient à une question de subjectivité culturelle. Le magazine _CommonWealth_ titre directement son reportage sur TAIDE : « empêcher l’invasion culturelle de l’IA chinoise »[^14].

En avril 2024, l’équipe TAIDE publie le modèle commercial TAIDE-LX-7B et le modèle académique TAIDE-LX-13B, qui obtiennent de bons résultats dans des tâches d’écriture, de traduction et de résumé[^15]. En 2026, TAIDE 2.0 est publié ; avec le modèle Breeze-8B soutenu par MediaTek, l’écosystème taïwanais des LLM passe de la phase de « rattrapage » à celle de « l’utilisabilité »[^16].

Le plus intéressant est l’éclosion des applications. L’Université nationale Chung Hsing utilise TAIDE pour créer un système de recherche de connaissances agricoles, « 神農 TAIDE » ; l’Université nationale de Tainan développe un agent conversationnel taïwanais-anglais pour l’enseignement du taïwanais ; l’Université nationale Yang Ming Chiao Tung entraîne des versions taïwanaise et hakka de TAIDE[^17]. Ces applications confirment une chose : un modèle de langue est à la fois un produit technique et un support culturel. Une IA qui ne comprend ni le « Jour où le ciel se perce » ni les processions de Mazu ne peut pas vraiment servir les Taïwanais.

La taille de TAIDE reste toutefois modeste : 8B paramètres pour la version commerciale et 13B pour la version académique, soit plus de deux ordres de grandeur de moins que le niveau supposé de GPT-4 d’OpenAI, estimé à plus d’un billion de paramètres. Derrière cet écart se trouve un problème de budget GPU, plus qu’un problème de compétence. Entraîner un LLM de frontière exige une puissance de calcul qui se chiffre en centaines de millions de dollars, du même ordre que le budget annuel d’un organisme national de recherche.

---

## Une cybersécurité IA forgée par les attaques

Taïwan est l’un des pays les plus fréquemment ciblés par les cyberattaques au monde. Cette réalité malheureuse a, de manière inattendue, donné naissance à une industrie de cybersécurité IA particulièrement robuste.

Fondée fin 2017, CyCraft est la première entreprise taïwanaise à combiner IA et surveillance des terminaux. Sa technologie a été mentionnée sept fois dans des rapports du cabinet mondial Gartner, et elle est la seule entreprise taïwanaise à avoir passé trois fois l’évaluation de référence américaine MITRE ATT&CK[^18]. En février 2026, CyCraft est cotée sur le Taiwan Innovation Board de la Bourse de Taïwan, devenant le premier éditeur logiciel taïwanais de cybersécurité IA doté de capacités internationales de R&D autonome à entrer sur le marché des capitaux taïwanais[^19].

Ses clients couvrent les administrations taïwanaises, les unités de défense, les banques et les entreprises de semi-conducteurs : précisément les cibles les plus souvent visées par des pirates soutenus par des États. L’entreprise possède des filiales au Japon et à Singapour et exporte dans toute la région Asie-Pacifique cette « expérience de terrain née des attaques subies ».

Ce cas montre que l’avantage taïwanais en IA ne vient pas seulement des semi-conducteurs, mais aussi des capacités opérationnelles forgées par une situation géopolitique particulière.

---

## Politique publique : de « l’an un de l’IA » au ministère des Affaires numériques

Le développement de la politique taïwanaise en matière d’IA peut se comprendre à travers trois moments.

2017-2018 correspond à la phase de lancement. Le Yuan exécutif désigne 2017 comme « l’an un de l’IA » et propose l’idée d’une « grande stratégie de petit pays pour l’IA », reconnaissant la petite taille du marché taïwanais, mais mettant l’accent sur trois cartes : la fabrication de semi-conducteurs, la chaîne d’approvisionnement ICT et les talents scientifiques et techniques. En 2018, la première phase du « Plan d’action IA de Taïwan » est lancée, avec plus de 40 milliards de nouveaux dollars taïwanais investis sur quatre ans, notamment dans l’infrastructure de calcul IA « Taiwan AI Cloud » (TWCC)[^20].

En 2022, la politique s’institutionnalise. Le ministère des Affaires numériques (moda) est créé, intégrant des fonctions numériques jusque-là dispersées entre le ministère des Sciences et de la Technologie, le ministère de l’Économie et le ministère des Transports. La portée de cette étape est claire : la politique IA cesse d’être un « projet du ministère des Sciences » pour devenir une « stratégie nationale interministérielle ». La même année, le gouvernement publie des « Lignes directrices pour le développement de la recherche scientifique en intelligence artificielle », insistant sur des principes tels que l’humain au centre, la transparence, l’explicabilité, l’équité et la non-discrimination.

Depuis 2023, le tournant est celui de l’IA générative. Le choc ChatGPT provoque un changement rapide de cap. Le projet TAIDE est lancé, un projet de loi fondamentale sur l’IA est promu, et l’adoption de l’IA dans le secteur public s’accélère. La stratégie taïwanaise est très pragmatique : ne pas rivaliser avec les États-Unis et la Chine sur le nombre d’articles de recherche fondamentale, mais greffer l’IA sur les avantages manufacturiers existants. Fabrication intelligente, imagerie médicale, prédiction du rendement dans les semi-conducteurs : autant de domaines où Taïwan possède des données, des terrains d’application et de la compétitivité.

Le problème est que, dans les listes de lauréats des deux Nobel annoncées en octobre 2024, aucun nom ne provenait de cette trajectoire de « fabrication intelligente ».

---

## L’inquiétude : l’écart logiciel d’un empire matériel

Derrière les chiffres brillants, le développement de l’IA à Taïwan souffre d’un problème structurel : un déséquilibre profond entre matériel et logiciel.

Taïwan produit 90 % des serveurs d’IA du monde et la majorité des puces d’IA, mais reste peu visible dans les segments « souples » : développement de modèles, écosystèmes de données, logiciels de plateforme. Aucun des vingt premiers modèles d’IA mondiaux, qu’il s’agisse de GPT, Claude, Gemini ou LLaMA, ne vient de Taïwan. Si l’on compare les travaux récompensés par les deux Nobel de 2024, du réseau de Hopfield à la rétropropagation et à AlphaFold, ces trois lignes restent très éloignées de l’industrie taïwanaise.

La cause est une nouvelle version d’un vieux problème. Lorsque le salaire annuel d’un ingénieur de TSMC peut dépasser deux millions de dollars taïwanais, les jeunes pousses logicielles peinent à attirer les meilleurs talents. Google, Microsoft et NVIDIA disposent de centres de R&D à Taïwan ; leurs salaires et avantages créent un puissant effet d’aspiration. Pour un diplômé du département d’informatique de l’Université nationale de Taïwan, le premier choix est souvent une multinationale ou le département IT de TSMC, plutôt qu’une start-up IA locale.

Le défi plus fondamental est celui des données. La valeur d’un modèle d’IA vient de ses données d’entraînement, et le volume de données de haute qualité en chinois traditionnel est infime par rapport à l’anglais ou au chinois simplifié. Les textes produits par 23 millions de Taïwanais ne peuvent naturellement pas rivaliser avec ceux du monde anglophone ou de la Chine continentale. Le projet TAIDE tente de résoudre ce problème, mais le désavantage d’échelle des données est structurel.

Le véritable pari de l’IA taïwanaise se situe donc dans les applications verticales plutôt que dans les modèles de base : au lieu d’affronter frontalement OpenAI ou Google sur les modèles généralistes, Taïwan choisit de trouver une position irremplaçable dans l’IA appliquée aux procédés de semi-conducteurs, l’imagerie médicale, la cybersécurité IA et le NLP en chinois traditionnel. Dans ces domaines, Taïwan possède des données et des contextes d’usage uniques, difficiles à reproduire ailleurs.

---

## Le choix IA d’une île

En 2026, Taïwan se trouve dans une position singulière : l’île n’a jamais été aussi indispensable dans la chaîne d’approvisionnement matérielle de l’IA, mais elle reste périphérique dans l’écosystème logiciel de l’IA.

Ce n’est pas entièrement négatif. Historiquement, le modèle de réussite de Taïwan a toujours consisté à « ne pas être la marque, mais la marque derrière la marque ». Le modèle de fonderie pure inventé par Morris Chang en 1987 a fait de TSMC l’une des dix premières entreprises mondiales par capitalisation. Aujourd’hui, la même logique se répète dans l’industrie des serveurs d’IA : Foxconn ne développe pas de modèles d’IA, mais les modèles d’IA du monde entier tournent sur des serveurs assemblés par Foxconn.

Mais les règles du jeu de l’ère de l’IA pourraient être différentes. Lorsque le centre de gravité de la valeur glisse du matériel vers le logiciel et les données, les marges d’un modèle limité à la sous-traitance peuvent se contracter. Les deux Nobel attribués en 2024 sont tous allés à des acteurs de la couche logicielle. Hopfield a écrit un modèle mathématique, Hinton un algorithme d’entraînement, Hassabis une méthode pour résoudre un problème biologique. Tous ces travaux fonctionnent sur du matériel fabriqué à Taïwan, mais les médailles ne récompensent pas le matériel.

Taïwan doit faire émerger des capacités logicielles et de données sur la base de son hégémonie matérielle : le matériel demeure le socle, mais de nouvelles couches de valeur doivent se superposer. TAIDE est une tentative ; CyCraft en est une autre ; Taiwan AI Labs aussi. Leur point commun : ne pas chercher à faire « la plus grande IA du monde », mais « l’IA qui comprend le mieux Taïwan ».

Il y a 42 ans, lorsque Hopfield écrivait ses douze pages à Princeton, personne ne savait qu’elles deviendraient une base mathématique des modèles de mémoire de l’humanité. Il y a 50 ans, lorsque Anfinsen formulait son hypothèse sur le repliement des protéines dans son discours Nobel, personne ne prévoyait qu’il faudrait attendre cet après-midi de 2020 pour qu’un groupe de Londoniens la résolve. L’échelle temporelle de la recherche fondamentale est plus longue que chaque édition du Computex.

Le repas du marché nocturne de Ningxia représente la position que Taïwan a accumulée en 42 ans. Où se jouera la prochaine bataille ? Pas devant un stand d’omelette aux huîtres, mais dans la capacité de Taïwan à donner à un étudiant qui programme aujourd’hui dans un dortoir de l’Université nationale de Taïwan le courage et l’environnement nécessaires pour décrocher, dans vingt ou trente ans, le Nobel de cette île.

---

**Pour aller plus loin** :

- [L’essor d’une île IA : développement de l’intelligence artificielle à Taïwan et stratégies d’avenir](/technology/AI發展) — Version antérieure du récit de l’architecture politique : plan d’action IA, cinq domaines stratégiques, et manière dont la « montagne sacrée » des semi-conducteurs s’articule à la révolution de l’IA.
- [Taiwan AI Labs](/technology/台灣人工智慧實驗室) — Le parcours complet d’Ethan Tu, de PTT à AI Labs, et l’écosystème des modèles de langue open source TAIDE / TAME / FedGPT.
- [Taiwan AI Academy](/technology/台灣人工智慧學校) — L’appel téléphonique inachevé et l’« école militaire de l’IA » fondée par Chen Sheng-wei grâce à 180 millions de dollars taïwanais de financement privé : huit ans d’histoire de formation des talents et plus de dix mille anciens.
- [L’IA dans le quotidien taïwanais](/technology/台灣AI日常) — Chronique de l’entrée de l’IA générative dans la vie quotidienne à Taïwan, des commandes en supérette aux examens groupés de l’Administration nationale de l’assurance maladie.
- [Entreprise taïwanaise : TSMC](/economy/台灣企業：台積電) — Leader mondial de la fonderie de wafers, cœur de la fabrication des puces d’IA, du modèle de fonderie pure de Morris Chang aux technologies de packaging avancé.
- [Industrie des semi-conducteurs](/technology/半導體產業) — Panorama complet de l’écosystème taïwanais des semi-conducteurs, de la conception IC au packaging et aux tests.
- [Développement de l’industrie taïwanaise de la cybersécurité](/technology/台灣資安產業發展) — Comment la pression géopolitique a fait naître une industrie de cybersécurité IA de niveau Asie-Pacifique.

---

## Sources des images

Cet article utilise quatre images du domaine public ou sous licence CC, toutes mises en cache dans `public/article-images/technology/` afin d’éviter les hotlinks vers les serveurs sources :

- [Estructura tridimensional de la proteïna CBLN1 per AlphaFold amb codificació rainbow](https://commons.wikimedia.org/wiki/File:Estructura_tridimensional_de_la_prote%C3%AFna_CBLN1_per_AlphaFold_amb_codificaci%C3%B3_rainbow.png) — Image héro, structure prédite par AlphaFold de la protéine CBLN1, codage couleur rainbow de l’extrémité N vers l’extrémité C. Photo : BQUB25-UPoch (own work, AlphaFold + PyMOL), 2025-11-15, CC BY 4.0.
- [Geoffrey E. Hinton, 2024 Nobel Prize Laureate in Physics (3x4 cropped)](<https://commons.wikimedia.org/wiki/File:Geoffrey_E._Hinton,_2024_Nobel_Prize_Laureate_in_Physics_(3x4_cropped).jpg>) — Image inline, portrait officiel de Hinton pendant la semaine Nobel 2024. Photo : Arthur Petron, 2024-12-08, CC BY-SA 4.0.
- [John J. Hopfield, 2024 Nobel Prize Laureate in Physics 1 (cropped)](<https://commons.wikimedia.org/wiki/File:John_J._Hopfield,_2024_Nobel_Prize_Laureate_in_Physics_1_(cropped).jpg>) — Image inline, portrait officiel de Hopfield pendant la semaine Nobel 2024. Photo : Arthur Petron, 2024-12-08, CC BY-SA 4.0.
- [TSMC Fab 5](https://commons.wikimedia.org/wiki/File:TSMC_Fab_5.jpg) — Image inline, usine Fab 5 de TSMC à Hsinchu, site physique de la fonderie des puces d’IA. Photo : Wikimedia Commons (cache existant).

---

## Références

[^1]: [Tom's Hardware: Semiconductor legends take a stroll in a Taiwanese night market](https://www.tomshardware.com/tech-industry/semiconductor-legends-take-a-stroll-in-a-taiwanese-night-market-nvidia-tsmc-mediatek-and-quanta-heads-seen-eating-dinner) — Reportage sur la scène du marché nocturne de Ningxia le 29 mai 2024, documentant le repas partagé par Jensen Huang, Morris Chang, Barry Lam et Rick Tsai.

[^2]: [Taiwan News: Nvidia CEO calls Taiwan 'one of the most important countries in the world'](https://www.taiwannews.com.tw/news/5880054) — Propos publics de Jensen Huang lors de sa visite à Taïwan le 2024-05-30.

[^3]: [Wikipedia: Jensen Huang](https://en.wikipedia.org/wiki/Jensen_Huang) — Données biographiques : Jensen Huang né à Taipei en 1963, enfance à Tainan, immigration aux États-Unis à neuf ans.

[^4]: Tous les GPU avancés de NVIDIA (A100, H100, série Blackwell) sont fabriqués par TSMC. Voir [Klover.ai: TSMC AI Fabricating Dominance](https://www.klover.ai/tsmc-ai-fabricating-dominance-chip-manufacturing-leadership-ai-era/) — Analyse industrielle couvrant les relations de fonderie pour toute la gamme des GPU d’IA de NVIDIA.

[^5]: [SQ Magazine: AI Chip Statistics 2025](https://sqmagazine.co.uk/ai-chip-statistics/) — Source du chiffre de 72 % de part des revenus mondiaux de la fonderie de wafers détenus par TSMC en 2025 ; voir aussi les articles contemporains de Motley Fool.

[^6]: [PatentPC: The AI Chip Market Explosion](https://patentpc.com/blog/the-ai-chip-market-explosion-key-stats-on-nvidia-amd-and-intels-ai-dominance) — Source de la part de marché de 86 % de NVIDIA dans les GPU d’IA.

[^7]: [Tech-Now: Taiwan Leads Global AI Server Shift, Surpassing iPhones in 2025](https://tech-now.io/en/blogs/taiwans-ai-server-revolution-how-foxconn-and-odms-redefined-global-tech-leadership-in-2025) — Données sur les 90 % d’expéditions mondiales de serveurs d’IA assurées par Foxconn, Quanta et Wistron.

[^8]: [DigiTimes: Foxconn, Wistron, Quanta to sustain trillion-dollar revenue on AI server in 2026](https://www.digitimes.com/news/a20260109PD249/revenue-ai-server-foxconn-wistron-quanta.html) — Reportage sur le chiffre d’affaires annuel supérieur à mille milliards de dollars taïwanais des trois ODM et sur le dépassement de l’électronique grand public par les serveurs d’IA.

[^9]: [36Kr: Who Will Divide Up the CoWoS Production Capacity in 2026?](https://eu.36kr.com/en/p/3580962946874242) — Données sur la demande de NVIDIA en wafers CoWoS, estimée à 595 000 unités, soit 60 % du total mondial.

[^10]: [NVIDIA Newsroom: Foxconn Builds AI Factory in Partnership With Taiwan and NVIDIA](https://nvidianews.nvidia.com/news/foxconn-builds-ai-factory-in-partnership-with-taiwan-and-nvidia) — Coopération autour de l’usine IA de 100 MW à Kaohsiung ; voir aussi la couverture de CNBC sur la capacité électrique de 100 MW.

[^11]: [Site officiel de Taiwan AI Labs, À propos](https://ailabs.tw/zh/關於我們/) — Présentation officielle d’Ethan Tu, fondateur de PTT à l’Université nationale de Taïwan en 1995, puis fondateur de Taiwan AI Labs à son retour à Taïwan en avril 2017.

[^12]: [TechNews 科技新報：AI 人才在台灣，該走該留？專訪台灣人工智慧實驗室創辦人杜奕瑾](https://finance.technews.tw/2025/08/18/taiwan-ai-labs-ethan/) — Entretien présentant les projets clés, dont la transcription 雅婷 et l’IA médicale par apprentissage fédéré.

[^13]: [Yuan exécutif : renforcer les infrastructures IA de Taïwan — créer le moteur de dialogue IA fiable TAIDE](https://www.ey.gov.tw/Page/5A8A0CB5B41DA11E/582206fe-26fc-4184-b911-aa6e4569ff3e) — Présentation officielle du lancement du projet TAIDE en avril 2023.

[^14]: [CommonWealth Magazine：「防止中國 AI 文化侵略」台灣第一個繁體中文大語言模型 TAIDE，能做什麼？](https://www.cw.com.tw/article/5129076) — Reportage sur TAIDE et source du discours sur la subjectivité culturelle des LLM en chinois traditionnel.

[^15]: [Communiqué du Conseil national des sciences et de la technologie : TAIDE 一年有成 公私協力共同推進具臺灣特色之大型語言模型](https://www.nstc.gov.tw/folksonomy/detail/dd2d9d72-8f7b-44dd-976c-438d5ce683af?l=ch) — Publication en avril 2024 du TAIDE-LX-7B commercial et du 13B académique.

[^16]: [CloudInsight: Taiwan LLM Development Status 2026](https://cloudinsight.cc/en/blog/taiwan-llm) — Panorama complet de l’écosystème taïwanais des LLM, dont TAIDE 2.0 et Breeze-8B.

[^17]: Même rapport CloudInsight. Présentation détaillée d’applications telles que « 神農 TAIDE » de l’Université nationale Chung Hsing, l’agent conversationnel taïwanais-anglais de l’Université nationale de Tainan et les modèles TAIDE en taïwanais et hakka de l’Université nationale Yang Ming Chiao Tung.

[^18]: [CIO Taiwan：台灣資安業者巡禮——奧義智慧科技](https://www.cio.com.tw/taiwanese-ahn-an-smart-technology/) — Présentation détaillée de CyCraft, mentionnée sept fois par Gartner et trois fois validée par l’évaluation MITRE ATT&CK.

[^19]: [Site officiel de CyCraft : 創新板首發 AI 資安王者！奧義賽博今日掛牌](https://www.cycraft.com/news/taiwans-first-ai-cybersecurity-stock-20260205) — Communiqué du 5 février 2026 sur la cotation au Taiwan Innovation Board.

[^20]: [Conseil national des sciences et de la technologie : stratégie de recherche IA](https://www.nstc.gov.tw/folksonomy/detail/dbf8da09-22be-4ef1-8294-8832fc6e8a26?l=ch) — Cadre politique de la première phase du Plan d’action IA de Taïwan, budget de 40 milliards et construction du TWCC.

[^N1]: [The Nobel Prize in Physics 2024 press release](https://www.nobelprize.org/prizes/physics/2024/press-release/) — Communiqué officiel de l’Académie royale des sciences de Suède du 8 octobre 2024. Original : « The Royal Swedish Academy of Sciences has decided to award the Nobel Prize in Physics 2024 to John J. Hopfield and Geoffrey Hinton 'for foundational discoveries and inventions that enable machine learning with artificial neural networks.' » Dotation de 11 millions de couronnes suédoises, partagée entre les deux lauréats.

[^N2]: [The Nobel Prize in Chemistry 2024 press release](https://www.nobelprize.org/prizes/chemistry/2024/press-release/) — Communiqué du 9 octobre 2024. Dotation de 11 millions de couronnes suédoises : David Baker reçoit la moitié « for computational protein design », Demis Hassabis et John Jumper se partagent l’autre moitié « for protein structure prediction ».

[^N3]: Hopfield, J. J. (1982). "Neural networks and physical systems with emergent collective computational abilities." [PNAS, 79(8), 2554-2558](https://www.pnas.org/doi/10.1073/pnas.79.8.2554) — Article original du réseau de Hopfield, qui compare les réseaux neuronaux à un système de spin glass et propose d’associer un minimum d’énergie au stockage de la mémoire. Publié en avril 1982.

[^N4]: Rumelhart, D. E., Hinton, G. E., & Williams, R. J. (1986). "Learning representations by back-propagating errors." [Nature, 323, 533-536](https://www.nature.com/articles/323533a0) — Article classique sur l’algorithme de rétropropagation, travail fondateur des méthodes d’entraînement des réseaux neuronaux.

[^N5]: Krizhevsky, A., Sutskever, I., & Hinton, G. E. (2012). "ImageNet Classification with Deep Convolutional Neural Networks." [NeurIPS 2012 / NIPS Proceedings](https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html) — Article original d’AlexNet, taux d’erreur top-5 de 15,3 % à ImageNet ILSVRC-2012 contre 26,2 % pour le deuxième, tournant clé de l’industrialisation de l’apprentissage profond.

[^N6]: [PanSci 泛科學：2024 諾貝爾物理獎—— Hopfield 與 Hinton 開啟了人工神經網路機器學習時代](https://pansci.asia/archives/378242) — Content Curation Partner per MOU 2026-05-05. Couvre le contexte de proposition du réseau de Hopfield, l’analogie avec le spin glass, l’accumulation des citations de l’article et le lien mathématique avec l’apprentissage profond contemporain.

[^N7]: [The Guardian: Nobel physics prize 2024 winner John Hopfield warns of AI dangers](https://www.theguardian.com/science/2024/oct/08/nobel-prize-physics-2024-john-hopfield-geoffrey-hinton-ai-machine-learning) — Reportage du 2024-10-08 sur l’entretien téléphonique du prix Nobel de physique, où Hopfield et Hinton émettent le même jour des avertissements sur les risques de l’IA.

[^N8]: [Wikipedia: Geoffrey Hinton](https://en.wikipedia.org/wiki/Geoffrey_Hinton) — Hinton né le 6 décembre 1947 à Wimbledon, Londres ; Google rachète DNNresearch pour 44 millions de dollars en mars 2013, après quoi il rejoint Google.

[^N9]: [BBC News: AI 'godfather' Geoffrey Hinton warns of dangers as he quits Google](https://www.bbc.com/news/world-us-canada-65452940) — Le 2023-05-01, après son départ de Google, Hinton exprime à la BBC ses inquiétudes sur les risques de l’IA. Original : « I left so that I could talk about the dangers of AI without considering how this impacts Google », « a part of me now regrets my life's work ». Les détails de l’entretien contemporain du NYT sont aussi cités dans cet article.

[^N10]: [Nature: AI scientist Geoffrey Hinton wins Nobel prize for physics](https://www.nature.com/articles/d41586-024-03213-8) — Récit détaillé par _Nature_ de l’attribution du Nobel de physique 2024 et de l’entretien téléphonique avec Hinton.

[^N11]: [Wikipedia: Economic history of Taiwan](https://en.wikipedia.org/wiki/Economic_history_of_Taiwan) — Données sur le PIB de Taïwan en 1986 ; le parc scientifique de Hsinchu est fondé en décembre 1980.

[^N12]: Anfinsen, C. B. (1973). "Principles that govern the folding of protein chains." [Science, 181(4096), 223-230](https://www.science.org/doi/10.1126/science.181.4096.223) — L’un des travaux récompensés par le Nobel de chimie 1972, proposant l’hypothèse selon laquelle le repliement des protéines est déterminé par la séquence d’acides aminés.

[^N13]: [Nature: 'It will change everything': DeepMind's AI makes gigantic leap in solving protein structures](https://www.nature.com/articles/d41586-020-03348-4) — Reportage du 30 novembre 2020 sur les résultats de CASP14 : AlphaFold 2 obtient une médiane GDT de 92,4, et l’organisateur de CASP John Moult commente que « in some sense the problem is solved ».

[^N14]: [DeepMind: AlphaFold reveals the structure of the protein universe](https://www.deepmind.com/blog/alphafold-reveals-the-structure-of-the-protein-universe) — Annonce du 28 juillet 2022 indiquant que l’AlphaFold Protein Structure Database couvre un million d’espèces et environ 200 millions de structures protéiques.

[^N15]: [Abramson, J., Adler, J., Dunger, J. et al. (2024). Accurate structure prediction of biomolecular interactions with AlphaFold 3. Nature 630, 493-500](https://www.nature.com/articles/s41586-024-07487-w) — Publication d’AlphaFold 3 le 8 mai 2024, étendant la prédiction aux complexes entre protéines et ADN / ARN / ligands / ions.

[^N16]: [Wikipedia: Demis Hassabis](https://en.wikipedia.org/wiki/Demis_Hassabis) — Hassabis commence les échecs à quatre ans, codéveloppe _Theme Park_ avec Peter Molyneux à 17 ans (1994), fonde DeepMind à Londres en 2010, rachetée par Google en 2014 pour environ 400 millions de livres sterling.

[^N17]: [Centre de recherche en génomique de l’Academia Sinica](https://www.genomics.sinica.edu.tw/) — Centre de recherche sur la structure des glycomolécules et des protéines établi pendant la présidence de Chi-Huey Wong à l’Academia Sinica (2006-2016).

[^N18]: [PanSci 泛科學：2024 諾貝爾化學獎—— David Baker、Demis Hassabis、John Jumper 解開蛋白質摺疊難題](https://pansci.asia/archives/378388) — Content Curation Partner per MOU 2026-05-05. Couvre la controverse autour du Nobel de chimie attribué à AlphaFold et le débat sur les frontières disciplinaires entre biologie structurale et chimie computationnelle.

[^N19]: [PanSci 泛科學：AlphaFold 3 預測蛋白質與其他分子互動，藥物開發再升級](https://pansci.asia/archives/377917) — Content Curation Partner per MOU 2026-05-05. Analyse de l’impact d’AlphaFold 3 sur le développement de médicaments et l’ingénierie enzymatique.

[^N20]: [PanSci 泛科學：「人造腦」OI 挑戰 AI——培養皿裡的腦組織能取代矽晶片嗎？](https://pansci.asia/archives/366027) — Content Curation Partner per MOU 2026-05-05. Recherche de l’équipe de Thomas Hartung à Johns Hopkins sur les cerveaux artificiels, comme voie de calcul alternative à l’IA sur silicium.
