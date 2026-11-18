# -*- coding: utf-8 -*-
"""Direito Constitucional · Defesa do Estado: estados de defesa e de sítio, Forças Armadas — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "dc-defesa-01", "DC", "DC-12", "resumo", "Defesa do Estado: estados de defesa e de sítio, Forças Armadas",
    "Direito Constitucional · Defesa do Estado",
    "constitucional_defesa", "Constitucional_Defesa_do_Estado_RESUMO.pdf", None, ["Defesa", "do Estado"], RES_SUB,
    RES_ITEMS("estado de defesa, estado de sítio e Forças Armadas"),
    "Tópico do edital: Defesa do Estado e das instituições democráticas (arts. 136 a 143) — Direito Constitucional",
    "Base: Constituição Federal de 1988 e LC 97/1999.", 25)

THEORY = [
    exam("O que a banca cobra",
         "A diferença entre **estado de defesa** e **estado de sítio** e a missão e o regime das **Forças Armadas**."),
    h2("1. Estado de defesa"),
    bl("Ordem pública ou paz social em **locais restritos**: **instabilidade institucional** grave e iminente ou **calamidade** natural.",
       "Presidente decreta, ouvidos os **Conselhos** (opinativos); Congresso recebe em **24 h** e decide por **maioria absoluta** em **10 dias**.",
       "**30 dias** + **uma** prorrogação de 30.",
       "Medidas: restringir **reunião**, sigilo de **correspondência** e de **comunicações**; ocupar bens públicos na calamidade.",
       "Prisão: comunicada ao juiz, **até 10 dias** sem autorização judicial, **sem incomunicabilidade**."),
    h2("2. Estado de sítio"),
    bl("**Comoção grave nacional** ou **ineficácia** do estado de defesa; **guerra** ou **agressão armada** estrangeira.",
       "Presidente **pede autorização prévia** ao Congresso (**maioria absoluta**).",
       "Comoção: **30 dias**, prorrogável **cada vez** por 30. Guerra: **enquanto durar**.",
       "Medidas (comoção): permanência em local, detenção fora de presídio comum, restrições a sigilo e **imprensa**, suspensão de **reunião**, "
       "**busca domiciliar**, intervenção em serviços públicos, requisição de bens.",
       "Fiscalização: comissão de **5** congressistas; executores respondem por **ilícitos**."),
    h2("3. Forças Armadas"),
    bl("Marinha, Exército e Aeronáutica; **permanentes e regulares**; **hierarquia e disciplina**; autoridade suprema do **Presidente**.",
       "Missão: **defesa da Pátria**, **garantia dos poderes constitucionais** e, por iniciativa de qualquer deles, da **lei e da ordem** (GLO, LC 97/1999).",
       "Não são **poder moderador** (ADI 6.457).",
       "Militar: sem **sindicato** e sem **greve**; sem **filiação partidária** na ativa; cargo civil permanente › **reserva**.",
       "Oficial perde posto só por **tribunal militar** (indignidade); condenado a mais de **2 anos** é submetido a esse julgamento.",
       "Serviço militar **obrigatório**; serviço **alternativo** por imperativo de consciência; **mulheres e eclesiásticos** isentos em tempo de paz."),
]

SUMMARY = [
    h2("Quadro rápido"),
    tb(["", "Defesa", "Sítio"], [0.26, 0.37, 0.37], [
        ("Área", "Locais restritos", "Pode ser nacional"),
        ("Congresso", "Depois (24 h)", "Antes (autoriza)"),
        ("Quórum", "Maioria absoluta", "Maioria absoluta"),
        ("Prazo", "30 + 30 (uma vez)", "30 + 30 (cada vez)"),
        ("Guerra", "Não", "Enquanto durar"),
        ("Reunião", "Restringe", "Suspende"),
        ("Busca domiciliar", "Não", "Sim"),
        ("Imprensa", "Não", "Restringe"),
        ("Prisão", "Até 10 dias sem juiz", "Detenção em local especial"),
        ("Conselhos", "Ouvidos", "Ouvidos"),
    ]),
    h2("Leve para a prova"),
    bl("Defesa: Congresso **aprova depois**.",
       "Sítio: Congresso **autoriza antes**.",
       "Os dois: **maioria absoluta**.",
       "Defesa prorroga **uma vez**.",
       "Guerra = **sítio**.",
       "Busca em casa: **só no sítio**.",
       "Preso: **até 10 dias**, nunca incomunicável.",
       "FA: autoridade do **Presidente**.",
       "GLO: decide o **Presidente**.",
       "Militar: sem greve, sem sindicato, sem partido."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "DEFESA DO ESTADO", "rootSub": "arts. 136 a 143",
    "left": [
        {"label": "Defesa: hipóteses", "items": ["locais restritos", "instabilidade", "calamidade natural"]},
        {"label": "Defesa: controle", "items": ["Congresso em 24 h", "maioria absoluta", "rejeitado: cessa"]},
        {"label": "Defesa: medidas", "items": ["reunião", "correspondência", "comunicações"]},
        {"label": "Defesa: prisão", "items": ["comunica ao juiz", "até 10 dias", "sem incomunicabilidade"]},
        {"label": "Sítio: hipóteses", "items": ["comoção nacional", "defesa ineficaz", "guerra, agressão"]},
    ],
    "right": [
        {"label": "Sítio: controle", "items": ["autorização prévia", "maioria absoluta", "comissão de 5"]},
        {"label": "Sítio: medidas", "items": ["busca domiciliar", "imprensa", "requisição de bens"]},
        {"label": "Forças Armadas", "items": ["Marinha, Exército", "Aeronáutica", "hierarquia e disciplina"]},
        {"label": "Missão", "items": ["defesa da Pátria", "poderes constitucionais", "lei e ordem (GLO)"]},
        {"label": "Militares", "items": ["sem greve", "sem partido na ativa", "serviço obrigatório"]},
    ],
}

QUIZ = quiz([
    ("C", "Compete ao Presidente da República decretar o estado de defesa, ouvidos o Conselho da República e o Conselho de Defesa Nacional.",
     "Art. 136, caput."),
    ("E", "O estado de defesa pode ser prorrogado sucessivas vezes, por períodos de trinta dias, enquanto persistirem as razões que o justificaram.",
     "Admite-se uma única prorrogação."),
    ("C", "No estado de defesa, podem ser impostas restrições ao sigilo de correspondência e de comunicação telefônica.",
     "Art. 136, § 1º, I, b e c."),
    ("E", "O estado de sítio é decretado pelo Congresso Nacional, mediante solicitação do Presidente da República.",
     "Quem decreta é o Presidente, após autorização do Congresso."),
    ("C", "A resposta a agressão armada estrangeira autoriza a decretação do estado de sítio.",
     "Art. 137, II."),
    ("E", "Na vigência do estado de sítio decretado por comoção grave, é vedada qualquer restrição à liberdade de imprensa.",
     "O art. 139, III, admite restrições à liberdade de imprensa, na forma da lei."),
    ("C", "As Forças Armadas destinam-se à defesa da Pátria, à garantia dos poderes constitucionais e, por iniciativa de qualquer destes, da lei e da ordem.",
     "Art. 142, caput."),
    ("E", "Ao militar da ativa é permitida a filiação a partido político, desde que não exerça cargo de comando.",
     "Enquanto em serviço ativo, o militar não pode estar filiado a partido."),
    ("C", "As Forças Armadas devem atribuir serviço alternativo aos que, em tempo de paz, alegarem imperativo de consciência.",
     "Art. 143, § 1º."),
    ("E", "No estado de defesa, o preso por crime contra o Estado pode ser mantido incomunicável por até dez dias.",
     "A incomunicabilidade do preso é vedada."),
], 10)

SOURCES = [
    "Constituição da República Federativa do Brasil de 1988, arts. 136 a 143.",
    "Lei Complementar 97/1999; STF, ADI 6.457.",
    SRC_R,
]
