# -- coding: utf-8 --
"""Contabilidade · Conceitos, objeto e finalidade — RESUMO (revisão)."""
from common import *

MATERIAL = {
    "id": "cont-conceitos-01",
    "version": "0.1.0",
    "status": "Em revisão pelo autor",
    "subjectId": "CONT",
    "topicIds": ["CONT-01"],
    "kind": "resumo",
    "title": "Contabilidade: conceito, objeto e finalidade",
    "subtitle": "Contabilidade Geral · Fundamentos",
    "minutes": 40,
    "folder": "contabilidade_conceitos",
    "pdf": "contabilidade_conceitos.pdf",
    "outName": "Contabilidade_Conceitos_RESUMO.pdf",
    "header": "Contabilidade · Conceito, objeto e finalidade",
    "coverKicker": "Contabilidade Geral  ·  Fundamentos",
    "coverTitle": ["Contabilidade:", "conceito, objeto e finalidade"],
    "coverSub": ["Resumo direto ao ponto, quadro comparativo, mapa mental", "e 10 questões no estilo Cebraspe com gabarito comentado."],
    "coverItems": [("01", "Teoria", "conceito, objeto, finalidade, funções, usuários e técnicas"),
                   ("02", "Resumo", "quadro “o quê × para quê” e “leve para a prova”"),
                   ("03", "Mapa mental", "uma página para revisar em 5 minutos"),
                   ("04", "Questões", "10 itens certo/errado + gabarito comentado")],
    "coverTopic": "Tópico do edital: Conceitos, objeto e finalidade (Contabilidade Geral)",
    "coverBase": "Base: CPC 00 (R2), Lei nº 6.404/1976 e doutrina.",
}

THEORY = [
    exam("O que a banca cobra",
         "Trocas de conceito: **objeto × objetivo**; contabilidade como **ciência exata**; campo restrito a **empresas**; função "
         "**administrativa × econômica**; e, do CPC 00, **usuários primários** e características **fundamentais × de melhoria**."),

    h2("1. Conceito, objeto e finalidade"),
    tb(["Pergunta", "Resposta"], [0.28, 0.72], [
        ("O que é?", "**Ciência social aplicada** que estuda, registra, controla e interpreta os fatos que afetam o patrimônio. Não é ciência exata."),
        ("O que estuda? (objeto)", "O **patrimônio**: conjunto de **bens, direitos e obrigações** de uma entidade."),
        ("Para que serve? (finalidade)", "**Fornecer informações úteis** para a tomada de decisão, servindo ao **controle** e ao **planejamento**."),
        ("Onde se aplica? (campo)", "Nas **aziendas**: qualquer entidade com patrimônio — física ou jurídica, pública ou privada, **com ou sem fins lucrativos**."),
    ]),
    nt("Definição clássica (1º Congresso Brasileiro de Contabilidade, 1924): ciência que estuda e pratica as funções de orientação, de controle e de registro relativas à administração econômica."),

    h2("2. Patrimônio em uma linha"),
    p("**Bens + direitos = ativo**. **Obrigações = passivo exigível**. A diferença é o **patrimônio líquido**. "
      "Aspecto **qualitativo** = natureza dos elementos; aspecto **quantitativo** = valor em moeda."),

    h2("3. Funções"),
    bl("**Administrativa**: controlar o patrimônio.",
       "**Econômica**: apurar o resultado (lucro ou prejuízo), também chamado de rédito."),

    h2("4. Usuários"),
    tb(["Grupo", "Quem são"], [0.3, 0.7], [
        ("Internos", "Administradores, gerentes, sócios que gerem o negócio, empregados."),
        ("Externos", "Investidores, bancos, fornecedores, clientes, governo, sindicatos."),
        ("Primários (CPC 00)", "**Investidores, credores por empréstimos e outros credores, existentes e potenciais.** A administração e os órgãos reguladores **não** são usuários primários."),
    ]),

    h2("5. Técnicas contábeis"),
    tb(["Técnica", "Verbo", "Produto"], [0.36, 0.24, 0.4], [
        ("Escrituração", "Registrar", "Livros Diário e Razão"),
        ("Demonstrações contábeis", "Resumir", "Balanço, DRE e demais demonstrações"),
        ("Auditoria", "Conferir", "Relatório do auditor"),
        ("Análise das demonstrações", "Interpretar", "Índices"),
    ]),
    nt("Lei nº 6.404/1976, art. 176: BP, DRE, DLPA e DFC; a DVA só é obrigatória para companhias abertas. Exercício social: um ano."),

    h2("6. Três ideias de base"),
    bl("**Entidade**: o patrimônio da empresa não se mistura com o dos sócios.",
       "**Continuidade**: presume-se que a entidade seguirá operando (premissa subjacente no CPC 00).",
       "**Competência**: receitas e despesas no período do **fato gerador**, independentemente de recebimento ou pagamento. O contrário é o **regime de caixa**."),

    h2("7. Características qualitativas (CPC 00 R2)"),
    tb(["Grupo", "Características"], [0.26, 0.74], [
        ("Fundamentais", "**Relevância** (faz diferença na decisão; valor preditivo e confirmatório; materialidade) e **representação fidedigna** (completa, neutra e isenta de erros)."),
        ("De melhoria", "**Comparabilidade, capacidade de verificação, tempestividade e compreensibilidade.**"),
    ]),
    trap("Pegadinha",
         "Só **duas** são fundamentais. Tempestividade e comparabilidade são **de melhoria**. "
         "E **comparabilidade não é uniformidade**."),
]

