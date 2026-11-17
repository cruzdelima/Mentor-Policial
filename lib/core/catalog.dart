/// Catálogo: carreiras, cargos, matérias, tópicos e parâmetros do método.
/// Vem de assets/catalog/catalog.json e, no futuro, poderá ser atualizado por pacotes de conteúdo.
library;

import 'extras.dart';

class Cargo {
  const Cargo(this.id, this.name, {this.contest});

  factory Cargo.fromJson(Map<String, dynamic> j) => Cargo(
        j['id'] as String,
        j['name'] as String,
        contest: j['contest'] == null ? null : ContestInfo.fromJson(j['contest'] as Map<String, dynamic>),
      );

  final String id;
  final String name;

  /// Preenchido quando o "cargo" é um concurso específico com edital publicado (modo pós-edital).
  final ContestInfo? contest;

  bool get isContest => contest != null;
}

/// Dados de um concurso pós-edital (ex.: CFO CBMPE 2026).
class ContestInfo {
  ContestInfo({
    required this.base,
    required this.orgao,
    required this.uf,
    required this.banca,
    required this.examDate,
    required this.editalUrl,
    required this.vagas,
    required this.status,
    required this.notes,
    required this.topicIds,
    required this.questions,
  });

  factory ContestInfo.fromJson(Map<String, dynamic> j) => ContestInfo(
        base: j['base'] as String? ?? '',
        orgao: j['orgao'] as String? ?? '',
        uf: j['uf'] as String? ?? '',
        banca: j['banca'] as String? ?? '',
        examDate: DateTime.tryParse(j['examDate'] as String? ?? ''),
        editalUrl: j['editalUrl'] as String? ?? '',
        vagas: j['vagas'] as String? ?? '',
        status: j['status'] as String? ?? '',
        notes: j['notes'] as String? ?? '',
        topicIds: [for (final t in j['topicIds'] as List? ?? const []) t as String],
        questions: {
          for (final e in ((j['questions'] as Map?) ?? const {}).entries) e.key as String: (e.value as num).toInt(),
        },
      );

  /// Cargo do ciclo básico usado como referência (e como plano B se o concurso for removido).
  final String base;
  final String orgao;
  final String uf;
  final String banca;
  final DateTime? examDate;
  final String editalUrl;
  final String vagas;
  final String status;
  final String notes;

  /// Assuntos do edital, na ordem do edital.
  final List<String> topicIds;

  /// Número de questões por matéria (0 = não informado).
  final Map<String, int> questions;

  int get totalQuestions => questions.values.fold(0, (a, b) => a + b);
}

class Career {
  Career({
    required this.code,
    required this.name,
    required this.esfera,
    required this.escolaridade,
    required this.banca,
    required this.discursiva,
    required this.observacao,
    required this.marca,
    required this.cargos,
  });

  factory Career.fromJson(Map<String, dynamic> j) => Career(
        code: j['code'] as String,
        name: j['name'] as String,
        esfera: j['esfera'] as String,
        escolaridade: j['escolaridade'] as String,
        banca: j['banca'] as String,
        discursiva: j['discursiva'] as bool,
        observacao: j['observacao'] as String,
        marca: j['marca'] as String,
        cargos: [for (final c in j['cargos'] as List) Cargo.fromJson(c as Map<String, dynamic>)],
      );

  final String code;
  final String name;
  final String esfera;
  final String escolaridade;
  final String banca;
  final bool discursiva;
  final String observacao;
  final String marca;
  final List<Cargo> cargos;

  /// Cargos do ciclo básico (pré-edital).
  List<Cargo> get cycleCargos => cargos.where((c) => !c.isContest).toList();

  /// Concursos com edital publicado (pós-edital).
  List<Cargo> get contests => cargos.where((c) => c.isContest).toList();
}

class Subject {
  Subject({required this.id, required this.name, required this.colorHex, required this.weights});

  factory Subject.fromJson(Map<String, dynamic> j) => Subject(
        id: j['id'] as String,
        name: j['name'] as String,
        colorHex: j['color'] as String,
        weights: {
          for (final e in (j['weights'] as Map<String, dynamic>).entries) e.key: (e.value as num).toInt(),
        },
      );

