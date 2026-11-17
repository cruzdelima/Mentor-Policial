# -*- coding: utf-8 -*-
"""Língua Portuguesa · Compreensão e interpretação de textos — MATERIAL APROFUNDADO (estudo inicial)."""
from common import *

MATERIAL = material(
    "lp-interpretacao-02", "LP", "LP-05", "aprofundado", "Compreensão e interpretação de textos", "Língua Portuguesa · Leitura",
    "portugues_interpretacao_aprofundado", "Portugues_Interpretacao_de_Textos_APROFUNDADO.pdf", None,
    ["Compreensão e", "interpretação de textos"],
    ["Teoria completa e método de resolução: o que o texto diz, o que ele permite concluir", "e onde a banca arma as pegadinhas, com 20 questões sobre três textos inéditos."],
    [("01", "Conceitos", "compreensão, interpretação, extrapolação e redução"),
     ("02", "Implícitos", "pressupostos, subentendidos e inferências"),
     ("03", "Ponto de vista", "tese, argumentos, modalização e vozes do texto"),
     ("04", "Método", "como ler o texto e julgar cada item do Cebraspe"),
     ("05", "Questões", "20 itens certo/errado sobre três textos + gabarito")],
    "Tópico do edital: Compreensão e interpretação de textos (Língua Portuguesa)",
    "Base: gramáticas de referência, linguística textual (Koch; Fiorin e Savioli) e padrão de cobrança do Cebraspe.", 180)

