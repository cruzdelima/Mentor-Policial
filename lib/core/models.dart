/// Modelos de dados do usuário (perfil, progresso, diário) com serialização JSON.
/// Tudo é salvo localmente, no computador do aluno.
library;

import 'dates.dart';

const kDiaryTypes = ['Teoria', 'Questões', 'Revisão', 'Simulado', 'Lei seca', 'Discursiva'];
const kSources = ['Material do app', 'PDF / livro', 'Videoaula', 'Plataforma de questões', 'Prova anterior', 'Simulado', 'Lei seca', 'Resumo / mapa', 'Outro'];
const kHourOptions = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0, 6.0, 7.0, 8.0];

String fmtHours(double h) {
  final whole = h.floor();
  final min = ((h - whole) * 60).round();
  return min == 0 ? '${whole}h' : '${whole}h${two(min)}';
}

class Profile {
  Profile({
    required this.name,
    required this.esfera,
    required this.careerCode,
    required this.optionId,
    required this.hoursPerDay,
    required this.studyWeekdays,
    required this.reviewWeekday,
    required this.level,
    required this.startDate,
    this.examDate,
    this.targetName = '',
  });

  factory Profile.fromJson(Map<String, dynamic> j) => Profile(
        name: j['name'] as String? ?? '',
        esfera: j['esfera'] as String,
        careerCode: j['careerCode'] as String,
        optionId: j['optionId'] as String,
        hoursPerDay: (j['hoursPerDay'] as num).toDouble(),
        studyWeekdays: [for (final d in j['studyWeekdays'] as List) (d as num).toInt()]..sort(),
        reviewWeekday: (j['reviewWeekday'] as num).toInt(),
        level: (j['level'] as num).toInt(),
        startDate: parseIso(j['startDate'] as String),
        examDate: j['examDate'] == null ? null : parseIso(j['examDate'] as String),
        targetName: j['targetName'] as String? ?? '',
      );

  String name;
  String esfera;
  String careerCode;
  String optionId;
  double hoursPerDay;

  /// 1 = segunda ... 7 = domingo. Inclui o dia de revisão.
  List<int> studyWeekdays;

  /// Dia da semana reservado para a revisão semanal (0 = sem dia de revisão).
  int reviewWeekday;

  /// 0 iniciante, 1 intermediário, 2 avançado.
  int level;
  DateTime startDate;
  DateTime? examDate;
  String targetName;

  /// Dias de conteúdo novo (dias de estudo menos o dia de revisão).
  List<int> get contentWeekdays => studyWeekdays.where((d) => d != reviewWeekday).toList();

  Map<String, dynamic> toJson() => {
        'name': name,
        'esfera': esfera,
        'careerCode': careerCode,
        'optionId': optionId,
        'hoursPerDay': hoursPerDay,
        'studyWeekdays': studyWeekdays,
        'reviewWeekday': reviewWeekday,
        'level': level,
        'startDate': isoDate(startDate),
        'examDate': examDate == null ? null : isoDate(examDate!),
        'targetName': targetName,
      };

  Profile copy() => Profile.fromJson(toJson());

  /// Assinatura do que altera a trilha/cronograma (mudou → replanejar).
  String get planSignature =>
      '$careerCode|$optionId|$hoursPerDay|${studyWeekdays.join(',')}|$reviewWeekday|$level|${isoDate(startDate)}';
}

class DiaryEntry {
  DiaryEntry({
    required this.id,
    required this.date,
    required this.type,
    this.subjectId,
    this.topicIds = const [],
    this.questions = 0,
    this.correct = 0,
    this.minutes = 0,
    this.source = '',
    this.notes = '',
    this.origin = '',
  });

  factory DiaryEntry.fromJson(Map<String, dynamic> j) => DiaryEntry(
        id: j['id'] as String,
        date: parseIso(j['date'] as String),
        type: j['type'] as String,
        subjectId: j['subjectId'] as String?,
        topicIds: [for (final t in (j['topicIds'] as List? ?? const [])) t as String],
        questions: (j['questions'] as num? ?? 0).toInt(),
        correct: (j['correct'] as num? ?? 0).toInt(),
        minutes: (j['minutes'] as num? ?? 0).toInt(),
        source: j['source'] as String? ?? '',
        notes: j['notes'] as String? ?? '',
        origin: j['origin'] as String? ?? '',
      );

