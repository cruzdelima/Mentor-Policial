# -*- coding: utf-8 -*-
"""Língua Portuguesa · Relações semânticas entre orações, períodos e parágrafos — MATERIAL APROFUNDADO."""
from common import *

MATERIAL = material(
    "lp-relacoes-02", "LP", "LP-22", "aprofundado", "Relações semânticas entre orações, períodos e parágrafos", "Língua Portuguesa · Texto",
    "portugues_relacoes_aprofundado", "Portugues_Relacoes_Semanticas_APROFUNDADO.pdf", None, ["Relações semânticas", "entre orações e parágrafos"],
    ["Teoria completa para o primeiro estudo: as relações lógicas do texto, com e sem conectivo,", "e os articuladores entre parágrafos, com 20 questões no estilo Cebraspe."],
    [("01", "Relações lógicas", "adição, oposição, concessão, causa, conclusão e outras"),
     ("02", "Sem conectivo", "relações implícitas entre orações justapostas"),
     ("03", "Entre parágrafos", "articuladores textuais"),
     ("04", "Oposição × concessão", "a diferença de foco"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Relações semânticas entre orações, períodos e parágrafos (Língua Portuguesa)",
    "Base: gramáticas de referência e Koch, A coesão textual.", 150)

THEORY = [
    exam("Como estudar este material",
         "Este tópico une **conjunções** (veja o material *Advérbio, preposição e conjunção*) e **coesão sequencial**. "
         "A pergunta da banca é sempre a mesma: **qual a relação lógica** entre as partes do texto, e ela se mantém se o conector for trocado? "
         "Aqui o foco é o texto: relações implícitas e articuladores entre parágrafos."),

    h2("1. As relações lógicas"),
    tb(["Relação", "Conectores típicos", "Exemplo"], [0.16, 0.42, 0.42], [
        ("Adição", "e, nem, além disso, também, não só… mas também", "Prendeu o autor; **além disso**, recuperou a carga."),
        ("Oposição (adversidade)", "mas, porém, contudo, todavia, no entanto, em contrapartida", "Confessou, **mas** não indicou os comparsas."),
        ("Concessão", "embora, ainda que, mesmo que, apesar de, não obstante", "**Embora** houvesse provas, arquivou-se o caso."),
        ("Causa", "porque, pois, como, já que, visto que, uma vez que, em razão de", "**Como** não compareceu, foi conduzido."),
        ("Consequência", "tão… que, de modo que, de forma que", "Chovia **tanto que** a operação foi adiada."),
        ("Conclusão", "logo, portanto, por isso, assim, dessa forma, consequentemente", "Há provas; **portanto**, haverá denúncia."),
        ("Explicação", "pois, porque, que (após afirmação ou ordem)", "Saia, **pois** a reunião vai começar."),
        ("Condição", "se, caso, desde que, contanto que", "**Se** houver flagrante, haverá prisão."),
        ("Finalidade", "para que, a fim de que, com o objetivo de", "Isolou a área **para que** não houvesse contaminação."),
        ("Tempo", "quando, enquanto, assim que, depois que, antes que", "**Assim que** chegou, isolou a área."),
        ("Proporção", "à medida que, à proporção que, quanto mais… mais", "**À medida que** a perícia avançava, surgiam provas."),
        ("Comparação", "como, tal qual, mais/menos… que", "Agiu **como** um profissional."),
        ("Conformidade", "conforme, segundo, consoante", "**Segundo** o laudo, houve fraude."),
        ("Alternância", "ou… ou, ora… ora, quer… quer", "**Ora** confirmava, **ora** negava."),
        ("Exemplificação, retificação, resumo", "por exemplo, isto é, ou melhor, em síntese, em suma", "**Em síntese**, a operação foi bem-sucedida."),
    ]),

    h2("2. Oposição × concessão"),
    p("As duas expressam contraste, mas com **foco** diferente:"),
    bl("**Oposição (mas)**: o argumento **depois** do conector prevalece — *O réu é primário, **mas** o crime é grave* (destaque: a gravidade).",
       "**Concessão (embora)**: o argumento **da oração concessiva** é reconhecido, mas **não impede** o da principal — "
       "***Embora** o réu seja primário, o crime é grave* (mesmo destaque, construção diferente).",
       "Por isso, *mas* e *embora* podem reescrever a mesma ideia, **trocando a posição** dos argumentos: "
       "*Confessou, mas negou a autoria* ≈ *Embora tenha confessado, negou a autoria*."),

    h2("3. Relações sem conectivo"),
    p("Orações e períodos **justapostos** (separados só por pontuação) mantêm relações lógicas que o leitor infere:"),
    bl("*Choveu muito. A operação foi adiada.* › **causa e consequência** (= *por isso*).",
       "*O réu negou tudo. As imagens o desmentiram.* › **oposição** (= *porém*).",
       "*Feche a porta: está ventando.* › **explicação** (= *pois*).",
       "O Cebraspe pergunta: “a inserção de *portanto* entre os períodos explicitaria a relação já existente”."),

    h2("4. Entre parágrafos"),
    tb(["Função", "Articuladores"], [0.3, 0.7], [
        ("Introduzir / ordenar", "Em primeiro lugar, inicialmente, primeiramente, a princípio"),
        ("Acrescentar argumento", "Além disso, ademais, também, outrossim, não bastasse isso"),
        ("Opor", "Em contrapartida, por outro lado, no entanto, entretanto"),
        ("Concluir", "Dessa forma, assim, portanto, em suma, em síntese, por fim"),
        ("Exemplificar", "Por exemplo, a exemplo de, como se vê em"),
        ("Retomar", "Nesse sentido, diante disso, nesse contexto"),
    ]),

    h2("5. Como o Cebraspe cobra"),
    bl("“O conector X introduz ideia de Y” (causa, concessão, conclusão…).",
       "“A substituição de X por Y manteria a relação de sentido” — mesmo grupo lógico.",
       "“Entre os períodos há relação implícita de causa e consequência.”",
       "“O parágrafo X introduz argumento contrário ao do parágrafo anterior.”"),
]

QUIZ = quiz([
    ("C", "Em “Prendeu o autor; além disso, recuperou a carga”, a expressão além disso estabelece relação de adição.",
     "Acrescenta uma informação à anterior."),
    ("E", "Em “Embora houvesse provas, o caso foi arquivado”, a conjunção embora introduz ideia de causa.",
     "Embora introduz concessão: as provas não impediram o arquivamento."),
    ("C", "Em “Há provas suficientes; portanto, haverá denúncia”, portanto introduz uma conclusão.",
     "A denúncia é conclusão lógica da existência de provas."),
    ("E", "Em “Isolou a área para que não houvesse contaminação”, a locução para que expressa causa.",
     "Para que expressa finalidade."),
    ("C", "Em “Segundo o laudo, houve fraude”, segundo expressa conformidade.",
     "Equivale a conforme o laudo."),
    ("E", "Em “À medida que a perícia avançava, surgiam provas”, a locução à medida que expressa causa.",
     "À medida que expressa proporção."),
    ("C", "Em “Chovia tanto que a operação foi adiada”, a estrutura tanto… que expressa consequência.",
     "O adiamento é consequência da chuva intensa."),
    ("E", "Em “Ora confirmava a versão, ora a negava”, há relação de adição.",
     "Ora… ora expressa alternância."),
    ("C", "Em “Se houver flagrante, haverá prisão”, a conjunção se introduz condição.",
     "A prisão depende do flagrante."),
    ("E", "Em “Em síntese, a operação foi bem-sucedida”, a expressão em síntese introduz exemplificação.",
     "Em síntese introduz resumo ou conclusão."),

    ("C", "Entre os períodos “Choveu muito durante a madrugada. A operação foi adiada.” há relação implícita de causa e consequência.",
     "A inserção de por isso explicitaria a relação já existente."),
    ("E", "Entre os períodos “O réu negou tudo. As imagens o desmentiram.” há relação implícita de adição.",
     "O segundo período contraria o primeiro: relação de oposição."),
    ("C", "O período “Confessou, mas negou a autoria do disparo” poderia ser reescrito como “Embora tenha confessado, negou a autoria do disparo”, mantendo-se a relação de contraste.",
     "A oposição foi transformada em concessão, com o mesmo foco no segundo argumento."),
    ("E", "A substituição de embora por porque em “Embora estivesse ferido, o agente continuou” manteria a relação de sentido.",
     "Porque introduz causa, não concessão: o sentido se altera."),
    ("C", "A expressão Em contrapartida, no início de um parágrafo, indica que ele introduz ideia contrária à do parágrafo anterior.",
     "É articulador de oposição entre parágrafos."),
    ("E", "O articulador Além disso, no início de um parágrafo, indica que o parágrafo apresentará conclusão do texto.",
     "Além disso acrescenta argumento; para concluir, usam-se dessa forma, em suma."),
    ("C", "Em “Saia, pois a reunião vai começar”, a conjunção pois introduz explicação.",
     "Justifica a ordem dada na oração anterior."),
    ("E", "Em “O réu é primário, mas o crime é grave”, o argumento que prevalece é o da primariedade do réu.",
     "Com mas, prevalece o argumento posterior: a gravidade do crime."),
    ("C", "Em “Como não compareceu, foi conduzido coercitivamente”, como poderia ser substituído por visto que, mantendo-se a relação de causa.",
     "Ambos introduzem causa."),
    ("E", "Em “Assim que chegou, o perito isolou a área”, a locução assim que expressa conformidade.",
     "Assim que expressa tempo (= logo que)."),
], 20)

SOURCES = [GRAM, "Ingedore Villaça Koch, A coesão textual.", SRC_A]
