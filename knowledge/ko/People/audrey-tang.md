---
title: '탕펑: 그녀의 유명한 결정은 매번 ‘천재’라는 표지를 거부하는 일이었다'
description: '8세에 동급생에게 걷어차여 의식을 잃었고, 14세에는 젠중 입학 추천을 거절했으며, 24세에는 트랜스젠더로 커밍아웃했지만 대변인이 되기를 거부했고, 35세에 내각에 들어가며 처음 내건 조건은 ‘사무실 없음’이었다. 2025년 12월 2일, 그녀는 스톡홀름에서 Right Livelihood Award를 수상했다. 무대 위에서 그녀가 말한 것은 ‘나’가 아니라 ‘우리’였다.'
date: 2026-05-16
author: 'Taiwan.md'
category: 'People'
subcategory: '教育與社會'
tags:
  [
    '인물',
    '탕펑',
    '디지털발전부',
    'g0v',
    '트랜스젠더',
    '프로그래밍',
    '열린 정부',
    'vTaiwan',
    'Plurality',
    'Right Livelihood Award',
  ]
readingTime: 14
lastVerified: 2026-05-16
lastHumanReview: true
featured: true
translatedFrom: 'People/唐鳳.md'
sourceCommitSha: 'da3bf446e'
sourceContentHash: 'sha256:08facc4576d7feb3'
sourceBodyHash: 'sha256:6a5330c17c122b19'
translatedAt: '2026-05-16T05:07:55+08:00'
---

# 탕펑: 그녀의 유명한 결정은 매번 ‘천재’라는 표지를 거부하는 일이었다

> **30초 개관:**
> 8세에 동급생에게 걷어차여 의식을 잃고 휴학했고, 14세에는 젠중 입학 추천을 거절했으며, 24세에는 트랜스젠더로 커밍아웃했지만 대변인이 되기를 거부했고, 35세에 내각에 들어가며 처음 내건 조건은 “사무실 없음”이었다. 2020년 새벽, 그녀는 g0v Slack에서 장밍쭝과 함께 코드를 고쳐 마스크 지도를 만들었다. 2025년 12월 2일에는 스톡홀름에서 Right Livelihood Award를 수상했다. 모두가 그녀의 개인사를 기대했지만, 무대 위에서 그녀가 강조한 것은 “우리”라는 두 글자였다. 세계는 그녀를 천재로 여긴다. 그러나 그녀의 유명한 결정은 매번 그 자리를 거부하는 일이었다.

## 2만 달러를 태운 마스크 지도

2020년 1월 말, 코로나19가 대만에서 확산되기 시작했다. 약국의 마스크 공급은 빠듯했고, 정부는 2월 6일부터 실명제 구매를 시행한다고 발표했다. 타이난의 하오샹 스튜디오 엔지니어 우잔웨이(Howard)는 2월 2일 새벽 직접 손을 움직여 Google Maps API로 주변 편의점의 마스크 재고를 확인할 수 있는 지도를 만들었다. 그는 새벽에 배포한 뒤 커뮤니티에 공유했다[^1].

점심을 먹고 컴퓨터 앞으로 돌아왔을 때, Google API 백엔드 청구서에는 이미 2만 달러가 찍혀 있었다. 24시간 안에 몰려든 사용량이 그만큼의 비용을 태운 것이다.

그날 탕펑은 g0v의 Slack 채널에 나타났다. 명령을 내리러 온 것이 아니었다. 그녀는 Google 엔지니어 팀과 조율해 우선 당장의 청구 비용을 눌러두었다. 동시에 g0v의 오랜 동료 몇 명, 즉 장밍쭝(kiang, 전 타이난 스마트시티 오피스 집행비서), 건강보험서 정보팀(장링즈, 천쯔위)과 함께 생각했다. 대만 전역 6000여 개 약국의 마스크 재고를 30초마다 동기화해 누구나 열 수 있는 지도에 올리려면 어떻게 해야 하는가[^2].

2월 6일 오전 8시, 건강보험서의 open data가 공식 공개되는 바로 그 순간 약국 마스크 구매 지도가上线됐다. 24시간 안에 100만 명 이상이 사용했다. 2월 15일까지 HackMD에는 관련 애플리케이션 101개가 누적됐고, g0v 커뮤니티는 140개가 넘는 도구를 만들어냈다[^2][^3].

장밍쭝은 훗날 자신의 강연 속기록에 이런 말을 남겼다.

> ✦ “정무위원은 정보 아키텍처에 매우 능숙해서, 우리가 어떤 요구를 제기해도 모두 이해했다. 가장 중요한 것은 탕펑에게 결정권이 있었고, 직접 코드를 고칠 수도 있었다는 점이다. 그래서 우리는 북상해 어느 장관에게 보고할 필요가 전혀 없었다.”[^4]

이 이야기의 주인공은 탕펑 한 사람이 아니다. 장밍쭝, 우잔웨이, 건강보험서 정보팀의 공무원들, g0v 커뮤니티의 수백 명 엔지니어, 그리고 탕펑 사무실에서 밤새 번갈아 코드를 고친 그 모든 사람들이다.

하지만 2020년 이후 외국 언론이 쓴 모든 판본에서 주인공은 그녀 한 사람이었다. BBC는 “Audrey Tang이 코드로 대만을 구했다”고 썼고, Wired는 “The Hacker Who Became Taiwan's Digital Minister”라고 썼으며, TIME은 그녀를 “팬데믹에 맞선 세계 지도자” 명단에 올렸다.

그녀는 모든 인터뷰에서 공을 다시 돌려놓는다. 그러나 “천재 장관이 대만을 구했다”는 서사는 40여 년 동안 그녀의 몸에 달라붙어 있었고, 그렇게 쉽게 떼어낼 수 있는 것이 아니었다.

