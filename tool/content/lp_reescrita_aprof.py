# -*- coding: utf-8 -*-
"""Língua Portuguesa · Reescrita de frases e parágrafos — MATERIAL APROFUNDADO (estudo inicial)."""
from common import *

MATERIAL = material(
    "lp-reescrita-02", "LP", "LP-17", "aprofundado", "Reescrita de frases e parágrafos", "Língua Portuguesa · Texto",
    "portugues_reescrita_aprofundado", "Portugues_Reescrita_APROFUNDADO.pdf", None, ["Reescrita de frases", "e parágrafos"],
    ["Teoria completa para o primeiro estudo: o método para julgar reescritas, as transformações", "que mais caem e 20 questões no estilo Cebraspe."],
    [("01", "Método", "correção primeiro, sentido depois"),
     ("02", "Transformações", "vozes, discurso direto e indireto, nominalização"),
     ("03", "Conectivos e orações", "substituir, desenvolver e reduzir"),
     ("04", "Armadilhas", "o que parece igual e muda o sentido"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Reescrita de frases e parágrafos do texto (Língua Portuguesa)",
    "Base: gramáticas de referência (Bechara; Cunha e Cintra).", 240)

THEORY = [
    exam("Como estudar este material",
         "A reescrita é o formato preferido do Cebraspe: “a reescrita a seguir mantém a correção gramatical e o sentido original do texto”. "
         "Ela junta **toda** a gramática (concordância, regência, crase, pontuação, colocação) com **interpretação**. "
         "Este material dá o método e as transformações mais frequentes; os outros tópicos de gramática dão o conteúdo."),

    h2("1. O método: duas perguntas, nesta ordem"),
    tb(["Pergunta", "O que conferir"], [0.3, 0.7], [
        ("1. A reescrita está **correta**?", "Concordância (verbal e nominal), regência, crase, pontuação, colocação pronominal, tempos e modos verbais, grafia"),
        ("2. O **sentido** foi mantido?", "Conectivos (mesma relação lógica?), tempos verbais, voz, palavras de foco (*só, até, ainda*), vírgulas de orações adjetivas, determinantes, ordem dos termos"),
    ]),
    p("Basta **um** problema em qualquer das duas para o item ser **errado**. Quando a banca pergunta só por uma delas (“mantém a correção”), "
      "julgue só aquela."),
    key("Leia o original e a reescrita lado a lado",
        "Marque cada diferença entre as duas versões e teste uma por uma. A maioria dos erros está numa única palavra trocada: "
        "um tempo verbal, uma vírgula, uma preposição."),

    h2("2. Transformações que mais caem"),
    h3("Voz ativa › voz passiva"),
    bl("O objeto direto vira sujeito; o sujeito vira agente da passiva; o verbo *ser* fica **no tempo da ativa**; o particípio concorda.",
       "*Os peritos **analisarão** as provas* › *As provas **serão analisadas** pelos peritos.* (e não *foram analisadas*)",
       "Passiva sintética › analítica: *Investigou-se a denúncia* › *A denúncia **foi investigada**.*",
       "Só verbos transitivos diretos vão para a passiva: *Precisa-se de agentes* **não** vira “agentes são precisados”."),
    h3("Discurso direto › indireto"),
    tb(["Discurso direto", "Discurso indireto"], [0.5, 0.5], [
        ("Presente: *“Estou cansado”*", "Imperfeito: disse que **estava** cansado"),
        ("Pretérito perfeito: *“Vi o réu”*", "Mais-que-perfeito: disse que **tinha visto** o réu"),
        ("Futuro do presente: *“Abrirei o inquérito”*", "Futuro do pretérito: disse que **abriria** o inquérito"),
        ("Imperativo: *“Saia!”*", "Subjuntivo: mandou que **saísse**"),
        ("1ª pessoa: *eu, meu*", "3ª pessoa: *ele, seu/dele*"),
        ("*aqui, este, hoje, ontem, amanhã*", "*ali/lá, aquele, naquele dia, no dia anterior, no dia seguinte*"),
    ]),
    p("*O delegado disse: — Vou abrir o inquérito* › *O delegado disse que **ia** abrir o inquérito.*"),
    h3("Nominalização"),
    p("Transformar um verbo em substantivo mantém o sentido: *O delegado **decidiu** arquivar* › *A **decisão** do delegado foi arquivar.* "
      "*Quando terminou a audiência* › *Com o **término** da audiência*."),
    h3("Desenvolvimento e redução de orações"),
    bl("*Ao chegar* = *quando chegou* · *Terminada a audiência* = *assim que terminou a audiência* · *Sendo primário* = *como é primário*.",
       "*O laudo, **que foi elaborado** ontem,* = *O laudo, **elaborado** ontem,*",
       "*É necessário **revisar** os procedimentos* = *É necessário **que se revisem** os procedimentos* (atenção à concordância do *se*)."),
    h3("Substituição de conectivos"),
    bl("Mesmo grupo: mantém (*mas › porém*; *portanto › por isso*; *embora › ainda que*).",
       "Grupo diferente: altera (*porém › portanto*; *à medida que › na medida em que*).",
       "Mudança de construção que preserva a relação lógica: *Como chovia, a operação foi adiada* › *Chovia; **por isso**, a operação foi adiada* (causa e consequência mantidas).",
       "Concessivas pedem subjuntivo: *Embora **estivesse** ferido* › *Apesar de **estar** ferido* (preposição + infinitivo)."),
    h3("Deslocamento de termos"),
    bl("Adjunto adverbial pode mudar de lugar, com vírgulas: *A equipe cumpriu o mandado ontem* › *Ontem, a equipe cumpriu o mandado.*",
       "Conjunções como *porém, contudo, portanto* podem ir para o meio da oração, entre vírgulas, com ponto e vírgula antes.",
       "Colocação pronominal: confira a palavra atrativa depois do deslocamento (*Disse-me* › *Não me disse*)."),

    h2("3. Armadilhas: parece igual, mas muda"),
    tb(["Original", "Reescrita", "Problema"], [0.33, 0.33, 0.34], [
        ("Os agentes, que estavam armados, entraram.", "Os agentes que estavam armados entraram.", "Explicativa vira restritiva: muda o sentido"),
        ("**Só** o juiz pode decretar.", "O juiz pode **só** decretar.", "Foco muda: sentido alterado"),
        ("Os peritos **analisarão** as provas.", "As provas **foram** analisadas.", "Tempo verbal alterado"),
        ("O suspeito **teria** fugido.", "O suspeito fugiu.", "Hipótese vira fato"),
        ("O agente chegou **antes do** perito.", "O perito chegou **antes do** agente.", "Inversão de papéis"),
        ("Disse-me que viria.", "Me disse que viria.", "Início com pronome átono: erro"),
        ("Se o réu **colaborar**…", "Caso o réu **colabora**…", "*Caso* exige subjuntivo"),
        ("É necessário que se **apurem** os fatos.", "É necessário que se **apure** os fatos.", "Passiva sintética: concordância"),
    ]),

    h2("4. Como o Cebraspe cobra"),
    bl("“A reescrita mantém a correção gramatical e o sentido original” — faça as duas perguntas.",
       "“A seguinte proposta de reescrita prejudicaria a coerência do texto.”",
       "“O trecho poderia ser reescrito da seguinte forma, sem alteração de sentido.”",
       "Paráfrases com troca de conectivo, voz verbal, discurso ou nominalização."),
]

QUIZ = quiz([
    ("C", "A reescrita de “A polícia prendeu o suspeito” como “O suspeito foi preso pela polícia” mantém a correção gramatical e o sentido original.",
     "Transposição correta para a voz passiva, com o verbo ser no pretérito perfeito."),
    ("E", "A reescrita de “Os peritos analisarão as provas” como “As provas foram analisadas pelos peritos” mantém o sentido original.",
     "O tempo mudou: o correto seria serão analisadas."),
    ("C", "A reescrita de “O delegado disse: — Vou abrir o inquérito” em discurso indireto pode ser “O delegado disse que ia abrir o inquérito”.",
     "O presente (vou) passa ao imperfeito (ia), e a 1ª pessoa passa à 3ª."),
    ("E", "A transposição de “A testemunha afirmou: — Vi o réu aqui ontem” para “A testemunha afirmou que viu o réu aqui ontem” respeita as adaptações do discurso indireto.",
     "No indireto: que tinha visto o réu ali no dia anterior."),
    ("C", "A reescrita de “Embora estivesse ferido, o agente continuou” como “Apesar de estar ferido, o agente continuou” mantém a correção e o sentido.",
     "Embora + subjuntivo equivale a apesar de + infinitivo: ambos concessivos."),
    ("E", "A reescrita de “Como chovia, a operação foi adiada” como “Chovia; por isso, a operação foi adiada” altera a relação lógica entre as orações.",
     "A relação de causa e consequência é mantida; muda apenas a construção."),
    ("C", "A reescrita de “O delegado decidiu arquivar o caso” como “A decisão do delegado foi arquivar o caso” mantém o sentido original.",
     "A nominalização preserva o conteúdo."),
    ("E", "A reescrita de “Os agentes, que estavam armados, entraram” como “Os agentes que estavam armados entraram” mantém o sentido original.",
     "Sem vírgulas, a oração passa a restritiva: apenas parte dos agentes estaria armada."),
    ("C", "A substituição de Só por Apenas em “Só o juiz pode decretar a prisão” mantém o sentido original.",
     "As duas palavras têm o mesmo valor de exclusão na mesma posição."),
    ("E", "A reescrita de “Só o juiz pode decretar a prisão” como “O juiz pode só decretar a prisão” mantém o sentido original.",
     "O foco muda: na reescrita, o juiz não pode fazer outra coisa além de decretar."),

    ("C", "A reescrita de “Quando terminou a audiência, o réu foi levado ao presídio” como “Terminada a audiência, o réu foi levado ao presídio” mantém a correção e o sentido.",
     "A oração reduzida de particípio tem o mesmo valor temporal."),
    ("E", "A reescrita de “É necessário que se apurem os fatos” como “É necessário que se apure os fatos” mantém a correção gramatical.",
     "Na passiva sintética, o verbo concorda com o sujeito os fatos: apurem."),
    ("C", "A reescrita de “Investigou-se a denúncia” como “A denúncia foi investigada” mantém a correção e o sentido.",
     "Passiva sintética transformada em analítica, no mesmo tempo."),
    ("E", "A reescrita de “Precisa-se de agentes” como “Agentes são precisados” mantém a correção gramatical.",
     "Precisar de é transitivo indireto e não admite voz passiva."),
    ("C", "A reescrita de “O laudo, que foi elaborado ontem, confirmou a fraude” como “O laudo, elaborado ontem, confirmou a fraude” mantém a correção e o sentido.",
     "A oração adjetiva foi reduzida ao particípio, mantidas as vírgulas."),
    ("E", "A reescrita de “Se o réu colaborar, terá o benefício” como “Caso o réu colabora, terá o benefício” mantém a correção gramatical.",
     "Caso exige subjuntivo: caso o réu colabore."),
    ("C", "A reescrita de “Os moradores denunciaram o tráfico, mas a polícia não agiu” como “Os moradores denunciaram o tráfico; a polícia, porém, não agiu” mantém a correção e o sentido.",
     "Porém deslocado, entre vírgulas, com ponto e vírgula antes, mantém a oposição."),
    ("E", "A reescrita de “Disse-me que viria” como “Me disse que viria” mantém a correção gramatical segundo a norma-padrão.",
     "No padrão formal, não se inicia período com pronome oblíquo átono."),
    ("C", "A reescrita de “Não se sabe quem cometeu o crime” como “Desconhece-se o autor do crime” mantém o sentido original.",
     "Quem cometeu o crime equivale a o autor do crime; não se sabe equivale a desconhece-se."),
    ("E", "A reescrita de “O agente chegou ao local antes do perito” como “O perito chegou ao local antes do agente” mantém o sentido original.",
     "A ordem de chegada foi invertida."),
], 20)

SOURCES = [GRAM, SRC_A]
