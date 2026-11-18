# -*- coding: utf-8 -*-
"""Direito Constitucional · Administração Pública e servidores (arts. 37 a 41) — MATERIAL APROFUNDADO."""
from common import *

MATERIAL = material(
    "dc-administracao-02", "DC", "DC-08", "aprofundado", "Administração Pública e servidores (arts. 37 a 41)",
    "Direito Constitucional · Organização do Estado",
    "constitucional_administracao_aprofundado", "Constitucional_Administracao_Publica_APROFUNDADO.pdf", None, ["Administração", "Pública e servidores"],
    ["Princípios, concurso, cargos, teto, acumulação, responsabilidade do Estado, mandato eletivo", "e estabilidade, com 20 questões no estilo Cebraspe."],
    [("01", "Princípios", "LIMPE e regras gerais do art. 37"),
     ("02", "Acesso aos cargos", "concurso, comissão, nepotismo"),
     ("03", "Remuneração", "teto, acumulação (EC 138/2025)"),
     ("04", "Servidores", "responsabilidade, mandato, estabilidade"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Administração Pública e servidores públicos (arts. 37 a 41) — Direito Constitucional",
    "Base: Constituição Federal de 1988, súmulas vinculantes e jurisprudência do STF.", 240)

THEORY = [
    exam("Como estudar este material",
         "O art. 37 é o segundo artigo mais cobrado da Constituição, depois do art. 5º. A banca troca prazos (**2 anos** de validade do concurso, "
         "**3 anos** para a estabilidade), cobra o **teto** de cada Poder, a **acumulação** de cargos (que mudou com a **EC 138/2025**) e a "
         "**responsabilidade objetiva** do Estado, que interessa diretamente ao policial."),

    h2("1. Princípios expressos (art. 37, caput)"),
    key("Mnemônico: LIMPE",
        "**L**egalidade, **I**mpessoalidade, **M**oralidade, **P**ublicidade e **E**ficiência (esta incluída pela **EC 19/1998**). Valem para a "
        "administração **direta e indireta** de **qualquer dos Poderes** da União, dos Estados, do DF e dos Municípios."),
    tb(["Princípio", "Ideia central"], [0.22, 0.78], [
        ("Legalidade", "O administrador só pode fazer o que a **lei autoriza** (para o particular, pode tudo o que a lei não proíbe)."),
        ("Impessoalidade", "Atuação voltada ao interesse público, sem favorecimentos; os atos são do **órgão**, não do agente. Fundamenta a vedação à promoção pessoal (§ 1º)."),
        ("Moralidade", "Além de legal, o ato deve ser ético e honesto. Fundamenta a vedação ao **nepotismo** (SV 13)."),
        ("Publicidade", "Transparência dos atos, condição de eficácia; admite sigilo quando imprescindível à segurança da sociedade e do Estado."),
        ("Eficiência", "Busca de resultados com qualidade e economia de recursos."),
    ]),
    nt("**Publicidade institucional** (§ 1º): deve ter caráter **educativo, informativo ou de orientação social**, sem nomes, símbolos ou "
       "imagens que caracterizem **promoção pessoal** de autoridades ou servidores."),

    h2("2. Acesso aos cargos públicos"),
    bl("Cargos, empregos e funções são acessíveis aos **brasileiros** que preencham os requisitos da lei e aos **estrangeiros**, na forma da lei (I).",
       "A investidura depende de **concurso público de provas ou de provas e títulos**, ressalvados os **cargos em comissão** declarados em lei "
       "de **livre nomeação e exoneração** (II).",
       "**Validade do concurso**: **até 2 anos**, **prorrogável uma vez, por igual período** (III).",
       "Durante o prazo **improrrogável** previsto no edital, o aprovado será convocado **com prioridade** sobre novos concursados (IV).",
       "**Funções de confiança**: exercidas **exclusivamente** por servidores ocupantes de **cargo efetivo**. **Cargos em comissão**: "
       "preenchidos por servidores de carreira nos casos e **percentuais mínimos** da lei. Ambos destinam-se apenas a **direção, chefia e "
       "assessoramento** (V).",
       "Reserva de percentual de cargos e empregos para **pessoas com deficiência** (VIII).",
       "**Contratação temporária** para necessidade temporária de excepcional interesse público, nos casos da lei (IX).",
       "A não observância do concurso ou do prazo de validade implica a **nulidade** do ato e a punição da autoridade responsável (§ 2º)."),
    tb(["Jurisprudência", "Regra"], [0.24, 0.76], [
        ("RE 598.099", "O aprovado **dentro do número de vagas** do edital tem **direito subjetivo** à nomeação no prazo de validade."),
        ("SV 13", "**Nepotismo**: viola a Constituição nomear cônjuge, companheiro ou parente até o **3º grau** da autoridade nomeante ou de servidor da mesma "
                  "pessoa jurídica com cargo de direção, chefia ou assessoramento para cargo em comissão ou função de confiança (inclui o nepotismo cruzado)."),
        ("SV 43", "É inconstitucional o provimento, **sem concurso**, em cargo que não integra a carreira na qual o servidor foi investido (ascensão, transposição)."),
        ("SV 44", "Só por **lei** se pode sujeitar a **exame psicotécnico** a habilitação de candidato a cargo público."),
        ("Súmula 683", "O **limite de idade** só se legitima quando justificado pela natureza das atribuições do cargo."),
        ("RE 898.450", "Edital não pode vetar candidato **tatuado**, salvo tatuagem que viole valores constitucionais (ex.: apologia ao crime ou ao racismo)."),
    ]),
    trap("Pegadinha: nepotismo e cargos políticos",
         "O STF entende que a SV 13, em regra, **não alcança** a nomeação para **cargos políticos** (Ministro, Secretário de Estado ou "
         "Município), salvo fraude ou falta de qualificação. E a vedação vai até o **3º grau**, não até o 2º."),

    h2("3. Direitos coletivos, remuneração e teto"),
    bl("O servidor civil tem direito à **livre associação sindical** (VI). A **greve** é exercida nos termos de **lei específica** (VII).",
       "A remuneração e o subsídio só podem ser fixados ou alterados por **lei específica**, assegurada **revisão geral anual**, sempre na mesma "
       "data e sem distinção de índices (X).",
       "É vedada a **vinculação** ou **equiparação** de espécies remuneratórias (XIII).",
       "Os vencimentos são **irredutíveis** (XV), mas a irredutibilidade não protege valores acima do teto."),
    h3("Teto remuneratório (XI)"),
    tb(["Ente", "Teto"], [0.3, 0.7], [
        ("Geral (todos)", "**Subsídio mensal dos Ministros do STF**"),
        ("Municípios", "Subsídio do **Prefeito**"),
        ("Estados e DF, Executivo", "Subsídio do **Governador**"),
        ("Estados e DF, Legislativo", "Subsídio dos **Deputados Estaduais e Distritais**"),
        ("Estados e DF, Judiciário", "Subsídio dos **Desembargadores do TJ**, limitado a **90,25%** do subsídio dos Ministros do STF "
                                     "(aplica-se também a **membros do MP, Procuradores e Defensores Públicos**)"),
    ]),
    nt("O § 12 faculta aos Estados e ao DF fixar, por emenda à Constituição estadual, um **subteto único**: o subsídio dos Desembargadores "
       "do TJ. Para o STF, no caso de **acumulação lícita** de cargos, o teto incide sobre **cada** remuneração isoladamente (Temas 377 e 384)."),
    h3("Acumulação de cargos (XVI e XVII)"),
    key("Texto da Constituição (EC 138/2025)",
        "XVI – é vedada a acumulação remunerada de cargos públicos, exceto, quando houver **compatibilidade de horários**, observado em qualquer "
        "caso o teto: a) a de **dois cargos de professor**; b) a de **um cargo de professor com outro de qualquer natureza**; c) a de **dois "
        "cargos ou empregos privativos de profissionais de saúde**, com profissões regulamentadas."),
    bl("Até dezembro de 2025, a alínea **b** só permitia professor com cargo **técnico ou científico**. A **EC 138/2025** passou a admitir "
       "professor com cargo **de qualquer natureza**: um **policial** pode, por exemplo, acumular com um cargo de professor, havendo "
       "compatibilidade de horários.",
       "A proibição de acumular se estende a **empregos e funções** e alcança autarquias, fundações, empresas públicas, sociedades de economia "
       "mista, suas subsidiárias e controladas (XVII).",
       "**Militares estaduais** (art. 42, § 3º, EC 101/2019) também podem acumular nas hipóteses do inciso XVI, com **prevalência da atividade militar**."),
    h3("Administração indireta (XIX e XX)"),
    bl("Somente por **lei específica** poderá ser **criada autarquia** e **autorizada** a instituição de empresa pública, sociedade de economia "
       "mista e fundação. **Lei complementar** definirá as áreas de atuação das fundações.",
       "A criação de **subsidiárias** depende de **autorização legislativa**.",
       "Obras, serviços, compras e alienações são contratados mediante **licitação**, ressalvados os casos da lei (XXI)."),

    h2("4. Improbidade e responsabilidade civil do Estado"),
    key("Improbidade (§ 4º)",
        "Os atos de improbidade importarão a **suspensão dos direitos políticos**, a **perda da função pública**, a **indisponibilidade dos bens** "
        "e o **ressarcimento ao erário**, na forma e gradação previstas em lei, **sem prejuízo da ação penal** cabível."),
    bl("Desde a Lei 14.230/2021, a Lei de Improbidade (8.429/1992) exige **dolo** para todas as modalidades.",
       "A ação de ressarcimento ao erário é **imprescritível** apenas quando fundada em **ato doloso** de improbidade (STF, Tema 897)."),
    key("Responsabilidade objetiva (§ 6º)",
        "As pessoas jurídicas de **direito público** e as de **direito privado prestadoras de serviços públicos** responderão pelos danos que seus "
        "agentes, **nessa qualidade**, causarem a terceiros, assegurado o **direito de regresso** contra o responsável nos casos de **dolo ou culpa**."),
    tb(["Ponto", "Regra"], [0.3, 0.7], [
        ("Estado × vítima", "Responsabilidade **objetiva** (teoria do **risco administrativo**): basta provar ato, dano e nexo causal; dispensa culpa."),
        ("Agente × Estado", "Responsabilidade **subjetiva**: o Estado só cobra do agente (regresso) se provar **dolo ou culpa**."),
        ("Dupla garantia", "A vítima deve acionar o **Estado**, não diretamente o agente público (STF, Tema 940)."),
        ("Excludentes", "Culpa **exclusiva** da vítima, caso fortuito, força maior e fato de terceiro afastam ou atenuam a responsabilidade."),
        ("Preso", "O Estado responde pela **morte de detento** sob sua custódia (STF, Tema 592), salvo se provar que não podia evitá-la."),
        ("Concessionária", "Responde objetivamente também perante **não usuários** do serviço (ex.: pedestre atropelado por ônibus)."),
    ]),
    trap("Pegadinha da área policial",
         "Se um policial, **em serviço**, fere um terceiro por erro, a vítima cobra do **Estado** sem precisar provar culpa. O policial só "
         "responde **regressivamente**, se o Estado provar **dolo ou culpa**. Se o policial estava de folga, mas usou a **arma da corporação** "
         "ou agiu invocando a condição de policial, o STF também admite a responsabilidade do Estado."),

    h2("5. Servidor em mandato eletivo (art. 38)"),
    tb(["Mandato", "Situação do servidor"], [0.32, 0.68], [
        ("Federal, estadual ou distrital", "**Afastado** do cargo (recebe o subsídio do mandato)."),
        ("**Prefeito**", "**Afastado** do cargo, sendo-lhe facultado **optar** pela remuneração."),
        ("**Vereador**", "Havendo **compatibilidade de horários**, **acumula** as vantagens do cargo e do mandato; não havendo, aplica-se a regra do prefeito."),
    ]),
    p("Em qualquer caso de afastamento, o tempo de serviço é contado para todos os efeitos legais, **exceto** para promoção por **merecimento**."),

    h2("6. Servidores: regime e remuneração (arts. 39 e 40)"),
    bl("Membros de Poder, detentores de mandato eletivo, Ministros de Estado e Secretários são remunerados por **subsídio** em **parcela única**, "
       "vedado acréscimo de gratificações e adicionais (§ 4º).",
       "Os **servidores policiais** do art. 144 também são remunerados por **subsídio** (art. 144, § 9º).",
       "Aplicam-se aos servidores vários direitos do art. 7º: 13º, adicional noturno, salário-família, jornada de 8h/44h, repouso semanal, hora "
       "extra, férias com 1/3, licenças à gestante e paternidade (§ 3º).",
       "**Previdência** (art. 40): regime próprio, contributivo e solidário; **aposentadoria compulsória aos 75 anos**; os **policiais** "
       "podem ter idade e tempo de contribuição diferenciados, por **lei complementar** do ente (§ 4º-B)."),

    h2("7. Estabilidade (art. 41)"),
    key("Texto da Constituição",
        "Art. 41. São estáveis após **três anos de efetivo exercício** os servidores nomeados para **cargo de provimento efetivo** em virtude de "
        "**concurso público**."),
    bl("É condição para adquirir a estabilidade a **avaliação especial de desempenho** por comissão instituída para essa finalidade (§ 4º).",
       "Só têm a estabilidade do art. 41 os servidores de **cargo efetivo**. **Empregados públicos** e ocupantes de **cargo em comissão** não têm.",
       "**Estabilidade** (no serviço público) não se confunde com **efetividade** (atributo do cargo)."),
    tb(["O estável perde o cargo por…", "Base"], [0.62, 0.38], [
        ("**Sentença judicial transitada em julgado**", "Art. 41, § 1º, I"),
        ("**Processo administrativo** com ampla defesa", "Art. 41, § 1º, II"),
        ("**Avaliação periódica de desempenho**, na forma de **lei complementar**, com ampla defesa", "Art. 41, § 1º, III"),
        ("**Excesso de despesa com pessoal**, depois de cortados comissionados e não estáveis", "Art. 169, § 4º"),
    ]),
    tb(["Instituto", "O que é"], [0.24, 0.76], [
        ("Reintegração", "Invalidada por sentença a demissão do estável, ele volta ao cargo; o eventual ocupante é **reconduzido** ao cargo de "
                         "origem, sem direito a indenização, **aproveitado** em outro cargo ou posto em **disponibilidade** (§ 2º)."),
        ("Disponibilidade", "Extinto o cargo ou declarada sua desnecessidade, o estável fica em disponibilidade, com **remuneração proporcional "
                            "ao tempo de serviço**, até seu adequado **aproveitamento** em outro cargo (§ 3º)."),
    ]),
]

QUIZ = quiz([
    ("C", "Os princípios da legalidade, impessoalidade, moralidade, publicidade e eficiência aplicam-se à administração direta e indireta de qualquer dos Poderes da União, dos estados, do DF e dos municípios.",
     "É o caput do art. 37."),
    ("E", "O prazo de validade do concurso público será de até dois anos, prorrogável por duas vezes, por igual período.",
     "A prorrogação é admitida uma única vez."),
    ("C", "As funções de confiança são exercidas exclusivamente por servidores ocupantes de cargo efetivo.",
     "Art. 37, V."),
    ("E", "Os cargos em comissão destinam-se às atribuições de direção, chefia, assessoramento e execução de atividades técnicas.",
     "Destinam-se apenas a direção, chefia e assessoramento."),
    ("C", "O teto remuneratório no âmbito dos municípios é o subsídio do prefeito.",
     "Art. 37, XI."),
    ("E", "A remuneração dos servidores públicos pode ser fixada por decreto do chefe do Poder Executivo, desde que respeitado o teto.",
     "A fixação ou alteração exige lei específica (art. 37, X)."),
    ("C", "Somente por lei específica poderá ser criada autarquia.",
     "Art. 37, XIX. Para empresa pública, sociedade de economia mista e fundação, a lei autoriza a instituição."),
    ("E", "São estáveis após dois anos de efetivo exercício os servidores nomeados para cargo efetivo em virtude de concurso público.",
     "O prazo é de três anos (art. 41, desde a EC 19/1998)."),
    ("C", "O servidor público estável pode perder o cargo mediante procedimento de avaliação periódica de desempenho, na forma de lei complementar, assegurada ampla defesa.",
     "Art. 41, § 1º, III."),
    ("E", "O servidor investido no mandato de prefeito pode acumular as vantagens do cargo com a remuneração do mandato, havendo compatibilidade de horários.",
     "O prefeito é afastado e pode optar pela remuneração; a acumulação com compatibilidade de horários é regra do vereador."),

    ("C", "À luz do texto constitucional, após a Emenda Constitucional 138/2025, um policial civil pode acumular seu cargo com o de professor de escola pública estadual, desde que haja compatibilidade de horários e se observe o teto remuneratório.",
     "A alínea b do art. 37, XVI, passou a admitir cargo de professor com outro de qualquer natureza."),
    ("E", "Um agente de polícia federal pode acumular seu cargo com o de técnico administrativo de um tribunal, desde que comprovada a compatibilidade de horários.",
     "Nenhum dos dois cargos é de professor ou privativo de profissional de saúde; a acumulação é vedada."),
    ("C", "Durante uma perseguição, um policial em serviço atingiu por erro um transeunte. Nessa situação, o Estado responde objetivamente pelo dano, sendo dispensável à vítima comprovar culpa do agente.",
     "Art. 37, § 6º: responsabilidade objetiva, na modalidade do risco administrativo."),
    ("E", "A vítima de dano causado por policial no exercício da função pode escolher entre acionar diretamente o agente ou o Estado, já que ambos respondem objetivamente.",
     "Pela tese da dupla garantia (Tema 940), a ação deve ser proposta contra o Estado; o agente responde apenas regressivamente, por dolo ou culpa."),
    ("C", "Viola a Constituição a nomeação do sobrinho do secretário de segurança pública para cargo em comissão na mesma secretaria.",
     "Sobrinho é parente de 3º grau; aplica-se a SV 13."),
    ("E", "O edital de concurso para a polícia militar pode vedar a participação de candidatos com qualquer tatuagem visível, em nome da disciplina militar.",
     "O STF (RE 898.450) só admite restrição a tatuagens que violem valores constitucionais."),
    ("C", "A exigência de exame psicotécnico em concurso para cargo policial depende de previsão em lei.",
     "SV 44."),
    ("E", "O candidato aprovado fora do número de vagas previsto no edital tem direito subjetivo à nomeação durante o prazo de validade do concurso.",
     "O direito subjetivo é do aprovado dentro do número de vagas (RE 598.099)."),
    ("C", "O Estado responde objetivamente pela morte de preso sob sua custódia, salvo se demonstrar que não podia evitá-la.",
     "STF, Tema 592."),
    ("E", "A ação de ressarcimento ao erário é imprescritível em qualquer hipótese de dano causado por agente público.",
     "Para o STF, só é imprescritível quando fundada em ato doloso de improbidade (Tema 897)."),
], 20)

SOURCES = [
    "Constituição da República Federativa do Brasil de 1988, arts. 37 a 42, 144, § 9º, e 169; EC 19/1998, 101/2019, 103/2019 e 138/2025.",
    "Supremo Tribunal Federal: Súmulas Vinculantes 13, 43 e 44; Súmula 683; RE 598.099; RE 898.450; Temas 377, 384, 592, 897 e 940.",
    "Lei 8.429/1992, alterada pela Lei 14.230/2021 (improbidade administrativa).",
    SRC_A,
]
