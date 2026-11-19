import 'dart:async';
import 'dart:convert';
import 'dart:io';
import 'dart:math' as math;

import 'package:flutter/services.dart';
import 'package:flutter/widgets.dart';

import '../core/bancas.dart';
import '../core/catalog.dart';
import '../core/dates.dart';
import '../core/extras.dart';
import '../core/models.dart';
import '../core/planner.dart';
import '../core/stats.dart';
import '../data/catalog_store.dart';
import '../data/content.dart';
import '../data/storage.dart';

const kAppVersion = '0.9.1';
const kAppChannel = 'Beta de testes';

/// Última versão publicada (GitHub Releases). O app compara a tag (ex.: v0.3.0) com [kAppVersion].
const kUpdateApiUrl = 'https://api.github.com/repos/cruzdelima/Mentor-Policial/releases/latest';

/// Links fixos que sempre baixam a versão mais recente.
const kDownloadWindows = 'https://github.com/cruzdelima/Mentor-Policial/releases/latest/download/Taticum-Setup.exe';
const kDownloadMac = 'https://github.com/cruzdelima/Mentor-Policial/releases/latest/download/Taticum-macOS.dmg';

enum AppPage { qg, missions, edital, diary, materials, contests, settings, admin }

/// Aplica a escolha de cargo/concurso ao perfil. Concurso pós-edital preenche a data da prova e o nome.
void selectOption(Catalog cat, Profile p, String optionId, {DateTime? today}) {
  final prev = cat.cargoOrNull(p.optionId);
  final next = cat.cargo(optionId);
  final career = cat.careerOfOption(optionId)!;
  if (prev?.contest != null) {
    if (p.targetName == prev!.name) p.targetName = '';
    final d = prev.contest!.examDate;
    if (d != null && p.examDate != null && sameDay(p.examDate!, d)) p.examDate = null;
    p.baseOptionId = '';
  }
  p
    ..optionId = optionId
    ..careerCode = career.code
    ..esfera = career.esfera;
  final ct = next.contest;
  if (ct != null) {
    p.targetName = next.name;
    p.baseOptionId = ct.base;
    final d = ct.examDate;
    if (d != null && (today == null || d.isAfter(today))) p.examDate = d;
  }
}

/// Biblioteca de conteúdos: embutidos + pacotes locais.
class ContentLibrary {
  ContentLibrary(this.all);

  /// Todos os materiais (inclusive os ainda em revisão).
  final List<MaterialInfo> all;
  final Map<String, StudyMaterial> _cache = {};

  /// Visão do dono: mostra também os materiais em revisão.
  bool showAll = false;

  /// Decisões de revisão publicadas pelo dono (id → liberado), que valem sobre a situação embutida.
  Map<String, bool> review = const {};

  bool isApproved(MaterialInfo m) => review[m.id] ?? m.builtinApproved;

  /// Perfil de banca do aluno ('cebraspe', 'aocp' ou 'neutro'): define a versão dos materiais que abre.
  String banca = 'cebraspe';

  /// Versão escolhida pelo dono para conferir (null = a do perfil).
  String? preview;

  /// Versão do material que abre para esta pessoa: a da banca, ou a neutra, ou a base.
  String variantFor(MaterialInfo m) {
    final want = preview ?? banca;
    if (want == 'cebraspe') return 'cebraspe';
    if (m.variants.contains(want)) return want;
    if (m.variants.contains('neutro')) return 'neutro';
    return 'cebraspe';
  }

  /// Materiais que esta pessoa pode ver: alunos só veem os revisados.
  List<MaterialInfo> get items => showAll ? all : all.where(isApproved).toList();

