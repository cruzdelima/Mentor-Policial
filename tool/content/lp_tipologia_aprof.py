# -*- coding: utf-8 -*-
"""Língua Portuguesa · Tipologia e gêneros textuais — MATERIAL APROFUNDADO (estudo inicial)."""
from common import *

MATERIAL = material(
    "lp-tipologia-02", "LP", "LP-15", "aprofundado", "Tipologia e gêneros textuais", "Língua Portuguesa · Texto",
    "portugues_tipologia_aprofundado", "Portugues_Tipologia_Generos_APROFUNDADO.pdf", None, ["Tipologia e", "gêneros textuais"],
    ["Teoria completa para o primeiro estudo: tipos textuais, gêneros e como reconhecer cada um,", "com 20 questões no estilo Cebraspe."],
    [("01", "Tipo × gênero", "a diferença que a banca cobra"),
     ("02", "Os tipos", "narrativo, descritivo, expositivo, argumentativo, injuntivo"),
     ("03", "Marcas linguísticas", "tempos verbais, pessoa e conectores de cada tipo"),
     ("04", "Gêneros", "jornalísticos, oficiais e do dia a dia policial"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Tipologia e gêneros textuais (Língua Portuguesa)",
    "Base: gramáticas de referência e estudos de linguística textual (Marcuschi).", 90)

THEORY = [
    exam("Como estudar este material",
         "O Cebraspe pergunta “o texto é predominantemente narrativo / argumentativo?” e “o texto pertence ao gênero X”. "
         "Para acertar, olhe a **finalidade** do texto (contar, descrever, informar, convencer, orientar) e as **marcas linguísticas** "
         "(tempos verbais, pessoa, conectores). O assunto do texto não define o tipo."),

    h2("1. Tipo textual × gênero textual"),
    tb(["", "Tipo textual", "Gênero textual"], [0.18, 0.41, 0.41], [
        ("O que é", "Sequência linguística definida pela estrutura e pela finalidade", "Texto concreto, reconhecido socialmente, com função e formato próprios"),
        ("Quantidade", "Poucos (cinco ou seis)", "Ilimitados (surgem e desaparecem)"),
        ("Exemplos", "narrativo, descritivo, expositivo, argumentativo, injuntivo", "notícia, editorial, boletim de ocorrência, ofício, edital, receita, crônica"),
    ]),
    p("Um **gênero** costuma ter um tipo **predominante**, mas mistura sequências de outros tipos (**heterogeneidade tipológica**). "
      "Um boletim de ocorrência, por exemplo, é predominantemente narrativo, mas descreve o suspeito e os objetos."),

    h2("2. Os tipos textuais"),
    tb(["Tipo", "Finalidade", "Marcas linguísticas"], [0.17, 0.3, 0.53], [
        ("Narrativo", "Contar fatos em sequência temporal", "Personagens, narrador, tempo e espaço; verbos de ação no **pretérito perfeito**; marcadores de tempo (*depois, em seguida, às 22h*)"),
        ("Descritivo", "Caracterizar seres, objetos, lugares", "Adjetivos e locuções adjetivas; verbos de estado e de ligação; **pretérito imperfeito** ou presente; enumeração de traços"),
        ("Expositivo", "Informar, explicar um conceito ou fenômeno", "3ª pessoa, **presente** atemporal, definições, exemplos, dados; tom neutro"),
        ("Argumentativo (dissertativo-argumentativo)", "Convencer: defender uma tese", "Tese, argumentos e conclusão; **operadores argumentativos** (*portanto, além disso, no entanto*); modalizadores (*é necessário, certamente*)"),
        ("Injuntivo (instrucional)", "Orientar, instruir, ordenar", "**Imperativo** ou **infinitivo**; sequência de passos; enumeração"),
    ]),
    nt("Alguns autores incluem o tipo **dialogal** (conversação, entrevista). O Cebraspe trata o argumentativo e o expositivo como dissertativos; "
       "a diferença é que o expositivo **informa** e o argumentativo **defende um ponto de vista**."),

    h2("3. Como reconhecer o tipo"),
    tb(["Pergunta", "Se a resposta for sim…"], [0.55, 0.45], [
        ("Há fatos que avançam no tempo, com personagens?", "Narrativo"),
        ("O texto pinta um retrato, sem progressão temporal?", "Descritivo"),
        ("Explica um assunto sem tomar partido?", "Expositivo"),
        ("Defende uma ideia e tenta convencer o leitor?", "Argumentativo"),
        ("Diz ao leitor o que fazer?", "Injuntivo"),
    ]),
    trap("O assunto não define o tipo",
         "Um texto sobre um crime pode ser **narrativo** (como aconteceu), **descritivo** (como era o local), **expositivo** (o que diz a lei) "
         "ou **argumentativo** (por que a pena deveria ser maior). Olhe a finalidade, não o tema."),

    h2("4. Gêneros mais cobrados"),
    tb(["Gênero", "Tipo predominante", "Características"], [0.22, 0.24, 0.54], [
        ("Notícia", "Narrativo / expositivo", "Relata fato recente, linguagem impessoal; lide responde o quê, quem, quando, onde, como, por quê"),
        ("Reportagem", "Expositivo", "Aprofunda o tema, com dados, entrevistas e contexto"),
        ("Editorial", "Argumentativo", "Opinião do veículo de imprensa, sem assinatura"),
        ("Artigo de opinião", "Argumentativo", "Opinião assinada por um autor"),
        ("Crônica", "Narrativo (com reflexão)", "Fato do cotidiano, tom leve, pode ter humor, lirismo ou crítica"),
        ("Boletim de ocorrência", "Narrativo", "Relato do fato, com descrição de envolvidos e objetos"),
        ("Laudo pericial", "Descritivo / expositivo", "Descreve vestígios e expõe conclusões técnicas"),
        ("Relatório", "Expositivo / narrativo", "Relata atividades e resultados, com conclusões"),
        ("Edital", "Injuntivo / expositivo", "Torna público e estabelece regras e prazos"),
        ("Ofício", "Expositivo / injuntivo", "Comunicação oficial entre órgãos (padrão ofício)"),
        ("Manual, receita", "Injuntivo", "Instruções em passos"),
    ]),

    h2("5. Como o Cebraspe cobra"),
    bl("“O texto é predominantemente narrativo / descritivo / argumentativo.”",
       "“Trata-se de texto do gênero X” — confira a finalidade e o suporte (jornal, documento oficial).",
       "“O texto apresenta trechos descritivos, embora seja predominantemente narrativo” — heterogeneidade tipológica.",
       "Marcas linguísticas: “predominam verbos no pretérito perfeito, típicos da narração”."),
]

T1 = ("Às 22h, a guarnição recebeu o chamado. Minutos depois, chegou ao local, encontrou a porta arrombada e deteve dois suspeitos "
      "que fugiam pelos fundos.")
T2 = ("A ampliação do videomonitoramento é necessária. Além de inibir delitos, as imagens agilizam as investigações. "
      "Portanto, investir em câmeras é investir em segurança.")
T3 = "O suspeito tinha cerca de 1,80 m, cabelos curtos e grisalhos e usava jaqueta escura e tênis brancos."
T4 = "Mantenha a calma. Não reaja. Memorize as características do assaltante e acione a polícia assim que possível."

QUIZ = quiz([
    ("C", "O texto narrativo organiza fatos em sequência temporal e apresenta personagens, tempo e espaço.",
     "São os elementos característicos da narração."),
    ("E", "O texto descritivo caracteriza-se pela defesa de uma tese por meio de argumentos.",
     "Defender tese é próprio do texto argumentativo; o descritivo caracteriza seres e lugares."),
    ("C", "Textos injuntivos empregam formas verbais no imperativo ou no infinitivo para orientar o leitor.",
     "É o caso de manuais, receitas e instruções de editais."),
    ("E", "Tipo textual e gênero textual são expressões sinônimas.",
     "Tipos são poucas sequências estruturais; gêneros são textos concretos e ilimitados."),
    ("C", "O editorial é gênero predominantemente argumentativo.",
     "Expressa a opinião do veículo de imprensa sobre um tema."),
    ("E", "A notícia tem como característica principal a defesa da opinião do jornalista.",
     "A notícia relata fatos com linguagem impessoal; a opinião é própria do artigo e do editorial."),
    ("C", "Um mesmo gênero pode apresentar sequências de tipos textuais diferentes.",
     "É a heterogeneidade tipológica: um boletim de ocorrência narra e também descreve."),
    ("E", "No texto expositivo, predominam a primeira pessoa e a expressão de opiniões pessoais.",
     "O expositivo informa com linguagem impessoal, em 3ª pessoa."),
    ("C", "O boletim de ocorrência é gênero em que predomina a sequência narrativa.",
     "Relata um fato em ordem temporal, com envolvidos e circunstâncias."),
    ("E", "Receitas culinárias são exemplos típicos de texto descritivo.",
     "Receitas orientam o leitor passo a passo: são injuntivas."),

    ("C", "O trecho é predominantemente narrativo.",
     "Há ações em sequência temporal (recebeu, chegou, encontrou, deteve) e marcadores de tempo.", T1),
    ("E", "No trecho, predominam formas verbais no pretérito imperfeito, típicas da descrição.",
     "Predominam formas no pretérito perfeito (recebeu, chegou, deteve), típicas da narração."),
    ("C", "O texto é argumentativo: apresenta tese, argumentos e conclusão.",
     "A tese (a ampliação é necessária) é sustentada por argumentos e retomada na conclusão.", T2),
    ("E", "No texto, o conector Portanto introduz um argumento contrário à tese.",
     "Portanto introduz a conclusão, favorável à tese."),
    ("C", "No trecho, predomina a sequência descritiva.",
     "O trecho caracteriza o suspeito, com verbos no imperfeito e adjetivos.", T3),
    ("E", "O trecho é injuntivo, pois orienta o leitor a agir.",
     "O trecho não dá instruções; apenas caracteriza o suspeito."),
    ("C", "O trecho é injuntivo.",
     "Orienta o leitor sobre como agir, com verbos no imperativo.", T4),
    ("E", "No trecho, as formas verbais estão no modo indicativo, como é típico das instruções.",
     "As formas mantenha, reaja, memorize e acione estão no imperativo."),
    ("C", "O edital de concurso público é gênero em que predominam sequências injuntivas e expositivas.",
     "Estabelece regras e prazos e expõe informações sobre o certame."),
    ("E", "A crônica é gênero exclusivamente argumentativo, sem trechos narrativos.",
     "A crônica parte em geral de um fato do cotidiano narrado, acrescido de reflexão."),
], 20)

SOURCES = [GRAM, "Luiz Antônio Marcuschi, Produção textual, análise de gêneros e compreensão.", SRC_A]
