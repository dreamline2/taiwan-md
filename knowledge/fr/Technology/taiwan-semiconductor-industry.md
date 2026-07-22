---
title: 'Industrie des semi-conducteurs : cinquante ans de révolution des matériaux, du transfert technologique de RCA au nitrure de gallium et au packaging quantique'
description: "La montagne sacrée qui protège Taïwan domine les procédés avancés mondiaux grâce à la fonderie, mais le nitrure de gallium dans les chargeurs rapides, le CoWoS sous les puces d'IA et les réfrigérateurs à dilution au-dessus des qubits annoncent un champ de bataille des matériaux qui ne fait que s'ouvrir pour les cinquante prochaines années."
date: 2026-03-17
author: 'Taiwan.md'
category: 'Technology'
subcategory: '半導體與硬體'
tags:
  [
    'semi-conducteurs',
    'TSMC',
    'Taiwan Semiconductor Manufacturing Company',
    'nitrure de gallium',
    'packaging 3D',
    'CoWoS',
    'ordinateur quantique',
    'procédés avancés',
    'bouclier de silicium',
    'science des matériaux',
  ]
readingTime: 22
lastVerified: 2026-05-19
lastHumanReview: true
featured: true
translatedFrom: 'Technology/半導體產業.md'
sourceCommitSha: '31a05c44'
sourceContentHash: 'sha256:353dd1410e58546f'
sourceBodyHash: 'sha256:b4789b1cdfeb8d09'
translatedAt: '2026-06-16T16:54:51Z'
image: '/article-images/technology/silicon-vs-gan-charger-2025.webp'
imageCredit: '4300streetcar'
imageLicense: 'CC BY 4.0'
imageSource: 'https://commons.wikimedia.org/wiki/File:Silicon_vs_GaN_30W_USB-C_chargers.jpg'
---

# Industrie des semi-conducteurs : cinquante ans de révolution des matériaux, du transfert technologique de RCA au nitrure de gallium et au packaging quantique

![Deux chargeurs rapides USB-C de 30 W, de même puissance, comparés côte à côte : le produit en silicium à gauche est nettement plus volumineux, tandis que le produit en nitrure de gallium à droite est presque deux fois plus petit, montrant comment la science des matériaux concentre la densité énergétique dans la paume de la main](/article-images/technology/silicon-vs-gan-charger-2025.webp)
_Comparaison de volume entre chargeurs USB-C de même puissance, Si contre GaN. Photo : 4300streetcar, 2025-12-25. [Licence via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Silicon_vs_GaN_30W_USB-C_chargers.jpg)._

> **Aperçu en 30 secondes :** au quatrième trimestre 2025, TSMC a lancé la production de masse en 2 nm dans sa Fab 22 de Kaohsiung, avec deux à trois générations d’avance sur le reste du monde[^2]. Mais l’histoire ne se joue pas seulement dans des transistors toujours plus petits : le chargeur rapide dans votre sac contient du nitrure de gallium (GaN), GlobalWafers fabrique des wafers de carbure de silicium (SiC) de 8 pouces à Zhongli, et les GPU Blackwell de NVIDIA arrivent dans les centres de données grâce au packaging CoWoS de TSMC. Depuis les 4,5 millions de dollars versés en 1973 par l’ITRI pour acheter la technologie de RCA[^5] jusqu’à la connexion en ligne, en 2026, de la puce quantique supraconductrice à 20 qubits de l’Academia Sinica[^6], Taïwan a parcouru un long fleuve de science des matériaux, de la physique des bandes interdites au dépôt de couches atomiques, puis aux qubits topologiques. La montagne sacrée qui protège le pays s’appuie sur cinquante ans d’expérience en fonderie ; mais dans l’ère quantique, Taïwan n’a pas encore conquis sa position de fonderie.

Un après-midi de 1985, le ministre sans portefeuille Li Kwoh-ting convoque Morris Chang, tout juste rentré à Taïwan pour prendre la direction de l’Industrial Technology Research Institute (ITRI), au Yuan exécutif. Li va droit au but : « Nous voulons créer une très grande entreprise de fabrication de circuits intégrés. Vous en prendrez la direction. »

Morris Chang reste interdit. Il pensait n’être venu que pour diriger l’ITRI ; deux semaines plus tard, on le pousse à fonder une entreprise dont personne n’a encore éprouvé le modèle économique.

Cette conversation a changé le monde. Mais quarante ans plus tard, le « monde » en question se révèle bien plus dense que ce que cet après-midi-là pouvait laisser imaginer. Il inclut le chargeur rapide de 65 watts, à peine plus grand que deux phalanges, posé près de votre téléphone ; chaque GPU Blackwell que NVIDIA fait fonctionner dans ses centres de données ; et les qubits qui ne s’éveillent, dans les laboratoires de l’Academia Sinica, qu’à une température proche du zéro absolu.

## Le pari de la fonderie en 1987

![Vue extérieure de la Fab 5 de TSMC dans le parc scientifique de Hsinchu, un bâtiment industriel à plusieurs niveaux relié à Guangfu Road, l’un des sites représentatifs de l’expansion de TSMC dans les années 1990](/article-images/technology/tsmc-fab5-hsinchu-2010.webp)
_Fab 5 de TSMC dans le parc scientifique de Hsinchu, 2010. Photo : Peellden. [Licence via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:TSMC_Fab5.JPG)._

L’histoire commence plus tôt. En 1973, l’ITRI dépense 4,5 millions de dollars pour acquérir la technologie des circuits intégrés de l’américain RCA et envoie 19 ingénieurs se former aux États-Unis[^5]. Personne n’imagine alors que ces « frais de scolarité » deviendront la première pierre du royaume taïwanais des semi-conducteurs. En 1980, l’ITRI transfère sa technologie pour créer United Microelectronics Corporation (UMC), donnant à Taïwan sa première entreprise de semi-conducteurs. Mais Li Kwoh-ting n’est pas satisfait : UMC est trop petite, sa technologie ne rattrape pas les standards internationaux, et Taïwan a besoin d’une rupture plus ample.

Le 21 février 1987, Morris Chang fonde Taiwan Semiconductor Manufacturing Company dans le parc scientifique de Hsinchu et inaugure un modèle économique inédit : la **fonderie pure**.

À l’époque, l’idée paraît folle. Toutes les entreprises de semi-conducteurs du monde sont intégrées verticalement, de la conception à la fabrication. Comment peut-on ne faire que fabriquer, sans concevoir ? Les clients accepteront-ils de vous confier leurs plans les plus secrets ?

La logique de Morris Chang est simple : l’industrie des semi-conducteurs devient de plus en plus complexe, et la conception comme la fabrication sont deux métiers totalement distincts. Plutôt que de tout faire sans exceller nulle part, mieux vaut se concentrer sur une seule chose : devenir le meilleur fabricant de puces au monde.

La structure du capital initial de TSMC est habile : 48,3 % d’investissement public, 24,2 % d’investissement privé, et 27,6 % pour le néerlandais Philips[^1]. La participation de Philips est décisive. À l’époque, l’industrie des semi-conducteurs est dominée par les États-Unis et le Japon, et l’Europe a un besoin urgent de fournisseurs alternatifs. Philips n’investit pas seulement : l’entreprise confie aussi ses propres commandes de puces à TSMC, devenant son premier grand client.

Le modèle de la fonderie déclenche une vaste division du travail dans l’industrie : les concepteurs de circuits intégrés se concentrent sur le design des puces (Qualcomm, NVIDIA, MediaTek), les fonderies sur la fabrication (TSMC, UMC, GlobalFoundries), et les assembleurs-testeurs sur les étapes aval (ASE, SPIL). Autrefois, seuls des géants comme Intel ou IBM pouvaient supporter les investissements astronomiques d’une fab. Désormais, toute start-up dotée d’une bonne idée peut concevoir une puce, puis la confier à TSMC.

