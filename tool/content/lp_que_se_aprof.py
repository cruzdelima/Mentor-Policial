# -*- coding: utf-8 -*-
"""Língua Portuguesa · Funções do "que" e do "se" — MATERIAL APROFUNDADO (estudo inicial)."""
from common import *

MATERIAL = material(
    "lp-que-se-02", "LP", "LP-23", "aprofundado", "Funções do “que” e do “se”", "Língua Portuguesa · Morfossintaxe",
    "portugues_que_se_aprofundado", "Portugues_Funcoes_Que_Se_APROFUNDADO.pdf", None, ["Funções do", "“que” e do “se”"],
    ["Teoria completa para o primeiro estudo: as classes e funções do que e do se,", "com os testes de reconhecimento e 20 questões no estilo Cebraspe."],
    [("01", "O que", "relativo, integrante, conjunção, pronome, advérbio, preposição"),
     ("02", "Testes", "o qual, isso, valor da conjunção"),
     ("03", "O se", "pronome, partícula apassivadora, índice de indeterminação, conjunção"),
     ("04", "Concordância", "o se e o verbo"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Funções do “que” e do “se” (Língua Portuguesa)",
    "Base: gramáticas de referência (Bechara; Cunha e Cintra).", 150)

THEORY = [
    exam("Como estudar este material",
         "O *que* e o *se* são as palavras mais versáteis da língua. As bancas pedem a **classificação** (“o *que* é pronome relativo”) e "
         "as **consequências** dela: concordância (*vendem-se casas* × *precisa-se de*), pontuação e sentido. Use os testes de cada seção."),

    h2("1. Funções do “que”"),
    tb(["Classe", "Como reconhecer", "Exemplo"], [0.2, 0.38, 0.42], [
        ("Pronome relativo", "Retoma um antecedente; troca por **o qual / a qual**", "O documento **que** o réu apresentou é falso. (o qual)"),
        ("Conjunção integrante", "Inicia oração substantiva; a oração troca por **isso**", "Espero **que** o laudo saia hoje. (espero isso)"),
        ("Conjunção adverbial", "Liga orações com valor de causa, consequência, comparação, finalidade, concessão", "Correu tanto **que** caiu (consecutiva). Mais rápido **que** ele (comparativa)."),
        ("Conjunção coordenativa", "Explicativa (= pois) ou aditiva (em repetições)", "Venha logo, **que** a reunião vai começar. Fala **que** fala."),
        ("Pronome interrogativo", "Em perguntas diretas ou indiretas", "**Que** houve? Não sei **que** houve."),
        ("Pronome indefinido / adjetivo", "Acompanha substantivo em exclamação ou interrogação", "**Que** operação! **Que** horas são?"),
        ("Advérbio de intensidade", "Modifica adjetivo ou advérbio (= quão)", "**Que** difícil foi a prova!"),
        ("Preposição", "Equivale a *de*, em *ter que*", "Tenho **que** sair. (= tenho de sair)"),
        ("Partícula expletiva (de realce)", "Pode ser retirada sem prejuízo", "Quase **que** caí. Eu é **que** decidi."),
        ("Substantivo", "Com determinante; leva acento", "Ele tem um **quê** de mistério."),
        ("Interjeição", "Expressa espanto; leva acento", "**Quê!** Você foi aprovado?"),
    ]),
    key("Relativo × integrante",
        "Se trocar por **o qual** funciona, é **relativo** (e exerce função sintática na oração). Se a oração inteira vira **isso**, é **integrante** "
        "(e não exerce função, só liga). *O laudo **que** chegou* (o qual chegou) × *Soube **que** chegou* (soube isso)."),

    h2("2. Funções do “se”"),
    tb(["Classe", "Como reconhecer", "Exemplo"], [0.22, 0.4, 0.38], [
        ("Pronome reflexivo", "Sujeito pratica e sofre a ação (objeto direto ou indireto)", "O agente **se** feriu. Ele **se** deu um prêmio."),
        ("Pronome recíproco", "Ação mútua entre dois ou mais", "Os suspeitos **se** acusaram."),
        ("Partícula apassivadora", "**VTD** + se; troca pela passiva analítica", "Vendem-**se** viaturas. (viaturas são vendidas)"),
        ("Índice de indeterminação do sujeito", "**VTI, VI ou VL** + se; verbo no singular", "Precisa-**se** de agentes. Vive-**se** bem aqui."),
        ("Parte integrante do verbo", "Verbos pronominais (o se não tem função)", "Ele **se** queixou. Arrependeu-**se**. Suicidou-**se**."),
        ("Partícula expletiva", "Realce, pode ser retirada", "Foi-**se** embora. Passaram-**se** os dias."),
        ("Conjunção condicional", "= caso", "**Se** houver flagrante, haverá prisão."),
        ("Conjunção integrante", "Inicia oração substantiva (= isso)", "Não sei **se** ele voltará."),
        ("Conjunção causal", "= já que (uso menos comum)", "**Se** você já sabia, por que não avisou?"),
    ]),
    trap("Apassivador × indeterminador",
         "Olhe o **verbo**: transitivo direto + se = **apassivador**, e o verbo concorda com o sujeito (*revisaram-se os inquéritos*). "
         "Transitivo indireto, intransitivo ou de ligação + se = **indeterminador**, e o verbo fica no singular (*trata-se de casos graves*). "
         "Teste da apassivadora: transforme em *ser + particípio* (*os inquéritos foram revisados*)."),

    h2("3. Consequências na prova"),
    bl("**Concordância**: *Vendem-se casas* (sujeito plural) × *Precisa-se de agentes* (singular).",
       "**Pontuação**: oração com *que* relativo explicativo vai entre vírgulas; com *que* integrante, sem vírgula.",
       "**Regência**: a preposição exigida pelo verbo vem antes do *que* relativo (*o cargo a que aspiro*).",
       "**Colocação**: *que* e *se* (conjunções) são palavras atrativas: *Disse que **se** arrependeu*; *Se **me** chamarem, irei*."),

    h2("4. Como as bancas cobram"),
    bl("“O vocábulo *que* é pronome relativo e retoma X.”",
       "“O *se* é partícula apassivadora; por isso, o verbo está no plural.”",
       "“O *se* poderia ser substituído por *caso*” (condicional).",
       "“A retirada do *que* em *Eu é que decidi* não prejudicaria a correção” (expletivo)."),
]

QUIZ = quiz([
    ("C", "Em “O documento que o réu apresentou é falso”, o vocábulo que é pronome relativo.",
     "Retoma documento e pode ser trocado por o qual."),
    ("E", "Em “Espero que o laudo saia hoje”, o vocábulo que é pronome relativo.",
     "É conjunção integrante: a oração equivale a isso."),
    ("C", "Em “Correu tanto que caiu”, o que é conjunção que introduz ideia de consequência.",
     "Tanto… que forma correlação consecutiva."),
    ("E", "Em “Tenho que entregar o relatório”, o vocábulo que é conjunção integrante.",
     "Em ter que, o que funciona como preposição (= ter de)."),
    ("C", "Em “Quase que o suspeito escapou”, o que é partícula expletiva e poderia ser retirado sem prejuízo da correção.",
     "Quase o suspeito escapou mantém o sentido."),
    ("E", "Em “Que difícil foi a prova!”, o vocábulo que é pronome relativo.",
     "Intensifica o adjetivo difícil: é advérbio de intensidade."),
    ("C", "Em “Venha logo, que a reunião vai começar”, o que é conjunção explicativa.",
     "Equivale a pois."),
    ("E", "Em “O agente se feriu durante a abordagem”, o se é índice de indeterminação do sujeito.",
     "O agente pratica e sofre a ação: pronome reflexivo."),
    ("C", "Em “Vendem-se viaturas apreendidas”, o se é partícula apassivadora.",
     "Vender é transitivo direto: viaturas apreendidas são vendidas."),
    ("E", "Em “Precisa-se de agentes”, o se é partícula apassivadora.",
     "Precisar de é transitivo indireto: o se indetermina o sujeito."),

    ("C", "Em “O réu arrependeu-se do crime”, o se é parte integrante do verbo.",
     "Arrepender-se é verbo pronominal; o se não exerce função sintática."),
    ("E", "Em “Os suspeitos se acusaram mutuamente”, o se é pronome reflexivo, e não recíproco.",
     "A ação é mútua entre os suspeitos: o se é recíproco."),
    ("C", "Em “Se houver flagrante, a prisão será imediata”, o se poderia ser substituído por caso, com ajuste do verbo para haja.",
     "Se condicional equivale a caso + subjuntivo presente."),
    ("E", "Em “Ninguém sabe se o suspeito voltará”, o se é conjunção condicional.",
     "Introduz oração substantiva (ninguém sabe isso): conjunção integrante."),
    ("C", "Em “Revisaram-se os inquéritos pendentes”, o verbo está no plural porque o se é partícula apassivadora e os inquéritos pendentes é o sujeito.",
     "Equivale a os inquéritos pendentes foram revisados."),
    ("E", "Em “Trata-se de casos graves”, o verbo poderia ir para o plural, pois o se é partícula apassivadora.",
     "Tratar de é transitivo indireto: o se indetermina o sujeito e o verbo fica no singular."),
    ("C", "Em “Eu é que decidi o caso”, o termo é que tem valor de realce e poderia ser retirado sem prejuízo da correção.",
     "Eu decidi o caso mantém a correção; é que apenas enfatiza."),
    ("E", "Em “Não sei que houve na operação”, o vocábulo que é conjunção integrante.",
     "Em interrogativa indireta, que é pronome interrogativo (= o que)."),
    ("C", "Em “Foi-se embora sem avisar”, o se é partícula expletiva.",
     "Pode ser retirado: foi embora sem avisar."),
    ("E", "Em “Ele tem um quê de mistério”, quê é pronome relativo.",
     "Precedido de artigo e acentuado, quê é substantivo."),
], 20)

SOURCES = [GRAM, SRC_A]
