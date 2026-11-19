import 'package:flutter/material.dart';

import '../../core/bancas.dart';
import '../../core/catalog.dart';
import '../../data/content.dart';
import '../../state/account.dart';
import '../../state/app_state.dart';
import '../dialogs.dart';
import '../theme.dart';
import '../widgets.dart';

/// Checklist de produção de conteúdo (ADMIN › MATERIAIS): para cada concurso ou cargo, cada assunto do edital com
/// o aprofundado e o resumo, marcando o que já foi lançado na plataforma e o que já foi validado (liberado aos alunos).
///
/// As marcas não são manuais: "lançado" vem da biblioteca de conteúdo do app (o material existe para o assunto) e
/// "validado" vem da revisão do dono (botão REVISEI). Assim o checklist nunca fica desatualizado.
class ContentChecklist extends StatefulWidget {
  const ContentChecklist({super.key});

  @override
  State<ContentChecklist> createState() => _ContentChecklistState();
}

enum _Filter { all, missing, pending, ready }

class _ContentChecklistState extends State<ContentChecklist> {
  String? optionId;
  _Filter filter = _Filter.all;
  final Set<String> busy = {};

  /// Opções da lista: concursos pós-edital primeiro, depois os cargos do ciclo básico.
  List<({String id, String label, String group})> _options(Catalog cat) => [
        for (final c in cat.contests) (id: c.id, label: c.name, group: 'Concursos (pós-edital)'),
        for (final career in cat.careers)
          for (final c in career.cycleCargos) (id: c.id, label: '${career.name} · ${c.name}', group: 'Ciclo básico'),
      ];

  Future<void> _toggle(AppController app, MaterialInfo m, bool approve) async {
    final ok = await confirm(
      context,
      approve ? 'VALIDAR E LIBERAR' : 'RECOLHER PARA REVISÃO',
      approve
          ? 'Confirma que revisou "${m.title}" (${m.isDeep ? 'aprofundado' : 'resumo'})? Ele passa a aparecer para todos os alunos.'
          : '"${m.title}" (${m.isDeep ? 'aprofundado' : 'resumo'}) deixa de aparecer para os alunos até você liberar de novo.',
      ok: approve ? 'LIBERAR' : 'RECOLHER',
      danger: !approve,
    );
    if (!ok || !mounted) return;
    setState(() => busy.add(m.id));
    try {
      await app.setReviewed(m, approve);
      if (mounted) toast(context, approve ? 'Material validado e liberado.' : 'Material recolhido para revisão.');
    } catch (e) {
      if (mounted) toast(context, 'Não foi possível salvar: $e');
    } finally {
      if (mounted) setState(() => busy.remove(m.id));
    }
  }

