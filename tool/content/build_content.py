# -*- coding: utf-8 -*-
"""Gera os conteúdos (JSON do app + PDF) a partir dos módulos-fonte desta pasta.

Cada assunto tem dois materiais:
  * aprofundado — estudo inicial, teoria completa + 20 questões;
  * resumo      — revisão, direto ao ponto + quadro + mapa mental + 10 questões.

uso: python3 build_content.py [pasta do projeto flutter] [pasta extra para cópia dos PDFs]
"""
import importlib
import bancas
import json
import os
import re
import shutil
import sys

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Flowable, Frame, KeepTogether, NextPageTemplate, PageBreak, PageTemplate,
                                Paragraph, Spacer, Table, TableStyle)

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

# Ordem = ordem na biblioteca do app.
MODULES = [
    'lp_ortografia_aprof', 'lp_ortografia_resumo',
    'lp_acentuacao_aprof', 'lp_acentuacao_resumo',
    'lp_classes1_aprof', 'lp_classes1_resumo',
    'lp_pronomes_aprof', 'lp_pronomes_resumo',
    'lp_interpretacao_aprof', 'lp_interpretacao_resumo',
    'lp_verbos_aprof', 'lp_verbos_resumo',
    'lp_conectivos_aprof', 'lp_conectivos_resumo',
    'lp_termos_aprof', 'lp_termos_resumo',
    'lp_coordenadas_aprof', 'lp_coordenadas_resumo',
    'lp_subordinadas_aprof', 'lp_subordinadas_resumo',
    'lp_concordancia_aprof', 'lp_concordancia_resumo',
    'lp_regencia_aprof', 'lp_regencia_resumo',
    'lp_crase_aprof', 'lp_crase_resumo',
    'lp_pontuacao_aprof', 'lp_pontuacao_resumo',
    'lp_tipologia_aprof', 'lp_tipologia_resumo',
    'lp_coesao_aprof', 'lp_coesao_resumo',
    'lp_reescrita_aprof', 'lp_reescrita_resumo',
    'lp_formacao_aprof', 'lp_formacao_resumo',
    'lp_semantica_aprof', 'lp_semantica_resumo',
    'lp_redacao_oficial_aprof', 'lp_redacao_oficial_resumo',
    'lp_figuras_aprof', 'lp_figuras_resumo',
    'lp_relacoes_aprof', 'lp_relacoes_resumo',
    'lp_que_se_aprof', 'lp_que_se_resumo',
    'lp_variacao_aprof', 'lp_variacao_resumo',
    'info_virus_aprof', 'info_virus_resumo',
    'cont_conceitos_aprof', 'cont_conceitos_resumo',
    'dc_principios_aprof', 'dc_principios_resumo',
    'dc_direitos_aprof', 'dc_direitos_resumo',
    'dc_remedios_aprof', 'dc_remedios_resumo',
    'dc_sociais_aprof', 'dc_sociais_resumo',
    'dc_nacionalidade_aprof', 'dc_nacionalidade_resumo',
    'dc_politicos_aprof', 'dc_politicos_resumo',
    'dc_organizacao_aprof', 'dc_organizacao_resumo',
    'dc_administracao_aprof', 'dc_administracao_resumo',
    'dc_legislativo_aprof', 'dc_legislativo_resumo',
    'dc_executivo_aprof', 'dc_executivo_resumo',
    'dc_judiciario_aprof', 'dc_judiciario_resumo',
    'dc_defesa_aprof', 'dc_defesa_resumo',
    'dc_seguranca_aprof', 'dc_seguranca_resumo',
    'rlm_proposicoes_aprof', 'rlm_proposicoes_resumo',
    'rlm_tabela_aprof', 'rlm_tabela_resumo',
    'rlm_equivalencias_aprof', 'rlm_equivalencias_resumo',
    'rlm_negacao_aprof', 'rlm_negacao_resumo',
    'rlm_argumentacao_aprof', 'rlm_argumentacao_resumo',
    'rlm_quantificadores_aprof', 'rlm_quantificadores_resumo',
    'rlm_conjuntos_aprof', 'rlm_conjuntos_resumo',
    'rlm_proporcao_aprof', 'rlm_proporcao_resumo',
    'rlm_problemas_aprof', 'rlm_problemas_resumo',
    'rlm_sequencias_aprof', 'rlm_sequencias_resumo',
    'rlm_contagem_aprof', 'rlm_contagem_resumo',
    'rlm_probabilidade_aprof', 'rlm_probabilidade_resumo',
    'rlm_funcoes_aprof', 'rlm_funcoes_resumo',
    'rlm_geometria_aprof', 'rlm_geometria_resumo',
]

