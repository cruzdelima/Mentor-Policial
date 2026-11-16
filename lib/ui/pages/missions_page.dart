import 'package:flutter/material.dart';

import '../../core/dates.dart';
import '../../core/models.dart';
import '../../core/planner.dart';
import '../../state/app_state.dart';
import '../dialogs.dart';
import '../theme.dart';
import '../widgets.dart';

enum _View { day, week, trail }

class MissionsPage extends StatefulWidget {
  const MissionsPage({super.key});

  @override
  State<MissionsPage> createState() => _MissionsPageState();
}

class _MissionsPageState extends State<MissionsPage> {
  DateTime? selected;
  _View view = _View.day;
  String trailFilter = '';
  bool showDone = false;

  @override
  Widget build(BuildContext context) {
    final app = AppScope.of(context);
    final s = app.schedule!;
    if (app.missionsFocus != null) {
      selected = app.missionsFocus;
      app.missionsFocus = null;
    }
    final day = selected ?? app.today;
    final p = app.profile;
    final overdue = s.overdue;
    return Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
      PageHeader(
        title: 'Missões',
        subtitle: '${app.career.code} · ${app.cargo.name} · ${fmtHours(p.hoursPerDay)} por dia · '
            '${p.contentWeekdays.length} dias de conteúdo + revisão · ${app.catalog.levels[p.level]}',
        actions: [
          _ViewToggle(value: view, onChanged: (v) => setState(() => view = v)),
          OutlinedButton.icon(
            onPressed: () async {
              final ok = await confirm(context, 'Replanejar a partir de hoje',
                  'As missões pendentes serão redistribuídas a partir de hoje, na ordem do ciclo. Nada do que você já concluiu é perdido.',
                  ok: 'REPLANEJAR');
              if (ok) app.replan();
            },
            icon: const Icon(Icons.autorenew, size: 18),
            label: const Text('REPLANEJAR'),
          ),
        ],
      ),
      if (overdue.isNotEmpty) OverdueBanner(count: overdue.length),
      Expanded(
        child: switch (view) {
          _View.day => _dayView(app, s, day),
          _View.week => _weekView(app, s, day),
          _View.trail => _trailView(app, s),
        },
      ),
    ]);
  }

  Widget _dayView(AppController app, Schedule s, DateTime day) {
    final plan = s.dayPlan(day);
    return ListView(padding: const EdgeInsets.fromLTRB(28, 4, 28, 32), children: [
      WeekStrip(selected: day, onSelect: (d) => setState(() => selected = d)),
      const SizedBox(height: 18),
      Align(
        alignment: Alignment.topLeft,
        child: ConstrainedBox(constraints: const BoxConstraints(maxWidth: 1040), child: DayDetail(plan: plan)),
      ),
    ]);
  }

  Widget _weekView(AppController app, Schedule s, DateTime day) {
    final monday = addDays(day, -(day.weekday - 1));
    return ListView(padding: const EdgeInsets.fromLTRB(28, 4, 28, 32), children: [
      Row(children: [
        IconButton(onPressed: () => setState(() => selected = addDays(day, -7)), icon: const Icon(Icons.chevron_left)),
        Text('SEMANA DE ${fmtDayMonth(monday)} A ${fmtDayMonth(addDays(monday, 6))}', style: AppText.h3()),
        IconButton(onPressed: () => setState(() => selected = addDays(day, 7)), icon: const Icon(Icons.chevron_right)),
        const Spacer(),
        TextButton(onPressed: () => setState(() => selected = app.today), child: const Text('HOJE')),
      ]),
      const SizedBox(height: 8),
      for (var i = 0; i < 7; i++) ...[
        _WeekDayRow(
          plan: s.dayPlan(addDays(monday, i)),
          onOpen: () => setState(() {
            selected = addDays(monday, i);
            view = _View.day;
          }),
        ),
        const SizedBox(height: 8),
      ],
    ]);
  }

  Widget _trailView(AppController app, Schedule s) {
    final q = trailFilter.trim().toLowerCase();
    final units = s.trail.units.where((u) {
      if (!showDone && app.isUnitDone(u)) return false;
      if (q.isEmpty) return true;
      return u.topic.name.toLowerCase().contains(q) || u.subject.name.toLowerCase().contains(q) || u.subject.id.toLowerCase() == q || '#${u.seq}' == q;
    }).toList();
    final done = s.doneCount;
    return Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
      Padding(
        padding: const EdgeInsets.fromLTRB(28, 4, 28, 12),
        child: Row(children: [
          SizedBox(
            width: 320,
            child: TextField(
              onChanged: (v) => setState(() => trailFilter = v),
              decoration: const InputDecoration(prefixIcon: Icon(Icons.search, size: 20), hintText: 'Buscar assunto, matéria ou #missão'),
            ),
          ),
          const SizedBox(width: 16),
          FilterChip(
            label: const Text('Mostrar concluídas'),
            selected: showDone,
            onSelected: (v) => setState(() => showDone = v),
            selectedColor: AppColors.panel2,
            checkmarkColor: AppColors.gold,
          ),
          const Spacer(),
          Text('$done de ${s.trail.units.length} missões concluídas · ${minutesLabel(s.remainingMinutes)} restantes', style: AppText.small()),
        ]),
      ),
      Expanded(
        child: units.isEmpty
            ? const EmptyState(icon: Icons.search_off, title: 'Nada encontrado', text: 'Ajuste a busca ou mostre as missões concluídas.')
            : ListView.builder(
                padding: const EdgeInsets.fromLTRB(28, 0, 28, 28),
                itemCount: units.length,
                itemExtent: 58,
                itemBuilder: (context, i) => _TrailRow(unit: units[i]),
              ),
      ),
    ]);
  }
}

