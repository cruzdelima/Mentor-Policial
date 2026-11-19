# -*- coding: utf-8 -*-
"""Raciocínio Lógico · Sequências e progressões — MATERIAL APROFUNDADO."""
from common import *

MATERIAL = material(
    "rlm-sequencias-02", "RLM", "RLM-10", "aprofundado", "Sequências e progressões", "Raciocínio Lógico e Matemática · Sequências",
    "raciocinio_sequencias_aprofundado", "RaciocinioLogico_Sequencias_APROFUNDADO.pdf", None, ["Sequências e", "progressões"],
    ["Padrões numéricos e de letras, progressão aritmética e geométrica, termo geral", "e soma dos termos, com 20 questões no estilo Cebraspe."],
    [("01", "Padrões", "números, letras e figuras"),
     ("02", "PA", "termo geral e soma"),
     ("03", "PG", "termo geral, soma e soma infinita"),
     ("04", "Aplicações", "contagem de múltiplos e crescimento"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Sequências e progressões — Raciocínio Lógico e Matemática",
    "Base: matemática do ensino médio.", 70)

THEORY = [
    exam("Como estudar este material",
         "Sequências caem de dois jeitos: **descobrir a lei de formação** de uma lista (números, letras, figuras) e **calcular termos e "
         "somas** de PA e PG. Decore as quatro fórmulas e treine a pergunta “o que acontece de um termo para o seguinte?”."),

    h2("1. Descobrindo o padrão"),
    p("Compare termos vizinhos: a diferença é constante (soma)? O quociente é constante (multiplicação)? As diferenças crescem? Há duas "
      "sequências intercaladas (posições ímpares e pares)?"),
    tb(["Sequência", "Lei de formação", "Próximo"], [0.36, 0.44, 0.2], [
        ("5, 12, 19, 26, ...", "soma 7", "33"),
        ("2, 6, 18, 54, ...", "multiplica por 3", "162"),
        ("2, 3, 5, 9, 17, ...", "dobra e subtrai 1 (diferenças 1, 2, 4, 8)", "33"),
        ("1, 1, 2, 3, 5, 8, ...", "cada termo é a soma dos dois anteriores (Fibonacci)", "13"),
        ("1, 4, 9, 16, ...", "quadrados perfeitos", "25"),
        ("A, C, E, G, ...", "pula uma letra", "I"),
        ("3, 10, 5, 20, 7, 30, ...", "duas intercaladas: 3, 5, 7 e 10, 20, 30", "9"),
    ]),
    nt("Nas sequências de letras, considere o alfabeto de **26 letras** (com K, W e Y), salvo se o item disser outra coisa. Numere as "
       "letras (A = 1, B = 2...) para enxergar o padrão."),

    h2("2. Progressão aritmética (PA)"),
    key("Fórmulas da PA",
        "Cada termo é o anterior **mais a razão r**. **Termo geral: aₙ = a₁ + (n − 1) · r**. **Soma dos n primeiros: Sₙ = (a₁ + aₙ) · n / 2**."),
    bl("PA (3, 7, 11, ...): r = 4. O 20º termo é a₂₀ = 3 + 19 × 4 = **79**. A soma dos 20 primeiros é (3 + 79) × 20/2 = **820**.",
       "Soma de 1 a 100: (1 + 100) × 100/2 = **5.050**.",
       "Em uma PA, cada termo é a **média** dos seus vizinhos: a₂ = (a₁ + a₃)/2.",
       "**Quantos múltiplos de 7** há entre 100 e 300? O primeiro é 105 e o último 294: 294 = 105 + (n − 1) × 7 → **n = 28**."),

    h2("3. Progressão geométrica (PG)"),
    key("Fórmulas da PG",
        "Cada termo é o anterior **vezes a razão q**. **Termo geral: aₙ = a₁ · qⁿ⁻¹**. **Soma dos n primeiros: Sₙ = a₁ · (qⁿ − 1)/(q − 1)**. "
        "Se **0 < |q| < 1**, a soma infinita é **S = a₁/(1 − q)**."),
    bl("PG (2, 6, 18, ...): q = 3. O 6º termo é 2 × 3⁵ = **486**. A soma dos 6 primeiros é 2 × (3⁶ − 1)/(3 − 1) = **728**.",
       "PG (1, 2, 4, 8, ...): o 10º termo é 2⁹ = **512** e a soma dos 10 primeiros é 2¹⁰ − 1 = **1.023**.",
       "Soma infinita de (10, 5, 2,5, ...): q = 1/2 → S = 10/(1 − 1/2) = **20**.",
       "Crescimento percentual constante é uma PG: um valor que cresce **10% ao ano** é multiplicado por **1,1** a cada ano. "
       "R$ 1.000 viram 1.000 × 1,1³ = **R$ 1.331** em 3 anos."),
    trap("PA × PG",
         "Aumento de **quantidade fixa** (15 apreensões a mais por mês) é **PA**. Aumento de **percentual fixo** (10% ao mês) é **PG**. "
         "Não confunda a razão da PA (soma) com a da PG (multiplicação)."),

    h2("4. Como o Cebraspe cobra"),
    bl("Uma lista com a lei de formação e itens sobre um termo distante (o 50º, o 100º): use o **termo geral**.",
       "Situações com crescimento mensal (apreensões, efetivo, gastos) e itens sobre o total acumulado: use a **soma**.",
       "Padrões de letras e figuras: numere e procure a regra.",
       "Na dúvida real, **deixe em branco**: no Cebraspe, cada erro anula um acerto."),
]

QUIZ = quiz([
    ("C", "Na sequência 5, 12, 19, 26, ..., o 10º termo é 68.",
     "PA de razão 7: 5 + 9 × 7 = 68."),
    ("E", "Na sequência 2, 6, 18, 54, ..., o próximo termo é 108.",
     "PG de razão 3: 54 × 3 = 162."),
    ("C", "Na sequência 1, 1, 2, 3, 5, 8, 13, ..., o termo seguinte a 13 é 21.",
     "Fibonacci: 8 + 13."),
    ("C", "Na sequência de letras A, C, E, G, ..., a próxima letra é I.",
     "Pula uma letra a cada passo."),
    ("E", "O 20º termo da PA (3, 7, 11, ...) é 83.",
     "a₂₀ = 3 + 19 × 4 = 79."),
    ("C", "A soma dos 20 primeiros termos da PA (3, 7, 11, ...) é 820.",
     "(3 + 79) × 20/2."),
    ("C", "A soma dos números naturais de 1 a 100 é 5.050.",
     "(1 + 100) × 100/2."),
    ("E", "O 6º termo da PG (2, 6, 18, ...) é 1.458.",
     "a₆ = 2 × 3⁵ = 486."),
    ("C", "A soma dos infinitos termos da PG (10, 5, 2,5, ...) é 20.",
     "S = 10/(1 − 1/2)."),
    ("E", "Em uma PA, o termo central de três termos consecutivos é sempre o produto dos outros dois dividido por 2.",
     "É a média aritmética (soma dividida por 2)."),

    ("C", "Entre 100 e 300 há exatamente 28 múltiplos de 7.",
     "De 105 a 294: (294 − 105)/7 + 1 = 28."),
    ("C", "Uma delegacia registrou 120 apreensões em janeiro e, a cada mês, 15 a mais que no mês anterior. Ao final de dezembro, o total do ano foi de 2.430 apreensões.",
     "PA com a₁ = 120 e a₁₂ = 285: (120 + 285) × 12/2 = 2.430."),
    ("E", "Na situação do item anterior, em dezembro foram registradas 300 apreensões.",
     "a₁₂ = 120 + 11 × 15 = 285."),
    ("C", "Um orçamento de R$ 1.000 que aumenta 10% ao ano, de forma cumulativa, passa a R$ 1.331 após 3 anos.",
     "PG de razão 1,1: 1.000 × 1,1³."),
    ("E", "Um valor que aumenta 10% ao ano, de forma cumulativa, forma uma progressão aritmética de razão 10.",
     "Aumento percentual constante gera PG de razão 1,1."),
    ("C", "Na sequência 3, 10, 5, 20, 7, 30, ..., o próximo termo é 9.",
     "Posições ímpares: 3, 5, 7, 9."),
    ("C", "A soma dos 10 primeiros termos da PG (1, 2, 4, 8, ...) é 1.023.",
     "2¹⁰ − 1."),
    ("E", "Na sequência 2, 3, 5, 9, 17, ..., o próximo termo é 25.",
     "Diferenças 1, 2, 4, 8, 16: o próximo é 33."),
    ("C", "A soma dos números pares de 2 a 100 é 2.550.",
     "PA com 50 termos: (2 + 100) × 50/2."),
    ("E", "O 50º termo da PA (5, 8, 11, ...) é 155.",
     "5 + 49 × 3 = 152."),
], 20)

SOURCES = [
    "Matemática do ensino médio: sequências, progressões aritméticas e geométricas.",
    "Obras de referência: Iezzi e Hazzan, Fundamentos de matemática elementar, v. 4.",
    SRC_A,
]
