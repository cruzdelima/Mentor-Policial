# -- coding: utf-8 --
"""Contabilidade · Conceitos, objeto e finalidade — MATERIAL APROFUNDADO (estudo inicial)."""
from common import *

MATERIAL = {
    "id": "cont-conceitos-02",
    "version": "0.1.0",
    "status": "Em revisão pelo autor",
    "subjectId": "CONT",
    "topicIds": ["CONT-01"],
    "kind": "aprofundado",
    "title": "Contabilidade: conceito, objeto e finalidade",
    "subtitle": "Contabilidade Geral · Fundamentos",
    "minutes": 150,
    "folder": "contabilidade_conceitos_aprofundado",
    "pdf": "contabilidade_conceitos_aprofundado.pdf",
    "outName": "Contabilidade_Conceitos_APROFUNDADO.pdf",
    "header": "Contabilidade · Conceito, objeto e finalidade",
    "coverKicker": "Contabilidade Geral  ·  Fundamentos",
    "coverTitle": ["Contabilidade:", "conceito, objeto e finalidade"],
    "coverSub": ["Teoria completa para quem nunca estudou a matéria: do conceito à Estrutura Conceitual,", "com 20 questões no estilo Cebraspe e gabarito comentado."],
    "coverItems": [("01", "Base", "conceito, objeto, finalidade, funções e campo de aplicação"),
                   ("02", "Usuários", "internos, externos e usuários primários (CPC 00)"),
                   ("03", "Técnicas", "escrituração, demonstrações, auditoria e análise"),
                   ("04", "Estrutura", "princípios, características qualitativas e regime de competência"),
                   ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "coverTopic": "Tópico do edital: Conceitos, objeto e finalidade (Contabilidade Geral)",
    "coverBase": "Base: CPC 00 (R2) — Estrutura Conceitual para Relatório Financeiro, Lei nº 6.404/1976 e doutrina.",
}

THEORY = [
    exam("Como estudar este material",
         "Contabilidade costuma ser a matéria que mais assusta quem vem de fora da área — e é uma das que mais pesam na prova de Agente da PF. "
         "Este primeiro assunto é **conceitual**: não há cálculo, mas há um vocabulário que será usado em todos os assuntos seguintes. "
         "Leia com calma, resolva as 20 questões e, nas revisões, use o **PDF de resumo**."),

    h2("1. O que é contabilidade"),
    p("**Contabilidade** é a **ciência social aplicada** que estuda, registra, controla e interpreta os fatos que afetam o **patrimônio** das "
      "entidades, com o objetivo de fornecer **informações úteis** para a tomada de decisão."),
    p("A definição clássica, aprovada no **Primeiro Congresso Brasileiro de Contabilidade (1924)**, ainda aparece em provas: "
      "“Contabilidade é a ciência que estuda e pratica as funções de **orientação, de controle e de registro** relativas à administração econômica.”"),
    bl("É **ciência**, e não apenas técnica ou arte: tem objeto próprio (o patrimônio) e método próprio.",
       "É ciência **social**: estuda um fenômeno que resulta da ação humana — a gestão da riqueza. **Não é ciência exata**, embora use a matemática como ferramenta.",
       "É **aplicada**: existe para resolver um problema prático — informar."),
    trap("Pegadinha: ciência exata",
         "A banca gosta de afirmar que a contabilidade é ciência exata “por lidar com números”. Errado: os números são o instrumento; "
         "o objeto é o patrimônio, fenômeno social."),

    h2("2. Objeto: o patrimônio"),
    p("O **objeto** da contabilidade é o **patrimônio das entidades**. Patrimônio é o **conjunto de bens, direitos e obrigações** vinculado a uma "
      "pessoa física ou jurídica, com ou sem finalidade lucrativa."),
    tb(["Elemento", "O que é", "Exemplos"], [0.2, 0.42, 0.38], [
        ("Bens", "Coisas úteis, capazes de satisfazer necessidades e avaliáveis em dinheiro. Podem ser tangíveis ou intangíveis.", "Dinheiro em caixa, estoques, veículos, imóveis, marcas, softwares"),
        ("Direitos", "Valores que a entidade tem a receber de terceiros.", "Duplicatas a receber, clientes, aluguéis a receber, aplicações"),
        ("Obrigações", "Valores que a entidade deve a terceiros.", "Fornecedores, salários a pagar, empréstimos, impostos a recolher"),
    ]),
    bl("**Bens + direitos** formam o **ativo** (parte positiva do patrimônio).",
       "**Obrigações** formam o **passivo exigível** (parte negativa).",
       "A diferença entre os dois é o **patrimônio líquido** (ou situação líquida): a riqueza própria da entidade. "
       "A relação **Ativo = Passivo + Patrimônio Líquido** é a equação fundamental do patrimônio, tema do próximo material."),
    key("Objeto × objetivo",
        "**Objeto** é o que a contabilidade estuda: o **patrimônio**. **Objetivo** (finalidade) é para que ela serve: "
        "**fornecer informações** úteis aos usuários. A troca de um pelo outro é a pegadinha mais comum deste assunto."),
    h3("Aspectos do patrimônio"),
    bl("**Aspecto qualitativo**: a natureza de cada elemento — do que o patrimônio é composto (caixa, veículos, fornecedores).",
       "**Aspecto quantitativo**: a expressão monetária de cada elemento — quanto vale cada componente.",
       "**Estática patrimonial**: o patrimônio visto em um momento, como em uma fotografia (representada pelo balanço patrimonial).",
       "**Dinâmica patrimonial**: as variações do patrimônio ao longo do tempo, causadas pelos atos de gestão (representada pela demonstração do resultado)."),

    h2("3. Finalidade (objetivo)"),
    p("A finalidade da contabilidade é **gerar informações** de natureza econômica, financeira e patrimonial que sirvam ao **controle** e ao "
      "**planejamento**, ajudando os usuários a **tomar decisões**."),
    bl("**Controle**: verificar se o que foi realizado está de acordo com o que foi planejado e com as normas.",
       "**Planejamento**: decidir, entre alternativas, o que fazer no futuro, com base nas informações registradas."),
    p("Para a **Estrutura Conceitual (CPC 00 R2)**, o objetivo do relatório financeiro para fins gerais é **fornecer informações financeiras sobre a "
      "entidade que reporta que sejam úteis para investidores, credores por empréstimos e outros credores, existentes e potenciais, na tomada de "
      "decisões referente à oferta de recursos à entidade**."),
    trap("Pegadinha: apurar imposto",
         "A finalidade da contabilidade **não é** apurar tributos nem atender ao Fisco. O governo é um dos usuários, mas a informação contábil "
         "é voltada à tomada de decisão dos usuários em geral."),

    h2("4. Funções da contabilidade"),
    tb(["Função", "O que significa"], [0.25, 0.75], [
        ("Administrativa", "**Controlar o patrimônio**: acompanhar bens, direitos e obrigações, mostrando sua composição e suas variações."),
        ("Econômica", "**Apurar o resultado** (rédito): verificar se a entidade teve lucro ou prejuízo no período."),
    ]),

    h2("5. Campo de aplicação"),
    p("O campo de aplicação da contabilidade são as **aziendas**: entidades econômico-administrativas, isto é, patrimônios geridos por alguém. "
      "Alcança **qualquer pessoa, física ou jurídica, com ou sem fins lucrativos, de direito público ou privado**, que possua patrimônio."),
    bl("Empresas (indústria, comércio, serviços, bancos).",
       "Entidades sem fins lucrativos (associações, fundações, igrejas, sindicatos, partidos políticos).",
       "Entes públicos (União, estados, municípios, autarquias) — contabilidade aplicada ao setor público.",
       "Pessoas físicas."),
    trap("Pegadinha: só empresas",
         "A contabilidade **não se restringe** a entidades com fins lucrativos. Onde há patrimônio a controlar, há campo para a contabilidade."),

    h2("6. Usuários da informação contábil"),
    p("**Usuário** é toda pessoa, física ou jurídica, que tenha interesse na situação da entidade e use a informação contábil para decidir."),
    tb(["Grupo", "Quem são", "O que querem saber"], [0.18, 0.4, 0.42], [
        ("Internos", "Administradores, diretores, gerentes, sócios que participam da gestão, empregados", "Desempenho, custos, metas, capacidade de pagar salários"),
        ("Externos", "Investidores, acionistas que não participam da gestão, bancos, fornecedores, clientes, governo, sindicatos, concorrentes, público", "Retorno e risco, capacidade de pagamento, continuidade, tributos devidos"),
    ]),
    key("Usuários primários (CPC 00 R2)",
        "Os relatórios financeiros para fins gerais são direcionados aos **usuários primários**: **investidores, credores por empréstimos e outros "
        "credores, existentes e potenciais**. São os que não podem exigir que a entidade lhes preste informações diretamente. "
        "A **administração** também se interessa pela informação, mas **não precisa** desses relatórios, porque obtém internamente o que deseja. "
        "**Órgãos reguladores e o público em geral** podem achar os relatórios úteis, mas eles **não são direcionados** primariamente a esses grupos."),

    h2("7. Técnicas contábeis"),
    p("Para cumprir sua finalidade, a contabilidade usa quatro técnicas:"),
    tb(["Técnica", "O que é", "Produto"], [0.26, 0.46, 0.28], [
        ("Escrituração", "Registro dos fatos que alteram o patrimônio, em ordem cronológica, nos livros próprios.", "Livro Diário e Livro Razão"),
        ("Demonstrações contábeis", "Exposição resumida e ordenada dos dados registrados, em determinada data ou período.", "Balanço patrimonial, DRE e demais demonstrações"),
        ("Auditoria", "Exame e verificação da exatidão dos registros e das demonstrações.", "Relatório (parecer) do auditor"),
        ("Análise das demonstrações (análise de balanços)", "Decomposição, comparação e interpretação das demonstrações.", "Índices e relatórios de análise"),
    ]),
    nt("Ordem lógica: primeiro se **registra** (escrituração), depois se **resume** (demonstrações), depois se **confere** (auditoria) e se **interpreta** (análise)."),
    h3("Demonstrações obrigatórias (Lei nº 6.404/1976, art. 176)"),
    bl("**Balanço patrimonial (BP)**: posição patrimonial e financeira em uma data.",
       "**Demonstração do resultado do exercício (DRE)**: lucro ou prejuízo do período.",
       "**Demonstração dos lucros ou prejuízos acumulados (DLPA)**.",
       "**Demonstração dos fluxos de caixa (DFC)** — dispensada para a companhia fechada com patrimônio líquido inferior a R$ 2 milhões na data do balanço.",
       "**Demonstração do valor adicionado (DVA)** — obrigatória para as **companhias abertas**.",
       "As demonstrações são complementadas por **notas explicativas**. O **exercício social** tem duração de **um ano** (art. 175)."),

    h2("8. Entidade, continuidade e competência"),
    p("Três ideias sustentam toda a contabilidade e serão usadas em todos os assuntos seguintes."),
    tb(["Ideia", "Significado", "Consequência prática"], [0.2, 0.42, 0.38], [
        ("Entidade", "O patrimônio da entidade **não se confunde** com o dos seus sócios ou proprietários.", "A conta de luz da casa do sócio não é despesa da empresa."),
        ("Continuidade", "Presume-se que a entidade **continuará em operação** no futuro previsível. No CPC 00, é a **premissa subjacente** das demonstrações.", "Os ativos são avaliados pensando no uso, e não na venda forçada."),
        ("Competência", "Receitas e despesas são reconhecidas no período em que **ocorrem** (fato gerador), **independentemente de recebimento ou pagamento**.", "A venda a prazo em dezembro é receita de dezembro, mesmo que o cliente pague em janeiro."),
    ]),
    key("Regime de competência × regime de caixa",
        "No **regime de competência**, vale o **fato gerador**. No **regime de caixa**, vale a **entrada ou saída de dinheiro**. "
        "A contabilidade societária adota o **regime de competência** (Lei nº 6.404/1976, art. 177). "
        "A demonstração dos fluxos de caixa é a única elaborada com base em entradas e saídas de caixa."),
    h3("E os “princípios de contabilidade”?"),
    p("A **Resolução CFC nº 750/1993** listava os princípios de contabilidade: **entidade, continuidade, oportunidade, registro pelo valor original, "
      "competência e prudência**. Ela foi **revogada** (com efeitos a partir de 1º/1/2017), porque o conteúdo já está na Estrutura Conceitual. "
      "Os princípios continuam a existir na doutrina e ainda aparecem em provas."),
    tb(["Princípio", "Ideia central"], [0.3, 0.7], [
        ("Entidade", "Autonomia patrimonial: o patrimônio da entidade é separado do patrimônio dos sócios."),
        ("Continuidade", "A entidade seguirá operando; isso influencia a classificação e a avaliação dos elementos patrimoniais."),
        ("Oportunidade", "A informação deve ser **íntegra e tempestiva**: registrada no momento certo e com a extensão correta."),
        ("Registro pelo valor original", "Os componentes do patrimônio são registrados, inicialmente, pelos valores originais das transações."),
        ("Competência", "Receitas e despesas no período em que ocorrem, independentemente de recebimento ou pagamento."),
        ("Prudência", "Diante de alternativas igualmente válidas, adota-se o **menor valor para o ativo** e o **maior para o passivo**."),
    ]),

    h2("9. Características qualitativas da informação (CPC 00 R2)"),
    p("Para ser **útil**, a informação contábil precisa ter certas qualidades. A Estrutura Conceitual as divide em dois grupos."),
    tb(["Grupo", "Característica", "Significado"], [0.18, 0.24, 0.58], [
        ("Fundamentais", "Relevância", "É capaz de **fazer diferença** nas decisões. Tem **valor preditivo**, **valor confirmatório** ou ambos. A **materialidade** é um aspecto da relevância, específico da entidade."),
        ("Fundamentais", "Representação fidedigna", "Retrata a **essência** do fenômeno. Deve ser **completa, neutra e isenta de erros**. A neutralidade é apoiada pelo exercício da **prudência**."),
        ("De melhoria", "Comparabilidade", "Permite identificar semelhanças e diferenças entre itens, entre entidades e entre períodos."),
        ("De melhoria", "Capacidade de verificação", "Observadores diferentes, bem informados e independentes, podem chegar a consenso sobre a representação."),
        ("De melhoria", "Tempestividade", "Informação disponível a tempo de influenciar a decisão."),
        ("De melhoria", "Compreensibilidade", "Informação classificada, caracterizada e apresentada de forma clara e concisa."),
    ]),
    bl("A informação só é útil se for, **ao mesmo tempo**, relevante **e** fidedigna. As características de melhoria **aumentam** a utilidade, "
       "mas não tornam útil uma informação irrelevante ou não fidedigna.",
       "**Essência sobre a forma**: registra-se a realidade econômica da operação, ainda que a forma jurídica seja outra.",
       "**Restrição do custo**: o benefício de fornecer a informação deve justificar o custo de produzi-la.",
       "**Comparabilidade não é uniformidade**: coisas diferentes devem parecer diferentes. **Consistência** (usar os mesmos métodos) ajuda a alcançar a comparabilidade."),
    trap("Pegadinha: quais são as fundamentais?",
         "Só duas características são **fundamentais**: **relevância** e **representação fidedigna**. Comparabilidade, capacidade de verificação, "
         "tempestividade e compreensibilidade são **de melhoria**. A banca troca os grupos."),

    h2("10. Ramos da contabilidade"),
    tb(["Ramo", "Foco"], [0.3, 0.7], [
        ("Financeira (societária, geral)", "Usuários **externos**; segue normas obrigatórias (Lei nº 6.404/1976 e CPCs)."),
        ("Gerencial", "Usuários **internos**; informações sob medida para a gestão, sem forma obrigatória."),
        ("De custos", "Apuração do custo de produtos e serviços."),
        ("Pública", "Patrimônio das entidades do setor público."),
        ("Tributária", "Apuração e planejamento dos tributos."),
        ("Auditoria e perícia", "Verificação dos registros (auditoria) e produção de prova técnica em processos (perícia)."),
    ]),
    key("Por que o policial estuda isso",
        "A investigação de crimes financeiros — lavagem de dinheiro, desvio de recursos públicos, fraudes — depende de ler balanços, "
        "identificar patrimônio incompatível e seguir o dinheiro. O vocabulário deste material é a base desse trabalho."),

    h2("11. Como o Cebraspe cobra"),
    bl("Troca de **objeto** (patrimônio) por **objetivo** (informação).",
       "Contabilidade como “ciência exata” ou restrita a “entidades com fins lucrativos”.",
       "Função **administrativa** (controle) × função **econômica** (resultado).",
       "Técnicas contábeis: definição de cada uma e a ordem lógica.",
       "CPC 00: usuários primários e a divisão entre características fundamentais e de melhoria.",
       "Entidade: mistura entre patrimônio do sócio e patrimônio da empresa.",
       "Competência × caixa: reconhecimento da receita ou da despesa independentemente do dinheiro."),
]

QUIZ = quiz([
    ("C", "A contabilidade é uma ciência social aplicada cujo objeto é o patrimônio das entidades.",
     "Ciência social (o patrimônio resulta da ação humana) e aplicada; o objeto é o patrimônio."),
    ("E", "Por empregar métodos quantitativos e registrar valores monetários, a contabilidade é classificada como ciência exata.",
     "Os números são instrumento. A contabilidade é ciência social aplicada."),
    ("E", "O objeto da contabilidade é o fornecimento de informações úteis aos usuários, e sua finalidade é o patrimônio das entidades.",
     "Os conceitos estão invertidos: o objeto é o patrimônio; a finalidade é fornecer informações úteis."),
    ("C", "O patrimônio, sob o ponto de vista contábil, compreende o conjunto de bens, direitos e obrigações de uma entidade.",
     "Bens e direitos formam o ativo; obrigações, o passivo exigível."),
    ("C", "A função administrativa da contabilidade consiste em controlar o patrimônio, ao passo que a função econômica consiste em apurar o resultado.",
     "Controle do patrimônio (administrativa) e apuração do lucro ou prejuízo, o rédito (econômica)."),
    ("E", "O campo de aplicação da contabilidade restringe-se às entidades com finalidade lucrativa, uma vez que apenas estas apuram resultado.",
     "Alcança qualquer entidade que possua patrimônio: com ou sem fins lucrativos, pública ou privada, pessoa física ou jurídica."),
    ("C", "A escrituração é a técnica contábil que consiste no registro, em livros próprios, dos fatos que provocam alterações no patrimônio.",
     "É a primeira das técnicas; alimenta as demonstrações, a auditoria e a análise."),
    ("E", "A auditoria é a técnica contábil destinada a decompor, comparar e interpretar as demonstrações contábeis, por meio de índices.",
     "Essa é a análise das demonstrações (análise de balanços). A auditoria examina e verifica a exatidão dos registros e das demonstrações."),
    ("C", "O aspecto qualitativo do patrimônio refere-se à natureza dos elementos que o compõem, enquanto o aspecto quantitativo refere-se à sua expressão monetária.",
     "Qualitativo: do que é feito (caixa, veículos). Quantitativo: quanto vale."),
    ("E", "De acordo com o regime de competência, as receitas devem ser reconhecidas apenas no momento do efetivo recebimento dos valores.",
     "Isso descreve o regime de caixa. Pela competência, a receita é reconhecida quando ocorre o fato gerador, independentemente do recebimento."),

    ("C", "Segundo a Estrutura Conceitual, o objetivo do relatório financeiro para fins gerais é fornecer informações financeiras úteis a investidores, credores por empréstimos e outros credores, existentes e potenciais, na tomada de decisões referentes à oferta de recursos à entidade.",
     "É o objetivo expresso no CPC 00 (R2), que também define esses grupos como usuários primários."),
    ("E", "A administração da entidade é considerada usuária primária dos relatórios financeiros para fins gerais, pois depende exclusivamente deles para obter as informações de que necessita.",
     "A administração não precisa se apoiar nesses relatórios, pois obtém internamente as informações. Os usuários primários são investidores e credores, existentes e potenciais."),
    ("C", "Relevância e representação fidedigna são as características qualitativas fundamentais da informação contábil-financeira útil.",
     "São as duas fundamentais. As demais (comparabilidade, capacidade de verificação, tempestividade e compreensibilidade) são de melhoria."),
    ("E", "A comparabilidade e a tempestividade são características qualitativas fundamentais, sem as quais a informação contábil não pode ser considerada útil.",
     "São características de melhoria: aumentam a utilidade de uma informação que já é relevante e fidedigna."),
    ("C", "Para ser representação fidedigna, a informação deve ser completa, neutra e isenta de erros.",
     "São os três atributos da representação fidedigna no CPC 00 (R2)."),
    ("E", "Em observância à ideia de entidade, as despesas pessoais dos sócios pagas com recursos da empresa devem ser registradas como despesas operacionais da sociedade.",
     "O patrimônio da entidade não se confunde com o dos sócios. Despesa pessoal do sócio não é despesa da empresa."),
    ("C", "A informação contábil-financeira relevante é aquela capaz de fazer diferença nas decisões tomadas pelos usuários, o que ocorre quando ela tem valor preditivo, valor confirmatório ou ambos.",
     "É a definição de relevância na Estrutura Conceitual."),
    ("E", "Nos termos da Lei nº 6.404/1976, a demonstração do valor adicionado é obrigatória para todas as sociedades por ações, abertas ou fechadas.",
     "A DVA é obrigatória apenas para as companhias abertas."),
    ("C", "A continuidade pressupõe que a entidade continuará em operação no futuro previsível, o que influencia a forma de avaliação de seus ativos e passivos.",
     "É a premissa subjacente das demonstrações contábeis no CPC 00."),
    ("E", "As demonstrações contábeis constituem a técnica pela qual se verifica a exatidão dos registros contábeis, razão pela qual antecedem a escrituração.",
     "Verificar a exatidão é auditoria. E as demonstrações são elaboradas a partir da escrituração, não antes dela."),
], 20)

SOURCES = [
    "Comitê de Pronunciamentos Contábeis — CPC 00 (R2): Estrutura Conceitual para Relatório Financeiro.",
    "Lei nº 6.404/1976 (Lei das Sociedades por Ações), arts. 175 a 177.",
    "Resolução CFC nº 750/1993 (princípios de contabilidade), revogada com efeitos a partir de 1º/1/2017.",
    "Doutrina de referência: Iudícibus e outros, Manual de contabilidade societária; Ribeiro, Contabilidade geral.",
    "Os 20 itens foram escritos para o Taticum. O Bloco B segue o padrão de cobrança da banca, mas não reproduz questões de provas.",
]
