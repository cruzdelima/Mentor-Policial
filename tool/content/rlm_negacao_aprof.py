# -*- coding: utf-8 -*-
"""Raciocínio Lógico · Negação de proposições — MATERIAL APROFUNDADO."""
from common import *

MATERIAL = material(
    "rlm-negacao-02", "RLM", "RLM-04", "aprofundado", "Negação de proposições", "Raciocínio Lógico e Matemática · Lógica proposicional",
    "raciocinio_negacao_aprofundado", "RaciocinioLogico_Negacao_APROFUNDADO.pdf", None, ["Negação de", "proposições"],
    ["Como negar cada conectivo e as proposições com todo, algum e nenhum,", "com 20 questões no estilo Cebraspe."],
    [("01", "Negação simples", "o que muda e o que não muda"),
     ("02", "Conectivos", "e, ou, se... então, se e somente se"),
     ("03", "Quantificadores", "todo, algum, nenhum"),
     ("04", "Armadilhas", "contrário não é negação"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Negação de proposições — Raciocínio Lógico",
    "Base: lógica proposicional e de quantificadores.", 70)

THEORY = [
    exam("Como estudar este material",
         "A negação é cobrada em itens do tipo “a negação da proposição X é Y”. Para acertar, você precisa de duas coisas: as **regras de "
         "negação de cada conectivo** e saber que **negar não é dizer o contrário**. A negação é verdadeira exatamente quando a original é falsa."),

    h2("1. A ideia central"),
    key("Definição",
        "A negação de P (¬P) tem **sempre o valor oposto** ao de P. Por isso, a negação de uma proposição composta é a proposição que é "
        "verdadeira **exatamente nas linhas em que a original é falsa**."),
    tb(["Proposição", "Negação correta", "Errado (contrário)"], [0.34, 0.33, 0.33], [
        ("*O agente está armado.*", "*O agente não está armado.*", "—"),
        ("*A sala está cheia.*", "*A sala não está cheia.*", "*A sala está vazia.*"),
        ("*O preso é culpado.*", "*O preso não é culpado.*", "*O preso é inocente*: só equivale se o contexto não admitir outra opção"),
    ]),
    nt("“Vazia” é o **contrário** de “cheia”, mas existe meio-termo (a sala pode estar meio cheia). A negação só **nega**; não troca por um "
       "antônimo."),

    h2("2. Negação dos conectivos"),
    tb(["Proposição", "Negação", "Como lembrar"], [0.22, 0.34, 0.44], [
        ("P ∧ Q", "**¬P ∨ ¬Q**", "De Morgan: nega as duas e troca e por ou"),
        ("P ∨ Q", "**¬P ∧ ¬Q**", "De Morgan: nega as duas e troca ou por e"),
        ("P → Q", "**P ∧ ¬Q**", "**MA**ntém a primeira, **NE**ga a segunda e troca por **e** (MANÉ)"),
        ("P ↔ Q", "**P ⊻ Q** (ou exclusivo)", "Também: (P ∧ ¬Q) ∨ (¬P ∧ Q) · P ↔ ¬Q · ¬P ↔ Q"),
        ("P ⊻ Q", "**P ↔ Q**", "A negação do ou exclusivo é a bicondicional"),
        ("¬P", "P", "Dupla negação"),
    ]),
    key("A negação da condicional não é uma condicional",
        "*Se chover, a operação será adiada.* Negação: *Chove e a operação **não** será adiada.* O item que nega com “se... então” "
        "(como *Se não chover, a operação não será adiada*) está **errado**."),
    h3("Exemplos com frases"),
    tb(["Proposição", "Negação"], [0.5, 0.5], [
        ("*João é agente e Maria é perita.*", "*João não é agente ou Maria não é perita.*"),
        ("*O réu confessou ou há testemunhas.*", "*O réu não confessou e não há testemunhas.*"),
        ("*Se o laudo atrasar, o prazo será prorrogado.*", "*O laudo atrasou e o prazo não será prorrogado.*"),
        ("*Haverá operação se e somente se houver mandado.*", "*Ou haverá operação ou haverá mandado* (um sem o outro)."),
        ("*Nem o delegado nem o escrivão estavam presentes.*", "*O delegado ou o escrivão estava presente.*"),
    ]),

    h2("3. Negação com quantificadores"),
    tb(["Proposição", "Negação", "Não é negação (contrária)"], [0.3, 0.36, 0.34], [
        ("*Todo policial é concursado.*", "*Algum policial não é concursado.* (= existe policial que não é)", "*Nenhum policial é concursado.*"),
        ("*Algum policial é concursado.*", "*Nenhum policial é concursado.*", "*Algum policial não é concursado.*"),
        ("*Nenhum policial é concursado.*", "*Algum policial é concursado.*", "*Todo policial é concursado.*"),
        ("*Algum policial não é concursado.*", "*Todo policial é concursado.*", "—"),
    ]),
    key("Regra",
        "**Todo ↔ algum... não** e **algum ↔ nenhum**. Para negar “todo”, basta **um contraexemplo**; para negar “algum”, é preciso dizer "
        "que **nenhum**."),
    nt("“Pelo menos um”, “existe” e “há” equivalem a “algum”. “Não é verdade que todo...” = “algum... não”."),

    h2("4. Negações em sequência"),
    p("Quando a proposição mistura conectivos, negue o **conectivo principal** e depois aplique as regras às partes. Exemplo: negar "
      "*Se o investigado for servidor, ele será afastado e responderá a processo*: P → (Q ∧ R). Negação: P ∧ ¬(Q ∧ R) = P ∧ (¬Q ∨ ¬R): "
      "*O investigado é servidor e não será afastado ou não responderá a processo.*"),

    h2("5. Como o Cebraspe cobra"),
    bl("“A negação de *Se P, então Q* é *Se não P, então não Q*”: **errado**. A negação é *P e não Q*.",
       "“A negação de *Todo A é B* é *Nenhum A é B*”: **errado**. É *Algum A não é B*.",
       "“A negação de *P e Q* é *não P e não Q*”: **errado**. É *não P ou não Q*.",
       "Também cai a forma “é **equivalente** à negação de...”: primeiro negue, depois aplique uma equivalência."),
]

QUIZ = quiz([
    ("C", "A negação de P ∧ Q é ¬P ∨ ¬Q.",
     "Lei de De Morgan."),
    ("E", "A negação de P ∨ Q é ¬P ∨ ¬Q.",
     "É ¬P ∧ ¬Q: o conectivo precisa ser trocado."),
    ("C", "A negação de P → Q é P ∧ ¬Q.",
     "Mantém a primeira, nega a segunda e troca por “e”."),
    ("E", "A negação de P → Q é ¬P → ¬Q.",
     "A negação da condicional é uma conjunção: P ∧ ¬Q."),
    ("C", "A negação de P ↔ Q é equivalente a (P ∧ ¬Q) ∨ (¬P ∧ Q).",
     "É o ou exclusivo: verdadeiro quando os valores são diferentes."),
    ("E", "A negação de “Todo agente é concursado” é “Nenhum agente é concursado”.",
     "A negação é “Algum agente não é concursado”."),
    ("C", "A negação de “Algum perito é médico” é “Nenhum perito é médico”.",
     "Algum ↔ nenhum."),
    ("C", "A negação de “Nenhum suspeito foi liberado” é “Algum suspeito foi liberado”.",
     "Basta um ter sido liberado para a proposição original ser falsa."),
    ("E", "A negação de “A porta está aberta” é “A porta está fechada”.",
     "Fechada é o contrário. A negação é “A porta não está aberta”."),
    ("C", "A negação de ¬P ∧ Q é P ∨ ¬Q.",
     "¬(¬P ∧ Q) ⇔ ¬¬P ∨ ¬Q ⇔ P ∨ ¬Q."),

    ("C", "A negação da proposição “Se o servidor recebeu vantagem indevida, então cometeu ato de improbidade” é “O servidor recebeu vantagem indevida e não cometeu ato de improbidade”.",
     "¬(P → Q) ⇔ P ∧ ¬Q."),
    ("E", "A negação da proposição “O delegado assinou o relatório e o escrivão o juntou aos autos” é “O delegado não assinou o relatório e o escrivão não o juntou aos autos”.",
     "A negação é “O delegado não assinou o relatório ou o escrivão não o juntou aos autos”."),
    ("C", "A negação da proposição “O suspeito fugiu ou foi preso” é “O suspeito não fugiu e não foi preso”.",
     "¬(F ∨ P) ⇔ ¬F ∧ ¬P."),
    ("E", "A negação da proposição “Se houver flagrante, haverá prisão” é “Se não houver flagrante, não haverá prisão”.",
     "A negação é “Há flagrante e não há prisão”."),
    ("C", "A negação da proposição “Todos os candidatos foram aprovados no teste físico” é “Pelo menos um candidato não foi aprovado no teste físico”.",
     "Todo ↔ algum... não; “pelo menos um” = “algum”."),
    ("E", "A negação da proposição “Algum documento apreendido é falso” é “Algum documento apreendido não é falso”.",
     "A negação de “algum é” é “nenhum é”."),
    ("C", "A negação da proposição “O laudo será refeito se e somente se houver contestação” é “Ou o laudo será refeito ou haverá contestação”.",
     "A negação da bicondicional é o ou exclusivo."),
    ("C", "A negação de P → (Q ∧ R) é equivalente a P ∧ (¬Q ∨ ¬R).",
     "¬(P → (Q ∧ R)) ⇔ P ∧ ¬(Q ∧ R) ⇔ P ∧ (¬Q ∨ ¬R)."),
    ("E", "A negação da proposição “Nem Ana nem Bruno são agentes” é “Ana e Bruno são agentes”.",
     "¬(¬A ∧ ¬B) ⇔ A ∨ B: “Ana ou Bruno é agente”."),
    ("C", "A proposição “Não é verdade que todo crime é doloso” é equivalente a “Existe crime que não é doloso”.",
     "Negar “todo” é afirmar que há pelo menos um que não é."),
], 20)

SOURCES = [
    "Lógica proposicional e de quantificadores: regras de negação.",
    "Obras de referência: Alencar Filho, Iniciação à lógica matemática; Copi, Introdução à lógica.",
    SRC_A,
]
