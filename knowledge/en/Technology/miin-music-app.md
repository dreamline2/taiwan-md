---
title: 'Miin: The Same Claim That “Information Wants to Be Free” Led Ethan Tu to Build PTT, and Also into a Copyright Lawsuit'
description: 'In 1995, he used “information wants to be free” to set up PTT in an NTU dormitory; in 2017, he returned to Taiwan to build an AI system for identifying coordinated cognitive-warfare accounts; and, in the name of fighting disinformation, he was sued for aggregating other outlets’ news. The same conviction became both his weapon and the basis of a lawsuit, while Taiwan happens to stand at the front edge of a problem the world still has not solved.'
date: 2026-04-01
author: 'Taiwan.md Contributors'
category: 'Technology'
subcategory: '數位治理與公民科技'
tags:
  [
    'AI',
    'disinformation',
    'cognitive warfare',
    'digital resilience',
    'Ethan Tu',
    'copyright',
  ]
lastVerified: 2026-06-15
lastHumanReview: false
featured: false
translatedFrom: 'Technology/迷音Miin.md'
sourceCommitSha: '83f479d60'
sourceContentHash: 'sha256:aee5ba49019fb762'
sourceBodyHash: 'sha256:183d8e607cc534cd'
translatedAt: '2026-06-17T01:18:25+08:00'
image: '/article-images/technology/miin-homepage-2026.webp'
imageCredit: '迷音 Miin 官方網站（miin.cc）首頁截圖'
---

> **30-second overview:** In June 2026, a group of pro-Taiwan internet users on Threads urged people to switch to “Miin,” and the post shot past 3,000 likes. Miin is an open-source platform led by [PTT Bulletin Board System](/en/Technology/ptt-bulletin-board-system/) founder [Ethan Tu](/en/People/ethan-tu/). It markets itself around “free expression” and uses AI to identify coordinated accounts involved in [cognitive warfare](/en/Society/cognitive-warfare-against-taiwan/). Its method is counterintuitive: it does not judge whether news is true or false, but watches which usually silent accounts begin firing in sync the moment a press conference starts. But at the end of 2025, NextApple sued Miin, accusing it of using more than 250 of its news articles without authorization. A person who built PTT and opposed platform censorship returned to Taiwan to build a tool for identifying “who is manipulating the conversation,” and then aggregated other people’s news in order to fight disinformation. The same claim that “information wants to be free” has been his conviction for 30 years, Miin’s current selling point, and now the lawsuit against him.

One afternoon in June 2026, a post urging people to “leave Meta and switch to Miin” surged to 3,200 likes within 12 hours.[^1] The call came from a group of pro-Taiwan internet users. Some had seen their Facebook accounts repeatedly reported and restricted, prompting them to look for a platform built by Taiwanese people themselves. “Another digital migration for seventh-graders: let’s go, let’s go to miin,” one person wrote, linking Facebook to Threads and then to Miin as part of a single road on which Taiwanese people keep growing new spaces for themselves.[^1]

They may not have known that a version of this scene had already happened in Taiwan 30 years earlier. The person behind Miin also acted in 1995 on the phrase “information wants to be free,” building a place in an NTU dormitory where Taiwanese people could argue, fall in love, and organize. That place was PTT. From that computer in the dormitory to Miin today, the same conviction runs through everything: information should flow freely. That sentence led him to build PTT, to oppose platform censorship, to use AI to detect coordinated accounts steering opinion from behind the scenes, and to aggregate other outlets’ news in order to fight disinformation. The same sentence is the weapon in his hand and the cause of action in a lawsuit. That is the most fascinating and most difficult part of Miin’s story.

## After That 486, He Circled the Earth

