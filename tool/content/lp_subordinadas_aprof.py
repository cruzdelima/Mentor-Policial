# -*- coding: utf-8 -*-
"""Língua Portuguesa · Orações subordinadas — MATERIAL APROFUNDADO (estudo inicial)."""
from common import *

MATERIAL = material(
    "lp-subordinadas-02", "LP", "LP-10", "aprofundado", "Orações subordinadas", "Língua Portuguesa · Sintaxe do período",
    "portugues_subordinadas_aprofundado", "Portugues_Oracoes_Subordinadas_APROFUNDADO.pdf", None, ["Orações", "subordinadas"],
    ["Teoria completa para o primeiro estudo: substantivas, adjetivas restritivas e explicativas,", "as nove adverbiais e as reduzidas, com 20 questões no estilo Cebraspe."],
    [("01", "Substantivas", "as seis funções e o teste do ISSO"),
     ("02", "Adjetivas", "restritiva × explicativa e a vírgula que muda o sentido"),
     ("03", "Adverbiais", "as nove circunstâncias e suas conjunções"),
     ("04", "Reduzidas", "infinitivo, gerúndio e particípio"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Sintaxe do período — orações subordinadas (Língua Portuguesa)",
    "Base: gramáticas de referência (Bechara; Cunha e Cintra).", 240)

THEORY = [
    exam("Como estudar este material",
         "Este é um dos tópicos mais cobrados pelo Cebraspe, quase sempre de forma indireta: “a retirada das vírgulas alteraria o sentido” "
         "(adjetiva explicativa × restritiva), “o vocábulo *que* é pronome relativo”, “a oração expressa uma concessão”. "
         "Estude na ordem: **substantivas** (o teste do ISSO), **adjetivas** (a vírgula) e **adverbiais** (o sentido)."),

    h2("1. Subordinação"),
    p("Na subordinação, uma oração (**subordinada**) exerce uma **função sintática** em outra (**principal**): sujeito, objeto, adjunto… "
      "Por isso as subordinadas se dividem conforme a classe de palavra a que equivalem:"),
    tb(["Subordinada", "Equivale a", "Exemplo"], [0.2, 0.26, 0.54], [
        ("Substantiva", "um **substantivo**", "Espero **que ele confesse**. (= espero **a confissão**)"),
        ("Adjetiva", "um **adjetivo**", "O réu **que confessou** foi solto. (= o réu **confesso**)"),
        ("Adverbial", "um **advérbio**", "**Quando a viatura chegou**, ele fugiu. (= **ontem**, ele fugiu)"),
    ]),

    h2("2. Orações subordinadas substantivas"),
    p("Introduzidas pelas **conjunções integrantes** *que* e *se* (ou por pronomes e advérbios interrogativos). "
      "**Teste**: a oração inteira pode ser substituída por **ISSO**."),
    tb(["Tipo", "Função", "Exemplo"], [0.2, 0.32, 0.48], [
        ("Subjetiva", "**Sujeito** do verbo da principal", "É fundamental **que as provas sejam preservadas**. (Isso é fundamental)"),
        ("Objetiva direta", "**Objeto direto**", "O delegado afirmou **que o caso estava encerrado**. (afirmou isso)"),
        ("Objetiva indireta", "**Objeto indireto** (com preposição)", "Lembrou-se **de que havia esquecido o celular**. (lembrou-se disso)"),
        ("Completiva nominal", "**Complemento nominal** (com preposição)", "Tenho certeza **de que ele mentiu**. (certeza disso)"),
        ("Predicativa", "**Predicativo** do sujeito, após verbo de ligação", "A verdade é **que ninguém viu o crime**. (a verdade é isso)"),
        ("Apositiva", "**Aposto**, em geral após dois-pontos", "Só uma coisa importava: **que a vítima fosse localizada**."),
    ]),
    key("Como reconhecer a subjetiva",
        "Estruturas típicas: **verbo de ligação + adjetivo/substantivo** (*É necessário que…, É verdade que…*), "
        "**verbos como** *convir, importar, parecer, constar, acontecer* (*Convém que…, Parece que…*) e **voz passiva** "
        "(*Sabe-se que…, Foi decidido que…*). O verbo da principal fica sempre na **3ª pessoa do singular**."),
    bl("**Objetiva indireta × completiva nominal**: as duas têm preposição. Olhe o termo que a oração completa: **verbo** › objetiva indireta; "
       "**nome** › completiva nominal. *Necessito **de que me ajudem*** (verbo) × *Tenho necessidade **de que me ajudem*** (nome).",
       "**Se** integrante: *Ninguém sabe **se** o suspeito voltará* (= ninguém sabe isso).",
       "Não se separa por **vírgula** a oração substantiva da principal (salvo a apositiva, com dois-pontos ou vírgula)."),

    h2("3. Orações subordinadas adjetivas"),
    p("Introduzidas por **pronome relativo** (*que, quem, o qual, cujo, onde, quanto*), que retoma um termo anterior (antecedente). "
      "**Teste**: o *que* relativo pode ser trocado por **o qual / a qual / os quais / as quais**."),
    tb(["Tipo", "Pontuação", "Sentido", "Exemplo"], [0.15, 0.17, 0.33, 0.35], [
        ("Restritiva", "**Sem** vírgulas", "**Restringe**: só uma parte do grupo", "Os presos **que trabalham** têm direito à remição."),
        ("Explicativa", "**Entre** vírgulas", "**Explica**: vale para todo o grupo", "Os agentes, **que estavam de plantão**, atenderam a ocorrência."),
    ]),
    trap("A vírgula que muda o sentido",
         "*Os policiais **que estavam de folga** foram convocados* — só os que estavam de folga. "
         "*Os policiais, **que estavam de folga**, foram convocados* — todos estavam de folga. "
         "Por isso, **inserir ou retirar as vírgulas** de uma oração adjetiva **altera o sentido** — e é item garantido no Cebraspe."),
    h3("Que relativo × que integrante"),
    tb(["", "Relativo", "Integrante"], [0.2, 0.4, 0.4], [
        ("Teste", "Troca por **o qual**", "Troca da oração por **isso**"),
        ("Função", "Exerce função sintática na oração (sujeito, objeto…)", "Não exerce função; só liga"),
        ("Exemplo", "*O documento **que** o réu apresentou é falso.* (o qual)", "*Espero **que** o laudo saia hoje.* (espero isso)"),
    ]),

    h2("4. Orações subordinadas adverbiais"),
    p("Exercem função de **adjunto adverbial** da principal e expressam uma circunstância. O sentido vem da conjunção:"),
    tb(["Tipo", "Conjunções", "Exemplo"], [0.17, 0.4, 0.43], [
        ("Causal", "porque, como (anteposto), já que, visto que, uma vez que", "**Como o réu não compareceu**, foi conduzido."),
        ("Concessiva", "embora, ainda que, mesmo que, conquanto, se bem que", "**Embora estivesse cansado**, concluiu o laudo."),
        ("Condicional", "se, caso, desde que, contanto que, a menos que", "**Se houver flagrante**, a prisão será imediata."),
        ("Conformativa", "conforme, segundo, consoante, como", "Agiu **conforme o advogado orientara**."),
        ("Comparativa", "como, (tal) qual, mais/menos… (do) que", "Correu **como um atleta (corre)**."),
        ("Consecutiva", "tão/tanto/tal… que, de modo que, de sorte que", "Estudou **tanto que passou em primeiro**."),
        ("Final", "para que, a fim de que", "Isolou a área **para que não houvesse contaminação**."),
        ("Proporcional", "à medida que, à proporção que, quanto mais… mais", "**À medida que a perícia avançava**, surgiam provas."),
        ("Temporal", "quando, enquanto, assim que, logo que, desde que, mal", "**Quando a viatura chegou**, o suspeito fugiu."),
    ]),
    bl("**Concessiva e condicional** pedem **subjuntivo**: *embora **estivesse**; caso **confesse***.",
       "**Desde que** + subjuntivo = condição; + indicativo = tempo.",
       "**Pontuação**: a adverbial **anteposta** ou **intercalada** à principal costuma vir separada por vírgula; "
       "posposta, a vírgula é facultativa (e não se usa antes das consecutivas *tão… que*)."),

    h2("5. Orações reduzidas"),
    p("Não têm conectivo e apresentam o verbo numa **forma nominal**. Para classificá-las, **desenvolva**: transforme-as em oração com conjunção."),
    tb(["Forma", "Exemplo", "Desenvolvida", "Valor"], [0.16, 0.3, 0.34, 0.2], [
        ("Infinitivo", "**Ao chegar** à delegacia, o advogado pediu vista.", "**Quando chegou** à delegacia…", "Temporal"),
        ("Infinitivo", "É necessário **revisar os procedimentos**.", "É necessário **que se revisem**…", "Subjetiva"),
        ("Gerúndio", "**Sendo réu primário**, terá direito ao benefício.", "**Como é réu primário**…", "Causal"),
        ("Particípio", "**Terminada a audiência**, os autos foram conclusos.", "**Assim que terminou** a audiência…", "Temporal"),
    ]),

    h2("6. Como o Cebraspe cobra"),
    bl("**Vírgulas da adjetiva**: retirar ou inserir altera o sentido (restritiva × explicativa).",
       "**Natureza do que**: relativo (troca por *o qual*) × integrante (troca por *isso*).",
       "**Classificação pelo sentido**: “a oração expressa concessão / causa / condição / finalidade”.",
       "**Substituição de conectivo**: *embora* por *ainda que* (mantém); *como* causal por *visto que* (mantém); *à medida que* por *na medida em que* (altera).",
       "**Vírgula indevida** entre a principal e a substantiva (*É necessário, que…* é erro)."),
]

QUIZ = quiz([
    ("C", "No período “É fundamental que as provas sejam preservadas”, a oração “que as provas sejam preservadas” é subordinada substantiva subjetiva.",
     "A oração é o sujeito de é fundamental (isso é fundamental)."),
    ("E", "No período “O delegado afirmou que o caso estava encerrado”, a oração introduzida por que é subordinada adjetiva.",
     "A oração é objeto direto de afirmou (afirmou isso): substantiva objetiva direta."),
    ("C", "Em “Ninguém sabe se o suspeito voltará”, o vocábulo se é conjunção integrante.",
     "Se introduz oração substantiva objetiva direta (ninguém sabe isso)."),
    ("E", "No período “Tenho certeza de que ele mentiu”, a oração “de que ele mentiu” é subordinada substantiva objetiva indireta.",
     "A oração completa o substantivo certeza: é completiva nominal."),
    ("C", "No período “Lembrou-se de que havia esquecido o celular”, a oração introduzida por de que é subordinada substantiva objetiva indireta.",
     "Completa o verbo lembrar-se, que exige a preposição de."),
    ("E", "No período “Os agentes, que estavam de plantão, atenderam a ocorrência”, a oração entre vírgulas restringe o sentido do termo agentes.",
     "Entre vírgulas, a oração adjetiva é explicativa: refere-se a todos os agentes."),
    ("C", "No período “Os presos que trabalham têm direito à remição”, a oração adjetiva restritiva indica que apenas parte dos presos tem esse direito.",
     "Sem vírgulas, a oração restringe: só os presos que trabalham."),
    ("E", "No período “Embora estivesse cansado, o perito concluiu o laudo”, a oração subordinada expressa causa.",
     "Embora introduz concessão: o cansaço não impediu a conclusão do laudo."),
    ("C", "No período “Se houver flagrante, a prisão será imediata”, a oração subordinada é adverbial condicional.",
     "Se introduz a condição para o fato da principal."),
    ("E", "No período “Ao chegar à delegacia, o advogado pediu vista dos autos”, a oração reduzida expressa finalidade.",
     "Desenvolvida, a oração é quando chegou à delegacia: valor temporal."),

    ("C", "No período “O laudo, que foi elaborado por dois peritos, confirmou a fraude”, a supressão das vírgulas alteraria o sentido do período.",
     "Sem vírgulas, a oração passaria a restritiva, sugerindo a existência de outros laudos."),
    ("E", "Em “O documento que o réu apresentou é falso”, o vocábulo que é conjunção integrante.",
     "Que retoma documento e pode ser trocado por o qual: é pronome relativo."),
    ("C", "No período “A verdade é que ninguém viu o crime”, a oração “que ninguém viu o crime” é subordinada substantiva predicativa.",
     "A oração é predicativo do sujeito a verdade, após o verbo de ligação ser."),
    ("E", "No período “Só uma coisa importava: que a vítima fosse localizada”, a oração após os dois-pontos é subordinada adjetiva explicativa.",
     "A oração explica o termo uma coisa e funciona como aposto: substantiva apositiva."),
    ("C", "No período “À medida que a perícia avançava, novas provas surgiam”, a oração subordinada expressa proporção.",
     "À medida que relaciona proporcionalmente os dois fatos."),
    ("E", "No período “Estudou tanto que passou em primeiro lugar”, a oração “que passou em primeiro lugar” é subordinada adverbial final.",
     "Tanto… que indica consequência: a oração é consecutiva."),
    ("C", "No período “O réu agiu conforme o advogado orientara”, a oração “conforme o advogado orientara” é subordinada adverbial conformativa.",
     "Conforme indica conformidade: o réu agiu de acordo com a orientação."),
    ("E", "No período “Terminada a audiência, os autos foram conclusos”, a oração reduzida de particípio tem valor de concessão.",
     "Desenvolvida, é assim que terminou a audiência: valor temporal."),
    ("C", "No período “Quando a viatura chegou, o suspeito fugiu”, a vírgula após chegou separa a oração adverbial anteposta à principal.",
     "Oração adverbial anteposta costuma ser separada da principal por vírgula."),
    ("E", "Em “É necessário que todos colaborem”, a inserção de vírgula logo após necessário estaria de acordo com a norma-padrão.",
     "A vírgula separaria a principal da oração subjetiva, que é seu sujeito."),
], 20)

SOURCES = [GRAM, SRC_A]
