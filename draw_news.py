#!/usr/bin/env python3
"""Draw the 20 November 2026 world-news front page (1024x1024 PNG).

Build-time generator only: the submitted program (main.ts) just copies the
committed entry.png to /output, so the graded run is byte-deterministic.
Run:  python3 draw_news.py   -> writes entry.png next to this script.
News facts (all first reported 20 Nov 2026, sources in README.md):
  1. GTA VI: $3.79bn day-one retail sales, 32.5m pre-order copies (Reuters/CNN).
  2. Russian missiles/drone land in Poland; strikes hit three Kyiv bridges.
  3. ICJ: Myanmar committed genocide against the Rohingya.
  4. Markets slide: S&P 500 -3.7% into correction, Nikkei -5.06% (AI sell-off).
  5. Anthropic Nasdaq debut: +17%, $81.3bn raised, largest IPO on record.
  6. UK-EU summit deals: food trade, carbon markets, youth mobility.
  7. Magnitude 6.7 earthquake, central Peru (ticker).
"""
import math
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (246, 241, 231)
INK = (17, 17, 17)
RED = (178, 34, 34)
DARK = (20, 24, 38)
GREY = (90, 86, 78)

F = "/usr/share/fonts/truetype/dejavu/"
SERIF_B = F + "DejaVuSerif-Bold.ttf"
SANS_B = F + "DejaVuSans-Bold.ttf"
SANS = F + "DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, lines, fnt, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


def panel(draw, x, y, w, h, fill=(255, 255, 255), outline=INK, width=2):
    draw.rectangle([x, y, x + w, y + h], fill=fill, outline=outline, width=width)


def kicker(draw, x, y, s, color=RED, size=17):
    draw.text((x, y), s, font=font(SANS_B, size), fill=color)
    return y + size + 6


# ---------------------------------------------------------------- canvas
img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# Masthead
d.text((512, 18), "THE WORLD IN ONE PAGE", font=font(SERIF_B, 56),
       fill=INK, anchor="ma")
d.line([(28, 96), (996, 96)], fill=RED, width=4)
d.rectangle([28, 104, 996, 138], fill=INK)
d.text((512, 110), "FRIDAY, 20 NOVEMBER 2026  •  THE DAY'S WORLD NEWS IN ONE IMAGE",
       font=font(SANS_B, 21), fill=(255, 255, 255), anchor="ma")

# ---------------------------------------------------------------- lead: GTA VI
LX, LY, LW, LH = 28, 152, 968, 312
panel(d, LX, LY, LW, LH)
# neon Vice-City art on the right
AX, AY, AW, AH = LX + 592, LY + 2, 374, LH - 4
for i in range(AH):
    t = i / AH
    r = int(58 + (255 - 58) * t)
    g = int(28 + (120 - 28) * t)
    b = int(110 + (60 - 110) * t)
    d.line([(AX, AY + i), (AX + AW, AY + i)], fill=(r, g, b))
