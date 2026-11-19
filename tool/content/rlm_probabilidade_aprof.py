# -*- coding: utf-8 -*-
"""Raciocínio Lógico · Probabilidade — MATERIAL APROFUNDADO."""
from common import *

MATERIAL = material(
    "rlm-probabilidade-02", "RLM", "RLM-12", "aprofundado", "Probabilidade", "Raciocínio Lógico e Matemática · Probabilidade",
    "raciocinio_probabilidade_aprofundado", "RaciocinioLogico_Probabilidade_APROFUNDADO.pdf", None, ["Probabilidade"],
    ["Probabilidade clássica, complementar, união, eventos independentes, condicional", "e repetição de experimentos, com 20 questões no estilo Cebraspe."],
    [("01", "Definição", "casos favoráveis sobre possíveis"),
     ("02", "Regras", "complementar, união e interseção"),
     ("03", "Condicional", "probabilidade dentro de um grupo"),
     ("04", "Repetições", "com e sem reposição, binomial"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Probabilidade — Raciocínio Lógico e Matemática",
    "Base: probabilidade elementar e análise combinatória.", 90)

THEORY = [
    exam("Como estudar este material",
         "Probabilidade é cobrada em **toda** prova de PF e PRF, quase sempre com uma situação concreta (sorteio de equipes, tiros, "
         "testes de bafômetro, perfil de servidores). Domine três ideias: **favoráveis/possíveis**, **complementar** (“pelo menos um”) e "
         "**multiplicação** para eventos em sequência. A combinatória do material anterior é a base para contar os casos."),

    h2("1. Definição clássica"),
    key("Probabilidade",
        "Em um espaço amostral com resultados **igualmente prováveis**: **P(A) = número de casos favoráveis / número de casos possíveis**. "
        "Sempre **0 ≤ P(A) ≤ 1** (de 0% a 100%)."),
    bl("Dado honesto: P(par) = 3/6 = **1/2**; P(número maior que 4) = 2/6 = **1/3**.",
       "Dois dados: 36 resultados. P(soma 7) = 6/36 = **1/6**; P(soma 12) = **1/36**; P(soma pelo menos 10) = 6/36 = **1/6**.",
       "Baralho de 52 cartas: P(ás) = 4/52 = **1/13**.",
       "Evento **impossível**: P = 0. Evento **certo**: P = 1."),

    h2("2. Regras"),
    tb(["Regra", "Fórmula", "Uso"], [0.22, 0.4, 0.38], [
        ("**Complementar**", "P(não A) = 1 − P(A)", "“Pelo menos um”, “nenhum”"),
        ("**União**", "P(A ∪ B) = P(A) + P(B) − P(A ∩ B)", "“A ou B”"),
        ("**Mutuamente exclusivos**", "P(A ∪ B) = P(A) + P(B)", "Não podem ocorrer juntos"),
        ("**Independentes**", "P(A ∩ B) = P(A) · P(B)", "Um não altera o outro"),
        ("**Condicional**", "P(A | B) = P(A ∩ B)/P(B)", "Sabendo que B ocorreu"),
    ]),
    bl("Se P(A) = 0,3 e P(B) = 0,5, independentes: P(A ∩ B) = **0,15** e P(A ∪ B) = 0,3 + 0,5 − 0,15 = **0,65**.",
       "Lançar uma moeda 3 vezes: P(pelo menos uma cara) = 1 − P(nenhuma cara) = 1 − 1/8 = **7/8**."),
    trap("Exclusivos não são independentes",
         "Eventos **mutuamente exclusivos** (não ocorrem juntos) com probabilidades positivas **não** são independentes: se um ocorreu, o "
         "outro passa a ter probabilidade zero. Não confunda “não podem ocorrer juntos” com “um não influencia o outro”."),

    h2("3. Probabilidade condicional"),
    p("Quando o item diz “**sabendo que**”, “**dado que**” ou “**entre os que**”, o espaço amostral **encolhe** para o grupo informado. Monte "
      "uma tabela de dupla entrada."),
    tb(["", "Fez o curso", "Não fez", "Total"], [0.25, 0.25, 0.25, 0.25], [
        ("Homens", "25", "15", "40"),
        ("Mulheres", "10", "10", "20"),
        ("Total", "35", "25", "60"),
    ]),
    bl("Sorteado um policial ao acaso: P(fez o curso) = 35/60 = **7/12**.",
       "**Sabendo que** o sorteado fez o curso, P(ser mulher) = 10/35 = **2/7** (o espaço passa a ser os 35 que fizeram).",
       "**Sabendo que** é mulher, P(fez o curso) = 10/20 = **1/2**."),

    h2("4. Experimentos repetidos"),
    h3("Com e sem reposição"),
    bl("Urna com 5 bolas brancas e 3 pretas. Retiram-se 2 bolas.",
       "**Sem reposição**: P(duas pretas) = 3/8 × 2/7 = **3/28** (o total diminui).",
       "**Com reposição**: P(duas pretas) = 3/8 × 3/8 = **9/64**.",
       "Sem reposição, também se pode contar por combinação: C(3, 2)/C(8, 2) = 3/28."),
    h3("Exatamente k sucessos (binomial)"),
    key("Fórmula",
        "Em **n** repetições independentes, com probabilidade **p** de sucesso em cada uma: **P(exatamente k) = C(n, k) · pᵏ · (1 − p)ⁿ⁻ᵏ**. "
        "O C(n, k) conta **em quais tentativas** ocorrem os sucessos."),
    bl("Um atirador acerta o alvo com probabilidade 0,8. Em 3 tiros, P(exatamente 2 acertos) = C(3, 2) × 0,8² × 0,2 = 3 × 0,64 × 0,2 = **0,384**.",
       "P(pelo menos um acerto em 3 tiros) = 1 − 0,2³ = 1 − 0,008 = **0,992**.",
       "Erro comum: esquecer o C(n, k) e responder 0,8² × 0,2 = 0,128."),

    h2("5. Sorteios com combinatória"),
    p("Quando se sorteia um **grupo**, conte os casos com combinação. De 10 servidores (4 mulheres), sorteia-se uma comissão de 3: "
      "P(só mulheres) = C(4, 3)/C(10, 3) = 4/120 = **1/30**; P(pelo menos uma mulher) = 1 − C(6, 3)/C(10, 3) = 1 − 20/120 = **5/6**."),

    h2("6. Como o Cebraspe cobra"),
    bl("Um texto com uma situação (equipes, testes, tiros, sorteios) e itens com probabilidades em fração ou porcentagem.",
       "“Pelo menos um”: **complementar**.",
       "“Sabendo que”: **condicional** (encolha o espaço).",
       "Sem reposição: o denominador **diminui** a cada retirada.",
       "Na dúvida real, **deixe em branco**: no Cebraspe, cada erro anula um acerto."),
]

QUIZ = quiz([
    ("C", "No lançamento de um dado honesto, a probabilidade de sair número par é 1/2.",
     "3 favoráveis em 6."),
    ("E", "No lançamento de dois dados honestos, a probabilidade de a soma ser 7 é 1/36.",
     "Há 6 pares com soma 7: 6/36 = 1/6."),
    ("C", "A probabilidade de um evento é sempre um número entre 0 e 1, inclusive.",
     "Definição."),
    ("C", "Se P(A) = 0,3, então P(não A) = 0,7.",
     "Complementar."),
    ("E", "Se A e B são independentes, com P(A) = 0,3 e P(B) = 0,5, então P(A ∪ B) = 0,8.",
     "P(A ∪ B) = 0,3 + 0,5 − 0,15 = 0,65."),
    ("C", "Lançando-se uma moeda honesta 3 vezes, a probabilidade de sair pelo menos uma cara é 7/8.",
     "1 − (1/2)³."),
    ("E", "Eventos mutuamente exclusivos, ambos com probabilidade positiva, são independentes.",
     "Se um ocorre, o outro fica impossível: há dependência."),
    ("C", "Retirando-se, sem reposição, 2 bolas de uma urna com 5 brancas e 3 pretas, a probabilidade de ambas serem pretas é 3/28.",
     "3/8 × 2/7."),
    ("E", "Retirando-se, com reposição, 2 bolas da mesma urna, a probabilidade de ambas serem pretas é 3/28.",
     "Com reposição: 3/8 × 3/8 = 9/64."),
    ("C", "A probabilidade de retirar um ás de um baralho comum de 52 cartas é 1/13.",
     "4/52."),

    ("C", "Em uma delegacia com 60 policiais, 40 homens e 20 mulheres, 25 homens e 10 mulheres fizeram um curso de inteligência. Sorteando-se um policial ao acaso, a probabilidade de ele ter feito o curso é 7/12.",
     "35/60 = 7/12."),
    ("C", "Na situação do item anterior, sabendo que o sorteado fez o curso, a probabilidade de ser mulher é 2/7.",
     "Condicional: 10/35."),
    ("E", "Na mesma situação, sabendo que o sorteado é mulher, a probabilidade de ela ter feito o curso é 2/7.",
     "Entre as 20 mulheres, 10 fizeram: 1/2."),
    ("C", "Um atirador acerta o alvo com probabilidade 0,8 em cada tiro, de forma independente. A probabilidade de acertar exatamente 2 de 3 tiros é 0,384.",
     "C(3, 2) × 0,8² × 0,2."),
    ("E", "Na situação do item anterior, a probabilidade de acertar exatamente 2 de 3 tiros é 0,128.",
     "Faltou multiplicar por C(3, 2) = 3, que conta as posições dos acertos."),
    ("C", "Na mesma situação, a probabilidade de acertar pelo menos um dos 3 tiros é 0,992.",
     "1 − 0,2³."),
    ("C", "De 10 servidores, 4 mulheres e 6 homens, sorteia-se uma comissão de 3. A probabilidade de a comissão ter só mulheres é 1/30.",
     "C(4, 3)/C(10, 3) = 4/120."),
    ("E", "Na situação do item anterior, a probabilidade de a comissão ter pelo menos uma mulher é 1/6.",
     "1 − C(6, 3)/C(10, 3) = 1 − 1/6 = 5/6."),
    ("C", "Se a probabilidade de um teste de etilômetro dar positivo para um motorista abordado é 0,1, de forma independente, a probabilidade de os dois primeiros motoristas testarem negativo é 0,81.",
     "0,9 × 0,9."),
    ("E", "Se A e B são eventos quaisquer, então P(A ∪ B) = P(A) + P(B).",
     "Só vale se forem mutuamente exclusivos; em geral, subtrai-se P(A ∩ B)."),
], 20)

SOURCES = [
    "Probabilidade elementar: definição clássica, regras da adição e da multiplicação, probabilidade condicional e distribuição binomial.",
    "Obras de referência: Morgado et al., Análise combinatória e probabilidade (SBM); Bussab e Morettin, Estatística básica.",
    SRC_A,
]
