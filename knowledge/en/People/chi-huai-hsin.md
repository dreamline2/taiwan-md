---
title: 'Chi Huai-hsin: The Taiwanese Researcher Who Taught AI to Think Step by Step and Brought Cognitive Psychology Into Machines'
description: "Chi Huai-hsin is a vice president of research at Google DeepMind and a co-author of the chain-of-thought paper that taught AI to reason step by step. Raised in Tamsui, this Taiwanese researcher turned the concept of how humans learn in cognitive psychology, Piaget's schema theory, into a method for teaching machines to reason. And the breakthrough that changed AI cost only about US$5,000, because it was never a problem that compute could solve."
date: 2026-06-27
author: 'Taiwan.md'
category: 'People'
subcategory: '科技與企業'
tags:
  [
    'People',
    'Chi Huai-hsin',
    'Ed Chi',
    'AI',
    'Google DeepMind',
    'chain of thought',
    'Chain of Thought',
    'cognitive psychology',
    'Tamsui',
  ]
lastVerified: 2026-06-27
lastHumanReview: false
featured: true
translatedFrom: 'People/紀懷新.md'
sourceCommitSha: '489ea1601'
sourceContentHash: 'sha256:50346fd81e3daf96'
sourceBodyHash: 'sha256:64d75052423ad414'
translatedAt: '2026-06-28T00:38:05+08:00'
image: '/article-images/people/ed-chi-deepmind-talk-2026.webp'
---

When the whole world was chasing AI with hundreds of millions of dollars in compute, one paper changed the way machines reasoned, at a cost of only about US$5,000.

That paper was called "Chain of Thought." What it did sounds almost too simple to count as a breakthrough: in the examples shown to an AI, add a few more lines of "solution process," guiding it to first work out the intermediate steps and then give the answer, like asking a student to draft the work before writing the conclusion directly. Among its nine co-authors was a Taiwanese researcher born in Tamsui: Chi Huai-hsin.

He later explained that US$5,000 this way: "That problem was not one that could be solved with compute. It was another mode of thinking."[^1]

> **30-Second Overview:** Chi Huai-hsin (Ed H. Chi) is a vice president of research at Google DeepMind and one of the co-authors of the chain-of-thought paper that taught AI to "reason step by step." Every time you ask ChatGPT or Gemini to "think step by step" and it answers better, the idea that lets machines reason in stages has a line running back to Taiwan. At around age 15, he immigrated to the United States with his mother, who was pursuing a PhD. While helping her write an educational psychology dissertation, he learned a psychological concept about "how humans learn": Piaget's schema theory. Thirty years later, he brought that concept into machines. Taiwan recognizes the "pride of Taiwan" who make chips, but it barely recognizes the person who helped shape "how AI thinks."

## His Mother's Doctoral Dissertation

The story does not begin at Google. It begins at a desk.

Chi Huai-hsin grew up in Tamsui. "I am someone born and raised in Taiwan. I was born in Tamsui, and then when I was about 15, I went to the United States with my parents to study, because my mother had gone there to pursue a PhD."[^2] Hidden inside that sentence is an uncommon scene: in those years, most Taiwanese children who went abroad did so alone as "little overseas students," but his whole family moved west because his mother was going to study for a doctorate. A Taiwanese family immigrating to the United States because of the mother's education was not common in that era.

![Sunset over the Youchekou boardwalk in Tamsui, where Chi Huai-hsin was born and raised](/article-images/people/tamsui-sunset-boardwalk-2024.webp)

_Tamsui, where Chi Huai-hsin was born and raised. More than thirty years later, something he took from here would become a method for teaching machines to think._

His mother was pursuing a PhD in educational psychology. During his high school and college years, he helped her write her dissertation. A child still in school helped his own mother organize an academic paper about "how humans learn." In that process, he first encountered Swiss psychologist Piaget's schema theory.

Schema theory says that the human mind contains organized structures of knowledge, called "schemas," through which we understand the world. When learning something new, we either fit the new information into an old schema, which is called assimilation, or the old schema cannot hold it and must be revised or rebuilt, which is called accommodation. This sounds abstract, but it answers a very basic question: how does a person go from "not knowing how" to "knowing how"?

The concept on that desk would, thirty years later, become a method for teaching machines to reason. But before that, he had to walk a long road, and one that few people were walking.

