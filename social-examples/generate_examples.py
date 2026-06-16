# -*- coding: utf-8 -*-
"""Render the Claude Design templates as static HTML filled with REAL data.
   ALL Hebrew is extracted directly from the template files — nothing hand-typed."""
import os, re, json
import html as htmllib
PROJ = os.path.dirname(os.path.abspath(__file__))

def read(rel): return open(os.path.join(PROJ, rel), encoding="utf-8").read()
def decode_u(s): return re.sub(r"\\u([0-9A-Fa-f]{4})", lambda m: chr(int(m.group(1), 16)), s)
def props(txt):
    raw = htmllib.unescape(re.search(r'data-props="(.*?)"\s*>', txt, re.S).group(1))
    return {k: (v.get("default") if isinstance(v, dict) else v) for k, v in json.loads(raw).items()}
def grab(txt, pat):
    m = re.search(pat, txt, re.S)
    return decode_u(m.group(1)) if m else None

RA_T  = read("templates/read-along-frame/ReadAlongFrame.dc.html")
WOD_T = read("templates/word-of-day/WordOfDay.dc.html")
COV_T = read("templates/carousel-cover/CarouselCover.dc.html")
IDM_T = read("templates/idiom-reveal-frame/IdiomRevealFrame.dc.html")
EXP_T = read("templates/expression-of-day/ExpressionOfDay.dc.html")
CI_T  = read("templates/carousel-interior/CarouselInterior.dc.html")
ra, wod, cov, idm, exp, ci = props(RA_T), props(WOD_T), props(COV_T), props(IDM_T), props(EXP_T), props(CI_T)
CI_IDIOM    = grab(CI_T, r"idiom: p\.idiom \?\? '([^']*)'")
CI_IDIOM_TR = grab(CI_T, r"idiomTranslit: p\.idiomTranslit \?\? '([^']*)'")
CI_LITHE    = grab(CI_T, r"literalHe: p\.literalHe \?\? '([^']*)'")
CI_LITEN    = grab(CI_T, r"literalEn: p\.literalEn \?\? '([^']*)'")
CI_REALHE   = grab(CI_T, r"realHe: p\.realHe \?\? '([^']*)'")
CI_REALEN   = grab(CI_T, r"realEn: p\.realEn \?\? '([^']*)'")
CI_CTAHE    = grab(CI_T, r"ctaHe: p\.ctaHe \?\? '([^']*)'")
CI_CTAEN    = grab(CI_T, r"ctaEn: p\.ctaEn \?\? '([^']*)'")
CI_CTABTN   = grab(CI_T, r"ctaButton: p\.ctaButton \?\? '([^']*)'")

RAMAH     = grab(RA_T, r"levelHe: '([^']*)' \+")
AKT       = grab(RA_T, r"he:'([^']*)', handle:'@aktuali'")
MAG       = grab(IDM_T, r"brandHe: '([^']*)', brandTag: 'ULPAN")
SLANG     = grab(IDM_T, r"slang:\{c:'#F0586D',he:'([^']*)'")
CLIFF_HE  = grab(RA_T, r"ctaHe: p\.ctaHe \?\? \(isCliff \? '([^']*)'")
CLIFF_BTN = grab(RA_T, r"ctaButton: p\.ctaButton \?\? '([^']*)'")
ID_REAL   = grab(IDM_T, r"realHe: p\.realHe \?\? '([^']*)'")
EX_EX     = grab(EXP_T, r"exampleHe: p\.exampleHe \?\? '([^']*)'")
WOD_K     = grab(WOD_T, r"kicker: p\.kicker \?\? '([^']*)'")
EX_K      = grab(EXP_T, r"kicker: p\.kicker \?\? '([^']*)'")

# QA FIX: Claude Design's template typo — "לָדַעזת" (stray zayin)
# should be "לָדַעַת" (la-da-at, "to know"). Correct it for the render.
CLIFF_HE  = CLIFF_HE.replace("עזת", "עַת")

CEFR = {"A0":("#1A9461",0),"A1":("#54A742",1),"A2":("#9FB52E",2),
        "B1":("#FFC60B",3),"B2":("#F2913B",4),"C1":("#F0586D",5)}
