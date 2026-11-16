import 'package:flutter/material.dart';

import '../../core/dates.dart';
import '../../core/models.dart';
import '../../core/stats.dart';
import '../../state/app_state.dart';
import '../charts.dart';
import '../theme.dart';
import '../widgets.dart';
import 'missions_page.dart';

class QgPage extends StatelessWidget {
  const QgPage({super.key});

  String _greeting(DateTime now) {
    final h = now.hour;
    if (h < 12) return 'Bom dia';
    if (h < 18) return 'Boa tarde';
    return 'Boa noite';
  }

  @override
  Widget build(BuildContext context) {
    final app = AppScope.of(context);
    final p = app.profile;
    final s = app.schedule!;
    final st = app.stats!;
    final today = app.today;
    final plan = s.dayPlan(today);
    final week = s.weekNo(today);
    final overdue = s.overdue.length;
    final exam = p.examDate;
    final left = exam == null ? null : daysBetween(today, exam);
    final constancy = st.constancy(p);
    final streak = st.streak(p);
    final totalUnits = s.trail.units.length;
    final doneUnits = s.doneCount;

    return ListView(
      padding: const EdgeInsets.only(bottom: 36),
      children: [
        // ------------------------------------------------ cabeçalho
        Container(
          margin: const EdgeInsets.fromLTRB(28, 22, 28, 18),
          padding: const EdgeInsets.fromLTRB(24, 20, 24, 20),
          decoration: BoxDecoration(
            gradient: const LinearGradient(colors: [AppColors.panel2, AppColors.panel], begin: Alignment.topLeft, end: Alignment.bottomRight),
            borderRadius: BorderRadius.circular(14),
            border: Border.all(color: AppColors.lineSoft),
          ),
          child: Row(children: [
            Expanded(
              child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                Text('QG · CENTRAL DE COMANDO', style: AppText.label(AppColors.gold)),
                const SizedBox(height: 6),
                Text('${_greeting(app.clock())}, ${p.name.isEmpty ? 'aluno' : p.name}'.toUpperCase(), style: AppText.h1().copyWith(fontSize: 32)),
                const SizedBox(height: 6),
                Text(
                  [
                    app.cargo.name,
                    if (p.targetName.isNotEmpty) p.targetName,
                    week > 0 ? 'semana $week do ciclo' : 'ciclo começa em ${fmtDate(p.startDate)}',
                    fmtLong(today),
                  ].join('  ·  '),
                  style: AppText.small(),
                ),
              ]),
            ),
            if (left != null && left >= 0)
              _Countdown(days: left, date: exam!)
            else
              OutlinedButton.icon(
                onPressed: () => app.goTo(AppPage.settings),
                icon: const Icon(Icons.event, size: 18),
                label: const Text('DEFINIR DATA DA PROVA'),
              ),
          ]),
        ),
        if (overdue > 0) OverdueBanner(count: overdue, showOpen: true),

        // ------------------------------------------------ KPIs
        Padding(
          padding: const EdgeInsets.symmetric(horizontal: 28),
          child: LayoutBuilder(builder: (context, c) {
            final tiles = [
              KpiTile(label: 'Dias estudados', value: '${st.studyDays}', sub: streak > 0 ? 'sequência atual: $streak' : 'comece hoje', icon: Icons.calendar_month_outlined),
              KpiTile(label: 'Questões', value: thousands(st.questions), sub: '${thousands(st.correct)} acertos', icon: Icons.fact_check_outlined),
              KpiTile(
                label: 'Acerto',
                value: pct(st.accuracy),
                sub: 'meta: 80% ou mais',
                color: st.accuracy == null ? AppColors.text : (st.accuracy! >= 0.8 ? AppColors.green : (st.accuracy! < 0.7 ? AppColors.red : AppColors.gold2)),
                icon: Icons.track_changes,
              ),
              KpiTile(label: 'Nota líquida', value: pct(st.net), sub: 'certas − erradas', color: AppColors.gold2, icon: Icons.balance),
              KpiTile(label: 'Constância', value: pct(constancy), sub: 'dias com estudo / previstos', icon: Icons.local_fire_department_outlined),
              KpiTile(label: 'Edital · teoria', value: pct(st.theoryShare), sub: '${st.theoryDone} de ${st.activeTopics} assuntos', icon: Icons.checklist_rtl),
            ];
            final perRow = c.maxWidth > 1250 ? 6 : 3;
            final w = (c.maxWidth - 12 * (perRow - 1)) / perRow;
            return Wrap(spacing: 12, runSpacing: 12, children: [for (final t in tiles) SizedBox(width: w, child: t)]);
          }),
        ),
        const SizedBox(height: 18),

        // ------------------------------------------------ hoje + projeção
        Padding(
          padding: const EdgeInsets.symmetric(horizontal: 28),
          child: Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Expanded(
              flex: 7,
              child: Panel(
                accent: AppColors.gold,
                child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
                  SectionLabel(
                    'Missões de hoje · ${weekdayShort(today)} ${fmtDayMonth(today)}',
                    trailing: TextButton.icon(
                      onPressed: () => app.goTo(AppPage.missions, day: today),
                      icon: const Icon(Icons.open_in_new, size: 16),
                      label: const Text('CRONOGRAMA'),
                    ),
                  ),
                  DayDetail(plan: plan, compact: true),
                ]),
              ),
            ),
            const SizedBox(width: 16),
            Expanded(
              flex: 5,
              child: Panel(
                child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
                  const SectionLabel('Projeção · 1ª volta'),
                  Row(children: [
                    ProgressRing(
                      value: totalUnits == 0 ? 0 : doneUnits / totalUnits,
                      size: 118,
                      child: Column(mainAxisSize: MainAxisSize.min, children: [
                        Text(pct(totalUnits == 0 ? 0 : doneUnits / totalUnits), style: AppText.h1(AppColors.gold2)),
                        Text('$doneUnits/$totalUnits', style: AppText.small()),
                      ]),
                    ),
                    const SizedBox(width: 20),
                    Expanded(
                      child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                        Text('FIM PREVISTO', style: AppText.label()),
                        Text(s.endDate == null ? 'concluída' : fmtDate(s.endDate!), style: AppText.h2(AppColors.gold2)),
                        const SizedBox(height: 8),
                        Text('RESTAM', style: AppText.label()),
                        Text('${minutesLabel(s.remainingMinutes)} · ${s.weeksFor(p.hoursPerDay)} semanas', style: AppText.strong()),
                        if (exam != null && s.endDate != null) ...[
                          const SizedBox(height: 8),
                          Text(
                            s.endDate!.isAfter(exam) ? 'Termina depois da prova: aumente as horas ou priorize o peso 3.' : 'Termina antes da prova.',
                            style: AppText.small(s.endDate!.isAfter(exam) ? AppColors.red : AppColors.green),
                          ),
                        ],
                      ]),
                    ),
                  ]),
                  const SizedBox(height: 16),
                  Text('E SE EU ESTUDAR…', style: AppText.label()),
                  const SizedBox(height: 8),
                  Wrap(spacing: 8, runSpacing: 8, children: [
                    for (final h in const [1.0, 2.0, 3.0, 4.0, 6.0, 8.0])
                      Container(
                        width: 92,
                        padding: const EdgeInsets.symmetric(vertical: 8),
                        decoration: BoxDecoration(
                          color: h == p.hoursPerDay ? AppColors.gold.withValues(alpha: 0.15) : AppColors.field,
                          borderRadius: BorderRadius.circular(8),
                          border: Border.all(color: h == p.hoursPerDay ? AppColors.gold : AppColors.line),
                        ),
                        child: Column(children: [
                          Text('${fmtHours(h)}/dia', style: AppText.label(AppColors.text)),
                          Text('${s.weeksFor(h)} sem', style: AppText.small(h == p.hoursPerDay ? AppColors.gold2 : AppColors.muted)),
                        ]),
                      ),
                  ]),
                ]),
              ),
            ),
          ]),
        ),
        const SizedBox(height: 16),

        // ------------------------------------------------ gráfico + alertas
        Padding(
          padding: const EdgeInsets.symmetric(horizontal: 28),
          child: Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Expanded(
              flex: 7,
              child: Panel(
                child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
                  const SectionLabel('Questões por semana · linha = % de acerto'),
                  _weeklyChart(st),
                ]),
              ),
            ),
            const SizedBox(width: 16),
            Expanded(flex: 5, child: _Alerts(stats: st)),
          ]),
        ),
        const SizedBox(height: 16),

        // ------------------------------------------------ ciclo por matéria
        Padding(padding: const EdgeInsets.symmetric(horizontal: 28), child: _CycleTable()),
      ],
    );
  }

  Widget _weeklyChart(Stats st) {
    final w = st.weekly(12);
    if (w.every((x) => x.questions == 0)) {
      return const SizedBox(
        height: 200,
        child: EmptyState(icon: Icons.bar_chart, title: 'Sem questões ainda', text: 'Conclua missões de questões ou lance no DIÁRIO para ver sua evolução.'),
      );
    }
    return BarLineChart(points: [for (final p in w) ChartPoint(fmtDayMonth(p.start), p.questions.toDouble(), rate: p.accuracy)], height: 210);
  }
}