## 8세에 동급생에게 걷어차여 의식을 잃고, 14세에 젠중을 거절하다

1981년 4월 18일, 탕펑은 타이베이에서 태어났다. 원래 이름은 탕쭝한이었다. 아버지 탕광화는 『중국시보』 전 부편집장이었고, 어머니 리야칭은 같은 신문의 취재팀 부주임이었다[^5].

그녀에게는 선천성 심장병이 있었다. 학교는 세 차례 지능검사를 실시했는데, 매번 “최소 160”이라는 결과가 나왔다. 이는 검사 도구의 최고 등급이었다. 8세 때 집에는 아직 컴퓨터가 없었다. 그녀는 Applesoft BASIC 프로그래밍 책 한 권을 읽고 종이에 컴퓨터 키보드와 화면을 손으로 그린 뒤, 버튼과 컴퓨터가 출력할 수 있는 내용을 적었다[^5].

하지만 “천재 아동”이라는 표지는 2026년에 그녀의 이름 옆에 가장 자주 붙는 수식어일지 몰라도, 1989년의 그 8세 아이에게 그런 자리는 없었다. 그 자리에는 집단폭행, 멍, 그리고 “너는 왜 죽지 않느냐”는 말만 있었다.

초등학교 6년 동안 그녀는 유치원 세 곳, 초등학교 여섯 곳을 옮겨 다녔다. 초등학교 2학년 어느 날, 교사가 시험지를 나눠주고 교실을 나갔다. 탕펑은 일찍 문제를 다 풀었다. 풀지 못한 몇몇 학생들이 손을 뻗어 그녀의 시험지를 빼앗으려 했다. 그녀는 시험지를 들고 뛰다가 넘어졌고, 그중 한 학생이 온 힘을 다해 그녀를 걷어찼다. 그녀는 벽에 부딪혀 의식을 잃었다[^6]. 훗날 그 학생은 한마디를 했고, 『금주간』은 이를 verbatim으로 남겼다.

> ✦ “너는 왜 죽지 않아? 네가 죽으면 내가 최고가 되잖아.”[^6]

그녀는 집에 돌아간 뒤 아무 말도 하지 않았다. 어느 날 어머니가 목욕을 시키다 그녀의 배에 든 멍을 보았고, 그 자리에서 휴학 절차를 밟기로 결정했다[^6].

어머니 리야칭은 훗날 독일로 가 대안교육을 연구했고, 1994년 우라이에 씨앗 친자실험소학을 세워 초대 교장을 맡았다[^7]. 1995년, 14세의 탕펑은 우라이 산중에서 칩거한 뒤 부모에게 선언했다. 더는 진학하지 않겠다. 젠중 추천 입학을 포기하겠다[^8].

그것은 “나는 너무 천재라 학교가 필요 없다”는 선택이 아니었다. 그것은 8세에 이미 자신을 숨기는 법을 배운 아이가 14세에 내린 결정이었다. “영재”라는 자리에 의해 규정되는 판본은 내가 원하지 않는다는 결정.

그녀는 훗날 여러 차례 말했다. “나는 현대 세계에 아직도 천재라는 말이 있다고 생각하지 않는다. 인터넷 시대에는 사실 모든 사람이 IQ 180이다.”[^9]

## 24세에 이름을 바꾸었지만, 트랜스젠더 대변인이 되기를 거부하다

그녀는 12세에 Perl을 배우기 시작했다[^10]. 19세였던 2000년에는 이미 캘리포니아 실리콘밸리의 소프트웨어 회사에서 엔지니어로 일하고 있었다[^11].

2005년 2월 1일, 24세의 그녀는 Pugs 프로젝트를 시작했다. Haskell로 Perl 6의 컴파일러와 인터프리터를 구현하는 프로젝트였다[^12]. Pugs는 Perl 커뮤니티에서 일종의 bootstrap 공정이었다. 하나의 언어가 다른 언어를 통해 자기 자신을 구현하는 일이었다. 그녀는 2001년부터 2006년 사이 CPAN에서 100개가 넘는 Perl 프로젝트를 시작했다[^13]. 국제 오픈소스 커뮤니티는 그녀를 Audrey 또는 au라고 불렀다.

2005년 말, 그녀는 자신의 블로그 blog.elixus.org에서 스스로 트랜스젠더임을 밝혔다[^14]. 그녀는 에스트로겐을 복용했지만 수술은 받지 않았다. 중국어 이름을 “탕펑”으로 바꾸었고, 영어 이름 Autrijus도 Audrey로 바꾸었다.

그 블로그 글에서 그녀는 이렇게 썼다.

> ✦ “현재든, 과거든, 미래든, 모두가 나를 여성 명사로 불러주면 기쁘겠다.”[^14]

아버지 탕광화가 인터뷰에서 보인 반응은 훗날 여러 매체에 verbatim으로 실렸다.

> ✦ “그 아이가 성별의 전환을 통해 더 행복해지고 창의력을 더 발휘할 수 있으며, 그것이 누구에게도 해를 끼치지 않는다면 받아들이지 않을 이유가 없다.”[^15]

그녀는 “트랜스젠더 대변인”이라는 자리를 거부했다. 2020년 내각 인사 자료표의 성별란에 그녀는 “없음”이라고 적었다. 당시 그녀는 기자에게 이렇게 설명했다[^16].

> ✦ “나는 ‘탈범주’다. 성별 논쟁에서 나는 어느 편에도 서지 않는다. 이 문제가 중요하지 않다고 생각한다는 뜻이 아니라, 논쟁이 어떤 문제도 해결하지 못한다고 생각한다는 뜻이다.”[^16]