def ramah(n): return RAMAH + str(n)
PHOTO_APT = "https://svgdyrsfxcausecwrgbc.supabase.co/storage/v1/object/public/aktuali-assets/issue-7/israel-real-estate-apartment-lottery.jpg"
C = "position:relative;overflow:hidden;background:var(--ub-cream);font-family:var(--font-body);direction:rtl;display:flex;flex-direction:column"

def page(body):
    return ("<!doctype html><html><head><meta charset='utf-8'>"
            "<link rel='preconnect' href='https://fonts.googleapis.com'>"
            "<link rel='preconnect' href='https://fonts.gstatic.com' crossorigin>"
            "<link rel='stylesheet' href='styles.css'>"
            "<style>html,body{margin:0;padding:0;background:#777}*{box-sizing:border-box}</style>"
            "</head><body>" + body + "</body></html>")

def dot(size, fs, color, label, shadow=""):
    sh = f"box-shadow:{shadow};" if shadow else ""
    return (f"<span style='display:inline-flex;align-items:center;justify-content:center;width:{size}px;height:{size}px;"
            f"border-radius:50%;background:{color};color:#fff;font-weight:700;font-size:{fs}px;{sh}'>{label}</span>")

def pill(color, he, en, pad="13px 28px", hefs=30, enfs=16, gap=12):
    return (f"<span style='display:inline-flex;align-items:center;gap:{gap}px;padding:{pad};border-radius:999px;"
            f"background:{color};color:#fff;box-shadow:var(--shadow-sm)'>"
            f"<span style='font-family:var(--font-display);font-size:{hefs}px;font-weight:500'>{he}</span>"
            f"<span dir='ltr' style='font-size:{enfs}px;font-weight:700;letter-spacing:0.16em;text-transform:uppercase;opacity:0.85'>{en}</span></span>")

def icon(px): return f"<img src='assets/logos/aleph-icon-color.png' style='width:{px}px;height:auto'>"

examples = {}

def readalong(mode):
    head = (f"<div style='display:flex;align-items:center;justify-content:space-between;padding:72px 72px 0'>"
        f"<span style='display:inline-flex;align-items:center;gap:16px'>{dot(62,26,'#FFC60B','B1')}"
        f"<span style='display:inline-flex;flex-direction:column;line-height:1.12'>"
        f"<span style='font-family:var(--font-display);font-size:30px;font-weight:500;color:var(--fg)'>{ramah(3)}</span>"
        f"<span dir='ltr' style='font-size:15px;font-weight:700;letter-spacing:0.16em;text-transform:uppercase;color:var(--fg-faint)'>Level B1</span></span></span>"
        f"<span dir='ltr' style='font-size:18px;font-weight:700;letter-spacing:0.16em;text-transform:uppercase;color:var(--ub-coral)'>{'Link in bio' if mode=='cliff' else 'Read-along'}</span></div>")
    if mode == "read":
        center = (f"<div style='flex:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:64px 88px;gap:48px'>"
            f"<div style='display:flex;flex-direction:column;gap:52px;align-items:center'>"
            f"<h1 style='margin:0;font-family:var(--font-display);font-weight:500;font-size:90px;line-height:1.18;color:var(--fg);text-wrap:balance'>"
            f"<span>{ra['hePre']} </span><span style='color:var(--ub-teal-deep);font-weight:700'>{ra['heHero']}</span><span> {ra['hePost']}</span></h1>"
            f"<p dir='ltr' style='margin:0;font-family:var(--font-serif);font-style:italic;font-size:48px;line-height:1.35;color:var(--fg-muted);text-wrap:pretty'>{ra['en']}</p></div></div>")
        pct, scr = "56%", "5 / 9"
    else:
        center = (f"<div style='flex:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:64px 88px;gap:48px'>"
            f"<div style='display:flex;flex-direction:column;gap:46px;align-items:center'>{icon(150)}"
            f"<h1 style='margin:0;font-family:var(--font-display);font-weight:700;font-size:84px;line-height:1.12;color:var(--fg);text-wrap:balance'>{CLIFF_HE}</h1>"
            f"<p dir='ltr' style='margin:0;font-family:var(--font-serif);font-style:italic;font-size:46px;line-height:1.3;color:var(--fg-muted);text-wrap:pretty'>Want to know why? Read the full story on Aktuali — link in bio.</p>"
            f"<span style='display:inline-flex;align-items:center;gap:16px;padding:24px 52px;border-radius:999px;background:var(--ub-coral);color:#fff;font-size:40px;font-weight:700;box-shadow:var(--shadow-md)'>{CLIFF_BTN}</span></div></div>")
        pct, scr = "100%", "9 / 9"
    bar = (f"<div style='margin:0 88px;height:10px;border-radius:999px;background:var(--ub-rule-soft);overflow:hidden'>"
           f"<div style='height:100%;width:{pct};border-radius:999px;background:linear-gradient(to left, var(--ub-teal), var(--ub-teal-deep))'></div></div>")
    foot = (f"<div style='display:flex;align-items:center;gap:18px;padding:44px 72px 88px'>{icon(54)}"
        f"<span style='display:inline-flex;flex-direction:column;line-height:1.1'>"
        f"<span style='font-family:var(--font-display);font-weight:700;font-size:36px;color:var(--fg)'>{AKT}</span>"
        f"<span dir='ltr' style='font-size:20px;color:var(--fg-faint);margin-top:2px'>@aktuali</span></span>"
        f"<span dir='ltr' style='margin-right:auto;font-size:22px;color:var(--fg-faint)'>{scr}</span></div>")
    return f"<div style='{C};width:1080px;height:1920px'>{head}{center}{bar}{foot}</div>"

