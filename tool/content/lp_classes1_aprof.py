# -*- coding: utf-8 -*-
"""Língua Portuguesa · Substantivo, adjetivo, artigo e numeral — MATERIAL APROFUNDADO (estudo inicial)."""
from common import *

MATERIAL = material(
    "lp-classes1-02", "LP", "LP-03", "aprofundado", "Substantivo, adjetivo, artigo e numeral", "Língua Portuguesa · Morfologia",
    "portugues_classes1_aprofundado", "Portugues_Substantivo_Adjetivo_Artigo_Numeral_APROFUNDADO.pdf", None,
    ["Substantivo, adjetivo,", "artigo e numeral"],
    ["Teoria completa para o primeiro estudo das classes nominais: conceito, flexões e empregos", "que a banca cobra, com 20 questões no estilo Cebraspe e gabarito comentado."],
    [("01", "Panorama", "as dez classes de palavras e como reconhecê-las no texto"),
     ("02", "Substantivo", "classificação, gênero, número (inclusive compostos) e grau"),
     ("03", "Adjetivo", "locução adjetiva, flexão, graus e mudança de sentido"),
     ("04", "Artigo e numeral", "empregos que alteram o sentido da frase"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Classes de palavras — substantivo, adjetivo, artigo e numeral (Língua Portuguesa)",
    "Base: gramáticas de referência (Bechara; Cunha e Cintra).", 150)

THEORY = [
    exam("Como estudar este material",
         "O Cebraspe não pede definição de classe gramatical: pede que você **reconheça a classe de uma palavra dentro do texto** e avalie o "
         "que muda quando se troca, se retira ou se desloca um termo. Por isso, mais importante que decorar listas é entender o **critério**: "
         "a classe depende da **função que a palavra exerce na frase**. Leia, faça as 20 questões e revise pelo **PDF de resumo**."),

    h2("1. Panorama: as dez classes de palavras"),
    tb(["Classe", "O que faz", "Varia?"], [0.2, 0.62, 0.18], [
        ("Substantivo", "Nomeia seres, coisas, ações, estados, sentimentos", "Sim"),
        ("Adjetivo", "Caracteriza o substantivo", "Sim"),
        ("Artigo", "Determina o substantivo (definido ou indefinido)", "Sim"),
        ("Numeral", "Indica quantidade, ordem, múltiplo ou fração", "Sim"),
        ("Pronome", "Substitui ou acompanha o substantivo", "Sim"),
        ("Verbo", "Indica ação, estado ou fenômeno, situando-o no tempo", "Sim"),
        ("Advérbio", "Modifica verbo, adjetivo ou outro advérbio", "Não"),
        ("Preposição", "Liga palavras", "Não"),
        ("Conjunção", "Liga orações ou termos de mesma função", "Não"),
        ("Interjeição", "Exprime emoção", "Não"),
    ]),
    key("A classe depende do contexto",
        "A mesma palavra muda de classe conforme a frase. **O jantar** foi servido (substantivo) × Vamos **jantar** (verbo). "
        "Homem **alto** (adjetivo) × Falou **alto** (advérbio). **Um** livro qualquer (artigo) × Comprei **um** livro, não dois (numeral). "
        "Nunca classifique a palavra isolada: volte à frase."),

    h2("2. Substantivo"),
    p("**Substantivo** é a palavra que dá nome aos seres em geral: pessoas, lugares, objetos, instituições, ações, qualidades, estados e sentimentos. "
      "É o **núcleo** do sujeito, dos objetos e dos demais termos nominais da oração."),
    h3("Classificação"),
    tb(["Tipo", "Definição", "Exemplos"], [0.2, 0.46, 0.34], [
        ("Comum × próprio", "Nomeia todos os seres da espécie × um ser em particular", "cidade, rio × Brasília, Amazonas"),
        ("Concreto × abstrato", "Tem existência própria (real ou imaginária) × depende de outro ser para existir: ação, estado, qualidade, sentimento", "casa, ar, fada, Deus × prisão, beleza, saudade, coragem"),
        ("Simples × composto", "Um radical × mais de um", "chuva × guarda-chuva, passatempo"),
        ("Primitivo × derivado", "Não vem de outra palavra × vem", "pedra × pedreiro"),
        ("Coletivo", "No singular, indica conjunto de seres da mesma espécie", "quadrilha, frota, júri, arquipélago, elenco"),
    ]),
    trap("Pegadinha: concreto × abstrato",
         "Concreto não é “o que se pode tocar”. **Ar, alma, fada, saci, Deus** são concretos: são seres (reais ou imaginários) com existência "
         "independente. **Abstrato** é o nome de ação, estado ou qualidade, que só existe em outro ser: *a **corrida** do atleta, a **tristeza** do preso*."),
    h3("Substantivação"),
    p("Qualquer palavra passa a funcionar como substantivo quando vem **determinada por artigo, pronome ou numeral**: *o **não** dele foi firme; "
      "o **porquê** da demora; aquele **olhar**; os **prós** e os **contras**; o **azul** do céu.* É a chamada **derivação imprópria**, muito cobrada."),
    h3("Gênero"),
    tb(["Tipo", "Como funciona", "Exemplos"], [0.24, 0.4, 0.36], [
        ("Biforme", "Uma forma para cada gênero", "aluno/aluna; ator/atriz; réu/ré; cônsul/consulesa"),
        ("Comum de dois gêneros", "Uma só forma; o gênero aparece no artigo", "o/a agente, o/a policial, o/a colega, o/a estudante, o/a mártir"),
        ("Sobrecomum", "Uma só forma e um só gênero para os dois sexos", "a criança, a testemunha, a vítima, o cônjuge, o indivíduo, a pessoa"),
        ("Epiceno", "Animais com um só gênero (macho/fêmea)", "a cobra macho, o jacaré fêmea"),
    ]),
    tb(["São masculinos", "São femininos"], [0.5, 0.5], [
        ("o dó, o champanha, o eclipse, o guaraná, o telefonema, o grama (peso), o herpes, o formicida, o apêndice, o lança-perfume",
         "a alface, a cal, a dinamite, a omoplata, a musse, a comichão, a libido, a derme, a entorse, a aguardente"),
    ]),
    tb(["Masculino", "Feminino"], [0.5, 0.5], [
        ("**o capital** (dinheiro)", "**a capital** (cidade)"),
        ("**o cabeça** (líder)", "**a cabeça** (parte do corpo)"),
        ("**o moral** (ânimo)", "**a moral** (ética; conclusão)"),
        ("**o grama** (unidade de massa)", "**a grama** (vegetação)"),
        ("**o caixa** (funcionário; livro)", "**a caixa** (objeto)"),
        ("**o rádio** (aparelho)", "**a rádio** (emissora)"),
        ("**o guia** (pessoa; manual)", "**a guia** (documento)"),
    ]),
    h3("Número: regras do plural"),
    tb(["Terminação", "Plural", "Exemplos"], [0.24, 0.3, 0.46], [
        ("Vogal ou ditongo", "+ S", "casa/casas; pai/pais; troféu/troféus"),
        ("R, Z, N", "+ ES", "mar/mares; juiz/juízes; cânon/cânones (hífen: hifens)"),
        ("S (oxítonas e monossílabos)", "+ ES", "país/países; mês/meses; gás/gases"),
        ("S (paroxítonas e proparoxítonas) e X", "Invariável", "o lápis/os lápis; o ônibus/os ônibus; o tórax/os tórax"),
        ("AL, EL, OL, UL", "Troca L por IS", "jornal/jornais; papel/papéis; anzol/anzóis (exceções: mal/males; cônsul/cônsules)"),
        ("IL", "Oxítona: IS. Paroxítona: EIS", "fuzil/fuzis; funil/funis × fóssil/fósseis; réptil/répteis; projétil/projéteis"),
        ("M", "Troca por NS", "homem/homens; item/itens"),
        ("ÃO", "ÕES (maioria), ÃES ou ÃOS", "eleição/eleições; pão/pães, capitão/capitães, alemão/alemães, escrivão/escrivães, tabelião/tabeliães; mão/mãos, cidadão/cidadãos, irmão/irmãos, órgão/órgãos, cristão/cristãos"),
    ]),
    bl("**Só se usam no plural**: as algemas, os arredores, as férias, as núpcias, os óculos, os pêsames, os víveres, as costas (dorso).",
       "**Plural com mudança de timbre** (metafonia): ovo/ovos (ó), posto/postos (ó), esforço/esforços (ó), olho/olhos (ó). "
       "Mantêm o **ô** fechado: acordos, almoços, bolsos, esposos, gostos, rostos.",
       "**Diminutivos em -zinho**: passa-se a palavra para o plural, retira-se o S e acrescenta-se *-zinhos*: pão › pães › **pãezinhos**; "
       "flor › flores › **florezinhas**; animal › animais › **animaizinhos**; papel › papéis › **papeizinhos**."),
    h3("Plural dos substantivos compostos"),
    tb(["Estrutura", "Quem varia", "Exemplos"], [0.4, 0.2, 0.4], [
        ("Substantivo + substantivo; substantivo + adjetivo; adjetivo + substantivo; numeral + substantivo", "**Os dois**", "couves-flores, tenentes-coronéis, guardas-civis, cartões-postais, boas-vidas, segundas-feiras, primeiros-ministros"),
        ("Verbo + substantivo; palavra invariável + substantivo; palavras repetidas", "**Só o segundo**", "guarda-chuvas, beija-flores, porta-vozes, vice-presidentes, abaixo-assinados, ex-diretores, reco-recos, tique-taques"),
        ("Substantivo + preposição + substantivo", "**Só o primeiro**", "pés de moleque, mulas sem cabeça, pores do sol, águas-de-colônia"),
        ("2º substantivo indica finalidade, tipo ou semelhança", "**Só o primeiro** (admite-se os dois)", "navios-escola, bananas-prata, peixes-espada, salários-família (ou navios-escolas…)"),
        ("Verbo + palavra invariável; verbos de sentido oposto", "**Nenhum**", "os bota-fora, os leva e traz, os pisa-mansinho, os perde-ganha"),
    ]),
    trap("Pegadinha: guarda",
         "Em **guarda-chuvas, guarda-roupas, guarda-costas**, *guarda* é **verbo** e não varia. Em **guardas-civis, guardas-noturnos, "
         "guardas-florestais**, *guarda* é **substantivo** (a pessoa) e vai para o plural com o adjetivo."),
    h3("Grau"),
    bl("**Analítico** (com adjetivo): casa grande, casa pequena. **Sintético** (com sufixo): casarão, casinha.",
       "O grau pode exprimir **afeto** (paizinho, amigão) ou **desprezo** (gentinha, livreco, jornaleco) — valor que a banca explora em interpretação.",
       "Alguns aumentativos e diminutivos perderam a ideia de tamanho e viraram palavras independentes: cartão, portão, folhinha (calendário), cartilha."),

    h2("3. Adjetivo"),
    p("**Adjetivo** é a palavra que **caracteriza o substantivo**, atribuindo-lhe qualidade, estado, aspecto ou origem: *policial **experiente**, "
      "rua **deserta**, servidor **federal**, cidadão **brasileiro***. Concorda em gênero e número com o substantivo."),
    h3("Locução adjetiva"),
    p("Expressão formada, em geral, por **preposição + substantivo**, com valor de adjetivo. Muitas têm um adjetivo correspondente:"),
    tb(["Locução", "Adjetivo", "Locução", "Adjetivo"], [0.25, 0.25, 0.25, 0.25], [
        ("de pai / de mãe", "paterno / materno", "de chuva / de rio", "pluvial / fluvial"),
        ("de criança", "infantil, pueril", "de cidade / de campo", "urbano / rural, campestre"),
        ("de irmão", "fraterno, fraternal", "de guerra", "bélico"),
        ("de aluno / de professor", "discente / docente", "de morte", "letal, mortal"),
        ("de estômago / de fígado", "gástrico / hepático", "de olho / de ouvido", "ocular / auricular"),
        ("de lei / de juiz", "legal / judicial", "de prisão", "carcerário, prisional"),
        ("do Estado / do governo", "estatal / governamental", "de dinheiro", "pecuniário"),
        ("sem cheiro / sem sabor", "inodoro / insípido", "de idade", "etário"),
    ]),
    nt("Nem toda expressão com “de” é locução adjetiva. Em **a prisão do suspeito**, o termo tem valor de alvo da ação (o suspeito foi preso); "
       "em **a casa do suspeito**, indica posse. A diferença será decisiva no estudo de adjunto adnominal e complemento nominal."),
    h3("Flexão dos adjetivos compostos"),
    tb(["Caso", "Regra", "Exemplos"], [0.34, 0.26, 0.4], [
        ("Adjetivo + adjetivo", "Só o **último** varia", "questões político-sociais, acordos luso-brasileiros, clínicas médico-cirúrgicas, olhos verde-claros"),
        ("Cor + **substantivo**", "**Invariável**", "camisas verde-garrafa, blusas amarelo-ouro, tons azul-piscina, paredes cinza-chumbo"),
        ("Cor expressa por substantivo", "**Invariável**", "ternos cinza, blusas rosa, carros vinho, sapatos gelo, tons pastel"),
        ("azul-marinho, azul-celeste", "**Invariáveis**", "uniformes azul-marinho"),
        ("surdo-mudo", "**Os dois** variam", "crianças surdas-mudas"),
    ]),
    h3("Grau do adjetivo"),
    tb(["Grau", "Forma", "Exemplo"], [0.32, 0.3, 0.38], [
        ("Comparativo de igualdade", "tão … quanto (ou como)", "É tão ágil quanto o colega."),
        ("Comparativo de superioridade", "mais … (do) que", "É mais ágil (do) que o colega."),
        ("Comparativo de inferioridade", "menos … (do) que", "É menos ágil (do) que o colega."),
        ("Superlativo absoluto analítico", "muito, extremamente + adjetivo", "É muito ágil."),
        ("Superlativo absoluto sintético", "adjetivo + sufixo", "É agilíssimo."),
        ("Superlativo relativo", "o mais / o menos … de", "É o mais ágil da equipe."),
    ]),
    bl("**Comparativos e superlativos irregulares**: bom › **melhor**, **ótimo**; mau › **pior**, **péssimo**; grande › **maior**, **máximo**; "
       "pequeno › **menor**, **mínimo**.",
       "Usa-se **mais bom, mais mau, mais grande, mais pequeno** quando se comparam **duas qualidades do mesmo ser**: "
       "*Ele é mais bom do que inteligente. A sala é mais grande do que confortável.*",
       "**Superlativos eruditos**: amigo › amicíssimo; antigo › antiquíssimo; célebre › celebérrimo; cruel › crudelíssimo; difícil › dificílimo; "
       "doce › dulcíssimo; fácil › facílimo; fiel › fidelíssimo; humilde › humílimo; livre › libérrimo; magro › macérrimo; nobre › nobilíssimo; "
       "pobre › paupérrimo; sábio › sapientíssimo; sagrado › sacratíssimo; simples › simplicíssimo; feio › feiíssimo; sério › seriíssimo."),
    h3("Posição do adjetivo e mudança de sentido"),
    tb(["Depois do substantivo (sentido próprio)", "Antes do substantivo (sentido figurado ou afetivo)"], [0.5, 0.5], [
        ("homem **pobre** (sem recursos)", "**pobre** homem (digno de pena)"),
        ("homem **grande** (alto)", "**grande** homem (notável)"),
        ("amigo **velho** (idoso)", "**velho** amigo (de longa data)"),
        ("funcionário **simples** (modesto)", "**simples** funcionário (mero)"),
        ("notícia **certa** (correta)", "**certa** notícia (uma qualquer — passa a pronome indefinido)"),
        ("oficial **alto** (de estatura)", "**alto** oficial (de posto elevado)"),
    ]),
    h3("Adjetivo × advérbio"),
    p("O adjetivo refere-se a **substantivo** e **varia**; o advérbio refere-se a **verbo, adjetivo ou advérbio** e **não varia**. "
      "*Elas falaram **alto*** (advérbio: modo de falar). *Elas são **altas*** (adjetivo). *A cerveja que desce **redondo***. "
      "*Vendeu **caro** as joias* (advérbio) × *As joias são **caras*** (adjetivo). Teste: tente pôr no plural ou no feminino."),

    h2("4. Artigo"),
    p("**Artigo** é a palavra que antecede o substantivo para **determiná-lo**: de modo preciso (**definido**: o, a, os, as) ou vago "
      "(**indefinido**: um, uma, uns, umas). Combina-se com preposições: *do, no, pelo, ao, à, num, dum*."),
    tb(["Emprego", "Efeito", "Exemplo"], [0.3, 0.36, 0.34], [
        ("Definido", "Ser já conhecido ou único; retomada de algo mencionado", "Prenderam **o** suspeito (aquele de que já se falou)."),
        ("Indefinido", "Ser qualquer, ainda não mencionado; também aproximação e realce", "Prenderam **um** suspeito. Eram **uns** vinte homens. Foi **uma** confusão!"),
        ("**todo o** × **todo**", "Com artigo = inteiro. Sem artigo = qualquer, cada", "**Todo o** país parou (o país inteiro). **Todo** país tem leis (qualquer país)."),
        ("Antes de possessivo", "**Facultativo**", "Vi **(a)** sua casa. Por isso a crase também é facultativa: *Fui a/à sua casa.*"),
        ("Antes de nome de pessoa", "Indica intimidade; evita-se em contexto formal", "**O** Pedro chegou."),
        ("Depois de **cujo**", "**Proibido**", "O réu **cujo** advogado faltou (nunca “cujo o”)."),
        ("Depois de **ambos**", "**Obrigatório**", "**Ambos os** policiais."),
        ("Substantivação", "Transforma qualquer palavra em substantivo", "**O** cantar dos pássaros; **um** não."),
    ]),
    trap("Pegadinha: retirar o artigo",
         "A banca pergunta se a supressão do artigo “mantém a correção e o sentido”. Em geral mantém a **correção**, mas altera o **sentido** "
         "(de definido para genérico). E, se o artigo estiver fundido em uma crase (*à*), retirá-lo elimina também o acento grave."),

    h2("5. Numeral"),
    p("**Numeral** é a palavra que indica **quantidade exata**, **ordem**, **multiplicação** ou **fração**."),
    tb(["Tipo", "Indica", "Exemplos"], [0.24, 0.3, 0.46], [
        ("Cardinal", "Quantidade", "um, dois, cem, mil, milhão"),
        ("Ordinal", "Posição em uma série", "primeiro, décimo, vigésimo, centésimo, milésimo"),
        ("Multiplicativo", "Múltiplo", "dobro (duplo), triplo, quádruplo"),
        ("Fracionário", "Parte", "meio, terço, quarto, onze avos"),
        ("Coletivo", "Conjunto de quantidade exata", "dúzia, dezena, centena, década, século, par"),
    ]),
    h3("Empregos que caem"),
    bl("**Papas, reis, séculos e capítulos**: ordinal **até décimo**; cardinal **de onze em diante**, quando o numeral vem depois do substantivo — "
       "*João Paulo II (segundo), Pio X (décimo), Luís XIV (catorze), século V (quinto), século XXI (vinte e um), capítulo XII (doze).*",
       "**Artigos de lei, decretos e portarias**: ordinal **até nove**; cardinal **de dez em diante** — *artigo 5º (quinto), artigo 9º (nono), "
       "artigo 10 (dez), artigo 121 (cento e vinte e um).*",
       "**Primeiro dia do mês**: ordinal — *1º de janeiro*. Os demais, cardinal.",
       "**Um**: é **numeral** quando indica quantidade (opõe-se a dois, três; aceita *só, apenas*) e **artigo indefinido** quando indica imprecisão "
       "(opõe-se a *o*).",
       "**Milhão, bilhão, milhar** são **masculinos**: *dois milhões de pessoas; os milhares de vítimas* (nunca “as milhares”).",
       "**Ambos** equivale a *os dois* e é numeral; a forma *ambos os dois* é redundância a evitar em texto formal.",
       "**Meio** é numeral quando significa *metade* e concorda com o substantivo (*meia garrafa, meio-dia e meia [hora]*); "
       "é advérbio quando significa *um pouco* e fica invariável (*ela está meio cansada*).",
       "**Flexão**: um/uma, dois/duas, e as centenas a partir de duzentos (*duzentas páginas, trezentas mil pessoas*). "
       "Ordinais variam em gênero e número (*primeira, primeiros*).",
       "**Escrita por extenso**: usa-se **e** entre centenas, dezenas e unidades (*trezentos e quarenta e dois*); "
       "não se usa *e* entre milhar e centena, salvo se a centena terminar em dois zeros ou vier sozinha (*mil duzentos e trinta; mil e duzentos; dois mil e dez*)."),

    h2("6. Como o Cebraspe cobra"),
    bl("**Classificação no contexto**: “o vocábulo X, na linha Y, classifica-se como adjetivo”. Veja a que palavra ele se refere.",
       "**Substantivação**: “o termo X está empregado como substantivo” — procure o artigo ou o determinante.",
       "**Supressão ou inserção de artigo**: efeito no sentido (definido × genérico; *todo o* × *todo*) e na crase.",
       "**Deslocamento do adjetivo**: “a anteposição do adjetivo manteria o sentido” — lembre *homem pobre* × *pobre homem*.",
       "**Flexão de compostos** e de adjetivos de cor em itens de reescrita no plural.",
       "**Valor do grau**: diminutivo afetivo ou depreciativo, superlativo como recurso de ênfase.",
       "**Adjetivo × advérbio**: palavra invariável ligada ao verbo é advérbio."),
]

QUIZ = quiz([
    ("C", "Em “O olhar do investigador revelava desconfiança”, o vocábulo olhar está empregado como substantivo.",
     "Vem determinado por artigo e é núcleo do sujeito: caso de substantivação."),
    ("E", "Os substantivos saudade, coragem e prisão classificam-se como concretos, pois designam realidades que podem ser percebidas pelas pessoas.",
     "São abstratos: nomeiam sentimento, qualidade e ação, que dependem de outro ser para existir."),
    ("C", "O substantivo testemunha é sobrecomum, pois apresenta uma só forma e um só gênero para designar pessoas de ambos os sexos.",
     "A testemunha (homem ou mulher). O mesmo ocorre com a vítima, a criança, o cônjuge."),
    ("E", "O plural de guarda-civil é guarda-civis, pois, nos compostos iniciados por guarda, apenas o segundo elemento varia.",
     "Em guarda-civil, guarda é substantivo e civil é adjetivo: variam os dois — guardas-civis. Só o segundo varia quando guarda é verbo: guarda-chuvas."),
    ("C", "Estão corretas as formas de plural cidadãos, escrivães e eleições.",
     "São os três plurais possíveis das palavras em -ão: -ãos, -ães e -ões."),
    ("E", "Na frase “As agentes compraram blusas verde-garrafas”, o adjetivo composto está corretamente flexionado.",
     "Quando o segundo elemento do adjetivo de cor é substantivo, o composto fica invariável: blusas verde-garrafa."),
    ("C", "Em “Ele é mais bom do que esperto”, o emprego de mais bom está correto, pois se comparam duas qualidades do mesmo ser.",
     "Nesse caso não se usa a forma sintética melhor."),
    ("E", "Em “Todo o país acompanhou o julgamento”, a supressão do artigo o manteria o sentido original do período.",
     "Todo o país = o país inteiro. Todo país = qualquer país. A supressão altera o sentido."),
    ("C", "Em “As testemunhas falaram baixo durante o depoimento”, o vocábulo baixo é advérbio e, por isso, permanece invariável.",
     "Refere-se ao verbo falar (modo), não a um substantivo."),
    ("E", "A leitura correta de “artigo 10 do Código Penal” é “artigo décimo”.",
     "Em artigos de lei, usa-se o ordinal até o nono e o cardinal de dez em diante: artigo dez."),

    ("C", "Em “O não do delegado encerrou a discussão”, a palavra não, originalmente advérbio, está substantivada.",
     "O artigo o transforma o advérbio em substantivo (derivação imprópria)."),
    ("E", "Em “Trata-se de um pobre homem”, a posposição do adjetivo ao substantivo (“homem pobre”) preservaria o sentido original.",
     "Pobre homem = digno de pena; homem pobre = sem recursos. O deslocamento altera o sentido."),
    ("C", "A expressão “de chuva”, em “águas de chuva”, tem valor adjetivo e poderia ser substituída por pluviais.",
     "É locução adjetiva, equivalente ao adjetivo pluvial."),
    ("E", "No trecho “o réu cujo o advogado renunciou”, o emprego do artigo após o pronome cujo está de acordo com a norma-padrão.",
     "Não se usa artigo depois de cujo: o réu cujo advogado renunciou."),
    ("C", "Em “Havia uns trinta manifestantes no local”, o vocábulo uns exprime ideia de aproximação.",
     "O artigo indefinido antes de numeral indica quantidade aproximada."),
    ("E", "O substantivo capital apresenta o mesmo sentido em “o capital da empresa” e “a capital do estado”.",
     "O capital = recursos, dinheiro; a capital = cidade-sede. A mudança de gênero altera o sentido."),
    ("C", "Em “As milhares de pessoas presentes aplaudiram”, há desvio de concordância, pois o numeral milhar é masculino.",
     "O correto é os milhares de pessoas."),
    ("E", "Em “Ela ficou meia confusa com as perguntas”, o emprego de meia está correto, por concordar com o pronome ela.",
     "Com o sentido de um pouco, meio é advérbio e não varia: meio confusa."),
    ("C", "Na expressão “questões político-econômicas”, apenas o segundo elemento do adjetivo composto está flexionado, em conformidade com a norma-padrão.",
     "Em adjetivos compostos formados por dois adjetivos, só o último varia."),
    ("E", "O diminutivo em “Aquele jornalzinho só publica boatos” indica exclusivamente o tamanho reduzido do jornal.",
     "No contexto, o diminutivo tem valor depreciativo, e não de tamanho."),
], 20)

SOURCES = [GRAM, "Acordo Ortográfico da Língua Portuguesa (grafia dos compostos) e VOLP (Academia Brasileira de Letras).", SRC_A]
