# -- coding: utf-8 --
"""Língua Portuguesa · Ortografia oficial — RESUMO (revisão)."""
from common import *

MATERIAL = {
    "id": "lp-ortografia-01",
    "version": "0.1.0",
    "status": "Em revisão pelo autor",
    "subjectId": "LP",
    "topicIds": ["LP-01"],
    "kind": "resumo",
    "title": "Ortografia oficial",
    "subtitle": "Língua Portuguesa · Ortografia",
    "minutes": 45,
    "folder": "portugues_ortografia",
    "pdf": "portugues_ortografia.pdf",
    "outName": "Portugues_Ortografia_RESUMO.pdf",
    "header": "Língua Portuguesa · Ortografia oficial",
    "coverKicker": "Língua Portuguesa  ·  Ortografia",
    "coverTitle": ["Ortografia oficial"],
    "coverSub": ["Resumo direto ao ponto, quadros de consulta, mapa mental", "e 10 questões no estilo Cebraspe com gabarito comentado."],
    "coverItems": [("01", "Teoria", "letras, pares perigosos, porquês e hífen"),
                   ("02", "Resumo", "quadro do hífen e “leve para a prova”"),
                   ("03", "Mapa mental", "uma página para revisar em 5 minutos"),
                   ("04", "Questões", "10 itens certo/errado + gabarito comentado")],
    "coverTopic": "Tópico do edital: Ortografia oficial (Língua Portuguesa)",
    "coverBase": "Base: Acordo Ortográfico da Língua Portuguesa (Decreto nº 6.583/2008) e VOLP.",
}

