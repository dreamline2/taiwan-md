# Description

This PR resolves the issue where footnotes were failing to render in translated articles (KO, EN, JA) and standardizes the content fortification for the "Taiwan Campus Folk Song Movement" article across languages.

## Key Changes

### 1. Footnote Rendering System

- Implemented a manual footnote parser in `src/pages/[lang]/[category]/[slug].astro` to support GFM-style footnotes (`[^1]`) within the custom `marked` rendering pipeline.
- Ported premium footnote CSS styles from the default language template to ensure consistent visual excellence (blue superscripts, back-reference arrows, and mobile-optimized touch targets).

### 2. Content Fortification (Campus Folk Song Movement)

- Added 9 verifiable footnotes to the "Taiwan Campus Folk Song Movement" article, covering key historical figures (Kimbo, Luo Dayou), events (Tamkang Incident), and songs (Descendants of the Dragon).
- Synced these improvements across Traditional Chinese and Korean versions.

### 3. Slug & Translation Standardization

- Standardized article filenames to a canonical English slug (`taiwan-campus-folk-song-movement.md`) across `src/content/` and `knowledge/` directories.
- Updated `knowledge/_translations.json` to reflect the new mapping, resolving 404 errors and broken cross-language links.

## Verification

- [x] Verified footnotes are clickable and jump to references in KO and ZH-TW.
- [x] Verified back-jump (↩) functionality.
- [x] Verified that 404s are resolved after slug synchronization.
- [x] Visual consistency check against reference articles (e.g., Cheng Li-wun).

## User Review Required

> [!IMPORTANT]
> The footnote logic is implemented manually in the Astro templates to avoid adding new dependencies while maintaining the project's custom `marked` configuration.
