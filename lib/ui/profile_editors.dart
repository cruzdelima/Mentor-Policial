import 'package:flutter/material.dart';

import '../core/catalog.dart';
import '../core/dates.dart';
import '../core/extras.dart';
import '../core/models.dart';
import 'theme.dart';
import 'widgets.dart';

const kWeekdayShort = ['SEG', 'TER', 'QUA', 'QUI', 'SEX', 'SÁB', 'DOM'];
const kWeekdayLong = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo'];

const _esferaInfo = {
  'Federal': ('PF · PRF · Polícia Penal Federal', Icons.account_balance_outlined),
  'Estadual': ('Polícia Civil · PM · Bombeiros · Polícia Penal', Icons.map_outlined),
  'Municipal': ('Guarda Civil Municipal', Icons.location_city_outlined),
};

class EsferaPicker extends StatelessWidget {
  const EsferaPicker({super.key, required this.catalog, required this.value, required this.onChanged});
  final Catalog catalog;
  final String? value;
  final ValueChanged<String> onChanged;

  @override
  Widget build(BuildContext context) {
    return Wrap(
      spacing: 14,
      runSpacing: 14,
      children: [
        for (final e in catalog.esferas)
          ChoiceCard(
            width: 260,
            selected: value == e,
            color: AppColors.gold,
            onTap: () => onChanged(e),
            leading: Container(
              width: 36,
              height: 36,
              decoration: BoxDecoration(color: AppColors.esfera(e), borderRadius: BorderRadius.circular(8)),
              child: Icon(_esferaInfo[e]!.$2, color: Colors.white, size: 20),
            ),
            title: e,
            subtitle: _esferaInfo[e]!.$1,
            footer: Text('${catalog.careersOf(e).length} carreira(s) · ${catalog.careersOf(e).expand((c) => c.cargos).length} cargo(s)',
                style: AppText.small(AppColors.dim)),
          ),
      ],
    );
  }
}

class CareerPicker extends StatelessWidget {
  const CareerPicker({super.key, required this.catalog, required this.esfera, required this.value, required this.onChanged});
  final Catalog catalog;
  final String esfera;
  final String? value;
  final ValueChanged<String> onChanged;

  @override
  Widget build(BuildContext context) {
    return Wrap(
      spacing: 14,
      runSpacing: 14,
      children: [
        for (final c in catalog.careersOf(esfera))
          ChoiceCard(
            width: 340,
            selected: value == c.code,
            onTap: () => onChanged(c.code),
            leading: Container(
              padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 6),
              decoration: BoxDecoration(color: AppColors.esfera(c.esfera), borderRadius: BorderRadius.circular(6)),
              child: Text(c.code, style: AppText.h3(Colors.white)),
            ),
            title: c.name,
            subtitle: c.observacao,
            footer: Wrap(spacing: 6, runSpacing: 6, children: [
              Pill(c.banca, color: AppColors.blue),
              Pill(c.escolaridade, color: AppColors.muted),
              if (c.discursiva) const Pill('Discursiva', color: AppColors.amber),
              Pill('Marca: ${c.marca}', color: AppColors.gold),
            ]),
          ),
      ],
    );
  }
}

class CargoPicker extends StatelessWidget {
  const CargoPicker({super.key, required this.catalog, required this.career, required this.value, required this.onChanged});
  final Catalog catalog;
  final Career career;
  final String? value;
  final ValueChanged<String> onChanged;

  @override
  Widget build(BuildContext context) {
    final cycle = career.cycleCargos;
    final contests = career.contests;
    return Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
      if (contests.isNotEmpty) ...[
        Text('CICLO BÁSICO · PRÉ-EDITAL', style: AppText.label(AppColors.muted)),
        const SizedBox(height: 4),
        Text('Para quem estuda antes do edital sair: núcleo comum dos últimos concursos.', style: AppText.small(AppColors.dim)),
        const SizedBox(height: 10),
      ],
      Wrap(
        spacing: 14,
        runSpacing: 14,
        children: [
          for (final o in cycle)
            Builder(builder: (context) {
              final subs = catalog.subjects.where((s) => s.weightFor(o.id) > 0).toList()
                ..sort((a, b) => b.weightFor(o.id).compareTo(a.weightFor(o.id)));
              final heavy = subs.where((s) => s.weightFor(o.id) >= 3).map((s) => s.name).join(', ');
              return ChoiceCard(
                width: 340,
                selected: value == o.id,
                onTap: () => onChanged(o.id),
                title: o.name,
                subtitle: '${subs.length} matérias no ciclo básico${heavy.isEmpty ? '' : ' · peso alto: $heavy'}',
                footer: Wrap(spacing: 5, runSpacing: 5, children: [
                  for (final s in subs) SubjectTag(s),
                ]),
              );
            }),
        ],
      ),
      if (contests.isNotEmpty) ...[
        const SizedBox(height: 24),
        Text('PÓS-EDITAL · CONCURSOS COM EDITAL PUBLICADO', style: AppText.label(AppColors.gold)),
        const SizedBox(height: 4),
        Text('O plano segue exatamente o conteúdo e a ordem do edital, com a data da prova.', style: AppText.small(AppColors.dim)),
        const SizedBox(height: 10),
        Wrap(spacing: 14, runSpacing: 14, children: [
          for (final o in contests) ContestCard(catalog: catalog, cargo: o, selected: value == o.id, onTap: () => onChanged(o.id)),
        ]),
      ],
    ]);
  }
}

