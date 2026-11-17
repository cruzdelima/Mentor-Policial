# -*- coding: utf-8 -*-
"""Gera a imagem "Como instalar o Mentor Policial" para enviar aos testadores.

uso: python3 tool/tutorial/make_tutorial.py [saída.png]
"""
import math
import os
import sys

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, 'tool', 'tutorial', 'Tutorial_Instalacao_Mentor_Policial.png')
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
    c.text(x + 114, y + 18, 'github.com/…/MentorPolicial-Setup.exe', B(15), fill=(90, 98, 112), anchor='lm')
    # painel de downloads
    px, py, pw = x + w - 380, y + 46, 360
    c.rect(px, py, pw, h - 58, fill=WHITE, r=10, outline=(210, 214, 222), width=2)
    c.text(px + 18, py + 14, 'Downloads', BB(18), fill=(40, 44, 52))
    c.rect(px + 14, py + 46, pw - 28, 58, fill=(236, 242, 252), r=8)
    c.rect(px + 26, py + 56, 38, 38, fill=GOLD, r=6)
    c.text(px + 45, py + 75, 'exe', HB(16), fill=NAVY, anchor='mm')
    c.text(px + 76, py + 58, 'MentorPolicial-Setup.exe', BB(17), fill=(30, 34, 40))
    c.text(px + 76, py + 81, 'Concluído · 20 MB', B(15), fill=(100, 106, 118))
    ring(c, px + 14, py + 46, pw - 28, 58)
    cursor(c, px + 250, py + 82)
    c.text(x + 24, y + 70, 'Abriu o link?', HB(26), fill=(40, 44, 52))
    c.text(x + 24, y + 102, 'O download começa', B(19), fill=(90, 98, 112))
    c.text(x + 24, y + 128, 'sozinho.', B(19), fill=(90, 98, 112))


def mock_keep(c, x, y, w, h):
    c.rect(x, y, w, h, fill=WHITE, r=12, outline=(210, 214, 222), width=2)
    c.circle(x + 34, y + 36, 14, fill=(245, 191, 79))
    c.text(x + 34, y + 36, '!', HB(22), fill=WHITE, anchor='mm')
    c.text(x + 60, y + 22, 'MentorPolicial-Setup.exe não é baixado com frequência', BM(17), fill=(40, 44, 52))
    c.text(x + 60, y + 48, 'Clique nos três pontinhos (…) ou na seta, se precisar.', B(15), fill=(110, 116, 128))
    bx, by = x + 60, y + 82
    c.rect(bx, by, 140, 40, fill=(0, 103, 192), r=6)
    c.text(bx + 70, by + 20, 'Manter', BB(18), fill=WHITE, anchor='mm')
    ring(c, bx, by, 140, 40)
    c.rect(bx + 160, by, 140, 40, fill=(240, 242, 246), r=6, outline=(200, 204, 212), width=1)
    c.text(bx + 230, by + 20, 'Excluir', BM(18), fill=(60, 64, 72), anchor='mm')
    c.text(bx + 330, by + 10, 'No Edge, pode aparecer', B(15), fill=(110, 116, 128))
    c.text(bx + 330, by + 30, '“Manter mesmo assim”.', BB(15), fill=(60, 64, 72))
    cursor(c, bx + 96, by + 24)


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
    c.text(x + 18, y + 20, 'Instalação — Mentor Policial', BM(16), fill=(40, 44, 52), anchor='lm')
    badge(c, x + 24, y + 58, 52)
    c.text(x + 96, y + 62, 'Instalação concluída', BB(22), fill=(30, 34, 40))
    c.text(x + 96, y + 94, 'O Mentor Policial foi instalado no seu computador.', B(16), fill=(90, 98, 112))
    c.rect(x + 96, y + 124, 22, 22, fill=(0, 103, 192), r=4)
    c.line([(x + 101, y + 135), (x + 106, y + 141), (x + 114, y + 129)], fill=WHITE, width=3)
    c.text(x + 128, y + 126, 'Abrir o Mentor Policial', B(17), fill=(40, 44, 52))
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
    c.text(ix + 40, iy + 88, 'Mentor', BM(15), fill=WHITE, anchor='mm')
    c.text(ix + 40, iy + 106, 'Policial', BM(15), fill=WHITE, anchor='mm')
    c.text(x + 270, y + 46, 'Para abrir de novo:', HB(26), fill=WHITE)
    c.text(x + 270, y + 82, 'atalho na Área de Trabalho', B(19), fill=(200, 216, 236))
    c.text(x + 270, y + 108, 'ou no menu Iniciar.', B(19), fill=(200, 216, 236))