class _ViewToggle extends StatelessWidget {
  const _ViewToggle({required this.value, required this.onChanged});
  final _View value;
  final ValueChanged<_View> onChanged;

  @override
  Widget build(BuildContext context) {
    Widget b(_View v, String label, IconData icon) => Padding(
          padding: const EdgeInsets.only(right: 4),
          child: ToggleChip(label: label, selected: value == v, onTap: () => onChanged(v), minWidth: 70),
        );
    return Row(mainAxisSize: MainAxisSize.min, children: [
      b(_View.day, 'DIA', Icons.today),
      b(_View.week, 'SEMANA', Icons.view_week),
      b(_View.trail, 'TRILHA', Icons.route),
    ]);
  }
}

class OverdueBanner extends StatelessWidget {
  const OverdueBanner({super.key, required this.count, this.showOpen = false});
  final int count;
  final bool showOpen;

  @override
  Widget build(BuildContext context) {
    final app = AppScope.read(context);
    return Container(
      margin: const EdgeInsets.fromLTRB(28, 0, 28, 14),
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
      decoration: BoxDecoration(
        color: AppColors.red.withValues(alpha: 0.10),
        borderRadius: BorderRadius.circular(10),
        border: Border.all(color: AppColors.red.withValues(alpha: 0.5)),
      ),
      child: Row(children: [
        const Icon(Icons.warning_amber_rounded, color: AppColors.red),
        const SizedBox(width: 12),
        Expanded(
          child: Text(
            count == 1 ? '1 missão atrasada. Faça hoje ou replaneje: as pendentes voltam para a fila a partir de hoje.'
                : '$count missões atrasadas. Faça hoje ou replaneje: as pendentes voltam para a fila a partir de hoje.',
            style: AppText.body(),
          ),
        ),
        if (showOpen) TextButton(onPressed: () => app.goTo(AppPage.missions), child: const Text('VER MISSÕES')),
        const SizedBox(width: 8),
        ElevatedButton.icon(
          style: ElevatedButton.styleFrom(backgroundColor: AppColors.red, foregroundColor: AppColors.bg),
          onPressed: app.replan,
          icon: const Icon(Icons.autorenew, size: 18),
          label: const Text('REPLANEJAR'),
        ),
      ]),
    );
  }
}

/// Faixa com os 7 dias da semana do dia selecionado.
class WeekStrip extends StatelessWidget {
  const WeekStrip({super.key, required this.selected, required this.onSelect});
  final DateTime selected;
  final ValueChanged<DateTime> onSelect;

  @override
  Widget build(BuildContext context) {
    final app = AppScope.of(context);
    final s = app.schedule!;
    final monday = addDays(selected, -(selected.weekday - 1));
    return Row(children: [
      IconButton(tooltip: 'Semana anterior', onPressed: () => onSelect(addDays(selected, -7)), icon: const Icon(Icons.chevron_left)),
      for (var i = 0; i < 7; i++)
        Expanded(
          child: Padding(
            padding: const EdgeInsets.symmetric(horizontal: 3),
            child: _DayChip(plan: s.dayPlan(addDays(monday, i)), selected: sameDay(addDays(monday, i), selected), onTap: () => onSelect(addDays(monday, i))),
          ),
        ),
      IconButton(tooltip: 'Próxima semana', onPressed: () => onSelect(addDays(selected, 7)), icon: const Icon(Icons.chevron_right)),
      const SizedBox(width: 4),
      OutlinedButton(onPressed: () => onSelect(app.today), child: const Text('HOJE')),
    ]);
  }
}

