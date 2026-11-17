# -*- coding: utf-8 -*-
"""Língua Portuguesa · Concordância nominal e verbal — MATERIAL APROFUNDADO (estudo inicial)."""
from common import *

MATERIAL = material(
    "lp-concordancia-02", "LP", "LP-11", "aprofundado", "Concordância nominal e verbal", "Língua Portuguesa · Sintaxe",
    "portugues_concordancia_aprofundado", "Portugues_Concordancia_APROFUNDADO.pdf", None, ["Concordância", "nominal e verbal"],
    ["Teoria completa para o primeiro estudo: regra geral, sujeito composto, casos especiais", "e concordância nominal, com 20 questões no estilo Cebraspe."],
    [("01", "Verbal", "regra geral, sujeito posposto e composto"),
     ("02", "Casos especiais", "coletivos, porcentagem, relativos, ser, haver, se"),
     ("03", "Nominal", "adjetivo e vários substantivos"),
     ("04", "Palavras-armadilha", "anexo, mesmo, obrigado, meio, menos, é proibido"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Concordância nominal e verbal (Língua Portuguesa)",
    "Base: gramáticas de referência (Bechara; Cunha e Cintra).", 240)

THEORY = [
    exam("Como estudar este material",
         "Concordância é o tópico de gramática mais cobrado pelo Cebraspe. O segredo é sempre **achar o sujeito** antes de julgar o verbo — "
         "principalmente quando ele vem **depois** do verbo, quando é longo ou quando o verbo é impessoal. Faça a seção 1 com calma: "
         "a maior parte das questões cai ali."),

    h2("1. Concordância verbal: regra geral"),
    p("O verbo concorda com o **núcleo do sujeito** em **número** e **pessoa**: *O **agente** chegou. Os **agentes** chegaram.*"),
    h3("Sujeito posposto"),
    p("O sujeito depois do verbo continua comandando a concordância: ***Faltam** dois documentos. **Chegaram** os laudos. **Ocorreram** várias prisões.* "
      "Pergunte ao verbo: *o que falta? o que chegou?*"),
    h3("Sujeito longo ou distante do verbo"),
    p("*A **análise** dos documentos apreendidos pelos agentes nas três operações **revelou** fraudes* (o núcleo é *análise*, não *operações*)."),
    h3("Sujeito composto"),
    tb(["Situação", "Concordância", "Exemplo"], [0.3, 0.32, 0.38], [
        ("Anteposto ao verbo", "**Plural**", "O delegado e o escrivão **chegaram**."),
        ("Posposto ao verbo", "Plural **ou** com o núcleo mais próximo", "**Chegaram** / **Chegou** o delegado e os escrivães."),
        ("Pessoas diferentes", "Prevalece a 1ª; depois a 2ª", "Eu e tu **iremos**. Tu e ele **ireis** (ou **irão**)."),
        ("Núcleos sinônimos ou em gradação", "Singular ou plural", "O medo e o pavor **dominou/dominaram** a vila."),
        ("Ligados por *ou* com exclusão", "**Singular**", "O delegado ou o escrivão **assinará** o termo."),
        ("Ligados por *ou* sem exclusão", "**Plural**", "Furto ou roubo **são** crimes contra o patrimônio."),
        ("Ligados por *nem… nem*", "Em regra, **plural**", "Nem o réu nem o advogado **compareceram**."),
        ("Resumidos por *tudo, nada, ninguém*", "**Singular**", "Armas, drogas, dinheiro, **tudo** **foi** apreendido."),
    ]),

    h2("2. Casos especiais da concordância verbal"),
    tb(["Caso", "Regra", "Exemplo"], [0.24, 0.36, 0.4], [
        ("Coletivo", "Singular", "A **tropa** **avançou**."),
        ("Coletivo + especificador no plural", "Singular ou plural", "A maioria dos agentes **aprovou/aprovaram**."),
        ("Mais de um", "Singular (plural se houver reciprocidade)", "**Mais de um** agente **foi** ferido."),
        ("Mais de / cerca de + número", "Concorda com o **numeral**", "**Mais de dez** candidatos **foram** eliminados. **Cerca de trinta** policiais **participaram**."),
        ("Porcentagem", "Com o numeral ou com o especificador", "**1%** dos eleitores **votou**. **30%** da tropa **está/estão** de folga."),
        ("Um dos que", "Plural (preferível)", "Ele é **um dos que** mais **trabalham**."),
        ("Que (relativo)", "Concorda com o **antecedente**", "Fui **eu que** **redigi**. Fomos **nós que** **redigimos**."),
        ("Quem", "3ª do singular ou com o antecedente", "Fui eu **quem redigiu** / **quem redigi**."),
        ("Qual de nós / quais de nós", "Singular com *qual*; com *quais*, concorda com *nós* ou 3ª pessoa", "**Qual** de nós **irá**? **Quais** de nós **iremos/irão**?"),
        ("Nome próprio plural com artigo", "Plural", "**Os Estados Unidos são**…"),
    ]),
    h3("Verbos impessoais e o pronome se"),
    bl("**Haver** (existir, acontecer, tempo) e **fazer** (tempo, clima): **singular**, inclusive o auxiliar — *Havia provas. Deve haver provas. Faz dois anos.*",
       "**Existir, ocorrer, acontecer** têm sujeito e vão ao plural: *Existiam provas. Ocorreram falhas.*",
       "**VTD + se** (voz passiva sintética): concorda com o sujeito — *Revisaram-se os inquéritos. Vendem-se viaturas.*",
       "**VTI, VI ou VL + se** (sujeito indeterminado): **singular** — *Precisa-se de agentes. Trata-se de casos graves.*"),
    h3("Verbo ser"),
    bl("Concorda, em regra, com o **predicativo** quando o sujeito é *tudo, isto, isso, aquilo* ou nome de coisa no singular: *Tudo **são** flores. Isso **são** detalhes.*",
       "**Pessoa** prevalece: *O responsável **sou** eu.*",
       "**Horas, datas e distâncias**: concorda com o numeral — ***São** duas horas. **É** meio-dia. **É** uma hora. Hoje **são** 10 de maio* (ou *Hoje **é** dia 10*).",
       "**Quantidade, preço, peso** com *é muito, é pouco, é suficiente*: singular — *Dez metros **é** pouco.*"),
    trap("As pegadinhas campeãs",
         "*Deve existir provas* (errado: **devem existir**) · *Haviam provas* (errado: **havia**) · *Precisam-se de* (errado: **precisa-se**) · "
         "*Vende-se casas* (errado: **vendem-se**) · *Faltou três agentes* (errado: **faltaram**)."),

    h2("3. Concordância nominal"),
    p("Artigo, adjetivo, pronome e numeral concordam em **gênero** e **número** com o substantivo a que se referem."),
    tb(["Situação", "Concordância", "Exemplo"], [0.3, 0.34, 0.36], [
        ("Adjetivo **depois** de vários substantivos", "Plural (masculino prevalece) **ou** com o mais próximo", "Laudo e perícia **completos** / **completa**."),
        ("Adjetivo **antes** de vários substantivos", "Com o **mais próximo**", "**Completa** perícia e laudo."),
        ("Adjetivo predicativo de sujeito composto", "Plural", "O laudo e a perícia estão **completos**."),
        ("Um substantivo e vários adjetivos", "*as polícias civil e militar* ou *a polícia civil e a militar*", "—"),
    ]),

    h2("4. Palavras-armadilha"),
    tb(["Palavra", "Regra", "Exemplo"], [0.2, 0.38, 0.42], [
        ("anexo, incluso, obrigado, mesmo, próprio, quite", "**Variam**: concordam com o substantivo", "Seguem **anexos** os documentos. **Obrigada**, disse a delegada. Ela **mesma** assinou."),
        ("em anexo", "**Invariável**", "Seguem **em anexo** as fotos."),
        ("menos, alerta (advérbio)", "**Invariáveis**", "Havia **menos** provas. (nunca *menas*)"),
        ("meio, bastante", "Advérbio (junto de adjetivo) não varia; adjetivo/pronome varia", "**meio** nervosa · **meia** hora · **bastante** cansados · **bastantes** provas"),
        ("só", "*sozinho* varia; *somente* não", "Ficaram **sós**. **Só** eles ficaram."),
        ("é proibido, é necessário, é bom", "Sem determinante: invariável; com artigo: concorda", "**É proibido** entrada. **É proibida a** entrada."),
        ("meio-dia e meia", "*meia* = metade da hora", "Chegou ao **meio-dia e meia**."),
        ("possível (o mais… possível)", "Concorda com o artigo", "**o mais** rápido **possível** · **os mais** rápidos **possíveis**"),
    ]),

    h2("5. Como o Cebraspe cobra"),
    bl("“A forma verbal X está no plural para concordar com Y” — confira se Y é mesmo o núcleo do sujeito.",
       "“A substituição de *existir* por *haver* exigiria a forma *havia*” — verbo impessoal no singular.",
       "“O verbo poderia ser empregado no singular” — sujeito composto posposto, coletivo com especificador.",
       "Reescritas que trocam o sujeito de número sem ajustar o verbo ou o particípio."),
]

QUIZ = quiz([
    ("C", "Em “Faltam dois documentos no processo”, o verbo está no plural para concordar com o sujeito dois documentos.",
     "O sujeito vem posposto ao verbo, mas continua comandando a concordância."),
    ("E", "Em “Deve existir provas suficientes no inquérito”, a concordância verbal está de acordo com a norma-padrão.",
     "Existir é pessoal: o sujeito é provas suficientes, e a locução vai ao plural (devem existir)."),
    ("C", "Em “A maioria dos agentes aprovou a medida”, o verbo poderia ser empregado no plural (aprovaram), sem prejuízo da correção.",
     "Com coletivo partitivo seguido de especificador no plural, admitem-se singular e plural."),
    ("E", "Em “Mais de um agente foram feridos na operação”, a concordância está de acordo com a norma-padrão.",
     "Com mais de um, o verbo fica no singular: mais de um agente foi ferido."),
    ("C", "Em “Fui eu que redigi o relatório”, a forma verbal redigi concorda com o antecedente do pronome relativo.",
     "O relativo que leva o verbo a concordar com o antecedente eu."),
    ("E", "Em “Seguem anexo os documentos solicitados”, a concordância nominal está de acordo com a norma-padrão.",
     "Anexo é adjetivo e concorda com o substantivo: seguem anexos os documentos (ou em anexo)."),
    ("C", "Em “Ela mesma assinou o termo de depoimento”, o vocábulo mesma concorda com o pronome a que se refere.",
     "Mesmo, com valor de próprio, é variável."),
    ("E", "Está de acordo com a norma-padrão a frase “É proibida entrada de pessoas estranhas”.",
     "Sem artigo, a expressão fica invariável (é proibido entrada); com artigo, concorda (é proibida a entrada)."),
    ("C", "Em “São duas horas da madrugada”, o verbo ser concorda com o numeral.",
     "Na indicação de horas, o verbo ser concorda com a expressão numérica."),
    ("E", "Em “Os Estados Unidos é um parceiro estratégico”, a concordância está de acordo com a norma-padrão.",
     "Nome próprio plural precedido de artigo leva o verbo ao plural: os Estados Unidos são."),

    ("C", "No trecho “Chegaram o delegado e os escrivães”, o verbo poderia ficar no singular, concordando com o núcleo mais próximo, sem prejuízo da correção.",
     "Com sujeito composto posposto, admite-se a concordância com o núcleo mais próximo: chegou o delegado e os escrivães."),
    ("E", "Em “Precisam-se de mais agentes na delegacia”, a concordância está de acordo com a norma-padrão.",
     "Precisar de é transitivo indireto: o se indetermina o sujeito, e o verbo fica no singular."),
    ("C", "Em “Revisaram-se os inquéritos pendentes”, a forma verbal no plural justifica-se pela concordância com o sujeito os inquéritos pendentes.",
     "Revisar é transitivo direto: há voz passiva sintética."),
    ("E", "No trecho “Cerca de trinta policiais participou da operação”, a concordância está de acordo com a norma-padrão.",
     "Com cerca de + numeral, o verbo concorda com o numeral: participaram."),
    ("C", "Em “O delegado ou o escrivão assinará o termo”, o verbo no singular indica que apenas um deles praticará a ação.",
     "Com ou de valor excludente, o verbo fica no singular."),
    ("E", "Em “Houveram muitas reclamações contra a abordagem”, a concordância está de acordo com a norma-padrão.",
     "Haver no sentido de acontecer é impessoal: houve muitas reclamações."),
    ("C", "Em “As provas e o depoimento foram analisados”, o emprego do particípio no masculino plural está de acordo com a norma-padrão.",
     "Com núcleos de gêneros diferentes, o predicativo vai ao masculino plural."),
    ("E", "Em “Muito obrigado, disse a delegada ao fim da entrevista”, a concordância nominal está de acordo com a norma-padrão.",
     "Obrigado concorda com quem fala: a delegada diria muito obrigada."),
    ("C", "Em “Ele é um dos agentes que mais trabalham na delegacia”, o verbo trabalhar no plural está de acordo com a norma-padrão.",
     "Na expressão um dos que, o verbo vai preferencialmente ao plural, concordando com agentes."),
    ("E", "Em “Mais de dez candidatos foi eliminado na prova física”, a concordância está de acordo com a norma-padrão.",
     "Com mais de + numeral, o verbo concorda com o numeral: mais de dez candidatos foram eliminados."),
], 20)

SOURCES = [GRAM, SRC_A]
