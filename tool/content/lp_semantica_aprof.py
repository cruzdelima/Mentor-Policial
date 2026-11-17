# -*- coding: utf-8 -*-
"""Língua Portuguesa · Semântica e significação das palavras — MATERIAL APROFUNDADO (estudo inicial)."""
from common import *

MATERIAL = material(
    "lp-semantica-02", "LP", "LP-19", "aprofundado", "Semântica e significação das palavras", "Língua Portuguesa · Semântica",
    "portugues_semantica_aprofundado", "Portugues_Semantica_APROFUNDADO.pdf", None, ["Significação", "das palavras"],
    ["Teoria completa para o primeiro estudo: sinônimos, antônimos, homônimos, parônimos,", "polissemia e sentido figurado, com 20 questões no estilo Cebraspe."],
    [("01", "Relações", "sinonímia, antonímia, hiperonímia"),
     ("02", "Homônimos e parônimos", "os pares que mais caem em prova policial"),
     ("03", "Polissemia", "uma palavra, vários sentidos"),
     ("04", "Denotação e conotação", "sentido literal e figurado; ambiguidade"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Significação das palavras (Língua Portuguesa)",
    "Base: gramáticas de referência e Vocabulário Ortográfico da Língua Portuguesa (ABL).", 90)

THEORY = [
    exam("Como estudar este material",
         "O Cebraspe cobra semântica principalmente como **substituição**: “a substituição de X por Y manteria o sentido do texto”. "
         "A sinonímia é sempre **contextual**: duas palavras podem ser sinônimas numa frase e não em outra. Os parônimos da seção 2 caem "
         "com frequência em provas da área policial (*mandado × mandato*, *flagrante × fragrante*, *infringir × infligir*)."),

    h2("1. Relações de sentido"),
    bl("**Sinonímia**: sentidos semelhantes no contexto — *O suspeito **fugiu** / **evadiu-se***.",
       "**Antonímia**: sentidos opostos — *legal × ilegal; absolver × condenar*.",
       "**Hiperonímia e hiponímia**: termo geral × termo específico — *arma* (hiperônimo) › *pistola, fuzil* (hipônimos). "
       "O hiperônimo é muito usado para retomar o hipônimo sem repeti-lo."),

    h2("2. Homônimos e parônimos"),
    bl("**Homônimos**: mesma pronúncia e/ou mesma grafia, sentidos diferentes. "
       "**Homófonos** (mesmo som, grafia diferente): *cela × sela, sessão × seção × cessão, censo × senso, concerto × conserto*. "
       "**Homógrafos** (mesma grafia, som diferente): *colher* (verbo) × *colher* (talher). "
       "**Perfeitos** (mesmo som e grafia): *são* (sadio) × *são* (verbo) × *são* (santo).",
       "**Parônimos**: palavras **parecidas** na grafia e na pronúncia, com sentidos diferentes."),
    tb(["Par", "Sentidos"], [0.32, 0.68], [
        ("mandado × mandato", "**mandado**: ordem judicial (*mandado de prisão*) · **mandato**: período de representação (*mandato de deputado*)"),
        ("flagrante × fragrante", "**flagrante**: evidente, no ato (*prisão em flagrante*) · **fragrante**: perfumado"),
        ("infringir × infligir", "**infringir**: violar (*infringiu a lei*) · **infligir**: aplicar pena (*infligiu castigo*)"),
        ("ratificar × retificar", "**ratificar**: confirmar · **retificar**: corrigir"),
        ("deferir × diferir", "**deferir**: atender (*pedido deferido*) · **diferir**: adiar; ser diferente"),
        ("eminente × iminente", "**eminente**: importante, elevado · **iminente**: prestes a acontecer"),
        ("descrição × discrição", "**descrição**: ato de descrever · **discrição**: reserva, prudência"),
        ("emergir × imergir", "**emergir**: vir à tona · **imergir**: mergulhar"),
        ("tráfego × tráfico", "**tráfego**: trânsito · **tráfico**: comércio ilegal"),
        ("vultoso × vultuoso", "**vultoso**: de grande valor (*quantia vultosa*) · **vultuoso**: inchado (rosto)"),
        ("despensa × dispensa", "**despensa**: lugar de guardar alimentos · **dispensa**: licença, isenção"),
        ("cessão × sessão × seção", "**cessão**: ato de ceder · **sessão**: reunião · **seção**: divisão, setor"),
        ("censo × senso", "**censo**: recenseamento · **senso**: juízo (*bom senso*)"),
        ("acender × ascender", "**acender**: pôr fogo · **ascender**: subir"),
        ("comprimento × cumprimento", "**comprimento**: extensão · **cumprimento**: saudação; execução (*cumprimento do mandado*)"),
    ]),

    h2("3. Polissemia"),
    p("Uma palavra com **vários sentidos relacionados**, que o contexto define: *banco* (assento, instituição financeira, banco de dados); "
      "*operação* (policial, cirúrgica, matemática, financeira). Diferente da homonímia, os sentidos da palavra polissêmica têm origem comum."),

    h2("4. Denotação, conotação e ambiguidade"),
    bl("**Denotação**: sentido literal, de dicionário — *A pedra caiu*.",
       "**Conotação**: sentido figurado, expressivo — *Ele tem um coração de **pedra***.",
       "**Ambiguidade**: duplo sentido não intencional. *O policial viu o assaltante **correndo*** (quem corria?). "
       "*O delegado disse ao escrivão que **seu** relatório estava errado* (de quem?). Desfaz-se reescrevendo a frase."),

    h2("5. Como o Cebraspe cobra"),
    bl("“A substituição de X por Y manteria o sentido do texto” — sinonímia **no contexto**.",
       "“O vocábulo X foi empregado em sentido conotativo.”",
       "“O trecho apresenta ambiguidade” — procure o termo com dois referentes.",
       "Parônimos trocados em frases da área jurídica e policial."),
]

QUIZ = quiz([
    ("C", "Em “O juiz expediu o mandado de prisão”, a substituição de mandado por mandato prejudicaria o sentido da frase.",
     "Mandado é ordem judicial; mandato é período de representação."),
    ("E", "Em “O perigo era eminente, e a equipe recuou”, o vocábulo eminente está adequadamente empregado.",
     "O sentido é de algo prestes a acontecer: iminente."),
    ("C", "Em “O motorista infringiu as normas de trânsito”, infringir significa violar.",
     "Infringir = desrespeitar; infligir = aplicar pena."),
    ("E", "Em “O juiz retificou a sentença, confirmando-a integralmente”, o verbo retificar está adequadamente empregado.",
     "Confirmar é ratificar; retificar é corrigir."),
    ("C", "Em “O tráfego na avenida foi interrompido”, o vocábulo tráfego refere-se ao trânsito de veículos.",
     "Tráfico seria comércio ilegal."),
    ("E", "Em “O agente agiu com descrição durante a investigação”, o vocábulo descrição está empregado no sentido de reserva, prudência.",
     "Reserva e prudência correspondem a discrição."),
    ("C", "Em “O pedido de liberdade provisória foi deferido”, o vocábulo deferido significa atendido.",
     "Deferir = conceder; diferir = adiar."),
    ("E", "Em “Foi apreendida uma quantia vultuosa”, o adjetivo está adequadamente empregado para indicar grande valor.",
     "Grande valor é vultosa; vultuoso significa inchado."),
    ("C", "A palavra operação é polissêmica, podendo designar, entre outros sentidos, ação policial e procedimento cirúrgico.",
     "Os sentidos são relacionados e definidos pelo contexto."),
    ("E", "Em “A cessão do júri começou às 9h”, o vocábulo cessão está adequadamente empregado.",
     "Reunião é sessão; cessão é ato de ceder."),

    ("C", "Em “O réu foi preso em flagrante delito”, flagrante não poderia ser substituído por fragrante.",
     "Fragrante significa perfumado."),
    ("E", "Em “Ele tem um coração de pedra”, a palavra pedra foi empregada em sentido denotativo.",
     "O sentido é figurado (conotativo): insensível."),
    ("C", "Em “O policial viu o assaltante correndo”, há ambiguidade quanto a quem estava correndo.",
     "Correndo pode referir-se ao policial ou ao assaltante."),
    ("E", "O vocábulo arma é hipônimo de pistola.",
     "Arma é o termo geral (hiperônimo); pistola é hipônimo."),
    ("C", "Os vocábulos cela e sela são homófonos.",
     "Têm a mesma pronúncia e grafias e sentidos diferentes."),
    ("E", "Os vocábulos sessão e seção são homônimos perfeitos.",
     "Têm grafias diferentes: são homófonos."),
    ("C", "Em “O censo indicou aumento da população carcerária”, censo significa recenseamento.",
     "Senso, com s, significa juízo."),
    ("E", "Os verbos deferir e diferir são sinônimos.",
     "Deferir é atender; diferir é adiar ou ser diferente."),
    ("C", "Em “O cumprimento do mandado ocorreu sem incidentes”, cumprimento significa execução.",
     "Comprimento, com o, refere-se a extensão."),
    ("E", "Em “Após horas, o corpo imergiu à superfície do lago”, o verbo imergir está adequadamente empregado.",
     "Vir à tona é emergir; imergir é mergulhar."),
], 20)

SOURCES = [GRAM, "Academia Brasileira de Letras, Vocabulário Ortográfico da Língua Portuguesa.", SRC_A]
