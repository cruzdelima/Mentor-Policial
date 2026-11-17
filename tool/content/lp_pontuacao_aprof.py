# -*- coding: utf-8 -*-
"""Língua Portuguesa · Pontuação — MATERIAL APROFUNDADO (estudo inicial)."""
from common import *

MATERIAL = material(
    "lp-pontuacao-02", "LP", "LP-14", "aprofundado", "Pontuação", "Língua Portuguesa · Sintaxe",
    "portugues_pontuacao_aprofundado", "Portugues_Pontuacao_APROFUNDADO.pdf", None, ["Pontuação:", "vírgula e outros sinais"],
    ["Teoria completa para o primeiro estudo: vírgula, ponto e vírgula, dois-pontos,", "travessão, parênteses e aspas, com 20 questões no estilo Cebraspe."],
    [("01", "Vírgula proibida", "entre sujeito, verbo e complementos"),
     ("02", "Vírgula obrigatória", "aposto, vocativo, enumeração, intercalações"),
     ("03", "Orações", "adjetivas, adverbiais, coordenadas e elipse"),
     ("04", "Outros sinais", "ponto e vírgula, dois-pontos, travessão, aspas"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Emprego dos sinais de pontuação (Língua Portuguesa)",
    "Base: gramáticas de referência (Bechara; Cunha e Cintra).", 150)

THEORY = [
    exam("Como estudar este material",
         "Pontuação é o item mais frequente nas provas do Cebraspe, quase sempre em forma de reescrita: “a inserção de vírgula após X "
         "prejudicaria a correção”, “a supressão das vírgulas alteraria o sentido”, “os travessões poderiam ser substituídos por vírgulas”. "
         "A vírgula depende da **sintaxe**: revise *Termos da oração* se tiver dúvida sobre sujeito e complementos."),

    h2("1. Vírgula proibida"),
    p("A ordem direta da oração é **sujeito + verbo + complementos + adjuntos**. Entre esses termos, na ordem direta, **não se usa vírgula**:"),
    bl("Entre **sujeito e verbo** — mesmo que o sujeito seja longo: *Os documentos apreendidos na operação de ontem **foram** periciados.*",
       "Entre **verbo e complemento**: *O delegado determinou **a abertura** do inquérito.*",
       "Entre **nome e complemento nominal** ou **adjunto adnominal**: *A investigação **da fraude** demorou.*",
       "Entre a **oração principal e a substantiva**: *É necessário **que** todos compareçam.*"),
    trap("Vírgula entre sujeito e verbo",
         "*O delegado, determinou a abertura do inquérito* e *Os servidores que faltaram, serão advertidos* estão errados. "
         "O segundo caso engana porque o sujeito termina numa oração adjetiva restritiva: a vírgula não pode separá-lo do verbo."),

    h2("2. Vírgula obrigatória: termos"),
    tb(["Uso", "Exemplo"], [0.34, 0.66], [
        ("Separar termos de enumeração", "Convocaram peritos, escrivães e agentes."),
        ("Isolar **aposto explicativo**", "Recife, capital de Pernambuco, sediou o evento."),
        ("Isolar **vocativo**", "Senhores, a sessão está aberta."),
        ("Isolar expressões explicativas e retificativas", "As provas, isto é, os documentos e as imagens, foram anexadas."),
        ("Isolar conjunções deslocadas", "O laudo, porém, não foi concluído."),
        ("Separar o local nas datas", "Recife, 17 de novembro de 2026."),
        ("Marcar **elipse** do verbo (zeugma)", "Ele cuidou das provas, e ela, dos depoimentos."),
    ]),
    h3("Adjunto adverbial deslocado"),
    p("No início ou no meio da oração, o adjunto adverbial **pode** ser isolado por vírgulas. Se for **curto**, a vírgula é **facultativa**; "
      "se for **longo**, recomenda-se: *Ontem (,) a equipe cumpriu o mandado. Durante as primeiras horas da madrugada, a equipe cumpriu o mandado.*"),

    h2("3. Vírgula entre orações"),
    tb(["Oração", "Regra", "Exemplo"], [0.24, 0.34, 0.42], [
        ("Adjetiva **explicativa**", "Entre vírgulas", "O réu, que confessou, foi condenado."),
        ("Adjetiva **restritiva**", "**Sem** vírgulas", "O réu que confessou foi condenado."),
        ("Adverbial **anteposta** ou intercalada", "Vírgula recomendada", "Quando a viatura chegou, o suspeito fugiu."),
        ("Adverbial **posposta**", "Vírgula facultativa", "O suspeito fugiu quando a viatura chegou."),
        ("Coordenadas assindéticas", "Vírgula", "Chegou, viu, prendeu."),
        ("Adversativas, conclusivas, explicativas", "Vírgula antes da conjunção", "Confessou, mas negou a autoria."),
        ("Aditivas com *e*", "Sem vírgula; com vírgula se os sujeitos forem diferentes ou houver polissíndeto", "A equipe chegou, e o suspeito fugiu."),
        ("Reduzidas de gerúndio e particípio antepostas", "Vírgula", "Terminada a audiência, os autos foram conclusos."),
    ]),
    key("A vírgula que muda o sentido",
        "Retirar ou inserir as vírgulas de uma **oração adjetiva** muda o sentido: com vírgulas, a informação vale para **todos**; "
        "sem vírgulas, **restringe** o grupo. O Cebraspe pergunta isso em quase toda prova."),

    h2("4. Outros sinais"),
    tb(["Sinal", "Usos principais", "Exemplo"], [0.16, 0.42, 0.42], [
        ("Ponto e vírgula", "Separar orações coordenadas longas ou que já têm vírgulas; separar itens de enumeração; anteceder conjunção deslocada", "A PM cuidou do cerco; a PC, da investigação."),
        ("Dois-pontos", "Anunciar enumeração, citação, explicação, síntese ou consequência", "Apreenderam três itens: armas, drogas e dinheiro."),
        ("Travessão", "Diálogo; isolar termo ou oração intercalada, com destaque (equivale a vírgulas ou parênteses)", "A testemunha — que estava nervosa — mudou a versão."),
        ("Parênteses", "Informações acessórias, explicações, datas, siglas", "A Lei Maria da Penha (Lei 11.340/2006) foi aplicada."),
        ("Aspas", "Citação literal, ironia, estrangeirismo, neologismo, títulos", "Chamou o plano de “infalível”, mas tudo deu errado."),
        ("Reticências", "Interrupção, hesitação, suspensão do pensamento", "Ele estava ali… depois sumiu."),
    ]),
    nt("Na troca de sinais, observe a **equivalência de função**: vírgulas, travessões duplos e parênteses podem isolar a mesma intercalação; "
       "o ponto e vírgula não equivale aos dois-pontos (estes anunciam explicação ou consequência)."),

    h2("5. Como o Cebraspe cobra"),
    bl("“A inserção de vírgula após X prejudicaria a correção” — verifique se separaria sujeito e verbo ou verbo e complemento.",
       "“A supressão das vírgulas alteraria o sentido” — oração adjetiva explicativa.",
       "“A vírgula após X é facultativa” — adjunto adverbial curto anteposto.",
       "“Os travessões poderiam ser substituídos por vírgulas” — intercalação.",
       "“O ponto e vírgula poderia ser substituído por ponto” — orações independentes, com ajuste de maiúscula."),
]

QUIZ = quiz([
    ("C", "Em “Os documentos apreendidos na operação foram periciados”, a inserção de vírgula logo após operação prejudicaria a correção gramatical.",
     "A vírgula separaria o sujeito do verbo."),
    ("E", "Em “O delegado, determinou a abertura do inquérito”, a vírgula está empregada de acordo com a norma-padrão.",
     "Não se separa o sujeito do verbo por vírgula."),
    ("C", "Em “Senhores, a sessão está aberta”, a vírgula isola o vocativo.",
     "Senhores chama os interlocutores: é vocativo, isolado por vírgula."),
    ("E", "O período “Recife capital de Pernambuco sediou o encontro” está corretamente pontuado.",
     "O aposto explicativo capital de Pernambuco deve vir entre vírgulas."),
    ("C", "Em “Ontem à noite, a equipe cumpriu o mandado”, a vírgula após noite é facultativa, por ser curto o adjunto adverbial anteposto.",
     "Adjunto adverbial curto deslocado admite ou dispensa a vírgula."),
    ("E", "No período “Ele cuidou das provas, e ela, dos depoimentos”, a vírgula após ela poderia ser suprimida sem prejuízo da correção.",
     "Essa vírgula marca a elipse do verbo cuidou e é necessária."),
    ("C", "No trecho “A Lei Maria da Penha (Lei 11.340/2006) foi aplicada”, os parênteses poderiam ser substituídos por vírgulas sem prejuízo da correção.",
     "Ambos isolam a informação acessória intercalada."),
    ("E", "O ponto e vírgula não pode ser empregado para separar orações coordenadas.",
     "O ponto e vírgula separa orações coordenadas, sobretudo longas ou já marcadas por vírgulas."),
    ("C", "Em “A equipe apreendeu três itens: armas, munições e drogas”, os dois-pontos introduzem uma enumeração.",
     "Os dois-pontos anunciam os itens que especificam três itens."),
    ("E", "No período “O réu, que confessou o crime, foi condenado”, a retirada das vírgulas manteria o sentido original.",
     "Sem vírgulas, a oração passa a restritiva, sugerindo que havia outros réus."),

    ("C", "Em “A testemunha — que estava nervosa — mudou a versão”, os travessões poderiam ser substituídos por vírgulas sem prejuízo da correção.",
     "Travessões duplos e vírgulas podem isolar a mesma oração intercalada."),
    ("E", "No período “Os agentes chegaram, e o suspeito fugiu”, o emprego da vírgula antes de e é proibido.",
     "Com sujeitos diferentes, a vírgula antes de e é admitida."),
    ("C", "Em “O laudo, porém, não foi concluído”, as vírgulas que isolam porém são obrigatórias.",
     "Conjunção deslocada para o interior da oração deve ficar entre vírgulas."),
    ("E", "No período “Quando a viatura chegou o suspeito já havia fugido”, a inserção de vírgula após chegou prejudicaria a correção.",
     "A vírgula separaria a oração adverbial anteposta, o que é recomendado."),
    ("C", "Em “As provas, isto é, os documentos e as imagens, foram anexadas”, as vírgulas isolam expressão explicativa e o termo a que ela se refere.",
     "Isto é introduz explicação, que vem isolada por vírgulas."),
    ("E", "O período “É importante, que todos compareçam à audiência” está corretamente pontuado.",
     "Não se separa a oração principal da substantiva subjetiva."),
    ("C", "Em “Convocaram-se peritos, escrivães e agentes”, as vírgulas separam termos de uma enumeração.",
     "Termos coordenados em sequência são separados por vírgula."),
    ("E", "O período “Os servidores que faltaram, serão advertidos” está corretamente pontuado.",
     "A vírgula separa o sujeito (que termina na oração restritiva) do verbo."),
    ("C", "Em “Ele chamou o plano de “infalível”, mas tudo deu errado”, as aspas podem sugerir ironia.",
     "As aspas destacam a palavra e indicam que ela é usada em sentido irônico."),
    ("E", "Em “A PM cuidou do cerco; a PC, da investigação”, o ponto e vírgula poderia ser substituído por dois-pontos sem alteração de sentido.",
     "Dois-pontos indicariam explicação ou consequência, alterando a relação entre as orações."),
], 20)

SOURCES = [GRAM, SRC_A]
