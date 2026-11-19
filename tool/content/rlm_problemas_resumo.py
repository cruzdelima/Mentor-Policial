# -*- coding: utf-8 -*-
"""Raciocínio Lógico · Problemas aritméticos e equações — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "rlm-problemas-01", "RLM", "RLM-09", "resumo", "Problemas aritméticos e equações", "Raciocínio Lógico e Matemática · Matemática básica",
    "raciocinio_problemas", "RaciocinioLogico_Problemas_RESUMO.pdf", None, ["Problemas e", "equações"], RES_SUB,
    RES_ITEMS("frações, MMC, MDC, equações e problemas"),
    "Tópico do edital: Problemas aritméticos e equações — Raciocínio Lógico e Matemática",
    "Base: matemática básica.", 25)

THEORY = [
    exam("O que a banca cobra",
         "Problemas em texto: **traduzir em equação**, MMC e MDC disfarçados e **testar o valor** do item."),
    h2("1. Ferramentas"),
    bl("Frações: MMC nos denominadores; “de” = multiplicar.",
       "**MMC**: eventos que voltam a coincidir.",
       "**MDC**: maior grupo igual possível."),
    h2("2. Equações"),
    bl("1º grau: isole x.",
       "Sistemas: adição ou substituição.",
       "2º grau: **Δ = b² − 4ac**; x = (−b ± √Δ)/2a.",
       "Soma = **−b/a**; produto = **c/a**. Δ < 0: sem raiz real."),
    h2("3. Problemas"),
    bl("Idades: some o **mesmo t** a todos.",
       "Trabalho conjunto: **1/a + 1/b = 1/T**.",
       "Um enche e outro esvazia: **subtraia** as taxas.",
       "Teste o número do item no enunciado."),
]

SUMMARY = [
    h2("Quadro rápido"),
    tb(["Problema", "Conta", "Exemplo"], [0.3, 0.32, 0.38], [
        ("Coincidir de novo", "MMC", "12 e 18 min → 36 min"),
        ("Maior equipe igual", "MDC", "48 e 36 → 12"),
        ("Juntos", "1/a + 1/b", "6 h e 3 h → 2 h"),
        ("Enche e vaza", "1/a − 1/b", "10 h e 15 h → 30 h"),
        ("Idades", "mesmo t para todos", "40 e 10 → 20 anos"),
        ("Rodas", "sistema", "20 veículos, 56 rodas → 8 carros"),
    ]),
    h2("Leve para a prova"),
    bl("Dê **nome** à incógnita.",
       "Soma −b/a, produto c/a.",
       "Coincidir = **MMC**.",
       "Dividir em grupos = **MDC**.",
       "Some as **taxas** por hora.",
       "Na dúvida, **teste** o valor."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "PROBLEMAS", "rootSub": "e equações",
    "left": [
        {"label": "Frações", "items": ["MMC embaixo", "de = vezes", "fração do resto"]},
        {"label": "MMC", "items": ["eventos repetidos", "coincidem de novo", "12 e 18: 36"]},
        {"label": "MDC", "items": ["dividir igualmente", "maior grupo", "48 e 36: 12"]},
        {"label": "1º grau", "items": ["isole x", "sistemas", "adição ou substituição"]},
        {"label": "2º grau", "items": ["delta", "Bhaskara", "soma e produto"]},
    ],
    "right": [
        {"label": "Idades", "items": ["mesmo tempo", "para todos", "monte a igualdade"]},
        {"label": "Trabalho", "items": ["some as taxas", "1/a + 1/b", "inverta no fim"]},
        {"label": "Enche e vaza", "items": ["subtraia", "as taxas", "1/10 - 1/15"]},
        {"label": "Divisão", "items": ["antes e depois", "monte a equação", "ou teste o valor"]},
        {"label": "Método", "items": ["nomeie", "traduza o texto", "confira no fim"]},
    ],
}

QUIZ = quiz([
    ("C", "Se 5x + 3 = 28, então x = 5.",
     "5x = 25."),
    ("E", "As raízes de x² − 7x + 10 = 0 são −2 e −5.",
     "Soma 7 e produto 10: raízes 2 e 5."),
    ("C", "A equação x² − 4x + 4 = 0 tem uma única raiz real.",
     "Δ = 16 − 16 = 0: raiz dupla x = 2."),
    ("C", "O MMC de 4, 6 e 10 é 60.",
     "60 é o menor múltiplo comum."),
    ("E", "O MDC de 60, 72 e 84 é 6.",
     "MDC(60, 72, 84) = 12."),
    ("C", "Duas impressoras fazem um serviço em 4 h e em 12 h, respectivamente. Juntas, fazem o serviço em 3 h.",
     "1/4 + 1/12 = 1/3."),
    ("E", "Uma mãe tem 36 anos e a filha, 6. Daqui a 10 anos, a mãe terá o triplo da idade da filha.",
     "46 e 16: 46 não é o triplo de 16. O triplo ocorre em 9 anos (45 e 15)."),
    ("C", "Se x + y = 20 e 2x + 4y = 56, então y = 8.",
     "2x + 4y = 56 → x + 2y = 28 → y = 8."),
    ("C", "Três quartos de 2/3 de 240 é igual a 120.",
     "240 × 2/3 = 160; 160 × 3/4 = 120."),
    ("E", "Se a soma de dois números pares consecutivos é 46, o maior deles é 22.",
     "x + x + 2 = 46 → x = 22; o maior é 24."),
], 10)

SOURCES = [
    "Matemática básica.",
    SRC_R,
]
