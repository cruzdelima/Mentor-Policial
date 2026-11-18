# -*- coding: utf-8 -*-
"""Direito Constitucional · Poder Executivo — MATERIAL APROFUNDADO."""
from common import *

MATERIAL = material(
    "dc-executivo-02", "DC", "DC-10", "aprofundado", "Poder Executivo", "Direito Constitucional · Organização dos Poderes",
    "constitucional_executivo_aprofundado", "Constitucional_Poder_Executivo_APROFUNDADO.pdf", None, ["Poder", "Executivo"],
    ["Eleição, posse, substituição e vacância, atribuições do Presidente, crimes de responsabilidade,", "Ministros e Conselhos, com 20 questões no estilo Cebraspe."],
    [("01", "Eleição e mandato", "maioria absoluta, segundo turno, posse em 5 de janeiro"),
     ("02", "Sucessão", "linha sucessória e dupla vacância"),
     ("03", "Atribuições", "art. 84 e as delegáveis"),
     ("04", "Responsabilidade", "crimes de responsabilidade e comuns, Conselhos"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Poder Executivo (arts. 76 a 91) — Direito Constitucional",
    "Base: Constituição Federal de 1988 e jurisprudência do STF.", 150)

THEORY = [
    exam("Como estudar este material",
         "O Executivo é cobrado em quatro frentes: **eleição e posse** (com a nova data de posse da EC 111/2021), **dupla vacância** (eleição "
         "direta ou indireta), **atribuições delegáveis** do art. 84 e o **processo** contra o Presidente (quem autoriza, quem julga, quando ele "
         "é afastado)."),

    h2("1. Presidencialismo"),
    p("O Poder Executivo é exercido pelo **Presidente da República**, auxiliado pelos **Ministros de Estado** (art. 76). No presidencialismo, "
      "o Presidente acumula as funções de **Chefe de Estado** (representa o país nas relações internacionais) e **Chefe de Governo** "
      "(dirige a administração federal). O Executivo é **monocrático**."),

    h2("2. Eleição, posse e mandato"),
    tb(["Ponto", "Regra"], [0.26, 0.74], [
        ("Data", "**1º turno**: primeiro domingo de **outubro**; **2º turno**: último domingo de **outubro** do ano anterior ao fim do mandato."),
        ("Quem vence", "Quem obtiver a **maioria absoluta** dos votos, **não computados os brancos e os nulos** (votos válidos)."),
        ("2º turno", "Se ninguém alcançar a maioria absoluta, nova eleição entre os **dois mais votados**; vence a maioria dos votos válidos."),
        ("Desistência", "Se, antes do 2º turno, ocorrer **morte, desistência ou impedimento** de candidato, convoca-se o de **maior votação** entre os remanescentes."),
        ("Vice", "É eleito **junto** com o Presidente registrado (chapa única)."),
        ("Posse", "Em sessão do **Congresso Nacional**, com compromisso de manter, defender e cumprir a Constituição."),
        ("Prazo para assumir", "Se em **10 dias** da data fixada o Presidente ou o Vice, salvo força maior, não tiver assumido, o cargo é declarado **vago**."),
        ("Mandato", "**4 anos**, com início em **5 de janeiro** do ano seguinte ao da eleição; permitida **uma reeleição**."),
    ]),
    key("Atenção: nova data de posse (EC 111/2021)",
        "A posse do Presidente passou de 1º de janeiro para **5 de janeiro**, e a dos **Governadores**, para **6 de janeiro**. A regra vale a "
        "partir dos eleitos em **2026**, que tomam posse em **2027**."),

    h2("3. Substituição, sucessão e vacância"),
    bl("O **Vice-Presidente** **substitui** o Presidente nos **impedimentos** (temporários) e o **sucede** na **vaga** (definitiva).",
       "Impedidos ambos, ou vagos os cargos, são chamados **sucessivamente** ao exercício da Presidência: o **Presidente da Câmara**, o "
       "**Presidente do Senado** e o **Presidente do STF**. Eles apenas **substituem** temporariamente: não sucedem.",
       "O Presidente e o Vice não podem ausentar-se do País por **mais de 15 dias** sem **licença do Congresso**, sob pena de **perda do cargo**."),
    tb(["Dupla vacância (art. 81)", "Eleição", "Prazo"], [0.36, 0.34, 0.3], [
        ("Nos **dois primeiros anos** do mandato", "**Direta** (pelo povo)", "**90 dias** depois de aberta a última vaga"),
        ("Nos **dois últimos anos** do mandato", "**Indireta**, pelo **Congresso Nacional**, na forma da lei", "**30 dias** depois da última vaga"),
    ]),
    p("Em ambos os casos, os eleitos apenas **completam o período** dos antecessores (**mandato-tampão**)."),
    trap("Pegadinha: quem sucede",
         "Só o **Vice** sucede. Os Presidentes da Câmara, do Senado e do STF **substituem** temporariamente, até a nova eleição. E a ordem é "
         "**Câmara, Senado, STF**: a banca costuma inverter Câmara e Senado."),

    h2("4. Atribuições do Presidente (art. 84)"),
    tb(["Grupo", "Atribuições (seleção)"], [0.22, 0.78], [
        ("Chefe de Estado", "Manter relações com Estados estrangeiros; **celebrar tratados**, sujeitos a referendo do Congresso; **declarar guerra** "
                            "(autorizado ou referendado pelo Congresso) e celebrar a paz; exercer o **comando supremo das Forças Armadas**."),
        ("Chefe de Governo", "Nomear e exonerar **Ministros de Estado**; exercer a direção superior da administração federal; iniciar o processo "
                             "legislativo; **sancionar, promulgar e publicar** as leis e expedir **decretos e regulamentos** para sua fiel execução; "
                             "**vetar** projetos; editar **medidas provisórias**."),
        ("Segurança do Estado", "Decretar o **estado de defesa** e o **estado de sítio**; decretar e executar a **intervenção federal**."),
        ("Nomeações", "Nomear, após aprovação do Senado, os Ministros do **STF** e dos Tribunais Superiores, o **PGR**, o presidente e os diretores "
                      "do Banco Central; nomear **1/3** dos Ministros do TCU; nomear o **AGU** (sem aprovação do Senado)."),
        ("Clemência", "Conceder **indulto** e **comutar penas**, com audiência, se necessário, dos órgãos instituídos em lei."),
    ]),
    key("Atribuições delegáveis (parágrafo único)",
        "O Presidente pode delegar aos **Ministros de Estado**, ao **Procurador-Geral da República** ou ao **Advogado-Geral da União** apenas: "
        "**VI** – dispor, por **decreto**, sobre a **organização e o funcionamento** da administração federal, quando não implicar aumento de despesa "
        "nem criação ou extinção de órgãos, e sobre a **extinção de funções ou cargos públicos, quando vagos**; **XII** – conceder **indulto** e "
        "**comutar penas**; **XXV**, primeira parte – **prover** os cargos públicos federais. Mnemônico: **D-I-P** (Decreto autônomo, Indulto, Provimento)."),
    bl("O decreto do inciso VI é o **decreto autônomo**: inova na ordem jurídica sem depender de lei, nas hipóteses estritas da Constituição.",
       "Para o STF, quem recebe a delegação para **prover** cargos também pode **desprover** (demitir), por simetria."),

    h2("5. Responsabilidade do Presidente"),
    p("**Crimes de responsabilidade** (art. 85) são infrações **político-administrativas**: atos do Presidente que atentem contra a "
      "Constituição e, especialmente, contra a existência da União; o livre exercício do Legislativo, do Judiciário, do Ministério Público e dos "
      "Poderes dos entes federados; os direitos políticos, individuais e sociais; a segurança interna; a **probidade na administração**; a **lei "
      "orçamentária**; e o cumprimento das leis e das decisões judiciais. São definidos em **lei especial** (Lei 1.079/1950), de competência da "
      "**União** (SV 46)."),
    tb(["", "Crime comum", "Crime de responsabilidade"], [0.24, 0.38, 0.38], [
        ("Autorização", "**Câmara**, por **2/3**", "**Câmara**, por **2/3**"),
        ("Julgamento", "**STF**", "**Senado**, presidido pelo Presidente do STF"),
        ("Afastamento das funções", "Quando o **STF recebe** a denúncia ou queixa", "Quando o **Senado instaura** o processo"),
        ("Pena", "A do crime", "**Perda do cargo** + **inabilitação por 8 anos**"),
    ]),
    bl("Se, decorrido o prazo de **180 dias**, o julgamento não estiver concluído, **cessa o afastamento**, sem prejuízo do prosseguimento do processo.",
       "Nas infrações comuns, enquanto não sobrevier **sentença condenatória**, o Presidente **não está sujeito a prisão**.",
       "**Imunidade temporária** (§ 4º): na vigência do mandato, o Presidente **não pode ser responsabilizado** por **atos estranhos** ao exercício "
       "de suas funções. A persecução fica para depois do mandato.",
       "Essas prerrogativas são **exclusivas do Presidente**: as Constituições estaduais **não podem** estendê-las aos **Governadores** (STF). "
       "Governadores são julgados pelo **STJ** nos crimes comuns, sem necessidade de autorização da Assembleia (ADI 5.540)."),

    h2("6. Ministros de Estado e Conselhos"),
    bl("**Ministros de Estado** (arts. 87 e 88): escolhidos entre **brasileiros maiores de 21 anos** no exercício dos direitos políticos; "
       "**referendam** os atos e decretos do Presidente; são julgados pelo **STF** nos crimes comuns e de responsabilidade, salvo nos crimes de "
       "responsabilidade **conexos** com os do Presidente (Senado). O **Ministro da Defesa** deve ser **brasileiro nato**."),
    tb(["", "Conselho da República (arts. 89 e 90)", "Conselho de Defesa Nacional (art. 91)"], [0.18, 0.41, 0.41], [
        ("Natureza", "Órgão **superior de consulta** do Presidente", "Órgão de **consulta** nos assuntos de **soberania nacional e defesa** do Estado democrático"),
        ("Composição", "Vice-Presidente; Presidentes da Câmara e do Senado; **líderes da maioria e da minoria** de cada Casa; **Ministro da Justiça**; "
                       "**6 cidadãos brasileiros natos** com mais de **35 anos** (2 nomeados pelo Presidente, 2 eleitos pelo Senado, 2 pela Câmara), "
                       "mandato de **3 anos**, vedada a recondução",
         "Vice-Presidente; Presidentes da Câmara e do Senado; Ministros da **Justiça**, da **Defesa**, das **Relações Exteriores** e do "
         "**Planejamento**; **Comandantes da Marinha, do Exército e da Aeronáutica**"),
        ("Opina sobre", "**Intervenção federal**, **estado de defesa** e **estado de sítio**; questões relevantes para a estabilidade das instituições",
         "**Declaração de guerra** e celebração da paz; estado de defesa, sítio e intervenção; uso de áreas indispensáveis à segurança do território, "
         "como a **faixa de fronteira**"),
    ]),
    nt("As manifestações dos Conselhos são **opinativas**: não vinculam o Presidente. O Conselho da República tem **cidadãos** e **líderes "
       "partidários**; o de Defesa Nacional tem **militares** e Ministros ligados à defesa."),
]

QUIZ = quiz([
    ("C", "Será considerado eleito Presidente da República o candidato que obtiver a maioria absoluta de votos, não computados os brancos e os nulos.",
     "Art. 77, § 2º."),
    ("E", "O mandato do Presidente da República eleito em 2026 terá início em 1º de janeiro de 2027.",
     "Desde a EC 111/2021, o mandato presidencial começa em 5 de janeiro do ano seguinte ao da eleição."),
    ("C", "Se, decorridos dez dias da data fixada para a posse, o Presidente ou o Vice-Presidente, salvo motivo de força maior, não tiver assumido o cargo, este será declarado vago.",
     "Art. 78, parágrafo único."),
    ("E", "Em caso de impedimento do Presidente e do Vice-Presidente, será chamado ao exercício da Presidência, em primeiro lugar, o presidente do Senado Federal.",
     "A ordem é: presidente da Câmara, presidente do Senado e presidente do STF."),
    ("C", "Vagando os cargos de Presidente e Vice-Presidente nos dois primeiros anos do mandato, far-se-á eleição direta noventa dias depois de aberta a última vaga.",
     "Art. 81, caput."),
    ("E", "O Presidente da República pode ausentar-se do país por até trinta dias sem licença do Congresso Nacional.",
     "O limite é de quinze dias; acima disso, exige-se licença, sob pena de perda do cargo."),
    ("C", "Compete privativamente ao Presidente da República exercer o comando supremo das Forças Armadas.",
     "Art. 84, XIII."),
    ("E", "O Presidente da República pode delegar aos Ministros de Estado a competência para editar medidas provisórias.",
     "Só são delegáveis as atribuições dos incisos VI, XII e XXV (primeira parte) do art. 84."),
    ("C", "Os Ministros de Estado são escolhidos entre brasileiros maiores de vinte e um anos e no exercício dos direitos políticos.",
     "Art. 87."),
    ("E", "O Conselho da República é composto, entre outros, pelos comandantes da Marinha, do Exército e da Aeronáutica.",
     "Os comandantes militares integram o Conselho de Defesa Nacional."),

    ("C", "Considere que o Presidente e o Vice-Presidente da República tenham morrido em acidente no terceiro ano do mandato. Nesse caso, o Congresso Nacional elegerá, em trinta dias, os novos ocupantes, que apenas completarão o período dos antecessores.",
     "Na vacância nos dois últimos anos, a eleição é indireta, em trinta dias (art. 81, § 1º)."),
    ("E", "Assumindo a Presidência por dupla vacância, o presidente da Câmara dos Deputados exercerá o cargo até o fim do mandato, sem necessidade de nova eleição.",
     "O presidente da Câmara apenas substitui temporariamente; haverá eleição direta ou indireta."),
    ("C", "O Presidente da República pode delegar ao Ministro da Justiça a concessão de indulto.",
     "O inciso XII do art. 84 está entre as atribuições delegáveis."),
    ("E", "Admitida pela Câmara a acusação contra o Presidente da República por crime comum, ele será imediatamente afastado de suas funções.",
     "Nos crimes comuns, o afastamento ocorre com o recebimento da denúncia ou queixa pelo STF."),
    ("C", "Na vigência de seu mandato, o Presidente da República não pode ser responsabilizado por atos estranhos ao exercício de suas funções.",
     "Art. 86, § 4º (imunidade temporária à persecução penal)."),
    ("E", "Constituição estadual pode condicionar a instauração de ação penal contra o governador por crime comum à prévia autorização da Assembleia Legislativa, por simetria com o modelo federal.",
     "O STF considera inconstitucional essa exigência; o governador é julgado pelo STJ sem autorização prévia."),
    ("C", "Por meio de decreto, o Presidente pode extinguir cargos públicos federais, desde que estejam vagos.",
     "Art. 84, VI, b."),
    ("E", "Por meio de decreto autônomo, o Presidente da República pode criar órgãos públicos na administração federal, desde que não haja aumento de despesa.",
     "O decreto do art. 84, VI, a, não pode criar nem extinguir órgãos."),
    ("C", "Se o julgamento do Presidente da República por crime de responsabilidade não estiver concluído em cento e oitenta dias, cessará o seu afastamento, sem prejuízo do regular prosseguimento do processo.",
     "Art. 86, § 2º."),
    ("E", "Os crimes de responsabilidade do Presidente da República podem ser definidos em lei estadual, desde que observados os princípios da Constituição Federal.",
     "Compete à União definir os crimes de responsabilidade e as normas de processo e julgamento (SV 46)."),
], 20)

SOURCES = [
    "Constituição da República Federativa do Brasil de 1988, arts. 76 a 91; EC 111/2021.",
    "Lei 1.079/1950 (crimes de responsabilidade).",
    "Supremo Tribunal Federal: Súmula Vinculante 46; ADI 5.540.",
    SRC_A,
]
