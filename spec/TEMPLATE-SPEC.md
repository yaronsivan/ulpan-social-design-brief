# Social Engine — Consolidated Template Spec

- **Date:** 2026-06-15
- **Status:** Locked (from real-content prototypes on Aktuali #7 + Magazine)
- **Parent:** `2026-06-15-autonomous-social-growth-engine-design.md`
- **Purpose:** The precise structural blueprint for every social atom — exact counts, layouts, badges, gates — so (a) Yaron can design branded visual templates against it and (b) the renderer can fill them deterministically.

---

## 0. Source of these numbers
Derived from agent pipelines run on real content: a B1 Aktuali news story ("free apartment") in two ordering variants + cliffhanger mode, and a Magazine "chutzpah" expressions card. Full prototype outputs: `../2026-06-15-social-engine-content-prototypes.md` and `../2026-06-15-social-engine-cliffhanger-prototype.md`.

---

## 1. Shared primitives (every atom)
- **Hebrew is RTL, large, on top; English gloss smaller, beneath.** On-screen Hebrew is **dotted (niqqud)**; the TTS narration feed is **undotted** (per voice test 2026-06-15).
- **Cover text sits ON the photo** (+ dark gradient scrim for contrast). **All interior text sits ON a solid branded panel** (no photo) so dotted Hebrew stays legible.
- **Badge slot** (top corner) — CEFR dot OR register pill (see §2).
- **Brand lockup/footer** (Aktuali or מגזין הבית wordmark + handle).
- **Imagery:** real/original photos preferred; minimize AI imagery.
- **AI disclosure:** platform AI-voice toggle enabled once (cloned voice); no per-post disclaimer.

**Canvas sizes**
| Atom | Size |
|---|---|
| Read-along / idiom-reveal video | 1080×1920 (9:16) |
| Carousel | 1080×1350 (4:5) |
| Word-of-day / expression micro | 1080×1080 (1:1) |

---

## 2. Badge & register system
- **CEFR dots** — difficulty, for graded (news) content. 6-step color gradient: A0/A1 green → A2 → B1 → B2 → C1 red. Shape = **dot**.
- **Register pills** — for non-CEFR feature/slang content. Values: `נֵיטְרָלִי/Neutral`, `דִּבּוּרִי/Colloquial`, `סְלֶנְג/Slang`, `גַּס/Crude (gated)`. Shape = **pill** (deliberately different from dots).
- **Rule:** *dots = difficulty, pills = register.* Every atom wears exactly one.

---

## 3. Read-along video (news hero) — three modes
Karaoke word-highlight synced to ElevenLabs word-level timestamps; HE line large + EN gloss beneath; level-aware density (**EN every screen A0–B1; selective B2–C1**). Hero word mid-video; level dot badge.

| Mode | HE words | Duration | Screens | Payoff | Use |
|---|---|---|---|---|---|
| **Full-resolution** | 55–65 | ~30s (32–35s w/ holds) | 9 (1 sentence/screen) | Resolved on-screen; link/follow final screen | Default; value/saves |
| **Cliffhanger** | ~40 | ~22–25s | ~6 | **Withheld** → CTA to site; hero word NOT shown | Conversion beat |
| **Lede-teaser** | ~24 | ~13–15s | 3 (2 lede + 1 CTA) | Read opening only, cut before explanation → site | Conversion beat |

---

## 4. Idiom-reveal video (expressions hero)
Signature format. Per idiom: **literal screen (greyed "bait")** → **reveal screen (real meaning, bold/accent)** → **example screen**. ~3 idioms → ~11 screens, **30–40s**, ~55–60 HE words. Cover + follow-beat bookend. Register pill badge.

---

## 5. Carousel
Cover ON photo+scrim; interior ON branded panel; EN paired on every slide; badge on every slide.

| Family | Slides | Structure |
|---|---|---|
| **News** | 7 | 1 cover + 4–5 point + 1 vocab + 1 CTA |
| **Expressions** | variable (5–8) | 1 cover + **N idiom (3–5)** + 1 recap + 1 CTA |

- **Cover headline ≤30 HE chars.**
- **Interior line ≤45 HE chars.**
- Idiom slide layout: **literal (muted, top) / real meaning (bold, bottom)**.
- Vocab/idiom/recap slides are always panel, never photo.

---

## 6. Word-of-day / Expression-of-the-day micro (1080²)
| News word-of-day | Expression-of-day |
|---|---|
| label → word (XL, ≤6 chars) → translit + EN gloss → HE example (≤50 chars) → EN example | register pill → idiom (XL) → translit → **literal (muted)** → **real (bold)** → mini-example footer |

---

## 7. Captions
| | Instagram | Facebook |
|---|---|---|
| Length | 400–470 chars (cliffhanger ≤~700 incl. hashtags) | 400–550 chars |
| Hashtags | **12** (HE + EN + niche e.g. olim/nadlan + brand) | **≤3** |
| CTA | comment-to-DM (**easy-to-type keyword**) + bio-link mention | direct inline link / Follow (no comment-bait) |
| Tone | punchy, emoji, scroll-stopper | English-forward, narrative, older diaspora |

**comment-to-DM keyword rule:** trivially typeable (simple undotted Hebrew or English, e.g. `דירה`, `CHUTZPAH`). Never niqqud-dependent or rare.

---

## 8. Pipeline / production rules
- **Ordering = HYBRID:** narration is the semantic spine (angle + hero word + thesis); each atom gets ONE native-format liberty; lead with the punchiest stat/curiosity hook.
- **Level handling:**
  - *News (CEFR-graded):* multi-level fan-out — **spread different levels across different stories** in the feed, **weighted A2–B2** (edges A0/C1 represented but thinner); occasional deliberate "same story, two levels" contrast piece. Algorithm self-personalizes by level.
  - *Features (non-graded):* **single conservative render** + register pill; no fan-out.
- **Cliffhanger mix:** ~**25–35%** of posts cliffhanger; rest full-resolution. Cliffhanger only when ONE genuine surprising "why" exists.

---

## 9. Content-appropriateness gate (mandatory)
Score every item before composition on **(a) literal-image safety** (would the literal translation on-image trip a profanity/sexual/violence filter?) and **(b) register tier**, checking BOTH literal and real meaning.
- Neutral / colloquial / slang → auto-publish.
- Crude → soften / treatment-only.
- **Vulgar or literal-unsafe → DROP** from feed (never soften; optional age-gated Stories-only lane). Canonical drop: שם זין.

## 10. Curiosity-hook generator (cliffhanger fuel)
5 reusable patterns: **Paradox**, **Number That Shouldn't Be**, **Reversal**, **Withheld Mechanism**, **Hidden Stakes** (full templates + examples in the cliffhanger prototype doc).
**Honesty guardrail:** the withheld payoff must be a single, real, article-grounded fact. If the engine can't name the specific withheld fact from the article body → reject the hook, fall back to full-resolution.

## 11. Native-QA / quality rules
- **Framing precision:** describe content for what it *is* (e.g., expressions *about/exemplifying* chutzpah — NOT "synonyms for חוצפה"). Loose/synonym framing = defect.
- **Inherited accuracy:** idiom/vocab meanings are only as good as the source → native-QA pass required (e.g., עשה שכונה = *did a sloppy/low-quality job*, not "made a scene").
- **Dotting standardization** (e.g., יִזְמִים vs יַזָּמִים — pick one), **plene (כתיב מלא)** spelling, **years as digits in brackets**.

---

## 12. ✅ Design checklist — what the branded templates must provide
Visual templates Yaron designs need these slots/zones:

1. **Read-along video frame (9:16):** HE line zone (RTL, niqqud, karaoke-highlight-ready) + EN gloss zone beneath + level-dot badge corner + brand footer + final CTA card layout (full mode) and a separate "withhold + link" CTA card (cliffhanger).
2. **Idiom-reveal video frame (9:16):** literal-bait state (muted) + reveal state (accent) + example state + register-pill badge.
3. **Carousel cover (4:5):** photo full-bleed + dark scrim + headline overlay (≤30 HE chars) + EN subhead + badge.
4. **Carousel interior panel (4:5):** solid brand panel + HE line (≤45 chars) + EN line + badge; idiom variant with muted-literal/bold-real two-line split; CTA slide variant.
5. **Word-of-day card (1:1)** and **Expression-of-day card (1:1):** the zone stacks in §6.
6. **Badge assets:** 6 CEFR dots (green→red) + register pills (4).
7. **Brand lockups:** Aktuali + מגזין הבית wordmarks/handles.

---

## 13. Open / deferred
- Validate the cliffhanger on a Magazine intrigue feature (optional polish).
- Patch the עשה שכונה definition + dotting standard in the Magazine source.
- Recipe/how-to genre excluded for now (low source-trust).
