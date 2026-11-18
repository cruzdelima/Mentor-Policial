# -*- coding: utf-8 -*-
"""Gera a imagem "Como instalar o Taticum" para enviar aos testadores.

uso: python3 tool/tutorial/make_tutorial.py [saída.png]
"""
import math
import os
import sys

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, 'tool', 'tutorial', 'Tutorial_Instalacao_Taticum.png')
F = os.path.join(ROOT, 'assets', 'fonts')

S = 2  # renderiza em 2x e reduz (bordas mais suaves)
W = 1080
NAVY, NAVY2, PANEL, FIELD = (10, 18, 32), (17, 28, 48), (22, 36, 61), (26, 43, 72)
GOLD, GOLD2 = (224, 178, 58), (245, 200, 66)
TEXT, MUTED, DIM, LINE = (230, 237, 247), (142, 160, 188), (78, 95, 122), (35, 54, 90)
RED, GREEN, BLUE_WIN, WHITE = (248, 113, 113), (52, 211, 153), (0, 90, 158), (255, 255, 255)


def font(name, size):
    return ImageFont.truetype(os.path.join(F, name + '.ttf'), size * S)


HB = lambda s: font('BarlowCondensed-Bold', s)
HS = lambda s: font('BarlowCondensed-SemiBold', s)
B = lambda s: font('Barlow-Regular', s)
BM = lambda s: font('Barlow-Medium', s)
BB = lambda s: font('Barlow-Bold', s)


def words(s):
    """Divide em palavras; cada palavra é uma lista de trechos (texto, negrito)."""
    out, bold = [], False
    for raw in s.split(' '):
        if not raw:
            continue
        runs, parts = [], raw.split('**')
        for i, part in enumerate(parts):
            if i > 0:
                bold = not bold
            if part:
                runs.append((part, bold))
        if runs:
            out.append(runs)
    return out


class Canvas:
    def __init__(self, h):
        self.img = Image.new('RGB', (W * S, h * S), NAVY)
        self.d = ImageDraw.Draw(self.img)

    def rect(self, x, y, w, h, fill=None, r=0, outline=None, width=1):
        box = [x * S, y * S, (x + w) * S, (y + h) * S]
        if r:
            self.d.rounded_rectangle(box, radius=r * S, fill=fill, outline=outline, width=width * S)
        else:
            self.d.rectangle(box, fill=fill, outline=outline, width=width * S)

    def text(self, x, y, s, f, fill=TEXT, anchor='la'):
        self.d.text((x * S, y * S), s, font=f, fill=fill, anchor=anchor)

    def width(self, s, f):
        return self.d.textlength(s, font=f) / S

    def wrap(self, x, y, s, f, maxw, fill=TEXT, lh=None, bold_f=None, bold_fill=None):
        """Texto com quebra automática; trechos entre ** ficam em negrito (pontuação colada ao negrito)."""
        lh = lh or (f.size / S) * 1.42
        bf = bold_f or f
        space = self.width(' ', f)
        lines, line, cur = [], [], 0
        for word in words(s):
            ww = sum(self.width(t, bf if bold else f) for t, bold in word)
            if line and cur + ww > maxw:
                lines.append(line)
                line, cur = [], 0
            line.append(word)
            cur += ww + space
        if line:
            lines.append(line)
        for ln in lines:
            cx = x
            for word in ln:
                for t, bold in word:
                    ff = bf if bold else f
                    self.text(cx, y, t, ff, fill=(bold_fill or fill) if bold else fill)
                    cx += self.width(t, ff)
                cx += space
            y += lh
        return y

    def circle(self, cx, cy, r, fill=None, outline=None, width=1):
        self.d.ellipse([(cx - r) * S, (cy - r) * S, (cx + r) * S, (cy + r) * S], fill=fill, outline=outline, width=width * S)

    def poly(self, pts, fill):
        self.d.polygon([(x * S, y * S) for x, y in pts], fill=fill)

    def line(self, pts, fill, width=2):
        self.d.line([(x * S, y * S) for x, y in pts], fill=fill, width=width * S)