Color _kindColor(DayKind k) => switch (k) {
      DayKind.study => AppColors.blue,
      DayKind.review => AppColors.amber,
      DayKind.rest => AppColors.dim,
      DayKind.finished => AppColors.green,
      DayKind.beforeStart => AppColors.dim,
    };

class _DayChip extends StatelessWidget {
  const _DayChip({required this.plan, required this.selected, required this.onTap});
  final DayPlan plan;
  final bool selected;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    final app = AppScope.of(context);
    final (done, total) = app.schedule!.dayProgress(plan);
    final isToday = sameDay(plan.date, app.today);
    final past = plan.date.isBefore(app.today);
    final kc = _kindColor(plan.kind);
    Color stateColor = AppColors.dim;
    if (total > 0) {
      if (done == total) {
        stateColor = AppColors.green;
      } else if (done > 0) {
        stateColor = AppColors.amber;
      } else if (past) {
        stateColor = AppColors.red;
      }
    }
    return Material(
      color: selected ? AppColors.panel2 : AppColors.panel,
      borderRadius: BorderRadius.circular(10),
      child: InkWell(
        onTap: onTap,
        borderRadius: BorderRadius.circular(10),
        child: Container(
          padding: const EdgeInsets.symmetric(vertical: 10, horizontal: 6),
          decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(10),
            border: Border.all(color: selected ? AppColors.gold : (isToday ? AppColors.gold.withValues(alpha: 0.5) : AppColors.lineSoft), width: selected ? 1.6 : 1),
          ),
          child: Column(children: [
            Text(weekdayShort(plan.date), style: AppText.label(isToday ? AppColors.gold2 : AppColors.muted)),
            const SizedBox(height: 2),
            Text(fmtDayMonth(plan.date), style: AppText.h3(isToday ? AppColors.gold2 : AppColors.text)),
            const SizedBox(height: 6),
            Text(plan.kindLabel, style: AppText.label(kc).copyWith(fontSize: 10.5), maxLines: 1, overflow: TextOverflow.fade, softWrap: false),
            const SizedBox(height: 6),
            Container(
              height: 4,
              margin: const EdgeInsets.symmetric(horizontal: 8),
              decoration: BoxDecoration(color: total == 0 ? AppColors.lineSoft : stateColor, borderRadius: BorderRadius.circular(4)),
            ),
            const SizedBox(height: 4),
            Text(total == 0 ? ' ' : '$done/$total', style: AppText.small(AppColors.dim).copyWith(fontSize: 11)),
          ]),
        ),
      ),
    );
  }
}

/// Detalhe de um dia: missões da trilha + tarefas (revisão 24h, lei seca, revisão semanal...).
class DayDetail extends StatelessWidget {
  const DayDetail({super.key, required this.plan, this.compact = false});
  final DayPlan plan;
  final bool compact;

