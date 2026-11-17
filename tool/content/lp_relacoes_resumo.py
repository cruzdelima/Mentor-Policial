# -*- coding: utf-8 -*-
"""Língua Portuguesa · Relações semânticas entre orações, períodos e parágrafos — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "lp-relacoes-01", "LP", "LP-22", "resumo", "Relações semânticas entre orações, períodos e parágrafos", "Língua Portuguesa · Texto",
    "portugues_relacoes", "Portugues_Relacoes_Semanticas_RESUMO.pdf", None, ["Relações semânticas", "entre orações e parágrafos"], RES_SUB,
    RES_ITEMS("relações lógicas, relações implícitas e articuladores"),
    "Tópico do edital: Relações semânticas entre orações, períodos e parágrafos (Língua Portuguesa)",
    "Base: gramáticas de referência e Koch, A coesão textual.", 30)

THEORY = [
    exam("O que a banca cobra",
         "A **relação lógica** entre partes do texto e se ela se mantém na troca do conector."),
    h2("1. Relações e conectores"),
    tb(["Relação", "Conectores"], [0.24, 0.76], [
        ("Adição", "e, nem, além disso, também"),
        ("Oposição", "mas, porém, contudo, no entanto, em contrapartida"),
        ("Concessão", "embora, ainda que, apesar de"),
        ("Causa", "porque, como, já que, visto que"),
        ("Consequência", "tão… que, de modo que"),
        ("Conclusão", "logo, portanto, dessa forma"),
        ("Condição", "se, caso, desde que + subjuntivo"),
        ("Finalidade", "para que, a fim de que"),
        ("Tempo", "quando, assim que, enquanto"),
        ("Proporção", "à medida que, quanto mais… mais"),
        ("Conformidade", "conforme, segundo"),
        ("Resumo", "em síntese, em suma"),
    ]),
    h2("2. Pontos-chave"),
    bl("**Mas**: prevalece o argumento **depois** dele. **Embora**: a concessiva não impede a principal.",
       "Períodos **justapostos** têm relação implícita (*Choveu. Adiaram* = causa e consequência).",
       "Articuladores entre parágrafos: *em primeiro lugar, além disso, em contrapartida, dessa forma, em síntese*."),
]

SUMMARY = [
    h2("Leve para a prova"),
    bl("Identifique a relação **antes** de olhar o conector.",
       "Troca no **mesmo grupo** mantém o sentido.",
       "Mas: vale o que vem **depois**.",
       "Embora: pede **subjuntivo**.",
       "Sem conectivo também há relação lógica.",
       "Além disso = **acrescenta**.",
       "Em contrapartida = **opõe**.",
       "Dessa forma, em suma = **conclui**.",
       "À medida que = **proporção**; na medida em que = **causa**.",
       "Segundo, conforme = **conformidade**."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "RELAÇÕES", "rootSub": "lógicas do texto",
    "left": [
        {"label": "Adição", "items": ["e, nem", "além disso", "não só… mas também"]},
        {"label": "Oposição", "items": ["mas, porém", "em contrapartida", "vale o que vem depois"]},
        {"label": "Concessão", "items": ["embora + subjuntivo", "ainda que", "apesar de + infinitivo"]},
        {"label": "Causa", "items": ["porque, como", "já que, visto que", "em razão de"]},
        {"label": "Consequência e conclusão", "items": ["tão… que", "portanto, logo", "dessa forma"]},
    ],
    "right": [
        {"label": "Condição e fim", "items": ["se, caso", "para que", "a fim de que"]},
        {"label": "Tempo e proporção", "items": ["quando, assim que", "à medida que", "quanto mais… mais"]},
        {"label": "Conformidade", "items": ["conforme", "segundo", "consoante"]},
        {"label": "Implícitas", "items": ["períodos justapostos", "inferência do leitor", "por isso subentendido"]},
        {"label": "Parágrafos", "items": ["em primeiro lugar", "além disso", "em síntese"]},
    ],
}

QUIZ = quiz([
    ("C", "Em “O réu colaborou; por isso, teve a pena reduzida”, a expressão por isso introduz conclusão ou consequência.",
     "A redução da pena decorre da colaboração."),
    ("E", "Em “Ainda que chova, a operação ocorrerá”, a locução ainda que expressa condição.",
     "Ainda que expressa concessão."),
    ("C", "Em “Conforme determina a lei, o preso foi apresentado ao juiz”, conforme expressa conformidade.",
     "Equivale a de acordo com o que determina a lei."),
    ("E", "Em “Já que todos chegaram, a reunião começou”, a locução já que expressa tempo.",
     "Já que expressa causa."),
    ("C", "Entre os períodos “O suspeito fugiu. A porta estava aberta.” pode-se inferir relação de explicação ou causa.",
     "O segundo período explica como a fuga ocorreu."),
    ("E", "A substituição de porém por portanto mantém a relação de sentido entre as orações.",
     "Porém indica oposição; portanto, conclusão."),
    ("C", "Em contrapartida é articulador que introduz ideia oposta à anterior.",
     "Equivale a por outro lado."),
    ("E", "Em “Quanto mais investigava, mais provas encontrava”, há relação de concessão.",
     "Quanto mais… mais expressa proporção."),
    ("C", "Em “Estudou para que fosse aprovado”, a locução para que expressa finalidade.",
     "Indica o objetivo do estudo."),
    ("E", "Em períodos justapostos, sem conectivos, não há relação lógica entre as orações.",
     "A relação existe e é inferida pelo leitor."),
], 10)

SOURCES = [GRAM, SRC_R]
