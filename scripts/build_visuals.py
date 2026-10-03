#!/usr/bin/env python3
"""Build the guide's diagrams as light and dark SVGs.

Every visual is defined once here and rendered in two themes, so the light
and dark versions never drift apart. The README shows the right one with a
<picture> element.

Usage:
    python3 scripts/build_visuals.py          # write SVGs to assets/
    python3 scripts/build_visuals.py --check  # also verify text fits (needs Pillow)

House style: no em or en dashes in any visible text.
"""

from __future__ import annotations

import os
import pathlib
import sys
from xml.sax.saxutils import escape

ROOT = pathlib.Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"

FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"

THEMES = {
    "light": {
        "card": "#f6f8fa",
        "surface": "#ffffff",
        "border": "#d1d9e0",
        "text": "#1f2328",
        "muted": "#59636e",
        "green": "#1a7f37",
        "green_bg": "#dafbe1",
        "amber": "#9a6700",
        "amber_bg": "#fff8c5",
        "red": "#cf222e",
        "red_bg": "#ffebe9",
        "blue": "#0969da",
    },
    "dark": {
        "card": "#151b23",
        "surface": "#0d1117",
        "border": "#3d444d",
        "text": "#f0f6fc",
        "muted": "#9198a1",
        "green": "#3fb950",
        "green_bg": "#12261e",
        "amber": "#d29922",
        "amber_bg": "#2b2111",
        "red": "#f85149",
        "red_bg": "#301517",
        "blue": "#4493f8",
    },
}

DASHES = (chr(0x2013), chr(0x2014))  # en and em dash, banned by house style

# Text-fit constraints collected while building: (text, font_px, bold, max_width)
FIT: list[tuple[str, float, bool, float]] = []


def text(x, y, s, size, fill, weight=400, anchor="start", spacing=0.0, max_width=None):
    if max_width is not None:
        FIT.append((s, size, weight >= 600, max_width))
    ls = f' letter-spacing="{spacing}"' if spacing else ""
    return (
        f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" '
        f'fill="{fill}" text-anchor="{anchor}"{ls}>{escape(s)}</text>'
    )


def doc(w, h, title, desc, body, t, radius=16, framed=True):
    frame = (
        f'<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="{radius}" '
        f'fill="{t["card"]}" stroke="{t["border"]}"/>'
        if framed
        else f'<rect width="{w}" height="{h}" fill="{t["surface"]}"/>'
    )
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        f'viewBox="0 0 {w} {h}" role="img" aria-labelledby="t d">\n'
        f'<title id="t">{escape(title)}</title>\n'
        f'<desc id="d">{escape(desc)}</desc>\n'
        f'<style>text {{ font-family: {FONT}; }}</style>\n'
        f"{frame}\n{body}\n</svg>\n"
    )


def shield(x, y, scale, t):
    """Shield with a keyhole, drawn in a 160 x 200 box."""
    return (
        f'<g transform="translate({x},{y}) scale({scale})">'
        f'<path d="M80 0 L160 28 V100 C160 152 126 186 80 200 C34 186 0 152 0 100 V28 Z" fill="{t["blue"]}"/>'
        f'<path d="M80 18 L144 40 V100 C144 142 117 170 80 182 C43 170 16 142 16 100 V40 Z" '
        f'fill="none" stroke="{t["card"]}" stroke-opacity="0.35" stroke-width="3"/>'
        f'<circle cx="80" cy="86" r="20" fill="{t["card"]}"/>'
        f'<path d="M69 98 H91 L97 146 H63 Z" fill="{t["card"]}"/>'
        f"</g>"
    )


def pill(x, y, label, color, bg, size=14, pad=16, height=32, t=None):
    # Width is estimated generously so labels never touch the edge.
    w = round(len(label) * size * 0.62 + pad * 2)
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{height}" rx="{height / 2}" fill="{bg}"/>'
        + text(x + w / 2, y + height / 2 + size * 0.36, label, size, color, 700, "middle")
    ), w


# ---------------------------------------------------------------- banner

