# Magazine templates — validation findings (2026-06-16)

Validated the 6 new Claude Design magazine templates (issue-teaser, whats-inside,
feature-teaser, from-the-kitchen, games-teaser, editors-note) by rendering their
ACTUAL DCLogic runtime with real Water-issue data (mag_issues / mag_articles).
Renders: `renders/14`–`19`. Editorial register confirmed — clearly distinct from Aktuali. ✅

## Issues to fix in Claude Design
1. **box-sizing reset missing.** Templates assume `*{box-sizing:border-box}`, but it's
   not in `styles.css`. Without it, padded root divs compute to width 1080+padding
   (content-box → ~1240px) and overflow. Fix: add `*{ box-sizing:border-box }` to a
   token/reset file imported by `styles.css` so every consumer is correct.
2. **whats-inside footer: literal `·`.** The section footer markup is
   `{{ themeEn }} · {{ issueShort }}` — a JS-style escape sitting in raw HTML
   template text, which the runtime does NOT decode. Renders as `Water · Issue 07`.
   Fix: use a real `·` (or `&#183;`) in the template HTML.
3. **issue-teaser overflows at 4:5.** Big theme (152px) + full-size framed cover (560px)
   + hook + CTA exceed 1350px, clipping the CTA/footer. Use the `9:16` format (1920px has
   headroom), or shrink the cover/theme for the 4:5 variant.

## Good
- feature-teaser, from-the-kitchen, games-teaser, editors-note: render perfectly with
  real data (real Kinneret photo+title; real Green Shakshuka + ingredients; Yaron's real
  photo in the editor's note). The `format` 4:5/9:16 toggle works.
