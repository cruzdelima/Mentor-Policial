# -*- coding: utf-8 -*-
"""Direito Constitucional · Defesa do Estado: estados de defesa e de sítio, Forças Armadas — MATERIAL APROFUNDADO."""
from common import *

MATERIAL = material(
    "dc-defesa-02", "DC", "DC-12", "aprofundado", "Defesa do Estado: estados de defesa e de sítio, Forças Armadas",
    "Direito Constitucional · Defesa do Estado",
    "constitucional_defesa_aprofundado", "Constitucional_Defesa_do_Estado_APROFUNDADO.pdf", None, ["Defesa", "do Estado"],
    ["Estado de defesa e estado de sítio lado a lado, controle pelo Congresso, Forças Armadas,", "GLO e serviço militar, com 20 questões no estilo Cebraspe."],
    [("01", "Sistema de crises", "princípios e visão geral"),
     ("02", "Estado de defesa", "hipóteses, prazo, medidas, prisão"),
     ("03", "Estado de sítio", "autorização prévia, prazos e medidas"),
     ("04", "Forças Armadas", "missão, GLO, regime dos militares"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Defesa do Estado e das instituições democráticas (arts. 136 a 143) — Direito Constitucional",
    "Base: Constituição Federal de 1988, LC 97/1999 e jurisprudência do STF.", 90)

THEORY = [
    exam("Como estudar este material",
         "Monte uma tabela comparando **estado de defesa** e **estado de sítio**: hipótese, quem ouve, quando o Congresso se manifesta, quórum, "
         "prazo e medidas. A banca quase sempre troca uma característica de um pelo outro. Nas Forças Armadas, o foco é a **missão** (art. 142) "
         "e as **restrições** aos militares."),

    h2("1. O sistema constitucional de crises"),
    p("O Título V trata da **defesa do Estado e das instituições democráticas**. Em situações de crise, a Constituição permite **restringir "
      "temporariamente** alguns direitos, sempre com **necessidade**, **temporariedade**, **proporcionalidade** e **controle** pelo Congresso e "
      "pelo Judiciário. Os executores respondem pelos **ilícitos** cometidos."),
    nt("Durante o estado de defesa, o estado de sítio e a intervenção federal, a Constituição **não pode ser emendada** (art. 60, § 1º)."),

    h2("2. Estado de defesa (art. 136)"),
    key("Hipóteses",
        "Preservar ou prontamente restabelecer, em **locais restritos e determinados**, a **ordem pública** ou a **paz social** ameaçadas por **grave "
        "e iminente instabilidade institucional** ou atingidas por **calamidades de grandes proporções na natureza**."),
    bl("**Quem decreta**: o **Presidente da República**, depois de **ouvir** o Conselho da República e o Conselho de Defesa Nacional (opiniões "
       "**não vinculantes**).",
       "**Controle**: decretado, o ato é submetido ao **Congresso** em **24 horas**, com a justificação. O Congresso decide por **maioria absoluta** "
       "em **10 dias**; se estiver em recesso, será convocado extraordinariamente em **5 dias**. **Rejeitado**, o estado de defesa **cessa imediatamente**.",
       "**Prazo**: **até 30 dias**, prorrogável **uma vez** por igual período.",
       "O decreto indica o **tempo de duração**, as **áreas** abrangidas e as **medidas coercitivas**."),
    tb(["Medidas permitidas no estado de defesa"], [1.0], [
        ("Restrições ao direito de **reunião**, ainda que exercida no seio das associações",),
        ("Restrições ao **sigilo de correspondência** e ao **sigilo de comunicação telegráfica e telefônica**",),
        ("Na **calamidade pública**, **ocupação e uso temporário de bens e serviços públicos**, respondendo a União pelos danos e custos",),
    ]),
    h3("Prisão durante o estado de defesa (§ 3º)"),
    bl("A prisão por **crime contra o Estado**, determinada pelo **executor da medida**, será **comunicada imediatamente ao juiz** competente, que a "
       "**relaxará** se não for legal. O preso pode requerer **exame de corpo de delito**.",
       "A comunicação vem acompanhada de declaração do **estado físico e mental** do detido.",
       "A prisão **não pode passar de 10 dias**, salvo quando **autorizada pelo Judiciário**.",
       "É **vedada a incomunicabilidade** do preso."),

    h2("3. Estado de sítio (arts. 137 a 139)"),
    tb(["Hipótese", "Prazo"], [0.62, 0.38], [
        ("**I** – **comoção grave de repercussão nacional** ou fatos que comprovem a **ineficácia** de medida tomada durante o **estado de defesa**",
         "**Até 30 dias**, prorrogável **cada vez** por no máximo 30 (sem limite de prorrogações)"),
        ("**II** – **declaração de estado de guerra** ou **resposta a agressão armada estrangeira**", "**Enquanto durar** a guerra ou a agressão"),
    ]),
    bl("**Quem decreta**: o **Presidente**, ouvidos os dois Conselhos, depois de **solicitar autorização prévia** ao **Congresso Nacional**, que "
       "decide por **maioria absoluta**.",
       "O decreto indica a **duração**, as **normas** necessárias à sua execução e as **garantias constitucionais** que ficarão suspensas; depois de "
       "publicado, o Presidente designa o **executor** e as **áreas** abrangidas.",
       "O Congresso permanece **em funcionamento** até o término das medidas. A Mesa designa **comissão de 5 membros** para acompanhar e fiscalizar "
       "a execução (o mesmo vale para o estado de defesa)."),
    tb(["Medidas no sítio por comoção grave (art. 139)"], [1.0], [
        ("**Obrigação de permanência** em localidade determinada",),
        ("**Detenção** em edifício **não destinado** a acusados ou condenados por crimes comuns",),
        ("Restrições à inviolabilidade da **correspondência**, ao sigilo das **comunicações**, à prestação de **informações** e à **liberdade de "
         "imprensa**, radiodifusão e televisão, na forma da lei",),
        ("**Suspensão** da liberdade de **reunião**",),
        ("**Busca e apreensão em domicílio**",),
        ("**Intervenção** nas empresas de serviços públicos",),
        ("**Requisição de bens**",),
    ]),
    nt("Não se inclui nas restrições a difusão de **pronunciamentos de parlamentares** feitos em suas Casas, desde que liberada pela respectiva Mesa. "
       "No sítio por **guerra** (inciso II), a Constituição não traz rol fechado de medidas, mas os princípios de necessidade e proporcionalidade "
       "continuam valendo."),
    h3("Comparação"),
    tb(["", "Estado de defesa", "Estado de sítio"], [0.22, 0.39, 0.39], [
        ("Gravidade", "Menor", "Maior"),
        ("Área", "**Locais restritos e determinados**", "Pode ser **nacional**"),
        ("Conselhos", "Ouvidos (não vinculam)", "Ouvidos (não vinculam)"),
        ("Congresso", "Controle **posterior**: recebe o decreto em 24 h e **aprova** ou rejeita", "Controle **prévio**: **autoriza** antes do decreto"),
        ("Quórum", "Maioria **absoluta**", "Maioria **absoluta**"),
        ("Prazo", "30 dias + **1** prorrogação de 30", "30 dias, prorrogáveis **cada vez** por 30 (comoção); guerra: enquanto durar"),
        ("Busca domiciliar", "**Não** prevista", "**Prevista** (comoção grave)"),
    ]),
    trap("Pegadinhas clássicas",
         "No **estado de defesa**, o Congresso **aprova** depois (24 h); no **estado de sítio**, **autoriza** antes. A prorrogação do estado de "
         "defesa é **uma só**; a do sítio por comoção pode ser **repetida**. Busca e apreensão em domicílio só aparece no **sítio**. E quem decreta "
         "os dois é sempre o **Presidente**, não o Congresso."),
    p("Cessado o estado de defesa ou de sítio, **cessam também seus efeitos**, sem prejuízo da **responsabilidade** pelos ilícitos dos executores "
      "ou agentes. O Presidente relata ao Congresso as medidas aplicadas, com a relação nominal dos atingidos e a indicação das restrições (art. 141)."),

    h2("4. Forças Armadas (arts. 142 e 143)"),
    key("Texto da Constituição",
        "Art. 142. As Forças Armadas, constituídas pela **Marinha**, pelo **Exército** e pela **Aeronáutica**, são **instituições nacionais permanentes "
        "e regulares**, organizadas com base na **hierarquia** e na **disciplina**, sob a **autoridade suprema do Presidente da República**, e "
        "destinam-se à **defesa da Pátria**, à **garantia dos poderes constitucionais** e, por iniciativa de qualquer destes, da **lei e da ordem**."),
    bl("**GLO** (garantia da lei e da ordem): o emprego das Forças Armadas é regulado pela **LC 97/1999**; ocorre por **decisão do Presidente**, por "
       "iniciativa própria ou dos Presidentes do STF, do Senado ou da Câmara, depois de **esgotados** os instrumentos de segurança pública do art. 144, "
       "em área previamente definida e por tempo limitado.",
       "O STF afirmou que o art. 142 **não** confere às Forças Armadas papel de **poder moderador** nem autoriza intervenção militar sobre os "
       "Poderes (ADI 6.457).",
       "**Não cabe habeas corpus** em relação a **punições disciplinares militares** (§ 2º), salvo para examinar a legalidade, conforme o STF."),
    h3("Regime dos militares (art. 142, § 3º)"),
    bl("As **patentes** são conferidas pelo **Presidente da República**.",
       "São **proibidas a sindicalização e a greve**.",
       "Enquanto em **serviço ativo**, o militar **não pode estar filiado** a partido político.",
       "O militar da ativa que tomar posse em **cargo público civil permanente** será **transferido para a reserva**, salvo nas hipóteses de "
       "acumulação admitidas (profissionais de saúde).",
       "O **oficial** só perde o **posto e a patente** se julgado **indigno** ou **incompatível** com o oficialato por decisão de **tribunal militar "
       "permanente** (em tempo de paz) ou de tribunal especial (em guerra). O oficial condenado a pena privativa de liberdade **superior a 2 anos**, "
       "por sentença transitada em julgado, será submetido a esse julgamento.",
       "Essas regras se aplicam, no que couber, aos **militares dos Estados** (PM e bombeiros), por força do art. 42, § 1º, e o oficial estadual "
       "perde o posto por decisão do **Tribunal de Justiça** ou do Tribunal de Justiça Militar, onde houver."),
    h3("Serviço militar (art. 143)"),
    bl("É **obrigatório**, nos termos da lei.",
       "Às Forças Armadas compete atribuir **serviço alternativo** aos que, em **tempo de paz**, alegarem **imperativo de consciência** (crença "
       "religiosa, convicção filosófica ou política).",
       "As **mulheres** e os **eclesiásticos** ficam **isentos** do serviço militar obrigatório em **tempo de paz**, sujeitos a outros encargos da lei."),
]

QUIZ = quiz([
    ("C", "O estado de defesa pode ser decretado para restabelecer a ordem pública em locais restritos e determinados atingidos por calamidade de grandes proporções na natureza.",
     "Art. 136, caput."),
    ("E", "O estado de defesa depende de autorização prévia do Congresso Nacional.",
     "O decreto é submetido ao Congresso em 24 horas, que o aprova ou rejeita depois; a autorização prévia é exigida no estado de sítio."),
    ("C", "O tempo de duração do estado de defesa não será superior a trinta dias, podendo ser prorrogado uma vez, por igual período.",
     "Art. 136, § 2º."),
    ("E", "No estado de defesa, a prisão por crime contra o Estado pode durar até trinta dias sem autorização judicial.",
     "Não pode superar dez dias, salvo autorização do Judiciário."),
    ("C", "Durante o estado de defesa, é vedada a incomunicabilidade do preso.",
     "Art. 136, § 3º, IV."),
    ("E", "A declaração de estado de guerra autoriza a decretação do estado de defesa.",
     "A guerra ou a agressão armada estrangeira é hipótese de estado de sítio."),
    ("C", "O Congresso Nacional decide por maioria absoluta tanto sobre o decreto de estado de defesa quanto sobre o pedido de autorização para o estado de sítio.",
     "Arts. 136, § 4º, e 137, parágrafo único."),
    ("E", "As Forças Armadas estão sob a autoridade suprema do Ministro de Estado da Defesa.",
     "Estão sob a autoridade suprema do Presidente da República."),
    ("C", "Ao militar são proibidas a sindicalização e a greve.",
     "Art. 142, § 3º, IV."),
    ("E", "As mulheres estão sujeitas ao serviço militar obrigatório em tempo de paz, nas mesmas condições dos homens.",
     "As mulheres e os eclesiásticos são isentos do serviço militar obrigatório em tempo de paz."),

    ("C", "Durante estado de sítio decretado por comoção grave de repercussão nacional, pode ser determinada a busca e apreensão em domicílio.",
     "Art. 139, V."),
    ("E", "Durante o estado de defesa, o executor da medida pode determinar a busca e apreensão em domicílio de pessoas suspeitas de crimes contra o Estado.",
     "A busca e apreensão em domicílio está entre as medidas do estado de sítio, não do estado de defesa."),
    ("C", "O estado de sítio decretado em razão de comoção grave de repercussão nacional não pode ser decretado por mais de trinta dias, nem prorrogado, de cada vez, por prazo superior.",
     "Art. 138, § 1º."),
    ("E", "Rejeitado pelo Congresso Nacional o decreto de estado de defesa, as medidas continuarão em vigor até o fim do prazo nele fixado.",
     "Rejeitado o decreto, cessa imediatamente o estado de defesa (art. 136, § 7º)."),
    ("C", "Cessado o estado de sítio, cessarão também seus efeitos, sem prejuízo da responsabilidade pelos ilícitos cometidos por seus executores ou agentes.",
     "Art. 141."),
    ("E", "Conforme o STF, o art. 142 da Constituição permite às Forças Armadas atuar como poder moderador em caso de conflito entre os Poderes.",
     "O STF rejeitou essa interpretação (ADI 6.457)."),
    ("C", "O emprego das Forças Armadas na garantia da lei e da ordem pode ocorrer por iniciativa de qualquer dos poderes constitucionais, cabendo a decisão ao Presidente da República.",
     "Art. 142 e LC 97/1999."),
    ("E", "O oficial das Forças Armadas condenado a pena privativa de liberdade superior a um ano perde automaticamente o posto e a patente.",
     "A perda depende de julgamento por tribunal militar; o oficial condenado a pena superior a dois anos é submetido a esse julgamento."),
    ("C", "O militar enquanto em serviço ativo não pode estar filiado a partido político.",
     "Art. 142, § 3º, V."),
    ("E", "Os pareceres do Conselho da República e do Conselho de Defesa Nacional sobre a decretação do estado de defesa vinculam o Presidente da República.",
     "Os Conselhos são ouvidos, mas suas manifestações são apenas opinativas."),
], 20)

SOURCES = [
    "Constituição da República Federativa do Brasil de 1988, arts. 42, 60, § 1º, e 136 a 143.",
    "Lei Complementar 97/1999 (organização e emprego das Forças Armadas).",
    "Supremo Tribunal Federal: ADI 6.457.",
    SRC_A,
]
