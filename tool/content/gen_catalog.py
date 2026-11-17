# Gera assets/catalog/catalog.json a partir do mesmo cadastro usado na planilha.
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catalog_data import CAREERS, SUBJECTS, TOPICS, LEI_SECA, NEON, TEORIA, MINQ, PARAMS
from contests_data import CONTESTS, to_json as contest_json

CARGOS = {
    'PF':  [('PF_AG', 'Agente de Polícia Federal'), ('PF_ES', 'Escrivão de Polícia Federal'), ('PF_PAP', 'Papiloscopista Policial Federal')],
    'PRF': [('PRF', 'Policial Rodoviário Federal')],
    'PPF': [('PPF', 'Policial Penal Federal')],
    'PC':  [('PC_AG', 'Agente / Investigador / Inspetor'), ('PC_ES', 'Escrivão de Polícia Civil')],
    'PM':  [('PM_SD', 'Soldado'), ('PM_CFO', 'Oficial — CFO (Curso de Formação de Oficiais)')],
    'BM':  [('BM_SD', 'Soldado Bombeiro'), ('BM_CFO', 'Oficial — CFO Bombeiro (Curso de Formação de Oficiais)')],
    'PP':  [('PP', 'Policial Penal')],
    'GCM': [('GCM', 'Guarda Civil Municipal')],
}
NAMES = {'PF': 'Polícia Federal', 'PRF': 'Polícia Rodoviária Federal', 'PPF': 'Polícia Penal Federal', 'PC': 'Polícia Civil',
         'PM': 'Polícia Militar', 'BM': 'Corpo de Bombeiros Militar', 'PP': 'Polícia Penal Estadual', 'GCM': 'Guarda Civil Municipal'}
EXTRA_SUBJ = [
    ('ARQ', 'Arquivologia', 'FDE68A'),
    ('QUI', 'Química', '86EFAC'),
    ('BIO', 'Biologia', 'F0ABFC'),
    ('DPM', 'Direito Penal Militar', 'FCA5A5'),
    ('DPPM', 'Direito Processual Penal Militar', 'D8B4FE'),
    ('LE', 'Língua Estrangeira (inglês ou espanhol)', '7DD3FC'),
]
EXTRA_TOPICS = {
    'ARQ': [('Conceitos fundamentais de arquivologia', 'P'), ('Gestão de documentos', 'M'),
            ('Protocolo: recebimento, registro, tramitação e expedição', 'M'), ('Classificação de documentos de arquivo', 'M'),
            ('Arquivamento e ordenação de documentos', 'M'), ('Tabela de temporalidade e avaliação de documentos', 'M'),
            ('Acondicionamento, armazenamento e preservação', 'P'), ('Documentos digitais e gestão eletrônica', 'M')],
    'QUI': [('Estrutura atômica e tabela periódica', 'M'), ('Ligações químicas e geometria molecular', 'M'),
            ('Funções inorgânicas', 'M'), ('Reações químicas e estequiometria', 'G'), ('Soluções e concentrações', 'M'),
            ('Química orgânica: cadeias e funções', 'M')],
    'BIO': [('Citologia', 'M'), ('Bioquímica: proteínas, lipídios e ácidos nucleicos', 'M'), ('Genética', 'G'),
            ('Histologia', 'M'), ('Pele e anexos (base da papiloscopia)', 'P'), ('Fisiologia humana', 'G')],
    'DPM': [('Aplicação da lei penal militar', 'M'), ('Crime militar: conceito, art. 9º do CPM e classificação', 'G'),
            ('Imputabilidade penal', 'P'), ('Concurso de agentes', 'P'), ('Penas: espécies e aplicação', 'M'),
            ('Medidas de segurança', 'P'), ('Ação penal e extinção da punibilidade', 'M'),
            ('Crimes contra a autoridade e a disciplina militar', 'M'), ('Crimes contra o serviço e o dever militar', 'M'),
            ('Crimes contra a pessoa e o patrimônio no CPM', 'M'), ('Crimes contra a Administração Militar', 'M'),
            ('Crimes militares em tempo de guerra', 'P'), ('Súmulas e jurisprudência dos tribunais superiores', 'P')],
    'DPPM': [('Polícia judiciária militar e inquérito policial militar', 'G'), ('Ação penal militar', 'M'),
             ('Justiça Militar: organização e competência', 'M'), ('Prisão em flagrante, preventiva e menagem', 'M'),
             ('Processos especiais e recursos', 'P')],
    'LE':  [('Leitura e compreensão de textos', 'G'), ('Vocabulário, sinônimos, antônimos e falsos cognatos', 'M'),
            ('Classes de palavras: substantivos, adjetivos, artigos, pronomes e advérbios', 'M'),
            ('Tempos e modos verbais; verbos regulares e irregulares', 'M'),
            ('Verbos modais, voz passiva e question tags (inglês)', 'M'),
            ('Preposições, conjunções e orações condicionais e relativas', 'M'),
            ('Divergências entre português e espanhol (espanhol)', 'P')],
}

