# -*- coding: utf-8 -*-
"""Raciocínio Lógico · Negação de proposições — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "rlm-negacao-01", "RLM", "RLM-04", "resumo", "Negação de proposições", "Raciocínio Lógico e Matemática · Lógica proposicional",
    "raciocinio_negacao", "RaciocinioLogico_Negacao_RESUMO.pdf", None, ["Negação de", "proposições"], RES_SUB,
    RES_ITEMS("conectivos e quantificadores"),
    "Tópico do edital: Negação de proposições — Raciocínio Lógico",
    "Base: lógica proposicional e de quantificadores.", 20)

THEORY = [
    exam("O que a banca cobra",
         "“A negação de X é Y”: as regras de cada **conectivo**, os **quantificadores** e a diferença entre **negar** e dizer o **contrário**."),
    h2("1. Conectivos"),
    bl("**¬(P ∧ Q) = ¬P ∨ ¬Q**.",
       "**¬(P ∨ Q) = ¬P ∧ ¬Q**.",
       "**¬(P → Q) = P ∧ ¬Q** (MANÉ: mantém, nega, e).",
       "**¬(P ↔ Q) = P ⊻ Q** = (P ∧ ¬Q) ∨ (¬P ∧ Q).",
       "**¬(P ⊻ Q) = P ↔ Q**."),
    h2("2. Quantificadores"),
    bl("**Todo A é B** → algum A **não** é B.",
       "**Algum A é B** → **nenhum** A é B.",
       "**Nenhum A é B** → algum A é B.",
       "“Pelo menos um”, “existe”, “há” = algum."),
    h2("3. Cuidado"),
    bl("Negação **não é contrário**: cheia → não cheia (não “vazia”).",
       "A negação da condicional **não** tem “se... então”."),
]

SUMMARY = [
    h2("Quadro rápido"),
    tb(["Proposição", "Negação"], [0.45, 0.55], [
        ("P e Q", "não P **ou** não Q"),
        ("P ou Q", "não P **e** não Q"),
        ("Se P, então Q", "P **e** não Q"),
        ("P se e somente se Q", "ou P ou Q"),
        ("Nem P nem Q", "P ou Q"),
        ("Todo A é B", "Algum A não é B"),
        ("Algum A é B", "Nenhum A é B"),
        ("Nenhum A é B", "Algum A é B"),
    ]),
    h2("Leve para a prova"),
    bl("De Morgan: **nega e troca**.",
       "Condicional: **MANÉ**.",
       "Bicondicional: vira **ou exclusivo**.",
       "Todo ↔ **algum não**.",
       "Algum ↔ **nenhum**.",
       "Negar não é dizer o **contrário**."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "NEGAÇÃO", "rootSub": "valor sempre oposto",
    "left": [
        {"label": "Negar o e", "items": ["não P ou não Q", "De Morgan", "troca por ou"]},
        {"label": "Negar o ou", "items": ["não P e não Q", "De Morgan", "troca por e"]},
        {"label": "Negar se então", "items": ["mantém a primeira", "nega a segunda", "liga com e"]},
        {"label": "Negar sse", "items": ["ou exclusivo", "um sem o outro", "valores diferentes"]},
        {"label": "Dupla negação", "items": ["não não P", "é P", "volta ao original"]},
    ],
    "right": [
        {"label": "Todo", "items": ["algum não é", "basta um contraexemplo", "não é nenhum"]},
        {"label": "Algum", "items": ["nenhum é", "pelo menos um", "existe, há"]},
        {"label": "Nenhum", "items": ["algum é", "basta um", "que seja"]},
        {"label": "Contrário", "items": ["não é negação", "cheia e vazia", "há meio-termo"]},
        {"label": "Composta", "items": ["nega o principal", "depois as partes", "passo a passo"]},
    ],
}

QUIZ = quiz([
    ("C", "A negação de “O agente dirigia e o escrivão anotava” é “O agente não dirigia ou o escrivão não anotava”.",
     "De Morgan."),
    ("E", "A negação de “Se o carro for roubado, o seguro pagará” é “Se o carro não for roubado, o seguro não pagará”.",
     "A negação é “O carro foi roubado e o seguro não pagará”."),
    ("C", "A negação de “Todo laudo é assinado por dois peritos” é “Algum laudo não é assinado por dois peritos”.",
     "Todo ↔ algum não."),
    ("E", "A negação de “Algum preso fugiu” é “Algum preso não fugiu”.",
     "A negação é “Nenhum preso fugiu”."),
    ("C", "A negação de P ∨ ¬Q é ¬P ∧ Q.",
     "De Morgan com dupla negação."),
    ("C", "A negação de P ↔ Q é equivalente a P ↔ ¬Q.",
     "Ambas são verdadeiras quando P e Q têm valores diferentes."),
    ("E", "A negação de “O réu é culpado” é “O réu é inocente”.",
     "A negação é “O réu não é culpado”; inocente seria o contrário."),
    ("C", "A negação de “Nenhum servidor faltou” é “Pelo menos um servidor faltou”.",
     "Nenhum ↔ algum."),
    ("E", "A negação de P ∧ ¬Q é ¬P ∧ Q.",
     "É ¬P ∨ Q."),
    ("C", "A negação de P → Q é equivalente a ¬(¬P ∨ Q).",
     "P → Q ⇔ ¬P ∨ Q; negar os dois lados mantém a equivalência."),
], 10)

SOURCES = [
    "Lógica proposicional e de quantificadores.",
    SRC_R,
]