THEORY = [
    exam("O que a banca cobra",
         "Em ortografia, o Cebraspe quase sempre propõe uma **troca**: de uma palavra por outra parecida (mandado/mandato), de uma grafia por outra "
         "(por que/porque, mal/mau) ou a retirada de um hífen. Julgue sempre duas coisas: a **correção gramatical** e o **sentido**."),

    h2("1. O Acordo em quatro linhas"),
    bl("Alfabeto com **26 letras** (K, W e Y voltaram).",
       "**Trema** abolido (permanece só em nomes estrangeiros e derivados). **A pronúncia não mudou.**",
       "Obrigatório no Brasil desde **1º/1/2016** (Decreto nº 6.583/2008).",
       "Mudou regras de **acentuação** (outro material) e de **hífen**."),

    h2("2. Emprego das letras"),
    tb(["Letra", "Regra", "Exemplos"], [0.12, 0.46, 0.42], [
        ("S", "-ês/-esa (origem, título); -oso/-osa; depois de ditongo; verbos pôr e querer", "português, marquesa, gostoso, coisa, pus, quis"),
        ("S × Z", "**-isar** se a primitiva tem S; **-izar** se não tem", "análise › analisar; real › realizar"),
        ("Z", "-ez/-eza (substantivo abstrato vindo de adjetivo)", "rapidez, beleza, pobreza"),
        ("X", "Depois de ditongo, de **en-** e de **me-**", "caixa, enxada, mexer (exceções: encher, encharcar, mecha)"),
        ("G", "-agem, -igem, -ugem; -ágio, -égio, -ígio, -ógio, -úgio", "garagem, vertigem, relógio (exceções: pajem, lambujem)"),
        ("J", "Verbos em -jar; origem tupi/africana; derivadas de palavra com J", "viajem (verbo), jiboia, laranjeira"),
        ("Ç", "Depois de ditongo; verbos em **-ter** › -tenção", "eleição, traição; reter › retenção"),
        ("SS", "-ced- › -cess-; -gred- › -gress-; -prim- › -press-; -tir › -ssão", "cessão, agressão, impressão, discussão"),
        ("S", "-nd- › -ns-; -rt-/-rg- › -rs-", "pretensão, ascensão, conversão, imersão"),
    ]),
    trap("Pegadinha: três grafias",
         "**Cessão** = ato de ceder. **Sessão** = reunião. **Seção** = parte, setor. E **viagem** é substantivo; **viajem** é verbo."),

    h2("3. Pares perigosos"),
    tb(["Palavra", "Sentido", "Palavra", "Sentido"], [0.17, 0.33, 0.17, 0.33], [
        ("mandado", "ordem judicial", "mandato", "poder; período do cargo"),
        ("ratificar", "confirmar", "retificar", "corrigir"),
        ("infligir", "aplicar pena", "infringir", "violar a lei"),
        ("iminente", "prestes a ocorrer", "eminente", "ilustre"),
        ("deferir", "conceder", "diferir", "adiar; divergir"),
        ("descriminar", "deixar de ser crime", "discriminar", "distinguir; segregar"),
        ("tráfico", "comércio ilegal", "tráfego", "trânsito"),
        ("cassar", "anular", "caçar", "perseguir"),
        ("emergir", "vir à tona", "imergir", "mergulhar"),
        ("flagrante", "evidente; no ato", "fragrante", "perfumado"),
        ("descrição", "ato de descrever", "discrição", "reserva"),
        ("tachar", "censurar, rotular", "taxar", "tributar"),
    ]),

    h2("4. Porquês e expressões"),
    tb(["Forma", "Uso", "Teste"], [0.22, 0.48, 0.3], [
        ("por que", "Pergunta (direta ou indireta); = pelo qual", "“por qual razão”"),
        ("por quê", "Fim de frase", "vem antes de ponto"),
        ("porque", "Causa ou explicação", "“pois”"),
        ("porquê", "Substantivo", "“o motivo”"),
        ("mal × mau", "Mal ≠ bem (também = assim que). Mau ≠ bom.", "troque por bem/bom"),
        ("há × a", "Há = tempo passado. A = futuro ou distância.", "troque por “faz”"),
        ("onde × aonde", "Aonde só com verbo de movimento que pede a.", "“a que lugar”"),
        ("ao encontro de × de encontro a", "A favor × contra.", ""),
        ("a fim de × afim", "Para × semelhante.", ""),
        ("senão × se não", "Caso contrário × caso não.", ""),
        ("à medida que × na medida em que", "Proporção × causa.", "não existe “à medida em que”"),
    ]),

    h2("5. Hífen"),
    key("Regra de bolso",
        "**Letras iguais se separam, letras diferentes se juntam; H sempre com hífen; R e S dobram depois de vogal.**"),
    tb(["Situação", "Hífen?", "Exemplos"], [0.42, 0.14, 0.44], [
        ("2º elemento começa com H", "Sim", "anti-higiênico, super-homem"),
        ("Vogais iguais", "Sim", "micro-ondas, contra-ataque"),
        ("Vogais diferentes", "Não", "autoescola, infraestrutura"),
        ("Vogal + R ou S", "Não (dobra)", "antirracismo, ultrassom, minissaia"),
        ("R + R", "Sim", "inter-regional, super-resistente"),
        ("ex-, vice-, pós-, pré-, pró-, recém-, além-, aquém-, sem-", "Sempre", "ex-diretor, pré-natal, recém-nascido"),
        ("co-, re-, pre-, pro- (átonos)", "Nunca", "coordenar, reeditar, preexistente"),
        ("sub- + B, H, R", "Sim", "sub-base, sub-região"),
        ("mal- + vogal, H, L", "Sim", "mal-estar, mal-humorado; mas malcriado"),
        ("Composto sem elemento de ligação", "Sim", "guarda-chuva, segunda-feira, decreto-lei"),
        ("Locução com elemento de ligação", "Não", "dia a dia, fim de semana, mão de obra, pé de moleque"),
        ("Exceções e espécies de plantas e animais", "Sim", "cor-de-rosa, pé-de-meia, bem-te-vi, erva-doce"),
        ("Perdeu a noção de composição", "Junto", "paraquedas, girassol, mandachuva, pontapé"),
        ("não e quase como prefixo", "Não", "não agressão, quase delito"),
    ]),
]

