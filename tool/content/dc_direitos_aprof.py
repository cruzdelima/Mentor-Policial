# -*- coding: utf-8 -*-
"""Direito Constitucional · Direitos e deveres individuais e coletivos (art. 5º) — MATERIAL APROFUNDADO."""
from common import *

MATERIAL = material(
    "dc-direitos-02", "DC", "DC-02", "aprofundado", "Direitos e deveres individuais e coletivos (art. 5º)",
    "Direito Constitucional · Direitos fundamentais",
    "constitucional_direitos_aprofundado", "Constitucional_Direitos_Individuais_APROFUNDADO.pdf", None,
    ["Direitos", "individuais e coletivos"],
    ["Teoria completa do art. 5º: liberdades, domicílio, sigilo e garantias penais,", "com os julgados do STF e 20 questões no estilo Cebraspe."],
    [("01", "Teoria geral", "características, destinatários, §§ 1º a 4º"),
     ("02", "Liberdades", "expressão, crença, reunião, associação"),
     ("03", "Privacidade", "domicílio, sigilo, dados pessoais"),
     ("04", "Garantias penais", "crimes inafiançáveis, penas, extradição"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Direitos e deveres individuais e coletivos — Direito Constitucional",
    "Base: Constituição Federal de 1988, jurisprudência do STF e doutrina.", 240)

THEORY = [
    exam("Como estudar este material",
         "O art. 5º tem **79 incisos** e é o artigo mais cobrado da Constituição em provas policiais. A banca troca palavras da letra da lei "
         "(**dia** por **noite**, **autorização** por **aviso**, **inafiançável** por **imprescritível**) e cobra os julgados do STF que "
         "afetam o trabalho policial: entrada em domicílio, interceptação, algemas e prova ilícita. Leia o art. 5º inteiro ao menos uma vez."),

    h2("1. Teoria geral dos direitos fundamentais"),
    p("O **Título II** da Constituição (arts. 5º a 17) reúne os direitos e garantias fundamentais em cinco grupos: direitos **individuais e "
      "coletivos** (art. 5º), **sociais** (arts. 6º a 11), **nacionalidade** (arts. 12 e 13), **direitos políticos** (arts. 14 a 16) e "
      "**partidos políticos** (art. 17)."),
    tb(["Característica", "O que significa"], [0.28, 0.72], [
        ("Universalidade", "Pertencem a todos os seres humanos, sem discriminação."),
        ("Relatividade", "Nenhum direito é absoluto: podem ceder diante de outro direito no caso concreto (ponderação)."),
        ("Irrenunciabilidade", "O titular pode deixar de exercer, mas não pode renunciar ao direito."),
        ("Inalienabilidade", "Não podem ser vendidos nem transferidos."),
        ("Imprescritibilidade", "Não se perdem pelo passar do tempo."),
        ("Historicidade", "Surgem e se ampliam ao longo da história (as “gerações” ou “dimensões”)."),
    ]),
    tb(["Dimensão", "Valor", "Exemplos"], [0.18, 0.22, 0.6], [
        ("1ª", "Liberdade", "Direitos civis e políticos: vida, liberdade, propriedade, voto. Exigem **abstenção** do Estado."),
        ("2ª", "Igualdade", "Direitos sociais, econômicos e culturais: saúde, educação, trabalho. Exigem **prestação** do Estado."),
        ("3ª", "Fraternidade", "Direitos difusos: meio ambiente, paz, desenvolvimento, consumidor."),
    ]),
    h3("Quem é titular"),
    bl("O caput fala em **brasileiros e estrangeiros residentes no País**, mas o STF estende os direitos fundamentais também ao "
       "**estrangeiro não residente** (o turista, o estrangeiro em trânsito): ele pode, por exemplo, impetrar habeas corpus.",
       "**Pessoas jurídicas** também são titulares dos direitos compatíveis com a sua natureza (propriedade, sigilo, devido processo).",
       "Os direitos fundamentais valem também nas **relações entre particulares** (**eficácia horizontal**). O STF anulou a exclusão de sócio "
       "de associação feita sem direito de defesa (RE 201.819)."),
    h3("Os quatro parágrafos do art. 5º"),
    tb(["Parágrafo", "Regra"], [0.14, 0.86], [
        ("§ 1º", "As normas definidoras de direitos e garantias fundamentais têm **aplicação imediata**."),
        ("§ 2º", "O rol **não é taxativo**: há direitos decorrentes do regime, dos princípios e dos **tratados internacionais**."),
        ("§ 3º", "Tratados de **direitos humanos** aprovados em **cada Casa** do Congresso, em **dois turnos**, por **três quintos** dos votos, "
                 "equivalem às **emendas constitucionais**."),
        ("§ 4º", "O Brasil se submete à jurisdição do **Tribunal Penal Internacional** a cuja criação tenha manifestado adesão."),
    ]),
    key("Hierarquia dos tratados",
        "Tratado de direitos humanos com o rito do § 3º = **emenda constitucional** (ex.: Convenção sobre os Direitos das Pessoas com Deficiência). "
        "Tratado de direitos humanos **sem** esse rito = **supralegal** (acima das leis, abaixo da Constituição; ex.: Pacto de São José). "
        "Demais tratados = **lei ordinária**. Por causa do Pacto de São José, é ilícita a prisão civil do depositário infiel (**Súmula Vinculante 25**)."),

    h2("2. Caput, igualdade e legalidade"),
    key("Texto da Constituição",
        "Art. 5º Todos são iguais perante a lei, sem distinção de qualquer natureza, garantindo-se aos brasileiros e aos estrangeiros residentes "
        "no País a inviolabilidade do direito à **vida**, à **liberdade**, à **igualdade**, à **segurança** e à **propriedade** (…)"),
    bl("**Igualdade (I)**: homens e mulheres são iguais em direitos e obrigações. A igualdade é **material**: tratar desigualmente os "
       "desiguais na medida da desigualdade. Por isso são válidas as **ações afirmativas** (cotas raciais, ADPF 186).",
       "Concurso público pode fixar **limite de idade** ou exigência física quando a natureza do cargo justificar e a exigência estiver em **lei** "
       "(Súmula 683 do STF).",
       "**Legalidade (II)**: ninguém será obrigado a fazer ou deixar de fazer alguma coisa **senão em virtude de lei**. Para o particular, "
       "tudo o que a lei não proíbe é permitido."),

    h2("3. Liberdades"),
    tb(["Inciso", "Regra", "Atenção"], [0.1, 0.5, 0.4], [
        ("III", "Ninguém será submetido a **tortura** nem a tratamento desumano ou degradante.", "Proibição absoluta na prática."),
        ("IV", "É livre a manifestação do pensamento, sendo **vedado o anonimato**.", "A denúncia anônima, sozinha, não basta para instaurar inquérito: a polícia deve fazer diligências preliminares."),
        ("V", "Direito de **resposta**, proporcional ao agravo, além de indenização por dano material, moral ou à imagem.", ""),
        ("VI a VIII", "Liberdade de **consciência e de crença**; assistência religiosa em entidades de internação coletiva; **escusa de consciência**.",
         "Quem se recusa a cumprir obrigação legal a todos imposta e também a prestação alternativa pode ter **direitos políticos** atingidos (art. 15, IV)."),
        ("IX", "Expressão intelectual, artística, científica e de comunicação, **independentemente de censura ou licença**.", ""),
        ("X", "São invioláveis a **intimidade**, a **vida privada**, a **honra** e a **imagem**.", "Assegura indenização por dano material ou moral."),
        ("XIII", "Livre exercício de **profissão**, atendidas as qualificações que a **lei** estabelecer.", "Norma de eficácia contida."),
        ("XV", "Livre **locomoção** no território nacional em **tempo de paz**.", "Pode entrar, permanecer ou sair com seus bens, nos termos da lei."),
    ]),
    h3("Reunião (XVI)"),
    key("Texto da Constituição",
        "Todos podem reunir-se **pacificamente, sem armas**, em locais **abertos ao público**, **independentemente de autorização**, desde que não "
        "frustrem outra reunião anteriormente convocada para o mesmo local, sendo apenas exigido **prévio aviso** à autoridade competente."),
    trap("Pegadinha: aviso não é autorização",
         "A banca troca **prévio aviso** por **prévia autorização**. Errado. A finalidade do aviso é permitir que o poder público organize o "
         "trânsito e a segurança. O STF validou a “Marcha da Maconha” como exercício da liberdade de reunião e de expressão (ADPF 187)."),
    h3("Associação (XVII a XXI)"),
    bl("É plena a liberdade de associação para **fins lícitos**, vedada a de **caráter paramilitar**.",
       "A criação de associações e, na forma da lei, a de cooperativas **independe de autorização**, vedada a interferência estatal.",
       "Dissolução compulsória: só por **decisão judicial transitada em julgado**. Suspensão das atividades: basta **decisão judicial**.",
       "Ninguém será compelido a associar-se ou a permanecer associado.",
       "As entidades associativas, **quando expressamente autorizadas**, têm legitimidade para representar seus filiados judicial ou extrajudicialmente."),
    tb(["Medida", "Exige"], [0.5, 0.5], [
        ("Suspender atividades", "Decisão judicial (basta liminar)"),
        ("Dissolver compulsoriamente", "Decisão judicial **transitada em julgado**"),
    ]),

    h2("4. Privacidade: domicílio, sigilo e dados"),
    key("Inviolabilidade do domicílio (XI)",
        "A casa é **asilo inviolável** do indivíduo, ninguém nela podendo penetrar sem consentimento do morador, **salvo** em caso de "
        "**flagrante delito** ou **desastre**, ou para **prestar socorro**, ou, **durante o dia**, por **determinação judicial**."),
    tb(["Situação", "Quando pode entrar"], [0.5, 0.5], [
        ("Consentimento do morador", "Dia ou noite"),
        ("Flagrante delito", "Dia ou noite"),
        ("Desastre", "Dia ou noite"),
        ("Prestar socorro", "Dia ou noite"),
        ("Ordem judicial", "**Somente durante o dia**"),
    ]),
    bl("**Casa** tem sentido amplo: inclui o **escritório** profissional fechado ao público, o **quarto de hotel ocupado** e o trailer usado "
       "como moradia. Não inclui bar ou loja na parte aberta ao público.",
       "**Fundadas razões (RE 603.616, Tema 280)**: a entrada forçada **sem mandado** é lícita, mesmo à noite, quando amparada em **fundadas "
       "razões**, devidamente **justificadas a posteriori**, que indiquem que dentro da casa ocorre **situação de flagrante delito**. "
       "Sem essas razões, há responsabilidade do agente e **nulidade** das provas.",
       "Nos **crimes permanentes** (tráfico na modalidade *ter em depósito*, posse ilegal de arma), o flagrante se prolonga no tempo."),
    trap("Pegadinha: dia e noite",
         "Só a **ordem judicial** fica restrita ao **dia**. Flagrante, desastre e socorro autorizam a entrada **a qualquer hora**. A banca "
         "também afirma que “a autoridade policial pode determinar a busca domiciliar”: errado, a busca por ordem exige **juiz** "
         "(cláusula de reserva de jurisdição)."),
    key("Sigilo das comunicações (XII)",
        "É inviolável o sigilo da **correspondência** e das comunicações **telegráficas**, de **dados** e das comunicações **telefônicas**, "
        "**salvo, no último caso**, por **ordem judicial**, nas hipóteses e na forma que a **lei** estabelecer, para fins de **investigação "
        "criminal** ou **instrução processual penal**."),
    bl("A interceptação telefônica é regulada pela **Lei 9.296/1996** e só cabe na esfera **penal**. A prova obtida licitamente pode ser "
       "**emprestada** a processo administrativo disciplinar.",
       "**CPI** pode quebrar sigilo **bancário, fiscal e de dados telefônicos** (registros de ligações), mas **não** pode determinar "
       "**interceptação** telefônica: isso é reserva de jurisdição.",
       "Gravação de conversa feita por **um dos interlocutores** sem o conhecimento do outro é prova lícita.",
       "Nenhuma liberdade pública é absoluta: o sigilo de correspondência pode ceder, por exemplo, na interceptação de cartas de presos por "
       "motivo de segurança, com base na lei."),
    p("A **EC 115/2022** incluiu o inciso **LXXIX**: é assegurado o direito à **proteção dos dados pessoais**, inclusive nos meios digitais."),

    h2("5. Propriedade"),
    bl("É garantido o direito de propriedade (XXII), que atenderá a sua **função social** (XXIII).",
       "**Desapropriação** (XXIV): por necessidade ou utilidade pública, ou por interesse social, mediante **justa e prévia indenização em dinheiro**, "
       "ressalvados os casos da Constituição (reforma agrária e política urbana, pagas em títulos).",
       "**Requisição** (XXV): no caso de **iminente perigo público**, a autoridade pode usar a propriedade particular, assegurada **indenização "
       "ulterior, se houver dano**.",
       "A **pequena propriedade rural** trabalhada pela família não será objeto de penhora por débitos de sua atividade produtiva (XXVI)."),
    tb(["", "Desapropriação", "Requisição"], [0.24, 0.38, 0.38], [
        ("Efeito", "Transfere a propriedade", "Apenas usa o bem"),
        ("Indenização", "Prévia, justa e em dinheiro (regra)", "Posterior, e só se houver dano"),
    ]),

    h2("6. Garantias penais e processuais"),
    tb(["Inciso", "Garantia"], [0.12, 0.88], [
        ("XXXV", "A lei não excluirá da apreciação do Poder Judiciário lesão ou ameaça a direito (**inafastabilidade**)."),
        ("XXXVI", "A lei não prejudicará o **direito adquirido**, o **ato jurídico perfeito** e a **coisa julgada**."),
        ("XXXVII", "Não haverá juízo ou tribunal de **exceção**."),
        ("XXXVIII", "**Júri**: plenitude de defesa, sigilo das votações, soberania dos veredictos e competência para os **crimes dolosos contra a vida**."),
        ("XXXIX", "Não há crime sem **lei anterior** que o defina, nem pena sem prévia cominação legal."),
        ("XL", "A lei penal não retroagirá, **salvo para beneficiar** o réu."),
        ("XLV", "Nenhuma pena passará da pessoa do condenado (a obrigação de reparar o dano e o perdimento de bens podem alcançar os sucessores, até o limite do patrimônio transferido)."),
        ("LIII", "Ninguém será processado nem sentenciado senão pela **autoridade competente** (juiz natural)."),
        ("LIV e LV", "**Devido processo legal**; **contraditório** e **ampla defesa**, inclusive no processo administrativo."),
        ("LVI", "São inadmissíveis as provas obtidas por **meios ilícitos** (e, em regra, as delas derivadas)."),
        ("LVII", "Ninguém será considerado culpado até o **trânsito em julgado** de sentença penal condenatória."),
        ("LVIII", "O **civilmente identificado** não será submetido a identificação criminal, **salvo nas hipóteses previstas em lei**."),
        ("LXXVIII", "**Razoável duração do processo**, no âmbito judicial e administrativo."),
    ]),
    h3("Crimes com tratamento mais severo"),
    tb(["Crime", "Inafiançável", "Imprescritível", "Sem graça ou anistia"], [0.4, 0.2, 0.2, 0.2], [
        ("**Racismo** (XLII)", "Sim", "Sim", "—"),
        ("**Ação de grupos armados** contra a ordem constitucional e o Estado Democrático (XLIV)", "Sim", "Sim", "—"),
        ("**Tortura, tráfico, terrorismo e hediondos** (XLIII)", "Sim", "**Não**", "Sim"),
    ]),
    key("Mnemônico",
        "**RAÇÃO** é imprescritível: **RA**cismo e **AÇÃO** de grupos armados. **3TH** (tortura, tráfico, terrorismo e hediondos) são "
        "inafiançáveis e insuscetíveis de graça ou anistia, mas **prescrevem**. O racismo ainda é punido com **reclusão**. O STF equiparou a "
        "**injúria racial** ao racismo (HC 154.248) e enquadrou a **homotransfobia** na Lei do Racismo (ADO 26)."),
    h3("Penas"),
    bl("**Penas vedadas (XLVII)**: de **morte** (salvo em caso de **guerra declarada**), de caráter **perpétuo**, de **trabalhos forçados**, de "
       "**banimento** e **cruéis**.",
       "**Penas admitidas (XLVI)**, entre outras: privação ou restrição da liberdade, perda de bens, multa, prestação social alternativa e "
       "suspensão ou interdição de direitos.",
       "As presidiárias têm direito de permanecer com os filhos durante o período de **amamentação** (L).",
       "A pena será cumprida em estabelecimentos distintos, de acordo com a natureza do delito, a idade e o sexo do apenado (XLVIII)."),
    h3("Extradição (LI e LII)"),
    tb(["Quem", "Pode ser extraditado?"], [0.32, 0.68], [
        ("Brasileiro **nato**", "**Nunca**."),
        ("Brasileiro **naturalizado**", "Em caso de **crime comum praticado antes da naturalização** ou de comprovado envolvimento em **tráfico** de drogas (antes ou depois)."),
        ("**Estrangeiro**", "Sim, **exceto** por crime **político** ou de **opinião**."),
    ]),
    h3("Prisão e direitos do preso"),
    bl("Ninguém será preso senão em **flagrante delito** ou por **ordem escrita e fundamentada de autoridade judiciária competente**, salvo "
       "nos casos de **transgressão militar** ou **crime propriamente militar** (LXI).",
       "A prisão e o local onde o preso se encontra serão comunicados **imediatamente** ao **juiz** e à **família** ou pessoa indicada (LXII).",
       "O preso será informado de seus direitos, entre os quais o de **permanecer calado**, sendo-lhe assegurada a assistência da família e de "
       "advogado (LXIII). Ninguém é obrigado a produzir prova contra si mesmo.",
       "O preso tem direito à **identificação dos responsáveis** por sua prisão ou por seu interrogatório policial (LXIV).",
       "A prisão ilegal será **imediatamente relaxada** pela autoridade judiciária (LXV).",
       "Não haverá **prisão civil** por dívida, salvo a do responsável pelo inadimplemento voluntário e inescusável de **pensão alimentícia** (LXVII). "
       "A do depositário infiel, embora ainda escrita no inciso, é ilícita (SV 25)."),
    nt("**Súmula Vinculante 14**: é direito do defensor ter acesso amplo aos elementos de prova **já documentados** no inquérito que digam "
       "respeito ao exercício do direito de defesa. Diligências em andamento podem ficar em sigilo."),

    h2("7. Como o Cebraspe cobra"),
    bl("Situação policial concreta: entrada em casa à noite, busca com ou sem mandado, gravação, interceptação, uso de algemas.",
       "Troca de palavras na letra da lei: aviso × autorização, dia × noite, transitada em julgado × decisão judicial.",
       "Quadro dos crimes: imprescritível × inafiançável × insuscetível de graça ou anistia.",
       "Extradição de nato, naturalizado e estrangeiro."),
]

QUIZ = quiz([
    ("C", "Os direitos fundamentais previstos no art. 5º da Constituição Federal de 1988 alcançam também o estrangeiro não residente que esteja de passagem pelo Brasil.",
     "O STF interpreta o caput de forma ampla: o estrangeiro em trânsito pode, por exemplo, impetrar habeas corpus."),
    ("E", "A Constituição exige prévia autorização da autoridade competente para que se realizem reuniões pacíficas em locais abertos ao público.",
     "Exige-se apenas prévio aviso. A reunião independe de autorização."),
    ("C", "A dissolução compulsória de uma associação depende de decisão judicial transitada em julgado; a suspensão de suas atividades pode ser determinada por decisão judicial ainda não definitiva.",
     "É a distinção do art. 5º, XIX."),
    ("E", "Por determinação judicial, a polícia pode ingressar em domicílio a qualquer hora do dia ou da noite.",
     "A entrada por determinação judicial só pode ocorrer durante o dia."),
    ("C", "Em caso de desastre ou para prestar socorro, é permitido ingressar na casa sem o consentimento do morador, inclusive durante a noite.",
     "Flagrante, desastre e socorro autorizam a entrada a qualquer hora."),
    ("E", "A interceptação de comunicações telefônicas pode ser autorizada judicialmente para instruir ação civil de improbidade administrativa.",
     "A Constituição a admite apenas para investigação criminal ou instrução processual penal."),
    ("C", "Tratados internacionais de direitos humanos aprovados em cada Casa do Congresso Nacional, em dois turnos, por três quintos dos votos dos respectivos membros, equivalem às emendas constitucionais.",
     "É a regra do art. 5º, § 3º."),
    ("E", "O crime de tortura é imprescritível, conforme dispõe expressamente a Constituição.",
     "A tortura é inafiançável e insuscetível de graça ou anistia, mas não é imprescritível. Imprescritíveis são o racismo e a ação de grupos armados."),
    ("C", "O brasileiro naturalizado pode ser extraditado por comprovado envolvimento em tráfico ilícito de entorpecentes, ainda que o fato seja posterior à naturalização.",
     "Para o tráfico, a Constituição não exige que o crime seja anterior à naturalização."),
    ("E", "A Constituição admite a pena de morte em caso de grave comoção interna, desde que decretado o estado de sítio.",
     "A única exceção é a guerra declarada."),

    ("C", "Durante patrulhamento noturno, policiais militares receberam informações concretas e verificaram movimentação típica de venda de drogas em uma residência; ao se aproximarem, viram um homem arremessar pacotes de entorpecente para dentro do imóvel. Nessa situação, o ingresso na casa sem mandado judicial é lícito, desde que as fundadas razões sejam justificadas posteriormente.",
     "O STF (RE 603.616) admite a entrada sem mandado, mesmo à noite, quando fundadas razões, justificadas a posteriori, indicarem flagrante delito."),
    ("E", "Delegado de polícia que investiga crime de roubo pode, por despacho fundamentado, determinar a busca domiciliar na casa do suspeito durante o dia, dispensando a ordem judicial em razão da urgência.",
     "A busca domiciliar por determinação está sujeita à reserva de jurisdição: só o juiz pode ordená-la."),
    ("C", "Comissão parlamentar de inquérito pode determinar a quebra do sigilo dos registros telefônicos de investigado, mas não pode autorizar a interceptação de suas comunicações telefônicas.",
     "A interceptação é cláusula de reserva de jurisdição; os registros (dados) podem ser obtidos pela CPI, por decisão fundamentada."),
    ("E", "A gravação de conversa telefônica feita por um dos interlocutores, sem o conhecimento do outro, é prova ilícita, pois viola o sigilo das comunicações.",
     "O STF considera lícita a gravação feita por um dos interlocutores, sobretudo para defesa de direito próprio."),
    ("C", "Considere que um quarto de hotel esteja ocupado por um hóspede. Nesse caso, o cômodo recebe a proteção constitucional da inviolabilidade do domicílio.",
     "O conceito constitucional de casa abrange o aposento ocupado de habitação coletiva."),
    ("E", "O racismo e o crime de terrorismo são inafiançáveis e imprescritíveis, nos termos da Constituição Federal.",
     "O terrorismo é inafiançável e insuscetível de graça ou anistia, mas não é imprescritível."),
    ("C", "O civilmente identificado pode ser submetido à identificação criminal nas hipóteses previstas em lei.",
     "O art. 5º, LVIII, ressalva os casos que a lei estabelecer."),
    ("E", "A prisão civil do depositário infiel continua admitida no ordenamento brasileiro, porque está expressamente prevista no inciso LXVII do art. 5º da Constituição.",
     "Apesar do texto, o STF a considera ilícita (SV 25), por força do status supralegal do Pacto de São José da Costa Rica."),
    ("C", "Em respeito ao direito à identificação dos responsáveis pela prisão, o preso pode exigir que lhe sejam informados os nomes dos policiais que o prenderam e dos que conduziram o seu interrogatório.",
     "É o art. 5º, LXIV."),
    ("E", "A Constituição assegura ao preso o direito de permanecer calado, mas o silêncio, no interrogatório policial, poderá ser interpretado em prejuízo de sua defesa.",
     "O silêncio é direito e não pode ser interpretado em desfavor do investigado."),
], 20)

SOURCES = [
    "Constituição da República Federativa do Brasil de 1988, art. 5º.",
    "Supremo Tribunal Federal: RE 603.616 (Tema 280); RE 466.343 e Súmula Vinculante 25; Súmula Vinculante 14; ADPF 186; ADPF 187; "
    "RE 201.819; HC 154.248; ADO 26; Súmula 683.",
    "Lei 9.296/1996 (interceptação telefônica).",
    "Doutrina de referência: Lenza, Direito constitucional; Mendes e Branco, Curso de direito constitucional.",
    SRC_A,
]