[Ethan Tu](/en/People/ethan-tu/) was born in Kaohsiung in 1976. In September 1995, while he was a second-year student in National Taiwan University’s Department of Computer Science and Information Engineering, he used a self-assembled 486 computer in a men’s dormitory, running Linux and open-source software, to set up a BBS under the code name “ptt.” That became PTT, and Tu was its first station master.[^2] The English Wikipedia entry still records this: PTT was “founded on 9 September 1995 by Yi-Chin Tu（杜奕瑾）,” when he was a sophomore in NTU’s Department of Computer Science and Information Engineering.[^2]

After founding the site, his path for a time moved far away from cybersecurity and public opinion. In 2003, he went to the United States to conduct genetic-sequencing research at the National Institutes of Health (NIH). In 2006, he joined Microsoft. In 2012, he entered Microsoft’s AI division as a Principal Development Manager and participated in the development of the voice assistant Cortana. One clarification is needed to avoid misunderstanding: he was a major R&D figure on the product team, while outside accounts sometimes describe him as Cortana’s “global head.” That role was in fact held by Mike Calcagno.[^3]

Laid out this way, his résumé shows that he was never merely an engineer. Genetic sequencing is about finding meaningful patterns in vast datasets; voice assistants are about teaching machines to understand human intent. Both involve reading signal out of noise. In March 2017, Tu brought that skill set back to Taiwan and founded [Taiwan AI Labs](/en/Technology/taiwan-ai-labs/), which presented itself publicly as Asia’s first nonprofit AI research organization.[^4] This time, the old problem of signal and noise would be aimed at the thickening haze on social platforms.

```tw-timeline
From PTT to Miin: Ethan Tu’s 30 years, circling the globe and returning to the same sentence
1995 | The 486 in the dormitory | As an NTU computer science sophomore, used a self-assembled computer to set up PTT and became its founding station master
2006 | Off to Microsoft | Later joined the AI division and participated in development of the voice assistant Cortana
2017 | Returned to Taiwan to build nonprofit AI | Founded Taiwan AI Labs
2022 | “One in every four accounts” | During Nancy Pelosi’s visit to Taiwan, used behavioral detection to count cognitive-operation accounts
2025 | Sent to court | Miin scraped more than 250 NextApple articles and was referred for investigation under the Copyright Act
2026 | Let’s go, let’s go to miin | Pro-Taiwan internet users treated Miin as a refuge from Meta
Source: This article’s compilation from Wikipedia, Taiwan AI Labs, and NextApple
```

## It Does Not Check Whether News Is True; It Watches Who Fires at the Same Second

Miin did not appear out of nowhere. It stitched together two earlier lab projects: “Reporter Quick Copy” in 2017, which used AI to automatically rewrite popular PTT posts into draft news articles, and “Islanders’ Satellite,” developed in cooperation with NTU computer science professor Chen Yun-nung.[^5] After the two converged, Miin placed reports on the same event from more than 20 domestic digital media outlets alongside Facebook and PTT discussions, letting readers see how the same matter appeared under different standpoints, while marking accounts that might be part of coordinated operations.

What truly sets it apart is the underlying judgment it makes about disinformation. Most people instinctively assume that fighting disinformation means checking whether each post is true or false. Tu’s view is almost the opposite. In a talk hosted by the Taiwan FactCheck Center Education Foundation, he put it bluntly: “Using artificial intelligence to judge whether news content is true is very dangerous. Therefore, Taiwan AI Labs’ research method analyzes behavioral propagation and information-diffusion patterns, rather than relying on AI to detect whether content is true or false.”[^6]

In other words, the algorithm does not read what a post says or whether it is true. It reads how the post is pushed, who relays it, and at what moment. Coordinated accounts have some distinctive habits: they are usually quiet and not especially active, but at key moments they simultaneously release similar, attacking, or misleading messages; “as soon as one amplifier sends a message, the others retweet it.”[^7] During COVID, one example he repeatedly cited involved the period when attacks on World Health Organization Director-General Tedros Adhanom Ghebreyesus were most intense on PTT: around 2 p.m., exactly when Taiwan’s pandemic press conferences began. The active hours of these coordinated accounts were nine to five, as if steering public opinion were someone’s office job.[^7]