  static Future<ContentLibrary> load(AssetBundle bundle, Storage storage) async {
    final items = <MaterialInfo>[];
    try {
      final j = jsonDecode(await bundle.loadString('assets/content/index.json')) as Map<String, dynamic>;
      for (final m in j['materials'] as List) {
        items.add(MaterialInfo.fromJson(m as Map<String, dynamic>, 'asset'));
      }
    } catch (e) {
      debugPrint('Conteúdo embutido indisponível: $e');
    }
    // Pacotes locais: <dados>/conteudos/<pacote>/index.json (atualização de conteúdo sem nova versão do app).
    try {
      if (await storage.packsDir.exists()) {
        for (final d in storage.packsDir.listSync().whereType<Directory>()) {
          final f = File(Storage.join(d.path, 'index.json'));
          if (!await f.exists()) continue;
          final j = jsonDecode(await f.readAsString()) as Map<String, dynamic>;
          for (final m in j['materials'] as List) {
            final info = MaterialInfo.fromJson(m as Map<String, dynamic>, d.path);
            items.removeWhere((x) => x.id == info.id);
            items.add(info);
          }
        }
      }
    } catch (e) {
      debugPrint('Pacote de conteúdo inválido: $e');
    }
    return ContentLibrary(items);
  }

  /// Materiais do assunto, com o aprofundado (estudo inicial) na frente.
  List<MaterialInfo> forTopic(String topicId) {
    final list = items.where((m) => m.topicIds.contains(topicId)).toList();
    return [...list.where((m) => m.isDeep), ...list.where((m) => !m.isDeep)];
  }

  /// Resumo (material de revisão) do primeiro assunto da lista que tiver um.
  MaterialInfo? reviewFor(List<String> topicIds) {
    for (final id in topicIds) {
      for (final m in items) {
        if (!m.isDeep && m.topicIds.contains(id)) return m;
      }
    }
    return null;
  }

  Future<StudyMaterial> open(MaterialInfo info, AssetBundle bundle) async {
    final v = variantFor(info);
    final key = '${info.id}@$v';
    final cached = _cache[key];
    if (cached != null) return cached;
    final file = v == 'cebraspe' ? 'material.json' : 'material.$v.json';
    String text;
    if (info.source == 'asset') {
      text = await bundle.loadString('assets/content/${info.folder}/$file');
    } else {
      text = await File(Storage.join(Storage.join(info.source, info.folder), file)).readAsString();
    }
    final m = StudyMaterial.fromJson(info, jsonDecode(text) as Map<String, dynamic>, variant: v);
    _cache[key] = m;
    return m;
  }

  /// Caminho do PDF no disco (copia do app para a pasta de dados quando necessário).
  Future<String?> pdfPath(StudyMaterial m, AssetBundle bundle, Storage storage) async {
    final pdf = m.pdf;
    if (pdf == null) return null;
    if (m.info.source != 'asset') return Storage.join(Storage.join(m.info.source, m.info.folder), pdf);
    final data = await bundle.load('assets/content/${m.info.folder}/$pdf');
    await storage.materialsDir.create(recursive: true);
    final suffix = m.variant == 'cebraspe' ? '' : '_${m.variant}';
    final name = 'Taticum_${m.info.folder}${suffix}_v${m.info.version}.pdf';
    final f = File(Storage.join(storage.materialsDir.path, name));
    if (!await f.exists() || await f.length() != data.lengthInBytes) {
      await f.writeAsBytes(data.buffer.asUint8List(data.offsetInBytes, data.lengthInBytes), flush: true);
    }
    return f.path;
  }
}

class AppController extends ChangeNotifier {
  AppController({
    required this.catalog,
    required this.storage,
    required this.data,
    required this.content,
    required this.bundle,
    DateTime Function()? clock,
    Map<String, dynamic>? catalogBase,
    Map<String, dynamic>? extras,
    this.extrasVersion = 0,
    this.remote,
    this.catalogStore,
  })  : clock = clock ?? DateTime.now,
        catalogBase = catalogBase ?? const {},
        extras = extras ?? emptyExtras() {
    _day = today;
    content.review = reviewOf(this.extras);
    _fixMissingOption();
    _recompute();
  }

  /// Dono: vê os materiais em revisão e pode liberá-los aos alunos.
  bool get reviewer => content.showAll;
  set reviewer(bool v) {
    if (content.showAll == v) return;
    content.showAll = v;
    notifyListeners();
  }

