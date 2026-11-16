# Gera assets/catalog/catalog.json a partir do mesmo cadastro usado na planilha.
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catalog_data import CAREERS, SUBJECTS, TOPICS, LEI_SECA, NEON, TEORIA, MINQ, PARAMS

CARGOS = {
    'PF':  [('PF_AG', 'Agente de Polícia Federal'), ('PF_ES', 'Escrivão de Polícia Federal'), ('PF_PAP', 'Papiloscopista Policial Federal')],
    'PRF': [('PRF', 'Policial Rodoviário Federal')],
    'PPF': [('PPF', 'Policial Penal Federal')],
    'PC':  [('PC_AG', 'Agente / Investigador / Inspetor'), ('PC_ES', 'Escrivão de Polícia Civil')],
    'PM':  [('PM_SD', 'Soldado')],
    'BM':  [('BM_SD', 'Soldado Bombeiro')],
    'PP':  [('PP', 'Policial Penal')],
    'GCM': [('GCM', 'Guarda Civil Municipal')],
}
NAMES = {'PF': 'Polícia Federal', 'PRF': 'Polícia Rodoviária Federal', 'PPF': 'Polícia Penal Federal', 'PC': 'Polícia Civil',
         'PM': 'Polícia Militar', 'BM': 'Corpo de Bombeiros Militar', 'PP': 'Polícia Penal Estadual', 'GCM': 'Guarda Civil Municipal'}
EXTRA_SUBJ = [
    ('ARQ', 'Arquivologia', 'FDE68A'),
    ('QUI', 'Química', '86EFAC'),
    ('BIO', 'Biologia', 'F0ABFC'),
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
}
base_w = {s[0]: dict(zip([c[0] for c in CAREERS], s[4])) for s in SUBJECTS}
for sid, _, _ in EXTRA_SUBJ:
    base_w[sid] = {c[0]: 0 for c in CAREERS}

def weights_for(option, career):
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
    topics.append({'id': f'{sig}-{counter[sig]:02d}', 'subject': sig, 'n': counter[sig], 'name': name, 'size': size,
                   'scope': scope.split() if scope else []})
for sid, items in EXTRA_TOPICS.items():
    for k, (name, size) in enumerate(items, start=1):
        topics.append({'id': f'{sid}-{k:02d}', 'subject': sid, 'n': k, 'name': name, 'size': size, 'scope': []})

catalog = {
    'version': '2026.11.1',
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
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'assets', 'catalog', 'catalog.json')
json.dump(catalog, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('careers', len(careers), 'options', len(option_weights), 'subjects', len(subjects), 'topics', len(topics))
print([t for t in topics if t['id'] == 'INFO-12'])