Technically, the system clusters suspicious accounts according to “synchronized behavior” and “active hours.” In the lab’s analysis of the Israel-Hamas war, for example, 71,774 suspicious accounts were organized into 9,737 distinct coordinated groups.[^8] The point was never what any one account said, but which sets of accounts always moved and fell silent together. Viewed in isolation, each one might look like an ordinary internet user. Stacked together, a rhythm emerges that is too orderly to feel natural.

```tw-versus
Traditional fact-checking: asks about content | Miin: asks about behavior
Judges whether each post is true or false | Does not ask true or false; watches how accounts move
By the time a fact-check is published, the disinformation has often already spread | Identifies coordinated accounts that are “usually quiet, but fire in sync at key moments”
Difficulty: Who is qualified to determine truth? | Difficulty: How much synchronization counts as coordination, and the threshold is still set by people
Source: Ethan Tu interview remarks, Taiwan FactCheck Center Education Foundation
```

> **Curator’s note:** The design choice to “catch behavior, not content” is worth pausing over, because it elegantly sidesteps the sharpest accusation against content moderation. If you delete a post, you must first claim that you know it is false, and “who is qualified to determine truth” is precisely one of the hardest questions to settle in free-speech debates. Tu shifts the object of judgment from “is this sentence correct?” to “are this group of accounts behaving normally?” In effect, he turns a value judgment into a statistical one. That move is clever. What must also be stated honestly is that it does not eliminate the problem of “who decides.” It merely moves the question from “who decides whether content is true” to “who decides what kind of synchronization counts as manipulation.” Where the threshold is set, and how much synchronization counts as coordination, remain human decisions. Only this time, the definition is encoded in an algorithm that has not yet been made public.

## How Solid Is a Number Like “One in Every Four Accounts”?

Miin deserves serious attention because it connects to a real international front line. Taiwan is a heavily targeted site of foreign information manipulation; in academia this is already a consensus, not marketing copy. A 2022 paper in Oxford University Press’s _Journal of Global Security Studies_ defined cognitive warfare as “controlling others’ mental states and behaviors by manipulating environmental stimuli,” and explicitly identified Taiwan as a front-line case.[^9]

The number most widely associated with Tu was counted on that front line. In an interview, he said that after the outbreak of the Russia-Ukraine war, “one in every 10 accounts” posting related commentary on Twitter involved cognitive operations; during Nancy Pelosi’s visit to Taiwan in August 2022, the proportion was even higher: “one in every four accounts” was related to cognitive operations.[^10] The “one quarter” figure is vivid and easy to repeat, but readers should remember its nature: it appeared in a January 2023 media interview as Tu’s oral observation, not in a public, peer-reviewed technical report. The denominator, thresholds, and sampling method are all invisible to outsiders.[^10]

The lab has also produced several sets of somewhat firmer first-hand data. For the 2024 European Parliament elections, it said it detected 20,041 behaviorally abnormal coordinated accounts, accounting for about 12.58% of related discussion volume.[^11] For Taiwan’s 2024 presidential election, it calculated more than 30,000 coordinated-account groups, with two leading Facebook groups alone controlling 45.71% of the operational volume.[^12] These numbers, with their decimal points, look more precise than “one in every four.” But for outside researchers to reproduce and verify the methodology behind them, there is not yet a public peer-review channel. Academic work on detecting this kind of “coordinated inauthentic behavior” has also long warned of a common criticism: that such criteria “lack objectivity,” and that healthy disagreement may be misclassified as manipulation.[^13] The threat is real, and academics take this front line seriously. But laying out the scale marks and making the detection withstand external scrutiny are the steps it must still take to grow from “one lab’s observation” into a public tool everyone can trust.

