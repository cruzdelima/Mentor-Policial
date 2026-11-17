/// Regras de cadastro: senha forte, e-mail e telefone brasileiro.
/// As mesmas regras de senha são exigidas pelo servidor (Supabase › Auth › Password requirements).
library;

class PasswordRule {
  const PasswordRule(this.label, this.test);
  final String label;
  final bool Function(String) test;
}

/// Caracteres especiais aceitos (mesmo conjunto do servidor de contas).
const kSpecialChars = r'''!@#$%^&*()_+-=[]{};':"|<>?,./`~''';

final kPasswordRules = <PasswordRule>[
  PasswordRule('No mínimo 8 caracteres', (s) => s.length >= 8),
  PasswordRule('Uma letra maiúscula', (s) => RegExp('[A-Z]').hasMatch(s)),
  PasswordRule('Uma letra minúscula', (s) => RegExp('[a-z]').hasMatch(s)),
  PasswordRule('Um número', (s) => RegExp('[0-9]').hasMatch(s)),
  PasswordRule('Um caractere especial (ex.: ! @ # \$ %)', (s) => s.split('').any(kSpecialChars.contains)),
];

bool isStrongPassword(String s) => kPasswordRules.every((r) => r.test(s));

/// Senhas comuns demais para serem aceitas, mesmo cumprindo as regras.
const _common = {'senha@123', 'senha123!', 'password1!', 'mudar@123', 'brasil@123', 'abc@1234', 'qwerty@123', 'policia@123'};

String? passwordProblem(String s) {
  if (!isStrongPassword(s)) return 'A senha não cumpre todas as regras.';
  if (_common.contains(s.toLowerCase())) return 'Essa senha é muito comum. Escolha outra.';
  return null;
}

bool isValidEmail(String s) => RegExp(r'^[^\s@]+@[^\s@]+\.[^\s@]{2,}$').hasMatch(s.trim());

/// Normaliza um celular brasileiro para o formato internacional (+55DDNNNNNNNNN).
/// Aceita "(85) 99999-1234", "85999991234", "+55 85 99999-1234". Devolve null se for inválido.
String? normalizePhone(String raw) {
  var d = raw.replaceAll(RegExp(r'\D'), '');
  if (d.startsWith('55') && (d.length == 12 || d.length == 13)) d = d.substring(2);
  if (d.startsWith('0')) d = d.substring(1);
  if (d.length != 10 && d.length != 11) return null;
  final ddd = int.parse(d.substring(0, 2));
  if (ddd < 11 || ddd > 99) return null;
  if (d.length == 11 && d[2] != '9') return null;
  return '+55$d';
}

/// +5585999991234 › (85) 99999-1234
String formatPhone(String e164) {
  final d = e164.replaceAll(RegExp(r'\D'), '');
  final n = d.startsWith('55') ? d.substring(2) : d;
  if (n.length == 11) return '(${n.substring(0, 2)}) ${n.substring(2, 7)}-${n.substring(7)}';
  if (n.length == 10) return '(${n.substring(0, 2)}) ${n.substring(2, 6)}-${n.substring(6)}';
  return e164;
}