<div class="video-embed" style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;margin:1.5rem 0;border-radius:8px;">
  <iframe src="https://www.youtube.com/embed/51woDEK5NME" title="VK 科技閱讀時間 EP122 ft. 紀懷新" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

_In VK Tech Reading Time EP122, Chi Huai-hsin personally recounts the origin of chain of thought: from helping his mother write an educational psychology doctoral dissertation and learning Piaget's schema theory, all the way to turning it into a method for teaching AI to reason. This interview is the spiritual source of this article._

## From Tamsui to Minnesota, Following a Doctoral Admission Letter

After arriving in Minnesota, he completed high school, college, master's, and PhD work all at the same school: the University of Minnesota, earning three degrees in six and a half years.[^3] He entered with the highest honors, Summa Cum Laude. His doctoral dissertation was in information visualization, titled "A Framework for Information Visualization Spreadsheets," and his advisor, John T. Riedl, was a pioneer in recommender systems.

![University of Minnesota campus, where Chi Huai-hsin completed three degrees: bachelor's, master's, and PhD](/article-images/people/umn-the-knoll-minneapolis.webp)

_At age 15, he followed his mother to Minnesota. He later completed three degrees in six and a half years at the University of Minnesota. His advisor, John T. Riedl, was a pioneer in recommender-system research, a line that would later connect back to Chi's work at Google._

But more worth remembering than the degrees is how he positioned himself.

In an interview, he said something very honest: "In English, I would say I'm a generalist... the kind of researcher who is jack of all trades but master of none. But when I realized that my math was not better than other people's, I felt that perhaps I could do research that was more like bridging, a bridge between one field and another."[^4]

In academia, that is a costly choice. He himself has said that when you do bridging research, "you are not really a person in field A, and you are not really a researcher in field B either." The world gives someone who understands only one side a clear position; someone standing between two sides is often accepted by neither. But that in-between space was precisely where he placed his bet. Later events would show that several of AI's most important steps happened exactly in that kind of space.

> **✦** "Perhaps I could do research that was more like bridging, a bridge between one field and another."

## In Palo Alto, He Learned to Turn Psychology Into Programs

In 1997, he interned at a legendary place: Xerox PARC, the Xerox Palo Alto Research Center.

The name may be unfamiliar to Taiwanese readers, but you use things it invented every day. The mouse, graphical user interfaces, laser printers, Ethernet: many of the technologies that laid the foundations of the personal-computer era were born at this research center, set up by a copier company next to Stanford University. Steve Jobs famously visited, saw its graphical interface, learned from the idea, and turned it into the later Macintosh. When Chi arrived, PARC was in its second golden age.

![The Xerox Alto computer developed at Xerox PARC in 1973, a pioneer of personal computing and graphical interfaces](/article-images/people/xerox-alto-1973.webp)

_The Alto, developed by Xerox PARC in 1973, was a pioneer of personal computing and graphical interfaces. Later, at this site, Chi Huai-hsin learned to turn cognitive psychology into runnable programs._

The key was not what dazzling technology he built, but whom he encountered. "My own boss at the time was Stuart Card. He was a student of Allen Newell."[^5] That academic lineage leads upward to a Nobel laureate in economics: Herbert Simon.

Simon proposed "bounded rationality": when making decisions, humans are constrained by cognition, information, and time, and therefore cannot possibly be "fully rational." He also coined the term "satisficing," a "good enough" form of decision-making: people do not seek the optimal solution, only a solution that will do. Simon and Newell together analogized the human mind to an information-processing machine, arguing that "problem-solving" is a step-by-step search through a problem space. Card brought this line of thinking into Palo Alto, and Chi received it from Card.

> 📝 **Curator's Note**
> The standard AI story goes like this: machines are getting smarter because chips are getting faster, data is getting bigger, and models are getting larger. This narrative is convenient, but it misses another hidden line. As early as the 1950s, Simon was asking "how the human mind makes decisions under constraints"; in 1974, Card brought psychology into computer research at Palo Alto; in the 1990s, Chi Huai-hsin took up the baton and turned foraging theory into a model of how people search for information online. For half a century, a group of people kept pursuing the same question: how, exactly, do humans think? While the mainstream was busy making machines compute faster, they were busy making machines think more like people. Chain of thought is the fruit of that hidden line.

