# -*- coding: utf-8 -*-
"""Língua Portuguesa · Coesão e coerência textual — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "lp-coesao-01", "LP", "LP-16", "resumo", "Coesão e coerência textual", "Língua Portuguesa · Texto",
    "portugues_coesao", "Portugues_Coesao_Coerencia_RESUMO.pdf", None, ["Coesão e", "coerência textual"], RES_SUB,
    RES_ITEMS("referenciação, conectivos, elipse e coerência"),
    "Tópico do edital: Coesão e coerência textual (Língua Portuguesa)",
    "Base: gramáticas de referência e Koch, A coesão textual.", 30)

THEORY = [
    exam("O que a banca cobra",
         "**Referência** (“o termo X retoma Y”), **conectivos** e a diferença entre coesão e coerência. Substitua o termo pelo referente e teste."),
    h2("1. Conceitos"),
    bl("**Coesão**: ligação linguística (pronomes, conectivos, sinônimos).",
       "**Coerência**: unidade de sentido, sem contradição. Conectivo não garante coerência."),
    h2("2. Coesão referencial"),
    bl("**Anáfora** retoma; **catáfora** antecipa.",
       "Mecanismos: pronomes, sinônimos, **hiperônimos** (*fuzil › a arma*), expressões nominais (*a fuga*), **elipse**, advérbios (*lá, aí*), numerais (*o último*).",
       "**Esse** retoma; **este** anuncia ou indica o mais próximo; **aquele**, o mais distante."),
    h2("3. Coesão sequencial"),
    bl("Conectivos e articuladores: *além disso, porém, portanto, em síntese*.",
       "Marcadores temporais ordenam os fatos."),
    h2("4. Coerência"),
    bl("Não contradição, continuidade do tema, progressão e compatibilidade com o mundo.",
       "O conectivo deve combinar com o conteúdo."),
]

SUMMARY = [
    h2("Quadro: mecanismos de coesão"),
    tb(["Mecanismo", "Exemplo"], [0.36, 0.64], [
        ("Pronome", "O réu negou. **Ele** mentiu."),
        ("Sinônimo", "O **carro**… o **veículo**…"),
        ("Hiperônimo", "O **fuzil**… a **arma**…"),
        ("Expressão nominal", "Fugiu pela janela. **A fuga**…"),
        ("Elipse", "Chegaram e **(eles)** isolaram a área."),
        ("Advérbio", "Fomos a Recife. **Lá**…"),
        ("Conectivo", "Confessou; **porém**, recorreu."),
    ]),
    h2("Leve para a prova"),
    bl("Substitua o termo pelo referente proposto.",
       "Confira **concordância** e **sentido** do referente.",
       "Pronome nem sempre retoma o termo **mais próximo**.",
       "**Esse** = anáfora; **este** = catáfora.",
       "Hiperônimo retoma hipônimo (*fuzil › arma*).",
       "Elipse: termo omitido e identificável.",
       "Relativo retoma o antecedente.",
       "Coesão ≠ coerência.",
       "Contradição = incoerência.",
       "Progressão = informação nova."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "COESÃO E COERÊNCIA", "rootSub": "ligação e sentido",
    "left": [
        {"label": "Coesão", "items": ["ligação linguística", "superfície do texto", "pronomes e conectivos"]},
        {"label": "Anáfora e catáfora", "items": ["anáfora: retoma", "catáfora: antecipa", "esse × este"]},
        {"label": "Retomada", "items": ["sinônimos", "hiperônimos", "expressões nominais"]},
        {"label": "Elipse", "items": ["termo omitido", "identificável", "sujeito oculto"]},
        {"label": "Outros", "items": ["lá, aí", "o primeiro, o último", "relativos"]},
    ],
    "right": [
        {"label": "Sequencial", "items": ["conectivos", "articuladores", "tempos verbais"]},
        {"label": "Coerência", "items": ["sentido", "sem contradição", "relação com o mundo"]},
        {"label": "Progressão", "items": ["mantém o tema", "acrescenta dados", "não repete à toa"]},
        {"label": "Teste", "items": ["substitua o termo", "confira concordância", "confira o sentido"]},
        {"label": "Pegadinhas", "items": ["referente não é o mais próximo", "conectivo incoerente", "repetição excessiva"]},
    ],
}

T = "O agente abordou o motorista e pediu os documentos dele. Como o homem estava nervoso, o policial redobrou a atenção."

QUIZ = quiz([
    ("C", "A expressão o homem retoma o motorista.",
     "É uma expressão nominal que retoma o referente já mencionado.", T),
    ("E", "O pronome dele refere-se ao agente.",
     "Os documentos são do motorista."),
    ("C", "A expressão o policial retoma O agente.",
     "Policial é sinônimo contextual de agente."),
    ("E", "O conector Como introduz ideia de comparação.",
     "Anteposto à principal, como tem valor causal."),
    ("C", "Hiperônimos podem retomar hipônimos, como em “o revólver… a arma”.",
     "O termo geral retoma o específico."),
    ("E", "A catáfora consiste na retomada de um termo já mencionado.",
     "Retomar é anáfora; catáfora antecipa o que virá."),
    ("C", "A elipse é um mecanismo de coesão em que um termo identificável pelo contexto é omitido.",
     "Ex.: Chegaram cedo e (eles) isolaram a área."),
    ("E", "Todo texto coeso é necessariamente coerente.",
     "Um texto pode ter elementos coesivos e ser contraditório."),
    ("C", "Em “O suspeito fugiu. A fuga foi filmada”, a fuga é expressão nominal que retoma o fato narrado antes.",
     "O substantivo resume a ação anterior."),
    ("E", "Os pronomes relativos não exercem função coesiva, pois apenas ligam orações.",
     "Retomam um antecedente: são coesivos."),
], 10)

SOURCES = [GRAM, SRC_R]
