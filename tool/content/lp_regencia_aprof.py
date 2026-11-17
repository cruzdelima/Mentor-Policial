# -*- coding: utf-8 -*-
"""Língua Portuguesa · Regência nominal e verbal — MATERIAL APROFUNDADO (estudo inicial)."""
from common import *

MATERIAL = material(
    "lp-regencia-02", "LP", "LP-12", "aprofundado", "Regência nominal e verbal", "Língua Portuguesa · Sintaxe",
    "portugues_regencia_aprofundado", "Portugues_Regencia_APROFUNDADO.pdf", None, ["Regência", "nominal e verbal"],
    ["Teoria completa para o primeiro estudo: os verbos que mais caem, regência nominal", "e preposição antes do pronome relativo, com 20 questões no estilo Cebraspe."],
    [("01", "Conceito", "termo regente, termo regido e transitividade"),
     ("02", "Verbos", "assistir, aspirar, visar, preferir, implicar, chegar e outros"),
     ("03", "Nominal", "nomes que pedem preposição"),
     ("04", "Relativos", "a preposição que vem antes do que"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Regência nominal e verbal (Língua Portuguesa)",
    "Base: gramáticas de referência e Dicionário de regência verbal (Celso Luft).", 150)

THEORY = [
    exam("Como estudar este material",
         "Regência aparece no Cebraspe de três formas: **verbo com sentido que muda conforme a regência** (*assistir, aspirar, visar*), "
         "**preposição antes do pronome relativo** (*o cargo a que aspiro*) e **crase**, que depende da regência. "
         "Decore o quadro da seção 2: são poucos verbos, e eles se repetem em todas as provas."),

    h2("1. Conceito"),
    p("**Regência** é a relação entre um termo que exige complemento (**regente**) e o complemento (**regido**). "
      "Quando o regente é um **verbo**, é regência verbal; quando é um **nome** (substantivo, adjetivo, advérbio), é regência nominal."),
    bl("**Transitivo direto (VTD)**: complemento sem preposição — *Prendeu o suspeito.*",
       "**Transitivo indireto (VTI)**: complemento com preposição — *Obedeceu às ordens.*",
       "**Transitivo direto e indireto (VTDI)**: os dois — *Entregou o laudo ao juiz.*",
       "**Intransitivo (VI)**: sem complemento — *O suspeito fugiu.*",
       "Alguns verbos **mudam de sentido** conforme a regência. É exatamente isso que a banca cobra."),

    h2("2. Verbos que mais caem"),
    tb(["Verbo", "Regência e sentido", "Exemplo"], [0.15, 0.45, 0.4], [
        ("assistir", "**a** algo = ver, presenciar (VTI) · alguém = ajudar (VTD) · **a** alguém = caber direito (VTI) · **em** = morar", "Assistimos **ao** julgamento. O médico assistiu **o** ferido. Assiste **ao** réu o direito de calar."),
        ("aspirar", "algo = inspirar, sorver (VTD) · **a** algo = desejar (VTI)", "Aspirou **o** gás. Aspira **ao** cargo de delegado."),
        ("visar", "algo = mirar, pôr visto (VTD) · **a** algo = pretender (VTI; a preposição é recomendada)", "Visou **o** alvo. Visou **o** cheque. Visa **ao** bem comum."),
        ("obedecer / desobedecer", "**a** algo ou alguém (VTI)", "Obedeça **às** normas. Desobedeceu **ao** comandante."),
        ("preferir", "algo **a** algo (sem *mais* e sem *do que*)", "Prefiro trabalhar **a** ficar parado."),
        ("chegar / ir / voltar", "**a** um lugar (e não *em*)", "Chegamos **ao** local. Foi **ao** banco."),
        ("implicar", "algo = acarretar (VTD, sem *em*) · **com** alguém = antipatizar · **em** algo = envolver-se", "A decisão implica **novos custos**. Implicou-se **em** fraude."),
        ("proceder", "**a** algo = realizar (VTI) · sem complemento = ter fundamento", "Procedeu-se **à** oitiva. A denúncia não procede."),
        ("pagar / perdoar", "coisa = OD; pessoa = OI (**a**)", "Pagou **a dívida ao** credor. Perdoou **ao** réu."),
        ("informar / avisar / certificar / notificar", "alguém **de** algo **ou** algo **a** alguém", "Informei **o delegado do** fato. Informei **ao delegado o** fato."),
        ("esquecer / lembrar", "algo (VTD) · **esquecer-se de / lembrar-se de** (pronominal)", "Esqueci **o** prazo. Esqueci-**me do** prazo."),
        ("agradecer", "algo **a** alguém", "Agradeceu **ao** colega **a** ajuda."),
        ("responder", "**a** algo ou alguém", "Respondeu **ao** ofício."),
        ("custar", "= ser difícil: sujeito é a coisa difícil; pessoa é OI", "Custou-**me** entender. (e não *eu custei a entender*, na norma estrita)"),
        ("namorar", "alguém (VTD, sem *com*)", "Ele namora **a** colega."),
        ("simpatizar / antipatizar", "**com** (não pronominal)", "Simpatizou **com** o colega. (e não *simpatizou-se*)"),
        ("morar / residir / situar", "**em**", "Reside **na** Rua da Aurora. Situado **na** Avenida X."),
        ("querer", "algo = desejar (VTD) · **a** alguém = estimar (VTI)", "Quero **a** promoção. Quero **aos** meus pais."),
    ]),
    trap("As quatro mais cobradas",
         "*Assistir **ao*** jogo (ver) · *aspirar **ao*** cargo (desejar) · *preferir X **a** Y* (nunca “mais do que”) · *implicar* sem *em* (acarretar)."),

    h2("3. Regência nominal"),
    tb(["Nome", "Preposição", "Exemplo"], [0.3, 0.2, 0.5], [
        ("acessível, favorável, contrário, obediente, preferível, relativo, vinculado", "a", "medida **favorável aos** servidores"),
        ("apto, propenso, necessário", "a, para", "**apto ao** serviço / **para** o serviço"),
        ("ávido, ansioso", "de, por, para", "**ávido de/por** justiça"),
        ("compatível, solidário", "com", "**compatível com** o cargo"),
        ("residente, situado, domiciliado", "em", "**residente em** Recife"),
        ("suspeito, capaz, digno", "de", "**suspeito de** furto"),
        ("imune", "a, de", "**imune a/de** críticas"),
        ("respeito", "a, com, para com, por", "**respeito às** leis"),
    ]),

    h2("4. Regência e pronome relativo"),
    p("Quando o verbo da oração adjetiva exige preposição, ela vem **antes do pronome relativo**:"),
    tb(["Verbo", "Construção correta", "Erro comum"], [0.2, 0.42, 0.38], [
        ("aspirar a", "o cargo **a que** aspiro", "o cargo que aspiro"),
        ("precisar de", "os documentos **de que** precisamos", "os documentos que precisamos"),
        ("referir-se a", "a lei **a que** me referi", "a lei que me referi"),
        ("gostar de", "o livro **de que** gosto", "o livro que gosto"),
        ("confiar em", "a pessoa **em quem** confio", "a pessoa que confio"),
        ("assistir a (ver)", "o filme **a que** assisti", "o filme que assisti"),
    ]),
    key("Truque",
        "Transforme a oração: *aspiro **ao** cargo* › *o cargo **a que** aspiro*. A preposição que aparece na frase “desmontada” sobe para antes do relativo."),
    h3("Verbos com regências diferentes e o mesmo complemento"),
    p("*Entrou e saiu **da** sala* está errado, porque *entrar* pede *em*. O correto é: *Entrou **na** sala e saiu **dela**.* "
      "O mesmo vale para *Assistiu e gostou **do** filme* (correto: *Assistiu **ao** filme e gostou **dele***)."),

    h2("5. Como o Cebraspe cobra"),
    bl("“A supressão da preposição X prejudicaria a correção” — confira a regência do verbo.",
       "“A forma *assistiu ao* poderia ser substituída por *assistiu o*” — só se o sentido for ajudar.",
       "Pronome relativo sem a preposição exigida pelo verbo.",
       "*Preferir mais… do que*, *implicar em*, *chegar em*: erros clássicos.",
       "Crase: só existe se houver preposição exigida pela regência."),
]

QUIZ = quiz([
    ("C", "Em “Os agentes assistiram ao vídeo da câmera de segurança”, a regência verbal está de acordo com a norma-padrão.",
     "Assistir no sentido de ver é transitivo indireto e exige a preposição a."),
    ("E", "Segundo a norma-padrão, está correta a frase “Todos assistiram o julgamento pela televisão”.",
     "No sentido de ver, assistir pede a preposição a: assistiram ao julgamento."),
    ("C", "Em “O socorrista assistiu o ferido até a chegada da ambulância”, o verbo assistir é transitivo direto e significa prestar assistência.",
     "No sentido de ajudar, assistir é transitivo direto."),
    ("E", "Em “O escrivão aspira o cargo de delegado”, a regência verbal está de acordo com a norma-padrão.",
     "No sentido de desejar, aspirar exige a preposição a: aspira ao cargo."),
    ("C", "Em “O delegado visou o documento antes de enviá-lo”, o verbo visar, no sentido de pôr visto, é transitivo direto.",
     "Visar é transitivo direto nos sentidos de pôr visto e de mirar."),
    ("E", "A frase “Prefiro trabalhar do que ficar parado” está de acordo com a norma-padrão.",
     "Preferir pede a preposição a, sem do que: prefiro trabalhar a ficar parado."),
    ("C", "Em “Chegamos ao local da ocorrência às 8h”, a regência do verbo chegar está de acordo com a norma-padrão.",
     "Verbos de movimento como chegar e ir regem a preposição a."),
    ("E", "Segundo a gramática normativa, está correta a frase “A nova regra implica em mais custos”.",
     "No sentido de acarretar, implicar é transitivo direto: implica mais custos."),
    ("C", "Em “Obedeça às normas de segurança”, a regência verbal e o acento grave estão corretos.",
     "Obedecer pede a preposição a, que se funde com o artigo as."),
    ("E", "A frase “Esqueci do prazo do recurso” está de acordo com a norma-padrão.",
     "Esquecer é transitivo direto (esqueci o prazo); com preposição, só na forma pronominal (esqueci-me do prazo)."),

    ("C", "Em “O cargo a que ele aspira exige nível superior”, a preposição antes do pronome relativo é exigida pelo verbo aspirar.",
     "Aspirar a: a preposição antecede o relativo que."),
    ("E", "Em “Os documentos que precisamos estão sobre a mesa”, a regência está de acordo com a norma-padrão.",
     "Precisar pede a preposição de: os documentos de que precisamos."),
    ("C", "A frase “Informei o delegado do ocorrido” está correta, assim como estaria “Informei ao delegado o ocorrido”.",
     "Informar admite as duas construções: alguém de algo ou algo a alguém."),
    ("E", "Em “O réu pagou o advogado com cheque”, a construção segue a regência do verbo pagar recomendada pela norma-padrão.",
     "Pagar tem a pessoa como objeto indireto: pagou ao advogado."),
    ("C", "Em “Custa-me acreditar nessa versão”, o sujeito do verbo custar é a oração “acreditar nessa versão”.",
     "No sentido de ser difícil, custar tem como sujeito aquilo que é difícil; a pessoa é objeto indireto."),
    ("E", "A frase “Ele simpatizou-se com o novo colega” está de acordo com a norma-padrão.",
     "Simpatizar não é pronominal: ele simpatizou com o novo colega."),
    ("C", "Em “O delegado procedeu à oitiva das testemunhas”, a regência do verbo proceder está de acordo com a norma-padrão.",
     "No sentido de realizar, proceder pede a preposição a."),
    ("E", "Em “O agente entrou e saiu da sala rapidamente”, a regência dos dois verbos está respeitada.",
     "Entrar pede em e sair pede de: entrou na sala e saiu dela."),
    ("C", "Em “A medida é favorável aos servidores”, a regência nominal está de acordo com a norma-padrão.",
     "Favorável rege a preposição a."),
    ("E", "Segundo a norma-padrão, está correta a frase “O suspeito reside à Rua da Aurora”.",
     "Residir rege a preposição em: reside na Rua da Aurora."),
], 20)

SOURCES = [GRAM, "Celso Pedro Luft, Dicionário prático de regência verbal.", SRC_A]
