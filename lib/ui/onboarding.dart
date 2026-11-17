import 'package:flutter/material.dart';

import '../core/dates.dart';
import '../core/models.dart';
import '../core/planner.dart';
import '../state/app_state.dart';
import 'profile_editors.dart';
import 'theme.dart';
import 'widgets.dart';

/// Primeiro acesso: nome → esfera → concurso → cargo → rotina → resumo do plano.
class Onboarding extends StatefulWidget {
  const Onboarding({super.key});

  @override
  State<Onboarding> createState() => _OnboardingState();
}

class _OnboardingState extends State<Onboarding> {
  int step = 0;
  final name = TextEditingController();
  final target = TextEditingController();
  late Profile draft;
  bool _init = false;

  static const steps = ['Apresentação', 'Esfera', 'Concurso', 'Cargo', 'Rotina', 'Plano'];

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    if (_init) return;
    _init = true;
    final app = AppScope.read(context);
    final today = app.today;
    draft = Profile(
      name: '',
      esfera: '',
      careerCode: '',
      optionId: '',
      hoursPerDay: 3,
      studyWeekdays: [1, 2, 3, 4, 5, 6],
      reviewWeekday: 6,
      level: 0,
      startDate: today,
    );
  }

  @override
  void dispose() {
    name.dispose();
    target.dispose();
    super.dispose();
  }

  bool get canNext => switch (step) {
        0 => name.text.trim().isNotEmpty,
        1 => draft.esfera.isNotEmpty,
        2 => draft.careerCode.isNotEmpty,
        3 => draft.optionId.isNotEmpty,
        4 => draft.contentWeekdays.isNotEmpty,
        _ => true,
      };

  void next() {
    if (!canNext) return;
    if (step < steps.length - 1) {
      setState(() => step++);
    } else {
      draft.name = name.text.trim();
      draft.targetName = target.text.trim();
      AppScope.read(context).completeOnboarding(draft);
    }
  }

  @override
  Widget build(BuildContext context) {
    final app = AppScope.of(context);
    return Scaffold(
      body: Row(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          Container(
            width: 300,
            color: AppColors.sidebar,
            child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
              const TapeBand(height: 22),
              Padding(
                padding: const EdgeInsets.fromLTRB(26, 30, 26, 30),
                child: Row(children: [
                  const BadgeLogo(size: 46),
                  const SizedBox(width: 14),
                  Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                    Text('TATICUM', style: AppText.h1(AppColors.gold2).copyWith(fontSize: 30, letterSpacing: 3, height: 1.0)),
                    Text('MENTOR POLICIAL', style: AppText.label(AppColors.muted).copyWith(fontSize: 12.6, letterSpacing: 2.2)),
                  ]),
                ]),
              ),
              for (var i = 0; i < steps.length; i++) _StepTile(index: i, label: steps[i], current: step, onTap: i < step ? () => setState(() => step = i) : null),
              const Spacer(),
              Padding(
                padding: const EdgeInsets.all(26),
                child: Text('Ciclo básico para carreiras policiais, com o método de um aprovado na PF 2025.', style: AppText.small(AppColors.dim)),
              ),
            ]),
          ),
          Expanded(
            child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
              Expanded(
                child: SingleChildScrollView(
                  padding: const EdgeInsets.fromLTRB(48, 44, 48, 32),
                  child: Align(
                    alignment: Alignment.topLeft,
                    child: ConstrainedBox(
                      constraints: const BoxConstraints(maxWidth: 1040),
                      child: AnimatedSwitcher(
                        duration: const Duration(milliseconds: 220),
                        child: KeyedSubtree(key: ValueKey(step), child: _body(app)),
                      ),
                    ),
                  ),
                ),
              ),
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 48, vertical: 16),
                decoration: const BoxDecoration(color: AppColors.panel, border: Border(top: BorderSide(color: AppColors.lineSoft))),
                child: Row(children: [
                  if (step > 0) OutlinedButton.icon(onPressed: () => setState(() => step--), icon: const Icon(Icons.arrow_back, size: 18), label: const Text('VOLTAR')),
                  const Spacer(),
                  Text('${step + 1} de ${steps.length}', style: AppText.small()),
                  const SizedBox(width: 16),
                  ElevatedButton.icon(
                    onPressed: canNext ? next : null,
                    icon: Icon(step == steps.length - 1 ? Icons.play_arrow : Icons.arrow_forward, size: 18),
                    label: Text(step == steps.length - 1 ? 'INICIAR OPERAÇÃO' : (step == 0 ? 'COMEÇAR' : 'CONTINUAR')),
                  ),
                ]),
              ),
            ]),
          ),
        ],
      ),
    );
  }

  Widget _title(String kicker, String title, String text) => Padding(
        padding: const EdgeInsets.only(bottom: 26),
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Text(kicker.toUpperCase(), style: AppText.label(AppColors.gold)),
          const SizedBox(height: 6),
          Text(title.toUpperCase(), style: AppText.h1().copyWith(fontSize: 34)),
          const SizedBox(height: 8),
          ConstrainedBox(constraints: const BoxConstraints(maxWidth: 720), child: Text(text, style: AppText.body(AppColors.muted))),
        ]),
      );

  Widget _body(AppController app) {
    final cat = app.catalog;
    switch (step) {
      case 0:
        return Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          _title('Bem-vindo', 'Seu mentor para a área policial',
              'Você escolhe o concurso e quanto tempo tem por dia. O Mentor monta as missões de cada dia, agenda as revisões e acompanha seus números — do jeito que o autor estudou para ser aprovado na Polícia Federal.'),
          const Wrap(spacing: 14, runSpacing: 14, children: [
            _Feature(Icons.flag_outlined, 'Metas, não horas', 'Cada dia tem missões claras: teoria de um assunto e um bloco de questões.'),
            _Feature(Icons.autorenew, 'Revisão automática', 'Revisão de 24 horas, semanal e de 30 dias, sem você precisar planejar.'),
            _Feature(Icons.insights_outlined, 'Seus números', 'Diário, edital verticalizado e % de acerto por matéria e por assunto.'),
          ]),
          const SizedBox(height: 34),
          SizedBox(
            width: 420,
            child: TextField(
              controller: name,
              autofocus: true,
              onChanged: (_) => setState(() {}),
              onSubmitted: (_) => next(),
              style: AppText.h3(),
              decoration: const InputDecoration(labelText: 'Como você quer ser chamado?', prefixIcon: Icon(Icons.badge_outlined)),
            ),
          ),
        ]);
      case 1:
        return Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          _title('Passo 1', 'Qual esfera?', 'Escolha onde está o concurso que você quer. Dá para mudar depois, sem perder o que já estudou.'),
          EsferaPicker(
            catalog: cat,
            value: draft.esfera.isEmpty ? null : draft.esfera,
            onChanged: (e) => setState(() {
              if (draft.esfera != e) {
                draft.careerCode = '';
                draft.optionId = '';
              }
              draft.esfera = e;
            }),
          ),
        ]);
      case 2:
        return Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          _title('Passo 2', 'Qual concurso?', 'As matérias e os pesos do ciclo vêm do núcleo comum dos últimos editais de cada carreira. Concursos com edital publicado aparecem no próximo passo.'),
          CareerPicker(
            catalog: cat,
            esfera: draft.esfera,
            value: draft.careerCode.isEmpty ? null : draft.careerCode,
            onChanged: (c) => setState(() {
              if (draft.careerCode != c) draft.optionId = '';
              draft.careerCode = c;
              final career = cat.career(c);
              if (career.cargos.length == 1) selectOption(cat, draft, career.cargos.first.id, today: app.today);
            }),
          ),
          const SizedBox(height: 26),
          SizedBox(
            width: 420,
            child: TextField(
              controller: target,
              decoration: const InputDecoration(labelText: 'Concurso específico (opcional)', hintText: 'Ex.: PF 2027, PCDF, PM-SP'),
            ),
          ),
        ]);
      case 3:
        final career = cat.career(draft.careerCode);
        return Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          _title('Passo 3', 'Qual cargo?', 'Cada cargo tem pesos próprios. Matérias de peso alto entram no 1º dia; as demais entram aos poucos.'),
          CargoPicker(
            catalog: cat,
            career: career,
            value: draft.optionId.isEmpty ? null : draft.optionId,
            onChanged: (o) => setState(() {
              selectOption(cat, draft, o, today: app.today);
              target.text = draft.targetName;
            }),
          ),
        ]);
      case 4:
        return Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          _title('Passo 4', 'Sua rotina', 'As metas são calculadas pelo seu tempo e pelo seu nível — nada de metas impossíveis.'),
          RoutineEditor(catalog: cat, profile: draft, today: app.today, onChanged: () => setState(() {})),
        ]);
      default:
        return _summary(app);
    }
  }

  Widget _summary(AppController app) {
    final cat = app.catalog;
    final trail = Planner.buildTrail(cat, draft, const {});
    final sched = Schedule(catalog: cat, trail: trail, profile: draft, data: UserData(profile: draft, anchorDate: draft.startDate), today: draft.startDate);
    final first = sched.dayPlan(sched.studyDates.isEmpty ? draft.startDate : sched.studyDates.first);
    final end = sched.endDate;
    final weeks = end == null ? 0 : daysBetween(draft.startDate, end) ~/ 7 + 1;
    final career = cat.career(draft.careerCode);
    return Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
      _title('Passo 5', 'Seu plano de operação', 'Confira o resumo. Tudo pode ser ajustado depois em AJUSTES — o cronograma se recalcula sozinho.'),
      Wrap(spacing: 14, runSpacing: 14, children: [
        SizedBox(width: 220, child: KpiTile(label: 'Missões', value: '${trail.units.length}', sub: '${trail.activeTopics.length} assuntos do edital')),
        SizedBox(width: 220, child: KpiTile(label: 'Carga do ciclo', value: '${(trail.totalMinutes / 60).round()} h', sub: 'teoria + questões')),
        SizedBox(width: 220, child: KpiTile(label: '1ª volta', value: '$weeks sem', sub: end == null ? '' : 'até ${fmtDate(end)}', color: AppColors.gold2)),
        SizedBox(width: 220, child: KpiTile(label: 'Por dia', value: fmtHours(draft.hoursPerDay), sub: '${draft.contentWeekdays.length} dias de conteúdo/semana')),
      ]),
      const SizedBox(height: 22),
      Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
        Expanded(
          flex: 5,
          child: Panel(
            child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              const SectionLabel('Ordem de entrada das matérias'),
              for (final sp in trail.subjects)
                Padding(
                  padding: const EdgeInsets.symmetric(vertical: 5),
                  child: Row(children: [
                    Container(width: 8, height: 8, decoration: BoxDecoration(color: AppColors.hex(sp.subject.colorHex), shape: BoxShape.circle)),
                    const SizedBox(width: 10),
                    Expanded(child: Text(sp.subject.name, style: AppText.body(), overflow: TextOverflow.ellipsis)),
                    Dots(sp.weight),
                    const SizedBox(width: 10),
                    SizedBox(width: 90, child: Text(sp.entry, style: AppText.small(sp.weight >= 3 ? AppColors.gold2 : AppColors.muted))),
                  ]),
                ),
            ]),
          ),
        ),
        const SizedBox(width: 16),
        Expanded(
          flex: 4,
          child: Panel(
            accent: AppColors.gold,
            child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              SectionLabel('Missões do 1º dia · ${fmtDate(first.date)}'),
              for (final u in first.units)
                Padding(
                  padding: const EdgeInsets.only(bottom: 10),
                  child: Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
                    Text('#${u.seq}', style: AppText.h3(AppColors.gold)),
                    const SizedBox(width: 10),
                    Expanded(
                      child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                        Text('${u.subject.name} · ${u.title}', style: AppText.strong()),
                        Text('${u.topic.name} · ${minutesLabel(u.minutes)}', style: AppText.small()),
                      ]),
                    ),
                  ]),
                ),
              const SizedBox(height: 4),
              Text('+ revisão de 24h e 10 min de lei seca todos os dias.', style: AppText.small(AppColors.teal)),
              const SizedBox(height: 14),
              Text('${career.code} · ${cat.cargo(draft.optionId).name}', style: AppText.small(AppColors.dim)),
            ]),
          ),
        ),
      ]),
    ]);
  }
}

