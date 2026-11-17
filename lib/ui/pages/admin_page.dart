import 'package:flutter/material.dart';

import '../../core/dates.dart';
import '../../core/validation.dart';
import '../../data/auth.dart';
import '../../state/account.dart';
import '../dialogs.dart';
import '../theme.dart';
import '../widgets.dart';

/// Administração: lista de contas, concessão de administradores (só o dono) e registro de auditoria.
/// Toda a autorização é feita no servidor; esta tela apenas exibe o que ele libera.
class AdminPage extends StatefulWidget {
  const AdminPage({super.key});

  @override
  State<AdminPage> createState() => _AdminPageState();
}

class _AdminPageState extends State<AdminPage> {
  List<AccountProfile>? users;
  List<AuditEntry> audit = const [];
  String? error;
  String query = '';
  bool loading = false;

  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addPostFrameCallback((_) => _load());
  }

  Future<void> _load() async {
    final acc = AccountScope.read(context);
    if (acc == null) return;
    setState(() {
      loading = true;
      error = null;
    });
    try {
      final u = await acc.service.listProfiles();
      List<AuditEntry> a = const [];
      try {
        a = await acc.service.auditLog();
      } catch (_) {}
      if (mounted) {
        setState(() {
          users = u;
          audit = a;
        });
      }
    } on AuthError catch (e) {
      if (mounted) setState(() => error = e.message);
    } finally {
      if (mounted) setState(() => loading = false);
    }
  }

  Future<void> _setRole(AccountProfile p, Role role) async {
    final acc = AccountScope.read(context)!;
    final grant = role == Role.admin;
    final ok = await confirm(
      context,
      grant ? 'Conceder administrador' : 'Remover administrador',
      grant
          ? '${p.name.isEmpty ? p.email : p.name} poderá ver a lista de alunos (nome, e-mail e telefone) e o registro de auditoria. '
              'Conceda apenas a pessoas de confiança.'
          : '${p.name.isEmpty ? p.email : p.name} voltará a ser aluno e perderá o acesso à administração.',
      ok: grant ? 'CONCEDER' : 'REMOVER',
      danger: !grant,
    );
    if (!ok) return;
    try {
      await acc.service.setRole(p.id, role);
      if (mounted) toast(context, grant ? 'Administrador concedido.' : 'Administrador removido.');
      await _load();
    } on AuthError catch (e) {
      if (mounted) toast(context, e.message);
    }
  }

  @override
  Widget build(BuildContext context) {
    final acc = AccountScope.maybeOf(context);
    if (acc == null || !acc.isAdmin) {
      return const EmptyState(icon: Icons.lock_outline, title: 'Acesso restrito', text: 'Esta área é exclusiva de administradores.');
    }
    final list = (users ?? const <AccountProfile>[]).where((u) {
      final q = query.trim().toLowerCase();
      return q.isEmpty || u.email.toLowerCase().contains(q) || u.name.toLowerCase().contains(q) || u.phone.contains(q);
    }).toList();
    final all = users ?? const <AccountProfile>[];
    final admins = all.where((u) => u.isAdmin).length;
    final last7 = all.where((u) => DateTime.now().difference(u.createdAt).inDays < 7).length;

    return Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
      PageHeader(
        title: 'Administração',
        subtitle: acc.isOwner
            ? 'Você é o dono: só você concede ou remove administradores. Toda alteração fica registrada.'
            : 'Acesso de administrador: consulta de contas. Só o dono altera permissões.',
        actions: [
          OutlinedButton.icon(onPressed: loading ? null : _load, icon: const Icon(Icons.refresh, size: 18), label: const Text('ATUALIZAR')),
        ],
      ),
      if (error != null)
        Padding(
          padding: const EdgeInsets.fromLTRB(28, 0, 28, 12),
          child: Panel(borderColor: AppColors.red, child: Text(error!, style: AppText.body(AppColors.red))),
        ),
      Expanded(
        child: ListView(padding: const EdgeInsets.fromLTRB(28, 0, 28, 32), children: [
          Wrap(spacing: 12, runSpacing: 12, children: [
            SizedBox(width: 220, child: KpiTile(label: 'Contas', value: users == null ? '…' : thousands(all.length), icon: Icons.people_outline)),
            SizedBox(width: 220, child: KpiTile(label: 'Novas em 7 dias', value: users == null ? '…' : '$last7', icon: Icons.person_add_alt)),
            SizedBox(width: 220, child: KpiTile(label: 'Administradores', value: users == null ? '…' : '$admins', icon: Icons.admin_panel_settings_outlined, color: AppColors.gold2)),
          ]),
          const SizedBox(height: 18),
          Panel(
            padding: EdgeInsets.zero,
            child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
              Padding(
                padding: const EdgeInsets.all(16),
                child: Row(children: [
                  const Expanded(child: SectionLabel('Contas')),
                  SizedBox(
                    width: 320,
                    child: TextField(
                      onChanged: (v) => setState(() => query = v),
                      decoration: const InputDecoration(prefixIcon: Icon(Icons.search, size: 20), hintText: 'Buscar por nome, e-mail ou telefone'),
                    ),
                  ),
                ]),
              ),
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
                decoration: const BoxDecoration(color: AppColors.panel2, border: Border(bottom: BorderSide(color: AppColors.gold, width: 1.5))),
                child: Row(children: [
                  Expanded(flex: 3, child: Text('NOME', style: AppText.label(AppColors.gold))),
                  Expanded(flex: 4, child: Text('E-MAIL', style: AppText.label(AppColors.gold))),
                  Expanded(flex: 2, child: Text('CELULAR', style: AppText.label(AppColors.gold))),
                  SizedBox(width: 110, child: Text('CRIADA EM', style: AppText.label(AppColors.gold))),
                  SizedBox(width: 130, child: Text('PERMISSÃO', style: AppText.label(AppColors.gold))),
                  const SizedBox(width: 200),
                ]),
              ),
              if (users == null && loading) const Padding(padding: EdgeInsets.all(28), child: Center(child: CircularProgressIndicator())),
              if (users != null && list.isEmpty) Padding(padding: const EdgeInsets.all(24), child: Text('Nenhuma conta encontrada.', style: AppText.small())),
              for (final u in list)
                Container(
                  padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
                  decoration: const BoxDecoration(border: Border(bottom: BorderSide(color: AppColors.lineSoft))),
                  child: Row(children: [
                    Expanded(flex: 3, child: Text(u.name.isEmpty ? '—' : u.name, style: AppText.strong(), overflow: TextOverflow.ellipsis)),
                    Expanded(flex: 4, child: SelectableText(u.email, style: AppText.body(), maxLines: 1)),
                    Expanded(flex: 2, child: Text(u.phone.isEmpty ? '—' : formatPhone(u.phone), style: AppText.small(AppColors.text))),
                    SizedBox(width: 110, child: Text(fmtDate(u.createdAt), style: AppText.small())),
                    SizedBox(
                      width: 130,
                      child: Align(
                        alignment: Alignment.centerLeft,
                        child: Pill(roleLabel(u.role).toUpperCase(), color: u.isOwner ? AppColors.gold : (u.isAdmin ? AppColors.blue : AppColors.muted), filled: u.isOwner),
                      ),
                    ),
                    SizedBox(
                      width: 200,
                      child: Align(
                        alignment: Alignment.centerRight,
                        child: !acc.isOwner || u.isOwner
                            ? const SizedBox()
                            : u.isAdmin
                                ? TextButton.icon(
                                    style: TextButton.styleFrom(foregroundColor: AppColors.red),
                                    onPressed: () => _setRole(u, Role.student),
                                    icon: const Icon(Icons.remove_moderator_outlined, size: 17),
                                    label: const Text('REMOVER ADMIN'),
                                  )
                                : TextButton.icon(
                                    onPressed: () => _setRole(u, Role.admin),
                                    icon: const Icon(Icons.add_moderator_outlined, size: 17),
                                    label: const Text('TORNAR ADMIN'),
                                  ),
                      ),
                    ),
                  ]),
                ),
            ]),
          ),
          const SizedBox(height: 18),
          Panel(
            child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
              const SectionLabel('Registro de auditoria · últimas 50 alterações'),
              if (audit.isEmpty) Text('Nenhuma alteração de permissão registrada.', style: AppText.small()),
              for (final a in audit)
                Padding(
                  padding: const EdgeInsets.symmetric(vertical: 4),
                  child: Text('${fmtDate(a.at)} ${two(a.at.hour)}:${two(a.at.minute)} · ${a.actorEmail} · ${a.action} · ${a.targetEmail} ${a.detail}',
                      style: AppText.small(AppColors.text)),
                ),
            ]),
          ),
        ]),
      ),
    ]);
  }
}
