# -*- coding: utf-8 -*-
"""Raciocínio Lógico · Quantificadores e diagramas lógicos — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "rlm-quantificadores-01", "RLM", "RLM-06", "resumo", "Quantificadores e diagramas lógicos", "Raciocínio Lógico e Matemática · Lógica de primeira ordem",
    "raciocinio_quantificadores", "RaciocinioLogico_Quantificadores_RESUMO.pdf", None, ["Quantificadores", "e diagramas"], RES_SUB,
    RES_ITEMS("todo, algum, nenhum e diagramas"),
    "Tópico do edital: Quantificadores e diagramas lógicos — Raciocínio Lógico",
    "Base: lógica de primeira ordem e silogística.", 20)

THEORY = [
    exam("O que a banca cobra",
         "Premissas com **todo**, **algum** e **nenhum** e uma conclusão para julgar: **desenhe** e procure o contraexemplo."),
    h2("1. Categóricas"),
    bl("**Todo A é B**: A dentro de B. Não inverte.",
       "**Nenhum A é B**: sem interseção. Inverte.",
       "**Algum A é B**: pelo menos um na interseção. Inverte.",
       "**Algum A não é B**: pelo menos um de A fora de B. Não inverte."),
    h2("2. Diagramas"),
    bl("Desenhe primeiro **todo** e **nenhum**; depois **algum**.",
       "Se houver mais de um desenho possível, a conclusão precisa valer em **todos**.",
       "Achou um desenho com premissas V e conclusão F: **não decorre**."),
    h2("3. Negação e equivalências"),
    bl("Todo ↔ algum **não**; algum ↔ **nenhum**.",
       "“Nem todo” = algum não.",
       "Todo A é B = se é A, é B = quem não é B não é A."),
]

SUMMARY = [
    h2("Quadro rápido"),
    tb(["Premissas", "Conclusão", "Decorre?"], [0.5, 0.3, 0.2], [
        ("Todo A é B; nenhum B é C", "Nenhum A é C", "Sim"),
        ("Algum A é B; todo B é C", "Algum A é C", "Sim"),
        ("Todo A é B; algum B é C", "Algum A é C", "Não"),
        ("Todo A é B; todo C é B", "Algum A é C", "Não"),
        ("Nenhum A é B; algum C é B", "Algum C não é A", "Sim"),
        ("Todo A é B; x não é B", "x não é A", "Sim"),
        ("Todo A é B; x é B", "x é A", "Não"),
    ]),
    h2("Leve para a prova"),
    bl("Algum = **pelo menos um**.",
       "Todo **não inverte**.",
       "Nenhum e algum **invertem**.",
       "Desenhe e busque o **contraexemplo**.",
       "Todo ↔ algum não.",
       "Algum ↔ nenhum."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "QUANTIFICADORES", "rootSub": "e diagramas",
    "left": [
        {"label": "Todo", "items": ["A dentro de B", "não inverte", "nega: algum não"]},
        {"label": "Nenhum", "items": ["sem interseção", "inverte", "nega: algum"]},
        {"label": "Algum", "items": ["pelo menos um", "inverte", "nega: nenhum"]},
        {"label": "Algum não", "items": ["um de A fora de B", "não inverte", "nega: todo"]},
        {"label": "Símbolos", "items": ["universal: todo", "existencial: existe", "fecha a sentença"]},
    ],
    "right": [
        {"label": "Método", "items": ["universais primeiro", "depois o algum", "busque contraexemplo"]},
        {"label": "Decorre", "items": ["todo e nenhum", "algum e todo", "fora de B, fora de A"]},
        {"label": "Não decorre", "items": ["todo e algum", "dois todos para B", "dois alguns"]},
        {"label": "Equivalências", "items": ["todo = se então", "contrapositiva", "nem todo = algum não"]},
        {"label": "Armadilha", "items": ["algum não diz", "que algum não é", "pode ser todos"]},
    ],
}

QUIZ = quiz([
    ("C", "“Nenhum policial é corrupto” equivale a “Nenhum corrupto é policial”.",
     "A universal negativa inverte."),
    ("E", "“Todo agente é servidor” equivale a “Todo servidor é agente”.",
     "A universal afirmativa não inverte."),
    ("C", "Das premissas “Todo agente é servidor” e “Nenhum servidor é empresário”, conclui-se que nenhum agente é empresário.",
     "Os agentes estão dentro dos servidores."),
    ("E", "Das premissas “Todo agente é servidor” e “Algum servidor é professor”, conclui-se que algum agente é professor.",
     "O servidor professor pode não ser agente."),
    ("C", "Das premissas “Algum perito é químico” e “Todo químico é cientista”, conclui-se que algum perito é cientista.",
     "O perito químico está dentro dos cientistas."),
    ("E", "A negação de “Algum candidato faltou” é “Algum candidato não faltou”.",
     "É “Nenhum candidato faltou”."),
    ("C", "“Nem todo suspeito é culpado” equivale a “Existe suspeito que não é culpado”.",
     "Nega o “todo”."),
    ("E", "De “Algum servidor é estável” conclui-se que algum servidor não é estável.",
     "Pode ser que todos sejam estáveis."),
    ("C", "Das premissas “Todo delegado é bacharel” e “Caio não é bacharel”, conclui-se que Caio não é delegado.",
     "Quem está fora de B está fora de A."),
    ("E", "Das premissas “Todo delegado é bacharel” e “Caio é bacharel”, conclui-se que Caio é delegado.",
     "Caio pode ser bacharel sem ser delegado."),
], 10)

SOURCES = [
    "Lógica de primeira ordem e silogística.",
    SRC_R,
]
