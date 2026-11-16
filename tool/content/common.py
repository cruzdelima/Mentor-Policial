# -*- coding: utf-8 -*-
GA = "Bloco A · inéditas"
GB = "Bloco B · padrão de cobrança da banca"
INSTR20 = ("Julgue os itens a seguir. São 20 itens: o Bloco A treina o conteúdo; o Bloco B segue o padrão de cobrança da banca. "
           "No estilo Cebraspe, cada erro anula um acerto: na dúvida, deixe em branco.")
INSTR10 = "Julgue os itens a seguir. No estilo Cebraspe, cada erro anula um acerto: na dúvida, deixe em branco."


def quiz(items, n):
    """items: lista de (gabarito, texto, comentário). Os 10 últimos de um bloco de 20 vão para o Bloco B."""
    qs = []
    for i, (ans, text, comment) in enumerate(items, start=1):
        q = {"id": f"q{i}", "answer": ans, "text": text, "comment": ("**Certo.** " if ans == "C" else "**Errado.** ") + comment}
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
