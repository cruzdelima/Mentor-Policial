import 'package:flutter/foundation.dart' show kIsWeb;
import 'package:flutter/material.dart';

import '../../core/dates.dart';
import '../../core/models.dart';
import '../../core/validation.dart';
import '../../data/auth.dart';
import '../../state/account.dart';
import '../../state/cloud_sync.dart';
import '../auth_screen.dart' show PasswordChecklist;
import '../../data/storage.dart';
import '../../platform/web_bridge.dart';
import '../../state/app_state.dart';
import '../dialogs.dart';
import '../profile_editors.dart';
import '../theme.dart';
import '../widgets.dart';

class SettingsPage extends StatefulWidget {
  const SettingsPage({super.key});

  @override
  State<SettingsPage> createState() => _SettingsPageState();
}

class _SettingsPageState extends State<SettingsPage> {
  late Profile draft;
  final name = TextEditingController();
  final target = TextEditingController();
  bool _init = false;

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    if (!_init) {
      _init = true;
      _reset();
    }
  }

  void _reset() {
    final app = AppScope.read(context);
    draft = app.profile.copy();
    name.text = draft.name;
    target.text = draft.targetName;
  }

  @override
  void dispose() {
    name.dispose();
    target.dispose();
    super.dispose();
  }

  bool _dirty(AppController app) {
    final a = app.profile.toJson().toString();
    final b = (draft.copy()
          ..name = name.text.trim()
          ..targetName = target.text.trim())
        .toJson()
        .toString();
    return a != b;
  }

  void _save(AppController app) {
    final p = draft.copy()
      ..name = name.text.trim()
      ..targetName = target.text.trim();
    final replans = p.planSignature != app.profile.planSignature;
    app.updateProfile(p);
    toast(context, replans ? 'Salvo. Cronograma recalculado a partir de hoje.' : 'Alterações salvas.');
    setState(() {});
  }

  @override
  Widget build(BuildContext context) {
    final app = AppScope.of(context);
    final dirty = _dirty(app);
    final replans = (draft.copy()).planSignature != app.profile.planSignature;
    return Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
      PageHeader(
        title: 'Ajustes',
        subtitle: 'Perfil, concurso, rotina e seus dados. Mudanças na rotina recalculam o cronograma a partir de hoje — nada do que você já fez se perde.',
        actions: [
          if (dirty) ...[
            TextButton(
              onPressed: () => setState(_reset),
              child: const Text('DESCARTAR'),
            ),
            ElevatedButton.icon(onPressed: () => _save(app), icon: const Icon(Icons.save_outlined, size: 18), label: Text(replans ? 'SALVAR E REPLANEJAR' : 'SALVAR')),
          ],
        ],
      ),
      Expanded(
        child: ListView(padding: const EdgeInsets.fromLTRB(28, 0, 28, 40), children: [
          if (AccountScope.maybeOf(context) != null) ...[const _AccountPanel(), const SizedBox(height: 16)],
          Panel(
            child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              const SectionLabel('Perfil e concurso'),
              Wrap(spacing: 16, runSpacing: 16, children: [
                SizedBox(width: 300, child: TextField(controller: name, onChanged: (_) => setState(() {}), decoration: const InputDecoration(labelText: 'Nome'))),
                SizedBox(
                  width: 300,
                  child: TextField(
                    controller: target,
                    onChanged: (_) => setState(() {}),
                    decoration: const InputDecoration(labelText: 'Concurso específico (opcional)', hintText: 'Ex.: PF 2027'),
                  ),
                ),
              ]),
              const SizedBox(height: 18),
              Row(children: [
                Pill(draft.esfera.toUpperCase(), color: AppColors.esfera(draft.esfera), filled: true),
                const SizedBox(width: 10),
                Expanded(
                  child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                    Text('${app.catalog.careerOrNull(draft.careerCode)?.name ?? draft.careerCode} · ${app.catalog.cargoOrNull(draft.optionId)?.name ?? '—'}',
                        style: AppText.strong()),
                    if (app.catalog.cargoOrNull(draft.optionId)?.isContest ?? false)
                      Text('Pós-edital: o plano segue o edital deste concurso.', style: AppText.small(AppColors.gold2)),
                  ]),
                ),
                OutlinedButton.icon(
                  onPressed: () => _changeTarget(context),
                  icon: const Icon(Icons.swap_horiz, size: 18),
                  label: const Text('TROCAR CONCURSO / CARGO'),
                ),
              ]),
            ]),
          ),
          const SizedBox(height: 16),
          Panel(
            child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              const SectionLabel('Rotina e nível'),
              RoutineEditor(catalog: app.catalog, profile: draft, today: app.today, onChanged: () => setState(() {})),
            ]),
          ),
          const SizedBox(height: 16),
          const _DataPanel(),
          const SizedBox(height: 16),
          const _AboutPanel(),
        ]),
      ),
    ]);
  }

  Future<void> _changeTarget(BuildContext context) async {
    final app = AppScope.read(context);
    final cat = app.catalog;
    var esfera = draft.esfera, career = draft.careerCode, option = draft.optionId;
    final ok = await showDialog<bool>(
      context: context,
      builder: (ctx) => StatefulBuilder(builder: (ctx, setState) {
        final careerObj = career.isEmpty ? null : cat.career(career);
        return AlertDialog(
          title: Text('TROCAR CONCURSO E CARGO', style: AppText.h2()),
          content: SizedBox(
            width: 1080,
            height: 620,
            child: SingleChildScrollView(
              child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                Text('ESFERA', style: AppText.label(AppColors.gold)),
                const SizedBox(height: 10),
                EsferaPicker(
                  catalog: cat,
                  value: esfera,
                  onChanged: (e) => setState(() {
                    if (e != esfera) {
                      career = '';
                      option = '';
                    }
                    esfera = e;
                  }),
                ),
                const SizedBox(height: 22),
                Text('CONCURSO', style: AppText.label(AppColors.gold)),
                const SizedBox(height: 10),
                CareerPicker(
                  catalog: cat,
                  esfera: esfera,
                  value: career.isEmpty ? null : career,
                  onChanged: (c) => setState(() {
                    if (c != career) option = '';
                    career = c;
                    final co = cat.career(c);
                    if (co.cargos.length == 1) option = co.cargos.first.id;
                  }),
                ),
                if (careerObj != null) ...[
                  const SizedBox(height: 22),
                  Text('CARGO', style: AppText.label(AppColors.gold)),
                  const SizedBox(height: 10),
                  CargoPicker(catalog: cat, career: careerObj, value: option.isEmpty ? null : option, onChanged: (o) => setState(() => option = o)),
                ],
              ]),
            ),
          ),
          actions: [
            TextButton(onPressed: () => Navigator.pop(ctx, false), child: const Text('CANCELAR')),
            ElevatedButton(
              onPressed: option.isEmpty ? null : () => Navigator.pop(ctx, true),
              child: Text(cat.cargoOrNull(option)?.isContest ?? false ? 'USAR ESTE CONCURSO' : 'USAR ESTE CARGO'),
            ),
          ],
        );
      }),
    );
    if (ok == true) {
      setState(() {
        draft.targetName = target.text.trim();
        selectOption(cat, draft, option, today: app.today);
        target.text = draft.targetName;
      });
    }
  }
}