  @override
  Widget build(BuildContext context) {
    final app = AppScope.of(context);
    final owner = AccountScope.maybeOf(context)?.isOwner ?? false;
    final cat = app.catalog;
    final options = _options(cat);
    if (options.isEmpty) {
      return const EmptyState(icon: Icons.inventory_2_outlined, title: 'Nenhum concurso', text: 'Cadastre um concurso ou cargo no catálogo.');
    }
    final current = optionId != null && options.any((o) => o.id == optionId)
        ? optionId!
        : (options.any((o) => o.id == app.profile.optionId) ? app.profile.optionId : options.first.id);
    final career = cat.careerOfOption(current)!;
    final cargo = cat.cargo(current);
    final bancaName = cargo.contest?.banca ?? career.banca;
    final profile = bancaProfileOf(bancaName);

    // Assuntos do edital, por matéria, na ordem do edital.
    final subjects = cat.subjects.where((s) => s.weightFor(current) > 0).toList();
    if (cargo.isContest) {
      int pos(Subject s) {
        final ts = cat.topicsFor(s.id, career.code, current);
        return ts.isEmpty ? 1 << 20 : (cat.contestPosition(current, ts.first.id) ?? 1 << 20);
      }

      subjects.sort((a, b) => pos(a).compareTo(pos(b)));
    }
    final rows = <Subject, List<_Row>>{};
    for (final s in subjects) {
      final list = <_Row>[];
      for (final t in cat.topicsFor(s.id, career.code, current)) {
        final mats = app.content.all.where((m) => m.topicIds.contains(t.id)).toList();
        final deep = mats.where((m) => m.isDeep).firstOrNull;
        final res = mats.where((m) => !m.isDeep).firstOrNull;
        list.add(_Row(t, deep, res, app.content));
      }
      if (list.isNotEmpty) rows[s] = list;
    }
    final all = rows.values.expand((x) => x).toList();
    final launched = all.where((r) => r.launched).length;
    final validated = all.where((r) => r.validated).length;
    final missing = all.length - launched;

    bool keep(_Row r) => switch (filter) {
          _Filter.all => true,
          _Filter.missing => !r.launched,
          _Filter.pending => r.launched && !r.validated,
          _Filter.ready => r.validated,
        };

    return ListView(padding: const EdgeInsets.fromLTRB(28, 0, 28, 32), children: [
      Wrap(spacing: 12, runSpacing: 12, crossAxisAlignment: WrapCrossAlignment.center, children: [
        SizedBox(
          width: 520,
          child: DropdownButtonFormField<String>(
            initialValue: current,
            isExpanded: true,
            decoration: const InputDecoration(labelText: 'Concurso ou cargo'),
            items: [
              for (final o in options)
                DropdownMenuItem(value: o.id, child: Text('${o.group == 'Ciclo básico' ? 'Ciclo básico · ' : ''}${o.label}', overflow: TextOverflow.ellipsis)),
            ],
            onChanged: (v) => setState(() => optionId = v),
          ),
        ),
        Pill('BANCA: ${bancaName.isEmpty ? '—' : bancaName.toUpperCase()}', color: AppColors.blue),
        Pill('VERSÃO DOS MATERIAIS: ${bancaVariantLabel(profile).toUpperCase()}', color: AppColors.muted),
      ]),
      const SizedBox(height: 14),
      Wrap(spacing: 12, runSpacing: 12, children: [
        SizedBox(width: 200, child: KpiTile(label: 'Assuntos do edital', value: '${all.length}', icon: Icons.list_alt)),
        SizedBox(width: 200, child: KpiTile(label: 'Lançados (os dois)', value: '$launched', icon: Icons.upload_file_outlined, color: AppColors.blue)),
        SizedBox(width: 200, child: KpiTile(label: 'Validados e liberados', value: '$validated', icon: Icons.verified_outlined, color: AppColors.green)),
        SizedBox(width: 200, child: KpiTile(label: 'Falta produzir', value: '$missing', icon: Icons.pending_actions_outlined, color: AppColors.amber)),
      ]),
      const SizedBox(height: 12),
      Wrap(spacing: 6, runSpacing: 6, children: [
        ToggleChip(label: 'TODOS', selected: filter == _Filter.all, onTap: () => setState(() => filter = _Filter.all)),
        ToggleChip(label: 'FALTA PRODUZIR', selected: filter == _Filter.missing, color: AppColors.amber, onTap: () => setState(() => filter = _Filter.missing)),
        ToggleChip(label: 'FALTA VALIDAR', selected: filter == _Filter.pending, color: AppColors.blue, onTap: () => setState(() => filter = _Filter.pending)),
        ToggleChip(label: 'PRONTOS', selected: filter == _Filter.ready, color: AppColors.green, onTap: () => setState(() => filter = _Filter.ready)),
      ]),
      const SizedBox(height: 6),
      Text(
        'As marcas são automáticas: “lançado” quando o material está no app; “validado” quando você aperta REVISEI '
        '(aqui ou na tela do material). ${owner ? 'Clique na marca de validado para liberar ou recolher.' : ''}',
        style: AppText.small(),
      ),
      const SizedBox(height: 14),
      for (final e in rows.entries)
        if (e.value.any(keep))
          _SubjectBlock(
            subject: e.key,
            rows: e.value.where(keep).toList(),
            total: e.value,
            profile: profile,
            owner: owner,
            busy: busy,
            onToggle: (m, v) => _toggle(app, m, v),
            onOpen: (m) => app.goTo(AppPage.materials, materialId: m.id),
          ),
      if (!rows.values.expand((x) => x).any(keep))
        Padding(padding: const EdgeInsets.all(24), child: Text('Nenhum assunto neste filtro.', style: AppText.small())),
    ]);
  }
}

class _Row {
  _Row(this.topic, this.deep, this.res, this.lib);
  final Topic topic;
  final MaterialInfo? deep;
  final MaterialInfo? res;
  final ContentLibrary lib;

  bool get launched => deep != null && res != null;
  bool get validated => launched && lib.isApproved(deep!) && lib.isApproved(res!);
}

