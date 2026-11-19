# -*- coding: utf-8 -*-
"""Raciocínio Lógico · Sequências e progressões — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "rlm-sequencias-01", "RLM", "RLM-10", "resumo", "Sequências e progressões", "Raciocínio Lógico e Matemática · Sequências",
    "raciocinio_sequencias", "RaciocinioLogico_Sequencias_RESUMO.pdf", None, ["Sequências e", "progressões"], RES_SUB,
    RES_ITEMS("padrões, PA e PG"),
    "Tópico do edital: Sequências e progressões — Raciocínio Lógico e Matemática",
    "Base: matemática do ensino médio.", 20)

THEORY = [
    exam("O que a banca cobra",
         "A **lei de formação** de listas e o cálculo de **termos e somas** de PA e PG."),
    h2("1. Padrões"),
    bl("Diferença constante → PA. Quociente constante → PG.",
       "Diferenças que crescem, Fibonacci, quadrados, sequências **intercaladas**.",
       "Letras: numere (A = 1, B = 2...)."),
    h2("2. PA"),
    bl("**aₙ = a₁ + (n − 1) · r**.",
       "**Sₙ = (a₁ + aₙ) · n / 2**.",
       "Termo do meio = média dos vizinhos.",
       "Contar múltiplos: use o termo geral."),
    h2("3. PG"),
    bl("**aₙ = a₁ · qⁿ⁻¹**.",
       "**Sₙ = a₁ · (qⁿ − 1)/(q − 1)**.",
       "Soma infinita (|q| < 1): **a₁/(1 − q)**.",
       "Crescimento de p% ao período = PG de razão (1 + p/100)."),
]

SUMMARY = [
    h2("Quadro rápido"),
    tb(["", "PA", "PG"], [0.2, 0.4, 0.4], [
        ("Passo", "soma r", "multiplica por q"),
        ("Termo geral", "a₁ + (n − 1)r", "a₁ · qⁿ⁻¹"),
        ("Soma", "(a₁ + aₙ)n/2", "a₁(qⁿ − 1)/(q − 1)"),
        ("Exemplo", "3, 7, 11 (r = 4)", "2, 6, 18 (q = 3)"),
        ("Situação", "aumento fixo", "aumento percentual"),
    ]),
    h2("Leve para a prova"),
    bl("1 a 100 soma **5.050**.",
       "Quantidade fixa: **PA**.",
       "Percentual fixo: **PG**.",
       "Soma infinita: **a₁/(1 − q)**.",
       "Fibonacci: soma os **dois anteriores**."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "SEQUÊNCIAS", "rootSub": "PA e PG",
    "left": [
        {"label": "Padrões", "items": ["compare vizinhos", "diferença ou razão", "intercaladas"]},
        {"label": "Letras", "items": ["numere o alfabeto", "26 letras", "pula uma, duas"]},
        {"label": "Especiais", "items": ["Fibonacci", "quadrados", "dobra menos um"]},
        {"label": "PA termo", "items": ["primeiro termo", "mais (n - 1) r", "conta múltiplos"]},
        {"label": "PA soma", "items": ["primeiro + último", "vezes n", "dividido por 2"]},
    ],
    "right": [
        {"label": "PG termo", "items": ["primeiro termo", "vezes q elevado", "a n - 1"]},
        {"label": "PG soma", "items": ["q elevado a n - 1", "sobre q - 1", "vezes o primeiro"]},
        {"label": "Soma infinita", "items": ["q entre -1 e 1", "primeiro termo", "sobre 1 - q"]},
        {"label": "Crescimento", "items": ["fixo: PA", "percentual: PG", "10% ao ano: 1,1"]},
        {"label": "Propriedade", "items": ["PA: média", "dos vizinhos", "termo do meio"]},
    ],
}

QUIZ = quiz([
    ("C", "Na sequência 4, 9, 14, 19, ..., o 10º termo é 49.",
     "4 + 9 × 5."),
    ("E", "Na sequência 3, 6, 12, 24, ..., o 8º termo é 192.",
     "3 × 2⁷ = 384."),
    ("C", "A soma dos 10 primeiros termos da PA (2, 5, 8, ...) é 155.",
     "a₁₀ = 29; (2 + 29) × 10/2 = 155."),
    ("C", "A soma infinita da PG (8, 2, 1/2, ...) é 32/3.",
     "q = 1/4; 8/(3/4) = 32/3."),
    ("E", "Uma população de 10.000 que cresce 2% ao ano forma uma PA de razão 200.",
     "Crescimento percentual forma PG de razão 1,02."),
    ("C", "Na sequência 1, 4, 9, 16, 25, ..., o próximo termo é 36.",
     "Quadrados perfeitos."),
    ("E", "De 1 a 100, inclusive, há 24 múltiplos de 4.",
     "São 4, 8, ..., 100: 100 = 4 + (n − 1) × 4 → n = 25."),
    ("C", "Em uma PA, se a₂ = 10 e a₄ = 18, então a₃ = 14.",
     "Média dos vizinhos."),
    ("C", "Na sequência de letras B, E, H, K, ..., a próxima letra é N.",
     "Pula duas letras: B(2), E(5), H(8), K(11), N(14)."),
    ("E", "A razão da PG (81, 27, 9, ...) é 3.",
     "A razão é 1/3."),
], 10)

SOURCES = [
    "Matemática do ensino médio: progressões.",
    SRC_R,
]