/// Cartão de um concurso pós-edital (usado na escolha do cargo e na página Pós-edital).
class ContestCard extends StatelessWidget {
  const ContestCard({super.key, required this.catalog, required this.cargo, required this.selected, required this.onTap, this.width = 340});
  final Catalog catalog;
  final Cargo cargo;
  final bool selected;
  final VoidCallback onTap;
  final double width;

  @override
  Widget build(BuildContext context) {
    final c = cargo.contest!;
    final subs = catalog.subjects.where((s) => s.weightFor(cargo.id) > 0).toList()
      ..sort((a, b) => b.weightFor(cargo.id).compareTo(a.weightFor(cargo.id)));
    final facts = [
      if (c.banca.isNotEmpty) c.banca,
      if (c.totalQuestions > 0) '${c.totalQuestions} questões',
      '${c.topicIds.length} assuntos',
      if (c.vagas.isNotEmpty) '${c.vagas} vagas',
    ];
    return ChoiceCard(
      width: width,
      selected: selected,
      onTap: onTap,
      title: cargo.name,
      subtitle: [if (c.orgao.isNotEmpty) c.orgao, facts.join(' · ')].join('\n'),
      footer: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
        Wrap(spacing: 6, runSpacing: 6, children: [
          const Pill('PÓS-EDITAL', color: AppColors.gold, filled: true),
          if (c.examDate != null) Pill('PROVA ${fmtDate(c.examDate!)}', color: AppColors.amber),
          if (kContestStatus[c.status] != null) Pill(kContestStatus[c.status]!, color: AppColors.blue),
        ]),
        const SizedBox(height: 8),
        Wrap(spacing: 5, runSpacing: 5, children: [for (final s in subs) SubjectTag(s)]),
      ]),
    );
  }
}

/// Horas por dia, dias da semana, dia de revisão, nível e datas.
class RoutineEditor extends StatelessWidget {
  const RoutineEditor({super.key, required this.catalog, required this.profile, required this.onChanged, this.today});
  final Catalog catalog;
  final Profile profile;
  final VoidCallback onChanged;
  final DateTime? today;