SUMMARY = [
    h2("Quadro: o quê × para quê"),
    tb(["Conceito", "Resposta curta", "Erro clássico da banca"], [0.24, 0.36, 0.4], [
        ("Natureza", "Ciência social aplicada", "“Ciência exata”"),
        ("Objeto", "Patrimônio", "“Fornecer informações”"),
        ("Finalidade", "Informação útil para decidir", "“Apurar tributos” ou “o patrimônio”"),
        ("Campo de aplicação", "Qualquer entidade com patrimônio", "“Apenas entidades com fins lucrativos”"),
        ("Função administrativa", "Controlar o patrimônio", "Trocar com a econômica"),
        ("Função econômica", "Apurar o resultado", "Trocar com a administrativa"),
        ("Usuários primários", "Investidores e credores", "Incluir a administração ou o governo"),
        ("Regime adotado", "Competência", "“Receita só quando recebe”"),
    ]),
    h2("Leve para a prova"),
    bl("**Objeto = patrimônio. Objetivo = informação.**",
       "Ciência **social**, nunca exata.",
       "Vale para entidades **sem fins lucrativos** e para o **setor público**.",
       "Administrativa = **controle**; econômica = **resultado**.",
       "Técnicas: **registrar, resumir, conferir, interpretar**.",
       "Fundamentais: **relevância** e **representação fidedigna**. O resto é de melhoria.",
       "Fidedigna = **completa, neutra e isenta de erros**.",
       "**Entidade**: despesa do sócio não é despesa da empresa.",
       "**Competência**: fato gerador, não dinheiro.",
       "**DVA**: só companhia aberta."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "CONTABILIDADE",
    "rootSub": "ciência social aplicada",
    "left": [
        {"label": "Objeto", "items": ["Patrimônio da entidade", "Bens + direitos − obrigações", "Qualitativo e quantitativo"]},
        {"label": "Finalidade", "items": ["Informação útil para decidir", "Controle e planejamento", "Não é apurar imposto"]},
        {"label": "Funções", "items": ["Administrativa: controle", "Econômica: resultado (rédito)"]},
        {"label": "Campo de aplicação", "items": ["Aziendas: quem tem patrimônio", "Com ou sem fins lucrativos", "Pública ou privada"]},
        {"label": "Técnicas", "items": ["Escrituração: registrar", "Demonstrações: resumir", "Auditoria e análise"]},
    ],
    "right": [
        {"label": "Usuários", "items": ["Internos e externos", "Primários: investidores e credores", "Administração não é primária"]},
        {"label": "Ideias de base", "items": ["Entidade: sócio ≠ empresa", "Continuidade: seguirá operando", "Competência: fato gerador"]},
        {"label": "Fundamentais (CPC 00)", "items": ["Relevância", "Representação fidedigna", "Completa, neutra, sem erros"]},
        {"label": "De melhoria (CPC 00)", "items": ["Comparabilidade", "Capacidade de verificação", "Tempestividade e compreensibilidade"]},
        {"label": "Lei 6.404/1976", "items": ["BP, DRE, DLPA e DFC", "DVA: só companhia aberta", "Exercício social: 1 ano"]},
    ],
}

QUIZ = quiz([
    ("E", "A finalidade da contabilidade é o patrimônio, entendido como o conjunto de bens, direitos e obrigações.",
     "O patrimônio é o objeto. A finalidade é fornecer informações úteis para a tomada de decisão."),
    ("C", "A contabilidade aplica-se tanto a entidades com fins lucrativos quanto a entidades sem fins lucrativos, bem como a pessoas físicas.",
     "O campo de aplicação alcança qualquer entidade que possua patrimônio."),
    ("C", "Apurar o lucro ou o prejuízo de determinado período corresponde à função econômica da contabilidade.",
     "A função administrativa é controlar o patrimônio; a econômica, apurar o resultado."),
    ("E", "Os bens e os direitos de uma entidade compõem o seu passivo exigível.",
     "Bens e direitos compõem o ativo. O passivo exigível é formado pelas obrigações."),
    ("C", "A análise das demonstrações contábeis é a técnica que permite interpretar a situação da entidade por meio da decomposição e da comparação dos dados das demonstrações.",
     "É a técnica da interpretação, também chamada de análise de balanços."),
    ("E", "Conforme a Estrutura Conceitual, os órgãos reguladores e o governo são os usuários primários dos relatórios financeiros para fins gerais.",
     "Os usuários primários são investidores, credores por empréstimos e outros credores, existentes e potenciais."),
    ("C", "A compreensibilidade e a capacidade de verificação são características qualitativas de melhoria da informação contábil.",
     "As de melhoria são comparabilidade, capacidade de verificação, tempestividade e compreensibilidade."),
    ("E", "A informação contábil é considerada neutra quando é capaz de fazer diferença nas decisões dos usuários.",
     "Fazer diferença nas decisões é relevância. Neutralidade é ausência de viés, um dos atributos da representação fidedigna."),
    ("E", "Uma venda a prazo efetuada em dezembro, com recebimento em janeiro, deve ser reconhecida como receita de janeiro, conforme o regime de competência.",
     "Pela competência, a receita pertence ao período do fato gerador: dezembro. O reconhecimento em janeiro seguiria o regime de caixa."),
    ("C", "De acordo com a ideia de entidade, o patrimônio da pessoa jurídica não se confunde com o patrimônio de seus sócios.",
     "É a autonomia patrimonial."),
], 10)

SOURCES = [
    "CPC 00 (R2) — Estrutura Conceitual para Relatório Financeiro; Lei nº 6.404/1976, arts. 175 a 177.",
    "Texto e questões elaborados para o Mentor Policial (itens inéditos no estilo Cebraspe).",
]