def badge(c, x, y, w):
    h = w * 1.12

    def shield(inset):
        pts = [(w / 2, inset), (w - inset, h * 0.16 + inset * 0.6), (w - inset, h * 0.52)]
        for i in range(1, 21):
            t = i / 20
            pts.append(((1 - t) ** 2 * (w - inset) + 2 * (1 - t) * t * (w - inset) + t * t * w / 2,
                        (1 - t) ** 2 * h * 0.52 + 2 * (1 - t) * t * h * 0.82 + t * t * (h - inset)))
        for i in range(1, 21):
            t = i / 20
            pts.append(((1 - t) ** 2 * w / 2 + 2 * (1 - t) * t * inset + t * t * inset,
                        (1 - t) ** 2 * (h - inset) + 2 * (1 - t) * t * h * 0.82 + t * t * h * 0.52))
        pts.append((inset, h * 0.16 + inset * 0.6))
        return [(x + px, y + py) for px, py in pts]

    c.poly(shield(0), GOLD)
    c.poly(shield(w * 0.08), NAVY)
    c.poly(shield(w * 0.13), GOLD)
    c.poly(shield(w * 0.16), NAVY)
    cx, cy, r = x + w / 2, y + h * 0.47, w * 0.24
    star = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.42
        star.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    c.poly(star, GOLD2)


def ring(c, x, y, w, h):
    """Destaque vermelho em volta do que deve ser clicado."""
    c.rect(x - 6, y - 6, w + 12, h + 12, r=10, outline=RED, width=4)


def cursor(c, x, y):
    pts = [(x, y), (x, y + 30), (x + 8, y + 23), (x + 14, y + 36), (x + 20, y + 33), (x + 14, y + 21), (x + 24, y + 21)]
    c.poly(pts, WHITE)
    c.line(pts + [pts[0]], fill=NAVY, width=2)


def step_card(c, y, n, title, body, mock_h, mock):
    x, w = 48, W - 96
    text_top = y + 26
    # altura do texto
    h_text = measure(c, body, B(24), w - 120, BB(24))
    h = 26 + 44 + h_text + (24 + mock_h if mock_h else 0) + 30
    c.rect(x, y, w, h, fill=NAVY2, r=22, outline=LINE, width=2)
    c.circle(x + 50, y + 54, 30, fill=GOLD)
    c.text(x + 50, y + 54, str(n), HB(38), fill=NAVY, anchor='mm')
    c.text(x + 96, text_top, title.upper(), HB(34), fill=TEXT)
    ty = c.wrap(x + 96, text_top + 48, body, B(24), w - 120, fill=MUTED, bold_f=BB(24), bold_fill=TEXT)
    if mock_h:
        mock(c, x + 96, ty + 12, w - 126, mock_h)
    return y + h + 22


def measure(c, s, f, maxw, bf):
    lh = (f.size / S) * 1.42
    space = c.width(' ', f)
    lines, cur = 1, 0
    for word in words(s):
        ww = sum(c.width(t, bf if bold else f) for t, bold in word)
        if cur and cur + ww > maxw:
            lines += 1
            cur = 0
        cur += ww + space
    return lines * lh


# ------------------------------------------------------------------ ilustrações

def mock_download(c, x, y, w, h):
    c.rect(x, y, w, h, fill=(242, 244, 248), r=12)
    c.rect(x, y, w, 34, fill=(222, 226, 234), r=12)
    c.rect(x, y + 20, w, 14, fill=(222, 226, 234))
    for i, col in enumerate([(237, 106, 94), (245, 191, 79), (98, 197, 84)]):
        c.circle(x + 22 + i * 22, y + 17, 7, fill=col)
    c.rect(x + 100, y + 8, w - 220, 20, fill=WHITE, r=10)
    c.text(x + 114, y + 18, 'github.com/…/Taticum-Setup.exe', B(15), fill=(90, 98, 112), anchor='lm')
    # painel de downloads
    px, py, pw = x + w - 380, y + 46, 360
    c.rect(px, py, pw, h - 58, fill=WHITE, r=10, outline=(210, 214, 222), width=2)
    c.text(px + 18, py + 14, 'Downloads', BB(18), fill=(40, 44, 52))
    c.rect(px + 14, py + 46, pw - 28, 58, fill=(236, 242, 252), r=8)
    c.rect(px + 26, py + 56, 38, 38, fill=GOLD, r=6)
    c.text(px + 45, py + 75, 'exe', HB(16), fill=NAVY, anchor='mm')
    c.text(px + 76, py + 58, 'Taticum-Setup.exe', BB(17), fill=(30, 34, 40))
    c.text(px + 76, py + 81, 'Concluído · 13 MB', B(15), fill=(100, 106, 118))
    ring(c, px + 14, py + 46, pw - 28, 58)
    cursor(c, px + 250, py + 82)
    c.text(x + 24, y + 70, 'Abriu o link?', HB(26), fill=(40, 44, 52))
    c.text(x + 24, y + 102, 'O download começa', B(19), fill=(90, 98, 112))
    c.text(x + 24, y + 128, 'sozinho.', B(19), fill=(90, 98, 112))


