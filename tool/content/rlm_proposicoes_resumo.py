# -*- coding: utf-8 -*-
"""Raciocínio Lógico · Proposições e conectivos lógicos — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "rlm-proposicoes-01", "RLM", "RLM-01", "resumo", "Proposições e conectivos lógicos", "Raciocínio Lógico e Matemática · Lógica proposicional",
    "raciocinio_proposicoes", "RaciocinioLogico_Proposicoes_RESUMO.pdf", None, ["Proposições e", "conectivos"], RES_SUB,
    RES_ITEMS("proposição, simples e composta, conectivos"),
    "Tópico do edital: Proposições e conectivos lógicos — Raciocínio Lógico",
    "Base: lógica proposicional clássica.", 25)

THEORY = [
    exam("O que a banca cobra",
         "Reconhecer **proposição**, contar **proposições simples**, traduzir frases para **símbolos** e julgar o **valor lógico** de compostas."),
    h2("1. Proposição"),
    bl("Sentença **declarativa** que pode ser **V ou F** (nunca as duas).",
       "**Não são**: perguntas, exclamações, ordens, desejos, frases sem verbo, **sentenças abertas** (*x > 2*, *Ele é perito*) e paradoxos.",
       "Frase **negativa** ou **falsa** continua sendo proposição."),
    h2("2. Simples e composta"),
    bl("**Simples**: uma afirmação. **Composta**: duas ou mais simples ligadas por conectivos.",
       "Conte as afirmações independentes: *Se faltar e não justificar, será punido* tem **3**.",
       "O “e” de relação (*Ana e Pedro são irmãos*) não separa proposições."),
    h2("3. Conectivos"),
    tb(["Conectivo", "Símbolo", "Quando é verdadeira"], [0.3, 0.16, 0.54], [
        ("Negação (não)", "¬P", "Inverte o valor de P"),
        ("Conjunção (e)", "P ∧ Q", "Só se **as duas** forem V"),
        ("Disjunção (ou)", "P ∨ Q", "Se **ao menos uma** for V"),
        ("Disjunção exclusiva (ou... ou)", "P ⊻ Q", "Se os valores forem **diferentes**"),
        ("Condicional (se... então)", "P → Q", "Sempre, **exceto V → F**"),
        ("Bicondicional (se e somente se)", "P ↔ Q", "Se os valores forem **iguais**"),
    ]),
    h2("4. Redações da condicional"),
    bl("*Se P, então Q* = *Quando P, Q* = *Q, se P* = *P implica Q* = *P somente se Q* = *Todo P é Q*.",
       "**P** é **condição suficiente** para Q; **Q** é **condição necessária** para P.",
       "*Mas*, *porém*, *embora* = conjunção. *Nem P nem Q* = ¬P ∧ ¬Q."),
]

SUMMARY = [
    h2("Quadro rápido"),
    tb(["P", "Q", "P ∧ Q", "P ∨ Q", "P → Q", "P ↔ Q"], [0.1, 0.1, 0.2, 0.2, 0.2, 0.2], [
        ("V", "V", "V", "V", "V", "V"),
        ("V", "F", "F", "V", "**F**", "F"),
        ("F", "V", "F", "V", "V", "F"),
        ("F", "F", "F", "F", "V", "V"),
    ]),
    h2("Leve para a prova"),
    bl("Proposição: declarativa + **V ou F**.",
       "Sentença aberta **não** é proposição.",
       "Conjunção: **uma F derruba**.",
       "Disjunção: **uma V salva**.",
       "Condicional: só **V → F** é falsa (Vera Fischer).",
       "Bicondicional: **iguais** dão V.",
       "Ou... ou: **diferentes** dão V.",
       "*Somente se* aponta o **consequente**.",
       "Suficiente = antecedente; necessária = consequente.",
       "n proposições simples: **2ⁿ linhas**."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "PROPOSIÇÕES", "rootSub": "e conectivos",
    "left": [
        {"label": "É proposição", "items": ["declarativa", "pode ser V ou F", "negativa também"]},
        {"label": "Não é", "items": ["pergunta e ordem", "exclamação, desejo", "sentença aberta"]},
        {"label": "Simples", "items": ["uma afirmação", "letras P, Q, R", "valor V ou F"]},
        {"label": "Composta", "items": ["duas ou mais", "ligadas por conectivo", "conte as simples"]},
        {"label": "Princípios", "items": ["identidade", "não contradição", "terceiro excluído"]},
    ],
    "right": [
        {"label": "E (conjunção)", "items": ["só V se ambas V", "uma F derruba", "mas, porém, embora"]},
        {"label": "Ou (disjunção)", "items": ["só F se ambas F", "uma V salva", "inclusiva"]},
        {"label": "Ou... ou", "items": ["exclusiva", "V se diferentes", "não ambas"]},
        {"label": "Se... então", "items": ["só F em V e F", "suficiente: antes", "necessária: depois"]},
        {"label": "Se e somente se", "items": ["bicondicional", "V se iguais", "necessária e suficiente"]},
    ],
}

QUIZ = quiz([
    ("C", "A frase “Os peritos chegaram ao local às 10 horas” é uma proposição.",
     "Declarativa, pode ser V ou F."),
    ("E", "A frase “Quantos mandados foram cumpridos?” é uma proposição.",
     "Pergunta não é proposição."),
    ("E", "A sentença “Ela é a autora do crime” é uma proposição, pois tem sujeito e predicado.",
     "É sentença aberta: depende de quem é “ela”."),
    ("C", "Se P é verdadeira e Q é verdadeira, então P → Q é verdadeira.",
     "V → V é verdadeira."),
    ("E", "Se P é verdadeira e Q é falsa, então P ∨ Q é falsa.",
     "Basta uma verdadeira para a disjunção ser verdadeira."),
    ("C", "A proposição “Nem o agente nem o escrivão compareceram” pode ser representada por ¬A ∧ ¬E.",
     "“Nem... nem” é a conjunção de duas negações."),
    ("C", "Na proposição “Se houver flagrante, haverá prisão”, a ocorrência do flagrante é condição suficiente para a prisão.",
     "O antecedente é condição suficiente."),
    ("E", "A proposição “Se o relatório estiver pronto e o delegado assinar, o inquérito será remetido” contém duas proposições simples.",
     "Contém três: relatório pronto; delegado assina; inquérito remetido."),
    ("C", "Se P e Q têm valores lógicos diferentes, a bicondicional P ↔ Q é falsa.",
     "A bicondicional exige valores iguais."),
    ("E", "A proposição “Ana é perita, mas Bruno é delegado” é uma disjunção.",
     "“Mas” tem valor de conjunção."),
], 10)

SOURCES = [
    "Lógica proposicional clássica.",
    SRC_R,
]