Marie Claire와의 인터뷰에서 그녀는 또 하나의, 반복해서 인용되는 말을 남겼다.

> ✦ “길을 잃은 상태와 함께 지낼 수 있다면, 천천히 보이기 시작한다. 그것은 당신의 문제도 사회의 문제도 아니라 그 사이의 틈이라는 것을. 모든 것에는 틈이 있고, 틈은 빛이 들어오는 입구다.”[^17]

2010년부터 2016년까지 그녀는 Apple 고문을 겸했고, Siri 개발에도 참여했다. 시급은 1비트코인에 해당했다고 전해진다[^18]. 33세였던 2014년, 그녀는 Socialtext와 Apple 업무를 인수인계한 뒤 “은퇴”를 선언했다[^11].

## g0v와 해바라기 의사당: 공을 보이지 않는 사람들에게 나누다

2012년 10월, 그녀는 가오자량(clkao), 우타이후이(Kirby), 취샤오웨이(ipa) 등과 함께 g0v 영시정부를 공동 창립했다. 출발점은 행정원의 “경제동능 추진 방안” 광고에 대한 불만이었다. 예산 3300만의 정책 홍보 광고였지만, 보고 나서도 정부가 대체 무엇을 하려는지 알 수 없었다[^19].

g0v의 첫 프로젝트는 중앙정부 총예산 시각화였다. 두꺼운 예산서를 클릭 가능한 그림들로 펼쳐놓는 일이었다[^19]. 이후에는 맹전(MoeDict), 입법원영성(IVOD), 해바라기 학생운동 의사당 생중계가 이어졌다.

2014년 3월 18일 심야, 학생들이 입법원 의사당을 점거했다. 현장의 모든 선로, 카메라, 인터넷 생중계 장비는 탕펑이 직접 설치했다[^20].

하지만 그녀는 의사당에 한 시간만 머문 뒤 떠났다. 훗날 공시 PNN이 그녀를 인터뷰했을 때, 그녀는 이렇게 말했다.

> ✦ “의사당 내부에서 5개의 서로 다른 각도 카메라가 녹화하고 직접 송출하는 상황에서, 모든 활동은 이미 순수한 전시 공연과 의식이 되었다.”[^20]

그녀는 점거에도, 입장 표명에도 “관심이 없었다.” 그녀가 관심을 둔 것은 도구와 기술이었다. 동시에 그녀는 사비를 들여 정부 회의 속기록을 만들게 했다. 현장에 없는 사람도 완전한 대화를 읽을 수 있게 하기 위해서였다[^20].

해바라기 운동이 끝난 뒤, 2014년 4월 당시 정무위원이던 차이위링이 g0v 해커톤에 들어왔다. 그 순간부터 “정부”와 “g0v”라는 원래 대립하던 두 단어 사이에 중간지대가 자라기 시작했다[^21].

그 중간지대의 이름이 vTaiwan이다. 2015년부터 2018년까지 이 플랫폼은 26개 의제를 다뤘고, 그중 80%가 실질적인 정부 행동으로 이어졌다[^22]. 가장 유명한 사례는 Uber 규제 논의였다. 택시업계와 Uber 지지자들이 6년 동안 교착한 끝에, 일곱 가지 조건 아래 Uber가 합법화됐다[^22].

플랫폼의 핵심은 Pol.is 합의 엔진이다. 대량의 의견을 기계가 몇 개의 cluster로 정리해, 각 참여자가 “나는 누구와 생각이 매우 비슷한지, 누구와 매우 다른지, 어떤 주장은 모두가 동의하는지”를 볼 수 있게 한다. 그것은 투표하지 않고, 대립시키지도 않는다. 다만 차이의 형태를 그려낸다.

## 사무실 없음, 전면 공개 속기록, 주 3일 원격근무

2016년 8월 9일, 35세의 탕펑은 행정원장 린취안과 처음 만났다. 8월 15일, 그녀는 정무위원직을 맡는 데 동의했다. 9월 말 실리콘밸리에서 대만으로 돌아왔고, 10월 1일 행정원에 들어갔다[^23].

그녀가 사전에 합의한 세 가지 조건은 훗날 대만 공무 체계에서 처음 생긴 균열이 되었다. 매주 수요일과 금요일 원격근무, 모든 회의의 공개 속기록, 매일 행정원에 들어올 필요 없음[^23].

당시 린취안은 기자에게 이렇게 설명했다.

> ✦ “현재 행정원에는 원격근무 규범이 없지만, 그녀의 과거 장기적인 업무 방식은 모두 원격이었다. 업무에 영향이 없다면 컴퓨터를 통해 원거리에서 생각이나 정책 지시를 전달하는 것은 가능하다고 본다.”[^24]

그녀는 세 가지가 되었다. 대만 역사상 최연소 정무위원, 세계 최초로 공개적으로 트랜스젠더 정체성을 밝힌 장관급 정치인, 대만 최초의 “디지털 정무위원”이었다[^25].

행정원 안에 그녀의 고정 사무실은 없었다. 그녀는 청사 전체가 자신의 업무 공간이라고 말했다. 회의가 끝나면 속기록은 sayit.pdis.nat.gov.tw에 올라갔고, 누구나 검색할 수 있었다[^26].

그녀는 20명 규모의 팀을 꾸려 PDIS(Public Digital Innovation Space, 공공디지털혁신공간)라고 불렀다. 절반은 민간 전문가였고, 절반은 각 부처의 지원자였다. 여름방학에는 인턴 30명을 더했다[^26]. 그것은 관료제 조직이 아니었다. 하나의 작업 공간이었다.

