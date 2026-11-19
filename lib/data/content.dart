/// Conteúdos (apostilas, mapas mentais, questões). Vêm embutidos no app (assets/content)
/// e, no futuro, de pacotes baixados para a pasta de dados ("conteudos/<pacote>/index.json").
library;

class ContentBlock {
  ContentBlock(this.type, this.raw);
  factory ContentBlock.fromJson(Map<String, dynamic> j) => ContentBlock(j['t'] as String, j);

  /// h2, h3, p, bullets, callout, table, note, mindmap, image
  final String type;
  final Map<String, dynamic> raw;

  String get text => raw['text'] as String? ?? '';
  String get title => raw['title'] as String? ?? '';
  String get style => raw['style'] as String? ?? '';
  List<String> get items => [for (final x in raw['items'] as List? ?? const []) x as String];
  List<String> get head => [for (final x in raw['head'] as List? ?? const []) x as String];
  List<List<String>> get rows => [
        for (final r in raw['rows'] as List? ?? const []) [for (final c in r as List) c as String],
      ];
  List<double> get widths => [for (final w in raw['widths'] as List? ?? const []) (w as num).toDouble()];
}

class ContentSection {
  ContentSection({required this.id, required this.title, required this.blocks});
  factory ContentSection.fromJson(Map<String, dynamic> j) => ContentSection(
        id: j['id'] as String,
        title: j['title'] as String,
        blocks: [for (final b in j['blocks'] as List) ContentBlock.fromJson(b as Map<String, dynamic>)],
      );
  final String id;
  final String title;
  final List<ContentBlock> blocks;
}

class MindBranch {
  MindBranch(this.label, this.items);
  final String label;
  final List<String> items;
}

class MindMapSpec {
  MindMapSpec({required this.root, required this.rootSub, required this.left, required this.right});
  factory MindMapSpec.fromJson(Map<String, dynamic> j) {
    List<MindBranch> side(String k) => [
          for (final b in j[k] as List? ?? const [])
            MindBranch((b as Map<String, dynamic>)['label'] as String, [for (final i in b['items'] as List) i as String]),
        ];
    return MindMapSpec(root: j['root'] as String, rootSub: j['rootSub'] as String? ?? '', left: side('left'), right: side('right'));
  }
  final String root;
  final String rootSub;
  final List<MindBranch> left;
  final List<MindBranch> right;
}

class QuizQuestion {
  QuizQuestion({
    required this.id,
    required this.text,
    required this.answer,
    required this.comment,
    this.group = '',
    this.context = '',
    this.options = const [],
  });
  factory QuizQuestion.fromJson(Map<String, dynamic> j) => QuizQuestion(
        id: j['id'] as String,
        text: j['text'] as String,
        answer: j['answer'] as String,
        comment: j['comment'] as String? ?? '',
        group: j['group'] as String? ?? '',
        context: j['context'] as String? ?? '',
        options: [for (final o in j['options'] as List? ?? const []) o as String],
      );

  /// Alternativas (A a E) da questão de múltipla escolha. Vazio = item certo/errado.
  final List<String> options;
  bool get isChoice => options.isNotEmpty;

  /// Letras das alternativas.
  List<String> get letters => [for (var i = 0; i < options.length; i++) String.fromCharCode(65 + i)];

  /// Texto de apoio exibido antes do item (interpretação de texto).
  final String context;

  /// Bloco da questão (ex.: "Bloco A · inéditas"). Vazio = sem blocos.
  final String group;
  final String id;
  final String text;

  /// 'C' ou 'E' (certo/errado) ou a letra da alternativa correta (múltipla escolha).
  final String answer;
  final String comment;
}

class Quiz {
  Quiz({required this.style, required this.banca, required this.instructions, required this.questions, this.penalty = true});
  factory Quiz.fromJson(Map<String, dynamic> j) => Quiz(
        style: j['style'] as String? ?? 'CE',
        banca: j['banca'] as String? ?? '',
        instructions: j['instructions'] as String? ?? '',
        questions: [for (final q in j['questions'] as List) QuizQuestion.fromJson(q as Map<String, dynamic>)],
        penalty: j['penalty'] as bool? ?? true,
      );

