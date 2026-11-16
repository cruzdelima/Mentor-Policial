/// Números do aluno: diário, edital verticalizado e painel (QG).
library;

import 'catalog.dart';
import 'dates.dart';
import 'models.dart';
import 'planner.dart';

enum TopicStatus { outOfCycle, toStudy, inProgress, reinforce, consolidated }

extension TopicStatusLabel on TopicStatus {
  String get label => switch (this) {
        TopicStatus.outOfCycle => 'Fora do ciclo',
        TopicStatus.toStudy => 'A estudar',
        TopicStatus.inProgress => 'Em andamento',
        TopicStatus.reinforce => 'Reforçar',
        TopicStatus.consolidated => 'Consolidado',
      };
}

class TopicStats {
  bool theory = false;
  int questions = 0;
  int correct = 0;
  int reviews = 0;
  int minutes = 0;
  TopicStatus status = TopicStatus.toStudy;
  double? get accuracy => questions > 0 ? correct / questions : null;
}

class SubjectStats {
  int questions = 0;
  int correct = 0;
  int minutes = 0;
  int topics = 0;
  int theoryDone = 0;
  double? get accuracy => questions > 0 ? correct / questions : null;
}

class WeekPoint {
  WeekPoint(this.start, this.questions, this.correct, this.minutes);
  final DateTime start;
  final int questions;
  final int correct;
  final int minutes;
  double? get accuracy => questions > 0 ? correct / questions : null;
}

class Stats {
  Stats(this.catalog, this.data, this.trail, DateTime today) : today = dateOnly(today) {
    final days = <String>{};
    for (final e in data.diary) {
      questions += e.questions;
      correct += e.correct;
      minutes += e.minutes;
      days.add(isoDate(e.date));
      if (e.subjectId != null) {
        final s = subject[e.subjectId!] ??= SubjectStats();
        s.questions += e.questions;
        s.correct += e.correct;
        s.minutes += e.minutes;
      }
      for (final t in e.topicIds) {
        final ts = topic[t] ??= TopicStats();
        if (e.type == 'Teoria') ts.theory = true;
        if (e.type == 'Revisão') ts.reviews++;
        if (e.topicIds.length == 1) {
          ts.questions += e.questions;
          ts.correct += e.correct;
          ts.minutes += e.minutes;
        }
      }
    }
    for (final e in data.unitDone.entries) {
      days.add(isoDate(e.value.date));
      if (e.key.endsWith(':T')) {
        (topic[e.key.substring(0, e.key.length - 2)] ??= TopicStats()).theory = true;
      }
    }
    studyDays = days.length;
    _studyDaySet = days;

    for (final t in catalog.topics) {
      final ts = topic[t.id] ??= TopicStats();
      final active = trail.isActive(t.id);
      if (!active) {
        ts.status = TopicStatus.outOfCycle;
      } else if (!ts.theory && ts.questions == 0) {
        ts.status = TopicStatus.toStudy;
      } else if (ts.questions > 0 && ts.correct < 0.7 * ts.questions) {
        ts.status = TopicStatus.reinforce;
      } else if (ts.theory && ts.questions > 0 && ts.reviews >= 2) {
        ts.status = TopicStatus.consolidated;
      } else {
        ts.status = TopicStatus.inProgress;
      }
      if (active) {
        final ss = subject[t.subjectId] ??= SubjectStats();
        ss.topics++;
        if (ts.theory) ss.theoryDone++;
        activeTopics++;
        if (ts.theory) theoryDone++;
        if (ts.status == TopicStatus.reinforce) reinforce++;
        if (ts.status == TopicStatus.consolidated) consolidated++;
      }
    }
  }

  final Catalog catalog;
  final UserData data;
  final Trail trail;
  final DateTime today;
  int questions = 0;
  int correct = 0;
  int minutes = 0;
  int studyDays = 0;
  int activeTopics = 0;
  int theoryDone = 0;
  int reinforce = 0;
  int consolidated = 0;
  late final Set<String> _studyDaySet;
  final Map<String, TopicStats> topic = {};
  final Map<String, SubjectStats> subject = {};

  double? get accuracy => questions > 0 ? correct / questions : null;

  /// Nota líquida estilo Cebraspe: (certas − erradas) / total.
  double? get net => questions > 0 ? (2 * correct - questions) / questions : null;
  double get hours => minutes / 60;
  double get theoryShare => activeTopics == 0 ? 0 : theoryDone / activeTopics;

  bool studiedOn(DateTime d) => _studyDaySet.contains(isoDate(d));

  /// Dias com estudo ÷ dias de estudo previstos desde o início (até hoje).
  double? constancy(Profile p) {
    var planned = 0, studied = 0;
    var d = dateOnly(p.startDate);
    while (!d.isAfter(today)) {
      if (p.studyWeekdays.contains(d.weekday)) {
        final isToday = sameDay(d, today);
        final did = studiedOn(d);
        if (!isToday || did) {
          planned++;
          if (did) studied++;
        }
      }
      d = addDays(d, 1);
    }
    return planned == 0 ? null : studied / planned;
  }

  /// Sequência atual de dias de estudo cumpridos (ignora dias de descanso).
  int streak(Profile p) {
    var n = 0;
    var d = today;
    if (!studiedOn(d)) d = addDays(d, -1);
    for (var i = 0; i < 400; i++) {
      if (d.isBefore(p.startDate)) break;
      if (p.studyWeekdays.contains(d.weekday)) {
        if (studiedOn(d)) {
          n++;
        } else {
          break;
        }
      }
      d = addDays(d, -1);
    }
    return n;
  }

  /// Semanas (segunda a domingo) com questões, acertos e minutos — últimas [n].
  List<WeekPoint> weekly(int n) {
    final monday = addDays(today, -(today.weekday - 1));
    final starts = [for (var i = n - 1; i >= 0; i--) addDays(monday, -7 * i)];
    final q = List<int>.filled(n, 0), c = List<int>.filled(n, 0), m = List<int>.filled(n, 0);
    for (final e in data.diary) {
      final idx = daysBetween(starts.first, e.date);
      if (idx < 0) continue;
      final k = idx ~/ 7;
      if (k >= n) continue;
      q[k] += e.questions;
      c[k] += e.correct;
      m[k] += e.minutes;
    }
    return [for (var i = 0; i < n; i++) WeekPoint(starts[i], q[i], c[i], m[i])];
  }
}
