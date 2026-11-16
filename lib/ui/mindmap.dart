import 'package:flutter/material.dart';

import '../data/content.dart';
import 'theme.dart';

const _branchColors = [
  Color(0xFF5B9BFF),
  Color(0xFF34D399),
  Color(0xFFA78BFA),
  Color(0xFFFB923C),
  Color(0xFFF87171),
  Color(0xFF22D3EE),
  Color(0xFFFBBF24),
  Color(0xFF94A3B8),
  Color(0xFFF472B6),
  Color(0xFF4ADE80),
];

/// Mapa mental em duas colunas, desenhado a partir do JSON do material. Pode ser ampliado.
class MindMapView extends StatelessWidget {
  const MindMapView({super.key, required this.spec});
  final MindMapSpec spec;

  static const double canvasW = 1100;

  double get canvasH {
    double col(List<MindBranch> bs) => bs.fold<double>(0, (a, b) => a + 44 + 21.0 * b.items.length) + 16.0 * (bs.length - 1);
    final h = [col(spec.left), col(spec.right)].reduce((a, b) => a > b ? a : b);
    return h + 40;
  }

  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(builder: (context, c) {
      final scale = (c.maxWidth / canvasW).clamp(0.4, 1.0);
      return ClipRRect(
        borderRadius: BorderRadius.circular(12),
        child: Container(
          color: AppColors.sidebar,
          height: canvasH * scale + 8,
          child: InteractiveViewer(
            minScale: 1,
            maxScale: 3,
            child: Center(
              child: SizedBox(
                width: canvasW * scale,
                height: canvasH * scale,
                child: FittedBox(
                  child: SizedBox(width: canvasW, height: canvasH, child: CustomPaint(painter: _MindPainter(spec))),
                ),
              ),
            ),
          ),
        ),
      );
    });
  }
}

class _MindPainter extends CustomPainter {
  _MindPainter(this.spec);
  final MindMapSpec spec;

  TextPainter _tp(String s, TextStyle st, {double? maxW}) =>
      TextPainter(text: TextSpan(text: s, style: st), textDirection: TextDirection.ltr, maxLines: 1, ellipsis: '…')..layout(maxWidth: maxW ?? 2000);

  @override
  void paint(Canvas canvas, Size size) {
    final w = size.width, h = size.height;
    final cx = w / 2, cy = h / 2;
    const rw = 250.0, rh = 96.0, bw = 330.0, gap = 16.0;

    List<(Rect, MindBranch)> layout(List<MindBranch> bs, double x) {
      final hs = [for (final b in bs) 44 + 21.0 * b.items.length];
      final total = hs.fold<double>(0, (a, b) => a + b) + gap * (bs.length - 1);
      var y = cy - total / 2;
      final out = <(Rect, MindBranch)>[];
      for (var i = 0; i < bs.length; i++) {
        out.add((Rect.fromLTWH(x, y, bw, hs[i]), bs[i]));
        y += hs[i] + gap;
      }
      return out;
    }

    final left = layout(spec.left, 10);
    final right = layout(spec.right, w - bw - 10);
    final all = [...left, ...right];

    for (var i = 0; i < all.length; i++) {
      final (r, _) = all[i];
      final col = _branchColors[i % _branchColors.length];
      final isLeft = i < left.length;
      final s = Offset(isLeft ? cx - rw / 2 : cx + rw / 2, cy);
      final e = Offset(isLeft ? r.right : r.left, r.center.dy);
      final dx = isLeft ? -60.0 : 60.0;
      final p = Path()
        ..moveTo(s.dx, s.dy)
        ..cubicTo(s.dx + dx, s.dy, e.dx - dx, e.dy, e.dx, e.dy);
      canvas.drawPath(
        p,
        Paint()
          ..color = col.withValues(alpha: 0.85)
          ..style = PaintingStyle.stroke
          ..strokeWidth = 2.2,
      );
    }

    final root = RRect.fromRectAndRadius(Rect.fromCenter(center: Offset(cx, cy), width: rw, height: rh), const Radius.circular(14));
    canvas.drawRRect(root, Paint()..color = AppColors.panel2);
    canvas.drawRRect(
      root,
      Paint()
        ..color = AppColors.gold
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2.4,
    );
    final rt = _tp(spec.root, const TextStyle(fontFamily: AppText.fDisplay, fontWeight: FontWeight.w700, fontSize: 24, color: AppColors.gold2, letterSpacing: 0.8), maxW: rw - 16);
    rt.paint(canvas, Offset(cx - rt.width / 2, cy - rt.height + 4));
    final rs = _tp(spec.rootSub, const TextStyle(fontFamily: AppText.fBody, fontSize: 15, color: AppColors.muted));
    rs.paint(canvas, Offset(cx - rs.width / 2, cy + 8));

    for (var i = 0; i < all.length; i++) {
      final (r, b) = all[i];
      final col = _branchColors[i % _branchColors.length];
      final box = RRect.fromRectAndRadius(r, const Radius.circular(10));
      canvas.drawRRect(box, Paint()..color = AppColors.panel);
      canvas.save();
      canvas.clipRRect(box);
      canvas.drawRect(Rect.fromLTWH(r.left, r.top, r.width, 30), Paint()..color = col.withValues(alpha: 0.22));
      canvas.drawRect(Rect.fromLTWH(r.left, r.top, 4, r.height), Paint()..color = col);
      canvas.restore();
      canvas.drawRRect(
        box,
        Paint()
          ..color = col.withValues(alpha: 0.7)
          ..style = PaintingStyle.stroke
          ..strokeWidth = 1.4,
      );
      final title = _tp(b.label.toUpperCase(),
          TextStyle(fontFamily: AppText.fDisplay, fontWeight: FontWeight.w700, fontSize: 16.5, color: col, letterSpacing: 0.8), maxW: bw - 24);
      title.paint(canvas, Offset(r.left + 14, r.top + 15 - title.height / 2));
      var y = r.top + 38;
      for (final it in b.items) {
        canvas.drawCircle(Offset(r.left + 18, y + 9), 2.6, Paint()..color = col);
        final tp = _tp(it, const TextStyle(fontFamily: AppText.fBody, fontSize: 15, color: AppColors.text), maxW: bw - 40);
        tp.paint(canvas, Offset(r.left + 28, y));
        y += 21;
      }
    }
  }

  @override
  bool shouldRepaint(covariant _MindPainter old) => old.spec != spec;
}
