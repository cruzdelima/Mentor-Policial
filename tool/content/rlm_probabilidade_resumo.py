# -*- coding: utf-8 -*-
"""Raciocínio Lógico · Probabilidade — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "rlm-probabilidade-01", "RLM", "RLM-12", "resumo", "Probabilidade", "Raciocínio Lógico e Matemática · Probabilidade",
    "raciocinio_probabilidade", "RaciocinioLogico_Probabilidade_RESUMO.pdf", None, ["Probabilidade"], RES_SUB,
    RES_ITEMS("definição, regras, condicional e binomial"),
    "Tópico do edital: Probabilidade — Raciocínio Lógico e Matemática",
    "Base: probabilidade elementar.", 25)

THEORY = [
    exam("O que a banca cobra",
         "Situações concretas com **favoráveis/possíveis**, **complementar**, **condicional** e **repetições**."),
    h2("1. Definição"),
    bl("**P = favoráveis / possíveis** (resultados igualmente prováveis).",
       "0 ≤ P ≤ 1. Dois dados: 36 resultados."),
    h2("2. Regras"),
    bl("Complementar: **1 − P(A)** (“pelo menos um”).",
       "União: P(A) + P(B) − **P(A ∩ B)**.",
       "Independentes: **P(A) · P(B)**.",
       "Exclusivos **não** são independentes."),
    h2("3. Condicional"),
    bl("“Sabendo que”: o espaço **encolhe** para o grupo dado.",
       "P(A | B) = P(A ∩ B)/P(B). Use tabela de dupla entrada."),
    h2("4. Repetições"),
    bl("Sem reposição: o total **diminui**. Com reposição: repete a fração.",
       "Exatamente k em n: **C(n, k) · pᵏ · (1 − p)ⁿ⁻ᵏ**."),
]

SUMMARY = [
    h2("Quadro rápido"),
    tb(["Situação", "Conta", "Resultado"], [0.44, 0.34, 0.22], [
        ("Soma 7 com dois dados", "6/36", "1/6"),
        ("Pelo menos uma cara em 3", "1 − 1/8", "7/8"),
        ("2 pretas sem reposição (5B, 3P)", "3/8 × 2/7", "3/28"),
        ("2 pretas com reposição", "3/8 × 3/8", "9/64"),
        ("2 acertos em 3 (p = 0,8)", "3 × 0,64 × 0,2", "0,384"),
        ("Pelo menos 1 acerto em 3", "1 − 0,2³", "0,992"),
    ]),
    h2("Leve para a prova"),
    bl("Favoráveis ÷ possíveis.",
       "Pelo menos um: **complementar**.",
       "E (independentes): **multiplica**.",
       "Ou: soma e tira a interseção.",
       "Sabendo que: **encolhe o espaço**.",
       "Binomial: não esqueça o **C(n, k)**."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "PROBABILIDADE", "rootSub": "favoráveis / possíveis",
    "left": [
        {"label": "Definição", "items": ["favoráveis", "sobre possíveis", "entre 0 e 1"]},
        {"label": "Complementar", "items": ["1 menos P", "pelo menos um", "nenhum"]},
        {"label": "União", "items": ["soma as duas", "tira a interseção", "exclusivos: só soma"]},
        {"label": "Independentes", "items": ["multiplica", "um não muda o outro", "tiros, moedas"]},
        {"label": "Exclusivos", "items": ["não ocorrem juntos", "não são independentes", "interseção zero"]},
    ],
    "right": [
        {"label": "Condicional", "items": ["sabendo que", "encolhe o espaço", "tabela dupla"]},
        {"label": "Sem reposição", "items": ["total diminui", "3/8 e 2/7", "ou combinação"]},
        {"label": "Com reposição", "items": ["repete a fração", "3/8 e 3/8", "independentes"]},
        {"label": "Binomial", "items": ["exatamente k", "C(n, k)", "p e 1 - p"]},
        {"label": "Sorteio de grupo", "items": ["combinação", "favoráveis", "sobre total"]},
    ],
}

QUIZ = quiz([
    ("C", "No lançamento de dois dados honestos, a probabilidade de a soma ser pelo menos 10 é 1/6.",
     "Somas 10, 11 e 12: 3 + 2 + 1 = 6 casos em 36."),
    ("E", "No lançamento de um dado honesto, a probabilidade de sair número maior que 4 é 1/2.",
     "Só 5 e 6: 2/6 = 1/3."),
    ("C", "Se a probabilidade de chover amanhã é 0,35, a de não chover é 0,65.",
     "Complementar."),
    ("C", "Se A e B são independentes, com P(A) = 0,6 e P(B) = 0,7, então P(A ∩ B) = 0,42.",
     "0,6 × 0,7."),
    ("E", "Lançando-se uma moeda 3 vezes, a probabilidade de saírem 3 caras é 3/8.",
     "(1/2)³ = 1/8."),
    ("C", "Retirando-se 2 bolas, sem reposição, de uma urna com 5 brancas e 3 pretas, a probabilidade de nenhuma ser preta é 5/14.",
     "5/8 × 4/7 = 20/56."),
    ("E", "Na situação do item anterior, a probabilidade de pelo menos uma ser preta é 5/14.",
     "1 − 5/14 = 9/14."),
    ("C", "Em uma turma, 30 de 50 alunos são homens e 12 dos homens usam óculos. Sabendo que o sorteado é homem, a probabilidade de ele usar óculos é 2/5.",
     "12/30."),
    ("E", "Se um evento tem probabilidade 1,2, ele é mais provável que um evento certo.",
     "Probabilidade nunca passa de 1."),
    ("C", "Se cada tentativa tem probabilidade 1/2 de sucesso, de forma independente, a probabilidade de exatamente 1 sucesso em 2 tentativas é 1/2.",
     "C(2, 1) × 1/2 × 1/2 = 1/2."),
], 10)

SOURCES = [
    "Probabilidade elementar.",
    SRC_R,
]
