# -*- coding: utf-8 -*-
"""Língua Portuguesa · Semântica e significação das palavras — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "lp-semantica-01", "LP", "LP-19", "resumo", "Semântica e significação das palavras", "Língua Portuguesa · Semântica",
    "portugues_semantica", "Portugues_Semantica_RESUMO.pdf", None, ["Significação", "das palavras"], RES_SUB,
    RES_ITEMS("relações de sentido, parônimos e sentido figurado"),
    "Tópico do edital: Significação das palavras (Língua Portuguesa)",
    "Base: gramáticas de referência e Vocabulário Ortográfico da Língua Portuguesa (ABL).", 25)

THEORY = [
    exam("O que a banca cobra",
         "**Substituição** de palavras (sinonímia no contexto), **parônimos** e **sentido figurado**."),
    h2("1. Relações"),
    bl("**Sinônimos** (no contexto), **antônimos**, **hiperônimo** (geral: *arma*) × **hipônimo** (específico: *fuzil*).",
       "**Homófonos**: mesmo som (*cela/sela, sessão/seção/cessão*). **Homógrafos**: mesma grafia. **Parônimos**: parecidos.",
       "**Polissemia**: vários sentidos relacionados (*operação, banco*)."),
    h2("2. Parônimos da área policial"),
    tb(["Par", "Diferença"], [0.34, 0.66], [
        ("mandado / mandato", "ordem judicial / período de representação"),
        ("flagrante / fragrante", "evidente / perfumado"),
        ("infringir / infligir", "violar / aplicar pena"),
        ("ratificar / retificar", "confirmar / corrigir"),
        ("deferir / diferir", "atender / adiar"),
        ("eminente / iminente", "importante / prestes a ocorrer"),
        ("descrição / discrição", "descrever / reserva"),
        ("tráfego / tráfico", "trânsito / comércio ilegal"),
        ("vultoso / vultuoso", "grande valor / inchado"),
        ("emergir / imergir", "vir à tona / mergulhar"),
    ]),
    h2("3. Sentido"),
    bl("**Denotação**: literal. **Conotação**: figurado (*coração de pedra*).",
       "**Ambiguidade**: duplo sentido (*viu o assaltante correndo*)."),
]

SUMMARY = [
    h2("Leve para a prova"),
    bl("Sinonímia é **contextual**.",
       "Mandado = ordem; mandato = representação.",
       "Infringir a lei; infligir pena.",
       "Ratificar confirma; retificar corrige.",
       "Deferir atende; diferir adia.",
       "Iminente = vai acontecer.",
       "Discrição = reserva.",
       "Quantia vultosa (sem u).",
       "Hiperônimo retoma hipônimo.",
       "Ambiguidade: termo com dois referentes."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "SEMÂNTICA", "rootSub": "significação das palavras",
    "left": [
        {"label": "Sinonímia", "items": ["sentido semelhante", "depende do contexto", "fugiu = evadiu-se"]},
        {"label": "Hiperonímia", "items": ["arma: geral", "fuzil: específico", "retomada coesiva"]},
        {"label": "Homônimos", "items": ["cela / sela", "sessão / seção / cessão", "censo / senso"]},
        {"label": "Polissemia", "items": ["operação", "banco", "sentidos relacionados"]},
        {"label": "Sentido", "items": ["denotação: literal", "conotação: figurado", "ambiguidade"]},
    ],
    "right": [
        {"label": "Mandado", "items": ["mandado: ordem judicial", "mandato: representação", "cumprimento do mandado"]},
        {"label": "Infringir", "items": ["infringir: violar", "infligir: aplicar pena", "flagrante ≠ fragrante"]},
        {"label": "Ratificar", "items": ["ratificar: confirmar", "retificar: corrigir", "deferir ≠ diferir"]},
        {"label": "Iminente", "items": ["iminente: vai ocorrer", "eminente: importante", "emergir ≠ imergir"]},
        {"label": "Outros", "items": ["tráfego ≠ tráfico", "discrição: reserva", "vultoso: grande valor"]},
    ],
}

QUIZ = quiz([
    ("C", "Em “O deputado cumpre o segundo mandato”, o vocábulo mandato refere-se a período de representação.",
     "Mandado seria ordem judicial."),
    ("E", "Em “O juiz infligiu as regras do processo”, o verbo infligir foi empregado no sentido de violar.",
     "Violar é infringir; infligir é aplicar pena."),
    ("C", "Em “O tribunal ratificou a decisão de primeira instância”, ratificar significa confirmar.",
     "Retificar seria corrigir."),
    ("E", "Em “O ataque era eminente, e a população foi evacuada”, o adjetivo eminente está adequadamente empregado.",
     "Prestes a ocorrer é iminente."),
    ("C", "Em “A perícia exige discrição dos servidores”, discrição significa reserva.",
     "Descrição é o ato de descrever."),
    ("E", "Os vocábulos tráfego e tráfico são sinônimos.",
     "Tráfego é trânsito; tráfico é comércio ilegal."),
    ("C", "O vocábulo veículo é hiperônimo de viatura.",
     "Veículo é o termo geral; viatura é um tipo de veículo."),
    ("E", "Em “O réu tem nervos de aço”, a expressão foi empregada em sentido denotativo.",
     "O sentido é figurado: o réu é calmo, resistente."),
    ("C", "Em “O agente encontrou o colega na sua sala”, há ambiguidade.",
     "Não se sabe se a sala é do agente ou do colega."),
    ("E", "Os vocábulos cela e sela são parônimos.",
     "Têm a mesma pronúncia: são homófonos."),
], 10)

SOURCES = [GRAM, SRC_R]
