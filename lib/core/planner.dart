/// Motor de metas: monta a trilha de missões (ciclo básico) e o cronograma diário.
///
/// Regras (as mesmas da planilha Mentor Policial):
///  * Cada tópico do edital vira 2 missões: teoria + resumo e um bloco de questões.
///  * A duração depende do tamanho do tópico (P/M/G) e do nível do aluno.
///  * Matérias de peso 3 começam no dia 1; peso 2 entram após [weight2AfterHours] h; peso 1 após [weight1AfterHours] h.
///  * Dentro disso, as matérias se alternam de forma proporcional ao peso (fila justa ponderada).
///  * Cada dia de conteúdo tem capacidade = horas × 60 × (1 − % de revisão).
///    A missão pertence ao dia em que começa; se nenhuma começa no dia, ele continua a anterior.
///  * Dia de revisão semanal, revisão 24h, revisão de 30 dias, simulados quinzenais, discursiva e lei seca.
library;

import 'dart:math' as math;

import 'catalog.dart';
import 'dates.dart';
import 'models.dart';

enum Phase { theory, questions }

class Unit {
  Unit({
    required this.topic,
    required this.subject,
    required this.phase,
    required this.minutes,
    required this.questions,
    required this.size,
    required this.key,
  });

  final Topic topic;
  final Subject subject;
  final Phase phase;
  final int minutes;

  /// Nº de questões (para missões de questões).
  final int questions;
  final String size;
  final int key;

  /// Número da missão na trilha completa (1, 2, 3...).
  late final int seq;

  /// Minuto de início na trilha completa.
  late final int start;

  bool get isTheory => phase == Phase.theory;
  String get id => '${topic.id}:${isTheory ? 'T' : 'Q'}';
  String get title => isTheory ? 'Teoria + resumo' : '$questions questões';
  String get label => '#$seq · ${subject.id} · ${isTheory ? 'TEORIA + RESUMO' : '$questions QUESTÕES'}';
}

class SubjectPlan {
  SubjectPlan(this.subject, this.weight);
  final Subject subject;
  final int weight;
  int topics = 0;
  int minutes = 0;

  /// 'dia 1', 'após 40 h', 'após 100 h'
  String entry = '';
}

class Trail {
  Trail({required this.units, required this.subjects, required this.activeTopics, required this.v2, required this.v3}) {
    var acc = 0;
    for (var i = 0; i < units.length; i++) {
      units[i].seq = i + 1;
      units[i].start = acc;
      acc += units[i].minutes;
      _byId[units[i].id] = units[i];
    }
    totalMinutes = acc;
  }

  final List<Unit> units;
  final List<SubjectPlan> subjects;
  final List<Topic> activeTopics;
  final double v2;
  final double v3;
  late final int totalMinutes;
  final Map<String, Unit> _byId = {};

  Unit? unit(String id) => _byId[id];
  Unit? theoryOf(String topicId) => _byId['$topicId:T'];
  Unit? questionsOf(String topicId) => _byId['$topicId:Q'];
  bool isActive(String topicId) => _byId.containsKey('$topicId:T');
}

/// Uma tarefa de um dia (revisão, simulado, lei seca...).
class DayTask {
  DayTask({
    required this.key,
    required this.code,
    required this.title,
    required this.detail,
    this.topicIds = const [],
    this.minutes = 0,
    this.askQuestions = false,
    this.suggestedQuestions = 0,
    this.diaryType,
  });

  /// Chave única: 'aaaa-mm-dd|CÓDIGO'.
  final String key;

  /// REV24, LEI, REV_SEM, SIM, QREV, ERROS, PLAN, REV30, DISC, GERAL, POS
  final String code;
  final String title;
  final String detail;
  final List<String> topicIds;
  final int minutes;
  final bool askQuestions;
  final int suggestedQuestions;

  /// Tipo de lançamento no diário ao concluir (null = só marca como feita).
  final String? diaryType;
}

enum DayKind { beforeStart, study, review, rest, finished }

class DayPlan {
  DayPlan({
    required this.date,
    required this.kind,
    required this.weekNo,
    required this.history,
    this.units = const [],
    this.continuation,
    this.tasks = const [],
  });

  final DateTime date;
  final DayKind kind;
  final int weekNo;

  /// Dia anterior ao cronograma atual: mostra o que foi feito, não o que estava previsto.
  final bool history;
  final List<Unit> units;
  final Unit? continuation;
  final List<DayTask> tasks;

  bool get isStudy => kind == DayKind.study;
  bool get isReview => kind == DayKind.review;
  bool get isRest => kind == DayKind.rest;

