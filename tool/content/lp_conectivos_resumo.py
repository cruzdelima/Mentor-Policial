# -*- coding: utf-8 -*-
"""Língua Portuguesa · Advérbio, preposição e conjunção — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "lp-conectivos-01", "LP", "LP-07", "resumo", "Advérbio, preposição e conjunção", "Língua Portuguesa · Morfossintaxe",
    "portugues_conectivos", "Portugues_Conectivos_RESUMO.pdf", None, ["Advérbio, preposição", "e conjunção"], RES_SUB,
    RES_ITEMS("advérbios invariáveis, preposições e o sentido das conjunções"),
    "Tópico do edital: Advérbio, preposição e conjunção (Língua Portuguesa)",
    "Base: gramáticas de referência (Bechara; Cunha e Cintra).", 40)

THEORY = [
    exam("O que a banca cobra",
         "**Sentido** do conector e **substituições** que mantêm ou alteram esse sentido. Em segundo plano: *meio, bastante, a × há, sob × sobre, mal × mau*."),
    h2("1. Advérbio"),
    bl("Invariável; modifica verbo, adjetivo, advérbio ou a oração inteira.",
       "**meio** (= um pouco) e **bastante** (= muito) junto de adjetivo **não variam**: *meio nervosa; bastante cansados*.",
       "**Mal** (× bem) é advérbio; **mau** (× bom) é adjetivo.",
       "A **posição** de *só, somente, apenas, até* muda o sentido."),
    h2("2. Preposição"),
    bl("Liga termos. Essenciais: *a, ante, após, até, com, contra, de, desde, em, entre, para, perante, por, sem, sob, sobre, trás*.",
       "**há** = passado (*há três meses*); **a** = futuro ou distância (*daqui a dois dias*).",
       "**sob** = sujeição (*sob sigilo*); **sobre** = em cima, a respeito.",
       "Sujeito de infinitivo não se contrai (tradição): *antes **de o** juiz decidir*."),
    h2("3. Conjunções coordenativas"),
    tb(["Tipo", "Conjunções"], [0.22, 0.78], [
        ("Aditivas", "e, nem, não só… mas também"),
        ("Adversativas", "mas, porém, contudo, todavia, entretanto, no entanto"),
        ("Alternativas", "ou, ora… ora, quer… quer"),
        ("Conclusivas", "logo, portanto, por isso, por conseguinte, pois (posposto)"),
        ("Explicativas", "porque, que, porquanto, pois (anteposto)"),
    ]),
    h2("4. Conjunções subordinativas adverbiais"),
    tb(["Tipo", "Conjunções"], [0.22, 0.78], [
        ("Causal", "porque, como (anteposto), já que, visto que, uma vez que"),
        ("Concessiva", "embora, ainda que, mesmo que, conquanto (+ subjuntivo)"),
        ("Condicional", "se, caso, desde que + subjuntivo, contanto que"),
        ("Conformativa", "conforme, segundo, consoante, como"),
        ("Consecutiva", "tão/tanto/tal… que, de modo que"),
        ("Final", "para que, a fim de que"),
        ("Proporcional", "à medida que, à proporção que"),
        ("Temporal", "quando, assim que, logo que, desde que + indicativo"),
    ]),
    trap("Duplo sentido",
         "*desde que* (condição × tempo) · *como* (causa × conformidade × comparação) · *pois* (explicação × conclusão) · "
         "*à medida que* (proporção) × *na medida em que* (causa)."),
]

SUMMARY = [
    h2("Quadro: troca mantém ou altera?"),
    tb(["Troca", "Resultado", "Motivo"], [0.36, 0.2, 0.44], [
        ("mas › porém / contudo", "Mantém", "Todas adversativas"),
        ("portanto › logo / por isso", "Mantém", "Todas conclusivas"),
        ("porque › visto que", "Mantém", "Ambas causais"),
        ("embora › ainda que", "Mantém", "Ambas concessivas, com subjuntivo"),
        ("porém › portanto", "Altera", "Oposição vira conclusão"),
        ("à medida que › na medida em que", "Altera", "Proporção vira causa"),
        ("embora haja › apesar de haja", "Erro", "Apesar de pede infinitivo: apesar de haver"),
        ("há três anos › a três anos", "Erro", "Passado pede há"),
        ("meio nervosa › meia nervosa", "Erro", "Advérbio não varia"),
        ("agiu mal › agiu mau", "Erro", "Mau é adjetivo"),
    ]),
    h2("Leve para a prova"),
    bl("Identifique o **sentido** antes de olhar a conjunção.",
       "Adversativas são intercambiáveis entre si; conclusivas também.",
       "Concessiva e condicional pedem **subjuntivo**.",
       "**Desde que** + subjuntivo = condição; + indicativo = tempo.",
       "**Pois** depois do verbo = conclusão.",
       "**Como** no início do período = causa.",
       "**Tão… que** = consequência, não finalidade.",
       "*Mas* não se desloca; *porém, contudo, todavia* podem ir para o meio da oração.",
       "**Há** para o passado; **a** para o futuro.",
       "Advérbio junto de adjetivo **não concorda**."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "CONECTIVOS", "rootSub": "advérbio · preposição · conjunção",
    "left": [
        {"label": "Advérbio", "items": ["invariável", "meio nervosa · bastante cansados", "mal (bem) × mau (bom)"]},
        {"label": "Posição", "items": ["só o delegado ≠ só pode", "somente, apenas, até", "muda o foco da frase"]},
        {"label": "Preposição", "items": ["há: passado · a: futuro", "sob sigilo · sobre o caso", "de o juiz decidir"]},
        {"label": "Aditivas e alternativas", "items": ["e, nem, não só… mas também", "ou, ora… ora", "quer… quer"]},
        {"label": "Adversativas", "items": ["mas, porém, contudo", "todavia, entretanto", "no entanto"]},
    ],
    "right": [
        {"label": "Conclusivas e explicativas", "items": ["logo, portanto, por isso", "pois posposto: conclusão", "pois anteposto: explicação"]},
        {"label": "Causa e concessão", "items": ["como, já que, visto que", "embora + subjuntivo", "apesar de + infinitivo"]},
        {"label": "Condição e tempo", "items": ["se, caso", "desde que + subjuntivo: condição", "desde que + indicativo: tempo"]},
        {"label": "Proporção e consequência", "items": ["à medida que: proporção", "na medida em que: causa", "tão… que: consequência"]},
        {"label": "Fim e conformidade", "items": ["para que, a fim de que", "conforme, segundo", "consoante, como"]},
    ],
}

QUIZ = quiz([
    ("C", "Em “As provas eram bastante consistentes”, o vocábulo bastante é advérbio de intensidade.",
     "Modifica o adjetivo consistentes e equivale a muito; por isso não varia."),
    ("E", "Em “A vítima ficou meia confusa após o depoimento”, a concordância está de acordo com a norma-padrão.",
     "Meio, no sentido de um pouco, é advérbio: meio confusa."),
    ("C", "Em “Há cinco anos ocorreu o crime”, a forma há indica tempo decorrido.",
     "O verbo haver indica tempo passado; para tempo futuro usa-se a preposição a."),
    ("E", "Em “O prazo terminou, contudo o recurso foi aceito”, a conjunção contudo tem valor conclusivo.",
     "Contudo é adversativa: introduz oposição."),
    ("C", "Em “Ainda que haja provas, o juiz pode absolver o réu”, a locução ainda que poderia ser substituída por embora, sem prejuízo da correção e do sentido.",
     "Ambas são concessivas e pedem subjuntivo."),
    ("E", "Em “Visto que o réu confessou, a pena foi atenuada”, a locução visto que exprime finalidade.",
     "Visto que é causal: introduz o motivo da atenuação."),
    ("C", "Em “Leia o edital para que não haja dúvidas”, a locução para que poderia ser substituída por a fim de que, mantendo-se a relação de finalidade.",
     "Para que e a fim de que são finais."),
    ("E", "A locução na medida em que expressa proporção, equivalendo a à proporção que.",
     "Na medida em que expressa causa; quem indica proporção é à medida que."),
    ("C", "Em “Assim que chegou, o perito isolou a área”, a locução assim que tem valor temporal.",
     "Assim que equivale a logo que: marca tempo."),
    ("E", "Em “O laudo comprovou a falsificação; logo, o documento é inválido”, o vocábulo logo tem valor temporal.",
     "Nesse período, logo é conjunção conclusiva, equivalente a portanto."),
], 10)

SOURCES = [GRAM, SRC_R]