His main research at PARC was called "information foraging." The concept was that people searching for information online resemble animals foraging in the wild: they follow "scent"; when the scent is strong, they pursue it, and when it is weak, they give up. He engineered this biological and psychological foraging model into real runnable systems that predicted how people navigated among websites. This was the first practical test of "bridging": cognitive psychology on one side, information science on the other, and a bridge built in between.

```tw-timeline
1955 | Simon coins a term | Herbert Simon proposes satisficing and bounded rationality, viewing the human mind as an information-processing machine
1974 | Psychology enters the lab | Stuart Card brings the Newell-Simon tradition into Xerox PARC
1997 | Chi takes the baton | Chi interns at PARC and engineers foraging theory into an information-foraging model
2022 | Brought into machines | The chain-of-thought paper is published, turning cognitive psychology's "step-by-step reasoning" into a way to teach AI
Source: the scholars' Wikipedia entries and arXiv 2201.11903
```

## Not More Data, But More Like Humans

In 2011, he left PARC for Google. The reason was practical: "Research alone is not enough; you also have to build applied things." He had seen the Xerox model, where "basic research was very deep but could not be turned into products," up close.

At Google, he first worked on web data analysis. From 2015 to 2017, he led a team that rebuilt YouTube's neural-network recommender system. In 2017, he became chief scientist at Google Brain, leading a team of seventy people. In 2021, he was promoted to distinguished scientist, leading 120 people, and later became a vice president of research at DeepMind.[^6] Behind this string of titles is really the extension of a single methodological gene: information foraging was a model of "how people find things"; recommender systems were models of "what people want to watch"; and by the time of chain of thought, it became a model of "how people reason." From human cognition, all the way toward machines.

The turn toward chain of thought came from his dissatisfaction with a mainstream assumption in machine learning at the time. "Why does the machine need so much data before it can really learn?" he began to ask. "Could we use methods from cognitive psychology to teach machines to learn?"[^7]

So he returned to that concept. "This idea in fact came from... an idea from the 1960s and 1970s called schema theory. What it basically means is that if a person can use a template to solve a problem, perhaps we can also use this method to teach machines to learn. So chain of thought in fact began from this idea." When the interviewer asked whether this meant Piaget's schema, he answered: "Yes, exactly Piaget's schema idea. That was something I learned when I was in high school and college, because I was helping my mother write her doctoral dissertation in educational psychology. Later, slowly, these things connected together."[^8]

The seed on the desk had sprouted.

![Figure 1 from the chain-of-thought paper: the standard prompt on the left gives a wrong answer, while the chain-of-thought prompt on the right first writes out reasoning steps, highlighted in blue, before giving the correct answer](/article-images/people/chain-of-thought-figure1.webp)

_The most famous figure in the chain-of-thought paper: on the left, the model is asked in the ordinary way and calculates incorrectly; on the right, simply adding a stretch of reasoning process in the example, the blue-highlighted section, leads the model to answer correctly. The difference is not compute, but whether the model "writes out its thoughts step by step." Figure from Wei et al., 2022._

And it cost almost nothing. "Do you know how much compute we used in total? Probably only about US$5,000 worth of compute. Because that problem was not one that compute could solve; it was another mode of thinking. When we were doing that research, at the beginning there was basically no funding. It was something we thought up ourselves from nothing."[^1]

```tw-versus
Mainstream AI route | The chain-of-thought route
Larger models, more parameters | No need to retrain the model
Feed in more data | Add a few lines of solution process to the examples
Hundreds of millions of dollars in compute arms races | About US$5,000
Brute force in pursuit of scale | Borrow cognitive psychology from how humans learn
```

This is what this article most wants to say: the key to teaching AI to reason was not more compute, but becoming more like humans. And that "more like humans" grew out of an educational psychology doctoral dissertation that a child from Tamsui helped his mother write.

## He Told His Subordinate: Don't Use That Method; Try Schema

Here, we have to be honest.

The chain-of-thought paper had nine authors, and Chi Huai-hsin was listed seventh. The first author was Jason Wei, the main executor; the last author, conventionally the senior academic lead, was Denny Zhou, founder of Google Brain's reasoning research team. It would not be accurate to say this paper was "invented by Chi Huai-hsin." Denny Zhou was the leader of this research direction, and Denny Zhou was a researcher on Chi's team, his direct subordinate.

So what exactly was Chi's role? Listen to how he described it himself: "Denny Zhou was a researcher on my team. After he joined my team, he came to me and said he wanted to do research on reasoning... He was originally using a more traditional neural-symbolic method, and I told him I felt neural symbolic didn't seem to work very well. Could he consider other methods? Then we slowly discussed it and realized perhaps the concept of schema could be used."[^9]

