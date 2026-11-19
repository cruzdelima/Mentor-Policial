import 'package:flutter/material.dart';

import '../../core/catalog.dart';
import '../../core/dates.dart';
import '../../core/stats.dart';
import '../../state/app_state.dart';
import '../dialogs.dart';
import '../theme.dart';
import '../widgets.dart';

class EditalPage extends StatefulWidget {
  const EditalPage({super.key});

  @override
  State<EditalPage> createState() => _EditalPageState();
}

class _EditalPageState extends State<EditalPage> {
  String? subjectId;
  TopicStatus? status;
  String query = '';

  @override
  Widget build(BuildContext context) {
    final app = AppScope.of(context);
    final cat = app.catalog;
    final st = app.stats!;
    final trail = app.trail!;
    final opt = app.profile.optionId;
    final inCycle = cat.subjects.where((s) => s.weightFor(opt) > 0).toList()
      ..sort((a, b) => b.weightFor(opt).compareTo(a.weightFor(opt)));
    final outCycle = cat.subjects.where((s) => s.weightFor(opt) == 0).toList();
    final q = query.trim().toLowerCase();
    final contest = app.cargo.contest;
    final career = app.profile.careerCode;
    final topics = cat.topics.where((t) {
      if (subjectId != null && t.subjectId != subjectId) return false;
      final inPlan = cat.subject(t.subjectId).weightFor(opt) > 0;
      if (subjectId == null && !inPlan) return false;
      final applies = cat.topicApplies(t, career, opt);
      // Assuntos exclusivos de outro edital nunca aparecem; no pós-edital, só o que está no edital.
      if (t.contest != null && !applies) return false;
      if (contest != null && inPlan && !applies) return false;
      final ts = st.topic[t.id]!;
      if (status != null && ts.status != status) return false;
      if (q.isNotEmpty && !t.name.toLowerCase().contains(q)) return false;
      return true;
    }).toList();
    if (contest != null) {
      final subjOrder = {for (var i = 0; i < inCycle.length; i++) inCycle[i].id: i};
      topics.sort((a, b) {
        final c = (subjOrder[a.subjectId] ?? 99).compareTo(subjOrder[b.subjectId] ?? 99);
        if (c != 0) return c;
        return (cat.contestPosition(opt, a.id) ?? 9999).compareTo(cat.contestPosition(opt, b.id) ?? 9999);
      });
    }

    // Telas estreitas (tablet na horizontal): esconde as colunas PREVISTO e REVISÕES.
    final narrow = MediaQuery.sizeOf(context).width < 1240;
    return Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
      PageHeader(
        title: 'Edital verticalizado',
        subtitle: '${app.cargo.name}${contest == null ? '' : ' · PÓS-EDITAL${contest.examDate == null ? '' : ' · prova ${fmtDate(contest.examDate!)}'}${contest.totalQuestions > 0 ? ' · ${contest.totalQuestions} questões' : ''}'}'
            ' · ${st.activeTopics} assuntos no ${contest == null ? 'ciclo' : 'edital'} · teoria ${pct(st.theoryShare)} · '
            '${st.reinforce} para reforçar · ${st.consolidated} consolidados',
      ),
      Expanded(
        child: Row(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
          // ------------------------------------------------ matérias
          SizedBox(
            width: narrow ? 220 : 250,
            child: ListView(padding: EdgeInsets.fromLTRB(narrow ? 20 : 28, 0, 8, 28), children: [
              _SubjectTile(
                label: 'Todas as matérias do ciclo',
                color: AppColors.gold,
                selected: subjectId == null,
                progress: st.theoryShare,
                detail: '${st.theoryDone}/${st.activeTopics}',
                onTap: () => setState(() => subjectId = null),
              ),
              const SizedBox(height: 8),
              for (final s in inCycle)
                Builder(builder: (context) {
                  final ss = st.subject[s.id] ?? SubjectStats();
                  return _SubjectTile(
                    label: s.name,
                    color: AppColors.hex(s.colorHex),
                    selected: subjectId == s.id,
                    weight: s.weightFor(opt),
                    progress: ss.topics == 0 ? 0 : ss.theoryDone / ss.topics,
                    detail: '${contest != null && (contest.questions[s.id] ?? 0) > 0 ? '${contest.questions[s.id]}q · ' : ''}'
                        '${ss.accuracy == null ? '${ss.theoryDone}/${ss.topics}' : '${ss.theoryDone}/${ss.topics} · ${pct(ss.accuracy)}'}',
                    onTap: () => setState(() => subjectId = s.id),
                  );
                }),
              if (outCycle.isNotEmpty) ...[
                const SizedBox(height: 14),
                Text(contest == null ? 'FORA DO CICLO BÁSICO DO SEU CARGO' : 'FORA DO EDITAL', style: AppText.label(AppColors.dim)),
                const SizedBox(height: 6),
                for (final s in outCycle)
                  _SubjectTile(
                    label: s.name,
                    color: AppColors.dim,
                    selected: subjectId == s.id,
                    progress: 0,
                    detail: '',
                    onTap: () => setState(() => subjectId = s.id),
                  ),
              ],
            ]),
          ),
          // ------------------------------------------------ assuntos
          Expanded(
            child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
              Padding(
                padding: const EdgeInsets.fromLTRB(12, 0, 28, 12),
                child: Wrap(spacing: 8, runSpacing: 8, crossAxisAlignment: WrapCrossAlignment.center, children: [
                  SizedBox(
                    width: 260,
                    child: TextField(
                      onChanged: (v) => setState(() => query = v),
                      decoration: const InputDecoration(prefixIcon: Icon(Icons.search, size: 20), hintText: 'Buscar assunto'),
                    ),
                  ),
                  ToggleChip(label: 'TODOS', selected: status == null, onTap: () => setState(() => status = null)),
                  for (final s in const [TopicStatus.toStudy, TopicStatus.inProgress, TopicStatus.reinforce, TopicStatus.consolidated])
                    ToggleChip(label: s.label.toUpperCase(), selected: status == s, color: statusColor(s), onTap: () => setState(() => status = s)),
                ]),
              ),
              Container(
                margin: const EdgeInsets.fromLTRB(12, 0, 28, 0),
                padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 10),
                decoration: const BoxDecoration(
                  color: AppColors.panel2,
                  borderRadius: BorderRadius.vertical(top: Radius.circular(10)),
                  border: Border(bottom: BorderSide(color: AppColors.gold, width: 1.5)),
                ),
                child: Row(children: [
                  _h('Nº', 36),
                  Expanded(child: Text('ASSUNTO', style: AppText.label(AppColors.gold))),
                  _h('TAM.', 50),
                  if (!narrow) _h('PREVISTO', 84),
                  _h('TEORIA', 54),
                  _h('QUESTÕES', 70),
                  _h('% ACERTO', 70),
                  if (!narrow) _h('REVISÕES', 70),
                  _h('STATUS', narrow ? 108 : 120),
                  const SizedBox(width: 40),
                ]),
              ),
              Expanded(
                child: topics.isEmpty
                    ? const EmptyState(icon: Icons.filter_alt_off, title: 'Nenhum assunto', text: 'Nenhum assunto corresponde aos filtros escolhidos.')
                    : ListView.builder(
                        padding: const EdgeInsets.fromLTRB(12, 0, 28, 28),
                        itemCount: topics.length,
                        itemBuilder: (context, i) => _TopicRow(topic: topics[i], showSubject: subjectId == null, active: trail.isActive(topics[i].id), narrow: narrow),
                      ),
              ),
            ]),
          ),
        ]),
      ),
    ]);
  }

  Widget _h(String t, double w) => SizedBox(width: w, child: Text(t, style: AppText.label(AppColors.gold), textAlign: TextAlign.center));
}

