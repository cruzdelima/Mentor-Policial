# -*- coding: utf-8 -*-
"""Língua Portuguesa · Redação oficial — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "lp-redacao-oficial-01", "LP", "LP-20", "resumo", "Redação oficial", "Língua Portuguesa · Redação oficial",
    "portugues_redacao_oficial", "Portugues_Redacao_Oficial_RESUMO.pdf", None, ["Redação", "oficial"], RES_SUB,
    RES_ITEMS("atributos, tratamento, vocativos, fechos e padrão ofício"),
    "Tópico do edital: Redação oficial — Manual de Redação da Presidência da República",
    "Base: Manual de Redação da Presidência da República, 3ª edição (2018).", 30)

THEORY = [
    exam("O que a banca cobra",
         "**Tratamento** (e a concordância na 3ª pessoa), **vocativo**, **fecho** e **atributos** do texto oficial."),
    h2("1. Atributos"),
    bl("Clareza, precisão, objetividade, **concisão** (sem cortar o essencial), coesão, **impessoalidade** (sem opinião pessoal), "
       "formalidade e padronização, norma-padrão."),
    h2("2. Tratamento"),
    bl("Verbo e possessivo na **3ª pessoa**: *Vossa Excelência deve… seu parecer*.",
       "**Vossa** = falando com; **Sua** = falando sobre.",
       "**Vossa Excelência**: altas autoridades dos três Poderes, magistrados, MP, oficiais-generais. **Vossa Senhoria**: demais.",
       "Abolidos: *digníssimo, ilustríssimo*. *Doutor* é título acadêmico."),
    h2("3. Vocativo e fecho"),
    bl("**Excelentíssimo Senhor**: só chefes de Poder. Demais: **Senhor + cargo**.",
       "**Respeitosamente**: superior. **Atenciosamente**: mesma hierarquia ou inferior."),
    h2("4. Padrão ofício"),
    bl("Aviso e memorando agora são **ofício** (3ª edição).",
       "Partes: identificação (tipo, número, sigla), local e data **por extenso**, endereçamento, assunto, vocativo, texto, fecho, assinatura."),
]

SUMMARY = [
    h2("Quadro rápido"),
    tb(["Destinatário", "Tratamento", "Vocativo", "Fecho (de subordinado)"], [0.28, 0.24, 0.3, 0.18], [
        ("Presidente da República", "Vossa Excelência", "Excelentíssimo Senhor Presidente da República,", "Respeitosamente"),
        ("Ministro de Estado", "Vossa Excelência", "Senhor Ministro,", "Respeitosamente"),
        ("Juiz de direito", "Vossa Excelência", "Senhor Juiz,", "Respeitosamente"),
        ("Diretor (mesmo nível)", "Vossa Senhoria", "Senhor Diretor,", "Atenciosamente"),
    ]),
    h2("Leve para a prova"),
    bl("Tratamento: verbo na **3ª pessoa**.",
       "Vossa = com; Sua = sobre.",
       "Excelentíssimo: **só** chefes de Poder.",
       "Respeitosamente: **superior**.",
       "Atenciosamente: mesma ou inferior.",
       "Sem digníssimo e ilustríssimo.",
       "Doutor não é tratamento.",
       "Concisão sem perder o essencial.",
       "Impessoalidade: sem opinião pessoal.",
       "Data por extenso."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "REDAÇÃO OFICIAL", "rootSub": "Manual da Presidência, 3ª ed.",
    "left": [
        {"label": "Atributos", "items": ["clareza e precisão", "concisão e objetividade", "impessoalidade"]},
        {"label": "Formalidade", "items": ["padronização", "norma-padrão", "sem gírias"]},
        {"label": "Tratamento", "items": ["3ª pessoa", "Vossa: com", "Sua: sobre"]},
        {"label": "Excelência", "items": ["chefes de Poder", "ministros, juízes", "MP e generais"]},
        {"label": "Abolidos", "items": ["digníssimo", "ilustríssimo", "doutor como tratamento"]},
    ],
    "right": [
        {"label": "Vocativo", "items": ["Excelentíssimo: chefes de Poder", "Senhor + cargo", "Senhora Delegada,"]},
        {"label": "Fecho", "items": ["Respeitosamente: superior", "Atenciosamente: igual", "ou inferior"]},
        {"label": "Padrão ofício", "items": ["aviso e memorando", "agora são ofício", "3ª edição"]},
        {"label": "Partes", "items": ["identificação e data", "endereçamento e assunto", "texto, fecho, assinatura"]},
        {"label": "Pegadinhas", "items": ["deveis, vosso: erro", "data abreviada: erro", "opinião pessoal: erro"]},
    ],
}

QUIZ = quiz([
    ("C", "Em comunicações oficiais, o pronome Vossa Excelência exige verbo na terceira pessoa.",
     "Vossa Excelência deve, e não deveis."),
    ("E", "Em ofício dirigido a um senador, o vocativo adequado é Excelentíssimo Senhor Senador.",
     "Excelentíssimo é reservado aos chefes de Poder; para senador, Senhor Senador."),
    ("C", "O fecho Respeitosamente é adequado em ofício enviado por um delegado a um ministro.",
     "É o fecho para autoridade de hierarquia superior."),
    ("E", "A forma Ilustríssimo Senhor continua recomendada pelo Manual de Redação da Presidência da República.",
     "O manual aboliu essa forma."),
    ("C", "A impessoalidade impede que o texto oficial expresse impressões pessoais de quem o redige.",
     "O texto oficial fala em nome do órgão."),
    ("E", "Para se referir a uma autoridade, sem se dirigir a ela, emprega-se Vossa Excelência.",
     "Ao falar sobre a autoridade, usa-se Sua Excelência."),
    ("C", "Na 3ª edição do Manual, aviso e memorando passaram a ser chamados de ofício.",
     "Os documentos foram unificados no padrão ofício."),
    ("E", "Concisão, na redação oficial, significa reduzir o texto mesmo que se percam informações essenciais.",
     "Concisão elimina excessos, mantendo o essencial."),
    ("C", "Juízes recebem o tratamento Vossa Excelência.",
     "Magistrados estão entre as autoridades tratadas por Vossa Excelência."),
    ("E", "O fecho Atenciosamente é o indicado para autoridades de hierarquia superior.",
     "Para hierarquia superior, usa-se Respeitosamente."),
], 10)

SOURCES = ["Presidência da República, Manual de Redação da Presidência da República, 3ª edição (2018).", SRC_R]