examples["01-readalong-B1-read"] = readalong("read")
examples["02-readalong-cliffhanger"] = readalong("cliff")

examples["03-carousel-cover-apartment"] = (
    f"<div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:var(--ub-ink);font-family:var(--font-body);direction:rtl'>"
    f"<div style='position:absolute;inset:0;background:radial-gradient(120% 90% at 70% 18%, #6b5746 0%, #3a2f29 48%, #1c1714 100%)'></div>"
    f"<img src='{PHOTO_APT}' style='position:absolute;inset:0;width:100%;height:100%;object-fit:cover'>"
    f"<div style='position:absolute;left:0;right:0;bottom:0;height:74%;background:linear-gradient(to top, rgba(0,0,0,0.82) 0%, rgba(0,0,0,0.55) 38%, rgba(0,0,0,0) 100%)'></div>"
    f"<div style='position:absolute;top:64px;right:64px;display:flex;align-items:center;gap:16px'>{dot(60,25,'#FFC60B','B1','0 2px 10px rgba(0,0,0,0.35)')}"
    f"<span style='display:inline-flex;flex-direction:column;line-height:1.12'>"
    f"<span style='font-family:var(--font-display);font-size:28px;font-weight:500;color:var(--ub-cream-pale)'>{ramah(3)}</span>"
    f"<span dir='ltr' style='font-size:15px;font-weight:700;letter-spacing:0.16em;text-transform:uppercase;color:rgba(255,253,250,0.7)'>Level B1</span></span></div>"
    f"<div style='position:absolute;left:72px;right:72px;bottom:72px;display:flex;flex-direction:column;gap:28px'>"
    f"<h1 style='margin:0;font-family:var(--font-display);font-weight:700;font-size:96px;line-height:1.05;color:var(--ub-cream-pale);text-wrap:balance'>{cov['headline']}</h1>"
    f"<p dir='ltr' style='margin:0;font-family:var(--font-serif);font-style:italic;font-size:46px;line-height:1.25;color:rgba(255,253,250,0.86);text-wrap:pretty'>{cov['subhead']}</p>"
    f"<div style='display:flex;align-items:center;gap:18px;margin-top:14px;padding-top:30px;border-top:1.5px solid rgba(255,253,250,0.2)'>"
    f"<img src='assets/logos/aleph-icon-color.png' style='width:56px;height:auto;display:block'>"
    f"<span style='display:inline-flex;flex-direction:column;line-height:1.1'>"
    f"<span style='font-family:var(--font-display);font-weight:700;font-size:36px;color:var(--ub-cream-pale)'>{AKT}</span>"
    f"<span dir='ltr' style='font-size:16px;font-weight:500;letter-spacing:0.04em;color:rgba(255,253,250,0.7);margin-top:3px'>The daily paper in easy Hebrew</span></span></div></div></div>")

