# -*- coding: utf-8 -*-
"""Raciocínio Lógico · Geometria plana e espacial — MATERIAL APROFUNDADO."""
from common import *

MATERIAL = material(
    "rlm-geometria-02", "RLM", "RLM-14", "aprofundado", "Geometria plana e espacial", "Raciocínio Lógico e Matemática · Geometria",
    "raciocinio_geometria_aprofundado", "RaciocinioLogico_Geometria_APROFUNDADO.pdf", None, ["Geometria plana", "e espacial"],
    ["Ângulos, triângulos, Pitágoras, semelhança, polígonos, áreas, círculo e volumes", "de sólidos, com 20 questões no estilo Cebraspe."],
    [("01", "Ângulos e triângulos", "soma 180°, Pitágoras, semelhança"),
     ("02", "Polígonos", "ângulos internos e diagonais"),
     ("03", "Áreas", "figuras planas e círculo"),
     ("04", "Sólidos", "volumes, áreas e conversão em litros"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Geometria plana e espacial — Raciocínio Lógico e Matemática",
    "Base: geometria euclidiana do ensino fundamental e médio.", 85)

THEORY = [
    exam("Como estudar este material",
         "A geometria das provas de PM, Bombeiros, Guardas e Polícia Penal é **aplicada**: escadas apoiadas na parede, sombras, terrenos, "
         "caixas-d’água, tanques e reservatórios. Decore as fórmulas de área e volume e o **teorema de Pitágoras**; o resto é desenhar a "
         "situação e conferir as **unidades**."),

    h2("1. Ângulos e triângulos"),
    bl("Ângulo **reto**: 90°. **Raso**: 180°. Ângulos **complementares** somam 90°; **suplementares**, 180°.",
       "Ângulos **opostos pelo vértice** são iguais.",
       "A soma dos ângulos internos de qualquer triângulo é **180°**.",
       "Classificação pelos lados: **equilátero** (3 iguais, ângulos de 60°), **isósceles** (2 iguais), **escaleno** (todos diferentes)."),
    key("Teorema de Pitágoras",
        "Em um triângulo **retângulo**, **a² = b² + c²**, em que a é a **hipotenusa** (lado oposto ao ângulo reto) e b, c são os catetos. "
        "Ternos comuns: **3, 4, 5** · **6, 8, 10** · **5, 12, 13** · **9, 12, 15**."),
    bl("Uma escada de **5 m** apoiada em uma parede, com o pé a **3 m** da parede, alcança a altura de √(25 − 9) = **4 m**.",
       "Diagonal do quadrado de lado ℓ: **ℓ√2**. Altura do triângulo equilátero de lado ℓ: **ℓ√3/2**."),
    h3("Semelhança"),
    p("Triângulos com os mesmos ângulos são **semelhantes**: os lados correspondentes são **proporcionais**. Exemplo clássico: um poste "
      "faz sombra de 6 m no mesmo instante em que uma pessoa de 1,8 m faz sombra de 1,2 m. Altura do poste: 1,8 × 6/1,2 = **9 m**."),
    nt("Se os lados são multiplicados por k, as **áreas** ficam multiplicadas por **k²** e os **volumes** por **k³**."),

    h2("2. Polígonos"),
    tb(["Grandeza", "Fórmula", "Hexágono (n = 6)"], [0.4, 0.34, 0.26], [
        ("Soma dos ângulos internos", "(n − 2) · 180°", "720°"),
        ("Ângulo interno (polígono regular)", "(n − 2) · 180°/n", "120°"),
        ("Soma dos ângulos externos", "360°", "360°"),
        ("Número de diagonais", "n(n − 3)/2", "9"),
    ]),

    h2("3. Áreas e perímetros"),
    tb(["Figura", "Área", "Exemplo"], [0.24, 0.36, 0.4], [
        ("Retângulo", "base × altura", "8 × 5 = **40** (perímetro 26)"),
        ("Quadrado", "ℓ²", "lado 6: **36**"),
        ("Triângulo", "base × altura / 2", "base 12, altura 5: **30**"),
        ("Paralelogramo", "base × altura", "base 10, altura 4: **40**"),
        ("Trapézio", "(B + b) × h / 2", "bases 10 e 6, altura 4: **32**"),
        ("Losango", "D × d / 2", "diagonais 10 e 7: **35**"),
        ("Círculo", "π · r²", "raio 5 (π = 3,14): **78,5**"),
    ]),
    bl("**Comprimento da circunferência**: **2πr**. Raio 5 (π = 3,14): **31,4**.",
       "Converta antes de calcular: 1 m² = 10.000 cm²; 1 km² = 1.000.000 m²; 1 hectare = 10.000 m²."),

    h2("4. Geometria espacial"),
    tb(["Sólido", "Volume", "Exemplo"], [0.24, 0.32, 0.44], [
        ("Cubo", "a³", "aresta 4: **64** (área total 6a² = 96)"),
        ("Paralelepípedo", "a × b × c", "2 m × 1,5 m × 1 m = **3 m³**"),
        ("Prisma (qualquer)", "área da base × altura", "—"),
        ("Cilindro", "π · r² · h", "r = 2 m, h = 5 m, π = 3: **60 m³**"),
        ("Pirâmide e cone", "área da base × altura / 3", "um terço do prisma ou do cilindro de mesma base e altura"),
        ("Esfera", "(4/3) · π · r³", "r = 3 (π = 3,14): **113,04**"),
    ]),
    key("Volume em litros",
        "**1 m³ = 1.000 L** e **1 dm³ = 1 L**. Uma caixa-d’água de 3 m³ comporta **3.000 litros**. 1 L = 1.000 cm³ = 1.000 mL."),
    bl("Diagonal do cubo de aresta a: **a√3**. Diagonal do paralelepípedo: √(a² + b² + c²).",
       "Área lateral do cilindro: **2πrh**; área total: 2πrh + 2πr²."),

    h2("5. Como o Cebraspe cobra"),
    bl("Situações práticas: terreno, sala, viatura, tanque de combustível, reservatório de água.",
       "Itens que comparam figuras (dobrar o raio quadruplica a área e multiplica o volume por 8).",
       "Unidades misturadas (cm e m, m³ e litros): converta antes de comparar.",
       "Na dúvida real, **deixe em branco**: no Cebraspe, cada erro anula um acerto."),
]

QUIZ = quiz([
    ("C", "Em um triângulo retângulo de catetos 9 e 12, a hipotenusa mede 15.",
     "√(81 + 144) = √225."),
    ("E", "A soma dos ângulos internos de um triângulo é 360°.",
     "É 180°."),
    ("C", "Dois ângulos complementares somam 90°.",
     "Definição."),
    ("C", "A soma dos ângulos internos de um hexágono é 720°.",
     "(6 − 2) × 180°."),
    ("E", "Um hexágono tem 6 diagonais.",
     "6 × 3/2 = 9 diagonais."),
    ("C", "A área de um trapézio de bases 10 e 6 e altura 4 é 32.",
     "(10 + 6) × 4/2."),
    ("E", "A área de um círculo de raio 5, com π = 3,14, é 31,4.",
     "πr² = 78,5. O valor 31,4 é o comprimento da circunferência."),
    ("C", "O volume de um cubo de aresta 4 é 64.",
     "4³."),
    ("C", "Um reservatório com 3 m³ de volume comporta 3.000 litros.",
     "1 m³ = 1.000 L."),
    ("E", "O volume de um cone é igual ao de um cilindro de mesma base e mesma altura.",
     "O cone tem um terço do volume do cilindro."),

    ("C", "Uma escada de 5 m está apoiada em uma parede vertical, com o pé a 3 m da parede. O topo da escada está a 4 m do chão.",
     "Pitágoras: √(25 − 9) = 4."),
    ("C", "Um poste projeta sombra de 6 m no mesmo instante em que uma pessoa de 1,8 m projeta sombra de 1,2 m. O poste mede 9 m.",
     "Semelhança: 1,8/1,2 = h/6."),
    ("E", "Um terreno retangular de 8 m por 5 m tem perímetro de 40 m.",
     "Perímetro: 2 × (8 + 5) = 26 m. A área é 40 m²."),
    ("C", "Um tanque cilíndrico de raio 2 m e altura 5 m, com π = 3, tem volume de 60 m³.",
     "3 × 4 × 5."),
    ("E", "Na situação do item anterior, o tanque comporta 6.000 litros.",
     "60 m³ = 60.000 L."),
    ("C", "Dobrando-se o raio de um círculo, sua área fica multiplicada por 4.",
     "A área é proporcional ao quadrado do raio."),
    ("E", "Dobrando-se a aresta de um cubo, seu volume fica multiplicado por 4.",
     "O volume fica multiplicado por 2³ = 8."),
    ("C", "O ângulo interno de um octógono regular mede 135°.",
     "(8 − 2) × 180°/8."),
    ("C", "Uma caixa-d’água em forma de paralelepípedo com 2 m de comprimento, 1,5 m de largura e 1 m de altura comporta 3.000 L.",
     "2 × 1,5 × 1 = 3 m³."),
    ("E", "A área de um losango de diagonais 10 e 7 é 70.",
     "D × d/2 = 35."),
], 20)

SOURCES = [
    "Geometria euclidiana plana e espacial.",
    "Obras de referência: Dolce e Pompeo, Fundamentos de matemática elementar, v. 9 e 10.",
    SRC_A,
]
