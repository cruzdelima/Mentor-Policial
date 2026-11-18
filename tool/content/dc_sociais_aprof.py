# -*- coding: utf-8 -*-
"""Direito Constitucional · Direitos sociais (arts. 6º a 11) — MATERIAL APROFUNDADO."""
from common import *

MATERIAL = material(
    "dc-sociais-02", "DC", "DC-04", "aprofundado", "Direitos sociais (arts. 6º a 11)", "Direito Constitucional · Direitos fundamentais",
    "constitucional_sociais_aprofundado", "Constitucional_Direitos_Sociais_APROFUNDADO.pdf", None, ["Direitos", "sociais"],
    ["Rol do art. 6º, direitos dos trabalhadores, liberdade sindical e greve, inclusive", "a greve na segurança pública, com 20 questões no estilo Cebraspe."],
    [("01", "Art. 6º", "rol, renda básica, mínimo existencial"),
     ("02", "Art. 7º", "direitos dos trabalhadores urbanos e rurais"),
     ("03", "Arts. 8º e 9º", "sindicato e greve"),
     ("04", "Segurança pública", "greve de policiais e militares"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Direitos sociais (arts. 6º a 11) — Direito Constitucional",
    "Base: Constituição Federal de 1988, jurisprudência do STF e doutrina.", 90)

THEORY = [
    exam("Como estudar este material",
         "Direitos sociais são direitos de **2ª dimensão**: exigem que o Estado **faça** algo (prestações). A banca cobra o **rol do art. 6º** "
         "com itens trocados, os números do **art. 7º** (horas, dias, percentuais) e, em provas policiais, a **proibição de greve** para quem "
         "atua na segurança pública."),

    h2("1. Art. 6º: o rol dos direitos sociais"),
    key("Texto da Constituição",
        "Art. 6º São direitos sociais a **educação**, a **saúde**, a **alimentação**, o **trabalho**, a **moradia**, o **transporte**, o **lazer**, "
        "a **segurança**, a **previdência social**, a **proteção à maternidade e à infância**, a **assistência aos desamparados**, na forma desta Constituição."),
    tb(["Direito", "Incluído por"], [0.5, 0.5], [
        ("Moradia", "EC 26/2000"),
        ("Alimentação", "EC 64/2010"),
        ("Transporte", "EC 90/2015"),
        ("Renda básica familiar (parágrafo único)", "EC 114/2021"),
    ]),
    p("O **parágrafo único** (EC 114/2021) garante a **todo brasileiro em situação de vulnerabilidade social** o direito a uma **renda básica "
      "familiar**, paga pelo poder público em **programa permanente de transferência de renda**, nos termos da lei."),
    trap("Pegadinha: o que não está no art. 6º",
         "**Cultura**, **esporte**, **meio ambiente**, **igualdade** e **propriedade** **não** estão no rol do art. 6º (estão em outros "
         "artigos da Constituição). A banca também cita “**segurança pública**”: o art. 6º fala apenas em **segurança**."),
    h3("Conceitos ligados aos direitos sociais"),
    tb(["Conceito", "Significado"], [0.28, 0.72], [
        ("Reserva do possível", "O Estado só pode cumprir as prestações dentro dos **recursos disponíveis**. Não pode ser usada como desculpa genérica."),
        ("Mínimo existencial", "Núcleo básico de condições para uma vida digna. Não pode ser negado com base na reserva do possível."),
        ("Vedação do retrocesso", "Direitos sociais já concretizados não podem ser simplesmente suprimidos sem alternativa."),
        ("Controle judicial", "O Judiciário pode determinar ao Executivo a implementação de políticas públicas essenciais (ex.: vagas em creche) sem violar a separação dos Poderes."),
    ]),

    h2("2. Art. 7º: direitos dos trabalhadores"),
    p("O art. 7º lista direitos dos trabalhadores **urbanos e rurais**, “além de outros que visem à melhoria de sua condição social”. Os números são "
      "os mais cobrados:"),
    tb(["Direito", "Regra"], [0.36, 0.64], [
        ("Salário mínimo (IV)", "Fixado em **lei**, **nacionalmente unificado**, reajustes periódicos; **vedada sua vinculação** para qualquer fim."),
        ("Irredutibilidade do salário (VI)", "Salvo o disposto em **convenção ou acordo coletivo**."),
        ("13º salário (VIII)", "Com base na remuneração integral ou no valor da aposentadoria."),
        ("Participação nos lucros (XI)", "**Desvinculada da remuneração**; excepcionalmente, participação na gestão."),
        ("Salário-família (XII)", "Para o dependente do trabalhador de **baixa renda**."),
        ("Jornada (XIII)", "Até **8 horas diárias** e **44 semanais**, facultada compensação e redução por acordo ou convenção."),
        ("Turnos ininterruptos (XIV)", "Jornada de **6 horas**, salvo negociação coletiva."),
        ("Repouso semanal (XV)", "Remunerado, **preferencialmente aos domingos**."),
        ("Hora extra (XVI)", "Remuneração superior, **no mínimo, em 50%** à do normal."),
        ("Férias (XVII)", "Anuais remuneradas com, **pelo menos, um terço a mais** do salário normal."),
        ("Licença à gestante (XVIII)", "**120 dias**, sem prejuízo do emprego e do salário."),
        ("Licença-paternidade (XIX)", "Nos termos da lei. A **Lei 15.371/2026** a fixou em **10 dias em 2027**, **15 em 2028** e **20 a partir de 2029** (antes, 5 dias pelo ADCT)."),
        ("Aviso prévio (XXI)", "**Proporcional** ao tempo de serviço, **no mínimo 30 dias**."),
        ("Creche e pré-escola (XXV)", "Assistência gratuita aos filhos e dependentes **até 5 anos** de idade."),
        ("Prescrição (XXIX)", "**5 anos** para os créditos, até o limite de **2 anos** após a extinção do contrato."),
        ("Menores (XXXIII)", "Proibido trabalho **noturno, perigoso ou insalubre** a menores de **18**; qualquer trabalho a menores de **16**, salvo **aprendiz**, a partir de **14**."),
    ]),
    bl("Também são direitos: proteção contra **despedida arbitrária** (lei complementar, com indenização compensatória), **seguro-desemprego**, "
       "**FGTS**, adicional **noturno**, adicionais de **insalubridade e periculosidade**, **aposentadoria**, reconhecimento de **convenções e "
       "acordos coletivos** e seguro contra acidentes de trabalho.",
       "São proibidas diferenças de salários, de funções e de critério de admissão por motivo de **sexo, idade, cor ou estado civil** (XXX) e "
       "qualquer discriminação ao trabalhador **com deficiência** (XXXI).",
       "O trabalhador **avulso** tem igualdade de direitos com o de vínculo permanente (XXXIV). Os **domésticos** têm boa parte desses direitos "
       "(parágrafo único, ampliado pela EC 72/2013)."),
    key("Números para decorar",
        "**8 e 44** horas · **6** horas no turno ininterrupto · hora extra **+50%** · férias **+1/3** · gestante **120 dias** · aviso **30 dias** · "
        "creche **até 5 anos** · prescrição **5 anos / 2 anos** · aprendiz **14**, trabalho **16**, noturno **18**."),

    h2("3. Art. 8º: liberdade sindical"),
    bl("É livre a associação profissional ou sindical. A lei **não pode exigir autorização do Estado** para fundar sindicato, ressalvado o "
       "**registro** no órgão competente.",
       "**Unicidade sindical**: é vedada a criação de **mais de uma** organização sindical representativa da mesma categoria na **mesma base "
       "territorial**, que **não pode ser inferior à área de um Município**.",
       "**Ninguém** será obrigado a filiar-se ou a manter-se filiado.",
       "É **obrigatória** a participação dos sindicatos nas **negociações coletivas** de trabalho.",
       "O **aposentado filiado** tem direito a votar e ser votado.",
       "**Estabilidade do dirigente**: é vedada a dispensa do empregado sindicalizado a partir do **registro da candidatura** a cargo de direção "
       "e, se eleito, até **1 ano após o final do mandato**, salvo **falta grave**.",
       "A **contribuição confederativa** só é exigível dos **filiados** (Súmula Vinculante 40)."),

    h2("4. Art. 9º: direito de greve"),
    key("Texto da Constituição",
        "Art. 9º É assegurado o direito de greve, competindo aos **trabalhadores** decidir sobre a **oportunidade** de exercê-lo e sobre os "
        "**interesses** que devam por meio dele defender. § 1º A lei definirá os **serviços ou atividades essenciais** e disporá sobre o "
        "atendimento das necessidades inadiáveis da comunidade. § 2º Os **abusos** cometidos sujeitam os responsáveis às penas da lei."),
    tb(["Quem", "Greve"], [0.32, 0.68], [
        ("Trabalhador da iniciativa privada", "Direito assegurado (art. 9º; Lei 7.783/1989)."),
        ("Servidor público civil", "Exercido nos termos de **lei específica** (art. 37, VII). Como a lei não veio, aplica-se a lei do setor privado (MI 670, 708 e 712)."),
        ("**Policial civil** e demais servidores que atuam **diretamente na segurança pública**", "**Vedada** sob qualquer forma (STF, ARE 654.432, Tema 541). O poder público deve participar de mediação com a categoria."),
        ("**Militares** (Forças Armadas, PM e bombeiros)", "**Proibidas a sindicalização e a greve** (art. 142, § 3º, IV, aplicado aos militares estaduais pelo art. 42, § 1º)."),
    ]),
    trap("Pegadinha da área policial",
         "A Constituição proíbe expressamente greve e sindicalização dos **militares**. Para os **policiais civis**, a proibição de greve vem "
         "do **STF**, não do texto constitucional. Os policiais civis **podem** se sindicalizar."),

    h2("5. Arts. 10 e 11: participação dos trabalhadores"),
    bl("**Art. 10**: é assegurada a participação dos trabalhadores e empregadores nos **colegiados dos órgãos públicos** em que seus interesses "
       "profissionais ou previdenciários sejam objeto de discussão e deliberação.",
       "**Art. 11**: nas empresas de **mais de 200 empregados**, é assegurada a eleição de **um representante** destes para promover o "
       "entendimento direto com os empregadores."),
]

QUIZ = quiz([
    ("C", "O transporte foi incluído entre os direitos sociais do art. 6º da Constituição por emenda constitucional.",
     "Foi incluído pela EC 90/2015."),
    ("E", "A cultura e o meio ambiente integram o rol de direitos sociais do art. 6º da Constituição Federal.",
     "Não estão no art. 6º; são tratados em outros capítulos."),
    ("C", "A Constituição assegura renda básica familiar a todo brasileiro em situação de vulnerabilidade social, por meio de programa permanente de transferência de renda.",
     "É o parágrafo único do art. 6º (EC 114/2021)."),
    ("E", "A Constituição admite a vinculação do salário mínimo para fins de reajuste de benefícios e contratos.",
     "É vedada a vinculação do salário mínimo para qualquer fim."),
    ("C", "A remuneração do serviço extraordinário deve ser superior, no mínimo, em cinquenta por cento à do normal.",
     "Art. 7º, XVI."),
    ("E", "A jornada normal de trabalho não pode ser superior a oito horas diárias e quarenta horas semanais.",
     "O limite semanal é de 44 horas."),
    ("C", "É proibido qualquer trabalho a menores de dezesseis anos, salvo na condição de aprendiz, a partir de quatorze anos.",
     "Art. 7º, XXXIII."),
    ("E", "A lei pode exigir autorização do Estado para a fundação de sindicato, desde que fundada em critérios objetivos.",
     "A lei não pode exigir autorização; ressalva-se apenas o registro no órgão competente."),
    ("C", "É vedada a criação de mais de uma organização sindical representativa da mesma categoria na mesma base territorial, que não pode ser inferior à área de um município.",
     "É a unicidade sindical do art. 8º, II."),
    ("E", "Nas empresas com mais de cem empregados, a Constituição assegura a eleição de um representante destes para promover o entendimento direto com os empregadores.",
     "O art. 11 fala em empresas com mais de duzentos empregados."),

    ("C", "Um sindicato de policiais civis decidiu paralisar as atividades da categoria por tempo indeterminado. Conforme o entendimento do STF, essa paralisação é vedada, por se tratar de servidores que atuam diretamente na área de segurança pública.",
     "STF, ARE 654.432 (Tema 541): o exercício do direito de greve é vedado aos policiais civis."),
    ("E", "A Constituição Federal proíbe expressamente a sindicalização dos policiais civis.",
     "A vedação expressa de sindicalização e greve atinge os militares. Policiais civis podem se sindicalizar; a proibição de greve decorre do STF."),
    ("C", "Aos militares dos estados aplicam-se as proibições de sindicalização e de greve previstas para os membros das Forças Armadas.",
     "Art. 142, § 3º, IV, combinado com o art. 42, § 1º."),
    ("E", "O direito de greve dos servidores públicos civis é exercido nos termos de lei complementar, de modo que, enquanto esta não for editada, a greve é proibida.",
     "A Constituição exige lei específica (ordinária). Na falta dela, o STF mandou aplicar a lei de greve do setor privado."),
    ("C", "A contribuição confederativa só é exigível dos filiados ao sindicato respectivo.",
     "Súmula Vinculante 40."),
    ("E", "O empregado eleito para cargo de direção sindical tem estabilidade até dois anos após o final do mandato, salvo se cometer falta grave.",
     "A estabilidade vai até um ano após o final do mandato."),
    ("C", "A alegação genérica de falta de recursos (reserva do possível) não basta para afastar a obrigação do Estado de garantir o mínimo existencial.",
     "O mínimo existencial prevalece sobre a invocação genérica da reserva do possível."),
    ("E", "Considere que um trabalhador tenha sido demitido há três anos. Nesse caso, ele ainda pode cobrar judicialmente créditos dos últimos cinco anos do contrato, pois a prescrição trabalhista é de cinco anos.",
     "Após a extinção do contrato, a ação deve ser proposta em até dois anos."),
    ("C", "A Constituição proíbe diferença de salários, de exercício de funções e de critério de admissão por motivo de sexo, idade, cor ou estado civil.",
     "Art. 7º, XXX."),
    ("E", "A participação nos lucros ou resultados integra a remuneração do empregado para todos os efeitos legais.",
     "A Constituição a prevê desvinculada da remuneração."),
], 20)

SOURCES = [
    "Constituição da República Federativa do Brasil de 1988, arts. 6º a 11, 37, VII, 42 e 142, § 3º; ADCT, art. 10, § 1º.",
    "Lei 15.371/2026 (licença-paternidade e salário-paternidade); Lei 7.783/1989 (greve).",
    "Supremo Tribunal Federal: ARE 654.432 (Tema 541); MI 670, 708 e 712; Súmula Vinculante 40.",
    SRC_A,
]