2019년 그녀는 『Foreign Policy』 세계 100대 사상가에 선정됐다. 독자 투표 부문이었다[^27]. 언론은 그녀를 “세계에서 유일하게 공개적으로 트랜스젠더인 장관”, “프로그래밍 스타”라고 썼다. 그녀는 모든 인터뷰에서 공을 다시 돌려놓았다. 그러나 “천재 장관”의 이야기는 그녀가 한 말보다 훨씬 더 쉽게 전해졌다.

![2019년 5월 베를린 re:publica 디지털 사회 연례회의에서 연설하는 탕펑](/article-images/people/audrey-tang-re-publica-2019.jpg)
_2019년 5월 8일 베를린 re:publica 디지털 사회 연례회의 “Digital Social Innovation” 대담 현장. 탕펑과 Julia Kloiber가 함께 무대에 섰다. Photo: Jan Michalko. [CC BY-SA 2.0 via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Re_publica_19_-_Day_3_(32860400897).jpg).\_

## 보수적 아나키즘: 명령을 거부하고, 명령받기도 거부하다

탕펑은 스스로를 “보수적 아나키스트”라고 부른다. 표면적으로는 모순된 표현이다.

“보수”(conservative)는 기존에 존재하며 잘 작동하는 제도를 보존한다는 뜻이고, “아나키스트”(anarchist)는 권력 집중에 반대하고 위에서 아래로 내려오는 강제를 거부한다는 뜻이다. 이 두 단어를 붙여 쓰는 사람의 뜻은 대개 이렇다. 나는 기존 제도 안에 가치 있는 것이 있다고 믿지만, 누구에게도 권위로 타인에게 수용을 강제할 자격은 없다고 믿는다.

Rest of World와의 인터뷰에서 그녀는 거의 선언에 가까운 말을 남겼다.

> ✦ “Any top-down, coercion, whether it's from the capitalists or from the state, is equally bad.”(위에서 아래로 내려오는 어떤 강제든, 그것이 자본가에게서 오든 국가에게서 오든 똑같이 나쁘다.)[^28]

경제학자 Tyler Cowen과의 인터뷰에서 “당신의 역할은 무엇인가”라는 질문을 받았을 때, 그녀는 이렇게 말했다.

> ✦ “I'm working _with_ the government; I'm not working _for_ the government.”(나는 정부와 함께 일한다. 정부를 위해 일하는 것이 아니다.)[^29]

2020년 국제 컴퓨터과학 회의(ICFP) Q&A에서도 그녀는 이런 말을 던진 적이 있다.

> ✦ “In Taiwan we have this strange idea that broadband internet access is a human right. Everyone has broadband. And if you don't, it's my fault, personally.”(대만에는 이런 이상한 생각이 있다. 광대역 인터넷 접근은 기본 인권이라는 생각이다. 모든 사람에게 광대역이 있어야 한다. 만약 당신에게 없다면, 그것은 개인적으로 내 책임이다.)[^30]

그녀는 “인권”이라는 말을 무겁게 쓰지만, “개인적 책임”이라는 말은 다시 가볍게 쓴다. 그녀가 정부 직위에서 취하려는 태도는 “어딘가 비어 있으면 내가 가서 메운다”에 가깝다.

그녀의 작업 철학에는 humor over rumor라는 원칙이 있다. CoFacts 시스템이 viral disinformation을 감지하면, 그녀의 팀은 두 시간 안에 2분짜리 영상 한 편 또는 이미지 두 장, 200자 이내의 콘텐츠를 내놓아 유머로 허위정보에 대응한다. 이른바 2-2-2 원칙이다[^31].

2020년 2월의 “화장지 대란”은 같은 시기 국제 언론이 가장 많이 인용한 사례였다. 마스크와 화장지가 같은 펄프를 쓴다는 소문이 퍼지자 시민들이 공포에 빠져 사재기를 했다. 행정원은 몇 시간 안에 당시 행정원장 쑤전창의 “우리에게는 엉덩이가 하나뿐” 어깨 두드림 이미지를 내놓고, 원료 공급망이 다르다는 설명을 붙였다. 소문은 그날 바로 식었다[^31]. 그녀는 TED와 여러 국제 인터뷰에서 이를 humor over rumor의 전시 사례로 삼았다. 소문은 법으로 억누르는 것이 아니라, 그것보다 더 웃기고 동시에 사실을 집어넣은 이미지에 덮여 사라진다는 것이다.

2022년 8월 27일, 디지털발전부가 공식 출범했고 그녀는 초대 장관에 취임했다[^32]. 첫해 예산 정원은 598명, 공무 예산은 신대만달러 57억에 전향 예산 160억을 더해 총 217억이었다[^33].

재임 중 그녀는 디지털 회복탄력성을 추진했다. 영국 OneWeb과 룩셈부르크 SES의 저·중궤도 위성이 대만에 단말 장비를 배치하도록 설득했고, 20년 동안 손대지 않았던 『전자서명법』을 개정했으며, 111 정부 전용 단문메시지 플랫폼을上线해 사기 방지에 활용했고, 47개 A급 기관이 2년 안에 T-Road 통일 전송 표준을 도입하도록 요구했다[^34][^35].

그러나 그녀는 정면의 비판도 많이 받았다. 민중당 커원저는 “평균 한 사람당 3000만을 쓰는 셈인데, 이게 무슨 일인가?”라고 의문을 제기했다. 민진당 입법위원 류스팡은 “디지털부는 아직 자기 방향을 찾지 못했다”고 말했다. 국민당 입법위원 우이딩은 “시민들이 가장 관심을 갖는 온라인 사기에 대해 실질적 조치가 없다”고 말했다[^36][^37].

