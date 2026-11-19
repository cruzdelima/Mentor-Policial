# -*- coding: utf-8 -*-
"""Versões dos materiais por banca.

O texto dos módulos é escrito na versão base (Cebraspe). Este arquivo gera as outras:

* **neutro**: para carreiras cuja banca varia por estado (PC, PM, BM, PP, GCM no ciclo básico). Não cita banca
  específica; as questões continuam certo/errado, sem desconto por erro.
* **aocp**: para concursos do Instituto AOCP (CFO CBMPE e CFO PMPE 2026). O texto vem da versão neutra, com as
  seções "como cobra" dirigidas ao AOCP e um quadro da banca no início; nas questões, o Bloco A continua certo/errado
  (treino do conteúdo) e o Bloco B é de múltipla escolha com 5 alternativas, no padrão do AOCP.

Para uma banca nova: crie o perfil em PROFILES, as regras de texto e o arquivo de questões (me_<perfil>_<matéria>.py).
"""
import copy
import importlib
import re
from types import SimpleNamespace

PROFILES = {
    'cebraspe': {'nome': 'Cebraspe', 'quiz': 'estilo Cebraspe'},
    'neutro': {'nome': '', 'quiz': 'questões comentadas'},
    'aocp': {'nome': 'Instituto AOCP', 'quiz': 'certo/errado + padrão Instituto AOCP'},
}

# ------------------------------------------------------------------ regras de texto (ordem importa)
# Cada regra: (regex, substituição na versão neutra, substituição na versão AOCP)
RULES = [
    # quantidades de questões na capa e nas fontes
    (r'20 questões no estilo Cebraspe e gabarito comentado', '20 questões com gabarito comentado',
     '20 questões (10 de certo ou errado e 10 no padrão AOCP) com gabarito comentado'),
    (r'10 questões no estilo Cebraspe com gabarito comentado', '10 questões com gabarito comentado',
     '10 questões (5 de certo ou errado e 5 no padrão AOCP) com gabarito comentado'),
    (r'20 questões no estilo Cebraspe', '20 questões comentadas', '20 questões (10 de certo ou errado e 10 no padrão AOCP)'),
    (r'10 questões no estilo Cebraspe', '10 questões comentadas', '10 questões (5 de certo ou errado e 5 no padrão AOCP)'),
    (r'itens inéditos no estilo Cebraspe', 'itens inéditos', 'itens inéditos; o Bloco B segue o padrão do Instituto AOCP'),
    (r'padrão de cobrança do Cebraspe', 'padrão de cobrança das bancas', 'padrão de cobrança das bancas, em especial o do Instituto AOCP'),
    (r'10 itens certo/errado \+ gabarito comentado', '10 itens + gabarito comentado', '5 itens certo/errado + 5 de múltipla escolha AOCP'),
    (r'20 itens certo/errado \+ gabarito comentado', '20 itens + gabarito comentado', '10 itens certo/errado + 10 de múltipla escolha AOCP'),
    # títulos de seção
    (r'Como o Cebraspe cobra', 'Como as bancas cobram', 'Como o Instituto AOCP cobra'),
    (r'Como as bancas cobram', 'Como as bancas cobram', 'Como o Instituto AOCP cobra'),
    (r'Como o Cebraspe formula os itens', 'Como as bancas formulam as questões', 'Como as bancas formulam as questões'),
    (r'Substituições que o Cebraspe testa', 'Substituições que as bancas testam', 'Substituições que as bancas testam'),
    (r'Método de resolução \(Cebraspe\)', 'Método de resolução', 'Método de resolução'),
    (r'como ler o texto e julgar cada item do Cebraspe', 'como ler o texto e resolver cada questão', 'como ler o texto e resolver cada questão'),
    # regra geral: o Cebraspe → a banca / as provas
    (r'nas provas de interpretação do Cebraspe', 'nas provas de interpretação', 'nas provas de interpretação'),
    (r'nas provas do Cebraspe', 'nas provas', 'nas provas'),
    (r'itens do Cebraspe', 'itens de prova', 'questões de prova'),
    (r'formato preferido do Cebraspe', 'formato preferido das bancas', 'formato preferido das bancas'),
    (r'\bno Cebraspe\b', 'nas provas', 'nas provas'),
    (r'\bpelo Cebraspe\b', 'pelas bancas', 'pelas bancas'),
    (r'\bO Cebraspe\b', 'A banca', 'A banca'),
    (r'\bo Cebraspe\b', 'a banca', 'a banca'),
    (r'\bdo Cebraspe\b', 'das bancas', 'das bancas'),
    (r'\bao Cebraspe\b', 'à banca', 'à banca'),
]

