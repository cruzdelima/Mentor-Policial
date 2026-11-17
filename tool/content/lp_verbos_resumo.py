# -*- coding: utf-8 -*-
"""Língua Portuguesa · Verbos: flexão, tempos, modos e vozes — RESUMO (revisão)."""
from common import *

MATERIAL = material(
    "lp-verbos-01", "LP", "LP-06", "resumo", "Verbos: flexão, tempos, modos e vozes", "Língua Portuguesa · Morfossintaxe",
    "portugues_verbos", "Portugues_Verbos_RESUMO.pdf", None, ["Verbos:", "tempos, modos e vozes"], RES_SUB,
    RES_ITEMS("valor dos tempos, irregulares, imperativo e vozes verbais"),
    "Tópico do edital: Verbos — flexão, tempos, modos e vozes (Língua Portuguesa)",
    "Base: gramáticas de referência (Bechara; Cunha e Cintra).", 40)

THEORY = [
    exam("O que a banca cobra",
         "**Troca de tempos** (mantém ou altera o sentido?), **forma correta** dos irregulares (futuro do subjuntivo, *têm/detêm*) e "
         "**vozes** (passiva sintética e concordância com o *se*)."),
    h2("1. Valor dos tempos"),
    bl("**Perfeito** = fato concluído (*chegaram*). **Imperfeito** = hábito ou ação em curso (*chegavam*). Trocar um pelo outro **altera** o sentido.",
       "**Mais-que-perfeito**: passado anterior a outro passado. *fugira = tinha fugido = havia fugido* (troca **mantém** o sentido).",
       "**Futuro do pretérito**: hipótese, condição, polidez. *O suspeito **teria fugido*** = informação não confirmada.",
       "**Futuro do subjuntivo**: com *se, quando, assim que* — *quando ele **vier**, se ele **puder***."),
    h2("2. Formação"),
    bl("Presente do subjuntivo vem da **1ª pessoa do presente**: *faço › faça; trago › traga*.",
       "Imperfeito e futuro do subjuntivo vêm do **pretérito perfeito**: *fizeram › fizesse, fizer; vieram › viesse, vier*.",
       "**Imperativo afirmativo**: tu e vós do presente do indicativo **sem -s** (*faze, fazei*); o resto, do presente do subjuntivo (*faça, façamos, façam*).",
       "**Imperativo negativo**: tudo do presente do subjuntivo (*não faças, não faça*)."),
    trap("Futuro do subjuntivo",
         "*se eu **vir*** (ver) · *se eu **vier*** (vir) · *se ele **mantiver*** · *se ele **propuser*** · *se ele **intervier*** · *se ele **couber***. "
         "Errado: “quando eu ver”, “se ele manter”, “se ele propor”."),
    h2("3. Irregulares e impessoais"),
    bl("**ele detém / eles detêm** · **ele intervém / eles intervêm** · ele **interveio** (não “interviu”).",
       "**Haver** (existir, tempo) e **fazer** (tempo): sempre no singular, inclusive o auxiliar — *Deve haver provas. Faz dois anos.*",
       "**-iar** é regular, exceto **MARIO**: *medeio, anseio, remedeio, incendeio, odeio*. **-ear**: *passeio, nomeio*.",
       "**Reaver**: só formas com *v* — *ele **reouve***. **Requerer**: *eu requeiro, ele requereu*."),
    h2("4. Particípio e infinitivo"),
    bl("**ter/haver + regular** (*tinha aceitado*); **ser/estar + irregular** (*foi aceito*). *Pago, ganho, gasto* servem para os dois.",
       "Infinitivo **não flexiona** em locução (*devem apresentar*) e com pronome oblíquo (*mandou-os sair*).",
       "Infinitivo **flexiona** com sujeito próprio: *É preciso **sairmos** cedo.*"),
    h2("5. Vozes"),
    tb(["Voz", "Exemplo", "Observação"], [0.22, 0.4, 0.38], [
        ("Ativa", "A polícia prendeu os suspeitos.", "Sujeito agente"),
        ("Passiva analítica", "Os suspeitos foram presos pela polícia.", "*ser* no tempo da ativa; particípio concorda"),
        ("Passiva sintética", "Prenderam-se os suspeitos.", "VTD + se; verbo concorda com o sujeito"),
        ("Indeterminação", "Precisa-se de agentes.", "VTI/VI + se; verbo no singular"),
    ]),
]

