/// Desktop: arquivos de verdade na pasta de dados.
library;

import 'dart:io';

import 'fs.dart';

class IoFs extends Fs {
  @override
  String get separator => Platform.pathSeparator;

  @override
  Future<String?> read(String path) async {
    final f = File(path);
    return await f.exists() ? f.readAsString() : null;
  }

  @override
  Future<void> write(String path, String text) async {
    final f = File(path);
    await f.parent.create(recursive: true);
    final tmp = File('$path.tmp');
    await tmp.writeAsString(text, flush: true);
    if (await f.exists()) await f.delete();
    await tmp.rename(path);
  }

  @override
  Future<bool> exists(String path) => File(path).exists();

  @override
  Future<void> delete(String path) async {
    final f = File(path);
    if (await f.exists()) await f.delete();
  }

  @override
  Future<void> deleteTree(String dir) async {
    final d = Directory(dir);
    if (await d.exists()) await d.delete(recursive: true);
  }

  @override
  Future<List<String>> list(String dir) async {
    final d = Directory(dir);
    if (!await d.exists()) return const [];
    return [for (final e in d.listSync()) if (e is File) e.path];
  }
}
