# -*- coding: utf-8 -*-
"""Direito Constitucional · Direitos políticos e partidos (arts. 14 a 17) — MATERIAL APROFUNDADO."""
from common import *

MATERIAL = material(
    "dc-politicos-02", "DC", "DC-06", "aprofundado", "Direitos políticos e partidos (arts. 14 a 17)", "Direito Constitucional · Direitos fundamentais",
    "constitucional_politicos_aprofundado", "Constitucional_Direitos_Politicos_APROFUNDADO.pdf", None, ["Direitos políticos", "e partidos"],
    ["Voto, alistamento, elegibilidade, inelegibilidades, perda e suspensão de direitos", "políticos e partidos, com 20 questões no estilo Cebraspe."],
    [("01", "Soberania popular", "sufrágio, voto, plebiscito, referendo"),
     ("02", "Capacidade eleitoral", "alistamento, idades, condições de elegibilidade"),
     ("03", "Inelegibilidades", "reeleição, parentes, militares"),
     ("04", "Perda, suspensão e partidos", "art. 15, anterioridade, art. 17"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Direitos políticos e partidos políticos (arts. 14 a 17) — Direito Constitucional",
    "Base: Constituição Federal de 1988, jurisprudência do STF e do TSE.", 150)

THEORY = [
    exam("Como estudar este material",
         "O art. 14 é cheio de **idades e prazos**: 16, 18, 21, 30, 35 e 70 anos; 6 meses, 15 dias, 1 ano, 10 anos de serviço militar. A banca "
         "troca esses números e cobra as **inelegibilidades** por casos concretos (o filho do prefeito, o militar candidato). Faça uma tabela "
         "própria com os números e revise com o PDF de resumo."),

    h2("1. Soberania popular"),
    key("Texto da Constituição",
        "Art. 14. A soberania popular será exercida pelo **sufrágio universal** e pelo **voto direto e secreto**, com **valor igual para todos**, e, "
        "nos termos da lei, mediante: I – **plebiscito**; II – **referendo**; III – **iniciativa popular**."),
    tb(["Termo", "Significado"], [0.24, 0.76], [
        ("Sufrágio", "O **direito** de votar e ser votado. É **universal**: não depende de renda ou instrução."),
        ("Voto", "O **exercício** do sufrágio. É direto, secreto, igual, periódico, livre e personalíssimo."),
        ("Escrutínio", "O **modo** de votar e apurar (urna eletrônica)."),
        ("Plebiscito", "Consulta **prévia** ao ato: o povo decide antes."),
        ("Referendo", "Consulta **posterior**: o povo ratifica ou rejeita um ato já editado."),
        ("Iniciativa popular", "Projeto de lei federal subscrito por **1% do eleitorado nacional**, distribuído por **5 Estados**, com não menos de **0,3%** dos eleitores de cada um (art. 61, § 2º)."),
    ]),
    nt("O **voto direto, secreto, universal e periódico** é cláusula pétrea (art. 60, § 4º, II). A **obrigatoriedade** do voto **não** é: "
       "uma emenda pode tornar o voto facultativo."),

    h2("2. Alistamento e voto"),
    tb(["Situação", "Alistamento e voto"], [0.56, 0.44], [
        ("Maiores de **18** anos", "**Obrigatórios**"),
        ("**Analfabetos**", "Facultativos"),
        ("Maiores de **70** anos", "Facultativos"),
        ("Maiores de **16** e menores de **18**", "Facultativos"),
        ("**Estrangeiros**", "**Inalistáveis**"),
        ("**Conscritos**, durante o serviço militar obrigatório", "**Inalistáveis**"),
    ]),
    trap("Pegadinha: analfabeto",
         "O analfabeto **pode votar** (voto facultativo), mas é **inelegível** (§ 4º). Ele tem capacidade eleitoral **ativa**, mas não **passiva**."),

    h2("3. Condições de elegibilidade (§ 3º)"),
    bl("Nacionalidade brasileira; **pleno exercício** dos direitos políticos; **alistamento** eleitoral; **domicílio eleitoral** na circunscrição; "
       "**filiação partidária** (não há candidatura avulsa); **idade mínima**."),
    tb(["Idade mínima", "Cargos"], [0.2, 0.8], [
        ("**35 anos**", "Presidente e Vice-Presidente da República; **Senador**"),
        ("**30 anos**", "Governador e Vice-Governador de Estado e do DF"),
        ("**21 anos**", "Deputado federal, estadual ou distrital; **Prefeito** e Vice-Prefeito; juiz de paz"),
        ("**18 anos**", "**Vereador**"),
    ]),
    nt("A idade mínima é verificada, em regra, na data da **posse**; para vereador (18 anos), na data-limite do pedido de registro "
       "(Lei 9.504/1997, art. 11, § 2º)."),

    h2("4. Inelegibilidades"),
    tb(["Tipo", "Quem", "Regra"], [0.18, 0.34, 0.48], [
        ("Absoluta", "**Inalistáveis** e **analfabetos**", "Não podem concorrer a nenhum cargo."),
        ("Reeleição (§ 5º)", "Presidente, Governadores, Prefeitos e quem os **sucedeu** ou **substituiu** no curso do mandato", "Podem ser reeleitos para **um único período subsequente**."),
        ("Desincompatibilização (§ 6º)", "Os mesmos chefes do Executivo", "Para concorrer a **outros cargos**, devem **renunciar** até **6 meses** antes do pleito."),
        ("Reflexa (§ 7º)", "**Cônjuge** e parentes até o **2º grau** (consanguíneos, afins ou por adoção) dos chefes do Executivo ou de quem os substituiu nos 6 meses anteriores", "Inelegíveis **no território de jurisdição** do titular, **salvo** se já titulares de mandato eletivo e candidatos à **reeleição**."),
        ("Legal (§ 9º)", "Outros casos", "Fixados por **lei complementar** (LC 64/1990, alterada pela Lei da Ficha Limpa, LC 135/2010)."),
    ]),
    bl("Para concorrer à **reeleição**, o chefe do Executivo **não** precisa renunciar.",
       "**Súmula Vinculante 18**: a dissolução da sociedade ou do vínculo conjugal **no curso do mandato** não afasta a inelegibilidade reflexa.",
       "O STF veda o **prefeito itinerante**: quem exerceu dois mandatos consecutivos de prefeito não pode se candidatar a prefeito em **outro "
       "Município** no período seguinte (RE 637.485).",
       "Exemplo de inelegibilidade reflexa: o **filho do governador** não pode ser candidato a deputado **pelo mesmo Estado**, mas pode concorrer "
       "por outro Estado ou, se já for deputado, à reeleição."),
    h3("O militar candidato (§ 8º)"),
    tb(["Tempo de serviço", "Consequência"], [0.3, 0.7], [
        ("**Menos de 10 anos**", "Deve **afastar-se da atividade**."),
        ("**Mais de 10 anos**", "Será **agregado** pela autoridade superior e, se eleito, passará automaticamente, no ato da **diplomação**, para a **inatividade**."),
    ]),
    nt("O militar alistável é elegível. Como não pode estar filiado a partido enquanto em serviço ativo (art. 142, § 3º, V), o TSE dispensa a "
       "filiação prévia: basta o registro da candidatura apresentado pelo partido."),
    h3("Ação de impugnação de mandato eletivo (§§ 10 e 11)"),
    p("O mandato eletivo pode ser impugnado perante a **Justiça Eleitoral** no prazo de **15 dias contados da diplomação**, com provas de **abuso do "
      "poder econômico, corrupção ou fraude**. A ação tramita em **segredo de justiça**, e o autor responde se agir de forma temerária ou de má-fé."),

    h2("5. Perda e suspensão dos direitos políticos (art. 15)"),
    key("Texto da Constituição",
        "Art. 15. É **vedada a cassação** de direitos políticos, cuja perda ou suspensão só se dará nos casos de: I – cancelamento da naturalização "
        "por sentença transitada em julgado; II – incapacidade civil absoluta; III – condenação criminal transitada em julgado, enquanto durarem "
        "seus efeitos; IV – recusa de cumprir obrigação a todos imposta ou prestação alternativa (art. 5º, VIII); V – improbidade administrativa (art. 37, § 4º)."),
    tb(["Hipótese", "Classificação usual"], [0.6, 0.4], [
        ("Cancelamento da naturalização", "**Perda**"),
        ("Incapacidade civil absoluta", "Suspensão"),
        ("**Condenação criminal transitada em julgado**", "Suspensão, **enquanto durarem os efeitos** da pena"),
        ("Recusa de obrigação a todos imposta (escusa sem prestação alternativa)", "Perda para parte da doutrina; suspensão para a lei (Lei 8.239/1991)"),
        ("Improbidade administrativa", "Suspensão"),
    ]),
    bl("A suspensão por condenação criminal é **automática**: vale para qualquer crime e para qualquer pena, inclusive **multa** ou **pena "
       "restritiva de direitos** (STF, RE 601.182).",
       "A **cassação** (retirada arbitrária, por ato político) é **proibida**. Não confunda com a **cassação do mandato** de parlamentar, que "
       "é outra coisa (art. 55)."),

    h2("6. Anterioridade eleitoral (art. 16)"),
    key("Texto da Constituição",
        "Art. 16. A lei que alterar o processo eleitoral entrará em **vigor na data de sua publicação**, **não se aplicando** à eleição que ocorra "
        "até **1 ano** da data de sua vigência."),
    p("A lei vale desde a publicação, mas só se **aplica** às eleições que ocorrerem **mais de 1 ano** depois. O STF aplicou a regra à Lei da Ficha "
      "Limpa, que por isso não valeu para as eleições de 2010 (RE 633.703)."),

    h2("7. Partidos políticos (art. 17)"),
    bl("É **livre** a criação, fusão, incorporação e extinção de partidos, resguardados a soberania nacional, o regime democrático, o "
       "**pluripartidarismo** e os direitos fundamentais da pessoa humana.",
       "Preceitos: **caráter nacional**; **proibição de receber recursos** de entidade ou governo **estrangeiros**; **prestação de contas** à "
       "Justiça Eleitoral; funcionamento parlamentar de acordo com a lei.",
       "O partido adquire **personalidade jurídica** na forma da **lei civil** (cartório) e depois registra seu estatuto no **TSE**.",
       "É **vedada** a utilização de **organização paramilitar** pelos partidos.",
       "Têm **autonomia** para definir estrutura interna e regras de escolha e coligação; é vedada a **obrigatoriedade de vinculação** entre "
       "candidaturas nacionais, estaduais e municipais (fim da verticalização).",
       "São **vedadas coligações nas eleições proporcionais** (EC 97/2017). Nas majoritárias, continuam permitidas.",
       "**Cláusula de desempenho** (EC 97/2017): só têm acesso ao fundo partidário e à propaganda gratuita no rádio e na TV os partidos que "
       "atingirem votação mínima ou elegerem número mínimo de deputados federais, com exigências crescentes até 2030.",
       "**Fidelidade partidária** (§ 6º, EC 111/2021): deputados e vereadores que se desligarem do partido **perdem o mandato**, salvo **anuência "
       "do partido** ou justa causa prevista em lei. A regra **não** alcança os cargos **majoritários** (senador, prefeito, governador, "
       "presidente), conforme o STF (ADI 5.081).",
       "Os partidos devem aplicar no mínimo **30%** dos recursos do fundo partidário e do fundo eleitoral, e do tempo de propaganda, em "
       "**candidaturas femininas** (§ 8º, EC 117/2022)."),
]

QUIZ = quiz([
    ("C", "O alistamento eleitoral e o voto são facultativos para os analfabetos, para os maiores de setenta anos e para os maiores de dezesseis e menores de dezoito anos.",
     "Art. 14, § 1º, II."),
    ("E", "Os conscritos, durante o período do serviço militar obrigatório, têm voto facultativo.",
     "Os conscritos, nesse período, são inalistáveis."),
    ("C", "O analfabeto pode votar, mas é inelegível.",
     "Tem capacidade eleitoral ativa, mas não passiva (art. 14, § 4º)."),
    ("E", "A idade mínima para concorrer ao cargo de senador é de trinta anos.",
     "Para senador, exige-se 35 anos."),
    ("C", "A idade mínima de vinte e um anos é condição de elegibilidade para prefeito e para deputado federal.",
     "Art. 14, § 3º, VI, c."),
    ("E", "Para concorrer à reeleição, o governador deve renunciar ao mandato até seis meses antes do pleito.",
     "A renúncia (desincompatibilização) só é exigida para concorrer a outros cargos."),
    ("C", "É vedada a cassação de direitos políticos.",
     "Art. 15, caput. Admitem-se apenas perda e suspensão nas hipóteses constitucionais."),
    ("E", "A lei que alterar o processo eleitoral só entra em vigor um ano após a data de sua publicação.",
     "Entra em vigor na publicação; apenas não se aplica à eleição que ocorra até um ano da data de sua vigência."),
    ("C", "Os partidos políticos são proibidos de receber recursos financeiros de entidade ou governo estrangeiros.",
     "Art. 17, II."),
    ("E", "A Constituição permite coligações partidárias nas eleições proporcionais, desde que formalizadas até a data das convenções.",
     "Desde a EC 97/2017, são vedadas coligações nas eleições proporcionais."),

    ("C", "A filha de um prefeito em primeiro mandato deseja candidatar-se a vereadora no mesmo município. Nessa situação, ela é inelegível, salvo se já for vereadora e concorrer à reeleição.",
     "É a inelegibilidade reflexa do art. 14, § 7º."),
    ("E", "O irmão do governador de um estado é inelegível para o cargo de deputado federal em qualquer unidade da federação.",
     "A inelegibilidade reflexa vale apenas no território de jurisdição do titular; em outro estado, pode concorrer."),
    ("C", "Se o vínculo conjugal com o prefeito for dissolvido no curso do mandato, a ex-esposa continuará inelegível para o cargo de prefeito no mesmo município.",
     "Súmula Vinculante 18."),
    ("E", "Um militar com oito anos de serviço que deseje candidatar-se a deputado estadual será agregado pela autoridade superior e, se eleito, passará para a inatividade.",
     "Com menos de dez anos de serviço, o militar deve afastar-se da atividade; a agregação é para quem tem mais de dez anos."),
    ("C", "O policial condenado por crime, com sentença transitada em julgado, terá seus direitos políticos suspensos enquanto durarem os efeitos da condenação, ainda que a pena privativa de liberdade tenha sido substituída por restritiva de direitos.",
     "A suspensão é automática e não depende do tipo de pena (STF, RE 601.182)."),
    ("E", "Prefeito reeleito em um município pode candidatar-se a prefeito em município vizinho no período subsequente, pois a vedação à reeleição se restringe ao mesmo território.",
     "O STF veda o prefeito itinerante: a regra impede um terceiro mandato consecutivo de prefeito, ainda que em outro município."),
    ("C", "O mandato eletivo pode ser impugnado perante a Justiça Eleitoral no prazo de quinze dias contados da diplomação, com provas de abuso do poder econômico, corrupção ou fraude.",
     "Art. 14, § 10."),
    ("E", "Senador que se desfiliar sem justa causa do partido pelo qual foi eleito perderá o mandato por infidelidade partidária.",
     "A perda por infidelidade não se aplica aos cargos majoritários (ADI 5.081)."),
    ("C", "A obrigatoriedade do voto não é cláusula pétrea, de modo que emenda constitucional poderia instituir o voto facultativo.",
     "O art. 60, § 4º, II, protege o voto direto, secreto, universal e periódico, não a sua obrigatoriedade."),
    ("E", "O plebiscito é a consulta popular realizada após a edição do ato legislativo, para ratificá-lo ou rejeitá-lo.",
     "Essa é a definição de referendo. O plebiscito é convocado previamente."),
], 20)

SOURCES = [
    "Constituição da República Federativa do Brasil de 1988, arts. 14 a 17, 60, § 4º, e 142, § 3º; EC 97/2017, 111/2021 e 117/2022.",
    "LC 64/1990 e LC 135/2010 (Ficha Limpa); Lei 9.504/1997.",
    "Supremo Tribunal Federal: Súmula Vinculante 18; RE 637.485; RE 601.182; RE 633.703; ADI 5.081.",
    SRC_A,
]
