# -*- coding: utf-8 -*-
"""Língua Portuguesa · Figuras de linguagem — MATERIAL APROFUNDADO (estudo inicial)."""
from common import *

MATERIAL = material(
    "lp-figuras-02", "LP", "LP-21", "aprofundado", "Figuras de linguagem", "Língua Portuguesa · Semântica e estilística",
    "portugues_figuras_aprofundado", "Portugues_Figuras_Linguagem_APROFUNDADO.pdf", None, ["Figuras", "de linguagem"],
    ["Teoria completa para o primeiro estudo: figuras de palavra, de pensamento, de construção", "e de som, com 20 questões no estilo Cebraspe."],
    [("01", "De palavra", "metáfora, comparação, metonímia, catacrese, sinestesia"),
     ("02", "De pensamento", "antítese, paradoxo, hipérbole, eufemismo, ironia, personificação"),
     ("03", "De construção", "elipse, zeugma, pleonasmo, polissíndeto, assíndeto"),
     ("04", "De som", "aliteração, assonância, onomatopeia"),
     ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "Tópico do edital: Figuras de linguagem (Língua Portuguesa)",
    "Base: gramáticas de referência (Bechara; Cunha e Cintra).", 90)

THEORY = [
    exam("Como estudar este material",
         "Bancas como AOCP, FGV e Vunesp cobram a identificação da figura num trecho do texto; o Cebraspe costuma cobrar o **efeito** "
         "(“o emprego da hipérbole enfatiza…”). O segredo é separar figuras **parecidas**: metáfora × comparação, antítese × paradoxo, "
         "eufemismo × ironia, polissíndeto × assíndeto."),

    h2("1. Figuras de palavra"),
    tb(["Figura", "Definição", "Exemplo"], [0.17, 0.43, 0.4], [
        ("Metáfora", "Comparação **implícita**, sem conectivo", "Ele é **uma fera** no tiro."),
        ("Comparação (símile)", "Comparação **explícita**, com conectivo (*como, tal qual, parece*)", "Ele é forte **como um touro**."),
        ("Metonímia", "Troca de um termo por outro com o qual mantém relação real (autor pela obra, continente pelo conteúdo, parte pelo todo, marca pelo produto)", "Li **Machado de Assis**. Bebi **um copo** de água. Há poucos **braços** na lavoura."),
        ("Catacrese", "Metáfora já incorporada à língua, por falta de termo próprio", "**pé** da mesa, **braço** da cadeira, **embarcar** no ônibus"),
        ("Sinestesia", "Mistura de sensações (visão, audição, tato, paladar, olfato)", "Um grito **áspero**. Uma cor **quente**."),
        ("Antonomásia", "Substituição de um nome por qualidade ou apelido conhecido", "**O Poeta dos Escravos** (Castro Alves)."),
    ]),
    trap("Metáfora × comparação",
         "Se há **conectivo comparativo** (*como, tal qual, feito*), é **comparação**. Sem conectivo, é **metáfora**: *O delegado é **uma rocha*** × *O delegado é firme **como** uma rocha*."),

    h2("2. Figuras de pensamento"),
    tb(["Figura", "Definição", "Exemplo"], [0.17, 0.43, 0.4], [
        ("Antítese", "Aproximação de ideias **opostas**", "**Riso** e **choro** se misturavam no velório."),
        ("Paradoxo (oxímoro)", "Ideias opostas atribuídas **ao mesmo ser**, criando contradição aparente", "É dor que desatina sem doer. (Camões)"),
        ("Hipérbole", "**Exagero** intencional", "**Morri de rir**. Já te disse **um milhão de vezes**."),
        ("Eufemismo", "**Suaviza** uma ideia desagradável", "Ele **faltou com a verdade**. **Partiu desta para melhor**."),
        ("Ironia", "Diz o **contrário** do que se pensa, com tom crítico", "Que **bela** atuação: perdeu todos os prazos!"),
        ("Personificação (prosopopeia)", "Atribui características humanas a seres não humanos", "A cidade **dormia**. O vento **gemia**."),
        ("Gradação", "Sequência crescente ou decrescente de ideias", "Andei, corri, **voei**."),
        ("Apóstrofe", "Invocação, chamamento enfático", "**Deus**, ó Deus, onde estás?"),
    ]),
    trap("Antítese × paradoxo",
         "Na **antítese**, os opostos aparecem lado a lado, sem contradição lógica (*riso e choro*). No **paradoxo**, os opostos se fundem num mesmo ser, "
         "gerando contradição aparente (*dor que não dói*; *silêncio ensurdecedor*)."),

    h2("3. Figuras de construção (sintaxe)"),
    tb(["Figura", "Definição", "Exemplo"], [0.17, 0.43, 0.4], [
        ("Elipse", "Omissão de termo facilmente identificável", "Na sala, apenas silêncio. (havia)"),
        ("Zeugma", "Omissão de termo **já citado**", "Eu prefiro café; ele, chá. (prefere)"),
        ("Pleonasmo", "Repetição de ideia: **literário** (para ênfase) ou **vicioso** (erro)", "Vi **com meus próprios olhos** (literário). **Subir para cima** (vicioso)."),
        ("Polissíndeto", "Repetição de conectivos", "**E** chora, **e** grita, **e** corre."),
        ("Assíndeto", "Ausência de conectivos", "Chegou, viu, venceu."),
        ("Anáfora", "Repetição de palavra no início de versos ou frases", "**Tudo** passa, **tudo** muda, **tudo** acaba."),
        ("Hipérbato (inversão)", "Inversão da ordem direta", "Das armas o barulho ouvia-se ao longe."),
        ("Silepse", "Concordância com a **ideia**, não com a forma", "**A gente** fomos (pessoa) · **Vossa Excelência** está **cansado** (gênero)"),
    ]),

    h2("4. Figuras de som"),
    bl("**Aliteração**: repetição de **consoantes** — *O **r**ato **r**oeu a **r**oupa do **r**ei de **R**oma*.",
       "**Assonância**: repetição de **vogais** — *Sou um **a**rm**a**zém de m**á**goas*.",
       "**Onomatopeia**: imitação de sons — *tique-taque, zum-zum, bum*."),

    h2("5. Como as bancas cobram"),
    bl("Identificação: “no trecho X, há metonímia / hipérbole / eufemismo”.",
       "Efeito: “a hipérbole enfatiza a gravidade da situação”.",
       "Distinções: metáfora × comparação; antítese × paradoxo; polissíndeto × assíndeto; elipse × zeugma.",
       "Pleonasmo vicioso como erro em reescritas (*elo de ligação, surpresa inesperada, há anos atrás*)."),
]

QUIZ = quiz([
    ("C", "Em “Aquele agente é uma fera no tiro”, há metáfora.",
     "Comparação implícita, sem conectivo."),
    ("E", "Em “Ele é forte como um touro”, há metáfora.",
     "O conectivo como torna a comparação explícita: é comparação (símile)."),
    ("C", "Em “Li Machado de Assis nas férias”, há metonímia.",
     "O autor está no lugar da obra."),
    ("E", "Em “O pé da mesa quebrou”, há sinestesia.",
     "É catacrese: metáfora incorporada à língua por falta de termo próprio."),
    ("C", "Em “Ouviu-se um grito áspero na madrugada”, há sinestesia.",
     "Mistura audição (grito) e tato (áspero)."),
    ("E", "Em “Morri de rir com a piada”, há eufemismo.",
     "É hipérbole: exagero intencional."),
    ("C", "Em “O depoente faltou com a verdade”, há eufemismo.",
     "Suaviza a ideia de que ele mentiu."),
    ("E", "Em “Que bela atuação: perdeu todos os prazos!”, há paradoxo.",
     "Diz-se o contrário do que se pensa, com tom crítico: ironia."),
    ("C", "No verso camoniano “É dor que desatina sem doer”, há paradoxo.",
     "Atribui-se ao mesmo ser (a dor) uma característica contraditória (não doer)."),
    ("E", "Em “A cidade dormia quando o alarme soou”, há hipérbole.",
     "Atribui-se ação humana à cidade: personificação."),

    ("C", "Em “Riso e choro se misturavam no velório”, há antítese.",
     "Ideias opostas aproximadas, sem contradição lógica."),
    ("E", "A expressão “subir para cima” exemplifica pleonasmo literário, empregado para dar ênfase.",
     "É pleonasmo vicioso: redundância sem valor expressivo."),
    ("C", "Em “Chegou, viu, venceu”, há assíndeto.",
     "As orações estão ligadas sem conectivos."),
    ("E", "Em “E chora, e grita, e corre”, há assíndeto.",
     "A repetição do conectivo e caracteriza o polissíndeto."),
    ("C", "Em “Na sala, apenas silêncio”, há elipse do verbo.",
     "Omite-se havia, facilmente identificável."),
    ("E", "Em “Eu prefiro café; ele, chá”, há anáfora.",
     "Omite-se o verbo já citado (prefere): zeugma."),
    ("C", "Em “O tique-taque do relógio irritava a testemunha”, há onomatopeia.",
     "Tique-taque imita o som do relógio."),
    ("E", "Em “Ele partiu desta para melhor”, há ironia.",
     "A expressão suaviza a ideia de morte: eufemismo."),
    ("C", "Em “Andei, corri, voei”, há gradação.",
     "As ações seguem em sequência crescente de intensidade."),
    ("E", "Em “Bebi um copo de água”, há metáfora.",
     "O continente (copo) está no lugar do conteúdo (água): metonímia."),
], 20)

SOURCES = [GRAM, SRC_A]
