/// Cache local do catálogo extra (o que o dono/administradores publicaram pelo editor)
/// e a interface com o servidor que guarda a versão oficial.
library;

import 'dart:convert';

import '../core/extras.dart';
import '../platform/fs.dart';
import 'storage.dart';

/// Onde o catálogo extra é lido e publicado (no app: Supabase, via [AuthService]).
abstract class CatalogRemote {
  /// Versão publicada; null quando ainda não há nada publicado.
  Future<({Map<String, dynamic> data, int version})?> fetchCatalog();

  /// Publica [data]. [baseVersion] é a versão que o editor abriu (evita sobrescrever o trabalho de outra pessoa).
  Future<int> saveCatalog(Map<String, dynamic> data, int baseVersion, String note);
}

/// Cópia do catálogo extra no computador, para o app abrir sem internet.
/// Fica na pasta geral do app (vale para todas as contas do computador).
class CatalogStore {
  CatalogStore(this.dir);
  final String dir;

  String get _file => Storage.join(dir, 'catalogo_extra.json');

  Future<({Map<String, dynamic> data, int version})> read() async {
    try {
      final text = await Fs.instance.read(_file);
      if (text != null) {
        final j = jsonDecode(text) as Map<String, dynamic>;
        return (data: normalizeExtras(j['data']), version: (j['version'] as num? ?? 0).toInt());
      }
    } catch (_) {}
    return (data: emptyExtras(), version: 0);
  }

  Future<void> write(Map<String, dynamic> data, int version) async {
    try {
      await Fs.instance.write(_file, jsonEncode({'version': version, 'data': data}));
    } catch (_) {}
  }
}