```tw-stat
One in every four | Twitter accounts involved in cognitive operations during Pelosi’s visit to Taiwan | Oral observation in an interview; method not public
12.58% | Share of coordinated-account volume in the 2024 European Parliament elections | First-hand lab report
45.71% | Operational volume of two major Facebook coordinated groups in Taiwan’s 2024 election | First-hand lab report
Source: Taiwan AI Labs, Central News Agency
```

## He Fears Platforms Controlling Public Opinion, Yet Built a Ruler for Deciding “Manipulation”

Tu’s opposition to content moderation on PTT is a position he has stated clearly. In a 2024 interview with National Public Radio (NPR), he said that if content moderation becomes too strong, the system operator can in turn control the opinion of the whole society; Taiwan is a democratic society, and such matters should be decided by the people themselves.[^14] Put that sentence next to what he is doing at the lab, and an honest tension surfaces: someone so wary of “system operators controlling public opinion” has himself built a system that uses an unpublished algorithm to judge who is “manipulating” the conversation.

This tension does not need to be pointed out by others; he has genuinely run into it himself along the way. In 2022, he publicly supported the highly controversial Digital Intermediary Services Act, a draft law that would have given the government more power to intervene in online content. PTT users blasted the site’s founder with downvotes, and the draft was eventually sent back for reconsideration by the National Communications Commission after major backlash.[^15] It is uncomfortable to place together a person who told NPR that “the people should decide” and the same person’s support for a bill criticized as expanding government censorship powers. But it also honestly shows one thing: even those most alert to censorship, once placed in the position of defending against disinformation, can be pulled along by the same dilemma.

A more personal episode occurred in February 2023. Tu announced that “208 PTT accounts” had acted in coordination to hype the issue of egg prices. Internet users immediately challenged him to “provide evidence when you speak.” He chose to respond with sarcasm, but never publicly explained how those 208 accounts had been classified as coordinated.[^16] When the deciding algorithm is opaque, those named can only choose between “believe him” and “downvote him into oblivion.” That is precisely the situation he had least wanted PTT to reach. One clarification should be added: the label “Chinese Communist collaborator” that some internet users pinned on him was not his wording, and should not be treated by any side as a conclusion.

## To Fight Disinformation, He Scraped Other People’s News

If algorithmic opacity remained a matter of debate, the case at the end of 2025 went straight into the investigative process. In December 2025, NextApple accused the Miin website and app, launched by Taiwan Intelligent Engine Co., Ltd., of “illegally stealing more than 250 NextApple news reports without authorization, and reproducing and publishing them without permission” for members to read and discuss.[^17] NextApple’s parent company, Long Cheng Creative, filed a complaint under Article 91, Paragraph 1 of the Copyright Act. After Tu and Taiwan Intelligent Engine’s current responsible person, Liao Qun, appeared for questioning, they were referred for prosecution on suspicion of violating the Copyright Act. The alleged offense carries a maximum penalty of three years’ imprisonment plus a fine.[^17]

Both sides’ accounts need to be placed on the table. Tu and Liao admitted that Miin did scrape news from various media outlets, but denied profiting from it.[^17] The report used the phrase “stole again” and also mentioned that NextApple was not the only outlet; other media had also filed complaints against Tu and others. Here, a gap is worth neutrally pointing out: Miin’s public positioning has always been “nonprofit and open source,” but the entity sitting in the defendant’s seat is a for-profit company, Taiwan Intelligent Engine Co., Ltd. The nonprofit ideal and the for-profit legal person thus sit side by side in the same case.

Nor was this Tu’s first time entering a legal gray zone over “aggregating other people’s content.” “Reporter Quick Copy,” mentioned earlier, also used AI in 2017 to turn popular PTT posts into news articles and was accused by an entertainment company of damaging business credit. But that was a different legal issue, and in February 2023 the Taipei District Prosecutors Office issued a non-prosecution disposition due to insufficient evidence. That was non-prosecution, far from a conviction, and the two matters should not be conflated.[^18] It must also be made clear that as of this writing, the copyright case remains under investigation and in the judicial process, with no final judgment. This article does not reach any conclusion on the guilt or innocence of either side.