  final String id;
  final String name;
  final String colorHex;
  final Map<String, int> weights;

  int weightFor(String optionId) => weights[optionId] ?? 0;
}

class Topic {
  Topic({
    required this.id,
    required this.subjectId,
    required this.n,
    required this.name,
    required this.size,
    required this.scope,
    required this.index,
    this.contest,
  });

  factory Topic.fromJson(Map<String, dynamic> j, int index) => Topic(
        id: j['id'] as String,
        subjectId: j['subject'] as String,
        n: (j['n'] as num).toInt(),
        name: j['name'] as String,
        size: j['size'] as String,
        scope: [for (final s in j['scope'] as List) s as String],
        index: index,
        contest: j['contest'] as String?,
      );

  final String id;
  final String subjectId;
  final int n;
  final String name;

  /// P, M ou G.
  final String size;

  /// Siglas de carreira (ou ids de cargo) em que o tópico costuma cair. Vazio = todas.
  final List<String> scope;

  /// Posição no catálogo (desempate estável).
  final int index;

  /// Id do concurso, quando o assunto é exclusivo de um edital (cadastrado no modo pós-edital).
  final String? contest;

  int get sizeIndex => size == 'P' ? 0 : (size == 'G' ? 2 : 1);

  bool appliesTo(String careerCode, String optionId) =>
      scope.isEmpty || scope.contains(careerCode) || scope.contains(optionId);
}

class MethodParams {
  MethodParams({
    required this.theoryMinutes,
    required this.minutesPerQuestion,
    required this.questions,
    required this.reviewShare,
    required this.weight2AfterHours,
    required this.weight1AfterHours,
    required this.simuladoFromWeek,
    required this.simuladoEveryWeeks,
    required this.discursivaFromWeek,
    required this.fullSimuladoMinHours,
  });

  factory MethodParams.fromJson(Map<String, dynamic> j) {
    final tm = j['theoryMinutes'] as Map<String, dynamic>;
    final q = j['questions'] as Map<String, dynamic>;
    return MethodParams(
      theoryMinutes: [
        for (final size in const ['P', 'M', 'G']) [for (final v in tm[size] as List) (v as num).toInt()],
      ],
      minutesPerQuestion: [for (final v in j['minutesPerQuestion'] as List) (v as num).toDouble()],
      questions: [for (final size in const ['P', 'M', 'G']) (q[size] as num).toInt()],
      reviewShare: (j['reviewShare'] as num).toDouble(),
      weight2AfterHours: (j['weight2AfterHours'] as num).toDouble(),
      weight1AfterHours: (j['weight1AfterHours'] as num).toDouble(),
      simuladoFromWeek: (j['simuladoFromWeek'] as num).toInt(),
      simuladoEveryWeeks: (j['simuladoEveryWeeks'] as num).toInt(),
      discursivaFromWeek: (j['discursivaFromWeek'] as num).toInt(),
      fullSimuladoMinHours: (j['fullSimuladoMinHours'] as num).toDouble(),
    );
  }

  /// [tamanho P/M/G][nível 0..2] em minutos.
  final List<List<int>> theoryMinutes;

  /// [nível 0..2]
  final List<double> minutesPerQuestion;

  /// [tamanho P/M/G]
  final List<int> questions;
  final double reviewShare;
  final double weight2AfterHours;
  final double weight1AfterHours;
  final int simuladoFromWeek;
  final int simuladoEveryWeeks;
  final int discursivaFromWeek;
  final double fullSimuladoMinHours;
}

class Catalog {
  Catalog({
    required this.version,
    required this.careers,
    required this.subjects,
    required this.topics,
    required this.leiSeca,
    required this.params,
    required this.levels,
  }) {
    for (final s in subjects) {
      _subjects[s.id] = s;
    }
    for (final t in topics) {
      _topics[t.id] = t;
    }
    for (final c in careers) {
      for (final o in c.cargos) {
        _options[o.id] = o;
        _optionCareer[o.id] = c;
        final ct = o.contest;
        if (ct != null) _contestOrder[o.id] = {for (var i = 0; i < ct.topicIds.length; i++) ct.topicIds[i]: i};
      }
    }
  }

