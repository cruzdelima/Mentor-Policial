# -*- coding: utf-8 -*-
"""Raciocínio Lógico · Equivalências lógicas e Leis de De Morgan — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "rlm-equivalencias-01", "RLM", "RLM-03", "resumo", "Equivalências lógicas e Leis de De Morgan", "Raciocínio Lógico e Matemática · Lógica proposicional",
    "raciocinio_equivalencias", "RaciocinioLogico_Equivalencias_RESUMO.pdf", None, ["Equivalências", "lógicas"], RES_SUB,
    RES_ITEMS("condicional, bicondicional, De Morgan e propriedades"),
    "Tópico do edital: Equivalências lógicas e Leis de De Morgan — Raciocínio Lógico",
    "Base: lógica proposicional clássica.", 25)

THEORY = [
    exam("O que a banca cobra",
         "Frases que “**equivalem**” a outras: contrapositiva, troca pelo **ou**, De Morgan e as pegadinhas da **recíproca** e da **inversa**."),
    h2("1. Equivalência"),
    bl("Mesma tabela-verdade em **todas** as linhas.",
       "Uma linha diferente basta para **não** ser equivalente."),
    h2("2. Condicional"),
    bl("**P → Q ⇔ ¬Q → ¬P** (contrapositiva: inverte e nega).",
       "**P → Q ⇔ ¬P ∨ Q** (NEYMAR: nega a 1ª, mantém a 2ª, troca por ou).",
       "**P ∨ Q ⇔ ¬P → Q**.",
       "**Não** equivalem: recíproca **Q → P** e inversa **¬P → ¬Q**."),
    h2("3. De Morgan"),
    bl("**¬(P ∧ Q) ⇔ ¬P ∨ ¬Q**.",
       "**¬(P ∨ Q) ⇔ ¬P ∧ ¬Q** (= nem P nem Q).",
       "Nega as duas e **troca** o conectivo."),
    h2("4. Bicondicional e propriedades"),
    bl("**P ↔ Q ⇔ (P → Q) ∧ (Q → P) ⇔ ¬P ↔ ¬Q**.",
       "Distributiva: P ∧ (Q ∨ R) ⇔ (P ∧ Q) ∨ (P ∧ R).",
       "Absorção: P ∧ (P ∨ Q) ⇔ P; P ∨ (P ∧ Q) ⇔ P.",
       "(P ∧ Q) → R ⇔ P → (Q → R)."),
]

SUMMARY = [
    h2("Quadro rápido"),
    tb(["Proposição", "Equivale a", "Não equivale a"], [0.24, 0.42, 0.34], [
        ("P → Q", "¬Q → ¬P · ¬P ∨ Q", "Q → P · ¬P → ¬Q"),
        ("P ∨ Q", "¬P → Q · ¬Q → P", "P ∧ Q"),
        ("¬(P ∧ Q)", "¬P ∨ ¬Q", "¬P ∧ ¬Q"),
        ("¬(P ∨ Q)", "¬P ∧ ¬Q", "¬P ∨ ¬Q"),
        ("P ↔ Q", "(P → Q) ∧ (Q → P)", "P ⊻ Q"),
        ("P ⊻ Q", "¬(P ↔ Q) · P ↔ ¬Q", "P ↔ Q"),
    ]),
    h2("Leve para a prova"),
    bl("Contrapositiva: **inverte e nega**.",
       "NEYMAR: **nega, mantém, ou**.",
       "Recíproca e inversa **não** equivalem.",
       "De Morgan: **nega tudo e troca** e/ou.",
       "Nem P nem Q = **¬P ∧ ¬Q**.",
       "Teste com **P = V e Q = F**."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "EQUIVALÊNCIAS", "rootSub": "mesma tabela-verdade",
    "left": [
        {"label": "Contrapositiva", "items": ["inverte e nega", "não Q então não P", "sempre equivale"]},
        {"label": "Troca pelo ou", "items": ["nega a primeira", "mantém a segunda", "se então vira ou"]},
        {"label": "Ou para se", "items": ["P ou Q", "se não P, então Q", "caminho inverso"]},
        {"label": "Não equivale", "items": ["recíproca", "inversa", "pegadinha favorita"]},
        {"label": "Teste", "items": ["uma linha diferente", "derruba", "use P = V, Q = F"]},
    ],
    "right": [
        {"label": "De Morgan e", "items": ["não (P e Q)", "não P ou não Q", "troca o conectivo"]},
        {"label": "De Morgan ou", "items": ["não (P ou Q)", "não P e não Q", "nem P nem Q"]},
        {"label": "Bicondicional", "items": ["ida e volta", "não P sse não Q", "negação: ou exclusivo"]},
        {"label": "Distributiva", "items": ["e sobre ou", "ou sobre e", "como na álgebra"]},
        {"label": "Absorção", "items": ["P e (P ou Q) = P", "P ou (P e Q) = P", "dupla negação"]},
    ],
}

QUIZ = quiz([
    ("C", "A proposição “Se o perito chegou, a cena foi isolada” equivale a “Se a cena não foi isolada, o perito não chegou”.",
     "Contrapositiva."),
    ("E", "A proposição “Se o perito chegou, a cena foi isolada” equivale a “Se a cena foi isolada, o perito chegou”.",
     "É a recíproca."),
    ("C", "A proposição ¬P → Q é equivalente a P ∨ Q.",
     "¬P → Q ⇔ ¬¬P ∨ Q ⇔ P ∨ Q."),
    ("E", "A proposição “Não é verdade que Lúcia é agente ou escrivã” equivale a “Lúcia não é agente ou não é escrivã”.",
     "¬(A ∨ E) ⇔ ¬A ∧ ¬E: “não é agente e não é escrivã”."),
    ("C", "A proposição ¬(P ∧ Q) é equivalente a P → ¬Q.",
     "P → ¬Q ⇔ ¬P ∨ ¬Q ⇔ ¬(P ∧ Q)."),
    ("C", "A proposição P ↔ Q é equivalente a ¬P ↔ ¬Q.",
     "Negar os dois lados da bicondicional preserva os valores iguais ou diferentes."),
    ("E", "A proposição P → Q é equivalente a P ∧ ¬Q.",
     "P ∧ ¬Q é a negação de P → Q."),
    ("C", "A proposição P ∨ (P ∧ Q) é equivalente a P.",
     "Absorção."),
    ("E", "A proposição P ∧ (Q ∨ R) é equivalente a (P ∧ Q) ∨ R.",
     "Pela distributiva, equivale a (P ∧ Q) ∨ (P ∧ R). Com P = F e R = V, diferem."),
    ("C", "A proposição “Nem o delegado nem o agente estavam armados” equivale a “Não é verdade que o delegado ou o agente estava armado”.",
     "¬D ∧ ¬A ⇔ ¬(D ∨ A)."),
], 10)

SOURCES = [
    "Lógica proposicional clássica.",
    SRC_R,
]
