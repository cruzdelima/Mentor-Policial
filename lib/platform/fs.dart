/// Arquivos do app: no desktop, a pasta de dados do usuário; no navegador, o localStorage.
/// Os caminhos são textos ("pasta/arquivo"); quem chama não precisa saber onde estão guardados.
library;

import 'package:flutter/foundation.dart' show kIsWeb;

import 'fs_io.dart';
import 'web_bridge.dart';

abstract class Fs {
  static final Fs instance = kIsWeb ? _WebFs() : IoFs();

  String get separator;
  String join(String a, String b) => '$a$separator$b';

  Future<String?> read(String path);

  /// Grava de forma segura (no desktop: arquivo temporário + renomear).
  Future<void> write(String path, String text);
  Future<bool> exists(String path);
  Future<void> delete(String path);

  /// Apaga a pasta e tudo dentro dela.
  Future<void> deleteTree(String dir);

  /// Arquivos diretamente dentro da pasta (caminhos completos).
  Future<List<String>> list(String dir);
}

class _WebFs extends Fs {
  static const _prefix = 'taticum:';

  @override
  String get separator => '/';

  @override
  Future<String?> read(String path) async => webStorageGet('$_prefix$path');

  @override
  Future<void> write(String path, String text) async => webStorageSet('$_prefix$path', text);

  @override
  Future<bool> exists(String path) async => webStorageGet('$_prefix$path') != null;

  @override
  Future<void> delete(String path) async => webStorageRemove('$_prefix$path');

  @override
  Future<void> deleteTree(String dir) async {
    for (final k in webStorageKeys()) {
      if (k.startsWith('$_prefix$dir/')) webStorageRemove(k);
    }
  }

  @override
  Future<List<String>> list(String dir) async => [
        for (final k in webStorageKeys())
          if (k.startsWith('$_prefix$dir/') && !k.substring('$_prefix$dir/'.length).contains('/')) k.substring(_prefix.length),
      ];
}
