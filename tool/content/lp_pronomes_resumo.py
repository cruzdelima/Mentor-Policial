# -*- coding: utf-8 -*-
"""Língua Portuguesa · Pronomes: emprego e colocação — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "lp-pronomes-01", "LP", "LP-04", "resumo", "Pronomes: emprego e colocação", "Língua Portuguesa · Morfossintaxe",
    "portugues_pronomes", "Portugues_Pronomes_RESUMO.pdf", None, ["Pronomes:", "emprego e colocação"], RES_SUB,
    RES_ITEMS("pessoais, demonstrativos, relativos e colocação pronominal"),
    "Tópico do edital: Pronomes — emprego e colocação pronominal (Língua Portuguesa)",
    "Base: gramáticas de referência e Manual de Redação da Presidência da República.", 40)

THEORY = [
    exam("O que a banca cobra",
         "**Referência** (“o pronome retoma…”), **emprego** (*o* × *lhe*, *este* × *esse*, *cujo*, *onde*, preposição antes do relativo) "
         "e **colocação** (“o pronome pode ir para depois do verbo?” — procure a palavra atrativa)."),
    h2("1. Pessoais"),
    bl("**Para eu fazer** (sujeito de infinitivo) × **para mim** (sem verbo). **Entre mim e ti.**",
       "**o, a** = objeto direto; **lhe** = objeto indireto. *Eu o vi. Eu lhe obedeço.*",
       "Depois de **R, S, Z**: lo, la (*prendê-lo, fi-la*). Depois de **som nasal**: no, na (*prenderam-no*).",
       "**Com nós** só com reforço (*com nós dois*); senão, **conosco**. **Si, consigo**: só reflexivos.",
       "**Tratamento**: verbo e possessivo na **3ª pessoa**; **Vossa** = falando com; **Sua** = falando de."),
    h2("2. Possessivos e demonstrativos"),
    bl("**Seu** pode gerar **ambiguidade**; desfaz-se com *dele/dela*.",
       "**Este** = perto de quem fala; presente; o que **vai ser dito**. **Esse** = perto do ouvinte; o que **já foi dito**.",
       "Dois termos: **este** = o último citado; **aquele** = o primeiro.",
       "**O, a** = demonstrativo quando equivale a *aquilo, aquele, isso*: *o que disse; não o disse*."),
    h2("3. Relativos"),
    tb(["Relativo", "Regra", "Exemplo"], [0.16, 0.48, 0.36], [
        ("que", "Pessoa ou coisa", "o agente que prendeu"),
        ("quem", "Só pessoa, com preposição", "a pessoa a quem me referi"),
        ("cujo", "Posse; concorda com o possuído; **sem artigo** depois", "o réu cuja defesa…"),
        ("onde", "Só **lugar** (= em que)", "a rua onde mora"),
        ("o qual", "Desfaz ambiguidade; após preposição longa", "a lei segundo a qual…"),
    ]),
    key("Preposição antes do relativo",
        "*O filme **a que** assisti; a pessoa **de quem** gosto; o cargo **a que** aspiro; o autor **de cujo** livro falei.*"),
    h2("4. Indefinidos"),
    bl("**Algum** posposto = nenhum (*ajuda alguma*). **Certo** anteposto = indefinido (*certo dia*).",
       "**Todo o** = inteiro; **todo** = qualquer. **Bastantes** provas (= muitas)."),
    h2("5. Colocação pronominal"),
    tb(["Posição", "Quando", "Exemplo"], [0.18, 0.5, 0.32], [
        ("Próclise", "Palavra atrativa: negação, advérbio, relativo, indefinido, demonstrativo neutro, conjunção subordinativa, interrogativo; frases exclamativas e optativas; em + gerúndio", "Não me disse. Quando se soube…"),
        ("Mesóclise", "Futuro do presente ou do pretérito, **sem** atração", "Dir-se-ia. Far-lhe-ei."),
        ("Ênclise", "Início de frase; imperativo afirmativo; gerúndio; infinitivo impessoal", "Disseram-me. Sente-se."),
    ]),
    trap("Proibições",
         "Não se começa frase com pronome átono. **Nunca** ênclise com **futuro** (“farei-o”) nem com **particípio** (“tinha dado-me”)."),
    bl("**Facultativo**: sujeito expresso sem atração (*Ele me disse / Ele disse-me*).",
       "**Locução com infinitivo ou gerúndio**: *Devo-lhe dizer / Devo dizer-lhe*; com atração: *Não lhe devo dizer / Não devo dizer-lhe*.",
       "**Locução com particípio**: pronome junto ao auxiliar — *Tinha-me dito / Não me tinha dito*."),
]

SUMMARY = [
    h2("Quadro: certo × errado no padrão formal"),
    tb(["Evite", "Prefira", "Por quê"], [0.3, 0.3, 0.4], [
        ("Vi ele ontem.", "Vi-o ontem.", "Reto não é objeto"),
        ("Eu lhe convidei.", "Eu o convidei.", "Convidar é transitivo direto"),
        ("Entre eu e você.", "Entre mim e você.", "Preposição pede oblíquo tônico"),
        ("Para mim fazer.", "Para eu fazer.", "Sujeito de infinitivo"),
        ("O momento onde…", "O momento em que…", "Onde só para lugar"),
        ("O réu cujo o pai…", "O réu cujo pai…", "Cujo sem artigo"),
        ("O livro que gosto.", "O livro de que gosto.", "Gostar de"),
        ("Me disseram.", "Disseram-me.", "Não se inicia com átono"),
        ("Não disse-me.", "Não me disse.", "Negação atrai"),
        ("Tinha avisado-me.", "Tinha-me avisado.", "Particípio não aceita ênclise"),
    ]),
    h2("Leve para a prova"),
    bl("Referência: **substitua** o pronome pelo termo e confira a concordância.",
       "**O/a** sem preposição; **lhe** com preposição.",
       "**Esse** retoma; **este** anuncia.",
       "**Este** = o mais próximo; **aquele** = o mais distante.",
       "**Onde** só lugar; **cujo** só posse.",
       "A **preposição** do verbo vai para antes do relativo.",
       "Achou **palavra atrativa**? Próclise obrigatória.",
       "Futuro sem atração: **mesóclise**; com atração: próclise.",
       "Tratamento: **3ª pessoa**.",
       "**Isso/isto/o** podem retomar uma oração inteira."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "PRONOMES", "rootSub": "emprego e colocação",
    "left": [
        {"label": "Pessoais", "items": ["para eu fazer · para mim", "entre mim e ti", "o/a: direto · lhe: indireto"]},
        {"label": "Formas", "items": ["R, S, Z: prendê-lo, fi-la", "Nasal: prenderam-no", "conosco · com nós dois"]},
        {"label": "Tratamento", "items": ["Verbo na 3ª pessoa", "Vossa: com · Sua: de", "Seu, não vosso"]},
        {"label": "Demonstrativos", "items": ["este: vai dizer · esse: já disse", "este: próximo · aquele: distante", "o = aquilo: o que disse"]},
        {"label": "Possessivos e indefinidos", "items": ["seu: risco de ambiguidade", "ajuda alguma = nenhuma", "certo dia ≠ dia certo"]},
    ],
    "right": [
        {"label": "Relativos", "items": ["cujo: posse, sem artigo", "onde: só lugar", "quem: pessoa, com preposição"]},
        {"label": "Preposição + relativo", "items": ["a que assisti", "de quem gosto", "de cujo autor falei"]},
        {"label": "Próclise", "items": ["Negação, advérbio, relativo", "Conjunção subordinativa", "Indefinido, interrogativo"]},
        {"label": "Mesóclise e ênclise", "items": ["Futuro sem atração: dir-se-ia", "Início de frase: Disseram-me", "Imperativo: Sente-se"]},
        {"label": "Proibido", "items": ["Começar com átono", "Ênclise com futuro", "Ênclise com particípio"]},
    ],
}

QUIZ = quiz([
    ("E", "Em “Trouxeram os documentos para mim assinar”, o pronome está empregado conforme a norma-padrão.",
     "Como sujeito do infinitivo assinar, usa-se o pronome reto: para eu assinar."),
    ("C", "Em “Obedeço-lhe sem questionar”, o pronome lhe funciona como objeto indireto.",
     "Obedecer a alguém: o complemento é indireto, substituível por lhe."),
    ("C", "A combinação de fizeram com o pronome as resulta em fizeram-nas.",
     "Depois de terminação nasal, usam-se no, na, nos, nas."),
    ("E", "Em “Vossa Senhoria receberá vossos documentos amanhã”, o possessivo está corretamente empregado.",
     "Pronomes de tratamento pedem possessivo de 3ª pessoa: seus documentos."),
    ("E", "Em “O crime ocorreu em uma época onde não havia câmeras”, o emprego de onde está correto.",
     "Onde retoma apenas lugar. Para tempo, usa-se em que ou na qual."),
    ("C", "Em “A testemunha de cujo depoimento duvidamos foi dispensada”, o emprego da preposição de antes do relativo justifica-se pela regência de duvidar.",
     "Duvidar de: a preposição antecede o pronome relativo."),
    ("E", "Em “Ninguém avisou-me da mudança”, a colocação do pronome está de acordo com a norma-padrão.",
     "O pronome indefinido ninguém atrai o pronome: Ninguém me avisou."),
    ("C", "Em “Realizar-se-á nova perícia”, a mesóclise justifica-se pelo emprego do verbo no futuro do presente, sem palavra atrativa.",
     "Com futuro e sem atração, usa-se a mesóclise."),
    ("C", "Em “A ordem é esta: todos devem permanecer no local”, o pronome esta anuncia o que será dito em seguida.",
     "Este/esta/isto têm valor catafórico: apontam para o que vem depois."),
    ("E", "Em “Haviam contado-lhe toda a história”, o pronome está bem colocado.",
     "Não se usa ênclise com particípio: Haviam-lhe contado."),
], 10)

SOURCES = [GRAM, SRC_R]
