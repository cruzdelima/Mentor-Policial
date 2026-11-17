# -*- coding: utf-8 -*-
"""Língua Portuguesa · Variação linguística — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "lp-variacao-01", "LP", "LP-24", "resumo", "Variação linguística", "Língua Portuguesa · Linguagem",
    "portugues_variacao", "Portugues_Variacao_Linguistica_RESUMO.pdf", None, ["Variação", "linguística"], RES_SUB,
    RES_ITEMS("tipos de variação, normas e adequação"),
    "Tópico do edital: Variação linguística (Língua Portuguesa)",
    "Base: gramáticas de referência e Bagno, Preconceito linguístico.", 20)

THEORY = [
    exam("O que a banca cobra",
         "O **tipo** de variação, a **adequação** ao contexto e o **preconceito linguístico**."),
    h2("1. Tipos"),
    tb(["Tipo", "Depende de", "Exemplo"], [0.28, 0.28, 0.44], [
        ("Diatópica", "Região", "mandioca / aipim / macaxeira"),
        ("Diastrática", "Grupo social", "gírias, jargão profissional"),
        ("Diafásica", "Situação", "Prezado senhor × E aí?"),
        ("Diacrônica", "Tempo", "vossa mercê › você"),
        ("Diamésica", "Fala × escrita", "tá × está"),
    ]),
    h2("2. Normas e adequação"),
    bl("**Norma-padrão**: modelo das gramáticas, referência dos textos oficiais e das provas.",
       "**Norma culta**: uso real de falantes escolarizados. **Variedades populares**: têm regras próprias.",
       "**Adequação**: a variedade deve combinar com a situação.",
       "**Preconceito linguístico**: discriminar pelo modo de falar. Nenhuma variedade é inferior."),
]

SUMMARY = [
    h2("Leve para a prova"),
    bl("Região = **diatópica**.",
       "Grupo social = **diastrática**.",
       "Situação = **diafásica**.",
       "Tempo = **diacrônica**.",
       "Jargão = profissão; gíria = grupo; regionalismo = região.",
       "Variação **não** é erro.",
       "Documento oficial = **norma-padrão**.",
       "Adequação depende do **contexto**.",
       "Formal demais também pode ser inadequado.",
       "Preconceito linguístico: as bancas o condenam."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "VARIAÇÃO", "rootSub": "linguística",
    "left": [
        {"label": "Regional", "items": ["diatópica", "sotaques", "mandioca / aipim"]},
        {"label": "Social", "items": ["diastrática", "gírias", "jargão profissional"]},
        {"label": "Situacional", "items": ["diafásica", "formal × informal", "registro"]},
        {"label": "Histórica", "items": ["diacrônica", "vossa mercê › você", "pharmacia › farmácia"]},
        {"label": "Fala e escrita", "items": ["diamésica", "tá × está", "pra × para"]},
    ],
    "right": [
        {"label": "Norma-padrão", "items": ["gramáticas", "textos oficiais", "provas"]},
        {"label": "Norma culta", "items": ["uso real", "falantes escolarizados", "mais flexível"]},
        {"label": "Populares", "items": ["regras próprias", "nós vai", "os menino"]},
        {"label": "Adequação", "items": ["contexto decide", "ofício: padrão", "bilhete: informal"]},
        {"label": "Preconceito", "items": ["discriminar pela fala", "nenhuma é inferior", "bancas condenam"]},
    ],
}

QUIZ = quiz([
    ("C", "O uso de palavras diferentes para o mesmo objeto em regiões distintas do país é exemplo de variação diatópica.",
     "Diatópica = regional."),
    ("E", "A variação diastrática está ligada às mudanças da língua ao longo do tempo.",
     "Diastrática é social; a temporal é diacrônica."),
    ("C", "A linguagem informal é adequada em uma conversa entre amigos.",
     "Adequação depende da situação."),
    ("E", "Em um relatório oficial, o emprego de gírias é adequado se o destinatário as conhecer.",
     "Documentos oficiais exigem a norma-padrão."),
    ("C", "Jargão é o vocabulário técnico de um grupo profissional.",
     "Ex.: oitiva, flagrante, auto de prisão."),
    ("E", "As variedades populares da língua não possuem regras.",
     "Todas as variedades têm regras próprias."),
    ("C", "O preconceito linguístico é a discriminação de pessoas pelo modo como falam.",
     "Atinge sotaques e variedades populares."),
    ("E", "A passagem de vossa mercê a você é exemplo de variação situacional.",
     "É variação histórica (diacrônica)."),
    ("C", "A norma-padrão é a referência para os textos oficiais.",
     "Ofícios, relatórios e documentos seguem a norma-padrão."),
    ("E", "Variação linguística e erro gramatical são conceitos equivalentes.",
     "A variação é natural; o erro é avaliado em relação à norma-padrão em contextos formais."),
], 10)

SOURCES = [GRAM, SRC_R]
