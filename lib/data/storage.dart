/// Armazenamento local (sem dependências externas): pasta de dados do usuário,
/// gravação atômica do JSON, cópias de segurança e abertura de arquivos/links no sistema.
library;

import 'dart:convert';
import 'dart:io';

import '../core/dates.dart';
import '../core/models.dart';

class Storage {
  Storage(this.dir);

  /// Pasta padrão de dados do app em cada sistema.
  static Directory defaultDir() {
    final env = Platform.environment;
    String path;
    if (Platform.isWindows) {
      path = '${env['APPDATA'] ?? env['USERPROFILE'] ?? Directory.systemTemp.path}\\MentorPolicial';
    } else if (Platform.isMacOS) {
      path = '${env['HOME']}/Library/Application Support/MentorPolicial';
    } else {
      path = '${env['XDG_DATA_HOME'] ?? '${env['HOME']}/.local/share'}/mentor_policial';
    }
    return Directory(path);
  }

  final Directory dir;

  File get _file => File(_join(dir.path, 'dados.json'));
  File get _tmp => File(_join(dir.path, 'dados.json.tmp'));
  Directory get backups => Directory(_join(dir.path, 'backups'));
  Directory get materialsDir => Directory(_join(dir.path, 'materiais'));
  Directory get packsDir => Directory(_join(dir.path, 'conteudos'));

  static String _join(String a, String b) => '$a${Platform.pathSeparator}$b';
  static String join(String a, String b) => _join(a, b);

  Future<UserData> load() async {
    await dir.create(recursive: true);
    for (final f in [_file, _tmp]) {
      if (await f.exists()) {
        try {
          final j = jsonDecode(await f.readAsString()) as Map<String, dynamic>;
          return UserData.fromJson(j);
        } catch (_) {
          // arquivo corrompido: tenta o próximo / o backup mais recente
        }
      }
    }
    final latest = await _latestBackup();
    if (latest != null) {
      try {
        return UserData.fromJson(jsonDecode(await latest.readAsString()) as Map<String, dynamic>);
      } catch (_) {}
    }
    return UserData();
  }

  Future<File?> _latestBackup() async {
    if (!await backups.exists()) return null;
    final files = backups.listSync().whereType<File>().where((f) => f.path.endsWith('.json')).toList()
      ..sort((a, b) => b.path.compareTo(a.path));
    return files.isEmpty ? null : files.first;
  }

  Future<void>? _pending;
  String? _queued;

  /// Grava de forma atômica (arquivo temporário + renomear) e serializa as escritas.
  Future<void> save(UserData data) {
    _queued = const JsonEncoder.withIndent(' ').convert(data.toJson());
    return _pending ??= _flush();
  }

  Future<void> _flush() async {
    try {
      while (_queued != null) {
        final text = _queued!;
        _queued = null;
        await dir.create(recursive: true);
        await _tmp.writeAsString(text, flush: true);
        if (await _file.exists()) await _file.delete();
        await _tmp.rename(_file.path);
        await _dailyBackup(text);
      }
    } finally {
      _pending = null;
    }
  }

  /// Uma cópia por dia na pasta "backups" (mantém as 15 mais recentes).
  Future<void> _dailyBackup(String text) async {
    await backups.create(recursive: true);
    final f = File(_join(backups.path, 'dados_${isoDate(DateTime.now())}.json'));
    await f.writeAsString(text);
    final files = backups.listSync().whereType<File>().where((x) => x.path.endsWith('.json')).toList()
      ..sort((a, b) => b.path.compareTo(a.path));
    for (final old in files.skip(15)) {
      try {
        old.deleteSync();
      } catch (_) {}
    }
  }

  /// Exporta um backup para a pasta Documentos (ou para a pasta de dados) e devolve o caminho.
  Future<String> exportBackup(UserData data) async {
    final env = Platform.environment;
    final home = Platform.isWindows ? env['USERPROFILE'] : env['HOME'];
    Directory target = dir;
    if (home != null) {
      final docs = Directory(_join(home, 'Documents'));
      if (await docs.exists()) target = docs;
    }
    final now = DateTime.now();
    final name = 'MentorPolicial_backup_${isoDate(now)}_${two(now.hour)}${two(now.minute)}.json';
    final f = File(_join(target.path, name));
    await f.writeAsString(const JsonEncoder.withIndent(' ').convert(data.toJson()));
    return f.path;
  }

  /// Lê um backup exportado (valida antes de substituir os dados atuais).
  Future<UserData> readBackup(String path) async {
    final clean = path.trim().replaceAll('"', '');
    final f = File(clean);
    if (!await f.exists()) throw const FileSystemException('Arquivo não encontrado');
    final j = jsonDecode(await f.readAsString()) as Map<String, dynamic>;
    if (!j.containsKey('profile') || !j.containsKey('diary')) {
      throw const FormatException('Este arquivo não é um backup do Mentor Policial');
    }
    return UserData.fromJson(j);
  }
}

/// Abre um arquivo, pasta ou link com o programa padrão do sistema.
Future<bool> openExternal(String target) async {
  try {
    final t = target.trim();
    if (t.isEmpty) return false;
    if (Platform.isWindows) {
      final isUrl = t.startsWith('http://') || t.startsWith('https://') || t.startsWith('mailto:');
      if (isUrl) {
        await Process.run('rundll32', ['url.dll,FileProtocolHandler', t]);
      } else {
        // explorer.exe devolve código 1 mesmo quando abre com sucesso.
        await Process.run('explorer.exe', [t]);
      }
      return true;
    }
    final r = await Process.run(Platform.isMacOS ? 'open' : 'xdg-open', [t]);
    return r.exitCode == 0;
  } catch (_) {
    return false;
  }
}

bool looksLikeUrl(String s) {
  final t = s.trim().toLowerCase();
  return t.startsWith('http://') || t.startsWith('https://') || t.startsWith('www.');
}

String normalizeUrl(String s) {
  final t = s.trim();
  return t.toLowerCase().startsWith('www.') ? 'https://$t' : t;
}
