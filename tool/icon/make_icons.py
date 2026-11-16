# Gera os ícones do app (Windows .ico e macOS .png) — escudo dourado com estrela.
import math, os, sys
from PIL import Image, ImageDraw

ROOT = sys.argv[1] if len(sys.argv) > 1 else '.'
NAVY = (10, 18, 32, 255); GOLD = (224, 178, 58, 255); GOLD2 = (245, 200, 66, 255); PANEL = (22, 36, 61, 255)

def shield(w, h, inset, ox=0, oy=0):
    pts = []
    # contorno do escudo (topo em ponta, laterais retas, base curva)
    top = (w / 2, inset)
    tr = (w - inset, h * 0.16 + inset * 0.6)
    mr = (w - inset, h * 0.52)
    bot = (w / 2, h - inset)
    ml = (inset, h * 0.52)
    tl = (inset, h * 0.16 + inset * 0.6)
    pts += [top, tr, mr]
    for i in range(1, 21):  # curva direita
        t = i / 20
        x = (1 - t) ** 2 * mr[0] + 2 * (1 - t) * t * (w - inset) + t * t * bot[0]
        y = (1 - t) ** 2 * mr[1] + 2 * (1 - t) * t * (h * 0.82) + t * t * bot[1]
        pts.append((x, y))
    for i in range(1, 21):  # curva esquerda
        t = i / 20
        x = (1 - t) ** 2 * bot[0] + 2 * (1 - t) * t * inset + t * t * ml[0]
        y = (1 - t) ** 2 * bot[1] + 2 * (1 - t) * t * (h * 0.82) + t * t * ml[1]
        pts.append((x, y))
    pts.append(tl)
    return [(x + ox, y + oy) for x, y in pts]

def star(cx, cy, r):
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.42
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    return pts

def badge(size, background):
    S = size * 4  # supersampling
    img = Image.new('RGBA', (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    if background:
        pad = S * 0.09
        d.rounded_rectangle([pad, pad, S - pad, S - pad], radius=S * 0.2, fill=NAVY, outline=PANEL, width=int(S * 0.012))
        w = S * 0.56; h = w * 1.12; ox = (S - w) / 2; oy = (S - h) / 2 + S * 0.01
    else:
        w = S * 0.86; h = w * 1.12
        if h > S * 0.98:
            h = S * 0.98; w = h / 1.12
        ox = (S - w) / 2; oy = (S - h) / 2
    d.polygon(shield(w, h, 0, ox, oy), fill=GOLD)
    d.polygon(shield(w, h, w * 0.08, ox, oy), fill=NAVY)
    d.polygon(shield(w, h, w * 0.13, ox, oy), fill=GOLD)
    d.polygon(shield(w, h, w * 0.16, ox, oy), fill=NAVY)
    d.polygon(star(ox + w / 2, oy + h * 0.47, w * 0.24), fill=GOLD2)
    return img.resize((size, size), Image.LANCZOS)

win = os.path.join(ROOT, 'platform/windows/runner/resources/app_icon.ico')
big = badge(256, background=False)
big.save(win, sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
mac = os.path.join(ROOT, 'platform/macos/Runner/Assets.xcassets/AppIcon.appiconset')
for s in [16, 32, 64, 128, 256, 512, 1024]:
    badge(s, background=True).save(os.path.join(mac, f'app_icon_{s}.png'))
badge(512, background=True).save(os.path.join(ROOT, 'tool/icon/preview.png'))
print('ok')