  /// Marca o material como revisado (liberado aos alunos) ou o recolhe para revisão. Publica na hora.
  Future<void> setReviewed(MaterialInfo m, bool approved) async {
    await refreshCatalog();
    final next = cloneJson(normalizeExtras(extras));
    (next['review'] as Map)[m.id] = approved;
    await publishCatalog(next, '${approved ? 'Material revisado e liberado' : 'Material recolhido para revisão'}: '
        '${m.title} (${m.isDeep ? 'aprofundado' : 'resumo'})');
  }

  /// Carrega os dados de estudo. [storage] = pasta da conta logada (padrão: pasta única, sem contas).
  /// [remote] = servidor do catálogo extra (null quando o app roda sem contas).
  static Future<AppController> load({Storage? storage, CatalogRemote? remote}) async {
    final bundle = rootBundle;
    final base = jsonDecode(await bundle.loadString('assets/catalog/catalog.json')) as Map<String, dynamic>;
    final store = CatalogStore(Storage.defaultDir());
    final cached = await store.read();
    Catalog catalog;
    try {
      catalog = Catalog.fromJson(base, extras: cached.data);
    } catch (_) {
      catalog = Catalog.fromJson(base);
    }
    storage ??= Storage(Storage.defaultDir());
    final data = await storage.load();
    final content = await ContentLibrary.load(bundle, storage);
    final c = AppController(
      catalog: catalog,
      storage: storage,
      data: data,
      content: content,
      bundle: bundle,
      catalogBase: base,
      extras: cached.data,
      extrasVersion: cached.version,
      remote: remote,
      catalogStore: store,
    );
    c._startClock();
    Future<void>.delayed(const Duration(seconds: 3), c._lookForUpdate);
    if (remote != null) Future<void>.delayed(const Duration(seconds: 1), c.refreshCatalog);
    return c;
  }

  Catalog catalog;

  /// Catálogo embutido no app (JSON) e o catálogo extra publicado pelo dono/administradores.
  final Map<String, dynamic> catalogBase;
  Map<String, dynamic> extras;
  int extrasVersion;
  final CatalogRemote? remote;
  final CatalogStore? catalogStore;
  final Storage storage;
  final ContentLibrary content;
  final AssetBundle bundle;
  final DateTime Function() clock;
  UserData data;

  /// Persistência desligada nos testes automatizados.
  bool persist = true;

  Trail? trail;
  Schedule? schedule;
  Stats? stats;
  late DateTime _day;
  Timer? _timer;

  AppPage page = AppPage.qg;
  String? pendingMaterialId;
  DateTime? missionsFocus;

  DateTime get today => dateOnly(clock());
  bool get onboarded => data.profile != null;
  Profile get profile => data.profile!;
  Career get career => catalog.career(profile.careerCode);
  Cargo get cargo => catalog.cargo(profile.optionId);

  void _startClock() {
    _timer = Timer.periodic(const Duration(minutes: 1), (_) {
      if (!sameDay(_day, today)) {
        _day = today;
        _recompute();
        notifyListeners();
      }
    });
  }

  @override
  void dispose() {
    _timer?.cancel();
    super.dispose();
  }

  // ---------------------------------------------------------------- catálogo extra

  /// Busca no servidor a versão publicada do catálogo extra e aplica se mudou.
  Future<bool> refreshCatalog() async {
    final r = remote;
    if (r == null) return false;
    try {
      final got = await r.fetchCatalog();
      if (got == null || got.version == extrasVersion) return false;
      _useExtras(normalizeExtras(got.data), got.version);
      return true;
    } catch (_) {
      return false; // sem internet: segue com o cache
    }
  }

  /// Publica um novo catálogo extra (editor do dono/administradores) e já aplica neste computador.
  Future<void> publishCatalog(Map<String, dynamic> newExtras, String note) async {
    final r = remote;
    if (r == null) throw StateError('Sem servidor configurado.');
    // Valida antes de enviar: se não montar aqui, não monta em nenhum aluno.
    Catalog.fromJson(catalogBase, extras: newExtras);
    final v = await r.saveCatalog(newExtras, extrasVersion, note);
    _useExtras(normalizeExtras(newExtras), v);
  }