PROJ = sys.argv[1] if len(sys.argv) > 1 else os.path.abspath(os.path.join(HERE, '..', '..'))
EXTRA = sys.argv[2] if len(sys.argv) > 2 else None
FONTS = os.path.join(PROJ, 'assets', 'fonts')

for name, file in [('B', 'Barlow-Regular'), ('B-M', 'Barlow-Medium'), ('B-SB', 'Barlow-SemiBold'), ('B-B', 'Barlow-Bold'),
                   ('BC-SB', 'BarlowCondensed-SemiBold'), ('BC-B', 'BarlowCondensed-Bold'), ('BC-M', 'BarlowCondensed-Medium')]:
    pdfmetrics.registerFont(TTFont(name, os.path.join(FONTS, file + '.ttf')))
pdfmetrics.registerFontFamily('B', normal='B', bold='B-B', italic='B', boldItalic='B-B')
# Símbolos que a Barlow não tem (∧ ∨ → ↔ ∈ ∪ ∩ …) saem na DejaVu Sans, só onde aparecem.
SYM_DIR = os.path.join(HERE, 'fonts')
pdfmetrics.registerFont(TTFont('Sym', os.path.join(SYM_DIR, 'DejaVuSans.ttf')))
pdfmetrics.registerFont(TTFont('Sym-B', os.path.join(SYM_DIR, 'DejaVuSans-Bold.ttf')))
pdfmetrics.registerFontFamily('Sym', normal='Sym', bold='Sym-B', italic='Sym', boldItalic='Sym-B')
from fontTools.ttLib import TTFont as _FT
_BARLOW = set(_FT(os.path.join(FONTS, 'Barlow-Regular.ttf')).getBestCmap())
_SYMSET = set(_FT(os.path.join(SYM_DIR, 'DejaVuSans.ttf')).getBestCmap())
_SYMRUN = re.compile('([^\x00-\x7f]+)')


def _sym(t):
    def rep(m):
        out, buf = [], ''
        for ch in m.group(1):
            if ord(ch) in _BARLOW:
                if buf:
                    out.append(f'<font face="Sym">{buf}</font>'); buf = ''
                out.append(ch)
            else:
                buf += ch
        if buf:
            out.append(f'<font face="Sym">{buf}</font>')
        return ''.join(out)
    return _SYMRUN.sub(rep, t)

NAVY = colors.HexColor('#0A1220')
NAVY2 = colors.HexColor('#111C30')
PANEL = colors.HexColor('#16243D')
GOLD = colors.HexColor('#E0B23A')
GOLD2 = colors.HexColor('#F5C842')
INK = colors.HexColor('#18212F')
MUTED = colors.HexColor('#5B6B84')
LINE = colors.HexColor('#D5DCE8')
ZEBRA = colors.HexColor('#F3F6FA')
RED = colors.HexColor('#C2410C')
SOFT = colors.HexColor('#8EA0BC')

BRANCH = ['#2563EB', '#0E9F6E', '#7C3AED', '#C2410C', '#B91C1C', '#0891B2', '#A16207', '#475569', '#BE185D', '#15803D']
KIND_LABEL = {'aprofundado': 'MATERIAL APROFUNDADO', 'resumo': 'RESUMO PARA REVISÃO'}
KIND_USE = {'aprofundado': 'ESTUDO INICIAL', 'resumo': 'REVISÃO'}


# *exemplo* (destaque de exemplos) — pode conter **negrito** dentro.
ITALIC = re.compile(r'(?<!\*)\*(?=[^*]|\*\*[^*])((?:\*\*[^*]+?\*\*|[^*])+?)\*(?!\*)')


def md(text):
    """**negrito** vira <b>; *exemplo* vira destaque em azul (a fonte não tem itálico); escapa &, <, >."""
    t = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    t = ITALIC.sub(r'<font color="#2B5C8A">\1</font>', t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)
    t = _sym(t)
    return t.replace('\n', '<br/><br/>')


