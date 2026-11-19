/// Progresso de estudo salvo na nuvem.
///
/// O arquivo do computador continua sendo a fonte principal (o app funciona sem internet). A nuvem guarda uma cópia
/// com número de versão. Regras:
///  * Mudou algo aqui → envia alguns segundos depois (e, se estiver sem internet, assim que voltar).
///  * A nuvem tem versão mais nova e aqui não mudou nada → adota a versão da nuvem (outro aparelho estudou).
///  * As duas mudaram (ou é a primeira vez deste aparelho e os dois lados já têm dados) → pergunta ao aluno qual manter.
library;

import 'dart:async';
import 'dart:convert';
import 'dart:io';

import 'package:flutter/foundation.dart';

/// Cópia guardada na nuvem.
class RemoteStudy {
  RemoteStudy({required this.version, required this.device, required this.updatedAt, this.data});
  final int version;
  final String device;
  final DateTime updatedAt;
  final Map<String, dynamic>? data;
}

/// Servidor do progresso (implementado por AuthService; nos testes, por um falso).
abstract class StudyRemote {
  /// null = ainda não há cópia na nuvem. [withData] = false busca só a versão (mais leve).
  Future<RemoteStudy?> fetchStudy({bool withData = true});

  /// Grava e devolve a nova versão. Lança [StudyConflict] se outro aparelho gravou antes.
  Future<int> saveStudy(Map<String, dynamic> data, int baseVersion, String device);
}

class StudyConflict implements Exception {}

/// Sem internet (tenta de novo mais tarde, sem incomodar o aluno).
class StudyOffline implements Exception {}

/// O servidor ainda não tem a tabela (migração 0005 não aplicada): a sincronização fica desligada.
class StudyUnavailable implements Exception {}

enum SyncState { starting, synced, pending, syncing, offline, conflict, unavailable, error }

class CloudSync extends ChangeNotifier {
  CloudSync({
    required this.remote,
    required this.metaFile,
    required this.device,
    required this.readLocal,
    required this.adoptRemote,
    required this.localIsEmpty,
    this.pushDelay = const Duration(seconds: 4),
    this.pollEvery = const Duration(minutes: 3),
  });

  final StudyRemote remote;

  /// Arquivo com a versão que este aparelho recebeu/enviou por último e se há mudanças não enviadas.
  final File metaFile;
  final String device;
  final Map<String, dynamic> Function() readLocal;
  final void Function(Map<String, dynamic> data) adoptRemote;
  final bool Function() localIsEmpty;
  final Duration pushDelay;
  final Duration pollEvery;

  SyncState state = SyncState.starting;
  int version = 0;
  bool dirty = false;
  DateTime? lastSync;
  String lastError = '';

  /// Cópia da nuvem em conflito com a deste aparelho (aguardando o aluno escolher).
  RemoteStudy? conflict;

  Timer? _pushTimer;
  Timer? _poll;
  int _changes = 0;
  bool _busy = false;
  bool _disposed = false;

  Future<void> start() async {
    await _readMeta();
    await pull();
    _poll = Timer.periodic(pollEvery, (_) => _tick());
  }

  /// Chamado a cada alteração local.
  void markDirty() {
    _changes++;
    if (state == SyncState.unavailable) return;
    if (!dirty) {
      dirty = true;
      _writeMeta();
    }
    if (state != SyncState.conflict) _set(SyncState.pending);
    _pushTimer?.cancel();
    _pushTimer = Timer(pushDelay, push);
  }

  Future<void> _tick() async {
    if (state == SyncState.unavailable || state == SyncState.conflict || _busy) return;
    if (dirty) {
      await push();
    } else {
      await pull(checkOnly: true);
    }
  }

