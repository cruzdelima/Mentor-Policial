# -*- coding: utf-8 -*-
"""Língua Portuguesa · Análise sintática: termos da oração — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "lp-termos-01", "LP", "LP-08", "resumo", "Análise sintática: termos da oração", "Língua Portuguesa · Sintaxe",
    "portugues_termos", "Portugues_Termos_da_Oracao_RESUMO.pdf", None, ["Termos", "da oração"], RES_SUB,
    RES_ITEMS("sujeito, predicado, complementos, adjuntos, aposto e vocativo"),
    "Tópico do edital: Sintaxe da oração — termos da oração (Língua Portuguesa)",
    "Base: gramáticas de referência e Nomenclatura Gramatical Brasileira (NGB).", 40)

THEORY = [
    exam("O que a banca cobra",
         "**Função sintática** de termos, **sujeito posposto** e impessoalidade (concordância) e **vírgula** entre sujeito e verbo."),
    h2("1. Sujeito"),
    bl("**Simples, composto, oculto** (identificado pela desinência ou pelo contexto).",
       "**Indeterminado**: 3ª pessoa do plural **sem referente** (*Roubaram a viatura*) ou **VTI/VI/VL + se** (*Precisa-se de peritos*).",
       "**Sem sujeito**: *haver* (existir, tempo), *fazer/estar/ser* (tempo, clima), fenômenos da natureza.",
       "*Existir* tem sujeito: *Existiam provas*. Sujeito **posposto** também comanda o verbo: *Faltam dois documentos*."),
    h2("2. Predicado"),
    bl("**Verbal**: núcleo é verbo de ação (*prendeu o suspeito*).",
       "**Nominal**: verbo de ligação + predicativo (*ficou preocupado*).",
       "**Verbo-nominal**: verbo de ação + predicativo (*chegaram cansados*; *considerou o réu culpado*)."),
    h2("3. Complementos"),
    tb(["Termo", "Completa", "Exemplo"], [0.26, 0.32, 0.42], [
        ("Objeto direto", "VTD, sem preposição", "prendeu **o suspeito**"),
        ("Objeto indireto", "VTI, com preposição", "obedeceu **às ordens**"),
        ("Complemento nominal", "Nome (substantivo, adjetivo, advérbio)", "obediência **às leis**; favorável **ao réu**"),
        ("Agente da passiva", "Verbo na voz passiva", "instaurado **pelo delegado**"),
        ("Predicativo do objeto", "Característica do objeto", "julgou o réu **culpado**"),
    ]),
    h2("4. Acessórios, aposto e vocativo"),
    bl("**Adjunto adnominal**: caracteriza o substantivo (*os dois agentes **experientes da equipe***).",
       "**Adjunto adverbial**: circunstância (*ontem, no bairro, com cautela*).",
       "**Aposto**: explica, enumera, resume ou especifica (*Carlos, **o escrivão**, …*).",
       "**Vocativo**: chama o interlocutor, sempre entre vírgulas (***Soldado**, apresente-se*)."),
    key("CN × adjunto adnominal",
        "Termo com *de* ligado a substantivo abstrato: se é **alvo** da ação, é **complemento nominal** (*investigação **da fraude***); "
        "se **pratica** a ação ou indica posse/matéria, é **adjunto adnominal** (*chegada **dos agentes**; mesa **de madeira***). "
        "Ligado a **adjetivo ou advérbio**: sempre CN."),
    trap("Vírgula proibida",
         "Nunca separe **sujeito e verbo** nem **verbo e complemento** por vírgula, por mais longo que seja o sujeito."),
]

SUMMARY = [
    h2("Quadro de reconhecimento"),
    tb(["Pergunta", "Termo", "Exemplo"], [0.36, 0.26, 0.38], [
        ("Quem pratica / de quem se fala?", "Sujeito", "**Os agentes** chegaram."),
        ("O verbo pede algo sem preposição?", "Objeto direto", "Prendeu **o suspeito**."),
        ("O verbo pede algo com preposição?", "Objeto indireto", "Obedeceu **ao chefe**."),
        ("Um nome pede complemento?", "Complemento nominal", "Medo **de represálias**."),
        ("Quem age na passiva?", "Agente da passiva", "Preso **pela PM**."),
        ("Característica do sujeito?", "Predicativo do sujeito", "Ficou **calmo**."),
        ("Característica do objeto?", "Predicativo do objeto", "Julgou-o **culpado**."),
        ("Qualifica o substantivo?", "Adjunto adnominal", "Mesa **de madeira**."),
        ("Circunstância?", "Adjunto adverbial", "Saiu **à noite**."),
        ("Chama alguém?", "Vocativo", "**Senhor**, sente-se."),
    ]),
    h2("Leve para a prova"),
    bl("Comece pelo **verbo**: ele define sujeito e complementos.",
       "Sujeito posposto continua sendo sujeito (concordância!).",
       "*Haver* = existir: **sem sujeito**, verbo no singular.",
       "3ª do plural **com** referente = oculto; **sem** referente = indeterminado.",
       "VTD + se = passiva (sujeito); VTI + se = indeterminado.",
       "Predicado verbo-nominal = verbo de ação + predicativo.",
       "CN = alvo; adjunto adnominal = agente, posse, matéria.",
       "Complemento de adjetivo = sempre CN.",
       "Aposto explicativo e vocativo: entre vírgulas.",
       "Sujeito e verbo: **nunca** separados por vírgula."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "TERMOS", "rootSub": "da oração",
    "left": [
        {"label": "Sujeito", "items": ["simples · composto · oculto", "posposto: chegaram os laudos", "existir tem sujeito"]},
        {"label": "Indeterminado", "items": ["3ª pl. sem referente", "VTI/VI + se", "precisa-se de peritos"]},
        {"label": "Sem sujeito", "items": ["haver = existir", "faz dois anos", "choveu, anoiteceu"]},
        {"label": "Predicado", "items": ["verbal: ação", "nominal: VL + predicativo", "verbo-nominal: os dois"]},
        {"label": "Predicativo", "items": ["do sujeito: ficou calmo", "do objeto: julgou-o culpado", "teste do pronome"]},
    ],
    "right": [
        {"label": "Objetos", "items": ["OD: sem preposição", "OI: com preposição", "OD preposicionado: amar a Deus"]},
        {"label": "Complemento nominal", "items": ["completa nome", "alvo da ação", "favorável ao réu"]},
        {"label": "Adjuntos", "items": ["adnominal: caracteriza", "adverbial: circunstância", "agente, posse, matéria"]},
        {"label": "Aposto e vocativo", "items": ["aposto explica o termo", "vocativo chama", "ambos entre vírgulas"]},
        {"label": "Vírgula", "items": ["nunca sujeito | verbo", "nunca verbo | complemento", "adjunto deslocado: pode"]},
    ],
}

QUIZ = quiz([
    ("C", "Em “Existiam provas suficientes no processo”, o termo provas suficientes exerce a função de sujeito.",
     "Existir é verbo pessoal: provas suficientes é o sujeito, e o verbo concorda com ele."),
    ("E", "Em “Havia provas suficientes no processo”, o termo provas suficientes exerce a função de sujeito.",
     "Haver no sentido de existir é impessoal; provas suficientes é objeto direto."),
    ("C", "Em “Necessita-se de reforços”, o sujeito é indeterminado.",
     "Necessitar de é transitivo indireto; com o se, o sujeito fica indeterminado."),
    ("E", "Em “O suspeito parecia nervoso”, o termo nervoso exerce a função de adjunto adnominal.",
     "Parecer é verbo de ligação: nervoso é predicativo do sujeito."),
    ("C", "Em “Ele tem medo de represálias”, o termo de represálias exerce a função de complemento nominal.",
     "Completa o sentido do substantivo abstrato medo."),
    ("E", "Em “Compraram uma mesa de madeira para a sala”, o termo de madeira exerce a função de complemento nominal.",
     "De madeira indica matéria e caracteriza mesa: é adjunto adnominal."),
    ("C", "Em “Entreguei o ofício ao comandante”, o termo ao comandante exerce a função de objeto indireto.",
     "Entregar algo a alguém: ao comandante é o complemento preposicionado."),
    ("E", "Em “A denúncia foi feita por um vizinho”, o termo por um vizinho é adjunto adverbial de causa.",
     "Em voz passiva, quem pratica a ação é o agente da passiva."),
    ("C", "Em “Soldado, apresente-se ao comandante”, o termo Soldado exerce a função de vocativo.",
     "O termo chama o interlocutor e vem isolado por vírgula."),
    ("E", "Admite-se vírgula entre o sujeito e o verbo quando o sujeito é longo.",
     "Não se separa o sujeito do verbo por vírgula, qualquer que seja a extensão do sujeito."),
], 10)

SOURCES = [GRAM, SRC_R]