> **Curator’s note:** Put this lawsuit back inside the sentence that runs through the article, and it appears as the same impulse colliding with its own two faces. In one direction, “information wants to be free” means “other people’s news should not be locked behind paywalls; it should be aggregated so the public can compare it.” In the other direction, it means “I reproduced 250 of your reports without authorization.” The same conviction does not contain a natural boundary between “the public interest of fighting disinformation” and “infringing someone else’s economic rights in a work.” It depends on whether you stand with the person scraping data or with the person being scraped. In this case, whistleblower and infringer may be two names for the same act. Who ultimately gets to name it is now in the hands of prosecutors and judges. This is Taiwan’s version of the global battle between AI and creators, including _The New York Times_ lawsuit against OpenAI.

## Noah’s Ark, or Just a Clunky Forum

Return to the migration wave of June 2026. Put it back into its full context, and something more interesting becomes visible. The organizers told this line of development quite completely: about three years earlier, the green camp and pro-Taiwan users wanted to open a community space outside Facebook, and one person after another moved to Threads. Today, Threads has “become the world’s most-used large Taiwanese family group.” Now, Miin is being pushed to the foreground as an “open-source, nonprofit news and social aggregation platform” built by Taiwanese people themselves.[^1] Facebook to Threads to Miin is narrated as one migration chain, and this is exactly the script that [Taiwan’s history of online community migrations](/en/Technology/taiwan-online-community-migration/) has staged again and again.

But within the same wave of enthusiasm, the voices throwing cold water on it are the ones most worth hearing. The sharpest criticism precisely identified Miin’s lineage. Some people pointed out that Miin “cannot be pushed out” because it is “forum-style” rather than “waterfall-style”: like PTT and Dcard, each post initially shows only a title and users must click in to see the body, unlike Facebook, X, or Threads, where one screen can scroll past five posts. It cannot even like comments or reply under comments, making it feel awkward to use.[^1] Placing Miin alongside PTT accidentally says something true: these really are products made by the same person. Even that forum-like “poor transmissibility” is inherited from the same line.

That is the honest full picture of this migration wave: the patriotic push is real, the 3,200 likes are real, and the friction in product experience is also real. For now, it is a burst of discussion and a promotional wave, not yet a completed migration. It looks more like a refuge lit up by enthusiasm, but one that has not yet finished making itself smooth and convenient to use.

> **Curator’s note:** There is a gentle irony here. A platform designed to detect “coordinated operations” is this time relying on a coordinated wave of patriotic promotion: the same group of people posting in sync, reposting one another, and moving together at a key moment. Of course, promoting one’s own side and foreign manipulation are vastly different in motive and legitimacy; this comparison is not meant to equate the two. It simply reminds us that “coordination” as a signal is neutral. What label gets attached to it always depends on who is making the judgment, and for what purpose.

## The Same Sentence Is a Conviction, a Selling Point, and the Reason for Being a Defendant

Open the miin.cc homepage, and the line at the top reads: “Enjoy everyday moments anytime; speak freely!”[^19] This is how Miin defined itself in 2026. It has already moved far beyond the news-aggregation tool it was in 2024. Officially, it says it lets users “discuss news, share stories, and record daily life without obstruction,” uses AI to “create a creative experience tailored to you,” and helps users “see through different positions, coordinated operations, and factuality in events.”[^19] Side-by-side news, coordination detection, social posting, AI creation, and voice radio are all packed into the same app. And the phrase “speak freely” really does mean it wants you to make your voice heard.

Those four Chinese characters, “自由發聲,” stitch the whole matter into a closed loop.

