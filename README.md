# 🇹🇼 Taiwan.md

> **The world's first AI-native open knowledge base about Taiwan.**
> 全世界第一個 AI-native 的台灣開源知識庫。

[🌐 Live Site](https://taiwan.md) · [📖 English](https://taiwan.md/en) · [🕸️ Knowledge Graph](https://taiwan.md/graph) · [🤝 Contribute](https://taiwan.md/contribute)

[![GitHub stars](https://img.shields.io/github/stars/frank890417/taiwan-md?style=social)](https://github.com/frank890417/taiwan-md)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC_BY--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](CONTRIBUTING.md)

---

## Why Taiwan.md?

Taiwan produces **90% of the world's most advanced chips**, yet most people can't name three things about it beyond bubble tea. 

Taiwan.md is an open-source, curated, AI-friendly knowledge base that helps the world — and AI — truly understand Taiwan. Not a Wikipedia clone. Not a tourism guide. A **curated literary exhibition** of what makes Taiwan extraordinary.

**🖊️ Written in Traditional Chinese by default** — the world's oldest writing system still in daily use, and Taiwan is its last major home. [English version available →](https://taiwan.md/en)

---

## ✨ Features

- 📖 **68+ curated articles** across 13 categories  
- 🌐 **Bilingual** — 繁體中文 (SSOT) + English (26+ articles)
- 🤖 **AI-native** — [`llms.txt`](https://taiwan.md/llms.txt), [`robots.txt`](https://taiwan.md/robots.txt), structured Markdown
- 🕸️ **Interactive knowledge graph** with 72+ nodes and D3.js visualization
- 🎭 **Curated, not encyclopedic** — every page answers "why this matters"
- 📐 **Three-layer depth** — 30-sec overview → 5-min read → full article  
- 🎨 **Literary curatorial style** — essays, not bullet points
- 🔍 **SEO optimized** — JSON-LD structured data, Open Graph, RSS feeds
- 💾 **Image caching system** — optimized Wikimedia Commons integration
- 📝 **Contribution forms** — zero-code ways to contribute knowledge
- 🔓 **CC BY-SA 4.0** — free to cite, remix, share

---

## 📊 Stats

| Metric | Count |
|--------|-------|
| 🇹🇼 Chinese articles | 68+ |
| 🇺🇸 English articles | 26+ |
| 📂 Categories | 13 |
| 🏛️ Hub pages | 13 |
| 🕸️ Knowledge graph nodes | 72+ |
| 🖼️ Wikimedia images | 20+ |
| 🟢 Good First Issues | 10+ |

---

## 🗂️ 13 Categories

| | Category | Articles | Highlights |
|---|---------|----------|------------|
| 📜 | [歷史 History](https://taiwan.md/history) | 8+ | 史前→荷西→清治→日治→戒嚴→民主化 |
| 🗺️ | [地理 Geography](https://taiwan.md/geography) | 3+ | 五大山脈、板塊運動、溫泉、颱風 |
| 🎭 | [文化 Culture](https://taiwan.md/culture) | 4+ | 閩南客家原住民外省新住民多元融合 |
| 🧋 | [美食 Food](https://taiwan.md/food) | 6+ | 珍珠奶茶、牛肉麵、夜市、茶文化 |
| 🎨 | [藝術 Art](https://taiwan.md/art) | 3+ | 當代藝術、新媒體藝術、C-LAB |
| 🎵 | [音樂 Music](https://taiwan.md/music) | 3+ | 金曲獎、獨立音樂、大港開唱 |
| 💻 | [科技 Technology](https://taiwan.md/technology) | 4+ | 台積電矽盾、g0v 公民科技、數位民主 |
| 🌿 | [自然 Nature](https://taiwan.md/nature) | 4+ | 特有種、9 座國家公園、生物多樣性 |
| 👤 | [人物 People](https://taiwan.md/people) | 8+ | 李安、張忠謀、鄧麗君、唐鳳... |
| 🏛️ | [社會 Society](https://taiwan.md/society) | 5+ | 民主制度、人權與性別平等 |
| 💰 | [經濟 Economy](https://taiwan.md/economy) | 4+ | 經濟奇蹟、夜市經濟學、半導體產業 |
| 🏙️ | [生活 Lifestyle](https://taiwan.md/lifestyle) | 3+ | 便利商店、健保制度、捷運文化 |
| 🎯 | [政治 Politics](https://taiwan.md/politics) | 2+ | 總統制、立法院、地方自治 |

---

## 🤝 How to Contribute

Four ways, from zero-code to full PR:

| Path | For whom |
|------|----------|
| 🟢 **Fill a form** | Anyone — just write what you know |
| 🤖 **Ask your AI** | Paste our prompt to ChatGPT/Claude/Gemini |
| 📧 **Email us** | Send articles/photos to cheyu.wu@monoame.com |
| 🔴 **Fork & PR** | Developers — edit `knowledge/` directly |

👉 **[taiwan.md/contribute](https://taiwan.md/contribute)**

---

## 🏗️ Architecture

```
knowledge/           ← SSOT (Single Source of Truth)
├── History/         ← 中文文章 + _Hub.md (literary curatorial essays)
├── en/History/      ← English translations
├── ...
scripts/sync.sh      ← One-command sync to src/content/
src/
├── pages/           ← Astro v5 pages with SEO
├── layouts/         ← Glassmorphism nav, responsive design
└── content/         ← Build-time projection from knowledge/
public/
├── images/          ← Optimized Wikimedia Commons cache
└── ...
```

**Tech:** Astro v5 + GitHub Pages + marked.js + D3.js knowledge graph  
**SSOT:** All content lives in `knowledge/`. Website is a projection.  
**SEO:** JSON-LD structured data, Open Graph tags, RSS feeds  

---

## 🌏 International Benchmarks

Taiwan.md draws inspiration from:

| Project | Country | Focus |
|---------|---------|-------|
| [e-Estonia](https://e-estonia.com/) | 🇪🇪 Estonia | Digital society brand |
| [japan-guide.com](https://japan-guide.com) | 🇯🇵 Japan | Comprehensive travel knowledge |
| [About Singapore](https://www.sg101.gov.sg/) | 🇸🇬 Singapore | National education portal |
| [SwissInfo](https://www.swissinfo.ch/) | 🇨🇭 Switzerland | Multilingual public media |

**What makes us different:** Open source + AI-native + community-driven + literary curation (not encyclopedic)

---

## 📜 License

- **Content:** [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) — free to share and adapt
- **Code:** MIT

---

## 🖼️ Image Policy

All images sourced from [Wikimedia Commons](https://commons.wikimedia.org/) with verified CC licenses. Each image includes attribution, license type, and source link. Images are cached and optimized for performance.

---

## 👥 Contributors

<a href="https://github.com/frank890417/taiwan-md/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=frank890417/taiwan-md&max=100&columns=12&anon=1" />
</a>

---

## 💝 Sponsors

Help Taiwan's story reach the world. → [taiwan.md/about#sponsors](https://taiwan.md/about#sponsors)

---

## 🙏 Created by

**[Che-Yu Wu 吳哲宇](https://cheyuwu.com)** — New media artist, founder of [MonoLab](https://monolab.world), and builder of [Muse](https://muse.cheyuwu.com).

> *"If I could build a digital identity for myself, why not for Taiwan?"*

---

*Built with ❤️ in Taiwan. 用愛與驕傲，從台灣出發。*