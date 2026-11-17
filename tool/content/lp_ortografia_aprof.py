# -- coding: utf-8 --
"""Língua Portuguesa · Ortografia oficial — MATERIAL APROFUNDADO (estudo inicial)."""
from common import *

MATERIAL = {
    "id": "lp-ortografia-02",
    "version": "0.1.0",
    "status": "Em revisão pelo autor",
    "subjectId": "LP",
    "topicIds": ["LP-01"],
    "kind": "aprofundado",
    "title": "Ortografia oficial",
    "subtitle": "Língua Portuguesa · Ortografia",
    "minutes": 150,
    "folder": "portugues_ortografia_aprofundado",
    "pdf": "portugues_ortografia_aprofundado.pdf",
    "outName": "Portugues_Ortografia_APROFUNDADO.pdf",
    "header": "Língua Portuguesa · Ortografia oficial",
    "coverKicker": "Língua Portuguesa  ·  Ortografia",
    "coverTitle": ["Ortografia oficial"],
    "coverSub": ["Teoria completa para o primeiro estudo: emprego das letras, palavras que confundem,", "porquês e hífen, com 20 questões no estilo Cebraspe e gabarito comentado."],
    "coverItems": [("01", "Sistema", "Acordo Ortográfico, alfabeto e VOLP"),
                   ("02", "Letras", "S/Z, X/CH, G/J, SS/Ç/S/C, E/I"),
                   ("03", "Pares perigosos", "homônimos, parônimos e expressões que confundem"),
                   ("04", "Hífen", "prefixos, palavras compostas e locuções"),
                   ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "coverTopic": "Tópico do edital: Ortografia oficial (Língua Portuguesa)",
    "coverBase": "Base: Acordo Ortográfico da Língua Portuguesa (Decreto nº 6.583/2008) e VOLP da Academia Brasileira de Letras.",
}

THEORY = [
    exam("Como estudar este material",
         "Este é o material do **primeiro contato** com o assunto. Ortografia não se decora de uma vez: entenda as regras de formação "
         "(elas resolvem a maior parte dos casos), marque as exceções e faça as 20 questões. Nas revisões, use o **PDF de resumo**. "
         "Acentuação gráfica é assunto separado e tem material próprio."),

    h2("1. O que é ortografia oficial"),
    p("**Ortografia** é a parte da gramática que trata da escrita correta das palavras: emprego das letras, do hífen, das iniciais maiúsculas e dos "
      "sinais gráficos. É **oficial** porque decorre de norma: o **Acordo Ortográfico da Língua Portuguesa**, assinado em 1990 e promulgado no Brasil "
      "pelo **Decreto nº 6.583/2008**. As novas regras passaram a valer em 2009, conviveram com as antigas durante a transição e são "
      "**obrigatórias desde 1º de janeiro de 2016**."),
    p("O **Vocabulário Ortográfico da Língua Portuguesa (VOLP)**, da Academia Brasileira de Letras, é a referência para a grafia de cada palavra."),
    h3("O que o Acordo mudou (visão geral)"),
    bl("**Alfabeto**: passou a ter **26 letras**, com a reintegração de **K, W e Y** (usadas em nomes próprios estrangeiros e derivados, "
       "siglas, símbolos e unidades: Kant, kantiano, km, watt, Wagner).",
       "**Trema**: abolido das palavras portuguesas e aportuguesadas (frequente, linguiça, tranquilo). Permanece apenas em nomes próprios "
       "estrangeiros e derivados (Müller, mülleriano). **A pronúncia não mudou.**",
       "**Acentuação**: algumas regras foram alteradas (assunto do próximo material).",
       "**Hífen**: novas regras para prefixos e compostos (seção 6)."),
    key("Ponto-chave",
        "O Acordo mudou a **escrita**, nunca a **pronúncia**. Item que afirme mudança de pronúncia está errado."),

    h2("2. Emprego das letras"),
    p("Há duas ferramentas que resolvem a maioria das dúvidas: a **família da palavra** (derivadas mantêm a letra da primitiva: "
      "casa › casebre; cruz › cruzeiro; laranja › laranjeira) e os **sufixos**, que têm grafia fixa."),

    h3("S ou Z"),
    tb(["Usa-se", "Quando", "Exemplos"], [0.12, 0.48, 0.4], [
        ("S", "Sufixos **-ês, -esa** que indicam origem, nacionalidade ou título", "português, francesa, marquês, baronesa, camponês"),
        ("S", "Sufixos **-oso, -osa** (cheio de)", "gostoso, famosa, cauteloso"),
        ("S", "Depois de **ditongo**", "coisa, lousa, pausa, náusea, maisena"),
        ("S", "Formas dos verbos **pôr** e **querer**", "pus, pusesse, quis, quisera, compuseram"),
        ("S", "Verbos em **-isar** quando a palavra primitiva já tem S", "análise › analisar; pesquisa › pesquisar; aviso › avisar; paralisia › paralisar"),
        ("Z", "Sufixos **-ez, -eza** que formam substantivos abstratos a partir de adjetivos", "rápido › rapidez; belo › beleza; pobre › pobreza; sensato › sensatez"),
        ("Z", "Sufixo **-izar** quando a primitiva não tem S", "real › realizar; civil › civilizar; canal › canalizar; humano › humanizar"),
        ("Z", "Sufixo **-ização**", "realização, urbanização, fiscalização"),
    ]),
    trap("Pegadinha: -isar × -izar",
         "Olhe a primitiva: **análise** já tem S › **analisar**; **catálise** › **catalisar**; **pesquisa** › **pesquisar**. "
         "Sem S na primitiva, o sufixo é **-izar**: **ameno** › **amenizar**. Exceção clássica: **catequese** › **catequizar**."),

    h3("X ou CH"),
    tb(["Usa-se", "Quando", "Exemplos e exceções"], [0.12, 0.4, 0.48], [
        ("X", "Depois de **ditongo**", "caixa, peixe, faixa, frouxo, ameixa (exceções: caucho, recauchutar)"),
        ("X", "Depois da sílaba inicial **en-**", "enxada, enxame, enxergar, enxurrada, enxugar. Exceções: palavras derivadas de outras com CH — **encher** (cheio), **encharcar** (charco), **enchente**"),
        ("X", "Depois da sílaba inicial **me-**", "mexer, mexerico, mexicano. Exceção: **mecha** (de cabelo)"),
        ("X", "Palavras de origem indígena e africana", "abacaxi, xavante, xingar, orixá"),
        ("CH", "Palavras da mesma família de outras com CH", "chave › chaveiro; cheio › preencher; charco › encharcar"),
    ]),

    h3("G ou J"),
    tb(["Usa-se", "Quando", "Exemplos e exceções"], [0.12, 0.4, 0.48], [
        ("G", "Substantivos terminados em **-agem, -igem, -ugem**", "garagem, viagem, vertigem, ferrugem (exceções: **pajem, lambujem**)"),
        ("G", "Terminações **-ágio, -égio, -ígio, -ógio, -úgio**", "pedágio, colégio, prestígio, relógio, refúgio"),
        ("J", "Formas dos verbos terminados em **-jar**", "viajar › viajei, viajem; arranjar › arranjem; despejar › despejem"),
        ("J", "Palavras de origem tupi, africana e árabe", "jiboia, pajé, jerimum, canjica, jenipapo, alforje"),
        ("J", "Palavras derivadas de outras com J", "laranja › laranjeira; loja › lojista; cereja › cerejeira; gorja › gorjeta"),
    ]),
    trap("Pegadinha: viagem × viajem",
         "**Viagem** (com G) é **substantivo**: a viagem foi longa. **Viajem** (com J) é **verbo** viajar: espero que eles viajem cedo."),

    h3("SS, Ç, S, C e SC: os substantivos derivados de verbos"),
    p("A correlação entre a terminação do verbo e a do substantivo resolve quase tudo:"),
    tb(["Verbo com", "Substantivo com", "Exemplos"], [0.2, 0.2, 0.6], [
        ("-ced-", "-cess-", "ceder › cessão; conceder › concessão; exceder › excesso; interceder › intercessão"),
        ("-gred-", "-gress-", "agredir › agressão; progredir › progresso; regredir › regressão"),
        ("-prim-", "-press-", "imprimir › impressão; oprimir › opressão; reprimir › repressão"),
        ("-tir", "-ssão", "admitir › admissão; discutir › discussão; permitir › permissão; demitir › demissão"),
        ("-met-", "-miss-", "submeter › submissão; comprometer › compromisso; intrometer › intromissão"),
        ("-nd-", "-ns-", "pretender › pretensão; suspender › suspensão; expandir › expansão; ascender › ascensão; compreender › compreensão"),
        ("-rg-, -rt-", "-rs-", "imergir › imersão; submergir › submersão; converter › conversão; divertir › diversão; inverter › inversão"),
        ("-pel-, -corr-", "-puls-, -curs-", "expelir › expulsão; impelir › impulso; concorrer › concurso; discorrer › discurso"),
        ("-ter", "-tenção", "reter › retenção; deter › detenção; obter › obtenção; abster › abstenção"),
        ("-to (particípio/primitiva)", "-ção", "exceto › exceção; isento › isenção; correto › correção; ato › ação; canto › canção"),
    ]),
    bl("Usa-se **Ç** depois de **ditongo**: eleição, traição, feição, louça, caiçara.",
       "Usa-se **Ç** em palavras de origem tupi, africana e árabe: açaí, paçoca, miçanga, açúcar, muçulmano, açude.",
       "**SC** aparece em palavras de origem latina: nascer, crescer, descer, piscina, fascínio, consciência, adolescente, rescindir, suscitar, obsceno.",
       "**Exceção** (com Ç) e **excesso** (com SS) vêm de famílias diferentes: excetuar e exceder."),
    key("Três palavras, três grafias",
        "**Cessão** = ato de ceder (cessão de direitos). **Sessão** = reunião, período (sessão do júri, sessão de cinema). "
        "**Seção** (ou **secção**) = parte, divisão, setor (seção eleitoral, seção de pessoal)."),

    h3("E ou I"),
    bl("Verbos terminados em **-uar** e **-oar**: escrevem-se com **E** no presente do subjuntivo — continue, atue, efetue, perdoe, abençoe, magoe.",
       "Verbos terminados em **-uir**, **-air** e **-oer**: escrevem-se com **I** — possui, contribui, diminui, atrai, cai, sai, dói, mói.",
       "Prefixo **ante-** (antes): antebraço, antessala, antevéspera. Prefixo **anti-** (contra): antiaéreo, anticorpo, antissocial.",
       "Grafias que costumam ser cobradas: **privilégio**, **empecilho**, **disenteria**, **meritíssimo**, **creolina**, **cumeeira**, **irrequieto**, "
       "**digladiar**, **cabeleireiro**, **beneficente**, **reivindicar**, **mendigo**, **asterisco**, **prazerosamente**."),

    h2("3. Homônimos e parônimos"),
    p("**Homônimos** têm a mesma pronúncia (ou a mesma grafia) e sentidos diferentes: cela e sela. **Parônimos** são parecidos na escrita "
      "e na pronúncia: ratificar e retificar. O Cebraspe cobra esses pares em itens de **substituição de palavras**: a troca mantém a correção "
      "gramatical, mas altera o sentido."),
    tb(["Palavra", "Sentido", "Palavra", "Sentido"], [0.17, 0.33, 0.17, 0.33], [
        ("acender", "pôr fogo", "ascender", "subir"),
        ("apreçar", "perguntar o preço", "apressar", "dar pressa"),
        ("caçar", "perseguir animais", "cassar", "anular (mandato, direitos)"),
        ("censo", "recenseamento", "senso", "juízo, percepção"),
        ("concerto", "sessão musical; harmonia", "conserto", "reparo"),
        ("comprimento", "extensão", "cumprimento", "saudação; ato de cumprir"),
        ("deferir", "atender, conceder", "diferir", "adiar; ser diferente"),
        ("delatar", "denunciar", "dilatar", "aumentar, estender"),
        ("descrição", "ato de descrever", "discrição", "reserva, qualidade de discreto"),
        ("descriminar", "tirar o caráter de crime", "discriminar", "distinguir; segregar"),
        ("despercebido", "que não foi notado", "desapercebido", "desprevenido, desprovido"),
        ("emergir", "vir à tona", "imergir", "mergulhar"),
        ("emigrar", "sair do país", "imigrar", "entrar em país estrangeiro"),
        ("eminente", "ilustre, elevado", "iminente", "prestes a acontecer"),
        ("espiar", "observar às escondidas", "expiar", "pagar (culpa, pena)"),
        ("estrato", "camada", "extrato", "resumo; o que foi extraído"),
        ("flagrante", "evidente; ato de surpreender no crime", "fragrante", "perfumado"),
        ("incipiente", "que está no início", "insipiente", "ignorante"),
        ("infligir", "aplicar (pena, castigo)", "infringir", "violar, desrespeitar"),
        ("mandado", "ordem judicial", "mandato", "poder outorgado; período de cargo eletivo"),
        ("ratificar", "confirmar", "retificar", "corrigir"),
        ("soar", "produzir som", "suar", "transpirar"),
        ("tachar", "atribuir defeito, censurar", "taxar", "fixar taxa, tributar"),
        ("tráfego", "trânsito", "tráfico", "comércio ilegal"),
        ("vultoso", "volumoso, de grande vulto", "vultuoso", "com a face inchada e vermelha"),
    ]),
    key("Vocabulário de polícia",
        "Vários pares fazem parte da rotina policial e são os favoritos das bancas da área: **mandado** de prisão × **mandato** do deputado; "
        "**flagrante** delito; **infligir** pena × **infringir** a lei; **tráfico** de drogas × **tráfego** de veículos; "
        "**cassar** o mandato; **descriminar** uma conduta × **discriminar** uma pessoa; **ratificar** o depoimento × **retificar** o termo."),

    h2("4. Os porquês"),
    tb(["Forma", "Quando usar", "Teste", "Exemplo"], [0.14, 0.34, 0.24, 0.28], [
        ("por que", "Em perguntas (diretas ou indiretas); quando equivale a pelo qual e flexões", "Cabe “por qual razão” ou “pelo qual”", "Por que ele faltou? Não sei por que ele faltou. O motivo por que faltou é grave."),
        ("por quê", "No **fim** da frase ou antes de pausa forte", "Vem antes de ponto", "Ele faltou por quê? Faltou e não disse por quê."),
        ("porque", "Conjunção: introduz causa ou explicação", "Cabe “pois” ou “já que”", "Faltou porque estava doente."),
        ("porquê", "Substantivo: vem com artigo, pronome ou numeral", "Cabe “o motivo”", "Ninguém entendeu o porquê da falta."),
    ]),

    h2("5. Expressões que confundem"),
    tb(["Par", "Como distinguir"], [0.26, 0.74], [
        ("mal × mau", "**Mal** é o contrário de **bem** (advérbio ou substantivo; também conjunção = assim que): dormiu mal; mal chegou, saiu. **Mau** é o contrário de **bom** (adjetivo): mau policial."),
        ("mas × mais", "**Mas** indica oposição (= porém). **Mais** indica quantidade ou intensidade (contrário de menos)."),
        ("há × a (tempo)", "**Há** para tempo passado (= faz): saiu há duas horas. **A** para tempo futuro ou distância: chegará daqui a duas horas; fica a dois quilômetros. Com há, não use atrás (redundância)."),
        ("onde × aonde", "**Onde** com verbos que não indicam movimento: onde você mora? **Aonde** com verbos de movimento que pedem a preposição a: aonde você vai?"),
        ("acerca de × a cerca de × há cerca de", "**Acerca de** = sobre. **A cerca de** = a aproximadamente (distância, futuro). **Há cerca de** = faz ou existe aproximadamente."),
        ("afim × a fim de", "**Afim** = semelhante (ideias afins). **A fim de** = para, com o objetivo de."),
        ("ao encontro de × de encontro a", "**Ao encontro de** = a favor, em direção a. **De encontro a** = contra, em choque com."),
        ("senão × se não", "**Senão** = caso contrário, a não ser, mas sim. **Se não** = caso não (condição): se não chover, iremos."),
        ("em vez de × ao invés de", "**Em vez de** = no lugar de (serve sempre). **Ao invés de** = ao contrário de (só para ideias opostas)."),
        ("à medida que × na medida em que", "**À medida que** = à proporção que. **Na medida em que** = porque, uma vez que. Não existe “à medida em que”."),
        ("a princípio × em princípio", "**A princípio** = no começo. **Em princípio** = em tese, de modo geral."),
        ("tampouco × tão pouco", "**Tampouco** = também não. **Tão pouco** = muito pouco."),
        ("demais × de mais", "**Demais** = muito, em excesso; os outros. **De mais** opõe-se a de menos: nada de mais."),
        ("sob × sobre", "**Sob** = embaixo de (sob custódia, sob pena de). **Sobre** = em cima de; a respeito de."),
        ("a par × ao par", "**A par** = ciente. **Ao par** = em equivalência (câmbio, títulos)."),
        ("sessão × seção × cessão", "Reunião × parte × ato de ceder (ver seção 2)."),
    ]),
    bl("**Haja vista** é expressão invariável na forma mais aceita: haja vista os fatos.",
       "**Meio**, como advérbio (= um pouco), não varia: ela está meio cansada. Como numeral (= metade), varia: meia garrafa, meio-dia e meia.",
       "**Menos** nunca varia: menos pessoas (não existe “menas”).",
       "Escreve-se **de repente**, **por isso**, **a partir de**, **com certeza**, **em cima**, **embaixo**, **apesar de**, **de novo** — "
       "separadas ou juntas exatamente como aqui."),

    h2("6. Hífen"),
    h3("Prefixos e falsos prefixos: a regra geral"),
    tb(["Situação", "Regra", "Exemplos"], [0.3, 0.2, 0.5], [
        ("2º elemento começa com **H**", "**Com** hífen", "anti-higiênico, super-homem, pré-história, sobre-humano, extra-humano"),
        ("Prefixo termina na **mesma vogal** que inicia o 2º elemento", "**Com** hífen", "micro-ondas, anti-inflamatório, contra-ataque, arqui-inimigo, semi-interno, auto-observação"),
        ("Prefixo termina em vogal **diferente** da que inicia o 2º elemento", "**Sem** hífen", "autoescola, infraestrutura, extraoficial, semiaberto, antiaéreo, coautor, autoestima"),
        ("Prefixo termina em vogal e o 2º elemento começa com **R ou S**", "**Sem** hífen, **dobrando** a consoante", "antirracismo, contrarregra, ultrassom, minissaia, antissocial, semirreta, autorretrato"),
        ("Prefixo termina em vogal e o 2º elemento começa com outra consoante", "**Sem** hífen", "anteprojeto, semicírculo, ultramoderno, autodefesa, seminovo, contracheque"),
        ("Prefixo termina em **R** e o 2º elemento começa com **R**", "**Com** hífen", "hiper-requintado, inter-regional, super-resistente, inter-racial"),
        ("Prefixo termina em consoante e o 2º elemento começa com vogal ou outra consoante", "**Sem** hífen", "hiperativo, interestadual, superinteressante, supermercado, intermunicipal"),
    ]),
    key("Regra de bolso",
        "**Letras iguais se separam, letras diferentes se juntam.** E o **H** sempre pede hífen. "
        "Micro-ondas (o + o), inter-regional (r + r); autoescola (o + e), hiperativo (r + a)."),
    h3("Casos especiais de prefixos"),
    bl("**Sempre com hífen**: **ex-** (anterior), **vice-**, **sota-**, **soto-**; **pós-, pré-, pró-** (tônicos, acentuados); "
       "**além-, aquém-, recém-, sem-**. Exemplos: ex-diretor, vice-presidente, pós-graduação, pré-natal, pró-reitor, além-mar, recém-nascido, sem-terra.",
       "**Co-, re-, pre- e pro-** (átonos) **juntam-se** ao 2º elemento, mesmo com vogal igual: coordenar, cooperar, coautor, coerdeiro, "
       "reeditar, reescrever, preexistente, preestabelecer, proativo.",
       "**Sub-, sob-, ab-, ob-, ad-**: com hífen antes de **B, H e R** — sub-base, sub-região, sub-reitor, ab-rogar, ad-renal. "
       "Nos demais casos, sem hífen: subsolo, subchefe, subdelegado. O VOLP registra **sub-humano** e **subumano**.",
       "**Circum- e pan-**: com hífen antes de **vogal, H, M e N** — circum-navegação, pan-americano, circum-hospitalar.",
       "**Mal-**: com hífen antes de **vogal, H e L** — mal-estar, mal-humorado, mal-educado, mal-limpo. Nos demais: malcriado, malfeito, malvisto.",
       "**Bem-**: em regra, com hífen — bem-vindo, bem-estar, bem-humorado, bem-sucedido, bem-nascido. Algumas formas são aglutinadas: benfeitor, benquisto, benfazejo.",
       "**Não** e **quase**, usados como prefixo, **não levam hífen**: não agressão, não fumante, quase delito."),
    h3("Palavras compostas"),
    tb(["Situação", "Regra", "Exemplos"], [0.36, 0.16, 0.48], [
        ("Composto **sem elemento de ligação**, cujos termos formam uma unidade de sentido", "**Com** hífen", "guarda-chuva, segunda-feira, arco-íris, decreto-lei, médico-cirurgião, tenente-coronel, boa-fé, má-fé, porta-malas"),
        ("Compostos em que se perdeu a noção de composição", "**Sem** hífen (juntos)", "girassol, paraquedas, paraquedista, mandachuva, pontapé, madressilva, passatempo"),
        ("Locuções **com elemento de ligação** (preposição, artigo)", "**Sem** hífen", "pé de moleque, dia a dia, fim de semana, mão de obra, sala de jantar, cão de guarda, ponto e vírgula, à vontade"),
        ("Exceções consagradas pelo uso", "**Com** hífen", "água-de-colônia, arco-da-velha, cor-de-rosa, mais-que-perfeito, pé-de-meia, ao deus-dará, à queima-roupa"),
        ("Nomes de **espécies botânicas e zoológicas**", "**Com** hífen", "bem-te-vi, erva-doce, copo-de-leite, joão-de-barro, couve-flor, cobra-d'água"),
        ("Palavras **repetidas** ou onomatopaicas", "**Com** hífen", "reco-reco, tique-taque, blá-blá-blá, corre-corre"),
        ("Adjetivos pátrios compostos", "**Com** hífen", "sul-africano, norte-americano, mato-grossense, afro-brasileiro"),
        ("Topônimos iniciados por **Grã-, Grão-**, por verbo, ou ligados por artigo", "**Com** hífen", "Grã-Bretanha, Grão-Pará, Passa-Quatro, Baía de Todos-os-Santos, Trás-os-Montes"),
        ("Encadeamentos de palavras", "**Com** hífen", "ponte Rio-Niterói, eixo Rio-São Paulo, relação professor-aluno"),
    ]),
    bl("Com **pronomes** ligados ao verbo (ênclise e mesóclise), o hífen é obrigatório: disse-me, entregá-lo, dir-se-ia, vende-se.",
       "Na **translineação** (quebra de linha) de palavra com hífen, se a quebra coincidir com o hífen, repita-o no início da linha seguinte.",
       "Sufixos de origem tupi **-açu, -guaçu, -mirim** pedem hífen quando o 1º elemento termina em vogal acentuada ou a pronúncia exige: capim-açu, amoré-guaçu, anajá-mirim."),
    trap("Pegadinha: dia a dia e à toa",
         "Depois do Acordo, **dia a dia** não tem hífen em nenhum sentido (o dia a dia do policial; melhora dia a dia). O mesmo vale para "
         "**à toa**, **fim de semana**, **ponto de vista**, **mão de obra**, **pôr do sol** e **pé de moleque**."),

    h2("7. Iniciais maiúsculas e minúsculas"),
    bl("**Minúscula**: nomes dos **dias da semana, meses e estações do ano** (segunda-feira, janeiro, verão); pontos cardeais quando indicam direção "
       "(seguiu para o norte); fulano, sicrano, beltrano.",
       "**Maiúscula**: nomes próprios de qualquer espécie; nomes de instituições (Polícia Federal, Supremo Tribunal Federal); "
       "pontos cardeais quando indicam **região** (o Nordeste, o Sul do país); início de período; siglas.",
       "**Facultativa**: em títulos de obras, depois do primeiro elemento (Memórias Póstumas de Brás Cubas ou Memórias póstumas de Brás Cubas); "
       "em formas de tratamento (Senhor Doutor ou senhor doutor); em nomes de disciplinas e domínios do saber "
       "(Português ou português); em nomes de logradouros e templos (Rua ou rua da Liberdade)."),

    h2("8. Como o Cebraspe cobra"),
    bl("**“Estaria mantida a correção gramatical do texto caso…”**: a banca propõe trocar uma palavra por outra de grafia parecida. "
       "Verifique a grafia **e** o sentido: a troca de mandado por mandato mantém a correção gramatical, mas altera o sentido — leia até o fim do item.",
       "**“O emprego do hífen em X justifica-se pela mesma regra de Y”**: identifique a regra de cada palavra antes de comparar.",
       "**“A forma X poderia ser grafada Y, conforme o Acordo”**: lembre o que mudou e o que continuou igual.",
       "**Porquês e expressões** (mal/mau, há/a, onde/aonde) aparecem dentro de itens de reescrita.",
       "Cuidado com os absolutos: sempre, nunca, em todos os casos. Em ortografia, quase toda regra tem exceção."),
]

QUIZ = quiz([
    ("C", "Com o Acordo Ortográfico, o alfabeto da língua portuguesa passou a contar com 26 letras, em razão da reintegração de K, W e Y.",
     "As três letras voltaram oficialmente ao alfabeto, usadas em nomes estrangeiros e derivados, siglas, símbolos e unidades de medida."),
    ("E", "O Acordo Ortográfico eliminou o trema, o que alterou a pronúncia de palavras como frequente e tranquilo, nas quais a letra u deixou de ser pronunciada.",
     "O trema foi abolido da escrita, mas a pronúncia não mudou. O Acordo altera a grafia, nunca a fala."),
    ("C", "As palavras analisar, pesquisar e paralisar grafam-se com S porque derivam de palavras cujo radical já apresenta essa letra.",
     "Análise, pesquisa e paralisia têm S; por isso os verbos terminam em -isar, e não em -izar."),
    ("E", "Estão corretamente grafadas todas as palavras da série: enxada, enxurrada, enxarcar e enxame.",
     "Depois de en- usa-se X, mas encharcar deriva de charco e mantém o CH. A grafia correta é encharcar."),
    ("E", "Na frase “É preciso que os agentes viagem ainda hoje”, a forma verbal está corretamente grafada.",
     "O verbo viajar conserva o J em toda a conjugação: que os agentes viajem. Viagem, com G, é substantivo."),
    ("C", "Os substantivos pretensão, suspensão e ascensão grafam-se com S por derivarem de verbos cujo radical termina em -nd-.",
     "Pretender, suspender e ascender: a correlação -nd- › -ns- explica a grafia."),
    ("C", "Em “O delegado não informou por que o preso foi transferido”, a grafia por que, em duas palavras e sem acento, está correta.",
     "Trata-se de pergunta indireta: equivale a “por qual razão”. Usa-se por que separado e sem acento."),
    ("E", "Em “Mau chegou à delegacia, o suspeito confessou”, o vocábulo inicial está grafado corretamente, pois equivale a “assim que”.",
     "Com o sentido de “assim que”, usa-se mal (conjunção). Mau é adjetivo, contrário de bom."),
    ("C", "As palavras micro-ondas e anti-inflamatório recebem hífen pela mesma razão: o prefixo termina com a mesma vogal que inicia o segundo elemento.",
     "Letras iguais se separam: o + o e i + i."),
    ("E", "Conforme as regras atuais, grafam-se com hífen as palavras auto-escola, infra-estrutura e extra-oficial.",
     "Quando o prefixo termina em vogal diferente da que inicia o segundo elemento, não há hífen: autoescola, infraestrutura, extraoficial."),

    ("C", "A substituição de “ratificou” por “retificou” em “O perito ratificou o laudo” manteria a correção gramatical do período, mas alteraria seu sentido original.",
     "Ambas as formas existem e se encaixam na estrutura, mas ratificar é confirmar e retificar é corrigir."),
    ("E", "No trecho “O juiz expediu o mandato de prisão”, o vocábulo mandato está empregado de acordo com seu sentido usual, que é o de ordem judicial.",
     "Ordem judicial é mandado. Mandato é o poder outorgado a alguém ou o período de exercício de cargo eletivo."),
    ("C", "Em “O policial foi surpreendido pelo perigo iminente”, o termo iminente indica algo que está prestes a acontecer.",
     "Iminente = prestes a ocorrer. Eminente = ilustre, elevado."),
    ("E", "As palavras antissocial e contrarregra deveriam ser grafadas com hífen, pois o segundo elemento de cada uma inicia-se por consoante.",
     "Quando o prefixo termina em vogal e o segundo elemento começa por R ou S, não há hífen e a consoante é dobrada."),
    ("C", "Os vocábulos ex-diretor, vice-presidente e recém-nascido exemplificam casos em que o hífen é obrigatório independentemente da letra que inicia o segundo elemento.",
     "Ex-, vice- e recém- sempre se ligam por hífen, assim como pós-, pré-, pró- (tônicos), além-, aquém- e sem-."),
    ("E", "A expressão “dia-a-dia”, quando empregada como substantivo com o sentido de cotidiano, deve ser grafada com hífen.",
     "Locuções com elemento de ligação perderam o hífen: dia a dia, em qualquer sentido."),
    ("C", "No período “A testemunha saiu há duas horas e voltará daqui a pouco”, as formas há e a estão empregadas corretamente.",
     "Há indica tempo passado (faz duas horas); a indica tempo futuro (daqui a pouco)."),
    ("E", "Em “A decisão do diretor veio de encontro aos interesses dos servidores, que a comemoraram”, a expressão “de encontro a” está empregada adequadamente.",
     "De encontro a indica oposição, choque. Como os servidores comemoraram, o adequado é ao encontro dos interesses (a favor)."),
    ("C", "As palavras super-homem e anti-higiênico recebem hífen porque o segundo elemento se inicia pela letra H.",
     "Diante de H, o prefixo sempre se liga por hífen."),
    ("E", "As formas coordenar, reeditar e preexistente estão em desacordo com a ortografia oficial, pois deveriam receber hífen em razão do encontro de vogais iguais.",
     "Os prefixos co-, re- e pre- (átono) aglutinam-se ao segundo elemento mesmo diante de vogal igual. As três formas estão corretas."),
], 20)

SOURCES = [
    "Acordo Ortográfico da Língua Portuguesa (1990), promulgado pelo Decreto nº 6.583, de 29 de setembro de 2008.",
    "Academia Brasileira de Letras — Vocabulário Ortográfico da Língua Portuguesa (VOLP).",
    "Gramáticas de referência: Bechara, Moderna gramática portuguesa; Cunha e Cintra, Nova gramática do português contemporâneo.",
    "Os 20 itens foram escritos para o Taticum. O Bloco B segue o padrão de cobrança da banca, mas não reproduz questões de provas.",
]
