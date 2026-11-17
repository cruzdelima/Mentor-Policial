# -*- coding: utf-8 -*-
"""Língua Portuguesa · Crase — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "lp-crase-01", "LP", "LP-13", "resumo", "Crase", "Língua Portuguesa · Sintaxe",
    "portugues_crase", "Portugues_Crase_RESUMO.pdf", None, ["Crase:", "o acento grave"], RES_SUB,
    RES_ITEMS("casos obrigatórios, proibidos e facultativos"),
    "Tópico do edital: Emprego do sinal indicativo de crase (Língua Portuguesa)",
    "Base: gramáticas de referência (Bechara; Cunha e Cintra).", 30)

THEORY = [
    exam("O que a banca cobra",
         "Se o acento grave é **obrigatório, facultativo ou proibido**, e o **teste do masculino**."),
    h2("1. Regra"),
    bl("Crase = **preposição a** (regência) + **artigo a** (substantivo feminino) ou *a* de **aquele/aquela/aquilo**.",
       "**Teste do masculino**: se vira **ao**, há crase.",
       "**Teste da cidade**: *volto da* › crase; *volto de* › sem crase."),
    h2("2. Obrigatória"),
    bl("Regência + feminino com artigo: *à delegada, à audiência*.",
       "Locuções femininas: *às pressas, à noite, à vista, à medida que, à espera de*.",
       "Horas: *às 14h, à uma hora*. *À moda de*: *bife à milanesa*.",
       "*àquele, àquela, àquilo*; *à qual, às quais*.",
       "Casa e terra **determinadas**: *à casa dos pais*."),
    h2("3. Proibida"),
    bl("Masculino (*a prazo*), verbo (*a partir*), pronomes (*a ela, a Vossa Excelência*), *uma* (*a uma conclusão*).",
       "Palavras repetidas (*frente a frente*); *a* singular + plural (*a normas*).",
       "Cidade sem artigo (*a Recife*); *de… a* sem artigo (*de segunda a sexta*)."),
    h2("4. Facultativa"),
    bl("Possessivo feminino singular (*a/à sua chefe*), nome de mulher (*a/à Mariana*), depois de *até* (*até a/à delegacia*)."),
]

SUMMARY = [
    h2("Quadro rápido"),
    tb(["Situação", "Crase?", "Exemplo"], [0.4, 0.16, 0.44], [
        ("Verbo pede *a* + feminino", "Sim", "Refiro-me à lei."),
        ("Antes de masculino", "Não", "Comprou a prazo."),
        ("Antes de verbo", "Não", "Começou a chover."),
        ("Horas determinadas", "Sim", "Às 10h."),
        ("Pronome pessoal / tratamento", "Não", "Disse a ela."),
        ("Aquele / aquilo com preposição", "Sim", "Refiro-me àquilo."),
        ("Palavras repetidas", "Não", "Dia a dia."),
        ("A + plural", "Não", "Falou a pessoas."),
        ("Possessivo feminino singular", "Facultativa", "A/à sua chefe."),
        ("Cidade sem artigo", "Não", "Vou a Roma."),
    ]),
    h2("Leve para a prova"),
    bl("Precisa de **preposição** e **artigo** ao mesmo tempo.",
       "Teste do masculino: **ao** = crase.",
       "Volto **da** = crase; volto **de** = não.",
       "Nunca antes de **verbo** nem de **masculino**.",
       "Nunca antes de **ela, Vossa Excelência, uma**.",
       "Locução feminina: **às pressas, à noite**.",
       "Horas: **às** 10h; **à** uma hora.",
       "De… **a** (sem artigo) × **das… às** (com artigo).",
       "**Aquele** + preposição = **àquele**.",
       "Possessivo singular: **facultativa**."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "CRASE", "rootSub": "a + a",
    "left": [
        {"label": "Conceito", "items": ["preposição + artigo", "ou + aquele/aquilo", "acento grave"]},
        {"label": "Testes", "items": ["masculino: ao", "cidade: volto da", "regência do verbo"]},
        {"label": "Locuções", "items": ["às pressas, à noite", "à medida que", "à espera de"]},
        {"label": "Horas e moda", "items": ["às 14h", "à uma hora", "à milanesa"]},
        {"label": "Demonstrativos", "items": ["àquele setor", "àquilo", "à qual"]},
    ],
    "right": [
        {"label": "Proibida", "items": ["masculino: a prazo", "verbo: a partir", "a uma conclusão"]},
        {"label": "Pronomes", "items": ["a ela", "a Vossa Excelência", "a toda a equipe"]},
        {"label": "Repetição e plural", "items": ["frente a frente", "a normas", "de segunda a sexta"]},
        {"label": "Casa e terra", "items": ["voltou a casa", "à casa dos pais", "desceu a terra"]},
        {"label": "Facultativa", "items": ["à sua chefe", "à Mariana", "até à delegacia"]},
    ],
}

QUIZ = quiz([
    ("C", "Em “Nas férias, a equipe foi à praia”, o acento grave está corretamente empregado.",
     "Ir a + a praia: preposição e artigo."),
    ("E", "Em “O equipamento foi comprado à prazo”, o acento grave está corretamente empregado.",
     "Prazo é masculino: não há crase."),
    ("C", "Em “Às vezes, a perícia demora meses”, o acento grave marca locução adverbial feminina.",
     "Às vezes é locução adverbial feminina."),
    ("E", "Em “O delegado disse tudo à ela”, o acento grave está corretamente empregado.",
     "Não há crase antes de pronome pessoal."),
    ("C", "Em “Ninguém deu importância àquilo”, o acento grave está corretamente empregado.",
     "Dar importância a + aquilo."),
    ("E", "Em “A comitiva viajou à Roma em maio”, o acento grave está corretamente empregado.",
     "Teste: volto de Roma. Sem artigo, sem crase."),
    ("C", "Em “A reunião será à uma hora da tarde”, o acento grave está corretamente empregado.",
     "Indica hora determinada."),
    ("E", "Em “Começou à chover durante a operação”, o acento grave está corretamente empregado.",
     "Não há crase antes de verbo."),
    ("C", "Em “Pediu bife à milanesa”, o acento grave está corretamente empregado.",
     "Fica subentendida a expressão à moda de."),
    ("E", "Em “O trabalho é feito dia à dia”, o acento grave está corretamente empregado.",
     "Entre palavras repetidas não há crase."),
], 10)

SOURCES = [GRAM, SRC_R]