class _SubjectTile extends StatelessWidget {
  const _SubjectTile({required this.label, required this.color, required this.selected, required this.progress, required this.detail, required this.onTap, this.weight});
  final String label;
  final Color color;
  final bool selected;
  final double progress;
  final String detail;
  final VoidCallback onTap;
  final int? weight;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 4),
      child: Material(
        color: selected ? AppColors.panel2 : Colors.transparent,
        borderRadius: BorderRadius.circular(8),
        child: InkWell(
          onTap: onTap,
          borderRadius: BorderRadius.circular(8),
          child: Padding(
            padding: const EdgeInsets.fromLTRB(12, 9, 12, 9),
            child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
              Row(children: [
                Container(width: 8, height: 8, decoration: BoxDecoration(color: color, shape: BoxShape.circle)),
                const SizedBox(width: 8),
                Expanded(child: Text(label, style: AppText.strong(selected ? AppColors.text : AppColors.muted).copyWith(fontSize: 13.5), overflow: TextOverflow.ellipsis)),
                if (weight != null) Dots(weight!, color: color),
              ]),
              if (detail.isNotEmpty) ...[
                const SizedBox(height: 6),
                Row(children: [
                  Expanded(child: Bar(progress, color: color, height: 4)),
                  const SizedBox(width: 8),
                  Text(detail, style: AppText.small(AppColors.dim).copyWith(fontSize: 11.5)),
                ]),
              ],
            ]),
          ),
        ),
      ),
    );
  }
}