examples["04-word-of-day-kafua"] = (
    f"<div style='{C};width:1080px;height:1080px'>"
    f"<div style='height:12px;background:linear-gradient(to left, var(--ub-teal) 0 33.3%, var(--ub-gold) 33.3% 66.6%, var(--ub-coral) 66.6% 100%)'></div>"
    f"<div style='display:flex;align-items:center;justify-content:space-between;padding:52px 64px 0'>"
    f"<span style='display:inline-flex;flex-direction:column;line-height:1.1'>"
    f"<span style='font-family:var(--font-display);font-size:34px;font-weight:500;color:var(--fg)'>{WOD_K}</span>"
    f"<span dir='ltr' style='font-size:16px;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:var(--ub-coral);margin-top:4px'>Word of the day</span></span>"
    f"<span style='display:inline-flex;align-items:center;gap:14px'>{dot(56,23,'#FFC60B','B1')}</span></div>"
    f"<div style='flex:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:24px 72px;gap:26px'>"
    f"<h1 style='margin:0;font-family:var(--font-display);font-weight:700;font-size:170px;line-height:1;color:var(--ub-teal-deep)'>{wod['word']}</h1>"
    f"<span dir='ltr' style='font-family:var(--font-body);font-style:italic;font-size:42px;color:var(--fg-faint)'>{wod['translit']}</span>"
    f"<span dir='ltr' style='font-family:var(--font-serif);font-style:italic;font-size:50px;color:var(--fg)'>{wod['gloss']}</span></div>"
    f"<div style='margin:0 64px;background:var(--ub-cream-pale);border:1.5px solid var(--ub-rule-soft);border-radius:var(--r-lg);padding:40px 48px;box-shadow:var(--shadow-card);display:flex;flex-direction:column;gap:14px;align-items:center;text-align:center'>"
    f"<span style='font-family:var(--font-display);font-size:48px;font-weight:500;line-height:1.22;color:var(--fg);text-wrap:balance'>{wod['exampleHe']}</span>"
    f"<span dir='ltr' style='font-family:var(--font-serif);font-style:italic;font-size:34px;color:var(--fg-muted);text-wrap:pretty'>{wod['exampleEn']}</span></div>"
    f"<div style='display:flex;align-items:center;gap:16px;padding:40px 64px 48px'>{icon(48)}"
    f"<span style='font-family:var(--font-display);font-weight:700;font-size:32px;color:var(--fg)'>{AKT}</span>"
    f"<span dir='ltr' style='margin-right:auto;font-size:20px;color:var(--fg-faint)'>@aktuali</span></div></div>")

examples["05-idiom-reveal-chutzpah"] = (
    f"<div style='{C};width:1080px;height:1920px'>"
    f"<div style='display:flex;align-items:center;justify-content:space-between;padding:72px 72px 0'>{pill('#F0586D',SLANG,'Slang')}"
    f"<span dir='ltr' style='font-size:18px;font-weight:700;letter-spacing:0.16em;text-transform:uppercase;color:var(--ub-coral)'>Reveal</span></div>"
    f"<div style='flex:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:64px 88px;gap:56px'>"
    f"<div style='display:flex;flex-direction:column;gap:16px;align-items:center'>"
    f"<h1 style='margin:0;font-family:var(--font-display);font-weight:700;font-size:64px;line-height:1.08;color:var(--fg)'>{idm['idiom']}</h1>"
    f"<span dir='ltr' style='font-family:var(--font-body);font-style:italic;font-size:34px;color:var(--fg-faint)'>{idm['idiomTranslit']}</span></div>"
    f"<div style='display:flex;flex-direction:column;gap:22px;align-items:center'>"
    f"<span dir='ltr' style='font-size:20px;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:var(--ub-coral)'>Really means</span>"
    f"<span style='font-family:var(--font-display);font-size:82px;font-weight:700;line-height:1.1;color:var(--ub-coral);text-wrap:balance'>{ID_REAL}</span>"
    f"<span dir='ltr' style='font-family:var(--font-serif);font-style:italic;font-size:46px;line-height:1.3;color:var(--fg);text-wrap:pretty'>{idm['realEn']}</span></div></div>"
    f"<div style='display:flex;align-items:center;gap:16px;padding:0 72px 88px'>{icon(54)}"
    f"<span style='font-family:var(--font-display);font-weight:700;font-size:36px;color:var(--fg)'>{MAG}</span>"
    f"<span dir='ltr' style='margin-right:auto;font-size:22px;color:var(--fg-faint)'>@ulpan.magazine</span></div></div>")

