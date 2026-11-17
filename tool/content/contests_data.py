# -*- coding: utf-8 -*-
"""Concursos com edital publicado (modo pós-edital) que já vêm embutidos no app.

Formato igual ao do editor do app (catálogo extra): cada matéria tem peso (1 a 3),
número de questões e a lista de assuntos NA ORDEM DO EDITAL. Um assunto pode ser
'LP-05' (reaproveita o assunto do ciclo básico, com PDFs e progresso) ou
(nome, tamanho P/M/G) para um assunto exclusivo do edital.

Fonte do CFO CBMPE 2026: Edital nº 002/2026 (Portaria Conjunta SAD/SDS nº 300,
DOE-PE de 29/09/2026), Instituto AOCP — Anexo II, cargo 401.
"""

CBMPE26_TEN = {
    'id': 'CBMPE26_TEN',
    'career': 'BM',
    'base': 'BM_CFO',
    'name': 'CFO CBMPE 2026 — 2º Tenente (QOC)',
    'orgao': 'Corpo de Bombeiros Militar de Pernambuco',
    'uf': 'PE',
    'banca': 'Instituto AOCP',
    'examDate': '2027-02-28',
    'editalUrl': 'https://www.institutoaocp.org.br/',
    'vagas': '60',
    'status': 'aberto',
    'notes': ('Prova objetiva com 70 questões de 5 alternativas (Bloco I: 20, Bloco II: 20, Bloco III: 30) e redação '
              'de 15 a 20 linhas (30 pontos, mínimo 9). Exige 30% de cada bloco e do total, sem zerar disciplina. '
              'Requisitos: nível superior em qualquer área, CNH B, 18 a 30 anos. Confira sempre o edital e as retificações.'),
    'subjects': [
        {'id': 'LP', 'weight': 3, 'questions': 5, 'topics': [
            'LP-05', 'LP-15', 'LP-21', 'LP-22',
            'LP-01', 'LP-02', 'LP-03', 'LP-06', 'LP-07', 'LP-13', 'LP-08', 'LP-09', 'LP-10',
            'LP-23', 'LP-16', 'LP-14', 'LP-11', 'LP-12', 'LP-04', 'LP-18', 'LP-19',
            'LP-24']},
        {'id': 'LE', 'weight': 2, 'questions': 5, 'topics': ['LE-01', 'LE-02', 'LE-03', 'LE-04', 'LE-05', 'LE-06', 'LE-07']},
        {'id': 'INFO', 'weight': 2, 'questions': 5, 'topics': [
            'INFO-06', 'INFO-07', 'INFO-10', 'INFO-11', 'INFO-12', 'INFO-13', 'INFO-02',
            ('Windows 11: Prompt de Comando', 'P'), 'INFO-04', 'INFO-05', ('Apresentações (PowerPoint e Impress)', 'P')]},
        {'id': 'EST', 'weight': 2, 'questions': 5, 'topics': [
            'EST-01', 'EST-08', 'EST-06', 'EST-02', 'EST-03', 'EST-04', ('Testes de hipóteses e análise de variância', 'M'), 'EST-07']},
        {'id': 'RLM', 'weight': 2, 'questions': 5, 'topics': [
            'RLM-08', 'RLM-09', 'RLM-10', 'RLM-14', 'RLM-11', 'RLM-12', 'RLM-13',
            ('Equações, inequações e trigonometria', 'M'), ('Geometria analítica: plano cartesiano, retas e circunferências', 'M')]},
        {'id': 'FIS', 'weight': 2, 'questions': 5, 'topics': [
            ('Grandezas físicas, ordem de grandeza e vetores', 'P'), 'FIS-01', 'FIS-03', 'FIS-04', 'FIS-05',
            ('Gravitação e mecânica celeste', 'M'), 'FIS-08', ('Magnetismo e eletromagnetismo', 'M'),
            ('Ondas, óptica e radiação', 'M'), 'FIS-07', ('Termodinâmica', 'M')]},
        {'id': 'QUI', 'weight': 2, 'questions': 5, 'topics': [
            'QUI-01', 'QUI-02', 'QUI-03', 'QUI-04', 'QUI-05', ('Cinética e equilíbrio químico', 'M'),
            ('Oxirredução e eletroquímica', 'M'), 'QUI-06', ('Química aplicada: petróleo, polímeros e siderurgia', 'P'),
            ('Aspectos químicos do fogo e da combustão', 'M'), ('Produtos químicos perigosos', 'P'), ('Química da água', 'P')]},
        {'id': 'BIO', 'weight': 2, 'questions': 5, 'topics': [
            'BIO-02', 'BIO-01', 'BIO-04', ('Biotecnologia', 'P'), ('Evolução e classificação dos seres vivos', 'M'),
            'BIO-06', ('Ecologia e ciências ambientais', 'G'), ('Saúde e qualidade de vida das populações humanas', 'M')]},
        {'id': 'DC', 'weight': 3, 'questions': 8, 'topics': [
            ('Teoria da Constituição: conceito, classificação e estrutura', 'P'), ('Poder constituinte e mutação constitucional', 'P'),
            ('Eficácia e aplicabilidade das normas constitucionais', 'P'), ('Controle de constitucionalidade', 'G'),
            'DC-01', 'DC-02', 'DC-03', 'DC-04', 'DC-05', 'DC-06', 'DC-07', 'DC-08', 'DC-09', 'DC-10', 'DC-11',
            'DC-12', 'DC-13', ('Ordem social', 'M'), ('Constituição do Estado de Pernambuco', 'M'),
            ('ECA, Estatuto da Juventude e Lei Maria da Penha', 'M')]},
        {'id': 'DA', 'weight': 2, 'questions': 7, 'topics': [
            'DA-01', 'DA-02', 'DA-03', 'DA-04', 'DA-06', 'DA-07', 'DA-08', 'DA-09', 'DA-10']},
        {'id': 'INST', 'weight': 3, 'questions': 10, 'topics': [
            ('Código Disciplinar dos Militares de PE (Lei 11.817/00) e regulamento (Decreto 50.014/20)', 'G'),
            ('Estatuto dos Militares de PE (Lei 6.783/74)', 'G'), ('Organização Básica do CBMPE (Lei 15.187/13)', 'M'), 'INST-02']},
        {'id': 'DPM', 'weight': 2, 'questions': 5, 'topics': [
            'DPM-01', 'DPM-02', 'DPM-03', 'DPM-04', 'DPM-05', 'DPM-06', 'DPM-07', 'DPM-08', 'DPM-09', 'DPM-10',
            'DPM-11', 'DPM-12', 'DPM-13']},
    ],
}

CONTESTS = [CBMPE26_TEN]


def to_json(c):
    out = dict(c)
    out['subjects'] = []
    for s in c['subjects']:
        topics = [{'ref': t} if isinstance(t, str) else {'name': t[0], 'size': t[1]} for t in s['topics']]
        out['subjects'].append({'id': s['id'], 'weight': s['weight'], 'questions': s['questions'], 'topics': topics})
    return out