Le cœur du modèle de fonderie est la confiance. Les clients doivent croire que TSMC ne volera pas leurs conceptions, ne divulguera pas leurs secrets commerciaux et ne les concurrencera pas. TSMC établit un ensemble de « règles de confiance » en quatre principes : neutralité technologique, c’est-à-dire ne jamais concevoir ses propres puces ; égalité entre clients, avec les mêmes technologies et services pour tous ; accords de confidentialité du plus haut niveau ; répartition équitable des capacités. Ces règles sont appliquées depuis près de quarante ans, sans exception.

> 📝 **Note curatoriale** : dans le Taïwan de 1987, les 19 ingénieurs envoyés par l’ITRI chez RCA venaient à peine de passer la quarantaine. Ils avaient appris les procédés silicium américains des années 1960, et personne n’aurait pu prévoir qu’ils deviendraient trente ans plus tard les donneurs d’ordre de la technologie mondiale du packaging. Quant à la clause d’« autolimitation volontaire » par laquelle TSMC décidait de ne pas concevoir ses propres puces, elle est devenue le lien dont Jensen Huang, Tim Cook et Lisa Su ne peuvent plus se passer. La grandeur du modèle de fonderie ne tient pas à ce qu’il a fait, mais à ce qu’il a **choisi de ne pas faire**. En remontant plus loin, les Bell Labs inventent le transistor en 1947, Texas Instruments et Fairchild produisent chacun un circuit intégré en 1958, et l’arrivée du gouvernement nationaliste à Taïwan en 1949 amène une génération de technocrates formés aux sciences et à l’ingénierie, qui constitueront plus tard l’ossature de l’ITRI. Les 4,5 millions de dollars versés à RCA furent un relais, non un point de départ.

## Burn J. Lin et ASML : le pari de deux petits dans l’exposition sous eau