def num(c, x, y, n):
    c.circle(x, y, 16, fill=RED)
    c.text(x, y, str(n), HB(22), fill=WHITE, anchor='mm')


def mock_keep(c, x, y, w, h):
    # painel de downloads do Edge
    pw = 430
    c.rect(x, y, pw, h, fill=WHITE, r=12, outline=(210, 214, 222), width=2)
    c.text(x + 18, y + 14, 'Downloads', BB(18), fill=(40, 44, 52))
    c.rect(x + 14, y + 48, pw - 28, 92, fill=(255, 248, 230), r=8)
    c.circle(x + 40, y + 72, 12, fill=(245, 191, 79))
    c.text(x + 40, y + 72, '!', HB(18), fill=WHITE, anchor='mm')
    c.text(x + 60, y + 60, 'Taticum-Setup.exe não é baixado', BM(15), fill=(40, 44, 52))
    c.text(x + 60, y + 80, 'com frequência. Verifique se você', B(14), fill=(100, 106, 118))
    c.text(x + 60, y + 99, 'confia nele antes de abri-lo.', B(14), fill=(100, 106, 118))
    dx, dy = x + pw - 50, y + 58
    c.rect(dx - 4, dy, 30, 26, fill=(236, 238, 242), r=5)
    c.text(dx + 11, dy + 10, '…', BB(20), fill=(40, 44, 52), anchor='mm')
    ring(c, dx - 4, dy, 30, 26)
    num(c, dx + 11, dy - 22, 1)
    # menu aberto
    mx, my = x + pw - 190, y + 150
    c.rect(mx, my, 176, 96, fill=WHITE, r=8, outline=(200, 204, 212), width=2)
    c.rect(mx + 6, my + 8, 164, 36, fill=(232, 240, 252), r=6)
    c.text(mx + 20, my + 26, 'Manter', BM(17), fill=(30, 34, 40), anchor='lm')
    ring(c, mx + 6, my + 8, 164, 36)
    num(c, mx - 22, my + 26, 2)
    c.text(mx + 20, my + 70, 'Excluir', B(16), fill=(110, 116, 128), anchor='lm')
    # janela de confirmação
    bx, bw = x + pw + 30, w - pw - 30
    c.rect(bx, y, bw, h, fill=WHITE, r=12, outline=(210, 214, 222), width=2)
    c.text(bx + 20, y + 18, 'Verifique se você confia em', BB(17), fill=(30, 34, 40))
    c.text(bx + 20, y + 40, 'Taticum-Setup.exe antes de abri-lo', BB(17), fill=(30, 34, 40))
    c.text(bx + 20, y + 74, 'O Microsoft Defender SmartScreen não', B(14), fill=(100, 106, 118))
    c.text(bx + 20, y + 92, 'conseguiu verificar se é seguro.', B(14), fill=(100, 106, 118))
    c.text(bx + 20, y + 126, 'Mostrar mais', BM(16), fill=(0, 103, 192))
    ring(c, bx + 20, y + 124, c.width('Mostrar mais', BM(16)), 22)
    num(c, bx + 20 + c.width('Mostrar mais', BM(16)) + 28, y + 136, 3)
    c.rect(bx + 20, y + 172, 200, 38, fill=(240, 242, 246), r=6, outline=(200, 204, 212), width=1)
    c.text(bx + 120, y + 191, 'Manter mesmo assim', BM(16), fill=(30, 34, 40), anchor='mm')
    ring(c, bx + 20, y + 172, 200, 38)
    num(c, bx + 248, y + 191, 4)
    cursor(c, bx + 150, y + 194)


