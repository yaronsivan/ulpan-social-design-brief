# Ulpan Social — Design Brief

A self-contained design package for building **branded social-media templates** for two graded-Hebrew products. **No source code, no secrets** — brand assets, the template spec, real content examples, and live screenshots only.

## The two products (live, public)
- **אקטואלי / Aktuali** — daily graded-Hebrew **news** (6 CEFR levels). → https://aktuali.co.il
- **מגזין הבית / Ulpan Magazine** — bi-weekly graded-Hebrew **magazine** (articles, vocab, audio, games, expressions). → https://magazine.aktuali.co.il

They share **one brand system** (see `brand/`). Both are run by a Hebrew school as top-of-funnel for Hebrew learners (immigrants in Israel + diaspora reconnecting).

## What to design
Branded, reusable **social-media templates** (Instagram + Facebook first) that an automated engine will fill with content. The complete structural requirements — sizes, zones, text limits, badges, layouts per format — are in:

### → `spec/TEMPLATE-SPEC.md` (read this first; §12 is the explicit checklist of artboards to deliver)

**Artboards needed** (full detail in §12):
1. **Read-along video frame** (1080×1920) — RTL Hebrew line (with niqqud, karaoke-highlight-ready) + English gloss beneath; level-dot badge; brand footer; CTA end-card (two variants: full-resolution + cliffhanger).
2. **Idiom-reveal video frame** (1080×1920) — a "literal meaning (muted) → real meaning (bold)" reveal; register-pill badge.
3. **Carousel cover** (1080×1350) — photo full-bleed + dark scrim + Hebrew headline overlay (≤30 chars) + English subhead + badge.
4. **Carousel interior panel** (1080×1350) — solid brand panel + Hebrew line (≤45 chars) + English line + badge; an idiom variant (muted-literal / bold-real two-line split); a CTA slide.
5. **Word-of-day card** (1080×1080) and **Expression-of-the-day card** (1080×1080) — stacked zones (see spec §6).
6. **Badge assets** — 6 CEFR difficulty **dots** (A1 green → C1 red) + register **pills** (Neutral / Colloquial / Slang / Crude). *Dots = difficulty, pills = register.*
7. **Brand lockups** — Aktuali + מגזין הבית wordmarks/handles.

## Hard design rules (from the spec)
- **RTL Hebrew, large, on top; English gloss smaller, beneath.** On-screen Hebrew uses **niqqud** (vowel points) — fonts must render them cleanly.
- **Cover text sits ON the photo** (with a dark gradient scrim for contrast). **All interior text sits on a solid branded panel** (no photo) for legibility.
- Surfaces are **warm cream** (`--ub-cream #F6EEE4`), not plain white.
- Every atom wears exactly one badge (CEFR dot OR register pill).

## Folder guide
```
brand/
  brand-tokens.css   ← full colour palette + font notes (the design tokens)
  logos/             ← aleph icon, full logo, shalom mark, magazine favicon/icons, Yaron's photo (persona)
  letters/           ← the Hebrew-letter icon set (brand motif)
spec/
  TEMPLATE-SPEC.md   ← THE spec: sizes, layouts, text limits, badges, formats, design checklist (§12)
examples/
  content-prototypes.md      ← real generated posts (news read-along, carousel, captions, word-of-day)
  cliffhanger-prototype.md   ← the cliffhanger / curiosity-gap format on a real story
screenshots/        ← real screenshots of the live products to match the look & feel
```

## Brand palette (quick reference)
| Token | Hex | Role |
|---|---|---|
| `--ub-teal` | `#00B0C6` | primary (aleph) |
| `--ub-gold` | `#FFC60B` | secondary (bet) |
| `--ub-coral` | `#F0586D` | accent (gimmel) |
| `--ub-ink` | `#000000` | text / logo |
| `--ub-cream` | `#F6EEE4` | page surface (warm) |
| `--ub-teal-deep` | `#014550` | highlights |
| `--ub-coral-dark` | `#E36A46` | deeper accent |

Fonts: **Frank Ruhl Ulpan** (serif display/headlines), **Open Sans Hebrew** (body/UI), **Droid Serif Ulpan** (secondary). Google equivalents: Frank Ruhl Libre, Open Sans, Noto/Droid Serif.

## Persona note
The channel voice is the school's founder, **Yaron** (photo in `brand/logos/yaron.jpg`) — a real recurring face + his own cloned voice for narration. Templates should feel like *a person's* channel, warm and human, not a faceless brand.