  String get kindLabel => switch (kind) {
        DayKind.beforeStart => 'ANTES DO INÍCIO',
        DayKind.study => 'ESTUDO',
        DayKind.review => 'REVISÃO',
        DayKind.rest => 'DESCANSO',
        DayKind.finished => 'PÓS-TRILHA',
      };
}

class Planner {
  Planner._();

  /// Monta a trilha completa (ordem do ciclo) para o perfil.
  static Trail buildTrail(Catalog cat, Profile p, Map<String, TopicOverride> ov) {
    final prm = cat.params;
    final lv = p.level.clamp(0, 2);
    final active = <Topic>[];
    for (final t in cat.topics) {
      final s = cat.subjectOrNull(t.subjectId);
      if (s == null || s.weightFor(p.optionId) <= 0) continue;
      if (!t.appliesTo(p.careerCode, p.optionId)) continue;
      if (ov[t.id]?.skip ?? false) continue;
      active.add(t);
    }

    final subjIds = <String>{for (final t in active) t.subjectId};
    final plans = <String, SubjectPlan>{};
    for (final s in cat.subjects) {
      if (subjIds.contains(s.id)) plans[s.id] = SubjectPlan(s, s.weightFor(p.optionId));
    }
    final sw3 = plans.values.where((x) => x.weight >= 3).fold<int>(0, (a, x) => a + x.weight);
    final sw23 = plans.values.where((x) => x.weight >= 2).fold<int>(0, (a, x) => a + x.weight);
    final v2 = prm.weight2AfterHours * 60 / math.max(sw3, 1);
    final v3 = v2 + (prm.weight1AfterHours - prm.weight2AfterHours) * 60 / math.max(sw23, 1);

    final cum = <String, int>{};
    final units = <Unit>[];
    for (final t in active) {
      final sp = plans[t.subjectId]!;
      final size = ov[t.id]?.size ?? t.size;
      final si = size == 'P' ? 0 : (size == 'G' ? 2 : 1);
      final theory = prm.theoryMinutes[si][lv];
      final qn = prm.questions[si];
      final qmin = (qn * prm.minutesPerQuestion[lv]).round();
      final w = theory + qmin;
      final x = cum[t.subjectId] ?? 0;
      final off = sp.weight >= 3 ? 0.0 : (sp.weight == 2 ? v2 : v3);
      final key = ((off + (x + w / 2) / sp.weight) * 100).round();
      cum[t.subjectId] = x + w;
      sp.topics++;
      sp.minutes += w;
      units.add(Unit(topic: t, subject: sp.subject, phase: Phase.theory, minutes: theory, questions: 0, size: size, key: key));
      units.add(Unit(topic: t, subject: sp.subject, phase: Phase.questions, minutes: qmin, questions: qn, size: size, key: key));
    }
    units.sort((a, b) {
      final c = a.key.compareTo(b.key);
      if (c != 0) return c;
      final d = a.topic.index.compareTo(b.topic.index);
      if (d != 0) return d;
      return a.phase.index.compareTo(b.phase.index);
    });

    String fmtH(double h) => h == h.roundToDouble() ? h.toStringAsFixed(0) : h.toStringAsFixed(1);
    final list = plans.values.toList()..sort((a, b) => b.weight.compareTo(a.weight) != 0 ? b.weight.compareTo(a.weight) : b.minutes.compareTo(a.minutes));
    for (final sp in list) {
      sp.entry = sp.weight >= 3 ? 'dia 1' : (sp.weight == 2 ? 'após ${fmtH(prm.weight2AfterHours)} h' : 'após ${fmtH(prm.weight1AfterHours)} h');
    }
    return Trail(units: units, subjects: list, activeTopics: active, v2: v2, v3: v3);
  }
}

/// Cronograma: a trilha distribuída nos dias, a partir da data-âncora.
class Schedule {
  Schedule({
    required this.catalog,
    required this.trail,
    required this.profile,
    required this.data,
    required DateTime today,
  })  : today = dateOnly(today),
        anchor = dateOnly(data.anchorDate),
        cap = profile.hoursPerDay * 60 * (1 - catalog.params.reviewShare) {
    final content = profile.contentWeekdays.isEmpty ? [1, 2, 3, 4, 5, 6, 7] : profile.contentWeekdays;
    _contentDays = content.toSet();
    var acc = 0;
    for (final u in trail.units) {
      if (data.doneAtAnchor.contains(u.id)) continue;
      queue.add(u);
      _qStart[u.id] = acc;
      acc += u.minutes;
    }
    queueMinutes = acc;
    dayCount = acc == 0 ? 0 : ((acc - 0.01) / cap).floor() + 1;
    var d = anchor;
    while (studyDates.length < dayCount) {
      if (_contentDays.contains(d.weekday)) {
        _dayIndex[isoDate(d)] = studyDates.length;
        studyDates.add(d);
      }
      d = addDays(d, 1);
    }
    for (final u in queue) {
      final k = ((_qStart[u.id]! + 1e-6) / cap).floor();
      _unitDay[u.id] = k;
      (_dayUnits[k] ??= []).add(u);
    }
  }

