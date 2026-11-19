import 'dart:math' as math;

import 'package:flutter/foundation.dart' show kIsWeb;
import 'package:flutter/material.dart';

import '../core/catalog.dart';
import '../core/stats.dart';
import 'theme.dart';

/// Cartão base do app.
class Panel extends StatelessWidget {
  const Panel({super.key, required this.child, this.padding = const EdgeInsets.all(18), this.color, this.borderColor, this.accent});

  final Widget child;
  final EdgeInsetsGeometry padding;
  final Color? color;
  final Color? borderColor;

  /// Faixa colorida no topo do cartão.
  final Color? accent;

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        color: color ?? AppColors.panel,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: borderColor ?? AppColors.lineSoft),
      ),
      clipBehavior: Clip.antiAlias,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        mainAxisSize: MainAxisSize.min,
        children: [
          if (accent != null) Container(height: 3, color: accent),
          Padding(padding: padding, child: child),
        ],
      ),
    );
  }
}

/// Rótulo de seção: quadradinho dourado + texto em caixa alta.
class SectionLabel extends StatelessWidget {
  const SectionLabel(this.text, {super.key, this.trailing, this.color = AppColors.gold});
  final String text;
  final Widget? trailing;
  final Color color;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 12),
      child: Row(
        children: [
          Container(width: 4, height: 16, color: color),
          const SizedBox(width: 10),
          Expanded(child: Text(text.toUpperCase(), style: AppText.label(AppColors.text).copyWith(fontSize: 14))),
          if (trailing != null) trailing!,
        ],
      ),
    );
  }
}

class PageHeader extends StatelessWidget {
  const PageHeader({super.key, required this.title, this.subtitle, this.actions = const []});
  final String title;
  final String? subtitle;
  final List<Widget> actions;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.fromLTRB(28, 22, 28, 14),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.end,
        children: [
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(title.toUpperCase(), style: AppText.h1()),
                if (subtitle != null) ...[
                  const SizedBox(height: 4),
                  Text(subtitle!, style: AppText.small(), maxLines: 2, overflow: TextOverflow.ellipsis),
                ],
              ],
            ),
          ),
          for (final a in actions) Padding(padding: const EdgeInsets.only(left: 10), child: a),
        ],
      ),
    );
  }
}

class KpiTile extends StatelessWidget {
  const KpiTile({super.key, required this.label, required this.value, this.sub, this.color = AppColors.text, this.icon});
  final String label;
  final String value;
  final String? sub;
  final Color color;
  final IconData? icon;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.fromLTRB(16, 14, 16, 14),
      decoration: BoxDecoration(
        color: AppColors.panel,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: AppColors.lineSoft),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        mainAxisSize: MainAxisSize.min,
        children: [
          Row(children: [
            if (icon != null) ...[Icon(icon, size: 15, color: AppColors.muted), const SizedBox(width: 6)],
            Expanded(child: Text(label.toUpperCase(), style: AppText.label(), overflow: TextOverflow.ellipsis)),
          ]),
          const SizedBox(height: 10),
          FittedBox(fit: BoxFit.scaleDown, alignment: Alignment.centerLeft, child: Text(value, style: AppText.kpi(color))),
          const SizedBox(height: 6),
          Container(height: 2, width: 28, color: AppColors.gold),
          if (sub != null) ...[
            const SizedBox(height: 6),
            Text(sub!, style: AppText.small(), maxLines: 1, overflow: TextOverflow.ellipsis),
          ],
        ],
      ),
    );
  }
}

class Pill extends StatelessWidget {
  const Pill(this.text, {super.key, this.color = AppColors.muted, this.filled = false, this.icon});
  final String text;
  final Color color;
  final bool filled;
  final IconData? icon;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
      decoration: BoxDecoration(
        color: filled ? color : color.withValues(alpha: 0.12),
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: color.withValues(alpha: filled ? 1 : 0.45)),
      ),
      child: Row(mainAxisSize: MainAxisSize.min, children: [
        if (icon != null) ...[Icon(icon, size: 12, color: filled ? AppColors.bg : color), const SizedBox(width: 4)],
        Text(text, style: AppText.label(filled ? AppColors.bg : color).copyWith(fontSize: 11.5, letterSpacing: 0.6)),
      ]),
    );
  }
}

