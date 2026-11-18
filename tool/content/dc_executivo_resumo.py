# -*- coding: utf-8 -*-
"""Direito Constitucional · Poder Executivo — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "dc-executivo-01", "DC", "DC-10", "resumo", "Poder Executivo", "Direito Constitucional · Organização dos Poderes",
    "constitucional_executivo", "Constitucional_Poder_Executivo_RESUMO.pdf", None, ["Poder", "Executivo"], RES_SUB,
    RES_ITEMS("eleição, sucessão, atribuições e responsabilidade"),
    "Tópico do edital: Poder Executivo (arts. 76 a 91) — Direito Constitucional",
    "Base: Constituição Federal de 1988 e jurisprudência do STF.", 35)

THEORY = [
    exam("O que a banca cobra",
         "**Posse** (5 de janeiro), **dupla vacância**, atribuições **delegáveis** e o **processo** contra o Presidente."),
    h2("1. Eleição e mandato"),
    bl("Presidente = **Chefe de Estado** + **Chefe de Governo**, auxiliado pelos Ministros.",
       "Eleito por **maioria absoluta** dos votos **válidos**; senão, **2º turno** entre os dois mais votados.",
       "Mandato de **4 anos**, posse em **5 de janeiro** (EC 111/2021, a partir dos eleitos em 2026); uma reeleição.",
       "Não assumiu em **10 dias**: cargo **vago** (salvo força maior)."),
    h2("2. Sucessão"),
    bl("**Vice** substitui (impedimento) e **sucede** (vaga).",
       "Depois: Presidente da **Câmara**, do **Senado** e do **STF**, só **substituindo**.",
       "Dupla vacância: **2 primeiros anos** › eleição **direta** em **90 dias**; **2 últimos anos** › **indireta** pelo Congresso em **30 dias**; "
       "mandato-tampão.",
       "Sair do País por **mais de 15 dias** exige licença do Congresso."),
    h2("3. Atribuições"),
    bl("Relações exteriores, tratados (referendo do Congresso), comando das **Forças Armadas**, estado de defesa e de sítio, intervenção.",
       "Sanciona, veta, edita **MP**, expede decretos; nomeia Ministros, e, com o Senado, Ministros do STF e o PGR.",
       "Delegáveis a **Ministros, PGR e AGU**: **decreto autônomo** (VI), **indulto** e comutação (XII), **prover cargos** (XXV)."),
    h2("4. Responsabilidade"),
    bl("Câmara autoriza por **2/3** › **STF** (crime comum) ou **Senado** (crime de responsabilidade).",
       "Afastamento: crime comum com **recebimento da denúncia** pelo STF; responsabilidade com a **instauração** no Senado; cessa após **180 dias**.",
       "Sem prisão antes de **sentença condenatória**; não responde por **atos estranhos** às funções durante o mandato.",
       "Prerrogativas **não se estendem** a governadores (julgados pelo **STJ**, sem autorização da Assembleia).",
       "Conselho da **República**: líderes e **6 natos**; Conselho de **Defesa Nacional**: Ministros e **comandantes militares**; ambos opinativos."),
]

SUMMARY = [
    h2("Quadro rápido"),
    tb(["Item", "Regra"], [0.46, 0.54], [
        ("Posse do Presidente", "5 de janeiro (a partir de 2027)"),
        ("Prazo para assumir", "10 dias, senão o cargo vaga"),
        ("Linha de substituição", "Câmara › Senado › STF"),
        ("Vacância nos 2 primeiros anos", "Direta, em 90 dias"),
        ("Vacância nos 2 últimos anos", "Indireta, em 30 dias"),
        ("Saída do País sem licença", "Até 15 dias"),
        ("Atribuições delegáveis", "Decreto autônomo, indulto, provimento"),
        ("Crime comum", "Câmara 2/3 › STF"),
        ("Crime de responsabilidade", "Câmara 2/3 › Senado"),
        ("Afastamento máximo", "180 dias"),
    ]),
    h2("Leve para a prova"),
    bl("Maioria absoluta dos votos **válidos**.",
       "Posse em **5 de janeiro**.",
       "Só o **Vice sucede**.",
       "Ordem: **Câmara, Senado, STF**.",
       "Últimos dois anos: eleição **indireta**.",
       "Delegação: **DIP** a Ministros, PGR e AGU.",
       "MP **não** se delega.",
       "Crime comum: afasta com o **recebimento** da denúncia.",
       "Atos **estranhos** às funções: só após o mandato.",
       "Governador **não** tem essas prerrogativas."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "EXECUTIVO", "rootSub": "arts. 76 a 91",
    "left": [
        {"label": "Eleição", "items": ["maioria absoluta", "votos válidos", "2º turno"]},
        {"label": "Mandato", "items": ["4 anos", "posse em 5/1", "uma reeleição"]},
        {"label": "Substituição", "items": ["Vice sucede", "Câmara, Senado, STF", "só substituem"]},
        {"label": "Dupla vacância", "items": ["início: direta, 90 dias", "fim: indireta, 30 dias", "mandato-tampão"]},
        {"label": "Atribuições", "items": ["chefe de Estado", "chefe de Governo", "comando das FA"]},
    ],
    "right": [
        {"label": "Delegáveis", "items": ["decreto autônomo", "indulto", "prover cargos"]},
        {"label": "Crime comum", "items": ["Câmara: 2/3", "STF julga", "afasta no recebimento"]},
        {"label": "Responsabilidade", "items": ["Senado julga", "perda do cargo", "inabilitação 8 anos"]},
        {"label": "Imunidades", "items": ["sem prisão antes", "atos estranhos", "só o Presidente"]},
        {"label": "Conselhos", "items": ["República: 6 natos", "Defesa: comandantes", "opinativos"]},
    ],
}

QUIZ = quiz([
    ("C", "O Vice-Presidente substitui o Presidente no caso de impedimento e sucede-lhe no de vaga.",
     "Art. 79."),
    ("E", "O presidente do Supremo Tribunal Federal é o primeiro na linha de substituição do Presidente da República após o Vice-Presidente.",
     "O primeiro é o presidente da Câmara dos Deputados."),
    ("C", "Ocorrendo a vacância dos cargos de Presidente e Vice-Presidente nos últimos dois anos do período presidencial, a eleição será feita pelo Congresso Nacional.",
     "Art. 81, § 1º."),
    ("E", "Os eleitos após a dupla vacância exercerão mandato integral de quatro anos.",
     "Apenas completam o período dos antecessores."),
    ("C", "O Presidente da República pode delegar ao Advogado-Geral da União a atribuição de prover cargos públicos federais.",
     "Art. 84, parágrafo único."),
    ("E", "Nas infrações penais comuns, o Presidente da República é julgado pelo Senado Federal.",
     "Nas infrações comuns, o julgamento é do STF."),
    ("C", "Enquanto não sobrevier sentença condenatória nas infrações comuns, o Presidente da República não estará sujeito a prisão.",
     "Art. 86, § 3º."),
    ("E", "A condenação do Presidente da República por crime de responsabilidade acarreta a perda do cargo e a inabilitação para o exercício de função pública por cinco anos.",
     "A inabilitação é por oito anos."),
    ("C", "O Conselho da República é órgão superior de consulta do Presidente e pronuncia-se sobre intervenção federal, estado de defesa e estado de sítio.",
     "Art. 90, I."),
    ("E", "Os pareceres do Conselho de Defesa Nacional vinculam o Presidente da República na decretação do estado de sítio.",
     "As manifestações dos Conselhos são opinativas."),
], 10)

SOURCES = [
    "Constituição da República Federativa do Brasil de 1988, arts. 76 a 91; EC 111/2021.",
    SRC_R,
]
