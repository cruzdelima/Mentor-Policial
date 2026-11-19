/// Versões dos materiais por banca.
///
/// Cada material tem uma versão base (Cebraspe: itens certo/errado, em que o erro anula um acerto) e pode ter outras:
/// a neutra (sem citar banca, para carreiras cuja banca varia por estado) e a do Instituto AOCP (Bloco B em múltipla
/// escolha com 5 alternativas). O app escolhe a versão pela banca do concurso pós-edital ou, no ciclo básico, pela banca
/// do último concurso da carreira.
library;

const kBancaVariants = ['cebraspe', 'aocp', 'neutro'];

/// Perfil de material para o nome da banca ("Cebraspe (2021 e 2025)", "Instituto AOCP", "Varia por estado"...).
String bancaProfileOf(String banca) {
  final b = banca.toLowerCase();
  if (b.contains('cebraspe') || b.contains('cespe')) return 'cebraspe';
  if (b.contains('aocp')) return 'aocp';
  return 'neutro';
}

String bancaVariantLabel(String v) => switch (v) {
      'cebraspe' => 'Cebraspe',
      'aocp' => 'Instituto AOCP',
      _ => 'Neutra',
    };