class SubjectTag extends StatelessWidget {
  const SubjectTag(this.subject, {super.key, this.long = false});
  final Subject subject;
  final bool long;

  @override
  Widget build(BuildContext context) => Pill(long ? subject.name : subject.id, color: AppColors.hex(subject.colorHex));
}

Color statusColor(TopicStatus s) => switch (s) {
      TopicStatus.outOfCycle => AppColors.dim,
      TopicStatus.toStudy => AppColors.muted,
      TopicStatus.inProgress => AppColors.blue,
      TopicStatus.reinforce => AppColors.red,
      TopicStatus.consolidated => AppColors.green,
    };

class StatusPill extends StatelessWidget {
  const StatusPill(this.status, {super.key});
  final TopicStatus status;
  @override
  Widget build(BuildContext context) => Pill(
        status.label,
        color: statusColor(status),
        icon: switch (status) {
          TopicStatus.reinforce => Icons.priority_high,
          TopicStatus.consolidated => Icons.verified_outlined,
          TopicStatus.inProgress => Icons.trending_up,
          _ => null,
        },
      );
}

class Dots extends StatelessWidget {
  const Dots(this.value, {super.key, this.max = 3, this.color = AppColors.gold});
  final int value;
  final int max;
  final Color color;
  @override
  Widget build(BuildContext context) => Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          for (var i = 0; i < max; i++)
            Container(
              width: 8,
              height: 8,
              margin: const EdgeInsets.only(right: 3),
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                color: i < value ? color : Colors.transparent,
                border: Border.all(color: i < value ? color : AppColors.dim),
              ),
            ),
        ],
      );
}

class Bar extends StatelessWidget {
  const Bar(this.value, {super.key, this.color = AppColors.gold, this.height = 6});
  final double value;
  final Color color;
  final double height;
  @override
  Widget build(BuildContext context) => ClipRRect(
        borderRadius: BorderRadius.circular(height),
        child: SizedBox(
          height: height,
          child: Stack(fit: StackFit.expand, children: [
            Container(color: AppColors.field),
            FractionallySizedBox(
              alignment: Alignment.centerLeft,
              widthFactor: value.isNaN ? 0 : value.clamp(0.0, 1.0),
              child: Container(color: color),
            ),
          ]),
        ),
      );
}

/// Faixa de isolamento policial com texto repetido.
class TapeBand extends StatelessWidget {
  const TapeBand({super.key, this.text = 'TATICUM   //   CICLO BÁSICO   //   ', this.height = 26});
  final String text;
  final double height;
  @override
  Widget build(BuildContext context) {
    return Container(
      height: height,
      color: AppColors.gold2,
      alignment: Alignment.centerLeft,
      child: ClipRect(
        child: OverflowBox(
          alignment: Alignment.centerLeft,
          maxWidth: double.infinity,
          child: Text(
            List.filled(12, text).join(),
            maxLines: 1,
            softWrap: false,
            style: TextStyle(fontFamily: AppText.fDisplay, fontWeight: FontWeight.w700, fontSize: height * 0.48, letterSpacing: 1.2, color: AppColors.bg),
          ),
        ),
      ),
    );
  }
}

/// Distintivo do app (escudo + estrela), desenhado em código.
class BadgeLogo extends StatelessWidget {
  const BadgeLogo({super.key, this.size = 40});
  final double size;
  @override
  Widget build(BuildContext context) => SizedBox(width: size, height: size * 1.12, child: CustomPaint(painter: _BadgePainter()));
}