# Pesos completos dos cargos de oficial (ciclo básico pré-edital), a partir dos editais recentes de CFO.
CFO_WEIGHTS = {
    'PM_CFO': {'LP': 3, 'DC': 3, 'DA': 3, 'RLM': 2, 'DP': 2, 'DPP': 2, 'LPE': 2, 'DH': 2, 'DPM': 2, 'INST': 2,
               'INFO': 1, 'DPPM': 1, 'GER': 1},
    'BM_CFO': {'LP': 3, 'RLM': 3, 'FIS': 3, 'QUI': 2, 'BIO': 2, 'INFO': 2, 'DC': 2, 'DA': 2, 'INST': 2,
               'EST': 1, 'DPM': 1, 'GER': 1, 'LE': 1, 'DH': 1},
}
# Ajustes de escopo: assuntos que passam a valer (ou deixam de valer) para cargos específicos.
SCOPE_ADD = {'DC-09': ['PM_CFO', 'BM_CFO'], 'DC-10': ['PM_CFO', 'BM_CFO'], 'DC-11': ['PM_CFO', 'BM_CFO'],
             'DA-12': ['PM_CFO', 'BM_CFO'], 'DA-13': ['PM_CFO'], 'DP-13': ['PM_CFO'], 'DPP-10': ['PM_CFO'],
             'LPE-13': ['PM_CFO']}
SCOPE_SET = {'INST-07': ['PM_SD', 'BM_SD']}  # 'Direito Penal Militar (noções)': o oficial estuda a matéria inteira
base_w = {s[0]: dict(zip([c[0] for c in CAREERS], s[4])) for s in SUBJECTS}
for sid, _, _ in EXTRA_SUBJ:
    base_w[sid] = {c[0]: 0 for c in CAREERS}

def weights_for(option, career):
    if option in CFO_WEIGHTS:
        return {sid: CFO_WEIGHTS[option].get(sid, 0) for sid in base_w}
    w = {sid: base_w[sid][career] for sid in base_w}
    if option == 'PF_ES':
        w['CONT'] = 2; w['ARQ'] = 2
    if option == 'PF_PAP':
        w['CONT'] = 0; w['FIS'] = 2; w['QUI'] = 2; w['BIO'] = 2
    if option == 'PC_ES':
        w['ARQ'] = 1
    return w

careers = []
option_weights = {}
for code, nome, esf, esc, banca, disc, obs, marca in CAREERS:
    careers.append({'code': code, 'name': NAMES[code], 'esfera': esf, 'escolaridade': esc, 'banca': banca,
                    'discursiva': disc == 'Sim', 'observacao': obs, 'marca': marca,
                    'cargos': [{'id': i, 'name': n} for i, n in CARGOS[code]]})
    for i, _ in CARGOS[code]:
        option_weights[i] = weights_for(i, code)

subjects = []
for sid, nome, light, strong, _ in SUBJECTS:
    subjects.append({'id': sid, 'name': nome, 'color': NEON[sid], 'weights': {o: option_weights[o][sid] for o in option_weights}})
for sid, nome, color in EXTRA_SUBJ:
    subjects.append({'id': sid, 'name': nome, 'color': color, 'weights': {o: option_weights[o][sid] for o in option_weights}})

topics = []
counter = {}
for sig, name, size, scope in TOPICS:
    counter[sig] = counter.get(sig, 0) + 1
    tid = f'{sig}-{counter[sig]:02d}'
    sc = SCOPE_SET.get(tid, (scope.split() if scope else []) + SCOPE_ADD.get(tid, []))
    topics.append({'id': tid, 'subject': sig, 'n': counter[sig], 'name': name, 'size': size, 'scope': sc})
for sid, items in EXTRA_TOPICS.items():
    for k, (name, size) in enumerate(items, start=1):
        topics.append({'id': f'{sid}-{k:02d}', 'subject': sid, 'n': k, 'name': name, 'size': size, 'scope': []})

contests = [contest_json(c) for c in CONTESTS]
known = {t['id'] for t in topics}
sids = {x['id'] for x in subjects}
for c in contests:
    assert c['base'] in option_weights, c['base']
    for sj in c['subjects']:
        assert sj['id'] in sids, sj['id']
        for t in sj['topics']:
            if 'ref' in t:
                assert t['ref'] in known, t['ref']
                assert t['ref'].split('-')[0] == sj['id'], (t['ref'], sj['id'])

catalog = {
    'version': '2026.11.2',
    'careers': careers,
    'subjects': subjects,
    'topics': topics,
    'leiSeca': LEI_SECA,
    'params': {
        'theoryMinutes': {k: list(v) for k, v in TEORIA.items()},
        'minutesPerQuestion': list(MINQ),
        'questions': {'P': PARAMS['qP'], 'M': PARAMS['qM'], 'G': PARAMS['qG']},
        'reviewShare': PARAMS['rev'], 'weight2AfterHours': PARAMS['h2'], 'weight1AfterHours': PARAMS['h3'],
        'simuladoFromWeek': PARAMS['sim_start'], 'simuladoEveryWeeks': PARAMS['sim_every'],
        'discursivaFromWeek': PARAMS['disc_start'], 'fullSimuladoMinHours': PARAMS['sim_full_h'],
    },
    'levels': ['Iniciante (sem base)', 'Intermediário', 'Avançado'],
    'contests': contests,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'assets', 'catalog', 'catalog.json')
json.dump(catalog, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('careers', len(careers), 'options', len(option_weights), 'subjects', len(subjects), 'topics', len(topics))
print('contests', [(c['id'], sum(len(x['topics']) for x in c['subjects'])) for c in contests])
