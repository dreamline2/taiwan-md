---
title: "Taiwan's BIM and Construction Tech: Twelve Years of Case-by-Case Government Push Rewritten by an 18-Month Protocol"
description: "On May 23, 2014, the Public Construction Commission launched the 'Public Engineering BIM Promotion Platform' with the eight-character policy of 'case-by-case adaptation and gradual progress.' Eleven years and seven months later, a Taiwanese developer working in Tokyo pushed the repository named REVIT_MCP_study to GitHub, garnering over 70 stars and 80 forks. In between, Taiwan's construction industry traversed a long path from hand-drawn blueprints to 3D models, from individual attempts to national standards, and from tool upgrades to the redefinition of professions."
date: 2026-05-22
tags:
  [
    'Technology',
    'BIM',
    'Building Information Modeling',
    'Construction Technology',
    'Architecture',
    'Digital Transformation',
    'Revit',
    'MCP',
    'AI',
    'CTCI',
    'AECOM',
    'Shuotao',
  ]
subcategory: 'Construction Technology'
author: 'Taiwan.md'
category: 'Technology'
readingTime: 22
lastVerified: 2026-05-22
lastHumanReview: false
translatedFrom: 'Technology/台灣BIM與營建科技.md'
sourceCommitSha: '31a05c44'
sourceContentHash: 'sha256:5500ed1d9d4e0f85'
translatedAt: '2026-06-16T16:55:29Z'
sourceBodyHash: 'sha256:6207b1decb9dcfc4'
image: '/article-images/technology/freecad-bim-example-2024.webp'
imageCredit: 'Maxwxyz via Wikimedia Commons'
imageLicense: 'CC BY 4.0'
imageSource: 'https://commons.wikimedia.org/wiki/File:FreeCAD_1.0_Dark_BIM_Example.png'
---

# Taiwan's BIM and Construction Tech: Twelve Years of Case-by-Case Government Push Rewritten by an 18-Month Protocol

![FreeCAD 1.0 Open Source BIM Workbench Dark Theme Screenshot, showing a 3D model of a demonstration building in the center, the left panel listing various professional layers (structure, MEP, shell), and the bottom toolbar displaying BIM workbench-specific commands, reflecting the essence of engineering digital transformation where BIM systematizes building information](/article-images/technology/freecad-bim-example-2024.webp)
_FreeCAD 1.0 Dark Theme BIM Workbench Demo File. Photo: Maxwxyz, 2024-10-07. [License via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:FreeCAD_1.0_Dark_BIM_Example.png)._

> **30-Second Overview:** On May 23, 2014, the Public Construction Commission (PCC) launched the "Public Engineering BIM Promotion Platform" [^1], adopting a three-phase promotion based on the principles of "case-by-case adaptation and gradual progress," which remains non-mandatory to this day [^2]. During this same period, the National Taiwan University BIM Research Center offered its first course, the Taiwan BIM Industry Association was officially established [^3], the New Taipei City Government issued the first BIM building permit, and the Taipei City Department of Urban Development announced竣工 model operation specifications [^4], while BSI signed the MOU for the Taiwan BIM Task Group [^5]. Eleven years and seven months later, on December 10, 2025, a developer named CHIANG SHUOTAO pushed the repository `REVIT_MCP_study` to GitHub, accumulating 73 stars and 85 forks [^6]. Four months later, in April 2026, Autodesk announced that Revit 2027 would include a built-in Model Context Protocol server [^7]. The twelve years the government struggled to push forward, juxtaposed with an 18-month protocol from Anthropic, reveal the slow professional redefinition of Taiwan's construction industry from drafting to system integration.

---

## The Public Construction Commission's "Case-by-Case Adaptation"

On May 23, 2014, the Public Construction Commission of the Executive Yuan established something called the "Public Engineering Building Information Modeling (BIM) Promotion Platform" [^1]. The eight-character policy on the day of its launch was "**Case-by-Case Adaptation, Gradual Progress**."

These eight characters have been cited for many years.

The PCC divided its promotion strategy into three phases: Phase 1 (Republic of China Year 103 / 2014) "Encouragement and Pilot Selection," inviting non-building engineering host agencies to participate in pilot projects, prioritizing general contracting (EPC) bids based on best value; Phase 2 (Years 104-105 / 2015-2016) "Pilot Execution and Evaluation"; and Phase 3 "**Promoting the Use of BIM Technology in Public Engineering Projects Above a Certain Amount Starting from Year 106**" [^1].

However, the threshold of "above a certain amount" never became a universal mandate by 2026. The phrasing repeatedly emphasized by the PCC was "**Host agencies of engineering projects shall assess whether to adopt BIM technology based on individual case needs and the agency's contract management capabilities, rather than as a comprehensive, mandatory regulation**" [^2].

The control group is Hong Kong. The Hong Kong Development Bureau had long mandated the use of BIM for engineering projects with a cost estimate exceeding 30 million HKD [^8]. In Taiwan, the verbs "encourage," "pilot," and "self-assess" appear in turn in every white paper.

Public data available up to the search date shows that the PCC BIM platform has cumulatively seen "**over 60 engineering bidding agencies using BIM technology, with more than 120 application projects**" [^2]. Placed against Taiwan's annual public engineering projects numbering over 10,000, this figure is insignificant.

> **📝 Curator's Note**
> The common narrative is "The government couldn't push BIM because the industry couldn't keep up." This explanation is narratively convenient, but it reverses the causality. **The true sequence is closer to this: The government decided not to mandate BIM starting from 2014, because mandating it would mean wiping out the livelihoods of half the architectural firms.** Case-by-case adaptation is a political calculation: leaving the choice to the minority of agencies "capable of contract management," while the rest continue using AutoCAD, with no one disturbing the other.

---

## The Ministry of the Interior, Taipei, and New Taipei: Three Asynchronous Promotion Axes

The Public Construction Commission pushed its own agenda, while the Ministry of the Interior's Architectural Research and Information Institute (ABRI) pushed its own.

ABRI launched the "**Building Information Integration Sharing and Application R&D Promotion Plan**," a 4-year medium-term case plan, starting in Republic of China Year 104 (2015) [^9]. In Year 108 (2019), it connected to the second phase 4-year plan [^9]. The two major goals of the second phase were written broadly: "**Digital Upgrade of Building Technology**" + "**Digital Living Environment for Buildings**," with the latter aiming to integrate BIM with GIS and IoT to create a digital city [^10].

However, ABRI is not the executive agency for building management. Building management lies with county and city governments.

In 2014, **the New Taipei City Government issued the first building permit approved based on a BIM model** [^11]. That same year, New Taipei City announced the "**New Taipei City Public Building BIM As-Built Model Information Delivery Criteria**." By 2026, the New Taipei City Government's "Building Permit Computer-Aided Review System" (bim.ntpc.gov.tw) had accumulated over 20 completed BIM models [^11].

