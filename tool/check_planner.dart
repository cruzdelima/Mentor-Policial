// Verificação do motor de metas contra a planilha (dart run tool/check_planner.dart <expected.json>).
// Uso interno de desenvolvimento: não faz parte do app.
import 'dart:convert';
import 'dart:io';

import 'package:mentor_policial/core/catalog.dart';
import 'package:mentor_policial/core/dates.dart';
import 'package:mentor_policial/core/models.dart';
import 'package:mentor_policial/core/planner.dart';
import 'package:mentor_policial/core/stats.dart';

void main(List<String> args) {
  final cat = Catalog.fromJson(jsonDecode(File('assets/catalog/catalog.json').readAsStringSync()) as Map<String, dynamic>);
  final profile = Profile(
    name: 'Teste',
    esfera: 'Federal',
    careerCode: 'PF',
    optionId: 'PF_AG',
    hoursPerDay: 3,
    studyWeekdays: [1, 2, 3, 4, 5, 6],
    reviewWeekday: 6,
    level: 0,
    startDate: DateTime(2026, 11, 16),
  );
  final data = UserData(profile: profile, anchorDate: profile.startDate);
  final sw = Stopwatch()..start();
  final trail = Planner.buildTrail(cat, profile, data.overrides);
  final sched = Schedule(catalog: cat, trail: trail, profile: profile, data: data, today: DateTime(2026, 11, 16));
  print('trilha: ${trail.units.length} missões, ${trail.totalMinutes} min, fim ${fmtDate(sched.endDate!)}, ${sw.elapsedMilliseconds} ms');

  var failures = 0;
  if (args.isNotEmpty) {
    final exp = jsonDecode(File(args.first).readAsStringSync()) as Map<String, dynamic>;
    final rows = exp['trail'] as List;
    if (rows.length != trail.units.length) {
      print('✖ nº de missões: planilha ${rows.length}, app ${trail.units.length}');
      failures++;
    }
    for (var i = 0; i < rows.length && i < trail.units.length; i++) {
      final r = rows[i] as List;
      final u = trail.units[i];
      final phase = u.isTheory ? 'Teoria' : 'Questões';
      if (r[0] != u.subject.id || r[1] != u.topic.name || r[2] != phase || (r[3] as num).toInt() != u.minutes || (r[4] as num).toInt() != u.start) {
        if (failures < 8) print('✖ #${i + 1}: planilha $r · app [${u.subject.id}, ${u.topic.name}, $phase, ${u.minutes}, ${u.start}]');
        failures++;
      }
    }
    final days = exp['days'] as List;
    for (final dr in days) {
      final row = dr as List;
      final date = parseIso(row[0] as String);
      final p = sched.dayPlan(date);
      final sheetMissions = [for (var k = 2; k < 8; k++) row[k] as String].where((s) => s.startsWith('#')).map((s) => s.split(' ').first).toList();
      if (p.isStudy) {
        final app = [
          for (final u in p.units) '#${u.seq}',
          if (p.continuation != null) '#${p.continuation!.seq}',
        ];
        final sheet = row[2] as String;
        final sheetIds = sheet.contains('+ ') ? <String>[] : sheetMissions;
        if (sheetIds.isNotEmpty && sheetIds.join(',') != app.take(sheetIds.length).join(',')) {
          if (failures < 16) print('✖ ${row[0]}: planilha $sheetIds · app $app');
          failures++;
        }
      }
      final kind = row[1] as String;
      final appKind = p.kindLabel;
      if (kind != appKind && !(kind == 'ESTUDO' && appKind == 'PÓS-TRILHA')) {
        if (failures < 16) print('✖ ${row[0]}: tipo planilha $kind · app $appKind');
        failures++;
      }
    }
  }

  for (var i = 0; i < 9; i++) {
    final d = addDays(profile.startDate, i);
    final p = sched.dayPlan(d);
    print('${fmtDate(d)} ${weekdayShort(d)} ${p.kindLabel}: '
        '${p.units.map((u) => u.label).join(' | ')}${p.continuation != null ? ' (continuação ${p.continuation!.label})' : ''}');
    for (final t in p.tasks) {
      print('    · ${t.title} — ${t.detail}');
    }
  }
  final st = Stats(cat, data, trail, DateTime(2026, 11, 16));
  print('tópicos ativos: ${st.activeTopics}; semanas p/ 1h: ${sched.weeksFor(1)}, 3h: ${sched.weeksFor(3)}, 6h: ${sched.weeksFor(6)}');
  for (final sp in trail.subjects) {
    print('  ${sp.subject.id.padRight(5)} peso ${sp.weight} ${sp.entry.padRight(12)} ${sp.topics} tópicos ${(sp.minutes / 60).toStringAsFixed(0)} h');
  }

  // Todas as carreiras e níveis montam sem erro.
  for (final c in cat.careers) {
    for (final o in c.cargos) {
      for (var lv = 0; lv < 3; lv++) {
        final p2 = profile.copy()
          ..careerCode = c.code
          ..optionId = o.id
          ..level = lv;
        final t2 = Planner.buildTrail(cat, p2, {});
        final s2 = Schedule(catalog: cat, trail: t2, profile: p2, data: UserData(profile: p2, anchorDate: p2.startDate), today: p2.startDate);
        for (var i = 0; i < 400; i++) {
          s2.dayPlan(addDays(p2.startDate, i));
        }
        if (lv == 0) print('${o.id.padRight(7)} ${t2.units.length} missões · fim ${fmtDate(s2.endDate!)}');
      }
    }
  }
  print(failures == 0 ? '✔ motor confere com a planilha' : '✖ $failures divergências');
  exit(failures == 0 ? 0 : 1);
}
