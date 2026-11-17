// CFO (PM e BM), modo pós-edital e editor de catálogo.
import 'dart:convert';
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:mentor_policial/app.dart';
import 'package:mentor_policial/core/catalog.dart';
import 'package:mentor_policial/core/extras.dart';
import 'package:mentor_policial/core/models.dart';
import 'package:mentor_policial/core/planner.dart';
import 'package:mentor_policial/data/catalog_store.dart';
import 'package:mentor_policial/data/storage.dart';
import 'package:mentor_policial/state/app_state.dart';
import 'package:mentor_policial/ui/pages/catalog_editor.dart';

class DiskBundle extends CachingAssetBundle {
  @override
  Future<ByteData> load(String key) async {
    final bytes = await File(key).readAsBytes();
    return ByteData.view(bytes.buffer);
  }
}

/// Servidor de catálogo de mentira (guarda na memória).
class FakeRemote implements CatalogRemote {
  Map<String, dynamic>? data;
  int version = 0;
  @override
  Future<({Map<String, dynamic> data, int version})?> fetchCatalog() async => data == null ? null : (data: data!, version: version);
  @override
  Future<int> saveCatalog(Map<String, dynamic> d, int baseVersion, String note) async {
    if (baseVersion != version) throw StateError('conflito');
    data = cloneJson(d);
    return ++version;
  }
}

late Map<String, dynamic> base;
late Catalog catalog;
late ContentLibrary content;
final bundle = DiskBundle();
final now = DateTime(2026, 11, 18, 9);

Profile profileFor(String option) {
  final career = catalog.careerOfOption(option)!;
  final p = Profile(
    name: 'Teste',
    esfera: career.esfera,
    careerCode: career.code,
    optionId: 'PM_SD',
    hoursPerDay: 3,
    studyWeekdays: [1, 2, 3, 4, 5, 6],
    reviewWeekday: 6,
    level: 0,
    startDate: DateTime(2026, 11, 16),
  );
  selectOption(catalog, p, option, today: DateTime(2026, 11, 16));
  return p;
}

AppController controllerWith(UserData data, {CatalogRemote? remote, Map<String, dynamic>? extras}) {
  final storage = Storage(Directory.systemTemp.createTempSync('taticum_test'));
  return AppController(
    catalog: Catalog.fromJson(base, extras: extras),
    storage: storage,
    data: data,
    content: content,
    bundle: bundle,
    clock: () => now,
    catalogBase: base,
    extras: extras,
    remote: remote,
  )..persist = false;
}

Future<void> loadFont(String family, List<String> files) async {
  final loader = FontLoader(family);
  for (final f in files) {
    loader.addFont(File('assets/fonts/$f.ttf').readAsBytes().then((b) => ByteData.view(b.buffer)));
  }
  await loader.load();
}