class _Feature extends StatelessWidget {
  const _Feature(this.icon, this.title, this.text);
  final IconData icon;
  final String title;
  final String text;
  @override
  Widget build(BuildContext context) => SizedBox(
        width: 300,
        child: Panel(
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Icon(icon, color: AppColors.gold, size: 26),
            const SizedBox(height: 10),
            Text(title.toUpperCase(), style: AppText.h3()),
            const SizedBox(height: 4),
            Text(text, style: AppText.small()),
          ]),
        ),
      );
}

class _StepTile extends StatelessWidget {
  const _StepTile({required this.index, required this.label, required this.current, this.onTap});
  final int index;
  final String label;
  final int current;
  final VoidCallback? onTap;

  @override
  Widget build(BuildContext context) {
    final done = index < current, active = index == current;
    final color = active ? AppColors.gold2 : (done ? AppColors.green : AppColors.dim);
    return InkWell(
      onTap: onTap,
      child: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 26, vertical: 10),
        child: Row(children: [
          Container(
            width: 26,
            height: 26,
            alignment: Alignment.center,
            decoration: BoxDecoration(
              shape: BoxShape.circle,
              color: active ? AppColors.gold : Colors.transparent,
              border: Border.all(color: color, width: 1.5),
            ),
            child: done
                ? const Icon(Icons.check, size: 15, color: AppColors.green)
                : Text('${index + 1}', style: AppText.h3(active ? AppColors.bg : color).copyWith(fontSize: 13)),
          ),
          const SizedBox(width: 12),
          Text(label.toUpperCase(), style: AppText.h3(active ? AppColors.text : (done ? AppColors.muted : AppColors.dim)).copyWith(fontSize: 15)),
        ]),
      ),
    );
  }
}
