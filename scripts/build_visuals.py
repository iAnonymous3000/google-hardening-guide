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
        "blue_bg": "#ddf4ff",
        "track": "#e6eaef",
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
        "blue_bg": "#0f2440",
        "track": "#262c36",
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


# ---------------------------------------------------------- attack doors

DOORS = [
    ("Sign-in page",
     ["Phishing kits relay your", "password, codes and prompts", "in real time"],
     ["Passkeys and security keys"]),
    ("Your devices",
     ["Infostealer malware copies", "your session cookies and", "saved passwords"],
     ["Clean devices and signing", "out old sessions"]),
    ("Phone number",
     ["SIM swaps move your number", "to a criminal, along with", "your text codes"],
     ["Carrier lock, no text codes"]),
    ("Recovery",
     ["A hijacked recovery email", "or phone resets your", "whole account"],
     ["Strong recovery email and", "recovery contacts"]),
    ("Linked apps",
     ["Consent phishing plants an", "app token that outlives", "your password"],
     ["Review linked apps, read", "every consent screen"]),
    ("You",
     ["Fake Google Support calls", "ask you to read a code or", "approve a prompt"],
     ["Google never calls. Hang up."]),
]


def door_icon(cx, cy, t):
    # A simple door with a knob, inside a tinted circle.
    return (
        f'<circle cx="{cx}" cy="{cy}" r="17" fill="{t["blue_bg"]}"/>'
        f'<rect x="{cx - 7}" y="{cy - 10}" width="14" height="20" rx="2" fill="none" stroke="{t["blue"]}" stroke-width="2"/>'
        f'<circle cx="{cx + 3}" cy="{cy + 1}" r="1.8" fill="{t["blue"]}"/>'
    )