void main() {
  setUpAll(() async {
    base = jsonDecode(File('assets/catalog/catalog.json').readAsStringSync()) as Map<String, dynamic>;
    catalog = Catalog.fromJson(base);
    content = await ContentLibrary.load(bundle, Storage(Directory.systemTemp.createTempSync('taticum_c')));
    await loadFont('Barlow', ['Barlow-Regular', 'Barlow-Medium', 'Barlow-SemiBold', 'Barlow-Bold']);
    await loadFont('BarlowCondensed', ['BarlowCondensed-Medium', 'BarlowCondensed-SemiBold', 'BarlowCondensed-Bold']);
  });

  test('CFO da PM e do Bombeiro no ciclo básico', () {
    expect(catalog.career('PM').cycleCargos.map((c) => c.id), containsAll(['PM_SD', 'PM_CFO']));
    expect(catalog.career('BM').cycleCargos.map((c) => c.id), containsAll(['BM_SD', 'BM_CFO']));
    expect(catalog.subject('DPM').weightFor('PM_CFO'), 2);
    expect(catalog.subject('FIS').weightFor('BM_CFO'), 3);
    // Direito Penal Militar em noções é só do soldado; o oficial estuda a matéria inteira.
    final inst7 = catalog.topic('INST-07')!;
    expect(catalog.topicApplies(inst7, 'PM', 'PM_SD'), isTrue);
    expect(catalog.topicApplies(inst7, 'PM', 'PM_CFO'), isFalse);
    for (final o in ['PM_CFO', 'BM_CFO']) {
      final t = Planner.buildTrail(catalog, profileFor(o), const {});
      expect(t.units.length, greaterThan(200), reason: o);
    }
  });

  test('pós-edital: CFO CBMPE segue o edital', () {
    final c = catalog.cargo('CBMPE26_TEN');
    expect(c.isContest, isTrue);
    expect(catalog.careerOfOption(c.id)!.code, 'BM');
    expect(c.contest!.totalQuestions, 70);
    expect(c.contest!.examDate, DateTime(2027, 2, 28));
    final p = profileFor('CBMPE26_TEN');
    expect(p.examDate, DateTime(2027, 2, 28));
    expect(p.targetName, c.name);
    expect(p.baseOptionId, 'BM_CFO');
    final t = Planner.buildTrail(catalog, p, const {});
    expect(t.activeTopics.map((x) => x.id).toSet(), c.contest!.topicIds.toSet());
    // Ordem do edital dentro de cada matéria.
    final lp = t.units.where((u) => u.subject.id == 'LP' && u.isTheory).map((u) => u.topic.id).toList();
    expect(lp.take(3).toList(), ['LP-05', 'LP-15', 'CBMPE26_TEN:figuras-de-linguagem']);
    // Assuntos exclusivos do edital não aparecem no ciclo básico.
    final bm = Planner.buildTrail(catalog, profileFor('BM_CFO'), const {});
    expect(bm.activeTopics.any((x) => x.contest != null), isFalse);
    // Voltar ao ciclo limpa nome e data do concurso.
    selectOption(catalog, p, 'BM_CFO', today: DateTime(2026, 11, 16));
    expect(p.targetName, '');
    expect(p.examDate, isNull);
  });

  test('catálogo extra: área, matéria, cargo, concurso e ocultos', () {
    final ex = {
      'areas': [
        {'code': 'PCIENT', 'name': 'Polícia Científica', 'esfera': 'Estadual'},
      ],
      'subjects': [
        {'id': 'HPE', 'name': 'História de Pernambuco', 'color': 'FDBA74'},
      ],
      'cargos': [
        {'id': 'PCIENT_PERITO', 'career': 'PCIENT', 'name': 'Perito', 'weights': {'LP': 3, 'QUI': 2, 'HPE': 1}},
      ],
      'contests': [
        {
          'id': 'CFO_PMPE',
          'career': 'PM',
          'base': 'PM_CFO',
          'name': 'CFO PMPE 2026',
          'examDate': '2027-02-28',
          'subjects': [
            {
              'id': 'LP',
              'weight': 3,
              'questions': 10,
              'topics': [
                {'ref': 'LP-05'},
                {'name': 'Figuras de linguagem', 'size': 'P'},
              ],
            },
            {
              'id': 'HPE',
              'weight': 1,
              'questions': 5,
              'topics': [
                {'name': 'Revolução Pernambucana'},
              ],
            },
            {
              'id': 'NAO_EXISTE',
              'topics': [
                {'name': 'x'},
              ],
            },
          ],
        },
      ],
      'hidden': ['GCM', 'CBMPE26_TEN'],
    };
    final cat = Catalog.fromJson(base, extras: ex);
    expect(cat.careerOrNull('PCIENT')!.cargos.single.id, 'PCIENT_PERITO');
    expect(cat.careerOrNull('GCM'), isNull);
    expect(cat.hasOption('CBMPE26_TEN'), isFalse);
    expect(cat.cargo('CFO_PMPE').contest!.topicIds, ['LP-05', 'CFO_PMPE:figuras-de-linguagem', 'CFO_PMPE:revolucao-pernambucana']);
    expect(cat.subject('HPE').weightFor('CFO_PMPE'), 1);
    // Lixo vindo da rede não derruba o catálogo.
    expect(Catalog.fromJson(base, extras: {'contests': 'x', 'areas': [1, 2]}).careers.length, catalog.careers.length);
  });

  test('concurso removido do catálogo: aluno volta ao cargo de referência', () async {
    final p = profileFor('CBMPE26_TEN');
    final remote = FakeRemote()
      ..data = {
        'hidden': ['CBMPE26_TEN'],
      }
      ..version = 3;
    final app = controllerWith(UserData(profile: p, anchorDate: p.startDate, planSignature: p.planSignature), remote: remote);
    expect(app.profile.optionId, 'CBMPE26_TEN');
    expect(await app.refreshCatalog(), isTrue);
    expect(app.extrasVersion, 3);
    expect(app.profile.optionId, 'BM_CFO');
    expect(app.trail!.units, isNotEmpty);
    // Publicar: versão sobe e o catálogo é aplicado na hora.
    await app.publishCatalog({'hidden': <dynamic>[]}, 'teste');
    expect(app.extrasVersion, 4);
    expect(app.catalog.hasOption('CBMPE26_TEN'), isTrue);
  });

  testWidgets('telas no modo pós-edital e volta ao ciclo básico', (tester) async {
    for (final size in const [Size(1366, 768), Size(1180, 720)]) {
      tester.view.physicalSize = size;
      tester.view.devicePixelRatio = 1.0;
      addTearDown(tester.view.reset);
      final p = profileFor('CBMPE26_TEN');
      final app = controllerWith(UserData(profile: p, anchorDate: p.startDate, planSignature: p.planSignature));
      await tester.pumpWidget(MentorApp(controller: app));
      await tester.pumpAndSettle();
      for (final page in AppPage.values) {
        app.goTo(page);
        await tester.pumpAndSettle();
        expect(tester.takeException(), isNull, reason: '$page em $size');
      }
      app.goTo(AppPage.contests);
      await tester.pumpAndSettle();
      expect(find.text('SEU CONCURSO'), findsOneWidget);
      await tester.tap(find.text('VOLTAR AO CICLO BÁSICO'));
      await tester.pumpAndSettle();
      await tester.tap(find.text('VOLTAR'));
      await tester.pumpAndSettle();
      expect(app.profile.optionId, 'BM_CFO');
      await tester.ensureVisible(find.text('ESTUDAR PARA ESTE CONCURSO').first);
      await tester.pumpAndSettle();
      await tester.tap(find.text('ESTUDAR PARA ESTE CONCURSO').first);
      await tester.pumpAndSettle();
      await tester.tap(find.text('USAR ESTE EDITAL'));
      await tester.pumpAndSettle();
      expect(app.profile.optionId, 'CBMPE26_TEN');
      await tester.pump(const Duration(seconds: 4));
      await tester.pumpAndSettle();
    }
  });

  testWidgets('primeiro acesso escolhendo o CFO CBMPE', (tester) async {
    tester.view.physicalSize = const Size(1366, 768);
    tester.view.devicePixelRatio = 1.0;
    addTearDown(tester.view.reset);
    final app = controllerWith(UserData());
    await tester.pumpWidget(MentorApp(controller: app));
    await tester.pumpAndSettle();
    await tester.enterText(find.byType(TextField).first, 'Ana');
    await tester.pump();
    await tester.tap(find.text('COMEÇAR'));
    await tester.pumpAndSettle();
    await tester.tap(find.text('ESTADUAL'));
    await tester.pumpAndSettle();
    await tester.tap(find.text('CONTINUAR'));
    await tester.pumpAndSettle();
    await tester.tap(find.text('CORPO DE BOMBEIROS MILITAR'));
    await tester.pumpAndSettle();
    await tester.tap(find.text('CONTINUAR'));
    await tester.pumpAndSettle();
    expect(find.text('PÓS-EDITAL · CONCURSOS COM EDITAL PUBLICADO'), findsOneWidget);
    await tester.ensureVisible(find.text('CFO CBMPE 2026 — 2º TENENTE (QOC)'));
    await tester.pumpAndSettle();
    await tester.tap(find.text('CFO CBMPE 2026 — 2º TENENTE (QOC)'));
    await tester.pumpAndSettle();
    await tester.tap(find.text('CONTINUAR'));
    await tester.pumpAndSettle();
    await tester.tap(find.text('CONTINUAR'));
    await tester.pumpAndSettle();
    expect(find.text('SEU PLANO DE OPERAÇÃO'), findsOneWidget);
    await tester.tap(find.text('INICIAR OPERAÇÃO'));
    await tester.pumpAndSettle();
    expect(app.profile.optionId, 'CBMPE26_TEN');
    expect(app.profile.examDate, DateTime(2027, 2, 28));
    expect(tester.takeException(), isNull);
  });

  testWidgets('editor: cadastrar um concurso e publicar', (tester) async {
    tester.view.physicalSize = const Size(1366, 900);
    tester.view.devicePixelRatio = 1.0;
    addTearDown(tester.view.reset);
    final p = profileFor('PM_CFO');
    final remote = FakeRemote();
    final app = controllerWith(UserData(profile: p, anchorDate: p.startDate, planSignature: p.planSignature), remote: remote);
    await tester.pumpWidget(MaterialApp(home: AppScope(controller: app, child: const Scaffold(body: CatalogEditor()))));
    await tester.pumpAndSettle();
    expect(find.text('CATÁLOGO EM DIA'), findsOneWidget);

    await tester.tap(find.text('NOVO CONCURSO'));
    await tester.pumpAndSettle();
    await tester.enterText(find.widgetWithText(TextField, 'Nome do concurso'), 'CFO PMPE 2026');
    await tester.tap(find.widgetWithText(DropdownButtonFormField<String>, 'Área'));
    await tester.pumpAndSettle();
    await tester.tap(find.text('PM · Polícia Militar').last);
    await tester.pumpAndSettle();
    await tester.ensureVisible(find.widgetWithText(DropdownButtonFormField<String>, 'Matéria'));
    await tester.pumpAndSettle();
    await tester.tap(find.widgetWithText(DropdownButtonFormField<String>, 'Matéria'));
    await tester.pumpAndSettle();
    await tester.tap(find.text('Língua Portuguesa').last);
    await tester.pumpAndSettle();
    await tester.ensureVisible(find.widgetWithText(TextField, 'Assuntos (um por linha)'));
    await tester.pumpAndSettle();
    await tester.enterText(find.widgetWithText(TextField, 'Assuntos (um por linha)'), 'Compreensão e interpretação de textos\nFiguras de linguagem (P)');
    await tester.pumpAndSettle();
    expect(find.textContaining('1 aproveitados do ciclo básico'), findsOneWidget);
    await tester.tap(find.text('GUARDAR NO RASCUNHO'));
    await tester.pumpAndSettle();
    expect(find.text('ALTERAÇÕES NÃO PUBLICADAS'), findsOneWidget);
    expect(find.text('CFO PMPE 2026'), findsOneWidget);

    await tester.tap(find.text('PUBLICAR PARA TODOS'));
    await tester.pumpAndSettle();
    await tester.tap(find.text('PUBLICAR'));
    await tester.pumpAndSettle();
    expect(remote.version, 1);
    final c = app.catalog.cargo('CFO_PMPE_2026');
    expect(c.contest!.topicIds, ['LP-05', 'CFO_PMPE_2026:figuras-de-linguagem']);
    expect(app.catalog.topic('CFO_PMPE_2026:figuras-de-linguagem')!.size, 'P');
    expect(tester.takeException(), isNull);
    await tester.pump(const Duration(seconds: 4));
    await tester.pumpAndSettle();
  });
}
