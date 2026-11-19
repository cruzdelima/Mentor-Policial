import 'package:flutter_test/flutter_test.dart';
import 'package:mentor_policial/core/bancas.dart';
import 'package:mentor_policial/core/models.dart';
import 'package:mentor_policial/data/content.dart';
import 'package:mentor_policial/state/app_state.dart';

MaterialInfo _info(List<String> variants) => MaterialInfo(
      id: 'dc-x-02',
      folder: 'constitucional_x',
      title: 'X',
      subtitle: '',
      subjectId: 'DC',
      topicIds: const ['DC-02'],
      kind: 'aprofundado',
      minutes: 60,
      questions: 20,
      version: '0.1.0',
      status: 'Em revisão pelo autor',
      source: 'asset',
      variants: variants,
    );

void main() {
  test('perfil de banca a partir do nome', () {
    expect(bancaProfileOf('Cebraspe (2021 e 2025)'), 'cebraspe');
    expect(bancaProfileOf('CESPE/UnB'), 'cebraspe');
    expect(bancaProfileOf('Instituto AOCP'), 'aocp');
    expect(bancaProfileOf('Varia por estado'), 'neutro');
    expect(bancaProfileOf('FGV'), 'neutro');
  });

  test('versão do material segue a banca, com a neutra como reserva', () {
    final lib = ContentLibrary([]);
    final full = _info(['neutro', 'aocp']);
    final onlyNeutral = _info(['neutro']);
    final old = _info([]);
    lib.banca = 'cebraspe';
    expect(lib.variantFor(full), 'cebraspe');
    lib.banca = 'aocp';
    expect(lib.variantFor(full), 'aocp');
    expect(lib.variantFor(onlyNeutral), 'neutro');
    expect(lib.variantFor(old), 'cebraspe');
    lib.banca = 'neutro';
    expect(lib.variantFor(full), 'neutro');
    lib.preview = 'cebraspe';
    expect(lib.variantFor(full), 'cebraspe');
  });

  test('múltipla escolha e versão sem desconto não tiram ponto por erro', () {
    final q = Quiz.fromJson({
      'style': 'MISTO',
      'banca': 'x',
      'instructions': '',
      'penalty': false,
      'questions': [
        {'id': 'q1', 'text': 'a', 'answer': 'C', 'comment': ''},
        {'id': 'm2', 'text': 'b', 'answer': 'B', 'comment': '', 'options': ['1', '2', '3', '4', '5']},
      ],
    });
    expect(q.penalty, isFalse);
    expect(q.questions[1].isChoice, isTrue);
    expect(q.questions[1].letters, ['A', 'B', 'C', 'D', 'E']);
    final a = QuizAttempt(date: DateTime(2026), answers: const {}, correct: 1, wrong: 1, blank: 0, penalized: 0);
    expect(a.net, 1);
    final old = QuizAttempt.fromJson(<String, dynamic>{'date': '2026-01-01', 'answers': <String, dynamic>{}, 'correct': 3, 'wrong': 1, 'blank': 0});
    expect(old.net, 2);
  });
}