class _Countdown extends StatelessWidget {
  const _Countdown({required this.days, required this.date});
  final int days;
  final DateTime date;

  @override
  Widget build(BuildContext context) => Container(
        padding: const EdgeInsets.symmetric(horizontal: 22, vertical: 12),
        decoration: BoxDecoration(color: AppColors.bg, borderRadius: BorderRadius.circular(12), border: Border.all(color: AppColors.gold)),
        child: Column(children: [
          Text('FALTAM', style: AppText.label(AppColors.gold)),
          Text('$days', style: AppText.kpi(AppColors.gold2).copyWith(fontSize: 42)),
          Text(days == 1 ? 'DIA PARA A PROVA' : 'DIAS PARA A PROVA', style: AppText.label()),
          Text(fmtDate(date), style: AppText.small(AppColors.dim)),
        ]),
      );
}

class _Alerts extends StatelessWidget {
  const _Alerts({required this.stats});
  final Stats stats;

  @override
  Widget build(BuildContext context) {
    final app = AppScope.of(context);
    final weak = <(String, TopicStats)>[
      for (final e in stats.topic.entries)
        if (e.value.status == TopicStatus.reinforce) (e.key, e.value),
    ]..sort((a, b) => (a.$2.accuracy ?? 0).compareTo(b.$2.accuracy ?? 0));
    final subjects = stats.subject.entries.where((e) => e.value.questions >= 10).toList()
      ..sort((a, b) => (a.value.accuracy ?? 0).compareTo(b.value.accuracy ?? 0));
    return Panel(
      child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
        SectionLabel('Pontos de atenção',
            trailing: TextButton(onPressed: () => app.goTo(AppPage.edital), child: const Text('EDITAL')), color: AppColors.red),
        if (weak.isEmpty && subjects.isEmpty)
          Padding(
            padding: const EdgeInsets.symmetric(vertical: 24),
            child: Text('Nenhum alerta. Assuntos com menos de 70% de acerto aparecem aqui para reforço.', style: AppText.small()),
          ),
        for (final (id, ts) in weak.take(5))
          Builder(builder: (context) {
            final t = app.catalog.topic(id)!;
            final sub = app.catalog.subject(t.subjectId);
            return Padding(
              padding: const EdgeInsets.only(bottom: 10),
              child: Row(children: [
                SubjectTag(sub),
                const SizedBox(width: 10),
                Expanded(child: Text(t.name, style: AppText.body(), maxLines: 1, overflow: TextOverflow.ellipsis)),
                Text(pct(ts.accuracy), style: AppText.h3(AppColors.red)),
              ]),
            );
          }),
        if (subjects.isNotEmpty) ...[
          const SizedBox(height: 8),
          Text('MATÉRIAS COM MENOR ACERTO', style: AppText.label()),
          const SizedBox(height: 8),
          for (final e in subjects.take(3))
            Padding(
              padding: const EdgeInsets.only(bottom: 8),
              child: Row(children: [
                SizedBox(width: 150, child: Text(app.catalog.subject(e.key).name, style: AppText.small(AppColors.text), overflow: TextOverflow.ellipsis)),
                Expanded(child: Bar(e.value.accuracy ?? 0, color: (e.value.accuracy ?? 0) < 0.7 ? AppColors.red : AppColors.amber)),
                const SizedBox(width: 10),
                SizedBox(width: 42, child: Text(pct(e.value.accuracy), style: AppText.small(AppColors.text), textAlign: TextAlign.right)),
              ]),
            ),
        ],
      ]),
    );
  }
}