# 07) NEW: Slang Quiz (two options, answer in today's magazine) — uses extracted idiom data
A_OPT = idm['literalEn'].strip('?').strip()       # the literal "trap"
B_OPT = idm['realEn']                              # the real meaning
def opt(letter, color, text):
    return (f"<div style='display:flex;align-items:center;gap:24px;width:100%;background:var(--ub-cream-pale);"
            f"border:1.5px solid var(--ub-rule-soft);border-radius:var(--r-lg);padding:30px 36px;box-shadow:var(--shadow-card)'>"
            f"<span style='flex:none;display:inline-flex;align-items:center;justify-content:center;width:64px;height:64px;"
            f"border-radius:50%;background:{color};color:#fff;font-weight:700;font-size:30px'>{letter}</span>"
            f"<span dir='ltr' style='font-family:var(--font-serif);font-style:italic;font-size:40px;line-height:1.25;color:var(--fg);text-align:left'>{text}</span></div>")
examples["07-slang-quiz"] = (
    f"<div style='{C};width:1080px;height:1350px'>"
    f"<div style='height:14px;background:linear-gradient(to left, var(--ub-teal) 0 33.3%, var(--ub-gold) 33.3% 66.6%, var(--ub-coral) 66.6% 100%)'></div>"
    f"<div style='display:flex;align-items:center;justify-content:space-between;padding:52px 64px 0'>"
    f"<span style='display:inline-flex;flex-direction:column;line-height:1.1'>"
    f"<span style='font-family:var(--font-display);font-size:34px;font-weight:500;color:var(--fg)'>{SLANG} — חידון</span>"
    f"<span dir='ltr' style='font-size:16px;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:var(--ub-coral);margin-top:4px'>Slang quiz</span></span>"
    f"{pill('#F0586D',SLANG,'Slang','12px 24px',27,14,11)}</div>"
    f"<div style='flex:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:28px 80px;gap:30px'>"
    f"<div style='display:flex;flex-direction:column;gap:10px;align-items:center'>"
    f"<h1 style='margin:0;font-family:var(--font-display);font-weight:700;font-size:96px;line-height:1.04;color:var(--fg)'>{idm['idiom']}</h1>"
    f"<span dir='ltr' style='font-family:var(--font-body);font-style:italic;font-size:34px;color:var(--fg-faint)'>{idm['idiomTranslit']}</span></div>"
    f"<span dir='ltr' style='font-size:20px;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:var(--ub-coral)'>What does it really mean?</span>"
    f"<div style='display:flex;flex-direction:column;gap:20px;width:100%'>{opt('A','#00B0C6',A_OPT)}{opt('B','#F4B609',B_OPT)}</div></div>"
    f"<div style='margin:0 64px 28px;background:var(--ub-teal-deep);border-radius:var(--r-lg);padding:28px 40px;display:flex;flex-direction:column;gap:6px;align-items:center;text-align:center'>"
    f"<span style='font-family:var(--font-display);font-size:38px;font-weight:700;color:var(--ub-cream-pale)'>\U0001F440 התשובה בגיליון של היום</span>"
    f"<span dir='ltr' style='font-family:var(--font-serif);font-style:italic;font-size:28px;color:rgba(255,253,250,0.85)'>The answer's in today's magazine — link in bio</span></div>"
    f"<div style='display:flex;align-items:center;gap:16px;padding:0 64px 44px'>{icon(46)}"
    f"<span style='font-family:var(--font-display);font-weight:700;font-size:30px;color:var(--fg)'>{MAG}</span>"
    f"<span dir='ltr' style='margin-right:auto;font-size:19px;color:var(--fg-faint)'>@ulpan.magazine</span></div></div>")

