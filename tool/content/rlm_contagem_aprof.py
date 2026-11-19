# -*- coding: utf-8 -*-
"""Raciocínio Lógico · Princípios de contagem e análise combinatória — MATERIAL APROFUNDADO."""
from common import *

MATERIAL = material(
    "rlm-contagem-02", "RLM", "RLM-11", "aprofundado", "Princípios de contagem e análise combinatória", "Raciocínio Lógico e Matemática · Combinatória",
    "raciocinio_contagem_aprofundado", "RaciocinioLogico_Contagem_APROFUNDADO.pdf", None, ["Análise", "combinatória"],
    ["Princípio fundamental da contagem, fatorial, permutações, arranjos e combinações,", "com o teste da ordem e 20 questões no estilo Cebraspe."],
    [("01", "Princípio fundamental", "multiplicar as etapas"),
     ("02", "Permutações", "filas, anagramas e repetições"),
     ("03", "Arranjo ou combinação", "a ordem importa?"),
     ("04", "Casos especiais", "juntos, circular, pelo menos um"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Princípios de contagem e análise combinatória — Raciocínio Lógico e Matemática",
    "Base: análise combinatória do ensino médio.", 90)

THEORY = [
    exam("Como estudar este material",
         "Combinatória é um dos assuntos **mais cobrados** pelo Cebraspe em PF e PRF. Quase todo problema se resolve com o **princípio "
         "fundamental da contagem** e com uma pergunta: **a ordem importa?** Não decore fórmulas sem entender quando usar cada uma: "
         "resolva os exemplos pelo raciocínio das etapas."),

    h2("1. Princípio fundamental da contagem"),
    key("Regra",
        "Se uma escolha é feita em **etapas independentes**, com m₁ opções na primeira, m₂ na segunda e assim por diante, o total de "
        "possibilidades é o **produto** m₁ × m₂ × ... Use o **“e”** para multiplicar (etapas) e o **“ou”** para somar (casos separados)."),
    bl("Placas com **3 letras e 4 algarismos** (letras e algarismos podem repetir): 26 × 26 × 26 × 10 × 10 × 10 × 10 = **175.760.000**.",
       "Senhas de **4 algarismos distintos**: 10 × 9 × 8 × 7 = **5.040**.",
       "Números de **4 algarismos** (o primeiro não pode ser zero): 9 × 10 × 10 × 10 = **9.000**.",
       "Comece sempre pela etapa **com restrição** (primeiro algarismo, letra obrigatória)."),

    h2("2. Fatorial e permutações"),
    p("**n!** (lê-se “n fatorial”) = n × (n − 1) × ... × 2 × 1. Por definição, 0! = 1. Valores úteis: 3! = 6, 4! = 24, 5! = 120, "
      "6! = 720, 7! = 5.040."),
    tb(["Tipo", "Fórmula", "Exemplo"], [0.26, 0.24, 0.5], [
        ("**Permutação simples**", "Pₙ = n!", "Formas de enfileirar 5 agentes: 5! = **120**. Anagramas de PERITO (6 letras distintas): 6! = **720**."),
        ("**Com repetição**", "n!/(a! · b! ...)", "Anagramas de POLICIA (I duas vezes): 7!/2! = **2.520**. De DELEGADO (D e E duas vezes): 8!/(2! · 2!) = **10.080**."),
        ("**Circular**", "(n − 1)!", "5 pessoas em volta de uma mesa redonda: 4! = **24**."),
    ]),
    trap("Elementos que devem ficar juntos",
         "Em uma fila de 5 pessoas, de quantas formas duas delas ficam **lado a lado**? Trate as duas como um **bloco**: 4 “elementos” "
         "permutam em 4! = 24, e o bloco se arruma de 2! = 2 formas. Total: **48**."),

    h2("3. Arranjo ou combinação: a ordem importa?"),
    key("O teste da ordem",
        "Escolha um grupo e **troque a ordem** dos escolhidos. Se a troca gera uma **situação diferente** (cargos, posições, senhas), é "
        "**arranjo**. Se gera **a mesma** situação (comissão, equipe, grupo), é **combinação**."),
    tb(["", "Arranjo", "Combinação"], [0.18, 0.41, 0.41], [
        ("A ordem", "**importa**", "**não importa**"),
        ("Fórmula", "A(n, p) = n!/(n − p)!", "C(n, p) = n!/[p! · (n − p)!]"),
        ("Exemplo", "Escolher delegado, escrivão e agente entre 8 pessoas: 8 × 7 × 6 = **336**",
         "Escolher uma equipe de 3 entre 8 pessoas: 336/3! = **56**"),
        ("Também", "Pódio, senha, presidente e vice", "Comissão, grupo, apertos de mão, saladas"),
    ]),
    bl("Combinação = arranjo dividido por p! (as ordens dos p escolhidos contam como uma só).",
       "C(n, p) = C(n, n − p): escolher 3 de 10 para ir é o mesmo que escolher 7 para ficar.",
       "Apertos de mão entre 10 pessoas: C(10, 2) = **45**."),

    h2("4. Casos combinados"),
    bl("**Grupos de origens diferentes**: comissão com 2 agentes (de 6) **e** 1 escrivão (de 4): C(6, 2) × C(4, 1) = 15 × 4 = **60**.",
       "**Pelo menos um**: calcule o **total** e subtraia os casos **sem nenhum**. Comissões de 3 entre 10 pessoas (4 mulheres e 6 homens) com "
       "pelo menos uma mulher: C(10, 3) − C(6, 3) = 120 − 20 = **100**.",
       "**Casos separados** (“ou”): some. Comissões de 3 só de homens ou só de mulheres: C(6, 3) + C(4, 3) = 20 + 4 = **24**."),

    h2("5. Como o Cebraspe cobra"),
    bl("Um texto descreve uma escolha (equipes de plantão, senhas de sistema, placas, distribuição de viaturas) e os itens trazem números.",
       "A pegadinha mais comum é usar **arranjo onde é combinação** (ou o contrário): aplique o teste da ordem.",
       "Itens com “**pelo menos um**” quase sempre se resolvem pelo complementar.",
       "Na dúvida real, **deixe em branco**: no Cebraspe, cada erro anula um acerto."),
]

QUIZ = quiz([
    ("C", "Com 3 letras (entre 26) seguidas de 4 algarismos, podendo haver repetição, é possível formar 175.760.000 placas diferentes.",
     "26³ × 10⁴."),
    ("E", "O número de senhas de 4 algarismos distintos é 10.000.",
     "Com algarismos distintos: 10 × 9 × 8 × 7 = 5.040. O valor 10.000 admite repetição."),
    ("C", "Existem 9.000 números naturais de 4 algarismos.",
     "9 × 10 × 10 × 10 (o primeiro não pode ser zero)."),
    ("C", "O número de anagramas da palavra PERITO é 720.",
     "6 letras distintas: 6!."),
    ("E", "O número de anagramas da palavra POLICIA é 5.040.",
     "A letra I se repete: 7!/2! = 2.520."),
    ("C", "Há 120 maneiras de dispor 5 agentes em fila.",
     "5! = 120."),
    ("E", "O número de maneiras de escolher 3 agentes entre 8 para formar uma equipe é 336.",
     "Equipe não tem ordem: C(8, 3) = 56. O valor 336 é arranjo."),
    ("C", "O número de maneiras de escolher, entre 8 pessoas, um delegado, um escrivão e um agente (cargos distintos) é 336.",
     "A ordem importa (cargos): 8 × 7 × 6."),
    ("C", "Em uma reunião com 10 pessoas, se cada uma cumprimentar todas as outras com um aperto de mão, haverá 45 apertos de mão.",
     "C(10, 2) = 45."),
    ("E", "O número de maneiras de 5 pessoas sentarem em volta de uma mesa circular é 120.",
     "Permutação circular: (5 − 1)! = 24."),

    ("C", "Uma comissão de 3 membros deve ser formada a partir de 6 agentes e 4 escrivães, com exatamente 2 agentes e 1 escrivão. Há 60 comissões possíveis.",
     "C(6, 2) × C(4, 1) = 15 × 4."),
    ("C", "Entre 10 servidores, 4 mulheres e 6 homens, o número de comissões de 3 pessoas com pelo menos uma mulher é 100.",
     "Total C(10, 3) = 120 menos comissões só de homens C(6, 3) = 20."),
    ("E", "Na situação do item anterior, o número de comissões formadas só por mulheres é 24.",
     "Só mulheres: C(4, 3) = 4. O valor 24 é a soma das comissões só de homens e só de mulheres."),
    ("C", "Em uma fila de 5 pessoas, há 48 maneiras de duas pessoas determinadas ficarem lado a lado.",
     "Bloco: 4! × 2! = 48."),
    ("E", "O número de anagramas da palavra DELEGADO é 40.320.",
     "8!/(2! · 2!) = 10.080, porque D e E se repetem."),
    ("C", "O número de maneiras de escolher 4 viaturas entre 12 para uma operação, sem importar a ordem, é 495.",
     "C(12, 4) = 495."),
    ("C", "Se um agente tem 3 camisas, 4 calças e 2 pares de sapatos, ele pode montar 24 trajes diferentes.",
     "3 × 4 × 2."),
    ("E", "O número de maneiras de escolher presidente e vice-presidente de uma comissão entre 5 pessoas é 10.",
     "A ordem importa: 5 × 4 = 20. O valor 10 é C(5, 2)."),
    ("C", "Escolher 3 de 10 candidatos para uma vaga é feito do mesmo número de maneiras que escolher 7 dos 10 para não ocupá-la.",
     "C(10, 3) = C(10, 7)."),
    ("C", "Com os algarismos 1, 2, 3, 4 e 5, sem repetição, é possível formar 60 números de 3 algarismos.",
     "5 × 4 × 3."),
], 20)

SOURCES = [
    "Análise combinatória: princípio fundamental da contagem, permutações, arranjos e combinações.",
    "Obras de referência: Morgado et al., Análise combinatória e probabilidade (SBM); Iezzi et al., Fundamentos de matemática elementar, v. 5.",
    SRC_A,
]