They are Tu’s conviction, unchanged for 30 years. PTT on that 486 in a dormitory in 1995 and Miin on a phone in 2026 are two landings of the same impulse, separated by three decades: platforms should not decide on your behalf what you are allowed to say. They are also Miin’s sharpest selling point today. When pro-Taiwan internet users’ Facebook accounts were repeatedly reported and Meta no longer felt wholly trustworthy, the promise of “a platform of our own, built by Taiwanese people, where we can speak safely” landed precisely among those looking to preserve a space for themselves. At the same time, they are why Miin was taken to court: the same claim that “information wants to be free” led it to scrape more than 250 NextApple articles into its own database. It was then referred for investigation under the Copyright Act. The case is still ongoing; there has been no judgment.

So the next time you scroll past a post saying “let’s go, let’s go to miin,” remember: you are not only seeing another digital migration. You are watching an idea walk through half a lifetime, from a sophomore’s ideal that information should flow freely, into an algorithm for catching disinformation, into a lawsuit with no judgment yet, and into a place a group of people wants to defend for themselves. Where to draw the line between information freedom and copyright, and how to defend against disinformation without turning that defense into a new form of censorship, are lessons the whole world is still learning. Taiwan happens to stand very near the front. Someone is genuinely building, and people are genuinely arguing over it. The next time someone invokes “the public interest” to take something away, the question worth asking together is where that line is drawn, and whether it has been laid out for everyone to see. The right to lay it out for scrutiny has always been in our hands.

## Further Reading

- [Ethan Tu](/people/杜奕瑾) — The 30 years of the person who built PTT with a 486 computer, led Cortana work at Microsoft, and returned to Taiwan to build nonprofit AI
- [Taiwan AI Labs](/technology/台灣人工智慧實驗室) — The nonprofit AI institution behind Miin, from TAIDE to cognitive-warfare prevention
- [Cognitive warfare](/society/認知作戰) — Why Taiwan is described in academic work as a front line in this information war
- [Taiwan’s history of online community migrations](/technology/台灣網路社群遷徙史) — From BBS and Wretch to Threads, the story of Taiwanese people moving house online again and again

## Image Sources