S = {
    'body': ParagraphStyle('body', fontName='B', fontSize=10.2, leading=14.6, textColor=INK, spaceAfter=6),
    'h3': ParagraphStyle('h3', fontName='BC-B', fontSize=12.5, leading=15, textColor=NAVY, spaceBefore=6, spaceAfter=4, keepWithNext=1),
    'bullet': ParagraphStyle('bullet', fontName='B', fontSize=10.2, leading=14.2, textColor=INK, leftIndent=14, bulletIndent=3, spaceAfter=3,
                             bulletFontName='B-B', bulletColor=GOLD, bulletFontSize=11),
    'cell': ParagraphStyle('cell', fontName='B', fontSize=9.2, leading=12.2, textColor=INK),
    'cellb': ParagraphStyle('cellb', fontName='B-SB', fontSize=9.2, leading=12.2, textColor=NAVY),
    'head': ParagraphStyle('head', fontName='BC-B', fontSize=9.5, leading=12, textColor=colors.white),
    'note': ParagraphStyle('note', fontName='B', fontSize=8.6, leading=11.5, textColor=MUTED, spaceAfter=6),
    'ctitle': ParagraphStyle('ctitle', fontName='BC-B', fontSize=10.5, leading=13, textColor=GOLD2),
    'ctext': ParagraphStyle('ctext', fontName='B', fontSize=9.8, leading=13.8, textColor=colors.white),
    'ctext_dark': ParagraphStyle('ctext_dark', fontName='B', fontSize=9.8, leading=13.8, textColor=INK),
    'q': ParagraphStyle('q', fontName='B', fontSize=10.3, leading=14.6, textColor=INK),
    'qc': ParagraphStyle('qc', fontName='B', fontSize=9.6, leading=13.4, textColor=INK),
    'group': ParagraphStyle('group', fontName='BC-B', fontSize=11.5, leading=14, textColor=colors.HexColor('#8A6100'), spaceBefore=8, spaceAfter=6,
                            keepWithNext=1),
}


class SectionTitle(Flowable):
    def __init__(self, text, width):
        super().__init__()
        self.text, self.w = text, width
        self.height = 36
        self.keepWithNext = 1

    def wrap(self, aw, ah):
        return aw, self.height

    def draw(self):
        c = self.canv
        c.setFillColor(GOLD)
        c.rect(0, 14, 4, 16, stroke=0, fill=1)
        c.setFillColor(NAVY)
        size = 17
        while size > 11 and c.stringWidth(self.text.upper(), 'BC-B', size) > self.w - 14:
            size -= 0.5
        c.setFont('BC-B', size)
        c.drawString(12, 17, self.text.upper())
        c.setStrokeColor(LINE)
        c.setLineWidth(0.8)
        c.line(0, 8, self.w, 8)


def callout(style, title, text, width):
    if style == 'exam':
        bg, border, tcol, body = NAVY2, GOLD, GOLD2, S['ctext']
    elif style == 'key':
        bg, border, tcol, body = colors.HexColor('#FFF7E0'), GOLD, colors.HexColor('#8A6100'), S['ctext_dark']
    else:
        bg, border, tcol, body = colors.HexColor('#FDEEEA'), RED, RED, S['ctext_dark']
    ts = ParagraphStyle('t', parent=S['ctitle'], textColor=tcol)
    t = Table([[Paragraph(title.upper(), ts)], [Paragraph(md(text), body)]], colWidths=[width])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), bg),
        ('LINEBEFORE', (0, 0), (0, -1), 3.5, border),
        ('LEFTPADDING', (0, 0), (-1, -1), 12), ('RIGHTPADDING', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (-1, 0), 9), ('BOTTOMPADDING', (0, -1), (-1, -1), 10),
        ('TOPPADDING', (0, 1), (-1, -1), 2), ('BOTTOMPADDING', (0, 0), (-1, 0), 2),
    ]))
    return KeepTogether([Spacer(1, 4), t, Spacer(1, 8)])


def table(head, rows, widths, width):
    data = [[Paragraph(_sym(h.upper()), S['head']) for h in head]]
    for r in rows:
        data.append([Paragraph(md(r[0]), S['cellb'])] + [Paragraph(md(x), S['cell']) for x in r[1:]])
    t = Table(data, colWidths=[w * width for w in widths], repeatRows=1)
    style = [
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('LINEBELOW', (0, 0), (-1, 0), 1.5, GOLD),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 7), ('RIGHTPADDING', (0, 0), (-1, -1), 7),
        ('TOPPADDING', (0, 0), (-1, -1), 5), ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LINEBELOW', (0, 1), (-1, -1), 0.4, LINE),
    ]
    for i in range(2, len(data), 2):
        style.append(('BACKGROUND', (0, i), (-1, i), ZEBRA))
    t.setStyle(TableStyle(style))
    return [Spacer(1, 3), t, Spacer(1, 9)]


