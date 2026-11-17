# -*- coding: utf-8 -*-
"""Língua Portuguesa · Acentuação gráfica — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "lp-acentuacao-01", "LP", "LP-02", "resumo", "Acentuação gráfica", "Língua Portuguesa · Fonologia e ortografia",
    "portugues_acentuacao", "Portugues_Acentuacao_RESUMO.pdf", None, ["Acentuação gráfica"], RES_SUB,
    RES_ITEMS("regras gerais, hiatos, ditongos, verbos e Acordo"),
    "Tópico do edital: Acentuação gráfica (Língua Portuguesa)", "Base: Acordo Ortográfico (Decreto nº 6.583/2008) e gramáticas de referência.", 35)

THEORY = [
    exam("O que a banca cobra",
         "**“X e Y são acentuadas pela mesma regra”** e **“a retirada do acento manteria a correção”**. "
         "Método: separe as sílabas, ache a tônica, classifique e só então compare."),
    h2("1. Regras gerais"),
    tb(["Tipo", "Acentuam-se", "Exemplos"], [0.24, 0.4, 0.36], [
        ("Proparoxítonas", "Todas", "público, médico, álibi"),
        ("Oxítonas", "a(s), e(s), o(s), em, ens", "sofá, café, cipó, também, parabéns"),
        ("Monossílabos tônicos", "a(s), e(s), o(s)", "pá, pé, pó, mês, três"),
        ("Paroxítonas", "L, N, R, X, PS, I(S), US, UM/UNS, Ã(S), ÃO(S), ON(S), ditongo", "fácil, hífen, caráter, tórax, bíceps, júri, vírus, álbum, órgão, história"),
    ]),
    trap("Pegadinha",
         "**Hífen** tem acento; **hifens, itens, jovens** não. **Café** (oxítona) e **pé** (monossílabo) são **regras diferentes**."),
    h2("2. Ditongos abertos éi, éu, ói"),
    bl("**Com acento** em oxítonas e monossílabos: herói, papéis, chapéu, céu, dói.",
       "**Sem acento** em paroxítonas: ideia, assembleia, heroico, jiboia."),
    h2("3. Hiato: i e u tônicos"),
    bl("**Com acento** quando sozinhos na sílaba ou com S: saída, saúde, país, baú, juízes.",
       "**Sem acento** antes de L, M, N, R, Z na mesma sílaba e antes de NH: juiz, raiz, ruim, cair, rainha.",
       "**Sem acento** em paroxítona depois de ditongo: feiura, baiuca. Em oxítona, com acento: Piauí.",
       "**oo** e **ee** sem acento: voo, enjoo, leem, veem, creem, deem."),
    h2("4. Verbos"),
    tb(["Singular", "Plural", "Verbos"], [0.3, 0.3, 0.4], [
        ("tem, vem", "têm, vêm", "ter e vir"),
        ("mantém, contém, intervém", "mantêm, contêm, intervêm", "derivados de ter e vir"),
        ("crê, dê, lê, vê", "creem, deem, leem, veem", "crer, dar, ler, ver"),
    ]),
    nt("Vêm = verbo vir. Veem = verbo ver. Com pronome: amá-lo, vendê-la, compô-lo; parti-lo (sem acento); distribuí-lo (hiato)."),
    h2("5. Acento diferencial"),
    bl("**Obrigatório**: pôr × por; pôde × pode; têm/vêm × tem/vem.",
       "**Facultativo**: fôrma/forma; dêmos/demos.",
       "**Abolido**: para (verbo), pelo, pela, polo, pera."),
]

SUMMARY = [
    h2("Quadro: o que o Acordo mudou"),
    tb(["Caiu", "Agora se escreve", "Continua com acento"], [0.36, 0.3, 0.34], [
        ("Ditongo aberto em paroxítona", "ideia, heroico, jiboia", "herói, papéis, chapéu"),
        ("I/U após ditongo em paroxítona", "feiura, baiuca", "saída, saúde, Piauí"),
        ("Hiatos oo e ee", "voo, leem, veem", "têm, vêm"),
        ("Diferenciais", "para, pelo, polo", "pôr, pôde"),
        ("U tônico de gue/gui/que/qui", "argui, averigue", "—"),
        ("Trema", "frequente, linguiça", "Müller (nomes estrangeiros)"),
    ]),
    h2("Leve para a prova"),
    bl("**Proparoxítona**: todas.",
       "Oxítona e paroxítona têm regras **opostas**: café × mesa; fácil × papel.",
       "**-em/-ens**: acento só nas oxítonas (também, parabéns); nunca em item, itens, jovem.",
       "**História, série, água**: paroxítonas terminadas em ditongo.",
       "**Juiz** sem acento; **juízes** com acento.",
       "**Herói** com acento; **heroico** sem.",
       "**Têm/vêm** com circunflexo; **leem/veem/creem/deem** sem.",
       "**Mantém** (ele) × **mantêm** (eles).",
       "**Pôr** e **pôde** continuam com acento.",
       "Tirar o acento quase sempre cria outra palavra: secretária/secretaria, está/esta, país/pais."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "ACENTUAÇÃO GRÁFICA", "rootSub": "sílabas › tônica › classe › regra",
    "left": [
        {"label": "Proparoxítonas", "items": ["Todas levam acento", "público, médico, álibi"]},
        {"label": "Oxítonas", "items": ["a(s), e(s), o(s), em, ens", "café, cipó, também, parabéns"]},
        {"label": "Monossílabos tônicos", "items": ["a(s), e(s), o(s)", "pá, pé, pó, três", "Regra diferente da oxítona"]},
        {"label": "Paroxítonas", "items": ["L, N, R, X, PS, I, US, UM, Ã, ÃO", "Ditongo: história, série", "Sem acento: itens, hifens, jovem"]},
        {"label": "Ditongos abertos", "items": ["Oxítona: herói, papéis, céu", "Paroxítona: ideia, heroico"]},
    ],
    "right": [
        {"label": "Hiato com I e U", "items": ["saída, saúde, país, juízes", "Não: juiz, raiz, ruim, rainha", "Não: feiura, baiuca"]},
        {"label": "Hiatos OO e EE", "items": ["voo, enjoo, perdoo", "creem, deem, leem, veem"]},
        {"label": "Verbos", "items": ["tem/têm · vem/vêm", "mantém/mantêm", "vêm (vir) ≠ veem (ver)"]},
        {"label": "Diferencial", "items": ["Fica: pôr, pôde, têm, vêm", "Opcional: fôrma, dêmos", "Caiu: para, pelo, polo"]},
        {"label": "Banca", "items": ["“Mesma regra?” Classifique antes", "Sem acento muda o sentido", "secretária ≠ secretaria"]},
    ],
}

QUIZ = quiz([
    ("C", "As palavras médico e lâmpada são acentuadas por serem proparoxítonas.",
     "Todas as proparoxítonas são acentuadas."),
    ("E", "O vocábulo jovens deve receber acento gráfico, à semelhança de parabéns.",
     "Parabéns é oxítona em ens (com acento); jovens é paroxítona em ens (sem acento)."),
    ("E", "Com o Acordo Ortográfico, as palavras herói e chapéu perderam o acento gráfico.",
     "O acento caiu apenas nos ditongos abertos das paroxítonas (ideia, heroico). Em oxítonas e monossílabos, permanece."),
    ("C", "Em raízes, o acento gráfico justifica-se pela presença de i tônico em hiato, sozinho na sílaba.",
     "Ra-í-zes. Em ra-iz, o i forma sílaba com z e não é acentuado."),
    ("C", "Na frase “As testemunhas vêm à delegacia amanhã”, o acento circunflexo indica que o verbo vir está na terceira pessoa do plural.",
     "Vem (singular) × vêm (plural)."),
    ("E", "As formas voo e enjoo devem ser grafadas com acento circunflexo no primeiro o.",
     "O hiato oo perdeu o acento com o Acordo."),
    ("E", "As palavras tórax e sofá são acentuadas de acordo com a mesma regra.",
     "Tórax é paroxítona terminada em x; sofá é oxítona terminada em a."),
    ("C", "A palavra série recebe acento por ser paroxítona terminada em ditongo.",
     "Sé-rie: ditongo crescente final."),
    ("E", "Em “Ele contêm a multidão”, a forma verbal está corretamente acentuada.",
     "Com sujeito no singular, usa-se contém. Contêm é a forma do plural."),
    ("C", "O acento em pôr, verbo, é diferencial e foi mantido pelo Acordo Ortográfico.",
     "Distingue o verbo pôr da preposição por."),
], 10)

SOURCES = ["Acordo Ortográfico da Língua Portuguesa (1990), promulgado pelo Decreto nº 6.583/2008; VOLP.", SRC_R]