  void _useExtras(Map<String, dynamic> e, int version) {
    if (catalogBase.isEmpty) return;
    final Catalog next;
    try {
      next = Catalog.fromJson(catalogBase, extras: e);
    } catch (_) {
      return;
    }
    extras = e;
    extrasVersion = version;
    content.review = reviewOf(e);
    catalogStore?.write(e, version);
    catalog = next;
    if (_fixMissingOption()) {
      _changed();
    } else {
      _recompute();
      notifyListeners();
    }
  }

  /// Se o concurso/cargo do aluno foi removido do catálogo, volta para o cargo de referência.
  bool _fixMissingOption() {
    final p = data.profile;
    if (p == null || catalog.hasOption(p.optionId)) return false;
    String? opt = catalog.hasOption(p.baseOptionId) ? p.baseOptionId : null;
    opt ??= catalog.careerOrNull(p.careerCode)?.cycleCargos.firstOrNull?.id;
    opt ??= catalog.careers.expand((c) => c.cycleCargos).first.id;
    final career = catalog.careerOfOption(opt)!;
    p
      ..optionId = opt
      ..careerCode = career.code
      ..esfera = career.esfera;
    data.anchorDate = _anchorFor(p);
    data.doneAtAnchor = data.unitDone.keys.toSet();
    data.planSignature = p.planSignature;
    return true;
  }

  /// Troca o plano para um cargo do ciclo básico ou para um concurso pós-edital, sem perder o progresso.
  void studyFor(String optionId) {
    final p = profile.copy();
    selectOption(catalog, p, optionId, today: today);
    updateProfile(p);
  }

  /// Nome da banca que orienta os materiais: a do concurso pós-edital ou, no ciclo básico, a do último concurso da carreira.
  String get bancaName {
    if (data.profile == null) return '';
    final ct = catalog.cargoOrNull(profile.optionId)?.contest;
    if (ct != null && ct.banca.trim().isNotEmpty) return ct.banca;
    return catalog.careerOfOption(profile.optionId)?.banca ?? '';
  }

  void _recompute() {
    final p = data.profile;
    content.banca = bancaProfileOf(bancaName);
    if (p == null) {
      trail = null;
      schedule = null;
      stats = null;
      return;
    }
    final t = Planner.buildTrail(catalog, p, data.overrides);
    trail = t;
    schedule = Schedule(catalog: catalog, trail: t, profile: p, data: data, today: today);
    stats = Stats(catalog, data, t, today);
  }

  void _changed() {
    _recompute();
    notifyListeners();
    if (persist) storage.save(data);
  }

  void goTo(AppPage p, {String? materialId, DateTime? day}) {
    page = p;
    pendingMaterialId = materialId;
    missionsFocus = day;
    notifyListeners();
  }

  // ---------------------------------------------------------------- perfil e plano

  DateTime _anchorFor(Profile p) {
    final t = today;
    if (t.isBefore(p.startDate)) return p.startDate;
    final didToday = data.unitDone.values.any((d) => sameDay(d.date, t));
    return didToday ? addDays(t, 1) : t;
  }

  void completeOnboarding(Profile p) {
    data.profile = p;
    data.anchorDate = today.isBefore(p.startDate) ? p.startDate : today;
    data.doneAtAnchor = data.unitDone.keys.toSet();
    data.planSignature = p.planSignature;
    page = AppPage.qg;
    _changed();
  }

  /// Atualiza o perfil. Se algo que muda a trilha foi alterado, replaneja a partir de hoje.
  void updateProfile(Profile p) {
    final changed = p.planSignature != data.planSignature;
    data.profile = p;
    if (changed) {
      data.anchorDate = _anchorFor(p);
      data.doneAtAnchor = data.unitDone.keys.toSet();
      data.planSignature = p.planSignature;
    }
    _changed();
  }

  /// Recomeça o cronograma a partir de hoje, com as missões pendentes na ordem do ciclo.
  void replan() {
    data.anchorDate = _anchorFor(profile);
    data.doneAtAnchor = data.unitDone.keys.toSet();
    data.planSignature = profile.planSignature;
    _changed();
  }

  void _replanQuiet() {
    data.anchorDate = _anchorFor(profile);
    data.doneAtAnchor = data.unitDone.keys.toSet();
  }

