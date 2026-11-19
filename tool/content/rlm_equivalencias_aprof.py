# -*- coding: utf-8 -*-
"""Raciocínio Lógico · Equivalências lógicas e Leis de De Morgan — MATERIAL APROFUNDADO."""
from common import *

MATERIAL = material(
    "rlm-equivalencias-02", "RLM", "RLM-03", "aprofundado", "Equivalências lógicas e Leis de De Morgan", "Raciocínio Lógico e Matemática · Lógica proposicional",
    "raciocinio_equivalencias_aprofundado", "RaciocinioLogico_Equivalencias_APROFUNDADO.pdf", None, ["Equivalências", "lógicas"],
    ["Contrapositiva, condicional como disjunção, bicondicional, De Morgan e as propriedades", "dos conectivos, com 20 questões no estilo Cebraspe."],
    [("01", "Conceito", "mesma tabela-verdade, linha a linha"),
     ("02", "Condicional", "contrapositiva e troca pelo ou"),
     ("03", "De Morgan", "negar o e e o ou"),
     ("04", "Propriedades", "comutativa, distributiva, absorção"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Equivalências lógicas e Leis de De Morgan — Raciocínio Lógico",
    "Base: lógica proposicional clássica.", 80)

THEORY = [
    exam("Como estudar este material",
         "Equivalência é o assunto de lógica **mais cobrado** pelo Cebraspe em provas policiais. Quase todo item é uma frase do tipo "
         "“a proposição X é equivalente a Y”. Decore as **três equivalências da condicional** e as **duas leis de De Morgan**: elas resolvem "
         "a maior parte das questões."),

    h2("1. O que é equivalência"),
    key("Definição",
        "Duas proposições são **logicamente equivalentes** (A ⇔ B) quando têm **a mesma tabela-verdade**: em todas as linhas, os valores "
        "coincidem. Na prática, uma pode substituir a outra sem mudar o sentido lógico."),
    p("Para testar, monte as duas tabelas ou procure **uma linha** em que os valores sejam diferentes: basta uma para **não** haver "
      "equivalência. Outra forma: A e B são equivalentes quando A ↔ B é **tautologia**."),

    h2("2. As equivalências da condicional"),
    tb(["Proposição", "Equivalente", "Nome"], [0.24, 0.36, 0.4], [
        ("P → Q", "**¬Q → ¬P**", "Contrapositiva: **inverte e nega** as duas"),
        ("P → Q", "**¬P ∨ Q**", "Troca da condicional pelo ou: **nega a primeira, mantém a segunda, troca → por ∨**"),
        ("P ∨ Q", "¬P → Q", "O caminho inverso: nega a primeira e troca ∨ por →"),
    ]),
    key("Regra prática: NEYMAR",
        "Para trocar a condicional pelo **ou**: **NE**ga a primeira, **MA**ntém a segunda e troca o conectivo (**R**: “se... então” vira “ou”). "
        "*Se o suspeito fugiu, ele é culpado* ⇔ *O suspeito não fugiu ou é culpado*."),
    trap("Recíproca e inversa NÃO são equivalentes",
         "Dada P → Q: a **recíproca** é Q → P e a **inversa** é ¬P → ¬Q. Nenhuma das duas é equivalente a P → Q (mas são equivalentes "
         "entre si). *Se é policial, é concursado* não equivale a *Se é concursado, é policial*."),
    h3("Exemplo"),
    tb(["Forma", "Frase"], [0.22, 0.78], [
        ("P → Q", "*Se a perícia encontrou digitais, o suspeito esteve no local.*"),
        ("¬Q → ¬P", "*Se o suspeito não esteve no local, a perícia não encontrou digitais.* (equivalente)"),
        ("¬P ∨ Q", "*A perícia não encontrou digitais ou o suspeito esteve no local.* (equivalente)"),
        ("Q → P", "*Se o suspeito esteve no local, a perícia encontrou digitais.* (recíproca: **não** equivalente)"),
    ]),

    h2("3. A bicondicional"),
    tb(["Proposição", "Equivalentes"], [0.24, 0.76], [
        ("P ↔ Q", "(P → Q) ∧ (Q → P) · (¬P ↔ ¬Q) · (P ∧ Q) ∨ (¬P ∧ ¬Q)"),
        ("P ⊻ Q (ou exclusivo)", "¬(P ↔ Q) · P ↔ ¬Q · (P ∧ ¬Q) ∨ (¬P ∧ Q)"),
    ]),

    h2("4. Leis de De Morgan"),
    key("Negar o e e o ou",
        "**¬(P ∧ Q) ⇔ ¬P ∨ ¬Q** · **¬(P ∨ Q) ⇔ ¬P ∧ ¬Q**. Nega as duas e **troca o conectivo**: “e” vira “ou”, “ou” vira “e”."),
    tb(["Proposição", "Equivalente por De Morgan"], [0.5, 0.5], [
        ("*Não é verdade que João é agente e Maria é perita.*", "*João não é agente ou Maria não é perita.*"),
        ("*Não é verdade que choveu ou ventou.*", "*Não choveu e não ventou.* (= *Nem choveu nem ventou.*)"),
    ]),
    nt("De Morgan vale com mais de duas proposições: ¬(P ∧ Q ∧ R) ⇔ ¬P ∨ ¬Q ∨ ¬R. Também se aplica dentro de outras equivalências: "
       "(P ∧ Q) → R ⇔ ¬(P ∧ Q) ∨ R ⇔ ¬P ∨ ¬Q ∨ R."),

    h2("5. Propriedades dos conectivos"),
    tb(["Propriedade", "Conjunção", "Disjunção"], [0.22, 0.39, 0.39], [
        ("Dupla negação", "¬¬P ⇔ P", "¬¬P ⇔ P"),
        ("Idempotência", "P ∧ P ⇔ P", "P ∨ P ⇔ P"),
        ("Comutativa", "P ∧ Q ⇔ Q ∧ P", "P ∨ Q ⇔ Q ∨ P"),
        ("Associativa", "(P ∧ Q) ∧ R ⇔ P ∧ (Q ∧ R)", "(P ∨ Q) ∨ R ⇔ P ∨ (Q ∨ R)"),
        ("Distributiva", "P ∧ (Q ∨ R) ⇔ (P ∧ Q) ∨ (P ∧ R)", "P ∨ (Q ∧ R) ⇔ (P ∨ Q) ∧ (P ∨ R)"),
        ("Absorção", "P ∧ (P ∨ Q) ⇔ P", "P ∨ (P ∧ Q) ⇔ P"),
    ]),
    bl("A **condicional não é comutativa**: P → Q não equivale a Q → P. A bicondicional é: P ↔ Q ⇔ Q ↔ P.",
       "Condicional com antecedente composto: **(P ∧ Q) → R ⇔ P → (Q → R)** (exportação).",
       "Condicional com consequente composto: **P → (Q ∧ R) ⇔ (P → Q) ∧ (P → R)**."),

    h2("6. Como o Cebraspe cobra"),
    bl("O item traz uma frase longa e diz que ela **equivale** a outra. Simbolize as duas e compare com a tabela de equivalências.",
       "A pegadinha preferida é a **recíproca** (Q → P) apresentada como equivalente da condicional.",
       "Outra pegadinha: aplicar De Morgan **sem trocar o conectivo** (¬(P ∧ Q) como ¬P ∧ ¬Q).",
       "Na dúvida, procure **uma linha** que diferencie as duas proposições (ex.: P = V, Q = F)."),
]

QUIZ = quiz([
    ("C", "A proposição P → Q é equivalente a ¬Q → ¬P.",
     "É a contrapositiva."),
    ("E", "A proposição P → Q é equivalente a Q → P.",
     "Q → P é a recíproca. Com P = V e Q = F, P → Q é F e Q → P é V."),
    ("C", "A proposição P → Q é equivalente a ¬P ∨ Q.",
     "Nega a primeira, mantém a segunda e troca o conectivo."),
    ("E", "A proposição ¬(P ∧ Q) é equivalente a ¬P ∧ ¬Q.",
     "Por De Morgan, ¬(P ∧ Q) ⇔ ¬P ∨ ¬Q: é preciso trocar o conectivo."),
    ("C", "A proposição ¬(P ∨ Q) é equivalente a ¬P ∧ ¬Q.",
     "Segunda lei de De Morgan."),
    ("C", "A proposição P ↔ Q é equivalente a (P → Q) ∧ (Q → P).",
     "A bicondicional é a conjunção da condicional com a recíproca."),
    ("E", "A proposição P → Q é equivalente a ¬P → ¬Q.",
     "¬P → ¬Q é a inversa, que não equivale à condicional."),
    ("C", "A proposição P ∨ Q é equivalente a ¬P → Q.",
     "Pela regra da troca: ¬P → Q ⇔ ¬¬P ∨ Q ⇔ P ∨ Q."),
    ("C", "A proposição P ∧ (P ∨ Q) é equivalente a P.",
     "Absorção."),
    ("E", "A proposição P ∨ (Q ∧ R) é equivalente a (P ∨ Q) ∧ R.",
     "Pela distributiva, equivale a (P ∨ Q) ∧ (P ∨ R). Com P = V e R = F, a primeira é V e (P ∨ Q) ∧ R é F."),

    ("C", "A proposição “Se o investigado movimentou valores incompatíveis com sua renda, então ele será intimado” é equivalente a “Se o investigado não for intimado, então ele não movimentou valores incompatíveis com sua renda”.",
     "Contrapositiva: inverte e nega as duas."),
    ("E", "A proposição “Se o servidor recebeu propina, ele cometeu crime” é equivalente a “Se o servidor cometeu crime, ele recebeu propina”.",
     "É a recíproca: não é equivalente."),
    ("C", "A proposição “Se chover, a operação será adiada” é equivalente a “Não chove ou a operação será adiada”.",
     "P → Q ⇔ ¬P ∨ Q."),
    ("E", "A proposição “Não é verdade que o agente e o escrivão faltaram” é equivalente a “O agente não faltou e o escrivão não faltou”.",
     "¬(A ∧ E) ⇔ ¬A ∨ ¬E: “o agente não faltou ou o escrivão não faltou”."),
    ("C", "A proposição “Não é verdade que Pedro é delegado ou Ana é perita” é equivalente a “Pedro não é delegado e Ana não é perita”.",
     "¬(P ∨ A) ⇔ ¬P ∧ ¬A."),
    ("C", "A proposição “O réu confessou ou há provas suficientes” é equivalente a “Se o réu não confessou, então há provas suficientes”.",
     "P ∨ Q ⇔ ¬P → Q."),
    ("E", "A proposição “Se o candidato estudar, então será aprovado” é equivalente a “Se o candidato não estudar, então não será aprovado”.",
     "É a inversa (¬P → ¬Q), que não equivale à condicional."),
    ("C", "A proposição (P ∧ Q) → R é equivalente a ¬P ∨ ¬Q ∨ R.",
     "(P ∧ Q) → R ⇔ ¬(P ∧ Q) ∨ R ⇔ ¬P ∨ ¬Q ∨ R."),
    ("C", "A proposição P → (Q ∧ R) é equivalente a (P → Q) ∧ (P → R).",
     "A condicional distribui sobre a conjunção no consequente."),
    ("E", "A proposição P ↔ Q é equivalente a (P ∧ ¬Q) ∨ (¬P ∧ Q).",
     "Essa é a disjunção exclusiva, que é a negação da bicondicional."),
], 20)

SOURCES = [
    "Lógica proposicional clássica: equivalências notáveis e Leis de De Morgan.",
    "Obras de referência: Alencar Filho, Iniciação à lógica matemática; Copi, Introdução à lógica.",
    SRC_A,
]
