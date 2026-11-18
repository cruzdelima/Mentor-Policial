# -*- coding: utf-8 -*-
"""Direito Constitucional · Direitos e deveres individuais e coletivos (art. 5º) — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "dc-direitos-01", "DC", "DC-02", "resumo", "Direitos e deveres individuais e coletivos (art. 5º)",
    "Direito Constitucional · Direitos fundamentais",
    "constitucional_direitos", "Constitucional_Direitos_Individuais_RESUMO.pdf", None, ["Direitos", "individuais e coletivos"], RES_SUB,
    RES_ITEMS("liberdades, domicílio, sigilo e garantias penais"),
    "Tópico do edital: Direitos e deveres individuais e coletivos — Direito Constitucional",
    "Base: Constituição Federal de 1988 e jurisprudência do STF.", 40)

THEORY = [
    exam("O que a banca cobra",
         "Letra do art. 5º com palavras trocadas e julgados do STF ligados à atividade policial: **domicílio**, **interceptação**, **prova ilícita**, "
         "**extradição** e o quadro dos crimes **inafiançáveis e imprescritíveis**."),
    h2("1. Teoria geral"),
    bl("Características: universais, **relativos**, irrenunciáveis, inalienáveis, imprescritíveis, históricos.",
       "Titulares: brasileiros, estrangeiros residentes e, para o STF, também os **não residentes**; pessoas jurídicas no que couber.",
       "Valem entre particulares (**eficácia horizontal**).",
       "§ 1º aplicação imediata · § 2º rol aberto · § 3º tratado de DH com **3/5, 2 turnos, cada Casa** = emenda · § 4º TPI.",
       "Tratado de DH sem o rito do § 3º = **supralegal** (por isso a SV 25 proíbe prisão do depositário infiel)."),
    h2("2. Liberdades"),
    bl("Pensamento livre, **vedado o anonimato**; direito de resposta proporcional.",
       "**Reunião**: pacífica, sem armas, local aberto, **sem autorização**, só **prévio aviso**.",
       "**Associação**: fins lícitos, vedada a **paramilitar**; criação sem autorização; **suspensão** por decisão judicial; "
       "**dissolução** só com **trânsito em julgado**.",
       "Locomoção livre em **tempo de paz**; profissão livre, atendidas as qualificações da lei."),
    h2("3. Privacidade"),
    bl("Domicílio: **flagrante, desastre e socorro** a qualquer hora; **ordem judicial só de dia**.",
       "Entrada sem mandado: lícita com **fundadas razões** de flagrante, justificadas depois (RE 603.616).",
       "Casa inclui **escritório** fechado ao público e **quarto de hotel ocupado**.",
       "Interceptação telefônica: **ordem judicial**, na forma da **lei**, só para fins **penais**.",
       "CPI quebra sigilo bancário, fiscal e de registros telefônicos, mas **não intercepta**.",
       "Proteção de **dados pessoais** é direito fundamental (LXXIX, EC 115/2022)."),
    h2("4. Garantias penais"),
    bl("Imprescritíveis: **racismo** e **ação de grupos armados** (RAÇÃO).",
       "Inafiançáveis e sem graça ou anistia: **tortura, tráfico, terrorismo e hediondos** (prescrevem).",
       "Penas vedadas: morte (salvo **guerra declarada**), perpétua, trabalhos forçados, banimento, cruéis.",
       "Extradição: nato **nunca**; naturalizado por crime comum **anterior** ou **tráfico**; estrangeiro, salvo crime político ou de opinião.",
       "Prisão só em flagrante ou por ordem **escrita e fundamentada** de juiz (salvo transgressão e crime propriamente militar).",
       "Prisão civil apenas do devedor de **alimentos**."),
]

SUMMARY = [
    h2("Quadro rápido"),
    tb(["Tema", "Regra"], [0.34, 0.66], [
        ("Reunião", "Sem autorização · prévio aviso"),
        ("Associação: suspensão", "Decisão judicial"),
        ("Associação: dissolução", "Decisão judicial transitada em julgado"),
        ("Domicílio com ordem judicial", "Só durante o dia"),
        ("Flagrante, desastre, socorro", "Dia ou noite"),
        ("Interceptação telefônica", "Juiz · lei · fins penais"),
        ("Racismo", "Inafiançável, imprescritível, reclusão"),
        ("Tortura, tráfico, terrorismo, hediondos", "Inafiançáveis, sem graça ou anistia"),
        ("Pena de morte", "Só em guerra declarada"),
        ("Extradição de nato", "Nunca"),
    ]),
    h2("Leve para a prova"),
    bl("Reunião pede **aviso**, não autorização.",
       "Dissolver associação: **trânsito em julgado**.",
       "Mandado judicial: só **de dia**.",
       "Fundadas razões **justificadas depois** validam a entrada.",
       "Interceptação: só **penal** e só por **juiz**.",
       "CPI **não** intercepta.",
       "Imprescritível: **racismo e grupos armados**.",
       "**3TH** prescrevem.",
       "Nato **nunca** é extraditado.",
       "Depositário infiel **não** é preso (SV 25)."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "ART. 5º", "rootSub": "direitos individuais",
    "left": [
        {"label": "Teoria geral", "items": ["relativos", "eficácia horizontal", "estrangeiro não residente"]},
        {"label": "Tratados", "items": ["3/5, 2 turnos = EC", "sem rito = supralegal", "SV 25"]},
        {"label": "Reunião", "items": ["pacífica, sem armas", "sem autorização", "prévio aviso"]},
        {"label": "Associação", "items": ["fins lícitos", "suspensão: juiz", "dissolução: trânsito"]},
        {"label": "Domicílio", "items": ["ordem judicial: dia", "flagrante: qualquer hora", "fundadas razões"]},
    ],
    "right": [
        {"label": "Sigilo", "items": ["interceptação: juiz", "só fins penais", "CPI não intercepta"]},
        {"label": "Imprescritíveis", "items": ["racismo", "grupos armados", "RAÇÃO"]},
        {"label": "Inafiançáveis", "items": ["tortura, tráfico", "terrorismo, hediondos", "sem graça ou anistia"]},
        {"label": "Penas vedadas", "items": ["morte (salvo guerra)", "perpétua, banimento", "forçados, cruéis"]},
        {"label": "Extradição", "items": ["nato: nunca", "naturalizado: antes ou tráfico", "não por crime político"]},
    ],
}

QUIZ = quiz([
    ("C", "A liberdade de reunião em locais abertos ao público independe de autorização, exigindo-se apenas prévio aviso à autoridade competente.",
     "É a letra do art. 5º, XVI."),
    ("E", "As associações só podem ser compulsoriamente dissolvidas por decisão administrativa fundamentada do Ministério da Justiça.",
     "A dissolução compulsória exige decisão judicial transitada em julgado."),
    ("C", "O ingresso em domicílio para prestar socorro pode ocorrer durante a noite, mesmo sem o consentimento do morador.",
     "Socorro, desastre e flagrante não têm restrição de horário."),
    ("E", "O escritório profissional de um advogado, por não ser moradia, não recebe a proteção da inviolabilidade do domicílio.",
     "O conceito de casa abrange o compartimento não aberto ao público onde alguém exerce profissão."),
    ("C", "A interceptação telefônica depende de ordem judicial e só pode ser utilizada para investigação criminal ou instrução processual penal.",
     "É a parte final do art. 5º, XII."),
    ("E", "Os crimes hediondos, assim como o racismo, são imprescritíveis.",
     "Os hediondos são inafiançáveis e insuscetíveis de graça ou anistia, mas prescrevem."),
    ("C", "A Constituição veda a pena de banimento.",
     "Está no rol do art. 5º, XLVII."),
    ("E", "O brasileiro nato pode ser extraditado por crime de tráfico ilícito de entorpecentes cometido no exterior.",
     "O brasileiro nato nunca será extraditado."),
    ("C", "O estrangeiro não será extraditado por crime político ou de opinião.",
     "É o art. 5º, LII."),
    ("E", "Pela Constituição, a prisão de qualquer pessoa, fora do flagrante, depende de ordem escrita da autoridade policial competente.",
     "Fora do flagrante, a ordem deve ser escrita e fundamentada de autoridade judiciária, salvo transgressão ou crime propriamente militar."),
], 10)

SOURCES = [
    "Constituição da República Federativa do Brasil de 1988, art. 5º.",
    "Supremo Tribunal Federal: RE 603.616 (Tema 280); Súmula Vinculante 25.",
    SRC_R,
]
