# -*- coding: utf-8 -*-
"""Língua Portuguesa · Redação oficial — MATERIAL APROFUNDADO (estudo inicial)."""
from common import *

MATERIAL = material(
    "lp-redacao-oficial-02", "LP", "LP-20", "aprofundado", "Redação oficial", "Língua Portuguesa · Redação oficial",
    "portugues_redacao_oficial_aprofundado", "Portugues_Redacao_Oficial_APROFUNDADO.pdf", None, ["Redação", "oficial"],
    ["Segundo o Manual de Redação da Presidência (3ª edição): atributos,", "tratamento, vocativos, fechos e padrão ofício, com 20 questões no estilo Cebraspe."],
    [("01", "Atributos", "clareza, precisão, concisão, impessoalidade, formalidade"),
     ("02", "Tratamento", "Vossa Excelência, Vossa Senhoria e concordância"),
     ("03", "Vocativos e fechos", "Excelentíssimo, Senhor, Respeitosamente, Atenciosamente"),
     ("04", "Padrão ofício", "as partes do documento"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Redação oficial — Manual de Redação da Presidência da República",
    "Base: Manual de Redação da Presidência da República, 3ª edição (2018).", 150)

THEORY = [
    exam("Como estudar este material",
         "As questões de redação oficial são quase sempre sobre **pronomes de tratamento**, **vocativos**, **fechos** e **atributos** do texto oficial. "
         "Tudo vem do *Manual de Redação da Presidência da República* (3ª edição, 2018), que unificou os antigos aviso, memorando e ofício "
         "no **padrão ofício**. Este material resume o que cai; consulte o manual para os detalhes de formatação."),

    h2("1. Atributos da redação oficial"),
    tb(["Atributo", "O que significa"], [0.26, 0.74], [
        ("Clareza", "O texto é entendido de imediato pelo leitor"),
        ("Precisão", "Palavras exatas, sem ambiguidade; termo técnico só quando necessário e, se preciso, explicado"),
        ("Objetividade", "Ir direto ao assunto, com as ideias essenciais"),
        ("Concisão", "Transmitir o máximo de informação com o mínimo de palavras, **sem eliminar o essencial**"),
        ("Coesão e coerência", "Ideias bem ligadas e logicamente compatíveis"),
        ("Impessoalidade", "O texto é do órgão, não da pessoa: sem impressões pessoais"),
        ("Formalidade e padronização", "Civilidade no tratamento e uniformidade dos documentos"),
        ("Uso da norma-padrão", "Sem gírias, regionalismos ou linguagem coloquial"),
    ]),
    trap("Concisão não é cortar o essencial",
         "Concisão é eliminar o que sobra (repetições, adjetivos inúteis, rodeios), nunca a informação necessária. "
         "E impessoalidade não proíbe a 1ª pessoa do plural institucional: proíbe a opinião pessoal do redator."),

    h2("2. Pronomes de tratamento"),
    bl("Levam o verbo e os possessivos para a **3ª pessoa**: *Vossa Excelência **deve** apresentar **seu** parecer* (e não *deveis, vosso*).",
       "**Vossa** para falar **com** a autoridade; **Sua** para falar **sobre** ela: *Vossa Excelência decidiu?* × *Sua Excelência, o Ministro, decidiu.*",
       "A concordância de gênero dos adjetivos se faz com o **sexo da pessoa**: *Vossa Excelência está **atarefado/atarefada***."),
    tb(["Forma", "Para quem (exemplos)"], [0.24, 0.76], [
        ("Vossa Excelência", "Presidente e Vice-Presidente da República, Ministros, Governadores, Prefeitos, parlamentares, Oficiais-Generais, "
                             "magistrados (juízes, desembargadores, ministros de tribunais), membros do Ministério Público, Defensores"),
        ("Vossa Senhoria", "Demais autoridades e particulares"),
        ("Vossa Magnificência", "Reitores de universidade"),
        ("Vossa Santidade", "Papa"),
    ]),
    nt("O manual aboliu *digníssimo* (DD) e *ilustríssimo* (Ilmo.). *Doutor* não é forma de tratamento, e sim título acadêmico: "
       "use-o apenas para quem concluiu doutorado."),

    h2("3. Vocativos e fechos"),
    tb(["Elemento", "Regra", "Exemplo"], [0.18, 0.42, 0.4], [
        ("Vocativo", "**Excelentíssimo Senhor** + cargo: só para **chefes de Poder**", "Excelentíssimo Senhor Presidente da República, · Excelentíssimo Senhor Presidente do Supremo Tribunal Federal,"),
        ("Vocativo", "**Senhor** + cargo: demais autoridades", "Senhor Ministro, · Senhora Delegada, · Senhor Juiz,"),
        ("Fecho", "**Respeitosamente**: autoridades de hierarquia **superior**", "Ofício a ministro, enviado por diretor"),
        ("Fecho", "**Atenciosamente**: autoridades de **mesma** hierarquia ou **inferior**", "Ofício entre diretores"),
    ]),

    h2("4. Padrão ofício"),
    p("Na 3ª edição, os antigos **aviso** e **memorando** passaram a ser chamados de **ofício**: um só nome para a comunicação oficial "
      "entre órgãos e autoridades. Partes principais:"),
    tb(["Parte", "Como é"], [0.24, 0.76], [
        ("Identificação", "Tipo e número do documento, com a sigla do órgão: *OFÍCIO Nº 123/2026/DPF/SR/PE*"),
        ("Local e data", "Por extenso, à direita: *Recife, 17 de novembro de 2026.*"),
        ("Endereçamento", "Tratamento, nome, cargo e endereço do destinatário: *A Sua Senhoria o Senhor / [Nome] / [Cargo] / [Endereço]*"),
        ("Assunto", "Resumo do tema, em destaque: *Assunto: Solicitação de cópia de laudo.*"),
        ("Vocativo", "*Senhor Superintendente,*"),
        ("Texto", "Introdução (o assunto), desenvolvimento (detalhamento) e conclusão (o que se pede ou se informa)"),
        ("Fecho", "*Respeitosamente,* ou *Atenciosamente,*"),
        ("Assinatura", "Nome e cargo do signatário"),
    ]),
    nt("O manual também padroniza fonte, margens, numeração de páginas e uso de anexos. Em prova, os itens mais cobrados são os desta página: "
       "tratamento, vocativo, fecho, data por extenso e partes do documento."),

    h2("5. Como o Cebraspe cobra"),
    bl("Correção de pronome de tratamento e concordância na 3ª pessoa.",
       "Vocativo adequado ao destinatário (Excelentíssimo só para chefes de Poder).",
       "Fecho adequado à hierarquia.",
       "Atributos: “o trecho fere a impessoalidade / a concisão”.",
       "Trechos de ofício com linguagem coloquial, opinião pessoal ou expressões abolidas."),
]

QUIZ = quiz([
    ("C", "Clareza, precisão, objetividade, concisão, impessoalidade, formalidade e uso da norma-padrão são atributos da redação oficial.",
     "São os atributos listados no Manual de Redação da Presidência da República."),
    ("E", "A impessoalidade permite que o redator de um ofício expresse suas impressões pessoais sobre o assunto.",
     "O texto oficial é do órgão: impressões pessoais ferem a impessoalidade."),
    ("C", "Segundo a 3ª edição do Manual de Redação da Presidência da República, aviso e memorando passaram a ser denominados ofício.",
     "Houve a unificação no padrão ofício."),
    ("E", "A forma Vossa Excelência deve ser empregada quando se fala sobre a autoridade, e não com ela.",
     "Para falar sobre a autoridade usa-se Sua Excelência; Vossa é para falar com ela."),
    ("C", "Os pronomes de tratamento exigem verbo e possessivos na terceira pessoa.",
     "Vossa Excelência deve apresentar seu parecer."),
    ("E", "O fecho Respeitosamente é empregado em comunicações para autoridades de mesma hierarquia ou de hierarquia inferior.",
     "Respeitosamente é para hierarquia superior; Atenciosamente, para mesma ou inferior."),
    ("C", "O vocativo Excelentíssimo Senhor é reservado aos chefes de Poder.",
     "Ex.: Excelentíssimo Senhor Presidente da República."),
    ("E", "As formas Digníssimo e Ilustríssimo devem ser empregadas no endereçamento de ofícios a altas autoridades.",
     "O manual aboliu essas formas."),
    ("C", "Doutor não é forma de tratamento, e sim título acadêmico.",
     "O manual recomenda usá-lo apenas para quem tem doutorado."),
    ("E", "A concisão autoriza suprimir informações essenciais para que o texto fique mais curto.",
     "Concisão elimina excessos, não o essencial."),

    ("C", "Em ofício dirigido a um Ministro de Estado, o vocativo adequado é Senhor Ministro.",
     "Excelentíssimo fica restrito aos chefes de Poder."),
    ("E", "Em ofício dirigido ao Presidente da República, o vocativo adequado é Senhor Presidente.",
     "Para chefe de Poder: Excelentíssimo Senhor Presidente da República."),
    ("C", "O emprego de termos técnicos deve ser evitado na redação oficial ou, quando indispensável, acompanhado de explicação.",
     "Atende aos atributos de clareza e precisão."),
    ("E", "A redação oficial admite linguagem coloquial e gírias quando o destinatário é colega de trabalho.",
     "A redação oficial exige a norma-padrão em qualquer caso."),
    ("C", "A precisão refere-se à escolha de palavras exatas, que evitem ambiguidade.",
     "É um dos atributos do texto oficial."),
    ("E", "Com o pronome Vossa Senhoria, o verbo deve ser empregado na segunda pessoa do plural.",
     "Pronomes de tratamento pedem verbo na 3ª pessoa: Vossa Senhoria deve…"),
    ("C", "Em correspondência dirigida a um juiz de direito, a forma de tratamento adequada é Vossa Excelência.",
     "Magistrados recebem Vossa Excelência."),
    ("E", "O fecho Atenciosamente é o adequado para comunicações dirigidas a autoridades de hierarquia superior.",
     "Para hierarquia superior, usa-se Respeitosamente."),
    ("C", "Formalidade e padronização relacionam-se à civilidade no tratamento e à uniformidade dos documentos oficiais.",
     "Os documentos seguem padrões comuns de forma e linguagem."),
    ("E", "No padrão ofício, a data deve ser escrita de forma abreviada, apenas com algarismos.",
     "Local e data vêm por extenso: Recife, 17 de novembro de 2026."),
], 20)

SOURCES = ["Presidência da República, Manual de Redação da Presidência da República, 3ª edição (2018).", SRC_A]
