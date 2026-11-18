# -*- coding: utf-8 -*-
"""Direito Constitucional · Organização político-administrativa do Estado (arts. 18 a 33) — MATERIAL APROFUNDADO."""
from common import *

MATERIAL = material(
    "dc-organizacao-02", "DC", "DC-07", "aprofundado", "Organização político-administrativa do Estado (arts. 18 a 33)",
    "Direito Constitucional · Organização do Estado",
    "constitucional_organizacao_aprofundado", "Constitucional_Organizacao_do_Estado_APROFUNDADO.pdf", None, ["Organização", "do Estado"],
    ["Federação, criação de Estados e Municípios, repartição de competências, Estados,", "Municípios, DF e Territórios, com 20 questões no estilo Cebraspe."],
    [("01", "Federação", "entes autônomos, vedações, bens"),
     ("02", "Criação de entes", "Estados, Municípios e Territórios"),
     ("03", "Competências", "arts. 21 a 24 e as polícias"),
     ("04", "Entes em espécie", "Estados, Municípios, DF e Territórios"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Organização político-administrativa do Estado (arts. 18 a 33) — Direito Constitucional",
    "Base: Constituição Federal de 1988, jurisprudência do STF e doutrina.", 150)

THEORY = [
    exam("Como estudar este material",
         "O ponto mais cobrado é a **repartição de competências** (arts. 21 a 24). Aprenda a diferença entre competência **administrativa** "
         "(fazer) e **legislativa** (legislar), e entre **exclusiva, privativa, comum e concorrente**. Em provas policiais, a banca adora "
         "perguntar **quem legisla sobre as polícias** e **quem organiza as polícias do DF**."),

    h2("1. A federação brasileira"),
    key("Texto da Constituição",
        "Art. 18. A organização político-administrativa da República Federativa do Brasil compreende a **União**, os **Estados**, o **Distrito "
        "Federal** e os **Municípios**, todos **autônomos**, nos termos desta Constituição."),
    bl("**Brasília** é a Capital Federal (§ 1º).",
       "Os **Territórios Federais** integram a **União**: não são entes federativos. Sua criação, transformação em Estado ou reintegração ao "
       "Estado de origem é regulada em **lei complementar** (§ 2º).",
       "A **soberania** pertence à República Federativa do Brasil; os entes têm **autonomia**: auto-organização, autogoverno, "
       "autoadministração e autolegislação."),
    h3("Vedações aos entes (art. 19)"),
    bl("Estabelecer cultos religiosos ou igrejas, subvencioná-los, embaraçar-lhes o funcionamento ou manter com eles relações de dependência "
       "ou aliança, **ressalvada a colaboração de interesse público** (o Estado é **laico**).",
       "**Recusar fé aos documentos públicos.**",
       "Criar **distinções entre brasileiros** ou **preferências entre si**."),
    h3("Bens da União (art. 20), em destaque"),
    bl("Mar territorial, terrenos de marinha, recursos da plataforma continental e da zona econômica exclusiva.",
       "Lagos e rios em terrenos da União ou que **banhem mais de um Estado** ou sirvam de **limite com outros países**.",
       "**Recursos minerais**, inclusive os do subsolo, e os **potenciais de energia hidráulica**.",
       "**Cavidades naturais subterrâneas** e **sítios arqueológicos e pré-históricos**.",
       "**Terras tradicionalmente ocupadas pelos índios**.",
       "A **faixa de fronteira** tem até **150 km** de largura e é fundamental para a defesa do território (§ 2º)."),

    h2("2. Criação, fusão e desmembramento de entes"),
    tb(["Ente", "Requisitos"], [0.18, 0.82], [
        ("**Estados**", "**Plebiscito** da população diretamente interessada + **lei complementar** do Congresso Nacional (ouvidas as Assembleias Legislativas)."),
        ("**Municípios**", "**Lei estadual**, dentro do período fixado em **lei complementar federal**, após **Estudos de Viabilidade Municipal** "
                           "divulgados e **plebiscito** das populações dos Municípios envolvidos."),
        ("**Territórios**", "**Lei complementar** federal."),
    ]),
    nt("A lei complementar federal que fixa o período para criar Municípios **ainda não foi editada**. Por isso, Municípios criados depois "
       "da EC 15/1996 sem ela eram inconstitucionais; a **EC 57/2008** convalidou os criados até **31/12/2006**."),

    h2("3. Repartição de competências"),
    p("A Constituição reparte as competências pelo **princípio da predominância do interesse**: o que é de interesse **geral** fica com a "
      "**União**; o **regional**, com os **Estados**; o **local**, com os **Municípios**. O **DF** acumula as competências estaduais e municipais."),
    tb(["Artigo", "Tipo", "Quem", "Delegável?"], [0.1, 0.36, 0.3, 0.24], [
        ("21", "**Exclusiva** (administrativa: fazer)", "União", "**Não**"),
        ("22", "**Privativa** (legislativa: legislar)", "União", "**Sim**, por **lei complementar**, aos Estados, sobre questões específicas"),
        ("23", "**Comum** (administrativa)", "União, Estados, DF e Municípios", "—"),
        ("24", "**Concorrente** (legislativa)", "União, Estados e DF (**não** os Municípios)", "—"),
    ]),
    h3("Art. 21: competência exclusiva da União (seleção)"),
    bl("Manter relações com Estados estrangeiros; declarar a guerra e celebrar a paz; assegurar a defesa nacional.",
       "Decretar o **estado de sítio**, o **estado de defesa** e a **intervenção federal**.",
       "Emitir moeda; manter o serviço postal e o correio aéreo nacional.",
       "Autorizar e fiscalizar a produção e o comércio de **material bélico**.",
       "**Organizar e manter** a **polícia civil**, a **polícia penal**, a **polícia militar** e o **corpo de bombeiros militar do DF** (XIV).",
       "Executar os serviços de **polícia marítima, aeroportuária e de fronteiras** (XXII)."),
    h3("Art. 22: competência privativa da União para legislar (seleção)"),
    key("Mnemônico: CAPACETE DE PM",
        "Direito **C**ivil, **A**grário, **P**enal, **A**eronáutico, **C**omercial, **E**leitoral, do **T**rabalho, **E**spacial, "
        "**D**esapropriação, **P**rocessual e **M**arítimo."),
    bl("Trânsito e transporte; águas, energia, informática e telecomunicações; registros públicos; nacionalidade e cidadania.",
       "**Normas gerais** de organização, efetivos, material bélico, garantias, convocação, mobilização, inatividades e pensões das **polícias "
       "militares** e dos **corpos de bombeiros militares** (XXI).",
       "**Competência da polícia federal e das polícias rodoviária e ferroviária federais** (XXII).",
       "Material bélico; diretrizes e bases da educação; seguridade social; normas gerais de licitação e contratação.",
       "**Proteção e tratamento de dados pessoais** (XXX, EC 115/2022)."),
    nt("Súmulas Vinculantes ligadas ao tema: **SV 46** (definição dos crimes de responsabilidade e normas de processo e julgamento são da "
       "União); **SV 39** (compete privativamente à União legislar sobre **vencimentos** dos membros das **polícias civil e militar e do "
       "corpo de bombeiros militar do DF**)."),
    h3("Art. 23: competência comum (seleção)"),
    bl("Zelar pela guarda da Constituição, das leis e das instituições democráticas e conservar o patrimônio público.",
       "Cuidar da saúde e da assistência pública; proteger documentos, obras e bens de valor histórico e cultural.",
       "Proteger o **meio ambiente**, combater a poluição e preservar florestas, fauna e flora.",
       "Combater as causas da pobreza; estabelecer política de educação para a **segurança do trânsito**.",
       "**Lei complementar** fixa normas de **cooperação** entre os entes."),
    h3("Art. 24: competência concorrente"),
    key("Mnemônico: PUFETO",
        "Direito **P**enitenciário, **U**rbanístico, **F**inanceiro, **E**conômico, **T**ributário e **O**rçamento. Também: juntas comerciais, "
        "custas forenses, produção e consumo, proteção ao meio ambiente, educação e cultura, proteção à infância e à juventude, procedimentos em "
        "matéria processual e **organização, garantias, direitos e deveres das polícias civis** (XVI)."),
    tb(["Regra do art. 24", "Conteúdo"], [0.28, 0.72], [
        ("§ 1º", "A **União** edita **normas gerais**."),
        ("§ 2º", "Os **Estados** têm competência **suplementar**."),
        ("§ 3º", "Inexistindo lei federal de normas gerais, os Estados exercem a competência legislativa **plena**."),
        ("§ 4º", "A superveniência de lei federal **suspende a eficácia** (não revoga) da lei estadual, **no que lhe for contrário**."),
    ]),
    trap("Pegadinha: Direito Penal × Penitenciário",
         "Direito **Penal** e **Processual** são **privativos** da União (art. 22). Direito **Penitenciário** e **procedimentos** em matéria "
         "processual são **concorrentes** (art. 24). E o Município não aparece no art. 24, embora possa **suplementar** a legislação federal e "
         "estadual no que couber (art. 30, II)."),

    h2("4. Estados (arts. 25 a 28)"),
    bl("Organizam-se e regem-se pelas **Constituições** e leis que adotarem, observados os princípios da Constituição Federal.",
       "Têm a competência **residual** (remanescente): o que não lhes for vedado.",
       "Exploram diretamente, ou por concessão, os serviços locais de **gás canalizado** (vedada a medida provisória para regulamentá-los).",
       "Podem instituir **regiões metropolitanas**, aglomerações urbanas e microrregiões por **lei complementar estadual**.",
       "**Deputados estaduais** (art. 27): o **triplo** da representação do Estado na Câmara dos Deputados; atingido o número de **36**, "
       "acrescem-se tantos quantos forem os deputados federais acima de **12**.",
       "Mandato de **4 anos** para deputados estaduais e governador; aplicam-se aos deputados estaduais as regras de imunidades dos federais."),

    h2("5. Municípios (arts. 29 a 31)"),
    bl("Regem-se por **lei orgânica**, votada em **dois turnos**, com interstício mínimo de **10 dias**, e aprovada por **2/3** dos membros da "
       "Câmara Municipal.",
       "Competem-lhes legislar sobre **assuntos de interesse local**, suplementar a legislação federal e estadual no que couber e prestar os "
       "serviços públicos de interesse local, incluído o **transporte coletivo**, que tem caráter essencial.",
       "**SV 38**: o Município é competente para fixar o **horário de funcionamento** de estabelecimento comercial. Já o horário de "
       "funcionamento **bancário** é assunto da **União**.",
       "**SV 49**: ofende a livre concorrência lei municipal que impede a instalação de estabelecimentos comerciais do **mesmo ramo** em "
       "determinada área.",
       "**Fiscalização** (art. 31): controle externo pela **Câmara Municipal**, com auxílio dos Tribunais de Contas dos Estados ou dos "
       "Municípios, onde houver. O parecer prévio sobre as contas do prefeito só deixa de prevalecer por **2/3** da Câmara. É **vedada a "
       "criação** de novos Tribunais, Conselhos ou órgãos de Contas **Municipais**."),
    nt("Os Municípios **não têm Poder Judiciário** próprio nem **Ministério Público** próprio, e **não elegem representantes** para o Senado."),

    h2("6. Distrito Federal e Territórios (arts. 32 e 33)"),
    bl("O **DF** é **vedado dividir-se em Municípios**. Rege-se por **lei orgânica** (dois turnos, 10 dias, 2/3 da Câmara Legislativa).",
       "O DF acumula as competências legislativas **reservadas aos Estados e Municípios**.",
       "A **polícia civil**, a **polícia penal**, a **polícia militar** e o **corpo de bombeiros militar** do DF são **organizados e mantidos "
       "pela União**; **lei federal** dispõe sobre sua utilização pelo Governo do DF (art. 32, § 4º).",
       "O **Poder Judiciário** e o **Ministério Público** do DF também são organizados e mantidos pela União.",
       "**Territórios**: podem ser divididos em Municípios; o **governador** é nomeado pelo **Presidente** após aprovação do **Senado**; "
       "cada Território elege **4 deputados federais** e **nenhum senador**; com mais de **100 mil habitantes**, terá órgãos judiciários, "
       "Ministério Público e Defensoria Pública federais."),
]

QUIZ = quiz([
    ("C", "Os territórios federais integram a União e não são entes federativos.",
     "Art. 18, § 2º."),
    ("E", "Os municípios não têm autonomia política, pois estão subordinados aos estados em que se localizam.",
     "Todos os entes do art. 18 são autônomos; não há hierarquia entre eles."),
    ("C", "A incorporação, subdivisão ou desmembramento de estados depende de aprovação da população diretamente interessada, por plebiscito, e do Congresso Nacional, por lei complementar.",
     "Art. 18, § 3º."),
    ("E", "A criação de municípios é feita por lei complementar federal, após plebiscito da população do município de origem.",
     "A criação se faz por lei estadual, no período fixado por lei complementar federal, após estudos de viabilidade e plebiscito das populações envolvidas."),
    ("C", "A competência exclusiva da União, prevista no art. 21, é indelegável.",
     "Só a competência privativa do art. 22 admite delegação por lei complementar."),
    ("E", "Compete aos estados, concorrentemente com a União, legislar sobre direito penal e processual.",
     "Direito penal e processual são de competência privativa da União (art. 22, I)."),
    ("C", "Legislar sobre direito penitenciário é competência concorrente da União, dos estados e do Distrito Federal.",
     "Art. 24, I."),
    ("E", "No âmbito da competência concorrente, a superveniência de lei federal sobre normas gerais revoga a lei estadual que dispuser em sentido contrário.",
     "A lei federal superveniente suspende a eficácia da lei estadual no que lhe for contrário; não a revoga."),
    ("C", "Compete aos municípios legislar sobre assuntos de interesse local.",
     "Art. 30, I."),
    ("E", "É permitida a divisão do Distrito Federal em municípios, desde que aprovada pela Câmara Legislativa.",
     "O art. 32 veda a divisão do DF em municípios."),

    ("C", "Compete à União organizar e manter a polícia civil, a polícia penal, a polícia militar e o corpo de bombeiros militar do Distrito Federal.",
     "Art. 21, XIV."),
    ("E", "Lei distrital pode fixar os vencimentos dos integrantes da Polícia Civil do Distrito Federal, uma vez que o DF possui autonomia para organizar seus órgãos de segurança pública.",
     "SV 39: compete privativamente à União legislar sobre vencimentos das polícias civil e militar e do corpo de bombeiros do DF."),
    ("C", "Compete privativamente à União legislar sobre normas gerais de organização, efetivos, material bélico, garantias, convocação e mobilização das polícias militares e dos corpos de bombeiros militares.",
     "Art. 22, XXI."),
    ("E", "Compete à União legislar privativamente sobre organização, garantias, direitos e deveres das polícias civis.",
     "Essa matéria é de competência concorrente (art. 24, XVI)."),
    ("C", "Lei municipal pode fixar o horário de funcionamento dos estabelecimentos comerciais localizados no município.",
     "SV 38."),
    ("E", "Lei municipal pode proibir a instalação de farmácias a menos de quinhentos metros de outra já existente, como forma de organizar o comércio local.",
     "SV 49: a restrição ofende o princípio da livre concorrência."),
    ("C", "Considere que um estado tenha dezoito deputados federais. Nesse caso, a Assembleia Legislativa desse estado terá quarenta e dois deputados estaduais.",
     "O triplo de 12 é 36; os 6 deputados federais acima de 12 se somam: 36 + 6 = 42."),
    ("E", "Os municípios podem criar tribunais de contas municipais, desde que o façam por lei orgânica aprovada por dois terços da Câmara Municipal.",
     "O art. 31, § 4º, veda a criação de tribunais, conselhos ou órgãos de contas municipais."),
    ("C", "Inexistindo lei federal sobre normas gerais em matéria de competência concorrente, os estados exercerão a competência legislativa plena para atender a suas peculiaridades.",
     "Art. 24, § 3º."),
    ("E", "Cada território federal elege três senadores e quatro deputados federais.",
     "Territórios elegem quatro deputados federais, mas não elegem senadores."),
], 20)

SOURCES = [
    "Constituição da República Federativa do Brasil de 1988, arts. 18 a 33, 45 e 84; EC 57/2008, 104/2019 e 115/2022.",
    "Supremo Tribunal Federal: Súmulas Vinculantes 38, 39, 46 e 49.",
    "Doutrina de referência: Lenza, Direito constitucional; Mendes e Branco, Curso de direito constitucional.",
    SRC_A,
]
