/// Catálogo extra: o que o dono e os administradores acrescentam pelo editor do app
/// (novas áreas, cargos do ciclo básico, matérias e concursos pós-edital).
///
/// O documento é um JSON simples, guardado no Supabase (tabela catalog_docs) e em
/// cache no computador do aluno. Ele é aplicado POR CIMA do catálogo embutido:
/// itens com o mesmo id substituem os embutidos; ids em "hidden" somem da lista.
///
/// {
///   "areas":    [{code, name, esfera, escolaridade, banca, discursiva, observacao, marca}],
///   "subjects": [{id, name, color}],
///   "cargos":   [{id, career, name, weights: {LP: 3, ...}}],
///   "contests": [{id, career, base, name, orgao, uf, banca, examDate, editalUrl, vagas, status, notes,
///                 subjects: [{id, weight, questions, topics: [{ref: 'LP-05'} | {id?, name, size}]}]}],
///   "hidden":   ["PM_SD", "CBMPE26_TEN", ...],
///   "review":   {"lp-verbos-02": true, ...}   // materiais revisados pelo dono (true = liberado aos alunos)
/// }
library;

import 'dart:convert';

const kEsferas = ['Federal', 'Estadual', 'Municipal'];

/// Situações possíveis de um concurso pós-edital.
const kContestStatus = {
  'aberto': 'Inscrições abertas',
  'publicado': 'Edital publicado',
  'andamento': 'Em andamento',
  'encerrado': 'Encerrado',
};

Map<String, dynamic> emptyExtras() => {
      'areas': <dynamic>[],
      'subjects': <dynamic>[],
      'cargos': <dynamic>[],
      'contests': <dynamic>[],
      'hidden': <dynamic>[],
      'review': <String, dynamic>{},
    };

/// Cópia profunda (o editor trabalha numa cópia e só aplica ao salvar).
Map<String, dynamic> cloneJson(Map<String, dynamic> m) => jsonDecode(jsonEncode(m)) as Map<String, dynamic>;

/// Garante que todas as listas existem e descarta lixo (documento vindo da rede).
Map<String, dynamic> normalizeExtras(Object? raw) {
  final out = emptyExtras();
  if (raw is! Map) return out;
  for (final k in out.keys) {
    final v = raw[k];
    if (k == 'review') {
      if (v is Map) out[k] = {for (final e in v.entries) if (e.key is String && e.value is bool) e.key as String: e.value};
    } else if (v is List) {
      out[k] = [for (final x in v) if (x is Map || (k == 'hidden' && x is String)) x];
    }
  }
  return cloneJson(out);
}

bool extrasIsEmpty(Map<String, dynamic> e) => e.values.every((v) => (v is List && v.isEmpty) || (v is Map && v.isEmpty));

/// Decisões de revisão de materiais publicadas pelo dono (id → liberado).
Map<String, bool> reviewOf(Map<String, dynamic> extras) => {
      for (final e in ((extras['review'] as Map?) ?? const {}).entries)
        if (e.key is String && e.value is bool) e.key as String: e.value as bool,
    };

/// Transforma um nome em pedaço de id estável ("Ordem social" → "ordem-social").
String slug(String s) {
  const from = 'áàâãäéèêëíìîïóòôõöúùûüçñ';
  const to = 'aaaaaeeeeiiiiooooouuuucn';
  final b = StringBuffer();
  for (final ch in s.toLowerCase().split('')) {
    final i = from.indexOf(ch);
    final c = i >= 0 ? to[i] : ch;
    if (RegExp(r'[a-z0-9]').hasMatch(c)) {
      b.write(c);
    } else if (b.isNotEmpty && !b.toString().endsWith('-')) {
      b.write('-');
    }
  }
  var r = b.toString();
  if (r.length > 48) r = r.substring(0, 48);
  while (r.endsWith('-')) {
    r = r.substring(0, r.length - 1);
  }
  return r;
}

/// Gera um id curto e único a partir de um nome ("CFO PMPE 2027" → "CFO_PMPE_2027").
String makeId(String name, Iterable<String> taken) {
  var base = slug(name).toUpperCase().replaceAll('-', '_');
  if (base.isEmpty) base = 'ITEM';
  if (base.length > 24) base = base.substring(0, 24);
  final used = taken.toSet();
  var id = base;
  var n = 2;
  while (used.contains(id)) {
    id = '${base}_${n++}';
  }
  return id;
}

