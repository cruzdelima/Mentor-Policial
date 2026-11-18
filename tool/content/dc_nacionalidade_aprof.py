# -*- coding: utf-8 -*-
"""Direito Constitucional · Nacionalidade (arts. 12 e 13) — MATERIAL APROFUNDADO."""
from common import *

MATERIAL = material(
    "dc-nacionalidade-02", "DC", "DC-05", "aprofundado", "Nacionalidade (arts. 12 e 13)", "Direito Constitucional · Direitos fundamentais",
    "constitucional_nacionalidade_aprofundado", "Constitucional_Nacionalidade_APROFUNDADO.pdf", None, ["Nacionalidade"],
    ["Brasileiros natos e naturalizados, portugueses, cargos privativos e perda da nacionalidade", "após a EC 131/2023, com 20 questões no estilo Cebraspe."],
    [("01", "Conceitos", "nato, naturalizado, critérios de solo e de sangue"),
     ("02", "Natos", "as três hipóteses do art. 12, I"),
     ("03", "Naturalizados", "ordinária, extraordinária, portugueses"),
     ("04", "Diferenças e perda", "cargos privativos, extradição, EC 131/2023"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Nacionalidade (arts. 12 e 13) — Direito Constitucional",
    "Base: Constituição Federal de 1988, Lei 13.445/2017 e jurisprudência do STF.", 90)

THEORY = [
    exam("Como estudar este material",
         "Nacionalidade é tema curto e muito cobrado. Domine as **três hipóteses de brasileiro nato**, as **duas de naturalização**, a lista dos "
         "**cargos privativos de nato** e as **hipóteses de perda**, que mudaram com a **EC 131/2023**. Questões antigas sobre perda pela "
         "aquisição de outra nacionalidade estão **desatualizadas**."),

    h2("1. Conceitos"),
    tb(["Termo", "Significado"], [0.26, 0.74], [
        ("Nacionalidade", "Vínculo jurídico-político que liga a pessoa a um Estado e a torna parte do seu **povo**."),
        ("Povo", "Conjunto dos nacionais (natos e naturalizados)."),
        ("População", "Todos os que estão no território, nacionais ou estrangeiros (conceito demográfico)."),
        ("Cidadão", "O nacional no gozo dos **direitos políticos**."),
        ("Primária (originária)", "Decorre do **nascimento**: é a do brasileiro **nato**. Ato unilateral do Estado."),
        ("Secundária (adquirida)", "Decorre de **ato de vontade** posterior: é a do brasileiro **naturalizado**."),
        ("Polipátrida", "Quem tem mais de uma nacionalidade."),
        ("Apátrida (heimatlos)", "Quem não tem nenhuma nacionalidade."),
    ]),
    p("Há dois critérios para atribuir a nacionalidade primária: o **ius soli** (local do nascimento) e o **ius sanguinis** (nacionalidade dos "
      "pais). O Brasil adota o **ius soli como regra**, com hipóteses de **ius sanguinis** combinadas com outros requisitos."),

    h2("2. Brasileiros natos (art. 12, I)"),
    tb(["Alínea", "Hipótese", "Critério"], [0.1, 0.66, 0.24], [
        ("a", "Nascidos **no Brasil**, ainda que de pais estrangeiros, **desde que estes não estejam a serviço de seu país**.", "Ius soli"),
        ("b", "Nascidos **no estrangeiro**, de pai **ou** mãe brasileiros, desde que **qualquer deles** esteja **a serviço da República Federativa do Brasil**.", "Ius sanguinis + serviço"),
        ("c", "Nascidos no estrangeiro, de pai ou mãe brasileiros, desde que sejam **registrados em repartição brasileira competente** "
              "**ou** venham a **residir no Brasil** e optem, **em qualquer tempo**, depois de atingida a **maioridade**, pela nacionalidade brasileira.",
         "Ius sanguinis + registro ou residência e opção"),
    ]),
    bl("Na alínea **a**, a exceção exige que os pais estrangeiros estejam **a serviço do seu país** (ex.: filho de diplomata francês). Se "
       "estiverem a serviço de **outro** país ou de empresa privada, o filho é brasileiro nato.",
       "Na alínea **b**, “a serviço da República” abrange a administração **direta e indireta** de **qualquer ente** (União, Estados, DF e Municípios).",
       "Na alínea **c**, a **opção** é ato **personalíssimo**, feito na **Justiça Federal** (art. 109, X), e só pode ser exercida após a "
       "maioridade. Para o STF, enquanto **menor**, o filho que veio residir no Brasil é tido como brasileiro nato; atingida a maioridade, "
       "a nacionalidade fica sob **condição suspensiva** até que a opção seja feita.",
       "A redação atual da alínea c, que voltou a admitir o **registro consular**, veio da **EC 54/2007**."),

    h2("3. Brasileiros naturalizados (art. 12, II)"),
    tb(["Espécie", "Requisitos", "Natureza"], [0.22, 0.52, 0.26], [
        ("**Ordinária** (alínea a)", "Na forma da **lei** (Lei de Migração, 13.445/2017). Para **originários de países de língua portuguesa**, "
                                     "a Constituição exige apenas **residência por 1 ano ininterrupto** e **idoneidade moral**.", "Ato **discricionário** do Executivo"),
        ("**Extraordinária** (alínea b)", "Estrangeiros de **qualquer nacionalidade**, residentes no Brasil **há mais de 15 anos ininterruptos** "
                                          "e **sem condenação penal**, desde que **requeiram**.", "**Direito subjetivo**: preenchidos os requisitos, não pode ser negada"),
    ]),
    nt("Viagens curtas ao exterior **não interrompem** a residência contínua exigida para a naturalização, segundo a jurisprudência. "
       "A entrega do certificado de naturalização é ato do Poder Executivo (Ministério da Justiça)."),
    h3("Portugueses: a quase-nacionalidade (§ 1º)"),
    key("Texto da Constituição",
        "§ 1º Aos **portugueses** com **residência permanente** no País, **se houver reciprocidade** em favor de brasileiros, serão atribuídos os "
        "direitos inerentes ao **brasileiro**, salvo os casos previstos nesta Constituição."),
    bl("O português equiparado **não se naturaliza**: continua português, mas exerce direitos de brasileiro **naturalizado** (pode até votar e "
       "ser votado, se tiver o estatuto de igualdade de direitos políticos).",
       "Não pode ocupar os **cargos privativos de nato** e pode ser **extraditado**, mas apenas para **Portugal**."),

    h2("4. Diferenças entre natos e naturalizados"),
    key("Regra (§ 2º)",
        "A **lei não poderá** estabelecer distinção entre brasileiros natos e naturalizados, **salvo nos casos previstos nesta Constituição**. "
        "Só a própria Constituição pode diferenciar."),
    tb(["Diferença", "Onde"], [0.66, 0.34], [
        ("**Cargos privativos de brasileiro nato**", "Art. 12, § 3º"),
        ("**Extradição**: nato nunca; naturalizado por crime comum anterior ou tráfico", "Art. 5º, LI"),
        ("**Conselho da República**: seis cidadãos brasileiros **natos**", "Art. 89, VII"),
        ("**Empresa jornalística e de radiodifusão**: propriedade privativa de natos ou naturalizados **há mais de 10 anos**", "Art. 222"),
        ("**Perda** por cancelamento da naturalização (só atinge naturalizado)", "Art. 12, § 4º, I"),
    ]),
    key("Cargos privativos de nato: MP3.COM",
        "**M**inistro do STF · **P**residente e Vice-Presidente da República · **P**residente da Câmara · **P**residente do Senado · "
        "**C**arreira diplomática · **O**ficial das Forças Armadas · **M**inistro de Estado da Defesa."),
    trap("Pegadinha: cargos que NÃO são privativos",
         "**Senador, deputado, ministro de Estado** (salvo o da Defesa), **ministro do STJ ou do TSE**, **governador**, **delegado** e "
         "**Procurador-Geral da República** podem ser ocupados por **naturalizado**. Os presidentes da Câmara e do Senado precisam ser natos "
         "porque estão na **linha sucessória** da Presidência da República; por isso também os ministros do STF (o presidente do STF a integra)."),

    h2("5. Perda da nacionalidade (§ 4º, EC 131/2023)"),
    key("Texto da Constituição",
        "§ 4º Será declarada a perda da nacionalidade do brasileiro que: I – tiver **cancelada sua naturalização**, por **sentença judicial**, em "
        "virtude de **fraude relacionada ao processo de naturalização** ou de **atentado contra a ordem constitucional e o Estado Democrático**; "
        "II – fizer **pedido expresso** de perda da nacionalidade brasileira perante **autoridade brasileira competente**, **ressalvadas situações "
        "que acarretem apatridia**."),
    tb(["Hipótese", "Atinge", "Como"], [0.42, 0.24, 0.34], [
        ("Cancelamento da naturalização (fraude ou atentado à ordem constitucional)", "Só o **naturalizado**", "**Sentença judicial** (Justiça Federal)"),
        ("Pedido expresso de perda", "**Nato** e naturalizado", "Requerimento à autoridade brasileira; vedado se gerar **apatridia**"),
    ]),
    bl("**§ 5º**: a renúncia (pedido expresso) **não impede** o interessado de **readquirir** a nacionalidade brasileira **originária**, nos "
       "termos da lei.",
       "Desde a EC 131/2023, **adquirir outra nacionalidade não faz perder a brasileira**. A regra antiga (perda por naturalização voluntária no "
       "exterior, com exceções) foi **revogada**.",
       "Também saiu a expressão “**atividade nociva ao interesse nacional**”, substituída por fraude e atentado contra a ordem constitucional."),
    trap("Pegadinha da atualização",
         "Itens que afirmam “perde a nacionalidade o brasileiro que adquirir outra nacionalidade” estão **errados** desde outubro de 2023. "
         "E o cancelamento da naturalização exige **sentença judicial**, não ato do Ministro da Justiça."),

    h2("6. Art. 13: idioma e símbolos"),
    bl("A **língua portuguesa** é o idioma oficial da República Federativa do Brasil.",
       "São símbolos da República a **bandeira**, o **hino**, as **armas** e o **selo** nacionais.",
       "Os **Estados, o DF e os Municípios** **poderão** ter símbolos próprios."),
]

QUIZ = quiz([
    ("C", "É brasileiro nato o filho de estrangeiros nascido no Brasil, desde que nenhum dos pais esteja a serviço de seu país.",
     "É o critério do solo, com a exceção do art. 12, I, a."),
    ("E", "O filho de pai brasileiro nascido no exterior só será brasileiro nato se ambos os pais estiverem a serviço da República Federativa do Brasil.",
     "Basta que qualquer deles esteja a serviço do Brasil."),
    ("C", "O nascido no estrangeiro, de mãe brasileira, que seja registrado em repartição brasileira competente é brasileiro nato.",
     "Art. 12, I, c, na redação da EC 54/2007."),
    ("E", "A opção pela nacionalidade brasileira, prevista no art. 12, I, c, pode ser feita pelos pais, em nome do filho menor, perante o cartório de registro civil.",
     "A opção é personalíssima, só após a maioridade, e se processa na Justiça Federal."),
    ("C", "Para os originários de países de língua portuguesa, a Constituição exige, para a naturalização, apenas residência por um ano ininterrupto e idoneidade moral.",
     "Art. 12, II, a."),
    ("E", "O estrangeiro residente no Brasil há mais de dez anos ininterruptos e sem condenação penal pode requerer a naturalização extraordinária.",
     "Exige-se residência há mais de quinze anos ininterruptos."),
    ("C", "A lei não pode estabelecer distinções entre brasileiros natos e naturalizados, salvo nos casos previstos na própria Constituição.",
     "Art. 12, § 2º."),
    ("E", "O cargo de senador da República é privativo de brasileiro nato.",
     "Só a presidência do Senado é privativa de nato."),
    ("C", "O cargo de Ministro de Estado da Defesa é privativo de brasileiro nato.",
     "Art. 12, § 3º, VII."),
    ("E", "Perde a nacionalidade brasileira quem adquirir outra nacionalidade de forma voluntária, salvo quando a lei estrangeira impuser a naturalização como condição de permanência.",
     "Essa regra foi revogada pela EC 131/2023: a aquisição de outra nacionalidade não acarreta mais a perda."),

    ("C", "Um casal de turistas argentinos teve um filho durante as férias em Florianópolis. Nessa situação, a criança é brasileira nata.",
     "Os pais não estavam a serviço da Argentina; aplica-se o critério do solo."),
    ("E", "Filho de diplomata italiano a serviço da Itália, nascido em Brasília, é brasileiro nato, pois a Constituição adota o critério do solo sem exceções.",
     "Quando os pais estrangeiros estão a serviço de seu país, o filho nascido no Brasil não é brasileiro nato."),
    ("C", "Filho de servidora de autarquia estadual brasileira que estava em missão oficial no exterior, nascido no estrangeiro, é brasileiro nato.",
     "A expressão a serviço da República abrange a administração direta e indireta de qualquer ente federativo."),
    ("E", "Um brasileiro naturalizado pode ser eleito presidente da Câmara dos Deputados, desde que tenha mais de trinta e cinco anos de idade.",
     "A presidência da Câmara é privativa de brasileiro nato."),
    ("C", "O brasileiro naturalizado pode ser nomeado ministro do Superior Tribunal de Justiça.",
     "Apenas o cargo de ministro do STF é privativo de nato."),
    ("E", "O cancelamento da naturalização por fraude no processo pode ser declarado por ato administrativo do Ministro da Justiça.",
     "O art. 12, § 4º, I, exige sentença judicial."),
    ("C", "Brasileiro nato que faça pedido expresso de perda da nacionalidade perante autoridade brasileira competente poderá perdê-la, desde que isso não o torne apátrida, e poderá readquirir a nacionalidade originária, nos termos da lei.",
     "É a combinação do § 4º, II, com o § 5º do art. 12 (EC 131/2023)."),
    ("E", "Os portugueses com residência permanente no Brasil, havendo reciprocidade, são considerados brasileiros natos.",
     "Recebem os direitos de brasileiro, mas não se tornam natos nem naturalizados; não podem ocupar cargos privativos de nato."),
    ("C", "A propriedade de empresa jornalística pode pertencer a brasileiro naturalizado há mais de dez anos.",
     "Art. 222."),
    ("E", "Os municípios não podem ter símbolos próprios, pois a Constituição reserva à União a definição de bandeira, hino, armas e selo.",
     "O art. 13, § 2º, permite que Estados, DF e Municípios tenham símbolos próprios."),
], 20)

SOURCES = [
    "Constituição da República Federativa do Brasil de 1988, arts. 5º, LI, 12, 13, 89 e 222; EC 54/2007 e EC 131/2023.",
    "Lei 13.445/2017 (Lei de Migração).",
    "Doutrina de referência: Lenza, Direito constitucional; Mendes e Branco, Curso de direito constitucional.",
    SRC_A,
]
