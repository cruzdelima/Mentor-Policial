# -*- coding: utf-8 -*-
"""Raciocínio Lógico · Princípios de contagem e análise combinatória — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "rlm-contagem-01", "RLM", "RLM-11", "resumo", "Princípios de contagem e análise combinatória", "Raciocínio Lógico e Matemática · Combinatória",
    "raciocinio_contagem", "RaciocinioLogico_Contagem_RESUMO.pdf", None, ["Análise", "combinatória"], RES_SUB,
    RES_ITEMS("princípio fundamental, permutação, arranjo e combinação"),
    "Tópico do edital: Princípios de contagem e análise combinatória — Raciocínio Lógico e Matemática",
    "Base: análise combinatória.", 25)

THEORY = [
    exam("O que a banca cobra",
         "Contar escolhas com o **princípio fundamental** e decidir se **a ordem importa**."),
    h2("1. Princípio fundamental"),
    bl("Etapas (“e”): **multiplique**. Casos separados (“ou”): **some**.",
       "Comece pela etapa com **restrição**."),
    h2("2. Permutações"),
    bl("Simples: **n!**.",
       "Com repetição: **n!/(a! · b!...)**.",
       "Circular: **(n − 1)!**.",
       "Juntos: bloco permuta e se arruma por dentro."),
    h2("3. Arranjo × combinação"),
    bl("Troque a ordem dos escolhidos: muda a situação → **arranjo**; não muda → **combinação**.",
       "A(n, p) = n!/(n − p)!. C(n, p) = n!/[p!(n − p)!].",
       "Pelo menos um = **total − nenhum**."),
]

SUMMARY = [
    h2("Quadro rápido"),
    tb(["Situação", "Ferramenta", "Exemplo"], [0.36, 0.28, 0.36], [
        ("Senha, placa", "Princípio fundamental", "10 × 9 × 8 × 7 = 5.040"),
        ("Fila", "n!", "5 pessoas: 120"),
        ("Anagrama com letra repetida", "n!/a!", "POLICIA: 2.520"),
        ("Mesa redonda", "(n − 1)!", "5 pessoas: 24"),
        ("Cargos distintos", "Arranjo", "3 de 8: 336"),
        ("Equipe, comissão", "Combinação", "3 de 8: 56"),
        ("Pelo menos um", "Total − nenhum", "120 − 20 = 100"),
    ]),
    h2("Leve para a prova"),
    bl("“E” multiplica; “ou” soma.",
       "Ordem importa: **arranjo**.",
       "Ordem não importa: **combinação**.",
       "Combinação = arranjo ÷ **p!**.",
       "0! = 1; 5! = 120; 6! = 720.",
       "C(n, p) = C(n, n − p)."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "COMBINATÓRIA", "rootSub": "a ordem importa?",
    "left": [
        {"label": "Princípio", "items": ["etapas: multiplique", "casos: some", "restrição primeiro"]},
        {"label": "Fatorial", "items": ["n vezes n - 1...", "0! = 1", "5! = 120"]},
        {"label": "Permutação", "items": ["todos em ordem", "filas", "anagramas"]},
        {"label": "Com repetição", "items": ["divida pelos", "fatoriais", "das repetidas"]},
        {"label": "Circular", "items": ["(n - 1)!", "mesa redonda", "fixe um"]},
    ],
    "right": [
        {"label": "Arranjo", "items": ["ordem importa", "cargos, pódio", "senhas"]},
        {"label": "Combinação", "items": ["ordem não importa", "equipes, comissões", "arranjo / p!"]},
        {"label": "Teste", "items": ["troque a ordem", "mudou: arranjo", "igual: combinação"]},
        {"label": "Pelo menos um", "items": ["total", "menos nenhum", "complementar"]},
        {"label": "Juntos", "items": ["vire bloco", "permute os blocos", "arrume por dentro"]},
    ],
}

QUIZ = quiz([
    ("C", "Com os algarismos de 0 a 9, podem ser formadas 1.000 senhas de 3 dígitos, permitida a repetição.",
     "10 × 10 × 10."),
    ("E", "O número de anagramas da palavra ARARA é 120.",
     "A três vezes e R duas: 5!/(3! · 2!) = 10."),
    ("C", "Há 720 maneiras de organizar 6 processos em uma pilha.",
     "6! = 720."),
    ("C", "Escolher 2 entre 5 agentes para uma diligência, sem distinção de função, pode ser feito de 10 maneiras.",
     "C(5, 2) = 10."),
    ("E", "Escolher 2 entre 5 agentes, sendo um motorista e outro o responsável pela diligência, pode ser feito de 10 maneiras.",
     "Funções distintas: 5 × 4 = 20."),
    ("C", "O número de comissões de 4 pessoas escolhidas entre 9 é 126.",
     "C(9, 4) = 126."),
    ("E", "Seis pessoas podem sentar-se em volta de uma mesa redonda de 720 maneiras.",
     "Circular: 5! = 120."),
    ("C", "Com 7 agentes e 5 escrivães, é possível formar 210 equipes com 2 agentes e 3 escrivães.",
     "C(7, 2) × C(5, 3) = 21 × 10."),
    ("C", "Existem 648 números de 3 algarismos distintos.",
     "9 × 9 × 8 (o primeiro não pode ser zero)."),
    ("E", "Com 4 tipos de munição, é possível montar 12 sequências de 3 cartuchos, permitida a repetição de tipos.",
     "Com repetição: 4³ = 64."),
], 10)

SOURCES = [
    "Análise combinatória.",
    SRC_R,
]