Four years later, on November 6, 2018, **the Taipei City Government Department of Urban Development announced the "Taipei City Government Department of Urban Development Hosted Building Engineering Building Information Modeling (BIM) As-Built Model Attribute Data Operation Specifications"** [^4]. Taipei's specifications reference the international COBie (Construction Operations Building Information Exchange) format and incorporate relevant standards from the Ministry of the Interior's ABRI in Year 104 and the UK [^4]. The specifications require that when using different BIM modeling software, **IFC** (Industry Foundation Classes, an open international standard formulated by buildingSMART International, ISO 16739-1:2024) and COBie standard data must be exported and submitted [^4][^12].

> **💡 Did You Know?**
> IFC is an open international standard formulated by a non-profit organization called buildingSMART International [^12], unrelated to Autodesk or any single vendor. Its existence logic is similar to PDF: allowing models created by different software (Revit, ArchiCAD, Tekla, Navisworks) to be exchanged seamlessly. **The Danish government mandated the use of IFC format for public construction projects starting in 2010, and Norway, Finland, and Singapore followed suit** [^12]. Taiwan only incorporated IFC into specifications at the local level via the Taipei City Government in 2018. International standards had moved forward a decade earlier; Taiwan slowly caught up.

The timelines for the three axes of the Central Government, Taipei, and New Taipei were all asynchronous. For the same metro station, the design phase might use the Taipei Metro Bureau's BIM regulations (bound into the EPC contract), the building permit phase might use the Taipei City Department of Urban Development's as-built model operation specifications (COBie format), and the operation phase might fall into another set of facility management tools.

"**Currently, most public sector applications of BIM belong to the design and construction phases, and there are differences in application between traditional and EPC projects; subsequent operation and management models still adopt traditional practices**" [^13] — this is written in ABRI's own achievement report.

---

## Wanda Line, Miaoli Station, Taoyuan Airport T3: BIM Enters Public Engineering

In 2011, **the Taipei Metro Wanda Line included BIM in the engineering design contract for the first time** [^14].

This is a frequently cited "first" event in Taiwan's BIM promotion. Each section of the Wanda Line was required by contract to use the BIM mode for metro station body design, simultaneously introducing architecture, structure, and MEP disciplines for cross-disciplinary integration, **reducing design interface conflicts** [^14].

Following the Wanda Line, public engineering projects followed one after another. Taipei Metro Circular Line Y19 Elevated Station, multiple sports centers in New Taipei, Taiwan High Speed Rail's new Miaoli Station, Taoyuan Airport Terminal 3, Kaohsiung Circular Light Rail: every project has a case study written in the internal journals of ABRI, NTU NTUBIM, or the Metro Bureau.

The most cited "**Digital Victory**" is Taiwan HSR's Miaoli Station: BIM was introduced three months before groundbreaking, and the supervision team discovered multiple conflict points from the 3D model, **saving 20% in subsequent design change costs and allowing site layout to start two months ahead of schedule** [^15].

Taoyuan Airport Terminal 3 is another case of a different scale. In March 2021, **a team composed of Samsung C&T and Ronggong Engineering won the bid for the T3 main terminal building civil engineering with a new NT$44.5 billion** [^16]. The entire T3 is led in design by AECOM Engineering Consulting (along with Rogers Stirk Harbour + Partners and Ove Arup and Partners Hong Kong), relying on cross-border collaboration through BIM model flows between firms — this is AECOM's signature case repeatedly used in internal training materials [^17].

> **✦** The moment the Wanda Line first wrote BIM into the contract in 2011 was a quiet watershed in Taiwan's public engineering history. From that day on, none of Taiwan's major public engineering projects — metro, airport, HSR, light rail — would ask "how to do BIM" without it.

But these are all "indicator cases." All indicator cases in Taiwan share only one common flaw: **they are few**.

---

## Five Major Engineering Consultants + Two Organizations: The People Behind

The people pushing BIM into public engineering have names and faces.

**AECOM Engineering Consulting Co., Ltd.**: Established in 2007 through investment from the China Engineering Consultants Inc. (CECI, founded in 1969) [^18]. **In 2010, it was the first to establish a BIM Integration Center** [^19], one of the earliest in Taiwan's industry. Nearly 2,000 colleagues have 90% backgrounds in highways, railways, ports, airports, bridges, structures, tunnels, metro, architecture, mechanical, electrical, system control, BIM, ITS, PPP, etc. [^19].

**Sinotech Engineering Consultants**: Founded in 1970, transformed into an NPO in 1994, and then invested in Sinotech Engineering Consultants Co., Ltd. [^20]. Sinotech later turned BIM into something called "**Project Management Information System (PMIS)**": Based on the spirit of the ISO 19650 Common Data Environment (CDE), it contains seven main modules to assist in cross-disciplinary, cross-project information integration [^21].

**Evergreen Consulting Engineering Co., Ltd. (EGC)**: Founded in 1974. The structural design of Taipei 101 and the T&C Tower in Kaohsiung (85 floors) were both done by it [^22]. **CTBUH (Council on Tall Buildings and Urban Habitat) lists EGC as one of the top ten tall building structural consultants globally** [^22].

On the academic side, there are two key nodes:

**National Taiwan University Civil Engineering Information Simulation and Management Research Center (NTUBIM)**: Established in 2011, with Director Professor **Hsieh Shang-Hsien** from the Department of Civil Engineering. Co-founder Associate Professor **Kuo Jung-Chin** wrote an article titled "**BIM Development Impacting the Current Building System**" in December 2011 [^23], which remains one of the landmark early documents in Taiwan's BIM academic discourse. NTUBIM later took on multiple commissioned projects from ABRI and the Public Construction Commission, leading Taiwan's BIM collaborative operation guidelines and the Chinese translation of ISO 19650.

**Taiwan BIM Industry Association (TBIMA)**: Preceded by the Taiwan BIM Technology Enthusiasts Gathering in 2009, preparation started in 2011, and it was **officially established as a registered association under the Ministry of the Interior on March 10, 2012** [^3]. The association's main members come from Autodesk Taiwan's original training instructors in 2008: the lineage of Taiwan's BIM civil organizations grew directly from the Autodesk certified instructor circle.

> **📝 Curator's Note**
> At the MOU signing ceremony for the Taiwan BIM Task Group on October 3, 2018 [^5], five faces sat at the table: BSI (British Standards Institution) Taiwan, NTU NTUBIM, Taiwan Construction Research Institute, Taiwan Building and Technology Center, and TBIMA. **The Ministry of the Interior's ABRI was a "guiding unit" rather than a "signing unit,"** a hierarchical arrangement worth pondering. It implies that the government acknowledges that for international BIM standards, it is best to let academia and civil organizations take the lead, stepping back to the second line. The following year, BSI released the "**Chinese Version of ISO 19650**" [^24], a small soft declaration of sovereignty: Taiwan finally had its own official Chinese translation of international BIM standards.