THEORY = [
    exam("Como estudar este material",
         "Interpretação é o assunto que **mais pesa** em Português no Cebraspe: praticamente todos os itens de uma prova partem de um texto. "
         "Não existe decoreba aqui; existe **método**. Leia a teoria, depois resolva as 20 questões seguindo o passo a passo da seção 6 e, "
         "ao corrigir, descubra **qual tipo de erro** você cometeu (extrapolação, redução, contradição). Nas revisões, use o **PDF de resumo** "
         "e refaça questões de prova."),

    h2("1. Compreender × interpretar"),
    tb(["", "Compreensão", "Interpretação"], [0.18, 0.41, 0.41], [
        ("O que é", "Entender o que o texto **diz**", "Concluir o que o texto **permite deduzir**"),
        ("Onde está a resposta", "Na superfície do texto (explícito)", "Nas relações entre as partes do texto (implícito)"),
        ("Verbos típicos da banca", "*segundo o texto, de acordo com o autor, o texto informa, o autor afirma*", "*infere-se, depreende-se, conclui-se, o texto sugere, o autor deixa implícito*"),
        ("Exemplo", "Texto: “Os furtos caíram 30%.” Item: *Segundo o texto, os furtos diminuíram.*", "Texto: “Voltou a faltar ao serviço.” Item: *Infere-se que ele já havia faltado antes.*"),
    ]),
    key("A regra de ouro",
        "Interpretar **não é opinar**. A conclusão precisa estar **autorizada pelo texto**: se você precisou de uma informação que só existe "
        "na sua cabeça (conhecimento de mundo, opinião pessoal, “mas na prática…”), o item provavelmente está **errado**."),

    h2("2. Os três erros que a banca explora"),
    tb(["Erro", "O que o item faz", "Sinal de alerta", "Exemplo"], [0.15, 0.3, 0.25, 0.3], [
        ("**Extrapolação**", "Vai **além** do texto: generaliza, acrescenta causa, consequência ou opinião que o autor não deu", "*todos, sempre, nunca, somente, exclusivamente, garante, elimina, comprova*", "Texto: “os furtos caíram”. Item: “os crimes foram eliminados”."),
        ("**Redução**", "Fica **aquém** do texto: toma uma parte pelo todo, apresenta um aspecto como se fosse o único", "*apenas, só, unicamente, o único, a principal razão*", "Texto cita três fatores. Item: “o único fator é a iluminação”."),
        ("**Contradição**", "Afirma o **contrário** do texto", "Negações trocadas, antônimos, conectivos invertidos", "Texto: “não é inútil”. Item: “o autor considera a tecnologia inútil”."),
    ]),
    trap("Palavras absolutas",
         "**Sempre, nunca, todos, nenhum, somente, exclusivamente, totalmente, garante** quase sempre tornam o item errado — mas não automaticamente. "
         "Se o próprio texto for categórico (“**nenhum** laboratório recupera”), o item que repete a ideia pode estar certo. Compare com o texto, nunca julgue pela palavra isolada."),

    h2("3. Informação implícita"),
    p("Todo texto diz mais do que está escrito. A banca cobra dois tipos de informação implícita, com regras diferentes."),
    tb(["Tipo", "De onde vem", "Pode ser negado?", "Exemplo"], [0.15, 0.35, 0.2, 0.3], [
        ("**Pressuposto**", "De **marcas linguísticas** do próprio enunciado: verbos, advérbios, adjetivos, conectivos", "**Não**: o pressuposto continua valendo mesmo se a frase for negada", "“O réu **voltou a** mentir.” › ele já havia mentido. (Também em “O réu **não** voltou a mentir.”)"),
        ("**Subentendido**", "Do **contexto** e da intenção de quem fala; é insinuação", "**Sim**: quem fala pode dizer que não quis dizer aquilo", "Em sala abafada: “Está calor aqui, não?” › pedido para abrir a janela."),
    ]),
    h3("Marcas que geram pressupostos"),
    tb(["Marca", "Exemplo", "Pressuposto"], [0.3, 0.36, 0.34], [
        ("Verbos de mudança: *deixar de, passar a, continuar, voltar a, tornar-se*", "O agente **deixou de** fumar.", "Ele fumava."),
        ("Advérbios: *ainda, já, também, novamente, até*", "**Até** o delegado foi enganado.", "Era improvável que ele fosse enganado; outros também foram."),
        ("Adjetivos e substantivos: *novo, outro, ex-*", "O **ex**-diretor depôs.", "Ele não é mais diretor."),
        ("Verbos factivos: *lamentar, descobrir, perceber, reconhecer*", "Ele **reconheceu** que errou.", "Ele de fato errou."),
        ("Orações adjetivas restritivas", "Os presos **que fugiram** foram recapturados.", "Nem todos os presos fugiram."),
        ("Conectivos: *mas, embora, apesar de*", "É jovem, **mas** é competente.", "Haveria uma expectativa de que jovens não fossem competentes."),
    ]),
    h3("Inferência"),
    p("**Inferir** é tirar uma conclusão **necessária** a partir de informações do texto. O teste: *se as premissas do texto forem verdadeiras, "
      "a conclusão do item também tem de ser?* Se a conclusão for apenas **possível** ou **provável**, o item extrapola."),
    bl("Texto: “Só os servidores aprovados no curso foram promovidos; Ana foi promovida.” › Infere-se que **Ana foi aprovada no curso**. (necessário)",
       "Texto: “Ana foi promovida.” › “Infere-se que Ana é a melhor servidora do setor.” (possível, mas não necessário: **extrapolação**)"),

    h2("4. O ponto de vista do autor"),
    h3("Tese e argumentos"),
    bl("**Tese** é a ideia central que o autor defende. Costuma aparecer na **introdução** ou na **conclusão**, muitas vezes após conectivos como "
       "*portanto, assim, por isso, em suma, ou seja*.",
       "**Argumentos** sustentam a tese: exemplos, dados, comparações, relações de causa e consequência, citação de autoridade, contra-argumento seguido de refutação.",
       "Cuidado com o **contra-argumento**: muitos textos apresentam a ideia que vão combater (“Há quem diga que…”, “Durante muito tempo, acreditou-se…”). "
       "Atribuir ao autor essa ideia é o erro mais frequente em itens sobre ponto de vista."),
    h3("Modalização: o grau de certeza"),
    p("O autor marca o quanto se compromete com o que diz. A banca troca expressões e pergunta se o sentido foi mantido."),
    tb(["Efeito", "Marcas", "Exemplo"], [0.22, 0.42, 0.36], [
        ("Certeza", "*sem dúvida, evidentemente, é certo que, comprova, demonstra*", "**Evidentemente**, o laudo é falho."),
        ("Possibilidade, dúvida", "*talvez, possivelmente, pode, parece, ao que tudo indica, em princípio*, futuro do pretérito", "O laudo **seria** falho. O laudo **pode** ser falho."),
        ("Necessidade, obrigação", "*deve, é preciso, é necessário, é imprescindível*", "**É preciso** refazer o laudo."),
        ("Avaliação", "*felizmente, infelizmente, lamentavelmente*, adjetivos valorativos", "**Infelizmente**, o laudo é falho."),
    ]),
    key("Trocar o modalizador muda o sentido",
        "“O suspeito **pode** ter fugido” ≠ “O suspeito **fugiu**”. Passar de possibilidade a certeza (ou o inverso) **altera o sentido**, "
        "mesmo que a frase continue gramaticalmente correta."),
    h3("As vozes do texto"),
    bl("Nem tudo o que está no texto é opinião do autor. Ele pode **citar** outras pessoas (discurso direto ou indireto), **atribuir** ideias a terceiros "
       "(*segundo especialistas, para os críticos*) ou **ironizar**.",
       "Aspas podem indicar citação, ironia, palavra estrangeira, termo técnico ou distanciamento do autor em relação à expressão usada.",
       "Pergunte sempre: **quem** está dizendo isso? O autor ou alguém que ele menciona?"),

    h2("5. Ferramentas de leitura"),
    h3("Sentido de palavras e expressões no contexto"),
    p("O significado é dado pelo **contexto**, não pelo dicionário. Em itens de substituição, teste a troca na frase: o novo termo precisa manter o "
      "sentido **naquele trecho**. *Ele **acusou** o golpe* (sentiu, demonstrou ter sido atingido) não equivale a *ele **denunciou** o golpe*."),
    h3("Conectivos: as setas do raciocínio"),
    tb(["Relação", "Conectivos", "Atenção"], [0.2, 0.46, 0.34], [
        ("Oposição", "mas, porém, contudo, todavia, entretanto, no entanto", "A ideia mais forte vem **depois** do conectivo"),
        ("Concessão", "embora, ainda que, mesmo que, apesar de", "A ideia mais forte está na **outra** oração"),
        ("Causa", "porque, pois, já que, uma vez que, visto que", ""),
        ("Conclusão", "portanto, logo, por isso, assim, então", "Costuma introduzir a **tese**"),
        ("Condição", "se, caso, desde que, contanto que", "Não afirma que o fato aconteceu"),
        ("Finalidade", "para que, a fim de que", ""),
        ("Adição", "e, também, além disso, não só… mas também", ""),
    ]),
    h3("Referência"),
    p("Pronomes e expressões retomam ideias anteriores (**anáfora**) ou anunciam o que virá (**catáfora**). Muitos itens perguntam a que termo "
      "uma palavra se refere. **Substitua** o pronome pelo termo sugerido e releia: se o sentido se mantém, o item está certo. "
      "Lembre que *isso, isto* e *o* (= isso) podem retomar uma **oração inteira**."),
    h3("Título, tipo e finalidade"),
    bl("**Tipo textual**: narrativo (fatos em sequência), descritivo (características), **dissertativo-expositivo** (informa, explica) e "
       "**dissertativo-argumentativo** (defende ponto de vista). A banca costuma perguntar qual predomina. (Há material próprio sobre tipologia.)",
       "**Finalidade**: informar, convencer, orientar, criticar, alertar. Leia o texto inteiro antes de decidir.",
       "**Título**: costuma antecipar o tema ou a tese; não substitui a leitura do texto."),

    h2("6. Método de resolução (Cebraspe)"),
    tb(["Passo", "O que fazer"], [0.08, 0.92], [
        ("1", "Leia o **texto inteiro** uma vez, sem pressa e sem marcar nada. Pergunte-se: qual é o **tema**? O autor **informa** ou **defende** algo?"),
        ("2", "Faça uma frase-resumo de cada parágrafo, mentalmente ou na margem (“§1: câmeras sozinhas não previnem”)."),
        ("3", "Leia o item e identifique o **comando**: *segundo o texto* (compreensão), *infere-se* (interpretação), *o autor defende* (ponto de vista), "
              "*manteria o sentido* (reescrita)."),
        ("4", "**Volte ao trecho** do texto a que o item se refere. Não julgue de memória."),
        ("5", "Compare palavra por palavra: o item **ampliou** (extrapolação), **restringiu** (redução) ou **inverteu** (contradição) o que o texto diz?"),
        ("6", "Verifique **quem** diz: é o autor ou alguém que ele cita ou refuta?"),
        ("7", "Na dúvida real, **deixe em branco**: no Cebraspe, cada erro anula um acerto."),
    ]),
    exam("Como o Cebraspe formula os itens",
         "**“Depreende-se do texto que…”, “Infere-se…”, “Conclui-se…”**: exigem conclusão necessária. "
         "**“O texto sugere / deixa implícito…”**: pressuposto ou subentendido. "
         "**“De acordo com o texto / Segundo o autor…”**: informação explícita. "
         "**“A argumentação do texto baseia-se…”**: identifique tese e argumentos. "
         "**“O trecho X reforça / contrapõe / exemplifica a ideia de Y”**: relação entre partes do texto. "
         "**“Seriam mantidos a correção e o sentido caso…”**: reescrita — dois critérios, ambos precisam ser atendidos."),

    h2("7. Treino rápido: classifique o erro"),
    tb(["Texto diz", "Item afirma", "Julgamento"], [0.34, 0.34, 0.32], [
        ("“Parte dos agentes aprovou a mudança.”", "Os agentes aprovaram a mudança.", "**Errado** — extrapolação (parte › todos)"),
        ("“O policiamento e a iluminação reduziram os furtos.”", "O policiamento reduziu os furtos.", "**Certo** — o item não diz que foi o único fator"),
        ("“O policiamento e a iluminação reduziram os furtos.”", "Apenas o policiamento reduziu os furtos.", "**Errado** — redução"),
        ("“A tecnologia não resolve sozinha o problema.”", "A tecnologia é dispensável.", "**Errado** — contradição/extrapolação"),
        ("“O suspeito voltou a ser visto na região.”", "O suspeito já havia sido visto na região.", "**Certo** — pressuposto de *voltou a*"),
        ("“Há quem defenda penas maiores; o autor discorda.”", "O autor defende penas maiores.", "**Errado** — voz atribuída a terceiros"),
    ]),
]