  /// Monta o catálogo a partir do JSON embutido, aplicando os concursos embutidos e o catálogo extra.
  factory Catalog.fromJson(Map<String, dynamic> json, {Map<String, dynamic>? extras}) {
    final j = applyExtras(json, extras ?? const {});
    final topicsJson = j['topics'] as List;
    return Catalog(
      version: j['version'] as String,
      careers: [for (final c in j['careers'] as List) Career.fromJson(c as Map<String, dynamic>)],
      subjects: [for (final s in j['subjects'] as List) Subject.fromJson(s as Map<String, dynamic>)],
      topics: [
        for (var i = 0; i < topicsJson.length; i++) Topic.fromJson(topicsJson[i] as Map<String, dynamic>, i),
      ],
      leiSeca: [for (final s in j['leiSeca'] as List) s as String],
      params: MethodParams.fromJson(j['params'] as Map<String, dynamic>),
      levels: [for (final s in j['levels'] as List) s as String],
    );
  }

  final String version;
  final List<Career> careers;
  final List<Subject> subjects;
  final List<Topic> topics;
  final List<String> leiSeca;
  final MethodParams params;
  final List<String> levels;
  final Map<String, Subject> _subjects = {};
  final Map<String, Topic> _topics = {};
  final Map<String, Cargo> _options = {};
  final Map<String, Career> _optionCareer = {};
  final Map<String, Map<String, int>> _contestOrder = {};

  Subject subject(String id) => _subjects[id]!;
  Subject? subjectOrNull(String id) => _subjects[id];
  Topic? topic(String id) => _topics[id];

  List<String> get esferas => const ['Federal', 'Estadual', 'Municipal'];

  List<Career> careersOf(String esfera) => careers.where((c) => c.esfera == esfera && c.cargos.isNotEmpty).toList();

  Career career(String code) => careers.firstWhere((c) => c.code == code);

  Career? careerOrNull(String code) {
    for (final c in careers) {
      if (c.code == code) return c;
    }
    return null;
  }

  Cargo cargo(String optionId) => _options[optionId]!;
  Cargo? cargoOrNull(String optionId) => _options[optionId];
  Career? careerOfOption(String optionId) => _optionCareer[optionId];
  bool hasOption(String optionId) => _options.containsKey(optionId);

  /// Todos os concursos pós-edital, do mais próximo ao mais distante.
  List<Cargo> get contests {
    final list = _options.values.where((o) => o.isContest).toList();
    list.sort((a, b) {
      final da = a.contest!.examDate, db = b.contest!.examDate;
      if (da == null || db == null) return da == null ? (db == null ? a.name.compareTo(b.name) : 1) : -1;
      return da.compareTo(db);
    });
    return list;
  }

  /// O assunto entra no plano deste cargo/concurso?
  bool topicApplies(Topic t, String careerCode, String optionId) {
    final order = _contestOrder[optionId];
    if (order != null) return order.containsKey(t.id);
    if (t.contest != null) return false;
    return t.appliesTo(careerCode, optionId);
  }

  /// Assuntos para listas de escolha: os do plano do aluno quando a matéria está no plano; senão, os do catálogo.
  List<Topic> topicsToPick(String subjectId, String careerCode, String optionId) {
    final s = subjectOrNull(subjectId);
    if (s != null && s.weightFor(optionId) > 0) return topicsFor(subjectId, careerCode, optionId);
    return topicsOf(subjectId);
  }

  /// Posição do assunto no edital (só para concursos; null no ciclo básico).
  int? contestPosition(String optionId, String topicId) => _contestOrder[optionId]?[topicId];

  List<Topic> topicsOf(String subjectId) => topics.where((t) => t.subjectId == subjectId && t.contest == null).toList();

  /// Assuntos de uma matéria que valem para o cargo/concurso, na ordem certa (edital ou catálogo).
  List<Topic> topicsFor(String subjectId, String careerCode, String optionId) {
    final list = topics.where((t) => t.subjectId == subjectId && topicApplies(t, careerCode, optionId)).toList();
    final order = _contestOrder[optionId];
    if (order != null) list.sort((a, b) => order[a.id]!.compareTo(order[b.id]!));
    return list;
  }
}