/// Aplica [extras] sobre o JSON do catálogo [base] (não altera os originais).
/// Erros em itens isolados são ignorados: um item mal preenchido nunca derruba o app.
Map<String, dynamic> applyExtras(Map<String, dynamic> base, Map<String, dynamic> extras) {
  final j = cloneJson(base);
  final e = normalizeExtras(extras);
  final careers = (j['careers'] as List).cast<Map<String, dynamic>>();
  final subjects = (j['subjects'] as List).cast<Map<String, dynamic>>();
  final topics = (j['topics'] as List).cast<Map<String, dynamic>>();
  final topicIds = {for (final t in topics) t['id'] as String};

  Map<String, dynamic>? careerOf(String? code) {
    for (final c in careers) {
      if (c['code'] == code) return c;
    }
    return null;
  }

  Map<String, dynamic>? subjectOf(String? id) {
    for (final s in subjects) {
      if (s['id'] == id) return s;
    }
    return null;
  }

  void removeOption(String id) {
    for (final c in careers) {
      (c['cargos'] as List).removeWhere((x) => (x as Map)['id'] == id);
    }
    for (final s in subjects) {
      (s['weights'] as Map).remove(id);
    }
  }

  void putOption(Map<String, dynamic> career, Map<String, dynamic> cargo) {
    removeOption(cargo['id'] as String);
    (career['cargos'] as List).add(cargo);
  }

  // ------------------------------------------------ áreas (carreiras)
  for (final a in e['areas'] as List) {
    try {
      final code = '${a['code'] ?? ''}'.trim();
      if (code.isEmpty) continue;
      final esfera = kEsferas.contains(a['esfera']) ? a['esfera'] as String : 'Estadual';
      final data = <String, dynamic>{
        'code': code,
        'name': '${a['name'] ?? code}',
        'esfera': esfera,
        'escolaridade': '${a['escolaridade'] ?? ''}',
        'banca': '${a['banca'] ?? ''}',
        'discursiva': a['discursiva'] == true,
        'observacao': '${a['observacao'] ?? ''}',
        'marca': '${a['marca'] ?? ''}',
      };
      final old = careerOf(code);
      if (old == null) {
        careers.add({...data, 'cargos': <dynamic>[]});
      } else {
        old.addAll(data);
      }
    } catch (_) {}
  }

  // ------------------------------------------------ matérias
  for (final s in e['subjects'] as List) {
    try {
      final id = '${s['id'] ?? ''}'.trim();
      if (id.isEmpty) continue;
      final color = RegExp(r'^[0-9A-Fa-f]{6}$').hasMatch('${s['color']}') ? '${s['color']}' : 'CBD5E1';
      final old = subjectOf(id);
      if (old == null) {
        subjects.add({'id': id, 'name': '${s['name'] ?? id}', 'color': color, 'weights': <String, dynamic>{}});
      } else {
        old['name'] = '${s['name'] ?? old['name']}';
        old['color'] = color;
      }
    } catch (_) {}
  }

  // ------------------------------------------------ cargos do ciclo básico
  for (final c in e['cargos'] as List) {
    try {
      final id = '${c['id'] ?? ''}'.trim();
      final career = careerOf(c['career'] as String?);
      if (id.isEmpty || career == null) continue;
      putOption(career, {'id': id, 'name': '${c['name'] ?? id}'});
      final w = (c['weights'] as Map?) ?? const {};
      for (final s in subjects) {
        final v = (w[s['id']] as num?)?.toInt() ?? 0;
        (s['weights'] as Map)[id] = v.clamp(0, 3);
      }
    } catch (_) {}
  }

  // ------------------------------------------------ concursos (pós-edital)
  final contests = [...((j['contests'] as List?) ?? const []), ...(e['contests'] as List)];
  for (final c in contests.cast<Map>()) {
    try {
      final id = '${c['id'] ?? ''}'.trim();
      final career = careerOf(c['career'] as String?);
      if (id.isEmpty || career == null) continue;
      final order = <String>[];
      final questions = <String, int>{};
      final weights = <String, int>{};
      final usedIds = <String>{};
      for (final sj in (c['subjects'] as List? ?? const []).cast<Map>()) {
        final sid = '${sj['id'] ?? ''}';
        if (subjectOf(sid) == null) continue;
        weights[sid] = ((sj['weight'] as num?)?.toInt() ?? 2).clamp(1, 3);
        questions[sid] = (sj['questions'] as num?)?.toInt() ?? 0;
        var n = 0;
        for (final t in (sj['topics'] as List? ?? const []).cast<Map>()) {
          final ref = t['ref'] as String?;
          if (ref != null) {
            if (topicIds.contains(ref) && !order.contains(ref)) order.add(ref);
            continue;
          }
          final name = '${t['name'] ?? ''}'.trim();
          if (name.isEmpty) continue;
          var tid = (t['id'] as String?) ?? '$id:${slug(name)}';
          var k = 2;
          final root = tid;
          while (usedIds.contains(tid)) {
            tid = '$root-${k++}';
          }
          usedIds.add(tid);
          n++;
          final size = const ['P', 'M', 'G'].contains(t['size']) ? t['size'] as String : 'M';
          topics.removeWhere((x) => x['id'] == tid);
          topics.add({'id': tid, 'subject': sid, 'n': n, 'name': name, 'size': size, 'scope': [id], 'contest': id});
          topicIds.add(tid);
          order.add(tid);
        }
      }
      if (order.isEmpty) continue;
      putOption(career, {
        'id': id,
        'name': '${c['name'] ?? id}',
        'contest': {
          'base': '${c['base'] ?? ''}',
          'orgao': '${c['orgao'] ?? ''}',
          'uf': '${c['uf'] ?? ''}',
          'banca': '${c['banca'] ?? ''}',
          'examDate': '${c['examDate'] ?? ''}',
          'editalUrl': '${c['editalUrl'] ?? ''}',
          'vagas': '${c['vagas'] ?? ''}',
          'status': '${c['status'] ?? 'publicado'}',
          'notes': '${c['notes'] ?? ''}',
          'topicIds': order,
          'questions': questions,
        },
      });
      for (final s in subjects) {
        (s['weights'] as Map)[id] = weights[s['id']] ?? 0;
      }
    } catch (_) {}
  }

  // ------------------------------------------------ ocultos
  for (final h in (e['hidden'] as List).cast<String>()) {
    removeOption(h);
    careers.removeWhere((c) => c['code'] == h);
  }
  j.remove('contests');
  return j;
}
