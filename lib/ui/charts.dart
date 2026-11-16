import 'dart:math' as math;

import 'package:flutter/material.dart';

import 'theme.dart';

class ChartPoint {
  const ChartPoint(this.label, this.value, {this.rate, this.color});
  final String label;
  final double value;

  /// 0..1 (linha de % de acerto). null = sem dado.
  final double? rate;
  final Color? color;
}

/// Barras (volume) + linha (% de acerto, eixo à direita).
class BarLineChart extends StatelessWidget {
  const BarLineChart({super.key, required this.points, this.height = 200, this.barColor = AppColors.gold, this.valueSuffix = ''});
  final List<ChartPoint> points;
  final double height;
  final Color barColor;
  final String valueSuffix;

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: height,
      width: double.infinity,
      child: CustomPaint(painter: _BarLinePainter(points, barColor)),
    );
  }
}

class _BarLinePainter extends CustomPainter {
  _BarLinePainter(this.points, this.barColor);
  final List<ChartPoint> points;
  final Color barColor;

  TextPainter _tp(String s, double size, Color c, {FontWeight w = FontWeight.w500}) {
    final tp = TextPainter(
      text: TextSpan(text: s, style: TextStyle(fontFamily: AppText.fDisplay, fontSize: size, color: c, fontWeight: w)),
      textDirection: TextDirection.ltr,
    )..layout();
    return tp;
  }

  @override
  void paint(Canvas canvas, Size size) {
    if (points.isEmpty) return;
    const left = 34.0, right = 34.0, top = 12.0, bottom = 22.0;
    final w = size.width - left - right, h = size.height - top - bottom;
    final maxV = math.max(1.0, points.map((p) => p.value).reduce(math.max));
    final nice = _niceMax(maxV);
    final grid = Paint()
      ..color = AppColors.lineSoft
      ..strokeWidth = 1;
    for (var i = 0; i <= 4; i++) {
      final y = top + h - h * i / 4;
      canvas.drawLine(Offset(left, y), Offset(left + w, y), grid);
      final tp = _tp(_fmt(nice * i / 4), 10.5, AppColors.dim);
      tp.paint(canvas, Offset(left - tp.width - 6, y - tp.height / 2));
      final rp = _tp('${25 * i}%', 10.5, AppColors.dim);
      rp.paint(canvas, Offset(left + w + 6, y - rp.height / 2));
    }
    final n = points.length;
    final slot = w / n;
    final bw = math.min(26.0, slot * 0.62);
    final every = (n / 12).ceil();
    for (var i = 0; i < n; i++) {
      final p = points[i];
      final bh = h * (p.value / nice);
      final x = left + slot * i + (slot - bw) / 2;
      final r = RRect.fromRectAndCorners(Rect.fromLTWH(x, top + h - bh, bw, bh), topLeft: const Radius.circular(3), topRight: const Radius.circular(3));
      canvas.drawRRect(r, Paint()..color = p.color ?? barColor);
      if (i % every == 0 || i == n - 1) {
        final tp = _tp(p.label, 10.5, AppColors.muted);
        tp.paint(canvas, Offset(left + slot * i + slot / 2 - tp.width / 2, top + h + 5));
      }
    }
    final line = Paint()
      ..color = AppColors.text
      ..strokeWidth = 2
      ..style = PaintingStyle.stroke;
    final path = Path();
    var started = false;
    final dots = <Offset>[];
    for (var i = 0; i < n; i++) {
      final r = points[i].rate;
      if (r == null) continue;
      final pt = Offset(left + slot * i + slot / 2, top + h - h * r.clamp(0.0, 1.0));
      if (!started) {
        path.moveTo(pt.dx, pt.dy);
        started = true;
      } else {
        path.lineTo(pt.dx, pt.dy);
      }
      dots.add(pt);
    }
    canvas.drawPath(path, line);
    for (final d in dots) {
      canvas.drawCircle(d, 3.2, Paint()..color = AppColors.bg);
      canvas.drawCircle(d, 3.2, line..strokeWidth = 1.8);
    }
  }

  double _niceMax(double v) {
    final exp = math.pow(10, (math.log(v) / math.ln10).floor()).toDouble();
    for (final m in [1, 2, 2.5, 5, 10]) {
      if (m * exp >= v) return m * exp;
    }
    return 10 * exp;
  }

  String _fmt(double v) => v >= 1000 ? '${(v / 1000).toStringAsFixed(v % 1000 == 0 ? 0 : 1)}k' : v.toStringAsFixed(0);

  @override
  bool shouldRepaint(covariant _BarLinePainter old) => old.points != points;
}

/// Anel de progresso com conteúdo no centro.
class ProgressRing extends StatelessWidget {
  const ProgressRing({super.key, required this.value, this.size = 120, this.color = AppColors.gold, this.stroke = 10, this.child});
  final double value;
  final double size;
  final Color color;
  final double stroke;
  final Widget? child;

  @override
  Widget build(BuildContext context) => SizedBox(
        width: size,
        height: size,
        child: CustomPaint(
          painter: _RingPainter(value.isNaN ? 0 : value.clamp(0.0, 1.0), color, stroke),
          child: Center(child: child),
        ),
      );
}

class _RingPainter extends CustomPainter {
  _RingPainter(this.value, this.color, this.stroke);
  final double value;
  final Color color;
  final double stroke;

  @override
  void paint(Canvas canvas, Size size) {
    final rect = Offset.zero & size;
    final r = rect.deflate(stroke / 2);
    canvas.drawArc(r, 0, math.pi * 2, false,
        Paint()
          ..color = AppColors.field
          ..style = PaintingStyle.stroke
          ..strokeWidth = stroke);
    canvas.drawArc(r, -math.pi / 2, math.pi * 2 * value, false,
        Paint()
          ..color = color
          ..style = PaintingStyle.stroke
          ..strokeCap = StrokeCap.round
          ..strokeWidth = stroke);
  }

  @override
  bool shouldRepaint(covariant _RingPainter old) => old.value != value || old.color != color;
}