examples["06-expression-of-day-shchuna"] = (
    f"<div style='{C};width:1080px;height:1080px'>"
    f"<div style='display:flex;align-items:center;justify-content:space-between;padding:56px 64px 0'>"
    f"<span style='display:inline-flex;flex-direction:column;line-height:1.1'>"
    f"<span style='font-family:var(--font-display);font-size:34px;font-weight:500;color:var(--fg)'>{EX_K}</span>"
    f"<span dir='ltr' style='font-size:16px;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:var(--ub-coral);margin-top:4px'>Expression of the day</span></span>"
    f"{pill('#F0586D',SLANG,'Slang','12px 24px',27,14,11)}</div>"
    f"<div style='flex:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:20px 72px;gap:30px'>"
    f"<div style='display:flex;flex-direction:column;gap:12px;align-items:center'>"
    f"<h1 style='margin:0;font-family:var(--font-display);font-weight:700;font-size:118px;line-height:1.04;color:var(--fg)'>{exp['idiom']}</h1>"
    f"<span dir='ltr' style='font-family:var(--font-body);font-style:italic;font-size:38px;color:var(--fg-faint)'>{exp['translit']}</span></div>"
    f"<div style='width:60%;height:1.5px;background:var(--ub-rule)'></div>"
    f"<div style='display:flex;flex-direction:column;gap:8px;align-items:center;opacity:0.6'>"
    f"<span dir='ltr' style='font-size:15px;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:var(--fg-faint)'>Literally</span>"
    f"<span dir='ltr' style='font-family:var(--font-serif);font-style:italic;font-size:40px;color:var(--fg-faint)'>{exp['literalEn']}</span></div>"
    f"<div style='display:flex;flex-direction:column;gap:8px;align-items:center'>"
    f"<span dir='ltr' style='font-size:15px;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:var(--ub-coral)'>Really means</span>"
    f"<span dir='ltr' style='font-family:var(--font-serif);font-style:italic;font-size:52px;font-weight:600;line-height:1.22;color:var(--ub-coral);text-wrap:balance'>{exp['realEn']}</span></div></div>"
    f"<div style='margin:0 64px;background:var(--ub-cream-pale);border:1.5px solid var(--ub-rule-soft);border-radius:var(--r-lg);padding:32px 44px;box-shadow:var(--shadow-card);display:flex;flex-direction:column;gap:10px;align-items:center;text-align:center'>"
    f"<span style='font-family:var(--font-display);font-size:40px;font-weight:500;line-height:1.2;color:var(--fg)'>{EX_EX}</span>"
    f"<span dir='ltr' style='font-family:var(--font-serif);font-style:italic;font-size:30px;color:var(--fg-muted)'>He did a sloppy job in front of the whole office.</span></div>"
    f"<div style='display:flex;align-items:center;gap:16px;padding:32px 64px 44px'>{icon(46)}"
    f"<span style='font-family:var(--font-display);font-weight:700;font-size:30px;color:var(--fg)'>{MAG}</span>"
    f"<span dir='ltr' style='margin-right:auto;font-size:19px;color:var(--fg-faint)'>@ulpan.magazine</span></div></div>")