T1 = ("**Texto 1.** Durante muito tempo, acreditou-se que o aumento do número de câmeras nas ruas seria suficiente para reduzir a criminalidade. "
      "A experiência de várias cidades mostrou que a realidade é mais complexa. Câmeras ajudam a esclarecer crimes já cometidos, mas seu efeito preventivo "
      "depende de fatores que nenhuma lente controla: a iluminação dos espaços públicos, a presença de pessoas circulando, a rapidez da resposta policial. "
      "Em bairros onde as imagens eram monitoradas em tempo real e havia viaturas próximas, os furtos caíram; onde as gravações apenas se acumulavam em "
      "servidores, pouco mudou.\n"
      "Isso não significa que a tecnologia seja inútil. Significa que ela é ferramenta, e não política pública. Quem a trata como solução isolada costuma "
      "gastar muito e colher pouco, além de criar uma falsa sensação de segurança, que pode ser ainda mais perigosa do que a insegurança percebida.")

T2 = ("**Texto 2.** Ler bem não é decifrar palavras, é reconstruir intenções. O leitor apressado lê o que espera encontrar; o leitor atento lê o que "
      "efetivamente está escrito. A diferença parece pequena, mas decide provas, processos e reputações. Um depoimento mal lido pode transformar uma dúvida "
      "em certeza, e uma ressalva — “ao que tudo indica”, “em princípio” — pode desaparecer no resumo de quem tem pressa. Por isso, bons investigadores "
      "desconfiam das próprias primeiras impressões: anotam o que foi dito, separam o que foi inferido e só então formulam hipóteses. Não se trata de ler "
      "devagar, e sim de ler com método.")