class _DataPanel extends StatelessWidget {
  const _DataPanel();

  @override
  Widget build(BuildContext context) {
    final app = AppScope.of(context);
    return Panel(
      child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
        const SectionLabel('Seus dados'),
        if (kIsWeb)
          Text('No navegador, seus dados ficam guardados neste navegador e na cópia da nuvem da sua conta. '
              'Exporte um backup de vez em quando para ter uma cópia em arquivo.', style: AppText.small())
        else ...[
          Text('Tudo fica salvo $kNeste. Uma cópia de segurança diária é feita automaticamente (últimos 15 dias).', style: AppText.small()),
          const SizedBox(height: 8),
          SelectableText(app.storage.dir, style: AppText.small(AppColors.dim)),
        ],
        const SizedBox(height: 14),
        Wrap(spacing: 10, runSpacing: 10, children: [
          if (!kIsWeb)
            OutlinedButton.icon(
              onPressed: () => openExternal(app.storage.dir),
              icon: const Icon(Icons.folder_open_outlined, size: 18),
              label: const Text('ABRIR PASTA DE DADOS'),
            ),
          OutlinedButton.icon(
            onPressed: () async {
              try {
                final path = await app.exportBackup();
                if (context.mounted) toast(context, kIsWeb ? 'Backup baixado: $path' : 'Backup salvo em: $path');
              } catch (e) {
                if (context.mounted) toast(context, 'Falha ao exportar: $e');
              }
            },
            icon: const Icon(Icons.download_outlined, size: 18),
            label: const Text('EXPORTAR BACKUP'),
          ),
          OutlinedButton.icon(
            onPressed: () => _import(context),
            icon: const Icon(Icons.upload_outlined, size: 18),
            label: const Text('IMPORTAR BACKUP'),
          ),
          OutlinedButton.icon(
            style: OutlinedButton.styleFrom(foregroundColor: AppColors.red, side: const BorderSide(color: AppColors.red)),
            onPressed: () async {
              final ok = await confirm(
                context,
                'Apagar tudo',
                'Perfil, diário, missões concluídas e anotações serão apagados${kIsWeb ? '' : ' deste computador'}. Exporte um backup antes se quiser guardar.',
                ok: 'APAGAR TUDO',
                danger: true,
              );
              if (ok) app.resetAll();
            },
            icon: const Icon(Icons.delete_forever_outlined, size: 18),
            label: const Text('APAGAR TUDO'),
          ),
        ]),
      ]),
    );
  }

  Future<void> _import(BuildContext context) async {
    final app = AppScope.read(context);
    if (kIsWeb) {
      try {
        final text = await webPickText('.json,application/json');
        if (text == null || !context.mounted) return;
        final ok = await confirm(context, 'Importar backup', 'Os dados atuais serão substituídos pelos do arquivo escolhido.', ok: 'IMPORTAR');
        if (!ok) return;
        app.importBackupText(text);
        if (context.mounted) toast(context, 'Backup importado.');
      } catch (e) {
        if (context.mounted) toast(context, 'Falha ao importar: $e');
      }
      return;
    }
    final c = TextEditingController();
    final path = await showDialog<String>(
      context: context,
      builder: (ctx) => AlertDialog(
        title: Text('IMPORTAR BACKUP', style: AppText.h2()),
        content: SizedBox(
          width: 520,
          child: Column(mainAxisSize: MainAxisSize.min, crossAxisAlignment: CrossAxisAlignment.stretch, children: [
            Text('Cole o caminho do arquivo .json exportado (no Windows: clique com o botão direito no arquivo › "Copiar como caminho").',
                style: AppText.small()),
            const SizedBox(height: 12),
            TextField(controller: c, autofocus: true, decoration: const InputDecoration(labelText: 'Caminho do backup')),
            const SizedBox(height: 8),
            Text('Os dados atuais serão substituídos.', style: AppText.small(AppColors.amber)),
          ]),
        ),
        actions: [
          TextButton(onPressed: () => Navigator.pop(ctx), child: const Text('CANCELAR')),
          ElevatedButton(onPressed: () => Navigator.pop(ctx, c.text), child: const Text('IMPORTAR')),
        ],
      ),
    );
    if (path == null || path.trim().isEmpty) return;
    try {
      await app.importBackup(path);
      if (context.mounted) toast(context, 'Backup importado.');
    } catch (e) {
      if (context.mounted) toast(context, 'Não foi possível importar: $e');
    }
  }
}

