# -*- coding: utf-8 -*-
"""Raciocínio Lógico · Conjuntos e operações — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "rlm-conjuntos-01", "RLM", "RLM-07", "resumo", "Conjuntos e operações", "Raciocínio Lógico e Matemática · Conjuntos",
    "raciocinio_conjuntos", "RaciocinioLogico_Conjuntos_RESUMO.pdf", None, ["Conjuntos e", "operações"], RES_SUB,
    RES_ITEMS("notação, operações e diagramas de Venn"),
    "Tópico do edital: Conjuntos e operações — Raciocínio Lógico",
    "Base: teoria elementar dos conjuntos.", 20)

THEORY = [
    exam("O que a banca cobra",
         "**Notação** (∈ e ⊂), **operações** e **problemas numéricos** com diagramas de Venn."),
    h2("1. Notação"),
    bl("**∈**: elemento pertence a conjunto. **⊂**: conjunto contido em conjunto.",
       "Vazio é subconjunto de todo conjunto.",
       "n elementos → **2ⁿ subconjuntos**."),
    h2("2. Operações"),
    bl("**A ∪ B**: em A ou em B. **A ∩ B**: em A e em B.",
       "**A − B**: em A e não em B. **Aᶜ**: no universo e não em A.",
       "(A ∪ B)ᶜ = Aᶜ ∩ Bᶜ; (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ."),
    h2("3. Contagem"),
    bl("**n(A ∪ B) = n(A) + n(B) − n(A ∩ B)**.",
       "Três: soma os três, subtrai as interseções duplas, **soma** a tripla.",
       "Só A = n(A) − n(A ∩ B). Nenhum = total − n(A ∪ B).",
       "Preencha o Venn **de dentro para fora**."),
]

SUMMARY = [
    h2("Quadro rápido"),
    tb(["Quero", "Conta"], [0.42, 0.58], [
        ("Pelo menos um (2 conjuntos)", "n(A) + n(B) − n(A ∩ B)"),
        ("Os dois", "n(A) + n(B) − n(A ∪ B)"),
        ("Só A", "n(A) − n(A ∩ B)"),
        ("Exatamente um", "n(A ∪ B) − n(A ∩ B)"),
        ("Nenhum", "total − n(A ∪ B)"),
        ("Interseção mínima", "n(A) + n(B) − total (se positivo)"),
        ("Subconjuntos", "2ⁿ"),
    ]),
    h2("Leve para a prova"),
    bl("∈ elemento; ⊂ conjunto.",
       "União: **some e tire a interseção**.",
       "Três: **+ tripla** no final.",
       "Venn: **comece pelo meio**.",
       "Números dados são **totais** dos círculos."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "CONJUNTOS", "rootSub": "e operações",
    "left": [
        {"label": "Pertence", "items": ["elemento", "e conjunto", "1 pertence a A"]},
        {"label": "Contido", "items": ["conjunto", "e conjunto", "vazio em todos"]},
        {"label": "Subconjuntos", "items": ["2 elevado a n", "inclui o vazio", "e o próprio"]},
        {"label": "União", "items": ["em A ou em B", "soma menos", "a interseção"]},
        {"label": "Interseção", "items": ["em A e em B", "disjuntos: vazio", "região do meio"]},
    ],
    "right": [
        {"label": "Diferença", "items": ["A menos B", "só os de A", "não comuta"]},
        {"label": "Complementar", "items": ["fora de A", "dentro do universo", "De Morgan vale"]},
        {"label": "Três conjuntos", "items": ["soma os três", "menos as duplas", "mais a tripla"]},
        {"label": "Venn", "items": ["de dentro", "para fora", "totais nos círculos"]},
        {"label": "Numéricos", "items": ["naturais, inteiros", "racionais, reais", "pi é irracional"]},
    ],
}

QUIZ = quiz([
    ("C", "Se B = {a, b, c}, então {a, b} ⊂ B.",
     "{a, b} é subconjunto de B."),
    ("E", "Se B = {a, b, c}, então a ⊂ B.",
     "a é elemento: a ∈ B."),
    ("C", "Um conjunto com 4 elementos tem 16 subconjuntos.",
     "2⁴ = 16."),
    ("E", "Se n(A) = 12, n(B) = 9 e n(A ∩ B) = 4, então n(A ∪ B) = 21.",
     "12 + 9 − 4 = 17."),
    ("C", "Se A = {1, 3, 5, 7} e B = {5, 7, 9}, então B − A = {9}.",
     "Elementos de B que não estão em A."),
    ("C", "Entre 50 agentes, 30 fizeram curso de inteligência, 25 de tiro e 12 os dois. Então 7 agentes não fizeram nenhum dos cursos.",
     "Pelo menos um: 30 + 25 − 12 = 43; nenhum: 50 − 43 = 7."),
    ("E", "Na situação do item anterior, 30 agentes fizeram somente o curso de inteligência.",
     "Só inteligência: 30 − 12 = 18."),
    ("C", "Se 70 de 100 candidatos estudaram Lógica e 60 estudaram Português, pelo menos 30 estudaram as duas matérias.",
     "70 + 60 − 100 = 30."),
    ("E", "O conjunto dos números naturais contém o conjunto dos números inteiros.",
     "É o contrário: ℕ ⊂ ℤ."),
    ("C", "Se A ⊂ B, então A ∩ B = A.",
     "Os elementos comuns são os de A."),
], 10)

SOURCES = [
    "Teoria elementar dos conjuntos.",
    SRC_R,
]