  final String id;
  DateTime date;
  String type;
  String? subjectId;
  List<String> topicIds;
  int questions;
  int correct;
  int minutes;
  String source;
  String notes;

  /// De onde veio o lançamento: '' (manual), 'unit:<id>', 'task:<chave>', 'quiz:<material>'.
  String origin;

  int get wrong => questions - correct;
  double? get accuracy => questions > 0 ? correct / questions : null;

  Map<String, dynamic> toJson() => {
        'id': id,
        'date': isoDate(date),
        'type': type,
        'subjectId': subjectId,
        'topicIds': topicIds,
        'questions': questions,
        'correct': correct,
        'minutes': minutes,
        'source': source,
        'notes': notes,
        'origin': origin,
      };
}

class TopicOverride {
  TopicOverride({this.skip = false, this.size, this.notes = ''});

  factory TopicOverride.fromJson(Map<String, dynamic> j) =>
      TopicOverride(skip: j['skip'] as bool? ?? false, size: j['size'] as String?, notes: j['notes'] as String? ?? '');

  bool skip;
  String? size;
  String notes;

  bool get isEmpty => !skip && size == null && notes.isEmpty;

  Map<String, dynamic> toJson() => {'skip': skip, 'size': size, 'notes': notes};
}

/// Conclusão de uma missão (unidade da trilha) ou de uma tarefa do dia.
class Done {
  Done(this.date, [this.entryId]);

  factory Done.fromJson(Map<String, dynamic> j) => Done(parseIso(j['date'] as String), j['entry'] as String?);

  final DateTime date;
  final String? entryId;

  Map<String, dynamic> toJson() => {'date': isoDate(date), 'entry': entryId};
}

class QuizAttempt {
  QuizAttempt({required this.date, required this.answers, required this.correct, required this.wrong, required this.blank});

  factory QuizAttempt.fromJson(Map<String, dynamic> j) => QuizAttempt(
        date: parseIso(j['date'] as String),
        answers: {for (final e in (j['answers'] as Map<String, dynamic>).entries) e.key: e.value as String?},
        correct: (j['correct'] as num).toInt(),
        wrong: (j['wrong'] as num).toInt(),
        blank: (j['blank'] as num).toInt(),
      );

  final DateTime date;
  final Map<String, String?> answers;
  final int correct;
  final int wrong;
  final int blank;

  int get net => correct - wrong;

  Map<String, dynamic> toJson() =>
      {'date': isoDate(date), 'answers': answers, 'correct': correct, 'wrong': wrong, 'blank': blank};
}

/// Material adicionado pelo próprio aluno (link de videoaula, PDF no computador, site).
class UserMaterial {
  UserMaterial({required this.id, required this.title, required this.kind, required this.location, this.subjectId, this.topicId});

  factory UserMaterial.fromJson(Map<String, dynamic> j) => UserMaterial(
        id: j['id'] as String,
        title: j['title'] as String,
        kind: j['kind'] as String,
        location: j['location'] as String,
        subjectId: j['subjectId'] as String?,
        topicId: j['topicId'] as String?,
      );

  final String id;
  String title;

  /// 'pdf', 'video', 'link'
  String kind;

  /// URL ou caminho do arquivo.
  String location;
  String? subjectId;
  String? topicId;

  Map<String, dynamic> toJson() =>
      {'id': id, 'title': title, 'kind': kind, 'location': location, 'subjectId': subjectId, 'topicId': topicId};
}