def banner(t):
    w, h = 1000, 250
    b = [shield(56, 46, 0.78, t)]
    b.append(text(220, 104, "Google Account Hardening Guide", 40, t["text"], 700, max_width=750))
    b.append(text(221, 142, "Passkeys, recovery, sessions, Gmail, Chrome, Android", 19, t["muted"], max_width=740))
    b.append(text(221, 168, "and privacy. One ordered plan, sourced and current.", 19, t["muted"], max_width=740))
    x = 221
    for label, c in (("Baseline", "green"), ("Enhanced", "amber"), ("Maximum", "red")):
        p, pw = pill(x, 190, label, t[c], t[c + "_bg"], size=14)
        b.append(p)
        x += pw + 10
    return doc(
        w, h,
        "Google Account Hardening Guide",
        "Passkeys, recovery, sessions, Gmail, Chrome, Android and privacy in one ordered plan, at three levels: Baseline, Enhanced and Maximum.",
        "\n".join(b), t,
    )


# ------------------------------------------------------- text measurement

# Advance widths of printable ASCII (space to tilde) in DejaVu Sans and
# DejaVu Sans Bold, per 1000 units of font size. Layout measures with these
# tables so the SVGs come out the same on every machine. DejaVu is wider than
# the fonts GitHub renders with, so text measured to fit here fits there.
WIDTHS = {
    False: [
        318, 401, 460, 838, 636, 950, 780, 275, 390, 390, 500, 838, 318, 361, 318, 337,
        636, 636, 636, 636, 636, 636, 636, 636, 636, 636, 337, 337, 838, 838, 838, 531,
        1000, 684, 686, 698, 770, 632, 575, 775, 752, 295, 295, 656, 557, 863, 748, 787,
        603, 787, 695, 635, 611, 732, 684, 989, 685, 611, 685, 390, 337, 390, 838, 500,
        500, 613, 635, 550, 635, 615, 352, 635, 634, 278, 278, 579, 278, 974, 634, 612,
        635, 635, 411, 521, 392, 634, 592, 818, 592, 592, 525, 636, 337, 636, 838,
    ],
    True: [
        348, 456, 521, 838, 696, 1002, 872, 306, 457, 457, 523, 838, 380, 415, 380, 365,
        696, 696, 696, 696, 696, 696, 696, 696, 696, 696, 400, 400, 838, 838, 838, 580,
        1000, 774, 762, 734, 830, 683, 683, 821, 837, 372, 372, 775, 637, 995, 837, 850,
        733, 850, 770, 720, 682, 812, 774, 1103, 771, 724, 725, 457, 365, 457, 838, 500,
        500, 675, 716, 593, 716, 678, 435, 716, 712, 343, 343, 665, 343, 1042, 712, 687,
        716, 716, 493, 595, 478, 712, 652, 924, 645, 652, 582, 712, 365, 712, 838,
    ],
}


def measure(s, size, bold=False):
    """Width of s in px, with 2 percent to spare for kerning differences."""
    return sum(WIDTHS[bold][ord(c) - 32] for c in s) * size / 1000 * 1.02


def wrap(s, size, bold, max_w):
    """Split s into lines no wider than max_w."""
    lines, line = [], ""
    for word in s.split():
        trial = f"{line} {word}".strip()
        if line and measure(trial, size, bold) > max_w:
            lines.append(line)
            line = word
        else:
            line = trial
    return lines + [line]


# ------------------------------------------------------- sign-in strength

