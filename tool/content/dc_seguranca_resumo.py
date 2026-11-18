# -*- coding: utf-8 -*-
"""Direito Constitucional · Segurança Pública (art. 144) — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "dc-seguranca-01", "DC", "DC-13", "resumo", "Segurança Pública (art. 144)", "Direito Constitucional · Defesa do Estado",
    "constitucional_seguranca", "Constitucional_Seguranca_Publica_RESUMO.pdf", None, ["Segurança", "Pública"], RES_SUB,
    RES_ITEMS("órgãos, atribuições, guardas e jurisprudência"),
    "Tópico do edital: Segurança Pública (art. 144) — Direito Constitucional",
    "Base: Constituição Federal de 1988 e jurisprudência do STF.", 35)

THEORY = [
    exam("O que a banca cobra",
         "A **letra do art. 144**: missão de cada órgão, **subordinação**, guardas municipais e os julgados do STF."),
    h2("1. Caput"),
    bl("Segurança pública: **dever do Estado**, **direito e responsabilidade de todos**; preserva a **ordem pública** e a **incolumidade** das "
       "pessoas e do patrimônio.",
       "Órgãos: **PF, PRF, PFF, polícias civis, PMs e bombeiros, polícias penais** (EC 104/2019). Rol **taxativo** (STF).",
       "Polícias do DF: **mantidas pela União**, **subordinadas ao Governador do DF**."),
    h2("2. União"),
    bl("**PF**: crimes contra **ordem política e social** e contra **bens, serviços e interesses da União, autarquias e empresas públicas** "
       "(não SEM); crimes de **repercussão interestadual ou internacional** (Lei 10.446/2002); **tráfico, contrabando e descaminho** (sem "
       "exclusividade); polícia **marítima, aeroportuária e de fronteiras**; **polícia judiciária da União com exclusividade**.",
       "**PRF**: patrulhamento ostensivo das **rodovias** federais. **PFF**: das **ferrovias** federais."),
    h2("3. Estados"),
    bl("**Polícia civil**: dirigida por **delegado de carreira**; polícia judiciária e apuração de infrações, **exceto militares**, ressalvada a União.",
       "**PM**: **polícia ostensiva** e **preservação da ordem pública**. **Bombeiros**: **defesa civil**.",
       "**Polícia penal**: **segurança dos estabelecimentos penais**.",
       "PM e bombeiros: **forças auxiliares e reserva do Exército**, mas subordinados ao **Governador**, como as polícias civis e penais."),
    h2("4. Municípios e jurisprudência"),
    bl("Municípios **podem** criar **guardas** para proteger **bens, serviços e instalações** (Lei 13.022/2014).",
       "STF: guardas **integram** a segurança pública (ADPF 995) e podem fazer **policiamento ostensivo e comunitário**, sem **investigar** (Tema 656).",
       "Remuneração dos policiais: **subsídio**. Segurança viária: **educação, engenharia e fiscalização** de trânsito.",
       "Greve: **vedada** aos policiais civis (STF).",
       "**PEC 18/2025** aprovada pelo Congresso em novembro de 2026, **aguardando promulgação**: Susp na Constituição, mais atribuições para PF e "
       "PRF, polícia municipal. Até promulgar, vale o texto atual."),
]

SUMMARY = [
    h2("Quadro rápido"),
    tb(["Órgão", "Missão"], [0.32, 0.68], [
        ("PF", "Polícia judiciária da União (exclusiva); tráfico, contrabando"),
        ("PF", "Polícia marítima, aeroportuária e de fronteiras"),
        ("PRF", "Patrulhamento ostensivo das rodovias federais"),
        ("PFF", "Patrulhamento ostensivo das ferrovias federais"),
        ("Polícia civil", "Polícia judiciária, exceto crimes militares"),
        ("Polícia militar", "Polícia ostensiva e ordem pública"),
        ("Bombeiros", "Defesa civil"),
        ("Polícia penal", "Segurança dos estabelecimentos penais"),
        ("Guarda municipal", "Bens, serviços e instalações do Município"),
        ("Agentes de trânsito", "Segurança viária"),
    ]),
    h2("Leve para a prova"),
    bl("Segurança: **dever** do Estado, **responsabilidade** de todos.",
       "Exclusividade da PF: só **polícia judiciária da União**.",
       "SEM federal **não** atrai a PF.",
       "Ferrovia: **PFF**, não PRF.",
       "Polícia civil **não** apura crime militar.",
       "Bombeiro: **defesa civil**.",
       "PM obedece ao **Governador**.",
       "Polícias do DF: **União mantém**, Governador comanda.",
       "Guarda: **faculdade** do Município.",
       "Guarda **não** investiga."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "SEGURANÇA PÚBLICA", "rootSub": "art. 144",
    "left": [
        {"label": "Caput", "items": ["dever do Estado", "responsabilidade de todos", "ordem e incolumidade"]},
        {"label": "Polícia Federal", "items": ["bens da União", "tráfico, contrabando", "judiciária da União"]},
        {"label": "PF: fronteiras", "items": ["marítima", "aeroportuária", "de fronteiras"]},
        {"label": "PRF e PFF", "items": ["rodovias federais", "ferrovias federais", "patrulha ostensiva"]},
        {"label": "Polícia civil", "items": ["delegado de carreira", "polícia judiciária", "exceto militares"]},
    ],
    "right": [
        {"label": "PM e bombeiros", "items": ["ostensiva, ordem", "defesa civil", "reserva do Exército"]},
        {"label": "Polícia penal", "items": ["EC 104/2019", "estabelecimentos penais", "sistema penal"]},
        {"label": "Subordinação", "items": ["Governadores", "DF: União mantém", "SV 39"]},
        {"label": "Municípios", "items": ["guardas: faculdade", "ostensivo comunitário", "sem investigação"]},
        {"label": "Outros pontos", "items": ["subsídio", "segurança viária", "PEC 18/2025"]},
    ],
}

QUIZ = quiz([
    ("C", "A segurança pública é exercida para a preservação da ordem pública e da incolumidade das pessoas e do patrimônio.",
     "Caput do art. 144."),
    ("E", "A Polícia Federal exerce, com exclusividade, as funções de polícia judiciária dos estados.",
     "A PF exerce com exclusividade a polícia judiciária da União."),
    ("C", "Cabe à Polícia Federal prevenir e reprimir o contrabando e o descaminho, sem prejuízo da ação fazendária.",
     "Art. 144, § 1º, II."),
    ("E", "A Polícia Ferroviária Federal integra a estrutura da Polícia Rodoviária Federal.",
     "São órgãos distintos, com incisos próprios no caput do art. 144."),
    ("C", "As polícias civis não têm atribuição para apurar infrações penais militares.",
     "Art. 144, § 4º, parte final."),
    ("E", "Às polícias militares cabem as funções de polícia judiciária e a apuração de infrações penais comuns.",
     "Às PMs cabem a polícia ostensiva e a preservação da ordem pública."),
    ("C", "Os corpos de bombeiros militares executam atividades de defesa civil, além das atribuições definidas em lei.",
     "Art. 144, § 5º."),
    ("E", "As polícias penais estaduais subordinam-se ao Ministro da Justiça.",
     "Subordinam-se aos governadores (§ 6º)."),
    ("C", "A remuneração dos servidores policiais integrantes dos órgãos de segurança pública é fixada na forma de subsídio.",
     "Art. 144, § 9º."),
    ("E", "As guardas municipais destinam-se, conforme a Constituição, à apuração de infrações penais de menor potencial ofensivo ocorridas no município.",
     "Destinam-se à proteção de bens, serviços e instalações do município."),
], 10)

SOURCES = [
    "Constituição da República Federativa do Brasil de 1988, art. 144.",
    "Supremo Tribunal Federal: ADPF 995; RE 608.588 (Tema 656); ARE 654.432.",
    SRC_R,
]