That passage defines his real contribution. He was not the paper's main executor, but he was the person at the crucial fork who said, "Don't go that way." He rejected the neural-symbolic direction, which at the time seemed natural, and pushed the discussion toward schema. More importantly, he could think of schema because he had brought thirty years of cognitive-science perspective into the team. In other words, he was the person who made it possible for Denny Zhou to "possibly think of schema."

> 📝 **Curator's Note**
> The most common flaw in "pride of Taiwan" narratives is compressing a complex contribution into one sentence: "He invented X." But reality is often more interesting. What made Chi Huai-hsin truly irreplaceable was a twenty-year arc: he moved cognitive psychology into machines bit by bit, from information foraging to recommender systems and then to chain of thought. A paper can have nine authors, author order, and disputes over credit; but across the entire team, only he could spend twenty years continuously bringing the question of how humans think into engineering practice. To see his value, one has to zoom out to a twenty-year scale, rather than stopping at an author list.

He himself used a deeper framework to explain what came after chain of thought. When AI not only solves problems by following a template but can also "reflect" on its own thinking and revise it, he said: "In Piaget's cognitive science, or in learning sciences, this would be called assimilation and accommodation... This kind of real learning by machines seems to have truly begun."[^10] Solving a problem by following a template is assimilation; going back and rewriting the template is accommodation. He took the pair of concepts he learned while helping his mother write her dissertation and moved them intact into the description of machine learning.

He also connected chain of thought to another psychologist's framework: "Chain of thought plus fine-tuning, plus next-word prediction, seems to be the beginning of a reasoning machine, the so-called System 2 thinking, the kind Kahneman talks about."[^11] System 1 is intuitive, fast, effortless thinking: seeing a microphone and knowing it is a microphone. System 2 is effortful, rational thinking that requires step-by-step reasoning: the kind engaged when asked, "What is the definition of AGI?" In his view, past deep learning had already done System 1 deeply, while chain of thought was the starting point for machines beginning to do System 2.

## Reasoning Machines and Grandma's Standard

So when will AI really count as "arriving"? Chi Huai-hsin's answer is not in any technical benchmark. It is in grandma.

"The day your grandma scolds the robot at home and says, 'I already taught you once. How do you still not know?' then you will know AGI has arrived... Our benchmark grows out of grandma."[^12]

This line is sharper than it sounds. Today's robot vacuums still get tangled in cords and bump into furniture. We complain that they are dumb, but we do not truly get angry at them, because deep down we feel that "machines are supposed to be dumber than I am; teaching them several times is normal." But one day, if grandma scolds a robot the way she would scold a person who fails to learn, that means that in her mind she has already treated it as something that "should know after being taught once." The moment AGI arrives may be less like a score crossing a benchmark and more like a quiet shift in human expectations.

This also connects back to his view of artificial general intelligence. He believes two things are necessary for AGI: first, AI cannot live only in a virtual world; it has to integrate into real human living environments. Second, "I teach you once, and from then on you know"—it must be able to infer from one case to others and explore on its own, rather than requiring humans to teach it repeatedly. Project Astra, which he now leads, is about the first of these: a universal assistant that can perceive the situation you are in.

He has described a personal scene. About a year earlier, he brought the still-confidential Project Astra to a meeting in Barcelona. At a hotel rooftop bar, he took out his phone, scanned the city skyline, and asked it, "Where am I?" It answered, "It looks like you are in Barcelona." He followed up by asking which district it was, and it gave the correct district name. He then asked whether there were good restaurants nearby, "preferably with Michelin stars," and it answered that too. "I said, 'Can you help me make a reservation?' It said, 'Not yet, but maybe in the future.'" At that moment, he realized that this kind of personal assistant, one that really stays by your side and understands your situation, could be built within his lifetime.[^13]

<div class="video-embed" style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;margin:1.5rem 0;border-radius:8px;">
  <iframe src="https://www.youtube.com/embed/3rQ4jPvvY0c" title="塞掐 Sidechat E350 ft. 紀懷新" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

_In Sidechat E350, Chi Huai-hsin discusses smart glasses, the "grandma standard" for AGI, and Taiwan's opportunities. During the interview, he takes out a Project Astra smart-glasses prototype and says it should be Taiwan's first._

