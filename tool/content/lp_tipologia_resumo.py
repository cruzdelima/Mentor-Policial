# -*- coding: utf-8 -*-
"""Língua Portuguesa · Tipologia e gêneros textuais — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "lp-tipologia-01", "LP", "LP-15", "resumo", "Tipologia e gêneros textuais", "Língua Portuguesa · Texto",
    "portugues_tipologia", "Portugues_Tipologia_Generos_RESUMO.pdf", None, ["Tipologia e", "gêneros textuais"], RES_SUB,
    RES_ITEMS("os cinco tipos, suas marcas e os gêneros mais cobrados"),
    "Tópico do edital: Tipologia e gêneros textuais (Língua Portuguesa)",
    "Base: gramáticas de referência e estudos de linguística textual (Marcuschi).", 25)

THEORY = [
    exam("O que a banca cobra",
         "Qual o **tipo predominante** e qual o **gênero** do texto. Decida pela **finalidade** e pelas **marcas linguísticas**, não pelo assunto."),
    h2("1. Tipo × gênero"),
    bl("**Tipo**: poucas sequências (narrar, descrever, expor, argumentar, instruir).",
       "**Gênero**: textos concretos e ilimitados (notícia, BO, edital, ofício, crônica).",
       "Um gênero tem tipo **predominante**, mas mistura outros (heterogeneidade)."),
    h2("2. Os tipos e suas marcas"),
    tb(["Tipo", "Finalidade", "Marcas"], [0.2, 0.28, 0.52], [
        ("Narrativo", "Contar", "Pretérito perfeito, sequência temporal, personagens"),
        ("Descritivo", "Caracterizar", "Adjetivos, verbos de estado, imperfeito"),
        ("Expositivo", "Informar", "Presente, 3ª pessoa, definições e dados"),
        ("Argumentativo", "Convencer", "Tese, argumentos, conclusão, conectores"),
        ("Injuntivo", "Orientar", "Imperativo ou infinitivo, passos"),
    ]),
    h2("3. Gêneros"),
    bl("**Argumentativos**: editorial (do veículo), artigo de opinião (assinado).",
       "**Narrativos**: notícia (com exposição), crônica, boletim de ocorrência.",
       "**Expositivos**: reportagem, relatório, verbete. **Injuntivos**: edital, manual, receita.",
       "**Laudo**: descritivo e expositivo."),
]

SUMMARY = [
    h2("Quadro: como reconhecer"),
    tb(["Pista no texto", "Tipo"], [0.62, 0.38], [
        ("Ações em sequência, marcadores de tempo", "Narrativo"),
        ("Características, sem avanço temporal", "Descritivo"),
        ("Explica sem tomar partido", "Expositivo"),
        ("Defende uma ideia", "Argumentativo"),
        ("Diz o que fazer", "Injuntivo"),
    ]),
    h2("Leve para a prova"),
    bl("Finalidade decide o tipo; o **assunto** não.",
       "Gênero tem tipo **predominante**.",
       "Pretérito **perfeito** = narração; **imperfeito** = descrição.",
       "**Imperativo** = injunção.",
       "**Portanto, logo** = conclusão de argumento.",
       "Editorial = opinião do jornal; artigo = opinião assinada.",
       "Notícia = fato recente, impessoal.",
       "BO = narrativo com descrições.",
       "Edital = regras (injuntivo).",
       "Crônica = cotidiano + reflexão."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "TIPOS E GÊNEROS", "rootSub": "finalidade e marcas",
    "left": [
        {"label": "Tipo × gênero", "items": ["tipo: poucas sequências", "gênero: textos concretos", "heterogeneidade"]},
        {"label": "Narrativo", "items": ["contar fatos", "pretérito perfeito", "tempo e personagens"]},
        {"label": "Descritivo", "items": ["caracterizar", "adjetivos", "pretérito imperfeito"]},
        {"label": "Expositivo", "items": ["informar", "presente, 3ª pessoa", "definições e dados"]},
        {"label": "Argumentativo", "items": ["tese", "argumentos", "conclusão"]},
    ],
    "right": [
        {"label": "Injuntivo", "items": ["orientar", "imperativo", "passos"]},
        {"label": "Jornalísticos", "items": ["notícia: fato", "editorial: opinião", "reportagem: aprofunda"]},
        {"label": "Policiais", "items": ["BO: narrativo", "laudo: descritivo", "relatório: expositivo"]},
        {"label": "Oficiais", "items": ["edital: regras", "ofício: comunicação", "manual: instruções"]},
        {"label": "Atenção", "items": ["assunto não define tipo", "veja a finalidade", "veja os verbos"]},
    ],
}

T = "Após a abordagem, os agentes conduziram o suspeito à delegacia, onde o delegado lavrou o auto de prisão em flagrante."

QUIZ = quiz([
    ("C", "O trecho é predominantemente narrativo.",
     "Relata ações em sequência temporal (conduziram, lavrou).", T),
    ("E", "No trecho, predomina a sequência argumentativa, pois há defesa de uma tese.",
     "Não há tese nem argumentos; há relato de fatos."),
    ("C", "O artigo de opinião é gênero predominantemente argumentativo.",
     "Defende o ponto de vista do autor."),
    ("E", "O manual de instruções é gênero predominantemente narrativo.",
     "Orienta o leitor por passos: é injuntivo."),
    ("C", "No texto descritivo, é comum o emprego do pretérito imperfeito e de adjetivos.",
     "São marcas da caracterização."),
    ("E", "O assunto do texto é o critério decisivo para definir seu tipo textual.",
     "O tipo depende da finalidade e da estrutura, não do tema."),
    ("C", "O laudo pericial combina sequências descritivas e expositivas.",
     "Descreve vestígios e expõe conclusões técnicas."),
    ("E", "O editorial é assinado por um colunista e expressa a opinião pessoal dele.",
     "O editorial expressa a opinião do veículo e, em regra, não é assinado."),
    ("C", "O texto expositivo tem por finalidade informar ou explicar, em linguagem impessoal.",
     "Não busca convencer, e sim transmitir conhecimento."),
    ("E", "Um gênero textual apresenta sempre um único tipo textual, sem mistura de sequências.",
     "Os gêneros costumam combinar sequências de tipos diferentes."),
], 10)

SOURCES = [GRAM, SRC_R]