def attack_surface(t):
    w, h = 1000, 640
    b = [
        text(32, 54, "Six doors into your Google account", 27, t["text"], 700, max_width=900),
        text(32, 84, "Every control in this guide locks one of these doors.", 16, t["muted"], max_width=900),
    ]
    cw, ch, gap = 302, 242, 15
    xs = [32, 32 + cw + gap, 32 + 2 * (cw + gap)]
    ys = [112, 112 + ch + 14]
    for i, (name, attack, lock) in enumerate(DOORS):
        x, y = xs[i % 3], ys[i // 3]
        b.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="12" fill="{t["surface"]}" stroke="{t["border"]}"/>')
        b.append(door_icon(x + 36, y + 36, t))
        b.append(text(x + 64, y + 43, name, 19, t["text"], 700, max_width=cw - 80))
        b.append(text(x + 22, y + 82, "ATTACK", 11.5, t["red"], 700, spacing=1.2))
        for j, line in enumerate(attack):
            b.append(text(x + 22, y + 106 + j * 21, line, 15.5, t["text"], max_width=cw - 40))
        ly = y + 106 + len(attack) * 21 + 14
        b.append(text(x + 22, ly, "LOCK", 11.5, t["green"], 700, spacing=1.2))
        for j, line in enumerate(lock):
            b.append(text(x + 22, ly + 24 + j * 21, line, 15.5, t["text"], 700, max_width=cw - 40))
    desc = " ".join(
        f"{n}: {' '.join(a)}. Lock: {' '.join(l)}." for n, a, l in DOORS
    )
    return doc(w, h, "Six doors into your Google account", desc, "\n".join(b), t)


# ------------------------------------------------------- sign-in strength

METHODS = [
    ("Hardware security key", "Phishing-proof. The secret never leaves the key.", 1.00, "green", "Phishing-resistant"),
    ("Passkey", "Phishing-proof. Synced end-to-end encrypted.", 0.90, "green", "Phishing-resistant"),
    ("Google prompt", "Shows where a sign-in comes from, but relayable.", 0.55, "amber", "Phishable"),
    ("Authenticator app code", "Immune to SIM swaps. Relayed by phishing kits.", 0.45, "amber", "Phishable"),
    ("Text or voice code", "Hit by SIM swaps and relayed by phishing kits.", 0.22, "red", "Weak"),
    ("Password alone", "Phished, leaked and reused. Never enough.", 0.10, "red", "Weak"),
]


def sign_in_strength(t):
    w, h = 1000, 664
    b = [
        text(32, 54, "Phishing resistance by sign-in method", 27, t["text"], 700, max_width=900),
        text(32, 84, "How each method holds up against phishing kits, SIM swaps and malware.", 16, t["muted"], max_width=920),
    ]
    y, row_h, gap = 108, 70, 10
    for i, (name, desc, score, c, tag) in enumerate(METHODS):
        if i == 2:
            line_y = y + 14
            b.append(f'<line x1="32" y1="{line_y}" x2="968" y2="{line_y}" stroke="{t["red"]}" stroke-width="1.5" stroke-dasharray="6 6"/>')
            label = "Everything below this line can be relayed by a fake website"
            lw = 466  # label measured at 437px in a wide fallback font, plus padding
            b.append(f'<rect x="{500 - lw / 2}" y="{line_y - 13}" width="{lw}" height="26" rx="13" fill="{t["card"]}"/>')
            b.append(text(500, line_y + 4.5, label, 13, t["red"], 700, "middle", max_width=lw - 12))
            y += 30
        b.append(f'<rect x="32" y="{y}" width="936" height="{row_h}" rx="12" fill="{t["surface"]}" stroke="{t["border"]}"/>')
        b.append(f'<circle cx="66" cy="{y + row_h / 2}" r="16" fill="{t[c + "_bg"]}"/>')
        b.append(text(66, y + row_h / 2 + 5.5, str(i + 1), 15, t[c], 700, "middle"))
        b.append(text(96, y + 30, name, 18, t["text"], 700, max_width=420))
        b.append(text(96, y + 53, desc, 14.5, t["muted"], max_width=430))
        bx, bw = 548, 220
        b.append(f'<rect x="{bx}" y="{y + 27}" width="{bw}" height="16" rx="8" fill="{t["track"]}"/>')
        b.append(f'<rect x="{bx}" y="{y + 27}" width="{max(16, bw * score):.0f}" height="16" rx="8" fill="{t[c]}"/>')
        pw = 166
        px = 968 - 18 - pw
        b.append(f'<rect x="{px}" y="{y + 20}" width="{pw}" height="30" rx="15" fill="{t[c + "_bg"]}"/>')
        b.append(text(px + pw / 2, y + 40, tag, 13, t[c], 700, "middle", max_width=pw - 14))
        y += row_h + gap
    b.append(text(500, y + 26, "Your account is only as strong as the weakest method it still accepts.", 16, t["text"], 700, "middle", max_width=900))
    desc = "Sign-in methods ranked strongest to weakest. " + " ".join(
        f"{i + 1}. {n} ({tag}): {d}" for i, (n, d, _, _, tag) in enumerate(METHODS)
    )
    return doc(w, h, "Phishing resistance by sign-in method", desc, "\n".join(b), t)


# ----------------------------------------------------------------- levels

LEVELS = [
    ("LEVEL 1", "Baseline", "green", ["Everyone.", "About 20 minutes, free."],
     ["Passkeys on every device", "2-Step Verification on", "Backup codes offline",
      "Recovery info and contacts", "Devices and apps reviewed", "Gmail forwarding checked",
      "Carrier SIM lock on"]),
    ("LEVEL 2", "Enhanced", "amber", ["Money, crypto, a business,", "an audience or admin access."],
     ["Two hardware security keys", "No text message codes", "Saved passwords encrypted",
      "Recovery email hardened", "Calendar invite filter on", "Third-party cookies off",
      "3-month auto-delete"]),
    ("LEVEL 3", "Maximum", "red", ["Journalists, activists,", "executives, anyone targeted."],
     ["Advanced Protection on", "Phone lockdown mode on", "No apps with mail access",
      "Separate accounts per role", "Dedicated admin device", "Gemini unlinked from apps",
      "Backup key stored off-site"]),
]


def check_icon(cx, cy, c, bg):
    return (
        f'<circle cx="{cx}" cy="{cy}" r="10" fill="{bg}"/>'
        f'<path d="M{cx - 4.5} {cy + 0.5} L{cx - 1.2} {cy + 3.8} L{cx + 4.8} {cy - 3.2}" '
        f'fill="none" stroke="{c}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>'
    )


def levels(t):
    w, h = 1000, 584
    b = [
        text(32, 54, "Three levels of hardening", 27, t["text"], 700, max_width=900),
        text(32, 84, "Each level includes everything before it. Go as far as your risk requires.", 16, t["muted"], max_width=920),
    ]
    cw, gap = 302, 15
    for i, (tag, name, c, who, items) in enumerate(LEVELS):
        x, y = 32 + i * (cw + gap), 108
        ch = 446
        b.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="12" fill="{t["surface"]}" stroke="{t["border"]}"/>')
        b.append(f'<path d="M{x + 12} {y + 0.5} H{x + cw - 12} A11.5 11.5 0 0 1 {x + cw - 0.5} {y + 12} V{y + 6} H{x + 0.5} V{y + 12} A11.5 11.5 0 0 1 {x + 12} {y + 0.5} Z" fill="{t[c]}"/>')
        b.append(text(x + 24, y + 42, tag, 12, t[c], 700, spacing=1.5))
        b.append(text(x + 24, y + 76, name, 27, t["text"], 700, max_width=cw - 48))
        for j, line in enumerate(who):
            b.append(text(x + 24, y + 104 + j * 20, line, 15, t["muted"], max_width=cw - 44))
        b.append(f'<line x1="{x + 24}" y1="{y + 142}" x2="{x + cw - 24}" y2="{y + 142}" stroke="{t["border"]}"/>')
        for j, item in enumerate(items):
            iy = y + 178 + j * 40
            b.append(check_icon(x + 34, iy - 5, t[c], t[c + "_bg"]))
            b.append(text(x + 54, iy, item, 15.5, t["text"], max_width=cw - 70))
    desc = " ".join(f"{name} ({' '.join(who)}): {', '.join(items)}." for _, name, _, who, items in LEVELS)
    return doc(w, h, "Three levels of hardening", desc, "\n".join(b), t)


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
    "attack-surface": attack_surface,
    "sign-in-strength": sign_in_strength,
    "levels": levels,
}


def check_fit() -> int:
    try:
        from PIL import ImageFont
    except ImportError:
        print("Pillow not installed; skipping text-fit check.")
        return 0
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
        print("No wide reference font found; skipping text-fit check.")
        return 0
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
