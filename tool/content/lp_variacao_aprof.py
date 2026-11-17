# -*- coding: utf-8 -*-
"""Língua Portuguesa · Variação linguística — MATERIAL APROFUNDADO (estudo inicial)."""
from common import *

MATERIAL = material(
    "lp-variacao-02", "LP", "LP-24", "aprofundado", "Variação linguística", "Língua Portuguesa · Linguagem",
    "portugues_variacao_aprofundado", "Portugues_Variacao_Linguistica_APROFUNDADO.pdf", None, ["Variação", "linguística"],
    ["Teoria completa para o primeiro estudo: tipos de variação, norma-padrão, adequação", "e preconceito linguístico, com 20 questões no estilo das bancas."],
    [("01", "Tipos", "regional, social, situacional e histórica"),
     ("02", "Normas", "norma-padrão, norma culta e variedades populares"),
     ("03", "Adequação", "certo × adequado; níveis de formalidade"),
     ("04", "Preconceito linguístico", "o que as bancas esperam que você saiba"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Variação linguística (Língua Portuguesa)",
    "Base: gramáticas de referência e Bagno, Preconceito linguístico.", 90)

THEORY = [
    exam("Como estudar este material",
         "Tópico curto e conceitual. As bancas cobram o **tipo** de variação presente num trecho (regional, social, situacional, histórica), "
         "a ideia de **adequação** ao contexto e a postura contra o **preconceito linguístico**. A gramática normativa continua sendo a "
         "referência para a escrita formal e para a prova."),

    h2("1. A língua varia"),
    p("Toda língua muda no tempo e varia entre regiões, grupos sociais e situações de uso. Essas diferenças são **variedades linguísticas**, "
      "todas com regras próprias e capazes de comunicar. A variação é natural e não é sinônimo de erro."),

    h2("2. Tipos de variação"),
    tb(["Tipo", "Depende de", "Exemplos"], [0.26, 0.3, 0.44], [
        ("Diatópica (regional, geográfica)", "Região", "*mandioca / aipim / macaxeira*; *tu vais* no Sul; sotaques"),
        ("Diastrática (social)", "Grupo social: escolaridade, idade, profissão, classe", "gírias de jovens; jargão policial (*meliante, guarnição, QTH*); *nós vai* em variedades populares"),
        ("Diafásica (situacional, estilística)", "Situação de comunicação: formal ou informal", "*Prezado senhor* × *E aí, beleza?*"),
        ("Diacrônica (histórica)", "Época", "*vossa mercê* › *vosmecê* › *você* › *cê*; *pharmacia* › *farmácia*"),
        ("Diamésica", "Meio: fala ou escrita", "*Tá* na fala × *está* na escrita formal"),
    ]),
    bl("**Gíria**: vocabulário de um grupo social, muitas vezes passageiro.",
       "**Jargão**: vocabulário técnico de uma profissão (*flagrante, oitiva, auto de prisão*).",
       "**Regionalismo**: palavra ou construção típica de uma região."),

    h2("3. Norma-padrão, norma culta e variedades populares"),
    bl("**Norma-padrão**: modelo idealizado, descrito nas gramáticas normativas; é a referência para documentos oficiais, provas e textos formais.",
       "**Norma culta**: variedade efetivamente usada por falantes escolarizados em situações formais (é mais flexível que a norma-padrão).",
       "**Variedades populares**: usadas por grande parte da população no dia a dia, com regras próprias (*os menino*, *nós vai*)."),

    h2("4. Adequação × correção"),
    p("A noção de **adequação** substitui a ideia simples de *certo e errado* quando se fala de **uso**: a variedade deve combinar com a situação. "
      "Um ofício exige a norma-padrão; uma conversa entre amigos admite a linguagem informal. Usar linguagem formal demais numa conversa "
      "também é inadequação."),
    key("E na prova?",
        "As questões de gramática continuam julgando a **norma-padrão**. As de variação perguntam se a linguagem é **adequada** ao contexto "
        "e qual o **tipo** de variação. As duas visões convivem."),

    h2("5. Preconceito linguístico"),
    p("É a discriminação de pessoas pelo modo como falam (sotaque, variedade popular, regionalismo). As bancas costumam adotar a visão da "
      "sociolinguística: **não existe variedade inferior**; existe variedade **adequada ou inadequada** a cada situação."),

    h2("6. Como as bancas cobram"),
    bl("“No trecho, há marcas de variação regional / social / informal.”",
       "“O emprego de *tá* e *pra* indica registro informal, típico da oralidade.”",
       "“A linguagem empregada é adequada ao gênero e à situação.”",
       "“Variedades populares devem ser consideradas erradas” — afirmação que as bancas tratam como preconceituosa."),
]

QUIZ = quiz([
    ("C", "As diferenças entre mandioca, aipim e macaxeira exemplificam variação regional (diatópica).",
     "A mesma raiz recebe nomes diferentes conforme a região."),
    ("E", "A variação diacrônica está relacionada às diferenças entre grupos sociais.",
     "Diacrônica é a variação ao longo do tempo; a social é diastrática."),
    ("C", "O uso de termos técnicos próprios da atividade policial, como oitiva e flagrante, é exemplo de jargão profissional.",
     "Jargão é o vocabulário técnico de um grupo profissional."),
    ("E", "A variação linguística deve ser entendida como sinônimo de erro gramatical.",
     "Variação é fenômeno natural de toda língua."),
    ("C", "A escolha entre “Prezado senhor” e “E aí, beleza?” exemplifica variação situacional (diafásica).",
     "Depende do grau de formalidade da situação."),
    ("E", "A evolução de vossa mercê para você exemplifica variação regional.",
     "É mudança ao longo do tempo: variação histórica (diacrônica)."),
    ("C", "A norma-padrão é a referência para a redação de documentos oficiais.",
     "Textos formais e oficiais seguem a norma-padrão."),
    ("E", "Norma culta e norma-padrão são exatamente a mesma coisa.",
     "A norma-padrão é um modelo idealizado; a culta é o uso real de falantes escolarizados."),
    ("C", "Gírias são marcas de variação social, associadas a grupos específicos.",
     "Identificam grupos, como jovens ou profissões."),
    ("E", "Empregar linguagem formal em qualquer situação de comunicação é sempre o mais adequado.",
     "Adequação depende do contexto; formalidade excessiva numa conversa informal também é inadequada."),

    ("C", "Em um bilhete entre amigos, a forma “Tô chegando, me espera aí” é adequada à situação, embora não siga a norma-padrão.",
     "O registro informal é adequado ao contexto."),
    ("E", "Em um ofício, a forma “Tô encaminhando os documentos pro senhor” é adequada, pois a comunicação foi compreendida.",
     "O ofício exige a norma-padrão: estou encaminhando os documentos ao senhor."),
    ("C", "O preconceito linguístico consiste em discriminar pessoas pelo modo como falam.",
     "Sotaques e variedades populares são alvos comuns."),
    ("E", "Segundo a sociolinguística, as variedades populares são inferiores por não terem regras.",
     "Toda variedade tem regras próprias; nenhuma é inferior."),
    ("C", "O emprego de “tu vais” em algumas regiões do Sul do Brasil é exemplo de variação regional.",
     "O uso do pronome tu varia conforme a região."),
    ("E", "A diferença entre a fala e a escrita não constitui variação linguística.",
     "É a variação diamésica: fala e escrita têm características próprias."),
    ("C", "A mudança da grafia pharmacia para farmácia exemplifica variação histórica.",
     "Reflete mudança ao longo do tempo (e nas normas ortográficas)."),
    ("E", "Regionalismos são palavras de uso exclusivo de grupos profissionais.",
     "Regionalismo é típico de uma região; o de grupo profissional é jargão."),
    ("C", "Em questões de gramática, a referência de correção continua sendo a norma-padrão.",
     "A prova julga a norma-padrão; a variação é avaliada pela adequação."),
    ("E", "O uso de “a gente” no lugar de “nós” só ocorre em variedades populares.",
     "A gente é amplamente usado por falantes de todas as classes, sobretudo na fala."),
], 20)

SOURCES = [GRAM, "Marcos Bagno, Preconceito linguístico.", SRC_A]
