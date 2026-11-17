import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../core/catalog.dart';
import '../core/dates.dart';
import '../core/models.dart';
import '../core/planner.dart';
import '../state/app_state.dart';
import 'theme.dart';
import 'widgets.dart';

Future<bool> confirm(BuildContext context, String title, String text, {String ok = 'CONFIRMAR', bool danger = false}) async {
  final r = await showDialog<bool>(
    context: context,
    builder: (c) => AlertDialog(
      title: Text(title.toUpperCase(), style: AppText.h2()),
      content: ConstrainedBox(constraints: const BoxConstraints(maxWidth: 460), child: Text(text, style: AppText.body(AppColors.muted))),
      actions: [
        TextButton(onPressed: () => Navigator.pop(c, false), child: const Text('CANCELAR')),
        ElevatedButton(
          style: danger ? ElevatedButton.styleFrom(backgroundColor: AppColors.red) : null,
          onPressed: () => Navigator.pop(c, true),
          child: Text(ok),
        ),
      ],
    ),
  );
  return r ?? false;
}

class NumberField extends StatelessWidget {
  const NumberField({super.key, required this.controller, required this.label, this.suffix, this.autofocus = false, this.onSubmitted});
  final TextEditingController controller;
  final String label;
  final String? suffix;
  final bool autofocus;
  final VoidCallback? onSubmitted;

  @override
  Widget build(BuildContext context) => TextField(
        controller: controller,
        autofocus: autofocus,
        keyboardType: TextInputType.number,
        inputFormatters: [FilteringTextInputFormatter.digitsOnly, LengthLimitingTextInputFormatter(4)],
        decoration: InputDecoration(labelText: label, suffixText: suffix),
        style: AppText.strong(),
        onSubmitted: (_) => onSubmitted?.call(),
      );
}

int _int(TextEditingController c) => int.tryParse(c.text.trim()) ?? 0;

class _Labeled extends StatelessWidget {
  const _Labeled(this.label, this.child);
  final String label;
  final Widget child;
  @override
  Widget build(BuildContext context) => Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        mainAxisSize: MainAxisSize.min,
        children: [Text(label.toUpperCase(), style: AppText.label()), const SizedBox(height: 6), child],
      );
}