def mock_smartscreen(c, x, y, w, h):
    c.rect(x, y, w, h, fill=BLUE_WIN, r=10)
    c.text(x + 30, y + 26, 'O Windows protegeu o computador', B(30), fill=WHITE)
    c.text(x + 30, y + 78, 'O Microsoft Defender SmartScreen impediu que um aplicativo', B(16), fill=(214, 228, 240))
    c.text(x + 30, y + 100, 'não reconhecido fosse iniciado.', B(16), fill=(214, 228, 240))
    c.text(x + 30, y + 136, 'Mais informações', BB(18), fill=WHITE)
    c.line([(x + 30, y + 160), (x + 30 + c.width('Mais informações', BB(18)), y + 160)], fill=WHITE, width=2)
    ring(c, x + 30, y + 132, c.width('Mais informações', BB(18)), 32)
    c.circle(x + 30 + c.width('Mais informações', BB(18)) + 34, y + 148, 18, fill=RED)
    c.text(x + 30 + c.width('Mais informações', BB(18)) + 34, y + 148, '1', HB(24), fill=WHITE, anchor='mm')
    # depois de clicar
    bx, by = x + w - 420, y + h - 66
    c.rect(bx, by, 190, 44, fill=(0, 72, 128), r=4, outline=WHITE, width=2)
    c.text(bx + 95, by + 22, 'Executar assim mesmo', BM(16), fill=WHITE, anchor='mm')
    ring(c, bx, by, 190, 44)
    c.circle(bx - 26, by + 22, 18, fill=RED)
    c.text(bx - 26, by + 22, '2', HB(24), fill=WHITE, anchor='mm')
    c.rect(bx + 206, by, 190, 44, fill=(0, 72, 128), r=4, outline=(120, 160, 200), width=1)
    c.text(bx + 301, by + 22, 'Não executar', BM(16), fill=(200, 214, 228), anchor='mm')
    cursor(c, bx + 120, by + 26)


def mock_installer(c, x, y, w, h):
    c.rect(x, y, w, h, fill=(246, 247, 250), r=10, outline=(200, 204, 212), width=2)
    c.rect(x, y, w, 40, fill=WHITE, r=10)
    c.rect(x, y + 28, w, 12, fill=WHITE)
    c.text(x + 18, y + 20, 'Instalação — Taticum', BM(16), fill=(40, 44, 52), anchor='lm')
    badge(c, x + 24, y + 58, 52)
    c.text(x + 96, y + 62, 'Instalação concluída', BB(22), fill=(30, 34, 40))
    c.text(x + 96, y + 94, 'O Taticum foi instalado no seu computador.', B(16), fill=(90, 98, 112))
    c.rect(x + 96, y + 124, 22, 22, fill=(0, 103, 192), r=4)
    c.line([(x + 101, y + 135), (x + 106, y + 141), (x + 114, y + 129)], fill=WHITE, width=3)
    c.text(x + 128, y + 126, 'Abrir o Taticum', B(17), fill=(40, 44, 52))
    bx, by = x + w - 170, y + h - 58
    c.rect(bx, by, 140, 40, fill=(0, 103, 192), r=4)
    c.text(bx + 70, by + 20, 'Concluir', BB(18), fill=WHITE, anchor='mm')
    ring(c, bx, by, 140, 40)
    cursor(c, bx + 90, by + 24)


def mock_desktop(c, x, y, w, h):
    c.rect(x, y, w, h, fill=(20, 60, 110), r=10)
    for i in range(3):
        c.rect(x + 26, y + 20 + i * 54, 40, 34, fill=(70, 110, 160), r=4)
    ix, iy = x + 120, y + 26
    c.rect(ix - 14, iy - 10, 108, 128, fill=(40, 84, 136), r=8, outline=GOLD, width=3)
    c.rect(ix + 4, iy, 72, 72, fill=NAVY, r=14)
    badge(c, ix + 16, iy + 6, 48)
    c.text(ix + 40, iy + 96, 'Taticum', BM(16), fill=WHITE, anchor='mm')
    c.text(x + 270, y + 46, 'Para abrir de novo:', HB(26), fill=WHITE)
    c.text(x + 270, y + 82, 'atalho na Área de Trabalho', B(19), fill=(200, 216, 236))
    c.text(x + 270, y + 108, 'ou no menu Iniciar.', B(19), fill=(200, 216, 236))


