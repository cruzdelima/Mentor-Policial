# -*- coding: utf-8 -*-
"""Língua Portuguesa · Concordância nominal e verbal — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "lp-concordancia-01", "LP", "LP-11", "resumo", "Concordância nominal e verbal", "Língua Portuguesa · Sintaxe",
    "portugues_concordancia", "Portugues_Concordancia_RESUMO.pdf", None, ["Concordância", "nominal e verbal"], RES_SUB,
    RES_ITEMS("regra geral, casos especiais e palavras-armadilha"),
    "Tópico do edital: Concordância nominal e verbal (Língua Portuguesa)",
    "Base: gramáticas de referência (Bechara; Cunha e Cintra).", 40)

THEORY = [
    exam("O que a banca cobra",
         "**Sujeito posposto**, **verbos impessoais**, **pronome se** e **palavras variáveis** (anexo, mesmo, obrigado). Ache o sujeito antes de julgar o verbo."),
    h2("1. Verbal"),
    bl("Verbo concorda com o **núcleo** do sujeito, mesmo posposto: *Faltam dois documentos*.",
       "Sujeito composto **anteposto**: plural. **Posposto**: plural ou com o mais próximo.",
       "*Ou* excludente: singular. *Nem… nem*: plural. Resumido por *tudo*: singular.",
       "Coletivo: singular; coletivo + especificador plural: singular ou plural (*a maioria dos agentes aprovou/aprovaram*).",
       "**Mais de um**: singular. **Mais de / cerca de + número**: concorda com o número.",
       "**Que** relativo: com o antecedente (*fui eu que fiz*). **Quem**: 3ª pessoa ou antecedente.",
       "**Um dos que**: plural."),
    h2("2. Impessoais e o se"),
    bl("**Haver** (existir, tempo) e **fazer** (tempo): singular, inclusive o auxiliar.",
       "**Existir, ocorrer**: concordam com o sujeito.",
       "**VTD + se**: concorda (*vendem-se casas*). **VTI + se**: singular (*precisa-se de*)."),
    h2("3. Ser"),
    bl("Com *tudo, isso* + predicativo plural: *Tudo são flores*.",
       "Horas e datas: com o numeral — *São duas horas. É meio-dia. É uma hora.*"),
    h2("4. Nominal"),
    bl("Adjetivo **posposto** a vários substantivos: plural ou com o mais próximo. **Anteposto**: com o mais próximo.",
       "**Variam**: anexo, incluso, obrigado, mesmo, próprio, quite. **Não variam**: menos, em anexo, alerta.",
       "**Meio, bastante** junto de adjetivo: invariáveis. **Só** = sozinho varia.",
       "**É proibido / é necessário**: sem artigo, invariável; com artigo, concorda."),
]

SUMMARY = [
    h2("Quadro: certo × errado"),
    tb(["Evite", "Prefira", "Por quê"], [0.32, 0.32, 0.36], [
        ("Deve existir provas.", "Devem existir provas.", "Existir tem sujeito"),
        ("Haviam provas.", "Havia provas.", "Haver = existir"),
        ("Vende-se casas.", "Vendem-se casas.", "Passiva sintética"),
        ("Precisam-se de agentes.", "Precisa-se de agentes.", "VTI + se"),
        ("Faltou três agentes.", "Faltaram três agentes.", "Sujeito posposto"),
        ("Mais de um foram presos.", "Mais de um foi preso.", "Mais de um: singular"),
        ("Segue anexo as fotos.", "Seguem anexas as fotos.", "Anexo varia"),
        ("Muito obrigado (mulher).", "Muito obrigada.", "Concorda com quem fala"),
        ("Menas provas.", "Menos provas.", "Menos não varia"),
        ("Meia nervosa.", "Meio nervosa.", "Advérbio não varia"),
    ]),
    h2("Leve para a prova"),
    bl("Pergunte ao verbo: **quem / o que** faz?",
       "Sujeito posposto continua sendo sujeito.",
       "Núcleo do sujeito longo: ignore os adjuntos.",
       "Haver e fazer impessoais: **singular**.",
       "VTD + se: **plural** se o sujeito for plural.",
       "Mais de + número: com o **número**.",
       "Que relativo: com o **antecedente**.",
       "Adjetivo depois de vários nomes: plural ou o mais próximo.",
       "Anexo, mesmo, obrigado: **variam**.",
       "Menos e em anexo: **nunca** variam."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "CONCORDÂNCIA", "rootSub": "verbal e nominal",
    "left": [
        {"label": "Regra geral", "items": ["verbo com o núcleo", "sujeito posposto conta", "ache o sujeito primeiro"]},
        {"label": "Sujeito composto", "items": ["antes: plural", "depois: plural ou próximo", "ou excludente: singular"]},
        {"label": "Expressões", "items": ["mais de um: singular", "mais de dez: plural", "um dos que: plural"]},
        {"label": "Relativos", "items": ["fui eu que fiz", "fui eu quem fez/fiz", "coletivo + de: livre"]},
        {"label": "Ser", "items": ["tudo são flores", "são duas horas", "é meio-dia"]},
    ],
    "right": [
        {"label": "Impessoais", "items": ["havia provas", "faz dois anos", "deve haver"]},
        {"label": "Pronome se", "items": ["vendem-se casas", "precisa-se de", "trata-se de"]},
        {"label": "Nominal", "items": ["depois: plural ou próximo", "antes: o mais próximo", "masculino prevalece"]},
        {"label": "Variam", "items": ["anexo, incluso", "obrigado, mesmo", "próprio, quite"]},
        {"label": "Não variam", "items": ["menos, em anexo", "meio nervosa", "é proibido entrada"]},
    ],
}

QUIZ = quiz([
    ("C", "Em “Existem falhas graves no sistema”, a concordância verbal está de acordo com a norma-padrão.",
     "Existir é pessoal e concorda com o sujeito falhas graves."),
    ("E", "Em “Existe falhas graves no sistema”, a concordância verbal está de acordo com a norma-padrão.",
     "O sujeito plural exige o verbo no plural: existem."),
    ("C", "Em “Apreenderam-se várias armas”, o verbo no plural concorda com o sujeito várias armas.",
     "Apreender é transitivo direto; há passiva sintética."),
    ("E", "Em “Havia bastante candidatos inscritos”, a concordância nominal está de acordo com a norma-padrão.",
     "Junto de substantivo, bastante é pronome e varia: bastantes candidatos."),
    ("C", "Em “Elas mesmas redigiram o relatório”, o emprego de mesmas está de acordo com a norma-padrão.",
     "Mesmo, com valor de próprio, concorda com o termo a que se refere."),
    ("E", "Em “Segue anexa as fotografias do local”, a concordância está de acordo com a norma-padrão.",
     "O sujeito é as fotografias: seguem anexas as fotografias."),
    ("C", "Em “É proibida a entrada de pessoas armadas”, a concordância nominal está correta.",
     "Com o artigo a, a expressão concorda com o substantivo entrada."),
    ("E", "Em “Faltou três agentes ao plantão”, a concordância verbal está de acordo com a norma-padrão.",
     "O sujeito posposto três agentes exige o plural: faltaram."),
    ("C", "Em “A audiência começou ao meio-dia e meia”, a concordância de meia está correta.",
     "Meia refere-se a meia hora: meio-dia e meia."),
    ("E", "Em “Um ou outro agente faltaram ao treinamento”, a concordância está de acordo com a norma-padrão.",
     "Com um ou outro, o verbo fica no singular: faltou."),
], 10)

SOURCES = [GRAM, SRC_R]