# ------------------------------------------------------------------ montagem

def build():
    H = 3800
    c = Canvas(H)
    # faixa de isolamento
    c.rect(0, 0, W, 46, fill=GOLD2)
    t = 'MENTOR POLICIAL   //   VERSÃO DE TESTES   //   '
    x = -10
    while x < W:
        c.text(x, 23, t, HB(22), fill=NAVY, anchor='lm')
        x += c.width(t, HB(22))
    # cabeçalho
    badge(c, 56, 92, 110)
    c.text(196, 92, 'COMO INSTALAR O', HB(46), fill=GOLD2)
    c.text(196, 140, 'MENTOR POLICIAL', HB(72), fill=TEXT)
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
    y = step_card(c, y, 1, 'Abra o link no computador',
                  'Clique no **link de download** que você recebeu. O arquivo **MentorPolicial-Setup.exe** baixa sozinho. '
                  'Depois, clique nele na lista de downloads do navegador (ou abra a pasta **Downloads**).',
                  190, mock_download)
    y = step_card(c, y, 2, 'Se o navegador avisar, clique em Manter',
                  'Chrome e Edge às vezes dizem que o arquivo “não é baixado com frequência”. Isso acontece porque o app é **novo**. '
                  'Clique em **Manter**.',
                  140, mock_keep)
    y = step_card(c, y, 3, 'Tela azul? Mais informações › Executar assim mesmo',
                  'O Windows mostra esse aviso para programas novos, que ainda **não têm certificado digital**. '
                  'Clique em **Mais informações** e depois em **Executar assim mesmo**.',
                  250, mock_smartscreen)
    y = step_card(c, y, 4, 'Aguarde e clique em Concluir',
                  'A instalação é **automática**, sem perguntas e sem senha. No fim, clique em **Concluir**: o Mentor Policial abre sozinho.',
                  200, mock_installer)
    y = step_card(c, y, 5, 'Pronto!',
                  'Um atalho do **Mentor Policial** fica na Área de Trabalho. Na primeira vez, o app pergunta seu nome, o concurso e o cargo.',
                  170, mock_desktop)

    # Mac
    y += 6
    c.rect(48, y, 8, 40, fill=GOLD)
    c.text(72, y - 2, 'NO MAC', HB(44), fill=TEXT)
    y += 66
    mac = [
        ('Abra o link', 'Baixe o arquivo **MentorPolicial-macOS.dmg** e abra-o.'),
        ('Arraste para Aplicativos', 'Na janela que abrir, arraste o **Mentor Policial** para a pasta **Aplicativos**.'),
        ('Primeira vez: libere o app', 'Se o Mac disser que não pode verificar o app, clique em **OK**. Vá em **Ajustes do Sistema › Privacidade e Segurança**, '
                                       'role até o fim e clique em **Abrir Mesmo Assim**. Só é preciso fazer isso uma vez.'),
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
    c.text(W / 2, y, 'Dúvidas? Fale com quem te enviou o link.', BM(24), fill=MUTED, anchor='mm')
    y += 40
    img = c.img.crop((0, 0, W * S, int(y * S)))
    img = img.resize((W, int(y)), Image.LANCZOS)
    img.save(OUT, optimize=True)
    print(OUT, img.size)


if __name__ == '__main__':
    build()
