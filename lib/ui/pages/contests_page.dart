import 'package:flutter/material.dart';

import '../../core/catalog.dart';
import '../../core/dates.dart';
import '../../core/extras.dart';
import '../../data/storage.dart';
import '../../state/account.dart';
import '../../state/app_state.dart';
import '../dialogs.dart';
import '../theme.dart';
import '../widgets.dart';

/// Pós-edital: concursos com edital publicado. Escolher um faz o plano seguir o edital.
class ContestsPage extends StatelessWidget {
  const ContestsPage({super.key});

  @override
  Widget build(BuildContext context) {
    final app = AppScope.of(context);
    final cat = app.catalog;
    final mine = app.cargo.isContest ? app.cargo : null;
    final others = cat.contests.where((c) => c.id != mine?.id).toList();
    final isAdmin = AccountScope.maybeOf(context)?.isAdmin ?? false;
    return Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
      PageHeader(
        title: 'Pós-edital',
        subtitle: 'Concursos com edital publicado. Ao escolher um, o plano passa a seguir o conteúdo e a ordem do edital, '
            'com a data da prova. O que você já estudou continua valendo.',
        actions: [
          if (isAdmin)
            OutlinedButton.icon(
              onPressed: () => app.goTo(AppPage.admin),
              icon: const Icon(Icons.edit_outlined, size: 18),
              label: const Text('CADASTRAR CONCURSO'),
            ),
        ],
      ),
      Expanded(
        child: ListView(padding: const EdgeInsets.fromLTRB(28, 0, 28, 40), children: [
          if (mine != null) ...[
            _ContestPanel(cargo: mine, current: true),
            const SizedBox(height: 22),
          ],
          if (others.isNotEmpty) ...[
            SectionLabel(mine == null ? 'Concursos disponíveis' : 'Outros concursos'),
            for (final c in others) Padding(padding: const EdgeInsets.only(bottom: 14), child: _ContestPanel(cargo: c, current: false)),
          ],
          if (mine == null && others.isEmpty)
            const EmptyState(
              icon: Icons.campaign_outlined,
              title: 'Nenhum edital cadastrado',
              text: 'Quando um edital for publicado e cadastrado, ele aparece aqui.',
            ),
          const SizedBox(height: 8),
          Text(
            'Datas, vagas e conteúdo vêm do edital oficial e podem mudar por retificação. Confira sempre a página da banca.',
            style: AppText.small(AppColors.dim),
          ),
        ]),
      ),
    ]);
  }
}

class _ContestPanel extends StatelessWidget {
  const _ContestPanel({required this.cargo, required this.current});
  final Cargo cargo;
  final bool current;