  // ---------------------------------------------------------------- missões e tarefas

  bool isUnitDone(Unit u) => data.unitDone.containsKey(u.id);
  bool isTaskDone(String key) => data.taskDone.containsKey(key);

  void completeUnit(Unit u, {int questions = 0, int correct = 0, required int minutes, String source = '', String notes = ''}) {
    if (isUnitDone(u)) return;
    final e = DiaryEntry(
      id: data.nextId('d'),
      date: today,
      type: u.isTheory ? 'Teoria' : 'Questões',
      subjectId: u.subject.id,
      topicIds: [u.topic.id],
      questions: questions,
      correct: math.min(correct, questions),
      minutes: minutes,
      source: source,
      notes: notes,
      origin: 'unit:${u.id}',
    );
    data.diary.add(e);
    data.unitDone[u.id] = Done(today, e.id);
    _changed();
  }

  void undoUnit(Unit u) {
    final d = data.unitDone.remove(u.id);
    if (d?.entryId != null) data.diary.removeWhere((e) => e.id == d!.entryId);
    _changed();
  }

  void completeTask(DayTask t, {int questions = 0, int correct = 0, int? minutes, String notes = ''}) {
    if (isTaskDone(t.key)) return;
    String? entryId;
    if (t.diaryType != null) {
      final subjects = {for (final id in t.topicIds) catalog.topic(id)?.subjectId};
      final e = DiaryEntry(
        id: data.nextId('d'),
        date: today,
        type: t.diaryType!,
        subjectId: subjects.length == 1 ? subjects.first : null,
        topicIds: t.topicIds,
        questions: questions,
        correct: math.min(correct, questions),
        minutes: minutes ?? t.minutes,
        source: t.code == 'LEI' ? 'Lei seca' : (t.code == 'SIM' ? 'Simulado' : ''),
        notes: notes.isNotEmpty ? notes : (t.code == 'LEI' ? t.detail : t.title),
        origin: 'task:${t.key}',
      );
      data.diary.add(e);
      entryId = e.id;
    }
    data.taskDone[t.key] = Done(today, entryId);
    _changed();
  }

  void undoTask(String key) {
    final d = data.taskDone.remove(key);
    if (d?.entryId != null) data.diary.removeWhere((e) => e.id == d!.entryId);
    _changed();
  }

  // ---------------------------------------------------------------- diário

  void addEntry(DiaryEntry e) {
    data.diary.add(e);
    _changed();
  }

  void updateEntry(DiaryEntry e) {
    final i = data.diary.indexWhere((x) => x.id == e.id);
    if (i >= 0) data.diary[i] = e;
    _changed();
  }

  void deleteEntry(DiaryEntry e) {
    data.diary.removeWhere((x) => x.id == e.id);
    data.unitDone.removeWhere((k, v) => v.entryId == e.id);
    data.taskDone.removeWhere((k, v) => v.entryId == e.id);
    _changed();
  }

  String newId(String prefix) => data.nextId(prefix);

  // ---------------------------------------------------------------- edital

  TopicOverride _ov(String id) => data.overrides[id] ??= TopicOverride();

  void setSkip(String topicId, bool skip) {
    _ov(topicId).skip = skip;
    _replanQuiet();
    _changed();
  }

  void setSize(String topicId, String? size) {
    final t = catalog.topic(topicId);
    _ov(topicId).size = (size == null || size == t?.size) ? null : size;
    _replanQuiet();
    _changed();
  }

  void setTopicNotes(String topicId, String notes) {
    _ov(topicId).notes = notes;
    _changed();
  }

  // ---------------------------------------------------------------- materiais e questões

