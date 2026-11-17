# -*- coding: utf-8 -*-
"""Língua Portuguesa · Crase — MATERIAL APROFUNDADO (estudo inicial)."""
from common import *

MATERIAL = material(
    "lp-crase-02", "LP", "LP-13", "aprofundado", "Crase", "Língua Portuguesa · Sintaxe",
    "portugues_crase_aprofundado", "Portugues_Crase_APROFUNDADO.pdf", None, ["Crase:", "o acento grave"],
    ["Teoria completa para o primeiro estudo: quando o acento grave é obrigatório, proibido", "ou facultativo, com testes práticos e 20 questões no estilo Cebraspe."],
    [("01", "Conceito", "preposição a + artigo a"),
     ("02", "Obrigatória", "regência + feminino, locuções, horas, aquele"),
     ("03", "Proibida", "masculino, verbo, pronomes, plural sem artigo"),
     ("04", "Facultativa", "possessivos, nomes de mulher, até"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Emprego do sinal indicativo de crase (Língua Portuguesa)",
    "Base: gramáticas de referência (Bechara; Cunha e Cintra).", 150)

THEORY = [
    exam("Como estudar este material",
         "Crase não é acento de palavra: é a **fusão** de duas vogais *a*, marcada pelo **acento grave**. Por isso, ela só existe quando há, "
         "ao mesmo tempo, uma **preposição a** (exigida por alguma palavra) e um **artigo a** (exigido por um substantivo feminino), "
         "ou um *a* inicial de *aquele, aquela, aquilo*. Use os testes da seção 1 em todas as questões."),

    h2("1. Conceito e testes"),
    p("*Refiro-me **a** + **a** decisão* › *Refiro-me **à** decisão.* A preposição vem do verbo (*referir-se a*); o artigo vem do substantivo feminino (*a decisão*)."),
    key("Teste do masculino",
        "Troque a palavra feminina por uma masculina. Se aparecer **ao**, há crase: *Refiro-me **ao** despacho* › *Refiro-me **à** decisão*. "
        "Se aparecer só *a* ou *o*, não há: *Conheço **o** delegado* › *Conheço **a** delegada* (sem crase)."),
    key("Teste do lugar (cidades e países)",
        "Use o verbo *voltar*: se **volto da**, há crase; se **volto de**, não há. *Vou **à** Bahia (volto **da** Bahia). Vou **a** Recife (volto **de** Recife).* "
        "Com especificação, o artigo aparece: *Vou **à** Recife antiga.*"),

    h2("2. Crase obrigatória"),
    tb(["Caso", "Exemplo"], [0.42, 0.58], [
        ("Preposição exigida + palavra feminina com artigo", "Entregou o laudo **à** delegada. Assistiu **à** audiência."),
        ("Locuções adverbiais femininas", "**às** pressas, **à** noite, **às** vezes, **à** vista, **à** força, **à** toa, **à** distância de 50 m"),
        ("Locuções prepositivas e conjuntivas femininas", "**à** custa de, **à** frente de, **à** espera de, **à** medida que, **à** proporção que"),
        ("Horas determinadas", "A audiência começa **às** 14h. Chegou **à** uma hora."),
        ("*À moda de* (mesmo implícita)", "Bife **à** milanesa. Gol **à** Pelé."),
        ("Pronomes aquele(s), aquela(s), aquilo", "Encaminhe o ofício **àquele** setor. Refiro-me **àquilo**."),
        ("Relativos *a qual / as quais* com preposição", "A lei **à qual** me referi."),
        ("Palavra *casa* e *terra* determinadas", "Voltou **à** casa dos pais. Retornou **à** terra natal."),
    ]),

    h2("3. Crase proibida"),
    tb(["Antes de", "Exemplo"], [0.36, 0.64], [
        ("Palavra masculina (salvo *à moda de*)", "Comprou **a** prazo. Andou **a** cavalo."),
        ("Verbo", "Começou **a** investigar. Estava disposto **a** colaborar."),
        ("Pronomes pessoais, de tratamento (exceto *senhora, senhorita, dona*), indefinidos e demonstrativos *esta, essa*", "Disse **a** ela. Dirigiu-se **a** Vossa Excelência. Falou **a** toda a equipe."),
        ("*Uma* (artigo indefinido)", "Chegou **a** uma conclusão."),
        ("Palavras repetidas", "frente **a** frente, cara **a** cara, gota **a** gota"),
        ("*a* singular diante de palavra no plural", "Obedeceu **a** normas internas. Comunicou **a** autoridades."),
        ("Cidades sem artigo", "Vou **a** Brasília. (volto **de** Brasília)"),
        ("*Casa* (o próprio lar) e *terra* (oposta a bordo), sem determinante", "Voltou **a** casa cedo. Os marinheiros desceram **a** terra."),
        ("Correlação *de… a* sem artigo", "De segunda **a** sexta. De 8h **a** 12h. (com artigo: **das** 8h **às** 12h)"),
    ]),
    trap("Pegadinhas frequentes",
         "*à partir de* (errado: verbo) · *à ele* (pronome) · *à prazo* (masculino) · *à uma conclusão* (artigo indefinido) · "
         "*de segunda à sexta* (correlação sem artigo) · *à Vossa Excelência* (pronome de tratamento)."),

    h2("4. Crase facultativa"),
    bl("Antes de **pronome possessivo feminino singular**: *Entregou o laudo **a/à** sua chefe.* (o artigo antes do possessivo é opcional)",
       "Antes de **nome próprio feminino de pessoa**: *Enviou o ofício **a/à** Mariana.*",
       "Depois de **até**: *Foi **até a/à** delegacia.* (*até* sozinho ou *até a*)"),
    nt("No plural, o possessivo não é facultativo da mesma forma: *Entregou **às** suas chefes* (com artigo) ou *a suas chefes* (sem artigo, e então sem crase)."),

    h2("5. Como o Cebraspe cobra"),
    bl("“O emprego do acento grave é obrigatório / facultativo / proibido em X.”",
       "“A substituição de *diretora* por *diretor* exigiria a forma *ao*” — teste do masculino.",
       "“A retirada do acento grave prejudicaria a correção” — confira se há preposição e artigo.",
       "Crase e regência juntas: *assistir **à** audiência* (ver) × *assistir **a** vítima* (ajudar, OD: sem crase)."),
]

QUIZ = quiz([
    ("C", "Em “Refiro-me à decisão do juiz”, o acento grave está corretamente empregado.",
     "Referir-se exige a preposição a, e decisão admite o artigo a."),
    ("E", "Em “O agente começou à investigar o caso”, o acento grave está corretamente empregado.",
     "Não há crase antes de verbo."),
    ("C", "Em “A audiência começa às 14h”, o acento grave está corretamente empregado.",
     "Indicação de hora determinada leva crase."),
    ("E", "Em “Entregou o relatório à ele”, o acento grave está corretamente empregado.",
     "Não há crase antes de pronome pessoal."),
    ("C", "Em “Os agentes fizeram tudo às pressas”, o acento grave marca locução adverbial feminina.",
     "Locuções adverbiais femininas, como às pressas, levam acento grave."),
    ("E", "Em “Os delegados foram à Brasília para a reunião”, o acento grave está corretamente empregado.",
     "Teste: volto de Brasília. Sem artigo, não há crase."),
    ("C", "Em “O documentário retrata a viagem à Brasília dos anos 1960”, o acento grave está correto.",
     "A especificação faz o nome da cidade receber artigo: a Brasília dos anos 1960."),
    ("E", "Em “Os dois ficaram frente à frente durante o depoimento”, o acento grave está corretamente empregado.",
     "Entre palavras repetidas não há crase: frente a frente."),
    ("C", "Em “Encaminhe o ofício àquele setor”, o acento grave está corretamente empregado.",
     "A preposição a (encaminhar a) se funde com o a inicial de aquele."),
    ("E", "Em “O caso foi comunicado à autoridades estaduais”, o acento grave está corretamente empregado.",
     "A no singular diante de palavra no plural é só preposição: a autoridades."),

    ("C", "Em “Enviou o documento à diretora”, a substituição de diretora por diretor exigiria a forma ao.",
     "É o teste do masculino: se aparece ao, a crase no feminino está correta."),
    ("E", "Em “O servidor obedeceu a normas internas”, a ausência do acento grave constitui erro.",
     "O a singular antes de substantivo plural é apenas preposição; não há artigo."),
    ("C", "Em “Entregou o laudo à sua chefe”, o emprego do acento grave é facultativo.",
     "Antes de possessivo feminino singular, o artigo é opcional."),
    ("E", "Em “O réu voltou à casa dos pais”, o acento grave é proibido, pois não se usa crase antes da palavra casa.",
     "Casa determinada (dos pais) admite artigo: a crase é obrigatória."),
    ("C", "Em “Os jornalistas assistiram à audiência”, o acento grave decorre da regência de assistir, no sentido de ver, e do artigo feminino.",
     "Assistir a + a audiência."),
    ("E", "Em “Depois de horas, a equipe chegou a uma conclusão”, deveria ser empregado o acento grave antes de uma.",
     "Não há crase antes do artigo indefinido uma."),
    ("C", "Em “Os agentes ficaram à espera do mandado”, o acento grave integra locução prepositiva feminina.",
     "À espera de é locução prepositiva feminina."),
    ("E", "Em “O ofício foi dirigido à Vossa Excelência”, o acento grave está corretamente empregado.",
     "Pronomes de tratamento como Vossa Excelência não admitem artigo."),
    ("C", "Em “O pagamento foi feito à vista”, o acento grave marca locução adverbial feminina.",
     "À vista é locução adverbial feminina."),
    ("E", "Em “O plantão vai de segunda à sexta”, o emprego do acento grave está correto.",
     "Na correlação de… a sem artigo, não há crase: de segunda a sexta."),
], 20)

SOURCES = [GRAM, SRC_A]
