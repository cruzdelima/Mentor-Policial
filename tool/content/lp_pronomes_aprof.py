# -*- coding: utf-8 -*-
"""Língua Portuguesa · Pronomes: emprego e colocação — MATERIAL APROFUNDADO (estudo inicial)."""
from common import *

MATERIAL = material(
    "lp-pronomes-02", "LP", "LP-04", "aprofundado", "Pronomes: emprego e colocação", "Língua Portuguesa · Morfossintaxe",
    "portugues_pronomes_aprofundado", "Portugues_Pronomes_APROFUNDADO.pdf", None, ["Pronomes:", "emprego e colocação"],
    ["Teoria completa para o primeiro estudo: tipos de pronome, emprego de cada um e as regras", "de próclise, mesóclise e ênclise, com 20 questões no estilo Cebraspe."],
    [("01", "Pessoais", "retos, oblíquos e de tratamento"),
     ("02", "Demais tipos", "possessivos, demonstrativos, relativos, indefinidos e interrogativos"),
     ("03", "Referência", "o pronome como elemento de coesão"),
     ("04", "Colocação", "próclise, mesóclise, ênclise e locuções verbais"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Pronomes — emprego e colocação pronominal (Língua Portuguesa)",
    "Base: gramáticas de referência e Manual de Redação da Presidência da República (3ª edição).", 150)

THEORY = [
    exam("Como estudar este material",
         "Pronome é um dos assuntos mais rentáveis de Português no Cebraspe, porque aparece em três tipos de item: **referência** "
         "(“o pronome X retoma Y”), **emprego** (*o* × *lhe*, *este* × *esse*, *cujo*, *onde*) e **colocação** "
         "(“a posposição do pronome manteria a correção”). Estude nessa ordem, faça as 20 questões e revise pelo **PDF de resumo**."),

    h2("1. O que é pronome"),
    p("**Pronome** é a palavra que **substitui** ou **acompanha** o substantivo, relacionando-o a uma das pessoas do discurso: quem fala (1ª), "
      "com quem se fala (2ª) e de quem ou de que se fala (3ª)."),
    bl("**Pronome substantivo**: ocupa o lugar do nome — ***Ele** chegou. **Isso** é grave. **Alguém** ligou.*",
       "**Pronome adjetivo**: acompanha o nome — ***Meu** colega chegou. **Este** caso é grave. **Algum** vizinho ligou.*"),

    h2("2. Pronomes pessoais"),
    tb(["Pessoa", "Retos (sujeito)", "Oblíquos átonos (sem preposição)", "Oblíquos tônicos (com preposição)"], [0.16, 0.22, 0.32, 0.3], [
        ("1ª singular", "eu", "me", "mim, comigo"),
        ("2ª singular", "tu", "te", "ti, contigo"),
        ("3ª singular", "ele, ela", "o, a, lhe, se", "ele, ela, si, consigo"),
        ("1ª plural", "nós", "nos", "nós, conosco"),
        ("2ª plural", "vós", "vos", "vós, convosco"),
        ("3ª plural", "eles, elas", "os, as, lhes, se", "eles, elas, si, consigo"),
    ]),
    h3("Reto × oblíquo"),
    bl("Os **retos** funcionam como **sujeito** (ou predicativo); os **oblíquos**, como **complemento**.",
       "**Para eu fazer** × **para mim**: usa-se *eu* quando o pronome é **sujeito de um verbo no infinitivo** — *Trouxeram o relatório para **eu** assinar.* "
       "Sem verbo, usa-se *mim* — *Trouxeram o relatório para **mim**.*",
       "**Entre mim e ti / entre mim e ele**: depois de preposição, usam-se as formas oblíquas tônicas — *Não há segredos entre **mim** e **ti**.* "
       "(e não “entre eu e tu”).",
       "**Com nós × conosco**: usa-se *com nós* quando vem seguido de palavra de reforço (*mesmos, próprios, todos, dois, que*) — "
       "*Falou **com nós dois**. Falou **conosco**.*",
       "**Si e consigo** são **reflexivos**: referem-se ao próprio sujeito — *Ele só pensa em **si**. Levou os documentos **consigo**.* "
       "Não se usam para o interlocutor (“quero falar consigo” é desvio no padrão brasileiro)."),
    h3("O, a, os, as × lhe, lhes"),
    tb(["Pronome", "Função", "Exemplo"], [0.22, 0.38, 0.4], [
        ("o, a, os, as", "**Objeto direto** (verbo sem preposição)", "Prendi o suspeito › Prendi-**o**."),
        ("lhe, lhes", "**Objeto indireto** (verbo com preposição *a* ou *para*), em regra referente a pessoa", "Obedeço ao chefe › Obedeço-**lhe**. Entreguei o laudo ao juiz › Entreguei-**lhe** o laudo."),
        ("me, te, se, nos, vos", "Objeto direto **ou** indireto", "Viu-**me** (OD). Obedeceu-**me** (OI)."),
        ("lhe com valor possessivo", "Equivale a *seu, dele*", "Roubaram-**lhe** a carteira (= a carteira dele)."),
    ]),
    tb(["Verbo termina em", "O pronome o(s), a(s) vira", "Exemplos"], [0.26, 0.3, 0.44], [
        ("R, S ou Z", "**lo, la, los, las** (a consoante cai)", "prender + o = prendê-**lo**; fiz + a = fi-**la**; conduzimos + os = conduzimo-**los**"),
        ("Som nasal (M, ÃO, ÕE)", "**no, na, nos, nas**", "prenderam + o = prenderam-**no**; dão + as = dão-**nas**; põe + o = põe-**no**"),
        ("Outras terminações", "o, a, os, as", "prendi-**o**, encontrei-**a**"),
    ]),
    trap("Pegadinha: “vi ele”, “lhe vi”",
         "No padrão formal, **ele/ela não funcionam como objeto direto**: *Vi-**o*** (e não “vi ele”). E **lhe não substitui objeto direto**: "
         "*Eu **o** vi* (e não “eu lhe vi”); *Eu **a** convidei* (e não “lhe convidei”). Teste: se o verbo não pede preposição, use *o/a*."),
    h3("Pronomes de tratamento"),
    bl("Referem-se à **2ª pessoa** (com quem se fala), mas levam verbo e pronomes para a **3ª pessoa**: "
       "*Vossa Excelência **deve** apresentar **seu** relatório* (e não “vosso”).",
       "**Vossa** para falar **com** a autoridade; **Sua** para falar **da** autoridade: *Vossa Excelência decidiu?* × *Sua Excelência, o Ministro, decidiu.*",
       "A concordância de gênero se faz com o **sexo da pessoa**: *Vossa Excelência está **atarefado*** (homem) / ***atarefada*** (mulher).",
       "**Vossa Excelência**: altas autoridades dos três Poderes. **Vossa Senhoria**: demais autoridades e particulares. "
       "**Você** é pronome de tratamento e também pede verbo na 3ª pessoa.",
       "O Manual de Redação da Presidência (3ª ed.) **aboliu** os vocativos e fechos rebuscados: não se usam *digníssimo* nem *ilustríssimo*; "
       "*doutor* não é forma de tratamento, e sim título acadêmico."),

    h2("3. Pronomes possessivos"),
    p("Indicam posse em relação às pessoas do discurso: **meu, teu, seu, nosso, vosso** e flexões."),
    bl("**Ambiguidade de *seu***: *O delegado disse ao escrivão que **seu** relatório estava incompleto* (de quem?). "
       "Desfaz-se com **dele, dela** ou reescrevendo a frase. O Cebraspe cobra tanto a identificação da ambiguidade quanto a solução.",
       "Antes de possessivo, o **artigo é facultativo**: *(a) minha casa*.",
       "Com partes do corpo, peças de roupa e faculdades do espírito, dispensa-se o possessivo: *Machucou **a** mão* (e não “a sua mão”).",
       "O possessivo pode indicar aproximação (*tem seus quarenta anos*) ou afeto (*meu caro amigo*)."),

    h2("4. Pronomes demonstrativos"),
    tb(["Pronome", "Espaço", "Tempo", "Texto"], [0.22, 0.26, 0.24, 0.28], [
        ("**este, esta, isto**", "Perto de quem fala", "Presente", "O que **ainda vai ser dito** (catáfora)"),
        ("**esse, essa, isso**", "Perto de com quem se fala", "Passado ou futuro próximos", "O que **já foi dito** (anáfora)"),
        ("**aquele, aquela, aquilo**", "Longe dos dois", "Passado distante", "Termo mais distante, em oposição a *este*"),
    ]),
    bl("*A ordem é **esta**: ninguém sai.* (anuncia) × *Ninguém sai: **essa** é a ordem.* (retoma)",
       "Na retomada de **dois termos**, **este** refere-se ao **mais próximo** (o último citado) e **aquele**, ao **mais distante** (o primeiro): "
       "*Agentes e escrivães foram convocados; **estes** [escrivães] para os cartórios, **aqueles** [agentes] para as ruas.*",
       "**O, a, os, as** são demonstrativos quando equivalem a *aquele(s), aquela(s), aquilo, isso*: ***O** que ele disse é falso* (= aquilo que); "
       "*Não **o** disse* (= isso); *Das provas, só aceitou **as** que eram lícitas* (= aquelas).",
       "Também funcionam como demonstrativos **mesmo, próprio, tal, semelhante**: *Não diga **tal** coisa.* "
       "Evite *o mesmo* como substituto de *ele*: “o réu chegou e o mesmo foi ouvido” é construção condenada."),

    h2("5. Pronomes relativos"),
    p("Retomam um termo anterior (o **antecedente**) e introduzem **oração subordinada adjetiva**: **que, quem, o qual, cujo, onde, quanto, como**."),
    tb(["Relativo", "Emprego", "Exemplo"], [0.18, 0.44, 0.38], [
        ("que", "Universal: pessoa ou coisa", "O agente **que** fez a prisão."),
        ("quem", "Só pessoa; sempre precedido de preposição quando tem antecedente", "A testemunha **a quem** me referi."),
        ("o qual (e flexões)", "Pessoa ou coisa; evita ambiguidade; obrigatório depois de preposições de duas ou mais sílabas e locuções", "A lei **segundo a qual**…; o prazo **durante o qual**…"),
        ("cujo (e flexões)", "Indica **posse**; fica entre possuidor e possuído; concorda com o **possuído**; **não admite artigo** depois", "O réu **cuja** defesa foi rejeitada."),
        ("onde", "Só para **lugar físico** (= em que, no qual)", "A cidade **onde** nasci."),
        ("quanto", "Depois de *tudo, todos, tanto*", "Tudo **quanto** disse foi anotado."),
    ]),
    key("A preposição vem antes do relativo",
        "Se o verbo (ou o nome) da oração adjetiva pede preposição, ela aparece **antes do pronome relativo**: "
        "*o filme **a que** assisti* (assistir a); *a pessoa **de quem** gosto* (gostar de); *o cargo **a que** aspiro* (aspirar a); "
        "*a lei **a que** obedeço* (obedecer a); *o livro **de cujo** autor falei* (falar de); *o colega **em cuja** casa estive* (estar em)."),
    trap("Pegadinha: onde e cujo",
         "**Onde** só retoma lugar: “a situação onde”, “o momento onde”, “o processo onde” são desvios (use **em que** ou **no qual**). "
         "**Aonde** só com verbo de movimento que pede *a*: *o lugar aonde vou*. "
         "**Cujo** não pode ser trocado por “que o” nem seguido de artigo: “o réu que o advogado dele” e “cujo o advogado” estão errados."),

    h2("6. Pronomes indefinidos e interrogativos"),
    bl("**Indefinidos** referem-se à 3ª pessoa de modo vago: *algum, nenhum, todo, muito, pouco, certo, vários, qualquer, outro, tanto, alguém, "
       "ninguém, tudo, nada, cada, algo, outrem*.",
       "**Algum** depois do substantivo tem valor **negativo**: *Não recebeu ajuda **alguma*** (= nenhuma).",
       "**Certo** antes do substantivo é pronome indefinido (***certo** dia*); depois, é adjetivo (*o dia **certo***).",
       "**Todo o** (inteiro) × **todo** (qualquer). **Nenhum** (pronome) × **nem um** (nem um sequer, numeral).",
       "**Cada** não se usa sozinho no padrão formal: *Custam dez reais **cada um*** (e não “dez reais cada”).",
       "**Qualquer** tem plural **quaisquer**. **Bastante** é pronome quando acompanha substantivo e varia: ***bastantes** provas* (= muitas).",
       "**Interrogativos**: *que, quem, qual, quanto*, em perguntas diretas ou indiretas — ***Quem** assinou? Não sei **quem** assinou.*"),

    h2("7. O pronome como elemento de coesão"),
    p("Grande parte dos itens do Cebraspe pergunta **a que termo o pronome se refere**. O pronome pode retomar algo já dito (**anáfora**) ou "
      "anunciar algo que virá (**catáfora**)."),
    bl("**Método**: troque o pronome pelo termo que a banca indicou e releia a frase. Se o sentido se mantiver, é o referente.",
       "Confira a **concordância**: *o(s), a(s), ele(s), ela(s)* concordam em gênero e número com o referente; isso elimina candidatos.",
       "Pronomes como **isso, isto, o** (= isso) podem retomar **uma oração ou uma ideia inteira**, não só uma palavra: "
       "*O suspeito negou o crime, mas ninguém acreditou **nisso**.*",
       "O **relativo** retoma o termo imediatamente anterior — cuidado quando há dois candidatos: *o filho do delegado **que** chegou* (ambíguo); "
       "*o filho do delegado, **o qual** chegou* (o filho); *a filha do delegado, **o qual** chegou* (o delegado)."),

    h2("8. Colocação pronominal"),
    p("Trata da posição dos **pronomes oblíquos átonos** (*me, te, se, o, a, lhe, nos, vos, os, as, lhes*) em relação ao verbo."),
    tb(["Posição", "Nome", "Exemplo"], [0.3, 0.2, 0.5], [
        ("Antes do verbo", "**Próclise**", "Não **me** disseram a verdade."),
        ("No meio do verbo", "**Mesóclise**", "Dir-**me**-ão a verdade."),
        ("Depois do verbo", "**Ênclise**", "Disseram-**me** a verdade."),
    ]),
    h3("Próclise: quando há palavra atrativa"),
    tb(["Atrai o pronome", "Exemplos"], [0.42, 0.58], [
        ("Palavra **negativa** (não, nunca, jamais, ninguém, nada, nem)", "**Não se** esqueça. **Ninguém me** avisou."),
        ("**Advérbio** (sem vírgula depois)", "**Hoje se** sabe a verdade. **Sempre me** ajudou. **Aqui se** trabalha."),
        ("Pronome **relativo**", "O agente **que me** atendeu. O local **onde se** escondeu."),
        ("Pronome **indefinido** e **demonstrativo** neutro", "**Tudo se** resolve. **Alguém me** chamou. **Isso me** preocupa."),
        ("**Conjunção subordinativa**", "**Quando me** viu, fugiu. **Embora se** esforce… Disse **que se** atrasaria."),
        ("Pronome ou advérbio **interrogativo**", "**Quem te** contou? **Por que se** calou?"),
        ("Frases **exclamativas** e **optativas**", "**Deus te** proteja! **Como se** enganou!"),
        ("**Em + gerúndio**", "**Em se** tratando de provas…"),
    ]),
    h3("Mesóclise"),
    p("Só ocorre com verbo no **futuro do presente** ou no **futuro do pretérito**, quando **não há palavra atrativa**: "
      "*Realizar-**se**-á a audiência. Dir-**lhe**-ia a verdade.* Havendo atração, a próclise é obrigatória: *Não **se** realizará a audiência.*"),
    h3("Ênclise"),
    bl("No **início da frase** ou depois de pausa: *Entregaram-**me** o laudo.* No padrão formal, **não se inicia frase com pronome oblíquo átono**.",
       "Com **imperativo afirmativo**: *Sente-**se**. Diga-**me** a verdade.*",
       "Com **gerúndio** (sem *em*): *Saiu, deixando-**nos** preocupados.*",
       "Com **infinitivo impessoal**: *Era preciso avisá-**lo**.*"),
    key("Duas proibições absolutas",
        "**Nunca** se usa ênclise com verbo no **futuro** (“farei-o”, “diria-me” estão errados: *fá-lo-ei* ou *eu o farei*; *dir-me-ia* ou *ele me diria*). "
        "**Nunca** se usa ênclise com **particípio** (“tinha dado-me” está errado: *tinha-me dado* ou *me tinha dado*)."),
    h3("Casos facultativos"),
    bl("**Sujeito expresso** antes do verbo, sem palavra atrativa: próclise ou ênclise — *O delegado **me** chamou* / *O delegado chamou-**me**.*",
       "**Conjunção coordenativa**: *Chegou e **se** sentou* / *Chegou e sentou-**se**.*",
       "**Infinitivo** precedido de preposição ou de palavra atrativa: *Para não **o** incomodar* / *Para não incomodá-**lo**.*"),
    h3("Locuções verbais"),
    tb(["Estrutura", "Sem palavra atrativa", "Com palavra atrativa"], [0.28, 0.36, 0.36], [
        ("Auxiliar + **infinitivo** ou **gerúndio**", "Devo-**lhe** dizer. / Devo dizer-**lhe**. Estava-**me** esperando. / Estava esperando-**me**.", "Não **lhe** devo dizer. / Não devo dizer-**lhe**."),
        ("Auxiliar + **particípio**", "Tinha-**me** avisado. (pronome junto ao **auxiliar**)", "Não **me** tinha avisado."),
    ]),
    nt("No português do Brasil, é comum o pronome solto entre os dois verbos, sem hífen (*devo lhe dizer*). Gramáticos modernos aceitam a construção; "
       "em prova, prefira as formas do quadro, e nunca ligue o pronome ao particípio."),

    h2("9. Como o Cebraspe cobra"),
    bl("**Referência**: “o pronome X (l. 12) retoma Y”. Substitua e confira concordância e sentido.",
       "**Substituição de complemento por pronome**: “o termo destacado poderia ser substituído por *lhe*” — veja se o verbo pede preposição.",
       "**Colocação**: “o pronome poderia ser deslocado para depois do verbo” — procure a palavra atrativa. Se houver, o item está errado.",
       "**Relativos**: troca de *onde* por *em que* (correta para lugar), de *que* por *o qual* (correta se a concordância for mantida), "
       "e supressão da preposição antes do relativo (incorreta).",
       "**Demonstrativos**: troca de *esse* por *este* em retomadas — a banca costuma considerar que a troca **prejudica a coesão** quando o termo já foi citado.",
       "**Tratamento**: concordância na 3ª pessoa e uso de *Vossa* × *Sua*."),
]

QUIZ = quiz([
    ("C", "Em “O relatório foi entregue para eu revisar”, o emprego do pronome eu está correto, pois ele funciona como sujeito do verbo revisar.",
     "Antes de infinitivo, como sujeito, usa-se o pronome reto. Sem o verbo, seria para mim."),
    ("E", "Está de acordo com a norma-padrão a frase “Não há divergências entre eu e o diretor”.",
     "Depois de preposição, usa-se a forma oblíqua tônica: entre mim e o diretor."),
    ("C", "Em “O agente encontrou o foragido e conduziu-o à delegacia”, o pronome o exerce a função de objeto direto.",
     "Conduzir alguém: verbo transitivo direto; o pronome retoma o foragido."),
    ("E", "Na frase “Eu lhe vi ontem no fórum”, o pronome lhe está empregado de acordo com a norma-padrão.",
     "Ver é transitivo direto: Eu o vi (ou a vi). Lhe substitui objeto indireto."),
    ("C", "A junção da forma verbal prenderam com o pronome o resulta em prenderam-no.",
     "Depois de som nasal, o pronome assume as formas no, na, nos, nas."),
    ("E", "Em “Vossa Excelência deveis apresentar vosso parecer”, a concordância com o pronome de tratamento está correta.",
     "Pronomes de tratamento levam verbo e possessivo para a 3ª pessoa: Vossa Excelência deve apresentar seu parecer."),
    ("C", "Em “O servidor cuja ficha foi analisada será promovido”, o pronome cuja estabelece relação de posse e concorda com o substantivo ficha.",
     "Cujo concorda com o termo possuído e fica entre possuidor (servidor) e possuído (ficha)."),
    ("E", "Em “Vivemos um momento onde a prudência é necessária”, o pronome onde está empregado de acordo com a norma-padrão.",
     "Onde só retoma lugar físico. O adequado é em que ou no qual."),
    ("C", "Em “Não me informaram o horário”, a próclise é obrigatória em razão da presença de palavra negativa.",
     "O advérbio não atrai o pronome para antes do verbo."),
    ("E", "A frase “Farei-o assim que possível” apresenta colocação pronominal correta.",
     "Não se usa ênclise com futuro: Fá-lo-ei ou Eu o farei."),

    ("C", "Em “O delegado disse ao escrivão que seu relatório estava incompleto”, o emprego do pronome seu gera ambiguidade.",
     "Não se sabe se o relatório é do delegado ou do escrivão."),
    ("E", "Em “Quando se constatou a fraude, a auditoria foi ampliada”, o pronome se poderia ser deslocado para depois da forma verbal, sem prejuízo para a correção gramatical.",
     "A conjunção subordinativa quando atrai o pronome: a próclise é obrigatória."),
    ("C", "No trecho “Peritos e escrivães participaram da operação: estes cuidaram dos registros, e aqueles, dos vestígios”, o pronome estes retoma escrivães.",
     "Na retomada de dois termos, este refere-se ao mais próximo, e aquele, ao mais distante (peritos)."),
    ("E", "No período “Este é o documento que me referi na reunião”, a regência do verbo está respeitada.",
     "Referir-se a: a preposição deve anteceder o relativo — o documento a que me referi."),
    ("C", "Em “O que ele declarou foi registrado”, o vocábulo o é pronome demonstrativo e equivale a aquilo.",
     "Antes do relativo que, o pode ser demonstrativo: aquilo que ele declarou."),
    ("E", "Em “Tinha informado-me do prazo”, o pronome está corretamente colocado, visto que não há palavra atrativa.",
     "Não se usa ênclise com particípio. O pronome liga-se ao auxiliar: Tinha-me informado."),
    ("C", "Em “Devo dizer-lhe a verdade”, o pronome poderia ser colocado depois do verbo auxiliar (“Devo-lhe dizer a verdade”), mantendo-se a correção gramatical.",
     "Em locução com infinitivo, sem palavra atrativa, o pronome pode vir depois do auxiliar ou depois do verbo principal."),
    ("E", "Em “Não recebeu apoio algum da chefia”, o pronome algum tem sentido afirmativo e equivale a certo apoio.",
     "Posposto ao substantivo, algum tem valor negativo: equivale a nenhum."),
    ("C", "No período “O suspeito negou participação no crime, mas ninguém acreditou nisso”, o pronome contido em nisso retoma a ideia expressa na oração anterior.",
     "Isso retoma todo o conteúdo: o fato de o suspeito ter negado participação."),
    ("E", "Em “Me disseram que o prazo foi prorrogado”, a colocação do pronome no início do período está de acordo com a norma-padrão da língua escrita.",
     "No padrão formal, não se inicia período com pronome oblíquo átono: Disseram-me."),
], 20)

SOURCES = [GRAM, "Manual de Redação da Presidência da República, 3ª edição (pronomes de tratamento).", SRC_A]
