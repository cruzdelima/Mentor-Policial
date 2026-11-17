# -*- coding: utf-8 -*-
"""Língua Portuguesa · Verbos: flexão, tempos, modos e vozes — MATERIAL APROFUNDADO (estudo inicial)."""
from common import *

MATERIAL = material(
    "lp-verbos-02", "LP", "LP-06", "aprofundado", "Verbos: flexão, tempos, modos e vozes", "Língua Portuguesa · Morfossintaxe",
    "portugues_verbos_aprofundado", "Portugues_Verbos_APROFUNDADO.pdf", None, ["Verbos:", "tempos, modos e vozes"],
    ["Teoria completa para o primeiro estudo: valor dos tempos, imperativo, irregulares,", "vozes verbais e correlação de tempos, com 20 questões no estilo Cebraspe."],
    [("01", "Flexões", "pessoa, número, tempo, modo e voz"),
     ("02", "Tempos e modos", "valor de cada tempo e formação dos derivados"),
     ("03", "Irregulares", "ver, vir, ter, pôr, haver, intervir, mediar e outros"),
     ("04", "Vozes", "ativa, passiva analítica, passiva sintética e o “se”"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Verbos — flexão, tempos, modos e vozes (Língua Portuguesa)",
    "Base: gramáticas de referência (Bechara; Cunha e Cintra).", 150)

THEORY = [
    exam("Como estudar este material",
         "O Cebraspe cobra verbos de três jeitos: **valor do tempo** (“a substituição de *chegavam* por *chegaram* manteria o sentido?”), "
         "**forma correta** (futuro do subjuntivo, verbos derivados de *ter*, *vir*, *ver* e *pôr*) e **voz verbal** "
         "(passiva sintética, concordância com o *se*). Leia a teoria na ordem, faça as 20 questões e revise pelo **PDF de resumo**."),

    h2("1. O que é verbo"),
    p("**Verbo** é a palavra que exprime **ação**, **estado**, **mudança de estado** ou **fenômeno da natureza**, situando o fato no tempo. "
      "É a classe com mais flexões da língua."),
    tb(["Flexão", "O que indica", "Exemplos"], [0.18, 0.42, 0.4], [
        ("Pessoa", "Quem fala (1ª), com quem se fala (2ª), de quem se fala (3ª)", "prendo · prendes · prende"),
        ("Número", "Singular ou plural", "prende · prendem"),
        ("Tempo", "Presente, pretérito ou futuro", "prende · prendeu · prenderá"),
        ("Modo", "Atitude de quem fala: certeza, hipótese, ordem", "prende · que prenda · prenda!"),
        ("Voz", "Relação entre o sujeito e a ação", "prendeu · foi preso · prendeu-se"),
    ]),
    h3("Estrutura e conjugações"),
    bl("**Radical**: parte que carrega o sentido — *prend*-er, *cant*-ar.",
       "**Vogal temática**: indica a conjugação — **1ª** em *-ar* (cantar), **2ª** em *-er* (vender), **3ª** em *-ir* (partir).",
       "**Pôr** e seus derivados (*compor, depor, propor, repor, supor*) pertencem à **2ª conjugação**: a forma antiga era *poer*.",
       "**Desinências**: indicam modo e tempo (*canta-**va***) e número e pessoa (*cantava-**mos***)."),

    h2("2. Modos e tempos"),
    tb(["Modo", "Tempo", "Exemplo", "Valor principal"], [0.14, 0.27, 0.2, 0.39], [
        ("Indicativo", "Presente", "ele investiga", "Fato atual, habitual ou verdade geral; também passado (presente histórico)"),
        ("Indicativo", "Pretérito perfeito", "ele investigou", "Fato **concluído** no passado"),
        ("Indicativo", "Pretérito imperfeito", "ele investigava", "Fato **habitual** ou **em curso** no passado"),
        ("Indicativo", "Pretérito mais-que-perfeito", "ele investigara · tinha investigado", "Passado **anterior a outro** passado"),
        ("Indicativo", "Futuro do presente", "ele investigará", "Fato posterior ao momento da fala"),
        ("Indicativo", "Futuro do pretérito", "ele investigaria", "Fato condicionado, **hipótese**, incerteza ou polidez"),
        ("Subjuntivo", "Presente", "que ele investigue", "Desejo, dúvida, possibilidade no presente ou futuro"),
        ("Subjuntivo", "Pretérito imperfeito", "se ele investigasse", "Hipótese, condição irreal"),
        ("Subjuntivo", "Futuro", "quando ele investigar", "Possibilidade futura, em orações com *se*, *quando*, *assim que*"),
        ("Imperativo", "Afirmativo e negativo", "investigue! · não investigue!", "Ordem, pedido, conselho"),
    ]),
    key("Futuro do pretérito no texto jornalístico",
        "*O suspeito **teria fugido** para outro estado.* O futuro do pretérito apresenta a informação como **não confirmada**. "
        "Trocar por *fugiu* transforma a hipótese em fato: o Cebraspe considera que isso **altera o sentido**."),
    h3("Imperfeito × perfeito"),
    p("*Os agentes **chegavam** cedo* (todos os dias: hábito) × *Os agentes **chegaram** cedo* (naquele dia: fato concluído). "
      "A troca entre esses tempos quase sempre **altera o sentido** — é item clássico de prova."),
    h3("Mais-que-perfeito simples e composto"),
    p("*Quando a equipe chegou, o suspeito já **fugira*** = *já **tinha fugido*** = *já **havia fugido***. "
      "As três formas são equivalentes: a troca mantém sentido e correção."),

    h2("3. Formação dos tempos"),
    p("Quase todos os tempos derivam de três **tempos primitivos**. Dominar as derivações resolve as formas “difíceis” dos irregulares."),
    tb(["Tempo primitivo", "Deriva", "Exemplo (fazer)"], [0.3, 0.36, 0.34], [
        ("Presente do indicativo (1ª pessoa do singular, sem o -o)", "Presente do subjuntivo", "faç-o › que eu **faça**"),
        ("Pretérito perfeito (3ª pessoa do plural, sem o -ram)", "Mais-que-perfeito, imperfeito do subjuntivo e futuro do subjuntivo", "fize-ram › **fizera**, **fizesse**, quando eu **fizer**"),
        ("Infinitivo impessoal", "Imperfeito do indicativo, futuros do indicativo, gerúndio, particípio", "fazer › fazia, **farei**, **faria**, fazendo, feito"),
    ]),
    trap("A armadilha do futuro do subjuntivo",
         "Ele vem do **pretérito perfeito**, e não do infinitivo. Por isso: *se eu **vir*** (ver: viram), *se eu **vier*** (vir: vieram), "
         "*se ele **mantiver*** (manter: mantiveram), *se ele **propuser*** (propor: propuseram), *se ele **fizer***, *se ele **couber***, "
         "*se ele **intervier***. Está errado *“quando eu **ver**”*, *“se ele **manter**”*, *“se ele **propor**”*."),
    h3("Imperativo"),
    tb(["Pessoa", "Afirmativo", "Negativo"], [0.2, 0.4, 0.4], [
        ("tu", "**faze** (presente do indicativo sem -s)", "não **faças** (presente do subjuntivo)"),
        ("você", "**faça** (presente do subjuntivo)", "não **faça**"),
        ("nós", "**façamos**", "não **façamos**"),
        ("vós", "**fazei** (presente do indicativo sem -s)", "não **façais**"),
        ("vocês", "**façam**", "não **façam**"),
    ]),
    nt("O imperativo não tem 1ª pessoa do singular. Na redação formal, mantenha a **uniformidade de tratamento**: "
       "*Venha **você** e traga **seu** documento* (3ª pessoa) ou *Vem **tu** e traz **teu** documento* (2ª pessoa) — sem misturar."),

    h2("4. Verbos irregulares que mais caem"),
    tb(["Verbo", "Formas que a banca explora"], [0.2, 0.8], [
        ("ter e derivados (deter, manter, obter, conter, reter)", "ele **detém** · eles **detêm** · ele **deteve** · se ele **detiver** · se ele **detivesse**"),
        ("vir e derivados (intervir, provir, convir)", "ele **intervém** · eles **intervêm** · ele **interveio** · se ele **intervier** · se ele **interviesse**"),
        ("ver e derivados (prever, rever)", "eu **vi** · se eu **vir** · se ele **previr** · ele **previu** (prever segue *ver*)"),
        ("pôr e derivados (propor, depor, compor, supor)", "ele **propôs** · eles **propuseram** · se ele **propuser** · se ele **propusesse**"),
        ("haver", "impessoal no sentido de **existir** ou de **tempo decorrido**: *Havia provas. Há dois anos.* — sempre no singular"),
        ("fazer (tempo)", "impessoal: ***Faz** dois anos que o crime ocorreu* — sempre no singular"),
        ("requerer", "eu **requeiro** · ele **requereu** (no pretérito é regular, não segue *querer*)"),
        ("reaver", "só tem as formas em que *haver* tem a letra **v**: *nós reavemos, ele **reouve***; não existe “reavejo” nem “reaveu”"),
        ("verbos em -ear", "ditongo *-ei* nas formas rizotônicas: *passear › passeio, passeia; nomear › nomeio*"),
        ("verbos em -iar", "regulares (*premiar › premio*), exceto **M**ediar, **A**nsiar, **R**emediar, **I**ncendiar, **O**diar: *medeio, anseio, remedeio, incendeio, odeio*"),
    ]),
    key("Haver + auxiliar",
        "Quando *haver* (existir) ou *fazer* (tempo) formam locução, o **auxiliar também fica no singular**: "
        "***Deve haver** provas no inquérito. **Vai fazer** dez anos.*"),

    h2("5. Formas nominais"),
    bl("**Infinitivo**: *prender*. Pode ser **pessoal** (flexionado: *prendermos*) ou **impessoal**.",
       "**Gerúndio**: *prendendo*. Indica ação em curso. Evite o **gerundismo** (*vou estar enviando*): prefira *enviarei*.",
       "**Particípio**: *preso, prendido*. Forma os tempos compostos e a voz passiva."),
    h3("Particípios duplos (verbos abundantes)"),
    tb(["Auxiliar", "Particípio", "Exemplo"], [0.26, 0.24, 0.5], [
        ("ter / haver", "**regular** (-ado, -ido)", "O juiz **tinha aceitado** o recurso. A polícia **havia prendido** o suspeito."),
        ("ser / estar", "**irregular** (curto)", "O recurso **foi aceito**. O suspeito **está preso**."),
    ]),
    nt("*Pagar, ganhar* e *gastar* hoje usam o particípio curto também com *ter*: *tinha **pago**, tinha **ganho**, tinha **gasto***. "
       "*Chegar* só tem *chegado* (“tinha chego” é desvio)."),
    h3("Infinitivo flexionado: regras práticas"),
    bl("**Não se flexiona** em **locução verbal**: *Os servidores **devem apresentar** os documentos.*",
       "**Flexiona-se** quando tem **sujeito próprio**, diferente do da oração principal: *É necessário **revisarmos** os procedimentos.*",
       "Com verbos causativos e sensitivos (*mandar, deixar, fazer, ver, ouvir*) seguidos de **pronome oblíquo**, não se flexiona: *Mandou-**os sair**.* "
       "Com substantivo, ambas as formas são aceitas: *Mandou os presos **sair** / **saírem**.*"),

    h2("6. Vozes verbais"),
    tb(["Voz", "Estrutura", "Exemplo"], [0.22, 0.38, 0.4], [
        ("Ativa", "Sujeito **pratica** a ação", "A polícia **prendeu** os suspeitos."),
        ("Passiva analítica", "**ser** + particípio (+ agente da passiva)", "Os suspeitos **foram presos** pela polícia."),
        ("Passiva sintética", "verbo **transitivo direto** + **se** (partícula apassivadora)", "**Prenderam-se** os suspeitos."),
        ("Reflexiva", "Sujeito pratica e sofre a ação", "O agente **feriu-se** na operação."),
    ]),
    h3("Transposição ativa › passiva"),
    bl("O **objeto direto** da ativa vira **sujeito** da passiva; o sujeito da ativa vira **agente da passiva**.",
       "O verbo *ser* fica **no mesmo tempo e modo** do verbo da ativa: *prendeu › **foi** preso; prenderá › **será** preso; "
       "prendia › **era** preso; tinha prendido › **tinha sido** preso*.",
       "O **particípio concorda** com o novo sujeito: *As provas foram **analisadas**.*",
       "Só verbos **transitivos diretos** (ou diretos e indiretos) admitem passiva."),
    h3("“Se”: apassivador × indeterminador"),
    tb(["Verbo", "Papel do se", "Concordância", "Exemplo"], [0.2, 0.26, 0.22, 0.32], [
        ("Transitivo direto", "Partícula **apassivadora**", "Verbo concorda com o **sujeito**", "**Vendem-se** viaturas. **Investigou-se** a denúncia."),
        ("Transitivo indireto, intransitivo ou de ligação", "Índice de **indeterminação** do sujeito", "Verbo **sempre no singular**", "**Precisa-se** de agentes. **Trata-se** de casos graves."),
    ]),
    trap("Pegadinha da passiva sintética",
         "Em *Vendem-se viaturas*, **viaturas é o sujeito** (= viaturas são vendidas). Por isso o verbo vai ao plural, e *vende-se viaturas* é desvio. "
         "Já em *Trata-se de casos graves*, não há sujeito determinado: *“tratam-se de”* está errado."),

    h2("7. Correlação dos tempos"),
    tb(["Oração com", "Pede na outra oração", "Exemplo"], [0.32, 0.3, 0.38], [
        ("Imperfeito do subjuntivo (se + -sse)", "Futuro do pretérito", "Se o réu **colaborasse**, a pena **seria** reduzida."),
        ("Futuro do subjuntivo (se/quando + -r)", "Futuro do presente", "Se o réu **colaborar**, a pena **será** reduzida."),
        ("Presente do indicativo (verbo de vontade)", "Presente do subjuntivo", "**Quero** que ele **venha**."),
        ("Pretérito do indicativo (verbo de vontade)", "Imperfeito do subjuntivo", "**Queria** que ele **viesse**."),
    ]),

    h2("8. Como o Cebraspe cobra"),
    bl("**Substituição de tempo**: perfeito × imperfeito (altera), mais-que-perfeito simples × composto (mantém), futuro do pretérito × perfeito (altera: hipótese vira fato).",
       "**Correção de forma**: futuro do subjuntivo de *ver, vir, ter, pôr* e derivados; acento de *têm/vêm* e *detêm/intervêm*.",
       "**Voz**: reescrita na passiva com o tempo do verbo *ser* errado, ou com o particípio sem concordância.",
       "**Concordância com se**: *vendem-se* (plural) × *precisa-se de* (singular).",
       "**Verbos impessoais**: *haver* e *fazer* no plural são sempre erro quando indicam existência ou tempo."),
]

QUIZ = quiz([
    ("C", "Em “Se o perito vir o laudo, confirmará a fraude”, a forma vir corresponde ao futuro do subjuntivo do verbo ver.",
     "O futuro do subjuntivo deriva do pretérito perfeito (viram): se eu vir, se ele vir."),
    ("E", "A frase “Quando o delegado ver o relatório, tomará providências” está de acordo com a norma-padrão.",
     "O correto é quando o delegado vir; ver não se usa como futuro do subjuntivo."),
    ("C", "Em “O agente interveio na discussão”, a forma verbal está correta.",
     "Intervir conjuga-se como vir: ele veio, ele interveio (e não interviu)."),
    ("E", "Em “Haviam muitos policiais no local”, a concordância verbal está de acordo com a norma-padrão.",
     "Haver no sentido de existir é impessoal e fica no singular: havia muitos policiais."),
    ("C", "A transposição de “A comissão analisará os recursos” para a voz passiva analítica resulta em “Os recursos serão analisados pela comissão”.",
     "O verbo ser assume o tempo do verbo da ativa (futuro do presente) e o particípio concorda com o novo sujeito."),
    ("E", "Em “Vendem-se viaturas apreendidas”, a forma verbal poderia ser substituída por vende-se, sem prejuízo da correção gramatical.",
     "Há voz passiva sintética, e viaturas apreendidas é o sujeito: o verbo deve ficar no plural."),
    ("C", "Em “Precisa-se de investigadores”, o vocábulo se é índice de indeterminação do sujeito.",
     "Precisar de é transitivo indireto; com ele, o se indetermina o sujeito, e o verbo fica no singular."),
    ("E", "Está correta a frase “O recurso foi aceitado pelo juiz”, pois o particípio regular deve acompanhar o auxiliar ser.",
     "Com ser e estar usa-se o particípio irregular: o recurso foi aceito. O regular acompanha ter e haver."),
    ("C", "Em “É necessário revisarmos os procedimentos”, o infinitivo está flexionado porque possui sujeito próprio.",
     "O sujeito do infinitivo é nós, indicado pela desinência -mos."),
    ("E", "No imperativo afirmativo, a forma do verbo fazer correspondente a você é faz.",
     "Para você, o imperativo afirmativo vem do presente do subjuntivo: faça."),

    ("C", "No trecho “O suspeito teria fugido para outro estado”, o emprego do futuro do pretérito indica que a informação é apresentada como hipótese, e não como fato confirmado.",
     "Esse uso do futuro do pretérito, comum na imprensa, marca a informação como não confirmada."),
    ("E", "Em “Os agentes chegavam cedo todos os dias”, a substituição de chegavam por chegaram manteria o sentido de ação habitual no passado.",
     "O imperfeito indica hábito; o perfeito indica fato concluído. A troca altera o sentido."),
    ("C", "No período “Quando a equipe chegou, o suspeito já fugira”, a forma fugira poderia ser substituída por tinha fugido, sem prejuízo do sentido e da correção gramatical.",
     "O mais-que-perfeito simples (fugira) equivale ao composto (tinha fugido)."),
    ("E", "Na oração “Investigou-se a denúncia com cuidado”, o termo a denúncia exerce a função de objeto direto.",
     "Na passiva sintética, a denúncia é sujeito: a denúncia foi investigada."),
    ("C", "A correlação entre os tempos verbais está de acordo com a norma-padrão em “Se o réu colaborasse, a pena seria reduzida”.",
     "Imperfeito do subjuntivo na condição pede futuro do pretérito na principal."),
    ("E", "A correlação entre os tempos verbais está de acordo com a norma-padrão em “Se o réu colaborar, a pena seria reduzida”.",
     "Futuro do subjuntivo na condição pede futuro do presente: a pena será reduzida."),
    ("C", "Em “Deve haver provas suficientes no inquérito”, o verbo dever permanece no singular por formar locução com o verbo haver, impessoal.",
     "O auxiliar de verbo impessoal também fica no singular."),
    ("E", "Em “Eles detém a posse do imóvel”, a forma verbal está de acordo com a norma-padrão.",
     "No plural, os derivados de ter recebem acento circunflexo: eles detêm."),
    ("C", "Em “Os servidores devem apresentar os documentos”, o infinitivo não se flexiona por fazer parte de locução verbal.",
     "Em locução verbal, flexiona-se apenas o auxiliar (devem)."),
    ("E", "A forma eu medio, do verbo mediar, está de acordo com a norma-padrão.",
     "Mediar é exceção entre os verbos em -iar (MARIO): eu medeio, ele medeia."),
], 20)

SOURCES = [GRAM, SRC_A]