class _CycleTable extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final app = AppScope.of(context);
    final trail = app.trail!;
    final st = app.stats!;
    final total = trail.totalMinutes == 0 ? 1 : trail.totalMinutes;
    Widget head(String t, {int flex = 1, TextAlign align = TextAlign.left}) =>
        Expanded(flex: flex, child: Text(t, style: AppText.label(AppColors.gold), textAlign: align));
    return Panel(
      child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
        const SectionLabel('Ciclo de estudos por matéria'),
        Padding(
          padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 6),
          child: Row(children: [
            head('MATÉRIA', flex: 4),
            head('PESO · ENTRADA', flex: 3),
            head('% DO CICLO', flex: 2, align: TextAlign.center),
            head('CARGA', flex: 2, align: TextAlign.center),
            head('TEORIA FEITA', flex: 3),
            head('QUESTÕES', flex: 2, align: TextAlign.center),
            head('% ACERTO', flex: 2, align: TextAlign.center),
          ]),
        ),
        const Divider(color: AppColors.gold, thickness: 1.2),
        for (final sp in trail.subjects)
          Builder(builder: (context) {
            final ss = st.subject[sp.subject.id] ?? SubjectStats();
            final col = AppColors.hex(sp.subject.colorHex);
            final share = sp.topics == 0 ? 0.0 : ss.theoryDone / sp.topics;
            final acc = ss.accuracy;
            return Container(
              padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 9),
              decoration: const BoxDecoration(border: Border(bottom: BorderSide(color: AppColors.lineSoft))),
              child: Row(children: [
                Expanded(
                  flex: 4,
                  child: Row(children: [
                    Container(width: 8, height: 8, decoration: BoxDecoration(color: col, shape: BoxShape.circle)),
                    const SizedBox(width: 10),
                    Expanded(child: Text(sp.subject.name, style: AppText.strong(col), overflow: TextOverflow.ellipsis)),
                  ]),
                ),
                Expanded(flex: 3, child: Row(children: [Dots(sp.weight), const SizedBox(width: 8), Text(sp.entry, style: AppText.small())])),
                Expanded(flex: 2, child: Text(pct(sp.minutes / total), style: AppText.body(), textAlign: TextAlign.center)),
                Expanded(flex: 2, child: Text('${(sp.minutes / 60).round()} h', style: AppText.body(), textAlign: TextAlign.center)),
                Expanded(
                  flex: 3,
                  child: Row(children: [
                    Expanded(child: Bar(share, color: AppColors.gold)),
                    const SizedBox(width: 8),
                    SizedBox(width: 48, child: Text('${ss.theoryDone}/${sp.topics}', style: AppText.small())),
                  ]),
                ),
                Expanded(flex: 2, child: Text(ss.questions == 0 ? '—' : thousands(ss.questions), style: AppText.body(), textAlign: TextAlign.center)),
                Expanded(
                  flex: 2,
                  child: Text(
                    pct(acc),
                    style: AppText.strong(acc == null ? AppColors.dim : (acc >= 0.8 ? AppColors.green : (acc < 0.7 ? AppColors.red : AppColors.text))),
                    textAlign: TextAlign.center,
                  ),
                ),
              ]),
            );
          }),
      ]),
    );
  }
}
