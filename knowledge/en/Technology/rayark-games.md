---
title: 'Rayark Games: A Music Empire Built on Aesthetics, and Its Fourteen Years of Cracks'
description: "In 2012, six young people from National Taiwan University's College of Electrical Engineering and Computer Science pooled NT$30 million to make Cytus; within a month, it topped the charts in 14 countries. Fourteen years later, they had a Deemo anime film, an Implosion anime undelivered after eleven years, Sdorica entering maintenance mode in February 2026, and the choice after the 2020 ICE Morse code incident to cut ties with an employee in order to preserve the Chinese market. Aesthetics made Rayark visible to the world, and also made it stumble in every non-musical arena."
date: 2026-04-25
author: 'zaious'
category: 'Technology'
subcategory: '社群與數位文化'
tags:
  [
    'Rayark Games',
    'Rayark',
    'Cytus',
    'Deemo',
    'Sdorica',
    'rhythm games',
    'Taiwanese games',
    'Yu Ming-yang',
    'Chung Chih-yuan',
    'ICE',
    'Morse code',
    'Implosion',
    'VK克',
    'Mozarc',
  ]
readingTime: 20
lastVerified: 2026-05-26
lastHumanReview: false
featured: false
translatedFrom: 'Technology/雷亞遊戲.md'
sourceCommitSha: '31a05c44'
sourceContentHash: 'sha256:efb74dfc78d9c93c'
sourceBodyHash: 'sha256:28ef520886f893e3'
translatedAt: '2026-06-14T00:35:00+08:00'
image: '/article-images/technology/rayark-cafe-2021.webp'
imageCredit: 'Solomon203 / Wikimedia Commons'
imageLicense: 'CC BY-SA 4.0'
imageSource: 'https://commons.wikimedia.org/wiki/File:Rayark_Café_20211016.jpg'
---

> **30-second overview:** In September 2011, six young people from National Taiwan University's College of Electrical Engineering and Computer Science founded Rayark Games on Jinshan North Road in Taipei, with NT$30 million in capital and a team of 16. In January 2012, Cytus launched on iOS and reached No. 1 on the charts in 14 countries within a month. Deemo later entered Japan's Oricon chart, Implosion won the 2015 iOS Game of the Year, and VOEZ became a Nintendo Switch launch title. Fourteen years later, Rayark has released more than ten games and surpassed 130 million downloads worldwide, but the keyword surrounding the company has shifted from "genius" to "what a pity." After struggling on for eight years, Sdorica officially entered maintenance mode in February 2026; the Implosion anime, crowdfunded on Kickstarter in 2015, remained undelivered in 2026; and after the 2020 ICE Morse code incident, Rayark modified its game in line with the Chinese market. Aesthetics made Rayark visible to the world, and also made it stumble in every non-musical arena.

---

## What an Arcade Cabinet Taught Them