class _BadgePainter extends CustomPainter {
  @override
  void paint(Canvas canvas, Size s) {
    final w = s.width, h = s.height;
    Path shield(double inset) {
      final p = Path();
      p.moveTo(w / 2, inset);
      p.lineTo(w - inset, h * 0.16 + inset * 0.6);
      p.lineTo(w - inset, h * 0.52);
      p.quadraticBezierTo(w - inset, h * 0.82, w / 2, h - inset);
      p.quadraticBezierTo(inset, h * 0.82, inset, h * 0.52);
      p.lineTo(inset, h * 0.16 + inset * 0.6);
      p.close();
      return p;
    }

    canvas.drawPath(shield(0), Paint()..color = AppColors.gold);
    canvas.drawPath(shield(w * 0.08), Paint()..color = AppColors.bg);
    canvas.drawPath(
      shield(w * 0.14),
      Paint()
        ..color = AppColors.gold
        ..style = PaintingStyle.stroke
        ..strokeWidth = w * 0.025,
    );
    final cx = w / 2, cy = h * 0.47, r = w * 0.24;
    final star = Path();
    for (var i = 0; i < 10; i++) {
      final a = -math.pi / 2 + i * math.pi / 5;
      final rr = i.isEven ? r : r * 0.42;
      final pt = Offset(cx + rr * math.cos(a), cy + rr * math.sin(a));
      if (i == 0) {
        star.moveTo(pt.dx, pt.dy);
      } else {
        star.lineTo(pt.dx, pt.dy);
      }
    }
    star.close();
    canvas.drawPath(star, Paint()..color = AppColors.gold2);
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) => false;
}

/// Texto com **negrito** simples.
class RichMd extends StatelessWidget {
  const RichMd(this.text, {super.key, this.style, this.boldColor});
  final String text;
  final TextStyle? style;
  final Color? boldColor;

  @override
  Widget build(BuildContext context) {
    final base = style ?? AppText.body();
    return Text.rich(TextSpan(style: base, children: mdSpans(text, base, boldColor: boldColor)));
  }
}

/// *exemplo* (itálico, pode conter **negrito**) e **negrito**.
/// "neste computador" no app instalado, "neste navegador" na versão web.
const String kNeste = kIsWeb ? 'neste navegador' : 'neste computador';
const String kDeste = kIsWeb ? 'deste navegador' : 'deste computador';
const String kDESTE = kIsWeb ? 'DESTE NAVEGADOR' : 'DESTE COMPUTADOR';

final _italicRe = RegExp(r'(?<!\*)\*(?=[^*]|\*\*[^*])((?:\*\*[^*]+?\*\*|[^*])+?)\*(?!\*)');
final _boldRe = RegExp(r'\*\*(.+?)\*\*');

List<InlineSpan> mdSpans(String text, TextStyle base, {Color? boldColor}) {
  final spans = <InlineSpan>[];
  void bold(String t, TextStyle style) {
    var last = 0;
    for (final m in _boldRe.allMatches(t)) {
      if (m.start > last) spans.add(TextSpan(text: t.substring(last, m.start), style: style));
      spans.add(TextSpan(text: m.group(1), style: style.copyWith(fontWeight: FontWeight.w700, color: boldColor ?? style.color)));
      last = m.end;
    }
    if (last < t.length) spans.add(TextSpan(text: t.substring(last), style: style));
  }

  var last = 0;
  final italic = base.copyWith(fontStyle: FontStyle.italic);
  for (final m in _italicRe.allMatches(text)) {
    if (m.start > last) bold(text.substring(last, m.start), base);
    bold(m.group(1)!, italic);
    last = m.end;
  }
  if (last < text.length) bold(text.substring(last), base);
  return spans;
}

class EmptyState extends StatelessWidget {
  const EmptyState({super.key, required this.icon, required this.title, required this.text, this.action});
  final IconData icon;
  final String title;
  final String text;
  final Widget? action;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 36, horizontal: 20),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          Icon(icon, size: 40, color: AppColors.dim),
          const SizedBox(height: 12),
          Text(title.toUpperCase(), style: AppText.h3(AppColors.muted), textAlign: TextAlign.center),
          const SizedBox(height: 6),
          ConstrainedBox(
            constraints: const BoxConstraints(maxWidth: 440),
            child: Text(text, style: AppText.small(), textAlign: TextAlign.center),
          ),
          if (action != null) ...[const SizedBox(height: 16), action!],
        ],
      ),
    );
  }
}