def app_frame(c, x, y, w, h):
    c.rect(x, y, w, h, fill=(14, 23, 40), r=12, outline=LINE, width=2)
    badge(c, x + 22, y + 18, 30)
    c.text(x + 64, y + 18, 'TATICUM', HB(22), fill=GOLD2)
    c.text(x + 64, y + 40, 'MENTOR POLICIAL', HS(12), fill=MUTED)


def field(c, x, y, w, label, value):
    c.text(x, y, label, BM(13), fill=MUTED)
    c.rect(x, y + 20, w, 34, fill=FIELD, r=6, outline=LINE, width=1)
    c.text(x + 12, y + 37, value, B(15), fill=TEXT, anchor='lm')


def gold_button(c, x, y, w, label):
    c.rect(x, y, w, 40, fill=GOLD, r=6)
    c.text(x + w / 2, y + 20, label, HB(20), fill=NAVY, anchor='mm')
    ring(c, x, y, w, 40)


def mock_signup(c, x, y, w, h):
    app_frame(c, x, y, w, h)
    fx, fw = x + 30, (w - 80) / 2
    c.text(fx, y + 74, 'GRATUITO DURANTE OS TESTES', HS(14), fill=GOLD)
    c.text(fx, y + 92, 'CRIAR CONTA', HB(28), fill=TEXT)
    field(c, fx, y + 132, fw, 'Nome', 'Maria Souza')
    field(c, fx + fw + 20, y + 132, fw, 'E-mail (o mesmo do convite)', 'maria@email.com')
    field(c, fx, y + 196, fw, 'Celular', '(81) 99999-0000')
    field(c, fx + fw + 20, y + 196, fw, 'Senha (e repetir a senha)', '••••••••')
    c.rect(fx, y + 266, 20, 20, fill=GOLD, r=4)
    c.line([(fx + 4, y + 276), (fx + 9, y + 281), (fx + 16, y + 270)], fill=NAVY, width=3)
    c.text(fx + 30, y + 276, 'Li e aceito os Termos de Uso e a Política de Privacidade.', B(14), fill=TEXT, anchor='lm')
    gold_button(c, fx, y + 304, w - 60, 'CRIAR CONTA')
    cursor(c, fx + (w - 60) / 2 + 40, y + 326)


def mock_code(c, x, y, w, h):
    app_frame(c, x, y, w, h)
    fx = x + 30
    c.text(fx, y + 74, 'ÚLTIMO PASSO', HS(14), fill=GOLD)
    c.text(fx, y + 92, 'CONFIRME SEU E-MAIL', HB(28), fill=TEXT)
    c.text(fx, y + 128, 'Digite o código enviado para maria@email.com.', B(15), fill=MUTED)
    for i, d in enumerate('482916'):
        bx = fx + i * 56
        c.rect(bx, y + 158, 46, 52, fill=FIELD, r=8, outline=GOLD if i < 6 else LINE, width=2)
        c.text(bx + 23, y + 184, d, HB(30), fill=TEXT, anchor='mm')
    gold_button(c, fx, y + 228, 326, 'CONFIRMAR')
    cursor(c, fx + 200, y + 250)
    # e-mail ao lado
    ex, ew = fx + 380, w - 410
    c.rect(ex, y + 74, ew, 196, fill=WHITE, r=10)
    c.rect(ex, y + 74, ew, 40, fill=(10, 18, 32), r=10)
    c.rect(ex, y + 100, ew, 14, fill=(10, 18, 32))
    c.text(ex + 16, y + 94, 'TATICUM', HB(18), fill=GOLD2, anchor='lm')
    c.text(ex + 16, y + 128, 'Seu código de acesso', BB(16), fill=(30, 34, 40))
    c.text(ex + 16, y + 168, '482916', HB(40), fill=(30, 34, 40))
    c.text(ex + 16, y + 222, 'Chega em 1 minuto. Veja também', B(13), fill=(100, 106, 118))
    c.text(ex + 16, y + 240, 'a caixa de spam.', B(13), fill=(100, 106, 118))


