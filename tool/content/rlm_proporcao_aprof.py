# -*- coding: utf-8 -*-
"""Raciocínio Lógico · Razão, proporção, regra de três e porcentagem — MATERIAL APROFUNDADO."""
from common import *

MATERIAL = material(
    "rlm-proporcao-02", "RLM", "RLM-08", "aprofundado", "Razão, proporção, regra de três e porcentagem", "Raciocínio Lógico e Matemática · Matemática básica",
    "raciocinio_proporcao_aprofundado", "RaciocinioLogico_Proporcao_APROFUNDADO.pdf", None, ["Proporção e", "porcentagem"],
    ["Razão, proporção, divisão proporcional, regra de três simples e composta, porcentagem", "e variações sucessivas, com 20 questões no estilo Cebraspe."],
    [("01", "Razão e proporção", "propriedade fundamental e escala"),
     ("02", "Divisão proporcional", "direta e inversa"),
     ("03", "Regra de três", "simples e composta, direta e inversa"),
     ("04", "Porcentagem", "aumentos, descontos e variações sucessivas"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Razão, proporção, regra de três e porcentagem — Raciocínio Lógico e Matemática",
    "Base: matemática do ensino fundamental e médio.", 85)

THEORY = [
    exam("Como estudar este material",
         "É a matemática mais cobrada em provas policiais e a que mais aparece **dentro de outros assuntos** (probabilidade, problemas, "
         "estatística). O Cebraspe gosta de situações com **viaturas, efetivo, apreensões e orçamento**. Treine a regra de três composta "
         "e os **fatores multiplicativos** de porcentagem: eles resolvem os itens mais difíceis em uma linha."),

    h2("1. Razão e proporção"),
    key("Definições",
        "**Razão** entre a e b (b ≠ 0) é o quociente **a/b**. **Proporção** é a igualdade entre duas razões: **a/b = c/d**. Propriedade "
        "fundamental: o **produto dos meios é igual ao produto dos extremos**: **a · d = b · c**."),
    bl("Numa equipe com 12 agentes e 18 escrivães, a razão entre agentes e escrivães é 12/18 = **2/3** (lê-se “2 para 3”).",
       "Se x/15 = 4/6, então 6x = 60 e **x = 10**.",
       "**Escala** é a razão entre a medida no desenho e a medida real, na mesma unidade. Num mapa 1:50.000, **4 cm** no mapa são "
       "4 × 50.000 = 200.000 cm = **2 km** na realidade.",
       "**Velocidade média** e **densidade** também são razões (km/h, hab/km²)."),
    h3("Grandezas direta e inversamente proporcionais"),
    tb(["Tipo", "O que acontece", "Exemplo"], [0.24, 0.38, 0.38], [
        ("**Diretamente** proporcionais", "Uma dobra, a outra dobra. A **razão** entre elas é constante.", "Viaturas e litros de combustível"),
        ("**Inversamente** proporcionais", "Uma dobra, a outra cai pela metade. O **produto** é constante.", "Agentes e dias para concluir uma tarefa"),
    ]),

    h2("2. Divisão proporcional"),
    p("Para dividir um total em partes **diretamente proporcionais** a números dados, some os números, divida o total pela soma (a "
      "**constante**) e multiplique cada número por ela."),
    bl("Dividir **R$ 9.000** entre três delegacias proporcionalmente a **2, 3 e 4**: soma 9; constante 9.000/9 = 1.000. Partes: **2.000, 3.000 e 4.000**.",
       "Na divisão **inversamente proporcional**, use os **inversos** dos números. Dividir **R$ 600** inversamente a **2 e 3**: "
       "k/2 + k/3 = 600 → 5k/6 = 600 → k = 720. Partes: **360 e 240** (quem tem o número maior recebe menos).",
       "Dividir **R$ 3.600** inversamente a **2, 3 e 6**: k(1/2 + 1/3 + 1/6) = 3.600 → k = 3.600. Partes: **1.800, 1.200 e 600**."),

    h2("3. Regra de três"),
    h3("Simples"),
    bl("**Direta**: se 5 viaturas consomem 300 L por semana, 8 viaturas consomem 300 × 8/5 = **480 L**.",
       "**Inversa**: se 6 agentes concluem uma tarefa em 10 dias, 4 agentes concluem em 6 × 10/4 = **15 dias** (menos gente, mais dias)."),
    h3("Composta"),
    p("Isole a grandeza procurada e compare cada uma das outras com ela, perguntando: **se esta aumentar, a procurada aumenta "
      "(direta) ou diminui (inversa)?** Depois, multiplique o valor conhecido pelas frações, invertendo as das grandezas inversas."),
    tb(["Peritos", "Dias", "Laudos"], [0.33, 0.33, 0.34], [
        ("4", "6", "120"),
        ("6", "8", "x"),
    ]),
    p("Mais peritos → mais laudos (direta). Mais dias → mais laudos (direta). Então x = 120 × (6/4) × (8/6) = **240 laudos**."),
    trap("Cuidado com a grandeza inversa",
         "Se 8 agentes, trabalhando 6 horas por dia, fazem um levantamento em 15 dias, quantos dias levariam 10 agentes trabalhando 8 horas "
         "por dia? Mais agentes → menos dias (inversa); mais horas → menos dias (inversa). x = 15 × (8/10) × (6/8) = **9 dias**."),

    h2("4. Porcentagem"),
    key("Fator multiplicativo",
        "**x%** = x/100. Aumentar **p%** é multiplicar por **(1 + p/100)**; diminuir p% é multiplicar por **(1 − p/100)**. "
        "Ex.: aumento de 15% → × 1,15; desconto de 20% → × 0,80."),
    bl("30% de 250 = 0,3 × 250 = **75**.",
       "**Variação percentual** = (valor final − valor inicial)/valor inicial. De 80 para 100: 20/80 = **25%** de aumento. De 100 para 80: "
       "20/100 = **20%** de redução.",
       "Para achar o valor **antes** de um aumento: divida pelo fator. Se, após aumento de 20%, o valor é 2.400, o original é 2.400/1,2 = **2.000**.",
       "Percentual de percentual: 40% de 50% = 0,4 × 0,5 = **20%**."),
    h3("Variações sucessivas"),
    tb(["Situação", "Conta", "Resultado"], [0.42, 0.3, 0.28], [
        ("Aumento de 10% e depois de 20%", "1,10 × 1,20 = 1,32", "**+32%** (não 30%)"),
        ("Aumento de 20% e depois de 20%", "1,20 × 1,20 = 1,44", "**+44%**"),
        ("Desconto de 20% e depois aumento de 20%", "0,80 × 1,20 = 0,96", "**−4%**"),
        ("Aumento de 10% e depois desconto de 10%", "1,10 × 0,90 = 0,99", "**−1%**"),
        ("Descontos de 15% e de 10%", "0,85 × 0,90 = 0,765", "**−23,5%**"),
        ("Desfazer um aumento de 25%", "1/1,25 = 0,80", "desconto de **20%**"),
    ]),
    trap("Porcentagens não se somam",
         "Aumentos sucessivos **se multiplicam**. E um desconto de p% **não desfaz** um aumento de p%: o resultado final é sempre menor que "
         "o original."),

    h2("5. Como o Cebraspe cobra"),
    bl("Um texto com dados de uma operação (efetivo, viaturas, apreensões) e itens que pedem uma razão, uma divisão ou uma variação.",
       "Itens de variação sucessiva com o resultado “somado” (10% + 20% = 30%): **errados**.",
       "Regra de três composta com uma grandeza **inversa** escondida.",
       "Na dúvida real, **deixe em branco**: no Cebraspe, cada erro anula um acerto."),
]

QUIZ = quiz([
    ("C", "Em uma equipe com 12 agentes e 18 escrivães, a razão entre o número de agentes e o de escrivães é 2/3.",
     "12/18 = 2/3."),
    ("C", "Se x/15 = 4/6, então x = 10.",
     "6x = 60."),
    ("E", "Em um mapa na escala 1:50.000, uma distância de 4 cm corresponde a 20 km na realidade.",
     "4 × 50.000 = 200.000 cm = 2 km."),
    ("C", "Dividindo-se R$ 9.000 em partes diretamente proporcionais a 2, 3 e 4, a maior parte será de R$ 4.000.",
     "Constante 9.000/9 = 1.000; maior parte 4 × 1.000."),
    ("E", "Dividindo-se R$ 600 em partes inversamente proporcionais a 2 e 3, a maior parte será de R$ 240.",
     "k = 720; partes 360 e 240. A maior é 360."),
    ("C", "Se 5 viaturas consomem 300 L de combustível por semana, 8 viaturas, nas mesmas condições, consumirão 480 L.",
     "Regra de três direta: 300 × 8/5."),
    ("E", "Se 6 agentes concluem uma tarefa em 10 dias, 4 agentes, no mesmo ritmo, concluirão a tarefa em 6 dias.",
     "Grandezas inversas: 6 × 10/4 = 15 dias."),
    ("C", "Um aumento de 10% seguido de outro aumento de 20% corresponde a um aumento total de 32%.",
     "1,1 × 1,2 = 1,32."),
    ("E", "Um desconto de 20% seguido de um aumento de 20% faz o preço voltar ao valor original.",
     "0,8 × 1,2 = 0,96: queda de 4%."),
    ("C", "Para desfazer um aumento de 25%, é necessário um desconto de 20%.",
     "1/1,25 = 0,8."),

    ("C", "O efetivo de uma delegacia passou de 400 para 460 policiais. Nesse caso, o aumento foi de 15%.",
     "60/400 = 0,15."),
    ("E", "O número de apreensões caiu de 100 para 80 em um ano e voltou a 100 no ano seguinte. Nesse caso, o aumento no segundo ano foi de 20%.",
     "De 80 para 100: 20/80 = 25%."),
    ("C", "Se 4 peritos analisam 120 laudos em 6 dias, 6 peritos, no mesmo ritmo, analisam 240 laudos em 8 dias.",
     "120 × (6/4) × (8/6) = 240."),
    ("C", "Se 8 agentes, trabalhando 6 horas por dia, concluem um levantamento em 15 dias, então 10 agentes, trabalhando 8 horas por dia, concluem o mesmo levantamento em 9 dias.",
     "Duas grandezas inversas: 15 × (8/10) × (6/8) = 9."),
    ("E", "Um servidor teve reajustes de 20% em um ano e de 20% no ano seguinte. O reajuste acumulado foi de 40%.",
     "1,2 × 1,2 = 1,44: 44%."),
    ("C", "Se, após um aumento de 20%, o valor de uma diária passou a R$ 2.400, o valor anterior era R$ 2.000.",
     "2.400/1,2 = 2.000."),
    ("C", "Dois descontos sucessivos de 15% e 10% equivalem a um único desconto de 23,5%.",
     "0,85 × 0,9 = 0,765."),
    ("E", "Dividindo-se R$ 3.600 em partes inversamente proporcionais a 2, 3 e 6, a menor parte será de R$ 1.200.",
     "k = 3.600; partes 1.800, 1.200 e 600. A menor é 600."),
    ("C", "Se 40% dos servidores de um órgão são mulheres e 50% delas trabalham na área operacional, então as mulheres da área operacional são 20% dos servidores.",
     "0,4 × 0,5 = 0,2."),
    ("E", "Se o preço de um equipamento subiu 10% e depois caiu 10%, o preço final é igual ao inicial.",
     "1,1 × 0,9 = 0,99: 1% abaixo."),
], 20)

SOURCES = [
    "Matemática básica: razões, proporções, regra de três e porcentagem.",
    "Obras de referência: Iezzi et al., Matemática: ciência e aplicações; Dante, Matemática: contexto e aplicações.",
    SRC_A,
]
