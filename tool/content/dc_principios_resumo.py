# -- coding: utf-8 --
"""Direito Constitucional · Princípios fundamentais (arts. 1º a 4º) — RESUMO (revisão)."""
from common import *

MATERIAL = {
    "id": "dc-principios-01",
    "version": "0.1.0",
    "status": "Em revisão pelo autor",
    "subjectId": "DC",
    "topicIds": ["DC-01"],
    "kind": "resumo",
    "title": "Princípios fundamentais (arts. 1º a 4º)",
    "subtitle": "Direito Constitucional · Título I da Constituição",
    "minutes": 40,
    "folder": "constitucional_principios",
    "pdf": "constitucional_principios.pdf",
    "outName": "Constitucional_Principios_Fundamentais_RESUMO.pdf",
    "header": "Direito Constitucional · Princípios fundamentais",
    "coverKicker": "Direito Constitucional  ·  Título I da CF/88",
    "coverTitle": ["Princípios", "fundamentais"],
    "coverSub": ["Resumo direto ao ponto dos arts. 1º a 4º, quadro das três listas, mapa mental", "e 10 questões no estilo Cebraspe com gabarito comentado."],
    "coverItems": [("01", "Teoria", "fundamentos, Poderes, objetivos e relações internacionais"),
                   ("02", "Resumo", "quadro das três listas e “leve para a prova”"),
                   ("03", "Mapa mental", "uma página para revisar em 5 minutos"),
                   ("04", "Questões", "10 itens certo/errado + gabarito comentado")],
    "coverTopic": "Tópico do edital: Princípios fundamentais (arts. 1º a 4º) — Direito Constitucional",
    "coverBase": "Base: Constituição Federal de 1988 e jurisprudência do STF.",
}

THEORY = [
    exam("O que a banca cobra",
         "A **mistura das três listas** (fundamentos, objetivos e princípios internacionais) e os **conceitos**: república × federação, "
         "soberania × autonomia, democracia semidireta, funções típicas × atípicas e cláusulas pétreas."),

    h2("1. Art. 1º: o que o Brasil é"),
    tb(["Pergunta", "Resposta"], [0.34, 0.66], [
        ("Forma de governo", "**República** (eletividade, temporariedade, responsabilidade)"),
        ("Forma de Estado", "**Federação** (união indissolúvel de Estados, Municípios e DF)"),
        ("Regime político", "**Democracia** semidireta ou participativa"),
        ("Sistema de governo", "**Presidencialismo** (não está no art. 1º)"),
    ]),
    bl("**Municípios** são entes federativos; **Territórios** não (integram a União).",
       "**Soberania** é da República Federativa do Brasil; os entes têm **autonomia**.",
       "**Indissolúvel**: não há direito de secessão.",
       "**Cláusulas pétreas** (art. 60, § 4º): forma federativa; voto direto, secreto, universal e periódico; separação dos Poderes; "
       "direitos e garantias individuais. **República não está na lista.**",
       "O **preâmbulo** não tem força normativa (STF)."),
    key("Fundamentos: SO-CI-DI-VA-PLU",
        "**SO**berania; **CI**dadania; **DI**gnidade da pessoa humana; **VA**lores sociais do trabalho e da livre iniciativa; **PLU**ralismo político."),
    p("**Parágrafo único**: todo o poder emana do **povo**, que o exerce por meio de **representantes eleitos ou diretamente**. "
      "Instrumentos diretos: **plebiscito** (antes do ato), **referendo** (depois) e **iniciativa popular**."),
    nt("Dignidade da pessoa humana na prática policial: Súmula Vinculante 11 — algemas só em caso de resistência, fundado receio de fuga ou perigo à integridade física, com justificativa por escrito."),

    h2("2. Art. 2º: separação dos Poderes"),
    p("São Poderes da União, **independentes e harmônicos entre si**, o Legislativo, o Executivo e o Judiciário."),
    tb(["Poder", "Função típica", "Função atípica (exemplo)"], [0.2, 0.3, 0.5], [
        ("Legislativo", "Legislar e fiscalizar", "Julgar o Presidente por crime de responsabilidade (Senado)"),
        ("Executivo", "Administrar", "Editar medida provisória"),
        ("Judiciário", "Julgar", "Elaborar regimento interno; administrar seus serviços"),
    ]),
    bl("A separação é **relativa**: há **freios e contrapesos** (veto, derrubada de veto, controle de constitucionalidade, impeachment).",
       "É **cláusula pétrea**.",
       "Ministério Público, Defensoria e Tribunais de Contas **não são Poderes**."),

    h2("3. Art. 3º: objetivos fundamentais"),
    key("Objetivos: CON-GA-ER-PRO (verbos no infinitivo)",
        "**CON**struir uma sociedade livre, justa e solidária; **GA**rantir o desenvolvimento nacional; **ER**radicar a pobreza e a "
        "marginalização e reduzir as desigualdades sociais e regionais; **PRO**mover o bem de todos, sem preconceitos de origem, raça, sexo, "
        "cor, idade e quaisquer outras formas de discriminação."),
    trap("Pegadinha",
         "**Erradicar** a pobreza e a marginalização; **reduzir** as desigualdades. Desenvolvimento **nacional**, não regional."),

    h2("4. Art. 4º: relações internacionais"),
    bl("Independência nacional; prevalência dos direitos humanos; autodeterminação dos povos; não-intervenção; igualdade entre os Estados.",
       "Defesa da paz; solução pacífica dos conflitos.",
       "Repúdio ao terrorismo e ao racismo; cooperação entre os povos para o progresso da humanidade; concessão de asilo político.",
       "**Parágrafo único**: integração econômica, política, social e cultural dos povos da **América Latina**, visando a uma comunidade **latino-americana** de nações."),
]

