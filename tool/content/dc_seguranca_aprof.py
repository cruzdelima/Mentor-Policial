# -*- coding: utf-8 -*-
"""Direito Constitucional · Segurança Pública (art. 144) — MATERIAL APROFUNDADO."""
from common import *

MATERIAL = material(
    "dc-seguranca-02", "DC", "DC-13", "aprofundado", "Segurança Pública (art. 144)", "Direito Constitucional · Defesa do Estado",
    "constitucional_seguranca_aprofundado", "Constitucional_Seguranca_Publica_APROFUNDADO.pdf", None, ["Segurança", "Pública"],
    ["Órgãos do art. 144, atribuições de cada polícia, guardas municipais, segurança viária,", "jurisprudência do STF e a PEC 18/2025, com 20 questões."],
    [("01", "Caput", "dever do Estado e rol de órgãos"),
     ("02", "Polícias da União", "PF, PRF e Polícia Ferroviária Federal"),
     ("03", "Polícias dos Estados", "civil, militar, bombeiros e penal"),
     ("04", "Municípios e STF", "guardas, segurança viária, jurisprudência, PEC 18"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Segurança Pública (art. 144) — Direito Constitucional",
    "Base: Constituição Federal de 1988, Leis 13.022/2014 e 13.675/2018 e jurisprudência do STF.", 150)

THEORY = [
    exam("Como estudar este material",
         "É o artigo da **sua futura profissão**: a banca o cobra em praticamente toda prova policial, quase sempre pela **letra da Constituição**. "
         "Decore o **caput**, a **missão de cada órgão** e a quem cada um se **subordina**. Atenção à **PEC 18/2025** (PEC da Segurança Pública), "
         "aprovada pelo Congresso e aguardando promulgação: veja o quadro da seção 6."),

    h2("1. O caput do art. 144"),
    key("Texto da Constituição",
        "Art. 144. A segurança pública, **dever do Estado**, **direito e responsabilidade de todos**, é exercida para a **preservação da ordem "
        "pública** e da **incolumidade das pessoas e do patrimônio**, através dos seguintes órgãos: I – **polícia federal**; II – **polícia "
        "rodoviária federal**; III – **polícia ferroviária federal**; IV – **polícias civis**; V – **polícias militares** e **corpos de "
        "bombeiros militares**; VI – **polícias penais** federal, estaduais e distrital."),
    bl("A segurança pública é **dever do Estado**, mas também **direito e responsabilidade de todos**.",
       "As **polícias penais** foram incluídas pela **EC 104/2019**.",
       "Para o STF, o rol de órgãos do art. 144 é **taxativo**: os Estados **não podem criar** outros órgãos policiais fora desse modelo.",
       "As **guardas municipais** não estão nos incisos do caput: aparecem no § 8º. Mesmo assim, o STF reconhece que **integram o Sistema de "
       "Segurança Pública** (ADPF 995)."),
    tb(["Órgão", "Mantido por", "Subordinado a"], [0.36, 0.3, 0.34], [
        ("PF, PRF e Polícia Ferroviária Federal", "**União**", "Poder Executivo federal"),
        ("Polícia penal federal", "**União**", "Poder Executivo federal"),
        ("Polícias civis, militares, bombeiros e polícias penais dos **Estados**", "**Estados**", "**Governador** do Estado"),
        ("Polícias civil, militar, penal e bombeiros do **DF**", "**União** (art. 21, XIV)", "**Governador do DF** (§ 6º)"),
    ]),
    trap("Pegadinha do Distrito Federal",
         "As polícias do DF são **organizadas e mantidas pela União**, mas **subordinam-se ao Governador do DF**. Os vencimentos delas são "
         "fixados por **lei federal** (SV 39), e a lei federal dispõe sobre sua utilização pelo Governo do DF (art. 32, § 4º)."),

    h2("2. Polícias da União"),
    h3("Polícia Federal (§ 1º)"),
    p("Instituída por lei como órgão **permanente**, organizado e mantido pela **União** e estruturado em **carreira**, destina-se a:"),
    tb(["Inciso", "Atribuição"], [0.1, 0.9], [
        ("I", "Apurar infrações penais contra a **ordem política e social** ou em detrimento de **bens, serviços e interesses da União** ou de suas "
              "**autarquias** e **empresas públicas**, assim como outras infrações cuja prática tenha **repercussão interestadual ou internacional** "
              "e exija **repressão uniforme**, segundo se dispuser em lei."),
        ("II", "**Prevenir e reprimir** o **tráfico ilícito de entorpecentes** e drogas afins, o **contrabando** e o **descaminho**, sem prejuízo da "
               "ação fazendária e de outros órgãos públicos nas respectivas áreas de competência."),
        ("III", "Exercer as funções de **polícia marítima, aeroportuária e de fronteiras**."),
        ("IV", "Exercer, **com exclusividade**, as funções de **polícia judiciária da União**."),
    ]),
    bl("A lei que define as infrações de **repercussão interestadual ou internacional** é a **Lei 10.446/2002**. Nessas hipóteses, a PF investiga "
       "**sem prejuízo** das polícias estaduais, e o processo pode correr na **Justiça Estadual**: atribuição da PF não se confunde com "
       "competência da Justiça Federal.",
       "A PF atua contra o tráfico **sem exclusividade**: as polícias estaduais também reprimem o tráfico. A exclusividade é só da **polícia "
       "judiciária da União** (inciso IV).",
       "**Sociedades de economia mista** federais (como o Banco do Brasil e a Petrobras) **não** aparecem no inciso I: crimes contra elas, em "
       "regra, são investigados pela polícia civil."),
    trap("Pegadinhas da PF",
         "“A PF exerce **com exclusividade** a repressão ao tráfico” › errado (a exclusividade é da polícia judiciária da União). “A PF apura "
         "crimes contra **sociedades de economia mista** federais” › errado. “A PF exerce as funções de polícia **marítima, aeroportuária e de "
         "fronteiras**” › certo."),
    h3("Polícia Rodoviária Federal e Polícia Ferroviária Federal (§§ 2º e 3º)"),
    bl("Ambas são órgãos **permanentes**, organizados e mantidos pela **União** e estruturados em **carreira**.",
       "**PRF**: destina-se, na forma da lei, ao **patrulhamento ostensivo das rodovias federais**.",
       "**Polícia Ferroviária Federal**: destina-se, na forma da lei, ao **patrulhamento ostensivo das ferrovias federais**."),

    h2("3. Polícias dos Estados e do DF"),
    tb(["Órgão", "Atribuição constitucional"], [0.26, 0.74], [
        ("**Polícias civis** (§ 4º)", "Dirigidas por **delegados de polícia de carreira**, incumbem-lhes, **ressalvada a competência da União**, as funções de "
                                      "**polícia judiciária** e a **apuração de infrações penais**, **exceto as militares**."),
        ("**Polícias militares** (§ 5º)", "**Polícia ostensiva** e **preservação da ordem pública**."),
        ("**Corpos de bombeiros militares** (§ 5º)", "Além das atribuições definidas em lei, a execução de atividades de **defesa civil**."),
        ("**Polícias penais** (§ 5º-A)", "Vinculadas ao órgão administrador do sistema penal da unidade federativa, cabe-lhes a **segurança dos estabelecimentos penais**."),
    ]),
    key("Subordinação (§ 6º)",
        "As **polícias militares** e os **corpos de bombeiros militares**, **forças auxiliares e reserva do Exército**, subordinam-se, juntamente "
        "com as **polícias civis** e as **polícias penais estaduais e distrital**, aos **Governadores** dos Estados, do DF e dos Territórios."),
    bl("As PMs e os bombeiros são **forças auxiliares e reserva do Exército**, mas a subordinação é ao **Governador**, não ao Comandante do Exército.",
       "Os **militares dos Estados** seguem regras do art. 42 e, no que couber, do art. 142 (proibição de greve e sindicalização, por exemplo).",
       "A **apuração de crimes militares** cabe à própria corporação militar (inquérito policial militar), e não à polícia civil.",
       "O STF entende que a lavratura do **termo circunstanciado de ocorrência** não é ato exclusivo da polícia judiciária e pode ser feita por "
       "outros órgãos de segurança pública, como a PM e a PRF."),

    h2("4. Municípios, remuneração e segurança viária"),
    bl("**Guardas municipais** (§ 8º): os Municípios **poderão** constituí-las (é faculdade), destinadas à **proteção de seus bens, serviços e "
       "instalações**, conforme dispuser a lei. O Estatuto Geral das Guardas Municipais é a **Lei 13.022/2014**.",
       "**§ 7º**: a lei disciplinará a organização e o funcionamento dos órgãos de segurança pública. Essa lei é a **Lei 13.675/2018**, que criou o "
       "**Sistema Único de Segurança Pública (Susp)**.",
       "**§ 9º**: a remuneração dos servidores policiais é fixada por **subsídio** (parcela única).",
       "**§ 10** (EC 82/2014): a **segurança viária** compreende **educação, engenharia e fiscalização de trânsito** e compete, no âmbito dos "
       "Estados, do DF e dos Municípios, aos respectivos órgãos executivos e seus **agentes de trânsito**, estruturados em carreira."),
    tb(["Guardas municipais no STF", "Entendimento"], [0.28, 0.72], [
        ("ADPF 995 (2023)", "As guardas municipais **integram o Sistema de Segurança Pública**."),
        ("RE 608.588, Tema 656 (2025)", "É constitucional lei municipal que atribua às guardas **ações de segurança urbana**, inclusive **policiamento ostensivo "
                                        "e comunitário**, respeitadas as atribuições dos demais órgãos do art. 144 e **vedada** qualquer atividade de **polícia "
                                        "judiciária** (investigação). A atuação fica sujeita ao **controle externo do Ministério Público**."),
    ]),

    h2("5. Jurisprudência útil ao policial"),
    tb(["Tema", "Entendimento do STF"], [0.26, 0.74], [
        ("Greve", "É **vedado** o exercício do direito de greve, sob qualquer forma, aos **policiais civis** e a todos os servidores que atuam "
                  "**diretamente na segurança pública** (ARE 654.432)."),
        ("Entrada em domicílio", "Sem mandado, só com **fundadas razões** de flagrante, justificadas depois (RE 603.616)."),
        ("Algemas", "Só em caso de resistência, fundado receio de fuga ou perigo, com justificativa **por escrito** (SV 11)."),
        ("Responsabilidade", "Dano causado por policial em serviço: o **Estado** responde **objetivamente** (art. 37, § 6º)."),
        ("Investigação pelo MP", "O MP pode investigar diretamente; a PF tem **exclusividade** apenas da **polícia judiciária da União**."),
    ]),

    h2("6. PEC 18/2025: a PEC da Segurança Pública"),
    key("Situação em novembro de 2026",
        "A PEC foi aprovada pela Câmara (março de 2026) e pelo Senado, em segundo turno, em **3 de novembro de 2026**, e **aguarda promulgação** "
        "pelo Congresso. **Até a promulgação, vale o texto atual do art. 144**, que é o estudado neste material. Quando a emenda for "
        "promulgada, este PDF será atualizado no app."),
    bl("Leva para a Constituição o **Sistema Único de Segurança Pública (Susp)**, hoje previsto na Lei 13.675/2018, com cooperação federativa "
       "entre os órgãos.",
       "Cria o **Sistema de Políticas Penais**.",
       "Amplia a atuação da **Polícia Federal** contra o **crime organizado** de atuação interestadual ou internacional.",
       "Estende o patrulhamento da **PRF** a **ferrovias e hidrovias federais**.",
       "Abre caminho para os Municípios terem **polícia municipal** de caráter ostensivo e comunitário.",
       "Endurece o tratamento de **líderes de facções e milícias** (presídios de segurança máxima, regras de progressão de regime, perda de bens) "
       "e protege recursos dos fundos de segurança pública e penitenciário."),
    nt("Banca e edital: provas com edital publicado **antes** da promulgação costumam cobrar o texto anterior; depois dela, o texto novo. "
       "Confira sempre a data do edital."),
]

QUIZ = quiz([
    ("C", "A segurança pública é dever do Estado, direito e responsabilidade de todos.",
     "É a letra do caput do art. 144."),
    ("E", "As guardas municipais estão expressamente arroladas entre os incisos do caput do art. 144 da Constituição como órgãos de segurança pública.",
     "Os incisos listam PF, PRF, PFF, polícias civis, PMs e bombeiros e polícias penais; as guardas aparecem no § 8º."),
    ("C", "As polícias penais federal, estaduais e distrital foram incluídas no rol de órgãos de segurança pública por emenda constitucional.",
     "EC 104/2019."),
    ("E", "Compete à Polícia Federal exercer, com exclusividade, a prevenção e a repressão ao tráfico ilícito de entorpecentes.",
     "A exclusividade refere-se apenas às funções de polícia judiciária da União."),
    ("C", "Compete à Polícia Federal exercer as funções de polícia marítima, aeroportuária e de fronteiras.",
     "Art. 144, § 1º, III."),
    ("E", "A Polícia Rodoviária Federal destina-se ao patrulhamento ostensivo das rodovias e ferrovias federais.",
     "As ferrovias federais cabem à Polícia Ferroviária Federal (§ 3º)."),
    ("C", "Às polícias civis, dirigidas por delegados de polícia de carreira, incumbem, ressalvada a competência da União, as funções de polícia judiciária e a apuração de infrações penais, exceto as militares.",
     "Art. 144, § 4º."),
    ("E", "Cabe aos corpos de bombeiros militares a polícia ostensiva e a preservação da ordem pública.",
     "Essa é a missão das polícias militares; aos bombeiros cabe, além do previsto em lei, a defesa civil."),
    ("C", "As polícias militares e os corpos de bombeiros militares são forças auxiliares e reserva do Exército.",
     "Art. 144, § 6º."),
    ("E", "Os municípios são obrigados a constituir guardas municipais, destinadas à proteção de seus bens, serviços e instalações.",
     "A Constituição diz que os municípios poderão constituí-las: é faculdade."),

    ("C", "Crime de furto de equipamentos de uma agência dos Correios, empresa pública federal, insere-se na atribuição investigativa da Polícia Federal.",
     "Infrações em detrimento de bens de empresa pública federal são atribuição da PF (§ 1º, I)."),
    ("E", "Crime de roubo praticado contra agência do Banco do Brasil, sociedade de economia mista federal, é atribuição constitucional da Polícia Federal, por envolver patrimônio da União.",
     "Sociedades de economia mista não constam do § 1º, I; em regra, a atribuição é da polícia civil."),
    ("C", "As polícias civil e militar do Distrito Federal são organizadas e mantidas pela União, mas subordinam-se ao governador do Distrito Federal.",
     "Arts. 21, XIV, e 144, § 6º."),
    ("E", "As polícias militares, por serem forças auxiliares e reserva do Exército, subordinam-se ao Comandante do Exército em tempo de paz.",
     "Subordinam-se aos governadores (§ 6º)."),
    ("C", "Às polícias penais, vinculadas ao órgão administrador do sistema penal da unidade federativa, cabe a segurança dos estabelecimentos penais.",
     "Art. 144, § 5º-A."),
    ("E", "Conforme o STF, lei municipal pode atribuir à guarda municipal a investigação de crimes ocorridos no município, por meio de inquérito próprio, desde que comunicada à polícia civil.",
     "No Tema 656, o STF admitiu policiamento ostensivo e comunitário, mas vedou qualquer atividade de polícia judiciária."),
    ("C", "Segundo o STF, as guardas municipais integram o Sistema de Segurança Pública.",
     "ADPF 995."),
    ("E", "A Constituição prevê que a remuneração dos servidores policiais integrantes dos órgãos do art. 144 seja composta de vencimento básico acrescido de gratificações por desempenho.",
     "O § 9º determina a remuneração por subsídio, em parcela única."),
    ("C", "A segurança viária compreende a educação, a engenharia e a fiscalização de trânsito e compete, no âmbito dos estados, do DF e dos municípios, aos respectivos órgãos executivos e seus agentes de trânsito, estruturados em carreira.",
     "Art. 144, § 10 (EC 82/2014)."),
    ("E", "Conforme a jurisprudência do STF, os policiais civis podem exercer o direito de greve, desde que mantido o efetivo mínimo para os serviços essenciais.",
     "O STF vedou a greve dos policiais civis e de todos os servidores que atuam diretamente na segurança pública (ARE 654.432)."),
], 20)

SOURCES = [
    "Constituição da República Federativa do Brasil de 1988, arts. 21, XIV, 32, 37, § 6º, 42 e 144; EC 82/2014 e EC 104/2019.",
    "Leis 10.446/2002, 13.022/2014 (Estatuto Geral das Guardas Municipais) e 13.675/2018 (Susp).",
    "Supremo Tribunal Federal: ADPF 995; RE 608.588 (Tema 656); ARE 654.432 (Tema 541); RE 603.616; Súmulas Vinculantes 11 e 39.",
    "PEC 18/2025 (PEC da Segurança Pública): aprovada pelo Senado em 3/11/2026, aguardando promulgação na data deste material.",
    SRC_A,
]
