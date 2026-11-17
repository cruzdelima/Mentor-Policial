# -*- coding: utf-8 -*-
"""Língua Portuguesa · Estrutura e formação de palavras — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "lp-formacao-01", "LP", "LP-18", "resumo", "Estrutura e formação de palavras", "Língua Portuguesa · Morfologia",
    "portugues_formacao", "Portugues_Formacao_Palavras_RESUMO.pdf", None, ["Estrutura e", "formação de palavras"], RES_SUB,
    RES_ITEMS("derivação, composição e sentido dos afixos"),
    "Tópico do edital: Estrutura e formação de palavras (Língua Portuguesa)",
    "Base: gramáticas de referência (Bechara; Cunha e Cintra).", 25)

THEORY = [
    exam("O que a banca cobra",
         "O **processo de formação** de palavras do texto e o **sentido dos afixos**."),
    h2("1. Derivação"),
    tb(["Processo", "Exemplos"], [0.3, 0.7], [
        ("Prefixal", "reabrir, desleal, ilegal"),
        ("Sufixal", "investigação, policial, rapidamente"),
        ("Prefixal e sufixal", "infelizmente, deslealdade (uma das formas existe)"),
        ("Parassintética", "entardecer, amanhecer, enriquecer (nenhuma forma intermediária existe)"),
        ("Regressiva", "combate, ataque, saque, pesca (substantivo de verbo)"),
        ("Imprópria", "o jantar, o sim, um não (mudança de classe)"),
    ]),
    h2("2. Composição"),
    bl("**Justaposição** (sem perda de som): girassol, passatempo, pontapé, guarda-chuva.",
       "**Aglutinação** (com perda de som): planalto, aguardente, embora, fidalgo."),
    h2("3. Outros"),
    bl("**Hibridismo**: automóvel, televisão, sociologia. **Abreviação**: moto, foto. **Sigla**: PF. **Onomatopeia**: tique-taque."),
    h2("4. Afixos"),
    bl("Negação: *a-, des-, in-*. Oposição: *anti-, contra-*. Repetição: *re-*. Antes: *pré-*. Depois: *pós-*.",
       "Agente: *-dor, -or, -ista*. Ação: *-ção, -mento*. Possibilidade: *-vel*. Modo: *-mente*."),
]

SUMMARY = [
    h2("Quadro: casos que confundem"),
    tb(["Palavra", "Processo", "Por quê"], [0.24, 0.3, 0.46], [
        ("entardecer", "Parassíntese", "Não existe tardecer nem entarde"),
        ("infelizmente", "Prefixal e sufixal", "Existe felizmente"),
        ("girassol", "Justaposição", "Sem perda de som"),
        ("planalto", "Aglutinação", "Perde o o de plano"),
        ("combate", "Regressiva", "Vem de combater"),
        ("o jantar", "Imprópria", "Verbo vira substantivo"),
        ("televisão", "Hibridismo", "Grego + latim"),
        ("foto", "Abreviação", "Redução de fotografia"),
    ]),
    h2("Leve para a prova"),
    bl("Parassíntese: **sem** formas intermediárias.",
       "Prefixal e sufixal: **uma** forma intermediária existe.",
       "Justaposição **não** perde som.",
       "Aglutinação **perde** som.",
       "Regressiva: verbo › substantivo **menor**.",
       "Imprópria: muda a **classe**, não a forma.",
       "Hibridismo: línguas **diferentes**.",
       "*Des-, in-, a-*: negação.",
       "*Re-*: repetição.",
       "*-or, -dor*: agente."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "FORMAÇÃO", "rootSub": "de palavras",
    "left": [
        {"label": "Estrutura", "items": ["radical", "prefixo e sufixo", "desinências"]},
        {"label": "Prefixal e sufixal", "items": ["reabrir", "investigação", "infelizmente"]},
        {"label": "Parassíntese", "items": ["entardecer", "enriquecer", "sem forma intermediária"]},
        {"label": "Regressiva", "items": ["combate", "saque", "verbo › substantivo"]},
        {"label": "Imprópria", "items": ["o jantar", "o sim", "muda a classe"]},
    ],
    "right": [
        {"label": "Justaposição", "items": ["girassol", "pontapé", "sem perda de som"]},
        {"label": "Aglutinação", "items": ["planalto", "aguardente", "com perda de som"]},
        {"label": "Outros", "items": ["hibridismo: automóvel", "abreviação: moto", "sigla: PF"]},
        {"label": "Prefixos", "items": ["des-, in-: negação", "re-: repetição", "anti-: oposição"]},
        {"label": "Sufixos", "items": ["-or: agente", "-ção: ação", "-vel: possibilidade"]},
    ],
}

QUIZ = quiz([
    ("C", "A palavra esclarecer é formada por derivação parassintética.",
     "Não existem clarecer nem esclaro: prefixo e sufixo entram juntos."),
    ("E", "A palavra desleal é formada por derivação parassintética.",
     "É derivação prefixal: des- + leal, e leal existe."),
    ("C", "O substantivo ataque é formado por derivação regressiva.",
     "Forma-se a partir do verbo atacar."),
    ("E", "A palavra passatempo é formada por aglutinação.",
     "Passa + tempo, sem perda de som: justaposição."),
    ("C", "A palavra embora resulta de aglutinação.",
     "Vem de em boa hora, com perda de sons."),
    ("E", "Em “Ele deu um não como resposta”, a palavra não resulta de derivação sufixal.",
     "O advérbio virou substantivo sem mudar de forma: derivação imprópria."),
    ("C", "Na palavra ilegal, o prefixo i- indica negação.",
     "Ilegal = não legal."),
    ("E", "Na palavra investigador, o sufixo -dor indica resultado da ação.",
     "O sufixo -dor indica agente: quem investiga."),
    ("C", "A palavra sociologia é um hibridismo.",
     "Socio (latim) + logia (grego)."),
    ("E", "A palavra moto é formada por derivação regressiva.",
     "É abreviação de motocicleta."),
], 10)

SOURCES = [GRAM, SRC_R]
