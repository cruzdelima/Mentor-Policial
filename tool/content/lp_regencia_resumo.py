# -*- coding: utf-8 -*-
"""Língua Portuguesa · Regência nominal e verbal — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "lp-regencia-01", "LP", "LP-12", "resumo", "Regência nominal e verbal", "Língua Portuguesa · Sintaxe",
    "portugues_regencia", "Portugues_Regencia_RESUMO.pdf", None, ["Regência", "nominal e verbal"], RES_SUB,
    RES_ITEMS("verbos que mudam de sentido, regência nominal e relativos"),
    "Tópico do edital: Regência nominal e verbal (Língua Portuguesa)",
    "Base: gramáticas de referência e Dicionário de regência verbal (Celso Luft).", 35)

THEORY = [
    exam("O que a banca cobra",
         "Verbos cujo **sentido muda com a regência**, **preposição antes do relativo** e a regência que gera **crase**."),
    h2("1. Verbos"),
    tb(["Verbo", "Regência"], [0.24, 0.76], [
        ("assistir", "**a** = ver · OD = ajudar · **a** alguém = caber direito"),
        ("aspirar", "OD = inspirar · **a** = desejar"),
        ("visar", "OD = mirar, pôr visto · **a** = pretender"),
        ("obedecer", "**a**"),
        ("preferir", "algo **a** algo (sem *mais*, sem *do que*)"),
        ("chegar, ir", "**a** (não *em*)"),
        ("implicar", "OD = acarretar (sem *em*)"),
        ("proceder", "**a** = realizar"),
        ("pagar, perdoar", "coisa OD; pessoa **a**"),
        ("informar, avisar", "alguém **de** algo / algo **a** alguém"),
        ("esquecer, lembrar", "OD; ou *esquecer-se de, lembrar-se de*"),
        ("namorar", "OD (sem *com*)"),
        ("simpatizar", "**com** (não pronominal)"),
        ("residir, morar", "**em**"),
    ]),
    h2("2. Nominal"),
    bl("**a**: favorável, contrário, acessível, obediente, preferível, relativo.",
       "**com**: compatível, solidário. **em**: residente, situado. **de**: suspeito, capaz, digno."),
    h2("3. Relativos"),
    bl("A preposição do verbo vai para **antes do relativo**: *o cargo **a que** aspiro; os documentos **de que** preciso; a pessoa **em quem** confio*.",
       "Verbos com regências diferentes não dividem o mesmo complemento: *Entrou **na** sala e saiu **dela**.*"),
]

SUMMARY = [
    h2("Quadro: certo × errado"),
    tb(["Evite", "Prefira"], [0.5, 0.5], [
        ("Assisti o jogo.", "Assisti ao jogo."),
        ("Aspiro o cargo.", "Aspiro ao cargo."),
        ("Prefiro mais isto do que aquilo.", "Prefiro isto àquilo."),
        ("Cheguei em casa / no local.", "Cheguei a casa / ao local."),
        ("Isso implica em custos.", "Isso implica custos."),
        ("Esqueci do prazo.", "Esqueci o prazo / Esqueci-me do prazo."),
        ("Paguei o advogado.", "Paguei ao advogado."),
        ("O livro que gosto.", "O livro de que gosto."),
        ("Namora com a colega.", "Namora a colega."),
        ("Reside à Rua X.", "Reside na Rua X."),
    ]),
    h2("Leve para a prova"),
    bl("Assistir **a** = ver; assistir alguém = ajudar.",
       "Aspirar **a** = desejar.",
       "Preferir X **a** Y.",
       "Implicar (acarretar) é direto.",
       "Verbo de movimento: **a**.",
       "Pagar e perdoar: **a** pessoa.",
       "Esquecer sem *me*, sem *de*.",
       "Preposição sobe para antes do **que** relativo.",
       "Sem preposição exigida, **não há crase**.",
       "Dois verbos, duas regências: repita o complemento."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "REGÊNCIA", "rootSub": "verbal e nominal",
    "left": [
        {"label": "Assistir", "items": ["ao jogo: ver", "o ferido: ajudar", "ao réu o direito"]},
        {"label": "Aspirar e visar", "items": ["aspirar o ar", "aspirar ao cargo", "visar ao bem comum"]},
        {"label": "Preferir", "items": ["X a Y", "sem mais", "sem do que"]},
        {"label": "Movimento", "items": ["chegar a", "ir a", "voltar a"]},
        {"label": "Implicar e proceder", "items": ["implica custos", "procedeu à oitiva", "a denúncia procede"]},
    ],
    "right": [
        {"label": "Pessoa com a", "items": ["pagar ao credor", "perdoar ao réu", "obedecer ao chefe"]},
        {"label": "Pronominais", "items": ["esquecer-se de", "lembrar-se de", "simpatizar com (não se)"]},
        {"label": "Nominal", "items": ["favorável a", "compatível com", "residente em"]},
        {"label": "Relativos", "items": ["a que aspiro", "de que preciso", "em quem confio"]},
        {"label": "Pegadinhas", "items": ["entrou na sala e saiu dela", "namorar sem com", "reside na rua"]},
    ],
}

QUIZ = quiz([
    ("C", "Em “Milhares de pessoas assistiram ao jogo”, a regência verbal está de acordo com a norma-padrão.",
     "Assistir no sentido de ver exige a preposição a."),
    ("E", "Em “Ele visa o cargo de perito há anos”, no sentido de almejar, a regência recomendada pela norma-padrão foi observada.",
     "No sentido de pretender, recomenda-se a preposição a: visa ao cargo."),
    ("C", "Em “Todos devem obedecer ao regulamento”, a regência verbal está correta.",
     "Obedecer é transitivo indireto e rege a preposição a."),
    ("E", "A frase “Vou no banco depois do expediente” segue a regência prescrita pela norma-padrão.",
     "Ir rege a preposição a: vou ao banco."),
    ("C", "Em “Prefiro a verdade à mentira”, a regência de preferir está correta.",
     "Preferir algo a algo; a preposição se funde com o artigo a."),
    ("E", "A frase “Lembrei do compromisso na última hora” segue a norma-padrão estrita.",
     "Lembrar é transitivo direto (lembrei o compromisso) ou pronominal (lembrei-me do compromisso)."),
    ("C", "Em “Agradeci ao colega a ajuda na operação”, a regência de agradecer está correta.",
     "Agradecer algo a alguém."),
    ("E", "A frase “Ele namora com a colega de turma” segue a norma-padrão.",
     "Namorar é transitivo direto: ele namora a colega."),
    ("C", "Em “Este é o cargo a que aspiro”, a preposição antes do relativo é exigida pela regência de aspirar.",
     "Aspirar a no sentido de desejar."),
    ("E", "Em “Esta é a lei que me referi na reunião”, a regência está de acordo com a norma-padrão.",
     "Referir-se a: a lei a que me referi."),
], 10)

SOURCES = [GRAM, SRC_R]
