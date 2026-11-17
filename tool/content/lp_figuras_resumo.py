# -*- coding: utf-8 -*-
"""Língua Portuguesa · Figuras de linguagem — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "lp-figuras-01", "LP", "LP-21", "resumo", "Figuras de linguagem", "Língua Portuguesa · Semântica e estilística",
    "portugues_figuras", "Portugues_Figuras_Linguagem_RESUMO.pdf", None, ["Figuras", "de linguagem"], RES_SUB,
    RES_ITEMS("figuras de palavra, pensamento, construção e som"),
    "Tópico do edital: Figuras de linguagem (Língua Portuguesa)",
    "Base: gramáticas de referência (Bechara; Cunha e Cintra).", 25)

THEORY = [
    exam("O que a banca cobra",
         "Identificar a figura no trecho e seu **efeito**. Atenção aos pares parecidos."),
    h2("1. De palavra"),
    bl("**Metáfora**: comparação sem conectivo (*é uma fera*). **Comparação**: com conectivo (*forte como um touro*).",
       "**Metonímia**: relação real (*li Machado; bebi um copo*). **Catacrese**: *pé da mesa*. **Sinestesia**: *grito áspero*."),
    h2("2. De pensamento"),
    bl("**Antítese**: opostos lado a lado. **Paradoxo**: opostos no mesmo ser (*dor que não dói*).",
       "**Hipérbole**: exagero. **Eufemismo**: suavização. **Ironia**: o contrário, com crítica.",
       "**Personificação**: humano em não humano. **Gradação**: sequência crescente."),
    h2("3. De construção"),
    bl("**Elipse**: omissão de termo identificável. **Zeugma**: omissão de termo já citado.",
       "**Pleonasmo**: literário (ênfase) × vicioso (*subir para cima*).",
       "**Polissíndeto**: muitos *e*. **Assíndeto**: sem conectivos. **Anáfora**: repetição no início."),
    h2("4. De som"),
    bl("**Aliteração** (consoantes), **assonância** (vogais), **onomatopeia** (sons)."),
]

SUMMARY = [
    h2("Quadro: pares que confundem"),
    tb(["Par", "Diferença"], [0.34, 0.66], [
        ("Metáfora × comparação", "Sem conectivo × com conectivo"),
        ("Antítese × paradoxo", "Opostos lado a lado × opostos no mesmo ser"),
        ("Eufemismo × ironia", "Suaviza × diz o contrário"),
        ("Hipérbole × gradação", "Exagero × sequência crescente"),
        ("Elipse × zeugma", "Termo identificável × termo já citado"),
        ("Polissíndeto × assíndeto", "Repete conectivo × sem conectivo"),
        ("Metonímia × metáfora", "Relação real × semelhança"),
    ]),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "FIGURAS", "rootSub": "de linguagem",
    "left": [
        {"label": "Metáfora", "items": ["sem conectivo", "é uma fera", "≠ comparação"]},
        {"label": "Metonímia", "items": ["li Machado", "bebi um copo", "relação real"]},
        {"label": "Outras de palavra", "items": ["catacrese: pé da mesa", "sinestesia: grito áspero", "comparação: como"]},
        {"label": "Opostos", "items": ["antítese: riso e choro", "paradoxo: dor sem doer", "mesmo ser = paradoxo"]},
        {"label": "Intensidade", "items": ["hipérbole: morri de rir", "gradação: andei, corri", "eufemismo: suaviza"]},
    ],
    "right": [
        {"label": "Ironia e prosopopeia", "items": ["ironia: o contrário", "personificação", "a cidade dormia"]},
        {"label": "Omissão", "items": ["elipse: apenas silêncio", "zeugma: ele, chá", "termo já citado"]},
        {"label": "Conectivos", "items": ["polissíndeto: e, e, e", "assíndeto: vim, vi, venci", "anáfora: repetição"]},
        {"label": "Pleonasmo", "items": ["literário: ênfase", "vicioso: subir para cima", "elo de ligação"]},
        {"label": "Som", "items": ["aliteração: consoantes", "assonância: vogais", "onomatopeia"]},
    ],
}

QUIZ = quiz([
    ("C", "Em “A notícia caiu como uma bomba na delegacia”, há comparação.",
     "O conectivo como explicita a comparação."),
    ("E", "Em “O Brasil inteiro assistiu ao jogo”, há eufemismo.",
     "O todo (o Brasil) representa parte das pessoas: metonímia (ou hipérbole)."),
    ("C", "Em “Um silêncio ensurdecedor tomou conta da sala”, há paradoxo.",
     "Silêncio e ensurdecedor se fundem num mesmo ser, com contradição aparente."),
    ("E", "Em “Já te expliquei um milhão de vezes”, há gradação.",
     "É hipérbole: exagero intencional."),
    ("C", "Em “O vento sussurrava nas janelas”, há personificação.",
     "Atribui-se ao vento uma ação humana."),
    ("E", "Em “Ela é uma flor”, há comparação.",
     "Sem conectivo, trata-se de metáfora."),
    ("C", "Expressões como “elo de ligação” e “há anos atrás” são pleonasmos viciosos.",
     "Repetem ideias sem valor expressivo."),
    ("E", "Em “Vim, vi, venci”, há polissíndeto.",
     "A ausência de conectivos caracteriza o assíndeto."),
    ("C", "Em “O doce perfume da manhã”, há sinestesia.",
     "Mistura paladar (doce) e olfato (perfume)."),
    ("E", "A antítese consiste em atribuir características humanas a seres inanimados.",
     "Isso é personificação; antítese é a aproximação de ideias opostas."),
], 10)

SOURCES = [GRAM, SRC_R]