SUMMARY = [
    h2("Quadro das três listas"),
    tb(["Art. 1º — Fundamentos (o que é)", "Art. 3º — Objetivos (o que busca)", "Art. 4º — Relações internacionais"], [0.3, 0.36, 0.34], [
        ("Soberania", "Construir uma sociedade livre, justa e solidária", "Independência nacional"),
        ("Cidadania", "Garantir o desenvolvimento nacional", "Prevalência dos direitos humanos"),
        ("Dignidade da pessoa humana", "Erradicar a pobreza e a marginalização e reduzir as desigualdades", "Autodeterminação; não-intervenção; igualdade entre os Estados"),
        ("Valores sociais do trabalho e da livre iniciativa", "Promover o bem de todos, sem discriminação", "Defesa da paz; solução pacífica dos conflitos"),
        ("Pluralismo político", "—", "Repúdio ao terrorismo e ao racismo; cooperação; asilo político"),
    ]),
    h2("Leve para a prova"),
    bl("**Substantivo** = fundamento (art. 1º). **Verbo** = objetivo (art. 3º). **Postura externa** = art. 4º.",
       "República = forma de **governo**. Federação = forma de **Estado**.",
       "Só a **forma federativa** é cláusula pétrea; a república, não.",
       "**Soberania** é do Estado brasileiro; os entes têm **autonomia**.",
       "Poder do **povo**, exercido por representantes **ou diretamente**.",
       "Poderes **independentes e harmônicos**; separação **relativa**.",
       "**Erradicar** a pobreza; **reduzir** as desigualdades.",
       "Integração da **América Latina**.",
       "**Pluralismo político** é mais que pluripartidarismo.",
       "Preâmbulo: **sem força normativa**."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "PRINCÍPIOS FUNDAMENTAIS",
    "rootSub": "CF/88 · arts. 1º a 4º",
    "left": [
        {"label": "Art. 1º · O Estado", "items": ["República: forma de governo", "Federação: forma de Estado", "Estado Democrático de Direito"]},
        {"label": "Fundamentos", "items": ["Soberania · cidadania", "Dignidade da pessoa humana", "Trabalho e livre iniciativa · pluralismo"]},
        {"label": "Poder do povo", "items": ["Representantes ou diretamente", "Plebiscito · referendo", "Iniciativa popular"]},
        {"label": "Federação", "items": ["Estados, Municípios e DF", "Territórios não são entes", "Sem secessão · cláusula pétrea"]},
        {"label": "Art. 2º · Poderes", "items": ["Independentes e harmônicos", "Funções típicas e atípicas", "Freios e contrapesos"]},
    ],
    "right": [
        {"label": "Art. 3º · Objetivos", "items": ["Construir sociedade livre e justa", "Garantir o desenvolvimento nacional", "Erradicar a pobreza · promover o bem"]},
        {"label": "Art. 4º · Soberania", "items": ["Independência nacional", "Autodeterminação · não-intervenção", "Igualdade entre os Estados"]},
        {"label": "Art. 4º · Paz e valores", "items": ["Defesa da paz · solução pacífica", "Direitos humanos · asilo político", "Repúdio ao terrorismo e ao racismo"]},
        {"label": "Integração", "items": ["América Latina", "Econômica, política, social, cultural"]},
        {"label": "Jurisprudência", "items": ["Preâmbulo sem força normativa", "SV 11: uso de algemas", "República não é cláusula pétrea"]},
    ],
}

QUIZ = quiz([
    ("C", "São fundamentos da República Federativa do Brasil a soberania, a cidadania, a dignidade da pessoa humana, os valores sociais do trabalho e da livre iniciativa e o pluralismo político.",
     "É o rol do art. 1º, incisos I a V."),
    ("E", "Construir uma sociedade livre, justa e solidária é fundamento da República Federativa do Brasil.",
     "É objetivo fundamental (art. 3º, I). Os objetivos começam por verbo."),
    ("E", "A federação é a forma de governo adotada pela Constituição de 1988, e a república, a forma de Estado.",
     "Invertido: república é forma de governo; federação é forma de Estado."),
    ("C", "Os municípios integram a federação brasileira na condição de entes dotados de autonomia.",
     "A República é formada pela união indissolúvel dos Estados, dos Municípios e do Distrito Federal, todos autônomos."),
    ("E", "Compete ao Poder Legislativo, como função típica, julgar o presidente da República nos crimes de responsabilidade.",
     "O julgamento pelo Senado é função atípica. As funções típicas do Legislativo são legislar e fiscalizar."),
    ("C", "A separação dos Poderes não pode ser abolida por emenda constitucional.",
     "É cláusula pétrea (art. 60, § 4º, III)."),
    ("E", "É objetivo fundamental da República Federativa do Brasil erradicar as desigualdades sociais e regionais.",
     "O texto fala em erradicar a pobreza e a marginalização e reduzir as desigualdades sociais e regionais."),
    ("C", "A autodeterminação dos povos e a não-intervenção são princípios que regem as relações internacionais do Brasil.",
     "Art. 4º, III e IV."),
    ("E", "O referendo é a consulta formulada ao povo antes da edição do ato legislativo ou administrativo.",
     "Consulta prévia é plebiscito. O referendo é posterior ao ato, para confirmá-lo ou rejeitá-lo."),
    ("C", "A soberania aparece na Constituição como fundamento da República e, nas relações internacionais, manifesta-se no princípio da independência nacional.",
     "Art. 1º, I, e art. 4º, I."),
], 10)

SOURCES = [
    "Constituição da República Federativa do Brasil de 1988, arts. 1º a 4º, 14, 18 e 60; STF, Súmula Vinculante 11 e ADI 2.076.",
    "Texto e questões elaborados para o Mentor Policial (itens inéditos no estilo Cebraspe).",
]