PDIS가 각 부처에 임명한 PO(공공참여 연락인) 공무원들조차 혼란스러워했다. 『보도자』가 인터뷰한 한 PO의 verbatim은 이렇다.

> ✦ “PO를 한 지 이미 두 달이 됐는데, 일이 하나 더 늘었다고 느낀다. 현재로서는 우리가 어디까지 개입할 수 있는지, 얼마나 권한을 받을 수 있는지 아직 잘 모르겠다... 앞으로 이런 플랫폼에서 우리의 역할이 무엇인지 모르겠다.”[^38]

그녀는 이 질문에 답할 수 없었다. 아니, 그녀의 답은 “당신이 스스로 결정하라”였다.

“명령이 아니라 시범”의 대가는 느림이고, 보기 좋은 KPI가 아니며, 2년이 지나도 “디지털부가 대체 무엇을 했는가”를 분명히 말할 수 있는 사람이 없다는 점이다. 그녀가 건 도박은 문화 전환이었다. 문화 전환은 성공하거나, 아니면 없는 것이다.

그러나 PDIS의 SayIt 공개 속기록 시스템은 그녀가 퇴임한 날까지 7000건이 넘는 회의의 전문 기록을 축적했다[^26]. 누구든 “Uber”, “마스크”, “LINE Pay” 같은 키워드를 입력하면, 당시 그녀가 업자, 공무원, 입법위원과 나눈 모든 말을 읽을 수 있다. 이 시스템은 그녀가 정부에 들어오기 전에는 존재하지 않았고, 그녀가 떠난 뒤에도 아무도 제거하지 않았다. 그녀는 이것을 한 문장의 치적 언어로 끝낼 수 없지만, 실제로 7년 치 검색 가능한 정부 대화 기록을 남겼다. 대만 정치사에서 이는 처음 있는 일이었다.

## 스톡홀름의 시상대에서 그녀는 “우리”라고 말했다

2024년 5월 20일, 라이칭더 총통 취임식이 끝난 그날 밤, 탕펑은 곧장 타오위안 공항으로 향했다. 이후 석 달 동안 그녀는 20개국을 밟았다[^39].

같은 해 4월, 그녀는 경제학자 Glen Weyl, 그리고 전 세계에 분산된 Plurality Community와 함께 『Plurality: The Future of Collaborative Technology and Democracy』를 공동 출간했다. 이 책은 CC0로 공개됐다. 즉 누구나 책의 전문을 어떤 용도로든 사용할 수 있으며, 저자 표시도, 비용 지불도, 동의 요청도 필요 없다[^40].

책 제목 “Plurality”를 그들은 하나의 한자 기호로 나타냈다. ⿻이다. 중국어로는 “衆”라고 쓰고, 발음은 zhòng에 가깝다. 이 글자는 Unicode에서 “표의문자 서술 문자” 가운데 하나로, “두 가지가 서로 엮여 있는” 구조를 설명하는 데 쓰인다. 그녀는 국제 언론에 ⿻가 강조하는 것은 “엮임”(interweaving)이라고 설명했다. 여러 개체의 차이가 제거되지 않으면서 하나의 전체적인 결을 이룬다는 뜻이다. 이 개념은 “천재”와 정반대다. 천재는 하나의 밝은 점이 주변의 회색에 의해 돋보이는 것이지만, ⿻는 모든 실이 다른 실에 감겨 있고 어느 하나도 빠질 수 없는 상태다.

vTaiwan이 Uber 규제 건을 처리한 사례는 그녀가 ⿻를 설명할 때 자주 꺼내는 예다. 택시업계와 Uber 지지자들은 6년 동안 교착했고, 마지막에는 일곱 가지 부가 조건 아래 Uber가 합법화됐다[^22]. 이 합의에서는 어느 쪽도 완전히 “이기지” 않았지만, 어느 쪽도 완전히 “지지” 않았다. 그녀는 그것이야말로 민주주의의 진짜 형상이라고 말한다. 모든 사람의 결을 같은 천에 짜 넣는 작업이라는 것이다.

10월 7일, 외교부는 그녀를 중화민국 무임소대사(Cyber Ambassador-at-Large)로 임명했다[^41]. 그녀의 개인 홈페이지 audreyt.org와 cyberambassador.tw 위에 올라와 있는 변하지 않는 opening은 이 문장이다.

> ✦ “I want to be a good enough ancestor for future generations.”(나는 미래 세대에게 부끄럽지 않은 충분히 좋은 조상이 되고 싶다.)[^42]

2025년 12월 2일, 스톡홀름, Right Livelihood Foundation의 시상식장. Right Livelihood Award는 “또 하나의 노벨상”(Alternative Nobel Prize)이라 불리며, 1980년 스웨덴계 독일 자선가 Jakob von Uexküll이 노벨상이 포괄하지 못하는 영역을 보완하기 위해 만들었다.

탕펑은 이 상을 받은 첫 대만인이다[^43]. Citation은 이렇게 적고 있다.

> ✦ “For advancing the social use of digital technology to empower citizens, renew democracy and heal divides.”(디지털 기술의 사회적 활용을 진전시켜 시민에게 권한을 부여하고, 민주주의를 새롭게 하며, 분열을 치유한 공로.)[^43]

수상 연설에서 그녀가 처음 말한 것은 자신이 무엇을 했는가가 아니었다. 그녀는 cyberspace, 즉 네트워크 공간이 무엇인지 말했다.

