/// Utilitários de data sem dependências externas (formato brasileiro).
library;

DateTime dateOnly(DateTime d) => DateTime(d.year, d.month, d.day);

DateTime addDays(DateTime d, int days) => DateTime(d.year, d.month, d.day + days);

int daysBetween(DateTime a, DateTime b) =>
    DateTime.utc(b.year, b.month, b.day).difference(DateTime.utc(a.year, a.month, a.day)).inDays;

bool sameDay(DateTime a, DateTime b) => a.year == b.year && a.month == b.month && a.day == b.day;

String two(int n) => n.toString().padLeft(2, '0');

/// 16/11/2026
String fmtDate(DateTime d) => '${two(d.day)}/${two(d.month)}/${d.year}';

/// 16/11
String fmtDayMonth(DateTime d) => '${two(d.day)}/${two(d.month)}';

/// 2026-11-16 (chave para armazenamento)
String isoDate(DateTime d) => '${d.year}-${two(d.month)}-${two(d.day)}';

DateTime parseIso(String s) {
  final p = s.split('-').map(int.parse).toList();
  return DateTime(p[0], p[1], p[2]);
}

const _weekdaysShort = ['SEG', 'TER', 'QUA', 'QUI', 'SEX', 'SÁB', 'DOM'];
const _weekdaysLong = ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado', 'domingo'];
const _months = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'];

String weekdayShort(DateTime d) => _weekdaysShort[d.weekday - 1];
String weekdayLong(DateTime d) => _weekdaysLong[d.weekday - 1];
String monthName(int m) => _months[m - 1];

/// "segunda-feira, 16 de novembro"
String fmtLong(DateTime d) => '${weekdayLong(d)}, ${d.day} de ${monthName(d.month)}';
