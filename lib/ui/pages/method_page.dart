import 'package:flutter/material.dart';

import '../charts.dart';
import '../theme.dart';
import '../widgets.dart';

/// Diário do autor (Agente PF 2025, 457º AC): questões e acertos por ciclo semanal.
const _cycles = [
  (165, 142), (338, 277), (304, 247), (357, 286), (522, 418), (534, 451), (596, 491), (531, 425),
  (368, 310), (526, 430), (377, 306), (558, 466), (297, 234), (533, 437), (1028, 871), (1207, 1024),
  (872, 746), (805, 667), (553, 449), (716, 597), (1717, 1385), (940, 780), (1115, 931), (791, 688),
];

const _phaseColors = [Color(0xFF6B7A93), Color(0xFF5B9BFF), AppColors.gold];

class MethodPage extends StatelessWidget {
  const MethodPage({super.key});

  @override
  Widget build(BuildContext context) {
    const tiles = [
      ('Dias de estudo', '169', '08/02 → 27/07/2025'),
      ('Questões', '16.065', '95 por dia'),
      ('Acerto', '83%', '79% a 87% por ciclo'),
      ('Dias com 100+', '69', '18 com 200 ou mais'),
      ('Simulados', '17', '37 → 101 pontos'),
      ('Descanso', '4 dias', 'planejados'),
    ];
    const phases = [
      ('FASE 1 · FUNDAÇÃO', 'Ciclos 1 a 6', 'Uma matéria por dia. Revisão do dia anterior e revisão semanal. Só Português, Informática e Contabilidade.'),
      ('FASE 2 · METAS', 'Ciclos 7 a 14', 'Meta do dia: estudo + revisão + questões. Simulados com meta de nota.'),
      ('FASE 3 · PÓS-EDITAL', 'Ciclos 15 a 24', 'Todas as matérias, 2,4× mais questões e simulados quase semanais.'),
    ];
    const lessons = [
      ('Metas, não horas', 'Do ciclo 7 em diante, todo dia tinha uma meta: "ler 2 PDFs + 60 questões".', 'MISSÕES calcula as metas pelas suas horas e pelo seu nível.'),
      ('Poucas matérias no início', '6 semanas só com Português, Informática e Contabilidade.', 'Peso 3 começa no dia 1; peso 2 após 40 h; peso 1 após 100 h.'),
      ('Revisão 24h · 7 dias · 30 dias', 'Revisão do dia anterior em 101 dias; revisão completa todo 7º dia.', 'Revisão 24h diária, dia de revisão semanal e revisão de 30 dias.'),
      ('Questão todo dia', '16.065 questões; 69 dias com 100 ou mais.', 'Toda teoria é seguida de 15, 25 ou 40 questões.'),
      ('Acerto estável perto de 80%', '79% a 87% por ciclo, mesmo com volume 2,4× maior.', 'EDITAL marca "Reforçar" abaixo de 70%.'),
      ('Simulado com meta de nota', '37 pontos líquidos no 1º; 81 a 101 nos 3 últimos.', 'Simulado ou mini-simulado quinzenal a partir da semana 4.'),
      ('Erro vira plano', 'Lista "reestudar" por matéria; dias só com questões erradas.', 'Caderno de erros semanal e observações no DIÁRIO.'),
      ('Lei seca em doses', '17 dias de leitura, 315 questões, 86% de acerto.', '60 leituras de 10 minutos, em rodízio.'),
      ('Núcleo policial comum', 'Na reta final: provas de PCDF, PCPE, PCRO, PCAL, PRF e GCM.', 'Um edital para 8 carreiras, com pesos por cargo.'),
      ('Constância, descanso e TAF', '4 descansos planejados; TAF 11 semanas antes da prova.', 'Descanso semanal e replanejamento automático.'),
    ];

    return ListView(padding: const EdgeInsets.only(bottom: 36), children: [
      const PageHeader(
        title: 'Método',
        subtitle: 'Como o autor estudou para a Polícia Federal 2025 (Agente, 457º na ampla concorrência) — e como o app aplica isso no seu dia.',
      ),
      Padding(
        padding: const EdgeInsets.symmetric(horizontal: 28),
        child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
          const TapeBand(text: 'OS NÚMEROS DA APROVAÇÃO   //   AGENTE PF 2025   //   ', height: 24),
          const SizedBox(height: 14),
          LayoutBuilder(builder: (context, c) {
            final per = c.maxWidth > 1100 ? 6 : 3;
            final w = (c.maxWidth - 12 * (per - 1)) / per;
            return Wrap(spacing: 12, runSpacing: 12, children: [
              for (var i = 0; i < tiles.length; i++)
                SizedBox(
                  width: w,
                  child: KpiTile(label: tiles[i].$1, value: tiles[i].$2, sub: tiles[i].$3, color: i == 1 || i == 2 ? AppColors.gold2 : AppColors.text),
                ),
            ]);
          }),
          const SizedBox(height: 16),
          Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
            for (var i = 0; i < phases.length; i++) ...[
              if (i > 0) const SizedBox(width: 12),
              Expanded(
                child: Panel(
                  accent: _phaseColors[i],
                  child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                    Text(phases[i].$1, style: AppText.h3(_phaseColors[i])),
                    Text(phases[i].$2, style: AppText.small(AppColors.dim)),
                    const SizedBox(height: 8),
                    Text(phases[i].$3, style: AppText.body()),
                  ]),
                ),
              ),
            ],
          ]),
          const SizedBox(height: 16),
          Panel(
            child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
              const SectionLabel('Questões por ciclo semanal · cor = fase · linha = % de acerto'),
              BarLineChart(
                height: 240,
                points: [
                  for (var i = 0; i < _cycles.length; i++)
                    ChartPoint('C${i + 1}', _cycles[i].$1.toDouble(), rate: _cycles[i].$2 / _cycles[i].$1, color: _phaseColors[i < 6 ? 0 : (i < 14 ? 1 : 2)]),
                ],
              ),
              const SizedBox(height: 6),
              Text('Fonte: planilha de estudos do autor. Ciclos 15 a 24 = pós-edital (fora do escopo do ciclo básico).', style: AppText.small(AppColors.dim)),
            ]),
          ),
          const SizedBox(height: 16),
          Panel(
            padding: const EdgeInsets.fromLTRB(18, 18, 18, 8),
            child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
              const SectionLabel('10 lições do método'),
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                child: Row(children: [
                  const SizedBox(width: 48),
                  Expanded(flex: 3, child: Text('LIÇÃO', style: AppText.label(AppColors.gold))),
                  Expanded(flex: 4, child: Text('O QUE O DIÁRIO MOSTRA', style: AppText.label(AppColors.gold))),
                  Expanded(flex: 4, child: Text('NO APP', style: AppText.label(AppColors.gold))),
                ]),
              ),
              const Divider(color: AppColors.gold),
              for (var i = 0; i < lessons.length; i++)
                Container(
                  padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 12),
                  decoration: const BoxDecoration(border: Border(bottom: BorderSide(color: AppColors.lineSoft))),
                  child: Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
                    SizedBox(width: 48, child: Text((i + 1).toString().padLeft(2, '0'), style: AppText.h2(AppColors.gold))),
                    Expanded(flex: 3, child: Text(lessons[i].$1, style: AppText.strong())),
                    Expanded(flex: 4, child: Padding(padding: const EdgeInsets.only(right: 12), child: Text(lessons[i].$2, style: AppText.body(AppColors.muted)))),
                    Expanded(flex: 4, child: Text(lessons[i].$3, style: AppText.body(AppColors.blue))),
                  ]),
                ),
            ]),
          ),
        ]),
      ),
    ]);
  }
}
