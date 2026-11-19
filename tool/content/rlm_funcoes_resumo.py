# -*- coding: utf-8 -*-
"""Raciocínio Lógico · Funções: afim, quadrática, exponencial e logarítmica — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "rlm-funcoes-01", "RLM", "RLM-13", "resumo", "Funções: afim, quadrática, exponencial e logarítmica", "Raciocínio Lógico e Matemática · Funções",
    "raciocinio_funcoes", "RaciocinioLogico_Funcoes_RESUMO.pdf", None, ["Funções"], RES_SUB,
    RES_ITEMS("afim, quadrática, exponencial e logaritmo"),
    "Tópico do edital: Funções: afim, quadrática, exponencial e logarítmica — Raciocínio Lógico e Matemática",
    "Base: matemática do ensino médio.", 25)

THEORY = [
    exam("O que a banca cobra",
         "Valores de funções em **situações aplicadas**, **máximo e mínimo** da quadrática e **propriedades** de potências e logaritmos."),
    h2("1. Afim: ax + b"),
    bl("**a**: taxa de variação (a > 0 cresce). **b**: valor inicial.",
       "Zero: **x = −b/a**. Dois pontos: a = Δy/Δx.",
       "b = 0: linear (proporcional)."),
    h2("2. Quadrática: ax² + bx + c"),
    bl("a > 0: **mínimo**; a < 0: **máximo**.",
       "Vértice: **xᵥ = −b/2a**, **yᵥ = −Δ/4a**.",
       "Δ decide as raízes; c corta o eixo y."),
    h2("3. Exponencial e logaritmo"),
    bl("bˣ > 0 sempre; b > 1 cresce, 0 < b < 1 decresce.",
       "Iguale as bases: 2ˣ = 32 → x = 5.",
       "Logaritmo de a na base b: **é o expoente x tal que bˣ = a** (log₂ 8 = 3).",
       "log(ab) = log a + log b; log(a/b) = log a − log b; log aⁿ = n log a."),
]

SUMMARY = [
    h2("Quadro rápido"),
    tb(["Conta", "Resultado"], [0.6, 0.4], [
        ("f(x) = 2x + 3; f(5)", "13"),
        ("Zero de 2x + 3", "−3/2"),
        ("Mínimo de x² − 6x + 5", "−4 (em x = 3)"),
        ("Máximo de −5t² + 20t", "20 (em t = 2)"),
        ("2ˣ = 32", "x = 5"),
        ("log 8 (log 2 = 0,301)", "0,903"),
        ("log 5", "0,699"),
        ("log 6 (log 3 = 0,477)", "0,778"),
    ]),
    h2("Leve para a prova"),
    bl("Afim: **a** inclina, **b** começa.",
       "Máximo/mínimo: **vértice**.",
       "a < 0: boca para baixo, **máximo**.",
       "Exponencial nunca é negativa.",
       "Log é **expoente**.",
       "log (a + b) ≠ log a + log b."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "FUNÇÕES", "rootSub": "afim, quadrática, exp. e log",
    "left": [
        {"label": "Função", "items": ["cada x", "um único y", "domínio e imagem"]},
        {"label": "Afim", "items": ["a: inclinação", "b: valor inicial", "zero: -b/a"]},
        {"label": "Linear", "items": ["b = 0", "proporcional", "passa na origem"]},
        {"label": "Quadrática", "items": ["parábola", "a > 0: mínimo", "a < 0: máximo"]},
        {"label": "Vértice", "items": ["x = -b/2a", "y = -delta/4a", "meio das raízes"]},
    ],
    "right": [
        {"label": "Exponencial", "items": ["base > 1 cresce", "sempre positiva", "dobra a cada t"]},
        {"label": "Equação exp.", "items": ["iguale as bases", "2 elevado a x = 32", "x = 5"]},
        {"label": "Logaritmo", "items": ["é o expoente", "base 10 padrão", "x > 0"]},
        {"label": "Propriedades", "items": ["produto: soma", "quociente: diferença", "potência: desce"]},
        {"label": "Valores", "items": ["log 2 = 0,301", "log 3 = 0,477", "log 5 = 0,699"]},
    ],
}

QUIZ = quiz([
    ("C", "A função f(x) = 5x − 10 tem zero em x = 2.",
     "5x = 10."),
    ("E", "A função f(x) = 7 − 2x é crescente.",
     "a = −2 < 0: decrescente."),
    ("C", "O vértice da parábola f(x) = x² − 4x + 3 tem abscissa 2.",
     "xᵥ = 4/2."),
    ("E", "A função f(x) = −x² + 6x tem valor mínimo 9.",
     "a < 0: tem máximo, que é f(3) = 9."),
    ("C", "A solução de 3^(x − 1) = 81 é x = 5.",
     "81 = 3⁴ → x − 1 = 4."),
    ("C", "log 1.000 = 3.",
     "10³ = 1.000."),
    ("E", "Considerando log 2 = 0,301, tem-se log 20 = 0,602.",
     "log 20 = log 2 + log 10 = 1,301."),
    ("C", "A função f(x) = (1/2)ˣ é decrescente.",
     "Base entre 0 e 1."),
    ("C", "O logaritmo de 1 é 0 em qualquer base válida.",
     "b⁰ = 1."),
    ("E", "Se f(x) = 3x + 4 representa o custo de um serviço com taxa fixa, a taxa fixa é 3.",
     "A taxa fixa é o termo independente, b = 4."),
], 10)

SOURCES = [
    "Matemática do ensino médio: funções.",
    SRC_R,
]
