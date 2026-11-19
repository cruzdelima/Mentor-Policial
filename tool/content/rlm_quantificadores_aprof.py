# -*- coding: utf-8 -*-
"""Raciocínio Lógico · Quantificadores e diagramas lógicos — MATERIAL APROFUNDADO."""
from common import *

MATERIAL = material(
    "rlm-quantificadores-02", "RLM", "RLM-06", "aprofundado", "Quantificadores e diagramas lógicos", "Raciocínio Lógico e Matemática · Lógica de primeira ordem",
    "raciocinio_quantificadores_aprofundado", "RaciocinioLogico_Quantificadores_APROFUNDADO.pdf", None, ["Quantificadores", "e diagramas"],
    ["Todo, algum e nenhum, a representação em diagramas, as conclusões que decorrem", "e as que não decorrem, com 20 questões no estilo Cebraspe."],
    [("01", "Quantificadores", "universal e existencial"),
     ("02", "Proposições categóricas", "todo, algum, nenhum, algum não"),
     ("03", "Diagramas", "como desenhar cada uma"),
     ("04", "Silogismos", "conclusões que decorrem"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Quantificadores e diagramas lógicos — Raciocínio Lógico",
    "Base: lógica de primeira ordem e silogística aristotélica.", 75)

THEORY = [
    exam("Como estudar este material",
         "Os itens trazem duas ou três afirmações com **todo**, **algum** e **nenhum** e perguntam se uma conclusão é necessariamente "
         "verdadeira. A técnica é sempre a mesma: **desenhe os conjuntos** e procure **um desenho em que as premissas sejam verdadeiras e a "
         "conclusão falsa**. Se encontrar, a conclusão não decorre."),

    h2("1. Quantificadores"),
    tb(["Quantificador", "Símbolo", "Leitura", "Sinônimos"], [0.2, 0.12, 0.3, 0.38], [
        ("Universal", "∀x", "para todo x", "todo, qualquer, cada, todos os"),
        ("Existencial", "∃x", "existe x", "algum, pelo menos um, existe, há"),
    ]),
    p("Uma sentença aberta (*x é policial*) vira proposição quando é **quantificada**: *Todo x é policial* ou *Existe x que é policial*. "
      "Por isso, *Ele é policial* não é proposição, mas *Alguém é policial* é."),

    h2("2. As quatro proposições categóricas"),
    tb(["Tipo", "Forma", "Significado no diagrama"], [0.12, 0.28, 0.6], [
        ("A", "**Todo A é B**", "O círculo A fica **inteiro dentro** de B (A ⊂ B). Não diz que existe B fora de A."),
        ("E", "**Nenhum A é B**", "Os círculos A e B **não se tocam** (A ∩ B = ∅). Vale nos dois sentidos: nenhum B é A."),
        ("I", "**Algum A é B**", "Existe **pelo menos um** elemento na **interseção**. Vale nos dois sentidos: algum B é A."),
        ("O", "**Algum A não é B**", "Existe pelo menos um elemento de A **fora** de B. **Não** vale no sentido inverso."),
    ]),
    trap("O que “algum” NÃO diz",
         "*Algum policial é atleta* **não** significa que algum policial não é atleta: pode ser que **todos** sejam. Em lógica, “algum” é "
         "**pelo menos um**, sem limite superior. Do mesmo modo, *Todo A é B* **não** permite concluir *Todo B é A*."),
    h3("O que se pode inverter"),
    bl("*Nenhum A é B* ⇔ *Nenhum B é A*.",
       "*Algum A é B* ⇔ *Algum B é A*.",
       "*Todo A é B* **não** equivale a *Todo B é A* (só permite *Algum B é A*, se A não for vazio).",
       "*Algum A não é B* **não** equivale a *Algum B não é A*."),

    h2("3. Negações (revisão)"),
    tb(["Proposição", "Negação"], [0.5, 0.5], [
        ("Todo A é B", "Algum A não é B"),
        ("Nenhum A é B", "Algum A é B"),
        ("Algum A é B", "Nenhum A é B"),
        ("Algum A não é B", "Todo A é B"),
    ]),

    h2("4. Diagramas: o método"),
    p("Desenhe primeiro as afirmações **universais** (todo, nenhum), que fixam o desenho; depois as **particulares** (algum), que só marcam "
      "a existência de um elemento. Quando houver **várias formas possíveis** de desenhar, a conclusão só é válida se for verdadeira em "
      "**todas** elas."),
    h3("Exemplo 1 (conclusão válida)"),
    bl("P1: *Todo agente é concursado.* · P2: *Nenhum concursado é estagiário.*",
       "Desenho: o círculo dos agentes dentro do círculo dos concursados; o dos estagiários fora dos concursados.",
       "Conclusão válida: *Nenhum agente é estagiário.*"),
    h3("Exemplo 2 (conclusão inválida)"),
    bl("P1: *Todo perito é servidor.* · P2: *Algum servidor é professor.*",
       "O professor que é servidor pode estar **dentro** ou **fora** do círculo dos peritos.",
       "*Algum perito é professor* **não** decorre: há um desenho em que nenhum perito é professor."),
    h3("Exemplo 3 (conclusão válida com algum)"),
    bl("P1: *Algum escrivão é advogado.* · P2: *Todo advogado é bacharel.*",
       "O escrivão que é advogado está dentro do círculo dos advogados, que está dentro dos bacharéis.",
       "Conclusão válida: *Algum escrivão é bacharel.*"),

    h2("5. Quantificadores com conectivos"),
    bl("*Todo A é B* equivale a *Se x é A, então x é B* (para qualquer x).",
       "*Nenhum A é B* equivale a *Se x é A, então x não é B*.",
       "Por isso, *Todo policial é concursado* e *Se alguém é policial, então é concursado* têm o mesmo sentido.",
       "Contrapositiva: *Todo A é B* ⇔ *Todo não B é não A* (quem não é concursado não é policial)."),

    h2("6. Como o Cebraspe cobra"),
    bl("Duas premissas + uma conclusão: desenhe e procure o **contraexemplo**.",
       "Conclusões com **algum** a partir de premissas com **todo** e **algum** costumam ser armadilha: confira se o elemento está mesmo na interseção.",
       "Itens de negação: *Todo* ↔ *algum não*; *algum* ↔ *nenhum*.",
       "Na dúvida real, **deixe em branco**: no Cebraspe, cada erro anula um acerto."),
]

QUIZ = quiz([
    ("C", "A proposição “Nenhum agente é estagiário” é equivalente a “Nenhum estagiário é agente”.",
     "Na universal negativa, os conjuntos não se tocam: vale nos dois sentidos."),
    ("E", "A proposição “Todo escrivão é bacharel” é equivalente a “Todo bacharel é escrivão”.",
     "Todo A é B não permite inverter."),
    ("C", "A proposição “Algum perito é médico” é equivalente a “Algum médico é perito”.",
     "O elemento está na interseção: vale nos dois sentidos."),
    ("E", "Da proposição “Algum policial é atleta” conclui-se que algum policial não é atleta.",
     "“Algum” é pelo menos um; pode ser que todos sejam atletas."),
    ("C", "A proposição “Existe x tal que x é policial” é uma proposição, ainda que a sentença “x é policial” não o seja.",
     "O quantificador transforma a sentença aberta em proposição."),
    ("C", "Das premissas “Todo agente é concursado” e “Nenhum concursado é estagiário”, conclui-se que nenhum agente é estagiário.",
     "Os agentes estão dentro dos concursados, que não tocam os estagiários."),
    ("E", "Das premissas “Todo perito é servidor” e “Algum servidor é professor”, conclui-se que algum perito é professor.",
     "O servidor professor pode estar fora do círculo dos peritos."),
    ("C", "Das premissas “Algum escrivão é advogado” e “Todo advogado é bacharel”, conclui-se que algum escrivão é bacharel.",
     "O escrivão advogado está dentro dos bacharéis."),
    ("E", "A negação de “Algum suspeito não foi ouvido” é “Nenhum suspeito foi ouvido”.",
     "A negação é “Todo suspeito foi ouvido”."),
    ("C", "A proposição “Todo policial é concursado” equivale a “Quem não é concursado não é policial”.",
     "É a contrapositiva da universal afirmativa."),

    ("C", "Considere as premissas “Todo delegado é bacharel em direito” e “Rui não é bacharel em direito”. Delas se conclui que Rui não é delegado.",
     "Rui está fora do círculo dos bacharéis, que contém o dos delegados."),
    ("E", "Considere as premissas “Todo delegado é bacharel em direito” e “Lia é bacharel em direito”. Delas se conclui que Lia é delegada.",
     "Lia pode estar no círculo dos bacharéis, mas fora do dos delegados."),
    ("E", "Considere as premissas “Nenhum traficante é servidor” e “Algum servidor é investigado”. Delas se conclui que algum traficante é investigado.",
     "O servidor investigado não é traficante; os traficantes podem não ter interseção com os investigados."),
    ("C", "Considere as premissas “Nenhum traficante é servidor” e “Algum investigado é servidor”. Delas se conclui que algum investigado não é traficante.",
     "O investigado que é servidor não pode ser traficante."),
    ("E", "Considere as premissas “Todo agente é atirador” e “Todo escrivão é atirador”. Delas se conclui que algum agente é escrivão.",
     "Os dois círculos podem estar dentro do dos atiradores sem se tocar."),
    ("C", "Considere as premissas “Todo agente é atirador” e “Nenhum atirador é sedentário”. Delas se conclui que nenhum sedentário é agente.",
     "Os agentes estão dentro dos atiradores, que não tocam os sedentários."),
    ("E", "A negação de “Todos os presos foram transferidos” é “Nenhum preso foi transferido”.",
     "A negação é “Algum preso não foi transferido”."),
    ("C", "A proposição “Nem todo investigado é culpado” é equivalente a “Algum investigado não é culpado”.",
     "“Nem todo” nega o “todo”."),
    ("E", "Das premissas “Algum A é B” e “Algum B é C”, conclui-se que algum A é C.",
     "Os elementos das duas interseções podem ser diferentes."),
    ("C", "Se for verdadeira a proposição “Algum servidor não é estável”, então será falsa a proposição “Todo servidor é estável”.",
     "Uma é a negação da outra."),
], 20)

SOURCES = [
    "Lógica de primeira ordem (quantificadores) e silogística categórica.",
    "Obras de referência: Copi, Introdução à lógica; Alencar Filho, Iniciação à lógica matemática.",
    SRC_A,
]