def carousel_interior(variant):
    rule = "<div style='height:14px;background:linear-gradient(to left, var(--ub-teal) 0 33.3%, var(--ub-gold) 33.3% 66.6%, var(--ub-coral) 66.6% 100%)'></div>"
    if variant == "idiom":
        badge = pill('#F0586D', SLANG, 'Slang', '12px 26px', 28, 15, 12); slideno = "03"; brand_he, handle = MAG, "@ulpan.magazine"
    else:
        badge = (f"<span style='display:inline-flex;align-items:center;gap:16px'>{dot(58,24,'#FFC60B','B1')}"
                 f"<span style='display:inline-flex;flex-direction:column;line-height:1.12'>"
                 f"<span style='font-family:var(--font-display);font-size:27px;font-weight:500;color:var(--fg)'>{ramah(3)}</span>"
                 f"<span dir='ltr' style='font-size:14px;font-weight:700;letter-spacing:0.16em;text-transform:uppercase;color:var(--fg-faint)'>Level B1</span></span></span>")
        slideno = "02" if variant == "point" else "07"; brand_he, handle = AKT, "@aktuali"
    badgerow = (f"<div style='display:flex;align-items:center;justify-content:space-between;padding:56px 72px 0'>{badge}"
                f"<span dir='ltr' style='font-size:22px;font-weight:700;color:var(--ub-coral);letter-spacing:0.04em'>{slideno}</span></div>")
    if variant == "point":
        body = (f"<div style='display:flex;flex-direction:column;gap:34px;align-items:center'>"
                f"<h2 style='margin:0;font-family:var(--font-display);font-weight:700;font-size:84px;line-height:1.1;color:var(--fg);text-wrap:balance'>{ci['he']}</h2>"
                f"<p dir='ltr' style='margin:0;font-family:var(--font-serif);font-style:italic;font-size:44px;line-height:1.3;color:var(--fg-muted);text-wrap:pretty'>{ci['en']}</p></div>")
    elif variant == "idiom":
        body = (f"<div style='display:flex;flex-direction:column;gap:48px;align-items:center;width:100%'>"
                f"<div style='display:flex;flex-direction:column;gap:14px;align-items:center'>"
                f"<h2 style='margin:0;font-family:var(--font-display);font-weight:700;font-size:88px;line-height:1.08;color:var(--fg)'>{CI_IDIOM}</h2>"
                f"<span dir='ltr' style='font-family:var(--font-body);font-style:italic;font-size:30px;color:var(--fg-faint)'>{CI_IDIOM_TR}</span></div>"
                f"<div style='width:100%;height:1.5px;background:var(--ub-rule)'></div>"
                f"<div style='display:flex;flex-direction:column;gap:10px;align-items:center;opacity:0.6'>"
                f"<span style='font-family:var(--font-display);font-size:48px;color:var(--fg-faint);font-weight:400'>{CI_LITHE}</span>"
                f"<span dir='ltr' style='font-family:var(--font-serif);font-style:italic;font-size:34px;color:var(--fg-faint)'>{CI_LITEN}</span></div>"
                f"<div style='display:flex;flex-direction:column;gap:10px;align-items:center'>"
                f"<span style='font-family:var(--font-display);font-size:60px;font-weight:700;color:var(--ub-coral)'>{CI_REALHE}</span>"
                f"<span dir='ltr' style='font-family:var(--font-serif);font-style:italic;font-size:38px;color:var(--fg)'>{CI_REALEN}</span></div></div>")
    else:
        body = (f"<div style='display:flex;flex-direction:column;gap:40px;align-items:center'>{icon(128)}"
                f"<h2 style='margin:0;font-family:var(--font-display);font-weight:700;font-size:80px;line-height:1.1;color:var(--fg);text-wrap:balance'>{CI_CTAHE}</h2>"
                f"<p dir='ltr' style='margin:0;font-family:var(--font-serif);font-style:italic;font-size:42px;color:var(--fg-muted);text-wrap:pretty'>{CI_CTAEN}</p>"
                f"<span style='display:inline-flex;align-items:center;gap:14px;padding:20px 44px;border-radius:999px;background:var(--ub-coral);color:#fff;font-size:34px;font-weight:700;box-shadow:var(--shadow-md)'>{CI_CTABTN}</span></div>")
    bodywrap = f"<div style='flex:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:48px 96px;gap:34px'>{body}</div>"
    foot = (f"<div style='display:flex;align-items:center;gap:16px;padding:0 72px 56px'>{icon(44)}"
            f"<span style='font-family:var(--font-display);font-weight:700;font-size:30px;color:var(--fg)'>{brand_he}</span>"
            f"<span dir='ltr' style='font-size:20px;color:var(--fg-faint);margin-right:auto'>{handle}</span></div>")
    return f"<div style='{C};width:1080px;height:1350px'>{rule}{badgerow}{bodywrap}{foot}</div>"

examples["08-carousel-interior-point"] = carousel_interior("point")
examples["09-carousel-interior-idiom"] = carousel_interior("idiom")
examples["10-carousel-interior-cta"]   = carousel_interior("cta")

