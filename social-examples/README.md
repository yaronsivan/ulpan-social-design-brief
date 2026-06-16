# Social Examples — real-data renders of the Claude Design templates

These are the **Claude Design** social templates ("Ulpan Social Design System" handoff) filled with **real Aktuali / Magazine data** and rendered at exact canvas sizes. They prove the *templates → real-content* pipeline before building the production engine.

## `renders/` — 10 rendered examples
| File | Template | Size | Real data |
|---|---|---|---|
| 01-read-along-news | Read-along (read) | 1080×1920 | apartment story, B1, the קָפוּא sentence |
| 02-read-along-cliffhanger | Read-along (CTA, cliffhanger) | 1080×1920 | apartment, withhold→site |
| 03-carousel-cover | Carousel cover | 1080×1350 | apartment headline + **real news photo** |
| 04-word-of-day | Word of the Day | 1080×1080 | קָפוּא |
| 05-idiom-reveal | Idiom-reveal (reveal) | 1080×1920 | דָּחַף אֶת הָאַף (chutzpah) |
| 06-expression-of-day | Expression of the Day | 1080×1080 | עָשָׂה שְׁכוּנָה (corrected meaning) |
| 07-slang-quiz | **Slang Quiz** (new) | 1080×1350 | two-option cliffhanger → today's magazine |
| 08-carousel-interior-point | Carousel interior (point) | 1080×1350 | apartment "1 in 5" |
| 09-carousel-interior-idiom | Carousel interior (idiom) | 1080×1350 | chutzpah literal→real |
| 10-carousel-interior-cta | Carousel interior (CTA) | 1080×1350 | follow CTA |

## `templates/` — corrected/rebranded template source (.dc.html)
The Claude Design DCLogic templates, **with two corrections applied** vs the original export:
1. **Typo fix** — `ReadAlongFrame` cliffhanger string was `רוֹצִים לָדַעזת לָמָּה?` (stray ז); now `לָדַעַת`.
2. **Independent branding** — dropped the "ULPAN BAYIT MAGAZINE" school tagline from Magazine footers (product name + handle + aleph mark retained).
3. **New template** — `slang-quiz/SlangQuiz.dc.html` (two-option quiz → answer in today's magazine).

> Apply the same three changes in the **Claude Design project** (the source of truth) so the design system stays consistent there. The full design system (bundle, fonts, `_vendor/`, styles) lives in Claude Design + the downloaded handoff tarball — only the `.dc.html` sources are mirrored here.

## `generate_examples.py`
Builds the static HTML for each render by **extracting every Hebrew string directly from the template files** (no hand-typed niqqud), then filling the layouts with real data (apartment / chutzpah from Aktuali issue #7, real photo URLs). Run from a folder that also has the design system's `styles.css`, `tokens/`, `assets/`, fonts (from Claude Design) to re-render via a browser at the exact canvas sizes.

## Notes / findings
- **Fonts** are the Google equivalents Claude Design flagged (Frank Ruhl Libre / Open Sans / Noto Serif Hebrew); swap the real custom faces at build time.
- **Cover-photo relevance matters**: the apartment story's real Aktuali photo is a satellite map, not buildings — the production engine needs decent per-story image selection.
- **API reality for the quiz**: the static card is fully automatable; a *tappable* IG poll/quiz sticker is app-only (not postable via the Graph API).
