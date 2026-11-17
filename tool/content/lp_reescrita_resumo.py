# -*- coding: utf-8 -*-
"""Língua Portuguesa · Reescrita de frases e parágrafos — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "lp-reescrita-01", "LP", "LP-17", "resumo", "Reescrita de frases e parágrafos", "Língua Portuguesa · Texto",
    "portugues_reescrita", "Portugues_Reescrita_RESUMO.pdf", None, ["Reescrita de frases", "e parágrafos"], RES_SUB,
    RES_ITEMS("método, transformações e armadilhas"),
    "Tópico do edital: Reescrita de frases e parágrafos do texto (Língua Portuguesa)",
    "Base: gramáticas de referência (Bechara; Cunha e Cintra).", 35)

THEORY = [
    exam("O que a banca cobra",
         "Se a reescrita mantém **correção** e **sentido**. Compare as versões palavra por palavra."),
    h2("1. Método"),
    bl("**1º correção**: concordância, regência, crase, pontuação, colocação, tempos.",
       "**2º sentido**: conectivo, tempo verbal, voz, palavras de foco, vírgulas da adjetiva, ordem dos termos.",
       "Um problema basta para o item ser **errado**."),
    h2("2. Transformações"),
    bl("**Passiva**: *ser* no tempo da ativa; particípio concorda; só VTD.",
       "**Indireto**: presente › imperfeito; perfeito › mais-que-perfeito; futuro › futuro do pretérito; imperativo › subjuntivo; "
       "*eu › ele; aqui › ali; hoje › naquele dia; ontem › no dia anterior*.",
       "**Nominalização**: *decidiu › a decisão*.",
       "**Reduzidas**: *ao chegar = quando chegou; elaborado = que foi elaborado*.",
       "**Conectivos**: mesmo grupo mantém; grupo diferente altera. *Embora + subjuntivo = apesar de + infinitivo*."),
]

SUMMARY = [
    h2("Quadro: mantém ou altera?"),
    tb(["Mudança", "Resultado"], [0.64, 0.36], [
        ("Ativa › passiva no mesmo tempo", "Mantém"),
        ("Ativa no futuro › passiva no passado", "Altera"),
        ("Tirar vírgulas da adjetiva explicativa", "Altera"),
        ("Mover *só* do sujeito para o verbo", "Altera"),
        ("*Teria fugido* › *fugiu*", "Altera"),
        ("*mas* › *porém*", "Mantém"),
        ("*Como chovia* › *Chovia; por isso*", "Mantém"),
        ("*que foi elaborado* › *elaborado*", "Mantém"),
        ("*Disse-me* › *Me disse*", "Erro"),
        ("*Caso colabore* › *Caso colabora*", "Erro"),
    ]),
    h2("Leve para a prova"),
    bl("Correção **e** sentido: julgue os dois.",
       "Marque **todas** as diferenças entre as versões.",
       "Tempo verbal mudou? Sentido mudou.",
       "Vírgulas da adjetiva: **cuidado**.",
       "Palavras de foco (*só, até, ainda*) mudam de lugar? Confira.",
       "Passiva: só com **VTD**.",
       "Indireto: tempos **recuam**.",
       "Concessiva: subjuntivo ou *apesar de* + infinitivo.",
       "Novo conectivo: mesmo **grupo**?",
       "Colocação pronominal após deslocamento."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "REESCRITA", "rootSub": "correção e sentido",
    "left": [
        {"label": "Método", "items": ["1º correção", "2º sentido", "um erro basta"]},
        {"label": "Correção", "items": ["concordância e regência", "crase e pontuação", "colocação e tempos"]},
        {"label": "Sentido", "items": ["conectivos", "tempos verbais", "palavras de foco"]},
        {"label": "Voz passiva", "items": ["ser no tempo da ativa", "particípio concorda", "só VTD"]},
        {"label": "Discurso indireto", "items": ["vou › ia", "vi › tinha visto", "aqui › ali"]},
    ],
    "right": [
        {"label": "Nominalização", "items": ["decidiu › decisão", "terminou › término", "mantém sentido"]},
        {"label": "Reduzidas", "items": ["ao chegar = quando chegou", "elaborado = que foi", "sendo = como é"]},
        {"label": "Conectivos", "items": ["mesmo grupo: mantém", "outro grupo: altera", "embora › apesar de"]},
        {"label": "Armadilhas", "items": ["vírgula da adjetiva", "teria › fugiu", "só muda de lugar"]},
        {"label": "Erros", "items": ["me disse (início)", "caso colabora", "se apure os fatos"]},
    ],
}

QUIZ = quiz([
    ("C", "A reescrita de “A comissão aprovou o relatório” como “O relatório foi aprovado pela comissão” mantém a correção e o sentido.",
     "Transposição correta para a voz passiva, no mesmo tempo."),
    ("E", "A reescrita de “O juiz decidirá o caso” como “O caso foi decidido pelo juiz” mantém o sentido original.",
     "O tempo mudou: o caso será decidido."),
    ("C", "Em discurso indireto, “Ele disse: — Estou cansado” passa a “Ele disse que estava cansado”.",
     "O presente passa ao pretérito imperfeito."),
    ("E", "A reescrita de “O réu, que confessou, foi solto” como “O réu que confessou foi solto” mantém o sentido.",
     "A oração passa de explicativa a restritiva."),
    ("C", "A substituição de mas por porém, com o ajuste da pontuação, mantém a relação de oposição.",
     "Ambas são adversativas."),
    ("E", "A reescrita de “Embora chovesse, a operação ocorreu” como “Apesar de chovesse, a operação ocorreu” mantém a correção.",
     "Apesar de exige infinitivo: apesar de chover."),
    ("C", "A reescrita de “Quando chegou à delegacia, o advogado pediu vista” como “Ao chegar à delegacia, o advogado pediu vista” mantém o sentido.",
     "A reduzida de infinitivo com ao tem valor temporal."),
    ("E", "A reescrita de “O suspeito teria fugido” como “O suspeito fugiu” mantém o sentido.",
     "A hipótese passa a ser apresentada como fato."),
    ("C", "A reescrita de “A polícia investigou o caso” como “O caso foi investigado pela polícia” preserva o sentido original.",
     "Voz passiva analítica no mesmo tempo."),
    ("E", "A reescrita de “Disseram-me a verdade” como “Me disseram a verdade” mantém a correção segundo a norma-padrão.",
     "Não se inicia período com pronome oblíquo átono no padrão formal."),
], 10)

SOURCES = [GRAM, SRC_R]
