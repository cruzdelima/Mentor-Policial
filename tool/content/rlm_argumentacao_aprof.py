# -*- coding: utf-8 -*-
"""Raciocínio Lógico · Lógica de argumentação — MATERIAL APROFUNDADO."""
from common import *

MATERIAL = material(
    "rlm-argumentacao-02", "RLM", "RLM-05", "aprofundado", "Lógica de argumentação", "Raciocínio Lógico e Matemática · Lógica proposicional",
    "raciocinio_argumentacao_aprofundado", "RaciocinioLogico_Argumentacao_APROFUNDADO.pdf", None, ["Lógica de", "argumentação"],
    ["Argumento válido e inválido, regras de inferência, falácias e o método para julgar", "conclusões, com 20 questões no estilo Cebraspe."],
    [("01", "Argumento", "premissas, conclusão e validade"),
     ("02", "Regras de inferência", "modus ponens, modus tollens, silogismos"),
     ("03", "Falácias", "afirmar o consequente e negar o antecedente"),
     ("04", "Método", "premissas verdadeiras e caso falso"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Lógica de argumentação — Raciocínio Lógico",
    "Base: lógica proposicional clássica.", 80)

THEORY = [
    exam("Como estudar este material",
         "O Cebraspe apresenta um texto com algumas afirmações (as **premissas**) e pergunta se uma conclusão “**decorre**” delas ou se o "
         "argumento é **válido**. Você vai usar duas técnicas: **considerar as premissas verdadeiras** e descobrir o valor de cada letra, ou "
         "**tentar tornar o argumento inválido** (premissas V e conclusão F)."),

    h2("1. Argumento e validade"),
    key("Definições",
        "**Argumento** é um conjunto de proposições (**premissas**) das quais se pretende tirar outra (**conclusão**). É **válido** quando é "
        "**impossível** ter **todas as premissas verdadeiras e a conclusão falsa**. Formalmente: (premissa 1 ∧ premissa 2 ∧ ... ∧ premissa n) → conclusão é uma **tautologia**."),
    bl("**Validade** diz respeito à **forma**, não ao conteúdo. Um argumento pode ser válido com premissas falsas: *Todo peixe voa; o "
       "tubarão é peixe; logo, o tubarão voa* é **válido** (a conclusão decorre das premissas), embora falso.",
       "Argumento válido com **premissas verdadeiras** é chamado **sólido** (ou correto): sua conclusão é necessariamente verdadeira.",
       "Argumento **inválido** (falácia): existe ao menos uma situação com premissas V e conclusão F."),

    h2("2. Regras de inferência (formas válidas)"),
    tb(["Nome", "Premissas", "Conclusão", "Exemplo"], [0.2, 0.22, 0.14, 0.44], [
        ("**Modus ponens**", "P → Q; P", "Q", "*Se houve flagrante, houve prisão. Houve flagrante. Logo, houve prisão.*"),
        ("**Modus tollens**", "P → Q; ¬Q", "¬P", "*Se houve flagrante, houve prisão. Não houve prisão. Logo, não houve flagrante.*"),
        ("**Silogismo hipotético**", "P → Q; Q → R", "P → R", "*Se estudar, passa. Se passar, toma posse. Logo, se estudar, toma posse.*"),
        ("**Silogismo disjuntivo**", "P ∨ Q; ¬P", "Q", "*O autor é João ou Pedro. Não é João. Logo, é Pedro.*"),
        ("**Simplificação**", "P ∧ Q", "P", "*Choveu e ventou. Logo, choveu.*"),
        ("**Adição**", "P", "P ∨ Q", "*Choveu. Logo, choveu ou ventou.*"),
        ("**Dilema construtivo**", "P → Q; R → S; P ∨ R", "Q ∨ S", "*Se for de dia, usa o carro; se for de noite, usa a moto; é dia ou noite; logo, usa o carro ou a moto.*"),
    ]),

    h2("3. Falácias formais (formas inválidas)"),
    tb(["Nome", "Forma", "Por que falha"], [0.26, 0.3, 0.44], [
        ("**Afirmação do consequente**", "P → Q; Q; logo P", "Q pode ser verdadeira por outro motivo. *Se chover, a rua molha. A rua está molhada. Logo, choveu.* (pode ter sido um caminhão-pipa)"),
        ("**Negação do antecedente**", "P → Q; ¬P; logo ¬Q", "*Se chover, a rua molha. Não choveu. Logo, a rua não está molhada.* (idem)"),
        ("Disjunção inclusiva tomada como exclusiva", "P ∨ Q; P; logo ¬Q", "No “ou” inclusivo, as duas podem ser verdadeiras."),
    ]),
    trap("A pegadinha clássica",
         "*Se o investigado é culpado, ele mentiu. Ele mentiu. Logo, é culpado.* Parece convincente, mas é **afirmação do consequente**: "
         "o argumento é **inválido**."),

    h2("4. Método 1: considerar as premissas verdadeiras"),
    p("Quando o item pergunta o que **se pode concluir**, assuma que **todas as premissas são verdadeiras** e comece pela mais “fechada”: "
      "uma **proposição simples** ou uma **conjunção** (que obriga as duas partes a serem V). Depois, propague os valores pelas condicionais "
      "e disjunções."),
    h3("Exemplo"),
    bl("P1: *Se Ana é a autora, Bruno é cúmplice.* (A → B)",
       "P2: *Se Bruno é cúmplice, Caio não depôs.* (B → ¬C)",
       "P3: *Caio depôs.* (C)",
       "De P3, C = V. Em P2, ¬C = F; para P2 ser V, B tem de ser **F**. Em P1, B = F; para P1 ser V, A tem de ser **F**.",
       "Conclusões válidas: *Bruno não é cúmplice* e *Ana não é a autora*."),

    h2("5. Método 2: tentar tornar o argumento inválido"),
    p("Para testar se um argumento é válido, suponha a **conclusão falsa** e tente deixar **todas as premissas verdadeiras**. Se conseguir, "
      "o argumento é **inválido**; se der contradição, é **válido**."),
    h3("Exemplo"),
    bl("Premissas: P → Q e Q. Conclusão: P.",
       "Conclusão falsa: P = F. Premissa Q verdadeira: Q = V. Premissa P → Q: F → V = **V**.",
       "Conseguimos premissas V e conclusão F: o argumento é **inválido** (afirmação do consequente)."),

    h2("6. Problemas de verdade e mentira"),
    p("Em problemas com pessoas que **sempre mentem** ou **sempre dizem a verdade**, **suponha** que uma delas diz a verdade e verifique se "
      "surge contradição. Se surgir, a suposição está errada. Comece pelas falas que **se contradizem**: entre duas afirmações contraditórias, "
      "**exatamente uma** é verdadeira."),

    h2("7. Como o Cebraspe cobra"),
    bl("“A partir das premissas, é correto concluir que...”: use o método 1.",
       "“O argumento é válido”: use o método 2.",
       "Itens que concluem pela **recíproca** (afirmação do consequente) ou pela **inversa** (negação do antecedente): **errados**.",
       "Validade não depende de a conclusão ser verdadeira no mundo real.",
       "Na dúvida real, **deixe em branco**: no Cebraspe, cada erro anula um acerto."),
]

QUIZ = quiz([
    ("C", "O argumento formado pelas premissas P → Q e P e pela conclusão Q é válido.",
     "É o modus ponens."),
    ("C", "O argumento formado pelas premissas P → Q e ¬Q e pela conclusão ¬P é válido.",
     "É o modus tollens."),
    ("E", "O argumento formado pelas premissas P → Q e Q e pela conclusão P é válido.",
     "Afirmação do consequente: com P = F e Q = V, premissas V e conclusão F."),
    ("E", "O argumento formado pelas premissas P → Q e ¬P e pela conclusão ¬Q é válido.",
     "Negação do antecedente: com P = F e Q = V, premissas V e conclusão F."),
    ("C", "O argumento formado pelas premissas P ∨ Q e ¬P e pela conclusão Q é válido.",
     "Silogismo disjuntivo."),
    ("C", "O argumento formado pelas premissas P → Q e Q → R e pela conclusão P → R é válido.",
     "Silogismo hipotético."),
    ("E", "Um argumento válido tem, necessariamente, conclusão verdadeira.",
     "Só se as premissas forem verdadeiras. Validade é questão de forma."),
    ("C", "Um argumento é inválido quando é possível que todas as premissas sejam verdadeiras e a conclusão seja falsa.",
     "É a definição de argumento inválido."),
    ("E", "O argumento formado pelas premissas P ∨ Q e P e pela conclusão ¬Q é válido.",
     "No “ou” inclusivo, P e Q podem ser ambas verdadeiras."),
    ("C", "O argumento formado pela premissa P ∧ Q e pela conclusão Q é válido.",
     "Simplificação: se a conjunção é V, cada parte é V."),

    ("C", "Considere as premissas: “Se o veículo foi clonado, a placa não confere com o chassi” e “A placa confere com o chassi”. Delas se conclui corretamente que o veículo não foi clonado.",
     "Modus tollens: C → ¬P e P; logo ¬C."),
    ("E", "Considere as premissas: “Se o suspeito é o autor do furto, suas digitais estão no cofre” e “As digitais do suspeito estão no cofre”. Delas se conclui corretamente que o suspeito é o autor do furto.",
     "Afirmação do consequente: as digitais podem estar no cofre por outro motivo."),
    ("C", "Considere as premissas: “O autor do disparo foi Carlos ou Davi” e “Davi não efetuou o disparo”. Delas se conclui corretamente que Carlos foi o autor do disparo.",
     "Silogismo disjuntivo."),
    ("E", "Considere as premissas: “Se a denúncia for anônima, será feita uma verificação preliminar” e “A denúncia não foi anônima”. Delas se conclui corretamente que não será feita verificação preliminar.",
     "Negação do antecedente: a verificação pode ocorrer por outro motivo."),
    ("C", "Considere as premissas: “Se Paulo é agente, então Rita é escrivã”, “Se Rita é escrivã, então Sônia é perita” e “Sônia não é perita”. Então, Paulo não é agente.",
     "Sônia não é perita → Rita não é escrivã (modus tollens) → Paulo não é agente."),
    ("C", "Considere as premissas: “Se Paulo é agente, então Rita é escrivã”, “Se Rita é escrivã, então Sônia é perita” e “Sônia não é perita”. Então, Rita não é escrivã.",
     "Da segunda premissa, por modus tollens."),
    ("E", "Considere as premissas: “Ou o laudo foi entregue ou o prazo foi prorrogado” (disjunção inclusiva) e “O laudo foi entregue”. Delas se conclui corretamente que o prazo não foi prorrogado.",
     "Na disjunção inclusiva, as duas partes podem ser verdadeiras."),
    ("C", "O argumento “Todo agente é concursado; Marcos é agente; logo, Marcos é concursado” é válido.",
     "A conclusão decorre necessariamente das premissas."),
    ("C", "O argumento “Todo número primo é ímpar; 2 é primo; logo, 2 é ímpar” é válido, embora sua conclusão seja falsa.",
     "A forma é válida; a conclusão é falsa porque a primeira premissa é falsa."),
    ("E", "Três suspeitos depuseram: Ari disse “Bento mente”; Bento disse “Ciro mente”; Ciro disse “Ari e Bento mentem”. Sabendo que cada um sempre mente ou sempre diz a verdade, conclui-se que Ciro diz a verdade.",
     "Se Ciro dissesse a verdade, Ari e Bento mentiriam; mas então a fala de Ari (“Bento mente”) seria verdadeira, o que contradiz Ari "
     "mentir. Logo, Ciro mente; daí a fala de Bento (“Ciro mente”) é verdadeira, e a de Ari é falsa."),
], 20)

SOURCES = [
    "Lógica proposicional clássica: validade, regras de inferência e falácias formais.",
    "Obras de referência: Copi, Introdução à lógica; Alencar Filho, Iniciação à lógica matemática.",
    SRC_A,
]