At the interview, he took a prototype pair of smart glasses equipped with Project Astra out of his pocket and said it "should be" the first such device in Taiwan. He discussed where Taiwan's greatest opportunities lie. Hardware is one piece: "Taiwan's position in semiconductors, especially manufacturing, is very hard to shake." But then he turned: "If Taiwan can integrate hardware and software well, using the capabilities of large language models, it is indeed a very big opportunity."[^14]

## Taiwan Recognizes Chips, Not This Mind

At this point, one question cannot be avoided: does he count as Taiwanese?

The facts are clear: he left Taiwan at around age 15, completed high school, college, and graduate school in the United States, and has spent his entire career in Silicon Valley. He is Taiwanese American, a person born in Taiwan and raised into achievement in the United States. If someone says that the "pride of Taiwan" label exploits someone who immigrated long ago, that criticism is not baseless.

But there are also concrete things on the other side of the scale. He gives interviews in Chinese and actively says that he was "born in Tamsui, born and raised in Taiwan," without avoiding it. He continues to return to Taiwan to speak, leaving traces at National Taiwan Normal University, National Chung Hsing University, and National Yang Ming Chiao Tung University. He has specific observations about Taiwan's long-term care crisis, semiconductor position, and AI startup ecosystem. He has even noted that Taiwan already has about 15,000 users of DeepMind's protein-structure prediction tool.

What best captures his position, both inside and outside, is something he once told Taiwanese researchers: "This part of the research, in fact, I have talked about it every time I have come back to Taiwan over these many years, but I have not seen Taiwanese researchers... do much in this area. It is research that can be done without many chips."[^15]

Two identities tug against each other in that sentence. He says "come back to Taiwan," speaking as someone who recognizes himself as belonging here. But "I say this every time, yet no one does it" also carries the distance of an outsider, like someone who has been away from home for a long time, returning to see one corner of the house still left untouched, anxious but unable to do much. Whether he counts as a pride of Taiwan is not a conclusion this article will make for you. The facts are here; judge for yourself.

> 📊 **The Numbers Behind Him**

```tw-stat
About US$5,000 | Compute used by the chain-of-thought paper | Compared with the industry's hundreds-of-millions-of-dollars arms race
About 114,000 | Total Google Scholar citations | 82% of them from after 2021
13% → 83% | OpenAI o1 accuracy on International Mathematical Olympiad problems | o1 is explicitly built on chain of thought
```

_Source: Chi Huai-hsin's VK EP122 interview, Google Scholar, OpenAI o1 System Card (arXiv 2412.16720)_

## Showing Reasoning: More Transparent, or Better at Giving Reasons?

Chain of thought lets AI "show" its reasoning process. On the surface, this makes machines more transparent: you can see how they think. But there is a concern here that an honest person should place alongside the achievement.

> ⚠️ **Controversial View**
> Chain of thought lays the AI's "thinking process" before you, making it look more credible and more trustworthy. But academics have already raised doubts: the reasoning string shown by a model does not necessarily reflect the internal process by which it makes decisions. In research, this is called the "faithfulness" problem of reasoning chains. In other words, it may arrive at the answer first and then produce a polished explanation for you afterward. Being better at giving reasons is not the same as being more honest. At the same time, in March 2026, a jury in Los Angeles, United States, found in a social-media addiction case that platforms including YouTube bore responsibility for adolescent addiction, and Google was assigned roughly 30% of the liability. Chi Huai-hsin became an ACM Fellow in part for achievements including YouTube recommender systems, yet he has almost never publicly discussed the harms algorithms may bring. A person who can make machines "better at reasoning" is, for now, silent on the question of whether accountability will become harder after machines get better at giving reasons. Pointing this out is not meant to denounce anyone. It is simply to say that when we take pride in a Taiwanese person standing at the forefront of AI, we should also keep these questions in view.

There is no clean answer to this contradiction, but there should not be one. A technology that makes AI more human-like will simultaneously amplify the best and most troublesome human traits. Humans reason, and humans also invent reasons for their decisions. Seeing both sides is what it means to take this seriously.

## And Then?

Chi Huai-hsin has observed an eight-year cycle: the internet in 1991, Google's birth in 1999, the iPhone in 2007, mature deep learning in 2015, and Gemini and ChatGPT in 2023. By this rhythm, the next turning point will arrive around 2031. By then, he says, "no one will be surprised that you are using large models to do things," just as no one today is surprised that you use a mobile phone.