  @override
  Widget build(BuildContext context) {
    final app = AppScope.of(context);
    final cat = app.catalog;
    final c = cargo.contest!;
    final career = cat.careerOfOption(cargo.id)!;
    final st = app.stats!;
    final subs = cat.subjects.where((s) => s.weightFor(cargo.id) > 0).toList()
      ..sort((a, b) {
        final w = b.weightFor(cargo.id).compareTo(a.weightFor(cargo.id));
        return w != 0 ? w : (c.questions[b.id] ?? 0).compareTo(c.questions[a.id] ?? 0);
      });
    final done = c.topicIds.where((id) => st.topic[id]?.theory ?? false).length;
    final days = c.examDate == null ? null : daysBetween(app.today, c.examDate!);
    return Panel(
      accent: current ? AppColors.gold : null,
      borderColor: current ? AppColors.gold : null,
      child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
        Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Expanded(
            child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              if (current) Text('SEU CONCURSO', style: AppText.label(AppColors.gold)),
              Text(cargo.name.toUpperCase(), style: AppText.h2()),
              const SizedBox(height: 2),
              Text([career.name, if (c.orgao.isNotEmpty) c.orgao].join(' · '), style: AppText.small()),
              const SizedBox(height: 10),
              Wrap(spacing: 6, runSpacing: 6, children: [
                Pill(career.esfera.toUpperCase(), color: AppColors.esfera(career.esfera), filled: true),
                if (kContestStatus[c.status] != null) Pill(kContestStatus[c.status]!, color: AppColors.blue),
                if (c.banca.isNotEmpty) Pill(c.banca, color: AppColors.muted),
                if (c.examDate != null) Pill('PROVA ${fmtDate(c.examDate!)}', color: AppColors.amber),
                if (days != null && days >= 0) Pill('FALTAM $days DIAS', color: AppColors.gold),
                if (c.vagas.isNotEmpty) Pill('${c.vagas} VAGAS', color: AppColors.teal),
                if (c.totalQuestions > 0) Pill('${c.totalQuestions} QUESTÕES', color: AppColors.muted),
              ]),
            ]),
          ),
          const SizedBox(width: 16),
          Column(crossAxisAlignment: CrossAxisAlignment.end, children: [
            if (current)
              OutlinedButton.icon(
                onPressed: () => _leave(context),
                icon: const Icon(Icons.undo, size: 18),
                label: const Text('VOLTAR AO CICLO BÁSICO'),
              )
            else
              ElevatedButton.icon(
                onPressed: () => _choose(context),
                icon: const Icon(Icons.flag_outlined, size: 18),
                label: const Text('ESTUDAR PARA ESTE CONCURSO'),
              ),
            if (c.editalUrl.isNotEmpty) ...[
              const SizedBox(height: 8),
              TextButton.icon(
                onPressed: () => openExternal(c.editalUrl),
                icon: const Icon(Icons.open_in_new, size: 16),
                label: const Text('PÁGINA DO EDITAL'),
              ),
            ],
          ]),
        ]),
        if (c.notes.isNotEmpty) ...[
          const SizedBox(height: 12),
          Text(c.notes, style: AppText.body(AppColors.muted)),
        ],
        const SizedBox(height: 14),
        Text('${c.topicIds.length} assuntos no edital · $done já estudados (teoria)', style: AppText.small(AppColors.gold2)),
        const SizedBox(height: 10),
        Wrap(spacing: 10, runSpacing: 10, children: [
          for (final s in subs)
            Container(
              width: 250,
              padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 9),
              decoration: BoxDecoration(color: AppColors.panel2, borderRadius: BorderRadius.circular(8)),
              child: Row(children: [
                Container(width: 8, height: 8, decoration: BoxDecoration(color: AppColors.hex(s.colorHex), shape: BoxShape.circle)),
                const SizedBox(width: 8),
                Expanded(child: Text(s.name, style: AppText.small(AppColors.text), overflow: TextOverflow.ellipsis)),
                if ((c.questions[s.id] ?? 0) > 0) Text('${c.questions[s.id]}q  ', style: AppText.small(AppColors.dim)),
                Dots(s.weightFor(cargo.id), color: AppColors.hex(s.colorHex)),
              ]),
            ),
        ]),
      ]),
    );
  }

  Future<void> _choose(BuildContext context) async {
    final app = AppScope.read(context);
    final ok = await confirm(
      context,
      'ESTUDAR PARA ${cargo.name.toUpperCase()}',
      'Seu cronograma será recalculado a partir de hoje seguindo o edital deste concurso'
          '${cargo.contest!.examDate == null ? '' : ', com prova em ${fmtDate(cargo.contest!.examDate!)}'}. '
          'Diário, questões e assuntos já estudados continuam valendo.',
      ok: 'USAR ESTE EDITAL',
    );
    if (!ok || !context.mounted) return;
    app.studyFor(cargo.id);
    toast(context, 'Plano ajustado ao edital. Bons estudos!');
  }

  Future<void> _leave(BuildContext context) async {
    final app = AppScope.read(context);
    final cat = app.catalog;
    final base = cat.hasOption(cargo.contest!.base) ? cargo.contest!.base : cat.careerOfOption(cargo.id)!.cycleCargos.firstOrNull?.id;
    if (base == null) return;
    final ok = await confirm(
      context,
      'VOLTAR AO CICLO BÁSICO',
      'O plano volta para "${cat.cargo(base).name}" (núcleo comum dos editais), recalculado a partir de hoje. Nada do que você já estudou se perde.',
      ok: 'VOLTAR',
    );
    if (!ok || !context.mounted) return;
    app.studyFor(base);
    toast(context, 'Plano de volta ao ciclo básico.');
  }
}