![Rayark Inc. official logo, the brand mark used since 2012: a white R on a red background](/article-images/technology/rayark-logo-2012.webp)
_Rayark Inc. official logo. Source: [English Wikipedia File:Logo of Rayark Inc.png](https://en.wikipedia.org/wiki/File:Logo_of_Rayark_Inc.png). Fair use editorial commentary._

Rayark's story begins with a failure.

In 2008, Yu Ming-yang was a first-year master's student at National Taiwan University's Graduate Institute of Networking and Multimedia. He and two friends founded "Hypaa Studio" at the university and developed THEIA, a large-scale touchscreen arcade rhythm game.[^kopu] That same year, South Korea's PENTAVISION released DJ Max Technika on arcade platforms. Its gameplay was close to THEIA's, but it thoroughly outclassed THEIA in music quality, interface design, and overall polish.[^pentavision-wiki]

"We thought interesting gameplay would sell, but the market's reaction taught us that visuals and music are very important," Yu later recalled.[^kopu]

That sentence became the underlying logic of every Rayark product that followed: gameplay was only the foundation; aesthetics were the moat.

After THEIA failed, Hypaa Studio did not immediately shut down. They spent two years trying again, releasing a second arcade title, Mozarc, in 2010: a 6K falling-note rhythm game similar to PENTAVISION's DJ Max gameplay at the time, but using Hypaa's own music library.[^mozarc-fandom][^bahamut-mozarc] During its deployment period, Mozarc accumulated a set of tracks, including Bloody Purity, Colorful Skies, Saika, Beyond, Sanctity, and Holy Knight. Those titles would later appear in the song libraries of Cytus and Deemo.[^mozarc-fandom] In other words, Hypaa's two arcade games did not succeed commercially, but they left behind a body of musical assets that allowed Rayark, founded two years later, to build a song library without starting from zero.

> **💡 Did you know?**
> A Rayark player recalled in a 2026 comment: "Mozarc's art was extremely good. What was more unfortunate was that the plastic sheet buttons had too high a failure rate; later, after they were changed to microswitches, the feel was poor, and it faded from the market. Hypaa actually operated this game for a very long time. It is already hard to find the cabinets, I haven't seen anyone playing it, and the servers lasted for a long time before they were completely shut down."[^pttweb-mozarc-comment] This is the real reason Rayark moved from arcade cabinets to mobile platforms: the maintenance costs of hardware were not something an independent team could sustain.

Three years later, in September 2011, the team founded Rayark Games on Jinshan North Road in Taipei, with NT$30 million in capital and a 16-person team, shifting its focus entirely from arcade cabinets to mobile platforms.[^rayark-wiki] The six co-founders were Chung Chih-yuan, Yu Ming-yang, Chang Shih-chun, Hsieh Chang-yen, Yang Shan-yung, and Lee Yung-ting. Five came from National Taiwan University's Department of Computer Science and Information Engineering (Yang Shan-yung, class B91; Yu Ming-yang and Hsieh Chang-yen, class B92), and one came from NTU's Graduate Institute of Communication Engineering (Chung Chih-yuan).[^csiecomm-2013][^rayark-wiki]

> **💡 Did you know?**
> Yu Ming-yang was the only one of the six whose undergraduate degree was not in the College of Electrical Engineering and Computer Science. He studied in NTU's Department of Forestry, class B92. "I originally wanted to study computer science, but because I did not do well enough on the exam, I went to the forestry department," he said in a 2012 interview.[^csiecomm-2013] From forestry to NTU's Graduate Institute of Networking and Multimedia, and then to founding a mobile rhythm game company at age 26, this cross-disciplinary path became one source of Rayark's aesthetic sensibility and unexpectedly made him the company's public-facing representative.

Chung Chih-yuan was the chief technology officer. Several years later, he led the team's full transition from PaaS to a Kubernetes container architecture. Rayark operated nearly 50 K8s clusters on Google Cloud, and "three people could maintain a game with millions of users."[^ithome-rayark] Hsieh Chang-yen later became the producer of Sdorica.[^sdorica-wiki] Lee Yung-ting was a game director and one of Rayark's early company spokespeople.[^bnext-rayark]

The six-person NTU College of Electrical Engineering and Computer Science alumni background later became the engineering base beneath Rayark's aesthetic formula: they could fine-tune rhythm game judgment precision, build cross-platform engines, and keep servers stable on the day of the Nintendo Switch launch. But that base would encounter entirely different problems in long-term RPG operations, animation production, and political public relations.

---

## Cytus and Deemo: The Two Pillars of the Music Empire

On January 12, 2012, Cytus launched on iOS.[^cytus-wiki]

![Cytus II gameplay screenshot, showing the dynamic scanline note-tapping judgment mechanic — the Cytus series' signature gameplay](/article-images/technology/cytus-ii-gameplay.webp)
_The Cytus II version of the Cytus series' signature "dynamic scanline" gameplay. Source: [English Wikipedia File:Cytus II gameplay.png](https://en.wikipedia.org/wiki/File:Cytus_II_gameplay.png). Fair use editorial commentary._

The gameplay was simple and intuitive: tap notes as a dynamic scanline passed over them. What truly set it apart, however, was the quality of its art and music. Its science-fiction visual design and high-level original electronic music gave Cytus a memorable identity in a crowded field of homogeneous mobile rhythm games. Within a month of launch, it reached No. 1 on the App Store charts in 14 countries, held the top spot on Japan's rhythm game chart for 29 consecutive days, and reached 1 million paid downloads in April 2015.[^cytus-wiki]

On November 13, 2013, Deemo launched.[^deemo-wiki] If Cytus was science-fiction electronic music, Deemo was classical piano. Players performed piano pieces in a black-and-white fairy-tale world. The music moved from electronic toward classical and lyrical, while the art style shifted from cool-toned science fiction to warm hand-drawn illustration.

![DEEMO Last Recital PS Vita cover, the signature image of a little girl playing piano in a black-and-white fairy-tale piano room](/article-images/technology/deemo-cover.webp)
_The PS Vita cover of DEEMO Last Recital; its black-and-white fairy-tale style is the signature art direction of the Deemo series. Source: [English Wikipedia File:DeemoLastRecitalVita.jpg](https://en.wikipedia.org/wiki/File:DeemoLastRecitalVita.jpg). Fair use editorial commentary._

Deemo became one of Rayark's biggest commercial works. By October 2014, it had accumulated 7 million downloads; by the time its animated film was announced in 2021, it had reached 28 million downloads.[^deemo-wiki] Its soundtrack sold well in the Japanese market, and the game won App Store Taiwan's 2013 Best of the Year Independent Developer and Google Play Taiwan's 2014 Best Game Music. The Nintendo Switch version has a Metacritic score of 88.[^deemo-wiki] Its sequel, DEEMO II, launched on January 13, 2022, reached 1 million pre-registrations worldwide, surpassed 1 million downloads in its first week, and served as Rayark's tenth-anniversary title.[^deemo2-gnn]

> **📝 Curator's Note**
> Cytus and Deemo established Rayark's brand formula: rhythm game × high art quality × narrative packaging. This formula gave Rayark a distinctive position in the global mobile games market, but it also constrained every later attempt. Looking back fourteen years later, all of Rayark's most successful works were rhythm games, and all of its least successful attempts involved trying to apply this formula to non-musical fields.

---

![Rayark booth in 2018, with the backs of Pipimi and Popuko cosplayers from POP TEAM EPIC visible in the distance](/article-images/technology/rayark-booth-cosplayers-2018.webp)
_Rayark booth in 2018, seen from behind cosplay attendees. Source: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Cosplayers_of_Pipimi_and_Popuko_seen_from_behind_at_Rayark_booth_(40764217870).jpg). Photo: player cosplay snapshot, CC BY-SA 2.0.\_

## The Year of the Switch Launch, They Did Five Things at Once

Between 2015 and 2018, Rayark advanced five product lines simultaneously.

Implosion launched on iOS and Android on April 8, 2015, and came to Nintendo Switch on July 6, 2017.[^implosion-wiki] It was a 3D action game whose visual quality approached console standards among mobile games of its time. It used a paid App Store download model, had no in-app purchases, received a Metacritic score of 93, entered No. 7 on the App Store Top Grossing chart within a week of launch, and had 91.9% five-star ratings.[^implosion-wiki] It won 2015 iOS Game of the Year Asia, the 2015 Bahamut ACG Creation Award, and the 2014 Unity Awards Golden Cube.[^implosion-wiki]

In June 2016, VOEZ launched on mobile. The following year, on March 3, 2017, VOEZ became one of the Nintendo Switch launch titles. Rayark was one of the few non-Nintendo first-party rhythm game developers in the Switch launch lineup.[^voez-4gamers] By early 2017, worldwide downloads had surpassed 10 million.[^voez-4gamers] Nintendo Life gave it an 8/10 and called it the Switch's "secret weapon."[^voez-nintendo-life]

![VOEZ Nintendo Switch cover, featuring the signature watercolor visual style with a mirrored two-person composition](/article-images/technology/voez-switch-cover.webp)
_VOEZ Nintendo Switch cover, published by Flyhigh Works — a Switch launch title on March 3, 2017. Source: [English Wikipedia File:SwitchVOEZ.jpg](https://en.wikipedia.org/wiki/File:SwitchVOEZ.jpg). Fair use editorial commentary._

On January 18, 2018, Cytus II launched, a sequel arriving six years after the original Cytus.[^cytus2-gematsu] The new system pushed rhythm game players' judgment abilities to the limit, and the game later accumulated more than 18 million downloads worldwide. In May 2026, Rayark announced that Cytus II would launch on Nintendo Switch 2 and Switch in 2027, with more than 500 tracks included.[^cytus2-gematsu][^cytus2-qooapp]

During these years, Cytus also expanded into IP derivatives. In November 2014, Code: Cytus, a multimedia musical commissioned by the Quanta Culture and Education Foundation, was performed four times in Taiwan,[^cytus-wiki] moving mobile game tracks into the theater. In February 2015, Rayark collaborated with Japan's Capcom to develop Cytus: Omega, an arcade version unveiled at JAEPO 2015, with location testing beginning in July. This collaborative version was ultimately announced as canceled on March 30, 2018.[^cytus-wiki] A May 2026 comment by data_pythoness — "Cytus also wanted to make an arcade cabinet. I was lucky enough to try it on site. At the time, I was really looking forward to a large rhythm game arcade machine from Taiwan. Unfortunately, it later disappeared without a trace"[^threads-cytus-arcade-comment] — is the most direct player perspective on that derivative. On April 25, 2019, Cytus α launched on Nintendo Switch, adding two new chapters and an online Battle Score mode, with a Metacritic score of 81.[^cytus-wiki] This was the first official home-console release in the Cytus series.

Implosion proved Rayark's technical capacity to cross genres. But the business model of an action game is entirely different from that of a rhythm game. Rhythm games sustain revenue through continuing song-pack updates; action games are one-time purchases.

Then came Sdorica on April 19, 2018.[^sdorica-wiki]

---

## Leaving the Comfort Zone: Eight Years of Sdorica

![Sdorica game logo, the "aurora" subtitle version with aurora-themed character artwork](/article-images/technology/sdorica-logo.webp)
_Sdorica game logo, the aurora subtitle version. Source: [English Wikipedia File:Sdorica logo.png](https://en.wikipedia.org/wiki/File:Sdorica_logo.png). Fair use editorial commentary._

Sdorica was Rayark's boldest experiment.

Planning began in 2013, development began in 2014, and the game was originally scheduled to launch in 2016. It was delayed to 2017, then delayed again before finally entering public beta on April 19, 2018. After a five-year development cycle, it had more than 1.5 million pre-registrations, surpassed 2.5 million downloads on April 30, and surpassed 5 million downloads on May 11.[^sdorica-wiki] After launch, daily active users exceeded 1 million.

It was a mobile RPG telling the stories of heroes and soul infusions in the world of Sdorica, with Hsieh Chang-yen as producer.[^sdorica-wiki][^moegirl-sdorica] Rayark took the art budget of a rhythm game and used it for RPG character illustrations, and applied its narrative skills to a character-growth system. But the company quickly discovered that the playlist of a rhythm game and the content update cadence of an RPG require completely different muscles.

After launch, problems erupted in succession. The servers underestimated player numbers, gacha pool events did not open on schedule, a Dragon Boat Festival version displayed garbled Chinese text, Glowing Dust was not distributed, and so on.[^sdorica-udn] Between June and July 2018, Rayark's operational decisions triggered strong player backlash, including unannounced adjustments to character values and controversy over high-priced gift packs. Within four months, the game slid from its peak, becoming a turning point in Rayark's reputation.[^sdorica-bahamut-policy]

The event most deeply remembered by veteran players was the **Black Pongji nerf incident**. Black Pongji was a popular early Sdorica character. Paired with Angelia SP, he formed the strongest team composition at the time, and players invested substantial resources in building that team. After Rayark introduced the "zombie" mechanic (enemies could still counterattack after death) and limited Black Pongji's "taunt" to once per turn, this core team was effectively invalidated.[^sdorica-blackpongji] Rayark called it a bug fix rather than a nerf, but players did not accept that explanation. The change came shortly after a new "White Pang" character skin had been released, and veteran players read it as a commercial maneuver: **sell a skin first, then cut down an old character to force players toward a new one**.[^sdorica-blackpongji][^pttweb-rayark] "Quitting because Black Pongji was nerfed" became a shared farewell event in old Sdorica guild circles. One PTT player wrote in 2026: "When I first played Sdorica, a bunch of top-ranked players in my guild quit because Black Pongji was nerfed."[^pttweb-rayark-thread]

> **💡 Did you know?**
> Rayark almost never missed in rhythm games and action games, but it stumbled in an RPG that required long-term operations. The core capability of a rhythm game or buy-to-play game is "making a good product." The core capability of RPG operations is "continuously serving a group of people." These are completely different muscles.

Eight years later, on February 11, 2026, Rayark officially announced that Sdorica would enter maintenance mode:[^sdorica-gachago][^sdorica-bahamut-policy]

> New main story chapters, special events, limited-time gift packs, and other content would stop entirely. The final two characters, Valdrir DR and Chiyuki DR, would be distributed to all players through the in-game mailbox and obtained through the rerun of the Springwater Intoxication event, respectively. Special Infuse events would continue to rerun until July 2026; after the final rerun ended, no new reruns would open. The servers would continue operating for the foreseeable future.

"The active development life cycle of Sdorica has ended." This was the moment when Rayark itself declared the end of its RPG battlefield.[^sdorica-gachago] For core players who had stayed for years, this announcement was crueler than a sudden server shutdown: the servers would stay open, old characters could still be trained, but the new story would never arrive. Rayark also clearly understood the cost of this decision: eight years of story, eight years of character design, and eight years of accumulated worldbuilding would enter a frozen state, leaving players to decide for themselves how long they wished to remain.

For Rayark in early 2026, Sdorica's maintenance mode was a necessary stop-loss. Sdorica had continuously consumed Rayark's R&D resources for eight years and blurred the clarity of its brand positioning. A company founded on "making the most beautiful rhythm games" had become tied to an RPG that it could no longer sustain. Every additional year of delayed stop-loss made the company's overall narrative harder to explain. The side effect of the maintenance-mode announcement may be that the Cytus and DEEMO series become the clear center of Rayark's brand once again.

---

## Cracks Earlier Than Morse Code: The 2014-2017 VK克 Incident

Rayark's earliest public-relations crisis traces back to the VK克 plagiarism controversy, three years before the 2020 ICE incident.

In the summer of 2014, the composer Waiting, using the alias H&&D, received a demo from VK克 and found obvious plagiarized passages in it. He wrote to point out the problem, but VK克 refused to make changes.[^ettoday-vk-882323] A piece rejected by Erotes Studio, the team behind Rainy Port Keelung, under the title "Passing Through Rainy Time and Space," was renamed "Passing Through Time and Space" by VK克 several months later and resold to another client. In November 2014, it became the theme song for the mobile game League of Angels, and internet users discovered that the track appeared to resemble a passage from the opening theme of the anime Puella Magi Madoka Magica.[^ettoday-vk-882323][^cts-vk-201703131858055]

After Rayark discovered this, according to its official statement, it "resolved that before the controversy was settled, no new V.K songs would be included in Rayark's games."[^cts-vk-201703131858055] This addressed song inclusion; after the 2015 PS Vita version of Deemo, no new VK克 tracks were added.

The problem was that physical events did not stop in parallel. On May 14, 2016, Rayark continued to invite VK克 to participate in a Shanghai concert. On February 4, 2017, it again invited VK克 to take part in a Rayark "creation" lecture.[^ettoday-vk-882323] **Known plagiarism controversy, yet three consecutive years of public collaboration in various forms**: this was the trigger that finally led Waiting to go public.

On March 11, 2017, Waiting posted his allegations online: "Music is the same as illustration; plagiarism should not be tolerated."[^ettoday-vk-882323] The next day, March 12, Rayark publicly apologized on Facebook:[^cts-vk-201703131858055]

> After this incident occurred, Rayark did not fully stop collaborating with VK on physical events... In the future, we will adopt the same standard as for song inclusion: before the controversy is settled, we will not collaborate in any form.

Waiting and Rayark founder Tony were middle-school classmates.[^plurk-waiting] That friendship made the incident especially painful. Waiting later publicly announced the termination of collaboration and signed a "statement of non-use of works," bringing the two-year aftermath to an end.[^disp-bbs-vk]

> **💡 Did you know?**
> In its 2017 apology statement, Rayark explicitly admitted, word for word, that it "did not fully stop collaborating with VK on physical events." The value of this statement lies in how clearly it identified the shape of the problem: Rayark knew something was wrong, but because VK克 was a long-term collaborator and the commercial relationship was hard to cut, it handled the matter on two separate levels: no new song inclusion, but physical events continued. This was the first crack in the logic of "brand purity." When the brand narrative conflicted with commercial relationships, Rayark prioritized the commercial relationship for three years.

Although the VK克 incident was not a political landmine, it was the first conflict between Rayark's "aesthetic promise" logic and its commercial relationships. In the handling of the 2020 ICE Morse code incident, the same decision structure would appear again, only with higher stakes, because the other side was the Chinese market.

---

## Morse Code 1344 7609 2575

In March 2020, Rayark's music director ICE, whose real name is Wilson Lam and who is a Hong Kong musician who joined Rayark in 2014, released the album Consciousness in a personal capacity. It included the track "Telegraph : 1344 7609 2575" on his personal SoundCloud and YouTube.[^silentblue-wilson-lam][^itechpost-cytus2] The "1344 7609 2575" in the title was Chinese Morse code.

On July 17, 2020, Chinese internet users dug up the track and found that the decoded Morse code read: **Hongkongers add oil, liberate Hong Kong, revolution of our times**.[^udn-ice][^newtalk-ice]

The next day, July 18, Ice announced through a personal statement that he was leaving Rayark. The original text read:

> Regarding the controversy caused by the piece of music I released in March 2020, which has led to discussion among many internet users: because this was a private activity of mine, does not fall within the scope of work, and is unrelated to Rayark Games, I have therefore decided to resign voluntarily and leave Rayark Games effective immediately.[^newtalk-ice]

That same day, Chinese publisher Longyuan Network and Rayark Games issued a joint announcement stating that Cytus II would be taken down in China pending rectification.[^gnn-ice] Taiwanese players expressed dissatisfaction on Rayark's fan page and questioned whether the company was carrying out ideological censorship. As of July 20, Rayark had still not issued a formal explanation on its official Taiwanese platforms.[^techorange-ice] The following year, in May 2021, Longyuan and Rayark officially announced that after rectification, six tracks composed by ICE would be removed, that paid players would be compensated, and that the Chinese server of Cytus II would return to sale.[^4gamers-cytus2-ice-removal]

After leaving Rayark, ICE continued creating in a personal capacity. In July 2022, he publicly revealed his real identity; he is currently active under the name **Ice@Spaceport Productions**, producing trance and hardcore tracks and continuing to release new works on Facebook and X.[^namuwiki-ice][^facebook-iceloki][^x-iceloki] In Rayark's May 2026 comment section, one reader directly called this out: "Ice kept making songs afterward; it's just that his name is hard to use as an identifiable keyword."[^pttweb-rayark-thread] Two facts are simultaneously true: he did not disappear, and Rayark cannot remove him from its history.

This was Rayark's version of a "political landmine" incident, and the second conflict between its "aesthetic promise" logic and commercial relationships. Three years earlier, in the VK克 incident, Rayark chose to prioritize the commercial relationship. This time, facing a larger market, the decision structure was exactly the same.

One year earlier, in 2019, Devotion by [Red Candle Games](/technology/赤燭遊戲) was removed from Steam's China region on February 23 because of the talisman incident. Three days later, Red Candle announced the game's full removal from Steam.[^cedargames-wiki] Its later publisher, Shanghai JuMiao Information Technology, was placed under investigation by the Yangpu District Administration for Market Regulation, and its business license was revoked on June 17.[^cedargames-wiki] **The party that truly bore the cost was the publishing side**. Red Candle preserved the original content without retreating, but the publishing company was eliminated. In Rayark's 2020 ICE incident, the company chose a different path: let the person involved leave, modify the game accordingly, and preserve its Chinese publishing channel. The priority remained commercial relationships, following the same logic as in the VK克 incident.

> **⚠️ Contested Viewpoint**
> These were sharply different choices by two landmark Taiwanese indie teams facing pressure from the Chinese market. Red Candle did not retreat on content, and the publisher paid the price of elimination; Rayark let the content retreat and preserved the Chinese publishing channel. English-language outlet PocketGamer.biz framed the story with the headline "China pulls Cytus II from the App Store for secret pro-democracy Morse code message."[^pocketgamer-cytus2] In the Chinese-language world, discussion focused on whether "Rayark kneeled" and whether cutting ties was correct. One event, two readings. Rayark's choice this time, and its 2014-2017 choice regarding VK克, were the same brand logic extended to different pressure sources.

---

## Implosion: Eleven Years of Zero Day

![Implosion: Never Lose Hope game poster, a mecha action scene with App Store and Google Play release information](/article-images/technology/implosion-cover.webp)
_Implosion: Never Lose Hope promotional poster — a 3D mecha action game that won 2015 iOS Game of the Year Asia. Source: [English Wikipedia File:Implosion- Never Lose Hope - cover.png](https://en.wikipedia.org/wiki/File:Implosion-_Never_Lose_Hope_-_cover.png). Fair use editorial commentary._

Some promises look worse than silence.

On December 5, 2015, Rayark launched a Kickstarter campaign for the animated film Implosion: Zero Day, seeking US$400,000 for a 90-minute animation.[^inside-zero-day] Within 48 hours of launch, it had reached 18% of its funding target; within 10 days, it had surpassed NT$5 million.[^implosion-zero-day-wiki] It was originally scheduled for completion in August 2018.

It was not delivered in 2018.

On January 24, 2019, a third delay announcement admitted that "the IZD animated film cannot be completed in 2018 as expected," and offered a refund option: backers could choose refunds while still receiving rewards corresponding to their pledge tiers.[^disp-bbs-implosion] Refunds were tallied in February 2019, and the first batch of merchandise was shipped in March, including hoodies, T-shirts, collector's edition film scripts, the game soundtrack, comic chapters, and film wallpapers. The full set of merchandise would be shipped only after the film was completed.

From 2020 to 2026, five years of silence followed. Rayark's official Implosion page and the English Wikipedia entry for Implosion still maintained that the animation was "in production," with no release date.[^implosion-wiki] Global Kickstarter backers had paid for eleven years of waiting, and by 2026 had still not seen the film.

"They don't even dare talk about the movie's progress; they can't provide even half a schedule," one backer wrote under the 2019 delay announcement.[^disp-bbs-implosion]

This is Rayark's only genuinely "undelivered" promised project. More serious than Sdorica's operational cracks is the long-term silence toward global Kickstarter backers. Yet this matter received far less media attention in the Chinese-language world than the ICE incident, Sdorica's maintenance mode, or the AI art controversy. Perhaps the Chinese-language indie game industry is more tolerant of such delays; perhaps it is because the consequences of the delay were ultimately dispersed among all the backers who paid into that 2015 Kickstarter campaign.

---

## Those Still Here

Rayark Inc. as of May 2026: roughly 270 employees, NT$64 million in capital, headquarters at No. 47 Dongxing Road, Xinyi District, Taipei City. Since 2012, it has released more than ten games and accumulated more than 130 million downloads worldwide.[^rayark-104] It has a Rayark Japan branch in Tokyo and is not publicly listed.

The fourteen-year list of works is much longer than the article has mentioned so far. In addition to the five main lines of Cytus, Deemo, Implosion, VOEZ, and Sdorica, Rayark has also released Mandora (2012, casual puzzle),[^rayark-wiki] DEEMO ~Last Recital~ (2015, PS Vita rhythm game),[^deemo-wiki] DEEMO -Reborn- (2019-2020, PS4/Switch/Steam music adventure, with Steam reviews rated Very Positive),[^steamcharts-deemo-reborn] MO:Astray (2019-2020, Steam/Switch/mobile action puzzle),[^udn-moastray] Soul of Eden (August 26, 2020, card strategy, developed for more than four years and once accused of having mechanics similar to Clash Royale[^bnext-59103]), Chaos Academy (2021, tactical card game),[^rayark-wiki] and DEEMO II (January 13, 2022, with 1 million global pre-registrations and 1 million downloads in its first week).[^deemo2-gnn] Fourteen years, 10+ works, across five platforms: mobile, Switch, PS4, PC, and PS Vita.

> **💡 Did you know?**
> In Rayark's catalog, only the two main rhythm game lines, Cytus and Deemo, have maintained "Cytus-level brand recognizability." Other standalone works, including Implosion, VOEZ, and MO:Astray, are all high-quality, but it is hard for readers to sum them up in one sentence as "this is Rayark." When your brand equals "aesthetic rhythm games," cross-genre works instead dilute brand recognizability. Looking back over fourteen years, Rayark's strongest curatorial ability was not developing new categories, but extending the Cytus and Deemo IPs through musicals, soundtracks, arcade collaborations, and animated films.

The timeline of the past three years:

- In May 2023, Rayark faced an AI art controversy. Online rumors claimed "full AI creation + layoffs of artists." On May 27, Rayark issued a Twitter statement clarifying that it "had not used AI creation to produce large quantities of images needed for games, and had certainly not laid off the art team because of this."[^rayark-twitter-ai][^gnn-rayark-ai]
- On November 30, 2023, Rayark Concept Café closed.
- On October 14, 2024, the Rayark Concept online store ceased operations.[^rayark-concept-fb]
- On February 11, 2026, Sdorica entered maintenance mode.
- On May 22, 2026, Rayark announced that Cytus II would launch on Nintendo Switch 2 and Switch in 2027.[^cytus2-gematsu]

Compared with rhythm game companies from the same period, PENTAVISION, which had dealt Hypaa Studio a crushing defeat in 2008, took an entirely different path. In 2012, because of financial difficulties, it was liquidated and fully absorbed by its parent company Neowiz.[^pentavision-wiki] In 2017, Neowiz revived the series with DJMax Respect. In December 2024, DJMax Respect V surpassed 6 million downloads, and in 2025 Neowiz reached record-high revenue.[^digitaltoday-neowiz]

PENTAVISION survived by being absorbed by a large company and then revived. Rayark chose the opposite path: remain independent, expand into new categories, and absorb the cost of every mistake itself.

Rayark Games' situation is the most typical dilemma after Taiwanese independent game success: the first product erupts from passion and talent; subsequent products require organizational capability and operational discipline. The market ceiling of rhythm games meant Rayark had to expand categories, but every expansion diluted its original brand recognizability. Cytus players and Sdorica players are entirely different groups. Serving both groups under the same brand name can result in both feeling that "Rayark has changed."

Yet Rayark remains one of the few brands in Taiwan's game industry that global markets can name. Cytus II's 18 million downloads, the Deemo series' 28 million downloads, Implosion winning iOS Game of the Year, VOEZ as a Switch launch title, and the DEEMO animated film produced by Production I.G and Signal.MD with a theme song by Yuki Kajiura: in Taiwan's 2026 mobile game market, no second company has replicated these achievements.[^deemo-movie-rayark]

In 2008, Yu Ming-yang learned from an unsold arcade cabinet that "aesthetics are very important." Eighteen years later, that sentence remains Rayark's greatest asset, and possibly its greatest shackle: when you define yourself as "the people who make the most beautiful games," the market's tolerance for error falls to zero.

✦ Aesthetics made Rayark visible to the world, and also made it stumble in every non-musical arena.

Sdorica's eight-year operational cracks stemmed from the essential conflict between the formula of "art × music × story" and the nature of long-term RPG service. Every event update required new high-quality character illustrations; every narrative expansion required original musical accompaniment. This could be done at the scale of a 16-person team with NT$30 million in capital, but in the gacha cadence of hundreds of thousands of daily active users, it became a systemic time sink. The quality standard Rayark built through rhythm games — polishing until the reader could recognize it at a glance — collided with the content speed of mobile RPGs, where players consume a major update in three days on average. The two were fundamentally at odds.

The core problem with the eleven-year undelivered Implosion anime was that the standard of "making the most beautiful animation" met the execution limits of an independent company. Animation production at the level of Production I.G requires an organized production pipeline and a long-term stable writing team. When Rayark promised a 90-minute animated film on Kickstarter, it used game-making muscles to make a promise in the animation industry. Rayark could meet the technical threshold of the Implosion animation; the difficulty lay in making it, then sustaining the entire process until theatrical release. An independent company at this scale could not bear that cost.

The ICE incident showed the inevitable result of extending the logic of "brand purity" to employees. Rayark's entire brand had been built on a narrative of "aesthetics-led, politically neutral, able to serve cross-national markets." When an employee released a pro-Hong Kong song outside of work, the internal consistency of that entire brand narrative was challenged. Rayark's choice was to let the employee resign voluntarily, cooperate with the Chinese market in modifying the game, and preserve its Chinese publishing channel. This was the internal optimal solution of that brand logic, and also the comparison case against another indie path, Red Candle's.

What will the next Rayark look like? Perhaps there will not be one; perhaps it will require different muscles. When aesthetics are everything, every non-aesthetic choice becomes a crack, including politics, operations, and time. But Rayark's fourteen-year trajectory also demonstrates one thing: Taiwanese indie game teams have the capacity to hold a rare brand position in the global rhythm game market. In Asia, only Japan's BEMANI system and South Korea's DJ Max series had done this before. Rayark's story is not over. The day Cytus II launches on Nintendo Switch 2 in 2027 will be the next test of whether this aesthetic empire can continue to define "made by Taiwan" in the AI era.

---

## Further Reading

- [Taiwan's Game Industry and Digital Entertainment](/technology/台灣遊戲產業與數位娛樂) — A panoramic view of Taiwanese games, from licensing to original creation
- [Red Candle Games](/technology/赤燭遊戲) — Another path for Taiwanese indie games: telling stories through history and choosing to leave the Chinese market
- [Daewoo's Twin Swords](/technology/大宇雙劍) — The starting point for Taiwanese games telling stories in Chinese
- [X-Legend and the Overseas Expansion of Taiwanese Online Games](/technology/傳奇網路與台灣線上遊戲出海) — Another overseas story of Taiwanese games

---

## Image Sources

This article uses eight licensed images, all cached under `public/article-images/technology/` to avoid hotlinking source servers:

- **rayark-cafe-2021.jpg** (hero) — [Wikimedia Commons File:Rayark Café 20211016.jpg](https://commons.wikimedia.org/wiki/File:Rayark_Café_20211016.jpg) — Photo: Solomon203, 2021-10-16, CC BY-SA 4.0
- **rayark-logo-2012.png** (inline, §What an Arcade Cabinet Taught Them) — [English Wikipedia File:Logo of Rayark Inc.png](https://en.wikipedia.org/wiki/File:Logo_of_Rayark_Inc.png) — Fair use editorial commentary on Rayark Inc. brand identity
- **cytus-ii-gameplay.png** (inline, §Cytus and Deemo) — [English Wikipedia File:Cytus II gameplay.png](https://en.wikipedia.org/wiki/File:Cytus_II_gameplay.png) — Fair use editorial commentary on the Cytus series' signature gameplay
- **deemo-cover.jpg** (inline, §Cytus and Deemo) — [English Wikipedia File:DeemoLastRecitalVita.jpg](https://en.wikipedia.org/wiki/File:DeemoLastRecitalVita.jpg) — Fair use editorial commentary on the DEEMO series' art
- **rayark-booth-cosplayers-2018.jpg** (inline, §The Year of the Switch Launch) — [Wikimedia Commons](<https://commons.wikimedia.org/wiki/File:Cosplayers_of_Pipimi_and_Popuko_seen_from_behind_at_Rayark_booth_(40764217870).jpg>) — Photo: 2018 ACG event cosplay snapshot, CC BY-SA 2.0
- **voez-switch-cover.jpg** (inline, §The Year of the Switch Launch) — [English Wikipedia File:SwitchVOEZ.jpg](https://en.wikipedia.org/wiki/File:SwitchVOEZ.jpg) — Fair use editorial commentary on VOEZ as an NS launch title
- **sdorica-logo.png** (inline, §Leaving the Comfort Zone: Eight Years of Sdorica) — [English Wikipedia File:Sdorica logo.png](https://en.wikipedia.org/wiki/File:Sdorica_logo.png) — Fair use editorial commentary on Sdorica brand identity
- **implosion-cover.png** (inline, §Implosion: Eleven Years of Zero Day) — [English Wikipedia File:Implosion- Never Lose Hope - cover.png](https://en.wikipedia.org/wiki/File:Implosion-_Never_Lose_Hope_-_cover.png) — Fair use editorial commentary on Implosion's game identity

---

## References

[^rayark-wiki]: [Rayark Games — Wikipedia](https://zh.wikipedia.org/zh-tw/%E9%9B%B7%E4%BA%9E%E9%81%8A%E6%88%B2) — Six co-founders (Chung Chih-yuan, Yu Ming-yang, Chang Shih-chun, Hsieh Chang-yen, Yang Shan-yung, Lee Yung-ting), founding in September 2011, Jinshan North Road, 16-person team, NT$30 million in capital, product timeline

[^kopu]: [Rayark: One of Taiwan's Few Self-Developing Mobile Game Studios with a Distinctive Style — KOPU Lynn](https://kopu.chat/rayark/) — Hypaa Studio THEIA story, Yu Ming-yang's direct quote "visuals and music are very important," company founding background

[^csiecomm-2013]: [B92 Yu Ming-yang, B91 Yang Shan-yung, B92 Hsieh Chang-yen (Rayark Games) — csiecomm blog](http://csiecomm.blogspot.com/2013/07/b92-b91-b92.html) — 2012-12-07 interview; Yu Ming-yang's path from forestry to the Graduate Institute of Networking and Multimedia, Yang Shan-yung B91, Hsieh Chang-yen B92; Yu Ming-yang's direct quote: "I originally wanted to study computer science, but because I did not do well enough on the exam, I went to the forestry department"

[^ithome-rayark]: [Rayark Moves from PaaS to Containers; Three People Can Maintain a Million-Player Game — iThome](https://www.ithome.com.tw/people/109212) — CTO Chung Chih-yuan led containerization transformation, Rayark's 50 GCP K8s clusters

[^sdorica-wiki]: [Sdorica — Wikipedia](https://zh.wikipedia.org/zh-hant/Sdorica_%E8%90%AC%E8%B1%A1%E7%89%A9%E8%AA%9E) — Planning in 2013 / development in 2014 / public beta on 2018-04-19; 1.5 million pre-registrations; surpassed 2.5 million downloads on 4/30; surpassed 5 million downloads on 5/11; producer Hsieh Chang-yen

[^bnext-rayark]: [Rayark Games: The Team Behind Cytus, an iOS Game with Thousands of Five-Star Ratings — Business Next](https://www.bnext.com.tw/article/22202/BN-ARTICLE-22202) — Lee Yung-ting as director and company spokesperson, Yu Ming-yang co-founder, Chang Shih-chun co-founder

[^cytus-wiki]: [Cytus — Wikipedia](https://en.wikipedia.org/wiki/Cytus) — 2012-01-12 iOS / 4-13 Android launch; reached 1 million paid downloads in 2015-04; No. 1 chart ranking in 14 countries; held No. 1 on Japan's rhythm game chart for 29 consecutive days

[^deemo-wiki]: [Deemo — Wikipedia](https://en.wikipedia.org/wiki/Deemo) — 2013-11-13 iOS / 12-27 Android; 2015-06-24 Vita; 7 million downloads by 2014-10; 28 million downloads when the anime was announced in 2021; awards; DEEMO -Reborn-; DEEMO II; Memorial Keys animated film; Nintendo Switch version Metacritic 88

[^deemo2-gnn]: [Rayark's Tenth-Anniversary Title DEEMO II Officially Launches Worldwide — Bahamut GNN](https://gnn.gamer.com.tw/detail.php?sn=226618) — DEEMO II launched on 2022-01-13; 1 million downloads in first week; 1 million pre-registrations worldwide

[^implosion-wiki]: [Implosion: Never Lose Hope — Wikipedia](https://en.wikipedia.org/wiki/Implosion:_Never_Lose_Hope) — 2015-04-08 iOS/Android, 2017-07-06 Switch; awards; Metacritic 93; 91.9% five-star ratings in first week; 2015 iOS Game of the Year Asia + 2015 Bahamut ACG Creation Award + 2014 Unity Awards Golden Cube; Zero Day 90-minute animation in production

[^voez-4gamers]: [Rayark's VOEZ Coming to Nintendo Switch — 4Gamers](https://www.4gamers.com.tw/news/detail/31551/voze-achieved-10-million-download-and-will-be-launch-in-nintendo-switch) — VOEZ surpassed 10 million downloads by early 2017; 2017-03-03 NS launch title

[^voez-nintendo-life]: [VOEZ (2017) — Nintendo Life](https://www.nintendolife.com/games/switch-eshop/voez) — Nintendo Life score 8/10, "NS secret weapon"

[^cytus2-gematsu]: [Cytus II coming to Switch 2, Switch in 2027 — Gematsu](https://www.gematsu.com/2026/05/cytus-ii-coming-to-switch-2-switch-in-2027) — 2026-05-22 announcement of NS / NS2 2027 release; 18 million downloads worldwide; 500+ tracks

[^cytus2-qooapp]: [Rayark's Popular Rhythm Game Cytus II Confirmed for Switch 2 / Switch Version — QooApp](https://news.qoo-app.com/post/436892/cytus-ii-switch) — Chinese-language news confirmation; 2027 release

[^moegirl-sdorica]: [Sdorica — Moegirlpedia](https://zh.moegirl.tw/%E4%B8%87%E8%B1%A1%E7%89%A9%E8%AF%AD) — Developed and published by Rayark Games; launched on 2018-04-19; producer Hsieh Chang-yen

[^sdorica-udn]: [Sdorica Events Repeatedly Run into Problems — udn Game Corner](https://game.udn.com/game/story/10453/3209024) — June 2018 series of Sdorica operational controversies after launch, including overloaded servers, gacha pools not opening on schedule, Dragon Boat Festival garbled text, and Glowing Dust not distributed

[^sdorica-bahamut-policy]: [Sdorica Operations Policy Adjustment Notice — Bahamut Forum](https://forum.gamer.com.tw/C.php?bsn=29560&snA=11124) — 2026-02-11 Chinese maintenance-mode announcement; no new reruns after 2026-07; player community discussion

[^sdorica-gachago]: [Sdorica Enters Maintenance Mode After Final Character Releases — Gacha Go!](https://gachago.com/en/news/sdorica-enters-maintenance-mode-after-final-character-releases) — 2026-02-11 maintenance mode; Valdrir DR + Chiyuki DR as final two characters; servers remain operational; Infuse reruns through 2026-07; "Sdorica active development life cycle has ended"

[^silentblue-wilson-lam]: [Wilson Lam — SilentBlue.RemyWiki](https://silentblue.remywiki.com/Wilson_Lam) — ICE real name Wilson Lam; joined Rayark in 2014 as music director; record of 2020 departure incident

[^itechpost-cytus2]: ['Cytus II' Taken Down in China Due to a Composer's Song Containing Hidden Pro-Hong Kong Morse Code Message — iTechPost](https://www.itechpost.com/articles/103452/20200722/cytus-ii-taken-down-in-china-due-to-a-composers-song-containing-hidden-pro-hong-kong-morse-code-message.htm) — English-media perspective on the ICE incident

[^udn-ice]: [Reported Work Contained Morse Code Saying "Liberate Hong Kong"; Rayark Music Director Announces Departure — udn Game Corner](https://game.udn.com/game/story/10453/4711560) — 2020-07-17 Chinese internet users dug up the song; Morse code decoded as "Hongkongers add oil, liberate Hong Kong, revolution of our times"; complete ICE incident timeline

[^newtalk-ice]: [Music Found to Hide Anti-Extradition Slogan; Rayark Music Director Ice Voluntarily Resigns — Newtalk](https://newtalk.tw/news/view/2020-07-18/437743) — 2020-07-18 Ice's full statement quoted verbatim; key points of Longyuan announcement

[^gnn-ice]: [Rayark Music Director Ice Announces Departure over Controversy Caused by Song — Bahamut GNN](https://gnn.gamer.com.tw/detail.php?sn=200246) — Bahamut official report; joint announcement by Rayark and Longyuan

[^techorange-ice]: [Music Director's Private Work Supported Hong Kong; Was Rayark Games' Weibo Severance Correct? — TechOrange](https://techorange.com/2020/07/20/rayark-ice-support-hk-resign/) — As of 2020-07-20, Rayark had not issued a formal statement on its official Taiwanese platforms; player community criticism

[^4gamers-cytus2-ice-removal]: [China's Cytus II Taken Down for Rectification; All Tracks Composed by ICE to Be Removed — 4Gamers](https://www.4gamers.com.tw/news/detail/44034/cytus-ii-ban-songs-by-ice-in-china) — May 2021 removal of six ICE tracks; compensation for paid players

[^pocketgamer-cytus2]: [China pulls Cytus II from the App Store for secret pro-democracy Morse code message — PocketGamer.biz](https://www.pocketgamer.biz/asia/news/73974/china-pulls-cytus-ii-from-app-store/) — English industry-media framing; international media perspective

[^inside-zero-day]: [Rayark Games' Implosion Adaptation Implosion: Zero Day to Launch Kickstarter Campaign — INSIDE](https://www.inside.com.tw/article/5271-implosion-zero) — Kickstarter launched on 2015-12-05; 18% of funding target reached within 48 hours

[^implosion-zero-day-wiki]: [Implosion: Zero Day — Wikipedia](https://zh.wikipedia.org/zh-tw/%E8%81%9A%E7%88%86%EF%BC%9A%E7%AC%AC%E9%9B%B6%E6%97%A5) — Surpassed NT$5 million in 10 days; originally scheduled for completion in 2018-08; no new announcements after 2020

[^disp-bbs-implosion]: [Rayark Implosion Zero Movie Delayed for Third Time — Disp BBS ACG Board](https://disp.cc/b/ACG/b7Iw) — 2019-01-24 third delay announcement; refund plan; player criticism quoted verbatim

[^rayark-104]: [Rayark Inc. | Hiring — 104 Job Bank](https://www.104.com.tw/company/1a2x6bj6qc) — 270 employees; NT$64 million in capital; 130 million cumulative downloads; product list

[^rayark-twitter-ai]: [Rayark Official Twitter AI Art Clarification Statement](https://twitter.com/RayarkOfficial/status/1662466448709816331) — 2023-05-27 original text: "has not used AI creation to produce large quantities of images needed for games, and has certainly not laid off the art team because of this"

[^gnn-rayark-ai]: [Rayark Games Clarifies It Did Not Lay Off Large Numbers of Artists Due to Adoption of AI Technology — Bahamut GNN](https://gnn.gamer.com.tw/detail.php?sn=250502) — Full Chinese text of Rayark official clarification

[^rayark-concept-fb]: [Rayark Concept Facebook](https://www.facebook.com/RayarkConcept/) — 2024-10-14 announcement that the online store ceased operations

[^pentavision-wiki]: [Pentavision — Wikipedia](https://zh.wikipedia.org/zh-hans/Pentavision) — Acquired by Neowiz in 2006-04; DJ Max Technika in 2008; liquidated and closed in 2012; fully absorbed by Neowiz

[^digitaltoday-neowiz]: [Neowiz posts 60 billion won 2025 operating profit, up 82.2 percent — DigitalToday](https://www.digitaltoday.co.kr/en/view/3459/neowiz-2025-operating-profit-60-billion-won-up-822-percent) — DJ Max Respect V reached 6 million downloads in 2024-12; Neowiz annual revenue reached a record high in 2025

[^deemo-movie-rayark]: [Animated Theatrical Film DEEMO THE MOVIE, Based on Rayark's Rhythm Game DEEMO — Rayark Official](https://rayark.com/zh/news/20201113_deemomovie/) — DEEMO THE MOVIE production companies Production I.G + Signal.MD, chief director Junichi Fujisaku, director Shuhei Matsushita, theme song by Yuki Kajiura

[^mozarc-fandom]: [User blog:JCEXE/Small History of Hypaa Studio, pre-Rayark team — Cytus Wiki Fandom](https://cytus.fandom.com/wiki/User_blog:JCEXE/Small_History_of_Hypaa_Studio,_pre-Rayark_team) — Complete Hypaa Studio timeline; 2010 Mozarc 6K fall-style arcade game; Bloody Purity / Colorful Skies / Saika / Beyond / Sanctity / Holy Knight later moved to Cytus + Deemo

[^bahamut-mozarc]: [Prototype AC — MOZARC — Bahamut Creation](https://home.gamer.com.tw/artwork.php?sn=871313) — Introduction to the Mozarc prototype arcade cabinet; player community fan creation

[^pttweb-mozarc-comment]: [Threads taiwandotmd #DYwMkzBgW8k comment by donchuenbao](https://www.threads.com/@taiwandotmd/post/DYwMkzBgW8k) — 2026-05-26 Rayark article Threads player comment: "Between Hypaa and Rayark there was also a rhythm game arcade cabinet called Mozarc" + details on the failure rate of plastic sheet buttons

[^threads-cytus-arcade-comment]: [Threads taiwandotmd #DYwMkzBgW8k comment by data_pythoness](https://www.threads.com/@taiwandotmd/post/DYwMkzBgW8k) — 2026-05-26 player comment: "Cytus also wanted to make an arcade cabinet. I was lucky enough to try it on site. At the time, I was really looking forward to a large rhythm game arcade machine from Taiwan" — first-hand player record of Cytus: Omega location testing

[^sdorica-blackpongji]: [Sdorica Black Pongji Nerf Incident — Sdorica Bahamut Forum + catchtest Pixnet Impressions](https://forum.gamer.com.tw/C.php?bsn=29560&snA=6674) — Black Pongji zombie mechanic + taunt limited to once per turn; Black Pongji + Angelia SP team composition invalidated; Rayark called it a bug fix, which players did not accept; shortly after White Pang skin release

[^pttweb-rayark-thread]: [PTT C_Chat Rayark Games: A Music Empire Built on Aesthetics repost thread by GTES](https://www.pttweb.cc/bbs/C_Chat/M.1779745322.A.35D) — 2026-05-26 PTT C_Chat player community discussion thread; selfet: "When I first played Sdorica, a bunch of top-ranked players in my guild quit because Black Pongji was nerfed"; Jamer: "Ice kept making songs afterward; it's just that his name is hard to use as an identifiable keyword"

[^ettoday-vk-882323]: [Game Music Creator Accuses VK克 of Plagiarism: Music Is Like Illustration; Plagiarism Should Not Be Tolerated — ETtoday Game Cloud](https://game.ettoday.net/article/882323.htm) — 2017-03-11 full disclosure by Waiting@H&&D; timeline from Passing Through Rainy Time and Space → Passing Through Time and Space → League of Angels theme song; 2016/5/14 Shanghai concert + 2017/2/4 creation lecture

[^cts-vk-201703131858055]: [VK克 Accused of Compositional Plagiarism; Rayark: No Collaboration Before Incident Concludes — CTS News](https://news.cts.com.tw/mol/campus/201703/201703131858055.html) — 2017-03-13 complete verbatim Rayark FB apology statement; "After this incident occurred, Rayark did not fully stop collaborating with VK on physical events" + "In the future, we will adopt the same standard as for song inclusion: before the controversy is settled, we will not collaborate in any form"; Passing Through Time and Space suspected of plagiarizing Puella Magi Madoka Magica

[^plurk-waiting]: [Waiting Rayark "Statement of Non-Use of Works" Plurk](https://www.plurk.com/p/m4l9hh) — 2017 Waiting publicly announced termination of collaboration with Rayark; signed statement of non-use of works; mentioned middle-school classmate relationship with Rayark founder Tony

[^disp-bbs-vk]: [Composer Terminates Collaboration Because Rayark Supported V.K克, Who Was Involved in Plagiarism — Disp BBS Gossip](https://disp.cc/b/163-9Vfm) — March 2017 PTT Gossip post; Waiting and Rayark founder Tony's middle-school classmate relationship; complete incident timeline

[^cedargames-wiki]: [Red Candle Games — Wikipedia](https://zh.wikipedia.org/zh-tw/%E8%B5%A4%E7%83%9B%E9%81%8A%E6%88%B2) — 2019-02-23 Devotion removed from Steam China; 2019-02-26 Red Candle announced complete delisting; 2019-04-19 Shanghai JuMiao Information Technology placed under investigation; 2019-06-17 Yangpu District Administration for Market Regulation revoked Shanghai JuMiao's business license

[^namuwiki-ice]: [Ice (composer) — NamuWiki](<https://en.namu.wiki/w/Ice(%EC%9E%91%EA%B3%A1%EA%B0%80)>) — Wilson Lam aka Ice; joined Rayark in 2014; resigned on 2020-07-18; revealed real identity through an article on 2022-07-17; currently active at Spaceport Productions producing trance + hardcore tracks

[^facebook-iceloki]: [Ice - Spaceport Productions Facebook Page](https://www.facebook.com/iceloki/) — ICE personal Facebook page, display name "Ice - Spaceport Productions," continuing to publish musical works

[^x-iceloki]: [Ice@Spaceport Productions — X (Twitter)](https://x.com/ice_loki) — ICE personal X account, bio "Ice@Spaceport Productions," Hong Kong musician

[^bnext-59103]: [Once Accused of Plagiarism During Development, Rayark Spent Four Years Hatching Soul of Eden; Surpassed 1.5 Million Downloads in One Week — Business Next](https://www.bnext.com.tw/article/59103/rayark-soul-of-eden) — Soul of Eden developed for 4+ years; 1.5 million downloads in first week; once accused of copying Clash Royale; Rayark official response

[^steamcharts-deemo-reborn]: [DEEMO -Reborn- Steam Charts — Steambase](https://steambase.io/games/deemo-reborn/steam-charts) — DEEMO -Reborn- Steam release on 2020-09-03; 20K-50K owners; 3,242 reviews rated "Very Positive"

[^udn-moastray]: [Taiwanese Team-Made MO:Astray — udn Game Corner](https://game.udn.com/game/story/10451/4126084) — MO:Astray 2019-2020 reception / action-puzzle genre