# Tiers, not scores: sources rank these methods by tier only, not by distance.
# (name, why, color, tag); the relay line goes after the first row.
METHODS = [
    ("Passkey or security key", "Works only on Google's real site.", "green", "Phishing-resistant"),
    ("Google prompt or authenticator code", "A fake page passes them on as you approve or type.", "amber", "Phishable"),
    ("Text or voice code", "Relayed by fake pages and caught by SIM swaps.", "red", "Weak"),
    ("Password alone", "Phished, leaked and reused.", "red", "Weak"),
]
SIGN_IN_TITLE = "Which sign-in methods resist phishing"
SIGN_IN_SUBTITLE = "Which methods a fake sign-in page can relay"
RELAY_LABEL = "Everything below this line can be relayed by a fake sign-in page"
SIGN_IN_FOOTER = "No sign-in method stops malware that steals your signed-in session."
SIGN_IN_ALT = (
    "Sign-in methods by phishing resistance. Passkeys and security keys resist phishing. "
    "Below a line marking what a fake sign-in page can relay: Google prompts and "
    "authenticator codes are phishable; text or voice codes and a password alone are weak. "
    "No method stops malware that steals a signed-in session."
)


def sign_in_strength(t):
    # GitHub shows this at about 343 px wide on a phone. With w = 680 the
    # smallest text (22 px) still renders at 11 px there.
    w, m = 680, 16                        # canvas width, outer margin
    title, body, name_px, tag_px = 28, 22, 24, 22
    cx0, cw = m, w - 2 * m                # card left edge and width
    tx, tr = cx0 + 28, cx0 + cw - 20      # card text left and right edges
    b = []
    y = 52
    for line in wrap(SIGN_IN_TITLE, title, True, w - 2 * 24):
        b.append(text(24, round(y, 1), line, title, t["text"], 700, max_width=w - 2 * 24))
        y += title * 1.25
    y += 2
    for line in wrap(SIGN_IN_SUBTITLE, body, False, w - 2 * 24):
        b.append(text(24, round(y, 1), line, body, t["muted"], max_width=w - 2 * 24))
        y += body * 1.35
    y += 8
    for i, (name, why, c, tag) in enumerate(METHODS):
        if i == 1:
            y += 10
            lines = wrap(RELAY_LABEL, body, True, cw - 120)
            lw = max(measure(s, body, True) for s in lines) + 32
            lh = len(lines) * body * 1.3 + 18
            mid = y + lh / 2
            b.append(f'<line x1="{cx0}" y1="{mid:.1f}" x2="{cx0 + cw}" y2="{mid:.1f}" stroke="{t["red"]}" '
                     f'stroke-width="2" stroke-dasharray="7 7"/>')
            b.append(f'<rect x="{w / 2 - lw / 2:.1f}" y="{y:.1f}" width="{lw:.1f}" height="{lh:.1f}" rx="12" '
                     f'fill="{t["card"]}" stroke="{t["red"]}" stroke-width="1.5"/>')
            for j, s in enumerate(lines):
                b.append(text(w / 2, round(y + 9 + body * (1.0 + j * 1.3), 1), s, body, t["red"], 700, "middle", max_width=lw - 16))
            y += lh + 20
        pw = measure(tag, tag_px, True) + 26
        names = wrap(name, name_px, True, tr - tx - pw - 12)
        whys = wrap(why, body, False, tr - tx)
        h = 24 + len(names) * name_px * 1.25 + 8 + len(whys) * body * 1.35 + 14
        b.append(f'<rect x="{cx0 + 0.5}" y="{y:.1f}" width="{cw - 1}" height="{h:.1f}" rx="12" '
                 f'fill="{t["surface"]}" stroke="{t["border"]}"/>')
        b.append(f'<rect x="{cx0 + 10}" y="{y + 14:.1f}" width="6" height="{h - 28:.1f}" rx="3" fill="{t[c]}"/>')
        ly = y + 20 + name_px
        b.append(f'<rect x="{tr - pw:.1f}" y="{ly - name_px * 0.35 - 18:.1f}" width="{pw:.1f}" height="36" rx="18" fill="{t[c + "_bg"]}"/>')
        b.append(text(round(tr - pw / 2, 1), round(ly - name_px * 0.35 + tag_px * 0.36, 1), tag, tag_px, t[c], 700, "middle", max_width=pw - 12))
        for s in names:
            b.append(text(tx, round(ly, 1), s, name_px, t["text"], 700, max_width=tr - tx - pw - 12))
            ly += name_px * 1.25
        ly += 8 - name_px * 1.25 + body * 1.35
        for s in whys:
            b.append(text(tx, round(ly, 1), s, body, t["muted"], max_width=tr - tx))
            ly += body * 1.35
        y += h + 12
    y += 28
    for line in wrap(SIGN_IN_FOOTER, body, True, w - 2 * 24):
        b.append(text(w / 2, round(y, 1), line, body, t["text"], 700, "middle", max_width=w - 2 * 24))
        y += body * 1.35
    h = round(y + 14)
    return doc(w, h, SIGN_IN_TITLE, SIGN_IN_ALT, "\n".join(b), t)