SUMMARY = [
    h2("Quadro: certo × errado"),
    tb(["Evite", "Prefira", "Por quê"], [0.32, 0.32, 0.36], [
        ("Quando eu ver o laudo…", "Quando eu vir o laudo…", "Futuro do subjuntivo de ver"),
        ("Se ele manter a versão…", "Se ele mantiver a versão…", "Deriva de mantiveram"),
        ("Ele interviu na briga.", "Ele interveio na briga.", "Intervir segue vir"),
        ("Haviam muitas provas.", "Havia muitas provas.", "Haver = existir: impessoal"),
        ("Fazem dois anos.", "Faz dois anos.", "Fazer (tempo): impessoal"),
        ("Vende-se viaturas.", "Vendem-se viaturas.", "Passiva sintética: sujeito plural"),
        ("Tratam-se de casos.", "Trata-se de casos.", "VTI + se: singular"),
        ("O recurso foi aceitado.", "O recurso foi aceito.", "ser + particípio irregular"),
        ("Eles detém a posse.", "Eles detêm a posse.", "Plural com circunflexo"),
        ("Eu medio o conflito.", "Eu medeio o conflito.", "Mediar: exceção MARIO"),
    ]),
    h2("Leve para a prova"),
    bl("Perfeito × imperfeito: a troca **altera** o sentido.",
       "Mais-que-perfeito simples × composto: a troca **mantém** o sentido.",
       "Futuro do pretérito = **hipótese**; trocar por perfeito transforma em fato.",
       "Futuro do subjuntivo vem do **pretérito perfeito** (viram › vir).",
       "*Se + -sse* pede *-ria*; *se + -r* pede *-rá*.",
       "**Haver** e **fazer** impessoais: singular, inclusive o auxiliar.",
       "VTD + se: verbo concorda; VTI + se: singular.",
       "Na passiva, *ser* fica no **tempo da ativa**.",
       "Imperativo de *você* = presente do subjuntivo (*faça*).",
       "Uniformidade de tratamento: não misture *tu* e *você*."),
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "VERBOS", "rootSub": "tempos, modos e vozes",
    "left": [
        {"label": "Indicativo", "items": ["perfeito: fato concluído", "imperfeito: hábito", "fugira = tinha fugido"]},
        {"label": "Futuro do pretérito", "items": ["hipótese: teria fugido", "condição: seria reduzida", "polidez: gostaria"]},
        {"label": "Subjuntivo", "items": ["que eu faça (de faço)", "se eu fizesse (de fizeram)", "quando eu fizer"]},
        {"label": "Imperativo", "items": ["tu/vós: indicativo sem -s", "você: faça", "negativo: todo subjuntivo"]},
        {"label": "Correlação", "items": ["se -sse + -ria", "se -r + -rá", "queria que viesse"]},
    ],
    "right": [
        {"label": "Irregulares", "items": ["se eu vir · se eu vier", "mantiver · propuser", "interveio · detêm"]},
        {"label": "Impessoais", "items": ["havia provas", "faz dois anos", "deve haver"]},
        {"label": "Particípio", "items": ["ter + aceitado", "ser + aceito", "pago · ganho · gasto"]},
        {"label": "Vozes", "items": ["ativa · passiva analítica", "passiva sintética: VTD + se", "ser no tempo da ativa"]},
        {"label": "O se", "items": ["vendem-se casas (plural)", "precisa-se de (singular)", "trata-se de"]},
    ],
}

QUIZ = quiz([
    ("E", "Em “Se você ver o documento, avise-me”, a forma verbal está de acordo com a norma-padrão.",
     "O futuro do subjuntivo de ver é vir: se você vir o documento."),
    ("C", "Em “Se ele mantiver a versão, será indiciado”, a forma mantiver corresponde ao futuro do subjuntivo de manter.",
     "Manter segue ter: mantiveram › se ele mantiver."),
    ("C", "Em “Prenderam-se os suspeitos”, há voz passiva sintética, e o verbo concorda com o sujeito os suspeitos.",
     "Prender é transitivo direto; com o se apassivador, os suspeitos é o sujeito."),
    ("E", "Em “Tratam-se de casos graves”, a concordância verbal está de acordo com a norma-padrão.",
     "Tratar de é transitivo indireto; o se indetermina o sujeito e o verbo fica no singular: trata-se."),
    ("C", "Em “O laudo foi entregue ontem”, o emprego do particípio irregular com o auxiliar ser está de acordo com a norma-padrão.",
     "Com ser e estar, usa-se o particípio irregular: entregue."),
    ("E", "Em “Fazem dois anos que o crime ocorreu”, a concordância verbal está de acordo com a norma-padrão.",
     "Fazer indicando tempo decorrido é impessoal: faz dois anos."),
    ("C", "Em “O suspeito estaria armado”, o futuro do pretérito indica que a informação não está confirmada.",
     "É o uso do futuro do pretérito para expressar incerteza ou hipótese."),
    ("E", "A forma do imperativo negativo do verbo dizer correspondente a tu é não diz.",
     "O imperativo negativo vem todo do presente do subjuntivo: não digas."),
    ("C", "Em “Eles intervêm sempre que há conflito”, a forma verbal está de acordo com a norma-padrão.",
     "Intervir segue vir: ele intervém, eles intervêm."),
    ("E", "Em “O Estado reaveu os bens desviados”, a forma verbal está de acordo com a norma-padrão.",
     "Reaver segue haver nas formas com v: o Estado reouve os bens."),
], 10)

SOURCES = [GRAM, SRC_R]
