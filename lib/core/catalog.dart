/// Catálogo: carreiras, cargos, matérias, tópicos e parâmetros do método.
/// Vem de assets/catalog/catalog.json e, no futuro, poderá ser atualizado por pacotes de conteúdo.
library;

class Cargo {
  const Cargo(this.id, this.name);
  final String id;
  final String name;
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
        cargos: [
          for (final c in j['cargos'] as List) Cargo(c['id'] as String, c['name'] as String),
        ],
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
  });

  factory Topic.fromJson(Map<String, dynamic> j, int index) => Topic(
        id: j['id'] as String,
        subjectId: j['subject'] as String,
        n: (j['n'] as num).toInt(),
        name: j['name'] as String,
        size: j['size'] as String,
        scope: [for (final s in j['scope'] as List) s as String],
        index: index,
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
  }

  factory Catalog.fromJson(Map<String, dynamic> j) {
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

  Subject subject(String id) => _subjects[id]!;
  Subject? subjectOrNull(String id) => _subjects[id];
  Topic? topic(String id) => _topics[id];

  List<String> get esferas => const ['Federal', 'Estadual', 'Municipal'];

  List<Career> careersOf(String esfera) => careers.where((c) => c.esfera == esfera).toList();

  Career career(String code) => careers.firstWhere((c) => c.code == code);

  Cargo cargo(String optionId) => careers.expand((c) => c.cargos).firstWhere((c) => c.id == optionId);

  List<Topic> topicsOf(String subjectId) => topics.where((t) => t.subjectId == subjectId).toList();
}
