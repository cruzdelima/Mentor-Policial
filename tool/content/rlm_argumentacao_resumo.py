# -*- coding: utf-8 -*-
"""Raciocínio Lógico · Lógica de argumentação — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "rlm-argumentacao-01", "RLM", "RLM-05", "resumo", "Lógica de argumentação", "Raciocínio Lógico e Matemática · Lógica proposicional",
    "raciocinio_argumentacao", "RaciocinioLogico_Argumentacao_RESUMO.pdf", None, ["Lógica de", "argumentação"], RES_SUB,
    RES_ITEMS("validade, inferências, falácias e métodos"),
    "Tópico do edital: Lógica de argumentação — Raciocínio Lógico",
    "Base: lógica proposicional clássica.", 25)

THEORY = [
    exam("O que a banca cobra",
         "Se uma conclusão **decorre** das premissas e se o argumento é **válido**, com as falácias como pegadinha."),
    h2("1. Validade"),
    bl("**Válido**: impossível ter premissas **V** e conclusão **F**.",
       "Validade é de **forma**: argumento válido pode ter conclusão falsa (se alguma premissa for falsa).",
       "Válido + premissas verdadeiras = conclusão verdadeira."),
    h2("2. Formas válidas"),
    bl("**Modus ponens**: P → Q; P ⊢ Q.",
       "**Modus tollens**: P → Q; ¬Q ⊢ ¬P.",
       "**Silogismo hipotético**: P → Q; Q → R ⊢ P → R.",
       "**Silogismo disjuntivo**: P ∨ Q; ¬P ⊢ Q.",
       "**Simplificação**: P ∧ Q ⊢ P. **Adição**: P ⊢ P ∨ Q."),
    h2("3. Falácias"),
    bl("**Afirmar o consequente**: P → Q; Q ⊢ P (inválido).",
       "**Negar o antecedente**: P → Q; ¬P ⊢ ¬Q (inválido).",
       "P ∨ Q; P ⊢ ¬Q (inválido no ou inclusivo)."),
    h2("4. Métodos"),
    bl("**Concluir**: premissas V; comece pela simples ou pela conjunção e propague.",
       "**Validar**: conclusão F e tente premissas V; se der, é inválido.",
       "**Verdade e mentira**: suponha e procure contradição."),
]

SUMMARY = [
    h2("Quadro rápido"),
    tb(["Premissas", "Conclusão", "Situação"], [0.4, 0.2, 0.4], [
        ("P → Q; P", "Q", "Válido (modus ponens)"),
        ("P → Q; ¬Q", "¬P", "Válido (modus tollens)"),
        ("P → Q; Q", "P", "Inválido (afirma o consequente)"),
        ("P → Q; ¬P", "¬Q", "Inválido (nega o antecedente)"),
        ("P ∨ Q; ¬P", "Q", "Válido (silogismo disjuntivo)"),
        ("P ∨ Q; P", "¬Q", "Inválido"),
        ("P → Q; Q → R", "P → R", "Válido (silogismo hipotético)"),
    ]),
    h2("Leve para a prova"),
    bl("Válido = **sem caso V, V, F**.",
       "Forma, não conteúdo.",
       "Ponens **afirma** o antecedente.",
       "Tollens **nega** o consequente.",
       "Afirmar o consequente: **falácia**.",
       "Negar o antecedente: **falácia**.",
       "Comece pela **proposição simples**."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "ARGUMENTAÇÃO", "rootSub": "premissas e conclusão",
    "left": [
        {"label": "Válido", "items": ["premissas V", "conclusão nunca F", "questão de forma"]},
        {"label": "Sólido", "items": ["válido", "premissas verdadeiras", "conclusão verdadeira"]},
        {"label": "Modus ponens", "items": ["se P então Q", "P", "logo Q"]},
        {"label": "Modus tollens", "items": ["se P então Q", "não Q", "logo não P"]},
        {"label": "Silogismos", "items": ["hipotético: encadeia", "disjuntivo: elimina", "ou P ou Q, não P"]},
    ],
    "right": [
        {"label": "Falácia 1", "items": ["afirmar o consequente", "se P então Q; Q", "não dá P"]},
        {"label": "Falácia 2", "items": ["negar o antecedente", "se P então Q; não P", "não dá não Q"]},
        {"label": "Método concluir", "items": ["premissas V", "comece pela simples", "propague"]},
        {"label": "Método validar", "items": ["conclusão F", "premissas V?", "se der: inválido"]},
        {"label": "Verdade e mentira", "items": ["suponha um caso", "procure contradição", "falas opostas"]},
    ],
}

QUIZ = quiz([
    ("C", "De “Se houve fraude, a licitação será anulada” e “Houve fraude”, conclui-se que a licitação será anulada.",
     "Modus ponens."),
    ("C", "De “Se houve fraude, a licitação será anulada” e “A licitação não será anulada”, conclui-se que não houve fraude.",
     "Modus tollens."),
    ("E", "De “Se houve fraude, a licitação será anulada” e “A licitação será anulada”, conclui-se que houve fraude.",
     "Afirmação do consequente."),
    ("E", "De “Se houve fraude, a licitação será anulada” e “Não houve fraude”, conclui-se que a licitação não será anulada.",
     "Negação do antecedente."),
    ("C", "De “O mandado foi expedido pela vara criminal ou pela vara federal” e “Não foi pela vara criminal”, conclui-se que foi pela vara federal.",
     "Silogismo disjuntivo."),
    ("C", "Um argumento pode ser válido mesmo que todas as suas premissas sejam falsas.",
     "Validade é de forma."),
    ("E", "Se um argumento tem conclusão verdadeira, então ele é válido.",
     "Um argumento inválido também pode ter conclusão verdadeira."),
    ("C", "O argumento com premissas P → Q e Q → R e conclusão ¬R → ¬P é válido.",
     "Silogismo hipotético dá P → R, cuja contrapositiva é ¬R → ¬P."),
    ("E", "O argumento com premissas P ∨ Q e Q e conclusão ¬P é válido.",
     "No ou inclusivo, P também pode ser verdadeira."),
    ("C", "De “Se Ana viajou, Beto ficou” e “Se Beto ficou, Caio saiu” e “Caio não saiu”, conclui-se que Ana não viajou.",
     "Caio não saiu → Beto não ficou → Ana não viajou."),
], 10)

SOURCES = [
    "Lógica proposicional clássica.",
    SRC_R,
]