class _SubjectBlock extends StatelessWidget {
  const _SubjectBlock({
    required this.subject,
    required this.rows,
    required this.total,
    required this.profile,
    required this.owner,
    required this.busy,
    required this.onToggle,
    required this.onOpen,
  });
  final Subject subject;
  final List<_Row> rows;
  final List<_Row> total;
  final String profile;
  final bool owner;
  final Set<String> busy;
  final void Function(MaterialInfo, bool) onToggle;
  final void Function(MaterialInfo) onOpen;

  @override
  Widget build(BuildContext context) {
    final launched = total.where((r) => r.launched).length;
    final validated = total.where((r) => r.validated).length;
    Widget head(String t, double w) => SizedBox(width: w, child: Text(t, style: AppText.label(AppColors.gold), textAlign: TextAlign.center));
    return Padding(
      padding: const EdgeInsets.only(bottom: 16),
      child: Panel(
        padding: EdgeInsets.zero,
        child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
          Padding(
            padding: const EdgeInsets.fromLTRB(16, 14, 16, 10),
            child: Row(children: [
              SubjectTag(subject),
              const SizedBox(width: 10),
              Expanded(child: Text(subject.name, style: AppText.strong(), overflow: TextOverflow.ellipsis)),
              Text('$launched/${total.length} lançados · $validated/${total.length} validados', style: AppText.small()),
            ]),
          ),
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
            decoration: const BoxDecoration(color: AppColors.panel2, border: Border(bottom: BorderSide(color: AppColors.gold, width: 1.5))),
            child: Row(children: [
              SizedBox(width: 36, child: Text('Nº', style: AppText.label(AppColors.gold))),
              Expanded(child: Text('ASSUNTO DO EDITAL', style: AppText.label(AppColors.gold))),
              head('APROF. LANÇADO', 100),
              head('APROF. VALIDADO', 104),
              head('RESUMO LANÇADO', 100),
              head('RESUMO VALIDADO', 104),
            ]),
          ),
          for (var i = 0; i < rows.length; i++) _line(context, rows[i], i + 1),
        ]),
      ),
    );
  }

  Widget _line(BuildContext context, _Row r, int n) {
    final open = r.deep ?? r.res;
    final noVariant = [r.deep, r.res].whereType<MaterialInfo>().where((m) => profile != 'cebraspe' && !m.variants.contains(profile)).isNotEmpty;
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
      decoration: const BoxDecoration(border: Border(bottom: BorderSide(color: AppColors.lineSoft))),
      child: Row(children: [
        SizedBox(width: 36, child: Text('$n', style: AppText.small(AppColors.dim))),
        Expanded(
          child: Wrap(crossAxisAlignment: WrapCrossAlignment.center, spacing: 8, runSpacing: 4, children: [
            InkWell(
              onTap: open == null ? null : () => onOpen(open),
              child: Text(r.topic.name, style: AppText.body(open == null ? AppColors.text : AppColors.gold2)),
            ),
            if (r.topic.contest != null) const Pill('SÓ DESTE EDITAL', color: AppColors.amber),
            if (noVariant) Pill('SEM VERSÃO ${bancaVariantLabel(profile).toUpperCase()}', color: AppColors.red),
          ]),
        ),
        SizedBox(width: 100, child: Center(child: _Mark(on: r.deep != null))),
        SizedBox(width: 104, child: Center(child: _review(r.deep))),
        SizedBox(width: 100, child: Center(child: _Mark(on: r.res != null))),
        SizedBox(width: 104, child: Center(child: _review(r.res))),
      ]),
    );
  }

  Widget _review(MaterialInfo? m) {
    if (m == null) return const _Mark(on: false, disabled: true);
    if (busy.contains(m.id)) return const SizedBox(width: 18, height: 18, child: CircularProgressIndicator(strokeWidth: 2));
    return Builder(builder: (context) {
      final approved = AppScope.of(context).content.isApproved(m);
      final mark = _Mark(on: approved, color: AppColors.green);
      if (!owner) return mark;
      return Tooltip(
        message: approved ? 'Recolher para revisão' : 'Validar e liberar aos alunos',
        child: InkWell(borderRadius: BorderRadius.circular(6), onTap: () => onToggle(m, !approved), child: Padding(padding: const EdgeInsets.all(4), child: mark)),
      );
    });
  }
}

class _Mark extends StatelessWidget {
  const _Mark({required this.on, this.color = AppColors.blue, this.disabled = false});
  final bool on;
  final Color color;
  final bool disabled;

  @override
  Widget build(BuildContext context) => Icon(
        on ? Icons.check_box : Icons.check_box_outline_blank,
        size: 22,
        color: disabled ? AppColors.lineSoft : (on ? color : AppColors.muted),
      );
}
