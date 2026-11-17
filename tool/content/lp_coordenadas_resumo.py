# -*- coding: utf-8 -*-
"""Língua Portuguesa · Orações coordenadas — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "lp-coordenadas-01", "LP", "LP-09", "resumo", "Orações coordenadas", "Língua Portuguesa · Sintaxe do período",
    "portugues_coordenadas", "Portugues_Oracoes_Coordenadas_RESUMO.pdf", None, ["Orações", "coordenadas"], RES_SUB,
    RES_ITEMS("os cinco tipos, valores especiais e pontuação"),
    "Tópico do edital: Sintaxe do período — orações coordenadas (Língua Portuguesa)",
    "Base: gramáticas de referência (Bechara; Cunha e Cintra).", 40)

THEORY = [
    exam("O que a banca cobra",
         "**Sentido** da oração coordenada, **troca de conjunções** e **pontuação** (vírgula antes de *e* e de *mas*; conjunção deslocada)."),
    h2("1. Coordenação"),
    bl("Orações **sintaticamente independentes**: nenhuma é termo da outra; não há oração principal.",
       "**Assindética**: sem conjunção (*Chegou, viu, prendeu*). **Sindética**: com conjunção."),
    h2("2. Os cinco tipos"),
    tb(["Tipo", "Conjunções", "Exemplo"], [0.18, 0.42, 0.4], [
        ("Aditiva", "e, nem, não só… mas também", "Prendeu e algemou."),
        ("Adversativa", "mas, porém, contudo, todavia, entretanto, no entanto", "Confessou, mas recorreu."),
        ("Alternativa", "ou, ou… ou, ora… ora, quer… quer", "Ou fala, ou cala."),
        ("Conclusiva", "logo, portanto, por isso, pois (posposto)", "Confessou; logo, é culpado."),
        ("Explicativa", "porque, que, pois (anteposto)", "Saia, pois vai chover."),
    ]),
    h2("3. Valores especiais"),
    bl("**E adversativo**: *Estudou e não passou* (= mas).",
       "**Pois** antes do verbo = explicação; depois do verbo, entre vírgulas = conclusão.",
       "**Explicativa** justifica a afirmação (*Choveu, porque a rua está molhada*); **causal** dá a causa do fato (*A rua está molhada porque choveu*).",
       "**Mas** só no início; **porém, contudo, todavia, entretanto, portanto** podem ir para o meio, entre vírgulas."),
    h2("4. Pontuação"),
    bl("Vírgula antes de **mas, porém, portanto, pois**.",
       "**E** com mesmo sujeito: sem vírgula. Com sujeitos diferentes: vírgula admitida.",
       "Conjunção deslocada: **entre vírgulas**, e antes dela ponto e vírgula (*Confessou; o advogado, porém, recorreu*)."),
]

SUMMARY = [
    h2("Quadro: substituições"),
    tb(["Troca", "Resultado", "Motivo"], [0.38, 0.18, 0.44], [
        ("mas › porém / todavia", "Mantém", "Adversativas"),
        ("portanto › logo / por conseguinte", "Mantém", "Conclusivas"),
        ("pois (explicativo) › porque", "Mantém", "Explicativas"),
        ("portanto › porquanto", "Altera", "Conclusão vira explicação"),
        ("deve, pois, ser punido › porque", "Altera", "Pois posposto é conclusivo"),
        ("ou… ou › nem… nem", "Altera", "Alternância vira adição negativa"),
        ("…, mas o réu… › o réu, mas, …", "Erro", "Mas não se desloca"),
        ("…, porém… › …; o réu, porém, …", "Mantém", "Porém se desloca"),
    ]),
    h2("Leve para a prova"),
    bl("Coordenadas **não têm** oração principal.",
       "Assindética = sem conjunção; inclusive a primeira oração da sequência.",
       "**Nem** = e não.",
       "**Não só… mas também** = adição.",
       "**Pois** posposto = conclusão.",
       "Depois de **imperativo**: explicativa.",
       "*E* pode ter valor **adversativo**.",
       "Vírgula antes de *e* com **sujeitos diferentes**.",
       "Conjunção deslocada: **entre vírgulas**.",
       "**Porquanto** ≠ portanto."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "COORDENADAS", "rootSub": "orações independentes",
    "left": [
        {"label": "Coordenação", "items": ["sem oração principal", "independência sintática", "relação só de sentido"]},
        {"label": "Assindética", "items": ["sem conjunção", "chegou, viu, prendeu", "separada por vírgula"]},
        {"label": "Aditiva", "items": ["e, nem (= e não)", "não só… mas também", "e com valor adversativo"]},
        {"label": "Adversativa", "items": ["mas: só no início", "porém, contudo, todavia", "deslocável entre vírgulas"]},
        {"label": "Alternativa", "items": ["ou… ou", "ora… ora", "quer… quer"]},
    ],
    "right": [
        {"label": "Conclusiva", "items": ["logo, portanto, por isso", "pois depois do verbo", "por conseguinte"]},
        {"label": "Explicativa", "items": ["porque, que, porquanto", "pois antes do verbo", "após imperativo"]},
        {"label": "Explicativa × causal", "items": ["explicativa: justifica a fala", "causal: causa do fato", "choveu, porque…"]},
        {"label": "Vírgula", "items": ["antes de mas e portanto", "e + sujeitos diferentes", "polissíndeto: e…, e…"]},
        {"label": "Pegadinhas", "items": ["porquanto ≠ portanto", "nem… nem: adição", "mas não se desloca"]},
    ],
}

QUIZ = quiz([
    ("C", "As orações coordenadas são sintaticamente independentes entre si.",
     "Nenhuma exerce função sintática na outra; relacionam-se apenas pelo sentido."),
    ("E", "Em “Não fale alto, que o bebê está dormindo”, a oração introduzida por que é coordenada conclusiva.",
     "Que, após imperativo, introduz justificativa: a oração é explicativa."),
    ("C", "Em “Ele trabalha muito, mas não recebe horas extras”, a segunda oração é coordenada sindética adversativa.",
     "Mas introduz oposição em relação à primeira oração."),
    ("E", "Assim como porém, a conjunção mas pode ser deslocada para depois do sujeito da oração que introduz.",
     "Mas ocupa sempre o início da oração."),
    ("C", "Em “Ou confessa, ou será condenado”, as orações são coordenadas alternativas.",
     "Ou… ou expressa alternância/exclusão."),
    ("E", "Em “Choveu muito; por isso, a operação foi adiada”, a locução por isso introduz oração explicativa.",
     "Por isso introduz a consequência lógica: oração conclusiva."),
    ("C", "No período “Chegou, sentou, calou”, as orações são coordenadas assindéticas.",
     "Estão ligadas apenas por vírgulas, sem conjunção."),
    ("E", "Em “Ele não estudou nem trabalhou”, a conjunção nem tem valor adversativo.",
     "Nem equivale a e não: valor aditivo."),
    ("C", "Em “O réu confessou; deve, pois, ser punido”, a conjunção pois tem valor conclusivo.",
     "Posposto ao verbo e entre vírgulas, pois é conclusivo (= portanto)."),
    ("E", "Todo período composto por coordenação apresenta uma oração principal.",
     "Oração principal só existe na subordinação."),
], 10)

SOURCES = [GRAM, SRC_R]