/// Tudo o que o aluno produz. Um único arquivo JSON, com cópia de segurança.
class UserData {
  UserData({
    this.profile,
    DateTime? anchorDate,
    Set<String>? doneAtAnchor,
    this.planSignature = '',
    Map<String, Done>? unitDone,
    Map<String, Done>? taskDone,
    Map<String, TopicOverride>? overrides,
    List<DiaryEntry>? diary,
    Map<String, List<QuizAttempt>>? quizzes,
    List<UserMaterial>? materials,
    Map<String, int>? readProgress,
    this.seq = 0,
  })  : anchorDate = anchorDate ?? dateOnly(DateTime.now()),
        doneAtAnchor = doneAtAnchor ?? {},
        unitDone = unitDone ?? {},
        taskDone = taskDone ?? {},
        overrides = overrides ?? {},
        diary = diary ?? [],
        quizzes = quizzes ?? {},
        materials = materials ?? [],
        readProgress = readProgress ?? {};

  factory UserData.fromJson(Map<String, dynamic> j) => UserData(
        profile: j['profile'] == null ? null : Profile.fromJson(j['profile'] as Map<String, dynamic>),
        anchorDate: j['anchorDate'] == null ? null : parseIso(j['anchorDate'] as String),
        doneAtAnchor: {for (final s in (j['doneAtAnchor'] as List? ?? const [])) s as String},
        planSignature: j['planSignature'] as String? ?? '',
        unitDone: {
          for (final e in (j['unitDone'] as Map<String, dynamic>? ?? const {}).entries)
            e.key: Done.fromJson(e.value as Map<String, dynamic>),
        },
        taskDone: {
          for (final e in (j['taskDone'] as Map<String, dynamic>? ?? const {}).entries)
            e.key: Done.fromJson(e.value as Map<String, dynamic>),
        },
        overrides: {
          for (final e in (j['overrides'] as Map<String, dynamic>? ?? const {}).entries)
            e.key: TopicOverride.fromJson(e.value as Map<String, dynamic>),
        },
        diary: [for (final d in (j['diary'] as List? ?? const [])) DiaryEntry.fromJson(d as Map<String, dynamic>)],
        quizzes: {
          for (final e in (j['quizzes'] as Map<String, dynamic>? ?? const {}).entries)
            e.key: [for (final a in e.value as List) QuizAttempt.fromJson(a as Map<String, dynamic>)],
        },
        materials: [for (final m in (j['materials'] as List? ?? const [])) UserMaterial.fromJson(m as Map<String, dynamic>)],
        readProgress: {
          for (final e in (j['readProgress'] as Map<String, dynamic>? ?? const {}).entries) e.key: (e.value as num).toInt(),
        },
        seq: (j['seq'] as num? ?? 0).toInt(),
      );

  Profile? profile;

  /// Data a partir da qual o cronograma atual foi montado.
  DateTime anchorDate;

  /// Missões já concluídas quando o cronograma atual foi montado (ficam fora dele).
  Set<String> doneAtAnchor;
  String planSignature;
  Map<String, Done> unitDone;
  Map<String, Done> taskDone;
  Map<String, TopicOverride> overrides;
  List<DiaryEntry> diary;
  Map<String, List<QuizAttempt>> quizzes;
  List<UserMaterial> materials;

  /// Seções lidas por material (para "continuar de onde parou").
  Map<String, int> readProgress;
  int seq;

  String nextId(String prefix) {
    seq++;
    return '$prefix${DateTime.now().millisecondsSinceEpoch.toRadixString(36)}$seq';
  }

  Map<String, dynamic> toJson() => {
        'schema': 1,
        'profile': profile?.toJson(),
        'anchorDate': isoDate(anchorDate),
        'doneAtAnchor': doneAtAnchor.toList()..sort(),
        'planSignature': planSignature,
        'unitDone': {for (final e in unitDone.entries) e.key: e.value.toJson()},
        'taskDone': {for (final e in taskDone.entries) e.key: e.value.toJson()},
        'overrides': {
          for (final e in overrides.entries)
            if (!e.value.isEmpty) e.key: e.value.toJson(),
        },
        'diary': [for (final d in diary) d.toJson()],
        'quizzes': {for (final e in quizzes.entries) e.key: [for (final a in e.value) a.toJson()]},
        'materials': [for (final m in materials) m.toJson()],
        'readProgress': readProgress,
        'seq': seq,
      };
}
