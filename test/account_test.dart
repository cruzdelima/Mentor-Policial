// Testes das contas: regras de cadastro e tela de login/cadastro (sem acessar a internet).
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:mentor_policial/app.dart';
import 'package:mentor_policial/core/validation.dart';
import 'package:mentor_policial/data/auth.dart';
import 'package:mentor_policial/state/account.dart';

Future<void> loadFont(String family, List<String> files) async {
  final loader = FontLoader(family);
  for (final f in files) {
    loader.addFont(File('assets/fonts/$f.ttf').readAsBytes().then((b) => ByteData.view(b.buffer)));
  }
  await loader.load();
}

void main() {
  setUpAll(() async {
    await loadFont('Barlow', ['Barlow-Regular', 'Barlow-Medium', 'Barlow-SemiBold', 'Barlow-Bold']);
    await loadFont('BarlowCondensed', ['BarlowCondensed-Medium', 'BarlowCondensed-SemiBold', 'BarlowCondensed-Bold']);
  });

  test('regras de senha', () {
    expect(isStrongPassword('Abc@1234'), isTrue);
    expect(isStrongPassword('abc@1234'), isFalse, reason: 'sem maiúscula');
    expect(isStrongPassword('ABC@1234'), isFalse, reason: 'sem minúscula');
    expect(isStrongPassword('Abcd@efg'), isFalse, reason: 'sem número');
    expect(isStrongPassword('Abcd1234'), isFalse, reason: 'sem especial');
    expect(isStrongPassword('Ab@1234'), isFalse, reason: '7 caracteres');
    expect(passwordProblem('Senha@123'), isNotNull, reason: 'senha comum');
    expect(passwordProblem('Policial#2027x'), isNull);
  });

  test('e-mail e celular', () {
    expect(isValidEmail('aluno@gmail.com'), isTrue);
    expect(isValidEmail('aluno@gmail'), isFalse);
    expect(normalizePhone('(85) 99999-1234'), '+5585999991234');
    expect(normalizePhone('+55 11 98888-7777'), '+5511988887777');
    expect(normalizePhone('085 3222-1234'), '+558532221234');
    expect(normalizePhone('99999-1234'), isNull, reason: 'sem DDD');
    expect(normalizePhone('(85) 89999-1234'), isNull, reason: 'celular sem 9');
    expect(formatPhone('+5585999991234'), '(85) 99999-1234');
    // O formato normalizado é o mesmo exigido pelo banco (supabase/migrations/0001_contas.sql).
    expect(RegExp(r'^\+55[1-9][0-9]9?[0-9]{8}$').hasMatch(normalizePhone('(85) 99999-1234')!), isTrue);
  });

  test('papéis', () {
    expect(roleFrom('owner'), Role.owner);
    expect(roleFrom('admin'), Role.admin);
    expect(roleFrom('qualquer coisa'), Role.student);
  });

  testWidgets('tela de entrada cabe no tablet (horizontal, em pé e com teclado aberto)', (tester) async {
    for (final size in const [Size(1024, 768), Size(960, 600), Size(1024, 360), Size(768, 1024)]) {
      tester.view.physicalSize = size;
      tester.view.devicePixelRatio = 1;
      final acc = AccountController(
        service: AuthService(url: 'https://exemplo.invalid', apiKey: 'teste', storage: Directory.systemTemp.createTempSync('mp_auth').path),
      )..status = AccountStatus.signedOut;
      await tester.pumpWidget(MentorApp(account: acc));
      await tester.pumpAndSettle();
      expect(find.text('ENTRAR'), findsWidgets);
      await tester.tap(find.widgetWithText(TextButton, 'CRIAR CONTA'));
      await tester.pumpAndSettle();
      expect(tester.takeException(), isNull, reason: '$size');
    }
    tester.view.reset();
  });

  testWidgets('cadastro só libera o botão com dados válidos', (tester) async {
    tester.view.physicalSize = const Size(1366, 768);
    tester.view.devicePixelRatio = 1;
    addTearDown(tester.view.reset);
    final acc = AccountController(
      service: AuthService(url: 'https://exemplo.invalid', apiKey: 'teste', storage: Directory.systemTemp.createTempSync('mp_auth').path),
    )..status = AccountStatus.signedOut;
    await tester.pumpWidget(MentorApp(account: acc));
    await tester.pumpAndSettle();
    expect(find.text('ENTRAR'), findsWidgets);

    await tester.tap(find.widgetWithText(TextButton, 'CRIAR CONTA'));
    await tester.pumpAndSettle();
    final button = find.widgetWithText(ElevatedButton, 'CRIAR CONTA');
    bool enabled() => tester.widget<ElevatedButton>(button).onPressed != null;
    expect(enabled(), isFalse);

    final fields = find.byType(TextField);
    await tester.enterText(fields.at(0), 'Aluno Teste');
    await tester.enterText(fields.at(1), 'aluno@teste.com');
    await tester.enterText(fields.at(2), '(85) 99999-1234');
    await tester.enterText(fields.at(3), 'fraca');
    await tester.enterText(fields.at(4), 'fraca');
    await tester.pump();
    expect(enabled(), isFalse, reason: 'senha fraca');

    await tester.enterText(fields.at(3), 'Policial#2027x');
    await tester.enterText(fields.at(4), 'Policial#2027x');
    await tester.pump();
    expect(enabled(), isFalse, reason: 'termos não aceitos');

    await tester.ensureVisible(find.byType(Checkbox));
    await tester.tap(find.byType(Checkbox));
    await tester.pump();
    expect(enabled(), isTrue);
    expect(tester.takeException(), isNull);

    // Esqueci minha senha e volta.
    await tester.ensureVisible(find.widgetWithText(TextButton, 'ENTRAR'));
    await tester.tap(find.widgetWithText(TextButton, 'ENTRAR'));
    await tester.pumpAndSettle();
    await tester.tap(find.text('ESQUECI MINHA SENHA'));
    await tester.pumpAndSettle();
    expect(find.text('ENVIAR CÓDIGO'), findsOneWidget);
    expect(tester.takeException(), isNull);
  });
}
