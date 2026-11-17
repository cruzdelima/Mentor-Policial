# -*- coding: utf-8 -*-
GA = "Bloco A · inéditas"
GB = "Bloco B · padrão de cobrança da banca"
INSTR20 = ("Julgue os itens a seguir. São 20 itens: o Bloco A treina o conteúdo; o Bloco B segue o padrão de cobrança da banca. "
           "No estilo Cebraspe, cada erro anula um acerto: na dúvida, deixe em branco.")
INSTR10 = "Julgue os itens a seguir. No estilo Cebraspe, cada erro anula um acerto: na dúvida, deixe em branco."


def quiz(items, n):
    """items: lista de (gabarito, texto, comentário[, texto de apoio]). Os 10 últimos de um bloco de 20 vão para o Bloco B.
    O texto de apoio aparece antes do item (use no primeiro item de cada grupo que se refere ao mesmo texto)."""
    qs = []
    for i, it in enumerate(items, start=1):
        ans, text, comment = it[0], it[1], it[2]
        q = {"id": f"q{i}", "answer": ans, "text": text, "comment": ("**Certo.** " if ans == "C" else "**Errado.** ") + comment}
        if len(it) > 3:
            q["context"] = it[3]
        if n == 20:
            q["group"] = GA if i <= 10 else GB
        qs.append(q)
    return {"style": "CE", "banca": "estilo Cebraspe", "instructions": INSTR20 if n == 20 else INSTR10, "questions": qs}


def h2(t): return {"t": "h2", "text": t}
def h3(t): return {"t": "h3", "text": t}
def p(t): return {"t": "p", "text": t}
def nt(t): return {"t": "note", "text": t}
def bl(*items): return {"t": "bullets", "items": list(items)}
def tb(head, widths, rows): return {"t": "table", "head": head, "widths": widths, "rows": [list(r) for r in rows]}
def exam(title, t): return {"t": "callout", "style": "exam", "title": title, "text": t}
def key(title, t): return {"t": "callout", "style": "key", "title": title, "text": t}
def trap(title, t): return {"t": "callout", "style": "trap", "title": title, "text": t}


def material(mid, subject, topic, kind, title, subtitle, folder, out, kicker, cover_title, cover_sub, items, topic_line, base, minutes,
             status="Em revisão pelo autor"):
    """Monta o dicionário MATERIAL. kind: 'aprofundado' ou 'resumo'."""
    return {
        "id": mid, "version": "0.1.0", "status": status, "subjectId": subject, "topicIds": [topic], "kind": kind, "title": title,
        "subtitle": subtitle, "minutes": minutes, "folder": folder, "pdf": folder + ".pdf", "outName": out,
        "header": subtitle.split(" · ")[0] + " · " + title, "coverKicker": subtitle.replace(" · ", "  ·  "), "coverTitle": cover_title,
        "coverSub": cover_sub, "coverItems": items, "coverTopic": topic_line, "coverBase": base,
    } if kicker is None else {
        "id": mid, "version": "0.1.0", "status": status, "subjectId": subject, "topicIds": [topic], "kind": kind, "title": title,
        "subtitle": subtitle, "minutes": minutes, "folder": folder, "pdf": folder + ".pdf", "outName": out,
        "header": subtitle.split(" · ")[0] + " · " + title, "coverKicker": kicker, "coverTitle": cover_title,
        "coverSub": cover_sub, "coverItems": items, "coverTopic": topic_line, "coverBase": base,
    }


RES_ITEMS = lambda teoria: [("01", "Teoria", teoria), ("02", "Resumo", "quadro de consulta e “leve para a prova”"),
                            ("03", "Mapa mental", "uma página para revisar em 5 minutos"), ("04", "Questões", "10 itens certo/errado + gabarito comentado")]
RES_SUB = ["Resumo direto ao ponto, quadro de consulta, mapa mental", "e 10 questões no estilo Cebraspe com gabarito comentado."]
SRC_A = "Os 20 itens foram escritos para o Mentor Policial. O Bloco B segue o padrão de cobrança da banca, mas não reproduz questões de provas."
SRC_R = "Texto e questões elaborados para o Mentor Policial (itens inéditos no estilo Cebraspe)."
GRAM = "Gramáticas de referência: Bechara, Moderna gramática portuguesa; Cunha e Cintra, Nova gramática do português contemporâneo."
