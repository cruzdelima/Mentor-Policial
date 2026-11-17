# -*- coding: utf-8 -*-
"""Língua Portuguesa · Advérbio, preposição e conjunção — MATERIAL APROFUNDADO (estudo inicial)."""
from common import *

MATERIAL = material(
    "lp-conectivos-02", "LP", "LP-07", "aprofundado", "Advérbio, preposição e conjunção", "Língua Portuguesa · Morfossintaxe",
    "portugues_conectivos_aprofundado", "Portugues_Conectivos_APROFUNDADO.pdf", None, ["Advérbio, preposição", "e conjunção"],
    ["Teoria completa para o primeiro estudo: classes invariáveis, valor semântico dos conectivos", "e substituições cobradas em prova, com 20 questões no estilo Cebraspe."],
    [("01", "Advérbio", "circunstâncias, locuções, meio, bastante, mal × mau"),
     ("02", "Preposição", "essenciais, acidentais, contrações e valores"),
     ("03", "Conjunção", "coordenativas e subordinativas, com o sentido de cada uma"),
     ("04", "Substituições", "o que mantém e o que altera o sentido"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Advérbio, preposição e conjunção (Língua Portuguesa)",
    "Base: gramáticas de referência (Bechara; Cunha e Cintra).", 150)

THEORY = [
    exam("Como estudar este material",
         "Nessas três classes, o Cebraspe quase nunca pede nomenclatura pura. Ele pergunta pelo **sentido**: "
         "“a substituição de *porém* por *portanto* manteria o sentido?”, “o vocábulo *como* introduz ideia de causa?”. "
         "Por isso, o mais importante é o **quadro de conjunções** da seção 3. Decore os grupos, faça as 20 questões e revise pelo **PDF de resumo**."),

    h2("1. Advérbio"),
    p("**Advérbio** é a palavra **invariável** que modifica um **verbo**, um **adjetivo**, outro **advérbio** ou a **oração inteira**, "
      "acrescentando uma circunstância."),
    bl("Modifica verbo: *O agente agiu **rapidamente**.*",
       "Modifica adjetivo: *O laudo é **muito** detalhado.*",
       "Modifica advérbio: *Chegou **bem** cedo.*",
       "Modifica a oração: ***Infelizmente**, o suspeito fugiu.*"),
    tb(["Circunstância", "Exemplos"], [0.24, 0.76], [
        ("Tempo", "hoje, ontem, já, ainda, sempre, nunca, cedo, tarde, logo, depois"),
        ("Lugar", "aqui, ali, lá, perto, longe, dentro, fora, acima, abaixo"),
        ("Modo", "bem, mal, assim, depressa e a maioria dos terminados em -mente"),
        ("Intensidade", "muito, pouco, bastante, tão, meio, demais, quase"),
        ("Afirmação, negação, dúvida", "sim, certamente · não, nunca, jamais · talvez, possivelmente"),
    ]),
    bl("**Locução adverbial**: duas ou mais palavras com valor de advérbio — *às pressas, de repente, à noite, sem dúvida, de propósito*.",
       "Em sequência de advérbios em *-mente*, o sufixo pode ficar só no último: *agiu **rápida e eficientemente***.",
       "**Palavras denotativas** (*só, até, inclusive, exceto, eis, apenas* com valor de exclusão ou inclusão) não são advérbios pela NGB, "
       "mas mudam o sentido conforme a posição."),
    h3("Advérbio × adjetivo: invariável × variável"),
    tb(["Palavra", "Advérbio (não varia)", "Adjetivo ou pronome (varia)"], [0.16, 0.42, 0.42], [
        ("meio", "*A testemunha estava **meio** nervosa* (= um pouco)", "*Esperou **meia** hora* (= metade)"),
        ("bastante", "*Os agentes estão **bastante** cansados* (= muito)", "*Havia **bastantes** provas* (= muitas)"),
        ("alto, baixo, caro", "*Eles falaram **alto**. As provas custam **caro**.*", "*vozes **altas**, preços **caros***"),
        ("só", "*Eles **só** saíram à noite* (= somente)", "*Eles ficaram **sós*** (= sozinhos)"),
    ]),
    trap("Mal × mau",
         "**Mal** é advérbio (oposto de *bem*): *O policial agiu **mal**.* **Mau** é adjetivo (oposto de *bom*): *Foi um **mau** procedimento.* "
         "Teste: troque por *bem/bom*."),
    key("Posição muda o sentido",
        "***Só** o delegado pode autorizar* (ninguém mais) × *O delegado **só** pode autorizar* (não pode fazer outra coisa). "
        "***Ainda** não chegou* × *Não chegou **ainda***: aqui o sentido se mantém. O Cebraspe pede para avaliar caso a caso."),

    h2("2. Preposição"),
    p("**Preposição** é a palavra invariável que **liga dois termos**, subordinando o segundo ao primeiro: *casa **de** madeira; obedecer **a** normas*."),
    bl("**Essenciais** (só funcionam como preposição): *a, ante, após, até, com, contra, de, desde, em, entre, para, perante, por, sem, sob, sobre, trás*.",
       "**Acidentais** (palavras de outras classes usadas como preposição): *conforme, segundo, consoante, durante, mediante, exceto, salvo, como, visto*.",
       "**Locuções prepositivas**: *a fim de, apesar de, em vez de, ao invés de, por causa de, junto a, de acordo com, em frente a*."),
    tb(["Fenômeno", "O que é", "Exemplos"], [0.2, 0.38, 0.42], [
        ("Combinação", "Preposição + outra palavra **sem perda** de som", "a + o = **ao**; a + onde = **aonde**"),
        ("Contração", "Preposição + outra palavra **com perda** de som", "de + o = **do**; em + a = **na**; por + o = **pelo**; a + a = **à**"),
    ]),
    h3("Valores semânticos"),
    tb(["Relação", "Exemplo"], [0.24, 0.76], [
        ("Lugar", "Mora **em** Recife. Veio **de** Olinda."),
        ("Tempo", "Chegou **às** dez. Trabalha **desde** 2020."),
        ("Causa", "Morreu **de** fome. Foi preso **por** tráfico."),
        ("Finalidade", "Saiu **para** investigar."),
        ("Instrumento / meio", "Abriu **com** a chave. Viajou **de** avião."),
        ("Matéria / posse", "Mesa **de** madeira. Viatura **do** batalhão."),
        ("Assunto", "Falou **sobre** o caso."),
        ("Companhia", "Saiu **com** a equipe."),
    ]),
    trap("Sob × sobre · a × há",
         "**Sob** = debaixo de, sujeito a (*sob sigilo, sob custódia*); **sobre** = em cima de, a respeito de (*sobre a mesa, sobre o caso*). "
         "**Há** = tempo **passado** (*A operação ocorreu **há** três meses*); **a** = tempo **futuro** ou distância (*Daqui **a** dois dias; a cem metros*)."),
    nt("**Sujeito de infinitivo não se contrai com a preposição** na prescrição tradicional: *Está na hora **de o** delegado chegar* "
       "(e não *do delegado chegar*). O motivo: *o delegado* é sujeito de *chegar*, não complemento da preposição. "
       "O uso contraído é comum e aceito por parte dos gramáticos modernos, mas em prova siga a regra tradicional."),

    h2("3. Conjunção"),
    p("**Conjunção** liga **orações** (ou termos de mesma função), estabelecendo entre elas uma relação de sentido. "
      "É o conteúdo mais cobrado deste tópico: memorize o quadro."),
    h3("Coordenativas (ligam orações independentes)"),
    tb(["Tipo", "Sentido", "Conjunções"], [0.18, 0.24, 0.58], [
        ("Aditivas", "Soma", "e, nem (= e não), não só… mas também, tanto… quanto"),
        ("Adversativas", "Oposição", "mas, porém, contudo, todavia, entretanto, no entanto, não obstante"),
        ("Alternativas", "Alternância ou exclusão", "ou, ou… ou, ora… ora, quer… quer, seja… seja"),
        ("Conclusivas", "Conclusão", "logo, portanto, por isso, por conseguinte, assim, pois (**posposto** ao verbo)"),
        ("Explicativas", "Justificativa", "porque, que, porquanto, pois (**anteposto** ao verbo)"),
    ]),
    h3("Subordinativas adverbiais"),
    tb(["Tipo", "Conjunções e locuções", "Exemplo"], [0.17, 0.43, 0.4], [
        ("Causal", "porque, como (anteposto), já que, visto que, uma vez que, porquanto", "**Como** não compareceu, foi conduzido."),
        ("Concessiva", "embora, conquanto, ainda que, mesmo que, se bem que, posto que (+ subjuntivo)", "**Embora** houvesse provas, arquivou-se."),
        ("Condicional", "se, caso, desde que, contanto que, a menos que (+ subjuntivo)", "**Desde que** colabore, terá o benefício."),
        ("Conformativa", "conforme, segundo, consoante, como", "Agiu **conforme** determina a lei."),
        ("Comparativa", "como, (tal) qual, mais… (do) que, menos… (do) que, tanto quanto", "Correu **como** um atleta."),
        ("Consecutiva", "tão… que, tanto… que, tal… que, de modo que, de sorte que", "Correu **tanto que** se cansou."),
        ("Final", "para que, a fim de que, que", "Leia **para que** não erre."),
        ("Proporcional", "à medida que, à proporção que, ao passo que, quanto mais… mais", "**À medida que** avançava, surgiam provas."),
        ("Temporal", "quando, enquanto, assim que, logo que, desde que (+ indicativo), mal", "**Assim que** chegou, isolou a área."),
    ]),
    p("**Integrantes**: *que* e *se* introduzem orações substantivas — *Sei **que** ele mentiu. Não sei **se** ele mentiu.*"),
    trap("As conjunções de dois sentidos",
         "**Desde que** + subjuntivo = **condição**; + indicativo = **tempo**. "
         "**Como** anteposto = **causa**; *conforme* = **conformidade**; *igual a* = **comparação**. "
         "**Pois** antes do verbo = **explicação**; depois do verbo, entre vírgulas = **conclusão** (*Deve, **pois**, ser punido*). "
         "**À medida que** = **proporção**; **na medida em que** = **causa**."),
    key("Concessão pede subjuntivo",
        "*Embora **houvesse** provas* (e não *embora havia*). *Ainda que **chova***. Já **apesar de** é preposição: pede infinitivo ou substantivo — "
        "*Apesar de **haver** provas; apesar **das** provas*."),

    h2("4. Substituições que o Cebraspe testa"),
    tb(["Original", "Troca possível", "Resultado"], [0.24, 0.42, 0.34], [
        ("mas", "porém, contudo, todavia, entretanto, no entanto", "Mantém (ajustando a pontuação)"),
        ("portanto", "logo, por isso, por conseguinte, assim", "Mantém"),
        ("porque (causal)", "já que, visto que, uma vez que", "Mantém"),
        ("embora", "ainda que, mesmo que, conquanto", "Mantém (com subjuntivo)"),
        ("porém", "portanto, porquanto", "**Altera** (oposição vira conclusão ou causa)"),
        ("à medida que", "na medida em que", "**Altera** (proporção vira causa)"),
        ("embora", "apesar de (sem trocar o verbo)", "**Prejudica** a correção"),
    ]),

    h2("5. Como o Cebraspe cobra"),
    bl("**Relação de sentido**: “o conector X introduz ideia de causa / concessão / conclusão”.",
       "**Substituição**: a troca mantém o sentido e a correção? Confira o grupo da conjunção e o modo verbal exigido.",
       "**Variação**: *meio, bastante, só* como advérbio não variam.",
       "**a × há**, **sob × sobre**, **mal × mau**.",
       "**Deslocamento**: advérbios e palavras denotativas mudam o sentido conforme a posição."),
]

QUIZ = quiz([
    ("C", "Em “Os agentes trabalharam bastante”, o vocábulo bastante é advérbio de intensidade e, por isso, não varia.",
     "Bastante modifica o verbo trabalhar; como advérbio, é invariável."),
    ("E", "Em “A testemunha estava meia nervosa”, a concordância está de acordo com a norma-padrão.",
     "Meio, no sentido de um pouco, é advérbio e não varia: meio nervosa."),
    ("C", "Em “Daqui a dois dias o prazo termina”, o emprego de a está correto, pois indica tempo futuro.",
     "Para tempo futuro, usa-se a preposição a; há indica tempo passado."),
    ("E", "Em “A operação ocorreu a três meses”, o emprego de a está de acordo com a norma-padrão.",
     "Tempo decorrido se indica com o verbo haver: ocorreu há três meses."),
    ("C", "Em “O processo tramita sob sigilo”, a preposição sob não poderia ser substituída por sobre sem alteração de sentido.",
     "Sob indica sujeição (sob sigilo); sobre indica posição superior ou assunto."),
    ("E", "Segundo a prescrição gramatical tradicional, está correta a contração em “Está na hora do delegado chegar”.",
     "O delegado é sujeito do infinitivo; a tradição gramatical não admite a contração: de o delegado chegar."),
    ("C", "Em “O réu confessou, porém negou a autoria do disparo”, a conjunção porém poderia ser substituída por contudo, sem prejuízo do sentido e da correção.",
     "Porém e contudo são conjunções adversativas."),
    ("E", "Em “Estudou muito; portanto, foi aprovado”, a conjunção portanto expressa explicação.",
     "Portanto é conclusiva: introduz a consequência lógica do que foi dito."),
    ("C", "Em “Embora houvesse provas, o inquérito foi arquivado”, a conjunção embora introduz ideia de concessão.",
     "Embora apresenta um fato contrário que não impede o da oração principal."),
    ("E", "A frase “Embora havia provas, o inquérito foi arquivado” está de acordo com a norma-padrão.",
     "Conjunções concessivas como embora exigem subjuntivo: embora houvesse."),

    ("C", "No período “Desde que o réu colabore, terá direito ao benefício”, a locução desde que tem valor condicional.",
     "Com subjuntivo, desde que equivale a contanto que: indica condição."),
    ("E", "No período “Desde que assumiu o cargo, o delegado reorganizou a equipe”, a locução desde que tem valor condicional.",
     "Com indicativo, desde que tem valor temporal: a partir do momento em que."),
    ("C", "Em “Como o suspeito não compareceu, foi expedido mandado de condução”, o vocábulo como tem valor causal e poderia ser substituído por visto que.",
     "Como anteposto à principal tem valor de causa, equivalente a visto que, já que."),
    ("E", "Em “À medida que as investigações avançavam, surgiam novos suspeitos”, a locução à medida que poderia ser substituída por na medida em que, sem alteração de sentido.",
     "À medida que indica proporção; na medida em que indica causa. A troca altera o sentido."),
    ("C", "Em “O agente não só prendeu o suspeito, mas também apreendeu a arma”, estabelece-se relação de adição entre as orações.",
     "Não só… mas também é uma correlação aditiva."),
    ("E", "Em “Faça o relatório, pois o prazo vence hoje”, a conjunção pois tem valor conclusivo.",
     "Anteposto ao verbo, depois de imperativo, pois é explicativo: justifica a ordem."),
    ("C", "Em “O agente agiu conforme determina o regulamento”, o vocábulo conforme expressa conformidade.",
     "Conforme introduz oração subordinada adverbial conformativa."),
    ("E", "Em “O suspeito correu tanto que se cansou”, a oração introduzida por que expressa finalidade.",
     "Tanto… que indica consequência: a oração é consecutiva."),
    ("C", "Em “Somente o delegado pode autorizar a diligência”, o deslocamento de somente para depois de pode (“O delegado pode somente autorizar a diligência”) alteraria o sentido do período.",
     "Antes de delegado, a palavra exclui outras pessoas; depois de pode, exclui outras ações."),
    ("E", "Em “O policial agiu mau durante a abordagem”, o emprego de mau está de acordo com a norma-padrão, pois o termo modifica o verbo.",
     "Quem modifica o verbo é o advérbio mal (oposto de bem); mau é adjetivo."),
], 20)

SOURCES = [GRAM, SRC_A]
