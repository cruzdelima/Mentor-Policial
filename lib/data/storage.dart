/// Armazenamento local (sem dependências externas): pasta de dados do usuário,
/// gravação atômica do JSON, cópias de segurança e abertura de arquivos/links no sistema.
library;

import 'dart:convert';
import 'dart:io';

import 'package:flutter/foundation.dart' show kIsWeb;

import '../core/dates.dart';
import '../core/models.dart';
import '../platform/fs.dart';
import '../platform/web_bridge.dart';

class Storage {
  Storage(this.dir);

  /// Pasta padrão de dados do app em cada sistema. Na primeira abertura após a troca de nome,
  /// a pasta antiga (MentorPolicial) é renomeada para a nova (Taticum), sem perder nada.
  /// O app está rodando como pacote da Microsoft Store (MSIX)?
  static bool get isStorePackage =>
      !kIsWeb && Platform.isWindows && Platform.resolvedExecutable.toLowerCase().contains(r'\windowsapps\');

  /// Pasta (no navegador: prefixo) dos dados do app.
  static String defaultDir() {
    if (kIsWeb) return 'taticum';
    return _desktopDir().path;
  }

  static Directory _desktopDir() {
    if (isStorePackage) return _storeDir();
    final dir = _dirNamed('Taticum', 'taticum');
    if (!dir.existsSync()) {
      final legacy = _dirNamed('MentorPolicial', 'mentor_policial');
      if (legacy.existsSync()) {
        try {
          legacy.renameSync(dir.path);
        } catch (_) {
          return legacy; // pasta em uso: continua na antiga e tenta de novo na próxima abertura
        }
      }
    }
    return dir;
  }

  /// Versão da Store: usa uma pasta própria (o Windows guarda num local privado do pacote).
  /// Na primeira abertura, copia os dados da versão instalada pelo instalador (.exe), se houver,
  /// sem alterar os originais: as duas versões nunca escrevem nos mesmos arquivos.
  static Directory _storeDir() {
    final dir = _dirNamed('TaticumStore', 'taticum_store');
    if (dir.existsSync()) return dir;
    final old = _dirNamed('Taticum', 'taticum');
    try {
      if (old.existsSync()) _copyDir(old, dir);
    } catch (_) {}
    return dir;
  }

  static void _copyDir(Directory from, Directory to) {
    to.createSync(recursive: true);
    for (final e in from.listSync(followLinks: false)) {
      final name = e.path.split(Platform.pathSeparator).last;
      final target = join(to.path, name);
      if (e is Directory) {
        _copyDir(e, Directory(target));
      } else if (e is File) {
        e.copySync(target);
      }
    }
  }

  static Directory _dirNamed(String name, String linuxName) {
    final env = Platform.environment;
    String path;
    if (Platform.isWindows) {
      path = '${env['APPDATA'] ?? env['USERPROFILE'] ?? Directory.systemTemp.path}\\$name';
    } else if (Platform.isMacOS) {
      path = '${env['HOME']}/Library/Application Support/$name';
    } else {
      path = '${env['XDG_DATA_HOME'] ?? '${env['HOME']}/.local/share'}/$linuxName';
    }
    return Directory(path);
  }

  /// Pasta dos dados desta conta (no navegador, um prefixo do localStorage).
  final String dir;

  static final Fs _fs = Fs.instance;

  String get _file => join(dir, 'dados.json');
  String get _tmp => join(dir, 'dados.json.tmp');
  String get backups => join(dir, 'backups');

  /// Só no desktop: PDFs copiados do app e pacotes de conteúdo extras.
  Directory get materialsDir => Directory(join(dir, 'materiais'));
  Directory get packsDir => Directory(join(dir, 'conteudos'));

  static String join(String a, String b) => _fs.join(a, b);

  /// Nome deste aparelho, mostrado ao aluno quando há dados de dois aparelhos.
  static String deviceName() {
    if (kIsWeb) return 'Navegador';
    final os = Platform.isWindows ? 'Windows' : (Platform.isMacOS ? 'Mac' : 'Linux');
    try {
      final h = Platform.localHostname.trim();
      return h.isEmpty ? os : '$h ($os)';
    } catch (_) {
      return os;
    }
  }

  /// Controle da cópia na nuvem (versão recebida e mudanças pendentes).
  String get syncFile => join(dir, 'nuvem.json');

  Future<UserData> load() async {
    for (final f in [_file, _tmp]) {
      final text = await _fs.read(f);
      if (text == null) continue;
      try {
        return UserData.fromJson(jsonDecode(text) as Map<String, dynamic>);
      } catch (_) {
        // arquivo corrompido: tenta o próximo / o backup mais recente
      }
    }
    final files = (await _fs.list(backups)).where((f) => f.endsWith('.json')).toList()..sort((a, b) => b.compareTo(a));
    for (final f in files.take(3)) {
      try {
        return UserData.fromJson(jsonDecode((await _fs.read(f))!) as Map<String, dynamic>);
      } catch (_) {}
    }
    return UserData();
  }

  Future<void>? _pending;
  String? _queued;

  /// Grava de forma atômica (arquivo temporário + renomear) e serializa as escritas.
  Future<void> save(UserData data) {
    _queued = kIsWeb ? jsonEncode(data.toJson()) : const JsonEncoder.withIndent(' ').convert(data.toJson());
    return _pending ??= _flush();
  }

  Future<void> _flush() async {
    try {
      while (_queued != null) {
        final text = _queued!;
        _queued = null;
        await _fs.write(_file, text);
        if (!kIsWeb) await _dailyBackup(text); // no navegador, a cópia de segurança é a da nuvem
      }
    } finally {
      _pending = null;
    }
  }

  /// Uma cópia por dia na pasta "backups" (mantém as 15 mais recentes).
  Future<void> _dailyBackup(String text) async {
    await _fs.write(join(backups, 'dados_${isoDate(DateTime.now())}.json'), text);
    final files = (await _fs.list(backups)).where((x) => x.endsWith('.json')).toList()..sort((a, b) => b.compareTo(a));
    for (final old in files.skip(15)) {
      try {
        await _fs.delete(old);
      } catch (_) {}
    }
  }

  /// Guarda uma cópia dos dados antes de serem substituídos pela versão da nuvem (pasta "substituidos").
  Future<String> keepReplaced(UserData data) async {
    final now = DateTime.now();
    final path = join(join(dir, 'substituidos'), 'antes_da_nuvem_${isoDate(now)}_${two(now.hour)}${two(now.minute)}${two(now.second)}.json');
    await _fs.write(path, jsonEncode(data.toJson()));
    if (kIsWeb) {
      // No navegador, guarda só a cópia mais recente (o espaço é pequeno).
      for (final old in await _fs.list(join(dir, 'substituidos'))) {
        if (old != path) await _fs.delete(old);
      }
    }
    return path;
  }

  /// Exporta um backup para a pasta Documentos (ou para a pasta de dados) e devolve o caminho.
  Future<String> exportBackup(UserData data) async {
    if (kIsWeb) {
      final now = DateTime.now();
      final name = 'Taticum_backup_${isoDate(now)}_${two(now.hour)}${two(now.minute)}.json';
      webDownload(name, const JsonEncoder.withIndent(' ').convert(data.toJson()));
      return name;
    }
    final env = Platform.environment;
    final home = Platform.isWindows ? env['USERPROFILE'] : env['HOME'];
    Directory target = Directory(dir);
    if (home != null) {
      final docs = Directory(join(home, 'Documents'));
      if (await docs.exists()) target = docs;
    }
    final now = DateTime.now();
    final name = 'Taticum_backup_${isoDate(now)}_${two(now.hour)}${two(now.minute)}.json';
    final f = File(join(target.path, name));
    await f.writeAsString(const JsonEncoder.withIndent(' ').convert(data.toJson()));
    return f.path;
  }

  /// Lê um backup exportado (valida antes de substituir os dados atuais).
  Future<UserData> readBackup(String path) async {
    final clean = path.trim().replaceAll('"', '');
    final f = File(clean);
    if (!await f.exists()) throw const FileSystemException('Arquivo não encontrado');
    return parseBackup(await f.readAsString());
  }

  /// Valida o conteúdo de um backup (usado também no navegador, que lê o arquivo escolhido).
  static UserData parseBackup(String text) {
    final j = jsonDecode(text) as Map<String, dynamic>;
    if (!j.containsKey('profile') || !j.containsKey('diary')) {
      throw const FormatException('Este arquivo não é um backup do Taticum');
    }
    return UserData.fromJson(j);
  }
}

/// Abre um arquivo, pasta ou link com o programa padrão do sistema.
Future<bool> openExternal(String target) async {
  try {
    final t = target.trim();
    if (t.isEmpty) return false;
    if (kIsWeb) {
      if (!looksLikeUrl(t) && !t.startsWith('assets/') && !t.startsWith('mailto:') && !t.startsWith('blob:')) return false;
      webOpen(looksLikeUrl(t) ? normalizeUrl(t) : t);
      return true;
    }
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