  /// Busca a cópia da nuvem e decide o que fazer. [checkOnly] = só baixa os dados se a versão mudou.
  Future<void> pull({bool checkOnly = false}) async {
    if (_busy) return;
    _busy = true;
    _set(SyncState.syncing);
    try {
      var r = await remote.fetchStudy(withData: !checkOnly);
      if (r == null) {
        _busy = false;
        if (dirty || !localIsEmpty()) {
          dirty = true;
          await push();
        } else {
          _set(SyncState.synced);
        }
        return;
      }
      if (r.version == version) {
        _busy = false;
        if (dirty) {
          await push();
        } else {
          lastSync = DateTime.now();
          _set(SyncState.synced);
        }
        return;
      }
      if (r.data == null) r = await remote.fetchStudy();
      if (r == null || r.data == null) {
        _busy = false;
        _set(SyncState.error);
        return;
      }
      final firstTimeHere = version == 0 && !localIsEmpty();
      if (dirty || firstTimeHere) {
        conflict = r;
        _busy = false;
        _set(SyncState.conflict);
        return;
      }
      _adopt(r);
      _busy = false;
    } on StudyOffline {
      _busy = false;
      _set(SyncState.offline);
    } on StudyUnavailable {
      _busy = false;
      _set(SyncState.unavailable);
    } catch (e) {
      _busy = false;
      lastError = '$e';
      _set(SyncState.error);
    }
  }

  /// Envia a cópia deste aparelho.
  Future<void> push({bool force = false}) async {
    _pushTimer?.cancel();
    if (_busy || state == SyncState.unavailable || (state == SyncState.conflict && !force)) return;
    _busy = true;
    _set(SyncState.syncing);
    final snapshot = _changes;
    try {
      final base = force ? (conflict?.version ?? version) : version;
      version = await remote.saveStudy(readLocal(), base, device);
      conflict = null;
      lastSync = DateTime.now();
      if (_changes == snapshot) dirty = false;
      await _writeMeta();
      _busy = false;
      if (dirty) {
        _set(SyncState.pending);
        _pushTimer = Timer(pushDelay, push);
      } else {
        _set(SyncState.synced);
      }
    } on StudyConflict {
      _busy = false;
      await pull();
    } on StudyOffline {
      _busy = false;
      _set(SyncState.offline);
    } on StudyUnavailable {
      _busy = false;
      _set(SyncState.unavailable);
    } catch (e) {
      _busy = false;
      lastError = '$e';
      _set(SyncState.error);
    }
  }

  /// Conflito: o aluno escolheu os dados da nuvem (os deste aparelho são substituídos).
  Future<void> useRemote() async {
    final r = conflict;
    if (r == null) return;
    _adopt(r);
  }

  /// Conflito: o aluno escolheu os dados deste aparelho (a cópia da nuvem é substituída).
  Future<void> keepLocal() async {
    if (conflict == null) return;
    dirty = true;
    await push(force: true);
  }

  /// Sincronizar agora (botão em Ajustes).
  Future<void> syncNow() async {
    if (state == SyncState.conflict) return;
    if (dirty) {
      await push();
    } else {
      await pull();
    }
  }

  void _adopt(RemoteStudy r) {
    adoptRemote(r.data!);
    version = r.version;
    dirty = false;
    conflict = null;
    lastSync = DateTime.now();
    _writeMeta();
    _set(SyncState.synced);
  }

  void _set(SyncState s) {
    if (_disposed) return;
    state = s;
    notifyListeners();
  }

  Future<void> _readMeta() async {
    try {
      if (await metaFile.exists()) {
        final j = jsonDecode(await metaFile.readAsString()) as Map<String, dynamic>;
        version = (j['version'] as num?)?.toInt() ?? 0;
        dirty = j['dirty'] as bool? ?? false;
      }
    } catch (_) {}
  }

  Future<void> _writeMeta() async {
    try {
      await metaFile.parent.create(recursive: true);
      await metaFile.writeAsString(jsonEncode({'version': version, 'dirty': dirty}), flush: true);
    } catch (_) {}
  }

  @override
  void dispose() {
    _disposed = true;
    _pushTimer?.cancel();
    _poll?.cancel();
    super.dispose();
  }
}
