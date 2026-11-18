# -*- coding: utf-8 -*-
"""Direito Constitucional · Organização político-administrativa do Estado (arts. 18 a 33) — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "dc-organizacao-01", "DC", "DC-07", "resumo", "Organização político-administrativa do Estado (arts. 18 a 33)",
    "Direito Constitucional · Organização do Estado",
    "constitucional_organizacao", "Constitucional_Organizacao_do_Estado_RESUMO.pdf", None, ["Organização", "do Estado"], RES_SUB,
    RES_ITEMS("entes, criação, competências, DF e Territórios"),
    "Tópico do edital: Organização político-administrativa do Estado (arts. 18 a 33) — Direito Constitucional",
    "Base: Constituição Federal de 1988 e súmulas vinculantes do STF.", 35)

THEORY = [
    exam("O que a banca cobra",
         "**Arts. 21 a 24** (quem faz e quem legisla), as **polícias** na repartição de competências e a criação de Estados e Municípios."),
    h2("1. Federação"),
    bl("União, Estados, DF e Municípios: todos **autônomos**. Territórios **integram a União**.",
       "Vedado aos entes: aliança com **igrejas**, **recusar fé** a documentos públicos, **distinguir brasileiros**.",
       "Estados: **plebiscito** + **lei complementar** federal. Municípios: **lei estadual** + LC federal (período) + estudos + plebiscito.",
       "Faixa de fronteira: até **150 km**."),
    h2("2. Competências"),
    bl("**Art. 21 exclusiva** (fazer, União, indelegável): guerra, sítio, defesa, intervenção, moeda, **polícias do DF**, polícia marítima, "
       "aeroportuária e de fronteiras.",
       "**Art. 22 privativa** (legislar, União, **delegável por LC** aos Estados): **CAPACETE DE PM**, trânsito, normas gerais das **PMs e "
       "bombeiros**, competência da **PF, PRF e PFF**, dados pessoais.",
       "**Art. 23 comum** (fazer, todos): saúde, meio ambiente, patrimônio histórico, pobreza, educação para o trânsito.",
       "**Art. 24 concorrente** (legislar, União + Estados + DF): **PUFETO**, procedimentos processuais, **polícias civis**.",
       "No art. 24: União faz **normas gerais**; Estados **suplementam**; sem lei federal, Estado tem competência **plena**; lei federal "
       "posterior **suspende** a estadual contrária."),
    h2("3. Entes em espécie"),
    bl("**Estados**: competência **residual**; gás canalizado; regiões metropolitanas por **LC estadual**; deputados estaduais = **triplo** "
       "dos federais, e acima de 36 soma-se o que passar de 12.",
       "**Municípios**: lei orgânica (**2 turnos, 10 dias, 2/3**); interesse **local**; horário do comércio (**SV 38**); vedados novos "
       "tribunais de contas municipais.",
       "**DF**: **não** se divide em Municípios; competências de Estado + Município; polícias, Judiciário e MP **mantidos pela União**; "
       "vencimentos das polícias do DF por **lei federal** (SV 39).",
       "**Territórios**: governador nomeado pelo Presidente com aprovação do Senado; **4 deputados**, **nenhum senador**."),
]

SUMMARY = [
    h2("Quadro rápido"),
    tb(["Matéria", "Competência"], [0.6, 0.4], [
        ("Direito penal e processual penal", "Privativa da União (22)"),
        ("Direito penitenciário", "Concorrente (24)"),
        ("Normas gerais das PMs e bombeiros", "Privativa da União (22)"),
        ("Organização das polícias civis", "Concorrente (24)"),
        ("Competência da PF e da PRF", "Privativa da União (22)"),
        ("Organizar e manter as polícias do DF", "Exclusiva da União (21)"),
        ("Vencimentos das polícias do DF", "União (SV 39)"),
        ("Polícia marítima, aeroportuária, fronteiras", "Exclusiva da União (21)"),
        ("Horário do comércio local", "Município (SV 38)"),
        ("Proteger o meio ambiente", "Comum (23)"),
    ]),
    h2("Leve para a prova"),
    bl("Art. 21 **não** se delega; art. 22 se delega por **LC**.",
       "Município **não** está no art. 24.",
       "Lei federal nova **suspende**, não revoga.",
       "Penal: **22**. Penitenciário: **24**.",
       "Polícia civil (organização): **24**.",
       "PM (normas gerais): **22**.",
       "Polícias do DF: **União** organiza e mantém.",
       "DF **não** tem Municípios.",
       "Território: **4 deputados**, **0 senador**.",
       "Município cria **por lei estadual**."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "ORGANIZAÇÃO", "rootSub": "arts. 18 a 33",
    "left": [
        {"label": "Entes", "items": ["União, Estados", "DF, Municípios", "Territórios: da União"]},
        {"label": "Criação", "items": ["Estado: plebiscito + LC", "Município: lei estadual", "Território: LC"]},
        {"label": "Art. 21", "items": ["exclusiva, fazer", "indelegável", "polícias do DF"]},
        {"label": "Art. 22", "items": ["privativa, legislar", "delegável por LC", "CAPACETE DE PM"]},
        {"label": "Art. 23", "items": ["comum, fazer", "todos os entes", "saúde, meio ambiente"]},
    ],
    "right": [
        {"label": "Art. 24", "items": ["concorrente", "PUFETO", "polícias civis"]},
        {"label": "Regras do 24", "items": ["União: normas gerais", "Estado: suplementar", "lei nova suspende"]},
        {"label": "Estados", "items": ["residual", "gás canalizado", "deputados: triplo"]},
        {"label": "Municípios", "items": ["interesse local", "lei orgânica 2/3", "SV 38 e 49"]},
        {"label": "DF", "items": ["sem Municípios", "União mantém polícias", "SV 39"]},
    ],
}

QUIZ = quiz([
    ("C", "A competência legislativa privativa da União pode ser delegada aos estados, por lei complementar, para questões específicas.",
     "Art. 22, parágrafo único."),
    ("E", "Os municípios integram o rol de entes com competência legislativa concorrente previsto no art. 24 da Constituição.",
     "O art. 24 menciona apenas União, estados e Distrito Federal."),
    ("C", "Compete à União legislar privativamente sobre a competência da Polícia Federal e da Polícia Rodoviária Federal.",
     "Art. 22, XXII."),
    ("E", "A proteção do meio ambiente é competência administrativa exclusiva da União.",
     "É competência comum de todos os entes (art. 23, VI)."),
    ("C", "Compete à União executar os serviços de polícia marítima, aeroportuária e de fronteiras.",
     "Art. 21, XXII."),
    ("E", "Os estados podem instituir regiões metropolitanas por meio de lei ordinária estadual.",
     "Exige-se lei complementar estadual (art. 25, § 3º)."),
    ("C", "A lei orgânica do município deve ser votada em dois turnos, com interstício mínimo de dez dias, e aprovada por dois terços dos membros da Câmara Municipal.",
     "Art. 29, caput."),
    ("E", "O Distrito Federal organiza e mantém, com recursos próprios, a sua polícia civil e a sua polícia militar.",
     "A União organiza e mantém as polícias do DF (art. 21, XIV)."),
    ("C", "O governador de território federal é nomeado pelo Presidente da República, após aprovação do Senado Federal.",
     "Arts. 52, III, c, e 84, XIV."),
    ("E", "Legislar sobre direito urbanístico é competência privativa da União.",
     "É competência concorrente (art. 24, I)."),
], 10)

SOURCES = [
    "Constituição da República Federativa do Brasil de 1988, arts. 18 a 33.",
    "Supremo Tribunal Federal: Súmulas Vinculantes 38, 39 e 49.",
    SRC_R,
]
