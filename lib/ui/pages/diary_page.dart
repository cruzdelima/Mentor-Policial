import 'package:flutter/material.dart';

import '../../core/dates.dart';
import '../../core/models.dart';
import '../../state/app_state.dart';
import '../charts.dart';
import '../dialogs.dart';
import '../theme.dart';
import '../widgets.dart';

class DiaryPage extends StatefulWidget {
  const DiaryPage({super.key});

  @override
  State<DiaryPage> createState() => _DiaryPageState();
}

class _DiaryPageState extends State<DiaryPage> {
  String? type;
  String? subjectId;
  int limitDays = 30;

  Color _typeColor(String t) => switch (t) {
        'Teoria' => AppColors.blue,
        'Questões' => AppColors.gold,
        'Revisão' => AppColors.amber,
        'Simulado' => AppColors.red,
        'Lei seca' => AppColors.teal,
        'Discursiva' => AppColors.green,
        _ => AppColors.muted,
      };

  @override
  Widget build(BuildContext context) {
    final app = AppScope.of(context);
    final st = app.stats!;
    final entries = app.data.diary.where((e) => (type == null || e.type == type) && (subjectId == null || e.subjectId == subjectId)).toList()
      ..sort((a, b) {
        final c = b.date.compareTo(a.date);
        return c != 0 ? c : b.id.compareTo(a.id);
      });
    final byDay = <String, List<DiaryEntry>>{};
    for (final e in entries) {
      (byDay[isoDate(e.date)] ??= []).add(e);
    }
    final days = byDay.keys.toList();
    final shown = days.take(limitDays).toList();
    final usedSubjects = {for (final e in app.data.diary) e.subjectId, subjectId}.whereType<String>().toList()..sort();
    final weekly = st.weekly(16);

    return Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
      PageHeader(
        title: 'Diário de estudos',
        subtitle: 'Missões concluídas entram aqui sozinhas. Lance também o que estudar fora do cronograma.',
        actions: [
          ElevatedButton.icon(onPressed: () => showEntryDialog(context), icon: const Icon(Icons.add, size: 18), label: const Text('NOVO LANÇAMENTO')),
        ],
      ),
      Expanded(
        child: ListView(padding: const EdgeInsets.fromLTRB(28, 0, 28, 32), children: [
          LayoutBuilder(builder: (context, c) {
            final w = (c.maxWidth - 12 * 4) / 5;
            return Wrap(spacing: 12, runSpacing: 12, children: [
              SizedBox(width: w, child: KpiTile(label: 'Questões', value: thousands(st.questions), sub: '${thousands(st.correct)} acertos')),
              SizedBox(
                width: w,
                child: KpiTile(
                  label: 'Acerto',
                  value: pct(st.accuracy),
                  sub: 'meta: 80%+',
                  color: st.accuracy == null ? AppColors.text : (st.accuracy! >= 0.8 ? AppColors.green : (st.accuracy! < 0.7 ? AppColors.red : AppColors.gold2)),
                ),
              ),
              SizedBox(width: w, child: KpiTile(label: 'Nota líquida', value: pct(st.net), sub: 'certas − erradas', color: AppColors.gold2)),
              SizedBox(width: w, child: KpiTile(label: 'Horas', value: st.hours.toStringAsFixed(st.hours < 10 ? 1 : 0), sub: 'tempo lançado')),
              SizedBox(width: w, child: KpiTile(label: 'Lançamentos', value: '${app.data.diary.length}', sub: '${st.studyDays} dias com estudo')),
            ]);
          }),
          const SizedBox(height: 16),
          if (weekly.any((w) => w.questions > 0))
            Panel(
              child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
                const SectionLabel('Evolução semanal · barras = questões · linha = % de acerto'),
                BarLineChart(points: [for (final p in weekly) ChartPoint(fmtDayMonth(p.start), p.questions.toDouble(), rate: p.accuracy)], height: 190),
              ]),
            ),
          const SizedBox(height: 16),
          Wrap(spacing: 8, runSpacing: 8, crossAxisAlignment: WrapCrossAlignment.center, children: [
            ToggleChip(label: 'TUDO', selected: type == null, onTap: () => setState(() => type = null)),
            for (final t in kDiaryTypes)
              ToggleChip(label: t.toUpperCase(), selected: type == t, color: _typeColor(t), onTap: () => setState(() => type = type == t ? null : t)),
            const SizedBox(width: 12),
            SizedBox(
              width: 260,
              child: DropdownButtonFormField<String?>(
                initialValue: subjectId,
                isExpanded: true,
                dropdownColor: AppColors.panel2,
                decoration: const InputDecoration(prefixIcon: Icon(Icons.filter_list, size: 18)),
                items: [
                  const DropdownMenuItem<String?>(value: null, child: Text('Todas as matérias')),
                  for (final id in usedSubjects) DropdownMenuItem<String?>(value: id, child: Text(app.catalog.subjectOrNull(id)?.name ?? id)),
                ],
                onChanged: (v) => setState(() => subjectId = v),
              ),
            ),
          ]),
          const SizedBox(height: 14),
          if (entries.isEmpty)
            Panel(
              child: EmptyState(
                icon: Icons.edit_note,
                title: 'Diário vazio',
                text: 'Conclua uma missão em MISSÕES ou faça um lançamento manual. Questões, acertos e tempo alimentam o QG e o EDITAL.',
                action: ElevatedButton.icon(onPressed: () => showEntryDialog(context), icon: const Icon(Icons.add, size: 18), label: const Text('NOVO LANÇAMENTO')),
              ),
            ),
          for (final d in shown) _DayGroup(date: parseIso(d), entries: byDay[d]!, typeColor: _typeColor),
          if (days.length > shown.length)
            Center(
              child: TextButton(
                onPressed: () => setState(() => limitDays += 30),
                child: Text('MOSTRAR MAIS (${days.length - shown.length} DIAS)'),
              ),
            ),
        ]),
      ),
    ]);
  }
}