def mock_onboarding(c, x, y, w, h):
    app_frame(c, x, y, w, h)
    fx = x + 30
    steps = ['Esfera', 'Concurso', 'Cargo', 'Rotina', 'Plano']
    for i, t in enumerate(steps):
        cx = fx + 16 + i * ((w - 92) / 4)
        if i:
            c.line([(cx - (w - 92) / 4 + 18, y + 96), (cx - 18, y + 96)], fill=GOLD if i < 3 else LINE, width=2)
        c.circle(cx, y + 96, 16, fill=GOLD if i < 2 else (FIELD if i > 2 else NAVY), outline=GOLD if i <= 2 else LINE, width=2)
        c.text(cx, y + 96, str(i + 1), HB(18), fill=NAVY if i < 2 else (GOLD2 if i == 2 else MUTED), anchor='mm')
        c.text(cx, y + 126, t, BM(13), fill=TEXT if i <= 2 else MUTED, anchor='mm')
    c.text(fx, y + 150, 'PASSO 3', HS(14), fill=GOLD)
    c.text(fx, y + 168, 'QUAL CARGO?', HB(28), fill=TEXT)
    for i, (t, sel) in enumerate([('Agente de Polícia Federal', True), ('Escrivão de Polícia Federal', False)]):
        by = y + 206 + i * 46
        c.rect(fx, by, w - 60, 38, fill=PANEL if sel else FIELD, r=8, outline=GOLD if sel else LINE, width=2)
        c.circle(fx + 22, by + 19, 8, fill=GOLD if sel else None, outline=GOLD if sel else MUTED, width=2)
        c.text(fx + 42, by + 19, t, BM(15), fill=TEXT, anchor='lm')


# ------------------------------------------------------------------ montagem

