# -*- coding: utf-8 -*-
"""Língua Portuguesa · Coesão e coerência textual — MATERIAL APROFUNDADO (estudo inicial)."""
from common import *

MATERIAL = material(
    "lp-coesao-02", "LP", "LP-16", "aprofundado", "Coesão e coerência textual", "Língua Portuguesa · Texto",
    "portugues_coesao_aprofundado", "Portugues_Coesao_Coerencia_APROFUNDADO.pdf", None, ["Coesão e", "coerência textual"],
    ["Teoria completa para o primeiro estudo: referenciação, conectivos, elipse e progressão,", "com 20 questões no estilo Cebraspe sobre um texto policial."],
    [("01", "Conceitos", "coesão (ligação) × coerência (sentido)"),
     ("02", "Coesão referencial", "anáfora, catáfora, pronomes, sinônimos, elipse"),
     ("03", "Coesão sequencial", "conectivos e progressão"),
     ("04", "Coerência", "não contradição, continuidade e relação com o mundo"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Coesão e coerência textual (Língua Portuguesa)",
    "Base: gramáticas de referência e Koch, A coesão textual.", 150)

THEORY = [
    exam("Como estudar este material",
         "É o tópico mais presente nas provas de interpretação do Cebraspe: “o termo X retoma Y”, “o pronome Z refere-se a W”, "
         "“a substituição de X por Y prejudicaria a coesão”. Para acertar, **substitua** o termo pelo referente que a banca propõe e veja "
         "se a frase continua fazendo sentido e concordando."),

    h2("1. Coesão × coerência"),
    tb(["", "Coesão", "Coerência"], [0.18, 0.41, 0.41], [
        ("O que é", "Ligação **linguística** entre as partes do texto", "Unidade de **sentido** do texto"),
        ("Onde está", "Na superfície: pronomes, conectivos, sinônimos", "Na lógica: ideias compatíveis, sem contradição"),
        ("Exemplo de falha", "*O delegado chegou. O delegado ouviu. O delegado saiu.* (repetição)", "*Choveu muito; portanto, as ruas ficaram secas.*"),
    ]),
    p("Um texto pode ter muitos conectivos e ainda assim ser **incoerente**; e pode ser **coerente** com poucos elementos coesivos explícitos."),

    h2("2. Coesão referencial"),
    p("Retoma ou antecipa elementos do texto, evitando repetições."),
    bl("**Anáfora**: retoma o que já foi dito — *A PF deflagrou a operação. **Ela** cumpriu vinte mandados.*",
       "**Catáfora**: antecipa o que será dito — *Só **isto** importa: **a vida da vítima**.*"),
    tb(["Mecanismo", "Exemplo"], [0.34, 0.66], [
        ("Pronomes pessoais, demonstrativos, possessivos, relativos", "O réu negou o crime. **Essa** versão, contudo, foi desmentida."),
        ("Sinônimos e expressões equivalentes", "O **fuzil** foi apreendido. **O armamento** estava municiado."),
        ("Hiperônimos (termo geral)", "O **fuzil** foi apreendido. **A arma** estava municiada."),
        ("Expressões nominais definidas (rótulos)", "O suspeito fugiu pela janela. **A fuga** foi filmada."),
        ("Elipse (omissão de termo identificável)", "Os peritos chegaram cedo e **(eles)** isolaram a área."),
        ("Advérbios de lugar e tempo", "Fomos a Recife. **Lá**, encontramos o suspeito."),
        ("Numerais e expressões como *o primeiro, o último*", "Ouviram o delegado e o escrivão; **o último** confirmou a versão."),
    ]),
    key("Este, esse, aquele na referência",
        "**Esse** retoma (anáfora); **este** anuncia (catáfora) ou indica o mais próximo numa retomada de dois termos; **aquele** indica o mais distante: "
        "*Ouvi o perito e a escrivã: **esta** confirmou; **aquele**, não.*"),

    h2("3. Coesão sequencial"),
    p("Faz o texto **progredir**, encadeando as ideias com relações lógicas."),
    bl("**Conectivos** (conjunções, advérbios, locuções): *além disso, porém, portanto, porque, embora, em seguida*.",
       "**Articuladores entre parágrafos**: *Em primeiro lugar… Além disso… Em contrapartida… Dessa forma… Em síntese…*",
       "**Tempos verbais** e marcadores temporais que ordenam os fatos: *Às 22h… Minutos depois… No dia seguinte…*"),
    h3("Coesão lexical"),
    p("Repetição intencional, sinonímia, hiperonímia e campo semântico (*crime, delegacia, inquérito, perícia*) também ligam o texto. "
      "Repetir é um recurso coesivo legítimo, mas o excesso empobrece o texto."),

    h2("4. Coerência"),
    bl("**Não contradição**: uma informação não pode negar outra (*o réu, que estava preso, foi visto na festa*).",
       "**Continuidade**: o texto mantém o tema (fio condutor).",
       "**Progressão**: acrescenta informações novas a cada parte.",
       "**Relação com o mundo**: as informações são compatíveis com o conhecimento compartilhado.",
       "**Coerência das relações lógicas**: o conectivo precisa combinar com o conteúdo (*choveu; portanto, as ruas ficaram **molhadas***)."),

    h2("5. Como o Cebraspe cobra"),
    bl("“O termo X retoma Y” — substitua X por Y e confira sentido e concordância.",
       "“O pronome Z refere-se a W” — atenção ao referente mais próximo e ao sentido global.",
       "“A substituição de *esse* por *este* prejudicaria a coesão” — anáfora × catáfora.",
       "“Há elipse do sujeito em X” — o termo omitido é identificável.",
       "“O conector X estabelece relação de oposição entre os parágrafos” — coesão sequencial."),
]

TXT = ("A Polícia Federal deflagrou ontem a Operação Maré Alta. A ação, que contou com cem agentes, cumpriu vinte mandados em três estados. "
       "Segundo a corporação, o grupo investigado movimentou R$ 50 milhões. Seus líderes, entretanto, ainda não foram localizados. "
       "Isso preocupa os investigadores, pois eles podem deixar o país.")

QUIZ = quiz([
    ("C", "A expressão A ação retoma Operação Maré Alta.",
     "A ação é expressão nominal que retoma a operação citada no período anterior.", TXT),
    ("E", "O pronome que, em “que contou com cem agentes”, retoma cem agentes.",
     "O relativo retoma a ação: foi a ação que contou com cem agentes."),
    ("C", "A expressão a corporação retoma Polícia Federal.",
     "Corporação refere-se à instituição mencionada no início do texto."),
    ("E", "O possessivo Seus refere-se aos investigadores.",
     "Seus líderes são os líderes do grupo investigado."),
    ("C", "O pronome Isso retoma a informação de que os líderes ainda não foram localizados.",
     "Isso é anafórico e resume o conteúdo da frase anterior."),
    ("E", "O pronome eles, no último período, refere-se aos investigadores.",
     "Pelo sentido, quem pode deixar o país são os líderes do grupo."),
    ("C", "O vocábulo entretanto estabelece relação de oposição entre o êxito da operação e a não localização dos líderes.",
     "Entretanto é adversativo: contrapõe o resultado positivo à pendência."),
    ("E", "A substituição de A ação por Ela prejudicaria a correção gramatical do texto.",
     "Ela retomaria a operação de forma gramaticalmente correta."),
    ("C", "Em “O fuzil foi apreendido. A arma estava municiada”, a expressão a arma é hiperônimo de fuzil e garante a coesão.",
     "O termo mais geral (arma) retoma o mais específico (fuzil)."),
    ("E", "Em “O delegado chegou. O delegado ouviu as testemunhas. O delegado expediu o mandado”, a repetição torna o texto mais elegante.",
     "A repetição liga as frases, mas o excesso empobrece o texto; pronomes e elipse seriam preferíveis."),

    ("C", "Em “Só uma medida resolveria o caso: a prisão preventiva”, a expressão uma medida antecipa o que será dito, em relação catafórica.",
     "O termo aponta para a informação que vem depois dos dois-pontos."),
    ("E", "Em “Este é o problema: falta de efetivo”, o emprego de esse no lugar de este manteria a coesão, pois ambos são anafóricos.",
     "Este anuncia o que vem a seguir (catáfora); esse retoma o que já foi dito."),
    ("C", "Em “Os peritos chegaram cedo e isolaram a área”, a omissão do sujeito na segunda oração é recurso de coesão por elipse.",
     "O sujeito os peritos é facilmente identificado."),
    ("E", "Coesão e coerência são conceitos equivalentes: todo texto que emprega conectivos é coerente.",
     "Um texto pode ter conectivos e ser incoerente."),
    ("C", "Um texto pode ser coerente mesmo com poucos elementos coesivos explícitos.",
     "A coerência depende da unidade de sentido, que pode ser construída pelo contexto."),
    ("E", "O período “Choveu muito durante a noite; portanto, as ruas amanheceram secas” é coerente.",
     "A conclusão contradiz a premissa: não há coerência lógica."),
    ("C", "Em “O réu negou o crime. Essa versão, contudo, foi desmentida pelas imagens”, a expressão Essa versão retoma a negativa do réu.",
     "É uma expressão nominal que resume a informação anterior."),
    ("E", "Os advérbios lá e aí não podem exercer função coesiva referencial.",
     "Podem retomar lugares já mencionados: Fomos a Recife. Lá, encontramos o suspeito."),
    ("C", "Os pronomes relativos são elementos de coesão referencial, pois retomam um antecedente.",
     "Que, o qual, cujo e onde retomam termos anteriores."),
    ("E", "A progressão temática exige que o texto repita sempre a mesma informação, sem acrescentar dados novos.",
     "Progressão é justamente acrescentar informações novas mantendo o tema."),
], 20)

SOURCES = [GRAM, "Ingedore Villaça Koch, A coesão textual.", SRC_A]
