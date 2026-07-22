---
title: '대만 인공지능 발전과 미래 전략: 하드웨어 입장권은 얻었다, 다음 전장은 어디인가'
description: '2024년 10월 8일 노벨 물리학상은 Hopfield와 Hinton에게, 다음 날 화학상은 AlphaFold의 세 연구자에게 수여되었다. 같은 해 5월 29일, 젠슨 황은 타이베이 닝샤 야시장, 즉 night market에서 모리스 창과 굴전인 어아젠을 먹었다. 대만은 전 세계 AI 서버의 90%, 첨단 웨이퍼의 72%를 제조하지만, 42년 신경망 역사와 50년 단백질 접힘 난제의 해답 속에서는 부재했다. PTT 창립자 두이진의 Taiwan AI Labs부터 국가과학기술위원회가 베팅한 번체중문 LLM 모델 TAIDE까지, 이 섬은 계속 대리생산 공장으로만 남아도 충분한가?'
date: 2026-03-19
author: 'Taiwan.md 編輯組'
category: 'Technology'
subcategory: '人工智慧'
tags:
  [
    '인공지능',
    'AI',
    '반도체',
    '과학기술 정책',
    '디지털 전환',
    '노벨상',
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
translatedAt: '2026-06-16T16:55:29Z'
image: '/article-images/technology/alphafold-cbln1-structure-2025.webp'
imageCredit: 'BQUB25-UPoch (own work, AlphaFold + PyMOL)'
imageLicense: 'CC BY 4.0'
imageSource: 'https://commons.wikimedia.org/wiki/File:Estructura_tridimensional_de_la_prote%C3%AFna_CBLN1_per_AlphaFold_amb_codificaci%C3%B3_rainbow.png'
---

# 대만 인공지능 발전과 미래 전략: 하드웨어 입장권은 얻었다, 다음 전장은 어디인가

> **30초 개관:** 2024년 10월 8일, 노벨 물리학상은 Hopfield Network를 만든 물리학자와 backpropagation을 만든 인지과학자에게 수여되었다[^N1]. 다음 날인 10월 9일, 노벨 화학상은 AI로 50년 된 단백질 접힘 난제를 해결한 세 연구자에게 돌아갔다[^N2]. 같은 해 5월 29일, NVIDIA CEO 젠슨 황은 타이베이 닝샤 야시장, 즉 night market에 나타나 모리스 창, 배리 람, 릭 차이와 굴전인 어아젠을 먹었다. TSMC는 전 세계 파운드리 시장 매출의 72%를 차지하고, 폭스콘·콴타·위스트론은 합산해 전 세계 AI 서버의 90%를 생산한다. 그러나 이틀 연속 이어지며 42년 신경망 역사에 정당성을 부여한 과학적 의식 속에서, 대만 출신의 이름은 하나도 없었다. PTT 창립자 두이진이 세운 대만 인공지능 실험실부터 정부가 베팅한 번체중문 대형언어모델 TAIDE까지, “AI를 제조하는 것”에서 “AI가 되는 것”으로 향하는 도박이 진행 중이다.

---

## 42년 만의 인정: 2024년 노벨상, 이틀 연속 AI를 호명하다

2024년 10월 8일 오전, 스톡홀름. 스웨덴 왕립과학원은 그해 노벨 물리학상을 두 명의 AI 과학자에게 수여한다고 발표했다. 91세 프린스턴 명예교수 John J. Hopfield, 그리고 76세로 다섯 달 전 Google을 막 떠난 Geoffrey Hinton이었다. 상금 1,100만 스웨덴 크로나는 두 사람이 나누어 받았다[^N1].

심사위원회가 제시한 수상 사유는 “인공신경망을 통한 기계학습을 가능하게 한 기초적 발견과 발명”(for foundational discoveries and inventions that enable machine learning with artificial neural networks)이었다[^N1]. 노벨 물리학상 역사상 처음으로 신경망이라는 분야 자체에 직접 상이 놓인 순간이었다.

다음 날, 10월 9일에는 화학상 발표가 있었다. 수상자는 세 명이었다. 워싱턴대학교의 David Baker, 그리고 DeepMind의 Demis Hassabis와 John Jumper. Baker가 상금 절반을 받고, Hassabis와 Jumper가 나머지 절반을 공동 수상했다[^N2]. 수상 사유는 두 부분으로 나뉘었다. 앞부분은 Baker의 “계산 단백질 설계”, 뒷부분은 Hassabis와 Jumper의 “단백질 구조 예측”이었다.

이틀, 두 개의 노벨상, 모두 AI와 관련되어 있었다. 노벨상 역사에서 전례 없는 일이었다.

시간축을 대조해 보자. Hopfield가 1982년 《미국국립과학원회보》(PNAS)에 〈Neural networks and physical systems with emergent collective computational abilities〉라는 논문을 발표했을 때, 그는 막 응집물질물리학에서 신경과학으로 뛰어든 상태였다[^N3]. 1982년부터 2024년까지 정확히 42년이다. Hinton과 Rumelhart가 backpropagation 알고리즘을 사용할 수 있는 도구로 정리한 1986년 논문[^N4]도 발표부터 수상까지 38년이 걸렸다. AlphaFold는 2018년 CASP13에서 처음 등장한 뒤 2024년 노벨상을 받기까지 6년밖에 걸리지 않았다.

결국 이틀 동안 노벨상이 수여한 대상은 ChatGPT가 아니라, 30년 또는 40년 전 아무도 제대로 이해하지 못했던 몇 편의 논문이었다. 기초연구와 산업 응용 사이의 시차는 늘 이렇다.

![2024년 12월 8일 스톡홀름 노벨 주간에 인터뷰 중인 Geoffrey E. Hinton의 공식 초상. 짙은 정장, 백발, 카메라를 향한 차분한 표정](/article-images/technology/hinton-nobel-2024.webp)
_Geoffrey Hinton, 2024년 노벨 물리학상 수상자, 스톡홀름 노벨 주간. Photo: Arthur Petron, 2024-12-08. [CC BY-SA 4.0 via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Geoffrey_E._Hinton,_2024_Nobel_Prize_Laureate_in_Physics_(3x4*cropped).jpg).*

---

## 닝샤 야시장의 조 단위 만찬

2024년 5월 29일 저녁, Computex 개막 전날의 타이베이 닝샤 야시장에 이례적인 식객들이 나타났다. NVIDIA CEO 젠슨 황이 TSMC 창립자 모리스 창, 콴타 회장 배리 람, 미디어텍 CEO 릭 차이를 데리고 노점 앞에 비집고 앉아 굴전인 어아젠을 먹고 있었다[^1]. 행인들이 젠슨 황을 알아보자 순식간에 팬과 기자들이 몰려들었고, 현장은 연예인 추적에 가까운 분위기가 되었다.

이 식사의 시가총액을 모두 합하면 수조 달러를 넘는다. 그러나 진짜 이야기는 식탁 위가 아니라 그 뒤에 놓인 산업 사슬에 있다. 이 사람들이 대표하는 기업들은 전 세계 AI 연산의 물리적 토대를 떠받친다. 젠슨 황은 그 대만 방문 중 공개적으로 “대만은 세계에서 가장 중요한 국가 중 하나”라고 말했다[^2]. 이는 의례적 인사가 아니었다. 대만이 없다면 AI 혁명의 하드웨어 기반은 존재하지 않는다.

젠슨 황은 1963년 타이베이에서 태어나 어린 시절을 타이난에서 보냈고, 아홉 살에 미국으로 이민했다[^3]. 그가 1993년 공동 창업한 NVIDIA는 이제 AI 칩의 동의어가 되었다. ChatGPT 훈련에 쓰인 A100, H100부터 최신 Blackwell 시리즈까지, NVIDIA가 설계한 모든 첨단 GPU는 전부 TSMC가 제조한다[^4].

네 달 뒤 스톡홀름에서 발표된 두 노벨상 명단에는 이 식사와 관련된 이름이 하나도 없었다. 이 간극은 우연이 아니라 구조적 사실이다.

---

## 하드웨어: 한 섬이 전체 AI 혁명을 떠받치다

AI 하드웨어 공급망에서 대만의 위치는 “핵심적”이라고 표현하기에도 부족하다.

칩 제조 부문에서 TSMC는 2025년 전 세계 파운드리 시장 매출 점유율 72%를 차지했다[^5]. 가장 첨단인 7나노미터 이하 공정에서 TSMC의 시장점유율은 90%를 넘는다. NVIDIA의 AI GPU 시장 점유율은 약 86%이며, 이 GPU들은 거의 전량 TSMC가 위탁 생산한다[^6]. 전 세계에서 AI 모델을 훈련하고 실행하는 데 쓰이는 연산력의 절대다수는 대만의 클린룸에서 태어난다.

칩이 만들어진 뒤에는 데이터센터에 들어갈 서버로 조립되어야 한다. 이 단계 역시 대만이 주도한다. 폭스콘, 콴타, 위스트론 세 대형 ODM 업체는 합산해 전 세계 AI 서버의 약 90%를 생산한다[^7]. 2025년 이 세 회사의 연매출은 각각 신대만달러 1조 원, 약 320억 미국 달러를 넘어섰고, 그중 AI 서버 매출은 2분기에 처음으로 소비자 전자제품을 앞질렀다[^8].

AI 칩의 성능은 공정 미세화에만 달려 있지 않다. 패키징 기술에도 달려 있다. TSMC의 CoWoS(Chip on Wafer on Substrate) 첨단 패키징 기술은 NVIDIA 고급 GPU가 성능 목표에 도달하는 데 결정적이다. 2026년에는 NVIDIA 한 회사의 CoWoS 웨이퍼 수요만 59만 5천 장에 이를 것으로 추정되며, 이는 전 세계 총수요의 60%를 차지한다[^9].

폭스콘은 더 나아가 NVIDIA 및 대만 정부와 협력해 가오슝에 100메가와트(MW)급 AI 공장 슈퍼컴퓨터를 건설하고 있으며, 최신 NVIDIA Blackwell 아키텍처를 채택한다[^10]. 대만은 “AI 칩을 제조하는 곳”에서 “AI를 실행하는 곳”으로 올라서고 있다.

![TSMC 신주과학단지 Fab 5 공장 외관, 2010년대 모습. 반도체 파운드리 제조의 물리적 현장](/article-images/technology/tsmc-fab5-hsinchu-2010.webp)
_TSMC 신주 Fab 5 공장, AI 칩 파운드리의 물리적 현장. Photo: Wikimedia Commons via [TSMC Fab 5 file](https://commons.wikimedia.org/wiki/File:TSMC_Fab_5.jpg)._

문제는 하드웨어 입장권을 얻은 뒤, 다음 전장이 어디인가 하는 점이다.

> 📝 **큐레이터 노트**
>
> 통상적인 표현은 “대만의 호국신산이 AI 혁명을 떠받친다”는 것이다. 이 말은 서사적으로 편하지만, 인과관계의 절반을 거꾸로 놓는다. AI 혁명이 GPU를 필요로 했기 때문에 TSMC가 선택된 것이지, TSMC가 AI 혁명 때문에 자라난 것은 아니다. 진짜 긴장은 여기에 있다. GPU가 상품이 될 때, 다음 단계의 가치는 어디로 미끄러질 것인가? 2024년 두 노벨상이 내놓은 답은 모델 그 자체다. Hopfield가 쓴 12쪽짜리 논문, Hinton과 그의 학생 Krizhevsky가 2012년 AlexNet으로 ImageNet 이미지 인식 오류율을 26.2%에서 15.3%로 끌어내린 그 밤[^N5], 그리고 Hassabis의 팀이 AlphaFold로 CASP14에서 중위 GDT 92.4를 기록한 그 오후 말이다.

---

## Hopfield 1982: 물리학자가 쓴 기억 모델

1982년, 프린스턴의 응집물질물리학자 John Hopfield는 단 12쪽짜리 논문을 썼다. 제목은 길었다. 〈Neural networks and physical systems with emergent collective computational abilities〉. 논문은 《미국국립과학원회보》에 실렸다[^N3].

그가 한 일은 본질적으로 “기억”을 물리학으로 번역한 것이었다.

물리학에는 spin glass, 즉 스핀 유리라는 개념이 있다. 여러 자성 원자가 각자 스핀 방향을 갖고 서로 상호작용하며, 전체 시스템은 자발적으로 에너지가 가장 낮은 지점을 찾아간다. Hopfield는 이 개념을 뉴런으로 옮겼다. 뉴런을 스핀으로, 연결 강도를 상호작용으로 상상하면, 전체 네트워크는 자발적으로 어떤 “에너지 최소값”(energy minimum)의 안정 상태로 수렴한다[^N3]. 각각의 energy minimum이 저장된 기억 하나다.

이 모델의 우아함은 기억을 물리학 언어로 서술할 수 있게 했다는 데 있다. 불완전한 단서가 주어지면 네트워크는 스스로 가장 가까운 에너지 최저점을 찾아가고, 기억 전체를 보완한다. 이것이 훗날 생성형 AI가 하는 일의 수학적 조상이다.

1982년의 대만은 전자산업이 막 출발한 시기였고, TSMC도 아직 설립되지 않았다. 모리스 창이 42년 뒤 “호국신산”이 될 회사를 세우는 것은 1987년이 되어서였다. Hopfield의 논문은 2026년 기준 Google Scholar에서 2만 7천 회 이상 인용되었다[^N6].

더 흥미로운 것은 Hopfield가 나중에 한 말이다. 그는 프린스턴에서 평생 응집물질물리학을 연구했고, 신경과학으로 넘어간 일은 당시 동료들에게 “취미 삼은 외도”처럼 여겨졌다. 2024년 노벨상 명단이 발표되었을 때 그는 91세였다. 스웨덴 왕립과학원이 전화 인터뷰에서 수상 소감을 묻자, 그는 “아무도 AI의 방향을 이해하거나 통제하지 못한다”는 점에 불안을 느낀다고 말했다[^N7].

현대 AI 전체의 수학적 기초를 쓴 사람이 상을 받은 바로 그날, 모두에게 조금 조심하라고 경고한 것이다.

![2024년 12월 8일 스톡홀름 노벨 주간에 인터뷰 중인 John J. Hopfield의 초상. 짙은 정장, 백발, 침착한 표정](/article-images/technology/hopfield-nobel-2024.webp)
_John J. Hopfield, 2024년 노벨 물리학상 수상자, 스톡홀름 노벨 주간. Photo: Arthur Petron, 2024-12-08. [CC BY-SA 4.0 via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:John_J._Hopfield,_2024_Nobel_Prize_Laureate_in_Physics_1_(cropped).jpg).\_

---

## Hinton: 1986년 논문과 2023년 Google 퇴사의 경고

1947년 런던 윔블던에서 태어난 Geoffrey Hinton은 역사가 38년 늦게야 인정한 또 다른 인물이다[^N8].

1986년 Hinton은 David Rumelhart, Ronald Williams와 함께 《Nature》에 backpropagation에 관한 논문을 발표했다[^N4]. 이 알고리즘의 의미는 이렇다. 신경망이 오류를 범하면 그 오류 신호를 각 층으로 거꾸로 전파해, 층마다 연결 가중치를 조정할 수 있다. 이것이 오늘날 모든 딥러닝 모델이 스스로를 훈련하는 방식이다.

이 알고리즘은 1986년에 쓰였지만, 폭발하려면 세 가지 조건이 갖춰져야 했다. 충분히 저렴한 연산력, 충분히 대량의 데이터, 그리고 이 길을 믿으려는 사람들이었다. 앞의 두 조건은 2010년대 초에 준비되었고, 세 번째 조건의 대표 인물이 Hinton과 그의 두 학생 Alex Krizhevsky, Ilya Sutskever였다. 2012년 그들은 GPU로 훈련한 합성곱 신경망 AlexNet을 ImageNet 이미지 인식 대회에 출전시켜 top-5 오류율 15.3%를 기록했고, 2위의 26.2%를 크게 따돌렸다[^N5]. 그 순간 산업 전체는 backpropagation이 실제로 작동한다고 믿기 시작했다.

2013년 3월, Google은 4,400만 달러에 Hinton의 작은 회사 DNNresearch를 인수했고, 65세의 그를 영입했다[^N8]. 이후 10년 동안 그는 실리콘밸리에서 가장 권위 있는 AI 학자였다.

그리고 2023년 5월 1일, 《뉴욕타임스》는 한 인터뷰를 내보냈다. Hinton이 Google을 떠났다는 내용이었다.

그가 사임한 이유는 은퇴가 아니었다. 그는 인터뷰에서 “Google에 미칠 영향을 고려하지 않고 AI 위험에 대해 자유롭게 말할 수 있기를” 원한다고 밝혔다[^N9]. 그가 경고한 일에는 AI 시스템이 곧 인간보다 더 똑똑해질 수 있다는 점, 나쁜 사람들이 이를 악용할 수 있다는 점, 그리고 이를 막을 방법은 “무엇이 있는지 보기 어렵다”는 점이 포함되었다[^N9]. 그는 심지어 평생의 작업에 대해 “일부 후회한다”고도 말했다[^N9].

2024년 노벨 물리학상이 그에게 수여되었을 때, 그는 전화 인터뷰에서 다시 한번 경고를 반복했다. AI가 통제 불능이 될 가능성을 조심해야 한다는 것이었다[^N10].

딥러닝 훈련 알고리즘을 쓴 사람과 기억 모델을 쓴 사람이 2024년 10월 같은 날 스웨덴 왕립과학원의 무대에 서서, 동시에 이 물건이 상상보다 더 위험할 수 있다고 경고했다. 이 장면은 1945년 뉴멕시코 사막에서 오펜하이머가 버섯구름을 바라보던 표정과 일종의 대위법을 이룬다.

두 달 뒤, 2024년 12월 8일, 힌튼은 스톡홀름 대학교 Aula Magna 강당에서 노벨상 강연을 했다. 제목은 〈Boltzmann Machines〉였다. 힌튼과 호프필드가 이어받은 열역학 확률분포를 신경망에 쓰는 초기 연구였다. 강연을 들으면 알 수 있다. 1986년 backpropagation 논문은 고립된 통찰이 아니라, 1980년대 물리학과 인지과학이 교차하는 지점에서 자라난 하나의 사유 체계에서 나온 것이었다.

<div class="video-embed" style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;margin:1.5rem 0;border-radius:8px;">
  <iframe src="https://www.youtube.com/embed/iCS1ds0UDP8" title="Boltzmann Machines — Nobel Prize lecture by Geoffrey Hinton, Nobel Prize in Physics 2024" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

_스웨덴 왕립과학원 공식 채널: 제프리 힌튼의 2024년 12월 8일 노벨 물리학상 강연 「Boltzmann Machines」. 1980년대 세이노프스키와 함께 쓴 볼츠만 머신부터 backpropagation, 그리고 오늘의 LLM까지 통틀어 40년이다. 마지막 5분에서 그는 AI 위험에 대한 우려를 다시 말했다. 이번에는 노벨 강단에 서서._

---

## PTT에서 AI 실험실까지: 두이진의 두 번의 창업

대만이라는 섬으로 돌아오자. Hopfield가 기억 모델을 쓴 바로 그 무렵, 대만에는 컴퓨터공학과가 막 생겨나기 시작했다.

1995년, 국립대만대학교 컴퓨터공학과 2학년 학생 두이진은 486 컴퓨터 한 대와 오픈소스 소프트웨어로 기숙사 안에 [PTT](/ko/Technology/ptt-bulletin-board-system/)를 구축했다. 이는 훗날 대만 최대의 전자게시판이 되었다. 30년 뒤에도 PTT에는 매일 수십만 명이 접속하며, 대만 인터넷 문화의 살아 있는 화석으로 남아 있다.

두이진은 이후 Microsoft로 가서 Cortana 음성비서 개발에 참여했다. 2017년 4월, 그는 실리콘밸리의 고액 연봉을 포기하고 대만으로 돌아와 “대만 인공지능 실험실”(Taiwan AI Labs)을 창립했다. 이는 아시아 최초의 비영리 개방형 AI 연구기관이었다[^11].

그의 동기는 매우 분명했다. 대만에는 세계적 수준의 소프트웨어 인재가 있지만, 이들은 모두 실리콘밸리로 가버린다. 그는 돌아오고 싶거나 남고 싶은 사람들이 AI 연구를 할 수 있는 플랫폼을 만들고자 했다.

Taiwan AI Labs의 가장 유명한 제품은 “야팅 회의록”이다. 번체중문과 대만식 억양에 최적화된 음성인식 시스템이다. COVID-19 팬데믹 기간에는 가짜뉴스 탐지 도구와 연합학습 의료 AI도 개발했다[^12]. 이 프로젝트들의 공통점은 대만의 현지 문제를 해결하고, 대만의 현지 데이터를 사용했다는 점이다. 미국 모델을 번역해 가져다 쓴 것이 아니었다.

두이진의 이야기는 PTT에서 AI Labs까지, 어느 정도 대만 소프트웨어 발전의 축소판이다. 기술 역량이 부족한 것이 아니다. 부족한 것은 인재가 남을 수 있는 생태계다.

> 💡 **알고 있나요**
>
> 1986년 Hinton이 backpropagation을 발표한 그해, 대만 GDP는 약 779억 미국 달러, 1인당 GDP는 약 4,007달러였고, 신주과학단지는 운영을 시작한 지 6년밖에 되지 않았다[^N11]. 세 가지 일은 같은 지구에서 동시에 일어났지만, 이 역사선이 ImageNet 데이터셋 위에서 만나기까지는 26년이 더 필요했다. 기초연구의 시간척도는 언제나 산업 서사가 체감하는 것보다 길다.

---

## AlphaFold: 50년 단백질 접힘 난제의 또 다른 노벨상 절반

2024년 노벨 화학상의 이야기는 1972년의 한 질문에서 시작해야 한다.

그해 미국 생화학자 Christian Anfinsen은 노벨 화학상 수상 연설에서 하나의 가설을 제시했다. 단백질의 3차원 접힘 구조는 전적으로 그 아미노산 서열에 의해 결정된다는 것이었다[^N12]. 이 가설이 맞다면 이론적으로 우리는 아미노산 서열 하나만 보고도 대응하는 3D 구조를 계산해낼 수 있어야 했다. 그러나 이 “해야 한다”는 일은 반세기 동안 이루어지지 않았다. 단백질 접힘은 grand challenge로 불렸다. 학계는 2년마다 CASP 대회를 열어 모든 연구자가 제출한 예측 결과를 실험 구조와 비교했다. 1994년부터 13차례 열렸지만 누구도 돌파하지 못했다[^N13].

2018년 CASP13에서 DeepMind가 1세대 AlphaFold를 출전시켜 우승했지만, 정확도는 아직 실용 수준에 이르지 못했다. 진정한 전환점은 2020년 11월 30일의 CASP14였다. AlphaFold 2가 중위 GDT 92.4라는 성적을 냈다[^N13]. GDT 92.4란 예측 결과의 절반 이상에서 원자 위치가 실험값과 1옹스트롬 미만으로 차이 났다는 뜻으로, 실험 해상도 수준에 도달했다는 의미다. CASP 주최자 John Moult는 그날 “어떤 의미에서는 이 문제가 해결되었다”고 말했다[^N13].

50년 동안 풀리지 않았던 문제가 런던의 한 연구팀에 의해 6년 만에 풀린 것이다.

이후 일은 더 빠르게 진행되었다. 2021년 7월 AlphaFold 2 원시코드가 오픈소스로 공개되었다. 같은 해 DeepMind는 유럽분자생물학연구소(EMBL-EBI)와 협력해 AlphaFold가 예측한 단백질 구조를 공개 데이터베이스로 만들었다. 2022년 7월 이 데이터베이스는 100만 종, 약 2억 개 단백질 구조를 포괄하게 되었고, 이는 지구상 거의 모든 알려진 단백질의 3D 모델을 무료로 공개한 것과 같았다[^N14].

2024년 5월 8일, DeepMind는 《Nature》에 AlphaFold 3를 발표했다. 예측 능력은 단일 단백질에서 단백질과 DNA, RNA, 리간드(ligand), 이온 간 상호작용으로 확장되었다[^N15]. 신약 개발, 백신 설계, 효소공학에 이르기까지 분자가 어떻게 맞물리는지 알아야 하는 모든 분야의 밑바탕이 이 도구에 의해 다시 쓰였다.

AlphaFold를 만든 Demis Hassabis는 전통적인 생화학자가 아니다. 그는 네 살 때 체스를 시작했고, 13세에 마스터 타이틀을 얻었다. 17세에는 Peter Molyneux와 함께 시뮬레이션 게임 《Theme Park》를 공동 개발해 수백만 장을 판매했다[^N16]. 2010년 그는 Shane Legg, Mustafa Suleyman과 함께 런던에서 DeepMind를 창업했고, 2014년 Google이 약 4억 파운드에 인수했다[^N16]. 2016년 DeepMind의 AlphaGo가 이세돌을 꺾었고, 2020년에는 AlphaFold 2, 2024년에는 노벨상이 있었다. 세 사건 사이의 간격은 10년도 되지 않는다.

그 사이를 잇는 선은 하나의 같은 베팅이다. 인간이 과거에 인간의 두뇌로 풀지 못했던 문제를 신경망으로 푼다는 것이다. 바둑은 규칙이 닫힌 세계이고, 단백질 접힘은 규칙이 열려 있지만 물리적 제약이 강한 세계다. Hassabis는 두 경우 모두 전장을 정확히 골랐다.

대만에서는 중앙연구원 원치후이 원장 재임기(2006-2016)에 구축된 당분자 단백질 연구가 이 전선에 가장 가까운 학술 투자였다[^N17]. 중앙연구원 생의학연구소와 생화학연구소에도 AlphaFold의 오픈소스 가중치를 활용해 하류 연구를 수행하는 팀들이 있다. 그러나 AlphaFold급 핵심 모델 개발에 대응하는 제도적 기반은 현재 대만에 없다.

> ⚠️ **논쟁적 관점**
>
> AlphaFold가 노벨 화학상을 받은 데 대해서는 학계에서 논쟁이 있었다. 일부 구조생물학자는 이 상이 계산 도구를 화학의 전당에 올리는 것이 아니라, 가장 이른 핵심 실험을 수행한 X선 결정학 또는 핵자기공명 연구자들에게 돌아가야 했다고 본다[^N18]. 다른 한쪽은 이 논쟁 자체가 이미 낡았다고 본다. 알고리즘이 5년 안에 인류가 지구상 거의 모든 단백질의 3D 구조를 보완하도록 도왔다면, 그것이 곧 화학이라는 것이다. 두 입장의 논쟁은 2024년 10월 이후 점차 후자 쪽으로 이동했지만, 그 긴장은 사라지지 않았다. AI가 할 수 있는 일이 확장될 때, 전통 학문의 경계를 다시 그려야 하는가?

---

## TAIDE: 대만에는 왜 자체 언어모델이 필요한가

ChatGPT가 전 세계를 휩쓴 지 반년 뒤인 2023년 4월, 대만 국가과학기술위원회는 “TAIDE” 계획을 시작했다. 전체 이름은 Trustworthy AI Dialogue Engine, 즉 신뢰할 수 있는 생성형 AI 대화 엔진이다[^13].

인구 2,300만 명의 섬나라가 왜 자체 대형언어모델을 만들어야 하는가?

이유는 기술 자주성만이 아니다. 번체중문은 전 세계 AI 훈련자료에서 차지하는 비중이 극히 낮고, 대부분의 중국어 자료는 간체중문 웹사이트에서 온다. 대만인이 ChatGPT나 다른 모델을 사용할 때 받는 답변에는 종종 중국 대륙의 용어 습관과 관점의 전제가 섞여 있다. “영상”을 뜻할 때 대만식 “影片”이 아니라 대륙식 “視頻”을 쓰거나, “품질”을 뜻할 때 “品質”이 아니라 “質量”을 쓰는 차이는 겉보기에는 작아 보인다. 그러나 그 뒤에는 문화 주체성의 문제가 있다. 《天下雜誌》는 TAIDE를 보도하면서 제목에 “중국 AI 문화 침략을 막기 위해”라는 표현을 직접 사용했다[^14].

2024년 4월, TAIDE 팀은 상용판 TAIDE-LX-7B와 학술연구판 TAIDE-LX-13B 모델을 공개했다. 쓰기, 번역, 요약 등의 작업에서 양호한 성능을 보였다[^15]. 2026년에 이르러 TAIDE 2.0이 발표되고, 미디어텍이 지원한 Breeze-8B 모델까지 더해지면서 대만의 LLM 생태계는 “추격” 단계에서 “사용 가능” 단계로 들어섰다[^16].

더 흥미로운 것은 응용 단의 확산이다. 국립중흥대학교는 TAIDE로 농업 지식 검색 시스템 “신농 TAIDE”를 만들었다. 국립타이난대학교는 대만어 교육을 위한 대만어-영어 대화형 챗봇을 개발했다. 국립양밍자오퉁대학교는 대만어와 하카어 버전의 TAIDE 모델을 훈련했다[^17]. 이 응용들은 한 가지 사실을 입증한다. 언어모델은 기술 제품인 동시에 문화 매개체다. “천천일”과 “마쭈 순례”를 이해하지 못하는 AI는 대만인을 진정으로 섬길 수 없다.

그러나 TAIDE의 규모는 여전히 작다. 상용 8B와 학술연구용 13B 매개변수 규모는 OpenAI의 GPT-4급, 추정상 1조 매개변수를 넘는 수준과 비교하면 두 자릿수 이상 차이가 난다. 이 격차의 배후에는 능력 문제가 아니라 GPU 예산 문제가 있다. 최전선급 LLM 하나를 훈련하려면 억 달러 단위의 연산력이 필요하며, 이는 국가급 연구기관의 연간 예산과 같은 규모다.

---

## 해킹이 만들어낸 AI 보안

대만은 전 세계에서 사이버공격을 가장 빈번하게 받는 국가 중 하나다. 이 불행한 현실은 뜻밖에도 강력한 AI 보안 산업을 낳았다.

2017년 말 설립된 CyCraft는 AI와 엔드포인트 모니터링을 결합한 대만 최초의 보안 기업이다. 그 기술은 글로벌 조사기관 Gartner 보고서에 일곱 차례 수록되었고, 미국 MITRE ATT&CK 권위 평가를 세 차례 통과한 대만 유일의 업체다[^18]. 2026년 2월 CyCraft는 대만증권거래소 혁신판에 상장했다. 이는 대만 자본시장 최초의 국제급 자체 연구개발 역량을 갖춘 AI 보안 소프트웨어 원천 기업이었다[^19].

CyCraft의 고객에는 대만 정부기관, 국방기관, 은행, 반도체 기업이 포함된다. 이들은 국가급 해커의 표적이 가장 자주 되는 대상이다. 회사는 일본과 싱가포르에 자회사를 두고 있으며, “해킹당하며 축적한 실전 경험”을 아시아태평양 전역으로 수출하고 있다.

이 사례는 한 가지를 보여준다. 대만의 AI 우위는 반도체에서만 오는 것이 아니라, 특수한 지정학적 조건이 단련한 실전 능력에서도 나온다.

---

## 정책: “AI 원년”에서 디지털발전부까지

대만의 AI 정책 발전은 세 개의 지점으로 이해할 수 있다.

2017년부터 2018년까지는 출발 단계였다. 행정원은 2017년을 “AI 원년”으로 정하고, “AI 소국 대전략” 개념을 제시했다. 대만 시장이 작다는 점을 인정하되, 반도체 제조, ICT 공급망, 이공계 인재라는 세 장의 카드를 강조했다. 2018년에는 1기 “대만 AI 행동계획”을 시작해 4년 동안 신대만달러 400억 원 이상을 투입했고, AI 연산 인프라 “대만 AI 클라우드”(TWCC) 구축에 중점을 두었다[^20].

2022년에는 제도화로 나아갔다. 디지털발전부(moda)가 설립되어 과학기술부, 경제부, 교통부에 흩어져 있던 디지털 업무를 통합했다. 이 단계의 의미는 AI 정책이 “과학기술부의 프로젝트”에서 “부처를 가로지르는 국가전략”으로 격상되었다는 데 있다. 같은 해 정부는 “인공지능 과학연구 발전 지침”을 발표해 인간 중심, 투명성과 설명 가능성, 공정성과 비차별 등의 원칙을 강조했다.

2023년 이후는 생성형 AI 전환기다. ChatGPT의 충격은 정책을 급격히 방향 전환시켰다. TAIDE 계획이 시작되고, AI 기본법 초안이 추진되었으며, 공공부문의 AI 도입이 빨라졌다. 대만의 전략은 매우 실용적이다. 미국과 중국을 상대로 기초연구 논문 수를 겨루기보다, AI를 기존 제조업의 강점과 접목하는 것이다. 스마트 제조, 의료영상, 반도체 수율 예측은 모두 대만에 데이터와 현장, 경쟁력이 있는 분야다.

문제는 2024년 10월 그 이틀 동안의 노벨상 수상자 명단에 “스마트 제조”라는 경로에서 온 사람이 한 명도 없었다는 점이다.

---

## 불안: 하드웨어 제국의 소프트웨어 결손

화려한 숫자 뒤에는 대만 AI 발전의 구조적 문제가 있다. 하드웨어와 소프트웨어의 심각한 불균형이다.

대만은 전 세계 AI 서버의 90%와 AI 칩 대부분을 생산하지만, AI 모델 개발, 데이터 생태계, 플랫폼 소프트웨어 같은 “소프트”한 단계에서는 존재감이 낮다. GPT, Claude, Gemini, LLaMA를 포함한 전 세계 상위 20대 AI 모델 가운데 대만에서 나온 것은 하나도 없다. 2024년 두 노벨상의 수상 업적을 대조해 보면, Hopfield Network, backpropagation, AlphaFold에 이르는 세 줄기는 모두 대만 산업과 거리가 멀다.

이유는 오래된 문제의 새 버전이다. TSMC 엔지니어의 연봉이 신대만달러 200만 원을 넘을 수 있는 상황에서, 소프트웨어 스타트업이 최상위 인재를 확보하기는 어렵다. Google, Microsoft, NVIDIA는 대만에 연구개발센터를 세웠고, 임금과 복지는 강력한 흡입 효과를 만든다. 국립대만대학교 컴퓨터공학과 졸업생의 첫 선택은 종종 외국계 기업이나 TSMC IT이지, 현지 AI 스타트업 합류가 아니다.

더 근본적인 도전은 데이터다. AI 모델의 가치는 훈련 데이터에서 오는데, 고품질 번체중문 데이터의 양은 영어 또는 간체중문과 비교하면 극히 작다. 인구 2,300만 명의 대만이 생산하는 텍스트 양은 본질적으로 영어권이나 중국 대륙을 따라갈 수 없다. TAIDE 계획은 이 문제를 해결하려 하지만, 데이터 규모의 열세는 구조적이다.

대만 AI의 진짜 베팅은 기초모델이 아니라 수직 응용에 놓여 있다. 범용모델에서 OpenAI나 Google과 정면 대결하기보다, 대만은 반도체 공정 AI, 의료영상 AI, 보안 AI, 번체중문 NLP에서 대체 불가능한 위치를 찾는 쪽을 선택한다. 이들 분야에는 대만 고유의 데이터와 현장 우위가 있으며, 다른 이들이 복제하기 어렵다.

---

## 한 섬의 AI 선택

2026년의 대만은 독특한 위치에 서 있다. AI 하드웨어 공급망에서는 그 어느 때보다 대체 불가능하지만, AI 소프트웨어 생태계에서는 여전히 주변부에 있다.

이것이 전적으로 나쁜 일은 아니다. 역사적으로 대만의 성공 모델은 늘 “브랜드가 아니라 브랜드 뒤의 브랜드”가 되는 것이었다. 모리스 창이 1987년 발명한 순수 파운드리 모델은 TSMC를 세계 시가총액 상위 10대 기업으로 만들었다. 오늘날 같은 논리가 AI 서버 산업에서 반복되고 있다. 폭스콘은 AI 모델을 만들지 않지만, 전 세계 AI 모델은 폭스콘이 조립한 서버 위에서 달린다.

그러나 AI 시대의 게임 규칙은 다를 수 있다. 가치의 중심이 하드웨어에서 소프트웨어와 데이터로 미끄러질 때, 대리생산만 하는 이윤 공간은 압축될 것이다. 2024년 그 이틀 동안 노벨상이 수여된 대상은 모두 소프트웨어 계층의 사람들이었다. Hopfield가 쓴 것은 수학 모델이고, Hinton이 쓴 것은 훈련 알고리즘이며, Hassabis가 쓴 것은 생물학의 해법이다. 이 모든 작업은 대만이 만든 하드웨어 위에서 돌아가지만, 상은 하드웨어에 주어지지 않았다.

대만은 하드웨어 패권 위에 소프트웨어와 데이터의 역량을 길러야 한다. 하드웨어는 여전히 바닥판이고, 새로운 가치층은 그 위에 겹쳐진다. TAIDE는 하나의 시도이고, CyCraft도 하나의 시도이며, Taiwan AI Labs도 하나의 시도다. 이들의 공통점은 “세계에서 가장 큰 AI”를 추구하지 않고 “대만을 가장 잘 이해하는 AI”를 만들려 한다는 데 있다.

42년 전 Hopfield가 프린스턴에서 그 12쪽짜리 논문을 썼을 때, 아무도 그것이 오늘날 인간 기억 모델의 수학적 기초가 되리라고 알지 못했다. 50년 전 Anfinsen이 노벨상 연설에서 단백질 접힘 가설을 제시했을 때, 2020년 어느 오후 런던의 한 팀이 그것을 풀 때까지 기다려야 하리라고 예상한 사람도 없었다. 기초연구의 시간척도는 모든 Computex보다 길다.

닝샤 야시장의 그 식사는 대만이 이 42년 동안 축적한 위치였다. 다음 전장이 어디인가. 그것은 어아젠 노점 앞이 아니라, 대만이 지금 국립대만대학교 기숙사에서 코드를 쓰고 있는 어떤 학생이 20년 또는 30년 뒤 이 섬의 이름으로 노벨상을 받을 수 있도록 할 용기가 있는가에 달려 있다.

---

**더 읽을거리**:

- [AI 섬나라의 부상: 대만 인공지능 발전과 미래 전략](/technology/AI發展) — 초기 버전의 정책 구조 서사. AI 행동계획, 5대 전략 분야, 반도체 호국신산이 AI 혁명과 어떻게 접목되는지의 전경.
- [대만 인공지능 실험실](/technology/台灣人工智慧實驗室) — 두이진이 PTT에서 AI Labs까지 걸어온 전체 과정, TAIDE / TAME / FedGPT 오픈소스 언어모델 생태계.
- [대만 인공지능 학교](/technology/台灣人工智慧學校) — 끝까지 걸지 못한 그 전화, 그리고 천성웨이가 민간 모금 1억 8천만 원으로 세운 AI 사관학교. 8년 동안 동문 1만 명을 넘긴 인재 양성사.
- [대만 AI 일상](/technology/台灣AI日常) — 생성형 AI가 대만의 일상생활에 들어온 기록. 편의점 주문부터 건강보험서의 일괄 심사까지, 장면 단위의 관찰.
- [대만 기업: TSMC](/economy/台灣企業：台積電) — 전 세계 파운드리 선두 기업이자 AI 칩 제조의 핵심. 모리스 창의 순수 파운드리 모델부터 첨단 패키징까지의 이야기.
- [반도체 산업](/technology/半導體產業) — IC 설계부터 패키징·테스트까지, 대만 반도체 생태계의 전체상.
- [대만 보안 산업 발전](/technology/台灣資安產業發展) — 지정학적 압력이 어떻게 아시아태평양급 AI 보안 산업을 낳았는가.

---

## 이미지 출처

이 글은 퍼블릭 도메인 / CC 라이선스 이미지 4장을 사용했으며, 모두 원본 서버 핫링크를 피하기 위해 `public/article-images/technology/`에 캐시되어 있다.

- [Estructura tridimensional de la proteïna CBLN1 per AlphaFold amb codificació rainbow](https://commons.wikimedia.org/wiki/File:Estructura_tridimensional_de_la_prote%C3%AFna_CBLN1_per_AlphaFold_amb_codificaci%C3%B3_rainbow.png) — hero, CBLN1 단백질 AlphaFold 예측 구조, N→C 말단 rainbow 색상 코딩. Photo: BQUB25-UPoch (own work, AlphaFold + PyMOL), 2025-11-15, CC BY 4.0.
- [Geoffrey E. Hinton, 2024 Nobel Prize Laureate in Physics (3x4 cropped)](<https://commons.wikimedia.org/wiki/File:Geoffrey_E._Hinton,_2024_Nobel_Prize_Laureate_in_Physics_(3x4_cropped).jpg>) — inline, 2024년 노벨 주간 Hinton 공식 초상. Photo: Arthur Petron, 2024-12-08, CC BY-SA 4.0.
- [John J. Hopfield, 2024 Nobel Prize Laureate in Physics 1 (cropped)](<https://commons.wikimedia.org/wiki/File:John_J._Hopfield,_2024_Nobel_Prize_Laureate_in_Physics_1_(cropped).jpg>) — inline, 2024년 노벨 주간 Hopfield 공식 초상. Photo: Arthur Petron, 2024-12-08, CC BY-SA 4.0.
- [TSMC Fab 5](https://commons.wikimedia.org/wiki/File:TSMC_Fab_5.jpg) — inline, TSMC 신주 Fab 5 공장, AI 칩 파운드리의 물리적 현장. Photo: Wikimedia Commons (existing cache).

---

## 참고자료

[^1]: [Tom's Hardware: Semiconductor legends take a stroll in a Taiwanese night market](https://www.tomshardware.com/tech-industry/semiconductor-legends-take-a-stroll-in-a-taiwanese-night-market-nvidia-tsmc-mediatek-and-quanta-heads-seen-eating-dinner) — 2024년 5월 29일 닝샤 야시장 장면 보도. 젠슨 황, 모리스 창, 배리 람, 릭 차이가 한자리에서 식사한 장면을 기록했다.

[^2]: [Taiwan News: Nvidia CEO calls Taiwan 'one of the most important countries in the world'](https://www.taiwannews.com.tw/news/5880054) — 2024-05-30 젠슨 황의 대만 방문 공개 발언.

[^3]: [Wikipedia: Jensen Huang](https://en.wikipedia.org/wiki/Jensen_Huang) — 젠슨 황이 1963년 타이베이에서 태어나 어린 시절을 타이난에서 보내고 아홉 살에 미국으로 이민했다는 전기 자료.

[^4]: NVIDIA의 모든 첨단 GPU(A100, H100, Blackwell 시리즈)는 TSMC가 위탁 생산한다. [Klover.ai: TSMC AI Fabricating Dominance](https://www.klover.ai/tsmc-ai-fabricating-dominance-chip-manufacturing-leadership-ai-era/) 참조 — NVIDIA AI GPU 전 시리즈의 파운드리 관계를 다룬 산업 분석.

[^5]: [SQ Magazine: AI Chip Statistics 2025](https://sqmagazine.co.uk/ai-chip-statistics/) — 2025년 TSMC 파운드리 매출 시장점유율 72%의 데이터 출처. Motley Fool의 같은 시기 보도도 참조.

[^6]: [PatentPC: The AI Chip Market Explosion](https://patentpc.com/blog/the-ai-chip-market-explosion-key-stats-on-nvidia-amd-and-intels-ai-dominance) — NVIDIA AI GPU 시장점유율 86% 데이터 출처.

[^7]: [Tech-Now: Taiwan Leads Global AI Server Shift, Surpassing iPhones in 2025](https://tech-now.io/en/blogs/taiwans-ai-server-revolution-how-foxconn-and-odms-redefined-global-tech-leadership-in-2025) — 폭스콘, 콴타, 위스트론의 전 세계 AI 서버 90% 출하 데이터.

[^8]: [DigiTimes: Foxconn, Wistron, Quanta to sustain trillion-dollar revenue on AI server in 2026](https://www.digitimes.com/news/a20260109PD249/revenue-ai-server-foxconn-wistron-quanta.html) — 세 ODM의 연매출 1조 원 돌파와 AI 서버가 소비자 전자제품을 넘어섰다는 데이터 보도.

[^9]: [36Kr: Who Will Divide Up the CoWoS Production Capacity in 2026?](https://eu.36kr.com/en/p/3580962946874242) — NVIDIA의 CoWoS 웨이퍼 수요 59만 5천 장, 전 세계 60% 점유 데이터.

[^10]: [NVIDIA Newsroom: Foxconn Builds AI Factory in Partnership With Taiwan and NVIDIA](https://nvidianews.nvidia.com/news/foxconn-builds-ai-factory-in-partnership-with-taiwan-and-nvidia) — 가오슝 100MW AI 공장 협력안. 100MW 전력 용량은 CNBC 보도도 참조.

[^11]: [台灣人工智慧實驗室官網 關於我們](https://ailabs.tw/zh/關於我們/) — 두이진이 1995년 국립대만대학교에서 PTT를 창립하고, 2017년 4월 대만으로 돌아와 Taiwan AI Labs를 창립했다는 공식 소개.

[^12]: [TechNews 科技新報：AI 人才在台灣，該走該留？專訪台灣人工智慧實驗室創辦人杜奕瑾](https://finance.technews.tw/2025/08/18/taiwan-ai-labs-ethan/) — 야팅 회의록, 연합학습 의료 AI 등 핵심 프로젝트 소개.

[^13]: [行政院：完善臺灣 AI 基礎建設——打造可信任 AI 對話引擎 TAIDE](https://www.ey.gov.tw/Page/5A8A0CB5B41DA11E/582206fe-26fc-4184-b911-aa6e4569ff3e) — 2023년 4월 TAIDE 계획 시작에 관한 공식 설명.

[^14]: [天下雜誌：「防止中國 AI 文化侵略」台灣第一個繁體中文大語言模型 TAIDE，能做什麼？](https://www.cw.com.tw/article/5129076) — TAIDE 주제 보도. 번체중문 LLM의 문화 주체성 논의 출처.

[^15]: [國科會新聞稿：TAIDE 一年有成 公私協力共同推進具臺灣特色之大型語言模型](https://www.nstc.gov.tw/folksonomy/detail/dd2d9d72-8f7b-44dd-976c-438d5ce683af?l=ch) — 2024년 4월 TAIDE-LX-7B 상용판과 13B 학술연구판 공개.

[^16]: [CloudInsight: Taiwan LLM Development Status 2026](https://cloudinsight.cc/en/blog/taiwan-llm) — TAIDE 2.0, Breeze-8B 등 대만 LLM 생태계 종합 정리.

[^17]: 위 CloudInsight 보고서와 같음. 국립중흥대학교 “신농 TAIDE”, 국립타이난대학교 대만어-영어 대화형 챗봇, 국립양밍자오퉁대학교 대만어·하카어 TAIDE 모델 등 응용 사례를 상세히 다룸.

[^18]: [CIO Taiwan：台灣資安業者巡禮——奧義智慧科技](https://www.cio.com.tw/taiwanese-ahn-an-smart-technology/) — CyCraft가 Gartner에 일곱 차례 수록되고 MITRE ATT&CK 평가를 세 차례 통과했다는 상세 설명.

[^19]: [奧義智慧官網：創新板首發 AI 資安王者！奧義賽博今日掛牌](https://www.cycraft.com/news/taiwans-first-ai-cybersecurity-stock-20260205) — 2026년 2월 5일 혁신판 상장 보도자료.

[^20]: [國科會：AI 科研戰略](https://www.nstc.gov.tw/folksonomy/detail/dbf8da09-22be-4ef1-8294-8832fc6e8a26?l=ch) — 1기 대만 AI 행동계획의 400억 예산, TWCC 구축 등 정책 구조.

[^N1]: [The Nobel Prize in Physics 2024 press release](https://www.nobelprize.org/prizes/physics/2024/press-release/) — 2024년 10월 8일 스웨덴 왕립과학원의 공식 발표. 원문: “The Royal Swedish Academy of Sciences has decided to award the Nobel Prize in Physics 2024 to John J. Hopfield and Geoffrey Hinton 'for foundational discoveries and inventions that enable machine learning with artificial neural networks.'” 상금 1,100만 스웨덴 크로나는 두 사람이 나누어 받았다.

[^N2]: [The Nobel Prize in Chemistry 2024 press release](https://www.nobelprize.org/prizes/chemistry/2024/press-release/) — 2024년 10월 9일 발표. 상금 1,100만 스웨덴 크로나 중 David Baker가 “for computational protein design”으로 절반을, Demis Hassabis와 John Jumper가 “for protein structure prediction”으로 나머지 절반을 공동 수상했다.

[^N3]: Hopfield, J. J. (1982). "Neural networks and physical systems with emergent collective computational abilities." [PNAS, 79(8), 2554-2558](https://www.pnas.org/doi/10.1073/pnas.79.8.2554) — Hopfield Network 원 논문. 신경망을 spin glass 시스템에 비유하고, energy minimum이 기억 저장에 대응한다고 제시했다. 1982년 4월 발표.

[^N4]: Rumelhart, D. E., Hinton, G. E., & Williams, R. J. (1986). "Learning representations by back-propagating errors." [Nature, 323, 533-536](https://www.nature.com/articles/323533a0) — backpropagation 알고리즘의 고전 논문. 신경망 훈련법의 토대가 된 작업.

[^N5]: Krizhevsky, A., Sutskever, I., & Hinton, G. E. (2012). "ImageNet Classification with Deep Convolutional Neural Networks." [NeurIPS 2012 / NIPS Proceedings](https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html) — AlexNet 원 논문. ImageNet ILSVRC-2012 top-5 오류율 15.3%(2위 26.2%)로, 딥러닝 산업화의 결정적 전환점.

[^N6]: [PanSci 泛科學：2024 諾貝爾物理獎—— Hopfield 與 Hinton 開啟了人工神經網路機器學習時代](https://pansci.asia/archives/378242) — Content Curation Partner per MOU 2026-05-05. Hopfield Network의 제안 배경, spin glass 비유, 논문 인용 횟수 누적, 현대 딥러닝과의 수학적 연결을 다룬다.

[^N7]: [The Guardian: Nobel physics prize 2024 winner John Hopfield warns of AI dangers](https://www.theguardian.com/science/2024/oct/08/nobel-prize-physics-2024-john-hopfield-geoffrey-hinton-ai-machine-learning) — 2024-10-08 노벨 물리학상 전화 인터뷰 보도. Hopfield와 Hinton이 같은 날 AI 위험을 경고했다.

[^N8]: [Wikipedia: Geoffrey Hinton](https://en.wikipedia.org/wiki/Geoffrey_Hinton) — Hinton은 1947년 12월 6일 런던 윔블던에서 태어났고, 2013년 3월 Google이 4,400만 달러에 DNNresearch를 인수한 뒤 Google에 합류했다.

[^N9]: [BBC News: AI 'godfather' Geoffrey Hinton warns of dangers as he quits Google](https://www.bbc.com/news/world-us-canada-65452940) — 2023-05-01 Hinton이 Google을 떠난 뒤 BBC에 AI 위험 우려를 밝힌 보도. 원문 “I left so that I could talk about the dangers of AI without considering how this impacts Google”, “a part of me now regrets my life's work”. 같은 시기 NYT 인터뷰의 세부 내용도 이 보도에서 인용된다.

[^N10]: [Nature: AI scientist Geoffrey Hinton wins Nobel prize for physics](https://www.nature.com/articles/d41586-024-03213-8) — 2024년 노벨 물리학상 발표 현장과 Hinton 전화 인터뷰에 관한 Nature의 상세 보도.

[^N11]: [Wikipedia: Economic history of Taiwan](https://en.wikipedia.org/wiki/Economic_history_of_Taiwan) — 1986년 대만 GDP 데이터. 신주과학단지는 1980년 12월 설립되었다.

[^N12]: Anfinsen, C. B. (1973). "Principles that govern the folding of protein chains." [Science, 181(4096), 223-230](https://www.science.org/doi/10.1126/science.181.4096.223) — 1972년 노벨 화학상 수상 업적 중 하나. 단백질 접힘이 아미노산 서열에 의해 결정된다는 가설을 제시했다.

[^N13]: [Nature: 'It will change everything': DeepMind's AI makes gigantic leap in solving protein structures](https://www.nature.com/articles/d41586-020-03348-4) — 2020년 11월 30일 CASP14 결과 발표 보도. AlphaFold 2 중위 GDT 92.4, CASP 주최자 John Moult의 “in some sense the problem is solved” 발언.

[^N14]: [DeepMind: AlphaFold reveals the structure of the protein universe](https://www.deepmind.com/blog/alphafold-reveals-the-structure-of-the-protein-universe) — 2022년 7월 28일 AlphaFold Protein Structure Database가 100만 종, 약 2억 개 단백질 구조를 포괄한다고 발표.

[^N15]: [Abramson, J., Adler, J., Dunger, J. et al. (2024). Accurate structure prediction of biomolecular interactions with AlphaFold 3. Nature 630, 493-500](https://www.nature.com/articles/s41586-024-07487-w) — 2024년 5월 8일 AlphaFold 3 발표. 단백질과 DNA / RNA / ligand / 이온 복합체 예측으로 확장했다.

[^N16]: [Wikipedia: Demis Hassabis](https://en.wikipedia.org/wiki/Demis_Hassabis) — Hassabis는 네 살 때 체스를 시작했고, 17세였던 1994년 Peter Molyneux와 《Theme Park》를 공동 개발했으며, 2010년 런던에서 DeepMind를 창업했고, 2014년 Google이 약 4억 파운드에 인수했다.

[^N17]: [中央研究院基因體研究中心](https://www.genomics.sinica.edu.tw/) — 원치후이 원장 재임기(2006-2016)에 구축된 당분자 단백질 구조 연구센터.

[^N18]: [PanSci 泛科學：2024 諾貝爾化學獎—— David Baker、Demis Hassabis、John Jumper 解開蛋白質摺疊難題](https://pansci.asia/archives/378388) — Content Curation Partner per MOU 2026-05-05. AlphaFold의 노벨 화학상 수상 논쟁, 구조생물학과 계산화학의 학문 경계 논의를 다룬다.

[^N19]: [PanSci 泛科學：AlphaFold 3 預測蛋白質與其他分子互動，藥物開發再升級](https://pansci.asia/archives/377917) — Content Curation Partner per MOU 2026-05-05. AlphaFold 3가 신약 개발과 효소공학에 미치는 하류 영향 분석.

[^N20]: [PanSci 泛科學：「人造腦」OI 挑戰 AI——培養皿裡的腦組織能取代矽晶片嗎？](https://pansci.asia/archives/366027) — Content Curation Partner per MOU 2026-05-05. Thomas Hartung 팀의 Johns Hopkins 인공 뇌 연구를 다루며, AI 경로 밖의 대안적 연산 방향으로 제시한다.