def build():
    H = 5200
    c = Canvas(H)
    # faixa de isolamento
    c.rect(0, 0, W, 46, fill=GOLD2)
    t = 'TATICUM   //   VERSÃO DE TESTES   //   '
    x = -10
    while x < W:
        c.text(x, 23, t, HB(22), fill=NAVY, anchor='lm')
        x += c.width(t, HB(22))
    # cabeçalho
    badge(c, 56, 92, 110)
    c.text(196, 92, 'COMO INSTALAR O', HB(46), fill=GOLD2)
    c.text(196, 140, 'TATICUM', HB(72), fill=TEXT)
    c.text(198, 222, 'Grátis  ·  leva uns 2 minutos  ·  só uma vez', BM(24), fill=MUTED)
    c.rect(56, 284, W - 112, 64, fill=PANEL, r=14, outline=GOLD, width=2)
    c.text(84, 316, 'É um programa para', B(24), fill=TEXT, anchor='lm')
    c.text(84 + c.width('É um programa para ', B(24)), 316, 'COMPUTADOR', HB(30), fill=GOLD2, anchor='lm')
    c.text(84 + c.width('É um programa para ', B(24)) + c.width('COMPUTADOR ', HB(30)), 316,
           '(Windows ou Mac). Não é app de celular.', B(24), fill=TEXT, anchor='lm')

    y = 384
    c.rect(48, y, 8, 40, fill=GOLD)
    c.text(72, y - 2, 'NO WINDOWS', HB(44), fill=TEXT)
    y += 66
    y = step_card(c, y, 1, 'Baixe o instalador',
                  'No **e-mail de convite**, clique em **BAIXAR PARA WINDOWS**. O arquivo **Taticum-Setup.exe** baixa sozinho. '
                  'Depois, clique nele na lista de downloads do navegador (ou abra a pasta **Downloads**).',
                  190, mock_download)
    y = step_card(c, y, 2, 'O navegador avisou? Clique em Manter',
                  'Como o app é **novo**, o Edge diz que o arquivo “não é baixado com frequência”. Siga os números: '
                  '**…** › **Manter** › **Mostrar mais** › **Manter mesmo assim**. No Chrome, basta clicar em **Manter**.',
                  250, mock_keep)
    y = step_card(c, y, 3, 'Tela azul? Mais informações › Executar assim mesmo',
                  'O Windows mostra esse aviso para programas novos, que ainda **não têm certificado digital**. '
                  'Clique em **Mais informações** e depois em **Executar assim mesmo**.',
                  250, mock_smartscreen)
    y = step_card(c, y, 4, 'Aguarde e clique em Concluir',
                  'A instalação é **automática**, sem perguntas e sem senha. No fim, clique em **Concluir**: o Taticum abre sozinho. '
                  'Um atalho fica na **Área de Trabalho**.',
                  200, mock_installer)
    y = step_card(c, y, 5, 'Crie sua conta',
                  'Na tela de entrada, clique em **CRIAR CONTA**. Use o **mesmo e-mail que recebeu o convite**, preencha nome, celular e senha, '
                  'aceite os termos e clique em **CRIAR CONTA**.',
                  360, mock_signup)
    y = step_card(c, y, 6, 'Confirme com o código do e-mail',
                  'Chega no seu e-mail um **código de 6 dígitos**. Digite no app e clique em **CONFIRMAR**. '
                  'Não chegou? Olhe o **spam** ou clique em **REENVIAR CÓDIGO**.',
                  290, mock_code)
    y = step_card(c, y, 7, 'Monte seu plano',
                  'Escolha a **esfera**, o **concurso**, o **cargo** e quantas **horas por dia** você tem. '
                  'O Taticum monta o cronograma na hora, e tudo pode ser mudado depois em **AJUSTES**.',
                  320, mock_onboarding)

    # Mac
    y += 6
    c.rect(48, y, 8, 40, fill=GOLD)
    c.text(72, y - 2, 'NO MAC', HB(44), fill=TEXT)
    y += 66
    mac = [
        ('Baixe o instalador', 'No e-mail de convite, clique em **BAIXAR PARA MAC** e abra o arquivo **Taticum-macOS.dmg**.'),
        ('Arraste para Aplicativos', 'Na janela que abrir, arraste o **Taticum** para a pasta **Aplicativos**.'),
        ('Primeira vez: libere o app', 'Se o Mac disser que não pode verificar o app, clique em **OK**. Vá em **Ajustes do Sistema › Privacidade e Segurança**, '
                                       'role até o fim e clique em **Abrir Mesmo Assim**. Só é preciso fazer isso uma vez.'),
        ('Crie a conta e monte o plano', 'Siga os passos **5, 6 e 7** do Windows: são iguais no Mac.'),
    ]
    hh = 28
    for t_, b_ in mac:
        hh += 40 + measure(c, b_, B(23), W - 96 - 130, BB(23)) + 18
    c.rect(48, y, W - 96, hh, fill=NAVY2, r=22, outline=LINE, width=2)
    yy = y + 28
    for i, (t_, b_) in enumerate(mac, start=1):
        c.circle(98, yy + 20, 24, fill=GOLD)
        c.text(98, yy + 20, str(i), HB(30), fill=NAVY, anchor='mm')
        c.text(144, yy, t_.upper(), HB(30), fill=TEXT)
        yy = c.wrap(144, yy + 40, b_, B(23), W - 96 - 130, fill=MUTED, bold_f=BB(23), bold_fill=TEXT) + 18
    y += hh + 30

    # rodapé
    c.rect(48, y, W - 96, 170, fill=PANEL, r=22, outline=GOLD, width=2)
    c.text(80, y + 26, 'ATUALIZAÇÕES', HB(32), fill=GOLD2)
    c.wrap(80, y + 70, 'Quando sair uma versão nova, o app mostra uma **faixa amarela** com o botão **BAIXAR ATUALIZAÇÃO**. '
                       'É só instalar por cima: seu cronograma, seu diário e suas questões **continuam salvos**.',
           B(23), W - 160, fill=MUTED, bold_f=BB(23), bold_fill=TEXT)
    y += 200
    c.rect(48, y, W - 96, 150, fill=NAVY2, r=22, outline=LINE, width=2)
    c.text(80, y + 24, 'O APP DISSE QUE A CONTA JÁ EXISTE?', HB(30), fill=TEXT)
    c.wrap(80, y + 64, 'Clique em **ENTRAR** › **ESQUECI MINHA SENHA** e use o mesmo e-mail. Você recebe um código para criar a senha.',
           B(23), W - 160, fill=MUTED, bold_f=BB(23), bold_fill=TEXT)
    y += 180
    c.text(W / 2, y, 'Dúvidas? Fale com quem te enviou o convite.', BM(24), fill=MUTED, anchor='mm')
    y += 40
    img = c.img.crop((0, 0, W * S, int(y * S)))
    img = img.resize((W, int(y)), Image.LANCZOS)
    img.save(OUT, optimize=True)
    print(OUT, img.size)


if __name__ == '__main__':
    build()
