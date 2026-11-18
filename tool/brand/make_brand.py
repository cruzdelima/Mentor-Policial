# Gera a identidade visual do Taticum em PNG: logomarca (fundo escuro, fundo claro e símbolo),
# foto de perfil e banner de e-mail. Mesmo escudo dos ícones do app (tool/icon/make_icons.py).
# uso: python3 tool/brand/make_brand.py <pasta do projeto> <pasta de saída>
import os, sys
from PIL import Image, ImageDraw, ImageFont

ROOT = sys.argv[1] if len(sys.argv) > 1 else '.'
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(ROOT, 'docs', 'brand')
sys.path.insert(0, os.path.join(ROOT, 'tool', 'icon'))
os.makedirs(OUT, exist_ok=True)

NAVY = (10, 18, 32, 255); SIDEBAR = (6, 11, 21, 255); PANEL = (17, 28, 48, 255); LINE = (23, 36, 59, 255)
GOLD = (224, 178, 58, 255); GOLD2 = (245, 200, 66, 255); TEXT = (230, 237, 247, 255); MUTED = (142, 160, 188, 255)
FONTS = os.path.join(ROOT, 'assets', 'fonts')


def font(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name + '.ttf'), size)


def shield_pts(w, h, inset, ox, oy):
    top = (w / 2, inset); tr = (w - inset, h * 0.16 + inset * 0.6); mr = (w - inset, h * 0.52)
    bot = (w / 2, h - inset); ml = (inset, h * 0.52); tl = (inset, h * 0.16 + inset * 0.6)
    pts = [top, tr, mr]
    for i in range(1, 41):
        t = i / 40
        pts.append(((1 - t) ** 2 * mr[0] + 2 * (1 - t) * t * (w - inset) + t * t * bot[0],
                    (1 - t) ** 2 * mr[1] + 2 * (1 - t) * t * (h * 0.82) + t * t * bot[1]))
    for i in range(1, 41):
        t = i / 40
        pts.append(((1 - t) ** 2 * bot[0] + 2 * (1 - t) * t * inset + t * t * ml[0],
                    (1 - t) ** 2 * bot[1] + 2 * (1 - t) * t * (h * 0.82) + t * t * ml[1]))
    pts.append(tl)
    return [(x + ox, y + oy) for x, y in pts]


def star_pts(cx, cy, r):
    import math
    return [(cx + (r if i % 2 == 0 else r * 0.42) * math.cos(-math.pi / 2 + i * math.pi / 5),
             cy + (r if i % 2 == 0 else r * 0.42) * math.sin(-math.pi / 2 + i * math.pi / 5)) for i in range(10)]


def draw_badge(d, ox, oy, w, inner=NAVY):
    h = w * 1.12
    d.polygon(shield_pts(w, h, 0, ox, oy), fill=GOLD)
    d.polygon(shield_pts(w, h, w * 0.08, ox, oy), fill=inner)
    d.polygon(shield_pts(w, h, w * 0.13, ox, oy), fill=GOLD)
    d.polygon(shield_pts(w, h, w * 0.16, ox, oy), fill=inner)
    d.polygon(star_pts(ox + w / 2, oy + h * 0.47, w * 0.24), fill=GOLD2)
    return h