def bullets(items):
    return [Paragraph(md(x), S['bullet'], bulletText='•') for x in items] + [Spacer(1, 4)]


class MindMap(Flowable):
    """Mapa mental em duas colunas, ligado ao centro por curvas."""

    def __init__(self, spec, width, height):
        super().__init__()
        self.spec, self.w, self.h = spec, width, height

    def wrap(self, aw, ah):
        return self.w, self.h

    def draw(self):
        c = self.canv
        w, h = self.w, self.h
        cx, cy = w / 2, h / 2
        rw, rh, bw, gap = 196, 84, 244, 14
        left, right = self.spec['left'], self.spec['right']

        def layout(items, x):
            hs = [36 + 17 * len(b['items']) for b in items]
            total = sum(hs) + gap * (len(items) - 1)
            y = cy + total / 2
            out = []
            for b, bh in zip(items, hs):
                out.append((x, y - bh, bh, b))
                y -= bh + gap
            return out

        L = layout(left, 0)
        R = layout(right, w - bw)
        c.setLineWidth(1.6)
        for i, (x, y, bh, b) in enumerate(L):
            c.setStrokeColor(colors.HexColor(BRANCH[i % len(BRANCH)]))
            p = c.beginPath()
            sx, sy, ex, ey = cx - rw / 2, cy, x + bw, y + bh / 2
            p.moveTo(sx, sy)
            p.curveTo(sx - 45, sy, ex + 45, ey, ex, ey)
            c.drawPath(p, stroke=1, fill=0)
        for i, (x, y, bh, b) in enumerate(R):
            c.setStrokeColor(colors.HexColor(BRANCH[(i + len(L)) % len(BRANCH)]))
            p = c.beginPath()
            sx, sy, ex, ey = cx + rw / 2, cy, x, y + bh / 2
            p.moveTo(sx, sy)
            p.curveTo(sx + 45, sy, ex - 45, ey, ex, ey)
            c.drawPath(p, stroke=1, fill=0)
        c.setFillColor(NAVY)
        c.setStrokeColor(GOLD)
        c.setLineWidth(2)
        c.roundRect(cx - rw / 2, cy - rh / 2, rw, rh, 10, stroke=1, fill=1)
        c.setFillColor(GOLD2)
        size = 18
        while size > 10 and c.stringWidth(self.spec['root'], 'BC-B', size) > rw - 16:
            size -= 0.5
        c.setFont('BC-B', size)
        c.drawCentredString(cx, cy + 5, self.spec['root'])
        c.setFillColor(colors.white)
        c.setFont('B', 11)
        c.drawCentredString(cx, cy - 15, self.spec.get('rootSub', ''))
        for idx, (x, y, bh, b) in enumerate(L + R):
            col = colors.HexColor(BRANCH[idx % len(BRANCH)])
            c.setFillColor(colors.white)
            c.setStrokeColor(col)
            c.setLineWidth(1.2)
            c.roundRect(x, y, bw, bh, 7, stroke=1, fill=1)
            c.setFillColor(col)
            c.roundRect(x, y + bh - 25, bw, 25, 7, stroke=0, fill=1)
            c.rect(x, y + bh - 25, bw, 9, stroke=0, fill=1)
            c.setFillColor(colors.white)
            c.setFont('BC-B', 13)
            c.drawString(x + 10, y + bh - 17.5, b['label'].upper())
            yy = y + bh - 41
            for it in b['items']:
                size = 10.4
                while size > 7 and c.stringWidth(it, 'B', size) > bw - 28:
                    size -= 0.3
                c.setFont('B', size)
                c.setFillColor(col)
                c.circle(x + 13, yy + 3.5, 2, stroke=0, fill=1)
                c.setFillColor(INK)
                c.drawString(x + 21, yy, it)
                yy -= 17