SUMMARY = [
    h2("Leve para a prova"),
    bl("O Acordo mudou a **grafia**, nunca a **pronúncia**.",
       "Dúvida entre S e Z no verbo? Olhe a **primitiva**: analisar (análise), realizar (real).",
       "**-nd- › -ns-** (pretensão) e **-ter › -tenção** (retenção): as duas correlações mais cobradas.",
       "**Mandado** é ordem; **mandato** é poder ou período. **Ratificar** confirma; **retificar** corrige.",
       "Troca de parônimos: em regra, **mantém a correção** e **altera o sentido**.",
       "**Por que** em pergunta, mesmo indireta; **porque** quando cabe “pois”.",
       "Hífen: **iguais separam, diferentes juntam, H separa, R e S dobram**.",
       "**Dia a dia**, **fim de semana** e **mão de obra**: sem hífen.",
       "**Co-, re-, pre-** juntam sempre: coordenar, reeditar, preexistente.",
       "Em ortografia, desconfie de **sempre** e **nunca** no enunciado."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "ORTOGRAFIA OFICIAL",
    "rootSub": "Acordo de 1990 · obrigatório desde 2016",
    "left": [
        {"label": "Acordo", "items": ["26 letras: K, W e Y", "Trema abolido; pronúncia igual", "Mudou acento e hífen"]},
        {"label": "S e Z", "items": ["-ês/-esa: origem e título", "-ez/-eza: substantivo abstrato", "-isar (análise) × -izar (real)"]},
        {"label": "X, CH, G e J", "items": ["X após ditongo, en- e me-", "-agem, -ígio: com G", "viagem (nome) × viajem (verbo)"]},
        {"label": "SS, Ç e S", "items": ["-ced-/-tir › SS: cessão, discussão", "-nd- › S: pretensão", "-ter › Ç: retenção"]},
        {"label": "Pares perigosos", "items": ["mandado × mandato", "ratificar × retificar", "infligir × infringir"]},
    ],
    "right": [
        {"label": "Porquês", "items": ["por que: pergunta", "por quê: fim de frase", "porque: pois · porquê: o motivo"]},
        {"label": "Expressões", "items": ["mal ≠ bem · mau ≠ bom", "há: passado · a: futuro", "ao encontro de ≠ de encontro a"]},
        {"label": "Hífen: prefixos", "items": ["Iguais separam: micro-ondas", "Diferentes juntam: autoescola", "H separa; R e S dobram"]},
        {"label": "Hífen: sempre e nunca", "items": ["Sempre: ex-, vice-, pré-, recém-", "Nunca: co-, re-, pre- átono", "não e quase: sem hífen"]},
        {"label": "Hífen: compostos", "items": ["guarda-chuva, decreto-lei", "dia a dia, fim de semana", "paraquedas, girassol"]},
    ],
}

QUIZ = quiz([
    ("E", "Com a abolição do trema pelo Acordo Ortográfico, palavras como linguiça e cinquenta passaram a ser pronunciadas sem o som da letra u.",
     "O trema saiu da escrita, mas a pronúncia permaneceu a mesma."),
    ("C", "As palavras beleza e rapidez grafam-se com Z por serem substantivos abstratos derivados de adjetivos.",
     "Belo › beleza; rápido › rapidez: sufixos -eza e -ez."),
    ("E", "As formas verbais realisar e civilisar estão corretamente grafadas, pois os verbos terminados em -isar sempre se escrevem com S.",
     "Real e civil não têm S no radical: o sufixo é -izar (realizar, civilizar). Usa-se -isar quando a primitiva já tem S, como em análise › analisar."),
    ("C", "Em “A cessão do imóvel foi aprovada na sessão de ontem”, os vocábulos cessão e sessão estão empregados corretamente.",
     "Cessão = ato de ceder; sessão = reunião."),
    ("E", "No trecho “O deputado teve o mandado cassado”, o vocábulo mandado está empregado corretamente.",
     "O período de exercício de cargo eletivo é mandato. Mandado é ordem judicial."),
    ("C", "Em “Ninguém soube explicar o porquê da demora”, a grafia porquê está correta, por se tratar de substantivo.",
     "Vem com artigo e equivale a “o motivo”."),
    ("E", "Em “O relatório foi entregue a dois dias”, o emprego de a está correto, por indicar tempo decorrido.",
     "Tempo decorrido pede o verbo haver: há dois dias (= faz dois dias)."),
    ("C", "As palavras autoescola e infraestrutura dispensam o hífen porque o prefixo termina em vogal diferente daquela que inicia o segundo elemento.",
     "Vogais diferentes se juntam."),
    ("E", "Deve-se grafar com hífen a palavra ultra-som, visto que o segundo elemento se inicia por consoante.",
     "Prefixo terminado em vogal + S: sem hífen e com a consoante dobrada — ultrassom."),
    ("C", "Grafam-se sem hífen as locuções fim de semana, mão de obra e dia a dia.",
     "Locuções com elemento de ligação perderam o hífen, salvo exceções consagradas, como cor-de-rosa e pé-de-meia."),
], 10)

SOURCES = [
    "Acordo Ortográfico da Língua Portuguesa (1990), promulgado pelo Decreto nº 6.583/2008; VOLP (Academia Brasileira de Letras).",
    "Texto e questões elaborados para o Taticum (itens inéditos no estilo Cebraspe).",
]