  QuizAttempt submitQuiz(StudyMaterial m, Map<String, String?> answers, {int minutes = 0}) {
    final quiz = m.quiz!;
    var c = 0, w = 0, b = 0, pen = 0;
    for (final q in quiz.questions) {
      final a = answers[q.id];
      if (a == null) {
        b++;
      } else if (a == q.answer) {
        c++;
      } else {
        w++;
        if (quiz.penalty && !q.isChoice) pen++;
      }
    }
    final attempt = QuizAttempt(date: today, answers: Map.of(answers), correct: c, wrong: w, blank: b, penalized: pen);
    (data.quizzes[m.info.id] ??= []).add(attempt);
    if (c + w > 0) {
      data.diary.add(DiaryEntry(
        id: data.nextId('d'),
        date: today,
        type: 'Questões',
        subjectId: m.info.subjectId,
        topicIds: m.info.topicIds,
        questions: c + w,
        correct: c,
        minutes: minutes > 0 ? minutes : ((c + w) * 3),
        source: 'Material do app',
        notes: '${m.info.title} · ${quiz.penalty ? 'líquida ${c - pen}' : '$c acertos'}${b > 0 ? ' · $b em branco' : ''}',
        origin: 'quiz:${m.info.id}',
      ));
    }
    _changed();
    return attempt;
  }

  List<QuizAttempt> attemptsOf(String materialId) => data.quizzes[materialId] ?? const [];

  void setReadProgress(String materialId, int section) {
    final cur = data.readProgress[materialId] ?? -1;
    if (section > cur) {
      data.readProgress[materialId] = section;
      if (persist) storage.save(data);
    }
  }

  void addUserMaterial(UserMaterial m) {
    data.materials.add(m);
    _changed();
  }

  void removeUserMaterial(UserMaterial m) {
    data.materials.removeWhere((x) => x.id == m.id);
    _changed();
  }

  Future<String?> pdfPathOf(StudyMaterial m) => content.pdfPath(m, bundle, storage);

  // ---------------------------------------------------------------- dados

  Future<String> exportBackup() => storage.exportBackup(data);

  Future<void> importBackup(String path) async {
    final d = await storage.readBackup(path);
    data = d;
    _changed();
  }

  void resetAll() {
    data = UserData();
    page = AppPage.qg;
    _changed();
  }

  /// Versão nova encontrada no GitHub (null = nenhuma ou sem internet).
  ({String version, String url})? update;
  bool updateDismissed = false;

  Future<void> _lookForUpdate() async {
    if (Storage.isStorePackage) return; // a Microsoft Store atualiza sozinha
    final u = await checkUpdate();
    if (u != null) {
      update = u;
      notifyListeners();
    }
  }

  void dismissUpdate() {
    updateDismissed = true;
    notifyListeners();
  }

  /// Consulta a última versão publicada. Falhas (sem internet, limite da API) são ignoradas.
  Future<({String version, String url})?> checkUpdate() async {
    final client = HttpClient()
      ..connectionTimeout = const Duration(seconds: 6)
      ..userAgent = 'Taticum/$kAppVersion';
    try {
      final req = await client.getUrl(Uri.parse(kUpdateApiUrl));
      req.headers.set('Accept', 'application/vnd.github+json');
      final res = await req.close().timeout(const Duration(seconds: 10));
      if (res.statusCode != 200) return null;
      final j = jsonDecode(await res.transform(utf8.decoder).join()) as Map<String, dynamic>;
      final v = (j['tag_name'] as String? ?? '').replaceFirst(RegExp('^[vV]'), '');
      if (_newer(v, kAppVersion)) return (version: v, url: Platform.isMacOS ? kDownloadMac : kDownloadWindows);
      return null;
    } catch (_) {
      return null;
    } finally {
      client.close();
    }
  }

  static bool _newer(String a, String b) {
    List<int> p(String s) => [for (final x in s.split('.')) int.tryParse(x) ?? 0];
    final x = p(a), y = p(b);
    for (var i = 0; i < 3; i++) {
      final xi = i < x.length ? x[i] : 0, yi = i < y.length ? y[i] : 0;
      if (xi != yi) return xi > yi;
    }
    return false;
  }
}

/// Disponibiliza o controlador para a árvore de widgets.
class AppScope extends InheritedNotifier<AppController> {
  const AppScope({super.key, required AppController controller, required super.child}) : super(notifier: controller);

  static AppController of(BuildContext context) => context.dependOnInheritedWidgetOfExactType<AppScope>()!.notifier!;

  static AppController read(BuildContext context) => context.getInheritedWidgetOfExactType<AppScope>()!.notifier!;
}
