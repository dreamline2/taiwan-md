---
title: '台湾の人工知能発展と未来戦略：ハードウェアの入場券は手に入れた、次の戦いはどこにあるのか'
description: '2024 年 10 月 8 日、ノーベル物理学賞は Hopfield と Hinton に授与され、翌日の化学賞は AlphaFold の 3 人に授与されました。同年 5 月 29 日、黄仁勲は台北の寧夏夜市（ナイトマーケット）で張忠謀と蚵仔煎（牡蠣オムレツ）を食べました。台湾は世界の AI サーバーの 90%、先端ウェハーの 72% を製造していますが、42 年にわたるニューラルネットワークと 50 年にわたるタンパク質フォールディング難題の解答には不在でした。PTT 創設者の杜奕瑾による Taiwan AI Labs から、国家科学及技術委員会が注力する繁体字中国語 LLM モデル TAIDE まで、この島は受託製造工場でいるだけで十分なのでしょうか。'
date: 2026-03-19
author: 'Taiwan.md 編輯組'
category: 'Technology'
subcategory: '人工智慧'
tags:
  [
    '人工知能',
    'AI',
    '半導体',
    '科学技術政策',
    'デジタルトランスフォーメーション',
    'ノーベル賞',
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
translatedAt: '2026-06-16T16:55:14Z'
image: '/article-images/technology/alphafold-cbln1-structure-2025.webp'
imageCredit: 'BQUB25-UPoch (own work, AlphaFold + PyMOL)'
imageLicense: 'CC BY 4.0'
imageSource: 'https://commons.wikimedia.org/wiki/File:Estructura_tridimensional_de_la_prote%C3%AFna_CBLN1_per_AlphaFold_amb_codificaci%C3%B3_rainbow.png'
---

# 台湾の人工知能発展と未来戦略：ハードウェアの入場券は手に入れた、次の戦いはどこにあるのか

> **30 秒概観：** 2024 年 10 月 8 日、ノーベル物理学賞は Hopfield Network を書いた物理学者と、backpropagation を書いた認知科学者に授与されました[^N1]。翌 10 月 9 日、ノーベル化学賞は、AI を用いて 50 年にわたるタンパク質フォールディング難題を解いた 3 人の研究者に授与されました[^N2]。同年 5 月 29 日、NVIDIA CEO の黄仁勲は台北の寧夏夜市（ナイトマーケット）に現れ、張忠謀、林百里、蔡力行と蚵仔煎（牡蠣オムレツ）を食べました。TSMC は世界のファウンドリー市場収益の 72% を獲得し、鴻海、広達、緯創は合計で世界の AI サーバーの 9 割を生産しています。しかし、2 日連続で発表され、42 年にわたるニューラルネットワークの歴史に正当性を補ったこの科学的儀式の中に、台湾出身の名前は一つもありませんでした。PTT 創設者の杜奕瑾が設立した Taiwan AI Labs から、政府が注力する繁体字中国語の大規模言語モデル TAIDE まで、「AI を製造する」ことから「AI になる」ことへの賭けが進行しています。

---

## 42 年の承認：2024 年ノーベル賞の 2 日連続発表

2024 年 10 月 8 日午前、ストックホルム。スウェーデン王立科学アカデミーは、その年のノーベル物理学賞を 2 人の AI 科学者に授与すると発表しました。91 歳のプリンストン名誉教授 John J. Hopfield と、76 歳で 5 か月前に Google を退職したばかりの Geoffrey Hinton です。賞金は 1,100 万スウェーデン・クローナで、2 人が均等に分け合いました[^N1]。

選考委員会が示した授賞理由は、「人工ニューラルネットワークによる機械学習を可能にする基礎的発見と発明」（for foundational discoveries and inventions that enable machine learning with artificial neural networks）でした[^N1]。これはノーベル物理学賞の歴史上、ニューラルネットワークという領域に直接賞が与えられた初めての事例です。

翌日、10 月 9 日は化学賞でした。受賞者は 3 人。ワシントン大学の David Baker に加え、DeepMind の Demis Hassabis と John Jumper です。Baker が賞金の半分を受け取り、Hassabis と Jumper が残りの半分を共有しました[^N2]。授賞理由は 2 つに分かれ、前半は Baker の「計算によるタンパク質設計」、後半は Hassabis と Jumper の「タンパク質構造予測」でした。

2 日間、2 つのノーベル賞、そのすべてが AI に関係していました。ノーベル賞の歴史上、前例のないことです。

時間軸で照らし合わせてみます。Hopfield が 1982 年に『米国科学アカデミー紀要』（PNAS）で「Neural networks and physical systems with emergent collective computational abilities」という論文を発表した時、彼は凝縮系物理から神経科学へ足を踏み入れたばかりでした[^N3]。1982 年から 2024 年まで、丸 42 年です。Hinton と Rumelhart が backpropagation アルゴリズムを実用的な道具としてまとめた 1986 年の論文[^N4]も、発表から受賞まで 38 年かかりました。AlphaFold は 2018 年の CASP13 で初めて登場してから 2024 年のノーベル賞まで、わずか 6 年でした。

結局のところ、この 2 日間のノーベル賞が授与した対象は ChatGPT ではなく、30 年、40 年前に誰にもよく理解されなかった数本の論文でした。基礎研究と産業応用の時差は、常にこのようなものです。

![Geoffrey E. Hinton が 2024 年 12 月 8 日にストックホルムのノーベル・ウィークで取材を受けた公式ポートレート、濃色のスーツ、白髪、カメラに向かって穏やかな表情](/article-images/technology/hinton-nobel-2024.webp)
_Geoffrey Hinton、2024 年ノーベル物理学賞受賞者、ストックホルムのノーベル・ウィーク。Photo: Arthur Petron, 2024-12-08. [CC BY-SA 4.0 via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Geoffrey_E._Hinton,_2024_Nobel_Prize_Laureate_in_Physics_(3x4*cropped).jpg).*

---

## 寧夏夜市での兆元級会食

2024 年 5 月 29 日夕方、Computex 開幕前夜の台北・寧夏夜市に、珍しい一行の食客が現れました。NVIDIA CEO の黄仁勲が、TSMC 創業者の張忠謀、広達董事長の林百里、MediaTek CEO の蔡力行を連れ、屋台の前に身を寄せて蚵仔煎（牡蠣オムレツ）を食べていたのです[^1]。通行人が黄仁勲に気づくと、瞬く間にファンと記者に囲まれ、スターを追いかけるような光景になりました。

この一食に集まった企業価値を合計すれば、数兆米ドルを超えます。しかし本当の物語は食卓の上ではなく、その背後にある産業チェーンにありました。この数人が代表する企業は、世界の AI 計算を支える物理的基盤を担っています。黄仁勲はその台湾訪問中、公の場で「台湾は世界で最も重要な国の一つだ」と述べました[^2]。これは社交辞令ではありません。台湾がなければ、AI 革命のハードウェア基盤は存在しません。

黄仁勲は 1963 年に台北で生まれ、幼少期を台南で過ごし、9 歳で米国へ移住しました[^3]。彼が 1993 年に共同創業した NVIDIA は、現在では AI チップの代名詞です。NVIDIA が設計する先端 GPU は、ChatGPT の訓練に使われた A100、H100 から最新の Blackwell シリーズまで、すべて TSMC に製造を委託しています[^4]。

4 か月後にストックホルムで発表された 2 つのノーベル賞の受賞者名簿には、この会食と関係する名前は一つもありませんでした。この落差は偶然ではなく、構造的な事実です。

---

## ハードウェア：AI 革命全体を支える一つの島

AI ハードウェア供給網における台湾の地位は、「重要」という言葉では軽すぎます。

チップ製造の領域では、2025 年に TSMC が世界のファウンドリー市場で収益シェア 72% を獲得しました[^5]。最先端の 7 ナノメートル以下のプロセスでは、TSMC の市場シェアは 9 割を超えています。NVIDIA の AI GPU 市場シェアは約 86% であり、これらの GPU はほぼすべて TSMC が受託製造しています[^6]。世界中で AI モデルの訓練と運用に使われる計算力の大部分は、台湾のクリーンルームで生まれています。

チップが完成した後は、データセンターに入るサーバーへ組み立てる必要があります。この工程も台湾が主導しています。鴻海、広達、緯創の 3 大 ODM メーカーは、合計で世界の AI サーバーの約 9 割を生産しています[^7]。2025 年、これら 3 社の年間売上高はいずれも 1 兆台湾ドル（約 320 億米ドル）を突破し、そのうち AI サーバー収益は第 2 四半期に初めて消費者向け電子製品を上回りました[^8]。

AI チップの性能は、プロセスの微細化だけでなく、パッケージング技術にも左右されます。TSMC の CoWoS（Chip on Wafer on Substrate）先端パッケージング技術は、NVIDIA の高性能 GPU が性能目標を達成するための鍵です。2026 年には、NVIDIA 1 社だけで CoWoS ウェハー需要が 59.5 万枚に達すると予測され、世界総需要の 60% を占めます[^9]。

鴻海はさらに NVIDIA および台湾政府と協力し、高雄に 100 メガワット（MW）級の AI ファクトリー・スーパーコンピューターを建設し、最新の NVIDIA Blackwell アーキテクチャを採用します[^10]。台湾は「AI チップを製造する場所」から「AI を稼働させる場所」へと移行しつつあります。

![TSMC 新竹サイエンスパーク Fab 5 工場の外観、2010 年代の様子、半導体ファウンドリー製造の物理的現場](/article-images/technology/tsmc-fab5-hsinchu-2010.webp)
_TSMC 新竹 Fab 5 工場、AI チップ受託製造の物理的現場。Photo: Wikimedia Commons via [TSMC Fab 5 file](https://commons.wikimedia.org/wiki/File:TSMC_Fab_5.jpg)._

問題は、ハードウェアで入場券を手に入れた後、次の戦いがどこにあるのかです。

> 📝 **キュレーター・ノート**
>
> 一般的な語り方は「台湾の護国神山が AI 革命を支えている」というものです。この表現は物語として扱いやすい一方で、因果関係の半分を取り違えています。AI 革命が GPU を必要としたから TSMC が選ばれたのであって、TSMC が AI 革命によって生まれたわけではありません。本当の緊張は、GPU が商品化した時、次段階の価値がどこへ移るのかにあります。2024 年の 2 つのノーベル賞が示した答えは、モデルそのものです。Hopfield が書いたあの 12 ページ、Hinton と学生の Krizhevsky が 2012 年に AlexNet によって ImageNet 画像認識の誤り率を 26.2% から 15.3% へ引き下げたあの夜[^N5]、そして Hassabis らが AlphaFold で CASP14 の中央値 GDT 92.4 を達成したあの午後です。

---

## Hopfield 1982：物理学者が書いた記憶モデル

1982 年、プリンストンの凝縮系物理学者 John Hopfield は、わずか 12 ページの論文を書きました。題名は長く、「Neural networks and physical systems with emergent collective computational abilities」で、『米国科学アカデミー紀要』に掲載されました[^N3]。

彼が行ったことは、本質的には「記憶」を物理に翻訳することでした。

物理学には spin glass（スピングラス）という概念があります。多数の磁性原子がそれぞれスピン方向を持ち、互いに相互作用し、系全体が自発的にエネルギー最小点を見つけます。Hopfield はこの概念をニューロンに移植しました。ニューロンを spin と見なし、結合強度を相互作用と見なし、ネットワーク全体が自発的にある「エネルギー最小値」（energy minimum）の安定状態へ収束すると考えたのです[^N3]。一つ一つの energy minimum が、保存された記憶に相当します。

このモデルの優雅さは、記憶を物理の言語で記述できるものにした点にあります。不完全な手がかりを与えられると、ネットワークは自ら最も近いエネルギー最小点を見つけ、記憶全体を補完します。これは、後の生成 AI が行っていることの数学的祖先です。

1982 年当時の台湾では、電子産業がようやく立ち上がり始めたところで、TSMC はまだ設立されていませんでした。張忠謀が、42 年後に「護国神山」と呼ばれる企業を創業するのは 1987 年のことです。Hopfield の論文の Google Scholar における引用回数は、2026 年までに 2 万 7 千回以上に達しています[^N6]。

さらに興味深いのは、Hopfield が後に語った一言です。彼はプリンストンで長年にわたり凝縮系物理を研究し、神経科学へ入ったことは当時の同僚から「余技」のように見られていました。2024 年のノーベル賞受賞者が発表された時、彼は 91 歳でした。スウェーデン王立科学アカデミーの電話インタビューで受賞の感想を尋ねられた彼は、「誰も AI の方向を理解も制御もしていない」ことに不安を感じると述べました[^N7]。

現代 AI 全体の数学的基礎を書いた人物は、受賞したその日に、人々へ少し慎重になるよう促したのです。

![John J. Hopfield が 2024 年 12 月 8 日にストックホルムのノーベル・ウィークで取材を受けたポートレート、濃色のスーツ、白髪、落ち着いた表情](/article-images/technology/hopfield-nobel-2024.webp)
_John J. Hopfield、2024 年ノーベル物理学賞受賞者、ストックホルムのノーベル・ウィーク。Photo: Arthur Petron, 2024-12-08. [CC BY-SA 4.0 via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:John_J._Hopfield,_2024_Nobel_Prize_Laureate_in_Physics_1_(cropped).jpg).\_

---

## Hinton：1986 年の論文と、2023 年に Google を去った警告

1947 年にロンドンのウィンブルドンで生まれた Geoffrey Hinton は、歴史が 38 年遅れてようやく認めたもう一人の人物です[^N8]。

1986 年、Hinton は David Rumelhart、Ronald Williams とともに、『Nature』に backpropagation に関する論文を発表しました[^N4]。このアルゴリズムの意味は、ニューラルネットワークが誤った時に、その誤差信号を各層へ逆方向に伝え、層ごとに結合重みを調整できるというものです。これは今日のすべての深層学習モデルが自分を訓練する方法です。

このアルゴリズムは 1986 年に書かれましたが、爆発的に広がるには 3 つの条件がそろう必要がありました。十分に安価な計算力、十分に大量のデータ、そしてこの道を信じる人々です。前の 2 つは 2010 年代初頭に整い、3 つ目を代表したのが Hinton と、彼の 2 人の学生 Alex Krizhevsky、Ilya Sutskever でした。2012 年、彼らは GPU で訓練した畳み込みニューラルネットワーク AlexNet により、ImageNet 画像認識コンペティションで top-5 誤り率 15.3% を達成し、2 位の 26.2% を大きく引き離しました[^N5]。その瞬間、産業界全体が backpropagation は本当に機能するのだと信じるようになりました。

2013 年 3 月、Google は Hinton の小さな会社 DNNresearch を 4,400 万米ドルで買収し、65 歳の彼を傘下に収めました[^N8]。その後の 10 年間、彼はシリコンバレーで最も権威ある AI 研究者でした。

そして 2023 年 5 月 1 日、『ニューヨーク・タイムズ』が一つのインタビューを掲載しました。Hinton が Google を去ったのです。

退職理由は引退ではありませんでした。彼はインタビューで、「Google への影響を考えずに AI リスクについて自由に語れるようにするため」だと述べました[^N9]。彼が警告したことには、AI システムがまもなく人間より賢くなる可能性、悪意ある人に悪用される可能性、そしてそれを止める方法は「何があるのか見えにくい」ことが含まれていました[^N9]。彼は自分の一生の仕事についてさえ、「一部を後悔している」と語りました[^N9]。

2024 年にノーベル物理学賞が彼に授与された時、彼は電話インタビューでもう一度警告を繰り返しました。AI が制御不能になる可能性に注意すべきだ、という警告です[^N10]。

深層学習の訓練アルゴリズムを書いた人物と、記憶モデルを書いた人物が、2024 年 10 月のその日に同時にスウェーデン王立科学アカデミーの舞台に立ち、このものが想像以上に危険である可能性に注意するよう同時に促したのです。この光景は、1945 年にニューメキシコの砂漠でオッペンハイマーがキノコ雲を見つめた時の表情と、どこか対位法のように響き合います。

その2か月後、2024年12月8日、ヒントンはストックホルム大学の Aula Magna 講堂でノーベル賞講演を行いました。題目は〈Boltzmann Machines〉——ホップフィールドの系譜を引く、熱力学的確率分布をニューラルネットワークに書き込む初期の仕事です。聴き終えると分かります。1986年のバックプロパゲーション論文は孤立した洞察ではなく、1980年代の物理学と認知科学の交差点から育ったひとつの思想体系だったのだと。

<div class="video-embed" style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;margin:1.5rem 0;border-radius:8px;">
  <iframe src="https://www.youtube.com/embed/iCS1ds0UDP8" title="Boltzmann Machines — Nobel Prize lecture by Geoffrey Hinton, Nobel Prize in Physics 2024" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

_スウェーデン王立科学アカデミー公式チャンネル：ジェフリー・ヒントン 2024年12月8日のノーベル物理学賞講演「Boltzmann Machines」。1980年代にセイノフスキーと書いたボルツマン機械から、バックプロパゲーション、そして今日の LLM まで——実に40年。最後の5分、彼はノーベル講壇の上から、改めて AI リスクへの懸念を語りました。_

---

## PTT から AI ラボへ：杜奕瑾の 2 度の起業

台湾という島へ戻りましょう。Hopfield が記憶モデルを書いたのと同じ時期、台湾ではコンピューターサイエンス学科がようやくでき始めたところでした。

1995 年、台湾大学情報工学科 2 年生の杜奕瑾は、486 コンピューター 1 台とオープンソースソフトウェアを用い、寮の中で [PTT](/ja/Technology/ptt-bulletin-board-system/) を立ち上げました。これは後に台湾最大の電子掲示板となりました。30 年後の現在も、PTT には毎日数十万人がオンラインで訪れており、台湾ネット文化の生きた化石です。

杜奕瑾はその後 Microsoft に移り、音声アシスタント Cortana の開発に参加しました。2017 年 4 月、彼はシリコンバレーの高給を捨てて台湾へ戻り、「台湾人工知能実験室」（Taiwan AI Labs）を創設しました。これはアジア初の非営利かつオープンな AI 研究機関です[^11]。

彼の動機は非常に率直でした。台湾には世界級のソフトウェア人材がいるが、そうした人材は皆シリコンバレーへ行ってしまう。帰りたい人、残りたい人が AI 研究を行える場所を作りたい、というものでした。

Taiwan AI Labs の最も有名な製品は「雅婷逐字稿」です。繁体字中国語と台湾アクセントに最適化した音声認識システムです。COVID-19 パンデミック期には、同実験室は偽情報検出ツールと連合学習による医療 AI も開発しました[^12]。これらのプロジェクトに共通しているのは、解決しているのが台湾ローカルの問題であり、使っているのも台湾ローカルのデータであって、米国のモデルを翻訳して使っているのではないという点です。

PTT から AI Labs に至る杜奕瑾の物語は、ある意味で台湾ソフトウェア発展の縮図です。技術能力が不足しているのではなく、人材を残すエコシステムが不足しているのです。

> 💡 **知っていますか**
>
> Hinton が backpropagation を発表した 1986 年、台湾の GDP は約 779 億米ドル、1 人当たり GDP は約 4,007 米ドルで、新竹サイエンスパークは稼働開始からまだ 6 年でした[^N11]。3 つの出来事は同じ地球上で同時に起きていましたが、この歴史線が ImageNet データセット上で交差するまでには、さらに 26 年を要しました。基礎研究の時間尺度は、産業の物語が感じる時間よりも常に長いのです。

---

## AlphaFold：50 年にわたるタンパク質フォールディング難題のもう半分のノーベル賞

2024 年ノーベル化学賞の物語は、1972 年の一つの問題から始まります。

その年、米国の生化学者 Christian Anfinsen はノーベル化学賞受賞講演で、ある仮説を提示しました。タンパク質の三次元折りたたみ構造は、そのアミノ酸配列によって完全に決まる、という仮説です[^N12]。もしこの仮説が成り立つなら、理論上は一本のアミノ酸配列を見ただけで、対応する 3D 構造を計算できるはずです。しかしこの「はず」は半世紀にわたって実現しませんでした。タンパク質フォールディングは grand challenge と呼ばれました。学界は 2 年ごとに CASP コンペティションを開き、参加者が提出した予測結果を実験構造と比較しました。1994 年から 13 回開催されましたが、誰も突破できませんでした[^N13]。

転機は 2018 年の CASP13 でした。DeepMind が初代 AlphaFold を出場させ優勝しましたが、精度はまだ実用水準に達していませんでした。本当の転換点は 2020 年 11 月 30 日の CASP14 です。AlphaFold 2 は中央値 GDT 92.4 という成績を出しました[^N13]。GDT 92.4 とは、予測結果の半分以上で、原子位置と実験値のずれが 1 オングストローム未満であり、実験分解能の水準に達したことを意味します。CASP 主催者の John Moult はその日、「大きな意味で、この問題は解決された」と述べました[^N13]。

50 年解けなかった問題が、6 年のうちにロンドンの研究チームによって解かれたのです。

その後、事態はさらに速く進みました。2021 年 7 月、AlphaFold 2 のソースコードがオープンソース化されました。同年、DeepMind は欧州分子生物学研究所（EMBL-EBI）と協力し、AlphaFold が予測したタンパク質構造を公開データベース化しました。2022 年 7 月、このデータベースは 100 万種、約 2 億個のタンパク質構造をカバーし、地球上のほぼすべての既知タンパク質の 3D モデルを無料で公開したことになります[^N14]。

2024 年 5 月 8 日、DeepMind は『Nature』で AlphaFold 3 を発表し、予測能力を単一タンパク質から、タンパク質と DNA、RNA、リガンド（ligand）、イオンの相互作用へ拡張しました[^N15]。新薬開発、ワクチン設計、酵素工学に至るまで、分子同士がどのように結合するかを知る必要があるすべての領域で、このツールは基盤を書き換えました。

AlphaFold を作った Demis Hassabis は、伝統的な生化学者ではありません。彼は 4 歳でチェスを始め、13 歳でマスターの称号を得ました。17 歳の時には Peter Molyneux とともにシミュレーションゲーム『Theme Park』を共同開発し、数百万本を売り上げました[^N16]。2010 年、彼は Shane Legg、Mustafa Suleyman とともにロンドンで DeepMind を創業し、2014 年に Google が 4 億ポンドで買収しました[^N16]。2016 年に DeepMind の AlphaGo が李世乭を破り、2020 年に AlphaFold 2、2024 年にノーベル賞。この 3 つの出来事の間隔は 10 年未満です。

その中心にある線は同じ賭けです。神経ネットワークを用い、人間が人間の頭脳では解けなかった問題を解くこと。囲碁はルールが閉じた問題であり、タンパク質フォールディングはルールが開いている一方で物理的制約が強い問題です。Hassabis はこの 2 つの戦場をいずれも正しく選びました。

台湾側では、中央研究院院長の翁啓惠の在任期間（2006-2016）に築かれた糖分子タンパク質研究が、台湾でこの最前線に最も近い学術投資でした[^N17]。中央研究院生物医学研究所、生化学研究所にも、AlphaFold のオープンソース重みを用いて下流研究を行うチームがあります。しかし AlphaFold 級の中核モデル開発に対応する制度的基盤は、台湾には現在ありません。

> ⚠️ **論争的視点**
>
> AlphaFold がノーベル化学賞を受賞したことについては、学界で議論がありました。一部の構造生物学者は、この賞は計算ツールを化学の殿堂に引き上げるのではなく、初期の重要な実験を成し遂げた X 線結晶構造解析や核磁気共鳴の研究者に与えるべきだと考えました[^N18]。別の一部は、この議論自体がすでに時代遅れだと考えました。アルゴリズムが 5 年以内に地球上のほぼすべてのタンパク質の 3D 構造を人類のために補完できるなら、それは化学である、という立場です。2024 年 10 月以降、2 つの立場の議論は次第に後者へ傾きましたが、それが示す緊張は消えていません。AI ができることが広がる時、伝統的な学問分野の境界は引き直されるべきなのでしょうか。

---

## TAIDE：台湾はなぜ独自の言語モデルを必要とするのか

2023 年 4 月、ChatGPT が世界を席巻して半年後、台湾の国家科学及技術委員会（国科会）は「TAIDE」計画を開始しました。正式名称は Trustworthy AI Dialogue Engine（信頼できる生成 AI 対話エンジン）です[^13]。

なぜ 2,300 万人の島国が、自ら大規模言語モデルを作る必要があるのでしょうか。

理由は技術的自立だけではありません。繁体字中国語は世界の AI 訓練データの中で比率が極めて低く、中国語データの多くは簡体字中国語サイトに由来します。台湾人が ChatGPT や他のモデルを使う時、得られる回答にはしばしば中国大陸の用語習慣や視点の前提が含まれます。「視頻」ではなく「影片」、「質量」ではなく「品質」。こうした一見細かな違いの背後には、文化主体性の問題があります。『天下雑誌』は TAIDE を「中国 AI の文化侵略を防ぐ」という見出しで直接報じました[^14]。

2024 年 4 月、TAIDE チームは商用版 TAIDE-LX-7B と学術研究版 TAIDE-LX-13B モデルを公開し、文章作成、翻訳、要約などのタスクで良好な性能を示しました[^15]。2026 年には TAIDE 2.0 が発表され、MediaTek が支援する Breeze-8B モデルも加わり、台湾の LLM エコシステムは「追いつく」段階から「使える」段階へ入りました[^16]。

さらに興味深いのは、応用側での広がりです。中興大学は TAIDE を用いて農業知識検索システム「神農 TAIDE」を構築しました。台南大学は台湾語教育向けの台湾語・英語対話ボットを開発しました。陽明交通大学は台湾語版と客家語版の TAIDE モデルを訓練しました[^17]。これらの応用は、言語モデルが技術製品であると同時に文化の担い手でもあることを示しています。「天穿日」や「媽祖遶境」を理解しない AI は、台湾人に本当に奉仕することはできません。

ただし TAIDE の規模はなお小さいものです。商用 8B と学術研究 13B のパラメータ数は、OpenAI の GPT-4 級（推定 1 兆パラメータ超）と比べて 2 桁以上の差があります。この差の背後にあるのは能力の問題ではなく GPU 予算の問題です。最前線級の LLM を訓練するには、億米ドル単位の計算力が必要であり、国家級研究機関の年間予算と同じ桁になります。

---

## ハッキングから生まれた AI サイバーセキュリティ

台湾は、世界で最も頻繁にサイバー攻撃を受ける国の一つです。この不幸な現実は、意外にも強靭な AI サイバーセキュリティ産業を生み出しました。

2017 年末に設立された CyCraft（奧義智慧）は、台湾で初めて AI とエンドポイント監視を組み合わせたサイバーセキュリティ企業です。同社の技術は世界的調査会社 Gartner のレポートに 7 回収録され、台湾で唯一、米国 MITRE ATT&CK の権威ある評価を 3 回通過した企業です[^18]。2026 年 2 月、CyCraft は台湾証券取引所のイノベーションボードに上場し、台湾資本市場で初めて国際級の自主研究開発能力を持つ AI サイバーセキュリティ・ソフトウェア企業となりました[^19]。

CyCraft の顧客には、台湾の政府機関、国防部門、銀行、半導体企業が含まれます。これらはいずれも国家級ハッカーに最も狙われやすい対象です。同社は日本とシンガポールに子会社を置き、「攻撃を受け続けたことで得た実戦経験」をアジア太平洋全域へ輸出しつつあります。

この事例が示すのは、台湾の AI 優位性が半導体だけでなく、特殊な地政学的環境によって鍛えられた実戦能力にも由来するということです。

---

## 政策：「AI 元年」からデジタル発展部へ

台湾の AI 政策発展は、3 つの節目で理解できます。

2017 年から 2018 年は始動段階でした。行政院は 2017 年を「AI 元年」と定め、「AI 小国大戦略」という概念を提示しました。台湾の市場は小さいと認めつつ、半導体製造、ICT 供給網、理工系人材という 3 枚のカードを強調したのです。2018 年には第 1 期「台湾 AI 行動計画」が開始され、4 年で 400 億台湾ドル超を投じ、AI 計算インフラ「台湾 AI クラウド」（TWCC）の整備に重点が置かれました[^20]。

2022 年には制度化へ進みました。デジタル発展部（moda）が設立され、もともと科技部、経済部、交通部に分散していたデジタル関連業務を統合しました。この一歩の意味は、AI 政策が「科技部のプロジェクト」から「省庁横断の国家戦略」へ格上げされた点にあります。同年、政府は「人工知能科学研究発展指針」を発表し、人間中心、透明性と説明可能性、公平性と非差別などの原則を強調しました。

2023 年以降は生成 AI への転換です。ChatGPT の衝撃により、政策は急旋回しました。TAIDE 計画の開始、AI 基本法草案の推進、公的部門への AI 導入加速が起きました。台湾の戦略は非常に現実的です。基礎研究の論文数で米中と競うのではなく、AI を既存の製造業の強みと接続することです。スマート製造、医療画像、半導体歩留まり予測は、台湾がデータ、現場、競争力を持つ領域です。

問題は、2024 年 10 月のあの 2 日間のノーベル賞受賞者名簿に、「スマート製造」という経路から来た人物が一人もいなかったことです。

---

## 不安：ハードウェア帝国のソフトウェア不足

輝かしい数字の背後で、台湾の AI 発展には一つの構造的問題があります。ハードウェアとソフトウェアの深刻な不均衡です。

台湾は世界の AI サーバーの 9 割と AI チップの大部分を生産していますが、AI モデル開発、データエコシステム、プラットフォームソフトウェアといった「ソフト」な領域では存在感が低いままです。GPT、Claude、Gemini、LLaMA を含む世界の上位 20 大 AI モデルの中に、台湾発のものは一つもありません。2024 年のダブル・ノーベル賞の受賞業績と照らし合わせると、Hopfield Network、backpropagation、AlphaFold に至る 3 つの線はいずれも台湾産業から遠い場所にあります。

理由は、古い問題の新しい形です。TSMC のエンジニアの年収が 200 万台湾ドルを超える時、ソフトウェア・スタートアップがトップ人材を獲得するのは難しくなります。Google、Microsoft、NVIDIA が台湾に研究開発センターを設け、給与と福利厚生によって強力な吸引効果を生み出しています。台湾大学情報工学科の卒業生にとって第一候補は、しばしば外資系企業か TSMC の IT 部門であり、地元の AI スタートアップへの参加ではありません。

より根本的な課題はデータです。AI モデルの価値は訓練データから生まれますが、繁体字中国語の高品質データ量は、英語や簡体字中国語と比べてごくわずかです。台湾の 2,300 万人が生み出すテキスト量は、英語圏や中国大陸に自然には及びません。TAIDE 計画はこの問題を解決しようとしていますが、データ規模の劣位は構造的なものです。

台湾 AI の本当の賭けは、基盤モデルではなく垂直応用にあります。汎用モデルで OpenAI や Google と正面から戦うのではなく、台湾は半導体プロセス AI、医療画像 AI、サイバーセキュリティ AI、繁体字中国語 NLP で代替不可能な位置を見つける道を選んでいます。これらの領域では、台湾に固有のデータと現場の優位性があり、他者が容易に複製できません。

---

## 一つの島の AI の選択

2026 年の台湾は、独特の位置に立っています。AI ハードウェア供給網において、これほど不可欠であったことはありません。一方で、AI ソフトウェア・エコシステムにおいては、なお周縁にとどまっています。

これは完全に悪いことではありません。歴史的に、台湾の成功モデルは常に「ブランドにならず、ブランドの背後にあるブランドになる」ことでした。張忠謀が 1987 年に発明した純粋ファウンドリー・モデルは、TSMC を世界時価総額トップ 10 企業に押し上げました。今日、同じ論理が AI サーバー産業で繰り返されています。鴻海は AI モデルを作っていませんが、世界中の AI モデルは鴻海が組み立てたサーバー上で動いています。

しかし AI 時代のゲームルールは異なる可能性があります。価値の重心がハードウェアからソフトウェアとデータへ移る時、受託製造だけの利益空間は圧縮されます。2024 年のあの 2 日間にノーベル賞が授与された対象は、すべてソフトウェア層の人々でした。Hopfield が書いたのは数学モデルであり、Hinton が書いたのは訓練アルゴリズムであり、Hassabis が書いたのは生物学の解法でした。これらの仕事はいずれも台湾製造のハードウェア上で走っていますが、賞はハードウェアに与えられたわけではありません。

台湾は、ハードウェア覇権の基盤の上にソフトウェアとデータの能力を育てる必要があります。ハードウェアは依然として土台であり、その上に新しい価値層が積み重なります。TAIDE は一つの試みです。CyCraft も一つの試みです。Taiwan AI Labs も一つの試みです。それらに共通するのは、「世界最大の AI」を目指すのではなく、「台湾を最も理解する AI」を作ろうとしていることです。

42 年前、Hopfield がプリンストンであの 12 ページを書いた時、それが今日の人類の記憶モデルの数学的基礎になるとは誰も知りませんでした。50 年前、Anfinsen がノーベル講演でタンパク質フォールディング仮説を提示した時、それが 2020 年のあの午後にロンドンの人々によって解かれるまで待つことになるとは誰も予想しませんでした。基礎研究の時間尺度は、どの Computex よりも長いものです。

寧夏夜市でのあの食事は、台湾がこの 42 年で積み上げてきた位置を示しています。次の戦いはどこにあるのか。それは蚵仔煎の屋台の前ではありません。台湾が、今まさに台湾大学の寮でコードを書いているどこかの学生に、20 年後、30 年後にこの島のノーベル賞を取らせる勇気を持てるかどうかにあります。

---

**関連読書**：

- [AI 島国の台頭：台湾の人工知能発展と未来戦略](/technology/AI發展) — 早期版の政策構造の叙述。AI 行動計画、五大戦略領域、半導体の護国神山が AI 革命とどのように接続されたかの全景。
- [台湾人工知能実験室](/technology/台灣人工智慧實驗室) — 杜奕瑾が PTT から AI Labs に至るまでの全過程、TAIDE / TAME / FedGPT のオープンソース言語モデル・エコシステム。
- [台湾人工知能学校](/technology/台灣人工智慧學校) — かけ終えられなかった一本の電話と、陳昇瑋が 1.8 億台湾ドルの民間資金で築いた AI 軍校。8 年で卒業生が 1 万人を超えた人材育成史。
- [台湾 AI の日常](/technology/台灣AI日常) — 生成 AI が台湾の日常生活へ入っていく記録。コンビニの注文から中央健康保険署の一括審査まで、現場単位での観察。
- [台湾企業：TSMC](/economy/台灣企業：台積電) — 世界のファウンドリー首位、AI チップ製造の中核。張忠謀の純粋ファウンドリー・モデルから先端パッケージングまでの物語。
- [半導体産業](/technology/半導體產業) — IC 設計からパッケージング・テストまで、台湾半導体エコシステムの全体像。
- [台湾サイバーセキュリティ産業の発展](/technology/台灣資安產業發展) — 地政学的圧力がどのようにアジア太平洋級の AI サイバーセキュリティ産業を生み出したか。

---

## 画像出典

本文では 4 枚のパブリックドメイン / CC ライセンス画像を使用しており、すべて `public/article-images/technology/` にキャッシュし、元サーバーへのホットリンクを避けています。

- [Estructura tridimensional de la proteïna CBLN1 per AlphaFold amb codificació rainbow](https://commons.wikimedia.org/wiki/File:Estructura_tridimensional_de_la_prote%C3%AFna_CBLN1_per_AlphaFold_amb_codificaci%C3%B3_rainbow.png) — hero、CBLN1 タンパク質の AlphaFold 予測構造、N→C 端を rainbow で色分け。Photo: BQUB25-UPoch (own work, AlphaFold + PyMOL), 2025-11-15, CC BY 4.0.
- [Geoffrey E. Hinton, 2024 Nobel Prize Laureate in Physics (3x4 cropped)](<https://commons.wikimedia.org/wiki/File:Geoffrey_E._Hinton,_2024_Nobel_Prize_Laureate_in_Physics_(3x4_cropped).jpg>) — inline、2024 年ノーベル・ウィークの Hinton 公式ポートレート。Photo: Arthur Petron, 2024-12-08, CC BY-SA 4.0.
- [John J. Hopfield, 2024 Nobel Prize Laureate in Physics 1 (cropped)](<https://commons.wikimedia.org/wiki/File:John_J._Hopfield,_2024_Nobel_Prize_Laureate_in_Physics_1_(cropped).jpg>) — inline、2024 年ノーベル・ウィークの Hopfield 公式ポートレート。Photo: Arthur Petron, 2024-12-08, CC BY-SA 4.0.
- [TSMC Fab 5](https://commons.wikimedia.org/wiki/File:TSMC_Fab_5.jpg) — inline、TSMC 新竹 Fab 5 工場、AI チップ受託製造の物理的現場。Photo: Wikimedia Commons (existing cache).

---

## 参考資料

[^1]: [Tom's Hardware: Semiconductor legends take a stroll in a Taiwanese night market](https://www.tomshardware.com/tech-industry/semiconductor-legends-take-a-stroll-in-a-taiwanese-night-market-nvidia-tsmc-mediatek-and-quanta-heads-seen-eating-dinner) — 2024 年 5 月 29 日の寧夏夜市の場面に関する報道。黄仁勲、張忠謀、林百里、蔡力行が同席して食事する様子を記録しています。

[^2]: [Taiwan News: Nvidia CEO calls Taiwan 'one of the most important countries in the world'](https://www.taiwannews.com.tw/news/5880054) — 2024-05-30 の黄仁勲の訪台時の公的発言。

[^3]: [Wikipedia: Jensen Huang](https://en.wikipedia.org/wiki/Jensen_Huang) — 黄仁勲が 1963 年に台北で生まれ、幼少期を台南で過ごし、9 歳で米国へ移住したことに関する伝記資料。

[^4]: NVIDIA のすべての先端 GPU（A100、H100、Blackwell シリーズ）は TSMC によって受託製造されています。参照：[Klover.ai: TSMC AI Fabricating Dominance](https://www.klover.ai/tsmc-ai-fabricating-dominance-chip-manufacturing-leadership-ai-era/) — NVIDIA AI GPU 全系列の受託製造関係を扱う産業分析。

[^5]: [SQ Magazine: AI Chip Statistics 2025](https://sqmagazine.co.uk/ai-chip-statistics/) — 2025 年の TSMC ファウンドリー収益シェア 72% のデータ出典。Motley Fool の同時期報道も参照。

[^6]: [PatentPC: The AI Chip Market Explosion](https://patentpc.com/blog/the-ai-chip-market-explosion-key-stats-on-nvidia-amd-and-intels-ai-dominance) — NVIDIA の AI GPU 市場シェア 86% のデータ出典。

[^7]: [Tech-Now: Taiwan Leads Global AI Server Shift, Surpassing iPhones in 2025](https://tech-now.io/en/blogs/taiwans-ai-server-revolution-how-foxconn-and-odms-redefined-global-tech-leadership-in-2025) — 鴻海、広達、緯創による世界 AI サーバー 90% 出荷データ。

[^8]: [DigiTimes: Foxconn, Wistron, Quanta to sustain trillion-dollar revenue on AI server in 2026](https://www.digitimes.com/news/a20260109PD249/revenue-ai-server-foxconn-wistron-quanta.html) — 3 社の ODM 年間売上高が 1 兆台湾ドルを突破し、AI サーバーが消費者向け電子製品を上回ったことに関するデータ報道。

[^9]: [36Kr: Who Will Divide Up the CoWoS Production Capacity in 2026?](https://eu.36kr.com/en/p/3580962946874242) — NVIDIA の CoWoS ウェハー需要 59.5 万枚、世界需要の 60% を占めるというデータ。

[^10]: [NVIDIA Newsroom: Foxconn Builds AI Factory in Partnership With Taiwan and NVIDIA](https://nvidianews.nvidia.com/news/foxconn-builds-ai-factory-in-partnership-with-taiwan-and-nvidia) — 高雄 100MW AI ファクトリー協力案件。100MW の電力容量については CNBC 報道も参照。

[^11]: [台湾人工知能実験室公式サイト About Us](https://ailabs.tw/zh/關於我們/) — 杜奕瑾が 1995 年に台湾大学で PTT を創設し、2017 年 4 月に台湾へ戻って Taiwan AI Labs を創設したことに関する公式紹介。

[^12]: [TechNews 科技新報：AI 人才在台灣，該走該留？專訪台灣人工智慧實驗室創辦人杜奕瑾](https://finance.technews.tw/2025/08/18/taiwan-ai-labs-ethan/) — 雅婷逐字稿、連合学習による医療 AI など主要プロジェクトの紹介。

[^13]: [行政院：完善臺灣 AI 基礎建設——打造可信任 AI 對話引擎 TAIDE](https://www.ey.gov.tw/Page/5A8A0CB5B41DA11E/582206fe-26fc-4184-b911-aa6e4569ff3e) — 2023 年 4 月に開始された TAIDE 計画の公式説明。

[^14]: [天下雑誌：「防止中國 AI 文化侵略」台灣第一個繁體中文大語言模型 TAIDE，能做什麼？](https://www.cw.com.tw/article/5129076) — TAIDE に関する特集報道。繁体字中国語 LLM の文化主体性に関する議論の出典。

[^15]: [国家科学及技術委員会プレスリリース：TAIDE 一年有成 公私協力共同推進具臺灣特色之大型語言模型](https://www.nstc.gov.tw/folksonomy/detail/dd2d9d72-8f7b-44dd-976c-438d5ce683af?l=ch) — 2024 年 4 月の TAIDE-LX-7B 商用版、13B 学術研究版の公開。

[^16]: [CloudInsight: Taiwan LLM Development Status 2026](https://cloudinsight.cc/en/blog/taiwan-llm) — TAIDE 2.0、Breeze-8B など台湾 LLM エコシステムの包括的整理。

[^17]: 同上 CloudInsight レポート。中興大学「神農 TAIDE」、台南大学の台湾語・英語対話ボット、陽明交通大学の台湾語・客家語 TAIDE モデルなどの応用事例を詳述しています。

[^18]: [CIO Taiwan：台灣資安業者巡禮——奧義智慧科技](https://www.cio.com.tw/taiwanese-ahn-an-smart-technology/) — CyCraft が Gartner に 7 回掲載され、MITRE ATT&CK 評価を 3 回通過したことの詳細。

[^19]: [CyCraft 公式サイト：創新板首發 AI 資安王者！奧義賽博今日掛牌](https://www.cycraft.com/news/taiwans-first-ai-cybersecurity-stock-20260205) — 2026 年 2 月 5 日のイノベーションボード上場に関するプレスリリース。

[^20]: [国家科学及技術委員会：AI 科研戰略](https://www.nstc.gov.tw/folksonomy/detail/dbf8da09-22be-4ef1-8294-8832fc6e8a26?l=ch) — 第 1 期台湾 AI 行動計画の 400 億台湾ドル予算、TWCC 構築などの政策構造。

[^N1]: [The Nobel Prize in Physics 2024 press release](https://www.nobelprize.org/prizes/physics/2024/press-release/) — 2024 年 10 月 8 日のスウェーデン王立科学アカデミーによる公式発表。原文：「The Royal Swedish Academy of Sciences has decided to award the Nobel Prize in Physics 2024 to John J. Hopfield and Geoffrey Hinton 'for foundational discoveries and inventions that enable machine learning with artificial neural networks.'」賞金は 1,100 万スウェーデン・クローナで、2 人が均等に分け合いました。

[^N2]: [The Nobel Prize in Chemistry 2024 press release](https://www.nobelprize.org/prizes/chemistry/2024/press-release/) — 2024 年 10 月 9 日の発表。賞金は 1,100 万スウェーデン・クローナで、David Baker が「for computational protein design」により半分を受け取り、Demis Hassabis と John Jumper が「for protein structure prediction」により残りの半分を共有しました。

[^N3]: Hopfield, J. J. (1982). "Neural networks and physical systems with emergent collective computational abilities." [PNAS, 79(8), 2554-2558](https://www.pnas.org/doi/10.1073/pnas.79.8.2554) — Hopfield Network の原論文。ニューラルネットワークを spin glass システムに類比し、energy minimum が記憶保存に対応することを提案しました。1982 年 4 月発表。

[^N4]: Rumelhart, D. E., Hinton, G. E., & Williams, R. J. (1986). "Learning representations by back-propagating errors." [Nature, 323, 533-536](https://www.nature.com/articles/323533a0) — backpropagation アルゴリズムの古典的論文。ニューラルネットワーク訓練法の基礎的業績です。

[^N5]: Krizhevsky, A., Sutskever, I., & Hinton, G. E. (2012). "ImageNet Classification with Deep Convolutional Neural Networks." [NeurIPS 2012 / NIPS Proceedings](https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html) — AlexNet の原論文。ImageNet ILSVRC-2012 の top-5 誤り率 15.3%（2 位は 26.2%）を達成し、深層学習の産業化における重要な転換点となりました。

[^N6]: [PanSci 泛科学：2024 諾貝爾物理獎—— Hopfield 與 Hinton 開啟了人工神經網路機器學習時代](https://pansci.asia/archives/378242) — Content Curation Partner per MOU 2026-05-05。Hopfield Network の提案背景、spin glass との類比、論文引用回数の蓄積、現代深層学習との数学的関係を扱っています。

[^N7]: [The Guardian: Nobel physics prize 2024 winner John Hopfield warns of AI dangers](https://www.theguardian.com/science/2024/oct/08/nobel-prize-physics-2024-john-hopfield-geoffrey-hinton-ai-machine-learning) — 2024-10-08 のノーベル物理学賞電話インタビュー報道。Hopfield と Hinton が同日に AI リスクへの警告を示しました。

[^N8]: [Wikipedia: Geoffrey Hinton](https://en.wikipedia.org/wiki/Geoffrey_Hinton) — Hinton は 1947 年 12 月 6 日にロンドンのウィンブルドンで生まれ、2013 年 3 月に Google が DNNresearch を 4,400 万米ドルで買収した後、Google に加わりました。

[^N9]: [BBC News: AI 'godfather' Geoffrey Hinton warns of dangers as he quits Google](https://www.bbc.com/news/world-us-canada-65452940) — 2023-05-01、Hinton が Google 退職後に BBC に対し AI リスクへの懸念を表明しました。原文「I left so that I could talk about the dangers of AI without considering how this impacts Google」、「a part of me now regrets my life's work」。同時期の NYT インタビューの詳細も同報道で引用されています。

[^N10]: [Nature: AI scientist Geoffrey Hinton wins Nobel prize for physics](https://www.nature.com/articles/d41586-024-03213-8) — Nature による 2024 年ノーベル物理学賞授賞現場と Hinton の電話インタビューの詳述。

[^N11]: [Wikipedia: Economic history of Taiwan](https://en.wikipedia.org/wiki/Economic_history_of_Taiwan) — 1986 年の台湾 GDP データ。新竹サイエンスパークは 1980 年 12 月に設立されました。

[^N12]: Anfinsen, C. B. (1973). "Principles that govern the folding of protein chains." [Science, 181(4096), 223-230](https://www.science.org/doi/10.1126/science.181.4096.223) — 1972 年ノーベル化学賞受賞業績の一つ。タンパク質フォールディングがアミノ酸配列によって決まるという仮説を提示しました。

[^N13]: [Nature: 'It will change everything': DeepMind's AI makes gigantic leap in solving protein structures](https://www.nature.com/articles/d41586-020-03348-4) — 2020 年 11 月 30 日の CASP14 結果発表に関する報道。AlphaFold 2 の中央値 GDT 92.4、CASP 主催者 John Moult の「in some sense the problem is solved」というコメントを含みます。

[^N14]: [DeepMind: AlphaFold reveals the structure of the protein universe](https://www.deepmind.com/blog/alphafold-reveals-the-structure-of-the-protein-universe) — 2022 年 7 月 28 日、AlphaFold Protein Structure Database が 100 万種、約 2 億タンパク質構造をカバーしたと発表しました。

[^N15]: [Abramson, J., Adler, J., Dunger, J. et al. (2024). Accurate structure prediction of biomolecular interactions with AlphaFold 3. Nature 630, 493-500](https://www.nature.com/articles/s41586-024-07487-w) — 2024 年 5 月 8 日に AlphaFold 3 を発表。タンパク質と DNA / RNA / ligand / イオン複合体の予測へ拡張しました。

[^N16]: [Wikipedia: Demis Hassabis](https://en.wikipedia.org/wiki/Demis_Hassabis) — Hassabis は 4 歳でチェスを始め、17 歳（1994 年）に Peter Molyneux と『Theme Park』を共同開発し、2010 年にロンドンで DeepMind を創業、2014 年に Google が約 4 億ポンドで買収しました。

[^N17]: [中央研究院ゲノミクス研究センター](https://www.genomics.sinica.edu.tw/) — 翁啓惠院長在任期間（2006-2016）に築かれた糖分子タンパク質構造研究センター。

[^N18]: [PanSci 泛科学：2024 諾貝爾化學獎—— David Baker、Demis Hassabis、John Jumper 解開蛋白質摺疊難題](https://pansci.asia/archives/378388) — Content Curation Partner per MOU 2026-05-05。AlphaFold のノーベル化学賞をめぐる論争、構造生物学と計算化学の学問境界に関する議論を扱っています。

[^N19]: [PanSci 泛科学：AlphaFold 3 預測蛋白質與其他分子互動，藥物開發再升級](https://pansci.asia/archives/377917) — Content Curation Partner per MOU 2026-05-05。AlphaFold 3 が新薬開発、酵素工学にもたらす下流への影響分析。

[^N20]: [PanSci 泛科学：「人造腦」OI 挑戰 AI——培養皿裡的腦組織能取代矽晶片嗎？](https://pansci.asia/archives/366027) — Content Curation Partner per MOU 2026-05-05。Thomas Hartung チームによる Johns Hopkins の人工脳研究。AI の経路以外の代替計算方向として扱っています。