def grid(img, step, color=(120, 150, 200, 22)):
    """Quadriculado discreto (mesma textura das capas dos PDFs), mesclado por transparência."""
    W, H = img.size
    layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    g = ImageDraw.Draw(layer)
    for x in range(0, W, step):
        g.line([(x, 0), (x, H)], fill=color, width=max(1, step // 60))
    for y in range(0, H, step):
        g.line([(0, y), (W, y)], fill=color, width=max(1, step // 60))
    img.alpha_composite(layer)


def tape(d, W, y, h, text='TATICUM   //   MENTOR POLICIAL   //   '):
    d.rectangle([0, y, W, y + h], fill=GOLD2)
    f = font('BarlowCondensed-Bold', int(h * 0.52))
    x = -h
    while x < W:
        d.text((x, y + h / 2), text, font=f, fill=NAVY, anchor='lm')
        x += d.textlength(text, font=f)


def finish(img, scale, name):
    img = img.resize((img.width // scale, img.height // scale), Image.LANCZOS)
    path = os.path.join(OUT, name)
    img.save(path, optimize=True)
    print('ok', name, img.size)
    return path


def lockup(dark):
    """Logomarca horizontal com fundo transparente: escudo + TATICUM + MENTOR POLICIAL."""
    S = 4
    W, H = 1600 * S, 520 * S
    img = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    bw = 340 * S
    draw_badge(d, 60 * S, (H - bw * 1.12) / 2, bw)
    x = 60 * S + bw + 70 * S
    d.text((x, 250 * S), 'TATICUM', font=font('BarlowCondensed-Bold', 300 * S), fill=GOLD2 if dark else NAVY, anchor='ls')
    f2 = font('BarlowCondensed-SemiBold', 82 * S)
    sub = 'MENTOR POLICIAL'
    xx = x + 8 * S
    for ch in sub:  # espaçamento entre letras
        d.text((xx, 375 * S), ch, font=f2, fill=MUTED if dark else GOLD, anchor='ls')
        xx += d.textlength(ch, font=f2) + 20 * S
    bbox = img.getbbox()
    img = img.crop((bbox[0] - 20 * S, bbox[1] - 20 * S, bbox[2] + 20 * S, bbox[3] + 20 * S))
    return finish(img, S, 'logo_taticum_fundo_escuro.png' if dark else 'logo_taticum_fundo_claro.png')


def symbol():
    S = 4
    W = 1024 * S
    img = Image.new('RGBA', (W, W), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    bw = 820 * S
    draw_badge(d, (W - bw) / 2, (W - bw * 1.12) / 2, bw)
    return finish(img, S, 'simbolo_taticum.png')


def profile():
    S = 3
    W = 1080 * S
    img = Image.new('RGBA', (W, W), NAVY)
    grid(img, 90 * S)
    d = ImageDraw.Draw(img)
    # tudo dentro do círculo central (as redes recortam a foto em círculo)
    bw = 430 * S
    bh = bw * 1.12
    top = 185 * S
    draw_badge(d, (W - bw) / 2, top, bw)
    d.text((W / 2, top + bh + 175 * S), 'TATICUM', font=font('BarlowCondensed-Bold', 190 * S), fill=GOLD2, anchor='ms')
    return finish(img.convert('RGB'), S, 'foto_perfil_taticum.png')


def email_banner():
    S = 3
    W, H = 1200 * S, 400 * S
    img = Image.new('RGBA', (W, H), NAVY)
    grid(img, 60 * S)
    d = ImageDraw.Draw(img)
    tape(d, W, 0, 34 * S)
    bw = 200 * S
    by = 34 * S + (H - 34 * S - bw * 1.12) / 2
    draw_badge(d, 90 * S, by, bw)
    x = 90 * S + bw + 56 * S
    d.text((x, 205 * S), 'TATICUM', font=font('BarlowCondensed-Bold', 150 * S), fill=GOLD2, anchor='ls')
    f2 = font('BarlowCondensed-SemiBold', 40 * S)
    xx = x + 4 * S
    for ch in 'MENTOR POLICIAL':
        d.text((xx, 262 * S), ch, font=f2, fill=TEXT, anchor='ls')
        xx += d.textlength(ch, font=f2) + 10 * S
    d.line([(x + 4 * S, 290 * S), (x + 120 * S, 290 * S)], fill=GOLD, width=4 * S)
    d.text((x + 4 * S, 338 * S), 'Seu plano de estudos para a área policial', font=font('Barlow-Medium', 30 * S), fill=MUTED, anchor='ls')
    return finish(img.convert('RGB'), S, 'banner_email_taticum.png')


def msix_assets():
    """Imagens do pacote da Microsoft Store (tamanhos exatos pedidos pelo manifesto)."""
    out = os.path.join(ROOT, 'platform', 'windows', 'msix', 'Assets')
    os.makedirs(out, exist_ok=True)

    def tile(w, h, badge_h, bg, name):
        S = 8
        img = Image.new('RGBA', (w * S, h * S), bg)
        d = ImageDraw.Draw(img)
        bw = badge_h * S / 1.12
        draw_badge(d, (w * S - bw) / 2, (h * S - badge_h * S) / 2, bw)
        img.resize((w, h), Image.LANCZOS).save(os.path.join(out, name), optimize=True)
        print('ok msix', name, (w, h))

    clear = (0, 0, 0, 0)
    tile(50, 50, 46, clear, 'StoreLogo.png')
    tile(44, 44, 42, clear, 'Square44x44Logo.png')
    tile(150, 150, 96, NAVY, 'Square150x150Logo.png')
    tile(310, 150, 96, NAVY, 'Wide310x150Logo.png')


if __name__ == '__main__':
    if len(sys.argv) > 3 and sys.argv[3] == 'msix':
        msix_assets()
        sys.exit(0)
    lockup(True)
    lockup(False)
    symbol()
    profile()
    email_banner()