  @override
  Widget build(BuildContext context) {
    final app = AppScope.of(context);
    final s = app.schedule!;
    final (done, total) = s.dayProgress(plan);
    final isToday = sameDay(plan.date, app.today);
    final kc = _kindColor(plan.kind);
    final children = <Widget>[];

    if (!compact) {
      children.add(Row(crossAxisAlignment: CrossAxisAlignment.end, children: [
        Expanded(
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Text(isToday ? 'HOJE' : weekdayLong(plan.date).toUpperCase(), style: AppText.label(isToday ? AppColors.gold : AppColors.muted)),
            const SizedBox(height: 2),
            Text(fmtLong(plan.date).toUpperCase(), style: AppText.h2()),
          ]),
        ),
        if (plan.weekNo > 0) Pill('SEMANA ${plan.weekNo}', color: AppColors.muted),
        const SizedBox(width: 8),
        Pill(plan.kindLabel, color: kc, filled: true),
        if (total > 0) ...[const SizedBox(width: 8), Pill('$done/$total', color: done == total ? AppColors.green : AppColors.gold)],
      ]));
      children.add(const SizedBox(height: 14));
    }

    if (plan.kind == DayKind.beforeStart) {
      children.add(const EmptyState(icon: Icons.hourglass_empty, title: 'Antes do início', text: 'O ciclo começa na data definida em AJUSTES.'));
      return Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: children);
    }

    if (plan.history && plan.isStudy) {
      children.add(Padding(
        padding: const EdgeInsets.only(bottom: 10),
        child: Text('Dia anterior ao cronograma atual: abaixo, o que você concluiu nesta data.', style: AppText.small(AppColors.dim)),
      ));
      if (plan.units.isEmpty) children.add(Text('Nenhuma missão concluída neste dia.', style: AppText.small()));
    }

    for (final u in plan.units) {
      children.add(MissionCard(unit: u, compact: compact));
      children.add(const SizedBox(height: 10));
    }
    if (plan.continuation != null) {
      children.add(MissionCard(unit: plan.continuation!, continuation: true, compact: compact));
      children.add(const SizedBox(height: 10));
    }
    if (plan.isStudy && !plan.history && plan.units.isEmpty && plan.continuation == null) {
      children.add(Text('Sem missão nova neste dia.', style: AppText.small()));
    }

    if (plan.tasks.isNotEmpty) {
      if (plan.isStudy || plan.kind == DayKind.finished) children.add(const SizedBox(height: 6));
      for (final t in plan.tasks) {
        children.add(TaskTile(task: t, compact: compact));
        children.add(const SizedBox(height: 8));
      }
    }
    return Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: children);
  }
}

class MissionCard extends StatelessWidget {
  const MissionCard({super.key, required this.unit, this.continuation = false, this.compact = false});
  final Unit unit;
  final bool continuation;
  final bool compact;

  @override
  Widget build(BuildContext context) {
    final app = AppScope.of(context);
    final u = unit;
    final done = app.isUnitDone(u);
    final col = AppColors.hex(u.subject.colorHex);
    final materials = app.content.forTopic(u.topic.id);
    final pd = app.schedule!.plannedDate(u);
    final late = !done && pd != null && pd.isBefore(app.today);
    return Container(
      decoration: BoxDecoration(
        color: done ? AppColors.panel.withValues(alpha: 0.6) : AppColors.panel,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: late ? AppColors.red.withValues(alpha: 0.6) : AppColors.lineSoft),
      ),
      clipBehavior: Clip.antiAlias,
      child: IntrinsicHeight(
        child: Row(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
          Container(width: 5, color: done ? AppColors.green : col),
          Expanded(
            child: Padding(
              padding: EdgeInsets.symmetric(horizontal: 16, vertical: compact ? 10 : 14),
              child: Row(children: [
                Column(crossAxisAlignment: CrossAxisAlignment.start, mainAxisSize: MainAxisSize.min, children: [
                  Text('#${u.seq}', style: AppText.h2(done ? AppColors.dim : AppColors.gold).copyWith(fontSize: compact ? 18 : 22)),
                  Icon(u.isTheory ? Icons.menu_book_outlined : Icons.fact_check_outlined, size: 16, color: AppColors.dim),
                ]),
                const SizedBox(width: 16),
                Expanded(
                  child: Column(crossAxisAlignment: CrossAxisAlignment.start, mainAxisSize: MainAxisSize.min, children: [
                    Wrap(spacing: 6, runSpacing: 4, crossAxisAlignment: WrapCrossAlignment.center, children: [
                      SubjectTag(u.subject),
                      Text(u.isTheory ? 'TEORIA + RESUMO' : '${u.questions} QUESTÕES', style: AppText.label(done ? AppColors.dim : AppColors.text)),
                      Text('· ${minutesLabel(u.minutes)}', style: AppText.small(AppColors.dim)),
                      if (continuation) const Pill('CONTINUAÇÃO', color: AppColors.amber),
                      if (late) const Pill('ATRASADA', color: AppColors.red),
                    ]),
                    const SizedBox(height: 4),
                    Text(
                      u.topic.name,
                      style: AppText.strong(done ? AppColors.muted : AppColors.text).copyWith(
                        fontSize: compact ? 14 : 15.5,
                        decoration: done ? TextDecoration.lineThrough : null,
                        decorationColor: AppColors.dim,
                      ),
                    ),
                    if (!compact) Text(u.subject.name, style: AppText.small(AppColors.dim)),
                  ]),
                ),
                if (materials.isNotEmpty && !compact)
                  Padding(
                    padding: const EdgeInsets.only(right: 8),
                    child: OutlinedButton.icon(
                      onPressed: () => app.goTo(AppPage.materials, materialId: materials.first.id),
                      icon: const Icon(Icons.auto_stories_outlined, size: 17, color: AppColors.teal),
                      label: Text(u.isTheory ? 'ESTUDAR NO APP' : 'QUESTÕES NO APP'),
                    ),
                  ),
                _DoneButton(
                  done: done,
                  onTap: () {
                    if (done) {
                      app.undoUnit(u);
                    } else {
                      showUnitDoneDialog(context, u);
                    }
                  },
                ),
              ]),
            ),
          ),
        ]),
      ),
    );
  }
}