d.ellipse([AX + AW // 2 - 62, AY + 52, AX + AW // 2 + 62, AY + 176],
          fill=(255, 214, 90))
# skyline
for j, (bx, bw, bh) in enumerate([(0, 52, 96), (56, 40, 130), (100, 58, 84),
                                  (162, 44, 142), (210, 52, 100), (266, 46, 128),
                                  (316, 58, 92)]):
    d.rectangle([AX + bx, AY + AH - bh, AX + bx + bw, AY + AH], fill=(24, 8, 44))
    for wy in range(AY + AH - bh + 10, AY + AH - 8, 16):
        for wx in range(AX + bx + 8, AX + bx + bw - 6, 14):
            if (wx + wy) % 3 == 0:
                d.rectangle([wx, wy, wx + 5, wy + 7], fill=(255, 214, 90))
# palm silhouettes
def palm(px, py, s):
    d.line([(px, py), (px + 6 * s, py - 52 * s)], fill=(16, 40, 20), width=5)
    for ang in (-70, -35, 0, 35, 70):
        a = math.radians(ang - 90)
        ex, ey = px + 6 * s + 34 * s * math.cos(a), py - 52 * s + 30 * s * math.sin(a)
        d.line([(px + 6 * s, py - 52 * s), (ex, ey)], fill=(16, 40, 20), width=4)
palm(AX + 30, AY + AH - 6, 1.0)
palm(AX + AW - 70, AY + AH - 6, 0.85)
d.text((AX + AW // 2, AY + 196), "VI", font=font(SANS_B, 96),
       fill=(255, 255, 255), anchor="ma",
       stroke_width=3, stroke_fill=(24, 8, 44))

TX = LX + 24
y = LY + 18
y = kicker(d, TX, y, "ENTERTAINMENT  •  RECORD LAUNCH")
y = text_block(d, TX, y, wrap(d, "GTA VI makes $3.79 billion in a single day",
                              font(SANS_B, 44), 548),
               font(SANS_B, 44), INK, 50)
y += 6
y = text_block(d, TX, y, wrap(
    d, "Rockstar's blockbuster sold 32.5 million copies before release — "
       "the biggest entertainment launch in history, dwarfing GTA V's "
       "$800 million day one.", font(SANS, 23), 548),
    font(SANS, 23), (40, 40, 40), 30)
d.text((TX, LY + LH - 34), "Take-Two / Rockstar, 20 Nov 2026",
       font=font(SANS_B, 17), fill=GREY)

# ---------------------------------------------------------------- row 2: three panels
PY, PH = 480, 224
PW = 312
GAP = 16
panels2 = [
    ("WAR IN EUROPE", "Russian missiles land in Poland; Kyiv bridges hit",
     "NATO calls the breach a grave violation; three killed in Kyiv.", "kyiv"),
    ("JUSTICE  •  THE HAGUE", "World Court: Myanmar guilty of genocide",
     "The ICJ rules the 2017 crackdown was state-sponsored genocide.", "icj"),
    ("MARKETS", "Stocks slide as the AI sell-off deepens",
     "S&P 500 down 3.7% into correction; Nikkei falls 5.1%.", "markets"),
]
for i, (kick, head, body, art) in enumerate(panels2):
    x = 28 + i * (PW + GAP)
    panel(d, x, PY, PW, PH)
    # art band
    d.rectangle([x + 2, PY + 2, x + PW - 2, PY + 92], fill=DARK)
    if art == "kyiv":
        # explosion starburst
        cx, cy = x + 66, PY + 48
        for k in range(12):
            a = math.radians(k * 30)
            r1 = 34 if k % 2 == 0 else 14
            d.line([(cx, cy), (cx + r1 * math.cos(a), cy + r1 * math.sin(a))],
                   fill=(255, 170, 40), width=5)
        d.ellipse([cx - 12, cy - 12, cx + 12, cy + 12], fill=(255, 220, 90))
        # bridge
        d.line([(x + 140, PY + 70), (x + PW - 16, PY + 70)], fill=(200, 200, 210), width=4)
        for bx in range(x + 150, x + PW - 20, 24):
            d.line([(bx, PY + 70), (bx, PY + 44)], fill=(200, 200, 210), width=3)
        d.text((x + PW - 24, PY + 26), "POLAND • KYIV", font=font(SANS_B, 15),
               fill=(255, 255, 255), anchor="ra")
    elif art == "icj":
        cx, cy = x + PW // 2, PY + 50
        d.line([(cx, PY + 14), (cx, PY + 82)], fill=(220, 180, 80), width=4)
        d.line([(cx - 56, PY + 26), (cx + 56, PY + 26)], fill=(220, 180, 80), width=4)
        for sgn in (-1, 1):
            px = cx + sgn * 56
            d.line([(px, PY + 26), (px, PY + 56)], fill=(220, 180, 80), width=3)
            d.arc([px - 22, PY + 40, px + 22, PY + 74], 0, 180,
                  fill=(220, 180, 80), width=4)
            d.line([(px - 22, PY + 56), (px + 22, PY + 56)],
                   fill=(220, 180, 80), width=3)
        d.ellipse([cx - 6, PY + 8, cx + 6, PY + 20], fill=(220, 180, 80))
    else:  # markets
        pts = [(x + 16, PY + 44), (x + 70, PY + 40), (x + 120, PY + 58),
               (x + 175, PY + 54), (x + 225, PY + 72), (x + 290, PY + 82)]
        d.line(pts, fill=(230, 60, 60), width=5, joint="curve")
        d.polygon([(pts[-1][0], pts[-1][1]), (pts[-1][0] - 16, pts[-1][1] - 2),
                   (pts[-1][0] - 4, pts[-1][1] + 12)], fill=(230, 60, 60))
        d.text((x + 16, PY + 10), "S&P 500  −3.7%", font=font(SANS_B, 19),
               fill=(255, 255, 255))
    y = PY + 104
    y = kicker(d, x + 14, y, kick, size=15)
    y = text_block(d, x + 14, y, wrap(d, head, font(SANS_B, 21), PW - 28),
                   font(SANS_B, 21), INK, 25)
    text_block(d, x + 14, y + 4, wrap(d, body, font(SANS, 16), PW - 28),
               font(SANS, 16), (40, 40, 40), 21)

# ---------------------------------------------------------------- row 3: three panels
PY3, PH3 = 720, 176
panels3 = [
    ("TECH", "Anthropic's Nasdaq debut: shares +17%",
     "$81.3bn raised — record IPO.", "ipo"),
    ("EUROPE", "UK–EU sign deals on food, carbon, youth",
     "Brussels summit resets ties.", "eu"),
    ("DISASTER", "Magnitude 6.7 quake hits central Peru",
     "Tremor strikes near Cerro de Pasco.", "quake"),
]
for i, (kick, head, body, art) in enumerate(panels3):
    x = 28 + i * (PW + GAP)
    panel(d, x, PY3, PW, PH3)
    d.rectangle([x + 2, PY3 + 2, x + PW - 2, PY3 + 62], fill=(245, 240, 228))
    if art == "ipo":
        bars = [(18, 22), (48, 30), (78, 26), (108, 38), (138, 46)]
        for bx, bh in bars:
            d.rectangle([x + bx, PY3 + 56 - bh, x + bx + 22, PY3 + 56],
                        fill=(34, 139, 34))
        d.line([(x + 16, PY3 + 14), (x + 170, PY3 + 14)], fill=(34, 139, 34), width=3)
        d.text((x + 190, PY3 + 8), "+17%", font=font(SANS_B, 26), fill=(34, 139, 34))
    elif art == "eu":
        cx, cy = x + 52, PY3 + 32
        for k in range(12):
            a = math.radians(k * 30 - 90)
            sx, sy = cx + 26 * math.cos(a), cy + 26 * math.sin(a)
            d.ellipse([sx - 3, sy - 3, sx + 3, sy + 3], fill=(255, 204, 0))
        d.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=(255, 204, 0))
        d.text((x + 96, PY3 + 16), "UK  •  EU", font=font(SANS_B, 24), fill=(0, 51, 153))
    else:  # quake
        pts = []
        xx = x + 14
        for j, amp in enumerate([0, 4, -6, 12, -18, 26, -14, 8, -4, 0]):
            pts.append((xx + j * 28, PY3 + 34 + amp))
        d.line(pts, fill=(178, 34, 34), width=3, joint="curve")
        d.text((x + PW - 16, PY3 + 8), "6.7", font=font(SANS_B, 30),
               fill=(178, 34, 34), anchor="ra")
    y = PY3 + 72
    y = kicker(d, x + 14, y, kick, size=14)
    y = text_block(d, x + 14, y, wrap(d, head, font(SANS_B, 19), PW - 28),
                   font(SANS_B, 19), INK, 23)
    text_block(d, x + 14, y + 3, wrap(d, body, font(SANS, 15), PW - 28),
               font(SANS, 15), (40, 40, 40), 19)

# ---------------------------------------------------------------- ticker + footer
d.rectangle([28, 908, 996, 956], fill=INK)
d.text((512, 914), "ALSO TODAY:  Houthi missile hits Riyadh tower  •  BepiColombo reaches Mercury",
       font=font(SANS_B, 14), fill=(255, 255, 255), anchor="ma")
d.text((512, 934), "US loses measles-free status  •  Cyclone Akvan hits Odisha",
       font=font(SANS_B, 14), fill=(255, 255, 255), anchor="ma")
d.text((512, 966), "Drawn summary of the day's reported news — not a photograph.  "
       "Sources: Reuters, CNN, BBC, Barron's, 20 November 2026.",
       font=font(SANS, 14), fill=GREY, anchor="ma")

img.save("entry.png", optimize=True)
print("saved entry.png")