# Trechos que a regra geral não resolve bem (frases sobre o formato certo/errado). Aplicados antes das regras.
OVERRIDES = [
    ('Na dúvida real, **deixe em branco**: no Cebraspe, cada erro anula um acerto.',
     'Na dúvida real, confira a regra da sua banca: no Cebraspe, cada erro anula um acerto (deixe em branco); na múltipla escolha, '
     'o erro não desconta (não deixe em branco).',
     'Na dúvida real, **não deixe em branco**: no Instituto AOCP o erro não desconta. Elimine as alternativas erradas e marque a mais provável.'),
    ('Bancas como AOCP, FGV e Vunesp cobram a identificação da figura num trecho do texto; o Cebraspe costuma cobrar o **efeito**',
     'Bancas de múltipla escolha (AOCP, FGV, Vunesp) cobram a identificação da figura num trecho do texto; o Cebraspe costuma cobrar o **efeito**',
     'O Instituto AOCP cobra a **identificação da figura** num trecho do texto (“no trecho, há…”); outras bancas também cobram o **efeito**'),
]


def _sub_text(s, prof):
    if not isinstance(s, str) or ('Cebraspe' not in s and 'certo/errado' not in s and 'Como as bancas cobram' not in s):
        return s
    for old, neu, aocp in OVERRIDES:
        s = s.replace(old, (neu if prof == 'neutro' else aocp).replace('Cebraspe', '\x00'))
    for rx, neu, aocp in RULES:
        s = re.sub(rx, neu if prof == 'neutro' else aocp, s)
    return s.replace('\x00', 'Cebraspe')


def _walk(x, prof):
    if isinstance(x, str):
        return _sub_text(x, prof)
    if isinstance(x, list):
        return [_walk(i, prof) for i in x]
    if isinstance(x, tuple):
        return tuple(_walk(i, prof) for i in x)
    if isinstance(x, dict):
        return {k: _walk(v, prof) for k, v in x.items()}
    return x


# ------------------------------------------------------------------ quadros do Instituto AOCP por matéria
AOCP_INTRO = {
    'LP': ("Sua banca: Instituto AOCP",
           "Questões de **múltipla escolha com 5 alternativas (A a E)**, sem desconto por erro: **nunca deixe em branco**. Em Português, "
           "quase tudo parte de um **texto-base**: “de acordo com o texto”, “o termo destacado refere-se a”, “assinale a alternativa em que a "
           "reescrita mantém o sentido e a correção”. São comuns os enunciados “assinale a alternativa **incorreta**” e os de assertivas "
           "(“analise as assertivas I, II e III e assinale a alternativa correta”). Leia o comando duas vezes antes de olhar as alternativas."),
    'DC': ("Sua banca: Instituto AOCP",
           "Questões de **múltipla escolha com 5 alternativas (A a E)**, sem desconto por erro: **nunca deixe em branco**. Em Direito "
           "Constitucional, o AOCP cobra sobretudo a **letra da Constituição**: as alternativas reproduzem artigos com **uma palavra trocada** "
           "(prazo, quórum, competência, “salvo”/“inclusive”). É frequente o comando “**de acordo com a Constituição Federal**, assinale a "
           "alternativa correta” e também “assinale a alternativa **incorreta**”. Jurisprudência aparece menos que no Cebraspe, mas súmulas "
           "vinculantes conhecidas caem."),
    'INFO': ("Sua banca: Instituto AOCP",
             "Questões de **múltipla escolha com 5 alternativas (A a E)**, sem desconto por erro: **nunca deixe em branco**. Em Informática, "
             "o AOCP cobra **conceitos e definições** (“assinale a alternativa que apresenta o conceito de…”) e situações práticas curtas. "
             "Associe cada termo à sua definição exata: as alternativas erradas costumam trazer a definição de um termo vizinho."),
    'RLM': ("Sua banca: Instituto AOCP",
            "Questões de **múltipla escolha com 5 alternativas (A a E)**, sem desconto por erro: **nunca deixe em branco**. Em Raciocínio "
            "Lógico e Matemática, o AOCP cobra sobretudo **problemas com contas** (porcentagem, proporção, combinatória, probabilidade, "
            "funções e geometria) e, na lógica, **equivalências e negações** (“assinale a alternativa que apresenta a negação de...”). "
            "As alternativas erradas costumam trazer o resultado de um **erro comum** de cálculo."),
    'CONT': ("Sua banca: Instituto AOCP",
             "Questões de **múltipla escolha com 5 alternativas (A a E)**, sem desconto por erro: **nunca deixe em branco**. Em Contabilidade, "
             "o AOCP alterna conceitos e pequenos cálculos; confira cada alternativa contra a definição da norma."),
}