  final Catalog catalog;
  final Trail trail;
  final Profile profile;
  final UserData data;
  final DateTime today;
  final DateTime anchor;

  /// Minutos de conteúdo novo por dia.
  final double cap;
  final List<Unit> queue = [];
  final Map<String, int> _qStart = {};
  final Map<String, int> _unitDay = {};
  final Map<int, List<Unit>> _dayUnits = {};
  final Map<String, int> _dayIndex = {};
  final List<DateTime> studyDates = [];
  late final Set<int> _contentDays;
  late final int queueMinutes;
  late final int dayCount;

  MethodParams get params => catalog.params;

  DateTime? get endDate => studyDates.isEmpty ? null : studyDates.last;

  /// Data prevista da missão no cronograma atual (null = concluída antes do replanejamento).
  DateTime? plannedDate(Unit u) {
    final k = _unitDay[u.id];
    return k == null ? null : studyDates[k];
  }

  bool isDone(Unit u) => data.unitDone.containsKey(u.id);

  int get remainingMinutes => trail.units.where((u) => !isDone(u)).fold(0, (a, u) => a + u.minutes);
  int get doneCount => trail.units.where(isDone).length;

  List<Unit> get overdue => [
        for (final u in queue)
          if (!isDone(u) && studyDates[_unitDay[u.id]!].isBefore(today)) u,
      ];

  /// Próximas missões pendentes, na ordem da trilha.
  List<Unit> nextPending(int n) => [for (final u in queue) if (!isDone(u)) u].take(n).toList();

  int weekNo(DateTime d) => daysBetween(profile.startDate, d) ~/ 7 + 1;

  bool isContentDay(DateTime d) => _contentDays.contains(d.weekday);
  bool isReviewDay(DateTime d) => profile.reviewWeekday != 0 && d.weekday == profile.reviewWeekday;

  /// Nº de dias de conteúdo entre o início e [d] (exclusivo). Usado para o rodízio da lei seca.
  int contentDayNumber(DateTime d) {
    final days = daysBetween(profile.startDate, d);
    if (days <= 0) return 0;
    final weeks = days ~/ 7;
    var n = weeks * _contentDays.length;
    var x = addDays(profile.startDate, weeks * 7);
    while (x.isBefore(d)) {
      if (_contentDays.contains(x.weekday)) n++;
      x = addDays(x, 1);
    }
    return n;
  }

  /// Missões que contam para revisão num intervalo: as concluídas no período
  /// e, para datas de hoje em diante, as previstas ainda pendentes.
  List<Unit> unitsInRange(DateTime from, DateTime to) {
    final a = dateOnly(from), b = dateOnly(to);
    bool inRange(DateTime d) => !d.isBefore(a) && !d.isAfter(b);
    final out = <Unit>[];
    for (final u in trail.units) {
      final done = data.unitDone[u.id];
      if (done != null) {
        if (inRange(done.date)) out.add(u);
        continue;
      }
      final pd = plannedDate(u);
      if (pd != null && inRange(pd) && !pd.isBefore(today)) out.add(u);
    }
    return out;
  }

  static List<String> topicsOf(List<Unit> units) {
    final seen = <String>{};
    return [for (final u in units) if (seen.add(u.topic.id)) u.topic.id];
  }

  String _range(List<Unit> us) {
    if (us.isEmpty) return '';
    final a = us.map((u) => u.seq).reduce(math.min), b = us.map((u) => u.seq).reduce(math.max);
    return a == b ? '#$a' : '#$a a #$b';
  }

  String _topicNames(List<String> ids, {int max = 3}) {
    final names = [for (final id in ids) catalog.topic(id)?.name ?? id];
    if (names.length <= max) return names.join(' · ');
    return '${names.take(max).join(' · ')} +${names.length - max}';
  }

  double get minutesPerQuestion => params.minutesPerQuestion[profile.level.clamp(0, 2)];

