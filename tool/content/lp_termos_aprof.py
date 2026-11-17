# -*- coding: utf-8 -*-
"""Língua Portuguesa · Análise sintática: termos da oração — MATERIAL APROFUNDADO (estudo inicial)."""
from common import *

MATERIAL = material(
    "lp-termos-02", "LP", "LP-08", "aprofundado", "Análise sintática: termos da oração", "Língua Portuguesa · Sintaxe",
    "portugues_termos_aprofundado", "Portugues_Termos_da_Oracao_APROFUNDADO.pdf", None, ["Termos", "da oração"],
    ["Teoria completa para o primeiro estudo: sujeito, predicado, complementos,", "adjuntos, aposto e vocativo, com 20 questões no estilo Cebraspe."],
    [("01", "Essenciais", "tipos de sujeito, oração sem sujeito e predicado"),
     ("02", "Integrantes", "objetos, complemento nominal e agente da passiva"),
     ("03", "Acessórios", "adjuntos, aposto e vocativo"),
     ("04", "Distinções", "CN × adjunto, predicativo × adjunto, vírgula e sujeito"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Sintaxe da oração — termos da oração (Língua Portuguesa)",
    "Base: gramáticas de referência e Nomenclatura Gramatical Brasileira (NGB).", 240)

THEORY = [
    exam("Como estudar este material",
         "Sintaxe é a base de **concordância, regência, crase e pontuação**. O Cebraspe pergunta diretamente “o termo X exerce a função de…”, "
         "mas também cobra sintaxe de forma indireta: “a inserção de vírgula após X prejudicaria a correção” (porque separaria sujeito e verbo). "
         "Comece sempre pelo **verbo**: ache o verbo, pergunte quem pratica a ação (sujeito) e o que o verbo exige (complementos)."),

    h2("1. Frase, oração e período"),
    bl("**Frase**: enunciado com sentido completo, com ou sem verbo — *Silêncio! Que operação!*",
       "**Oração**: enunciado organizado em torno de um **verbo** (ou locução verbal).",
       "**Período**: frase formada por uma ou mais orações. **Simples** (uma oração) ou **composto** (duas ou mais).",
       "Regra prática: **número de orações = número de verbos** (locução verbal conta como um só)."),

    h2("2. Termos essenciais: sujeito e predicado"),
    h3("Tipos de sujeito"),
    tb(["Tipo", "Como reconhecer", "Exemplo"], [0.2, 0.42, 0.38], [
        ("Simples", "Um núcleo", "**Os agentes** chegaram."),
        ("Composto", "Dois ou mais núcleos", "**O delegado e o escrivão** chegaram."),
        ("Oculto (desinencial, elíptico)", "Não aparece, mas é identificado pela desinência ou pelo contexto", "**Chegamos** cedo. (nós)"),
        ("Indeterminado", "Existe, mas não se quer ou não se pode identificar", "**Assaltaram** a agência. **Precisa-se** de agentes."),
        ("Oração sem sujeito", "Verbo impessoal: não há sujeito", "**Houve** ocorrências. **Choveu**. **Faz** dois anos."),
    ]),
    key("Sujeito indeterminado: duas formas",
        "1) **Verbo na 3ª pessoa do plural sem referente** no texto: *Roubaram a viatura.* "
        "2) **Verbo transitivo indireto, intransitivo ou de ligação + se**: *Precisa-se de peritos. Vive-se bem aqui. Era-se feliz.* "
        "Se o verbo na 3ª do plural retoma alguém já citado (*Os presos fugiram. Roubaram a viatura*), o sujeito é **oculto**, não indeterminado."),
    h3("Orações sem sujeito (verbos impessoais)"),
    bl("**Haver** no sentido de existir, acontecer ou de tempo decorrido: *Havia provas. Houve tumulto. Há dois anos.*",
       "**Fazer**, **estar**, **ser** indicando tempo ou clima: *Faz frio. Está tarde. É uma hora. São dez horas.*",
       "**Fenômenos da natureza**: *Chovia. Ventou muito. Anoiteceu.*",
       "Atenção: **existir** não é impessoal. *Existiam provas* (sujeito: provas)."),
    h3("Sujeito posposto"),
    p("O sujeito pode vir **depois do verbo** — e é aí que mora o erro de concordância: *Chegaram **os laudos da perícia**. "
      "Faltam **dois documentos**. Ocorreram **várias prisões**.* Pergunte ao verbo: *o que chegou? o que falta?*"),

    h3("Tipos de predicado"),
    tb(["Predicado", "Núcleo", "Exemplo"], [0.22, 0.38, 0.4], [
        ("Verbal", "Um **verbo** significativo (ação)", "O agente **prendeu** o suspeito."),
        ("Nominal", "Um **nome** (predicativo), com verbo de ligação", "O delegado **ficou preocupado**."),
        ("Verbo-nominal", "Um verbo significativo **e** um predicativo", "Os agentes **chegaram cansados**."),
    ]),
    bl("**Verbos de ligação** (ligam sujeito a uma característica): *ser, estar, permanecer, ficar, parecer, continuar, andar, tornar-se, virar*.",
       "O mesmo verbo pode ser de ligação ou significativo: *Ele **anda** nervoso* (ligação) × *Ele **anda** pela rua* (intransitivo)."),
    h3("Predicativo do sujeito e do objeto"),
    bl("**Do sujeito**: característica atribuída ao sujeito — *O suspeito **parecia nervoso**. Os agentes chegaram **cansados**.*",
       "**Do objeto**: característica atribuída ao objeto — *O juiz considerou o réu **culpado**. Elegeram-no **presidente**.*",
       "Verbos que costumam pedir predicativo do objeto: *considerar, julgar, achar, eleger, nomear, chamar, tornar, deixar*."),

    h2("3. Transitividade e termos integrantes"),
    tb(["Verbo", "Exige", "Exemplo"], [0.26, 0.32, 0.42], [
        ("Intransitivo (VI)", "Nada; sentido completo", "O suspeito **fugiu**."),
        ("Transitivo direto (VTD)", "Objeto **sem** preposição", "Prendeu **o suspeito**."),
        ("Transitivo indireto (VTI)", "Objeto **com** preposição", "Obedeceu **às ordens**."),
        ("Transitivo direto e indireto (VTDI)", "Os dois objetos", "Entregou **o relatório** **ao juiz**."),
        ("De ligação (VL)", "Predicativo", "Ficou **calmo**."),
    ]),
    bl("**Objeto direto preposicionado**: complemento de VTD que, por ênfase ou clareza, recebe preposição — *Amar **a Deus**. Feriu **a si** mesmo.*",
       "**Objeto direto e indireto pleonásticos**: repetidos por pronome — *O relatório, entreguei-**o** ontem.*",
       "**Complemento nominal (CN)**: completa o sentido de um **nome** (substantivo abstrato, adjetivo ou advérbio), sempre com preposição — "
       "*obediência **às leis**; favorável **ao réu**; relativamente **ao caso***.",
       "**Agente da passiva**: quem pratica a ação na voz passiva, introduzido por *por* (*pelo*) ou *de* — *O inquérito foi instaurado **pelo delegado**.*"),

    h2("4. Termos acessórios"),
    bl("**Adjunto adnominal**: caracteriza ou determina um substantivo, sem ser exigido por ele — artigos, adjetivos, pronomes adjetivos, numerais e "
       "locuções adjetivas: ***Os** **dois** agentes **experientes** **da equipe**.*",
       "**Adjunto adverbial**: circunstância ligada ao verbo, adjetivo ou advérbio — tempo, lugar, modo, causa, intensidade, instrumento, companhia — "
       "*Ontem, a equipe cumpriu o mandado **no bairro** **com cautela**.*",
       "**Aposto**: termo que explica, enumera, resume ou especifica outro termo — *Carlos, **o escrivão da equipe**, lavrou o termo.*"),
    tb(["Aposto", "Exemplo"], [0.24, 0.76], [
        ("Explicativo (entre vírgulas)", "Recife, **capital de Pernambuco**, sediou a operação."),
        ("Enumerativo", "Apreenderam três itens: **armas, drogas e dinheiro**."),
        ("Resumitivo", "Armas, drogas, dinheiro, **tudo** foi apreendido."),
        ("Especificativo (sem vírgula)", "o delegado **Paulo**; a cidade **de Recife**; o rio **Capibaribe**"),
    ]),
    bl("**Vocativo**: termo usado para **chamar** o interlocutor. Não pertence à estrutura da oração e vem sempre **isolado por vírgula** — "
       "***Senhor delegado**, o relatório está pronto. Apresente-se, **soldado**.*"),

    h2("5. As distinções que mais caem"),
    h3("Complemento nominal × adjunto adnominal"),
    p("Os dois podem ser locuções com *de*. O teste é o **papel** do termo em relação ao substantivo abstrato:"),
    tb(["", "Complemento nominal", "Adjunto adnominal"], [0.22, 0.39, 0.39], [
        ("Papel", "**Paciente / alvo** da ação (sofre)", "**Agente** (pratica), posse, matéria, característica"),
        ("Exemplo", "*a investigação **da fraude*** (a fraude é investigada)", "*a chegada **dos agentes*** (os agentes chegam)"),
        ("Exemplo", "*o medo **de represálias***", "*a mesa **de madeira***; *a viatura **do batalhão***"),
        ("Com adjetivo ou advérbio", "Sempre CN: *útil **ao processo***", "—"),
    ]),
    trap("Ambiguidade clássica",
         "*A crítica **do professor*** pode ser adjunto (o professor critica) ou CN (o professor é criticado). "
         "Em prova, o contexto decide; quando não decide, a banca aceita a ambiguidade."),
    h3("Predicativo × adjunto adnominal"),
    p("*Encontrei o preso **nervoso*** (estado no momento: **predicativo do objeto**) × *Encontrei o preso **nervoso** que fugiu ontem* "
      "(característica que identifica: **adjunto adnominal**). Teste: troque o objeto por pronome — *Encontrei-o nervoso*: se o termo continua, é predicativo."),
    h3("Objeto indireto × adjunto adverbial"),
    p("*Entreguei o ofício **ao comandante*** (exigido pelo verbo: OI) × *Trabalhei **no batalhão*** (circunstância de lugar: adjunto adverbial)."),
    h3("Sintaxe e vírgula"),
    bl("**Não se separa por vírgula** o sujeito do verbo, nem o verbo de seus complementos — mesmo que o sujeito seja longo.",
       "**Adjunto adverbial deslocado** (no início ou no meio) pode ser isolado por vírgulas; se for curto, a vírgula é facultativa.",
       "**Aposto explicativo** e **vocativo** vêm isolados por vírgulas."),

    h2("6. Como o Cebraspe cobra"),
    bl("“O termo X exerce a função de sujeito / complemento de Y / adjunto”.",
       "“A inserção de vírgula após X prejudicaria a correção” — verifique se separaria sujeito e verbo.",
       "Concordância com **sujeito posposto** e com **haver** impessoal.",
       "“O sujeito da oração é indeterminado” — confira se há referente no texto (aí seria oculto).",
       "Complemento nominal × adjunto adnominal em expressões com *de*."),
]

QUIZ = quiz([
    ("C", "Em “Chegaram os laudos da perícia”, o sujeito é os laudos da perícia, posposto ao verbo.",
     "O que chegou? Os laudos da perícia: sujeito simples posposto, que leva o verbo ao plural."),
    ("E", "Em “Houve muitas ocorrências no feriado”, o termo muitas ocorrências exerce a função de sujeito.",
     "Haver no sentido de acontecer é impessoal: a oração não tem sujeito, e muitas ocorrências é objeto direto."),
    ("C", "A oração “Choveu durante toda a operação” não tem sujeito.",
     "Verbos que indicam fenômenos da natureza são impessoais."),
    ("E", "Em “Precisa-se de peritos”, o termo peritos é o sujeito da oração.",
     "Precisar de é transitivo indireto: o se indetermina o sujeito, e de peritos é objeto indireto."),
    ("C", "Em “O delegado ficou preocupado”, o termo preocupado é predicativo do sujeito.",
     "Ficar é verbo de ligação; preocupado é característica atribuída ao sujeito."),
    ("E", "Em “Os agentes chegaram cansados”, o predicado é verbal.",
     "Há verbo significativo (chegaram) e predicativo do sujeito (cansados): predicado verbo-nominal."),
    ("C", "Em “O juiz considerou o réu culpado”, o termo culpado é predicativo do objeto.",
     "Culpado é característica atribuída ao objeto direto o réu."),
    ("E", "Em “A obediência às leis é dever de todos”, o termo às leis exerce a função de objeto indireto.",
     "Às leis completa o substantivo obediência: é complemento nominal."),
    ("C", "Em “O inquérito foi instaurado pelo delegado”, o termo pelo delegado é agente da passiva.",
     "Na voz passiva analítica, quem pratica a ação é o agente da passiva."),
    ("E", "Em “Ontem, a equipe cumpriu o mandado”, o termo Ontem exerce a função de adjunto adnominal.",
     "Ontem indica circunstância de tempo ligada ao verbo: é adjunto adverbial."),

    ("C", "No trecho “A investigação da fraude demorou meses”, o termo da fraude complementa o sentido de investigação e exerce a função de complemento nominal.",
     "A fraude é o alvo da investigação (é investigada): papel de paciente, típico do complemento nominal."),
    ("E", "No trecho “A chegada dos agentes surpreendeu os moradores”, o termo dos agentes exerce a função de complemento nominal.",
     "Os agentes praticam a ação de chegar: papel de agente, típico do adjunto adnominal."),
    ("C", "No período “Carlos, o escrivão da equipe, lavrou o termo”, o trecho isolado por vírgulas é aposto explicativo.",
     "O trecho explica quem é Carlos e vem entre vírgulas."),
    ("E", "Em “Senhor delegado, o relatório está pronto”, o termo Senhor delegado é o sujeito da oração.",
     "É vocativo: chama o interlocutor. O sujeito é o relatório."),
    ("C", "Em “Os moradores do bairro denunciaram o tráfico”, a inserção de uma vírgula logo após bairro prejudicaria a correção gramatical do período.",
     "A vírgula separaria o sujeito (os moradores do bairro) do verbo."),
    ("E", "Em “O agente entregou ao juiz o relatório”, o termo ao juiz exerce a função de objeto direto.",
     "Ao juiz vem com preposição exigida por entregar: é objeto indireto. O objeto direto é o relatório."),
    ("C", "Em “Faz três anos que a quadrilha atua na região”, o verbo fazer é impessoal, e a oração em que ele aparece não tem sujeito.",
     "Fazer indicando tempo decorrido é impessoal."),
    ("E", "Em “Assaltaram a agência ontem à noite”, sem referência anterior a quem praticou a ação, o sujeito é oculto e pode ser identificado pela desinência verbal.",
     "Verbo na 3ª pessoa do plural sem referente no texto indica sujeito indeterminado."),
    ("C", "Em “O policial era um homem de coragem”, o termo de coragem exerce a função de adjunto adnominal.",
     "De coragem caracteriza o substantivo homem (equivale a corajoso): é adjunto adnominal."),
    ("E", "No período “Os policiais estão atentos”, a forma verbal estão classifica-se como transitiva direta.",
     "Estar, nesse caso, é verbo de ligação: liga o sujeito ao predicativo atentos."),
], 20)

SOURCES = [GRAM, "Nomenclatura Gramatical Brasileira (NGB).", SRC_A]