class _AboutPanel extends StatelessWidget {
  const _AboutPanel();

  @override
  Widget build(BuildContext context) {
    final app = AppScope.of(context);
    return Panel(
      child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
        const SectionLabel('Sobre'),
        Row(children: [
          const BadgeLogo(size: 44),
          const SizedBox(width: 14),
          Expanded(
            child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              Text('TATICUM · v$kAppVersion', style: AppText.h3()),
              Text('$kAppChannel · catálogo ${app.catalog.version} · ${app.content.items.length} material(is) liberado(s)', style: AppText.small()),
            ]),
          ),
        ]),
        const SizedBox(height: 12),
        Text(
          'Versão de testes: anote o que travou, o que ficou confuso e o que faria você usar todos os dias — e envie para a equipe do Taticum. '
          'Os pesos e assuntos seguem o núcleo comum dos últimos editais; confira sempre o edital do seu concurso.',
          style: AppText.small(),
        ),
        const SizedBox(height: 8),
        Text('Fontes tipográficas: Barlow e Barlow Condensed (SIL Open Font License).', style: AppText.small(AppColors.dim)),
      ]),
    );
  }
}

class _AccountPanel extends StatelessWidget {
  const _AccountPanel();

  @override
  Widget build(BuildContext context) {
    final acc = AccountScope.maybeOf(context)!;
    final p = acc.profile;
    return Panel(
      accent: AppColors.gold,
      child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
        const SectionLabel('Minha conta'),
        Wrap(spacing: 28, runSpacing: 12, children: [
          _info('E-mail', acc.email),
          _info('Celular', p == null || p.phone.isEmpty ? '—' : formatPhone(p.phone)),
          _info('Permissão', p == null ? '—' : roleLabel(p.role)),
          _info('Acesso', p == null ? '—' : _accessText(p)),
        ]),
        if (acc.offline) ...[
          const SizedBox(height: 10),
          Text('Sem conexão: seus estudos continuam salvos $kNeste. Os dados da conta serão atualizados quando a internet voltar.',
              style: AppText.small(AppColors.amber)),
        ],
        if (acc.app?.sync != null) ...[
          const SizedBox(height: 14),
          ListenableBuilder(listenable: acc.app!.sync!, builder: (context, _) => _SyncLine(sync: acc.app!.sync!)),
        ],
        const SizedBox(height: 16),
        Wrap(spacing: 10, runSpacing: 10, children: [
          OutlinedButton.icon(
            onPressed: p == null ? null : () => _editProfile(context, p),
            icon: const Icon(Icons.edit_outlined, size: 18),
            label: const Text('EDITAR NOME E CELULAR'),
          ),
          OutlinedButton.icon(
            onPressed: acc.offline ? null : () => _changePassword(context),
            icon: const Icon(Icons.password, size: 18),
            label: const Text('ALTERAR SENHA'),
          ),
          OutlinedButton.icon(
            onPressed: () async {
              if (await confirm(context, 'Sair da conta', 'Seus estudos continuam salvos $kNeste e voltam quando você entrar de novo.', ok: 'SAIR')) {
                await acc.signOut();
              }
            },
            icon: const Icon(Icons.logout, size: 18),
            label: const Text('SAIR'),
          ),
          OutlinedButton.icon(
            style: OutlinedButton.styleFrom(foregroundColor: AppColors.red, side: const BorderSide(color: AppColors.red)),
            onPressed: acc.offline || (p?.isOwner ?? false) ? null : () => _deleteAccount(context),
            icon: const Icon(Icons.person_remove_outlined, size: 18),
            label: const Text('EXCLUIR MINHA CONTA'),
          ),
        ]),
      ]),
    );
  }

  Widget _info(String label, String value) => Column(crossAxisAlignment: CrossAxisAlignment.start, mainAxisSize: MainAxisSize.min, children: [
        Text(label.toUpperCase(), style: AppText.label()),
        const SizedBox(height: 4),
        Text(value, style: AppText.strong()),
      ]);

  Future<void> _editProfile(BuildContext context, AccountProfile p) async {
    final acc = AccountScope.read(context)!;
    final name = TextEditingController(text: p.name);
    final phone = TextEditingController(text: p.phone.isEmpty ? '' : formatPhone(p.phone));
    String? error;
    await showDialog<void>(
      context: context,
      builder: (ctx) => StatefulBuilder(builder: (ctx, setState) {
        return AlertDialog(
          title: Text('EDITAR CONTA', style: AppText.h2()),
          content: SizedBox(
            width: 420,
            child: Column(mainAxisSize: MainAxisSize.min, children: [
              TextField(controller: name, decoration: const InputDecoration(labelText: 'Nome completo')),
              const SizedBox(height: 12),
              TextField(controller: phone, decoration: const InputDecoration(labelText: 'Celular com DDD')),
              if (error != null) Padding(padding: const EdgeInsets.only(top: 10), child: Text(error!, style: AppText.small(AppColors.red))),
            ]),
          ),
          actions: [
            TextButton(onPressed: () => Navigator.pop(ctx), child: const Text('CANCELAR')),
            ElevatedButton(
              onPressed: () async {
                final ph = normalizePhone(phone.text);
                if (name.text.trim().length < 2 || ph == null) {
                  setState(() => error = 'Confira o nome e o celular (com DDD).');
                  return;
                }
                try {
                  await acc.service.updateMyProfile(name: name.text, phone: ph);
                  await acc.refreshProfile();
                  if (ctx.mounted) Navigator.pop(ctx);
                } on AuthError catch (e) {
                  setState(() => error = e.message);
                }
              },
              child: const Text('SALVAR'),
            ),
          ],
        );
      }),
    );
  }

  Future<void> _changePassword(BuildContext context) async {
    final acc = AccountScope.read(context)!;
    final p1 = TextEditingController();
    final p2 = TextEditingController();
    String? error;
    await showDialog<void>(
      context: context,
      builder: (ctx) => StatefulBuilder(builder: (ctx, setState) {
        return AlertDialog(
          title: Text('ALTERAR SENHA', style: AppText.h2()),
          content: SizedBox(
            width: 440,
            child: Column(mainAxisSize: MainAxisSize.min, crossAxisAlignment: CrossAxisAlignment.start, children: [
              TextField(controller: p1, obscureText: true, onChanged: (_) => setState(() {}), decoration: const InputDecoration(labelText: 'Nova senha')),
              const SizedBox(height: 10),
              PasswordChecklist(password: p1.text),
              const SizedBox(height: 12),
              TextField(controller: p2, obscureText: true, decoration: const InputDecoration(labelText: 'Repita a nova senha')),
              if (error != null) Padding(padding: const EdgeInsets.only(top: 10), child: Text(error!, style: AppText.small(AppColors.red))),
            ]),
          ),
          actions: [
            TextButton(onPressed: () => Navigator.pop(ctx), child: const Text('CANCELAR')),
            ElevatedButton(
              onPressed: () async {
                final problem = passwordProblem(p1.text) ?? (p1.text != p2.text ? 'As senhas não conferem.' : null);
                if (problem != null) {
                  setState(() => error = problem);
                  return;
                }
                try {
                  await acc.service.changePassword(p1.text);
                  if (ctx.mounted) Navigator.pop(ctx);
                  if (context.mounted) toast(context, 'Senha alterada.');
                } on AuthError catch (e) {
                  setState(() => error = e.message);
                }
              },
              child: const Text('SALVAR'),
            ),
          ],
        );
      }),
    );
  }

  Future<void> _deleteAccount(BuildContext context) async {
    final acc = AccountScope.read(context)!;
    final c = TextEditingController();
    final ok = await showDialog<bool>(
      context: context,
      builder: (ctx) => StatefulBuilder(builder: (ctx, setState) {
        return AlertDialog(
          title: Text('EXCLUIR MINHA CONTA', style: AppText.h2(AppColors.red)),
          content: SizedBox(
            width: 460,
            child: Column(mainAxisSize: MainAxisSize.min, crossAxisAlignment: CrossAxisAlignment.start, children: [
              Text('Sua conta e seus dados pessoais serão apagados do servidor, e seus estudos serão apagados $kDeste. '
                  'Isso não pode ser desfeito.', style: AppText.body(AppColors.muted)),
              const SizedBox(height: 14),
              Text('Para confirmar, digite EXCLUIR:', style: AppText.small(AppColors.text)),
              const SizedBox(height: 8),
              TextField(controller: c, onChanged: (_) => setState(() {})),
            ]),
          ),
          actions: [
            TextButton(onPressed: () => Navigator.pop(ctx, false), child: const Text('CANCELAR')),
            ElevatedButton(
              style: ElevatedButton.styleFrom(backgroundColor: AppColors.red),
              onPressed: c.text.trim().toUpperCase() == 'EXCLUIR' ? () => Navigator.pop(ctx, true) : null,
              child: const Text('EXCLUIR DEFINITIVAMENTE'),
            ),
          ],
        );
      }),
    );
    if (ok != true) return;
    try {
      await acc.deleteAccount();
    } on AuthError catch (e) {
      if (context.mounted) toast(context, e.message);
    }
  }
}