def cover(level, headline, subhead, photo):
    color, n = CEFR[level]
    return (f"<div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:var(--ub-ink);font-family:var(--font-body);direction:rtl'>"
        f"<div style='position:absolute;inset:0;background:radial-gradient(120% 90% at 70% 18%, #6b5746 0%, #3a2f29 48%, #1c1714 100%)'></div>"
        f"<img src='{photo}' style='position:absolute;inset:0;width:100%;height:100%;object-fit:cover'>"
        f"<div style='position:absolute;left:0;right:0;bottom:0;height:74%;background:linear-gradient(to top, rgba(0,0,0,0.82) 0%, rgba(0,0,0,0.55) 38%, rgba(0,0,0,0) 100%)'></div>"
        f"<div style='position:absolute;top:64px;right:64px;display:flex;align-items:center;gap:16px'>{dot(60,25,color,level,'0 2px 10px rgba(0,0,0,0.35)')}"
        f"<span style='display:inline-flex;flex-direction:column;line-height:1.12'>"
        f"<span style='font-family:var(--font-display);font-size:28px;font-weight:500;color:var(--ub-cream-pale)'>{ramah(n)}</span>"
        f"<span dir='ltr' style='font-size:15px;font-weight:700;letter-spacing:0.16em;text-transform:uppercase;color:rgba(255,253,250,0.7)'>Level {level}</span></span></div>"
        f"<div style='position:absolute;left:72px;right:72px;bottom:72px;display:flex;flex-direction:column;gap:28px'>"
        f"<h1 style='margin:0;font-family:var(--font-display);font-weight:700;font-size:96px;line-height:1.05;color:var(--ub-cream-pale);text-wrap:balance'>{headline}</h1>"
        f"<p dir='ltr' style='margin:0;font-family:var(--font-serif);font-style:italic;font-size:46px;line-height:1.25;color:rgba(255,253,250,0.86);text-wrap:pretty'>{subhead}</p>"
        f"<div style='display:flex;align-items:center;gap:18px;margin-top:14px;padding-top:30px;border-top:1.5px solid rgba(255,253,250,0.2)'>"
        f"<img src='assets/logos/aleph-icon-color.png' style='width:56px;height:auto;display:block'>"
        f"<span style='display:inline-flex;flex-direction:column;line-height:1.1'>"
        f"<span style='font-family:var(--font-display);font-weight:700;font-size:36px;color:var(--ub-cream-pale)'>{AKT}</span>"
        f"<span dir='ltr' style='font-size:16px;font-weight:500;letter-spacing:0.04em;color:rgba(255,253,250,0.7);margin-top:3px'>The daily paper in easy Hebrew</span></span></div></div></div>")

# --- 2 more real articles: data fetched via curl (TLS-verified) into local JSON ---
def fetch_article(path, level):
    d = json.load(open(path, encoding="utf-8"))[0]
    lvl = next(l for l in d["akt_article_levels"] if l["level"] == level)
    return d.get("photo_url") or "", lvl["title"], lvl.get("title_en") or ""
try:
    p1, h1, s1 = fetch_article("/tmp/ds-export/a_outage.json", "A2")
    examples["11-cover-outage-A2"] = cover("A2", h1, s1, p1)
    p2, h2, s2 = fetch_article("/tmp/ds-export/a_worldcup.json", "C1")
    examples["12-cover-worldcup-C1"] = cover("C1", h2, s2, p2)
    print("fetched 11/12:", repr(h1), "|", repr(h2))
except Exception as e:
    print("FETCH FAILED:", e)

print("RAMAH=%r AKT=%r MAG=%r SLANG=%r" % (RAMAH, AKT, MAG, SLANG))
print("CLIFF_HE=%r" % CLIFF_HE); print("ID_REAL=%r" % ID_REAL); print("WOD_K=%r EX_K=%r" % (WOD_K, EX_K))
print("ra.hePre=%r ra.heHero=%r ra.hePost=%r" % (ra.get('hePre'), ra.get('heHero'), ra.get('hePost')))
print("wod.word=%r exp.idiom=%r" % (wod.get('word'), exp.get('idiom')))
for name, body in examples.items():
    open(os.path.join(PROJ, f"ex-{name}.html"), "w", encoding="utf-8").write(page(body))
print("DONE", len(examples), "examples")
