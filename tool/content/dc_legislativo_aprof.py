# -*- coding: utf-8 -*-
"""Direito Constitucional · Poder Legislativo e processo legislativo — MATERIAL APROFUNDADO."""
from common import *

MATERIAL = material(
    "dc-legislativo-02", "DC", "DC-09", "aprofundado", "Poder Legislativo e processo legislativo", "Direito Constitucional · Organização dos Poderes",
    "constitucional_legislativo_aprofundado", "Constitucional_Poder_Legislativo_APROFUNDADO.pdf", None, ["Poder", "Legislativo"],
    ["Congresso, Câmara e Senado, imunidades parlamentares, CPI e as espécies normativas,", "de emenda constitucional a medida provisória, com 20 questões."],
    [("01", "Estrutura", "Câmara, Senado e competências"),
     ("02", "Estatuto dos congressistas", "imunidades, foro, perda do mandato"),
     ("03", "CPI e TCU", "o que a CPI pode e não pode fazer"),
     ("04", "Processo legislativo", "EC, leis, sanção, veto, MP, lei delegada"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Poder Legislativo e processo legislativo (arts. 44 a 75) — Direito Constitucional",
    "Base: Constituição Federal de 1988 e jurisprudência do STF.", 150)

THEORY = [
    exam("Como estudar este material",
         "A banca cobra **números** (mandatos, quóruns, prazos), as **imunidades** dos parlamentares (prisão só em flagrante de crime "
         "inafiançável) e os **limites da CPI** (o que é reserva de jurisdição). No processo legislativo, o foco é a **emenda constitucional**, "
         "o **veto** e a **medida provisória**."),

    h2("1. Estrutura do Poder Legislativo"),
    p("O Legislativo federal adota o **bicameralismo federativo**: o **Congresso Nacional** é composto pela **Câmara dos Deputados** e pelo "
      "**Senado Federal**. Cada **legislatura** dura **4 anos**."),
    tb(["", "Câmara dos Deputados", "Senado Federal"], [0.2, 0.4, 0.4], [
        ("Representa", "O **povo**", "Os **Estados** e o **DF**"),
        ("Sistema eleitoral", "**Proporcional**", "**Majoritário**"),
        ("Número", "Proporcional à população: **mínimo 8**, **máximo 70** por Estado; **4** por Território", "**3 por Estado e DF**, cada um com **2 suplentes**"),
        ("Mandato", "**4 anos**", "**8 anos**; renovação a cada 4 anos, alternadamente, por **1/3** e **2/3**"),
        ("Idade mínima", "21 anos", "35 anos"),
    ]),
    nt("Salvo disposição em contrário, as deliberações de cada Casa e de suas comissões são tomadas por **maioria dos votos**, presente a "
       "**maioria absoluta** de seus membros (art. 47)."),
    h3("Competências em destaque"),
    tb(["Órgão", "Competência", "Exemplos"], [0.18, 0.24, 0.58], [
        ("Congresso (art. 49)", "Exclusiva, por **decreto legislativo**, **sem sanção**",
         "Resolver definitivamente sobre tratados que acarretem encargos gravosos; **aprovar** estado de defesa e intervenção federal; "
         "**autorizar** o estado de sítio; **sustar atos normativos** do Executivo que exorbitem do poder regulamentar; **julgar** as contas do "
         "Presidente; autorizar referendo e convocar plebiscito."),
        ("Câmara (art. 51)", "Privativa, por **resolução**",
         "**Autorizar**, por **2/3**, a instauração de processo contra o Presidente, o Vice e os Ministros de Estado; **tomar as contas** do "
         "Presidente quando não apresentadas em 60 dias."),
        ("Senado (art. 52)", "Privativa, por **resolução**",
         "**Processar e julgar** o Presidente e o Vice nos **crimes de responsabilidade**; julgar Ministros do STF, PGR e AGU nesses crimes; "
         "**aprovar** a escolha de ministros de tribunais superiores, do TCU, do PGR e do presidente do Banco Central; **suspender** a execução "
         "de lei declarada inconstitucional pelo STF em controle difuso (X)."),
    ]),
    key("Impeachment em duas etapas",
        "**Câmara** autoriza por **2/3** (juízo de admissibilidade) › **Senado** processa e julga, em sessão presidida pelo **Presidente do STF**. "
        "Condenação por **2/3** do Senado: **perda do cargo** + **inabilitação por 8 anos** para função pública."),

    h2("2. Estatuto dos congressistas"),
    tb(["Imunidade", "Regra (art. 53)"], [0.24, 0.76], [
        ("**Material** (inviolabilidade)", "Deputados e senadores são **invioláveis, civil e penalmente**, por quaisquer **opiniões, palavras e votos**, "
                                           "desde que ligados ao exercício do mandato. Dentro do Congresso, a proteção é ampla."),
        ("**Foro**", "Desde a **expedição do diploma**, são julgados pelo **STF**. Vale para crimes praticados **no cargo e em razão dele** e, desde "
                     "2025, **subsiste após o fim do mandato** (HC 232.627)."),
        ("**Prisão**", "Desde a expedição do diploma, **não podem ser presos**, **salvo em flagrante de crime inafiançável**. Os autos vão em **24 horas** "
                       "à Casa, que, pelo voto da **maioria de seus membros**, **resolve sobre a prisão**."),
        ("**Processo**", "Recebida a denúncia por crime **posterior à diplomação**, o STF dá ciência à Casa, que, por iniciativa de **partido** nela "
                         "representado e pelo voto da **maioria** de seus membros, pode **sustar o andamento da ação**. O pedido é apreciado em **45 dias**, "
                         "e a sustação **suspende a prescrição**."),
        ("**Testemunho**", "Não são obrigados a testemunhar sobre informações recebidas ou prestadas **em razão do mandato**, nem sobre quem as confiou."),
    ]),
    bl("A **incorporação às Forças Armadas** de parlamentar, ainda que militar e em tempo de guerra, depende de **prévia licença da Casa**.",
       "As imunidades **subsistem durante o estado de sítio** e só podem ser suspensas pelo voto de **2/3** da Casa, quanto a atos praticados "
       "**fora do recinto** do Congresso que sejam incompatíveis com a medida.",
       "**Deputados estaduais** têm as mesmas imunidades (art. 27, § 1º). **Vereadores** têm apenas a imunidade **material**, nos limites da "
       "**circunscrição do Município** (art. 29, VIII): não têm imunidade formal nem foro especial na Constituição Federal.",
       "As imunidades **não** se estendem ao **suplente**, que não exerce o mandato."),
    trap("Pegadinha da prisão em flagrante",
         "Parlamentar só pode ser preso em **flagrante de crime inafiançável**. Em flagrante de crime **afiançável**, não. E quem decide se a "
         "prisão se mantém é a **Casa**, por **maioria absoluta** (dos membros), em votação **aberta**."),
    h3("Perda do mandato (art. 55)"),
    tb(["Causa", "Quem decide"], [0.6, 0.4], [
        ("Infringir as proibições do art. 54; quebra de **decoro**; **condenação criminal transitada em julgado**", "A **Casa**, por **maioria absoluta**, em votação aberta (**cassação**)"),
        ("Faltar a **1/3** das sessões ordinárias; perda ou suspensão dos **direitos políticos**; decretação pela **Justiça Eleitoral**", "A **Mesa**, de ofício ou por provocação (**declaração**)"),
    ]),

    h2("3. CPI e fiscalização"),
    key("Texto da Constituição (art. 58, § 3º)",
        "As CPIs terão **poderes de investigação próprios das autoridades judiciais**, além de outros previstos nos regimentos, e serão criadas pela "
        "Câmara e pelo Senado, **em conjunto ou separadamente**, mediante requerimento de **1/3** de seus membros, para a apuração de **fato "
        "determinado** e por **prazo certo**, sendo suas conclusões, se for o caso, encaminhadas ao **Ministério Público**."),
    tb(["A CPI pode", "A CPI não pode (reserva de jurisdição)"], [0.5, 0.5], [
        ("Quebrar sigilo **bancário, fiscal e de dados** (inclusive registros telefônicos), por decisão fundamentada", "Determinar **interceptação** telefônica"),
        ("Ouvir **testemunhas** e investigados", "Determinar **busca e apreensão domiciliar**"),
        ("Requisitar documentos e informações; realizar perícias", "Decretar **prisão**, salvo em **flagrante**"),
        ("Convocar autoridades", "Decretar **indisponibilidade de bens** ou medidas cautelares"),
    ]),
    bl("A criação é **direito da minoria**: preenchidos os três requisitos (1/3, fato determinado, prazo certo), a CPI deve ser instalada, sem "
       "depender de votação em plenário.",
       "A CPI **não julga nem pune**: suas conclusões vão ao Ministério Público.",
       "O investigado tem **direito ao silêncio** e à assistência de advogado."),
    p("O **controle externo** contábil, financeiro e orçamentário da União é exercido pelo **Congresso Nacional** com o auxílio do **TCU** "
      "(arts. 70 e 71). O TCU tem **9 ministros**: **1/3** escolhido pelo Presidente da República, com aprovação do Senado, e **2/3** pelo "
      "Congresso. O TCU **aprecia** as contas do Presidente (parecer prévio); quem as **julga** é o Congresso."),

    h2("4. Processo legislativo"),
    p("O art. 59 lista as espécies normativas: **emendas à Constituição**, **leis complementares**, **leis ordinárias**, **leis delegadas**, "
      "**medidas provisórias**, **decretos legislativos** e **resoluções**."),
    h3("Emenda constitucional (art. 60)"),
    tb(["Fase", "Regra"], [0.22, 0.78], [
        ("Iniciativa", "**1/3** dos membros da Câmara **ou** do Senado; o **Presidente da República**; **mais da metade das Assembleias Legislativas**, "
                       "cada uma pela maioria relativa de seus membros. (**Não** há iniciativa popular nem do STF.)"),
        ("Votação", "Em **cada Casa**, em **2 turnos**, aprovada por **3/5** dos votos dos respectivos membros."),
        ("Promulgação", "Pelas **Mesas da Câmara e do Senado**, com o respectivo número de ordem. **Não há sanção nem veto**."),
        ("Limites circunstanciais", "Não pode ser emendada na vigência de **intervenção federal**, **estado de defesa** ou **estado de sítio**."),
        ("Limites materiais", "Cláusulas pétreas: **forma federativa**; **voto direto, secreto, universal e periódico**; **separação dos Poderes**; "
                              "**direitos e garantias individuais** (mnemônico **FO-VO-SE-DI**)."),
        ("Reapresentação", "Matéria **rejeitada** ou havida por prejudicada **não pode** ser objeto de nova proposta na **mesma sessão legislativa**."),
    ]),
    h3("Leis complementares e ordinárias"),
    tb(["", "Lei complementar", "Lei ordinária"], [0.2, 0.4, 0.4], [
        ("Quórum", "**Maioria absoluta**", "**Maioria simples** (relativa)"),
        ("Matéria", "Só as que a Constituição **expressamente** reserva", "Residual: tudo o que não for reservado a outra espécie"),
    ]),
    bl("**Iniciativa** (art. 61): qualquer membro ou comissão da Câmara, do Senado ou do Congresso; o Presidente; o **STF**; os **Tribunais "
       "Superiores**; o **PGR**; e os **cidadãos**.",
       "**Iniciativa privativa do Presidente** (§ 1º): efetivos das **Forças Armadas**; criação de **cargos** e aumento de **remuneração** na "
       "administração direta e autárquica; **servidores públicos da União** e seu regime jurídico; criação e extinção de **Ministérios**; "
       "**militares** das Forças Armadas.",
       "Os projetos do Presidente, do STF, dos Tribunais Superiores e de iniciativa popular **começam na Câmara**."),
    h3("Sanção, veto e promulgação (art. 66)"),
    bl("Aprovado o projeto, o Presidente tem **15 dias úteis** para **sancionar** ou **vetar**. O **silêncio** importa **sanção tácita**.",
       "O veto pode ser **total** ou **parcial**; o parcial abrange **texto integral** de artigo, parágrafo, inciso ou alínea (não se vetam "
       "palavras isoladas). Os motivos são comunicados em **48 horas** ao Presidente do Senado.",
       "O veto é apreciado em **sessão conjunta**, em **30 dias**, e só pode ser **rejeitado** pela **maioria absoluta** dos Deputados e Senadores, "
       "em votação **aberta**. Esgotado o prazo, o veto **tranca a pauta** da sessão conjunta.",
       "Promulgação: pelo **Presidente** em 48 horas; se não o fizer, pelo **Presidente do Senado**; se este não o fizer em igual prazo, pelo "
       "**Vice-Presidente do Senado**."),
    h3("Medida provisória (art. 62)"),
    bl("Editada pelo Presidente em caso de **relevância e urgência**, com **força de lei**, e submetida de imediato ao Congresso.",
       "Vigência de **60 dias**, prorrogável **uma vez** por mais **60**. O prazo **não corre no recesso** parlamentar.",
       "Se não for apreciada em **45 dias**, entra em **regime de urgência** e **sobrestá** as demais deliberações da Casa em que estiver (trancamento de pauta).",
       "A votação começa na **Câmara**, após parecer de **comissão mista**.",
       "É **vedada a reedição**, na **mesma sessão legislativa**, de MP rejeitada ou que tenha perdido eficácia por decurso de prazo.",
       "Rejeitada ou caducada, o Congresso disciplina as relações dela decorrentes por **decreto legislativo** em **60 dias**; se não o fizer, as "
       "relações constituídas durante sua vigência **continuam regidas** por ela."),
    key("Matérias vedadas à MP (§ 1º)",
        "**Nacionalidade, cidadania, direitos políticos, partidos e direito eleitoral**; **direito penal, processual penal e processual civil**; "
        "organização do **Judiciário** e do **Ministério Público**; planos plurianuais, diretrizes orçamentárias e orçamento (salvo **créditos "
        "extraordinários**); **detenção ou sequestro de bens e poupança**; matéria reservada a **lei complementar**; matéria já aprovada pelo "
        "Congresso e pendente de sanção ou veto."),
    h3("Lei delegada (art. 68)"),
    p("Elaborada pelo **Presidente**, que solicita a delegação ao Congresso. A delegação tem a forma de **resolução** do Congresso, que especifica "
      "conteúdo e termos. Se a resolução exigir apreciação do projeto pelo Congresso, a votação é **única**, **vedada qualquer emenda**. Não podem "
      "ser delegados: atos de competência exclusiva do Congresso ou privativa de cada Casa, matéria de **lei complementar**, organização do "
      "Judiciário e do MP, **nacionalidade, cidadania, direitos individuais, políticos e eleitorais** e matéria orçamentária."),
]

QUIZ = quiz([
    ("C", "Os senadores são eleitos pelo sistema majoritário, com mandato de oito anos, e cada estado elege três senadores.",
     "Art. 46."),
    ("E", "O número de deputados federais por estado varia entre o mínimo de quatro e o máximo de setenta.",
     "O mínimo por estado é de oito; quatro é o número fixo de cada território."),
    ("C", "Compete privativamente à Câmara dos Deputados autorizar, por dois terços de seus membros, a instauração de processo contra o Presidente da República.",
     "Art. 51, I."),
    ("E", "No processo de impeachment, o Presidente da República é julgado pelo Supremo Tribunal Federal, em sessão presidida pelo presidente do Senado.",
     "Nos crimes de responsabilidade, o julgamento é do Senado, em sessão presidida pelo presidente do STF."),
    ("C", "Deputados e senadores são invioláveis, civil e penalmente, por quaisquer de suas opiniões, palavras e votos.",
     "É a imunidade material do art. 53, caput."),
    ("E", "Desde a posse, os membros do Congresso Nacional não poderão ser presos, salvo em flagrante de crime inafiançável.",
     "A garantia começa com a expedição do diploma, antes da posse."),
    ("C", "As comissões parlamentares de inquérito são criadas mediante requerimento de um terço dos membros da Casa, para apuração de fato determinado e por prazo certo.",
     "Art. 58, § 3º."),
    ("E", "A Constituição pode ser emendada mediante proposta de iniciativa popular, subscrita por um por cento do eleitorado nacional.",
     "O art. 60 não prevê iniciativa popular para emendas constitucionais."),
    ("C", "A emenda constitucional é promulgada pelas Mesas da Câmara dos Deputados e do Senado Federal, não se sujeitando a sanção ou veto.",
     "Art. 60, § 3º."),
    ("E", "A lei complementar é aprovada por maioria simples, presente a maioria absoluta dos membros da Casa.",
     "A lei complementar exige maioria absoluta; a maioria simples é o quórum da lei ordinária."),

    ("C", "Um deputado federal foi surpreendido cometendo crime inafiançável. Nessa situação, ele pode ser preso em flagrante, devendo os autos ser remetidos em vinte e quatro horas à Câmara, que decidirá sobre a prisão pelo voto da maioria de seus membros.",
     "Art. 53, § 2º."),
    ("E", "Comissão parlamentar de inquérito pode determinar, por decisão fundamentada de seus membros, a busca e apreensão de documentos na residência do investigado.",
     "Busca domiciliar é cláusula de reserva de jurisdição: só o juiz pode determinar."),
    ("C", "Comissão parlamentar de inquérito pode determinar a quebra do sigilo bancário de investigado, desde que em decisão fundamentada.",
     "A CPI tem poderes de investigação próprios das autoridades judiciais."),
    ("E", "Vereador tem as mesmas imunidades formais dos deputados federais, de modo que só pode ser preso em flagrante de crime inafiançável.",
     "O vereador só tem a imunidade material, na circunscrição do município."),
    ("C", "Segundo o entendimento firmado pelo STF em 2025, o ex-senador continua a ser julgado pelo STF por crime praticado no exercício do mandato e em razão dele, ainda que a ação penal seja proposta após o fim do mandato.",
     "HC 232.627: o foro subsiste após o afastamento do cargo para crimes funcionais."),
    ("E", "O Presidente da República pode editar medida provisória para tipificar novo crime, desde que demonstradas a relevância e a urgência.",
     "É vedada medida provisória sobre direito penal (art. 62, § 1º, I, b)."),
    ("C", "A medida provisória tem vigência de sessenta dias, prorrogável uma vez por igual período, e esse prazo fica suspenso durante o recesso parlamentar.",
     "Art. 62, §§ 3º, 4º e 7º."),
    ("E", "O Presidente da República pode vetar parcialmente um projeto de lei, suprimindo apenas uma palavra de um artigo cujo sentido considere contrário ao interesse público.",
     "O veto parcial deve abranger texto integral de artigo, parágrafo, inciso ou alínea."),
    ("C", "Decorrido o prazo de quinze dias úteis sem manifestação do Presidente da República, o silêncio importará sanção.",
     "Art. 66, § 3º."),
    ("E", "Perde o mandato o deputado que faltar a um quinto das sessões ordinárias da Casa, cabendo ao plenário decidir por maioria absoluta.",
     "A causa é faltar a um terço das sessões ordinárias, e a perda é declarada pela Mesa."),
], 20)

SOURCES = [
    "Constituição da República Federativa do Brasil de 1988, arts. 27, 29, 44 a 75.",
    "Supremo Tribunal Federal: AP 937 (QO); HC 232.627 (foro após o fim do mandato); jurisprudência sobre os limites das CPIs.",
    "Doutrina de referência: Lenza, Direito constitucional; Mendes e Branco, Curso de direito constitucional.",
    SRC_A,
]
