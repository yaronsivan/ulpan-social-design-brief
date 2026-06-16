# Magazine Addendum Brief — for Claude Design

A follow-on to the main brief. The first round designed templates that skew **Aktuali (news)**. This addendum asks for a **distinct Magazine (מגזין הבית) visual treatment** + **magazine-specific templates including issue teasers**. Same brand DNA (aleph mark, `--ub-*` palette, fonts) — different *register*.

## The core ask: Magazine should feel editorial, not newsy
**Aktuali = a daily newspaper** (coral labels, tricolor top-rule, date+desk, tight/timely). **Magazine = an editorial/cultural publication** (slower, warmer, crafted). Make them distinguishable at a glance, while obviously the same family.

**Differentiation levers (keep the brand, shift the register):**
- **Lead accent = teal-deep (`--ub-teal-deep #014550`) + gold**, not Aktuali's coral. Coral becomes a rare highlight in Magazine.
- **Warm surfaces** — `--ub-cream-warm` / `--ub-sand`, more paper/editorial than Aktuali's plainer cream.
- **No tricolor news rule.** Use an editorial masthead + a single teal-deep hairline.
- **Serif-forward + generous whitespace** — bigger Frank Ruhl display, drop-cap/flourish energy; photography & the issue **theme** are the organizing principle.
- **Organized by issue + theme + sections** (גיליון 7 · מַיִם; sections: סִיפּוּר הַשַׁעַר / הַמְּדוֹרִים) — not date + desk.
- **Register pills lead** (slang/colloquial); CEFR dots are secondary in Magazine.
- **Framed cover *reveal*** for issue art (a magazine-on-the-table feel), not a full-bleed photo + scrim.

> An anchor mock of the direction is in `social-examples/renders/13-magazine-issue-teaser.png` — match that *feel*, refine the craft.

## Branding (decided)
Product-brand-forward: front **מגזין הבית**; keep the **aleph mark + palette + fonts**; **no "Ulpan Bayit Magazine" school tagline** in footers (just name + @handle).

## Templates to design (magazine-distinct)
1. **Issue teaser / cover reveal** (4:5 + 9:16) — masthead (גיליון N · month) + theme word (HE huge + EN) + framed cover image + one editorial hook + CTA "קראו את הגיליון". *The "new issue out now" promo.*
2. **"What's inside this issue"** carousel — cover slide (theme) → one slide per section/feature (title + level chip + a line) → CTA. The issue's table of contents → drives to the magazine.
3. **Feature long-read teaser** (4:5 / 9:16) — a single feature's hero: title (HE+EN) + an evocative pull-line + photo + level chip + "read the full feature".
4. **Recipe / "from the kitchen" card** (מהמטבח) — dish title + photo + a few ingredients or steps preview + level + CTA. Procedural, warm.
5. **Games teaser** (משחקים) — "play this issue's games" (Wordle / Memory / Anagram) with a teaser of the puzzle + CTA.
6. **Editor's-note snippet** — a short pull-quote from the editor's note in the editorial voice + issue theme + CTA.
7. *(Already in the system, magazine-native: idiom-reveal, expression-of-day, Slang Quiz.)*

## Shared primitives (keep from round 1)
Cover-text-on-photo+scrim (where photos are used), panel interiors, IG/FB caption shapes, comment-to-DM, CEFR dots + register pills, the aleph footer lockup.

## Data the engine will fill these with (real, from Supabase)
- Issue: `mag_issues` → `theme_he`, `theme_en`, `issue_number`, `cover_image_url`, `editor_note`.
- Articles: `mag_articles` (type: feature / recipe / expressions / dialogue) + `mag_article_levels` (title, title_en, level), `cover_image_url`.
- Games: `mag_issues.games_data`.
Design the templates around these fields (e.g., "what's inside" lists `mag_articles` titles by section).

## After Claude Design returns
Export the handoff; I'll validate each new template by rendering it with **real Water-issue data** (same loop we just ran), flag any issues, and we wire them into the build.
