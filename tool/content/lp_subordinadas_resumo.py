# -*- coding: utf-8 -*-
"""Língua Portuguesa · Orações subordinadas — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "lp-subordinadas-01", "LP", "LP-10", "resumo", "Orações subordinadas", "Língua Portuguesa · Sintaxe do período",
    "portugues_subordinadas", "Portugues_Oracoes_Subordinadas_RESUMO.pdf", None, ["Orações", "subordinadas"], RES_SUB,
    RES_ITEMS("substantivas, adjetivas, adverbiais e reduzidas"),
    "Tópico do edital: Sintaxe do período — orações subordinadas (Língua Portuguesa)",
    "Base: gramáticas de referência (Bechara; Cunha e Cintra).", 40)

THEORY = [
    exam("O que a banca cobra",
         "**Vírgulas da adjetiva** (restritiva × explicativa muda o sentido), **que relativo × integrante** e o **sentido** das adverbiais."),
    h2("1. Substantivas (teste: ISSO)"),
    tb(["Tipo", "Exemplo"], [0.26, 0.74], [
        ("Subjetiva", "É necessário **que todos colaborem**. Convém **que…** Sabe-se **que…**"),
        ("Objetiva direta", "Afirmou **que o caso estava encerrado**."),
        ("Objetiva indireta", "Lembrou-se **de que havia esquecido**. (completa verbo)"),
        ("Completiva nominal", "Tenho certeza **de que ele mentiu**. (completa nome)"),
        ("Predicativa", "A verdade é **que ninguém viu**."),
        ("Apositiva", "Só uma coisa importava: **que a vítima fosse localizada**."),
    ]),
    h2("2. Adjetivas (teste: o qual)"),
    bl("**Restritiva**: sem vírgulas; restringe o grupo — *Os presos **que trabalham** têm remição* (só alguns).",
       "**Explicativa**: entre vírgulas; vale para todos — *Os agentes, **que estavam de plantão**, atenderam*.",
       "Inserir ou retirar as vírgulas **altera o sentido**."),
    h2("3. Adverbiais"),
    tb(["Tipo", "Conjunções"], [0.22, 0.78], [
        ("Causal", "porque, como (anteposto), já que, visto que"),
        ("Concessiva", "embora, ainda que, mesmo que (+ subjuntivo)"),
        ("Condicional", "se, caso, desde que + subjuntivo"),
        ("Conformativa", "conforme, segundo, consoante"),
        ("Comparativa", "como, mais… (do) que"),
        ("Consecutiva", "tão/tanto… que, de modo que"),
        ("Final", "para que, a fim de que"),
        ("Proporcional", "à medida que, à proporção que"),
        ("Temporal", "quando, assim que, logo que, desde que + indicativo"),
    ]),
    h2("4. Reduzidas"),
    bl("Sem conectivo, com infinitivo, gerúndio ou particípio. **Desenvolva** para classificar.",
       "*Ao chegar* = quando chegou (tempo). *Sendo primário* = como é primário (causa). *Terminada a audiência* = assim que terminou (tempo)."),
    trap("Vírgula",
         "Nunca separe a **substantiva** da principal (*É necessário, que…* é erro). A **adverbial anteposta** costuma levar vírgula."),
]

SUMMARY = [
    h2("Quadro: como reconhecer"),
    tb(["Pista", "Oração", "Teste"], [0.38, 0.3, 0.32], [
        ("Que / se depois de verbo ou nome", "Substantiva", "Troca por **isso**"),
        ("É + adjetivo + que; convém que; sabe-se que", "Subjetiva", "Isso é necessário"),
        ("Preposição + que completando verbo", "Objetiva indireta", "lembrou-se disso"),
        ("Preposição + que completando nome", "Completiva nominal", "certeza disso"),
        ("Que retomando um termo", "Adjetiva", "Troca por **o qual**"),
        ("Adjetiva sem vírgula", "Restritiva", "Só uma parte"),
        ("Adjetiva entre vírgulas", "Explicativa", "Todos"),
        ("Conjunção de circunstância", "Adverbial", "Qual o sentido?"),
        ("Infinitivo, gerúndio, particípio", "Reduzida", "Desenvolva"),
    ]),
    h2("Leve para a prova"),
    bl("Substantiva = **isso**; adjetiva = **o qual**.",
       "Vírgulas na adjetiva: **explicativa**; sem vírgulas: **restritiva**.",
       "Retirar/inserir vírgulas da adjetiva **altera o sentido**.",
       "Subjetiva: verbo da principal na 3ª do singular.",
       "Preposição + que: verbo › objetiva indireta; nome › completiva nominal.",
       "Embora, ainda que = **concessão** (+ subjuntivo).",
       "Se, caso = **condição**.",
       "Tão… que = **consequência**; para que = **finalidade**.",
       "*Sendo réu primário* = causa.",
       "Sem vírgula entre principal e substantiva."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "SUBORDINADAS", "rootSub": "substantivas · adjetivas · adverbiais",
    "left": [
        {"label": "Substantivas", "items": ["que/se integrante", "teste: ISSO", "sem vírgula na principal"]},
        {"label": "Funções", "items": ["subjetiva · objetiva direta", "objetiva indireta · completiva", "predicativa · apositiva"]},
        {"label": "Subjetiva", "items": ["é necessário que", "convém que · parece que", "sabe-se que"]},
        {"label": "Adjetivas", "items": ["pronome relativo", "teste: o qual", "retoma um antecedente"]},
        {"label": "Restritiva × explicativa", "items": ["sem vírgula: restringe", "com vírgula: todos", "vírgula muda o sentido"]},
    ],
    "right": [
        {"label": "Causa e concessão", "items": ["como, já que, visto que", "embora + subjuntivo", "ainda que, mesmo que"]},
        {"label": "Condição e tempo", "items": ["se, caso", "quando, assim que", "desde que: os dois"]},
        {"label": "Fim e consequência", "items": ["para que, a fim de que", "tão… que", "de modo que"]},
        {"label": "Outras", "items": ["conforme: conformidade", "como: comparação", "à medida que: proporção"]},
        {"label": "Reduzidas", "items": ["ao chegar: tempo", "sendo primário: causa", "terminada a audiência: tempo"]},
    ],
}

QUIZ = quiz([
    ("C", "As orações subordinadas substantivas podem, em regra, ser substituídas pelo pronome isso.",
     "Elas equivalem a um substantivo; o teste do isso ajuda a reconhecê-las."),
    ("E", "No período “Convém que o réu seja ouvido”, a oração subordinada é substantiva objetiva direta.",
     "A oração é o sujeito de convém (isso convém): subjetiva."),
    ("C", "No período “Tenho receio de que o prazo expire”, a oração “de que o prazo expire” é subordinada substantiva completiva nominal.",
     "Completa o substantivo receio."),
    ("E", "A oração subordinada adjetiva restritiva deve vir isolada por vírgulas.",
     "Quem vem entre vírgulas é a explicativa; a restritiva não leva vírgulas."),
    ("C", "No período “Como o réu não compareceu, a audiência foi adiada”, a oração introduzida por como expressa causa.",
     "Como anteposto à principal tem valor causal (= visto que)."),
    ("E", "No período “Caso o réu confesse, a pena será atenuada”, a oração subordinada é adverbial concessiva.",
     "Caso introduz condição: a oração é condicional."),
    ("C", "No período “Lacraram a sala para que não houvesse fraude”, a oração introduzida por para que expressa finalidade.",
     "Para que é locução conjuntiva final."),
    ("E", "No período “Ainda que chova, a operação ocorrerá”, a oração subordinada é adverbial condicional.",
     "Ainda que introduz concessão: a chuva não impede a operação."),
    ("C", "No período “Sendo réu primário, ele terá direito ao benefício”, a oração reduzida de gerúndio tem valor causal.",
     "Desenvolvida: como é réu primário."),
    ("E", "Em “Espero que o laudo saia hoje”, o vocábulo que poderia ser substituído por o qual, pois é pronome relativo.",
     "Que é conjunção integrante: a oração é objetiva direta (espero isso)."),
], 10)

SOURCES = [GRAM, SRC_R]