---

## Revit, ArchiCAD, Tekla: The Undercurrents of Software Hegemony

![Autodesk Revit 2024 Operation Screen Screenshot, showing an object-oriented presentation of a simple partition wall along with doors and windows in 3D space, the left side is the component attribute panel, and the bottom right is the real-time synchronized preview of plan, elevation, and section views, reflecting the object-oriented modeling essence of BIM software](/article-images/technology/autodesk-revit-2024-bim-objects.webp)
_Autodesk Revit 2024 BIM Component Demo. Photo: DanielDefault, 2024. [License via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Revit_2024.png)._

Walk into any firm in Taiwan that has adopted BIM, and 90% of the startup screens will show Revit.

"**In Taiwan, 90% of architects (with BIM design capabilities) use Revit Architecture**" — this is the number written on the website of an ArchiCAD distributor [^25]. Although it is a single-source citation, it aligns with industry perception: Revit is near-monopolistic in Taiwan's architectural design field.

ArchiCAD is developed by the Hungarian company Graphisoft, running on Mac and Windows. It has a more intuitive design and a gentler learning curve than Revit, but users in Taiwan are significantly fewer [^26]. The agent Longting Information has held many demo sessions in Taipei's East District, and every time designers say: "I know how to use Revit, the firm only has Revit licenses." This is the lock-in of scale effects.

The steel structure field is another axis. **Tekla Structures (a Trimble company product, formerly XSteel) is currently the mainstream software for steel structure design in Taiwan** [^27]. Tekla's ability to handle steel structures is recognized by the industry in the fields of high-rise buildings, bridges, stadiums, and factories.

Infrastructure (railways, highways, tunnels) leans towards Bentley Systems' MicroStation system [^28]. CTCI, Sinotech, and AECOM use MicroStation along with Bentley's OpenRoads / OpenBridge for large EPC general contracting projects and cross-border rail engineering.

Running on these mainstream software are Autodesk's own Dynamo (visual programming) and the open-source pyRevit (Python extension framework). **In early 2016, Autodesk Taiwan specifically invited instructors from the Dynamo R&D team from Singapore to teach in Taiwan** [^29], after which Dynamo gained attention in Taiwan's BIM engineer circles. A typical scenario: an MEP engineer writes a Dynamo script to automatically sort the coordinates of all ducts, check clear heights, and generate section drawings — what used to take a whole day with CAD is now done in minutes [^30].

The stage for clash detection belongs to Autodesk Navisworks. Navisworks Manage integrates 3D navigation, clash detection, report export, 4D schedule simulation, and 5D cost estimation [^31]. In Taiwan's metro MEP engineering, there is a specialized term called **CSD / SEM** — CSD (Combined Service Drawing) is the MEP comprehensive drawing, and SEM (Structure / Electric / Mechanic) is the structure-MEP integrated drawing. Traditional methods used CAD overlay and paper verification; in the BIM era, Navisworks runs clash checks, finding conflict points from a 3D perspective [^32].

"**CSD/SEM Drawing Integration**" — these six words are now a required service listed on the websites of Taiwan's BIM consulting firms.

---

## CTCI, Hutsu, Dacin, Obayashi: Who Builds Taiwan

