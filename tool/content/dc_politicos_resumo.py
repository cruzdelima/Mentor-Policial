# -*- coding: utf-8 -*-
"""Direito Constitucional · Direitos políticos e partidos (arts. 14 a 17) — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "dc-politicos-01", "DC", "DC-06", "resumo", "Direitos políticos e partidos (arts. 14 a 17)", "Direito Constitucional · Direitos fundamentais",
    "constitucional_politicos", "Constitucional_Direitos_Politicos_RESUMO.pdf", None, ["Direitos políticos", "e partidos"], RES_SUB,
    RES_ITEMS("voto, elegibilidade, inelegibilidades e partidos"),
    "Tópico do edital: Direitos políticos e partidos políticos (arts. 14 a 17) — Direito Constitucional",
    "Base: Constituição Federal de 1988 e jurisprudência do STF.", 35)

THEORY = [
    exam("O que a banca cobra",
         "**Idades**, quem vota de forma **obrigatória ou facultativa**, **inelegibilidade reflexa**, militar candidato e o **art. 15**."),
    h2("1. Voto"),
    bl("Sufrágio **universal**; voto **direto, secreto**, igual e periódico (cláusula pétrea; a obrigatoriedade **não** é).",
       "Obrigatório: **18 a 70** anos. Facultativo: **analfabetos**, **maiores de 70**, **16 e 17 anos**.",
       "Inalistáveis: **estrangeiros** e **conscritos** (no serviço obrigatório).",
       "Plebiscito **antes**; referendo **depois**; iniciativa popular: **1%** do eleitorado, **5 Estados**, **0,3%** em cada."),
    h2("2. Elegibilidade"),
    bl("Condições: nacionalidade, pleno gozo dos direitos políticos, alistamento, domicílio, **filiação partidária**, idade.",
       "Idades: **35** (Presidente, Vice, Senador) · **30** (Governador) · **21** (Deputados, Prefeito, juiz de paz) · **18** (Vereador)."),
    h2("3. Inelegibilidades"),
    bl("Absolutas: **inalistáveis** e **analfabetos**.",
       "Chefes do Executivo: **uma reeleição** subsequente; para **outro cargo**, renúncia **6 meses** antes.",
       "**Reflexa**: cônjuge e parentes até **2º grau**, **no território** do titular, salvo **reeleição**; divórcio no mandato não afasta (SV 18).",
       "Militar: **menos de 10 anos** afasta-se; **mais de 10** é agregado e vai para a inatividade na **diplomação**.",
       "Outros casos: **lei complementar** (LC 64/1990, Ficha Limpa).",
       "AIME: **15 dias** da diplomação; abuso econômico, corrupção ou fraude; **segredo de justiça**."),
    h2("4. Art. 15, art. 16 e partidos"),
    bl("**Cassação vedada**. Perda ou suspensão: naturalização cancelada, incapacidade absoluta, **condenação criminal transitada** (enquanto "
       "durarem os efeitos), recusa de obrigação a todos imposta, **improbidade**.",
       "Lei eleitoral: vigora na **publicação**, mas não se aplica a eleição em até **1 ano**.",
       "Partidos: **caráter nacional**, sem dinheiro **estrangeiro**, prestam contas à Justiça Eleitoral, sem organização **paramilitar**.",
       "Sem coligação **proporcional**; **cláusula de desempenho**; infidelidade tira o mandato **só de deputados e vereadores**."),
]

SUMMARY = [
    h2("Quadro rápido"),
    tb(["Item", "Regra"], [0.42, 0.58], [
        ("Presidente, Vice, Senador", "35 anos"),
        ("Governador e Vice", "30 anos"),
        ("Deputados, Prefeito, juiz de paz", "21 anos"),
        ("Vereador", "18 anos"),
        ("Desincompatibilização", "6 meses antes, para outro cargo"),
        ("Inelegibilidade reflexa", "Até 2º grau, no território"),
        ("Militar com menos de 10 anos", "Afasta-se da atividade"),
        ("Militar com mais de 10 anos", "Agregado; inatividade na diplomação"),
        ("AIME", "15 dias da diplomação"),
        ("Anterioridade eleitoral", "1 ano"),
    ]),
    h2("Leve para a prova"),
    bl("Analfabeto **vota**, mas **não é votado**.",
       "Conscrito é **inalistável**.",
       "Senador: **35 anos**.",
       "Reeleição **sem** renúncia.",
       "Parente: só **no território** do titular.",
       "Divórcio no mandato **não** salva (SV 18).",
       "Prefeito itinerante: **vedado**.",
       "Cassação de direitos políticos: **vedada**.",
       "Lei eleitoral: **vigora já**, aplica após **1 ano**.",
       "Infidelidade: **só proporcionais**."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "DIREITOS POLÍTICOS", "rootSub": "arts. 14 a 17",
    "left": [
        {"label": "Voto", "items": ["direto e secreto", "universal, periódico", "obrigatório 18 a 70"]},
        {"label": "Facultativo", "items": ["analfabetos", "maiores de 70", "16 e 17 anos"]},
        {"label": "Inalistáveis", "items": ["estrangeiros", "conscritos", "logo, inelegíveis"]},
        {"label": "Idades", "items": ["35: Presidente, Senador", "30: Governador", "21: Deputado, Prefeito"]},
        {"label": "Democracia direta", "items": ["plebiscito: antes", "referendo: depois", "iniciativa: 1%"]},
    ],
    "right": [
        {"label": "Executivo", "items": ["uma reeleição", "outro cargo: 6 meses", "sem prefeito itinerante"]},
        {"label": "Reflexa", "items": ["cônjuge e 2º grau", "no território", "salvo reeleição"]},
        {"label": "Militar", "items": ["< 10 anos: afasta", "> 10 anos: agregado", "inativo na diplomação"]},
        {"label": "Art. 15", "items": ["cassação vedada", "condenação criminal", "improbidade"]},
        {"label": "Partidos", "items": ["caráter nacional", "sem coligação proporcional", "fidelidade"]},
    ],
}

QUIZ = quiz([
    ("C", "Os estrangeiros não podem alistar-se como eleitores.",
     "Art. 14, § 2º."),
    ("E", "O voto é facultativo para os maiores de sessenta e cinco anos.",
     "É facultativo para os maiores de setenta anos."),
    ("C", "A filiação partidária é condição de elegibilidade.",
     "Art. 14, § 3º, V. Não há candidatura avulsa."),
    ("E", "A idade mínima para o cargo de vereador é de vinte e um anos.",
     "Para vereador, exige-se dezoito anos."),
    ("C", "O cônjuge do governador é inelegível, no território do estado, salvo se já titular de mandato eletivo e candidato à reeleição.",
     "Art. 14, § 7º."),
    ("E", "O militar alistável é inelegível enquanto estiver em serviço ativo.",
     "O militar alistável é elegível, observadas as regras do § 8º."),
    ("C", "A condenação criminal transitada em julgado suspende os direitos políticos enquanto durarem seus efeitos.",
     "Art. 15, III."),
    ("E", "A lei que alterar o processo eleitoral não entrará em vigor antes de um ano de sua publicação.",
     "Vigora na publicação; só não se aplica à eleição que ocorra até um ano de sua vigência."),
    ("C", "É vedada aos partidos políticos a utilização de organização paramilitar.",
     "Art. 17, § 4º."),
    ("E", "Os partidos políticos adquirem personalidade jurídica com o registro de seus estatutos no Tribunal Superior Eleitoral.",
     "Adquirem personalidade na forma da lei civil; o registro no TSE vem depois."),
], 10)

SOURCES = [
    "Constituição da República Federativa do Brasil de 1988, arts. 14 a 17.",
    "Supremo Tribunal Federal: Súmula Vinculante 18; RE 637.485; ADI 5.081.",
    SRC_R,
]