> ✦ “Cyberspace is a conflict region, and my work turns that conflict into an energy source for co-creation. It is time we work on peace in this zone.”(네트워크 공간은 갈등 지역이며, 나의 작업은 그 갈등을 공동 창조의 에너지원으로 바꾸는 것이다. 이제 우리는 이 구역에서 평화를 위해 일해야 할 때다.)[^43]

그리고 그녀는 Plurality 책 표지에 적힌 자신의 말을 다시 말했다.

> ✦ “The superintelligence we are looking for is already here. It's us.”(우리가 찾고 있는 초지능은 이미 여기에 있다. 그것은 우리다.)[^44]

그녀는 “또 하나의 노벨상”이라 불리는 상패를 받아들고, 시상대 위에서 초점을 “우리”로 돌렸다. 전 세계가 대만의 천재로 여기는 그녀는 다시 한 번 “천재”라는 자리를 거부했다.

1989년 영재반 교실에서 걷어차였던 8세 아이에서 2025년 스톡홀름 시상대에 선 44세의 사람까지, 그 사이에는 하나하나의 거부로 포장된 긴 길이 있다. 각각의 거부는 겉으로는 반항처럼 보이지만, 함께 놓고 보면 같은 동작의 여러 변주임을 알 수 있다. “우수한 개인”이라는 자리에 의해 정의되기를 거부하고, 자신을 다시 노드, 다리, 공간의 건설자라는 역할로 돌려놓는 동작이다.

그녀는 천재가 되기를 거부한다. 세계는 그녀를 천재로 여기기를 고집한다. 그러나 그녀는 이 논쟁에서 세계가 이기도록 한 적이 없다. 다만 세계가 그녀가 대체 무엇을 말하고 있는지 알아듣는 데 아주 오랜 시간이 걸릴 뿐이다.

