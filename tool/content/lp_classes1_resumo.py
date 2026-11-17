# -*- coding: utf-8 -*-
"""Língua Portuguesa · Substantivo, adjetivo, artigo e numeral — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "lp-classes1-01", "LP", "LP-03", "resumo", "Substantivo, adjetivo, artigo e numeral", "Língua Portuguesa · Morfologia",
    "portugues_classes1", "Portugues_Substantivo_Adjetivo_Artigo_Numeral_RESUMO.pdf", None, ["Substantivo, adjetivo,", "artigo e numeral"], RES_SUB,
    RES_ITEMS("classificação, flexões e empregos que mudam o sentido"),
    "Tópico do edital: Classes de palavras — substantivo, adjetivo, artigo e numeral (Língua Portuguesa)",
    "Base: gramáticas de referência (Bechara; Cunha e Cintra).", 40)

THEORY = [
    exam("O que a banca cobra",
         "A **classe da palavra no contexto** (substantivação, adjetivo × advérbio, um artigo × um numeral) e o efeito de **trocar, tirar "
         "ou deslocar** um termo: artigo, adjetivo anteposto, flexão de compostos."),
    h2("1. Substantivo"),
    bl("**Concreto**: ser com existência própria, real ou imaginária (casa, ar, fada). **Abstrato**: ação, estado, qualidade, sentimento (prisão, beleza, saudade).",
       "**Substantivação**: qualquer palavra com determinante vira substantivo — *o olhar, um não, o porquê*.",
       "**Comum de dois**: o/a agente, o/a policial. **Sobrecomum**: a testemunha, a vítima, o cônjuge, a criança.",
       "**Gênero que muda o sentido**: o capital/a capital; o cabeça/a cabeça; o moral/a moral; o grama/a grama.",
       "**Atenção ao gênero**: o dó, o champanha, o eclipse × a alface, a cal, a dinamite, a omoplata."),
    tb(["Plural", "Regra", "Exemplos"], [0.2, 0.36, 0.44], [
        ("-ão", "-ões, -ães ou -ãos", "eleições; pães, capitães, escrivães; cidadãos, órgãos, irmãos"),
        ("-il", "Oxítona: -is. Paroxítona: -eis", "fuzis × fósseis, répteis"),
        ("-zinho", "Plural da base, sem o S, + zinhos", "pãezinhos, florezinhas, papeizinhos"),
        ("Compostos", "Variam os que são substantivo, adjetivo ou numeral", "couves-flores, guardas-civis, segundas-feiras"),
        ("Compostos", "Verbo e palavra invariável não variam", "guarda-chuvas, vice-presidentes, abaixo-assinados"),
        ("Compostos", "Com preposição: só o primeiro", "pés de moleque, pores do sol"),
    ]),
    h2("2. Adjetivo"),
    bl("**Locução adjetiva**: de chuva = pluvial; de rio = fluvial; de aluno = discente; de professor = docente; de prisão = carcerário.",
       "**Compostos**: só o último varia (político-sociais). **Cor + substantivo**: invariável (verde-garrafa, amarelo-ouro); também azul-marinho e azul-celeste.",
       "**Mais bom, mais grande**: corretos ao comparar duas qualidades do mesmo ser.",
       "**Superlativos eruditos**: paupérrimo, celebérrimo, amicíssimo, fidelíssimo, dificílimo, macérrimo, nobilíssimo.",
       "**Posição**: homem pobre (sem recursos) × pobre homem (coitado); grande homem × homem grande.",
       "**Adjetivo × advérbio**: *falaram alto* (advérbio, invariável) × *são altas* (adjetivo)."),
    h2("3. Artigo"),
    bl("**Todo o** = inteiro; **todo** = qualquer.",
       "Antes de **possessivo**: facultativo (por isso a crase também é).",
       "Depois de **cujo**: proibido. Depois de **ambos**: obrigatório.",
       "**Uns** + numeral = aproximação (*uns vinte homens*)."),
    h2("4. Numeral"),
    bl("**Reis, papas, séculos**: ordinal até décimo; cardinal de onze em diante (século V = quinto; século XXI = vinte e um).",
       "**Artigos de lei**: ordinal até nove; cardinal de dez em diante (art. 9º = nono; art. 10 = dez).",
       "**Milhão e milhar** são masculinos: *os milhares de pessoas*.",
       "**Meio**: numeral varia (*meia garrafa*); advérbio não (*meio cansada*).",
       "**Um**: numeral se indica quantidade; artigo se indica imprecisão."),
]

SUMMARY = [
    h2("Quadro: a mesma palavra, classes diferentes"),
    tb(["Palavra", "Como…", "Exemplo", "Como…", "Exemplo"], [0.12, 0.14, 0.3, 0.14, 0.3], [
        ("jantar", "substantivo", "O jantar atrasou.", "verbo", "Vamos jantar."),
        ("alto", "adjetivo", "Muro alto.", "advérbio", "Falou alto."),
        ("um", "artigo", "Um homem ligou.", "numeral", "Só um homem ligou."),
        ("meio", "numeral", "Meia hora.", "advérbio", "Meio tensa."),
        ("certo", "adjetivo", "Resposta certa.", "pronome", "Certa resposta."),
        ("não", "advérbio", "Não veio.", "substantivo", "Ouviu um não."),
    ]),
    h2("Leve para a prova"),
    bl("A classe depende da **função na frase**.",
       "Determinante antes = **substantivo** (o olhar, um não).",
       "Invariável ligado ao verbo = **advérbio**.",
       "**Guarda** verbo não varia (guarda-chuvas); **guarda** substantivo varia (guardas-civis).",
       "Cor + substantivo: **invariável**.",
       "Adjetivo anteposto pode **mudar o sentido**.",
       "**Todo o** ≠ **todo**.",
       "**Cujo** nunca vem seguido de artigo.",
       "Art. 9º (nono), art. 10 (dez).",
       "**Os** milhares; **meio** cansada."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "CLASSES NOMINAIS", "rootSub": "a classe depende da função na frase",
    "left": [
        {"label": "Substantivo", "items": ["Nomeia seres, ações, qualidades", "Abstrato: ação, estado, qualidade", "Substantivação: o olhar, um não"]},
        {"label": "Gênero", "items": ["Comum de dois: o/a agente", "Sobrecomum: a testemunha", "o capital ≠ a capital"]},
        {"label": "Plural", "items": ["-ão: -ões, -ães, -ãos", "fuzis × fósseis", "pãezinhos, florezinhas"]},
        {"label": "Plural dos compostos", "items": ["Variam os dois: guardas-civis", "Só o 2º: guarda-chuvas", "Só o 1º: pés de moleque"]},
        {"label": "Banca", "items": ["Classe no contexto", "Tirar o artigo muda o sentido?", "Deslocar o adjetivo muda?"]},
    ],
    "right": [
        {"label": "Adjetivo", "items": ["Caracteriza o substantivo", "Locução: de chuva = pluvial", "Adjetivo varia; advérbio não"]},
        {"label": "Adjetivo composto", "items": ["Só o último varia", "Cor + substantivo: invariável", "azul-marinho: invariável"]},
        {"label": "Grau e posição", "items": ["mais bom do que esperto", "paupérrimo, celebérrimo", "pobre homem ≠ homem pobre"]},
        {"label": "Artigo", "items": ["todo o = inteiro · todo = qualquer", "Facultativo antes de possessivo", "Nunca depois de cujo"]},
        {"label": "Numeral", "items": ["Século V: quinto · XXI: vinte e um", "Art. 9º: nono · art. 10: dez", "os milhares · meio cansada"]},
    ],
}

QUIZ = quiz([
    ("C", "Em “O porquê da decisão não foi divulgado”, o vocábulo porquê é substantivo.",
     "Está determinado por artigo e equivale a motivo."),
    ("E", "O plural de guarda-chuva é guardas-chuvas, pois os dois elementos são substantivos.",
     "Guarda, aqui, é verbo e não varia: guarda-chuvas."),
    ("C", "O substantivo vítima é sobrecomum.",
     "Tem uma só forma e um só gênero para os dois sexos."),
    ("E", "Em “Os carros azul-marinhos pertencem à corporação”, o adjetivo está corretamente flexionado.",
     "Azul-marinho é invariável: carros azul-marinho."),
    ("C", "A locução adjetiva em “corpo de alunos” equivale ao adjetivo discente.",
     "De aluno = discente; de professor = docente."),
    ("E", "As expressões “todo o batalhão” e “todo batalhão” têm o mesmo sentido.",
     "Com artigo, o batalhão inteiro; sem artigo, qualquer batalhão."),
    ("C", "Em “Os presos falaram baixo”, a palavra baixo é advérbio.",
     "Modifica o verbo e não varia."),
    ("E", "A leitura correta de “século XXI” é “século vigésimo primeiro”.",
     "A partir de onze, usa-se o cardinal: século vinte e um."),
    ("C", "Em “Ela chegou meio atrasada”, o vocábulo meio está corretamente empregado, por ser advérbio.",
     "Com o sentido de um pouco, não varia."),
    ("E", "O superlativo absoluto sintético erudito de pobre é pobríssimo, sendo incorreta a forma paupérrimo.",
     "Paupérrimo é a forma erudita, plenamente correta; pobríssimo é a forma popular, também registrada."),
], 10)

SOURCES = [GRAM, SRC_R]
