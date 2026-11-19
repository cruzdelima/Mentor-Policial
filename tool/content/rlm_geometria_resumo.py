# -*- coding: utf-8 -*-
"""Raciocínio Lógico · Geometria plana e espacial — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "rlm-geometria-01", "RLM", "RLM-14", "resumo", "Geometria plana e espacial", "Raciocínio Lógico e Matemática · Geometria",
    "raciocinio_geometria", "RaciocinioLogico_Geometria_RESUMO.pdf", None, ["Geometria plana", "e espacial"], RES_SUB,
    RES_ITEMS("triângulos, polígonos, áreas e volumes"),
    "Tópico do edital: Geometria plana e espacial — Raciocínio Lógico e Matemática",
    "Base: geometria euclidiana.", 25)

THEORY = [
    exam("O que a banca cobra",
         "**Pitágoras**, **semelhança**, **áreas** e **volumes** em situações práticas, com atenção às **unidades**."),
    h2("1. Triângulos"),
    bl("Soma dos ângulos: **180°**.",
       "Pitágoras: **a² = b² + c²** (3, 4, 5; 6, 8, 10; 5, 12, 13).",
       "Semelhança: lados proporcionais (sombras)."),
    h2("2. Polígonos e áreas"),
    bl("Soma dos internos: **(n − 2) · 180°**. Diagonais: **n(n − 3)/2**.",
       "Triângulo: b · h/2. Trapézio: (B + b) · h/2. Losango: D · d/2.",
       "Círculo: **πr²**; circunferência: **2πr**."),
    h2("3. Volumes"),
    bl("Prisma e cilindro: **base × altura**. Cilindro: πr²h.",
       "Pirâmide e cone: **um terço** de base × altura.",
       "Esfera: (4/3)πr³.",
       "**1 m³ = 1.000 L**; 1 dm³ = 1 L."),
]

SUMMARY = [
    h2("Quadro rápido"),
    tb(["Figura", "Fórmula"], [0.4, 0.6], [
        ("Retângulo", "b · h"),
        ("Triângulo", "b · h / 2"),
        ("Trapézio", "(B + b) · h / 2"),
        ("Círculo", "π r² (comprimento 2π r)"),
        ("Cubo", "a³ (diagonal a√3)"),
        ("Cilindro", "π r² h"),
        ("Cone e pirâmide", "Ab · h / 3"),
        ("Esfera", "(4/3) π r³"),
    ]),
    h2("Leve para a prova"),
    bl("Hipotenusa: oposta ao **ângulo reto**.",
       "Lados × k: área × **k²**, volume × **k³**.",
       "1 m³ = **1.000 L**.",
       "Perímetro ≠ área.",
       "Cone = **1/3** do cilindro."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "GEOMETRIA", "rootSub": "plana e espacial",
    "left": [
        {"label": "Ângulos", "items": ["complementares: 90", "suplementares: 180", "opostos: iguais"]},
        {"label": "Triângulo", "items": ["soma 180 graus", "equilátero: 60", "isósceles, escaleno"]},
        {"label": "Pitágoras", "items": ["hipotenusa ao quadrado", "soma dos catetos", "3, 4, 5"]},
        {"label": "Semelhança", "items": ["mesmos ângulos", "lados proporcionais", "sombras"]},
        {"label": "Polígonos", "items": ["(n - 2) x 180", "diagonais n(n - 3)/2", "externos: 360"]},
    ],
    "right": [
        {"label": "Áreas", "items": ["retângulo b x h", "triângulo: metade", "trapézio: média das bases"]},
        {"label": "Círculo", "items": ["área pi r ao quadrado", "comprimento 2 pi r", "dobrar r: área x 4"]},
        {"label": "Prismas", "items": ["base x altura", "cubo: aresta ao cubo", "paralelepípedo"]},
        {"label": "Pontudos", "items": ["cone e pirâmide", "um terço", "da base x altura"]},
        {"label": "Unidades", "items": ["1 m3 = 1.000 L", "1 dm3 = 1 L", "converta antes"]},
    ],
}

QUIZ = quiz([
    ("C", "Um triângulo retângulo de catetos 6 e 8 tem hipotenusa 10.",
     "√(36 + 64)."),
    ("E", "Se dois ângulos de um triângulo medem 50° e 60°, o terceiro mede 80°.",
     "180 − 110 = 70°."),
    ("C", "A área de um triângulo de base 12 e altura 5 é 30.",
     "12 × 5/2."),
    ("C", "Um polígono de 20 lados tem 170 diagonais.",
     "20 × 17/2."),
    ("E", "O comprimento de uma circunferência de raio 5, com π = 3,14, é 78,5.",
     "2πr = 31,4. O valor 78,5 é a área do círculo."),
    ("C", "Um cubo de aresta 4 tem área total de 96.",
     "6 × 16."),
    ("C", "Uma piscina de 10 m por 3 m com 3 m de profundidade contém, cheia, 90.000 L.",
     "90 m³ = 90.000 L."),
    ("E", "Uma pirâmide de base quadrada de lado 3 e altura 4 tem volume 36.",
     "Ab · h/3 = 9 × 4/3 = 12."),
    ("C", "Triplicando-se a aresta de um cubo, o volume fica multiplicado por 27.",
     "3³ = 27."),
    ("E", "Os ângulos internos de um quadrilátero somam 180°.",
     "(4 − 2) × 180° = 360°."),
], 10)

SOURCES = [
    "Geometria euclidiana.",
    SRC_R,
]
