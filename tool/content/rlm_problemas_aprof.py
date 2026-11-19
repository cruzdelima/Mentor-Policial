# -*- coding: utf-8 -*-
"""Raciocínio Lógico · Problemas aritméticos e equações — MATERIAL APROFUNDADO."""
from common import *

MATERIAL = material(
    "rlm-problemas-02", "RLM", "RLM-09", "aprofundado", "Problemas aritméticos e equações", "Raciocínio Lógico e Matemática · Matemática básica",
    "raciocinio_problemas_aprofundado", "RaciocinioLogico_Problemas_APROFUNDADO.pdf", None, ["Problemas e", "equações"],
    ["Frações, MMC e MDC, equações do 1º e do 2º grau, sistemas e os problemas típicos", "de prova, com 20 questões no estilo Cebraspe."],
    [("01", "Operações", "frações, decimais, MMC e MDC"),
     ("02", "Equações", "1º grau, sistemas e 2º grau"),
     ("03", "Problemas", "idades, trabalho conjunto, divisão"),
     ("04", "Método", "do texto para a equação"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Problemas aritméticos e equações — Raciocínio Lógico e Matemática",
    "Base: matemática do ensino fundamental e médio.", 85)

THEORY = [
    exam("Como estudar este material",
         "Os problemas do Cebraspe vêm em textos com várias informações e itens que afirmam um resultado. O segredo é **traduzir o texto "
         "em equação**: dê nome à incógnita, escreva as relações e só depois faça as contas. Muitas vezes dá para **testar o valor do item** "
         "no enunciado em vez de resolver a equação."),

    h2("1. Frações, MMC e MDC"),
    bl("Somar frações: iguale os denominadores pelo **MMC**. 1/4 + 1/6 = 3/12 + 2/12 = **5/12**.",
       "“2/5 de” = multiplicar por 2/5. 2/5 de R$ 10.000 = **R$ 4.000**.",
       "Fração do **restante**: se 2/5 do orçamento foram gastos e depois 3/4 do que sobrou, o segundo gasto foi 3/4 de 6.000 = **4.500**."),
    tb(["Ferramenta", "Quando usar", "Exemplo"], [0.14, 0.4, 0.46], [
        ("**MMC**", "Eventos que se **repetem** e coincidem; menor múltiplo comum.",
         "Duas rondas passam a cada 12 e 18 min. Juntas de novo em MMC(12, 18) = **36 min**."),
        ("**MDC**", "**Dividir** em grupos iguais do **maior tamanho** possível.",
         "48 agentes e 36 escrivães em equipes do mesmo tamanho, sem misturar: MDC(48, 36) = **12** por equipe → 4 + 3 = **7 equipes**."),
    ]),

    h2("2. Equação do 1º grau e sistemas"),
    bl("Isole a incógnita: 3x − 7 = 11 → 3x = 18 → **x = 6**.",
       "**Sistema** por adição: x + y = 50 e x − y = 10 → 2x = 60 → **x = 30**, **y = 20**.",
       "**Sistema** por substituição: carros (c) e motos (m) somam 20 veículos e 56 rodas: c + m = 20 e 4c + 2m = 56. "
       "Substituindo m = 20 − c: 4c + 40 − 2c = 56 → **c = 8**, **m = 12**."),

    h2("3. Equação do 2º grau"),
    key("Fórmula de Bhaskara",
        "Para ax² + bx + c = 0: **Δ = b² − 4ac** e **x = (−b ± √Δ)/2a**. Se Δ > 0, duas raízes reais distintas; Δ = 0, uma raiz (dupla); "
        "Δ < 0, **nenhuma raiz real**."),
    bl("**Soma** das raízes = **−b/a**; **produto** = **c/a**. Em x² − 5x + 6 = 0, soma 5 e produto 6: raízes **2 e 3**.",
       "x² − x − 12 = 0: soma 1, produto −12 → raízes **4 e −3**.",
       "Em problemas, descarte a raiz que não faz sentido (número negativo de pessoas, idade negativa)."),

    h2("4. Problemas típicos"),
    tb(["Tipo", "Como montar", "Exemplo"], [0.18, 0.36, 0.46], [
        ("**Idades**", "Some o mesmo tempo t às idades de todos.",
         "Pai com 40 e filho com 10. Em t anos, 40 + t = 2(10 + t) → **t = 20**."),
        ("**Trabalho conjunto**", "Some as **frações feitas por hora**: 1/a + 1/b = 1/T.",
         "A digitaliza um arquivo em 6 h e B em 3 h. Juntos: 1/6 + 1/3 = 1/2 → **2 h**."),
        ("**Um faz, outro desfaz**", "Subtraia as taxas.",
         "Uma bomba enche um tanque em 10 h e um vazamento o esvazia em 15 h: 1/10 − 1/15 = 1/30 → **30 h**."),
        ("**Divisão com mudança**", "Escreva a parte de cada um nas duas situações.",
         "R$ 1.200 divididos igualmente; com 2 pessoas a menos, cada um receberia R$ 50 a mais: 1.200/(n − 2) − 1.200/n = 50 → **n = 8**."),
    ]),
    trap("Teste o valor do item",
         "Se o item diz “o grupo tinha 8 pessoas”, confira: 1.200/8 = 150 e 1.200/6 = 200. A diferença é 50: **certo**. Testar é mais rápido "
         "que resolver a equação do 2º grau."),

    h2("5. Como o Cebraspe cobra"),
    bl("Um texto-base (orçamento de uma operação, escala de plantões, divisão de equipes) seguido de 3 a 5 itens com resultados.",
       "Itens de MMC disfarçados: “os dois plantões voltarão a coincidir em...”.",
       "Itens de MDC disfarçados: “o maior número de pessoas por equipe”.",
       "Na dúvida real, **deixe em branco**: no Cebraspe, cada erro anula um acerto."),
]

QUIZ = quiz([
    ("C", "A solução da equação 3x − 7 = 11 é x = 6.",
     "3x = 18."),
    ("E", "A soma 1/4 + 1/6 é igual a 2/10.",
     "1/4 + 1/6 = 3/12 + 2/12 = 5/12."),
    ("C", "Se x + y = 50 e x − y = 10, então x = 30.",
     "Somando: 2x = 60."),
    ("C", "As raízes da equação x² − 5x + 6 = 0 são 2 e 3.",
     "Soma 5 e produto 6."),
    ("E", "A equação x² + 2x + 5 = 0 possui duas raízes reais distintas.",
     "Δ = 4 − 20 = −16 < 0: nenhuma raiz real."),
    ("C", "Na equação x² − x − 12 = 0, o produto das raízes é −12.",
     "Produto = c/a = −12 (raízes 4 e −3)."),
    ("C", "O MMC de 12 e 18 é 36.",
     "Menor múltiplo comum."),
    ("E", "O MDC de 48 e 36 é 6.",
     "MDC(48, 36) = 12."),
    ("C", "Dois terços de 2/5 de um valor correspondem a 4/15 desse valor.",
     "2/3 × 2/5 = 4/15."),
    ("E", "Se o dobro de um número somado a 8 é igual a 30, esse número é 19.",
     "2x + 8 = 30 → x = 11."),

    ("C", "Duas equipes de ronda passam por um mesmo posto a cada 12 e a cada 18 minutos, respectivamente. Se passaram juntas às 8 h, voltarão a passar juntas às 8 h 36 min.",
     "MMC(12, 18) = 36."),
    ("C", "Para dividir 48 agentes e 36 escrivães em equipes com o mesmo número de pessoas, sem misturar cargos e com o maior número possível de pessoas por equipe, serão formadas 7 equipes.",
     "MDC = 12; 48/12 + 36/12 = 4 + 3."),
    ("E", "Em um pátio há carros e motos, num total de 20 veículos e 56 rodas. Nesse caso, há 12 carros.",
     "c + m = 20 e 4c + 2m = 56 → c = 8 e m = 12."),
    ("C", "Um pai tem 40 anos e o filho, 10. Daqui a 20 anos, a idade do pai será o dobro da do filho.",
     "60 = 2 × 30."),
    ("C", "Um servidor digitaliza um arquivo em 6 horas e outro, em 3 horas. Trabalhando juntos, no mesmo ritmo, levarão 2 horas.",
     "1/6 + 1/3 = 1/2."),
    ("E", "Uma bomba enche um tanque em 10 horas, e um vazamento o esvazia em 15 horas. Com a bomba ligada e o vazamento aberto, o tanque vazio ficará cheio em 25 horas.",
     "1/10 − 1/15 = 1/30: 30 horas."),
    ("C", "Um prêmio de R$ 1.200 seria dividido igualmente entre os membros de um grupo. Como 2 membros desistiram, cada um dos demais recebeu R$ 50 a mais. Então o grupo tinha inicialmente 8 membros.",
     "1.200/6 − 1.200/8 = 200 − 150 = 50."),
    ("E", "De um orçamento de R$ 10.000, gastaram-se 2/5 com combustível e 3/4 do restante com manutenção. Sobraram R$ 2.500.",
     "Combustível 4.000; restam 6.000; manutenção 4.500; sobram 1.500."),
    ("C", "Se a soma de três números inteiros consecutivos é 75, o maior deles é 26.",
     "x + x + 1 + x + 2 = 75 → x = 24; maior 26."),
    ("E", "Se dois quintos dos 150 candidatos de uma turma foram aprovados, o número de reprovados é 60.",
     "Aprovados 60; reprovados 90."),
], 20)

SOURCES = [
    "Matemática básica: operações, MMC e MDC, equações e sistemas.",
    "Obras de referência: Iezzi et al., Matemática: ciência e aplicações; Dante, Matemática: contexto e aplicações.",
    SRC_A,
]