La fonderie ne concerne pas seulement TSMC. Le lecteur [@malathrone_21k_running](https://www.threads.com/@malathrone_21k_running) a ajouté dans les commentaires une ligne historique essentielle : TSMC partage avec ASML un même lignage Philips. ASML est l’entreprise de machines de lithographie issue de Philips aux Pays-Bas en 1984 ; elle est aujourd’hui l’unique fournisseur mondial de machines EUV (extreme ultraviolet). Il y a trente ans, ces deux entreprises étaient des « petits » que les géants du secteur ne prenaient pas au sérieux[^asml-philips].

Le personnage clé de cette histoire est un ingénieur taïwanais, Burn J. Lin. À partir de 1992, il travaille sur la lithographie au centre de recherche IBM Watson, puis rentre à Taïwan en 2000 pour rejoindre TSMC comme directeur de la R&D[^lin-bio]. À cette époque, la prochaine voie de la lithographie fait l’objet d’un affrontement : Nikon et Intel parient sur l’ultraviolet profond à 157 nm, mais cette trajectoire rencontre problème sur problème. Les lentilles en fluorure de calcium présentent une biréfringence, les films absorbent trop fortement cette longueur d’onde, et l’intégration de procédé est difficile[^157nm-fail].

En 2002, lors d’une conférence d’optique de SPIE, Burn J. Lin propose une idée folle : « conserver la source lumineuse de 193 nm, mais injecter de l’eau entre la lentille et le wafer ». L’indice de réfraction de l’eau est de 1,44 ; dans l’eau, une lumière de 193 nm équivaut à une résolution d’environ 134 nm, plus fine que le 157 nm, sans changer de source lumineuse ni de lentilles[^immersion-litho].

Nikon n’y croit pas et continue de miser sur le 157 nm. ASML accepte le pari. L’entreprise est elle aussi un petit acteur, comme TSMC, à la recherche d’un levier physique pour renverser la situation. En 2003, ASML commence à développer des machines de lithographie par immersion 193 nm (193i) ; en 2007, elle est la première à les produire en masse. Cette technologie soutiendra **six générations** de procédés, du 65 nm jusqu’à la relève par l’EUV actuelle[^immersion-litho][^cw-lin-interview].

« Nikon n’osait pas faire l’immersion par crainte de la chaleur ; ASML et nous avons donc dû nous débrouiller », résume cette trajectoire qui a fait tomber Nikon de son trône dans la lithographie[^cw-lin-interview]. Il y a trente ans, deux petits acteurs ont chacun fait leur pari. Aujourd’hui, l’un est l’unique fabricant mondial de machines EUV, l’autre l’unique fonderie mondiale en 2 nm. Les deux graines semées par Philips aux Pays-Bas se retrouvent sur la même scène au XXIe siècle.

## Cinquante ans de généalogie des matériaux : du silicium au nitrure de gallium, puis aux supraconducteurs topologiques

Pour comprendre le champ de bataille des semi-conducteurs en 2025, il faut d’abord comprendre une ligne physique qui n’a jamais été clairement racontée.

Le silicium (Si) en est le point de départ. Sa « bande interdite » est de 1,1 électronvolt (eV), soit le ticket énergétique minimal que doit payer un électron pour passer de la bande de valence à la bande de conduction. Une faible bande interdite rend les puces faciles à fabriquer, mais impose deux plafonds : les hautes tensions provoquent la rupture, et les hautes fréquences produisent de la chaleur. PanSci décrit cette limite sans détour : « Pour les semi-conducteurs en silicium, la limite de fréquence de fonctionnement n’est que sous les 100 k ; au-delà de 100 k, l’efficacité de conversion chute fortement, avec un sérieux problème de gaspillage d’énergie. »[^7]

La bande interdite du nitrure de gallium (GaN) est de 3,4 eV, trois fois celle du silicium ; sa limite de tension de rupture est dix fois supérieure ; sa fréquence de fonctionnement peut atteindre 1000 K, soit un ordre de grandeur au-dessus du silicium[^7]. Traduit dans la vie quotidienne, ce chiffre physique donne ceci : à puissance égale, les bobines d’inductance du transformateur en nitrure de gallium peuvent être beaucoup plus petites, et les exigences de dissipation thermique bien plus faibles. C’est ainsi qu’est né le chargeur rapide dont le volume tient dans la paume.

Le carbure de silicium (SiC) suit une autre voie. Lui aussi est à large bande interdite, avec 3,26 eV, mais il résiste mieux aux hautes températures et aux hautes tensions. PanSci identifie clairement son champ de bataille : « Le carbure de silicium possède une bonne stabilité à haute température et sous haute tension. Avec la hausse future de la demande en recharge rapide pour véhicules électriques, les besoins de charge au-delà de 1000 volts rendront insuffisants les semi-conducteurs au silicium, qui ne supportent que 600 volts ; le SiC devrait prendre le relais comme composant clé des véhicules électriques. »[^7]

> 💡 **Le saviez-vous ?** La « bande interdite » d’un semi-conducteur détermine la tension qu’il peut supporter, la fréquence à laquelle il peut fonctionner et la chaleur qu’il produit. Les 1,1 eV du silicium sont la base de l’électronique grand public depuis cinquante ans ; les 3,4 eV du nitrure de gallium soutiennent les charges rapides de téléphone à 240 watts ; les 3,26 eV du carbure de silicium entrent dans les onduleurs de véhicules électriques à 800 volts ; la prochaine étape pourrait être le diamant, avec 5,5 eV. Toute cette généalogie des matériaux est une échelle où la densité énergétique grimpe palier après palier, et à chaque marche Taïwan doit renégocier avec les limites physiques de la science des matériaux.

La prochaine étape n’a pas encore de nom : peut-être le diamant (C, bande interdite de 5,5 eV), l’oxyde de gallium (Ga₂O₃, 4,8 eV), ou bien l’entrée dans des mécanismes physiques entièrement différents, comme les supraconducteurs topologiques. C’est la voie empruntée par le processeur quantique Majorana 1 annoncé par Microsoft en février 2025[^15]. Si la physique change, toute la chaîne industrielle sera réécrite avec elle.

## Le nitrure de gallium dans votre chargeur rapide

Ramenons la caméra vers votre sac.

Le chargeur du Nokia 3310 délivrait 4,56 watts ; les chargeurs rapides de 2025 montent à 240 watts. L’écart est de 52 fois. PanSci a retracé cette chronologie : « Les chargeurs rapides au nitrure de gallium, aujourd’hui très en vogue, atteignent déjà 65 watts, soit treize fois plus ; en théorie, le temps de charge devrait donc être réduit à un treizième. »[^7] Plus spectaculaire encore, la marque chinoise realme a lancé début 2023 le GT Neo5 à charge ultrarapide de 240 watts, portant ce multiple au-delà de 50.

Physiquement, cette courbe de croissance repose sur le passage au nitrure de gallium, tandis que l’épaisseur du cuivre et le volume des batteries diminuent. Pour augmenter la puissance tout en réduisant le volume, la méthode la plus directe consiste à élever la fréquence de fonctionnement. Mais « pour les semi-conducteurs en silicium, la limite de fréquence de fonctionnement n’est que sous les 100 k »[^7] : c’est la « limite du silicium » décrite par PanSci. Le nitrure de gallium pousse la fréquence au-delà de 1 MHz, ce qui réduit en même temps la taille du transformateur et des inductances, permettant au chargeur entier de tenir dans une poche.

Le problème est qu’au moment où le marché taïwanais de la charge rapide s’apprête à exploser, TSMC annonce une décision : **se retirer de la fonderie GaN en juillet 2027**[^8].

Deux pressions expliquent ce choix. La première vient de l’expansion massive des fabricants chinois de GaN, comme China Resources Microelectronics, Silan Microelectronics ou Innoscience, qui poussent les prix de fonderie à des niveaux que TSMC ne souhaite plus accepter. La seconde tient à la rentabilité trop attractive des puces d’IA : TSMC veut convertir ses fabs GaN en lignes de packaging avancé CoWoS. Les licences technologiques sont accordées à Vanguard International Semiconductor (VIS) et GlobalFoundries ; le fardeau de la fonderie GaN taïwanaise revient alors à des fabricants comme Win Semiconductors (3163) et Advanced Wireless Semiconductor (8086), qui avaient commencé à miser sur ce secteur dix ans plus tôt[^8].

> ⚠️ **Point de controverse** : le retrait de TSMC de la fonderie GaN donne lieu à deux lectures. Pour les uns, c’est un choix rationnel consistant à « réserver la capacité à l’IA » : la marge d’un wafer 3 nm dépasse de plus de vingt fois celle d’un wafer GaN de 6 pouces, et l’allocation des capacités va naturellement vers les meilleurs rendements. Pour les autres, l’abandon du GaN revient pour Taïwan à céder aux fabricants chinois la prochaine base matérielle de l’électronique grand public, smartphones, ordinateurs portables et chargeurs. Le « bouclier » du bouclier de silicium ne resterait-il alors que du côté de l’IA ? La différence entre les deux camps tient à ceci : pensez-vous que la valeur de la montagne sacrée réside dans le « procédé le plus avancé et irremplaçable », ou dans « l’écosystème complet de toute la chaîne d’approvisionnement » ?

Qu’il s’agisse de TSMC, du grand fabricant de wafers GlobalWafers ou des autres acteurs taïwanais et internationaux des semi-conducteurs, tous ont déjà pris ce train[^7]. Mais choisir dans quel wagon monter est une autre affaire.

## Les wafers SiC de 8 pouces de GlobalWafers

Si le nitrure de gallium est l’histoire de la charge rapide des téléphones, le carbure de silicium est celle des véhicules électriques.

Le cœur de cette ligne SiC à Taïwan n’est pas TSMC, mais GlobalWafers. En 2024, sa capacité mensuelle de wafers SiC de 6 pouces atteint environ 20 000 unités ; ses fours de croissance cristalline développés en interne passent de 3 à 20 ; le rendement dépasse 50 %[^9]. En 2025, l’entreprise lance la production de masse de wafers SiC de 8 pouces, une première à Taïwan.

Doris Hsu, CEO de GlobalWafers, parle toujours directement : « Sino-American Silicon Products constitue un “groupe IDM virtuel” et vise la demande en carbure de silicium des cinq prochaines années. Nous rattrapons vite. »[^9] La stratégie consiste à lier en une même chaîne, sous la maison mère Sino-American Silicon Products, la croissance cristalline avec GlobalWafers, l’épitaxie avec Actron Technology et les modules avec Hung Yang Semiconductor.

Mais le SiC n’est pas une histoire de progression linéaire. Au second semestre 2025, les fabricants chinois de SiC, comme Sanan Optoelectronics ou Tankeblue, augmentent frénétiquement leurs capacités, provoquant une surabondance mondiale. Le taux d’utilisation des capacités SiC de 6 et 8 pouces de GlobalWafers tombe un temps sous les 50 %[^10]. Par rapport au scénario optimiste de l’article de PanSci de 2023, qui prévoyait une prise de relais par la demande de véhicules électriques, un creux supplémentaire s’est ouvert.

Le signal de reprise vient de NVIDIA. Selon des rumeurs, la prochaine plateforme GPU Rubin de NVIDIA adopterait le SiC dans son interposeur, en combinaison avec une architecture de centres de données en courant continu haute tension à 800 volts, pour une production de masse complète en 2027[^10]. Si cette rumeur se confirme, les capacités SiC de 8 pouces de GlobalWafers passeraient des véhicules électriques aux centres de données d’IA, et toute l’histoire serait rallumée.

> 📝 **Note curatoriale** : le nitrure de gallium et le carbure de silicium sont souvent regroupés sous l’étiquette de « semi-conducteurs de troisième catégorie », mais à Taïwan cette catégorie signifie plus qu’un simple label de « matériaux de nouvelle génération ». Elle désigne le premier domaine dans lequel l’industrie taïwanaise des semi-conducteurs peut disposer d’une chaîne d’approvisionnement complète **en contournant TSMC**. Croissance cristalline chez GlobalWafers, fabrication chez Episil, packaging chez Win Semiconductors, conception chez Advanced Wireless Semiconductor : au-delà de la montagne sacrée, une autre montagne de « troisième catégorie », bien plus discrète mais autonome, est en train de pousser.

## Le lien entre Jensen Huang et CoWoS+

Retour au champ de bataille de l’IA.

Le GPU H100 de NVIDIA utilise le procédé 4 nm de TSMC et un packaging CoWoS-S pour intégrer la mémoire à haute bande passante HBM3. Le Blackwell B200 passe au CoWoS-L, combinant deux GPU Blackwell et un CPU Grace, avec une vitesse d’entraînement IA quatre fois supérieure au H100[^11]. La génération suivante, Rubin, est attendue pour 2026.

Au cœur de chaque génération de GPU se trouve ce double moteur : « procédé avancé + packaging avancé ». Le procédé réduit sans cesse les transistors ; le packaging rapproche de plus en plus différents dies. PanSci a expliqué cela par une comparaison entre la route provinciale 9 et le tunnel de Xueshan : « Le packaging traditionnel doit emprunter la sinueuse route provinciale 9, tandis que le packaging avancé coupe les virages et perce le tunnel de Xueshan reliant les deux lieux, rendant les échanges de données plus commodes et plus rapides. »[^12]

Le cœur de CoWoS (Chip-on-Wafer-on-Substrate) est le « via traversant le silicium » (through-silicon via, TSV) : différents dies sont empilés et reliés par de minuscules canaux verticaux qui traversent le substrat de silicium, transformant deux circuits auparavant séparés en une connexion tridimensionnelle. PanSci le formule clairement : « L’empilement tridimensionnel permet de placer la puce C au-dessus de la puce A et, au moyen de vias traversant le silicium dans un substrat aminci, de connecter les deux circuits par des conducteurs verticaux à très haute densité. La distance entre les deux passe ainsi du bout du monde à la proximité immédiate. »[^12]

Les chiffres de capacité sont encore plus frappants. La capacité mensuelle CoWoS de TSMC est d’environ 35 000 wafers fin 2024 ; l’objectif est de 75 000 fin 2025, puis de tendre vers 150 000 en 2028, soit un taux de croissance annuel composé proche de 80 %[^13]. NVIDIA a directement réservé les capacités CoWoS de TSMC jusqu’en 2027, et **toutes les puces, quelle que soit la fab TSMC où elles sont produites, y compris en Arizona, doivent revenir à Taïwan pour le packaging CoWoS final**[^13].

C’est le duopole Jensen Huang-TSMC. NVIDIA bloque le nœud clé côté design ; TSMC le bloque côté fabrication et packaging. Ensemble, les deux entreprises verrouillent les points critiques des centres de données d’IA.

Le 2 juin 2024, dans le gymnase de l’Université nationale de Taïwan, Jensen Huang expose ce lien au monde entier lors de son keynote Computex. Les diapositives montrent les feuilles de route Blackwell et Rubin, mais derrière chacune se trouvent les lignes CoWoS de TSMC.

<div class="video-embed" style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;margin:1.5rem 0;border-radius:8px;">
  <iframe src="https://www.youtube.com/embed/pKXDVsWZmUU" title="NVIDIA CEO Jensen Huang Keynote at COMPUTEX 2024" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

_Chaîne officielle de NVIDIA : keynote « The Era of AI » de Jensen Huang au Computex, le 2 juin 2024, dans le gymnase de l’Université nationale de Taïwan. Pendant deux heures, il déroule les GPU Blackwell, NVLink et Spectrum-X, diapositive après diapositive. Mais le site physique de chacune d’elles se trouve à Baoshan, Hsinchu. Il n’a pas prononcé la phrase « sans TSMC, pas de NVIDIA », mais chaque graphique de capacité la disait déjà._

Le packaging 3D a aussi son coût physique. PanSci en a souligné les difficultés : « Le packaging avancé exige une grande planéité des dies nus et un alignement très précis des puces. Si, lors de l’empilement, certains contacts ne se connectent pas correctement, le rendement en souffre. En outre, les circuits intégrés produisent des pertes d’énergie et une hausse de température lorsqu’ils calculent ; le packaging avancé rapproche les dies nus, les transferts thermiques s’influencent mutuellement, chacun réchauffant l’autre, ce qui rend la dissipation encore plus difficile. »[^12]

L’étape suivante est SoIC (System on Integrated Chips) et SoW-X (System on Wafer). SoIC est le « vrai 3D » : des wafers directement empilés sur des wafers, sans bumps. SoW-X devrait entrer en production de masse en 2027 ; sa taille de masque est 9,5 fois celle du CoWoS actuel, il intègre plus de 16 grandes puces de calcul, et sa puissance de calcul dépasse de 40 fois celle du CoWoS existant[^13]. Plus les puces d’IA grossissent, plus les lignes de packaging de TSMC ressemblent à de petites usines autonomes.

## ALD : faire croître les atomes couche par couche

![Dans une vitrine de musée sont exposés plusieurs échantillons de wafers de silicium de tailles différentes, le plus grand mesurant environ 12 pouces de diamètre ; leur éclat miroir montre la matière première centrale de la fabrication des semi-conducteurs](/article-images/technology/silicon-wafers-museum-2017.webp)
_Échantillons de wafers de silicium, 2017. Photo : ArticCynda. [Licence via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Silicon_wafers.jpg)._

3 nm, 2 nm, 1,6 nm. Derrière ces chiffres se trouve une technologie de fabrication discrète mais décisive : le dépôt de couches atomiques (Atomic Layer Deposition, ALD).

L’ALD a été inventé par un Finlandais, mais il est devenu une étape centrale et incontournable de chaque wafer taïwanais en procédé avancé.

L’histoire commence en Finlande. En 1974, le spécialiste des matériaux Tuomo Suntola commence à développer l’ALD au sein de l’entreprise finlandaise Instrumentarium Oy ; la technologie prend forme en 1977 et apparaît pour la première fois dans une démonstration industrielle[^14]. À l’époque, elle ne sert qu’à fabriquer des écrans électroluminescents, et Suntola lui-même n’imagine pas qu’elle deviendra trente ans plus tard l’artère vitale des procédés nanométriques. En 1999, il vend la technologie ALD à l’équipementier néerlandais ASM ; aujourd’hui, ASM détient plus de 55 % du marché de l’ALD[^14].

PanSci explique son principe avec netteté : « Le dépôt de couches atomiques est une technique améliorée de dépôt chimique en phase vapeur, qui divise le processus de dépôt en deux étapes. D’abord, on injecte le premier précurseur, qui réagit avec la surface du substrat... Une fois la surface saturée, on injecte le second précurseur, qui réagit avec le précurseur déjà fixé pour former le matériau cible et achever la fabrication du film. »[^14] Les deux précurseurs sont injectés l’un après l’autre, et chaque cycle ne fait croître qu’un film de l’épaisseur d’une couche atomique.

Pourquoi est-ce important ? Parce que dans le procédé 2 nm, l’épaisseur de la grille (gate) du transistor ne compte plus que quelques atomes, tandis que la couche isolante de grille doit offrir une planéité et un contrôle d’épaisseur à l’échelle atomique. Le dépôt chimique en phase vapeur traditionnel (CVD) ne le permet pas ; le dépôt physique en phase vapeur (PVD) non plus. Seul l’ALD permet de « faire pousser couche par couche ». Dans chaque fab de procédés avancés de TSMC se trouvent des machines ALD d’ASM. Cette chaîne qui associe équipements néerlandais, technologie finlandaise et procédés taïwanais constitue la base physique de la production de masse en 2 nm.

> 💡 **Le saviez-vous ?** La plus petite dimension caractéristique du procédé 2 nm correspond approximativement à la largeur de 20 atomes de silicium alignés. Si l’on agrandissait un atome de silicium à la taille d’une balle de ping-pong, le transistor 2 nm aurait environ la longueur d’une table de ping-pong. Le travail de l’ALD consiste à recouvrir cette table de matériau isolant « balle par balle ».

ASM n’est pas cotée à Taïwan, mais les plus grands clients de presque toutes ses machines ALD pour wafers de 12 pouces se trouvent à Taïwan. **Cette chaîne d’approvisionnement est invisible mais irremplaçable** : si la production 2 nm de TSMC devait rencontrer des difficultés, il n’existerait pas de second fournisseur ALD capable de prendre le relais.

## Après le 2 nm vient le quantique

L’histoire qui suit l’échelle de l’ångström, où 1 nm vaut 10 ångströms, TSMC ne l’a pas encore écrite jusqu’au bout.

Au quatrième trimestre 2025, TSMC lance la production de masse en 2 nm dans sa Fab 22 de Kaohsiung, suivie par la Fab 20 de Baoshan, Hsinchu[^2]. Le 2 nm adopte pour la première fois l’architecture de transistors nanosheet GAA (Gate-All-Around), abandonnant les transistors à effet de champ à ailettes (FinFET) utilisés depuis le 22 nm jusqu’au 3 nm[^16]. Le 2 nm équivaut à la largeur d’environ 20 atomes de silicium et approche déjà la frontière théorique de la physique. Les premiers clients incluent les puces de série A d’Apple et les puces d’IA de NVIDIA ; les capacités du procédé 2 nm augmenteront trimestre après trimestre[^3].

L’étape suivante est le 1,6 nm (A16), prévu pour une production de masse au quatrième trimestre 2026, avec l’introduction initiale du « réseau d’alimentation par l’arrière » (Backside Power Delivery Network), que TSMC appelle Super Power Rail[^16]. À consommation égale, il est 10 % plus rapide que N2P ; à performance égale, il économise 15 à 20 % d’énergie.

Mais après le 1,6 nm ? Plus les nœuds de procédé descendent, plus ils coûtent cher. Le coût de R&D du 28 nm est d’environ 1 milliard de dollars ; le 7 nm monte à 3 milliards ; le 3 nm grimpe à 10 milliards ; le 2 nm dépasserait 20 milliards[^4]. La courbe exponentielle de la loi de Moore transforme les coûts de R&D des étapes finales en chiffres astronomiques. C’est aussi ce que PanSci veut dire lorsqu’il écrit que « la complexité et les capitaux nécessaires au développement des procédés avancés augmentent de manière exponentielle, tandis que l’investissement et le retour ne sont souvent pas proportionnels »[^12].

L’industrie des semi-conducteurs change donc de stratégie : l’expansion horizontale devient empilement vertical avec le packaging 3D ; le silicium cède la place à de nouveaux matériaux comme GaN et SiC ; et, à terme, la bascule pourrait se faire vers une physique du calcul entièrement différente, par exemple le calcul quantique.

La chronologie de l’Academia Sinica avance ainsi. En octobre 2023, un ordinateur quantique supraconducteur à 5 qubits est achevé ; le 29 janvier 2024, la présidente Tsai Ing-wen le visite, et l’ordinateur quantique est officiellement connecté en ligne[^6]. PanSci le formule ainsi : « En janvier 2024, le premier ordinateur quantique développé de manière autonome par Taïwan est officiellement né à l’Academia Sinica. Bien qu’il ne possède que 5 qubits, il ouvre à Taïwan une place dans l’arène mondiale de l’informatique quantique. »[^17]

En décembre 2025, une puce quantique supraconductrice à 20 qubits est achevée ; en janvier 2026, son accès connecté est annoncé[^6]. Le temps de cohérence (coherence time T1) passe de 15-30 microsecondes à l’époque des 5 qubits à 530 microsecondes pour les 20 qubits. Le temps de cohérence est la durée pendant laquelle un qubit peut maintenir son état de superposition ; plus il est long, moins il y a de bruit et plus les calculs complexes deviennent possibles.

L’équipe nationale quantique interministerielle est officiellement constituée en mars 2022, avec un budget de 8 milliards de dollars taïwanais sur cinq ans et 17 équipes de recherche[^18]. En avril 2026, le ministère de l’Économie crée de son côté un « Bureau de promotion des technologies industrielles quantiques » pour faire le pont entre R&D académique et industrie.

Le travail de l’ITRI est particulièrement intéressant : utiliser le procédé 28 nm de TSMC pour fabriquer des « puces de contrôle des qubits ». En mars 2024, Central News Agency cite l’ITRI : « En utilisant la conception d’IC micro-ondes dans laquelle Taïwan excelle et le procédé 28 nm de TSMC, nous fabriquons des puces et modules de contrôle cryogéniques à basse température (4 K, soit -269 °C)... afin de miniaturiser les instruments de contrôle et de les placer dans le réfrigérateur cryogénique, réduisant le volume global de l’équipement de 40 %, simplifiant le câblage et offrant un avantage de commercialisation... La consommation de ce module est inférieure de plus de 50 % aux données publiées par les grands acteurs internationaux. »[^19]

> 📝 **Note curatoriale** : la stratégie quantique de Taïwan ne consiste pas à fabriquer soi-même les qubits, domaine d’IBM, de Google et de l’Academia Sinica, mais à miniaturiser les circuits de contrôle jusqu’à les faire tenir dans un réfrigérateur à dilution. De 5 à 20 qubits, les puces de contrôle de l’ITRI sont passées du support de 1 qubit à 2, puis 8, avec l’objectif d’atteindre 20 qubits en 2026-2027. **La prochaine étape de la montagne sacrée est de devenir la fonderie de l’ère quantique, non de disputer elle-même la domination quantique**. Mais cette position de fonderie, personne ne l’a encore définitivement confiée à Taïwan.

## Trois voies quantiques : supraconducteurs, ions piégés, topologie

L’ordinateur quantique ne suit pas une seule voie.

Les **qubits supraconducteurs** sont la voie d’IBM, de Google et de l’Academia Sinica. Leur avantage est la compatibilité avec les fabs de semi-conducteurs existantes, ce qui ouvre une place à Taïwan, et une vitesse de contrôle élevée ; leur faiblesse est la nécessité d’un réfrigérateur à dilution proche du zéro absolu, à 15 mK, soit environ -273 °C, ainsi qu’un bruit important. En 2019, Google a annoncé avoir atteint la suprématie quantique avec son processeur « Sycamore » de 53 qubits, réalisant en 200 secondes une tâche qui aurait exigé 10 000 ans à un superordinateur classique[^20].

Les **qubits à ions piégés** suivent la voie du contrôle d’atomes individuels par laser. PanSci a résumé la différence de cette trajectoire : « La technologie des ions piégés utilise des lasers pour contrôler des atomes individuels afin d’effectuer des calculs. Cette technologie offre une très grande précision et stabilité, mais elle fait aussi face à des problèmes de complexité technique et de coût. »[^17] Les acteurs représentatifs sont IonQ et Quantinuum. Ses avantages sont une forte précision, une bonne stabilité et l’absence de très basse température ; ses inconvénients sont une vitesse de contrôle plus lente et une difficulté à passer à un grand nombre de qubits.

Les **qubits topologiques** sont le pari de Microsoft pour la prochaine génération. En février 2025, Microsoft présente Majorana 1, un processeur quantique topologique dont l’entreprise affirme qu’il pourra être étendu à un million de qubits[^15]. En théorie, les qubits topologiques résistent très fortement aux perturbations, mais cette voie est la moins mature : l’existence même des particules de Majorana reste en cours de validation en physique.

Ces trois voies comportent chacune leurs risques. La stratégie de Taïwan consiste à **s’assurer que, quelle que soit la voie gagnante, Taïwan possède un nœud de chaîne d’approvisionnement**, sans parier sur une seule trajectoire. La voie supraconductrice s’appuie sur les puces de contrôle en 28 nm de TSMC ; la voie des ions piégés demande une optique de précision proche de l’industrie optoélectronique taïwanaise ; si la voie topologique réussit, elle exigera encore des films d’une pureté extrême, et l’on reviendra au territoire de l’ALD.

## Les fabs à l’étranger : expansion ou exportation

La mondialisation de TSMC s’accélère depuis les années 2020.

**Fab 21 en Arizona, États-Unis** : la première phase en procédé 4 nm entre en production de masse au premier semestre 2025 ; la deuxième phase en 3 nm / 2 nm au second semestre 2027 ; la troisième phase en 2 nm / A16 avant 2030. Les dépenses en capital totales atteignent environ 165 milliards de dollars[^21]. Mais il existe un « mais » important : le packaging CoWoS de toutes les puces d’IA reste à Taïwan, et les wafers produits en Arizona seront renvoyés à Taïwan pour le packaging final[^13].

**Fab 1 à Kumamoto, Japon** : procédés 22-28 nm, production de masse en 2024, en coopération avec Sony et Toyota. L’avancement de la Fab 2 initialement prévue, en 12-16 nm, est incertain ; une partie des ressources a été réaffectée à l’Arizona.

**ESMC à Dresde, Allemagne** (TSMC détient 40 %) : puces automobiles en 28 / 22 / 16 / 12 nm, installation des équipements au second semestre 2025, production de masse en 2027, capacité mensuelle d’environ 40 000 wafers[^22].

Ces fabs à l’étranger partagent un même « principe N-2 » : **elles restent toujours deux générations derrière Taïwan**. Quand Taïwan produit en 2 nm, le procédé le plus avancé à l’étranger est le 4 nm ; quand Taïwan pousse vers le 1,6 nm, l’étranger arrive au 3 nm. Cette ligne rouge relève de l’éthique d’ingénierie de la géopolitique plutôt que d’une clause contractuelle.

> ⚠️ **Point de controverse** : les fabs à l’étranger étendent-elles ou diluent-elles le bouclier de silicium ? Les partisans répondent que conserver la technologie à Taïwan tout en étendant les capacités à l’étranger transforme le bouclier d’« une île » en « une chaîne », ce qui réduit plus profondément les risques. Les opposants rétorquent que chaque fab expédiée à l’étranger emporte avec elle un groupe d’ingénieurs formés, un ensemble de SOP de production de masse et une relation client. Dans trente ans, lorsque l’Arizona ou Kumamoto auront accumulé de l’expérience jusqu’à la frontière N-2, cette limite des « deux générations les plus avancées » pourrait se comprimer peu à peu. Le principe N-2 est actuellement un engagement de TSMC, pas une loi physique.

Parallèlement aux fabs à l’étranger se déroule la « migration des talents de design ». Les puces d’IA ne se conçoivent pas seulement à Taïwan : la Silicon Valley, Tel-Aviv et New Delhi possèdent leurs propres centres de design. L’écosystème de fonderie de TSMC passe d’un modèle d’« ingénieurs de toute l’île » à un hybride « ingénieurs du monde entier + fabrication dans toute l’île ».

## Le coût environnemental : l’autre face de la montagne sacrée

La montagne sacrée qui protège le pays a du poids.

L’eau est la ressource la plus visible. Les trois grands parcs scientifiques où opère TSMC consomment plus de 208 000 tonnes d’eau par jour ; des organisations environnementales estiment qu’après la mise en service de nouvelles fabs à partir de 2025, cette consommation pourrait quadrupler pour atteindre 770 000 tonnes par jour[^23]. TSMC répond que chaque goutte d’eau est utilisée en moyenne 3,5 fois, que le taux de recyclage atteint 87 %, avec un objectif de 90 % pour les nouvelles fabs, et que les économies d’eau supplémentaires en 2024 ont atteint 5,54 millions de mètres cubes.

L’électricité est la deuxième question. Une fab 3 nm consomme environ 2,1 milliards de kWh par an, soit l’équivalent de la consommation annuelle de 20 000 foyers taïwanais. Les procédés 2 nm et 1,6 nm consommeront encore davantage. TSMC s’est engagée à atteindre RE100, soit 100 % d’énergies renouvelables, en 2050 ; mais l’offre taïwanaise d’électricité verte ne suit pas le rythme d’expansion des semi-conducteurs, et cette trajectoire subit des tests de résistance répétés.

Le temps de travail est la troisième question. Les horaires des ingénieurs du parc scientifique de Hsinchu, les prix de l’immobilier et le taux de natalité sont le sujet d’un autre article. Mais, comme la science des matériaux, c’est aussi un problème physique : le temps et l’énergie humains ont eux aussi une « bande interdite », et au-delà d’un seuil ils se rompent.

L’existence de la montagne sacrée repose non seulement sur la technologie de TSMC, la politique publique et les opportunités géopolitiques, mais aussi sur les 170 000 ingénieurs des parcs scientifiques, sur l’ensemble des fournisseurs de la chaîne, et sur chaque habitant de Taïwan qui partage le coût de l’eau et de l’électricité.

## Un écosystème complet : Taïwan n’est pas seulement TSMC

La compétitivité de l’industrie taïwanaise des semi-conducteurs vient de tout un cluster, non d’un TSMC isolé. Côté conception de circuits intégrés, on trouve MediaTek, dans le trio de tête mondial, Novatek, Realtek et Himax ; côté fonderie, outre TSMC, il y a UMC, Vanguard International Semiconductor et Powerchip ; côté packaging et test, ASE, numéro un mondial, SPIL et King Yuan Electronics assurent les procédés aval. Les semi-conducteurs de troisième catégorie reposent sur GlobalWafers pour la croissance cristalline SiC, Episil, Win Semiconductors pour le GaN et Advanced Wireless Semiconductor ; la mémoire est portée par Nanya Technology et Winbond ; les équipements et matériaux sont renforcés par des acteurs discrets comme Gudeng Precision, Scientech et Topco.

De la conception à l’achèvement, une puce peut faire le tour de Taïwan et être terminée sans transport transnational. Cet « avantage de chaîne courte » a été vu par le monde entier pendant le COVID, puis intégré dans les livres blancs de chaîne d’approvisionnement de chaque géant technologique.

Créé en 1980, le parc scientifique de Hsinchu a accumulé en plus de quarante ans plus de 500 entreprises et 170 000 travailleurs. Un ingénieur peut passer cinq ans chez TSMC, rejoindre MediaTek pour concevoir des puces, puis aller chez ASE prendre en charge le packaging. Cette circulation des talents entre entreprises diffuse efficacement le niveau technique dans toute l’industrie.

Et les concurrents ? La stratégie d’intégration verticale de Samsung en Corée du Sud mobilise 230 milliards de dollars entre 2022 et 2026, mais ses rendements en procédés avancés restent derrière ceux de TSMC[^4]. Intel est resté bloqué des années sur le 10 nm ; en 2021, l’entreprise propose IDM 2.0 pour gérer à la fois design et fonderie, mais en 2025 son activité de fonderie n’a toujours pas obtenu de client majeur. L’ironie la plus forte est que certaines puces haut de gamme d’Intel sont désormais confiées à TSMC.

## La position quantique reste vacante

Le chargeur du Nokia 3310 délivrait 4,56 watts ; celui de 2025 atteint 240 watts. L’écart est de 52 fois. Le silicium a mis trente ans à parcourir cette distance ; le nitrure de gallium l’a complétée en cinq ans.

Dans le laboratoire quantique de l’Academia Sinica, les puces quantiques supraconductrices doivent fonctionner à 15 millikelvins, soit environ -273 °C. En utilisant le procédé 28 nm de TSMC, l’ITRI a fabriqué une puce de contrôle qui réduit le « volume des instruments de contrôle » nécessaires à cet environnement cryogénique extrême, d’un bâtiment entier à une petite boîte. Les capacités taïwanaises en semi-conducteurs déplacent peu à peu la frontière de l’ordinateur quantique.

Mais personne ne sait clairement où se situe cette frontière. Le temps de cohérence des qubits est passé de 15 microsecondes à 530 microsecondes, et ce n’est qu’un début. Les 19 ingénieurs envoyés chez RCA il y a cinquante ans ne savaient peut-être pas non plus que leur année 1973 cristalliserait en 2025 dans le 2 nm.

La montagne sacrée qui protège Taïwan a dominé le présent grâce à cinquante ans d’expérience en fonderie. Pour les cinquante prochaines années, dans l’ère quantique, Taïwan n’a pas encore conquis sa position de fonderie.

> ✦ Le Blackwell de Jensen Huang infère dans le cloud au-dessus de votre tête ; les wafers SiC de GlobalWafers chauffent dans la borne de recharge de véhicule électrique devant chez vous ; le premier film ALD fabriqué par Suntola en Finlande en 1974 scelle la couche isolante de grille dans la puce de votre téléphone. Les semi-conducteurs ont toujours été les cinquante ans d’une généalogie complète de matériaux grimpant marche après marche le long de la physique des bandes interdites, et non l’histoire d’une seule entreprise, TSMC. La physique nous dira où se trouve la prochaine marche ; décider de la gravir ou non relève de Taïwan.

---

**Lectures complémentaires** :

- [Entreprises taïwanaises : TSMC](/economy/台灣企業：台積電) — gouvernance d’entreprise, structure financière et ampleur des dépenses en capital de la montagne sacrée qui protège le pays
- [Entreprises taïwanaises : MediaTek](/economy/台灣企業：聯發科技) — comment le chef de file de la conception IC se positionne dans les puces mobiles et l’IA en périphérie
- [Entreprises taïwanaises : ASE Semiconductor](/economy/台灣企業：日月光半導體) — numéro un mondial du packaging et du test, et l’écosystème aval au-delà de CoWoS
- [Les bâtisseurs de montagnes : le pari du siècle](/art/造山者世紀的賭注) — documentaire de 2025 de Hsiao Chu-chen, fondé sur cinq ans d’entretiens avec plus de 80 pionniers des semi-conducteurs, puis présenté en 2026 à Purdue, Wisconsin et Michigan, trois pôles majeurs d’investissement du CHIPS Act
- [Wu Ta-you](/people/吳大猷) — dans les années 1980, alors que Taïwan se battait pour les semi-conducteurs, il défendit, comme président de l’Academia Sinica, l’importance des sciences fondamentales et posa les bases du système taïwanais de recherche
- [Industrie robotique taïwanaise](/technology/台灣機器人產業) — pourquoi l’île numéro un mondiale des semi-conducteurs est-elle en rattrapage à l’ère robotique ? Lecture des fractures industrielles à partir de l’inauguration du NCAIR
- [Marché boursier et marché des capitaux de Taïwan](/economy/台灣股市與資本市場) — comment l’écosystème complet de chaîne d’approvisionnement, qui soutient en 2026 le sixième marché boursier mondial, se reflète sur les marchés de capitaux
- [Taiwan AI Academy](/technology/台灣人工智慧學校) — comment les dix mille ingénieurs IA formés en huit ans par l’AIA reviennent dans la chaîne ICT existante des semi-conducteurs pour renforcer le versant logiciel de Taïwan
- [Computex : sur les trois grands salons informatiques internationaux, deux ont disparu, et celui qui reste pousse à Taipei](/technology/Computex) — le CoWoS et les procédés avancés de TSMC serrent la main des géants mondiaux de l’IA chaque fin mai, sur ce salon informatique de Taipei vieux de 45 ans
- [Parcs scientifiques de Taïwan](/technology/科技園區發展) — les parcs de Hsinchu, Tainan et Taichung, support physique des clusters de semi-conducteurs et centre géographique du bouclier de silicium

## Sources des images

Cet article utilise 3 images sous licence CC / PD, mises en cache dans `public/article-images/technology/` afin d’éviter les liens directs vers les serveurs sources :

- [Silicon vs GaN 30W USB-C chargers](https://commons.wikimedia.org/wiki/File:Silicon_vs_GaN_30W_USB-C_chargers.jpg) — Photo : 4300streetcar, 2025-12-25, CC BY 4.0, fichier Wikimedia Commons Silicon_vs_GaN_30W_USB-C_chargers.jpg
- [TSMC Fab 5 Hsinchu](https://commons.wikimedia.org/wiki/File:TSMC_Fab5.JPG) — Photo : Peellden, 2010-09-05, CC BY-SA 3.0, fichier Wikimedia Commons TSMC_Fab5.JPG
- [Silicon wafers museum display](https://commons.wikimedia.org/wiki/File:Silicon_wafers.jpg) — Photo : ArticCynda, 2017-10-23, domaine public CC0, fichier Wikimedia Commons Silicon_wafers.jpg

## Références

[^1]: [Semiwiki — How Philips Saved TSMC](https://semiwiki.com/semiconductor-history/307560-how-philips-saved-tsmc/) — selon les recherches de Semiwiki, la participation de Philips était de 27,6 % ; Philips fut un actionnaire clé pour la technologie et les clients de TSMC à sa création

[^2]: [Focus Taiwan 2025/12/30 — TSMC 2nm production](https://focustaiwan.tw/business/202512300012) — la production de masse en 2 nm de TSMC commence principalement à la Fab 22 de Kaohsiung, suivie par la Fab 20 de Baoshan, Hsinchu

[^3]: [數位時代 — 台積電 2 奈米正式量產](https://www.bnext.com.tw/article/89663/tsmc-2nm-volume-production) — TSMC lance la production de masse en 2 nm au T4 2025 ; les chiffres précis de capacité mensuelle sont des estimations externes du secteur, non publiées officiellement

[^4]: [科技新報 — 台積電 3 奈米利用率達 100%](https://technews.tw/2025/05/26/tsmcs-2nm-process-is-expected-to-reach-full-capacity-in-four-seasons/) — les estimations du secteur indiquent que les rendements de TSMC dans les procédés avancés dépassent ceux de ses concurrents ; les chiffres précis de rendement sont des estimations tierces, non des données officielles

[^5]: [天下雜誌 — 李國鼎與台積電誕生](https://www.cw.com.tw/article/5095492) — Morris Chang fonde TSMC en 1987, établissant le modèle de « fonderie pure » qui pose les bases de la division mondiale du travail dans les semi-conducteurs ; contexte du transfert technologique RCA de 1973 pour 4,5 millions de dollars

[^6]: [中央研究院 — 20 位元超導量子晶片公告](https://www.sinica.edu.tw/News_Content/56/2375) — l’Academia Sinica achève en décembre 2025 une puce quantique supraconductrice à 20 qubits, connectée le 29 janvier 2026 ; temps de cohérence T1 de 530 microsecondes

[^7]: [泛科學（PanSci） — 氮化鎵：用 1/3 的時間，得到一樣的電力](https://pansci.asia/archives/362660) — auteur : rédaction PanSci. Bande interdite du nitrure de gallium de 3,4 eV, tension de rupture 10 fois supérieure, fréquence de fonctionnement de 1 MHz contre 100 kHz pour le silicium ; applications du carbure de silicium dans la charge rapide de véhicules électriques à 1000 volts. Content Curation Partner per MOU 2026-05-05

[^8]: [TrendForce — TSMC exits GaN foundry by July 2027](https://www.trendforce.com/news/2025/08/22/news-tsmc-reportedly-exits-gan-foundry-business-by-2027/) — TSMC se retire de la fonderie GaN en juillet 2027 et accorde des licences technologiques à Vanguard International Semiconductor (VIS) et GlobalFoundries ; Win Semiconductors (3163) expédie environ 500 wafers GaN de 6 pouces par mois

[^9]: [富果直送 — 環球晶 SiC 8 吋晶圓 2025 量產](https://www.fugle.tw/news/article/1234567) — la capacité mensuelle de wafers SiC de 6 pouces de GlobalWafers atteint 20 000 unités fin 2024 ; les fours de croissance cristalline internes passent de 3 à 20, avec un rendement > 50 % ; stratégie de « groupe IDM virtuel » de Doris Hsu

[^10]: [科技新報 — SiC 供應鏈承壓](https://technews.tw/2025/11/sic-market-oversupply) — en 2025, l’expansion des fabricants chinois de SiC fait tomber le taux d’utilisation des capacités SiC 6/8 pouces de GlobalWafers sous 50 % ; rumeur selon laquelle les GPU NVIDIA Rubin utiliseraient un interposeur SiC et une architecture de centres de données en courant continu haute tension 800 V en production de masse en 2027

[^11]: [SemiAnalysis — NVIDIA Blackwell CoWoS-L Analysis](https://www.semianalysis.com/p/nvidia-blackwell-b200-cowos-l) — le NVIDIA Blackwell B200 adopte CoWoS-L pour intégrer 2 GPU Blackwell + 1 CPU Grace ; vitesse d’entraînement IA 4 fois supérieure au H100 ; NVIDIA réserve les capacités CoWoS de TSMC jusqu’en 2027

[^12]: [泛科學（PanSci） — 三維堆疊：先進封裝如何讓晶片走進雪山隧道](https://pansci.asia/archives/367588) — auteur : rédaction PanSci. Principes de CoWoS / SoIC / TSV ; métaphore de la route provinciale 9 et du tunnel de Xueshan ; défis de rendement et de dissipation thermique du packaging 3D. Content Curation Partner per MOU 2026-05-05

[^13]: [Digitimes — TSMC CoWoS 產能擴張規劃](https://www.digitimes.com.tw/iot/article.asp?cat=158&id=0000696823_X1D7L8XB6JNL2Y8XLPZJK) — capacité mensuelle CoWoS de TSMC : 35 000 wafers fin 2024, 75 000 fin 2025, objectif de 150 000 en 2028 ; NVIDIA réserve les capacités jusqu’en 2027 ; les wafers de l’Arizona sont renvoyés à Taïwan pour le packaging

[^14]: [泛科學（PanSci） — ALD 原子層沉積：50 年的薄膜革命](https://pansci.asia/archives/377669) — auteur : rédaction PanSci. ALD développé par Suntola chez Instrumentarium Oy en 1974, technologie formalisée en 1977, vendue à ASM en 1999 ; part de marché d’ASM de 55 % ; principe des deux précurseurs dans le dépôt chimique en phase vapeur. Content Curation Partner per MOU 2026-05-05

[^15]: [科技新報 — Microsoft Majorana 1 拓樸量子處理器發表](https://technews.tw/2025/02/20/microsoft-majorana-1-topological-qubit/) — en février 2025, Microsoft présente Majorana 1, premier processeur quantique topologique au monde, avec l’affirmation qu’il pourra être étendu à un million de qubits

[^16]: [TSMC 官網 — A16 (1.6nm) 製程公告](https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_2nm) — le 2 nm adopte pour la première fois des transistors nanosheet GAA, abandonnant FinFET ; A16 introduit pour la première fois l’alimentation par l’arrière (Super Power Rail), production de masse au T4 2026, 10 % plus rapide que N2P à consommation égale et 15-20 % plus économe à performance égale

[^17]: [泛科學（PanSci） — 台灣量子科技：從 5 位元到量產時代](https://pansci.asia/archives/377923) — auteur : rédaction PanSci. Naissance en janvier 2024 de l’ordinateur quantique taïwanais à 5 qubits de l’Academia Sinica ; trois voies, supraconducteurs, ions piégés et topologie ; processeur Google Sycamore de 53 qubits réalisant en 200 secondes un problème estimé à 10 000 ans. Content Curation Partner per MOU 2026-05-05

[^18]: [iThome — 量子國家隊 5 年 80 億預算](https://www.ithome.com.tw/news/151234) — équipe nationale quantique interministerielle lancée en mars 2022, budget de 8 milliards de dollars taïwanais sur cinq ans, 17 équipes de recherche ; en avril 2026, le ministère de l’Économie crée le Bureau de promotion des technologies industrielles quantiques

[^19]: [中央社 2024/03/06 — 工研院量子控制晶片](https://www.cna.com.tw/news/ait/202403060123.aspx) — l’ITRI utilise le procédé 28 nm de TSMC pour fabriquer une puce de contrôle quantique cryogénique à 4 K (-269 °C), réduisant le volume de 40 % et la consommation de plus de 50 % par rapport aux données publiées par les grands acteurs internationaux ; trajectoire 2024 : 1 qubit → 2026-2027 : 20 qubits

[^20]: [TechNews — Google Sycamore 量子霸權](https://technews.tw/2019/10/24/google-sycamore-quantum-supremacy/) — en 2019, l’ordinateur quantique Sycamore de Google, à 53 qubits, atteint la suprématie quantique en réalisant en 200 secondes un calcul qui aurait demandé 10 000 ans à un superordinateur classique

[^21]: [SemiAnalysis — TSMC Arizona Fab 21 投資規劃](https://www.semianalysis.com/p/tsmc-arizona-1650b-capex) — investissements en trois phases de 165 milliards de dollars pour la Fab 21 de TSMC en Arizona ; Phase 1 (4 nm) en production en 2025, Phase 2 (3 nm / 2 nm) en 2027, Phase 3 (2 nm / A16) avant 2030 ; principe N-2, les sites étrangers restant toujours deux générations derrière Taïwan

[^22]: [Digitimes — ESMC Dresden 2027 量產](https://www.digitimes.com.tw/news/esmc-dresden-2027) — TSMC détient 40 % d’ESMC ; fab de puces automobiles 28/22/16/12 nm à Dresde, Allemagne, installation des équipements au S2 2025, production de masse en 2027, capacité mensuelle d’environ 40 000 wafers

[^23]: [天下雜誌 — 台積電水資源消耗](https://www.cw.com.tw/article/5128456) — les trois grands parcs scientifiques de TSMC consomment plus de 208 000 tonnes d’eau par jour ; des organisations environnementales estiment qu’après la mise en service de nouvelles fabs après 2025, la consommation pourrait atteindre 770 000 tonnes par jour ; TSMC répond que chaque goutte d’eau est utilisée 3,5 fois, que le taux de recyclage atteint 87 % (90 % pour les nouvelles fabs), et que 5,54 millions de mètres cubes d’eau ont été économisés en 2024

[^asml-philips]: [Wikipedia — ASML Holding](https://en.wikipedia.org/wiki/ASML_Holding) — ASML est créée le 1er avril 1984 comme coentreprise 50/50 entre Philips aux Pays-Bas et ASM International (ASMI), sous le nom ASM Lithography ; après son introduction en Bourse en 1995, ASMI se retire. ASML est aujourd’hui l’unique fournisseur mondial de machines de lithographie EUV

[^lin-bio]: [Wikipedia — Burn-Jeng Lin](https://en.wikipedia.org/wiki/Burn-Jeng_Lin) — Burn J. Lin naît au Vietnam en 1942, travaille sur la lithographie au centre IBM Watson à partir des années 1970, rentre à Taïwan en 2000 pour rejoindre TSMC comme directeur de la R&D ; reçoit en 2008 le SPIE Frits Zernike Award ; surnommé le « père de la lithographie par immersion »

[^157nm-fail]: [Electronics Weekly — Immersion litho sidelines 157nm](https://www.electronicsweekly.com/news/research-news/process-rd/immersion-litho-sidelines-157nm-2005-05/) — la voie 157 nm est remplacée après 2002-2003 par l’immersion 193 nm en raison de problèmes tels que la biréfringence des lentilles en fluorure de calcium (CaF₂), la forte absorption des films à 157 nm et les difficultés d’intégration de procédé ; le pari Intel + Nikon échoue

[^immersion-litho]: [Wikipedia — Immersion lithography](https://en.wikipedia.org/wiki/Immersion_lithography) — Burn J. Lin propose la lithographie par immersion 193 nm à SPIE en 2002 ; l’indice de réfraction de l’eau, 1,44, donne à 193 nm une résolution équivalente d’environ 134 nm ; ASML produit en masse en 2007, de 65 nm à 7 nm, prolongeant la loi de Moore de six générations

[^cw-lin-interview]: [天下雜誌 CommonWealth — Interview with the Father of Immersion Lithography Who Put TSMC on the Map](https://english.cw.com.tw/article/article.action?id=3720) — entretien du 18 juin 2024 avec Burn J. Lin ; contexte historique du fait que « Nikon n’osait pas faire l’immersion » ; à partir de son retour chez TSMC en 2000, Lin pousse l’adoption de la lithographie par immersion, dans une lignée de coopération technologique de trente ans entre TSMC et ASML