T3 = ("**Texto 3.** A polícia moderna produz mais dados do que consegue analisar. Boletins, relatórios, imagens, extratos e mensagens apreendidas "
      "acumulam-se em volume que nenhuma equipe humana daria conta de ler integralmente. A promessa dos sistemas automatizados é justamente esta: encontrar, "
      "no meio do excesso, o padrão que escaparia aos olhos. A promessa é real, mas vem acompanhada de riscos que não convém ignorar.\n"
      "O primeiro deles é confundir correlação com causa. Um algoritmo pode indicar que determinados endereços concentram ocorrências, mas não explica por "
      "quê — e a resposta pode estar menos no lugar do que na forma como os registros foram feitos. O segundo é a opacidade: decisões que afetam pessoas "
      "exigem justificativa, e “o sistema apontou” não é justificativa. O terceiro, talvez o mais sutil, é a acomodação. Quando a máquina sugere, o analista "
      "tende a confirmar; aos poucos, deixa de perguntar.\n"
      "Nada disso recomenda abandonar a tecnologia. Recomenda usá-la como quem usa uma lanterna: ela ilumina o caminho, mas quem decide para onde ir "
      "continua sendo quem a segura.")

QUIZ = quiz([
    ("C", "Com base no texto 1, depreende-se que a eficácia preventiva das câmeras está condicionada a outros fatores, como a rapidez da resposta policial.",
     "O texto afirma que o efeito preventivo depende de fatores como iluminação, circulação de pessoas e rapidez da resposta policial.", T1),
    ("E", "O autor do texto 1 defende que a instalação de câmeras é inútil para o enfrentamento da criminalidade.",
     "Contradição: o texto diz expressamente que isso “não significa que a tecnologia seja inútil”."),
    ("C", "A expressão “Durante muito tempo, acreditou-se”, no início do texto 1, pressupõe que essa crença foi, ao menos em parte, revista.",
     "A delimitação temporal sugere que a crença deixou de ser aceita; o período seguinte confirma isso."),
    ("E", "Conclui-se do texto 1 que, nos bairros com monitoramento em tempo real e viaturas próximas, a criminalidade foi eliminada.",
     "Extrapolação: o texto diz apenas que os furtos caíram."),
    ("C", "No segundo parágrafo do texto 1, a distinção entre “ferramenta” e “política pública” sustenta a ideia de que a tecnologia, isoladamente, não resolve o problema.",
     "É a tese do texto: a tecnologia é instrumento, e não solução por si só."),
    ("C", "De acordo com o texto 2, o leitor atento diferencia-se do apressado por se ater ao que de fato está escrito.",
     "Informação explícita: “o leitor atento lê o que efetivamente está escrito”.", T2),
    ("E", "O texto 2 recomenda que, para ler bem, é preciso ler devagar.",
     "Contradição: o último período diz “Não se trata de ler devagar, e sim de ler com método”."),
    ("C", "No texto 2, as expressões “ao que tudo indica” e “em princípio” exemplificam ressalvas que atenuam o grau de certeza de uma afirmação.",
     "São modalizadores de possibilidade; o texto alerta que podem se perder em resumos apressados."),
    ("E", "Infere-se do texto 2 que bons investigadores não devem formular hipóteses durante a apuração de um fato.",
     "Extrapolação/contradição: o texto diz que eles formulam hipóteses, mas só depois de anotar e separar o que foi dito do que foi inferido."),
    ("C", "No trecho “A diferença parece pequena, mas decide provas, processos e reputações”, contrapõe-se a aparente pouca importância da diferença às suas consequências relevantes.",
     "O conectivo mas introduz a ideia mais forte: as consequências importantes."),

    ("C", "O texto 3 reconhece a utilidade dos sistemas automatizados, mas aponta riscos associados ao seu uso.",
     "“A promessa é real, mas vem acompanhada de riscos.”", T3),
    ("E", "Segundo o texto 3, os algoritmos são capazes de explicar as causas da concentração de ocorrências em determinados endereços.",
     "Contradição: o algoritmo pode indicar a concentração, “mas não explica por quê”."),
    ("C", "Depreende-se do segundo parágrafo do texto 3 que a própria forma de registrar as ocorrências pode influenciar os padrões identificados pelos sistemas.",
     "O texto diz que a resposta pode estar “na forma como os registros foram feitos”."),
    ("E", "O autor do texto 3 sustenta que a expressão “o sistema apontou” é justificativa suficiente para decisões que afetem pessoas, desde que o sistema seja confiável.",
     "Contradição: o texto afirma que essa expressão “não é justificativa”; a ressalva sobre confiabilidade não está no texto."),
    ("C", "Ao qualificar a acomodação como “talvez o mais sutil” dos riscos, o autor do texto 3 atenua o grau de certeza da afirmação.",
     "Talvez é modalizador de possibilidade."),
    ("E", "No último parágrafo do texto 3, o autor conclui que a tecnologia deve ser abandonada em razão dos riscos apontados.",
     "Contradição: “Nada disso recomenda abandonar a tecnologia”."),
    ("C", "A comparação com a lanterna, no último parágrafo do texto 3, reforça a ideia de que a decisão deve permanecer com o ser humano.",
     "A lanterna ilumina, mas “quem decide para onde ir continua sendo quem a segura”."),
    ("C", "O texto 3 é predominantemente dissertativo-argumentativo.",
     "O autor apresenta uma tese (usar a tecnologia sem abdicar da decisão humana) e a sustenta com argumentos."),
    ("E", "Infere-se do texto 3 que as equipes humanas conseguem ler integralmente os dados produzidos pela polícia moderna, embora de forma lenta.",
     "Contradição: o texto diz que nenhuma equipe humana daria conta de ler integralmente esses dados."),
    ("E", "A substituição de “Nada disso recomenda abandonar a tecnologia” por Tudo isso recomenda abandonar a tecnologia manteria o sentido original do texto 3.",
     "A troca inverte o sentido da conclusão do autor."),
], 20)

SOURCES = [
    "KOCH, I. V.; ELIAS, V. M. Ler e compreender: os sentidos do texto. FIORIN, J. L.; SAVIOLI, F. P. Para entender o texto: leitura e redação.",
    GRAM,
    "Os textos 1, 2 e 3 e os 20 itens foram escritos para o Mentor Policial. O Bloco B segue o padrão de cobrança da banca, mas não reproduz questões de provas.",
]