  /// Se um item certo/errado errado anula um certo (padrão Cebraspe). Múltipla escolha nunca desconta.
  final bool penalty;
  final String style;
  final String banca;
  final String instructions;
  final List<QuizQuestion> questions;
}

/// Resumo de um material (lista da biblioteca).
class MaterialInfo {
  MaterialInfo({
    required this.id,
    required this.folder,
    required this.title,
    required this.subtitle,
    required this.subjectId,
    required this.topicIds,
    required this.kind,
    required this.minutes,
    required this.questions,
    required this.version,
    required this.status,
    required this.source,
    this.variants = const [],
  });

  factory MaterialInfo.fromJson(Map<String, dynamic> j, String source) => MaterialInfo(
        id: j['id'] as String,
        folder: j['folder'] as String,
        title: j['title'] as String,
        subtitle: j['subtitle'] as String? ?? '',
        subjectId: j['subjectId'] as String,
        topicIds: [for (final t in j['topicIds'] as List? ?? const []) t as String],
        kind: j['kind'] as String? ?? 'apostila',
        minutes: (j['minutes'] as num? ?? 0).toInt(),
        questions: (j['questions'] as num? ?? 0).toInt(),
        version: j['version'] as String? ?? '',
        status: j['status'] as String? ?? '',
        source: source,
        variants: [for (final v in j['variants'] as List? ?? const []) v as String],
      );

  /// Versões por banca disponíveis ('cebraspe' é a base, em material.json; as outras ficam em material.<versão>.json).
  final List<String> variants;

  final String id;
  final String folder;
  final String title;
  final String subtitle;
  final String subjectId;
  final List<String> topicIds;

  /// 'aprofundado' (estudo inicial) ou 'resumo' (revisão).
  final String kind;

  bool get isDeep => kind == 'aprofundado';
  String get kindLabel => isDeep ? 'APROFUNDADO · ESTUDO INICIAL' : 'RESUMO · REVISÃO';
  final int minutes;
  final int questions;
  final String version;

  /// Situação de revisão embutida no app ("Em revisão pelo autor" ou "Revisado/Aprovado pelo autor").
  /// O dono pode mudar pelo app (catálogo extra, chave "review"), sem nova versão.
  final String status;

  bool get builtinApproved {
    final s = status.toLowerCase();
    return s.startsWith('aprovado') || s.startsWith('revisado');
  }

  /// 'asset' (embutido no app) ou caminho da pasta do pacote local.
  final String source;
}

/// Material completo (aberto no leitor).
class StudyMaterial {
  StudyMaterial({
    required this.info,
    required this.sections,
    required this.mindmap,
    required this.quiz,
    required this.pdf,
    required this.sources,
    required this.videos,
    this.variant = 'cebraspe',
  });

  factory StudyMaterial.fromJson(MaterialInfo info, Map<String, dynamic> j, {String variant = 'cebraspe'}) => StudyMaterial(
        info: info,
        variant: variant,
        sections: [for (final s in j['sections'] as List? ?? const []) ContentSection.fromJson(s as Map<String, dynamic>)],
        mindmap: j['mindmap'] == null ? null : MindMapSpec.fromJson(j['mindmap'] as Map<String, dynamic>),
        quiz: j['quiz'] == null ? null : Quiz.fromJson(j['quiz'] as Map<String, dynamic>),
        pdf: j['pdf'] as String?,
        sources: [for (final s in j['sources'] as List? ?? const []) s as String],
        videos: [
          for (final v in j['videos'] as List? ?? const [])
            (title: (v as Map<String, dynamic>)['title'] as String, url: v['url'] as String),
        ],
      );

  final MaterialInfo info;

  /// Versão por banca que foi aberta.
  final String variant;
  final List<ContentSection> sections;
  final MindMapSpec? mindmap;
  final Quiz? quiz;

  /// Nome do PDF dentro da pasta do material.
  final String? pdf;
  final List<String> sources;

  /// Videoaulas vinculadas (link externo). Estrutura pronta para os próximos conteúdos.
  final List<({String title, String url})> videos;
}