![2021년 탕펑이 공개한 개인 서명 SVG](/article-images/people/audrey-tang-signature.svg)
_탕펑이 2021년 8월 공개한 개인 서명. 원래 일본 『문예춘추』 사용을 위해 제공했다. 저자: 탕펑 본인, [CC0 공공영역](https://commons.wikimedia.org/wiki/File:Audrey_Tang_signature_(51385705516).svg).\_

---

## 더 읽을거리

- [소다그린: 궁랴오의 작은 무대에서 ‘위딩쓰’ 투쟁까지, 20년에 걸친 음악 주권 탈환전](/music/蘇打綠) — 마찬가지로 2000년대에 부상한 대만의 이단아이며, “정해진 정체성에 의해 규정되기를 거부하는” 장기 투쟁이라는 점도 같다. 다만 무대는 정부가 아니라 음악 산업이다.
- [샤오상눙](/people/蕭上農) — INSIDE와 아이랴오리 공동창업자. 마찬가지로 “여러 영역을 가로지르는 것”으로 대만 기술계에서 자신의 역할을 정의했다.
- [우다유](/people/吳大猷) — 과학에서 기술로 이어지는 대만 지식 엘리트의 계승. 우다유는 중앙연구원 원장으로서 대만 과학연구 체제의 기초를 놓았다.

---

## 이미지 출처

이 글은 이미지 3장을 사용했으며, 모두 원 출처 서버의 핫링크를 피하기 위해 `public/article-images/people/`에 cache했다. 세 장은 Wikimedia Commons의 CC / CC0 라이선스 자료다.

- **hero**: [Portrait Audrey Tang (cropped)](<https://commons.wikimedia.org/wiki/File:Portrait_Audrey_Tang_(25915794061,_cropped).jpg>) — Photo: Camille McOuat, 2016-03-09 Paris, CC BY 2.0
- **scene-mid**: [Re:publica 19 - Day 3](<https://commons.wikimedia.org/wiki/File:Re_publica_19_-_Day_3_(32860400897).jpg>) — Photo: Jan Michalko, 2019-05-08 Berlin re:publica 디지털 사회 연례회의, CC BY-SA 2.0
- **signature**: [Audrey Tang signature](<https://commons.wikimedia.org/wiki/File:Audrey_Tang_signature_(51385705516).svg>) — 저자: 탕펑 본인, 2021-08-18, CC0 공공영역

## 참고자료

[^1]: [TechNews: 마스크 지도를 직접 만든 ‘키보드 구국’ 배후 팀을 밝히다(2020-02-23)](https://technews.tw/2020/02/23/expose-the-team-behind-mask-map/) — 우잔웨이 Howard가 새벽 deploy 후 API 청구서 2만 달러를 받았고, 탕펑이 Google 및 g0v와 조율한 타임라인을 상세히 서술한다.

[^2]: [장밍쭝 Medium: 약국 마스크 구매 지도上线(2020-02)](https://medium.com/%E6%B1%9F%E6%98%8E%E5%AE%97-kiang/%E8%97%A5%E5%B1%80%E5%8F%A3%E7%BD%A9%E6%8E%A1%E8%B3%BC%E5%9C%B0%E5%9C%96%E4%B8%8A%E7%B7%9A-54e11bd63e84) — 엔지니어 본인의 기록. verbatim “공식 자료는 2/6 오전 8시에야上线될 예정” 및 탕펑이 커뮤니티 참여 개발을 조율한 내용.

[^3]: [위생복리부 COVID-19 방역 핵심 의사결정망](https://covid19.mohw.gov.tw/ch/cp-4822-53563-205.html) — 정부 공식 서술 verbatim: “행정원 탕펑 정무위원이 민간 커뮤니티를 초청해 건강보험서 open data 자료를 통해 ‘방역 마스크 조회’ 응용 플랫폼을 제작했다.”

[^4]: [[TechNews: 마스크 지도를 직접 만들다(위 [^1]과 동일)](](https://technews.tw/2020/02/23/expose-the-team-behind-mask-map/)) — 자세한 내용은 원문 링크의 자료 보충 참조.

[^5]: [중국어 위키백과 〈탕펑〉 항목](https://zh.wikipedia.org/zh-tw/%E5%94%90%E9%B3%B3) — 출생 / 가족 배경 / 어린 시절 독학 BASIC 종이 키보드 등 기본 전기 자료.

[^6]: [금주간: 질투한 동급생에게 걷어차여 기절... 천재 탕펑, 어린 시절 여러 차례 자살을 생각하다(2020-11)](https://www.businesstoday.com.tw/article/category/183035/post/202011090020/) — 초등학교 2학년 교실 집단폭행 장면 + 동급생 발언 “너는 왜 죽지 않아” verbatim + 어머니가 목욕 중 멍을 발견하고 휴학을 결정한 내용.

[^7]: [중시신문망: 최연소 정무위원 탕펑, 리야칭은 교육개혁과 자기주도학습의 전범을 실천(2016-08-25)](https://www.chinatimes.com/realtimenews/20160825005980-260405) — 리야칭이 1992년 대만으로 돌아오고, 1994년 우라이 씨앗 친자실험소학을 창립해 초대 교장을 맡은 내용.

[^8]: [타이사운즈: ‘학교폭력’을 벗어나 자기주도학습으로! 탕펑이 14세 때 한 ‘중대한 발견’](https://www.taisounds.com/specialtopic/content/46/23226) — 14세에 우라이에서 칩거한 뒤 젠중 추천 입학을 거부한 내용.

[^9]: 여러 매체가 인용했으며, 본인이 여러 인터뷰에서 반복해 말한 문장: “나는 현대 세계에 아직도 천재라는 말이 있다고 생각하지 않는다”, “인터넷 시대에는 사실 모든 사람이 IQ 180이다.”

[^10]: [Wikipedia: Audrey Tang](https://en.wikipedia.org/wiki/Audrey_Tang) — “Tang started programming at the age of eight and began learning Perl at the age of 12”

[^11]: 중국어 위키백과 〈탕펑〉 항목(위 [^5]와 동일) — 2000년 19세에 이미 실리콘밸리 엔지니어로 일했고, 2014년 33세에 Socialtext + Apple 업무를 인수인계한 뒤 은퇴를 선언한 내용.

[^12]: [Wikipedia: Pugs (compiler)](https://en.wikipedia.org/wiki/Pugs_(compiler) — 위키백과 항목.

[^13]: [Wikipedia: Audrey Tang (English)](https://en.wikipedia.org/wiki/Audrey_Tang) — “Tang initiated over 100 Perl projects between June 2001 and July 2006, including the popular PAR archiver”

[^14]: 중국어 위키백과 〈탕펑〉 항목(위 [^5]와 동일) + 여러 매체의 verbatim 일치 인용: “현재든, 과거든, 미래든, 모두가 나를 여성 명사로 불러주면 기쁘겠다.” 원 출처는 2005년 블로그 blog.elixus.org.

[^15]: [금주간: 탕펑 아버지 인터뷰(2016-09)](https://www.businesstoday.com.tw/article/category/80407/post/201609010032/) — 아버지 탕광화 verbatim “받아들이지 않을 이유가 없다.”

[^16]: [대만여성 NMTH: 대만 최초 트랜스젠더 각료, 첫 디지털 정무위원 — 탕펑](https://women.nmth.gov.tw/?p=20105) — 탕펑 verbatim “나는 ‘탈범주’다” + 2020년 내각 인사 자료표 성별란에 “없음”이라고 적은 배경.

[^17]: [Marie Claire 대만: 어린 시절 괴롭힘을 지나, 탕펑은 말한다. “길을 잃은 상태와 잘 지내라”](https://www.marieclaire.com.tw/entertainment/story/52923/audrey-tang) — verbatim “모든 것에는 틈이 있고, 틈은 빛이 들어오는 입구다.”

[^18]: [중국어 위키백과 〈탕펑〉 항목(위 [^5]와 동일) +](https://www.britannica.com/biography/Audrey-Tang) — 자세한 내용은 원문 링크의 자료 보충 참조.

[^19]: [대만광화잡지: 시민 해커의 힘 g0v 영시정부](https://www.taiwan-panorama.com/Articles/Details?Guid=61281c3d-f79c-4db7-93d9-d18b29f90ba0) — 2012/10 출발점 + 중앙정부 총예산 시각화 + 공동창립자 명단.

[^20]: [공시신문 PNN: 해바라기 학생운동 보도(2014)](https://news.pts.org.tw/article/327548) — verbatim “현장의 모든 선로, 카메라, 모든 인터넷 생중계 장비는 그, 시민 해커 ‘탕펑’이 직접 설치했다” + 탕펑의 의사당 “전시 공연과 의식” 논평 + 사비로 속기록을 만든 내용.

[^21]: [보도자: 대화 공간을 만들다 — 탕펑의 기이한 여정](https://www.twreporter.org/a/g0v-audrey-tang) — verbatim 2014년 4월 차이위링이 g0v 해커톤에 들어간 일 + vTaiwan 기원.

[^22]: [Democracy Technologies: Consensus Building in Taiwan](https://democracy-technologies.org/participation/consensus-building-in-taiwan/) — vTaiwan이 2015-2018년 26개 의제를 처리했고 / 80%가 실질적 정부 행동을 이끌었으며 / Uber가 7개 조건 아래 합법화된 내용.

[^23]: [자유시보: 전통을 깨다, 탕펑 매주 수·금 ‘원격근무’(2016)](https://news.ltn.com.tw/news/politics/breakingnews/1859132) — 8/9 린취안과 첫 만남 / 8/15 동의 / 10/1 취임 / 입각 세 조건.

[^24]: [자유시보: 탕펑 원격근무, 린취안 “가능한 일이다”(2016)](https://news.ltn.com.tw/news/politics/breakingnews/1859246) — 린취안 verbatim “현재 행정원에는 원격근무 규범이 없지만... 가능하다.”

[^25]: 중국어 위키백과 〈탕펑〉 항목(위 [^5]와 동일) — 35세 대만 역사상 최연소 정무위원 + 세계 최초 공개 트랜스젠더 장관급 정치인.

[^26]: [pdis.nat.gov.tw 업무 기록 및 SayIt 공개 속기록 시스템](https://sayit.pdis.nat.gov.tw/) — PDIS 팀 20명 구조 + 절반 민간 + 절반 부처 지원자 + 인턴 30명.

[^27]: [Taipei Times: Audrey Tang named in “Top 100 Global Thinkers”(2019-01-25)](https://www.taipeitimes.com/News/front/archives/2019/01/25/2003708586) — Foreign Policy 세계 100대 사상가 선정(독자 투표 부문).

[^28]: [Rest of World: Audrey Tang on her “conservative-anarchist” vision for Taiwan's future(2020)](https://restofworld.org/2020/audrey-tang-the-conservative-anarchist/) — verbatim “Any top-down, coercion, whether it's from the capitalists or from the state, is equally bad”

[^29]: [Conversations with Tyler Ep.106: Audrey Tang](https://conversationswithtyler.com/episodes/audrey-tang/) — verbatim “I'm working with the government; I'm not working for the government”

[^30]: [Lindsey on X: ICFP 2020 Q&A 실시간 인용](https://x.com/lindsey/status/1297886318114963456) — verbatim “In Taiwan we have this strange idea that broadband internet access is a human right”

[^31]: [SwissInfo: Freedom of expression: humour over rumour](https://www.swissinfo.ch/eng/politics/freedom-of-expression-humour-over-rumour-lessons-from-taiwan-in-digital-democracy/46592080) — 자세한 내용은 원문 링크의 자료 보충 참조.

[^32]: [디지털발전부 공식 웹사이트: 역대 장관](https://moda.gov.tw/aboutus/ministers-since-2022/1527) — verbatim “2022년 8월 27일 2024년 5월 20일” 탕펑 임기.

[^33]: [자유시보: 탕펑이 디지털부 맡는다, 예산 정원 598명](https://news.ltn.com.tw/news/politics/breakingnews/4021987) — 자유시보 보도.

[^34]: [자유재경: 천재 IT 장관에서 자유 강사로, 탕펑 재임 중 3대 치적과 논란 돌아보기](https://ec.ltn.com.tw/article/breakingnews/4677986) — 디지털 회복탄력성 / OneWeb / SES 위성 / 전자서명법 개정 / 111 단문메시지 플랫폼.

[^35]: [INSIDE: 디지털발전부 창립 1주년! 탕펑의 2대 치적, 3대 논란 정리](https://www.inside.com.tw/article/32615-Taiwan-moda-anniversary) — 47개 A급 기관 T-Road 통일 전송 표준 + 동료 verbatim “과거의 단위에 비해 탕펑은 권력 이양을 더 원한다.”

[^36]: [원견잡지: 탕펑이 이끄는 ‘디지털발전부’ 출범 1년 앞두고 외부에서 치적 없다고 비판](https://www.gvm.com.tw/article/105627) — 류스팡 / 우이딩 verbatim 비판.

[^37]: [ETtoday: 디지털발전부 예산 211억, 커원저 놀라 “평균 1인당 3000만, 이게 무슨 일인가?”(2022-08-30)](https://www.ettoday.net/news/20220830/2327863.htm) — 커원저 verbatim 질의.

[^38]: [보도자: 열린 정부, 탕펑은 어떻게 공무원이라는 관문을 지나는가?](https://www.twreporter.org/a/open-government-audrey-political-commissar-challenges) — PO verbatim “PO를 한 지 이미 두 달이 됐는데... 어디까지 개입할 수 있는지 아직 잘 모르겠다.”

[^39]: [[자유재경: 천재 IT 장관에서 자유 강사로(위 [^34]와 동일)](](https://ec.ltn.com.tw/article/breakingnews/4677986)) — 자유시보 보도.

[^40]: [Plurality Institute: Book Launch of Plurality](https://www.plurality.institute/blog-posts/book-launch-plurality-the-future-of-collaborative-technology-and-democracy-by-e-glen-weyl-audrey-tang-and-the-plurality-community) — Glen Weyl + Plurality Community와 공저 / 2024년 4월 16일 출간 / CC0 공개.

[^41]: [중국어 위키백과 〈탕펑〉 항목(위 [^5]와 동일) +](https://cyberambassador.tw/) — 자세한 내용은 원문 링크의 자료 보충 참조.

[^42]: [audreyt.org](https://audreyt.org/) — 자세한 내용은 원문 링크의 자료 보충 참조.

[^43]: [Right Livelihood: Taiwan's Audrey Tang honoured with Right Livelihood Award(2025)](https://rightlivelihood.org/news/taiwans-audrey-tang-honoured-with-right-livelihood-award-for-advancing-digital-democracy-and-social-trust/) — Citation verbatim + Tang 수상 연설 verbatim “Cyberspace is a conflict region” 대목 + [Focus Taiwan 중앙사 영문판 보도](https://focustaiwan.tw/society/202512030022)

[^44]: cyberambassador.tw verbatim + Plurality 책 표지 철학 재서술 — “The superintelligence we are looking for is already here. It's us”