/// Como o aluno vê a própria classificação.
String _accessText(AccountProfile p) {
  if (p.isAdmin) return 'Completo (${roleLabel(p.role).toLowerCase()})';
  return switch (p.plan) {
    Plan.beta => 'Testador Beta · acesso gratuito',
    Plan.tester => 'Testador · acesso gratuito',
    Plan.monthly || Plan.annual =>
      '${planLabel(p.plan)}${p.planExpiresAt == null ? '' : ' · válida até ${fmtDate(p.planExpiresAt!)}'}',
    Plan.none => 'Gratuito durante os testes',
  };
}

/// Situação do progresso na nuvem, com o botão de sincronizar.
class _SyncLine extends StatelessWidget {
  const _SyncLine({required this.sync});
  final CloudSync sync;

  @override
  Widget build(BuildContext context) {
    final t = sync.lastSync;
    final at = t == null ? '' : ' às ${two(t.hour)}:${two(t.minute)}';
    final (IconData icon, Color color, String text) = switch (sync.state) {
      SyncState.synced => (Icons.cloud_done_outlined, AppColors.green, 'Progresso salvo na nuvem$at. Entre em outro aparelho com esta conta e continue de onde parou.'),
      SyncState.pending || SyncState.syncing || SyncState.starting => (Icons.cloud_upload_outlined, AppColors.muted, 'Enviando seu progresso para a nuvem…'),
      SyncState.offline => (Icons.cloud_off_outlined, AppColors.amber, 'Sem internet: o progresso está salvo $kNeste e sobe para a nuvem quando a conexão voltar.'),
      SyncState.conflict => (Icons.cloud_sync_outlined, AppColors.amber, 'O progresso $kDeste e o da nuvem são diferentes. Escolha qual manter na faixa no topo da tela.'),
      SyncState.unavailable => (Icons.cloud_off_outlined, AppColors.muted, 'O salvamento na nuvem ainda não foi ativado no servidor.'),
      SyncState.error => (Icons.error_outline, AppColors.red, 'Não foi possível salvar na nuvem agora. Tentaremos de novo em alguns minutos.'),
    };
    return Row(children: [
      Icon(icon, size: 20, color: color),
      const SizedBox(width: 8),
      Expanded(child: Text(text, style: AppText.small(color == AppColors.muted ? AppColors.text : color))),
      if (sync.state != SyncState.unavailable && sync.state != SyncState.conflict)
        TextButton.icon(
          onPressed: sync.state == SyncState.syncing ? null : sync.syncNow,
          icon: const Icon(Icons.sync, size: 17),
          label: const Text('SINCRONIZAR AGORA'),
        ),
    ]);
  }
}
