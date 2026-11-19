// Testes automatizados (rodam no GitHub Actions com `flutter test`).
// Montam o app com dados de exemplo e percorrem todas as telas procurando erros de layout.
import 'dart:convert';
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:mentor_policial/app.dart';
import 'package:mentor_policial/core/catalog.dart';
import 'package:mentor_policial/core/dates.dart';
import 'package:mentor_policial/core/models.dart';
import 'package:mentor_policial/core/planner.dart';
import 'package:mentor_policial/data/storage.dart';
import 'package:mentor_policial/state/app_state.dart';
import 'package:mentor_policial/ui/pages/content_checklist.dart';
import 'package:mentor_policial/ui/theme.dart';

/// Lê os assets direto do disco (fora da zona de tempo simulado dos testes).
class DiskBundle extends CachingAssetBundle {
  @override
  Future<ByteData> load(String key) async {
    final bytes = await File(key).readAsBytes();
    return ByteData.view(bytes.buffer);
  }
}

late Catalog catalog;
late ContentLibrary content;
final bundle = DiskBundle();
final storage = Storage(Directory.systemTemp.createTempSync('mentor_test').path);
final now = DateTime(2026, 11, 18, 9);

Future<void> loadFont(String family, List<String> files) async {
  final loader = FontLoader(family);
  for (final f in files) {
    loader.addFont(File('assets/fonts/$f.ttf').readAsBytes().then((b) => ByteData.view(b.buffer)));
  }
  await loader.load();
}

Profile pfProfile() => Profile(
      name: 'Teste',
      esfera: 'Federal',
      careerCode: 'PF',
      optionId: 'PF_AG',
      hoursPerDay: 3,
      studyWeekdays: [1, 2, 3, 4, 5, 6],
      reviewWeekday: 6,
      level: 0,
      startDate: DateTime(2026, 11, 16),
      examDate: DateTime(2027, 9, 12),
      targetName: 'PF 2027',
    );

AppController controllerWith(UserData data) {
  final c = AppController(catalog: catalog, storage: storage, data: data, content: content, bundle: bundle, clock: () => now)..persist = false;
  return c;
}

Future<void> setWindow(WidgetTester tester, [Size size = const Size(1366, 768)]) async {
  tester.view.physicalSize = size;
  tester.view.devicePixelRatio = 1.0;
  addTearDown(tester.view.reset);
}

