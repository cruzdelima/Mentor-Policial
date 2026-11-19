import 'package:flutter_test/flutter_test.dart';
import 'package:mentor_policial/data/auth.dart';

void main() {
  test('classificação dos alunos', () {
    expect(planFrom('free'), Plan.none); // valor provisório antigo
    expect(planFrom('beta'), Plan.beta);
    expect(planFrom('tester'), Plan.tester);
    expect(planLabel(Plan.tester), 'Testador Gratuito');
    expect(kManualPlans, isNot(contains(Plan.monthly)));
    final p = AccountProfile.fromJson(<String, dynamic>{
      'id': 'x',
      'email': 'a@b.com',
      'plan': 'annual',
      'plan_expires_at': DateTime.now().add(const Duration(days: 30)).toUtc().toIso8601String(),
      'plan_note': 'pago',
    });
    expect(p.plan, Plan.annual);
    expect(p.hasActiveSubscription, isTrue);
    expect(p.planNote, 'pago');
  });
}
