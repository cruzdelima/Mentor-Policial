# -- coding: utf-8 --
"""Direito Constitucional · Princípios fundamentais (arts. 1º a 4º) — MATERIAL APROFUNDADO (estudo inicial)."""
from common import *

MATERIAL = {
    "id": "dc-principios-02",
    "version": "0.1.0",
    "status": "Em revisão pelo autor",
    "subjectId": "DC",
    "topicIds": ["DC-01"],
    "kind": "aprofundado",
    "title": "Princípios fundamentais (arts. 1º a 4º)",
    "subtitle": "Direito Constitucional · Título I da Constituição",
    "minutes": 150,
    "folder": "constitucional_principios_aprofundado",
    "pdf": "constitucional_principios_aprofundado.pdf",
    "outName": "Constitucional_Principios_Fundamentais_APROFUNDADO.pdf",
    "header": "Direito Constitucional · Princípios fundamentais",
    "coverKicker": "Direito Constitucional  ·  Título I da CF/88",
    "coverTitle": ["Princípios", "fundamentais"],
    "coverSub": ["Teoria completa dos arts. 1º a 4º da Constituição: fundamentos, separação dos Poderes,", "objetivos e relações internacionais, com 20 questões no estilo Cebraspe."],
    "coverItems": [("01", "Art. 1º", "república, federação, Estado Democrático de Direito e fundamentos"),
                   ("02", "Art. 2º", "separação dos Poderes, funções típicas e atípicas"),
                   ("03", "Art. 3º", "objetivos fundamentais"),
                   ("04", "Art. 4º", "princípios das relações internacionais"),
                   ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "coverTopic": "Tópico do edital: Princípios fundamentais (arts. 1º a 4º) — Direito Constitucional",
    "coverBase": "Base: Constituição Federal de 1988, jurisprudência do STF e doutrina.",
}

THEORY = [
    exam("Como estudar este material",
         "São apenas quatro artigos, mas caem em praticamente toda prova. A banca cobra de dois jeitos: a **letra da Constituição** "
         "(trocando uma lista pela outra) e os **conceitos** por trás dela (república, federação, separação dos Poderes). "
         "Leia os artigos na íntegra, entenda os conceitos, resolva as 20 questões e use o **PDF de resumo** nas revisões."),

    h2("1. O Título I da Constituição"),
    p("A Constituição de 1988 abre com o **Título I — Dos Princípios Fundamentais**, formado pelos **arts. 1º a 4º**. Eles definem que Estado é o "
      "Brasil, quem exerce o poder, como ele se organiza, aonde quer chegar e como se comporta diante de outros países."),
    tb(["Artigo", "Conteúdo", "Palavra-chave"], [0.14, 0.56, 0.3], [
        ("Art. 1º", "Forma de Estado, forma de governo, regime político e os cinco **fundamentos**", "O que o Brasil **é**"),
        ("Art. 2º", "**Poderes** da União, independentes e harmônicos", "Como o poder se **divide**"),
        ("Art. 3º", "Quatro **objetivos** fundamentais", "O que o Brasil **quer alcançar**"),
        ("Art. 4º", "Dez **princípios** das relações internacionais", "Como o Brasil **age no exterior**"),
    ]),
    nt("O **preâmbulo** vem antes do art. 1º e não faz parte do Título I. Para o STF, ele **não tem força normativa**: não cria direitos nem "
       "obrigações e não é de reprodução obrigatória nas constituições estaduais (ADI 2.076). Serve como diretriz de interpretação."),

    h2("2. Art. 1º, caput: o que o Brasil é"),
    key("Texto da Constituição",
        "Art. 1º A **República Federativa do Brasil**, formada pela **união indissolúvel** dos **Estados e Municípios e do Distrito Federal**, "
        "constitui-se em **Estado Democrático de Direito** e tem como fundamentos: (…)"),
    tb(["Pergunta", "Resposta", "Onde está"], [0.3, 0.3, 0.4], [
        ("Forma de governo", "**República**", "“República Federativa do Brasil”"),
        ("Forma de Estado", "**Federação**", "“Federativa”, “união indissolúvel”"),
        ("Regime político", "**Democracia**", "“Estado Democrático de Direito”; parágrafo único"),
        ("Sistema de governo", "**Presidencialismo**", "Não está no art. 1º; decorre dos arts. 76 e seguintes"),
    ]),
    h3("República (forma de governo)"),
    p("Forma de governo é o modo como se dá a relação entre governantes e governados. Na **república**, o poder pertence ao povo e é exercido "
      "em seu nome. Suas marcas são:"),
    bl("**Eletividade**: os governantes são escolhidos pelo povo.",
       "**Temporariedade**: os mandatos têm prazo certo.",
       "**Responsabilidade**: os governantes prestam contas e respondem por seus atos.",
       "**Representatividade**: governam em nome do povo."),
    p("A forma oposta é a **monarquia**, marcada pela hereditariedade, pela vitaliciedade e pela irresponsabilidade política do monarca."),
    h3("Federação (forma de Estado)"),
    p("Forma de Estado é o modo como o poder político se distribui no território. Na **federação**, há mais de um centro de poder: "
      "entes **autônomos** convivem sob uma mesma Constituição."),
    bl("São entes federativos a **União, os Estados, o Distrito Federal e os Municípios**, todos autônomos (art. 18).",
       "O Brasil adota um federalismo de **três níveis**: os **Municípios** são entes federativos.",
       "Os **Territórios não são entes federativos**: integram a União (art. 18, § 2º). Hoje não existe nenhum.",
       "**Autonomia** se desdobra em auto-organização, autogoverno, autoadministração e autolegislação.",
       "**Soberania** é atributo da **República Federativa do Brasil** (o Estado como um todo). A **União**, os Estados, o DF e os Municípios têm apenas **autonomia**.",
       "**Indissolúvel**: não existe direito de **secessão**. A tentativa de separação autoriza a intervenção federal (art. 34, I).",
       "A federação brasileira formou-se por **desagregação** (movimento centrífugo): um Estado unitário que se descentralizou, em 1889/1891."),
    trap("Pegadinha: quem forma a República",
         "O caput do art. 1º fala em “união indissolúvel dos **Estados e Municípios e do Distrito Federal**”. A banca inclui os **Territórios** "
         "na lista ou exclui os **Municípios**. As duas alterações tornam o item errado."),
    h3("Estado Democrático de Direito"),
    bl("**Estado de Direito**: todos, inclusive o próprio Estado, submetem-se à lei; o poder é limitado e há direitos fundamentais garantidos.",
       "**Democrático**: a lei nasce da vontade popular, e o povo participa da formação das decisões políticas.",
       "A expressão une as duas ideias: governo limitado pelo Direito e legitimado pelo povo."),
    h3("Cláusulas pétreas: o que não pode ser abolido"),
    p("O art. 60, § 4º, proíbe emenda constitucional **tendente a abolir**: a **forma federativa de Estado**; o **voto direto, secreto, universal "
      "e periódico**; a **separação dos Poderes**; e os **direitos e garantias individuais**."),
    trap("Pegadinha: república é cláusula pétrea?",
         "A **forma federativa** é cláusula pétrea expressa. A **república** e o **presidencialismo** **não** estão no art. 60, § 4º "
         "(tanto que foram submetidos a plebiscito em 1993). A forma republicana é **princípio constitucional sensível** (art. 34, VII, a), "
         "cuja violação por um Estado autoriza intervenção federal."),

    h2("3. Art. 1º, incisos: os cinco fundamentos"),
    key("Texto da Constituição",
        "I – a **soberania**; II – a **cidadania**; III – a **dignidade da pessoa humana**; IV – os **valores sociais do trabalho e da livre "
        "iniciativa**; V – o **pluralismo político**."),
    tb(["Fundamento", "Significado", "Atenção"], [0.22, 0.46, 0.32], [
        ("Soberania", "Poder supremo dentro do território (ordem interna) e independente perante os outros Estados (ordem externa).", "No art. 4º aparece como **independência nacional**."),
        ("Cidadania", "Participação do indivíduo na vida do Estado. Em sentido amplo, vai além de votar e ser votado: é o exercício dos direitos fundamentais.", "Não se limita à capacidade eleitoral."),
        ("Dignidade da pessoa humana", "A pessoa é um fim em si mesma, e não um instrumento do Estado. É o valor que dá unidade aos direitos fundamentais.", "É **fundamento**, não objetivo nem princípio do art. 4º."),
        ("Valores sociais do trabalho e da livre iniciativa", "Equilíbrio entre o trabalho humano e a liberdade de empreender. Os **dois** são valores sociais.", "A livre iniciativa também fundamenta a ordem econômica (art. 170)."),
        ("Pluralismo político", "Respeito à diversidade de ideias, opiniões, crenças e organizações na sociedade.", "É mais amplo que pluripartidarismo (art. 17). Não é “pluralismo partidário”."),
    ]),
    key("Mnemônico: SO-CI-DI-VA-PLU",
        "**SO**berania, **CI**dadania, **DI**gnidade da pessoa humana, **VA**lores sociais do trabalho e da livre iniciativa, **PLU**ralismo político. "
        "Os fundamentos são **substantivos**: é o que o Estado **já é**."),
    h3("A dignidade da pessoa humana na atividade policial"),
    p("A dignidade fundamenta várias decisões do STF que interessam diretamente ao policial. A principal é a **Súmula Vinculante 11**: "
      "“Só é lícito o uso de algemas em casos de **resistência** e de **fundado receio de fuga** ou de **perigo à integridade física própria ou "
      "alheia**, por parte do preso ou de terceiros, **justificada a excepcionalidade por escrito**, sob pena de responsabilidade disciplinar, "
      "civil e penal do agente ou da autoridade e de nulidade da prisão ou do ato processual a que se refere, sem prejuízo da responsabilidade "
      "civil do Estado.”"),
    bl("A dignidade também embasou o reconhecimento da **união estável entre pessoas do mesmo sexo** (ADI 4.277 e ADPF 132), "
       "junto com o objetivo de promover o bem de todos sem discriminação (art. 3º, IV).",
       "É fundamento da vedação à tortura e ao tratamento desumano ou degradante (art. 5º, III)."),

    h2("4. Art. 1º, parágrafo único: de quem é o poder"),
    key("Texto da Constituição",
        "Parágrafo único. **Todo o poder emana do povo**, que o exerce **por meio de representantes eleitos ou diretamente**, nos termos desta Constituição."),
    bl("O **titular** do poder é o **povo** (soberania popular).",
       "O exercício se dá de duas formas: **indireta** (representantes eleitos) e **direta**.",
       "Por combinar as duas, o Brasil adota a **democracia semidireta** ou **participativa**.",
       "Instrumentos de participação direta (art. 14): **plebiscito** (consulta **prévia** ao ato), **referendo** (consulta **posterior**, "
       "para confirmar ou rejeitar o ato) e **iniciativa popular** de lei.",
       "Outros exemplos: ação popular, tribunal do júri, participação em conselhos."),
    trap("Pegadinha: “exclusivamente”",
         "O poder **não** é exercido “exclusivamente por meio de representantes” nem “exclusivamente de forma direta”. "
         "E quem detém o poder é o **povo**, não o Estado, a nação ou o governo."),

    h2("5. Art. 2º: a separação dos Poderes"),
    key("Texto da Constituição",
        "Art. 2º São Poderes da União, **independentes e harmônicos entre si**, o **Legislativo, o Executivo e o Judiciário**."),
    p("O poder do Estado é **uno e indivisível**; o que se divide são as **funções**. A ideia, sistematizada por Montesquieu, é evitar a "
      "concentração de poder: quem faz a lei não a executa nem julga."),
    tb(["Poder", "Funções típicas", "Exemplos de funções atípicas"], [0.16, 0.34, 0.5], [
        ("Legislativo", "**Legislar** e **fiscalizar** (inclusive com o auxílio do Tribunal de Contas)", "**Julgar**: o Senado julga o Presidente por crime de responsabilidade (art. 52, I). **Administrar**: organiza seus serviços, faz concursos e licitações."),
        ("Executivo", "**Administrar** (governar, executar as leis)", "**Legislar**: edita medidas provisórias (art. 62) e leis delegadas (art. 68). **Julgar**: decide processos administrativos."),
        ("Judiciário", "**Julgar** (aplicar o Direito ao caso concreto, com definitividade)", "**Legislar**: elabora seus regimentos internos (art. 96, I, a). **Administrar**: concede férias, organiza secretarias, faz concursos."),
    ]),
    bl("**Independentes**: nenhum Poder se subordina a outro; cada um tem autonomia para se organizar.",
       "**Harmônicos**: devem cooperar e se controlar mutuamente — é o sistema de **freios e contrapesos** (checks and balances).",
       "Exemplos de freios e contrapesos: o **veto** presidencial a projetos de lei; a **derrubada do veto** pelo Congresso; o **controle de "
       "constitucionalidade** das leis pelo Judiciário; a **aprovação pelo Senado** dos indicados ao STF; o **impeachment**.",
       "A separação dos Poderes é **cláusula pétrea** (art. 60, § 4º, III).",
       "O **Ministério Público**, a **Defensoria Pública** e os **Tribunais de Contas** têm autonomia, mas **não são Poderes**.",
       "No **Município** não há Poder Judiciário: existem apenas o Legislativo (Câmara) e o Executivo (Prefeitura)."),
    trap("Pegadinha: independentes × harmônicos",
         "A banca escreve “independentes e **autônomos**”, “**dependentes** e harmônicos” ou diz que a separação é **absoluta**. "
         "O texto é “**independentes e harmônicos entre si**”, e a separação é **relativa**: cada Poder exerce funções atípicas."),

    h2("6. Art. 3º: os objetivos fundamentais"),
    key("Texto da Constituição",
        "Art. 3º Constituem objetivos fundamentais da República Federativa do Brasil: I – **construir** uma sociedade livre, justa e solidária; "
        "II – **garantir** o desenvolvimento nacional; III – **erradicar** a pobreza e a marginalização e **reduzir** as desigualdades sociais e "
        "regionais; IV – **promover** o bem de todos, sem preconceitos de origem, raça, sexo, cor, idade e quaisquer outras formas de discriminação."),
    bl("Os objetivos são metas: o que o Estado **deve buscar**. Por isso começam com **verbos no infinitivo**.",
       "São **normas programáticas**: traçam programas de ação para o poder público.",
       "O rol é **exemplificativo**: há outros objetivos espalhados pela Constituição.",
       "O inciso IV traz um rol aberto de discriminações proibidas (“quaisquer outras formas”). É a base das **ações afirmativas**, "
       "como as cotas, consideradas constitucionais pelo STF."),
    key("Mnemônico: CON-GA-ER-PRO",
        "**CON**struir, **GA**rantir, **ER**radicar (e reduzir), **PRO**mover. Verbo no infinitivo = **objetivo** (art. 3º). "
        "Substantivo = **fundamento** (art. 1º) ou **princípio** internacional (art. 4º)."),
    trap("Pegadinha: erradicar × reduzir",
         "**Erradica-se** a **pobreza e a marginalização**; **reduzem-se** as **desigualdades** sociais e regionais. "
         "A banca escreve “erradicar as desigualdades” ou “reduzir a pobreza”. Outra troca comum: “garantir o desenvolvimento **regional**” "
         "(o correto é **nacional**)."),

    h2("7. Art. 4º: princípios das relações internacionais"),
    key("Texto da Constituição",
        "Art. 4º A República Federativa do Brasil rege-se nas suas relações internacionais pelos seguintes princípios: I – independência nacional; "
        "II – prevalência dos direitos humanos; III – autodeterminação dos povos; IV – não-intervenção; V – igualdade entre os Estados; "
        "VI – defesa da paz; VII – solução pacífica dos conflitos; VIII – repúdio ao terrorismo e ao racismo; IX – cooperação entre os povos "
        "para o progresso da humanidade; X – concessão de asilo político. Parágrafo único. A República Federativa do Brasil buscará a integração "
        "econômica, política, social e cultural dos povos da **América Latina**, visando à formação de uma **comunidade latino-americana de nações**."),
    tb(["Princípio", "Ideia"], [0.34, 0.66], [
        ("Independência nacional", "Face externa da soberania: o Brasil não se subordina a outro Estado."),
        ("Prevalência dos direitos humanos", "Os direitos humanos orientam a atuação externa do país."),
        ("Autodeterminação dos povos", "Cada povo decide o próprio destino político."),
        ("Não-intervenção", "O Brasil não interfere nos assuntos internos de outros Estados."),
        ("Igualdade entre os Estados", "Todos os Estados são juridicamente iguais."),
        ("Defesa da paz e solução pacífica dos conflitos", "Preferência por negociação, mediação e arbitragem."),
        ("Repúdio ao terrorismo e ao racismo", "Ambos são crimes inafiançáveis; o racismo é também imprescritível (art. 5º, XLII e XLIII)."),
        ("Cooperação entre os povos", "Para o progresso da humanidade."),
        ("Concessão de asilo político", "Proteção ao estrangeiro perseguido por motivos políticos. Liga-se à vedação de extradição por crime político ou de opinião (art. 5º, LII)."),
    ]),
    bl("O parágrafo único fala em **América Latina**, não em América do Sul nem em Mercosul.",
       "A integração é **econômica, política, social e cultural**.",
       "Para lembrar: quatro princípios tratam de **soberania e igualdade** (independência nacional, autodeterminação, não-intervenção, igualdade), "
       "dois tratam de **paz** (defesa da paz e solução pacífica) e os demais, de **valores humanitários** (direitos humanos, repúdio ao terrorismo "
       "e ao racismo, cooperação, asilo)."),
    trap("Pegadinha: misturar as três listas",
         "O item mais comum pega um elemento de uma lista e o coloca em outra: “a **soberania** é objetivo fundamental”; "
         "“a **dignidade da pessoa humana** é princípio das relações internacionais”; “o **pluralismo político** é objetivo”; "
         "“a **defesa da paz** é fundamento da República”. Antes de julgar, pergunte: é substantivo do art. 1º, verbo do art. 3º ou princípio externo do art. 4º?"),

    h2("8. Quadro para não confundir"),
    tb(["Art. 1º — Fundamentos", "Art. 3º — Objetivos", "Art. 4º — Relações internacionais"], [0.3, 0.36, 0.34], [
        ("Soberania", "Construir uma sociedade livre, justa e solidária", "Independência nacional"),
        ("Cidadania", "Garantir o desenvolvimento nacional", "Prevalência dos direitos humanos"),
        ("Dignidade da pessoa humana", "Erradicar a pobreza e a marginalização e reduzir as desigualdades sociais e regionais", "Autodeterminação dos povos; não-intervenção; igualdade entre os Estados"),
        ("Valores sociais do trabalho e da livre iniciativa", "Promover o bem de todos, sem preconceitos nem discriminação", "Defesa da paz; solução pacífica dos conflitos"),
        ("Pluralismo político", "—", "Repúdio ao terrorismo e ao racismo; cooperação entre os povos; asilo político"),
    ]),

    h2("9. Como o Cebraspe cobra"),
    bl("**Literalidade com troca**: fundamento no lugar de objetivo, objetivo no lugar de princípio internacional.",
       "**Conceitos**: forma de governo (república) × forma de Estado (federação) × regime (democracia) × sistema (presidencialismo).",
       "**Federação**: Municípios como entes; Territórios fora; soberania × autonomia; vedação à secessão.",
       "**Democracia semidireta**: representantes **ou** diretamente; plebiscito × referendo.",
       "**Separação dos Poderes**: funções típicas e atípicas; freios e contrapesos; cláusula pétrea.",
       "**Jurisprudência**: preâmbulo sem força normativa; Súmula Vinculante 11 (algemas); dignidade como vetor de interpretação."),
]

QUIZ = quiz([
    ("C", "A República Federativa do Brasil é formada pela união indissolúvel dos estados, dos municípios e do Distrito Federal e constitui-se em Estado Democrático de Direito.",
     "É o que dispõe o caput do art. 1º da Constituição."),
    ("E", "São fundamentos da República Federativa do Brasil a soberania, a cidadania, a dignidade da pessoa humana e a garantia do desenvolvimento nacional.",
     "Garantir o desenvolvimento nacional é objetivo fundamental (art. 3º, II), não fundamento."),
    ("C", "O pluralismo político, fundamento da República, não se confunde com o pluripartidarismo, pois abrange a diversidade de ideias e de concepções presentes na sociedade.",
     "O pluralismo político é mais amplo que a existência de vários partidos."),
    ("E", "Todo o poder emana do povo, que o exerce exclusivamente por meio de representantes eleitos.",
     "O povo exerce o poder por meio de representantes eleitos ou diretamente (art. 1º, parágrafo único)."),
    ("C", "O plebiscito, o referendo e a iniciativa popular são instrumentos de exercício direto do poder pelo povo.",
     "Estão previstos no art. 14 e caracterizam a democracia semidireta."),
    ("E", "Os territórios federais são entes federativos dotados de autonomia política e integram, ao lado dos estados e dos municípios, a República Federativa do Brasil.",
     "Os territórios integram a União e não são entes federativos (art. 18, § 2º)."),
    ("C", "Constitui objetivo fundamental da República Federativa do Brasil erradicar a pobreza e a marginalização e reduzir as desigualdades sociais e regionais.",
     "É a literalidade do art. 3º, III."),
    ("E", "A concessão de asilo político e a defesa da paz são objetivos fundamentais da República Federativa do Brasil.",
     "São princípios que regem as relações internacionais (art. 4º, VI e X)."),
    ("C", "A edição de medida provisória pelo presidente da República constitui exemplo de exercício de função atípica pelo Poder Executivo.",
     "Legislar é função típica do Legislativo; quando o Executivo edita medida provisória, exerce função atípica."),
    ("E", "A República Federativa do Brasil buscará a integração econômica, política, social e cultural dos povos da América do Sul, visando à formação de uma comunidade sul-americana de nações.",
     "O parágrafo único do art. 4º refere-se aos povos da América Latina e a uma comunidade latino-americana de nações."),

    ("E", "A forma republicana de governo constitui cláusula pétrea expressa na Constituição Federal de 1988.",
     "O art. 60, § 4º, protege a forma federativa de Estado, o voto direto, secreto, universal e periódico, a separação dos Poderes e os direitos e garantias individuais. A república não consta do rol."),
    ("C", "No Estado federal brasileiro, a soberania é atributo da República Federativa do Brasil, ao passo que a União, os estados, o Distrito Federal e os municípios são dotados de autonomia.",
     "Os entes federativos são autônomos (art. 18); soberano é o Estado brasileiro como um todo."),
    ("E", "O preâmbulo da Constituição Federal possui força normativa e é de reprodução obrigatória nas constituições estaduais.",
     "Segundo o STF, o preâmbulo não tem força normativa nem é norma de reprodução obrigatória."),
    ("C", "Só é lícito o uso de algemas em casos de resistência e de fundado receio de fuga ou de perigo à integridade física própria ou alheia, por parte do preso ou de terceiros, justificada a excepcionalidade por escrito.",
     "É o teor da Súmula Vinculante 11, que concretiza a dignidade da pessoa humana na atividade policial."),
    ("E", "O princípio da separação dos Poderes impede que o Poder Judiciário exerça qualquer atividade de natureza administrativa ou normativa.",
     "A separação é relativa: o Judiciário administra seus serviços e elabora seus regimentos internos, que são funções atípicas."),
    ("C", "A indissolubilidade do vínculo federativo significa que os entes federados não dispõem do direito de secessão.",
     "A união é indissolúvel; a tentativa de separação autoriza a intervenção federal."),
    ("E", "Os Poderes da União são independentes e autônomos entre si, não se admitindo controle de um Poder sobre o outro.",
     "O texto é “independentes e harmônicos entre si”, e o sistema de freios e contrapesos prevê controles recíprocos."),
    ("C", "O repúdio ao terrorismo e ao racismo e a prevalência dos direitos humanos são princípios que regem a República Federativa do Brasil em suas relações internacionais.",
     "Estão no art. 4º, II e VIII."),
    ("E", "A dignidade da pessoa humana e os valores sociais do trabalho e da livre iniciativa são objetivos fundamentais da República Federativa do Brasil.",
     "São fundamentos (art. 1º, III e IV). Objetivos estão no art. 3º e começam por verbos."),
    ("C", "Ao estabelecer que o poder é exercido por meio de representantes eleitos ou diretamente, a Constituição adotou a democracia semidireta, também chamada de participativa.",
     "A combinação de representação e participação direta caracteriza a democracia semidireta."),
], 20)

SOURCES = [
    "Constituição da República Federativa do Brasil de 1988, arts. 1º a 4º, 14, 18, 34 e 60.",
    "Supremo Tribunal Federal: Súmula Vinculante 11; ADI 2.076 (preâmbulo); ADI 4.277 e ADPF 132 (união homoafetiva).",
    "Doutrina de referência: Lenza, Direito constitucional; Mendes e Branco, Curso de direito constitucional; Silva, Curso de direito constitucional positivo.",
    "Os 20 itens foram escritos para o Mentor Policial. O Bloco B segue o padrão de cobrança da banca, mas não reproduz questões de provas.",
]