/// Concluir uma missão da trilha (teoria ou questões) e lançar no diário.
Future<void> showUnitDoneDialog(BuildContext context, Unit u) async {
  final app = AppScope.read(context);
  final hasMaterial = app.content.forTopic(u.topic.id).isNotEmpty;
  final q = TextEditingController(text: u.isTheory ? '' : '${u.questions}');
  final c = TextEditingController();
  final m = TextEditingController(text: '${u.minutes}');
  final notes = TextEditingController();
  var source = u.isTheory ? (hasMaterial ? 'Material do app' : 'PDF / livro') : 'Plataforma de questões';
  final col = AppColors.hex(u.subject.colorHex);

  await showDialog<void>(
    context: context,
    builder: (ctx) => StatefulBuilder(builder: (ctx, setState) => ListenableBuilder(listenable: Listenable.merge([q, c, m]), builder: (ctx, _) {
      String? error;
      if (!u.isTheory && _int(c) > _int(q)) error = 'Acertos não podem passar do total de questões.';
      void save() {
        if (error != null) return;
        if (!u.isTheory && _int(q) == 0) return;
        app.completeUnit(
          u,
          questions: u.isTheory ? 0 : _int(q),
          correct: u.isTheory ? 0 : _int(c),
          minutes: _int(m),
          source: source,
          notes: notes.text.trim(),
        );
        Navigator.pop(ctx);
      }

      final acc = _int(q) > 0 ? _int(c) / _int(q) : null;
      return AlertDialog(
        titlePadding: EdgeInsets.zero,
        title: Container(
          padding: const EdgeInsets.fromLTRB(24, 20, 24, 14),
          decoration: BoxDecoration(border: Border(left: BorderSide(color: col, width: 4))),
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Text('MISSÃO #${u.seq} · ${u.isTheory ? 'TEORIA + RESUMO' : '${u.questions} QUESTÕES'}', style: AppText.label(col)),
            const SizedBox(height: 4),
            Text(u.topic.name, style: AppText.h2()),
            Text(u.subject.name, style: AppText.small()),
          ]),
        ),
        content: SizedBox(
          width: 460,
          child: Column(mainAxisSize: MainAxisSize.min, crossAxisAlignment: CrossAxisAlignment.stretch, children: [
            if (!u.isTheory) ...[
              Row(children: [
                Expanded(child: NumberField(controller: q, label: 'Questões feitas', autofocus: true, onSubmitted: save)),
                const SizedBox(width: 12),
                Expanded(child: NumberField(controller: c, label: 'Acertos', onSubmitted: save)),
              ]),
              const SizedBox(height: 8),
              Row(children: [
                Text(acc == null ? 'Informe as questões e os acertos.' : 'Acerto: ${pct(acc)} · líquida ${_int(c) - (_int(q) - _int(c))}',
                    style: AppText.small(acc == null ? AppColors.muted : (acc >= 0.8 ? AppColors.green : (acc < 0.7 ? AppColors.red : AppColors.amber)))),
              ]),
              if (error != null) Padding(padding: const EdgeInsets.only(top: 6), child: Text(error, style: AppText.small(AppColors.red))),
              const SizedBox(height: 14),
            ],
            Row(children: [
              SizedBox(width: 150, child: NumberField(controller: m, label: 'Tempo', suffix: 'min', autofocus: u.isTheory, onSubmitted: save)),
              const SizedBox(width: 12),
              Expanded(
                child: DropdownButtonFormField<String>(
                  initialValue: source,
                  isExpanded: true,
                  decoration: const InputDecoration(labelText: 'Fonte'),
                  dropdownColor: AppColors.panel2,
                  items: [for (final s in kSources) DropdownMenuItem(value: s, child: Text(s))],
                  onChanged: (v) => setState(() => source = v ?? source),
                ),
              ),
            ]),
            const SizedBox(height: 14),
            TextField(
              controller: notes,
              maxLines: 2,
              decoration: InputDecoration(labelText: u.isTheory ? 'Anotações (opcional)' : 'O que errei / o que revisar (opcional)'),
            ),
          ]),
        ),
        actions: [
          TextButton(onPressed: () => Navigator.pop(ctx), child: const Text('CANCELAR')),
          ElevatedButton.icon(
            onPressed: (error != null || (!u.isTheory && _int(q) == 0)) ? null : save,
            icon: const Icon(Icons.check, size: 18),
            label: const Text('MISSÃO CUMPRIDA'),
          ),
        ],
      );
    })),
  );
}

