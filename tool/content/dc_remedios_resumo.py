# -*- coding: utf-8 -*-
"""Direito Constitucional · Remédios constitucionais — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "dc-remedios-01", "DC", "DC-03", "resumo", "Remédios constitucionais", "Direito Constitucional · Direitos fundamentais",
    "constitucional_remedios", "Constitucional_Remedios_RESUMO.pdf", None, ["Remédios", "constitucionais"], RES_SUB,
    RES_ITEMS("HC, MS, MI, HD e ação popular"),
    "Tópico do edital: Remédios constitucionais (art. 5º, LXVIII a LXXIII) — Direito Constitucional",
    "Base: Constituição Federal de 1988 e súmulas do STF.", 35)

THEORY = [
    exam("O que a banca cobra",
         "Qual remédio cabe no caso concreto, **quem pode propor**, a **gratuidade** e as súmulas do STF."),
    h2("1. Habeas corpus"),
    bl("Protege **só a liberdade de locomoção**, contra ilegalidade ou abuso de poder.",
       "**Preventivo** (salvo-conduto) ou **repressivo** (alvará de soltura).",
       "**Qualquer pessoa** impetra, **sem advogado**; cabe contra **particular**; juiz concede **de ofício**; **gratuito**.",
       "Não cabe: pena só de **multa** (693), exclusão de militar ou perda de patente (694), pena **já extinta** (695).",
       "Punição disciplinar militar: cabe só para a **legalidade**, não para o mérito."),
    h2("2. Mandado de segurança"),
    bl("Direito **líquido e certo** (prova documental pré-constituída), **não amparado por HC ou HD**.",
       "Contra **autoridade** ou agente de PJ no exercício de função pública. Prazo de **120 dias** da ciência do ato.",
       "Não cabe contra **lei em tese** (266) nem decisão **transitada em julgado** (268).",
       "**Coletivo**: partido **com representação no Congresso**; sindicato, entidade de classe ou associação (**1 ano**, exigido só da associação).",
       "Entidade impetra **sem autorização** dos associados (629), mesmo que só parte da categoria se beneficie (630)."),
    h2("3. Mandado de injunção"),
    bl("**Falta de norma regulamentadora** que inviabiliza direitos ou prerrogativas de **nacionalidade, soberania e cidadania**.",
       "Lei 13.300/2016: efeito **inter partes** em regra; pode ser **ultra partes** ou **erga omnes**.",
       "STF **concretista**: greve dos servidores com a lei do setor privado."),
    h2("4. Habeas data e ação popular"),
    bl("**HD**: conhecer ou **retificar dados da própria pessoa** em bancos governamentais ou de caráter público; exige **recusa prévia**; **gratuito**.",
       "**Ação popular**: só **cidadão** (eleitor); anula ato lesivo ao **patrimônio público**, **moralidade**, **meio ambiente**, patrimônio "
       "**histórico e cultural**; isento de custas **salvo má-fé**; **PJ não propõe** (365)."),
]

SUMMARY = [
    h2("Quadro rápido"),
    tb(["Remédio", "Para quê", "Quem"], [0.22, 0.46, 0.32], [
        ("HC", "Liberdade de locomoção", "Qualquer pessoa, sem advogado"),
        ("MS", "Direito líquido e certo residual", "Titular, com advogado"),
        ("MS coletivo", "Interesses de membros ou associados", "Partido com representação; sindicato; associação com 1 ano"),
        ("MI", "Falta de norma regulamentadora", "Titular; coletivo: MP, partido, sindicato, Defensoria"),
        ("HD", "Dados da própria pessoa", "O titular dos dados"),
        ("Ação popular", "Patrimônio público e moralidade", "Cidadão (eleitor)"),
    ]),
    h2("Leve para a prova"),
    bl("HC: só **ir e vir**.",
       "HC e HD são **gratuitos**.",
       "MS é **residual** e tem prazo de **120 dias**.",
       "MS não ataca **lei em tese**.",
       "Partido no MS coletivo: **representação no Congresso**.",
       "Associação: **1 ano** de funcionamento.",
       "MI: falta **norma regulamentadora**.",
       "HD: dados **meus**, com **recusa prévia**.",
       "Ação popular: só **cidadão**; PJ **não**.",
       "Moralidade basta: não precisa de **dano financeiro**."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "REMÉDIOS", "rootSub": "art. 5º, LXVIII a LXXIII",
    "left": [
        {"label": "Habeas corpus", "items": ["liberdade de locomoção", "qualquer pessoa", "gratuito"]},
        {"label": "HC: tipos", "items": ["preventivo: salvo-conduto", "repressivo: soltura", "de ofício pelo juiz"]},
        {"label": "HC: não cabe", "items": ["só multa (693)", "perda de patente (694)", "pena extinta (695)"]},
        {"label": "Mandado de segurança", "items": ["líquido e certo", "residual", "120 dias"]},
        {"label": "MS coletivo", "items": ["partido no Congresso", "associação: 1 ano", "sem autorização (629)"]},
    ],
    "right": [
        {"label": "Mandado de injunção", "items": ["falta de norma", "concretista", "greve dos servidores"]},
        {"label": "Habeas data", "items": ["dados da própria pessoa", "conhecer e retificar", "recusa prévia"]},
        {"label": "Ação popular", "items": ["só cidadão", "patrimônio e moralidade", "isento salvo má-fé"]},
        {"label": "Não propõem AP", "items": ["pessoa jurídica (365)", "Ministério Público", "estrangeiro"]},
        {"label": "Petição e certidão", "items": ["sem taxas", "sem advogado", "certidão negada: MS"]},
    ],
}

QUIZ = quiz([
    ("C", "O habeas corpus é cabível contra ato de particular que restrinja a liberdade de locomoção de alguém.",
     "A Constituição não restringe o HC a atos de autoridade."),
    ("E", "O habeas corpus somente pode ser impetrado por advogado regularmente inscrito na OAB.",
     "Qualquer pessoa pode impetrar habeas corpus."),
    ("C", "O mandado de segurança tem caráter residual, sendo cabível quando o direito líquido e certo não for amparado por habeas corpus ou habeas data.",
     "É a letra do art. 5º, LXIX."),
    ("E", "Partido político, independentemente de representação no Congresso Nacional, tem legitimidade para impetrar mandado de segurança coletivo.",
     "Exige-se representação no Congresso Nacional."),
    ("C", "Não cabe mandado de segurança contra lei em tese.",
     "Súmula 266 do STF."),
    ("E", "O mandado de injunção é cabível para suprir a omissão de ato administrativo concreto que deixou de conceder um benefício ao impetrante.",
     "O MI pressupõe falta de norma regulamentadora; contra ato administrativo concreto, cabe mandado de segurança."),
    ("C", "O habeas data permite ao impetrante obter a retificação de dados a seu respeito constantes de registros de entidades governamentais.",
     "É a alínea b do art. 5º, LXXII."),
    ("E", "O habeas data pode ser impetrado diretamente em juízo, sendo dispensável qualquer requerimento administrativo prévio.",
     "Sem a recusa ou a demora administrativa, falta interesse de agir (Súmula 2 do STJ)."),
    ("C", "A ação popular pode ser proposta para anular ato lesivo ao meio ambiente.",
     "O meio ambiente está entre os bens protegidos pelo art. 5º, LXXIII."),
    ("E", "Não cabe habeas corpus contra decisão condenatória à pena privativa de liberdade ainda não executada.",
     "A Súmula 693 afasta o HC na condenação apenas a pena de multa; havendo pena privativa de liberdade, cabe HC."),
], 10)

SOURCES = [
    "Constituição da República Federativa do Brasil de 1988, art. 5º, LXVIII a LXXVII.",
    "Súmulas do STF 266, 268, 365, 629, 630, 693, 694 e 695; Súmula 2 do STJ.",
    SRC_R,
]