  int get reviewQuestions {
    final v = (profile.hoursPerDay * 60 * 0.45 / minutesPerQuestion / 10).round() * 10;
    return math.max(10, v);
  }

  int get miniSimuladoItems {
    final v = (profile.hoursPerDay * 60 * 0.55 / 2.25 / 10).round() * 10;
    return math.max(10, v);
  }

  int get rev24Minutes => (profile.hoursPerDay * 60 * params.reviewShare).round();

  bool isSimuladoWeek(int w) => w >= params.simuladoFromWeek && (w - params.simuladoFromWeek) % params.simuladoEveryWeeks == 0;

  bool isDiscursivaWeek(int w) {
    final c = catalog.career(profile.careerCode);
    return c.discursiva && w >= params.discursivaFromWeek && (w - params.discursivaFromWeek) % 2 == 0;
  }

  DateTime? previousContentDay(DateTime d) {
    var x = addDays(d, -1);
    for (var i = 0; i < 14; i++) {
      if (x.isBefore(profile.startDate)) return null;
      if (_contentDays.contains(x.weekday)) return x;
      x = addDays(x, -1);
    }
    return null;
  }

  String leiSeca(DateTime d) => catalog.leiSeca[contentDayNumber(d) % catalog.leiSeca.length];

  DayPlan dayPlan(DateTime date) {
    final d = dateOnly(date);
    final iso = isoDate(d);
    final w = weekNo(d);
    if (d.isBefore(profile.startDate)) {
      return DayPlan(date: d, kind: DayKind.beforeStart, weekNo: 0, history: false);
    }
    final history = d.isBefore(anchor);

    if (isContentDay(d)) {
      final tasks = <DayTask>[];
      final prev = previousContentDay(d);
      if (prev != null) {
        final us = unitsInRange(prev, prev);
        if (us.isNotEmpty) {
          final ids = topicsOf(us);
          tasks.add(DayTask(
            key: '$iso|REV24',
            code: 'REV24',
            title: 'Revisão 24h · $rev24Minutes min',
            detail: 'Rever ${_range(us)}: ${_topicNames(ids)}',
            topicIds: ids,
            minutes: rev24Minutes,
            diaryType: 'Revisão',
          ));
        }
      }
      tasks.add(DayTask(
        key: '$iso|LEI',
        code: 'LEI',
        title: 'Lei seca · 10 min',
        detail: leiSeca(d),
        minutes: 10,
        diaryType: 'Lei seca',
      ));

      if (history) {
        final doneHere = [
          for (final u in trail.units)
            if (data.unitDone[u.id] != null && sameDay(data.unitDone[u.id]!.date, d)) u,
        ];
        return DayPlan(date: d, kind: DayKind.study, weekNo: w, history: true, units: doneHere, tasks: tasks);
      }
      final k = _dayIndex[iso];
      if (k == null) {
        // Depois do fim da trilha (ou dia sem conteúdo no cronograma atual).
        final finished = dayCount == 0 || d.isAfter(studyDates.last);
        if (finished) {
          tasks.insert(
            0,
            DayTask(
              key: '$iso|POS',
              code: 'POS',
              title: '1ª volta concluída: questões das matérias mais fracas',
              detail: 'Provas anteriores e questões das matérias com menor % de acerto (veja o EDITAL).',
              minutes: (profile.hoursPerDay * 60).round(),
              askQuestions: true,
              suggestedQuestions: reviewQuestions * 2,
              diaryType: 'Questões',
            ),
          );
          return DayPlan(date: d, kind: DayKind.finished, weekNo: w, history: false, tasks: tasks);
        }
        return DayPlan(date: d, kind: DayKind.study, weekNo: w, history: false, tasks: tasks);
      }
      final units = _dayUnits[k] ?? const <Unit>[];
      Unit? cont;
      if (units.isEmpty) {
        final m = k * cap;
        for (final u in queue) {
          if (_qStart[u.id]! <= m) cont = u;
        }
      }
      return DayPlan(date: d, kind: DayKind.study, weekNo: w, history: false, units: units, continuation: cont, tasks: tasks);
    }

    if (isReviewDay(d)) {
      final tasks = <DayTask>[];
      final week = unitsInRange(addDays(d, -6), addDays(d, -1));
      final wIds = topicsOf(week);
      if (week.isEmpty) {
        tasks.add(DayTask(
          key: '$iso|GERAL',
          code: 'GERAL',
          title: 'Revisão geral',
          detail: 'Matérias com menor % de acerto (veja o EDITAL e o QG).',
          minutes: (profile.hoursPerDay * 60 * 0.35).round(),
          diaryType: 'Revisão',
        ));
      } else {
        tasks.add(DayTask(
          key: '$iso|REV_SEM',
          code: 'REV_SEM',
          title: 'Revisão semanal',
          detail: 'Reler resumos ${_range(week)}: ${_topicNames(wIds)}',
          topicIds: wIds,
          minutes: (profile.hoursPerDay * 60 * 0.35).round(),
          diaryType: 'Revisão',
        ));
      }
      final sim = isSimuladoWeek(w);
      if (sim) {
        final full = profile.hoursPerDay >= params.fullSimuladoMinHours;
        tasks.add(DayTask(
          key: '$iso|SIM',
          code: 'SIM',
          title: full ? 'Simulado completo' : 'Mini-simulado · $miniSimuladoItems itens',
          detail: full ? 'Padrão da banca (4h30) + correção. Anote a nota líquida.' : '$miniSimuladoItems itens das matérias já estudadas + correção. Anote a nota líquida.',
          minutes: full ? 270 : (profile.hoursPerDay * 60 * 0.55).round(),
          askQuestions: true,
          suggestedQuestions: full ? 120 : miniSimuladoItems,
          diaryType: 'Simulado',
        ));
      } else {
        tasks.add(DayTask(
          key: '$iso|QREV',
          code: 'QREV',
          title: 'Questões de revisão · $reviewQuestions itens',
          detail: 'Questões dos assuntos da semana, misturados.',
          topicIds: wIds,
          minutes: (reviewQuestions * minutesPerQuestion).round(),
          askQuestions: true,
          suggestedQuestions: reviewQuestions,
          diaryType: 'Questões',
        ));
      }
      tasks.add(DayTask(
        key: '$iso|ERROS',
        code: 'ERROS',
        title: 'Caderno de erros',
        detail: sim ? 'Refazer as erradas do simulado e anotar o porquê de cada erro.' : 'Refazer as questões erradas da semana e anotar o porquê de cada erro.',
        minutes: 30,
        diaryType: 'Revisão',
      ));
      if (w >= 5) {
        final old = unitsInRange(addDays(d, -34), addDays(d, -29));
        if (old.isNotEmpty) {
          final ids = topicsOf(old);
          tasks.add(DayTask(
            key: '$iso|REV30',
            code: 'REV30',
            title: 'Revisão 30 dias',
            detail: 'Reler ${_range(old)}: ${_topicNames(ids)}',
            topicIds: ids,
            minutes: 30,
            diaryType: 'Revisão',
          ));
        }
      }
      if (isDiscursivaWeek(w)) {
        tasks.add(DayTask(
          key: '$iso|DISC',
          code: 'DISC',
          title: 'Discursiva',
          detail: '1 redação no padrão da banca + correção com o espelho.',
          minutes: 60,
          diaryType: 'Discursiva',
        ));
      }
      tasks.add(DayTask(
        key: '$iso|PLAN',
        code: 'PLAN',
        title: 'Planejamento',
        detail: 'Conferir o QG, marcar tópicos para reforçar e ajustar a semana.',
        minutes: 15,
      ));
      return DayPlan(date: d, kind: DayKind.review, weekNo: w, history: history, tasks: tasks);
    }

    return DayPlan(
      date: d,
      kind: DayKind.rest,
      weekNo: w,
      history: history,
      tasks: [
        DayTask(key: '$iso|REST', code: 'REST', title: 'Descanso', detail: 'Recuperação. TAF leve opcional (corrida, barra, flexão).'),
      ],
    );
  }

  /// Situação do dia: (feitas, total) considerando missões e tarefas marcáveis.
  (int, int) dayProgress(DayPlan p) {
    if (p.kind == DayKind.rest || p.kind == DayKind.beforeStart) return (0, 0);
    var total = 0, done = 0;
    if (!p.history) {
      for (final u in p.units) {
        total++;
        if (isDone(u)) done++;
      }
      if (p.continuation != null) {
        total++;
        if (isDone(p.continuation!)) done++;
      }
    }
    for (final t in p.tasks) {
      if (t.code == 'REST') continue;
      total++;
      if (data.taskDone.containsKey(t.key)) done++;
    }
    return (done, total);
  }

  /// Duração estimada (em semanas) para concluir o restante com outra carga diária.
  int weeksFor(double hours) {
    final c = hours * 60 * (1 - params.reviewShare);
    final days = (remainingMinutes / c).ceil();
    final per = _contentDays.length;
    return days == 0 ? 0 : ((days - 1) ~/ per) + 1;
  }
}
