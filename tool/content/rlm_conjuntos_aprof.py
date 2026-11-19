# -*- coding: utf-8 -*-
"""Raciocínio Lógico · Conjuntos e operações — MATERIAL APROFUNDADO."""
from common import *

MATERIAL = material(
    "rlm-conjuntos-02", "RLM", "RLM-07", "aprofundado", "Conjuntos e operações", "Raciocínio Lógico e Matemática · Conjuntos",
    "raciocinio_conjuntos_aprofundado", "RaciocinioLogico_Conjuntos_APROFUNDADO.pdf", None, ["Conjuntos e", "operações"],
    ["Pertinência, inclusão, união, interseção, diferença, complementar e os problemas", "com diagramas de Venn, com 20 questões no estilo Cebraspe."],
    [("01", "Noções", "elemento, conjunto, subconjunto"),
     ("02", "Operações", "união, interseção, diferença, complementar"),
     ("03", "Contagem", "fórmula da união para 2 e 3 conjuntos"),
     ("04", "Diagramas de Venn", "resolver de dentro para fora"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Conjuntos e operações — Raciocínio Lógico",
    "Base: teoria elementar dos conjuntos.", 70)

THEORY = [
    exam("Como estudar este material",
         "O Cebraspe cobra conjuntos em **problemas com números** (quantas pessoas falam inglês e espanhol, quantos policiais fizeram os dois "
         "cursos) e em itens de **notação** (pertence, está contido). A técnica principal é o **diagrama de Venn preenchido de dentro para "
         "fora**: comece sempre pela interseção."),

    h2("1. Noções básicas"),
    tb(["Símbolo", "Leitura", "Relação entre"], [0.16, 0.44, 0.4], [
        ("x ∈ A", "x pertence a A", "**elemento** e conjunto"),
        ("x ∉ A", "x não pertence a A", "elemento e conjunto"),
        ("A ⊂ B", "A está contido em B (A é subconjunto de B)", "**conjunto** e conjunto"),
        ("A ⊄ B", "A não está contido em B", "conjunto e conjunto"),
        ("∅ ou { }", "conjunto vazio", "—"),
        ("n(A)", "número de elementos de A", "—"),
    ]),
    bl("**Pertinência** (∈) liga elemento a conjunto; **inclusão** (⊂) liga conjunto a conjunto. Se A = {1, 2}, então 1 ∈ A e {1} ⊂ A, "
       "mas **não** {1} ∈ A.",
       "O **vazio** é subconjunto de **qualquer** conjunto, e todo conjunto é subconjunto de si mesmo.",
       "Um conjunto com **n** elementos tem **2ⁿ subconjuntos** (incluindo o vazio e ele próprio). O conjunto de todos eles é o "
       "**conjunto das partes**, P(A)."),

    h2("2. Operações"),
    tb(["Operação", "Notação", "Elementos", "Exemplo: A = {1, 2, 3}, B = {3, 4}"], [0.18, 0.14, 0.36, 0.32], [
        ("União", "A ∪ B", "estão em A **ou** em B (ou nos dois)", "{1, 2, 3, 4}"),
        ("Interseção", "A ∩ B", "estão em A **e** em B", "{3}"),
        ("Diferença", "A − B", "estão em A e **não** em B", "{1, 2}"),
        ("Diferença", "B − A", "estão em B e não em A", "{4}"),
        ("Complementar", "Aᶜ ou A'", "estão no universo U e não em A", "depende de U"),
    ]),
    bl("Quando A ∩ B = ∅, os conjuntos são **disjuntos**.",
       "Se A ⊂ B, então A ∪ B = B e A ∩ B = A.",
       "Leis de De Morgan para conjuntos: (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ e (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ (as mesmas da lógica)."),

    h2("3. Quantos elementos tem a união"),
    key("Dois conjuntos",
        "**n(A ∪ B) = n(A) + n(B) − n(A ∩ B)**. Subtrai-se a interseção porque ela foi contada duas vezes."),
    key("Três conjuntos",
        "**n(A ∪ B ∪ C) = n(A) + n(B) + n(C) − n(A ∩ B) − n(A ∩ C) − n(B ∩ C) + n(A ∩ B ∩ C)**."),
    bl("**Só A** (apenas A): n(A) − n(A ∩ B), em dois conjuntos.",
       "**Nenhum dos dois**: total − n(A ∪ B).",
       "**Exatamente um**: n(A ∪ B) − n(A ∩ B)."),

    h2("4. Problemas com diagrama de Venn"),
    p("Desenhe os círculos e preencha **primeiro a região mais interna** (a interseção de todos), depois as interseções de dois a dois e por "
      "último as regiões “só”. Cada número dado no enunciado costuma ser um **total do círculo**, não a região “só”."),
    h3("Exemplo resolvido"),
    bl("Numa delegacia com **60** policiais, **35** fizeram o curso de tiro, **28** o de direção defensiva e **10** fizeram os dois.",
       "Interseção: 10. Só tiro: 35 − 10 = **25**. Só direção: 28 − 10 = **18**.",
       "Fizeram pelo menos um: 25 + 18 + 10 = **53** (ou 35 + 28 − 10).",
       "Não fizeram nenhum: 60 − 53 = **7**."),
    h3("Exemplo com três conjuntos"),
    bl("Entre **100** candidatos, 50 estudaram Português (P), 40 Direito (D) e 30 Informática (I). Estudaram P e D: 15; P e I: 10; "
       "D e I: 8; as três: 5.",
       "Pela fórmula: 50 + 40 + 30 − 15 − 10 − 8 + 5 = **92** estudaram pelo menos uma.",
       "Nenhuma: 100 − 92 = **8**. Só P: 50 − 15 − 10 + 5 = **30**."),

    h2("5. Conjuntos numéricos (noção)"),
    bl("**Naturais** (ℕ): 0, 1, 2, 3...",
       "**Inteiros** (ℤ): ..., −2, −1, 0, 1, 2...",
       "**Racionais** (ℚ): frações de inteiros (inclui decimais exatos e dízimas periódicas).",
       "**Irracionais**: decimais infinitos não periódicos (√2, π).",
       "**Reais** (ℝ): racionais e irracionais. Vale ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ."),

    h2("6. Como o Cebraspe cobra"),
    bl("Um texto com totais de grupos e afirmações do tipo “exatamente x pessoas fizeram só um curso”. Monte o diagrama antes de julgar.",
       "Itens de notação: ∈ para elemento, ⊂ para conjunto.",
       "Número de subconjuntos: 2ⁿ.",
       "Na dúvida real, **deixe em branco**: no Cebraspe, cada erro anula um acerto."),
]

QUIZ = quiz([
    ("C", "Se A = {2, 4, 6}, então 4 ∈ A.",
     "4 é elemento de A."),
    ("E", "Se A = {2, 4, 6}, então {4} ∈ A.",
     "{4} é conjunto: o correto é {4} ⊂ A."),
    ("C", "O conjunto vazio é subconjunto de qualquer conjunto.",
     "Propriedade da inclusão."),
    ("C", "Um conjunto com 5 elementos possui 32 subconjuntos.",
     "2⁵ = 32."),
    ("E", "Se A = {1, 2, 3, 4} e B = {3, 4, 5}, então A − B = {1, 2, 5}.",
     "A − B = {1, 2}; o 5 está em B, não em A."),
    ("C", "Se A = {1, 2, 3, 4} e B = {3, 4, 5}, então A ∩ B = {3, 4}.",
     "Elementos comuns."),
    ("C", "Se A ⊂ B, então A ∪ B = B.",
     "Todos os elementos de A já estão em B."),
    ("E", "Se n(A) = 20, n(B) = 15 e n(A ∩ B) = 5, então n(A ∪ B) = 35.",
     "n(A ∪ B) = 20 + 15 − 5 = 30."),
    ("C", "O complementar da união de A e B é igual à interseção dos complementares de A e de B.",
     "Lei de De Morgan para conjuntos."),
    ("E", "O número π pertence ao conjunto dos números racionais.",
     "π é irracional."),

    ("C", "Em uma delegacia com 60 policiais, 35 fizeram o curso de tiro, 28 o de direção defensiva e 10 fizeram os dois. Nessa situação, 7 policiais não fizeram nenhum dos dois cursos.",
     "Pelo menos um: 35 + 28 − 10 = 53; nenhum: 60 − 53 = 7."),
    ("E", "Na situação do item anterior, 35 policiais fizeram somente o curso de tiro.",
     "Só tiro: 35 − 10 = 25."),
    ("C", "Na mesma situação, 43 policiais fizeram exatamente um dos dois cursos.",
     "Só tiro (25) + só direção (18) = 43."),
    ("C", "Em um grupo de 100 candidatos, 50 estudaram Português, 40 Direito e 30 Informática; 15 estudaram Português e Direito, 10 Português e Informática, 8 Direito e Informática, e 5 as três. Nesse caso, 8 candidatos não estudaram nenhuma das três matérias.",
     "União: 50 + 40 + 30 − 15 − 10 − 8 + 5 = 92; nenhuma: 100 − 92 = 8."),
    ("E", "Na situação do item anterior, 35 candidatos estudaram somente Português.",
     "Só Português: 50 − 15 − 10 + 5 = 30."),
    ("C", "Em uma operação, 40 agentes participaram da fase 1 e 30 da fase 2. Se 55 agentes participaram de pelo menos uma das fases, então 15 participaram das duas.",
     "55 = 40 + 30 − x → x = 15."),
    ("E", "Se, entre 80 servidores, 50 falam inglês e 45 falam espanhol, então nenhum servidor fala as duas línguas.",
     "50 + 45 = 95 > 80: ao menos 15 falam as duas."),
    ("C", "Se 50 dos 80 servidores falam inglês e 45 falam espanhol, então pelo menos 15 servidores falam as duas línguas.",
     "n(I ∩ E) = 50 + 45 − n(I ∪ E) ≥ 95 − 80 = 15."),
    ("E", "Se A e B são conjuntos disjuntos, então A ∩ B = A.",
     "Disjuntos têm interseção vazia."),
    ("C", "Todo número inteiro é também um número racional.",
     "Cada inteiro n pode ser escrito como n/1."),
], 20)

SOURCES = [
    "Teoria elementar dos conjuntos: operações e princípio da inclusão-exclusão.",
    "Obras de referência: Iezzi e Murakami, Fundamentos de matemática elementar, v. 1.",
    SRC_A,
]