/// Seletor em "cartões" grandes (usado no onboarding e nas configurações).
class ChoiceCard extends StatelessWidget {
  const ChoiceCard({
    super.key,
    required this.selected,
    required this.onTap,
    required this.title,
    this.subtitle,
    this.color = AppColors.gold,
    this.leading,
    this.footer,
    this.width,
  });

  final bool selected;
  final VoidCallback onTap;
  final String title;
  final String? subtitle;
  final Color color;
  final Widget? leading;
  final Widget? footer;
  final double? width;

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: width,
      child: Material(
        color: selected ? color.withValues(alpha: 0.14) : AppColors.panel,
        borderRadius: BorderRadius.circular(12),
        child: InkWell(
          onTap: onTap,
          borderRadius: BorderRadius.circular(12),
          child: Container(
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(
              borderRadius: BorderRadius.circular(12),
              border: Border.all(color: selected ? color : AppColors.lineSoft, width: selected ? 1.6 : 1),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              mainAxisSize: MainAxisSize.min,
              children: [
                Row(children: [
                  if (leading != null) ...[leading!, const SizedBox(width: 10)],
                  Expanded(child: Text(title.toUpperCase(), style: AppText.h3(selected ? AppColors.gold2 : AppColors.text))),
                  Icon(selected ? Icons.radio_button_checked : Icons.radio_button_off, size: 18, color: selected ? color : AppColors.dim),
                ]),
                if (subtitle != null) ...[const SizedBox(height: 6), Text(subtitle!, style: AppText.small())],
                if (footer != null) ...[const SizedBox(height: 10), footer!],
              ],
            ),
          ),
        ),
      ),
    );
  }
}

/// Botão-chip selecionável (horas, dias da semana, tamanhos).
class ToggleChip extends StatelessWidget {
  const ToggleChip({super.key, required this.label, required this.selected, required this.onTap, this.color = AppColors.gold, this.minWidth = 52});
  final String label;
  final bool selected;
  final VoidCallback? onTap;
  final Color color;
  final double minWidth;

  @override
  Widget build(BuildContext context) {
    return Material(
      color: selected ? color : AppColors.field,
      borderRadius: BorderRadius.circular(8),
      child: InkWell(
        onTap: onTap,
        borderRadius: BorderRadius.circular(8),
        child: Container(
          constraints: BoxConstraints(minWidth: minWidth),
          padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 9),
          decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(8),
            border: Border.all(color: selected ? color : AppColors.line),
          ),
          child: Text(
            label,
            textAlign: TextAlign.center,
            style: TextStyle(
              fontFamily: AppText.fDisplay,
              fontWeight: FontWeight.w700,
              fontSize: 14,
              letterSpacing: 0.5,
              color: selected ? AppColors.bg : (onTap == null ? AppColors.dim : AppColors.text),
            ),
          ),
        ),
      ),
    );
  }
}

String pct(double? v, {int digits = 0}) => v == null ? '—' : '${(v * 100).toStringAsFixed(digits)}%';

String thousands(int n) {
  final s = n.abs().toString();
  final b = StringBuffer();
  for (var i = 0; i < s.length; i++) {
    if (i > 0 && (s.length - i) % 3 == 0) b.write('.');
    b.write(s[i]);
  }
  return n < 0 ? '-$b' : b.toString();
}

String minutesLabel(int m) {
  if (m < 60) return '$m min';
  final h = m ~/ 60, r = m % 60;
  return r == 0 ? '${h}h' : '${h}h${r.toString().padLeft(2, '0')}';
}

Future<void> toast(BuildContext context, String msg) async {
  ScaffoldMessenger.of(context)
    ..hideCurrentSnackBar()
    ..showSnackBar(SnackBar(content: Text(msg), width: 520, duration: const Duration(seconds: 3)));
}