AOCP_HOW = {
    'LP': ["Cada questão tem **5 alternativas** e só uma resposta. Desconfie de alternativas com palavras absolutas (“sempre”, “nunca”, “apenas”).",
           "Nas questões de **reescrita**, teste as cinco: a correta mantém **sentido e correção**; as erradas mudam o sentido ou criam erro gramatical.",
           "No comando “assinale a alternativa **incorreta**”, marque cada alternativa com C ou E na margem: a resposta é a única E.",
           "Com assertivas I, II e III, julgue uma por uma e só então procure a alternativa que corresponde ao resultado."],
    'DC': ["As alternativas copiam o texto da Constituição com **uma palavra trocada**: prazo (dia × noite, 2 × 3 anos), quórum (maioria absoluta × 2/3), "
           "competência (Câmara × Senado) ou expressão de exceção (“salvo” × “inclusive”).",
           "No comando “assinale a alternativa **incorreta**”, marque C ou E em cada alternativa: a resposta é a única errada.",
           "Quando duas alternativas parecem certas, uma delas extrapola o texto (“sempre”, “em qualquer hipótese”). Fique com a mais fiel à letra da lei.",
           "Sem desconto por erro: elimine o que souber e marque a mais provável."],
    'INFO': ["Cada alternativa costuma trazer a definição de um termo diferente: identifique o termo pedido e procure a definição exata.",
             "Sem desconto por erro: elimine as alternativas absurdas e marque a mais provável."],
    'RLM': ["Faça a conta antes de olhar as alternativas: as erradas trazem o resultado de erros comuns (somar porcentagens, usar arranjo "
            "no lugar de combinação, esquecer o C(n, k) da probabilidade).",
            "Em lógica, simbolize a frase do enunciado e cada alternativa; a pegadinha preferida é a **recíproca** no lugar da contrapositiva.",
            "Quando a conta é longa, **teste as alternativas** no enunciado: muitas vezes é mais rápido.",
            "Sem desconto por erro: elimine o que souber e marque a mais provável."],
    'CONT': ["Refaça os cálculos com calma: as alternativas erradas trazem os resultados de erros comuns.",
             "Sem desconto por erro: nunca deixe em branco."],
}


def _add_aocp_blocks(theory, subject, has_how):
    """Insere o quadro do AOCP no início e as dicas na seção 'Como o Instituto AOCP cobra' (ou ao final)."""
    out = list(theory)
    intro = AOCP_INTRO.get(subject)
    if intro:
        pos = 1 if out and out[0].get('t') == 'callout' else 0
        out.insert(pos, {'t': 'callout', 'style': 'key', 'title': intro[0], 'text': intro[1]})
    how = AOCP_HOW.get(subject)
    if how:
        for i, b in enumerate(out):
            if b.get('t') == 'h2' and 'Instituto AOCP' in b.get('text', ''):
                out.insert(i + 1, {'t': 'bullets', 'items': how})
                break
        else:
            if has_how:
                out += [{'t': 'h2', 'text': 'Como o Instituto AOCP cobra'}, {'t': 'bullets', 'items': how}]
    return out


# ------------------------------------------------------------------ questões
INSTR_NEUTRO_20 = ("Julgue os itens a seguir como certos ou errados. São 20 itens: o Bloco A treina o conteúdo; o Bloco B segue o estilo "
                   "de prova. Se a sua banca for o Cebraspe, lembre que lá cada erro anula um acerto.")