class QuestionBox(Flowable):
    def __init__(self, n, text, width, options=None):
        super().__init__()
        self.n, self.text, self.w = n, text, width
        self.options = options or []
        self.p = Paragraph(md(text).replace('\n', '<br/>'), S['q'])
        self.ops = [Paragraph(f'<b>{chr(65 + i)})</b>&nbsp; ' + md(o), S['q']) for i, o in enumerate(self.options)]

    def wrap(self, aw, ah):
        tw = self.w - (46 if self.options else 112)
        _, ph = self.p.wrap(tw, ah)
        self.ph = ph
        self.oh = []
        for op in self.ops:
            _, h = op.wrap(self.w - 60, ah)
            self.oh.append(h)
        extra = sum(self.oh) + 4 * len(self.oh) + (6 if self.ops else 0)
        self.height = max(ph, 26) + 14 + extra
        return self.w, self.height

    def draw(self):
        c = self.canv
        h = self.height
        c.setFillColor(NAVY)
        c.roundRect(0, h - 30, 26, 24, 5, stroke=0, fill=1)
        c.setFillColor(GOLD2)
        c.setFont('BC-B', 13)
        c.drawCentredString(13, h - 23, f'{self.n:02d}')
        self.p.drawOn(c, 36, h - 6 - self.ph)
        if self.ops:
            y = h - 6 - max(self.ph, 26) - 6
            for op, oh in zip(self.ops, self.oh):
                y -= oh
                op.drawOn(c, 48, y)
                y -= 4
            c.setStrokeColor(LINE)
            c.setLineWidth(0.5)
            c.line(0, 2, self.w, 2)
            return
        x0 = self.w - 66
        for i, lab in enumerate(['C', 'E']):
            x = x0 + i * 34
            c.setStrokeColor(MUTED)
            c.setLineWidth(1)
            c.roundRect(x, h - 28, 26, 22, 4, stroke=1, fill=0)
            c.setFillColor(MUTED)
            c.setFont('BC-B', 12)
            c.drawCentredString(x + 13, h - 22, lab)
        c.setStrokeColor(LINE)
        c.setLineWidth(0.5)
        c.line(0, 2, self.w, 2)