# --------------------------------------------------------- social preview

def social_preview(t):
    w, h = 1280, 640
    b = [
        f'<rect width="{w}" height="{h}" fill="{t["surface"]}"/>',
        f'<rect x="40" y="40" width="{w - 80}" height="{h - 80}" rx="28" fill="{t["card"]}" stroke="{t["border"]}"/>',
        shield(118, 186, 1.2, t),
        text(372, 238, "Google Account", 74, t["text"], 700, max_width=840),
        text(372, 322, "Hardening Guide", 74, t["text"], 700, max_width=840),
        text(374, 380, "Passkeys, recovery, sessions, Gmail, Chrome,", 27, t["muted"], max_width=830),
        text(374, 416, "Android and privacy. Sourced and current.", 27, t["muted"], max_width=830),
    ]
    x = 374
    for label, c in (("Baseline", "green"), ("Enhanced", "amber"), ("Maximum", "red")):
        p, pw = pill(x, 446, label, t[c], t[c + "_bg"], size=19, pad=20, height=42)
        b.append(p)
        x += pw + 14
    b.append(text(374, 548, "github.com/iAnonymous3000/google-hardening-guide", 22, t["muted"], 400, max_width=820))
    return doc(w, h, "Google Account Hardening Guide", "Social preview image.", "\n".join(b), t, framed=False)


# ------------------------------------------------------------------- main

VISUALS = {
    "banner": banner,
    "sign-in-strength": sign_in_strength,
}


def skip(reason) -> int:
    """Skip the text-fit check locally, but fail in CI so it cannot pass silently."""
    if os.environ.get("CI"):
        print(f"{reason}; the text-fit check cannot run in CI.")
        return 1
    print(f"{reason}; skipping text-fit check.")
    return 0


def check_fit() -> int:
    try:
        from PIL import ImageFont
    except ImportError:
        return skip("Pillow not installed")
    candidates = {
        False: ["DejaVuSans.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "Arial.ttf"],
        True: ["DejaVuSans-Bold.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", "Arial Bold.ttf"],
    }
    fonts = {}
    for bold, paths in candidates.items():
        for p in paths:
            try:
                fonts[bold] = p
                ImageFont.truetype(p, 12)
                break
            except OSError:
                fonts.pop(bold, None)
    if len(fonts) < 2:
        return skip("No wide reference font found")
    bad = 0
    for s, size, bold, max_w in FIT:
        f = ImageFont.truetype(fonts[bold], round(size * 4))
        width = f.getlength(s) / 4
        if width > max_w:
            bad += 1
            print(f"TOO WIDE ({width:.0f}px > {max_w:.0f}px): {s!r}")
    print(f"Text-fit check: {len(FIT)} strings, {bad} too wide (measured with a wide fallback font).")
    return bad


def main() -> int:
    ASSETS.mkdir(exist_ok=True)
    for name, fn in VISUALS.items():
        for theme, t in THEMES.items():
            out = ASSETS / f"{name}-{theme}.svg"
            svg = fn(t)
            assert not any(d in svg for d in DASHES), f"long dash in {out.name}"
            out.write_text(svg, encoding="utf-8")
            print(f"wrote {out.relative_to(ROOT)}")
    (ASSETS / "social-preview.svg").write_text(social_preview(THEMES["dark"]), encoding="utf-8")
    print("wrote assets/social-preview.svg (export to PNG at 1280 x 640 for GitHub settings)")
    if "--check" in sys.argv:
        return 1 if check_fit() else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
