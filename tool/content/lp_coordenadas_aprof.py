# -*- coding: utf-8 -*-
"""Língua Portuguesa · Orações coordenadas — MATERIAL APROFUNDADO (estudo inicial)."""
from common import *

MATERIAL = material(
    "lp-coordenadas-02", "LP", "LP-09", "aprofundado", "Orações coordenadas", "Língua Portuguesa · Sintaxe do período",
    "portugues_coordenadas_aprofundado", "Portugues_Oracoes_Coordenadas_APROFUNDADO.pdf", None, ["Orações", "coordenadas"],
    ["Teoria completa para o primeiro estudo: coordenação, os cinco tipos de oração sindética,", "valores especiais das conjunções e pontuação, com 20 questões no estilo Cebraspe."],
    [("01", "Coordenação", "período composto, sindéticas e assindéticas"),
     ("02", "Os cinco tipos", "aditivas, adversativas, alternativas, conclusivas, explicativas"),
     ("03", "Valores especiais", "e adversativo, pois, mas × porém"),
     ("04", "Pontuação", "vírgula e ponto e vírgula na coordenação"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Sintaxe do período — orações coordenadas (Língua Portuguesa)",
    "Base: gramáticas de referência (Bechara; Cunha e Cintra).", 150)

THEORY = [
    exam("Como estudar este material",
         "Orações coordenadas aparecem no Cebraspe como **relação de sentido** (“a oração introduzida por *pois* expressa conclusão?”), "
         "**substituição de conjunção** e **pontuação** (vírgula antes de *e*, conjunção deslocada entre vírgulas). "
         "Este material complementa o de *Advérbio, preposição e conjunção*: aqui o foco é a oração inteira."),

    h2("1. Período composto por coordenação"),
    p("No **período composto**, há duas ou mais orações. Elas podem se relacionar de dois modos:"),
    tb(["Processo", "Relação", "Exemplo"], [0.2, 0.4, 0.4], [
        ("Coordenação", "Orações **sintaticamente independentes**: nenhuma é termo da outra", "*O agente revistou o carro **e** encontrou a droga.*"),
        ("Subordinação", "Uma oração exerce **função sintática** na outra (principal)", "*O agente disse **que encontrou a droga**.*"),
    ]),
    p("Independência sintática **não** significa independência de sentido: as coordenadas se relacionam pelo sentido (soma, oposição, conclusão…). "
      "No período composto só por coordenação **não existe oração principal**."),
    h3("Sindéticas e assindéticas"),
    bl("**Assindética**: ligada sem conjunção, só por pontuação — *Chegou, viu, prendeu.*",
       "**Sindética**: introduzida por conjunção coordenativa — *Chegou **e** prendeu.*",
       "Num período como *O delegado ouviu as testemunhas, analisou as imagens **e** expediu o mandado*, "
       "as duas primeiras orações são **assindéticas** e a última é **sindética aditiva**."),

    h2("2. Os cinco tipos de coordenada sindética"),
    tb(["Tipo", "Sentido", "Conjunções", "Exemplo"], [0.15, 0.17, 0.33, 0.35], [
        ("Aditiva", "Soma de fatos", "e, nem, não só… mas também, tanto… quanto", "Prendeu o autor **e** recuperou a carga."),
        ("Adversativa", "Oposição, contraste", "mas, porém, contudo, todavia, entretanto, no entanto", "Confessou, **mas** não indicou os comparsas."),
        ("Alternativa", "Alternância ou exclusão", "ou, ou… ou, ora… ora, quer… quer, seja… seja", "**Ou** colabora, **ou** será indiciado."),
        ("Conclusiva", "Conclusão lógica", "logo, portanto, por isso, assim, por conseguinte, pois (posposto)", "O laudo é conclusivo; **logo**, a autoria está provada."),
        ("Explicativa", "Justificativa do que se disse", "porque, que, pois (anteposto), porquanto", "Feche a porta, **pois** está ventando."),
    ]),
    bl("**Nem** = *e não*: *Não estudou **nem** trabalhou.* (adição de negações). Evite *e nem*, salvo com valor enfático (*nem sequer*).",
       "**Não só… mas também** e **tanto… quanto** são **correlações aditivas**, não adversativas."),

    h2("3. Valores especiais"),
    h3("“E” com valor adversativo"),
    p("A conjunção *e* pode ligar fatos que se opõem: *Estudou muito **e** não foi aprovado* (= *mas* não foi aprovado). "
      "A classificação formal continua aditiva, mas o Cebraspe pergunta pelo **sentido**: a relação é de **oposição**."),
    h3("Pois: explicativo × conclusivo"),
    tb(["Posição", "Valor", "Exemplo"], [0.3, 0.2, 0.5], [
        ("Antes do verbo, no início da oração", "Explicativo", "Saia logo, **pois** a reunião vai começar."),
        ("Depois do verbo, entre vírgulas", "Conclusivo", "O réu confessou; deve, **pois**, ser punido."),
    ]),
    h3("Explicativa × causal"),
    p("A **causal** (subordinada) indica a **causa real** do fato: *A rua está molhada **porque choveu***. "
      "A **explicativa** (coordenada) justifica **por que se afirma** algo: *Choveu, **porque a rua está molhada***. "
      "A rua molhada não causa a chuva; é a evidência que justifica a afirmação. Após **imperativo**, a oração com *porque/pois/que* é explicativa: "
      "*Venha logo, **que** a reunião vai começar.*"),
    h3("Mas × porém"),
    bl("**Mas** fica sempre no **início** da oração que introduz.",
       "**Porém, contudo, todavia, entretanto, no entanto** podem **deslocar-se** para o meio ou o fim da oração, entre vírgulas: "
       "*O suspeito, **porém**, negou tudo.* O sentido adversativo se mantém.",
       "**Conclusivas** também se deslocam: *O laudo, **portanto**, é confiável.*"),

    h2("4. Pontuação na coordenação"),
    tb(["Situação", "Regra", "Exemplo"], [0.3, 0.3, 0.4], [
        ("Assindéticas", "Separadas por vírgula (ou ponto e vírgula)", "Chegou, viu, prendeu."),
        ("Adversativas, conclusivas, explicativas", "Vírgula antes da conjunção", "Confessou, mas negou o crime."),
        ("Aditiva com **e**, mesmo sujeito", "Sem vírgula", "Revistou o carro e encontrou a droga."),
        ("Aditiva com **e**, sujeitos diferentes", "Vírgula admitida (recomendada para clareza)", "A equipe chegou cedo, e o suspeito já havia fugido."),
        ("**E** repetido (polissíndeto)", "Vírgula antes de cada e", "E correu, e gritou, e caiu."),
        ("Conjunção deslocada", "Isolada por vírgulas; antes, ponto e vírgula ou ponto", "Analisaram as provas; o laudo, portanto, é confiável."),
    ]),
    trap("Vírgula e ponto e vírgula",
         "Quando a conjunção adversativa ou conclusiva **inicia** a oração, basta a vírgula antes dela (*…, mas…*; *…, portanto…*). "
         "Quando ela é **deslocada** para o meio da oração, a fronteira entre as orações precisa de **ponto e vírgula** ou **ponto**: "
         "*O réu confessou; o advogado, **porém**, recorreu.*"),

    h2("5. Como o Cebraspe cobra"),
    bl("**Sentido**: “a oração introduzida por X expressa conclusão / explicação / oposição”.",
       "**Substituição**: *mas* por *porém* (mantém); *portanto* por *porquanto* (altera: porquanto é explicativo/causal).",
       "**Deslocamento**: *porém* entre vírgulas no meio da oração mantém a correção e o sentido.",
       "**Pontuação**: vírgula antes de *e* com sujeitos diferentes; vírgula antes de *mas*.",
       "**Classificação**: assindética × sindética; explicativa × conclusiva pelo *pois*."),
]

QUIZ = quiz([
    ("C", "O período “O agente revistou o carro e encontrou a droga” é composto por coordenação, e a segunda oração é coordenada sindética aditiva.",
     "As orações são independentes e a segunda é introduzida pela conjunção aditiva e."),
    ("E", "Em “Chegou, viu, prendeu”, as orações são coordenadas sindéticas.",
     "Não há conjunção ligando as orações: são assindéticas."),
    ("C", "Em “O réu confessou, mas não indicou os comparsas”, a segunda oração é coordenada sindética adversativa.",
     "Mas introduz oposição em relação à primeira oração."),
    ("E", "Em “Ou você colabora, ou será indiciado”, as orações são coordenadas conclusivas.",
     "Ou… ou indica alternância: as orações são alternativas."),
    ("C", "Em “O laudo é conclusivo; logo, a autoria está provada”, a conjunção logo introduz oração coordenada conclusiva.",
     "Logo apresenta a conclusão do que foi afirmado antes."),
    ("E", "Em “Feche a porta, pois está ventando”, a oração introduzida por pois é coordenada conclusiva.",
     "Pois anteposto ao verbo, após imperativo, é explicativo: justifica a ordem."),
    ("C", "No período “Estudou muito e não foi aprovado”, a conjunção e estabelece relação de sentido adversativa entre as orações.",
     "O resultado contraria a expectativa criada pela primeira oração: e equivale a mas."),
    ("E", "No período “O suspeito, porém, negou tudo”, o deslocamento da conjunção para o início da oração (“Porém o suspeito negou tudo”) eliminaria a ideia de oposição.",
     "Porém mantém o valor adversativo em qualquer posição da oração."),
    ("C", "A conjunção mas não pode ser deslocada para o interior da oração que introduz, ao contrário de porém e contudo.",
     "Mas ocupa sempre o início da oração; porém, contudo, todavia e entretanto podem se deslocar."),
    ("E", "Em “Nem o delegado nem o escrivão compareceram”, as conjunções expressam alternância.",
     "Nem… nem soma negações: a relação é de adição."),

    ("C", "No período “A equipe chegou cedo, e o suspeito já havia fugido”, o emprego da vírgula antes de e justifica-se por terem as orações sujeitos diferentes.",
     "Com sujeitos diferentes, a vírgula antes de e é admitida e evita leitura equivocada."),
    ("E", "No período “O réu é primário, portanto terá direito ao benefício”, a substituição de portanto por porquanto manteria o sentido original.",
     "Porquanto tem valor explicativo/causal; portanto é conclusivo. A troca altera o sentido."),
    ("C", "Em “O depoimento foi longo; todavia, não trouxe novidades”, todavia poderia ser substituído por no entanto, sem prejuízo da correção e do sentido.",
     "Todavia e no entanto são adversativas."),
    ("E", "Em “Choveu, porque a rua está molhada”, a oração introduzida por porque expressa a causa da chuva.",
     "A oração justifica a afirmação (é evidência), não causa o fato: é explicativa."),
    ("C", "Em “Ora o suspeito confirmava a versão, ora a negava”, há orações coordenadas alternativas.",
     "Ora… ora indica alternância entre os fatos."),
    ("E", "Orações coordenadas assindéticas são aquelas que dependem sintaticamente de uma oração principal.",
     "Coordenadas são sintaticamente independentes; no período só com coordenação não há oração principal."),
    ("C", "No período “Os peritos analisaram as provas; o laudo, portanto, é confiável”, a conjunção portanto, deslocada para o interior da oração, está corretamente isolada por vírgulas.",
     "Conjunção conclusiva deslocada fica entre vírgulas, e o ponto e vírgula marca a fronteira entre as orações."),
    ("E", "Em “Não só prendeu os autores, como também recuperou a carga”, a relação estabelecida entre as orações é de oposição.",
     "Não só… como também é correlação aditiva."),
    ("C", "No período “O delegado ouviu as testemunhas, analisou as imagens e expediu o mandado”, há duas orações coordenadas assindéticas e uma coordenada sindética aditiva.",
     "As duas primeiras não têm conjunção; a última é introduzida por e."),
    ("E", "No período “Venha logo, que a reunião vai começar”, o vocábulo que é pronome relativo.",
     "Que, nesse caso, é conjunção explicativa: equivale a pois."),
], 20)

SOURCES = [GRAM, SRC_A]
