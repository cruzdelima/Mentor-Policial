# -*- coding: utf-8 -*-
"""Raciocínio Lógico · Proposições e conectivos lógicos — MATERIAL APROFUNDADO."""
from common import *

MATERIAL = material(
    "rlm-proposicoes-02", "RLM", "RLM-01", "aprofundado", "Proposições e conectivos lógicos", "Raciocínio Lógico e Matemática · Lógica proposicional",
    "raciocinio_proposicoes_aprofundado", "RaciocinioLogico_Proposicoes_APROFUNDADO.pdf", None, ["Proposições e", "conectivos"],
    ["O que é e o que não é proposição, proposições simples e compostas, os cinco conectivos", "e a tradução da linguagem natural, com 20 questões no estilo Cebraspe."],
    [("01", "Proposição", "sentença declarativa com valor lógico"),
     ("02", "Simples e compostas", "quantas proposições há na frase"),
     ("03", "Conectivos", "não, e, ou, ou...ou, se...então, se e somente se"),
     ("04", "Tradução", "da frase para os símbolos e de volta"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Proposições e conectivos lógicos — Raciocínio Lógico",
    "Base: lógica proposicional clássica (princípios da identidade, da não contradição e do terceiro excluído).", 80)

THEORY = [
    exam("Como estudar este material",
         "Este é o assunto que abre a lógica e cai em quase toda prova policial do Cebraspe. A banca cobra três coisas: **reconhecer se uma "
         "frase é proposição**, **contar quantas proposições simples há** numa frase e **traduzir** frases para a forma simbólica (e o "
         "contrário). Faça os exemplos com lápis: a lógica se aprende escrevendo."),

    h2("1. O que é proposição"),
    key("Definição",
        "**Proposição** é toda **sentença declarativa** que pode ser julgada como **verdadeira (V)** ou **falsa (F)**, mas **não as duas "
        "coisas ao mesmo tempo**. O V ou o F é o **valor lógico** da proposição."),
    p("Para ser proposição, a frase precisa ter **sujeito e predicado** (uma oração com verbo) e **afirmar algo** que possa ser verdadeiro ou "
      "falso. Não importa se sabemos ou não o valor: *Existe vida em outro planeta* é proposição, ainda que ninguém saiba o valor."),
    tb(["Tipo de frase", "Exemplo", "É proposição?"], [0.28, 0.46, 0.26], [
        ("Declarativa (afirmativa ou negativa)", "*Brasília é a capital do Brasil.* · *O réu não confessou.*", "**Sim**"),
        ("Interrogativa", "*Quem assinou o boletim?*", "Não"),
        ("Exclamativa", "*Que operação bem-sucedida!*", "Não"),
        ("Imperativa (ordem, pedido)", "*Apresente os documentos.*", "Não"),
        ("Optativa (desejo)", "*Tomara que chova.*", "Não"),
        ("Sem verbo", "*Bom dia.* · *Excelente trabalho.*", "Não"),
        ("Sentença aberta (com variável)", "*x + 3 = 10.* · *Ele é policial.*", "Não: o valor depende de quem é x ou ele"),
        ("Paradoxo", "*Esta frase é falsa.*", "Não: não pode receber V nem F"),
    ]),
    trap("Pegadinhas clássicas",
         "**Sentença aberta** não é proposição: em *x > 5* ou *Ele foi aprovado*, o valor depende da variável (x, ele). Se a variável for "
         "**quantificada** (*Existe x tal que x > 5*) ou substituída (*7 > 5*), vira proposição. A frase **negativa** é proposição normalmente. "
         "Uma frase **falsa** também é proposição: o que importa é poder receber um valor lógico."),
    h3("Os três princípios"),
    bl("**Identidade**: uma proposição verdadeira é verdadeira; uma falsa é falsa.",
       "**Não contradição**: nenhuma proposição é verdadeira e falsa ao mesmo tempo.",
       "**Terceiro excluído**: toda proposição é verdadeira ou falsa; não existe terceira opção."),

    h2("2. Proposições simples e compostas"),
    p("A **proposição simples** traz uma única afirmação. A **composta** junta duas ou mais simples por meio de **conectivos**. Usamos letras "
      "maiúsculas (P, Q, R...) para as simples."),
    tb(["Frase", "Proposições simples", "Classificação"], [0.46, 0.34, 0.2], [
        ("*O agente prendeu o suspeito.*", "1", "Simples"),
        ("*O agente prendeu o suspeito e apreendeu a droga.*", "2 (prendeu; apreendeu)", "Composta"),
        ("*Se chover, a operação será adiada.*", "2 (chover; ser adiada)", "Composta"),
        ("*João e Maria são escrivães.*", "2 (João é escrivão; Maria é escrivã)", "Composta"),
        ("*João e Maria são casados um com o outro.*", "1 (relação entre os dois)", "Simples"),
    ]),
    nt("Cuidado com o “e” que **não separa** afirmações: em *Pedro e Ana são irmãos* (um do outro) ou *Recife fica entre Olinda e Jaboatão*, "
       "há uma única proposição. Pergunte: dá para separar em duas frases independentes sem mudar o sentido?"),

    h2("3. Os conectivos"),
    tb(["Conectivo", "Símbolo", "Leitura", "Nome"], [0.2, 0.14, 0.38, 0.28], [
        ("não", "¬P ou ~P", "não P; não é verdade que P", "Negação"),
        ("e", "P ∧ Q", "P e Q", "Conjunção"),
        ("ou", "P ∨ Q", "P ou Q", "Disjunção (inclusiva)"),
        ("ou... ou", "P ⊻ Q", "ou P ou Q (mas não ambos)", "Disjunção exclusiva"),
        ("se... então", "P → Q", "se P, então Q", "Condicional"),
        ("se e somente se", "P ↔ Q", "P se e somente se Q", "Bicondicional"),
    ]),
    h3("Quando cada composta é verdadeira"),
    tb(["Conectivo", "Regra de ouro"], [0.26, 0.74], [
        ("Conjunção (∧)", "Só é **V** se **as duas** forem V. Basta uma F para ser F."),
        ("Disjunção (∨)", "Só é **F** se **as duas** forem F. Basta uma V para ser V."),
        ("Disjunção exclusiva (⊻)", "É **V** quando os valores são **diferentes**; F quando são iguais."),
        ("Condicional (→)", "Só é **F** em **V → F** (antecedente V e consequente F). Em todos os outros casos é V."),
        ("Bicondicional (↔)", "É **V** quando os valores são **iguais**; F quando são diferentes."),
    ]),
    key("A condicional em uma frase",
        "**Vera Fischer é falsa**: o único caso em que P → Q é falsa é **V**era → **F**ischer, isto é, antecedente verdadeiro e consequente "
        "falso. Se o antecedente for falso, a condicional é verdadeira, qualquer que seja o consequente."),
    p("Na condicional P → Q, **P** é o **antecedente** (condição suficiente) e **Q** é o **consequente** (condição necessária). A promessa "
      "*Se você passar, eu pago o jantar* só é quebrada se você passar e eu não pagar."),

    h2("4. Formas equivalentes de escrever cada conectivo"),
    tb(["Conectivo", "Outras redações que a banca usa"], [0.24, 0.76], [
        ("Conjunção", "*mas*, *porém*, *contudo*, *embora*, *nem... nem* (= não P e não Q), vírgula entre ações: *Prendeu, autuou e liberou.*"),
        ("Condicional P → Q", "*Quando P, Q.* · *P implica Q.* · *Q, se P.* · *P é condição suficiente para Q.* · *Q é condição necessária para P.* "
                              "· *Todo P é Q.* · *P somente se Q.*"),
        ("Bicondicional", "*P se e só se Q.* · *P é condição necessária e suficiente para Q.*"),
        ("Disjunção exclusiva", "*Ou P ou Q.* · *P ou Q, mas não ambos.*"),
    ]),
    trap("Atenção à ordem na condicional",
         "*Q, se P* continua sendo **P → Q** (a condição é P). Já *P somente se Q* também é **P → Q**: o “somente se” aponta para o "
         "**consequente**. E *Q é necessária para P* = P → Q. A ordem em que as palavras aparecem na frase não é a ordem lógica."),

    h2("5. Ordem de precedência e parênteses"),
    p("Sem parênteses, resolve-se primeiro a **negação**, depois a **conjunção**, a **disjunção**, a **condicional** e, por último, a "
      "**bicondicional**. Na prova, a banca quase sempre coloca os parênteses; quando traduzir uma frase, use vírgulas e o sentido para "
      "agrupar."),
    tb(["Frase", "Forma simbólica"], [0.6, 0.4], [
        ("*Se chover e ventar, a operação será adiada.*", "(C ∧ V) → A"),
        ("*Chove, e, se ventar, a operação será adiada.*", "C ∧ (V → A)"),
        ("*Não é verdade que João é delegado e Maria é perita.*", "¬(J ∧ M)"),
        ("*João não é delegado e Maria é perita.*", "¬J ∧ M"),
    ]),

    h2("6. Como o Cebraspe cobra"),
    bl("**É proposição?** Itens trazem uma frase e afirmam que é (ou não) proposição. Pergunta, ordem, exclamação, desejo e sentença aberta "
       "não são.",
       "**Quantas proposições simples?** Conte as afirmações independentes. Ex.: *Se o servidor faltar e não justificar, será punido* tem "
       "**3** (faltar; justificar; ser punido).",
       "**Forma simbólica**: o item diz que a frase pode ser representada por P ∧ Q → R ou similar; confira os parênteses.",
       "**Valor lógico**: dados os valores de P e Q, o item afirma o valor da composta. Use a regra de ouro de cada conectivo.",
       "**Linhas da tabela-verdade**: com n proposições simples, a tabela tem **2ⁿ linhas** (assunto do próximo material)."),
]

QUIZ = quiz([
    ("C", "A sentença “O inquérito foi concluído no prazo legal” é uma proposição.",
     "É declarativa e pode ser julgada como verdadeira ou falsa."),
    ("E", "A sentença “Encaminhe o relatório ao delegado ainda hoje” é uma proposição.",
     "É imperativa (ordem): não pode ser julgada como verdadeira ou falsa."),
    ("E", "A sentença “x + 4 = 9” é uma proposição, pois tem sujeito, verbo e predicado.",
     "É sentença aberta: o valor depende de x. Não é proposição."),
    ("C", "A sentença “O suspeito não estava no local do crime” é uma proposição, ainda que seja negativa.",
     "Frases negativas declarativas são proposições."),
    ("C", "Se P é verdadeira e Q é falsa, então P ∧ Q é falsa.",
     "A conjunção só é verdadeira quando as duas componentes são verdadeiras."),
    ("C", "Se P é falsa e Q é verdadeira, então P ∨ Q é verdadeira.",
     "Basta uma componente verdadeira para a disjunção ser verdadeira."),
    ("E", "Se P é falsa e Q é falsa, então P → Q é falsa.",
     "Com antecedente falso, a condicional é verdadeira."),
    ("C", "Se P é verdadeira e Q é falsa, então P → Q é falsa.",
     "É o único caso de condicional falsa: V → F."),
    ("C", "Se P e Q são ambas falsas, a bicondicional P ↔ Q é verdadeira.",
     "A bicondicional é verdadeira quando as componentes têm o mesmo valor."),
    ("E", "A disjunção exclusiva “ou P ou Q” é verdadeira quando P e Q são ambas verdadeiras.",
     "Na exclusiva, as duas não podem ser verdadeiras juntas: valores iguais dão F."),

    ("C", "A proposição “Se o servidor faltar ao serviço e não apresentar justificativa, ele será punido” é composta por três proposições simples.",
     "As simples são: o servidor falta; o servidor apresenta justificativa; o servidor é punido."),
    ("E", "A sentença “Que belo trabalho de investigação!” pode ser julgada como verdadeira ou falsa e, portanto, é uma proposição.",
     "É exclamativa: não é proposição."),
    ("C", "A proposição “Pedro é escrivão ou Paulo é agente” é verdadeira se Pedro for escrivão, independentemente da profissão de Paulo.",
     "Na disjunção, basta uma componente verdadeira."),
    ("E", "Considerando-se P: “o laudo ficou pronto” e Q: “o inquérito foi relatado”, a proposição “o inquérito foi relatado somente se o laudo ficou pronto” é corretamente representada por P → Q.",
     "“Q somente se P” é Q → P: o “somente se” aponta para o consequente."),
    ("C", "A proposição “Ser aprovado no concurso é condição suficiente para tomar posse” pode ser escrita como “Se for aprovado no concurso, tomará posse”.",
     "A condição suficiente é o antecedente da condicional."),
    ("E", "A proposição “Ser maior de 18 anos é condição necessária para ser policial” equivale a “Se for maior de 18 anos, então será policial”.",
     "A condição necessária é o consequente: “se for policial, então é maior de 18 anos”."),
    ("C", "A sentença “Ele é o responsável pelo vazamento das informações” não é proposição, pois o pronome “ele” não está identificado.",
     "É sentença aberta: o valor depende de quem é “ele”."),
    ("C", "Se a proposição P → Q é falsa, então P é verdadeira e Q é falsa.",
     "A condicional só é falsa no caso V → F."),
    ("E", "A proposição “Não é verdade que o agente e o escrivão viajaram” é corretamente representada por ¬A ∧ ¬E, em que A: “o agente viajou” e E: “o escrivão viajou”.",
     "A negação atinge a conjunção inteira: ¬(A ∧ E). Por De Morgan, equivale a ¬A ∨ ¬E, não a ¬A ∧ ¬E."),
    ("C", "Se P é verdadeira, a proposição P ∨ Q é verdadeira, qualquer que seja o valor lógico de Q.",
     "Uma componente verdadeira basta para a disjunção."),
], 20)

SOURCES = [
    "Lógica proposicional clássica: conectivos, valores lógicos e princípios fundamentais.",
    "Obras de referência: Alencar Filho, Iniciação à lógica matemática; Copi, Introdução à lógica.",
    SRC_A,
]
