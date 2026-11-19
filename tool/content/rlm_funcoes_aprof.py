# -*- coding: utf-8 -*-
"""Raciocínio Lógico · Funções: afim, quadrática, exponencial e logarítmica — MATERIAL APROFUNDADO."""
from common import *

MATERIAL = material(
    "rlm-funcoes-02", "RLM", "RLM-13", "aprofundado", "Funções: afim, quadrática, exponencial e logarítmica", "Raciocínio Lógico e Matemática · Funções",
    "raciocinio_funcoes_aprofundado", "RaciocinioLogico_Funcoes_APROFUNDADO.pdf", None, ["Funções"],
    ["Função afim, quadrática (vértice, máximo e mínimo), exponencial e logarítmica,", "com aplicações e 20 questões no estilo Cebraspe."],
    [("01", "Conceito", "domínio, imagem e gráfico"),
     ("02", "Afim", "taxa de variação e zero"),
     ("03", "Quadrática", "raízes, vértice, máximo e mínimo"),
     ("04", "Exponencial e log", "crescimento e propriedades"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Funções: afim, quadrática, exponencial e logarítmica — Raciocínio Lógico e Matemática",
    "Base: matemática do ensino médio.", 90)

THEORY = [
    exam("Como estudar este material",
         "Funções aparecem em provas da PRF, das PMs e dos Bombeiros, quase sempre em **situações aplicadas**: custo de um serviço, "
         "trajetória de um projétil, crescimento de uma população, decaimento de uma substância. Para cada tipo de função, saiba "
         "**a lei**, **o formato do gráfico** e **a conta mais cobrada**."),

    h2("1. Conceito de função"),
    bl("Uma **função** f: A → B associa a **cada** elemento x de A **um único** y = f(x) de B.",
       "**Domínio**: os valores de x permitidos. **Imagem**: os valores que f(x) efetivamente assume.",
       "No gráfico, uma reta vertical corta o gráfico de uma função em **no máximo um** ponto."),

    h2("2. Função afim: f(x) = ax + b"),
    tb(["Elemento", "Significado", "Exemplo: f(x) = 2x + 3"], [0.2, 0.44, 0.36], [
        ("**a**", "taxa de variação (inclinação): quanto y muda quando x aumenta 1", "y sobe 2 a cada 1 de x"),
        ("**b**", "valor inicial: onde a reta corta o eixo y (x = 0)", "f(0) = 3"),
        ("Zero (raiz)", "x tal que f(x) = 0: x = −b/a", "x = −3/2"),
        ("Crescimento", "a > 0 crescente; a < 0 decrescente; a = 0 constante", "crescente"),
    ]),
    bl("Reta pelos pontos (1, 5) e (3, 11): a = (11 − 5)/(3 − 1) = **3**; b = 5 − 3 = **2**. Lei: f(x) = 3x + 2.",
       "Aplicação: uma corrida custa **R$ 5,00 fixos + R$ 2,50 por km**. C(x) = 2,5x + 5; 12 km custam **R$ 35,00**.",
       "Se b = 0, a função é **linear** e x e y são **diretamente proporcionais**."),

    h2("3. Função quadrática: f(x) = ax² + bx + c"),
    bl("Gráfico: **parábola**. **a > 0**: concavidade para **cima** (tem **mínimo**). **a < 0**: para **baixo** (tem **máximo**).",
       "**Raízes**: Bhaskara; **Δ** decide quantas são (Δ > 0 duas, Δ = 0 uma, Δ < 0 nenhuma real).",
       "**c** é onde a parábola corta o eixo y."),
    key("Vértice",
        "**xᵥ = −b/2a** e **yᵥ = −Δ/4a** (ou calcule f(xᵥ)). O yᵥ é o **valor máximo ou mínimo** da função; o xᵥ é **onde** ele ocorre. "
        "O vértice fica no meio das raízes: xᵥ = (x₁ + x₂)/2."),
    tb(["Situação", "Função", "Resposta"], [0.36, 0.34, 0.3], [
        ("Mínimo de f(x) = x² − 6x + 5", "raízes 1 e 5; xᵥ = 3", "mínimo **−4** em x = 3"),
        ("Lucro L(x) = −x² + 40x − 300", "xᵥ = −40/(−2) = 20", "lucro máximo **100** com x = 20"),
        ("Altura h(t) = −5t² + 20t (metros, segundos)", "tᵥ = −20/(−10) = 2", "altura máxima **20 m** em t = 2 s"),
    ]),

    h2("4. Função exponencial"),
    bl("Lei: **f(x) = a · bˣ**, com b > 0 e b ≠ 1.",
       "Base **b > 1**: crescente (crescimento exponencial). **0 < b < 1**: decrescente (decaimento).",
       "O gráfico nunca toca o eixo x: **bˣ > 0** sempre.",
       "Uma bactéria que **dobra a cada 3 horas**: N(t) = N₀ · 2^(t/3). Com 1.000 iniciais, após 9 h: 1.000 × 2³ = **8.000**.",
       "Equações exponenciais: iguale as bases. 2ˣ = 32 = 2⁵ → **x = 5**. 3^(x − 1) = 81 = 3⁴ → **x = 5**."),

    h2("5. Logaritmo e função logarítmica"),
    key("Definição",
        "O **logaritmo de a na base b** é o número x tal que **bˣ = a** (com a > 0, b > 0 e b ≠ 1). O logaritmo é o **expoente**. log₂ 8 = 3 porque 2³ = 8. Sem base escrita, "
        "a base é **10**: log 1.000 = 3."),
    tb(["Propriedade", "Fórmula"], [0.36, 0.64], [
        ("Produto", "log (a · b) = log a + log b"),
        ("Quociente", "log (a/b) = log a − log b"),
        ("Potência", "log aⁿ = n · log a"),
        ("Mudança de base", "logaritmo de a na base b = log a / log b (ex.: log₂ 10 = 1/log 2)"),
        ("Casos especiais", "em qualquer base b: log 1 = 0 e log b = 1"),
    ]),
    bl("Com **log 2 ≈ 0,301** e **log 3 ≈ 0,477**: log 8 = 3 × 0,301 = **0,903**; log 6 = 0,301 + 0,477 = **0,778**; "
       "log 5 = log (10/2) = 1 − 0,301 = **0,699**; log 20 = 1 + 0,301 = **1,301**.",
       "A função logarítmica f(x) = logaritmo de x na base b é a **inversa** da exponencial: só existe para **x > 0**.",
       "Aplicação: “em quanto tempo uma população que cresce 2% ao ano dobra?” → 1,02ᵗ = 2 → t = log 2 / log 1,02 (cerca de 35 anos)."),

    h2("6. Como o Cebraspe cobra"),
    bl("Uma situação (custo, trajetória, crescimento) descrita por uma função e itens sobre valores, máximo ou mínimo e tempo.",
       "Máximo e mínimo da quadrática: **vértice**, nunca as raízes.",
       "Logaritmos com valores dados (log 2, log 3): decomponha os números.",
       "Na dúvida real, **deixe em branco**: no Cebraspe, cada erro anula um acerto."),
]

QUIZ = quiz([
    ("C", "Se f(x) = 2x + 3, então f(5) = 13.",
     "2 × 5 + 3."),
    ("E", "O zero da função f(x) = 2x + 3 é x = 3/2.",
     "2x + 3 = 0 → x = −3/2."),
    ("C", "A função afim cujo gráfico passa pelos pontos (1, 5) e (3, 11) é f(x) = 3x + 2.",
     "a = 6/2 = 3; b = 5 − 3 = 2."),
    ("C", "A função f(x) = −4x + 10 é decrescente.",
     "a < 0."),
    ("E", "A parábola de f(x) = −x² + 4x tem concavidade voltada para cima.",
     "a = −1 < 0: concavidade para baixo."),
    ("C", "O valor mínimo da função f(x) = x² − 6x + 5 é −4.",
     "xᵥ = 3; f(3) = 9 − 18 + 5 = −4."),
    ("E", "A função f(x) = x² + 1 tem duas raízes reais.",
     "Δ = −4 < 0: nenhuma raiz real."),
    ("C", "A solução da equação 2ˣ = 32 é x = 5.",
     "32 = 2⁵."),
    ("C", "log₂ 8 = 3.",
     "2³ = 8."),
    ("E", "log (a + b) = log a + log b, para quaisquer a e b positivos.",
     "A propriedade vale para o produto: log (a · b) = log a + log b."),

    ("C", "Uma corrida de táxi custa R$ 5,00 de bandeirada mais R$ 2,50 por quilômetro. Uma corrida de 12 km custa R$ 35,00.",
     "5 + 2,5 × 12 = 35."),
    ("E", "Na situação do item anterior, o custo da corrida é diretamente proporcional à distância percorrida.",
     "Há um valor fixo (b = 5): a função é afim, não linear."),
    ("C", "O lucro de uma empresa é L(x) = −x² + 40x − 300, em que x é o número de unidades vendidas. O lucro máximo é obtido com 20 unidades.",
     "xᵥ = −40/(2 × (−1)) = 20."),
    ("E", "Na situação do item anterior, o lucro máximo é de R$ 400.",
     "L(20) = −400 + 800 − 300 = 100."),
    ("C", "Um projétil lançado verticalmente tem altura h(t) = −5t² + 20t, em metros, com t em segundos. Ele atinge a altura máxima de 20 m.",
     "tᵥ = 2; h(2) = −20 + 40 = 20."),
    ("C", "Uma cultura de bactérias que dobra a cada 3 horas passa de 1.000 para 8.000 bactérias em 9 horas.",
     "1.000 × 2^(9/3) = 1.000 × 2³."),
    ("E", "Considerando log 2 = 0,301, conclui-se que log 8 = 2,408.",
     "log 8 = 3 × 0,301 = 0,903."),
    ("C", "Considerando log 2 = 0,301 e log 3 = 0,477, conclui-se que log 6 = 0,778.",
     "log 6 = log 2 + log 3."),
    ("C", "Considerando log 2 = 0,301, conclui-se que log 5 = 0,699.",
     "log 5 = log 10 − log 2 = 1 − 0,301."),
    ("E", "A função f(x) = 3ˣ assume valores negativos para x < 0.",
     "A exponencial é sempre positiva: para x < 0, assume valores entre 0 e 1."),
], 20)

SOURCES = [
    "Matemática do ensino médio: funções afim, quadrática, exponencial e logarítmica.",
    "Obras de referência: Iezzi e Murakami, Fundamentos de matemática elementar, v. 1 e 2.",
    SRC_A,
]
