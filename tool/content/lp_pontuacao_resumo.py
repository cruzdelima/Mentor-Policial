# -*- coding: utf-8 -*-
"""Língua Portuguesa · Pontuação — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "lp-pontuacao-01", "LP", "LP-14", "resumo", "Pontuação", "Língua Portuguesa · Sintaxe",
    "portugues_pontuacao", "Portugues_Pontuacao_RESUMO.pdf", None, ["Pontuação:", "vírgula e outros sinais"], RES_SUB,
    RES_ITEMS("vírgula proibida e obrigatória, orações e demais sinais"),
    "Tópico do edital: Emprego dos sinais de pontuação (Língua Portuguesa)",
    "Base: gramáticas de referência (Bechara; Cunha e Cintra).", 35)

THEORY = [
    exam("O que a banca cobra",
         "**Inserção ou supressão** de vírgula (correção e sentido) e **troca de sinais** (vírgula, travessão, parênteses, ponto e vírgula)."),
    h2("1. Vírgula proibida"),
    bl("Sujeito | verbo · verbo | complemento · nome | complemento — na ordem direta, **nunca**.",
       "Principal | oração substantiva: *É necessário que…* (sem vírgula)."),
    h2("2. Vírgula obrigatória"),
    bl("Enumeração, **aposto explicativo**, **vocativo**, expressões explicativas (*isto é, ou seja*).",
       "Conjunção **deslocada** (*O laudo, porém, …*). Local em datas. **Elipse** do verbo (*ela, dos depoimentos*).",
       "Adjetiva **explicativa** entre vírgulas; **restritiva** sem vírgulas."),
    h2("3. Vírgula facultativa ou recomendada"),
    bl("Adjunto adverbial **curto** deslocado: facultativa. **Longo**: recomendada.",
       "Adverbial **anteposta**: recomendada; **posposta**: facultativa.",
       "Antes de **e** com sujeitos diferentes: admitida."),
    h2("4. Outros sinais"),
    bl("**Ponto e vírgula**: orações coordenadas longas, itens de lista, antes de conjunção deslocada.",
       "**Dois-pontos**: enumeração, citação, explicação, consequência.",
       "**Travessões duplos** e **parênteses**: isolam intercalações (como vírgulas).",
       "**Aspas**: citação, ironia, estrangeirismo."),
]

SUMMARY = [
    h2("Quadro: troca de sinais"),
    tb(["Troca", "Resultado"], [0.6, 0.4], [
        ("Vírgulas › travessões duplos (intercalação)", "Mantém"),
        ("Vírgulas › parênteses (informação acessória)", "Mantém"),
        ("Ponto e vírgula › ponto (orações independentes)", "Mantém (com maiúscula)"),
        ("Ponto e vírgula › dois-pontos", "Altera"),
        ("Retirar vírgulas da adjetiva explicativa", "Altera o sentido"),
        ("Inserir vírgula entre sujeito e verbo", "Erro"),
        ("Retirar vírgula do vocativo", "Erro"),
        ("Retirar vírgula do adjunto curto anteposto", "Mantém"),
    ]),
    h2("Leve para a prova"),
    bl("Sujeito e verbo: **nunca** vírgula.",
       "Sujeito terminado em oração restritiva também **não** leva vírgula antes do verbo.",
       "Explicativa: vírgulas; restritiva: sem.",
       "Retirar vírgulas da explicativa: **muda o sentido**.",
       "Vocativo e aposto explicativo: **sempre** isolados.",
       "Conjunção deslocada: **entre vírgulas**.",
       "Vírgula de elipse: **obrigatória**.",
       "Adjunto curto anteposto: **facultativa**.",
       "Travessões = vírgulas = parênteses (intercalação).",
       "Dois-pontos anunciam; ponto e vírgula separa."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "PONTUAÇÃO", "rootSub": "vírgula e outros sinais",
    "left": [
        {"label": "Proibida", "items": ["sujeito | verbo", "verbo | complemento", "principal | substantiva"]},
        {"label": "Obrigatória", "items": ["vocativo", "aposto explicativo", "enumeração"]},
        {"label": "Intercalações", "items": ["isto é, ou seja", "conjunção deslocada", "elipse do verbo"]},
        {"label": "Adjetivas", "items": ["explicativa: com vírgulas", "restritiva: sem vírgulas", "muda o sentido"]},
        {"label": "Adverbiais", "items": ["anteposta: vírgula", "posposta: facultativa", "adjunto curto: facultativa"]},
    ],
    "right": [
        {"label": "Coordenadas", "items": ["assindéticas: vírgula", "antes de mas", "e + sujeitos diferentes"]},
        {"label": "Ponto e vírgula", "items": ["orações longas", "itens de lista", "antes de porém deslocado"]},
        {"label": "Dois-pontos", "items": ["enumeração", "citação", "explicação"]},
        {"label": "Travessão e parênteses", "items": ["equivalem a vírgulas", "destaque", "informação acessória"]},
        {"label": "Aspas", "items": ["citação", "ironia", "estrangeirismo"]},
    ],
}

QUIZ = quiz([
    ("C", "A vírgula não deve separar o sujeito do verbo, mesmo quando o sujeito é extenso.",
     "Na ordem direta, sujeito e verbo não se separam por vírgula."),
    ("E", "O período “O policial, prendeu o suspeito em flagrante” está corretamente pontuado.",
     "A vírgula separa indevidamente o sujeito do verbo."),
    ("C", "Em “Soldado, apresente-se”, a vírgula isola o vocativo.",
     "Soldado chama o interlocutor."),
    ("E", "O período “Os documentos que estavam no cofre, desapareceram” está corretamente pontuado.",
     "A vírgula separa o sujeito, que termina na oração restritiva, do verbo."),
    ("C", "O aposto explicativo deve ser isolado por vírgulas, travessões ou parênteses.",
     "São sinais equivalentes para isolar o termo intercalado."),
    ("E", "Inserir vírgulas em uma oração adjetiva restritiva mantém o sentido do período.",
     "A restritiva passa a explicativa e o sentido muda."),
    ("C", "Em “O inquérito, contudo, foi arquivado”, as vírgulas que isolam contudo são obrigatórias.",
     "Conjunção deslocada fica entre vírgulas."),
    ("E", "O ponto e vírgula é empregado exclusivamente para separar itens de enumeração.",
     "Também separa orações coordenadas, sobretudo longas ou com vírgulas internas."),
    ("C", "Travessões duplos podem isolar uma oração intercalada, como fariam as vírgulas.",
     "Os dois sinais têm a mesma função nesse caso."),
    ("E", "Os dois-pontos são empregados apenas antes de citações.",
     "Também anunciam enumeração, explicação, síntese e consequência."),
], 10)

SOURCES = [GRAM, SRC_R]