class _DoneButton extends StatelessWidget {
  const _DoneButton({required this.done, required this.onTap, this.small = false});
  final bool done;
  final VoidCallback onTap;
  final bool small;

  @override
  Widget build(BuildContext context) {
    final size = small ? 30.0 : 38.0;
    return Tooltip(
      message: done ? 'Desmarcar (remove o lançamento do diário)' : 'Concluir e lançar no diário',
      child: Material(
        color: done ? AppColors.green : Colors.transparent,
        shape: CircleBorder(side: BorderSide(color: done ? AppColors.green : AppColors.muted, width: 1.6)),
        child: InkWell(
          customBorder: const CircleBorder(),
          onTap: onTap,
          child: SizedBox(width: size, height: size, child: Icon(Icons.check, size: small ? 17 : 21, color: done ? AppColors.bg : AppColors.muted)),
        ),
      ),
    );
  }
}

class TaskTile extends StatelessWidget {
  const TaskTile({super.key, required this.task, this.compact = false});
  final DayTask task;
  final bool compact;

  static (IconData, Color) look(String code) => switch (code) {
        'REV24' => (Icons.history, AppColors.amber),
        'LEI' => (Icons.gavel, AppColors.teal),
        'REV_SEM' || 'GERAL' => (Icons.autorenew, AppColors.amber),
        'SIM' => (Icons.timer_outlined, AppColors.red),
        'QREV' || 'POS' => (Icons.fact_check_outlined, AppColors.blue),
        'ERROS' => (Icons.report_outlined, AppColors.red),
        'REV30' => (Icons.event_repeat, AppColors.amber),
        'DISC' => (Icons.edit_document, AppColors.gold),
        'PLAN' => (Icons.map_outlined, AppColors.muted),
        _ => (Icons.self_improvement, AppColors.dim),
      };

  @override
  Widget build(BuildContext context) {
    final app = AppScope.of(context);
    final t = task;
    final rest = t.code == 'REST';
    final done = app.isTaskDone(t.key);
    final (icon, color) = look(t.code);
    final review = const {'REV24', 'REV_SEM', 'REV30'}.contains(t.code) ? app.content.reviewFor(t.topicIds) : null;
    return Container(
      padding: EdgeInsets.symmetric(horizontal: 14, vertical: compact ? 8 : 11),
      decoration: BoxDecoration(
        color: rest ? Colors.transparent : AppColors.panel,
        borderRadius: BorderRadius.circular(10),
        border: Border.all(color: AppColors.lineSoft),
      ),
      child: Row(children: [
        Container(
          width: 32,
          height: 32,
          decoration: BoxDecoration(color: color.withValues(alpha: 0.13), borderRadius: BorderRadius.circular(8)),
          child: Icon(icon, size: 18, color: color),
        ),
        const SizedBox(width: 14),
        Expanded(
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, mainAxisSize: MainAxisSize.min, children: [
            Text(t.title.toUpperCase(), style: AppText.label(done ? AppColors.dim : AppColors.text).copyWith(fontSize: 13)),
            const SizedBox(height: 2),
            Text(t.detail, style: AppText.small(done ? AppColors.dim : AppColors.muted), maxLines: compact ? 1 : 3, overflow: TextOverflow.ellipsis),
          ]),
        ),
        if (review != null && !compact)
          Padding(
            padding: const EdgeInsets.only(left: 10),
            child: OutlinedButton.icon(
              onPressed: () => app.goTo(AppPage.materials, materialId: review.id),
              icon: const Icon(Icons.bolt, size: 17, color: AppColors.amber),
              label: const Text('RESUMO NO APP'),
            ),
          ),
        if (!rest) ...[
          const SizedBox(width: 10),
          _DoneButton(
            small: true,
            done: done,
            onTap: () {
              if (done) {
                app.undoTask(t.key);
              } else if (t.askQuestions || t.code == 'DISC') {
                showTaskDoneDialog(context, t);
              } else {
                app.completeTask(t);
              }
            },
          ),
        ],
      ]),
    );
  }
}