  @override
  Widget build(BuildContext context) {
    final p = profile;
    final prm = catalog.params;
    String lvDesc(int i) {
      String m(int v) => minutesLabel(v);
      return 'Teoria P/M/G: ${m(prm.theoryMinutes[0][i])} · ${m(prm.theoryMinutes[1][i])} · ${m(prm.theoryMinutes[2][i])} · '
          '${prm.minutesPerQuestion[i].toStringAsFixed(0)} min por questão';
    }

    const lvHelp = [
      'Começando agora ou sem base na maioria das matérias.',
      'Já estudou boa parte do conteúdo e quer acelerar.',
      'Já foi a provas e está revisando para a próxima.',
    ];
    final content = p.contentWeekdays.length;
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text('HORAS LÍQUIDAS POR DIA', style: AppText.label()),
        const SizedBox(height: 4),
        Text('Conte só o tempo de estudo de verdade, sem pausas e sem celular.', style: AppText.small(AppColors.dim)),
        const SizedBox(height: 10),
        Wrap(spacing: 8, runSpacing: 8, children: [
          for (final h in kHourOptions)
            ToggleChip(
              label: fmtHours(h),
              selected: p.hoursPerDay == h,
              onTap: () {
                p.hoursPerDay = h;
                onChanged();
              },
            ),
        ]),
        const SizedBox(height: 24),
        Text('DIAS DE ESTUDO', style: AppText.label()),
        const SizedBox(height: 4),
        Text('Um deles é o dia da revisão semanal. Os dias desmarcados são de descanso.', style: AppText.small(AppColors.dim)),
        const SizedBox(height: 10),
        Wrap(spacing: 8, runSpacing: 8, children: [
          for (var d = 1; d <= 7; d++)
            ToggleChip(
              label: kWeekdayShort[d - 1],
              selected: p.studyWeekdays.contains(d),
              color: d == p.reviewWeekday ? AppColors.amber : AppColors.gold,
              onTap: () {
                if (p.studyWeekdays.contains(d)) {
                  if (p.studyWeekdays.length <= 2) return;
                  p.studyWeekdays = [...p.studyWeekdays]..remove(d);
                  if (p.reviewWeekday == d) p.reviewWeekday = p.studyWeekdays.last;
                } else {
                  p.studyWeekdays = [...p.studyWeekdays, d]..sort();
                }
                onChanged();
              },
            ),
        ]),
        const SizedBox(height: 12),
        Row(children: [
          Text('Revisão semanal no(a): ', style: AppText.small(AppColors.text)),
          const SizedBox(width: 8),
          Flexible(child: Wrap(spacing: 6, runSpacing: 6, children: [
            for (final d in p.studyWeekdays)
              ToggleChip(
                label: kWeekdayShort[d - 1],
                selected: p.reviewWeekday == d,
                color: AppColors.amber,
                minWidth: 44,
                onTap: () {
                  p.reviewWeekday = d;
                  onChanged();
                },
              ),
          ])),
        ]),
        const SizedBox(height: 8),
        Text('$content dia(s) de conteúdo novo + 1 de revisão + ${7 - p.studyWeekdays.length} de descanso por semana.',
            style: AppText.small(AppColors.gold2)),
        const SizedBox(height: 24),
        Text('SEU NÍVEL DE BASE', style: AppText.label()),
        const SizedBox(height: 4),
        Text('Define o tempo de cada missão. Na dúvida, comece como iniciante e ajuste depois.', style: AppText.small(AppColors.dim)),
        const SizedBox(height: 10),
        Wrap(spacing: 12, runSpacing: 12, children: [
          for (var i = 0; i < 3; i++)
            ChoiceCard(
              width: 300,
              selected: p.level == i,
              onTap: () {
                p.level = i;
                onChanged();
              },
              title: catalog.levels[i],
              subtitle: lvHelp[i],
              footer: Text(lvDesc(i), style: AppText.small(AppColors.dim)),
            ),
        ]),
        const SizedBox(height: 24),
        Wrap(spacing: 24, runSpacing: 16, children: [
          _DateField(
            label: 'INÍCIO DO CICLO',
            value: p.startDate,
            first: DateTime(2024),
            last: DateTime(2035),
            onChanged: (d) {
              p.startDate = d!;
              onChanged();
            },
          ),
          _DateField(
            label: 'DATA DA PROVA (OPCIONAL)',
            value: p.examDate,
            first: today ?? DateTime(2024),
            last: DateTime(2035),
            optional: true,
            onChanged: (d) {
              p.examDate = d;
              onChanged();
            },
          ),
        ]),
      ],
    );
  }
}

class _DateField extends StatelessWidget {
  const _DateField({required this.label, required this.value, required this.first, required this.last, required this.onChanged, this.optional = false});
  final String label;
  final DateTime? value;
  final DateTime first;
  final DateTime last;
  final ValueChanged<DateTime?> onChanged;
  final bool optional;

  @override
  Widget build(BuildContext context) {
    return Column(crossAxisAlignment: CrossAxisAlignment.start, mainAxisSize: MainAxisSize.min, children: [
      Text(label, style: AppText.label()),
      const SizedBox(height: 8),
      Row(mainAxisSize: MainAxisSize.min, children: [
        OutlinedButton.icon(
          icon: const Icon(Icons.event, size: 18),
          label: Text(value == null ? 'Definir data' : '${fmtDate(value!)} · ${weekdayShort(value!)}'),
          onPressed: () async {
            final init = value ?? (DateTime.now().isBefore(first) ? first : DateTime.now());
            final d = await showDatePicker(
              context: context,
              initialDate: init.isBefore(first) ? first : (init.isAfter(last) ? last : init),
              firstDate: first,
              lastDate: last,
            );
            if (d != null) onChanged(dateOnly(d));
          },
        ),
        if (optional && value != null)
          IconButton(tooltip: 'Remover data', onPressed: () => onChanged(null), icon: const Icon(Icons.close, size: 18, color: AppColors.muted)),
      ]),
    ]);
  }
}