class _TopicRow extends StatelessWidget {
  const _TopicRow({required this.topic, required this.showSubject, required this.active, this.narrow = false});
  final Topic topic;
  final bool narrow;
  final bool showSubject;
  final bool active;

  @override
  Widget build(BuildContext context) {
    final app = AppScope.of(context);
    final t = topic;
    final ts = app.stats!.topic[t.id]!;
    final ov = app.data.overrides[t.id];
    final skipped = ov?.skip ?? false;
    final size = ov?.size ?? t.size;
    final theory = app.trail!.theoryOf(t.id);
    final planned = theory == null ? null : app.schedule!.plannedDate(theory);
    final materials = app.content.forTopic(t.id);
    final sub = app.catalog.subject(t.subjectId);
    final hasNotes = (ov?.notes ?? '').isNotEmpty;
    final dim = !active;
    final txt = dim ? AppColors.dim : AppColors.text;
    String prev;
    if (skipped) {
      prev = 'pulado';
    } else if (!active) {
      prev = '—';
    } else if (ts.theory) {
      prev = 'feito';
    } else if (planned == null) {
      prev = '—';
    } else {
      prev = '${fmtDayMonth(planned)}/${(planned.year % 100).toString().padLeft(2, '0')}';
    }
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
      decoration: const BoxDecoration(color: AppColors.panel, border: Border(bottom: BorderSide(color: AppColors.lineSoft))),
      child: Row(children: [
        SizedBox(width: 36, child: Text('${t.n}', style: AppText.small(AppColors.dim), textAlign: TextAlign.center)),
        Expanded(
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, mainAxisSize: MainAxisSize.min, children: [
            Row(children: [
              if (showSubject) ...[SubjectTag(sub), const SizedBox(width: 8)],
              Flexible(child: Text(t.name, style: AppText.body(txt), overflow: TextOverflow.ellipsis, maxLines: 2)),
              if (materials.isNotEmpty) ...[
                const SizedBox(width: 8),
                Tooltip(
                  message: 'Material do app disponível',
                  child: InkWell(
                    onTap: () => app.goTo(AppPage.materials, materialId: materials.first.id),
                    child: const Icon(Icons.auto_stories, size: 17, color: AppColors.teal),
                  ),
                ),
              ],
              if (hasNotes) ...[const SizedBox(width: 6), Tooltip(message: ov!.notes, child: const Icon(Icons.sticky_note_2_outlined, size: 16, color: AppColors.amber))],
            ]),
            if (t.scope.isNotEmpty) Text('só para: ${t.scope.join(', ')}', style: AppText.small(AppColors.dim).copyWith(fontSize: 11)),
          ]),
        ),
        SizedBox(
          width: 50,
          child: Center(
            child: PopupMenuButton<String>(
              tooltip: 'Tamanho do assunto (muda a duração das missões)',
              initialValue: size,
              onSelected: (v) => app.setSize(t.id, v),
              itemBuilder: (_) => [
                for (final s in const ['P', 'M', 'G'])
                  PopupMenuItem(value: s, child: Text('$s · ${s == 'P' ? 'pequeno' : (s == 'M' ? 'médio' : 'grande')}${s == t.size ? ' (padrão)' : ''}')),
              ],
              child: Container(
                padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 3),
                decoration: BoxDecoration(
                  color: AppColors.field,
                  borderRadius: BorderRadius.circular(6),
                  border: Border.all(color: size != t.size ? AppColors.gold : AppColors.line),
                ),
                child: Text(size, style: AppText.h3(AppColors.gold2).copyWith(fontSize: 14)),
              ),
            ),
          ),
        ),
        if (!narrow) SizedBox(width: 84, child: Text(prev, style: AppText.small(prev == 'feito' ? AppColors.green : AppColors.muted), textAlign: TextAlign.center)),
        SizedBox(width: 54, child: Center(child: ts.theory ? const Icon(Icons.check_circle, size: 18, color: AppColors.green) : Text('—', style: AppText.small(AppColors.dim)))),
        SizedBox(width: 70, child: Text(ts.questions == 0 ? '—' : thousands(ts.questions), style: AppText.body(txt), textAlign: TextAlign.center)),
        SizedBox(
          width: 70,
          child: Text(
            pct(ts.accuracy),
            textAlign: TextAlign.center,
            style: AppText.strong(ts.accuracy == null ? AppColors.dim : (ts.accuracy! >= 0.8 ? AppColors.green : (ts.accuracy! < 0.7 ? AppColors.red : AppColors.text))),
          ),
        ),
        if (!narrow) SizedBox(width: 70, child: Center(child: Dots(ts.reviews.clamp(0, 3)))),
        SizedBox(width: narrow ? 108 : 120, child: Center(child: skipped ? const Pill('PULADO', color: AppColors.dim) : StatusPill(ts.status))),
        SizedBox(
          width: 40,
          child: PopupMenuButton<String>(
            tooltip: 'Opções',
            icon: const Icon(Icons.more_vert, size: 20, color: AppColors.muted),
            onSelected: (v) async {
              switch (v) {
                case 'skip':
                  final ok = await confirm(context, 'Pular assunto',
                      '“${t.name}” sai do ciclo e o cronograma é recalculado. Use quando o seu edital não cobrar este assunto.',
                      ok: 'PULAR');
                  if (ok) app.setSkip(t.id, true);
                case 'unskip':
                  app.setSkip(t.id, false);
                case 'notes':
                  if (context.mounted) await _notesDialog(context, t, ov?.notes ?? '');
                case 'material':
                  app.goTo(AppPage.materials, materialId: materials.first.id);
              }
            },
            itemBuilder: (_) => [
              if (!skipped && active) const PopupMenuItem(value: 'skip', child: Text('Pular (fora do meu edital)')),
              if (skipped) const PopupMenuItem(value: 'unskip', child: Text('Voltar para o ciclo')),
              const PopupMenuItem(value: 'notes', child: Text('Anotações')),
              if (materials.isNotEmpty) const PopupMenuItem(value: 'material', child: Text('Abrir material do app')),
            ],
          ),
        ),
      ]),
    );
  }

  Future<void> _notesDialog(BuildContext context, Topic t, String current) async {
    final app = AppScope.read(context);
    final c = TextEditingController(text: current);
    await showDialog<void>(
      context: context,
      builder: (ctx) => AlertDialog(
        title: Text(t.name.toUpperCase(), style: AppText.h2()),
        content: SizedBox(
          width: 520,
          child: TextField(
            controller: c,
            maxLines: 8,
            autofocus: true,
            decoration: const InputDecoration(hintText: 'Pegadinhas, artigos de lei, o que revisar, onde está o melhor material…'),
          ),
        ),
        actions: [
          TextButton(onPressed: () => Navigator.pop(ctx), child: const Text('CANCELAR')),
          ElevatedButton(
            onPressed: () {
              app.setTopicNotes(t.id, c.text.trim());
              Navigator.pop(ctx);
            },
            child: const Text('SALVAR'),
          ),
        ],
      ),
    );
  }
}