/// Concluir uma tarefa do dia que pede números (simulado, questões de revisão, discursiva).
Future<void> showTaskDoneDialog(BuildContext context, DayTask t) async {
  final app = AppScope.read(context);
  final q = TextEditingController(text: t.askQuestions ? '${t.suggestedQuestions}' : '');
  final c = TextEditingController();
  final m = TextEditingController(text: '${t.minutes}');
  final notes = TextEditingController();
  await showDialog<void>(
    context: context,
    builder: (ctx) => StatefulBuilder(builder: (ctx, setState) => ListenableBuilder(listenable: Listenable.merge([q, c, m]), builder: (ctx, _) {
      final bad = t.askQuestions && _int(c) > _int(q);
      void save() {
        if (bad) return;
        app.completeTask(
          t,
          questions: t.askQuestions ? _int(q) : 0,
          correct: t.askQuestions ? _int(c) : 0,
          minutes: _int(m),
          notes: notes.text.trim(),
        );
        Navigator.pop(ctx);
      }

      final net = _int(c) - (_int(q) - _int(c));
      return AlertDialog(
        title: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Text(t.title.toUpperCase(), style: AppText.h2()),
          const SizedBox(height: 4),
          Text(t.detail, style: AppText.small()),
        ]),
        content: SizedBox(
          width: 440,
          child: Column(mainAxisSize: MainAxisSize.min, crossAxisAlignment: CrossAxisAlignment.stretch, children: [
            if (t.askQuestions) ...[
              Row(children: [
                Expanded(child: NumberField(controller: q, label: 'Itens / questões', autofocus: true, onSubmitted: save)),
                const SizedBox(width: 12),
                Expanded(child: NumberField(controller: c, label: 'Acertos', onSubmitted: save)),
              ]),
              const SizedBox(height: 8),
              Text(
                bad ? 'Acertos não podem passar do total.' : (_int(q) > 0 ? 'Acerto ${pct(_int(c) / _int(q))} · nota líquida $net (certas − erradas)' : ''),
                style: AppText.small(bad ? AppColors.red : AppColors.muted),
              ),
              const SizedBox(height: 14),
            ],
            SizedBox(width: 160, child: NumberField(controller: m, label: 'Tempo', suffix: 'min', autofocus: !t.askQuestions, onSubmitted: save)),
            const SizedBox(height: 14),
            TextField(controller: notes, maxLines: 2, decoration: const InputDecoration(labelText: 'Observações (opcional)')),
          ]),
        ),
        actions: [
          TextButton(onPressed: () => Navigator.pop(ctx), child: const Text('CANCELAR')),
          ElevatedButton.icon(onPressed: bad ? null : save, icon: const Icon(Icons.check, size: 18), label: const Text('CONCLUIR')),
        ],
      );
    })),
  );
}

