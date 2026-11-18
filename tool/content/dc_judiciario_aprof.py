# -*- coding: utf-8 -*-
"""Direito Constitucional · Poder Judiciário e funções essenciais à Justiça — MATERIAL APROFUNDADO."""
from common import *

MATERIAL = material(
    "dc-judiciario-02", "DC", "DC-11", "aprofundado", "Poder Judiciário e funções essenciais à Justiça", "Direito Constitucional · Organização dos Poderes",
    "constitucional_judiciario_aprofundado", "Constitucional_Poder_Judiciario_APROFUNDADO.pdf", None, ["Poder Judiciário", "e funções essenciais"],
    ["Garantias da magistratura, STF, STJ, CNJ, Justiça Federal e Militar, Ministério Público,", "Advocacia e Defensoria Pública, com 20 questões no estilo Cebraspe."],
    [("01", "Estrutura e garantias", "órgãos, vitaliciedade, quinto constitucional"),
     ("02", "STF e STJ", "composição, competências, súmula vinculante"),
     ("03", "Justiças especializadas", "Justiça Federal, Militar e CNJ"),
     ("04", "Funções essenciais", "MP, Advocacia Pública, Advocacia, Defensoria"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Poder Judiciário e funções essenciais à Justiça (arts. 92 a 135) — Direito Constitucional",
    "Base: Constituição Federal de 1988 e jurisprudência do STF e do STJ.", 150)

THEORY = [
    exam("Como estudar este material",
         "É matéria extensa. Para provas policiais, priorize: **garantias e vedações** dos juízes, **composição do STF e do STJ**, **quem julga "
         "quem** (foro), a **competência da Justiça Federal** (base da atuação da PF), a **Justiça Militar estadual** e as funções do **Ministério "
         "Público**, inclusive o **controle externo da atividade policial**."),

    h2("1. Estrutura e garantias"),
    p("São órgãos do Poder Judiciário (art. 92): o **STF**; o **CNJ**; o **STJ**; o **TST**; os **TRFs** e juízes federais; os tribunais e juízes "
      "do **Trabalho**, **Eleitorais** e **Militares**; e os tribunais e juízes dos **Estados e do DF**. O Judiciário tem **autonomia "
      "administrativa e financeira** (art. 99)."),
    tb(["Garantia (art. 95)", "Conteúdo"], [0.24, 0.76], [
        ("**Vitaliciedade**", "No 1º grau, adquirida após **2 anos de exercício**. Nesse período, a perda do cargo depende de deliberação do **tribunal**; "
                              "depois, só por **sentença judicial transitada em julgado**."),
        ("**Inamovibilidade**", "O juiz não pode ser removido contra a vontade, salvo por **interesse público**, pelo voto da **maioria absoluta** do tribunal ou do CNJ."),
        ("**Irredutibilidade**", "Do subsídio, ressalvados o teto e os tributos."),
    ]),
    key("Vedações aos juízes (art. 95, parágrafo único)",
        "Exercer outro cargo ou função, **salvo uma de magistério**; receber **custas** ou participação em processo; dedicar-se a atividade "
        "**político-partidária**; receber auxílios ou contribuições de pessoas e entidades, ressalvadas as exceções legais; exercer a **advocacia** "
        "no juízo ou tribunal do qual se afastou antes de **3 anos** do afastamento (**quarentena**)."),
    bl("**Ingresso** (art. 93, I): juiz substituto, por **concurso de provas e títulos**, com participação da **OAB**, exigidos bacharelado em "
       "Direito e **3 anos de atividade jurídica**.",
       "**Quinto constitucional** (art. 94): **1/5** dos lugares dos **TRFs** e dos **TJs** é composto de membros do **Ministério Público** e "
       "**advogados** com mais de **10 anos** de carreira ou atividade. O órgão de classe forma **lista sêxtupla**; o tribunal, **lista tríplice**; "
       "o **Chefe do Executivo** escolhe um em **20 dias**.",
       "**Reserva de plenário** (art. 97): os tribunais só declaram a inconstitucionalidade de lei pelo voto da **maioria absoluta** de seus membros "
       "ou do órgão especial. A **SV 10** proíbe que órgão fracionário afaste a lei sem declarar formalmente a inconstitucionalidade."),

    h2("2. Supremo Tribunal Federal"),
    tb(["Ponto", "Regra"], [0.24, 0.76], [
        ("Composição", "**11 Ministros**, **brasileiros natos**, com mais de **35** e menos de **70 anos**, notável saber jurídico e reputação ilibada."),
        ("Nomeação", "Pelo **Presidente da República**, após aprovação pela **maioria absoluta do Senado**. Não há exigência de ser juiz de carreira."),
        ("Papel", "**Guardião da Constituição**."),
    ]),
    h3("Competências em destaque (art. 102)"),
    bl("**Originária**: ADI, ADC (e ADPF, na forma da lei); nas **infrações penais comuns**, o **Presidente**, o **Vice**, os **membros do Congresso**, "
       "seus próprios Ministros e o **PGR**; nas infrações comuns e de responsabilidade, os **Ministros de Estado**, os **Comandantes das Forças "
       "Armadas**, os membros dos **Tribunais Superiores** e do **TCU**; **habeas corpus** quando o paciente for uma dessas autoridades; **MS** e "
       "**HD** contra atos do Presidente, das Mesas da Câmara e do Senado, do TCU, do PGR e do próprio STF; **extradição** solicitada por Estado "
       "estrangeiro; ações contra o **CNJ** e o **CNMP**.",
       "**Recurso ordinário**: HC, MS, HD e MI decididos em **única instância** pelos **Tribunais Superiores**, se **denegatória** a decisão; "
       "**crime político**.",
       "**Recurso extraordinário**: causas decididas em única ou última instância quando a decisão **contrariar a Constituição**, declarar a "
       "inconstitucionalidade de tratado ou lei federal, ou julgar válida lei ou ato local contestado em face da Constituição ou de lei federal. "
       "Exige **repercussão geral**, que só pode ser recusada por **2/3** dos membros."),
    h3("Súmula vinculante (art. 103-A)"),
    bl("Editada pelo STF, de ofício ou por provocação, por **2/3** dos seus membros, após **reiteradas decisões** sobre matéria constitucional.",
       "Vincula os **demais órgãos do Judiciário** e a **administração pública direta e indireta** de **todas as esferas**.",
       "**Não vincula** o **Poder Legislativo** na função de legislar, nem o **próprio STF** (que pode rever ou cancelar a súmula).",
       "Contra ato ou decisão que contrariar súmula vinculante cabe **reclamação** ao STF."),
    h3("Legitimados para ADI e ADC (art. 103)"),
    tb(["Universais (sem pertinência temática)", "Especiais (precisam de pertinência temática)"], [0.5, 0.5], [
        ("Presidente da República", "Mesa de Assembleia Legislativa ou da Câmara Legislativa do DF"),
        ("Mesas do Senado e da Câmara", "Governador de Estado ou do DF"),
        ("Procurador-Geral da República", "Confederação sindical ou entidade de classe de âmbito nacional"),
        ("Conselho Federal da OAB; partido político com representação no Congresso", ""),
    ]),

    h2("3. CNJ, STJ e justiças especializadas"),
    bl("**CNJ** (art. 103-B): **15 membros**, presidido pelo **Presidente do STF**, mandato de **2 anos** (uma recondução). Faz o **controle "
       "administrativo e financeiro** do Judiciário e dos **deveres funcionais** dos juízes. **Não tem função jurisdicional** e **não tem "
       "competência sobre o STF**. O Corregedor Nacional é o Ministro do **STJ**.",
       "**STJ** (arts. 104 e 105): no mínimo **33 Ministros**, brasileiros (**não** se exige nato), com mais de 35 e menos de 70 anos; **1/3** de "
       "juízes dos TRFs, **1/3** de desembargadores dos TJs e **1/3** de advogados e membros do MP; nomeados pelo Presidente após aprovação da "
       "**maioria absoluta do Senado**. Julga **Governadores** nos **crimes comuns**; desembargadores e membros dos tribunais de contas estaduais "
       "nos crimes comuns e de responsabilidade; **homologa sentenças estrangeiras** e concede **exequatur** às cartas rogatórias; julga o "
       "**recurso especial** (contrariedade a **lei federal** ou divergência de interpretação), que exige demonstração de **relevância** (EC 125/2022)."),
    h3("Justiça Federal (art. 109): base da atuação da Polícia Federal"),
    bl("Causas em que a **União**, suas **autarquias** ou **empresas públicas federais** forem interessadas (sociedades de economia mista **não** "
       "atraem a Justiça Federal).",
       "**Crimes políticos** e infrações penais em detrimento de **bens, serviços ou interesse da União**, de suas autarquias ou empresas públicas, "
       "**excluídas as contravenções** e ressalvadas a Justiça Militar e a Eleitoral.",
       "Crimes previstos em **tratado** ou convenção internacional, quando iniciada a execução no País e o resultado ocorrer no exterior (ou o "
       "inverso): é o caso do **tráfico internacional** de drogas.",
       "Crimes contra a **organização do trabalho** e, nos casos da lei, contra o **sistema financeiro** e a ordem econômico-financeira.",
       "Crimes cometidos **a bordo de navios ou aeronaves**, ressalvada a Justiça Militar; crimes de **ingresso ou permanência irregular de "
       "estrangeiro**; disputa sobre **direitos indígenas**.",
       "**Graves violações de direitos humanos**: o **PGR** pode suscitar, perante o **STJ**, o **incidente de deslocamento de competência** (IDC) "
       "para a Justiça Federal (§ 5º)."),
    nt("**Súmula 122 do STJ**: compete à Justiça Federal o processo e julgamento unificado dos crimes conexos de competência federal e estadual. "
       "Contravenção penal é sempre da Justiça **Estadual**, mesmo que atinja interesse da União (Súmula 38 do STJ)."),
    h3("Justiça Militar"),
    tb(["", "Justiça Militar da União (art. 124)", "Justiça Militar estadual (art. 125)"], [0.18, 0.41, 0.41], [
        ("Julga", "Os **crimes militares** definidos em lei", "Os **militares dos Estados** nos crimes militares e as **ações contra atos disciplinares** militares"),
        ("Civis", "**Pode** julgar civis", "**Nunca** julga civis"),
        ("Exceção", "—", "Crime **doloso contra a vida de civil** praticado por militar estadual vai ao **Tribunal do Júri**"),
    ]),

    h2("4. Funções essenciais à Justiça"),
    h3("Ministério Público (arts. 127 a 130-A)"),
    bl("Instituição **permanente**, essencial à função jurisdicional, incumbida da defesa da **ordem jurídica**, do **regime democrático** e dos "
       "**interesses sociais e individuais indisponíveis**.",
       "Princípios: **unidade**, **indivisibilidade** e **independência funcional**. Tem autonomia funcional e administrativa.",
       "Abrange o **MPU** (MPF, MPT, MPM e MPDFT) e os **MPs dos Estados**.",
       "**PGR**: nomeado pelo Presidente entre integrantes da carreira, maiores de **35 anos**, após aprovação pela **maioria absoluta do Senado**, "
       "para mandato de **2 anos**, permitida a recondução. A destituição exige autorização da **maioria absoluta do Senado**.",
       "Garantias: **vitaliciedade** (após 2 anos), **inamovibilidade** e **irredutibilidade**. É vedada a advocacia e a atividade político-partidária."),
    key("Funções do MP de interesse policial (art. 129)",
        "Promover, **privativamente**, a **ação penal pública**; exercer o **controle externo da atividade policial**; **requisitar diligências "
        "investigatórias** e a **instauração de inquérito policial**, indicando os fundamentos jurídicos; promover o inquérito civil e a ação "
        "civil pública. O STF reconhece que o MP pode **investigar diretamente** na esfera penal, respeitados os direitos dos investigados "
        "(RE 593.727)."),
    tb(["Instituição", "Pontos principais"], [0.22, 0.78], [
        ("**Advocacia Pública** (arts. 131 e 132)", "A **AGU** representa a União judicial e extrajudicialmente; o **Advogado-Geral** é de **livre nomeação** do "
                                                    "Presidente entre cidadãos maiores de 35 anos. **Procuradores dos Estados e do DF**: concurso com participação da OAB; "
                                                    "estabilidade após **3 anos**."),
        ("**Advocacia** (art. 133)", "O advogado é **indispensável** à administração da justiça e **inviolável** por seus atos e manifestações no exercício da "
                                     "profissão, **nos limites da lei**."),
        ("**Defensoria Pública** (art. 134)", "Instituição **permanente**: orientação jurídica, promoção dos direitos humanos e defesa, judicial e extrajudicial, "
                                              "**integral e gratuita**, dos **necessitados**. Tem **autonomia funcional e administrativa**; princípios de unidade, "
                                              "indivisibilidade e independência funcional; os defensores são vedados de advogar fora das atribuições."),
    ]),
]

QUIZ = quiz([
    ("C", "A vitaliciedade, no primeiro grau, só é adquirida após dois anos de exercício, dependendo a perda do cargo, nesse período, de deliberação do tribunal a que o juiz estiver vinculado.",
     "Art. 95, I."),
    ("E", "É vedado ao juiz exercer qualquer outro cargo ou função, inclusive de magistério.",
     "O juiz pode exercer uma função de magistério."),
    ("C", "Os Ministros do STF são escolhidos entre brasileiros natos com mais de trinta e cinco e menos de setenta anos de idade.",
     "Arts. 12, § 3º, e 101 (limite de 70 anos pela EC 122/2022)."),
    ("E", "Os Ministros do STF são nomeados pelo Presidente da República após aprovação por dois terços do Senado Federal.",
     "A aprovação é por maioria absoluta do Senado."),
    ("C", "O CNJ não tem competência para fiscalizar a atuação dos Ministros do Supremo Tribunal Federal.",
     "O STF está acima do CNJ (ADI 3.367)."),
    ("E", "A súmula vinculante vincula o Poder Legislativo no exercício da função legislativa.",
     "Ela vincula o Judiciário e a administração pública, não o legislador."),
    ("C", "Compete ao STJ processar e julgar, nos crimes comuns, os governadores dos estados e do Distrito Federal.",
     "Art. 105, I, a."),
    ("E", "Compete ao STF homologar sentenças estrangeiras e conceder exequatur às cartas rogatórias.",
     "Desde a EC 45/2004, essa competência é do STJ."),
    ("C", "Compete ao Ministério Público exercer o controle externo da atividade policial.",
     "Art. 129, VII."),
    ("E", "A Defensoria Pública presta assistência jurídica integral e gratuita a todas as pessoas, independentemente de sua condição econômica.",
     "A Defensoria atende os necessitados."),

    ("C", "Agentes da Polícia Federal prenderam em flagrante, em aeroporto, pessoa que tentava embarcar para a Europa com cocaína. Nessa situação, a competência para o processo é da Justiça Federal, por se tratar de crime previsto em tratado internacional com caráter transnacional.",
     "Art. 109, V: tráfico internacional de drogas."),
    ("E", "Contravenção penal praticada em detrimento de bens da União é julgada pela Justiça Federal.",
     "O art. 109, IV, exclui as contravenções; a competência é da Justiça Estadual (Súmula 38 do STJ)."),
    ("C", "Os crimes praticados contra bens de empresa pública federal são, em regra, julgados pela Justiça Federal, o que não ocorre com os crimes contra bens de sociedade de economia mista federal.",
     "Sociedades de economia mista não constam do art. 109, IV."),
    ("E", "A Justiça Militar estadual tem competência para julgar civis que pratiquem crimes militares contra instituições militares estaduais.",
     "A Justiça Militar estadual julga apenas militares dos estados; civis podem ser julgados apenas pela Justiça Militar da União."),
    ("C", "Policial militar que, em serviço, mata dolosamente um civil será julgado pelo Tribunal do Júri, e não pela Justiça Militar estadual.",
     "Art. 125, § 4º, ressalva a competência do júri quando a vítima for civil."),
    ("E", "O incidente de deslocamento de competência para a Justiça Federal, nas hipóteses de grave violação de direitos humanos, é suscitado pelo Ministro da Justiça perante o STF.",
     "É suscitado pelo PGR perante o STJ (art. 109, § 5º)."),
    ("C", "O Ministério Público pode requisitar diligências investigatórias e a instauração de inquérito policial, indicando os fundamentos jurídicos de suas manifestações.",
     "Art. 129, VIII."),
    ("E", "O Procurador-Geral da República é nomeado pelo Presidente da República entre cidadãos de notável saber jurídico, integrantes ou não da carreira, para mandato de quatro anos.",
     "É escolhido entre integrantes da carreira, para mandato de dois anos, permitida a recondução."),
    ("C", "Partido político com representação no Congresso Nacional pode propor ação direta de inconstitucionalidade sem demonstrar pertinência temática.",
     "É legitimado universal."),
    ("E", "Os tribunais podem declarar a inconstitucionalidade de lei pelo voto da maioria simples de seus membros presentes à sessão.",
     "A reserva de plenário exige maioria absoluta dos membros do tribunal ou do órgão especial (art. 97)."),
], 20)

SOURCES = [
    "Constituição da República Federativa do Brasil de 1988, arts. 92 a 135; EC 45/2004, 122/2022 e 125/2022.",
    "Supremo Tribunal Federal: Súmula Vinculante 10; ADI 3.367; RE 593.727.",
    "Superior Tribunal de Justiça: Súmulas 38 e 122.",
    SRC_A,
]
