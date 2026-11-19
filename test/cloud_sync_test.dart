import 'dart:io';

import 'package:flutter_test/flutter_test.dart';
import 'package:mentor_policial/state/cloud_sync.dart';

/// Nuvem falsa: mesma regra de versão da função save_study.
class FakeCloud implements StudyRemote {
  Map<String, dynamic>? data;
  int version = 0;
  String device = '';
  bool unavailable = false;

  @override
  Future<RemoteStudy?> fetchStudy({bool withData = true}) async {
    if (unavailable) throw StudyUnavailable();
    if (data == null) return null;
    return RemoteStudy(version: version, device: device, updatedAt: DateTime(2026, 11, 19), data: withData ? Map.of(data!) : null);
  }

  @override
  Future<int> saveStudy(Map<String, dynamic> d, int baseVersion, String dev) async {
    if (unavailable) throw StudyUnavailable();
    if (baseVersion != version) throw StudyConflict();
    data = Map.of(d);
    device = dev;
    return ++version;
  }
}

class Device {
  Device(this.name, this.cloud, {Map<String, dynamic>? local}) : local = local ?? {} {
    final dir = Directory.systemTemp.createTempSync('taticum_sync_');
    sync = CloudSync(
      remote: cloud,
      metaPath: '${dir.path}/nuvem.json',
      device: name,
      readLocal: () => Map.of(this.local),
      adoptRemote: (d) => this.local = Map.of(d),
      localIsEmpty: () => this.local['profile'] == null,
      pushDelay: const Duration(hours: 1),
      pollEvery: const Duration(hours: 1),
    );
  }
  final String name;
  final FakeCloud cloud;
  Map<String, dynamic> local;
  late final CloudSync sync;

  Future<void> edit(String key, Object value) async {
    local[key] = value;
    sync.markDirty();
    await sync.push();
  }
}

void main() {
  test('dois aparelhos: envia, recebe e resolve conflito', () async {
    final cloud = FakeCloud();
    final pc = Device('PC', cloud, local: {'profile': 'Yann', 'dias': 1});
    await pc.sync.start();
    expect(cloud.version, 1, reason: 'primeiro aparelho envia o que já tinha');
    expect(pc.sync.state, SyncState.synced);

    final tablet = Device('Tablet', cloud);
    await tablet.sync.start();
    expect(tablet.local['dias'], 1, reason: 'aparelho novo recebe o progresso da nuvem');

    await pc.edit('dias', 2);
    expect(cloud.version, 2);
    await tablet.sync.pull(checkOnly: true);
    expect(tablet.local['dias'], 2, reason: 'quem não mudou nada adota a versão mais nova');

    // Os dois mudam sem sincronizar entre si.
    await pc.edit('dias', 3);
    tablet.local['dias'] = 99;
    tablet.sync.markDirty();
    await tablet.sync.push();
    expect(tablet.sync.state, SyncState.conflict);
    expect(tablet.sync.conflict?.device, 'PC');

    await tablet.sync.keepLocal();
    expect(cloud.data!['dias'], 99);
    expect(tablet.sync.state, SyncState.synced);

    await pc.sync.pull();
    expect(pc.local['dias'], 99);

    pc.sync.dispose();
    tablet.sync.dispose();
  });

  test('primeira vez em um aparelho que já tinha dados: pergunta ao aluno', () async {
    final cloud = FakeCloud()
      ..data = {'profile': 'Yann', 'dias': 5}
      ..version = 3
      ..device = 'PC';
    final note = Device('Notebook', cloud, local: {'profile': 'Yann', 'dias': 1});
    await note.sync.start();
    expect(note.sync.state, SyncState.conflict);
    await note.sync.useRemote();
    expect(note.local['dias'], 5);
    expect(note.sync.version, 3);
    note.sync.dispose();
  });

  test('servidor sem a migração: sincronização desligada sem erro', () async {
    final cloud = FakeCloud()..unavailable = true;
    final pc = Device('PC', cloud, local: {'profile': 'Yann'});
    await pc.sync.start();
    expect(pc.sync.state, SyncState.unavailable);
    pc.sync.markDirty();
    expect(pc.sync.state, SyncState.unavailable);
    pc.sync.dispose();
  });
}