void main() {
  setUpAll(() async {
    catalog = Catalog.fromJson(jsonDecode(File('assets/catalog/catalog.json').readAsStringSync()) as Map<String, dynamic>);
    content = await ContentLibrary.load(bundle, storage);
    for (final m in content.all) {
      await content.open(m, bundle);
    }
    await loadFont('Barlow', ['Barlow-Regular', 'Barlow-Medium', 'Barlow-SemiBold', 'Barlow-Bold']);
    await loadFont('BarlowCondensed', ['BarlowCondensed-Medium', 'BarlowCondensed-SemiBold', 'BarlowCondensed-Bold']);
  });

  test('motor de metas confere com a planilha (PF Agente, 3h, iniciante)', () {
    final p = pfProfile();
    final trail = Planner.buildTrail(catalog, p, const {});
    expect(trail.units.length, 296);
    expect(trail.totalMinutes, 36250);
    final s = Schedule(catalog: catalog, trail: trail, profile: p, data: UserData(profile: p, anchorDate: p.startDate), today: p.startDate);
    expect(isoDate(s.endDate!), '2027-11-02');
    final d1 = s.dayPlan(DateTime(2026, 11, 16));
    expect(d1.units.map((u) => u.id).toList(), ['LP-01:T', 'LP-01:Q']);
    expect(s.dayPlan(DateTime(2026, 11, 21)).kind, DayKind.review);
    expect(s.dayPlan(DateTime(2026, 11, 22)).kind, DayKind.rest);
  });

  test('todas as carreiras, cargos e níveis geram cronograma', () {
    for (final c in catalog.careers) {
      for (final o in c.cargos) {
        for (var lv = 0; lv < 3; lv++) {
          final p = pfProfile()
            ..esfera = c.esfera
            ..careerCode = c.code
            ..optionId = o.id
            ..level = lv;
          final t = Planner.buildTrail(catalog, p, const {});
          expect(t.units, isNotEmpty, reason: o.id);
          final s = Schedule(catalog: catalog, trail: t, profile: p, data: UserData(profile: p, anchorDate: p.startDate), today: p.startDate);
          for (var i = 0; i < 120; i++) {
            s.dayPlan(addDays(p.startDate, i));
          }
        }
      }
    }
  });

  testWidgets('primeiro acesso: do nome ao QG', (tester) async {
    await setWindow(tester);
    final app = controllerWith(UserData());
    await tester.pumpWidget(MentorApp(controller: app));
    await tester.pumpAndSettle();
    expect(find.text('SEU MENTOR PARA A ÁREA POLICIAL'), findsOneWidget);

    await tester.enterText(find.byType(TextField).first, 'Yann');
    await tester.pump();
    await tester.tap(find.text('COMEÇAR'));
    await tester.pumpAndSettle();

    await tester.tap(find.text('FEDERAL'));
    await tester.pumpAndSettle();
    await tester.tap(find.text('CONTINUAR'));
    await tester.pumpAndSettle();

    await tester.tap(find.text('POLÍCIA FEDERAL'));
    await tester.pumpAndSettle();
    await tester.tap(find.text('CONTINUAR'));
    await tester.pumpAndSettle();

    await tester.tap(find.text('AGENTE DE POLÍCIA FEDERAL'));
    await tester.pumpAndSettle();
    await tester.tap(find.text('CONTINUAR'));
    await tester.pumpAndSettle();

    expect(find.text('SUA ROTINA'), findsOneWidget);
    await tester.tap(find.text('CONTINUAR'));
    await tester.pumpAndSettle();

    expect(find.text('SEU PLANO DE OPERAÇÃO'), findsOneWidget);
    await tester.tap(find.text('INICIAR OPERAÇÃO'));
    await tester.pumpAndSettle();

    expect(app.onboarded, isTrue);
    expect(find.text('QG · CENTRAL DE COMANDO'), findsOneWidget);
  });

  testWidgets('todas as telas abrem sem erro (computador e tablet na horizontal)', (tester) async {
    // Junta todos os estouros de layout (em vez de parar no primeiro) para corrigir tudo de uma vez.
    final problems = <String>{};
    var where = '';
    final previous = FlutterError.onError;
    FlutterError.onError = (d) {
      final text = d.toString();
      final loc = RegExp(r'lib/ui/[\w/]+\.dart:\d+').firstMatch(text)?.group(0) ?? '';
      problems.add('$where: ${d.exceptionAsString().split('\n').first} $loc');
    };
    // Tablets na horizontal: iPad (1024×768 e 1133×744) e Android (960×600).
    for (final size in const [Size(1366, 768), Size(1180, 720), Size(1920, 1080), Size(1024, 768), Size(1133, 744), Size(960, 600)]) {
      await setWindow(tester, size);
      final p = pfProfile();
      final data = UserData(profile: p, anchorDate: p.startDate, planSignature: p.planSignature);
      final app = controllerWith(data);
      final day1 = app.schedule!.dayPlan(DateTime(2026, 11, 16));
      app.completeUnit(day1.units[0], minutes: 90);
      app.completeUnit(day1.units[1], questions: 15, correct: 9, minutes: 60);
      await tester.pumpWidget(MentorApp(controller: app));
      await tester.pumpAndSettle();

      for (final page in AppPage.values) {
        where = '$page em ${size.width.toInt()}×${size.height.toInt()}';
        app.goTo(page);
        await tester.pumpAndSettle();
      }
      where = 'materiais em ${size.width.toInt()}×${size.height.toInt()}';

      // Missões: visões semana e trilha.
      app.goTo(AppPage.missions);
      await tester.pumpAndSettle();
      await tester.tap(find.text('SEMANA'));
      await tester.pumpAndSettle();
      await tester.tap(find.text('TRILHA'));
      await tester.pumpAndSettle();
      expect(tester.takeException(), isNull);

      // Material: teoria, resumo com mapa mental e questões.
      app.goTo(AppPage.materials, materialId: 'info-malware-01');
      await tester.pumpAndSettle();
      await tester.tap(find.text('RESUMO + MAPA MENTAL'));
      await tester.pumpAndSettle();
      await tester.tap(find.textContaining('QUESTÕES (').first);
      await tester.pumpAndSettle();
      await tester.tap(find.text('C').first);
      await tester.pump();
      await tester.ensureVisible(find.text('CORRIGIR E LANÇAR NO DIÁRIO'));
      await tester.pumpAndSettle();
      await tester.tap(find.text('CORRIGIR E LANÇAR NO DIÁRIO'));
      await tester.pumpAndSettle();
      expect(find.text('NOTA LÍQUIDA'), findsOneWidget);
      expect(tester.takeException(), isNull);

      // Material aprofundado: teoria longa e 20 questões em dois blocos.
      app.reviewer = true; // visão do dono: abre também os materiais em revisão
      for (final m in content.all.where((m) => m.isDeep)) {
        app.goTo(AppPage.materials);
        await tester.pumpAndSettle();
        app.goTo(AppPage.materials, materialId: m.id);
        await tester.pumpAndSettle();
        await tester.tap(find.textContaining('QUESTÕES (20)').first);
        await tester.pumpAndSettle();
        expect(tester.takeException(), isNull, reason: m.id);
      }
      await tester.pump(const Duration(seconds: 4));
      await tester.pumpAndSettle();
    }
    FlutterError.onError = previous;
    expect(problems, isEmpty, reason: problems.join('\n'));
  });

  testWidgets('concluir missão pelo diálogo lança no diário', (tester) async {
    await setWindow(tester);
    final p = pfProfile();
    final app = controllerWith(UserData(profile: p, anchorDate: p.startDate, planSignature: p.planSignature));
    await tester.pumpWidget(MentorApp(controller: app));
    app.goTo(AppPage.missions, day: DateTime(2026, 11, 18));
    await tester.pumpAndSettle();
    await tester.tap(find.byTooltip('Concluir e lançar no diário').first);
    await tester.pumpAndSettle();
    expect(find.text('MISSÃO CUMPRIDA'), findsOneWidget);
    await tester.tap(find.text('MISSÃO CUMPRIDA'));
    await tester.pumpAndSettle();
    expect(app.data.diary, hasLength(1));
    expect(app.data.unitDone, hasLength(1));

    app.goTo(AppPage.diary);
    await tester.pumpAndSettle();
    await tester.tap(find.text('NOVO LANÇAMENTO').first);
    await tester.pumpAndSettle();
    expect(find.text('SALVAR'), findsOneWidget);
    expect(tester.takeException(), isNull);
  });

  testWidgets('checklist de materiais por edital (ADMIN)', (tester) async {
    final problems = <String>[];
    final previous = FlutterError.onError;
    FlutterError.onError = (d) => problems.add(d.exceptionAsString().split('\n').first);
    try {
      for (final size in const [Size(1366, 768), Size(1024, 768)]) {
        for (final option in const ['PF_AG', 'CBMPE26_TEN']) {
          await setWindow(tester, size);
          final p = pfProfile();
          final app = controllerWith(UserData(profile: p, anchorDate: p.startDate, planSignature: p.planSignature));
          await tester.pumpWidget(MaterialApp(
            key: ValueKey('$size$option'),
            theme: buildTheme(),
            home: AppScope(controller: app, child: Scaffold(body: ContentChecklist(initialOptionId: option))),
          ));
          await tester.pump(const Duration(milliseconds: 300));
          await tester.pump(const Duration(seconds: 2));
          // Nada pode ficar animando sem parar nesta tela.
          expect(tester.binding.transientCallbackCount, 0, reason: 'animação contínua em $option');
          expect(find.text('ASSUNTOS DO EDITAL'), findsOneWidget);
          if (option == 'CBMPE26_TEN') expect(find.text('SÓ DESTE EDITAL'), findsWidgets);
          for (final f in const ['FALTA PRODUZIR', 'FALTA VALIDAR', 'PRONTOS', 'TODOS']) {
            await tester.tap(find.text(f));
            await tester.pump(const Duration(milliseconds: 300));
          }
        }
      }
    } finally {
      FlutterError.onError = previous;
    }
    expect(problems, isEmpty, reason: problems.join('\n'));
  });
}
