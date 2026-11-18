# -*- coding: utf-8 -*-
"""Direito Constitucional · Direitos sociais (arts. 6º a 11) — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "dc-sociais-01", "DC", "DC-04", "resumo", "Direitos sociais (arts. 6º a 11)", "Direito Constitucional · Direitos fundamentais",
    "constitucional_sociais", "Constitucional_Direitos_Sociais_RESUMO.pdf", None, ["Direitos", "sociais"], RES_SUB,
    RES_ITEMS("rol do art. 6º, trabalhadores, sindicato e greve"),
    "Tópico do edital: Direitos sociais (arts. 6º a 11) — Direito Constitucional",
    "Base: Constituição Federal de 1988 e jurisprudência do STF.", 25)

THEORY = [
    exam("O que a banca cobra",
         "O **rol do art. 6º**, os **números do art. 7º** e a **greve** na segurança pública."),
    h2("1. Art. 6º"),
    bl("Educação, saúde, alimentação, trabalho, moradia, transporte, lazer, segurança, previdência, proteção à maternidade e à infância, "
       "assistência aos desamparados.",
       "Fora do rol: **cultura, esporte, meio ambiente, propriedade**.",
       "Renda básica familiar para quem está em **vulnerabilidade** (EC 114/2021).",
       "**Mínimo existencial** prevalece sobre a alegação genérica de **reserva do possível**."),
    h2("2. Art. 7º"),
    bl("Jornada **8h/44h**; turno ininterrupto **6h**; hora extra **+50%**; férias **+1/3**.",
       "Gestante **120 dias**; paternidade pela Lei 15.371/2026 (**10, 15 e 20 dias** em 2027, 2028 e 2029).",
       "Aviso prévio proporcional, **mínimo 30 dias**; creche **até 5 anos**.",
       "Prescrição: **5 anos**, até **2 anos** após o fim do contrato.",
       "Menores: noturno/perigoso/insalubre só após **18**; trabalho a partir de **16**; aprendiz a partir de **14**.",
       "Salário mínimo nacional e **sem vinculação**; irredutível **salvo acordo ou convenção**."),
    h2("3. Sindicato e greve"),
    bl("Sindicato sem **autorização** do Estado (só registro); **unicidade** na base territorial **mínima de um Município**.",
       "Ninguém é obrigado a se filiar; contribuição confederativa só de **filiados** (SV 40).",
       "Dirigente: estabilidade do **registro da candidatura** até **1 ano após o mandato**.",
       "Greve: trabalhadores decidem **oportunidade e interesses**; servidor civil por **lei específica**.",
       "**Militares**: sem greve e sem sindicato (texto da CF). **Policiais civis**: sem greve (STF), mas podem se sindicalizar.",
       "Art. 11: empresa com **mais de 200** empregados elege um representante."),
]

SUMMARY = [
    h2("Quadro rápido"),
    tb(["Item", "Número"], [0.55, 0.45], [
        ("Jornada diária / semanal", "8 h / 44 h"),
        ("Turno ininterrupto", "6 h"),
        ("Hora extra", "mínimo +50%"),
        ("Férias", "+1/3"),
        ("Licença-gestante", "120 dias"),
        ("Aviso prévio", "mínimo 30 dias"),
        ("Creche", "até 5 anos"),
        ("Prescrição", "5 anos / 2 anos"),
        ("Dirigente sindical", "até 1 ano após o mandato"),
        ("Representante na empresa", "mais de 200 empregados"),
    ]),
    h2("Leve para a prova"),
    bl("Art. 6º não tem **cultura** nem **meio ambiente**.",
       "Salário mínimo: **sem vinculação**.",
       "Semana de **44 horas**.",
       "Hora extra **+50%**, férias **+1/3**.",
       "Aprendiz **14**, trabalho **16**, noturno **18**.",
       "Sindicato: **registro**, não autorização.",
       "Unicidade: base **≥ um Município**.",
       "Militar: **sem greve e sem sindicato**.",
       "Policial civil: **sem greve** (STF).",
       "Servidor civil: greve por **lei específica**."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "DIREITOS SOCIAIS", "rootSub": "arts. 6º a 11",
    "left": [
        {"label": "Art. 6º", "items": ["educação, saúde, moradia", "transporte, alimentação", "lazer, segurança"]},
        {"label": "Fora do rol", "items": ["cultura", "esporte", "meio ambiente"]},
        {"label": "Conceitos", "items": ["reserva do possível", "mínimo existencial", "vedação do retrocesso"]},
        {"label": "Jornada", "items": ["8 h e 44 h", "turno: 6 h", "extra: +50%"]},
        {"label": "Licenças", "items": ["gestante: 120 dias", "paternidade: lei 2026", "férias: +1/3"]},
    ],
    "right": [
        {"label": "Menores", "items": ["aprendiz: 14", "trabalho: 16", "noturno: 18"]},
        {"label": "Sindicato", "items": ["sem autorização", "unicidade", "filiação livre"]},
        {"label": "Dirigente", "items": ["desde a candidatura", "até 1 ano após", "salvo falta grave"]},
        {"label": "Greve", "items": ["privado: art. 9º", "servidor: lei específica", "essenciais: lei"]},
        {"label": "Segurança pública", "items": ["militar: CF proíbe", "policial civil: STF", "mediação obrigatória"]},
    ],
}

QUIZ = quiz([
    ("C", "A alimentação e a moradia são direitos sociais expressamente previstos no art. 6º da Constituição Federal.",
     "Foram incluídas pelas EC 64/2010 e 26/2000."),
    ("E", "O esporte integra o rol de direitos sociais do art. 6º da Constituição.",
     "O esporte é tratado no art. 217, não no art. 6º."),
    ("C", "O salário do trabalhador é irredutível, salvo o disposto em convenção ou acordo coletivo.",
     "Art. 7º, VI."),
    ("E", "As férias anuais devem ser remuneradas com, pelo menos, metade a mais do que o salário normal.",
     "O acréscimo mínimo é de um terço."),
    ("C", "A licença à gestante tem duração de cento e vinte dias, sem prejuízo do emprego e do salário.",
     "Art. 7º, XVIII."),
    ("E", "O aviso prévio é de trinta dias, fixo, independentemente do tempo de serviço.",
     "É proporcional ao tempo de serviço, sendo no mínimo de trinta dias."),
    ("C", "Ninguém será obrigado a filiar-se ou a manter-se filiado a sindicato.",
     "Art. 8º, V."),
    ("E", "Os militares das Forças Armadas podem se sindicalizar, mas não podem fazer greve.",
     "Ao militar são proibidas a sindicalização e a greve."),
    ("C", "Para o STF, é vedado o exercício do direito de greve pelos policiais civis.",
     "ARE 654.432 (Tema 541)."),
    ("E", "Compete à lei, e não aos trabalhadores, decidir sobre a oportunidade de exercer o direito de greve.",
     "Pelo art. 9º, cabe aos trabalhadores decidir sobre a oportunidade e os interesses defendidos."),
], 10)

SOURCES = [
    "Constituição da República Federativa do Brasil de 1988, arts. 6º a 11, 42 e 142.",
    "Lei 15.371/2026; STF: ARE 654.432 (Tema 541); Súmula Vinculante 40.",
    SRC_R,
]