def build_pdf(C, path):
    M_ = C.MATERIAL
    kind = M_['kind']
    W, H = A4
    M = 18 * mm
    doc = BaseDocTemplate(path, pagesize=A4, leftMargin=M, rightMargin=M, topMargin=22 * mm, bottomMargin=18 * mm,
                          title=f"{M_['title']} ({KIND_LABEL[kind].lower()}) — Taticum", author='Taticum',
                          subject=M_['subtitle'], creator='Taticum')
    fw = W - 2 * M
    head_right = M_['header'].upper()

    def bar(c, pw, ph, left):
        c.setFillColor(NAVY)
        c.rect(0, ph - 13 * mm, pw, 13 * mm, stroke=0, fill=1)
        c.setFillColor(GOLD)
        c.rect(0, ph - 13 * mm - 2, pw, 2, stroke=0, fill=1)
        c.setFont('BC-B', 10.5)
        c.setFillColor(GOLD2)
        c.drawString(M, ph - 8.3 * mm, left)
        c.setFillColor(SOFT)
        c.setFont('BC-SB', 9.5)
        c.drawRightString(pw - M, ph - 8.3 * mm, head_right)

    def header(c, d):
        c.saveState()
        bar(c, W, H, f'TATICUM · {KIND_LABEL[kind]}')
        c.setFont('B', 8)
        c.setFillColor(MUTED)
        c.drawString(M, 10 * mm, f"Material v{M_['version']}")
        c.drawRightString(W - M, 10 * mm, str(d.page))
        c.restoreState()

    def header_land(c, d):
        c.saveState()
        LW, LH = landscape(A4)
        bar(c, LW, LH, 'TATICUM · MAPA MENTAL')
        c.setFont('B', 8)
        c.setFillColor(MUTED)
        c.drawRightString(LW - M, 9 * mm, str(d.page))
        c.restoreState()

    def cover(c, d):
        c.saveState()
        c.setFillColor(NAVY)
        c.rect(0, 0, W, H, stroke=0, fill=1)
        c.setFillColor(GOLD2)
        c.rect(0, H - 34 * mm, W, 11 * mm, stroke=0, fill=1)
        c.setFillColor(NAVY)
        c.setFont('BC-B', 11)
        txt = f'TATICUM   //   {KIND_LABEL[kind]}   //   '
        x = -20
        while x < W:
            c.drawString(x, H - 30.3 * mm, txt)
            x += c.stringWidth(txt, 'BC-B', 11)
        c.setStrokeColor(colors.HexColor('#13203A'))
        c.setLineWidth(0.6)
        for gx in range(0, int(W), 28):
            c.line(gx, 0, gx, H - 40 * mm)
        for gy in range(0, int(H - 40 * mm), 28):
            c.line(0, gy, W, gy)
        # selo do tipo de material
        c.setFillColor(GOLD)
        c.roundRect(M, H - 62 * mm, c.stringWidth(KIND_USE[kind], 'BC-B', 11) + 18, 7.5 * mm, 4, stroke=0, fill=1)
        c.setFillColor(NAVY)
        c.setFont('BC-B', 11)
        c.drawString(M + 9, H - 59.6 * mm, KIND_USE[kind])
        c.setFillColor(GOLD)
        c.setFont('BC-B', 13)
        c.drawString(M, H - 74 * mm, M_['coverKicker'].upper())
        size = 46
        for line in M_['coverTitle']:
            while size > 24 and c.stringWidth(line.upper(), 'BC-B', size) > W - 2 * M:
                size -= 1
        y = H - 95 * mm
        c.setFillColor(colors.white)
        c.setFont('BC-B', size)
        for line in M_['coverTitle']:
            c.drawString(M, y, line.upper())
            y -= size * 1.05
        y -= 4
        c.setFillColor(GOLD)
        c.rect(M, y + size * 0.45, 60 * mm, 2.2, stroke=0, fill=1)
        y -= 12
        c.setFillColor(colors.HexColor('#C9D4E5'))
        c.setFont('B', 13)
        for line in M_['coverSub']:
            c.drawString(M, y, line)
            y -= 19
        items = M_['coverItems']
        ch = (20 + 9 * len(items)) * mm
        y0 = 48 * mm
        c.setFillColor(PANEL)
        c.roundRect(M, y0, W - 2 * M, ch, 8, stroke=0, fill=1)
        c.setFillColor(GOLD2)
        c.setFont('BC-B', 11)
        c.drawString(M + 8 * mm, y0 + ch - 9 * mm, 'NESTE MATERIAL')
        # Coluna da descrição começa depois do rótulo mais longo (mínimo de 32 mm).
        lab = max(32 * mm, max(c.stringWidth(t.upper(), 'BC-B', 13) for _, t, _ in items) + 6 * mm)
        dx = M + 20 * mm + lab
        for i, (n, t, s) in enumerate(items):
            yy = y0 + ch - 19 * mm - i * 9 * mm
            c.setFillColor(GOLD)
            c.setFont('BC-B', 14)
            c.drawString(M + 8 * mm, yy, n)
            c.setFillColor(colors.white)
            c.setFont('BC-B', 13)
            c.drawString(M + 20 * mm, yy, t.upper())
            c.setFillColor(SOFT)
            size2 = 10
            while size2 > 7 and c.stringWidth(s, 'B', size2) > W - M - 6 * mm - dx:
                size2 -= 0.3
            c.setFont('B', size2)
            c.drawString(dx, yy, s)
        c.setFillColor(SOFT)
        c.setFont('B', 9)
        c.drawString(M, 30 * mm, M_['coverTopic'])
        c.drawString(M, 25 * mm, M_['coverBase'])
        c.setFillColor(GOLD)
        c.setFont('BC-B', 10)
        c.drawString(M, 17 * mm, f"VERSÃO {M_['version']}  ·  NOVEMBRO DE 2026")
        c.restoreState()

    LW, LH = landscape(A4)
    frame = Frame(M, 18 * mm, fw, H - 40 * mm, id='f', leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    lframe = Frame(M, 14 * mm, LW - 2 * M, LH - 32 * mm, id='lf', leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([
        PageTemplate(id='cover', frames=[Frame(M, M, fw, H - 2 * M, id='c')], onPage=cover, pagesize=A4),
        PageTemplate(id='page', frames=[frame], onPage=header, pagesize=A4),
        PageTemplate(id='land', frames=[lframe], onPage=header_land, pagesize=landscape(A4)),
    ])

    def render(blocks):
        out = []
        for b in blocks:
            t = b['t']
            if t == 'h2':
                out.append(SectionTitle(b['text'], fw))
            elif t == 'h3':
                out.append(Paragraph(md(b['text']), S['h3']))
            elif t == 'p':
                out.append(Paragraph(md(b['text']), S['body']))
            elif t == 'bullets':
                out += bullets(b['items'])
            elif t == 'callout':
                out.append(callout(b['style'], b['title'], b['text'], fw))
            elif t == 'table':
                out += table(b['head'], b['rows'], b['widths'], fw)
            elif t == 'note':
                out.append(Paragraph(md(b['text']), S['note']))
        return out

    story = [NextPageTemplate('page'), PageBreak()]
    story += render(C.THEORY)
    summary = getattr(C, 'SUMMARY', None)
    if summary:
        story.append(PageBreak())
        story += render([b for b in summary if b['t'] != 'mindmap'])
    mind = getattr(C, 'MINDMAP', None)
    if mind:
        story += [NextPageTemplate('land'), PageBreak()]
        story.append(MindMap(mind, LW - 2 * M, LH - 34 * mm))
    story += [NextPageTemplate('page'), PageBreak()]
    qs = C.QUIZ['questions']
    story.append(SectionTitle(f"Questões · {len(qs)} itens · {C.QUIZ['banca']}", fw))
    story.append(Paragraph(md(C.QUIZ['instructions']), S['body']))
    story.append(Spacer(1, 4))
    last = None
    for i, q in enumerate(qs, start=1):
        g = q.get('group')
        if g and g != last:
            story.append(Paragraph(g.upper(), S['group']))
            last = g
        if q.get('context'):
            story.append(callout('key', 'Texto para os próximos itens', q['context'], fw))
        story.append(QuestionBox(i, q['text'], fw, q.get('options')))
        story.append(Spacer(1, 6))
    story.append(PageBreak())
    story.append(SectionTitle('Gabarito comentado', fw))
    story.append(Paragraph('Gabarito rápido: ' + '  '.join(f'<b>{i:02d}</b> {q["answer"]}' for i, q in enumerate(qs, start=1)), S['note']))
    gab = [[Paragraph('ITEM', S['head']), Paragraph('GAB.', S['head']), Paragraph('COMENTÁRIO', S['head'])]]
    for i, q in enumerate(qs, start=1):
        col = '#0F766E' if q['answer'] == 'C' else ('#C2410C' if q['answer'] == 'E' else '#14213D')
        gab.append([Paragraph(f'<b>{i:02d}</b>', S['cellb']),
                    Paragraph(f'<font color="{col}"><b>{q["answer"]}</b></font>', ParagraphStyle('g', parent=S['cellb'], fontSize=12, alignment=TA_CENTER)),
                    Paragraph(md(q['comment']), S['qc'])])
    t = Table(gab, colWidths=[0.08 * fw, 0.08 * fw, 0.84 * fw], repeatRows=1)
    st = [('BACKGROUND', (0, 0), (-1, 0), NAVY), ('LINEBELOW', (0, 0), (-1, 0), 1.5, GOLD), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
          ('LEFTPADDING', (0, 0), (-1, -1), 7), ('RIGHTPADDING', (0, 0), (-1, -1), 7), ('TOPPADDING', (0, 0), (-1, -1), 6),
          ('BOTTOMPADDING', (0, 0), (-1, -1), 7), ('LINEBELOW', (0, 1), (-1, -1), 0.4, LINE)]
    for i in range(2, len(gab), 2):
        st.append(('BACKGROUND', (0, i), (-1, i), ZEBRA))
    t.setStyle(TableStyle(st))
    story.append(t)
    story.append(Spacer(1, 14))
    story.append(Paragraph('<b>FONTES</b>', ParagraphStyle('fs', parent=S['note'], textColor=NAVY, fontName='BC-B', fontSize=10)))
    for s in C.SOURCES:
        story.append(Paragraph(md(s), S['note']))
    doc.build(story)


APP_KEYS = ['id', 'version', 'status', 'subjectId', 'topicIds', 'kind', 'title', 'subtitle', 'minutes', 'pdf']


def build_json(C, path):
    mat = {k: C.MATERIAL[k] for k in APP_KEYS}
    summary = getattr(C, 'SUMMARY', None)
    mat['sections'] = [{'id': 'teoria', 'title': 'Teoria', 'blocks': C.THEORY}]
    if summary:
        mat['sections'].append({'id': 'resumo', 'title': 'Resumo + mapa mental', 'blocks': summary})
    mind = getattr(C, 'MINDMAP', None)
    if mind:
        mat['mindmap'] = mind
    mat['quiz'] = C.QUIZ
    mat['sources'] = C.SOURCES
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(mat, f, ensure_ascii=False, indent=1)


_CMAP = None


def check(C):
    """Confere o conteúdo antes de gerar: gabaritos, quantidade de questões e caracteres que a fonte do PDF não tem."""
    global _CMAP
    if _CMAP is None:
        from fontTools.ttLib import TTFont as FT
        _CMAP = FT(os.path.join(FONTS, 'Barlow-Regular.ttf')).getBestCmap()
    # Capa, mapa mental e títulos de seção são desenhados direto com a Barlow: lá não pode faltar glifo.
    strict = json.dumps([C.MATERIAL, getattr(C, 'MINDMAP', None),
                         [b.get('text') for b in (C.THEORY + (getattr(C, 'SUMMARY', None) or [])) if b.get('t') == 'h2'],
                         [b.get('title') for b in (C.THEORY + (getattr(C, 'SUMMARY', None) or [])) if b.get('t') == 'callout']], ensure_ascii=False)
    missing = sorted({ch for ch in strict if ord(ch) > 127 and ord(ch) not in _CMAP})
    assert not missing, f'{C.__name__}: caracteres sem glifo na fonte do PDF (capa, mapa ou título): {missing}'
    # No corpo do texto, o que a Barlow não tem sai na DejaVu (símbolos lógicos).
    text = json.dumps([C.THEORY, getattr(C, 'SUMMARY', None), C.QUIZ, C.SOURCES], ensure_ascii=False)
    missing = sorted({ch for ch in text if ord(ch) > 127 and ord(ch) not in _CMAP and ord(ch) not in _SYMSET})
    assert not missing, f'{C.__name__}: caracteres sem glifo nem na fonte de símbolos: {missing}'
    qs = C.QUIZ['questions']
    ids = [q['id'] for q in qs]
    assert len(ids) == len(set(ids)), f'{C.__name__}: ids repetidos'
    for q in qs:
        if q.get('options'):
            assert q['answer'] in 'ABCDE' and len(q['options']) == 5, f"{C.__name__} {q['id']}: múltipla escolha inválida"
            assert q['comment'].startswith(f"**Gabarito: {q['answer']}.**"), f"{C.__name__} {q['id']}: comentário não bate com o gabarito"
            assert len(set(q['options'])) == 5, f"{C.__name__} {q['id']}: alternativas repetidas"
            continue
        assert q['answer'] in ('C', 'E'), q['id']
        assert q['comment'].startswith('**Certo.**' if q['answer'] == 'C' else '**Errado.**'), f"{C.__name__} {q['id']}: comentário não bate com o gabarito"
    n = len(qs)
    c = sum(1 for q in qs if q['answer'] == 'C')
    assert n == (20 if C.MATERIAL['kind'] == 'aprofundado' else 10), f'{C.__name__}: {n} questões'
    return n, c


if __name__ == '__main__':
    index = {'version': '2026.11.4', 'materials': []}
    for name in MODULES:
        C = importlib.import_module(name)
        m = C.MATERIAL
        n, c = check(C)
        out_dir = os.path.join(PROJ, 'assets', 'content', m['folder'])
        os.makedirs(out_dir, exist_ok=True)
        pdf = os.path.join(out_dir, m['pdf'])
        build_pdf(C, pdf)
        build_json(C, os.path.join(out_dir, 'material.json'))
        variants = []
        for prof in ('neutro', 'aocp'):
            V = bancas.variant(C, prof)
            vjson = os.path.join(out_dir, f'material.{prof}.json')
            if V is None:
                for old in (vjson, os.path.join(out_dir, f"{m['folder']}.{prof}.pdf")):
                    if os.path.exists(old):
                        os.remove(old)
                continue
            check(V)
            build_pdf(V, os.path.join(out_dir, V.MATERIAL['pdf']))
            build_json(V, vjson)
            variants.append(prof)
            if EXTRA:
                shutil.copy(os.path.join(out_dir, V.MATERIAL['pdf']), os.path.join(EXTRA, V.MATERIAL['outName']))
        index['materials'].append({
            'id': m['id'], 'folder': m['folder'], 'title': m['title'], 'subtitle': m['subtitle'], 'subjectId': m['subjectId'],
            'topicIds': m['topicIds'], 'kind': m['kind'], 'minutes': m['minutes'], 'questions': n, 'version': m['version'], 'status': m['status'],
            'variants': variants,
        })
        if EXTRA:
            os.makedirs(EXTRA, exist_ok=True)
            shutil.copy(pdf, os.path.join(EXTRA, m['outName']))
        print(f"ok {name}: {n} questões ({c} C / {n - c} E) -> {m['pdf']} + {', '.join(variants) or 'sem versões'}")
    with open(os.path.join(PROJ, 'assets', 'content', 'index.json'), 'w', encoding='utf-8') as f:
        json.dump(index, f, ensure_ascii=False, indent=1)