The direction he is now betting on is bringing AI out of screens and into the real world: Project Astra, which can perceive your situation, and robots that can do household tasks. What moves him most when he talks is Taiwan's long-term care. "Could there really be some more affordable robots that can help with household chores?" Laundry, cooking, turning patients over, delivering medicine on time. When a society lacks workers, nurses are short-staffed, and hospitals have no beds, things that sound like science fiction are actually very practical hopes.

<div class="video-embed" style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;margin:1.5rem 0;border-radius:8px;">
  <iframe src="https://www.youtube.com/embed/nXVvvRhiGjI" title="Google Project Astra" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

_Google's official Project Astra vision video. This is the direction Chi Huai-hsin now oversees: a universal assistant that can share the same environment with you and understand the situation you are in._

Return to that desk.

A child from Tamsui followed his mother to Minnesota at around age 15 and, while helping her write an educational psychology doctoral dissertation, learned "how humans learn." Thirty years later, he turned that human concept into a method for teaching machines to think. One day, when your grandma says to the robot at home, "I already taught you once. How do you still not know?" the reason that machine can reason step by step, reflect, and infer from one case to others will have a long line behind it. One end of that line is a Silicon Valley laboratory. The other end is Tamsui.

## Image Sources

- Chi Huai-hsin lecture photo (hero): [GQ Taiwan "GQ Interview" Chi Huai-hsin](https://www.gq.com.tw/article/gq%E5%B0%88%E8%A8%AA-%E7%B4%80%E6%87%B7%E6%96%B0-ed-chi-2026) — fair use editorial commentary
- [Junyu-K / Wikimedia Commons](https://commons.wikimedia.org/wiki/File:20241130_淡水油車口木棧道的夕景.jpg) — CC BY-SA 4.0 (sunset over Tamsui Youchekou boardwalk)
- [SavagePanda845 (Elliot F) / Wikimedia Commons](https://commons.wikimedia.org/wiki/File:UMN-TheKnoll.jpg) — CC BY-SA 4.0 (University of Minnesota campus)
- [The wub / Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Xerox_Alto_I,_1973,_Computer_History_Museum.jpg) — CC BY-SA 4.0 (Xerox Alto computer)
- Chain-of-thought paper Figure 1: [Wei et al. 2022, arXiv:2201.11903](https://arxiv.org/abs/2201.11903) — fair use academic

## Further Reading

- [Jensen Huang](/people/黃仁勳) — the pride of Taiwan who makes AI run faster, the hardware side
- [Morris Chang](/people/張忠謀) — the founder of Taiwan's semiconductor industry, the mountain whose "position is very hard to shake" in Chi Huai-hsin's words
- [AI Industry](/technology/AI人工智慧產業) — Taiwan's position in the global AI supply chain
- [Taiwan's AI Development and Future Strategy](/technology/台灣人工智慧發展與未來策略) — the broader picture of AI in Taiwan
- [AI in Everyday Taiwan](/technology/台灣AI日常) — how AI has already entered Taiwanese life

## References

[^1]: [VK Tech Reading Time EP122: AI Evolution, AGI Prototypes, and a Lot of Psychology (ft. Chi Huai-hsin)](https://www.youtube.com/watch?v=51woDEK5NME) — Official VK interview with Chi Huai-hsin. At around the 52-minute mark, he personally explains that the chain-of-thought paper used only about US$5,000 in compute, the strongest first-hand evidence for its "anti-compute-arms-race" character.

[^2]: [Sidechat E350 (ft. Chi Huai-hsin)](https://www.youtube.com/watch?v=3rQ4jPvvY0c) — Official tech podcast interview from INSIDE. In the program opening, Chi introduces himself and states verbatim that he was born in Tamsui and moved to the United States with his mother at around age 15.

[^3]: [Ed H. Chi personal resume](https://www.edchi.net/resume) — Chi Huai-hsin's official website resume, recording his University of Minnesota BS in computer science (1992-1994), MS in computer science (1994-1996), and PhD in computer and information science (1996-1999), graduation with highest honors, and advisor John T. Riedl.

[^4]: [VK Tech Reading Time EP122: AI Evolution, AGI Prototypes, and a Lot of Psychology (ft. Chi Huai-hsin)](https://www.youtube.com/watch?v=51woDEK5NME) — Around the 56-minute mark, Chi describes turning toward "bridging" research because his math was not better than his peers', a key self-account for understanding his research style.

[^5]: [VK Tech Reading Time EP122: AI Evolution, AGI Prototypes, and a Lot of Psychology (ft. Chi Huai-hsin)](https://www.youtube.com/watch?v=51woDEK5NME) — Around the 5-minute mark, Chi explains the academic lineage at the Palo Alto Research Center: his boss Stuart Card was a student of Allen Newell. Proper names have been checked against academic sources ([Stuart Card Wikipedia](https://en.wikipedia.org/wiki/Stuart_Card)).

[^6]: [Ed H. Chi | Google Research](https://research.google/people/edchi/) — Official Google Research profile, recording his career trajectory and research areas at Google. Career details are also drawn from his personal resume at [edchi.net/resume](https://www.edchi.net/resume).

[^7]: [VK Tech Reading Time EP122: AI Evolution, AGI Prototypes, and a Lot of Psychology (ft. Chi Huai-hsin)](https://www.youtube.com/watch?v=51woDEK5NME) — Around the 9-minute mark, Chi explains that his dissatisfaction with "why machines need so much data to learn" was the starting point for chain of thought.

[^8]: [VK Tech Reading Time EP122: AI Evolution, AGI Prototypes, and a Lot of Psychology (ft. Chi Huai-hsin)](https://www.youtube.com/watch?v=51woDEK5NME) — Around minutes 9 to 10, the core first-hand account of the origin of chain of thought: schema theory, Piaget, and the personal link to helping his mother write an educational psychology doctoral dissertation. The spiritual core of this article.

[^9]: [VK Tech Reading Time EP122: AI Evolution, AGI Prototypes, and a Lot of Psychology (ft. Chi Huai-hsin)](https://www.youtube.com/watch?v=51woDEK5NME) — Around the 57-minute mark, Chi describes rejecting Denny Zhou's neural-symbolic method and turning toward schema, a first-hand basis for evaluating his role in the contribution. Paper authorship and order can be found at [arXiv 2201.11903](https://arxiv.org/abs/2201.11903).

[^10]: [VK Tech Reading Time EP122: AI Evolution, AGI Prototypes, and a Lot of Psychology (ft. Chi Huai-hsin)](https://www.youtube.com/watch?v=51woDEK5NME) — Around the 15-minute mark, Chi uses Piaget's assimilation and accommodation framework to describe the evolution from chain of thought to reflective reasoning, showing how directly he brings educational-psychology language into AI.

[^11]: [VK Tech Reading Time EP122: AI Evolution, AGI Prototypes, and a Lot of Psychology (ft. Chi Huai-hsin)](https://www.youtube.com/watch?v=51woDEK5NME) — Around the 17-minute mark, Chi connects chain of thought to Kahneman's System 1/System 2 framework from _Thinking, Fast and Slow_. Kahneman's _Thinking, Fast and Slow_ was published in 2011.

[^12]: [Sidechat E350 (ft. Chi Huai-hsin)](https://www.youtube.com/watch?v=3rQ4jPvvY0c) — In the opening and around the 60-minute mark, Chi proposes the "grandma standard" for AGI: when grandma scolds a robot the way she would scold a person, saying "I taught you once, how do you still not know?", AGI has arrived.

[^13]: [Sidechat E350 (ft. Chi Huai-hsin)](https://www.youtube.com/watch?v=3rQ4jPvvY0c) — Around the 30-minute mark, Chi recounts taking the confidential-stage Project Astra to Barcelona, scanning the skyline from a hotel rooftop bar, and having it correctly identify the city and district.

[^14]: [Sidechat E350 (ft. Chi Huai-hsin)](https://www.youtube.com/watch?v=3rQ4jPvvY0c) — Around the 40-minute mark, Chi comments that Taiwan's position in semiconductor manufacturing is "very hard to shake" and that hardware-software integration is a "very big opportunity" for Taiwan.

[^15]: [Sidechat E350 (ft. Chi Huai-hsin)](https://www.youtube.com/watch?v=3rQ4jPvvY0c) — Around the 52-minute mark, Chi calls out to Taiwanese researchers: this kind of research "does not need many chips" to do, yet after years of returning to Taiwan and saying this every time, he has not seen Taiwanese researchers invest much in it. This passage most clearly shows the tension in his outsider-insider identity.
