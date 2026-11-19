# -*- coding: utf-8 -*-
"""Raciocínio Lógico · Razão, proporção, regra de três e porcentagem — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "rlm-proporcao-01", "RLM", "RLM-08", "resumo", "Razão, proporção, regra de três e porcentagem", "Raciocínio Lógico e Matemática · Matemática básica",
    "raciocinio_proporcao", "RaciocinioLogico_Proporcao_RESUMO.pdf", None, ["Proporção e", "porcentagem"], RES_SUB,
    RES_ITEMS("proporção, regra de três e porcentagem"),
    "Tópico do edital: Razão, proporção, regra de três e porcentagem — Raciocínio Lógico e Matemática",
    "Base: matemática básica.", 25)

THEORY = [
    exam("O que a banca cobra",
         "Razões em situações reais, **divisão proporcional**, **regra de três composta** e **porcentagens sucessivas**."),
    h2("1. Razão e proporção"),
    bl("Razão a/b; proporção a/b = c/d → **a · d = b · c**.",
       "Escala 1:50.000 → 1 cm = 500 m.",
       "Direta: razão constante. Inversa: **produto** constante."),
    h2("2. Divisão proporcional"),
    bl("Direta: total ÷ soma dos números = constante; multiplique.",
       "Inversa: use os **inversos** (quem tem número maior recebe menos)."),
    h2("3. Regra de três"),
    bl("Compare cada grandeza com a procurada: aumenta junto (direta) ou ao contrário (inversa).",
       "Multiplique pelas frações, **invertendo as inversas**."),
    h2("4. Porcentagem"),
    bl("Aumento de p% → × (1 + p/100); desconto → × (1 − p/100).",
       "Variação = (final − inicial)/**inicial**.",
       "Sucessivas: **multiplique** os fatores.",
       "Valor antes do aumento: **divida** pelo fator."),
]

SUMMARY = [
    h2("Quadro rápido"),
    tb(["Situação", "Fator", "Resultado"], [0.44, 0.3, 0.26], [
        ("+10% e +20%", "1,1 × 1,2", "+32%"),
        ("+20% e +20%", "1,2 × 1,2", "+44%"),
        ("−20% e +20%", "0,8 × 1,2", "−4%"),
        ("+10% e −10%", "1,1 × 0,9", "−1%"),
        ("−15% e −10%", "0,85 × 0,9", "−23,5%"),
        ("Desfazer +25%", "1 ÷ 1,25", "−20%"),
        ("Desfazer −20%", "1 ÷ 0,8", "+25%"),
    ]),
    h2("Leve para a prova"),
    bl("Meios × extremos.",
       "Inversa: **inverta** a fração.",
       "Porcentagens se **multiplicam**.",
       "Variação: divide pelo **inicial**.",
       "Desconto não desfaz aumento de mesma taxa."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "PROPORÇÃO", "rootSub": "e porcentagem",
    "left": [
        {"label": "Razão", "items": ["a dividido por b", "escala", "velocidade"]},
        {"label": "Proporção", "items": ["a/b = c/d", "meios e extremos", "produto cruzado"]},
        {"label": "Direta", "items": ["dobra e dobra", "razão constante", "viaturas e litros"]},
        {"label": "Inversa", "items": ["dobra e cai à metade", "produto constante", "agentes e dias"]},
        {"label": "Divisão", "items": ["some os números", "ache a constante", "inversa: inversos"]},
    ],
    "right": [
        {"label": "Regra de três", "items": ["simples ou composta", "compare com a pedida", "inverta as inversas"]},
        {"label": "Fator", "items": ["+p%: 1 + p/100", "-p%: 1 - p/100", "multiplique"]},
        {"label": "Variação", "items": ["final menos inicial", "sobre o inicial", "80 a 100: 25%"]},
        {"label": "Sucessivas", "items": ["multiplicam", "10 e 20: 32%", "não somam"]},
        {"label": "Volta", "items": ["divida pelo fator", "+25% volta com -20%", "-20% volta com +25%"]},
    ],
}

QUIZ = quiz([
    ("C", "Se 3/x = 9/12, então x = 4.",
     "9x = 36."),
    ("E", "Em um mapa na escala 1:100.000, 3 cm representam 30 km.",
     "3 × 100.000 cm = 3 km."),
    ("C", "Dividindo-se R$ 1.200 em partes diretamente proporcionais a 1, 2 e 3, a maior parte é R$ 600.",
     "Constante 200; maior 3 × 200."),
    ("C", "Se 3 servidores digitalizam 900 páginas em 5 dias, 5 servidores, no mesmo ritmo, digitalizam 1.500 páginas em 5 dias.",
     "Direta: 900 × 5/3."),
    ("E", "Se 10 agentes fazem uma vistoria em 12 dias, 15 agentes fazem a mesma vistoria em 18 dias.",
     "Inversa: 10 × 12/15 = 8 dias."),
    ("C", "Um aumento de 30% sobre R$ 500 resulta em R$ 650.",
     "500 × 1,3."),
    ("E", "Dois aumentos sucessivos de 10% equivalem a um aumento de 20%.",
     "1,1 × 1,1 = 1,21: 21%."),
    ("C", "Se um valor caiu de 250 para 200, a redução foi de 20%.",
     "50/250 = 0,2."),
    ("E", "Se um preço de R$ 90 já inclui um desconto de 25%, o preço original era R$ 112,50.",
     "90/0,75 = 120."),
    ("C", "Para desfazer um desconto de 20%, é preciso um aumento de 25%.",
     "1/0,8 = 1,25."),
], 10)

SOURCES = [
    "Matemática básica.",
    SRC_R,
]
