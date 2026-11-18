# -*- coding: utf-8 -*-
"""Direito Constitucional · Poder Judiciário e funções essenciais à Justiça — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "dc-judiciario-01", "DC", "DC-11", "resumo", "Poder Judiciário e funções essenciais à Justiça", "Direito Constitucional · Organização dos Poderes",
    "constitucional_judiciario", "Constitucional_Poder_Judiciario_RESUMO.pdf", None, ["Poder Judiciário", "e funções essenciais"], RES_SUB,
    RES_ITEMS("garantias, STF, STJ, Justiça Federal e MP"),
    "Tópico do edital: Poder Judiciário e funções essenciais à Justiça (arts. 92 a 135) — Direito Constitucional",
    "Base: Constituição Federal de 1988 e jurisprudência do STF e do STJ.", 35)

THEORY = [
    exam("O que a banca cobra",
         "Garantias dos juízes, composição do **STF** e do **STJ**, **quem julga quem**, **Justiça Federal**, **Justiça Militar estadual** e o **MP**."),
    h2("1. Magistratura"),
    bl("Garantias: **vitaliciedade** (2 anos no 1º grau), **inamovibilidade** (salvo interesse público, maioria absoluta), **irredutibilidade**.",
       "Vedações: outro cargo **salvo um de magistério**; custas; política partidária; **quarentena de 3 anos** para advogar.",
       "Ingresso: concurso com OAB e **3 anos** de atividade jurídica. **Quinto**: MP e advogados com **10 anos**; sêxtupla › tríplice › Executivo.",
       "Reserva de plenário: inconstitucionalidade só por **maioria absoluta** do tribunal (SV 10)."),
    h2("2. Tribunais"),
    bl("**STF**: **11** Ministros **natos**, 35 a 70 anos; Presidente nomeia após **maioria absoluta** do Senado.",
       "STF julga, em crime comum, **Presidente, Vice, congressistas, PGR**; e Ministros de Estado, comandantes militares, tribunais superiores e TCU.",
       "**Súmula vinculante**: **2/3** do STF; vincula Judiciário e administração; **não** vincula o legislador nem o STF; cabe **reclamação**.",
       "**CNJ**: 15 membros, presidido pelo Presidente do STF; só administrativo; **não** controla o STF.",
       "**STJ**: mínimo **33** Ministros (não precisam ser natos); julga **Governadores** em crime comum; homologa **sentença estrangeira**."),
    h2("3. Justiça Federal e Militar"),
    bl("JF: União, autarquias e **empresas públicas** federais (não SEM); crimes contra **bens, serviços e interesses da União** (sem "
       "**contravenções**); crimes de **tratado** transnacionais; sistema financeiro; navios e aeronaves; estrangeiro irregular; indígenas.",
       "**IDC**: PGR suscita no **STJ**, em grave violação de direitos humanos.",
       "Justiça Militar estadual julga **só militares**; homicídio doloso de **civil** por PM vai ao **júri**."),
    h2("4. Funções essenciais"),
    bl("**MP**: unidade, indivisibilidade, independência funcional; ação penal pública **privativa**; **controle externo da atividade policial**; "
       "requisita diligências e inquérito; pode investigar.",
       "**PGR**: da carreira, 35 anos, Senado por **maioria absoluta**, **2 anos** com recondução.",
       "**AGU**: livre nomeação. **Advogado**: indispensável e inviolável nos limites da lei. **Defensoria**: necessitados, integral e gratuita."),
]

SUMMARY = [
    h2("Quadro rápido"),
    tb(["Quem", "É julgado por"], [0.5, 0.5], [
        ("Presidente (crime comum)", "STF"),
        ("Deputados e senadores", "STF"),
        ("Ministros de Estado", "STF"),
        ("Governadores (crime comum)", "STJ"),
        ("Desembargadores", "STJ"),
        ("Tráfico internacional de drogas", "Justiça Federal"),
        ("Contravenção contra bem da União", "Justiça Estadual"),
        ("Crime contra empresa pública federal", "Justiça Federal"),
        ("PM que mata civil dolosamente", "Tribunal do Júri"),
        ("Civil em crime militar estadual", "Justiça comum"),
    ]),
    h2("Leve para a prova"),
    bl("Juiz pode dar **aula**.",
       "Vitaliciedade no 1º grau: **2 anos**.",
       "STF: **11 natos**; STJ: **33**, não precisa ser nato.",
       "Senado aprova por **maioria absoluta**.",
       "SV não vincula o **legislador**.",
       "CNJ **não** controla o STF.",
       "Sentença estrangeira: **STJ**.",
       "Contravenção: **nunca** na Justiça Federal.",
       "JM estadual **não** julga civil.",
       "MP faz o **controle externo** da polícia."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "JUDICIÁRIO", "rootSub": "arts. 92 a 135",
    "left": [
        {"label": "Garantias", "items": ["vitaliciedade: 2 anos", "inamovibilidade", "irredutibilidade"]},
        {"label": "Vedações", "items": ["salvo magistério", "sem política", "quarentena: 3 anos"]},
        {"label": "STF", "items": ["11 natos", "35 a 70 anos", "Senado: absoluta"]},
        {"label": "Súmula vinculante", "items": ["2/3 do STF", "vincula Judiciário", "não o legislador"]},
        {"label": "STJ e CNJ", "items": ["STJ: governadores", "sentença estrangeira", "CNJ: administrativo"]},
    ],
    "right": [
        {"label": "Justiça Federal", "items": ["União e EP federal", "tratado transnacional", "sem contravenção"]},
        {"label": "Justiça Militar", "items": ["União: julga civil", "estadual: só militar", "civil morto: júri"]},
        {"label": "Ministério Público", "items": ["ação penal privativa", "controle externo", "requisita inquérito"]},
        {"label": "PGR", "items": ["da carreira", "2 anos", "recondução"]},
        {"label": "Outras funções", "items": ["AGU: livre nomeação", "advogado inviolável", "Defensoria: necessitados"]},
    ],
}

QUIZ = quiz([
    ("C", "É vedado aos juízes dedicar-se a atividade político-partidária.",
     "Art. 95, parágrafo único, III."),
    ("E", "O juiz que se aposentar pode advogar imediatamente no tribunal do qual se afastou.",
     "Há quarentena de três anos (art. 95, parágrafo único, V)."),
    ("C", "Um quinto dos lugares dos tribunais regionais federais e dos tribunais de justiça é composto de membros do Ministério Público e de advogados com mais de dez anos de carreira ou atividade.",
     "Art. 94."),
    ("E", "Os Ministros do Superior Tribunal de Justiça devem ser brasileiros natos.",
     "A Constituição não exige nacionalidade originária para o STJ."),
    ("C", "A súmula vinculante pode ser aprovada pelo STF mediante decisão de dois terços dos seus membros.",
     "Art. 103-A."),
    ("E", "O Conselho Nacional de Justiça exerce função jurisdicional e pode rever decisões judiciais.",
     "O CNJ tem competência apenas administrativa, financeira e disciplinar."),
    ("C", "Compete aos juízes federais processar e julgar os crimes cometidos a bordo de navios ou aeronaves, ressalvada a competência da Justiça Militar.",
     "Art. 109, IX."),
    ("E", "A Justiça Militar estadual é competente para julgar o crime doloso contra a vida de civil praticado por policial militar em serviço.",
     "A competência é do Tribunal do Júri (art. 125, § 4º)."),
    ("C", "A ação penal pública é promovida privativamente pelo Ministério Público.",
     "Art. 129, I."),
    ("E", "O advogado é inviolável por seus atos e manifestações no exercício da profissão, de forma absoluta e sem limites.",
     "A inviolabilidade é nos limites da lei (art. 133)."),
], 10)

SOURCES = [
    "Constituição da República Federativa do Brasil de 1988, arts. 92 a 135.",
    "Superior Tribunal de Justiça: Súmula 38.",
    SRC_R,
]