class _WeekDayRow extends StatelessWidget {
  const _WeekDayRow({required this.plan, required this.onOpen});
  final DayPlan plan;
  final VoidCallback onOpen;

  @override
  Widget build(BuildContext context) {
    final app = AppScope.of(context);
    final isToday = sameDay(plan.date, app.today);
    final (done, total) = app.schedule!.dayProgress(plan);
    final kc = _kindColor(plan.kind);
    final items = <String>[
      for (final u in plan.units) '#${u.seq} ${u.subject.id} · ${u.isTheory ? 'Teoria' : '${u.questions} questões'} · ${u.topic.name}',
      if (plan.continuation != null) '#${plan.continuation!.seq} (continuação) · ${plan.continuation!.topic.name}',
      for (final t in plan.tasks)
        if (t.code != 'REV24' && t.code != 'LEI') t.title,
    ];
    return Material(
      color: AppColors.panel,
      borderRadius: BorderRadius.circular(10),
      child: InkWell(
        onTap: onOpen,
        borderRadius: BorderRadius.circular(10),
        child: Container(
          padding: const EdgeInsets.all(14),
          decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(10),
            border: Border.all(color: isToday ? AppColors.gold : AppColors.lineSoft),
          ),
          child: Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
            SizedBox(
              width: 110,
              child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                Text(weekdayShort(plan.date), style: AppText.label(isToday ? AppColors.gold2 : AppColors.muted)),
                Text(fmtDayMonth(plan.date), style: AppText.h2(isToday ? AppColors.gold2 : AppColors.text)),
                const SizedBox(height: 4),
                Pill(plan.kindLabel, color: kc),
              ]),
            ),
            Expanded(
              child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                if (items.isEmpty) Text(plan.isRest ? 'Descanso e recuperação.' : '—', style: AppText.small()),
                for (final it in items)
                  Padding(padding: const EdgeInsets.only(bottom: 3), child: Text(it, style: AppText.body(), maxLines: 1, overflow: TextOverflow.ellipsis)),
              ]),
            ),
            if (total > 0) Pill('$done/$total', color: done == total ? AppColors.green : AppColors.muted),
          ]),
        ),
      ),
    );
  }
}

class _TrailRow extends StatelessWidget {
  const _TrailRow({required this.unit});
  final Unit unit;

  @override
  Widget build(BuildContext context) {
    final app = AppScope.of(context);
    final u = unit;
    final done = app.data.unitDone[u.id];
    final pd = app.schedule!.plannedDate(u);
    final late = done == null && pd != null && pd.isBefore(app.today);
    final status = done != null
        ? Pill('FEITA ${fmtDayMonth(done.date)}', color: AppColors.green, icon: Icons.check)
        : late
            ? const Pill('ATRASADA', color: AppColors.red)
            : Pill(pd == null ? '—' : '${weekdayShort(pd)} ${fmtDayMonth(pd)}', color: AppColors.muted);
    return Container(
      margin: const EdgeInsets.only(bottom: 6),
      padding: const EdgeInsets.symmetric(horizontal: 14),
      decoration: BoxDecoration(color: AppColors.panel, borderRadius: BorderRadius.circular(8), border: Border.all(color: AppColors.lineSoft)),
      child: Row(children: [
        SizedBox(width: 56, child: Text('#${u.seq}', style: AppText.h3(done != null ? AppColors.dim : AppColors.gold))),
        SizedBox(width: 64, child: Align(alignment: Alignment.centerLeft, child: SubjectTag(u.subject))),
        SizedBox(width: 120, child: Text(u.isTheory ? 'TEORIA' : '${u.questions} QUESTÕES', style: AppText.label(AppColors.text))),
        Expanded(child: Text(u.topic.name, style: AppText.body(done != null ? AppColors.muted : AppColors.text), maxLines: 1, overflow: TextOverflow.ellipsis)),
        SizedBox(width: 70, child: Text(minutesLabel(u.minutes), style: AppText.small())),
        SizedBox(width: 130, child: Align(alignment: Alignment.centerLeft, child: status)),
        IconButton(
          tooltip: done != null ? 'Desmarcar' : 'Concluir',
          onPressed: () => done != null ? app.undoUnit(u) : showUnitDoneDialog(context, u),
          icon: Icon(done != null ? Icons.check_circle : Icons.radio_button_unchecked, color: done != null ? AppColors.green : AppColors.muted),
        ),
      ]),
    );
  }
}
