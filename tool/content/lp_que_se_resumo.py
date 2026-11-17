# -*- coding: utf-8 -*-
"""Língua Portuguesa · Funções do "que" e do "se" — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "lp-que-se-01", "LP", "LP-23", "resumo", "Funções do “que” e do “se”", "Língua Portuguesa · Morfossintaxe",
    "portugues_que_se", "Portugues_Funcoes_Que_Se_RESUMO.pdf", None, ["Funções do", "“que” e do “se”"], RES_SUB,
    RES_ITEMS("classes do que e do se e os testes de reconhecimento"),
    "Tópico do edital: Funções do “que” e do “se” (Língua Portuguesa)",
    "Base: gramáticas de referência (Bechara; Cunha e Cintra).", 30)

THEORY = [
    exam("O que a banca cobra",
         "Classificar o *que* e o *se* e as consequências: **concordância** e **pontuação**."),
    h2("1. Que"),
    bl("**Relativo** (troca por *o qual*): *o laudo que chegou*.",
       "**Integrante** (oração = *isso*): *soube que chegou*.",
       "**Conjunção**: consecutiva (*tanto que*), comparativa (*mais que*), explicativa (*venha, que…*).",
       "**Interrogativo**: *Que houve?* **Advérbio**: *Que difícil!* **Preposição**: *tenho que sair*.",
       "**Expletivo**: *quase que caí; eu é que decidi*. **Substantivo**: *um quê*. **Interjeição**: *Quê!*"),
    h2("2. Se"),
    bl("**Reflexivo**: *ele se feriu*. **Recíproco**: *se acusaram*.",
       "**Apassivador** (VTD + se; verbo concorda): *vendem-se casas*.",
       "**Indeterminador** (VTI/VI/VL + se; singular): *precisa-se de agentes*.",
       "**Parte do verbo**: *queixar-se, arrepender-se*. **Expletivo**: *foi-se embora*.",
       "**Conjunção condicional** (= caso) e **integrante** (*não sei se…*)."),
]

SUMMARY = [
    h2("Quadro de testes"),
    tb(["Teste", "Resultado"], [0.56, 0.44], [
        ("Que troca por o qual", "Pronome relativo"),
        ("Oração com que vira isso", "Conjunção integrante"),
        ("Que pode ser retirado", "Partícula expletiva"),
        ("Ter que = ter de", "Preposição"),
        ("VTD + se › ser + particípio", "Partícula apassivadora"),
        ("VTI/VI + se", "Índice de indeterminação"),
        ("Se = caso", "Conjunção condicional"),
        ("Oração com se vira isso", "Conjunção integrante"),
    ]),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "QUE E SE", "rootSub": "classes e funções",
    "left": [
        {"label": "Que relativo", "items": ["troca por o qual", "retoma antecedente", "tem função sintática"]},
        {"label": "Que integrante", "items": ["oração = isso", "só liga", "espero que…"]},
        {"label": "Que conjunção", "items": ["tanto que: consequência", "mais que: comparação", "venha, que: explicação"]},
        {"label": "Que: outros", "items": ["que difícil: advérbio", "tenho que: preposição", "um quê: substantivo"]},
        {"label": "Que expletivo", "items": ["quase que caí", "eu é que decidi", "pode sair"]},
    ],
    "right": [
        {"label": "Se pronome", "items": ["reflexivo: se feriu", "recíproco: se acusaram", "parte do verbo: queixar-se"]},
        {"label": "Apassivador", "items": ["VTD + se", "verbo concorda", "vendem-se casas"]},
        {"label": "Indeterminador", "items": ["VTI/VI + se", "singular", "precisa-se de"]},
        {"label": "Se conjunção", "items": ["condicional: caso", "integrante: não sei se", "causal: já que"]},
        {"label": "Se expletivo", "items": ["foi-se embora", "passaram-se os dias", "pode sair"]},
    ],
}

QUIZ = quiz([
    ("C", "Em “A testemunha que depôs ontem foi ameaçada”, o que é pronome relativo.",
     "Retoma testemunha: a qual depôs ontem."),
    ("E", "Em “Afirmou que não estava no local”, o que é pronome relativo.",
     "A oração equivale a isso: conjunção integrante."),
    ("C", "Em “Tenho que comparecer à audiência”, o que equivale à preposição de.",
     "Ter que = ter de."),
    ("E", "Em “Que operação bem planejada!”, o que é conjunção integrante.",
     "Acompanha o substantivo em exclamação: pronome indefinido (adjetivo)."),
    ("C", "Em “Investigaram-se as denúncias”, o se é partícula apassivadora.",
     "As denúncias foram investigadas."),
    ("E", "Em “Vive-se bem nesta cidade”, o se é partícula apassivadora.",
     "Viver é intransitivo: o se indetermina o sujeito."),
    ("C", "Em “O réu queixou-se do tratamento”, o se é parte integrante do verbo.",
     "Queixar-se é verbo pronominal."),
    ("E", "Em “Se chover, a operação será adiada”, o se é conjunção integrante.",
     "Introduz condição: conjunção condicional."),
    ("C", "Em “Os dois agentes se cumprimentaram”, o se tem valor recíproco.",
     "A ação é mútua."),
    ("E", "Em “Aluga-se salas comerciais”, a concordância está correta, pois o se indetermina o sujeito.",
     "Alugar é transitivo direto: alugam-se salas comerciais (passiva sintética)."),
], 10)

SOURCES = [GRAM, SRC_R]
