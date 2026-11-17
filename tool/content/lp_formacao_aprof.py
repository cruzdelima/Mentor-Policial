# -*- coding: utf-8 -*-
"""Língua Portuguesa · Estrutura e formação de palavras — MATERIAL APROFUNDADO (estudo inicial)."""
from common import *

MATERIAL = material(
    "lp-formacao-02", "LP", "LP-18", "aprofundado", "Estrutura e formação de palavras", "Língua Portuguesa · Morfologia",
    "portugues_formacao_aprofundado", "Portugues_Formacao_Palavras_APROFUNDADO.pdf", None, ["Estrutura e", "formação de palavras"],
    ["Teoria completa para o primeiro estudo: elementos mórficos, derivação, composição", "e outros processos, com 20 questões no estilo Cebraspe."],
    [("01", "Estrutura", "radical, afixos, desinências e vogal temática"),
     ("02", "Derivação", "prefixal, sufixal, parassintética, regressiva, imprópria"),
     ("03", "Composição", "justaposição e aglutinação"),
     ("04", "Outros processos", "hibridismo, abreviação, sigla, onomatopeia"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Estrutura e formação de palavras (Língua Portuguesa)",
    "Base: gramáticas de referência (Bechara; Cunha e Cintra).", 90)

THEORY = [
    exam("Como estudar este material",
         "Assunto curto e muito previsível. O Cebraspe pergunta o **processo de formação** de uma palavra do texto ou o **sentido de um afixo** "
         "(“o prefixo *des-* indica negação”). Decore o quadro da seção 2 e o teste da parassíntese."),

    h2("1. Estrutura das palavras"),
    tb(["Elemento", "Função", "Exemplo"], [0.24, 0.4, 0.36], [
        ("Radical", "Parte que carrega o significado básico", "**polic**-ial, **polic**-iamento"),
        ("Prefixo", "Afixo antes do radical", "**in**-feliz, **re**-abrir, **des**-leal"),
        ("Sufixo", "Afixo depois do radical", "investiga-**ção**, agress-**or**, feliz-**mente**"),
        ("Vogal temática", "Indica a conjugação ou o grupo do nome", "cant-**a**-r, vend-**e**-r, part-**i**-r"),
        ("Desinências", "Indicam flexões (gênero, número, pessoa, tempo)", "agente-**s**, delegad-**a**, cantá-**va**-**mos**"),
        ("Vogal e consoante de ligação", "Facilitam a pronúncia", "gas-**ô**-metro, cafe-**t**-eira"),
    ]),

    h2("2. Derivação"),
    tb(["Processo", "Como se forma", "Exemplos"], [0.22, 0.4, 0.38], [
        ("Prefixal", "Prefixo + radical", "reabrir, desleal, ilegal, subchefe"),
        ("Sufixal", "Radical + sufixo", "investigação, policial, rapidamente, agressor"),
        ("Prefixal e sufixal", "Prefixo e sufixo, mas a palavra existe com **um só** deles", "**in**feliz**mente** (infeliz / felizmente), **des**leal**dade** (desleal / lealdade)"),
        ("Parassintética", "Prefixo e sufixo **ao mesmo tempo**: sem um deles, a palavra não existe", "**en**tard**ecer**, **a**manh**ecer**, **en**riqu**ecer**, **es**clar**ecer**, **a**pedr**ejar**"),
        ("Regressiva", "Redução da palavra; em geral, **substantivo a partir de verbo**", "combate (combater), ataque, saque (sacar), pesca, debate"),
        ("Imprópria (conversão)", "Mudança de classe, sem mudar a forma", "**o** jantar, **o** sim, **um** não, **o** porquê"),
    ]),
    key("Teste da parassíntese",
        "Retire o prefixo e, depois, o sufixo. Se **nenhuma** das duas formas existir, é parassíntese: *entardecer* › “tardecer”? não; “entarde”? não › **parassintética**. "
        "Se uma das formas existir, é prefixal e sufixal: *infelizmente* › *felizmente* existe › **prefixal e sufixal**."),

    h2("3. Composição"),
    tb(["Processo", "O que acontece", "Exemplos"], [0.22, 0.4, 0.38], [
        ("Justaposição", "Os radicais se unem **sem perda** de som", "girassol, passatempo, guarda-chuva, pontapé, pé de moleque"),
        ("Aglutinação", "Os radicais se unem **com perda** de som", "planalto (plano + alto), aguardente (água + ardente), embora (em boa hora), fidalgo (filho de algo)"),
    ]),
    trap("Justaposição × aglutinação",
         "*Girassol* parece aglutinação, mas *gira + sol* não perde nenhum som: é **justaposição**. *Planalto* perde o *o* de *plano*: é **aglutinação**."),

    h2("4. Outros processos"),
    bl("**Hibridismo**: elementos de línguas diferentes — *automóvel* (grego + latim), *televisão* (grego *tele* + latim *visão*), *burocracia* (francês + grego), *sociologia* (latim + grego).",
       "**Abreviação (redução)**: *moto* (motocicleta), *foto*, *cine*, *pneu*.",
       "**Siglonimização**: *PF, PRF, ONU, INSS*. Quando a sigla vira palavra e gera derivados: *petista, celetista*.",
       "**Onomatopeia**: imitação de sons — *tique-taque, zunzum, cochicho*.",
       "**Estrangeirismos** e **neologismos**: *deletar, printar*."),

    h2("5. Sentido de prefixos e sufixos"),
    tb(["Afixo", "Sentido", "Exemplos"], [0.18, 0.32, 0.5], [
        ("a-, an-, des-, in-, i-", "negação, privação", "atípico, anormal, desleal, ilegal, inativo"),
        ("anti-, contra-", "oposição", "antidrogas, contraordem"),
        ("re-", "repetição ou retrocesso", "reabrir, refazer, regredir"),
        ("pre-, pré-", "anterioridade", "prever, pré-edital"),
        ("pós-", "posterioridade", "pós-edital, pós-graduação"),
        ("sub-", "posição inferior", "subchefe, subsolo"),
        ("super-, hiper-", "excesso, posição superior", "superlotado, hipertensão"),
        ("ex-", "estado anterior ou movimento para fora", "ex-delegado, exportar"),
        ("-dor, -or, -ista", "agente", "investigador, agressor, motorista"),
        ("-ção, -mento", "ação ou resultado", "investigação, policiamento"),
        ("-vel", "possibilidade", "punível, inafiançável"),
        ("-mente", "modo (forma advérbios)", "rapidamente"),
    ]),

    h2("6. Como o Cebraspe cobra"),
    bl("“A palavra X é formada por derivação parassintética / prefixal e sufixal.”",
       "“O prefixo presente em X expressa negação.”",
       "“X e Y são formadas pelo mesmo processo.”",
       "“O vocábulo X resulta de derivação imprópria” (substantivação de verbo ou adjetivo)."),
]

QUIZ = quiz([
    ("C", "A palavra entardecer é formada por derivação parassintética.",
     "Não existem tardecer nem entarde: prefixo e sufixo entram juntos."),
    ("E", "A palavra infelizmente é formada por derivação parassintética.",
     "Existem infeliz e felizmente: é derivação prefixal e sufixal."),
    ("C", "O substantivo combate, formado a partir do verbo combater, exemplifica a derivação regressiva.",
     "Substantivo formado pela redução do verbo."),
    ("E", "A palavra girassol é formada por composição por aglutinação.",
     "Gira e sol se unem sem perda de som: justaposição."),
    ("C", "A palavra planalto é formada por composição por aglutinação.",
     "Plano + alto, com perda do o final de plano."),
    ("E", "Em “O jantar foi servido”, a palavra jantar resulta de derivação sufixal.",
     "O verbo passou a substantivo sem mudar de forma: derivação imprópria."),
    ("C", "A palavra automóvel é um hibridismo, pois une elementos de origem grega e latina.",
     "Auto (grego) + móvel (latim)."),
    ("E", "Na palavra desleal, o prefixo des- indica repetição.",
     "Des- indica negação: que não é leal."),
    ("C", "Na palavra investigação, o sufixo -ção forma substantivo a partir de verbo e indica ação.",
     "Investigar › investigação."),
    ("E", "A palavra aguardente é formada por composição por justaposição.",
     "Água + ardente, com perda de som: aglutinação."),

    ("C", "A sigla PF exemplifica o processo de formação por siglonimização.",
     "Forma-se com as letras iniciais de Polícia Federal."),
    ("E", "O verbo enriquecer é formado por derivação prefixal.",
     "Não existem enrico nem riquecer: é parassintética."),
    ("C", "Na palavra reabrir, o prefixo re- indica repetição.",
     "Reabrir = abrir de novo."),
    ("E", "A palavra pontapé é formada por composição por aglutinação.",
     "Ponta + pé, sem perda de som: justaposição."),
    ("C", "O substantivo saque, relacionado ao verbo sacar, é formado por derivação regressiva.",
     "Redução do verbo para formar o substantivo."),
    ("E", "A palavra televisão é formada apenas por elementos de origem latina.",
     "Tele é de origem grega: trata-se de hibridismo."),
    ("C", "A palavra deslealdade é formada por derivação prefixal e sufixal.",
     "Existem desleal e lealdade: os afixos não entram simultaneamente."),
    ("E", "A palavra foto, redução de fotografia, é formada por derivação regressiva.",
     "Trata-se de abreviação (redução vocabular)."),
    ("C", "A palavra tique-taque é formada por onomatopeia.",
     "Imita o som do relógio."),
    ("E", "Na palavra agressor, o sufixo -or indica lugar.",
     "O sufixo -or indica agente: quem agride."),
], 20)

SOURCES = [GRAM, SRC_A]
