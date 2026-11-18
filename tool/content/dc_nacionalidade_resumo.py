# -*- coding: utf-8 -*-
"""Direito Constitucional · Nacionalidade (arts. 12 e 13) — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "dc-nacionalidade-01", "DC", "DC-05", "resumo", "Nacionalidade (arts. 12 e 13)", "Direito Constitucional · Direitos fundamentais",
    "constitucional_nacionalidade", "Constitucional_Nacionalidade_RESUMO.pdf", None, ["Nacionalidade"], RES_SUB,
    RES_ITEMS("natos, naturalizados, cargos privativos e perda"),
    "Tópico do edital: Nacionalidade (arts. 12 e 13) — Direito Constitucional",
    "Base: Constituição Federal de 1988 (com a EC 131/2023).", 25)

THEORY = [
    exam("O que a banca cobra",
         "Hipóteses de **nato** e **naturalizado**, os **cargos privativos** e a **perda** após a **EC 131/2023**."),
    h2("1. Natos"),
    bl("**a)** Nascido **no Brasil**, salvo se os pais estrangeiros estiverem **a serviço do seu país**.",
       "**b)** Nascido no exterior, pai **ou** mãe brasileiros **a serviço do Brasil** (qualquer ente, direta ou indireta).",
       "**c)** Nascido no exterior, pai ou mãe brasileiros, **registrado em repartição brasileira** ou que venha **residir no Brasil** e **opte**, "
       "após a **maioridade**, em qualquer tempo (Justiça Federal, ato personalíssimo)."),
    h2("2. Naturalizados"),
    bl("**Ordinária**: na forma da lei; países de **língua portuguesa**: **1 ano** de residência + **idoneidade moral**. Ato discricionário.",
       "**Extraordinária**: **mais de 15 anos** de residência ininterrupta + **sem condenação penal** + requerimento. Direito subjetivo.",
       "**Português** residente, com **reciprocidade**: direitos de brasileiro, sem se naturalizar; nunca ocupa cargo de nato."),
    h2("3. Diferenças"),
    bl("Só a **Constituição** distingue nato e naturalizado.",
       "Cargos de nato: **MP3.COM** (Ministro do STF, Presidente e Vice, Presidentes da Câmara e do Senado, Carreira diplomática, Oficial das FA, "
       "Ministro da Defesa).",
       "Extradição: nato **nunca**; Conselho da República: **6 natos**; empresa jornalística: naturalizado **há mais de 10 anos**."),
    h2("4. Perda (EC 131/2023)"),
    bl("**Cancelamento da naturalização** por **sentença judicial**: **fraude** no processo ou **atentado** contra a ordem constitucional e o "
       "Estado Democrático.",
       "**Pedido expresso** à autoridade brasileira, **salvo se gerar apatridia**; quem renunciou pode **readquirir** a nacionalidade originária.",
       "Adquirir **outra nacionalidade** não faz mais perder a brasileira."),
    h2("5. Art. 13"),
    bl("Idioma oficial: **língua portuguesa**. Símbolos: **bandeira, hino, armas e selo**. Estados, DF e Municípios **podem** ter símbolos próprios."),
]

SUMMARY = [
    h2("Quadro rápido"),
    tb(["Situação", "Resultado"], [0.56, 0.44], [
        ("Nasceu no Brasil, pais estrangeiros turistas", "Nato"),
        ("Nasceu no Brasil, pais diplomatas a serviço do seu país", "Não é nato"),
        ("Nasceu no exterior, mãe a serviço do Brasil", "Nato"),
        ("Nasceu no exterior, registrado no consulado", "Nato"),
        ("Estrangeiro de língua portuguesa, 1 ano no Brasil", "Pode naturalizar-se"),
        ("Qualquer estrangeiro, mais de 15 anos, sem condenação", "Direito à naturalização"),
        ("Naturalizado quer ser senador", "Pode"),
        ("Naturalizado quer ser ministro do STF", "Não pode"),
        ("Brasileiro adquiriu outra nacionalidade", "Não perde (EC 131)"),
        ("Fraude na naturalização", "Perde, por sentença judicial"),
    ]),
    h2("Leve para a prova"),
    bl("Regra: **ius soli**.",
       "Exceção: pais **a serviço do seu país**.",
       "Basta **um** dos pais a serviço do Brasil.",
       "Opção: **após a maioridade**, na **Justiça Federal**.",
       "Língua portuguesa: **1 ano**.",
       "Extraordinária: **mais de 15 anos**.",
       "Cargos de nato: **MP3.COM**.",
       "Só a **Constituição** diferencia.",
       "Perda: **sentença** ou **pedido expresso**.",
       "Outra nacionalidade **não** gera perda."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "NACIONALIDADE", "rootSub": "arts. 12 e 13",
    "left": [
        {"label": "Nato: solo", "items": ["nasceu no Brasil", "pais não a serviço", "do seu país"]},
        {"label": "Nato: serviço", "items": ["nasceu no exterior", "pai ou mãe brasileiros", "a serviço do Brasil"]},
        {"label": "Nato: registro", "items": ["repartição brasileira", "ou residência + opção", "após a maioridade"]},
        {"label": "Naturalização", "items": ["língua portuguesa: 1 ano", "extraordinária: 15 anos", "sem condenação"]},
        {"label": "Portugueses", "items": ["residência permanente", "reciprocidade", "não vira nato"]},
    ],
    "right": [
        {"label": "Cargos de nato", "items": ["MP3.COM", "linha sucessória", "Ministro da Defesa"]},
        {"label": "Outras diferenças", "items": ["extradição", "Conselho da República", "empresa jornalística"]},
        {"label": "Perda I", "items": ["só naturalizado", "sentença judicial", "fraude ou atentado"]},
        {"label": "Perda II", "items": ["pedido expresso", "sem apatridia", "pode readquirir"]},
        {"label": "Art. 13", "items": ["língua portuguesa", "bandeira, hino", "armas e selo"]},
    ],
}

QUIZ = quiz([
    ("C", "O filho de estrangeiros que estejam a serviço de seu país, nascido no Brasil, não é brasileiro nato.",
     "É a exceção do art. 12, I, a."),
    ("E", "Para ser brasileiro nato, o filho de brasileiros nascido no exterior deve, obrigatoriamente, vir residir no Brasil.",
     "O registro em repartição brasileira competente também basta."),
    ("C", "A naturalização extraordinária exige residência ininterrupta no Brasil há mais de quinze anos, ausência de condenação penal e requerimento.",
     "Art. 12, II, b."),
    ("E", "O cargo de governador de estado é privativo de brasileiro nato.",
     "Não consta do rol do art. 12, § 3º."),
    ("C", "O cargo de oficial das Forças Armadas é privativo de brasileiro nato.",
     "Art. 12, § 3º, VI."),
    ("E", "Lei ordinária pode criar novas distinções entre brasileiros natos e naturalizados, desde que razoáveis.",
     "Somente a Constituição pode distinguir (art. 12, § 2º)."),
    ("C", "Após a EC 131/2023, a mera aquisição de outra nacionalidade não acarreta a perda da nacionalidade brasileira.",
     "A hipótese foi suprimida do § 4º."),
    ("E", "O pedido expresso de perda da nacionalidade brasileira será sempre deferido, ainda que o requerente se torne apátrida.",
     "A Constituição ressalva as situações que acarretem apatridia."),
    ("C", "A bandeira, o hino, as armas e o selo nacionais são símbolos da República Federativa do Brasil.",
     "Art. 13, § 1º."),
    ("E", "O português com residência permanente no Brasil, havendo reciprocidade, pode ser eleito Presidente da República.",
     "Recebe direitos de brasileiro, mas nunca pode ocupar cargo privativo de nato."),
], 10)

SOURCES = [
    "Constituição da República Federativa do Brasil de 1988, arts. 12 e 13; EC 131/2023.",
    SRC_R,
]