class _DayGroup extends StatelessWidget {
  const _DayGroup({required this.date, required this.entries, required this.typeColor});
  final DateTime date;
  final List<DiaryEntry> entries;
  final Color Function(String) typeColor;

  @override
  Widget build(BuildContext context) {
    final app = AppScope.of(context);
    final q = entries.fold<int>(0, (a, e) => a + e.questions);
    final c = entries.fold<int>(0, (a, e) => a + e.correct);
    final m = entries.fold<int>(0, (a, e) => a + e.minutes);
    final isToday = sameDay(date, app.today);
    return Padding(
      padding: const EdgeInsets.only(bottom: 14),
      child: Panel(
        padding: EdgeInsets.zero,
        child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
            color: AppColors.panel2,
            child: Row(children: [
              Text(isToday ? 'HOJE · ${fmtDate(date)}' : '${weekdayShort(date)} · ${fmtDate(date)}', style: AppText.h3(isToday ? AppColors.gold2 : AppColors.text)),
              const Spacer(),
              if (q > 0) Text('$q questões · ${pct(c / q)}   ', style: AppText.small(AppColors.text)),
              Text(minutesLabel(m), style: AppText.small()),
            ]),
          ),
          for (final e in entries) _EntryRow(entry: e, color: typeColor(e.type)),
        ]),
      ),
    );
  }
}

class _EntryRow extends StatelessWidget {
  const _EntryRow({required this.entry, required this.color});
  final DiaryEntry entry;
  final Color color;

  @override
  Widget build(BuildContext context) {
    final app = AppScope.of(context);
    final e = entry;
    final sub = e.subjectId == null ? null : app.catalog.subjectOrNull(e.subjectId!);
    final topicNames = [for (final id in e.topicIds) app.catalog.topic(id)?.name ?? id];
    final title = topicNames.isEmpty ? (e.notes.isNotEmpty ? e.notes : e.type) : (topicNames.length <= 2 ? topicNames.join(' · ') : '${topicNames.take(2).join(' · ')} +${topicNames.length - 2}');
    final acc = e.accuracy;
    final auto = e.origin.isNotEmpty;
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
      decoration: const BoxDecoration(border: Border(top: BorderSide(color: AppColors.lineSoft))),
      child: Row(children: [
        SizedBox(width: 96, child: Align(alignment: Alignment.centerLeft, child: Pill(e.type.toUpperCase(), color: color))),
        SizedBox(width: 64, child: Align(alignment: Alignment.centerLeft, child: sub == null ? Text('GERAL', style: AppText.label(AppColors.dim)) : SubjectTag(sub))),
        Expanded(
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, mainAxisSize: MainAxisSize.min, children: [
            Text(title, style: AppText.body(), maxLines: 1, overflow: TextOverflow.ellipsis),
            if (e.notes.isNotEmpty && topicNames.isNotEmpty) Text(e.notes, style: AppText.small(), maxLines: 1, overflow: TextOverflow.ellipsis),
          ]),
        ),
        SizedBox(
          width: 150,
          child: e.questions == 0
              ? const SizedBox()
              : Text.rich(
                  TextSpan(children: [
                    TextSpan(text: '${e.correct}/${e.questions}  ', style: AppText.strong()),
                    TextSpan(
                      text: pct(acc),
                      style: AppText.strong(acc! >= 0.8 ? AppColors.green : (acc < 0.7 ? AppColors.red : AppColors.gold2)),
                    ),
                    TextSpan(text: '  líq. ${e.correct - e.wrong}', style: AppText.small()),
                  ]),
                ),
        ),
        SizedBox(width: 70, child: Text(e.minutes == 0 ? '' : minutesLabel(e.minutes), style: AppText.small(), textAlign: TextAlign.right)),
        const SizedBox(width: 8),
        SizedBox(
          width: 120,
          child: Text(e.source, style: AppText.small(AppColors.dim), maxLines: 1, overflow: TextOverflow.ellipsis),
        ),
        if (auto) const Tooltip(message: 'Lançado automaticamente por uma missão, tarefa ou questionário', child: Icon(Icons.bolt, size: 16, color: AppColors.dim)),
        IconButton(tooltip: 'Editar', onPressed: () => showEntryDialog(context, entry: e), icon: const Icon(Icons.edit_outlined, size: 18, color: AppColors.muted)),
        IconButton(
          tooltip: 'Apagar',
          onPressed: () async {
            final ok = await confirm(
              context,
              'Apagar lançamento',
              auto ? 'Este lançamento veio de uma missão ou tarefa concluída. Ao apagar, ela volta a ficar pendente.' : 'O lançamento será removido do diário.',
              ok: 'APAGAR',
              danger: true,
            );
            if (ok) app.deleteEntry(e);
          },
          icon: const Icon(Icons.delete_outline, size: 18, color: AppColors.muted),
        ),
      ]),
    );
  }
}
