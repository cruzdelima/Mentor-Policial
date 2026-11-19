# -*- coding: utf-8 -*-
"""Raciocínio Lógico · Tabela-verdade, tautologia e contradição — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "rlm-tabela-01", "RLM", "RLM-02", "resumo", "Tabela-verdade, tautologia e contradição", "Raciocínio Lógico e Matemática · Lógica proposicional",
    "raciocinio_tabela_verdade", "RaciocinioLogico_TabelaVerdade_RESUMO.pdf", None, ["Tabela-verdade"], RES_SUB,
    RES_ITEMS("linhas, montagem, tautologia e atalhos"),
    "Tópico do edital: Tabela-verdade, tautologia e contradição — Raciocínio Lógico",
    "Base: lógica proposicional clássica.", 25)

THEORY = [
    exam("O que a banca cobra",
         "**Número de linhas**, **valor de uma linha** e se a proposição é **tautologia, contradição ou contingência**."),
    h2("1. Linhas"),
    bl("**2ⁿ linhas**, sendo n o número de proposições simples **distintas**.",
       "Letra repetida ou negada (P e ¬P) conta **uma vez**.",
       "3 letras: colunas VVVVFFFF, VVFFVVFF, VFVFVFVF."),
    h2("2. Classificação"),
    bl("**Tautologia**: só V (ex.: P ∨ ¬P, (P ∧ Q) → P, P → (P ∨ Q)).",
       "**Contradição**: só F (ex.: P ∧ ¬P, P ↔ ¬P).",
       "**Contingência**: V e F (ex.: P → Q, P ∧ Q).",
       "A negação de uma tautologia é contradição."),
    h2("3. Atalho"),
    bl("Para testar se A → B é tautologia, suponha **A = V e B = F**.",
       "Se isso for **impossível**, é tautologia; se for possível, não é.",
       "Para contar linhas V, conte as F e subtraia do total."),
]

SUMMARY = [
    h2("Quadro rápido"),
    tb(["Proposição", "Linhas V (de 4)", "Classificação"], [0.4, 0.26, 0.34], [
        ("P ∧ Q", "1", "Contingência"),
        ("P ∨ Q", "3", "Contingência"),
        ("P → Q", "3", "Contingência"),
        ("P ↔ Q", "2", "Contingência"),
        ("P ∨ ¬P", "4 (de 2)", "Tautologia"),
        ("P ∧ ¬P", "0 (de 2)", "Contradição"),
        ("[(P → Q) ∧ P] → Q", "4", "Tautologia (modus ponens)"),
        ("[(P → Q) ∧ Q] → P", "3", "Contingência (falácia)"),
    ]),
    h2("Leve para a prova"),
    bl("Linhas: **2ⁿ** (letras distintas).",
       "Tautologia: **só V**.",
       "Contradição: **só F**.",
       "Contingência: **V e F**.",
       "Atalho: força o caso **V → F**.",
       "Resolva de **dentro para fora**.",
       "Modus ponens é tautologia; afirmar o consequente, não."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "TABELA-VERDADE", "rootSub": "e classificação",
    "left": [
        {"label": "Linhas", "items": ["2 elevado a n", "n = letras distintas", "negação não conta"]},
        {"label": "Montagem", "items": ["todas as combinações", "de dentro para fora", "conectivo principal"]},
        {"label": "3 letras", "items": ["8 linhas", "4 em 4, 2 em 2", "1 em 1"]},
        {"label": "Contar linhas", "items": ["conte as falsas", "subtraia do total", "ou conte as V"]},
        {"label": "Exemplos", "items": ["P e Q: 1 linha V", "P ou Q: 3 linhas V", "se então: 3 linhas V"]},
    ],
    "right": [
        {"label": "Tautologia", "items": ["só V", "P ou não P", "modus ponens"]},
        {"label": "Contradição", "items": ["só F", "P e não P", "P sse não P"]},
        {"label": "Contingência", "items": ["V e F", "P então Q", "a maioria"]},
        {"label": "Atalho", "items": ["force V e F", "impossível: tautologia", "possível: não é"]},
        {"label": "Negação", "items": ["de tautologia", "vira contradição", "e vice-versa"]},
    ],
}

QUIZ = quiz([
    ("C", "A tabela-verdade de (P ∨ Q) ↔ (R ∧ S) tem 16 linhas.",
     "Quatro letras distintas: 2⁴ = 16."),
    ("E", "A tabela-verdade de P → (¬P ∨ Q) tem 8 linhas.",
     "Só P e Q: 4 linhas."),
    ("C", "A proposição P → P é uma tautologia.",
     "Nunca ocorre V → F com a mesma letra."),
    ("E", "A proposição P ∧ Q é uma tautologia.",
     "É falsa em três linhas: contingência."),
    ("C", "A proposição ¬(P ∨ ¬P) é uma contradição.",
     "É a negação de uma tautologia."),
    ("C", "A proposição P → Q é verdadeira em três das quatro linhas da tabela-verdade.",
     "Só é falsa em V → F."),
    ("E", "A proposição (P → Q) → P é uma tautologia.",
     "Com P = F, P → Q = V e o consequente P = F: V → F, falsa."),
    ("C", "Se P é falsa e Q é verdadeira, então (P ∧ Q) → P é verdadeira.",
     "Antecedente F: a condicional é verdadeira."),
    ("C", "A proposição [(P → Q) ∧ P] → Q é uma tautologia.",
     "É o modus ponens."),
    ("E", "Em uma tabela-verdade com 32 linhas, há 6 proposições simples distintas.",
     "2⁵ = 32: são 5 proposições simples."),
], 10)

SOURCES = [
    "Lógica proposicional clássica.",
    SRC_R,
]
