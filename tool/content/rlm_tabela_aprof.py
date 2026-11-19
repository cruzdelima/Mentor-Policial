# -*- coding: utf-8 -*-
"""Raciocínio Lógico · Tabela-verdade, tautologia e contradição — MATERIAL APROFUNDADO."""
from common import *

MATERIAL = material(
    "rlm-tabela-02", "RLM", "RLM-02", "aprofundado", "Tabela-verdade, tautologia e contradição", "Raciocínio Lógico e Matemática · Lógica proposicional",
    "raciocinio_tabela_verdade_aprofundado", "RaciocinioLogico_TabelaVerdade_APROFUNDADO.pdf", None, ["Tabela-verdade"],
    ["Como montar a tabela-verdade de qualquer proposição, quantas linhas ela tem e como reconhecer", "tautologia, contradição e contingência, com 20 questões no estilo Cebraspe."],
    [("01", "Linhas", "2 elevado ao número de proposições simples"),
     ("02", "Montagem", "coluna a coluna, do mais interno ao mais externo"),
     ("03", "Classificação", "tautologia, contradição e contingência"),
     ("04", "Atalhos", "testar só a linha que pode dar F"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Tabela-verdade, tautologia e contradição — Raciocínio Lógico",
    "Base: lógica proposicional clássica.", 80)

THEORY = [
    exam("Como estudar este material",
         "A tabela-verdade é a ferramenta que resolve quase todo item de lógica proposicional. O Cebraspe cobra: **o número de linhas**, "
         "**o valor de uma linha** e se uma proposição é **tautologia**. Monte pelo menos três tabelas inteiras à mão antes de usar os atalhos."),

    h2("1. Quantas linhas"),
    key("Regra",
        "Uma proposição com **n proposições simples distintas** tem uma tabela-verdade com **2ⁿ linhas**. Cada letra só conta **uma vez**, "
        "mesmo que apareça repetida ou negada."),
    tb(["Proposições simples", "Linhas", "Exemplo"], [0.28, 0.16, 0.56], [
        ("1", "2", "¬P"),
        ("2", "4", "P → Q · (P ∧ Q) ∨ ¬P"),
        ("3", "8", "(P ∨ Q) → R"),
        ("4", "16", "(P ∧ Q) ↔ (R ∨ S)"),
        ("5", "32", "[(P → Q) ∧ R] ∨ (S ↔ T)"),
    ]),
    trap("Pegadinha",
         "Em (P ∨ ¬P) → (Q ∧ P), há **duas** proposições simples (P e Q), e a tabela tem **4** linhas, não 8. A negação ¬P não é uma proposição "
         "simples nova."),

    h2("2. Como montar"),
    p("Distribua os valores das proposições simples de forma que **todas as combinações** apareçam uma única vez. Com 3 letras: a primeira "
      "coluna alterna de **4 em 4** (VVVVFFFF), a segunda de **2 em 2** (VVFFVVFF) e a terceira de **1 em 1** (VFVFVFVF). Depois, resolva "
      "do mais interno para o mais externo: primeiro as negações e os parênteses, por último o conectivo principal."),
    h3("Exemplo resolvido: (P ∧ Q) → ¬R"),
    tb(["P", "Q", "R", "P ∧ Q", "¬R", "(P ∧ Q) → ¬R"], [0.1, 0.1, 0.1, 0.22, 0.16, 0.32], [
        ("V", "V", "V", "V", "F", "**F**"),
        ("V", "V", "F", "V", "V", "V"),
        ("V", "F", "V", "F", "F", "V"),
        ("V", "F", "F", "F", "V", "V"),
        ("F", "V", "V", "F", "F", "V"),
        ("F", "V", "F", "F", "V", "V"),
        ("F", "F", "V", "F", "F", "V"),
        ("F", "F", "F", "F", "V", "V"),
    ]),
    p("A coluna final tem **7 V e 1 F**: a proposição só é falsa quando P, Q e R são todas verdadeiras (antecedente V e consequente F)."),

    h2("3. Tautologia, contradição e contingência"),
    tb(["Classificação", "Coluna final", "Exemplos"], [0.22, 0.3, 0.48], [
        ("**Tautologia**", "**Só V**, em todas as linhas", "P ∨ ¬P · P → P · (P ∧ Q) → P · P → (P ∨ Q)"),
        ("**Contradição**", "**Só F**, em todas as linhas", "P ∧ ¬P · P ↔ ¬P · ¬(P → P)"),
        ("**Contingência**", "Tem V **e** F", "P → Q · P ∧ Q · P ∨ Q · P ↔ Q"),
    ]),
    bl("A **negação de uma tautologia** é uma contradição, e vice-versa.",
       "Toda tautologia vale independentemente do conteúdo das proposições: *Ou chove ou não chove* é sempre verdadeira.",
       "As **regras de inferência** (modus ponens, modus tollens, silogismo) correspondem a condicionais tautológicas, como "
       "[(P → Q) ∧ P] → Q."),

    h2("4. Atalhos para não montar a tabela inteira"),
    key("Testar a condicional pelo caso falso",
        "Para saber se A → B é tautologia, **tente torná-la falsa**: suponha A verdadeira e B falsa. Se isso for **possível**, não é "
        "tautologia; se levar a uma **contradição** (uma letra precisaria ser V e F ao mesmo tempo), é tautologia."),
    p("Exemplo: (P ∧ Q) → P. Para ser falsa, o antecedente P ∧ Q seria V (logo P = V e Q = V) e o consequente P seria F. Mas P não pode ser V e "
      "F ao mesmo tempo: **impossível**. Logo, é **tautologia**."),
    p("Exemplo: (P ∨ Q) → P. Para ser falsa: P ∨ Q = V e P = F. Com P = F e Q = V isso acontece. Logo, **não** é tautologia (é contingência)."),
    bl("Para a **conjunção** ser V, todas as partes precisam ser V: comece por elas.",
       "Para a **disjunção** ser F, todas as partes precisam ser F.",
       "Conte as linhas pedidas: “a tabela tem exatamente k linhas com valor V” se resolve contando os casos que tornam a proposição falsa."),
    h3("Quantas linhas são V em cada conectivo (duas letras)"),
    tb(["Proposição", "Linhas V", "Linhas F"], [0.4, 0.3, 0.3], [
        ("P ∧ Q", "1", "3"),
        ("P ∨ Q", "3", "1"),
        ("P → Q", "3", "1"),
        ("P ↔ Q", "2", "2"),
        ("P ⊻ Q", "2", "2"),
    ]),

    h2("5. Como o Cebraspe cobra"),
    bl("“A tabela-verdade da proposição ... tem 16 linhas”: conte as letras **distintas** e faça 2ⁿ.",
       "“A proposição ... é uma tautologia”: use o atalho do caso falso.",
       "“Na tabela-verdade de ..., há exatamente x linhas em que a proposição é verdadeira”: conte os casos falsos e subtraia do total.",
       "“Se P é V e Q é F, então ...”: substitua os valores e resolva de dentro para fora.",
       "Na dúvida real, **deixe em branco**: no Cebraspe, cada erro anula um acerto."),
]

QUIZ = quiz([
    ("C", "A tabela-verdade da proposição (P ∧ Q) → R possui 8 linhas.",
     "Há 3 proposições simples: 2³ = 8."),
    ("E", "A tabela-verdade da proposição (P → ¬Q) ∨ (Q ∧ P) possui 16 linhas.",
     "Só há 2 proposições simples distintas (P e Q): 2² = 4 linhas."),
    ("C", "A proposição P ∨ ¬P é uma tautologia.",
     "Uma das duas é sempre verdadeira."),
    ("C", "A proposição P ∧ ¬P é uma contradição.",
     "P e ¬P nunca são verdadeiras ao mesmo tempo."),
    ("E", "A proposição P → Q é uma tautologia.",
     "É falsa quando P é V e Q é F: é contingência."),
    ("C", "A proposição (P ∧ Q) → P é uma tautologia.",
     "Para ser falsa, P teria de ser V (no antecedente) e F (no consequente): impossível."),
    ("E", "A proposição (P ∨ Q) → Q é uma tautologia.",
     "Com P = V e Q = F, o antecedente é V e o consequente F: a condicional é falsa."),
    ("C", "Na tabela-verdade da proposição P ∨ Q, há exatamente uma linha em que a proposição é falsa.",
     "Só quando P e Q são ambas falsas."),
    ("C", "A negação de uma tautologia é uma contradição.",
     "Se a coluna só tem V, a negação só tem F."),
    ("E", "A proposição P ↔ Q é verdadeira em três das quatro linhas de sua tabela-verdade.",
     "É verdadeira em duas linhas (valores iguais) e falsa em duas."),

    ("C", "Considere as proposições P: “o suspeito foi preso em flagrante”, Q: “houve mandado judicial” e R: “a prisão foi legal”. A tabela-verdade da proposição (P ∨ Q) → R tem 8 linhas.",
     "Três proposições simples: 2³ = 8."),
    ("C", "A proposição [(P → Q) ∧ P] → Q é uma tautologia.",
     "É o modus ponens. Para ser falsa, Q seria F e P seria V; então P → Q seria F e o antecedente também F: impossível."),
    ("E", "A proposição [(P → Q) ∧ Q] → P é uma tautologia.",
     "Com P = F e Q = V, o antecedente é V e o consequente F: a condicional é falsa (falácia da afirmação do consequente)."),
    ("C", "A proposição P → (P ∨ Q) é uma tautologia.",
     "Se P é V, P ∨ Q também é V: nunca ocorre V → F."),
    ("E", "Na tabela-verdade da proposição (P ∧ Q) → ¬R, a proposição é falsa em exatamente duas linhas.",
     "É falsa só quando P, Q e R são verdadeiras: uma única linha."),
    ("C", "Se P é verdadeira, Q é falsa e R é falsa, então a proposição (P ∨ Q) → R é falsa.",
     "P ∨ Q = V e R = F: V → F é falso."),
    ("E", "A proposição P ↔ ¬P é uma contingência.",
     "P e ¬P sempre têm valores diferentes: a bicondicional é sempre falsa (contradição)."),
    ("C", "A proposição (P → Q) ∨ (Q → P) é uma tautologia.",
     "Para a disjunção ser falsa, P → Q e Q → P teriam de ser falsas: P = V, Q = F e Q = V, P = F ao mesmo tempo. Impossível."),
    ("C", "Uma proposição composta por quatro proposições simples distintas tem tabela-verdade com 16 linhas.",
     "2⁴ = 16."),
    ("E", "Se a proposição A → B é uma tautologia, então B é uma tautologia.",
     "Basta que nunca ocorra A verdadeira e B falsa. Ex.: (P ∧ Q) → P é tautologia, mas P sozinha não é."),
], 20)

SOURCES = [
    "Lógica proposicional clássica: tabelas-verdade e classificação das proposições.",
    "Obras de referência: Alencar Filho, Iniciação à lógica matemática; Copi, Introdução à lógica.",
    SRC_A,
]