- Lead image: Screenshot of the homepage of Miin’s official website ([miin.cc](https://miin.cc/)), captured in June 2026 and used for the editorial purpose of introducing the platform.

## References

[^1]: [Public discussions about miin on Threads](https://www.threads.com/search?q=miin) — Captured on June 15, 2026; includes calls to leave Meta and switch to Miin, with about 3,200 likes; the phrase “another digital migration for seventh-graders: let’s go, let’s go to miin”; the Facebook → Threads → Miin migration-chain narrative; and user-experience criticisms including “forum-style vs. waterfall-style” and inability to like or reply to comments. The cited like count is an approximate value at the time of capture and remains subject to change.

[^2]: [杜奕瑾 — Wikipedia](https://zh.wikipedia.org/zh-tw/杜奕瑾) — Born in Kaohsiung in 1976; in September 1995, as a second-year NTU computer science student, set up PTT in a dormitory using a 486 computer, Linux, and open-source software under the code name “ptt,” becoming the founding station master. For the English wording, see [PTT Bulletin Board System — Wikipedia](https://en.wikipedia.org/wiki/PTT_Bulletin_Board_System): “The main site was founded on 9 September 1995 by Yi-Chin Tu（杜奕瑾）... then a sophomore in the Department of Computer Science and Information Engineering at National Taiwan University.”

[^3]: [杜奕瑾 — Wikipedia](https://zh.wikipedia.org/zh-tw/杜奕瑾) — Went to the United States in 2003 for genetic-sequencing research at the NIH; joined Microsoft in 2006; entered Microsoft’s AI division in 2012 as a Principal Development Manager and participated in Cortana development. Note: Cortana’s global head was Mike Calcagno, a different person. Tu did not hold that position; the article should not conflate the two.

[^4]: [PTT Founder Ethan Tu Returns to Taiwan to Establish AI Lab — Business Next](https://www.bnext.com.tw/article/44267/founder-of-ptt-ethan-tu-back-to-taiwan-to-establish-an-ai-lab) — Tu returned to Taiwan in March 2017 and founded Taiwan AI Labs, presenting it as Asia’s first nonprofit AI research organization and promoting it in the nonprofit form of the Taiwan Artificial Intelligence Development Foundation (2017).

[^5]: [Miin — Wikipedia](https://zh.wikipedia.org/zh-tw/迷音) — “Miin integrated two earlier Taiwan AI Labs research projects, ‘Reporter Quick Copy’ and ‘Islanders’ Satellite.’ It was led and developed by PTT founder Ethan Tu in cooperation with National Taiwan University Department of Computer Science and Information Engineering professor Chen Yun-nung.”

[^6]: [Disinformation and Cognitive Warfare: Ethan Tu on AI and Media Literacy — Taiwan FactCheck Center Education Foundation](https://education.tfc-taiwan.org.tw/education_resources/7861) — Tu verbatim: “以人工智慧判斷新聞內容真實與否，是非常危險的事情，因此『台灣人工智慧實驗室』的研究方式，是從行為傳播、訊息傳散的模式來分析，而不靠 AI 偵測內容真假。” (2022)

[^7]: [Coordinated accounts active nine to five; attacks concentrated during pandemic press conferences — Liberty Times Finance](https://ec.ltn.com.tw/article/breakingnews/3989765) — “The period when PTT attacks were most intense was around 2 p.m.... the start time of the pandemic press conference”; users with “coordinated behavior” were active “nine to five”; for coordinated accounts, “as soon as one amplifier sends a message, the others retweet it” (2022).

[^8]: [Analysis of Cognitive Warfare and Information Manipulation in the Israel-Hamas War — Taiwan AI Labs](https://ailabs.tw/uncategorized/analysis-of-cognitive-warfare-and-information-manipulation-in-the-israel-hamas-war-2023/) — “71,774 dubious user accounts... organized into 9,737 distinct coordinated groups”; the system clusters accounts according to synchronized behavior and active hours (2023).

[^9]: [How China’s Cognitive Warfare Works — Hung & Hung, Journal of Global Security Studies (Oxford University Press)](https://academic.oup.com/jogss/article/7/4/ogac016/6647447) — Defines cognitive warfare as “controlling others’ mental states and behaviors by manipulating environmental stimuli,” and uses Taiwan as a front-line case (2022).

[^10]: [During Pelosi’s Visit to Taiwan, One in Every Four Accounts Involved Cognitive Operations — Central News Agency](https://www.cna.com.tw/news/ait/202301200012.aspx) — “Taiwan AI Labs observed that after the outbreak of the Russia-Ukraine war last year, one in every 10 accounts posting related comments on Twitter involved cognitive operations; during then-U.S. House Speaker Nancy Pelosi’s visit to Taiwan last August, one in every four accounts was related to cognitive operations.” This was a January 2023 interview report, not a peer-reviewed technical report; the denominator, classification threshold, and sample scope were not public (2023).

[^11]: [Taiwan AI Labs Founder Ethan Tu at NATO Summit — Taiwan AI Labs](https://ailabs.tw/news-room/taiwan-ai-labs-founder-ethan-tu-at-nato-summit/) — Detected 20,041 behaviorally abnormal coordinated accounts in the 2024 European Parliament elections, accounting for 12.58% of related discussion volume; first-hand data, methodology not publicly peer-reviewed (2024).

[^12]: [2024 Taiwan Presidential Election Information Manipulation AI Observation Report — Taiwan AI Labs](https://ailabs.tw/uncategorized/2024-taiwan-presidential-election-information-manipulation-ai-observation-report/) — More than 30,000 coordinated-account groups in Taiwan’s 2024 presidential election; two leading Facebook groups (#61009/#61019) controlled 45.71% of operational volume; first-hand data, methodology not publicly peer-reviewed (2024).

[^13]: [On the Reliability of Coordinated Inauthentic Behavior Detection — arXiv](https://arxiv.org/pdf/2105.07454) — “Healthy disagreements may be wrongly flagged as manipulative... creating a chilling effect on free expression”; see also [arXiv:2408.01257](https://arxiv.org/html/2408.01257v1): “the criteria to establish the legitimacy of user behaviors lack objectivity” (2021/2024).

[^14]: [Taiwan deals with lots of misinformation, and it’s harder to track down — NPR / KLCC](https://www.klcc.org/npr-world-news/2024-01-11/taiwan-deals-with-lots-of-misinformation-and-its-harder-to-track-down) — Tu said that once content moderation becomes too strong, “the system operator can control the opinion of the society”; Taiwan is a democratic society and “The people should decide” (2024, English interview; paraphrased here).

[^15]: [Ethan Tu’s Support for the Digital Intermediary Services Act Draws Heavy PTT Backlash — Newtalk](https://newtalk.tw/news/view/2022-08-20/804618) — Tu’s public support for the Digital Intermediary Services Act triggered strong backlash from PTT users (2022); the draft was later sent back by the NCC after public backlash. See [NCC sends digital intermediary bill back to square one — Taipei Times](https://www.taipeitimes.com/News/taiwan/archives/2022/09/08/2003784968) (2022).

[^16]: [After Identifying 208 Coordinated PTT Accounts, Internet Users Demand Evidence; Ethan Tu Responds — Liberty Times](https://news.ltn.com.tw/news/life/breakingnews/4220960) — Egg-price coordination case; internet users said “you need evidence when you speak,” and Tu responded with sarcasm without publicly disclosing the methodology for judging coordination; “Chinese Communist collaborator” was a label pinned on him by internet users, not Tu’s wording (2023).

[^17]: [Miin Suspected of Illegally Stealing More Than 250 NextApple Articles — NextApple](https://news.nextapple.com/life/20251219/6FFCB8F55781BC5D3F473E9FA0E9FC0D) — “The Miin website and app launched by Taiwan Intelligent Engine Co., Ltd. illegally stole more than 250 NextApple news reports without authorization, reproducing and publishing them without permission to provide them for members to read and discuss”; Long Cheng Creative filed a complaint under Article 91, Paragraph 1 of the Copyright Act; Tu and Liao Qun were referred for prosecution, with a maximum penalty of three years’ imprisonment plus a fine; both admitted scraping but denied profit-making. Other media also filed complaints; see [Yahoo News repost](https://tw.news.yahoo.com/ai爬蟲再盜-壹蘋-ptt-創世神-杜奕瑾遭法辦-140400731.html). Case status (as of 2026-06, cross-checked across sources): no new public developments after referral for investigation; still under investigation, with no indictment, non-prosecution disposition, or judgment (2025).

[^18]: [“Reporter Quick Copy” AI Reposted Popular PTT Posts, Was Accused of Damaging Business Credit, and Received Non-Prosecution — ETtoday](https://www.ettoday.net/news/20230202/2432146.htm) — “Reporter Quick Copy” used AI to turn popular PTT posts into news articles and was accused by an entertainment company of damaging business credit. In February 2023, the Taipei District Prosecutors Office issued a non-prosecution disposition due to “insufficient evidence”; this is a different legal issue from the copyright case, and was non-prosecution rather than a conviction (2023).

[^19]: [Miin official website](https://miin.cc/) — Slogan: “日常隨享，自由發聲!”; official description: “In Miin, you can discuss news, share stories, and record daily life without obstruction... let AI and generative technologies create a creative experience tailored to you... Miin helps you see through different positions, coordinated operations, and factuality in events, bringing you the most comprehensive and secure information platform” (© 2026 Miin team). For first-hand real-time reporting on the memorandum of cooperation with Lithuania’s Oxylabs to build the Infodemic platform, see [Radio Taiwan International](https://www.rti.org.tw/news/view/id/2177403), from August 2023 and involving one company, Oxylabs. Some later think-tank reports describe the matter as 2024 and two companies; this article anchors the account to the 2023 first-hand fact.