![Taipei Dome Construction Site Street View, June 21, 2020, morning, the steel structure iron shell of the Taipei Dome in the distance is still under construction, a Hino 300 truck in the foreground passes the crosswalk near Exit 5 of the Guomindang Memorial Station on Zhongxiao East Road, reflecting the reality of Taipei's largest sports venue's decade-long construction and Obayashi's role in the construction management of this 65,000-ton circular steel pipe dome](/article-images/technology/taipei-dome-construction-cheng-2020.webp)
_Taipei Dome Construction Site, 2020-08-16, near Exit 5 of Guomindang Memorial Station on Zhongxiao East Road. Photo: Cheng-en Cheng, 2020-08-16. [License via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Taipei_Dome_and_Hino_300_BEM-5593_%2850281669428%29.jpg).\_

The main force supporting Taiwan's large-scale construction market is a group of general contracting engineering companies — they encountered BIM earlier than architectural firms and treated it as a production tool earlier.

Number one is **CTCI Group (Stock Code 9933)**. CTCI was jointly invested by the China Technical Services Society (CTSS), China Development Industrial Bank, and Central Investment Corporation in 1979 [^33] — this background is special: CTSS, founded in 1959, is a technical transfer institution serving Taiwan's industrial development. In the 1970s, during the boom of the petrochemical industry, it undertook a large amount of technical consulting work from state-owned enterprises like CPC. In 1979, CTSS spun off its engineering consulting business, becoming CTCI.

CTCI's business is **EPC** (Engineering, Procurement, Construction, a one-stop general contracting for engineering design/procurement/construction): refining, petrochemical, chemical, power, steel, storage and transportation, transportation, incinerators, public construction, and environmental engineering [^33]. As of 2021, it had 7,500 employees and established branches/offices in 15 countries [^33][^34]. The Saudi Arabia Amine Project, Saudi Kayan Ethylene Cracker General Contracting Project, SAMAC MMA and PMMA General Contracting Project — these names strung together are the Middle East footprint of Taiwan's EPC firms over the past 20 years [^33].

In 2011, an event that rewrote CTCI's shareholder structure occurred: **Japanese company Chiyoda Chemical Engineering acquired CTCI's shares, becoming the largest shareholder** [^33]. This is Taiwan's largest local general contracting company, now with its largest shareholder being a Japanese chemical engineering group. Most people don't know this trivia.

> **⚠️ Controversial Viewpoint**
> Overseas engineering for large EPC firms like CTCI is not without controversy. In 2017, a major delay and bad debt occurred in CTCI's natural gas treatment plant EPC project in India, with the group admitting "**fatal gaps in international risk control**" [^35]. That same year, the Kuoguang Petrochemical project was cancelled, and health disputes among Miaoli Liu-Liu residents continued to fester; multiple petrochemical projects involving CTCI were named in environmental narratives. BIM helped with engineering precision in these major cases, but precision does not solve land, labor, and environmental political problems.

In the private developer market, there is another group of names: **Hutsu Construction** has "accumulated the largest total floor area of high-tech factory buildings in the country" [^36]; **Dacin Engineering (2535)** is viewed by outsiders as "**TSMC's exclusive construction firm**," winning the order for the upper structure engineering of TSMC's Nankang 18P3 FAB plant [^37]. Dacin's BIM department wrote in internal briefings: "**Using BIM as a foundational tool platform for the development, planning, design, and construction-related integration and coordination of architectural projects**" [^37] — but this only accounts for a small portion of Dacin's contracted projects.

Foreign firms have two structural presences in Taiwan. **Taiwan Obayashi Construction** is the branch established by Japanese Obayashi Corporation (the builder of Tokyo Skytree) in 1989, constructing the entire Taipei 101, Taipei Metro Xinyi Line, Taoyuan Airport T3, and **Taipei Dome** [^38]. **Obayashi's Taiwan Branch website's "Company Profile" page explicitly lists "Construction Drawing Management and BIM Application" as main construction management items** [^38].

> **💡 Did You Know?**
> The entire steel structure of the Taipei Dome weighs 65,000 tons, making it the only dome in the world entirely constructed using circular steel pipes [^39]. Steel structure design is mostly done in Tekla Structures, and the model is imported into Navisworks for clash detection with other disciplines (MEP, fire protection). **Without BIM, completing a steel structure project of the Taipei Dome's scale without major errors would be almost impossible** — which is why Obayashi lists BIM in the "main construction management items" list of its company profile.

---

## Labor Shortage, Aging, Migrant Workers: Why Digital Transformation is Inevitable

Pull the scene to a typical morning on a construction site: 6:30 AM, workers arrive one by one. More than half are "grandpa-level" workers over 40 years old.

**New Taipei City Government's occupational disaster death statistics show that among 100+ death cases, over 77% are over 40 years old** [^40]. This number is already common knowledge in the civil engineer circle. Taiwan's construction industry labor force aging is a reality, not a trend in the making.

Low birth rates mean young people are not entering the construction industry. Difficult site conditions, uncompetitive salaries, and high casualty rates — the combination of these three things makes recruitment pressure in the construction industry increasingly severe [^40]. The Ministry of Labor agreed to open 15,000 migrant worker quotas for the construction industry in 2024, and by early 2026, they were "**about to be fully allocated**" [^41].

This is why digital transformation has become a must-do for the construction industry.

**BIM engineer job demand is high, with new hires earning 35,000-45,000 TWD/month, and 104 job positions with monthly salaries of 50,000+ TWD on 1111 Job Bank** [^42]. But "high demand" and "usable" are two different things — "**Learning BIM does not necessarily lead to significant salary growth, and most people choose more economical learning paths**" [^43]. Where is the career ceiling for BIM engineers? The industry has no consensus.

A deeper structural problem is: BIM pulls architects from the professional category of "**drafting**" to the new category of "**system integrator**." Tool upgrade is just the surface.

Architects drawing with AutoCAD draw collections of 2D lines. Drawing plans, elevations, sections — each drawing is independent, changing the plan and forgetting the elevation is daily routine. Engineers using Revit/BIM build an information model: behind every line is bound material, specification, vendor, price, construction sequence, maintenance cycle [^44]. Change the plan, and the elevation and section automatically sync.

Old architects look at young BIM engineers and say "this is a new generation's thing," but the real reason is simple — **that profession belongs to a different trade than the "architect" they entered the industry with**.

> **✦** "**BIM models often become outsourced work, disconnected from actual engineering, and many BIM centers or teams dissolve**" [^45] — this is NTU BIM Research Center's own observation of Taiwan's BIM promotion status.

---

## The USB-C-like Protocol: How Anthropic Connected AI to Revit

On November 25, 2024, Anthropic open-sourced something called **Model Context Protocol (MCP)** [^46].

The official announcement was written scientifically: "**MCP is an open standard, open-source framework introduced by Anthropic to standardize the way artificial intelligence (AI) systems like large language models (LLMs) integrate and share data with external tools, systems, and data sources**" [^47]. Anthropic's explanation is more colloquial: "**Think of MCP like a USB-C port for AI applications**" [^46] — just as USB-C unified device connections, MCP aims to unify the connection protocol between AI and data sources/tools.

Accompanying the MCP announcement were Python, TypeScript, C#, Java SDKs, plus pre-built MCP servers connecting Google Drive, Slack, GitHub, Git, Postgres, Puppeteer [^46].

The following events happened at a speed no one predicted.

On December 10, 2025, a developer named **CHIANG SHUOTAO** pushed the repository `REVIT_MCP_study` to GitHub [^48]. The repository description had only eight English words: "LEARN HOW TO BUILD UP YOUR REVIT MCP." Language distribution: **C# 54.2%, JavaScript 18.7%, PowerShell 14.3%, TypeScript 7.0%, HTML 3.3%, Shell 1.2%** [^48]. By May 2026, this personal repo had accumulated **73 stars and 85 forks** [^6].

Shuotao's GitHub personal page location is written as "Tokyo," but the README and all teaching documents are in Traditional Chinese, with content heavily echoing Taiwan's construction industry workflows. His peripheral repositories — `CAD_MCP_study`, `NAVISWORK_MCP`, `IFCSH` — form a personal open-source experiment series of BIM × MCP × AI [^49].

How to read this case?

It is not "Taiwan has its own BIM_MCP" — Shuotao's repo is part of the same ecosystem as the international `mcp-servers-for-revit/revit-mcp` and Autodesk's own Revit 2027 built-in MCP server [^7][^50]. Its significance lies in: **a Taiwanese developer, less than 13 months after Anthropic announced MCP, created a 70-star open-source teaching project, connecting international Revit MCP engineering practice back to the Chinese-speaking community**.

Four months later, **in April 2026, Autodesk announced that Revit 2027 would include a built-in MCP server and Autodesk Assistant** [^7]. The new Autodesk Assistant can do things like: "**Find all rooms missing MEP labels**," "**Set the fire rating of all doors in Phase 2 to 90 minutes**," "**Generate all plumbing views for this floor**" [^7] — operating Revit with natural language.

Things that used to take one to two years to learn in Revit can now be done by saying a sentence in Chinese (or English).

> **📝 Curator's Note**
> Aligning the timeline: From the PCC BIM platform launch on May 23, 2014, to Anthropic open-sourcing MCP on November 25, 2024, **10 years and 6 months passed**. During these 10 years of government BIM promotion, it went from "encouraging pilot" to "case-by-case adaptation," never reaching mandatory status. From Anthropic open-sourcing MCP to Autodesk Revit 2027 built-in MCP announcement, **only 17 months passed**. The speed at which a technology platform rewrites industry onboarding far exceeds the speed of policy promotion. **The real gap lies in the structure of two different promotion modes** — mandatory promotion requires coordinating hundreds of stakeholders, balancing dozens of industry lobbies, and adjusting multiple laws; platform promotion only requires open-sourcing the SDK and writing good documentation. Seeing this structure clearly is more important than complaining about the government or worshipping AI.

---

## From Drafting to System Integration: An Unfinished Professional Redefinition

Push the lens back to the 1990s architectural firm.

Back then, the firm's walls hung drafting tables, T-squares, needle pens, and blue-line printers. Architects drew plan views with needle pens on A1 large paper, and after finishing one, they sent it out to the blue-line printer for copies — the machine hummed, and blue-background white-line blueprints slowly rolled out from the other end. Change one thing, redraw the whole sheet.

AutoCAD released its Classic Mac OS version in 1992 and its Microsoft Windows version in 1993 [^51]. Taiwan architectural firms began large-scale adoption of CAD from the mid-1990s. The transition pain lasted about ten years — old architects resisted, young designers embraced, and firms split into two factions: "drawing on CAD" and "drawing on the desk."

From AutoCAD to Revit was the second transition. **Autodesk only introduced the term "Building Information Modeling" alongside Revit in 2002** [^52] — meaning, from hand-drawing to CAD and from CAD to BIM, the interval was about twenty years. But the pain of BIM transition is deeper than CAD transition, because this time the required level rose from tool replacement to **mindset restructuring**.

CAD digitizes your lines. BIM requires you to systematize the information of the entire building. A wall becomes a data object: "Partition wall for 2nd Floor Zone A office space, material: 12mm double-sided gypsum board plus 75mm light steel keel, fire resistance 1 hour, vendor XX, cost YY, construction sequence after MEP piping," no longer just two parallel lines.

Cross-disciplinary integration also changed. The traditional process was architects drawing plans, structural engineers drawing plans, MEP engineers drawing plans, and three sets of drawings finding conflicts when overlaid on site — a duct passing through a beam, a drain pipe hitting a structural column. The BIM process overlays drawings in the same 3D model during the design phase, completing clash checks and conflict reviews on the computer [^32].

"**Reducing design interface conflicts**" — these six words are written in the effectiveness reports of all Taiwan BIM case studies [^14][^15]. But the professional change behind these six words is: the power structure of architects, structural engineers, MEP engineers, and construction firms is being reshuffled. **In the past, the architect was the single author of the design phase; in the BIM era, design is a system integration of multi-party collaboration.**

This professional redefinition is not yet complete.

> **✦** "**Owners lack sufficient understanding of BIM applications, often operating with traditional engineering processes, limiting BIM technology effectiveness**" [^53] — this is BSI's most direct observation of Taiwan's owner-side issues. The bottleneck in pushing BIM is on the owner side; whether engineers can use it or not is secondary.

---

## What Comes Next

In May 2026, the situation of BIM in Taiwan is as follows:

- The central government has pushed for 12 years and still remains "case-by-case," without universal mandate [^2]
- Taipei and New Taipei have required BIM models at the building permit level since 2014/2018, but county/city specifications differ [^4][^11]
- Large engineering consultants (AECOM, Sinotech, Evergreen) and large construction firms (CTCI, Hutsu, Dacin, Obayashi) are all using it, with high demand for BIM engineer positions [^17][^19][^33][^42]
- Most small and medium architectural firms still rely on AutoCAD, with BIM penetration rate estimated in single-digit percentages [^43][^45]
- 17 months after Anthropic MCP open-sourcing in 2024-11, Autodesk Revit 2027 built-in MCP server was announced [^7][^46]
- A Taiwanese developer wrote a 73-star Revit MCP teaching repo, connecting the international ecosystem back to the Chinese-speaking community [^6][^48]

Connecting these six points, **Taiwan's BIM is a story of a profession being redefined from the outside by a technology platform**, still far from the appearance of a mature industry. The government's promotion speed cannot keep up with technology iteration, and the private sector's adoption speed cannot keep up with population aging. Taiwan's construction industry is pulled by three forces simultaneously: aging traditional practitioners, labor-short construction sites, and the new generation of AI × BIM tools.

In the next decade, the profession of "architect" in Taiwan may no longer look like it does now. The drafting part will be handed over to AI — changing the door fire rating for the entire project with a single sentence "**Set the fire rating of all doors in Phase 2 to 90 minutes**" [^7]. Architects' work will be closer to "**system integrator**," "**translator between owners and technology**," "**curator of multi-party collaboration**."

When the Public Construction Commission BIM platform first met on May 23, 2014, Taiwan HSR's Miaoli Station had not yet been built. On April 2026, when Autodesk announced Revit 2027's built-in MCP, TSMC's next fab in Kaohsiung was already preparing with full BIM drawings. Twelve years of "case-by-case adaptation" reached a place it didn't expect — a protocol open-sourced from Anthropic's office in California, California, rewriting the entire industry's onboarding curve from the platform side, bypassing the government's mandatory path which was originally the main route.

On December 10, 2025, when Shuotao pushed `REVIT_MCP_study` to GitHub [^48], it was exactly 11 years and 7 months since the PCC BIM platform was launched. In between those twelve years, Taiwan's construction industry traversed a long path from hand-drawn blueprints to 3D models, from individual attempts to national standards, from tool upgrades to professional redefinition. **This road is not finished — but how its next segment proceeds is no longer entirely in the hands of the Taiwan government.**

---

**Further Reading**:

- [Taiwan Architecture](/art/台灣建築) — An architectural culture narrative from stone houses to skyscrapers, this article is the sister piece to its engineering digitalization layer
- [Social Housing and Housing Justice](/society/社會住宅與居住正義) — BIM's application in social housing operation and maintenance management is a key plan for the Ministry of the Interior's ABRI in recent years
- [Taiwan Enterprises: TSMC](/economy/台灣企業：台積電) — BIM's application in TSMC factory buildings is the main practical field for construction firms like Dacin and Hutsu
- [Taiwan AI Development](/technology/AI發展) — Anthropic MCP and Revit 2027 built-in MCP are specific cases of AI × Industry
- [Semiconductor Industry](/technology/半導體產業) — Fab plant engineering overall solutions + BIM smart factory construction is the engineering foundation for semiconductor cluster expansion

## Image Sources

This article uses 3 Wikimedia Commons CC-licensed images, all cached in `public/article-images/technology/` to avoid hotlinking to the source server:

- [FreeCAD 1.0 Dark BIM Example](https://commons.wikimedia.org/wiki/File:FreeCAD_1.0_Dark_BIM_Example.png) — Photo: Maxwxyz, 2024-10-07, CC BY 4.0 (hero image: 3D model presentation of open-source BIM tools)
- [Autodesk Revit 2024 Object Demo](https://commons.wikimedia.org/wiki/File:Revit_2024.png) — Photo: DanielDefault, 2024, CC BY-SA 4.0 (inline image: Revit object-oriented modeling screen)
- [Taipei Dome and Hino 300 BEM-5593](https://commons.wikimedia.org/wiki/File:Taipei_Dome_and_Hino_300_BEM-5593_%2850281669428%29.jpg) — Photo: Cheng-en Cheng, 2020-08-16, CC BY-SA 2.0 (inline image: Taipei Dome construction site, 65,000-ton steel structure under construction)

The complete media authorization matrix record is in [`reports/research/2026-05/台灣BIM與營建科技.md`](../../reports/research/2026-05/台灣BIM與營建科技.md) §Media Authorization Matrix Table Three.

## References

[^1]: [Republic of China Executive Yuan Public Construction Commission: Public Engineering Building Information Modeling (BIM) Zone](https://www.pcc.gov.tw/content/index?eid=1345&type=C) — The official BIM promotion platform page of the Public Construction Commission, recording the official policy document of the establishment on May 23, 2014, and the three-phase promotion strategy "Encourage Pilot / Pilot Execution / Promote BIM in Public Engineering Above a Certain Amount Starting from Year 106."

[^2]: [Audit Office Public Policy Online Participation Platform: PCC BIM Promotion Strategy Opinion Collection](https://cy.join.gov.tw/policies/detail/8e95c8d6-ce87-4e05-afce-c46a33eb6f89) — The Audit Office's open discussion page, recording the PCC's promotion principle as "case-by-case adaptation, gradual progress," non-universal mandate; and official statistics of over 60 engineering bidding agencies using BIM and over 120 application projects.

[^3]: [Taiwan BIM Industry Association (TBIMA) Official Website](https://sites.google.com/view/tbima) — The official website of the Ministry of the Interior registered association, recording the historical context of the 2009 gathering origin, 2011 preparation, official establishment on March 10, 2012, and main members coming from the 2008 Autodesk Taiwan original training instructor circle.

[^4]: [Taipei City Government Department of Urban Development: Building Engineering BIM As-Built Model Attribute Data Operation Specifications v2.0](https://udd.gov.taipei/assets/50-10660/Documents/竣工模型屬性資料作業規範v2.0_20181109_new.pdf) — The official specification announced by Taipei City Department of Urban Development on November 9, 2018, referencing the COBie international format and specific requirements for exporting IFC standard data.

[^5]: [BSI Partners with Industry, Government, Academia, and Research to Sign "Taiwan BIM Task Group" Memorandum of Understanding](https://www.bsigroup.com/zh-TW/about-bsi/media-centre/press-release/2018-/october/bsitaiwan-bim-task-group/) — BSI Taiwan's October 3, 2018 MOU signing press release, recording the five signing units (BSI, NTU NTUBIM, Taiwan Construction Research Institute, Taiwan Building and Technology Center, TBIMA) and the guiding role of the Ministry of the Interior's ABRI.

[^6]: [shuotao/REVIT_MCP_study GitHub repository](https://github.com/shuotao/REVIT_MCP_study) — CHIANG SHUOTAO's personal open-source Revit MCP teaching project, created in December 2025, accumulating 73 stars and 85 forks by May 2026, with language distribution of C# 54.2% + JavaScript 18.7% + PowerShell 14.3% etc.

[^7]: [Autodesk Developer Blog: Revit API Agents, MCP, Copilot and Codex](https://blog.autodesk.io/revit-api-agents-mcp-copilot-and-codex/) — Autodesk's official developer blog announcement in April 2026, Revit 2027 built-in MCP server + Autodesk Assistant supporting natural language operation of Revit models.

[^8]: [ONC Lawyers: Adoption of BIM in the Construction Industry and Its Legal Implications](https://www.onc.hk/zh_HK/publication/adoption-of-bim-and-its-legal-complications-for-the-construction-industry) — Article from a Hong Kong law firm, recording the policy contrast of Hong Kong's Development Bureau mandating BIM for engineering projects with a cost estimate exceeding 30 million HKD.

[^9]: [Republic of China Ministry of the Interior Architectural Research and Information Institute: Building Information Modeling BIM Application Promotion Plan](https://www.abri.gov.tw/News_Content_Table.aspx?n=807&s=315634) — ABRI's official plan page, recording the goals and scope of the 4-year medium-term plan in 2015 (Republic of China Year 104) and the second phase plan in 2019 (Year 108).

[^10]: [Ministry of the Interior ABRI: Survey and Promotion Plan Research on the Development Achievements and Applications of Taiwan's Building Information Model (BIM)](https://www.abri.gov.tw/News_Content_Table.aspx?n=807&s=39612) — ABRI commissioned research achievement report, recording the two major goals of the second phase plan "Digital Upgrade of Building Technology" + "Digital Living Environment for Buildings" and the BIM × GIS × IoT digital city integration direction.

[^11]: [New Taipei City Government Public Works Bureau: Building Permit Computer-Aided Review System](https://www.bim.ntpc.gov.tw/) — The official website of the New Taipei City Government's BIM building permit review system, recording the first BIM model building permit in 2014, the cumulative achievement of 20+ completed BIM models, and the "New Taipei City Public Building BIM As-Built Model Information Delivery Criteria."

[^12]: [buildingSMART International: Industry Foundation Classes (IFC)](https://www.buildingsmart.org/standards/bsi-standards/industry-foundation-classes/) — buildingSMART International's official IFC standard page, recording the ISO 16739-1:2024 international standard, Denmark's mandatory public construction use of IFC starting in 2010, and other international adoption situations.

[^13]: [Ministry of the Interior ABRI: Building Information Modeling BIM Application Promotion Plan Achievement Report (Year 112)](https://ws.moi.gov.tw/001/Upload/404/relfile/9489/315634/0cccc6e2-2dc6-496f-a45f-69b60e2811b1.pdf) — ABRI's 2023 (Republic of China Year 112) achievement report, acknowledging the official diagnosis that "most public sector BIM applications belong to the design and construction phases, and operation management still adopts traditional practices."

[^14]: [New Taipei City Government Metro Bureau: Metro Wanda Line BIM Application](https://www.dorts.ntpc.gov.tw/documentary/articleInfo/P9z2zp0nZrDp?page=216) — New Taipei City Metro Bureau's engineering collection records that the Taipei Metro Wanda Line is the "first public engineering to include BIM in the contract," an official record of reducing design interface conflicts.

[^15]: [Flow BIM Service: Smart Office Case Sharing](https://bim.flow.tw/smartoffice-globalshowcase/) — Ruoshui International BIM Consulting Company's case sharing, citing specific data from Taiwan HSR's Miaoli Station BIM application: "saved 20% in design change costs, started two months earlier."

[^16]: [Liberty Times Net: Taoyuan Airport Third Terminal Bid Awarded, Samsung C&T and Ronggong Engineering Team Won with NT$44.5 Billion](https://ec.ltn.com.tw/article/breakingnews/3414669) — Liberty Times news release from March 2021, recording the bid award for Taoyuan Airport T3 main terminal building civil engineering, and the specific details of the team composed of Samsung C&T and Ronggong Engineering.

[^17]: [iThome: Construction Industry Achieves Building Digital Twin with BIM, AECOM Case](https://www.ithome.com.tw/people/137308) — iThome's 2021 in-depth report, interviewing AECOM's Chief Engineer Lin Yao-Cang, recording AECOM's Fengshan Station, Bagua Mountain Tunnel and other BIM full-life-cycle cases, and Taoyuan Airport T3 cross-border collaboration BIM process.

[^18]: [China Engineering Consultants Inc. (CECI): Classic 50 Major Events](https://www.ceci.org.tw/modules/article-content.aspx?s=13&i=226) — CECI's official website 50th anniversary major events, recording the establishment in 1969 and the investment establishment of AECOM Engineering Consulting Co., Ltd. in 2007.

[^19]: [AECOM Engineering Consulting Co., Ltd.: Company Introduction](https://www.104.com.tw/company/d1w3jw0) — AECOM's 104 Job Bank page, recording the official information that nearly 2,000 colleagues have 90% backgrounds in highways, railways, airports, bridges, BIM, ITS, PPP, etc., and the establishment of the BIM Integration Center in 2010.

[^20]: [Sinotech Engineering Consultants Society: Towards Sinotech Engineering's 50th Anniversary](https://50th-anniversary.sinotech.org.tw/about_ltd.html) — Sinotech Engineering Consultants Society's 50th anniversary official website, recording the establishment in 1970, transformation into an NPO in 1994, and the subsequent investment in Sinotech Engineering Consultants Co., Ltd.

[^21]: [Autodesk University: Design and Application of Sinotech Engineering BIM Collaborative Operation Platform](https://www.autodesk.com/autodesk-university/class/zhongxinggongchengBIMxietongzuoyepingtaizhishejiyuyingyong-2020) — Autodesk University's 2020 technical briefing, recording Sinotech Engineering's technical architecture based on the ISO 19650 CDE environment, building BIM issue tracking modules and PMIS seven main modules.

[^22]: [Evergreen Consulting Engineering Co., Ltd. (EGC) Official Website](https://www.egc.com.tw/) — Evergreen's official website, recording the establishment in 1974, over 80 professional personnel, structural design of Taipei 101 and Kaohsiung 85-story T&C Tower, and being listed by CTBUH as one of the top ten tall building structural consultants globally.

[^23]: [NTU BIM Research Center: BIM Development Impacting the Current Building System (Kuo Jung-Chin 2011.12)](https://www.ntubim.net/bim2356027396/bim-201112) — NTU NTUBIM's landmark early academic document, Associate Professor Kuo Jung-Chin's 2011 publication, one of the representative works of Taiwan's BIM academic discourse.

[^24]: [BSI: Adding Momentum to Construction Industry Digitalization, Taiwan BIM Task Group Releases BIM International Standard "ISO 19650 Chinese Version"](https://www.bsigroup.com/zh-TW/about-bsi/media-centre/press-release/2019/20197/iso-19650-tw-standard-launch/) — BSI's 2019 press release, recording the release of the ISO 19650 Chinese version, the supervision of ABRI Director Wang Rong-Jin, and the specific division of labor with NTU NTUBIM's translation assistance.

[^25]: [BIM-API: PyRevit + Dynamo Scripts](https://www.bim-api.com/en/blog/pyrevit-dynamo-scripts/) — BIM-API blog article, recording the industry observation number "In Taiwan, 90% of architects (with BIM design capabilities) use Revit Architecture."

[^26]: [Longting Information Graphisoft Archicad Agent Official Website](https://www.academicd.com/) — Graphisoft Taiwan agent Longting Information's official website, recording ArchiCAD's sales support and training resources in Taiwan, with market positioning as "a BIM software friendlier than Revit."

[^27]: [BIM Explorer: Tekla Structures Usage Experience Sharing](https://tpuaup.blogspot.com/2013/05/tekla-structures.html) — BIM blog article, recording Tekla Structures as the mainstream software for steel structure design in Taiwan, and the industry status of handling complex steel structures (stadiums, bridges, factories).

[^28]: [OITC Information Technology: MicroStation Infrastructure Design](https://www.oitc.com.tw/products-detail/MicroStation/79) — Taiwan's Bentley MicroStation agent's official website, recording MicroStation's application scope in Taiwan's railway, highway, tunnel, bridge, and other infrastructure engineering.

[^29]: [Digital Architecture Academy BIM+ Studio: Dynamo Architecture Basics Course](https://bimstudio.tabc.org.tw/blogs/bim%E7%9F%A5%E8%AD%98%E5%BA%AB/49627) — Taiwan Building and Technology Center BIM+ Studio course introduction, recording the key time point in early 2016 when Autodesk Taiwan invited instructors from the Dynamo R&D team from Singapore to teach in Taiwan.

[^30]: [WeBIM Services: How Dynamo Transforms Revit's World](https://webim.com.tw/en/tech-en/dynamo-application-webim-3/) — WeBIM technical article, recording specific application cases of Dynamo in Taiwan's BIM engineer circles (duct coordinate sorting, clear height judgment, automatic section drawing generation).

[^31]: [Autodesk Navisworks Product Overview](https://www.quickly.com.tw/autodesk/navisworks.php) — Autodesk Taiwan distributor Quickly's official website, recording Navisworks Manage's integrated functions of 3D navigation, clash detection, report export, 4D schedule simulation, and 5D cost estimation.

[^32]: [Airiti Library: BIM-Assisted Metro CSD/SEM Design Automation Development and Application](https://www.airitilibrary.com/Article/Detail/0257554X-202107-202107290004-202107290004-77-85) — Airiti Library academic journal paper, recording Taiwan's metro MEP engineering CSD (Combined Service Drawing) and SEM (Structure / Electric / Mechanic) BIM integration methodology.

[^33]: [CTCI Group - Wikipedia](https://zh.wikipedia.org/zh-tw/%E4%B8%AD%E9%BC%8E%E9%9B%86%E5%9C%98) — Wikipedia's CTCI Group entry, recording the 1979 establishment by CTSS, China Development Industrial Bank, and Central Investment Corporation; 2011 Japanese company Chiyoda Chemical Engineering acquiring the largest shareholder; 7,500 employees (2021); and major overseas EPC cases like Saudi Arabia Amine / Saudi Kayan / SAMAC MMA.

[^34]: [CTCI Group Official Website](https://www.ctci.com/www/ctci2022/page.aspx?L=CH) — CTCI Engineering's official website, recording general contracting engineering business, EPC model, and business scope of branches/offices in 15 countries.

[^35]: [Crossing: From CTCI's Overseas Huge Bad Debt Crisis, Looking at Taiwan's General Contractors' "International Risk Control" Fatal Gap](https://crossing.cw.com.tw/article/19832) — The Crossing's in-depth report, recording the controversial event of major delays and bad debts in CTCI's natural gas treatment plant EPC project in India in 2017.

[^36]: [Hutsu Construction Co., Ltd.: High-Tech Factory Performance](https://www.futsu.com.tw/p_hitech.html) — Hutsu Construction's official website high-tech factory page, recording the official statement "accumulated the largest total floor area of high-tech factory buildings in the country."

[^37]: [Dacin Engineering: BIM Experience](https://www.dacin.com.tw/bim/) — Dacin Engineering's official website BIM experience page, recording the official statement "using BIM as a foundational tool platform for the development, planning, design, and construction-related integration and coordination of architectural projects."

[^38]: [Taiwan Obayashi: Company Profile](https://www.obayashi.com.tw/topic/about/preview/3250113421819124234) — Taiwan Obayashi Construction Co., Ltd.'s official website, recording the 1989 establishment, Obayashi Corporation (builder of Tokyo Skytree) as the headquarters, and "Construction Drawing Management and BIM Application" as main construction management items.

[^39]: [Taipei Dome - Wikipedia](https://zh.wikipedia.org/zh-tw/%E8%87%BA%E5%8C%97%E5%A4%A7%E5%B7%A8%E8%9B%8B) — Wikipedia's Taipei Dome entry, recording engineering specifications of 120,000 square meters total floor area, 65,000 tons total steel structure weight, and being the only dome in the world entirely constructed using circular steel pipes.

[^40]: [United Daily News: Grandpa-Level Workers Hold the Field, Construction Industry Technology Faces Gap](https://udn.com/news/story/124689/9220106) — United Daily News investigative report, recording the reality of construction industry aging where over 40 years old accounts for 77% among 100+ occupational disaster deaths in New Taipei.

[^41]: [Liberty Electronic News: Country-Wide Labor Shortage! Construction Industry 15,000 Migrant Worker Quotas About to Run Out](https://estate.ltn.com.tw/article/21452) — Liberty Electronic News financial report, recording the labor force structural crisis where the Ministry of Labor agreed to open 15,000 migrant worker quotas for the construction industry in 2024-2026, and allocation is about to be completed.

[^42]: [1111 Job Bank: BIM Engineer Job Monthly Salary 50,000+ Search Results](https://www.1111.com.tw/search/job?page=1&col=ab&sort=desc&ks=bim,%E7%B9%AA%E5%9C%96&st=1&sa0=50000*) — 1111 Job Bank BIM engineer job search page, recording 104 positions with monthly salary 50,000+ and new hire salaries of 35,000-45,000 TWD, Taiwan's BIM engineer salary status.

[^43]: [Why is Taiwan's BIM Difficult to Land? Four Stages Reveal Truth and Turning Points](https://engineeringlifetw.com/whynotbim/) — Construction Life Blog's in-depth analysis article, recording Taiwan's BIM promotion cultural resistance: "past government building management based on CAD, industry processes following CAD, BIM models becoming outsourced work, many BIM centers or teams dissolving" specific reality.

[^44]: [Verakey Tuopu Engineering: What is BIM? Complete Analysis of 5 Major BIM Advantages](https://veracityconsultant.com.tw/what-is-bim/) — Verakey BIM Consulting Company's official website, explaining BIM's engineering digital transformation essence of systematizing building information (materials, specifications, vendors, prices, construction sequences, maintenance cycles).

[^45]: [Republic of China Ministry of the Interior Architectural Research and Information Institute: BIM Application Promotion Plan](https://www.abri.gov.tw/News_Content_Table.aspx?n=807&s=39506) — ABRI plan page, recording the self-diagnosis of Taiwan's BIM promotion status: "BIM models become outsourced work, disconnected from actual engineering, many BIM centers or teams dissolve."

[^46]: [Anthropic: Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) — Anthropic's official announcement open-sourcing Model Context Protocol (MCP) on November 25, 2024, describing "Think of MCP like a USB-C port for AI applications" and the accompanying release of Python / TypeScript / C# / Java SDKs.

[^47]: [Wikipedia: Model Context Protocol](https://en.wikipedia.org/wiki/Model_Context_Protocol) — Wikipedia English version MCP entry, recording Anthropic's open-sourcing on November 25, 2024, and Anthropic's donation of MCP to the Agentic AI Foundation (under Linux Foundation) in December 2025, complete timeline.

[^48]: [shuotao GitHub Personal Page](https://github.com/shuotao) — CHIANG SHUOTAO's GitHub personal page, recording location Tokyo, peripheral BIM × MCP × AI open-source experiment series repositories (CAD_MCP_study, NAVISWORK_MCP, IFCSH etc.).

[^49]: [shuotao/CAD_MCP_study GitHub repository](https://github.com/shuotao/CAD_MCP_study) — Shuotao's CAD × MCP open-source teaching project, forming part of the BIM × MCP × AI personal open-source experiment series along with REVIT_MCP_study and NAVISWORK_MCP.

[^50]: [Architosh: Autodesk Revit 2027—Big New AI and Graphics Changes](https://architosh.com/2026/04/autodesk-revit-2027-big-new-ai-and-graphics-changes/) — Architosh architectural software professional media April 2026 report, detailing Autodesk Revit 2027's built-in MCP server + Autodesk Assistant's specific functions and architecture.

[^51]: [AutoCAD - Wikipedia](https://en.wikipedia.org/wiki/AutoCAD) — Wikipedia English version AutoCAD entry, recording the historical timeline of initial release on CP/M and IBM PC platforms in December 1982, Classic Mac OS version in 1992, and Microsoft Windows version in 1993.

[^52]: [Building Information Model - Wikipedia](https://zh.wikipedia.org/zh-tw/%E5%BB%BA%E7%AF%89%E4%BF%A1%E6%81%AF%E6%A8%A1%E5%9E%8B) — Wikipedia Traditional Chinese BIM entry, recording the academic development history of BIM first proposed in 1975, research by Finnish and American scholars in the 1980s, and Autodesk introducing the term "Building Information Modeling" in 2002.

[^53]: [BSI Taiwan: The Commercial Value of Building Information Modelling (BIM)](https://www.bsigroup.com/zh-TW/insights-and-media/insights/blogs/business-value-of-building-information-modelling-bim/) — BSI Taiwan's official blog, recording the observation of structural problems on the owner side: "Owners lack sufficient understanding of BIM applications, often operating with traditional engineering processes, limiting BIM technology effectiveness."