/// Lançamento manual (ou edição) no diário.
Future<void> showEntryDialog(BuildContext context, {DiaryEntry? entry}) async {
  final app = AppScope.read(context);
  final cat = app.catalog;
  final opt = app.profile.optionId;
  final subjects = [...cat.subjects]..sort((a, b) {
      final c = b.weightFor(opt).compareTo(a.weightFor(opt));
      return c != 0 ? c : a.name.compareTo(b.name);
    });
  var date = entry?.date ?? app.today;
  var type = entry?.type ?? 'Questões';
  String? subjectId = entry?.subjectId;
  String? topicId = (entry?.topicIds.length ?? 0) == 1 ? entry!.topicIds.first : null;
  var source = entry?.source.isNotEmpty == true ? entry!.source : 'Plataforma de questões';
  if (!kSources.contains(source)) source = 'Outro';
  final q = TextEditingController(text: entry == null ? '' : '${entry.questions}');
  final c = TextEditingController(text: entry == null ? '' : '${entry.correct}');
  final m = TextEditingController(text: entry == null ? '' : '${entry.minutes}');
  final notes = TextEditingController(text: entry?.notes ?? '');

  await showDialog<void>(
    context: context,
    builder: (ctx) => StatefulBuilder(builder: (ctx, setState) => ListenableBuilder(listenable: Listenable.merge([q, c, m]), builder: (ctx, _) {
      final topics = subjectId == null ? <Topic>[] : cat.topicsToPick(subjectId!, app.profile.careerCode, opt);
      final bad = _int(c) > _int(q);
      final empty = _int(q) == 0 && _int(m) == 0;
      void save() {
        if (bad || empty) return;
        final e = DiaryEntry(
          id: entry?.id ?? app.newId('d'),
          date: date,
          type: type,
          subjectId: subjectId,
          topicIds: topicId != null ? [topicId!] : (entry?.topicIds.length ?? 0) > 1 ? entry!.topicIds : const [],
          questions: _int(q),
          correct: _int(c),
          minutes: _int(m),
          source: source,
          notes: notes.text.trim(),
          origin: entry?.origin ?? '',
        );
        if (entry == null) {
          app.addEntry(e);
        } else {
          app.updateEntry(e);
        }
        Navigator.pop(ctx);
      }

      return AlertDialog(
        title: Text(entry == null ? 'NOVO LANÇAMENTO' : 'EDITAR LANÇAMENTO', style: AppText.h2()),
        content: SizedBox(
          width: 560,
          child: SingleChildScrollView(
            child: Column(mainAxisSize: MainAxisSize.min, crossAxisAlignment: CrossAxisAlignment.stretch, children: [
              Row(children: [
                Expanded(
                  child: _Labeled(
                    'Data',
                    OutlinedButton.icon(
                      icon: const Icon(Icons.event, size: 18),
                      label: Text(fmtDate(date)),
                      onPressed: () async {
                        final d = await showDatePicker(
                          context: ctx,
                          initialDate: date,
                          firstDate: DateTime(2020),
                          lastDate: addDays(app.today, 1),
                        );
                        if (d != null) setState(() => date = dateOnly(d));
                      },
                    ),
                  ),
                ),
                const SizedBox(width: 12),
                Expanded(
                  child: _Labeled(
                    'Tipo',
                    DropdownButtonFormField<String>(
                      initialValue: type,
                      isExpanded: true,
                      dropdownColor: AppColors.panel2,
                      items: [for (final t in kDiaryTypes) DropdownMenuItem(value: t, child: Text(t))],
                      onChanged: (v) => setState(() => type = v ?? type),
                    ),
                  ),
                ),
              ]),
              const SizedBox(height: 14),
              _Labeled(
                'Matéria',
                DropdownButtonFormField<String?>(
                  initialValue: subjectId,
                  isExpanded: true,
                  dropdownColor: AppColors.panel2,
                  items: [
                    const DropdownMenuItem<String?>(value: null, child: Text('Geral / várias matérias')),
                    for (final s in subjects)
                      DropdownMenuItem<String?>(
                        value: s.id,
                        child: Row(children: [
                          Container(width: 8, height: 8, decoration: BoxDecoration(color: AppColors.hex(s.colorHex), shape: BoxShape.circle)),
                          const SizedBox(width: 8),
                          Expanded(child: Text(s.name, overflow: TextOverflow.ellipsis)),
                          if (s.weightFor(opt) == 0) Text('fora do ciclo', style: AppText.small(AppColors.dim)),
                        ]),
                      ),
                  ],
                  onChanged: (v) => setState(() {
                    subjectId = v;
                    topicId = null;
                  }),
                ),
              ),
              const SizedBox(height: 14),
              _Labeled(
                'Assunto do edital',
                DropdownButtonFormField<String?>(
                  key: ValueKey(subjectId),
                  initialValue: topicId,
                  isExpanded: true,
                  dropdownColor: AppColors.panel2,
                  items: [
                    const DropdownMenuItem<String?>(value: null, child: Text('—')),
                    for (final t in topics) DropdownMenuItem<String?>(value: t.id, child: Text('${t.n}. ${t.name}', overflow: TextOverflow.ellipsis)),
                  ],
                  onChanged: subjectId == null ? null : (v) => setState(() => topicId = v),
                ),
              ),
              const SizedBox(height: 14),
              Row(children: [
                Expanded(child: NumberField(controller: q, label: 'Questões')),
                const SizedBox(width: 10),
                Expanded(child: NumberField(controller: c, label: 'Acertos')),
                const SizedBox(width: 10),
                Expanded(child: NumberField(controller: m, label: 'Tempo', suffix: 'min')),
              ]),
              if (bad) Padding(padding: const EdgeInsets.only(top: 6), child: Text('Acertos não podem passar do total.', style: AppText.small(AppColors.red))),
              const SizedBox(height: 14),
              _Labeled(
                'Fonte',
                DropdownButtonFormField<String>(
                  initialValue: source,
                  isExpanded: true,
                  dropdownColor: AppColors.panel2,
                  items: [for (final s in kSources) DropdownMenuItem(value: s, child: Text(s))],
                  onChanged: (v) => setState(() => source = v ?? source),
                ),
              ),
              const SizedBox(height: 14),
              TextField(controller: notes, maxLines: 3, decoration: const InputDecoration(labelText: 'Observações · o que errei')),
            ]),
          ),
        ),
        actions: [
          TextButton(onPressed: () => Navigator.pop(ctx), child: const Text('CANCELAR')),
          ElevatedButton(onPressed: bad || empty ? null : save, child: const Text('SALVAR')),
        ],
      );
    })),
  );
}