INSTR_NEUTRO_10 = "Julgue os itens a seguir como certos ou errados. Se a sua banca for o Cebraspe, lembre que lá cada erro anula um acerto."
INSTR_AOCP = ("O Bloco A treina o conteúdo com itens de certo ou errado. O Bloco B segue o padrão do Instituto AOCP: múltipla escolha "
              "com 5 alternativas e uma única resposta. Não há desconto por erro: não deixe questões em branco.")
GA_AOCP = "Bloco A · treino do conteúdo (certo ou errado)"
GB_AOCP = "Bloco B · padrão Instituto AOCP (múltipla escolha)"


def me_items(items, start, group):
    """items: lista de (letra, enunciado, [5 alternativas], comentário[, texto de apoio])."""
    qs = []
    for i, it in enumerate(items, start=start):
        ans, text, opts, comment = it[0], it[1], it[2], it[3]
        assert ans in 'ABCDE' and len(opts) == 5, f'questão {i}: gabarito {ans} / {len(opts)} alternativas'
        q = {'id': f'm{i}', 'answer': ans, 'text': text, 'options': list(opts), 'comment': f'**Gabarito: {ans}.** ' + comment, 'group': group}
        if len(it) > 4:
            q['context'] = it[4]
        qs.append(q)
    return qs


def _quiz_neutro(quiz):
    q = copy.deepcopy(quiz)
    n = len(q['questions'])
    q['banca'] = PROFILES['neutro']['quiz']
    q['instructions'] = INSTR_NEUTRO_20 if n == 20 else INSTR_NEUTRO_10
    q['penalty'] = False
    for x in q['questions']:
        if x.get('group', '').startswith('Bloco B'):
            x['group'] = 'Bloco B · estilo de prova'
    return q


def _quiz_aocp(quiz, me):
    base = copy.deepcopy(quiz['questions'])
    n = len(base)
    keep = 10 if n == 20 else 5
    a = []
    for x in base[:keep]:
        x['group'] = GA_AOCP
        a.append(x)
    b = me_items(me, keep + 1, GB_AOCP)
    assert len(b) == keep, f'Bloco B do AOCP precisa de {keep} questões (tem {len(b)})'
    return {'style': 'MISTO', 'banca': PROFILES['aocp']['quiz'], 'instructions': INSTR_AOCP, 'penalty': False, 'questions': a + b}


def _me_for(module_name, subject):
    try:
        mod = importlib.import_module(f'me_aocp_{subject.lower()}')
    except ModuleNotFoundError:
        return None
    return getattr(mod, 'ME', {}).get(module_name)


def variant(C, prof):
    """Gera a versão `prof` ('neutro' ou 'aocp') do módulo C. Retorna None se a versão não puder ser gerada."""
    name = C.__name__
    subject = C.MATERIAL['subjectId']
    me = None
    if prof == 'aocp':
        me = _me_for(name, subject)
        if me is None:
            return None
    M = _walk(copy.deepcopy(C.MATERIAL), prof)
    folder = M['folder']
    M['pdf'] = f'{folder}.{prof}.pdf'
    M['outName'] = M['outName'].replace('.pdf', f'_{prof.upper()}.pdf')
    theory = _walk(copy.deepcopy(C.THEORY), prof)
    summary = _walk(copy.deepcopy(getattr(C, 'SUMMARY', None)), prof)
    if prof == 'aocp':
        has_how = any(b.get('t') == 'h2' and 'cobra' in b.get('text', '').lower() for b in C.THEORY)
        theory = _add_aocp_blocks(theory, subject, has_how=False)
        if not has_how and C.MATERIAL['kind'] == 'aprofundado':
            theory += [{'t': 'h2', 'text': 'Como o Instituto AOCP cobra'}, {'t': 'bullets', 'items': AOCP_HOW.get(subject, [])}]
        quiz = _quiz_aocp(C.QUIZ, me)
    else:
        quiz = _quiz_neutro(C.QUIZ)
    return SimpleNamespace(__name__=f'{name}[{prof}]', MATERIAL=M, THEORY=theory, SUMMARY=summary,
                           MINDMAP=_walk(copy.deepcopy(getattr(C, 'MINDMAP', None)), prof), QUIZ=quiz,
                           SOURCES=_walk(copy.deepcopy(C.SOURCES), prof))
