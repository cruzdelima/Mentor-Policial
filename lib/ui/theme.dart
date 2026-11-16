import 'package:flutter/material.dart';

/// Paleta "operacional": azul-marinho profundo, dourado de distintivo e cores de status.
class AppColors {
  AppColors._();

  static const bg = Color(0xFF0A1220);
  static const sidebar = Color(0xFF060B15);
  static const panel = Color(0xFF111C30);
  static const panel2 = Color(0xFF16243D);
  static const field = Color(0xFF1A2B48);
  static const line = Color(0xFF23365A);
  static const lineSoft = Color(0xFF17243B);
  static const text = Color(0xFFE6EDF7);
  static const muted = Color(0xFF8EA0BC);
  static const dim = Color(0xFF4E5F7A);
  static const gold = Color(0xFFE0B23A);
  static const gold2 = Color(0xFFF5C842);
  static const blue = Color(0xFF5B9BFF);
  static const green = Color(0xFF34D399);
  static const amber = Color(0xFFFBBF24);
  static const red = Color(0xFFF87171);
  static const teal = Color(0xFF2DD4BF);

  static const federal = Color(0xFF1E4FA3);
  static const estadual = Color(0xFF1F7A4A);
  static const municipal = Color(0xFFA35A12);

  static Color esfera(String e) => switch (e) {
        'Federal' => federal,
        'Estadual' => estadual,
        _ => municipal,
      };

  static Color hex(String h) => Color(int.parse('FF${h.replaceAll('#', '')}', radix: 16));
}

class AppText {
  AppText._();

  static const fDisplay = 'BarlowCondensed';
  static const fBody = 'Barlow';

  static TextStyle h1([Color c = AppColors.text]) =>
      TextStyle(fontFamily: fDisplay, fontWeight: FontWeight.w700, fontSize: 28, letterSpacing: 0.6, color: c, height: 1.1);
  static TextStyle h2([Color c = AppColors.text]) =>
      TextStyle(fontFamily: fDisplay, fontWeight: FontWeight.w700, fontSize: 20, letterSpacing: 0.5, color: c, height: 1.15);
  static TextStyle h3([Color c = AppColors.text]) =>
      TextStyle(fontFamily: fDisplay, fontWeight: FontWeight.w700, fontSize: 16, letterSpacing: 0.5, color: c, height: 1.2);
  static TextStyle label([Color c = AppColors.muted]) =>
      TextStyle(fontFamily: fDisplay, fontWeight: FontWeight.w600, fontSize: 12.5, letterSpacing: 1.1, color: c);
  static TextStyle kpi([Color c = AppColors.text]) =>
      TextStyle(fontFamily: fDisplay, fontWeight: FontWeight.w700, fontSize: 34, color: c, height: 1.0);
  static TextStyle body([Color c = AppColors.text]) => TextStyle(fontFamily: AppText.fBody, fontSize: 14, color: c, height: 1.45);
  static TextStyle small([Color c = AppColors.muted]) => TextStyle(fontFamily: AppText.fBody, fontSize: 12.5, color: c, height: 1.35);
  static TextStyle strong([Color c = AppColors.text]) =>
      TextStyle(fontFamily: AppText.fBody, fontSize: 14, fontWeight: FontWeight.w600, color: c, height: 1.4);
}

ThemeData buildTheme() {
  const scheme = ColorScheme.dark(
    primary: AppColors.gold,
    onPrimary: AppColors.bg,
    secondary: AppColors.blue,
    onSecondary: AppColors.bg,
    surface: AppColors.panel,
    onSurface: AppColors.text,
    error: AppColors.red,
    onError: AppColors.bg,
    outline: AppColors.line,
  );
  final base = ThemeData(useMaterial3: true, colorScheme: scheme, brightness: Brightness.dark, fontFamily: AppText.fBody);
  OutlineInputBorder border(Color c) => OutlineInputBorder(borderRadius: BorderRadius.circular(8), borderSide: BorderSide(color: c));
  return base.copyWith(
    scaffoldBackgroundColor: AppColors.bg,
    canvasColor: AppColors.bg,
    dividerColor: AppColors.line,
    dividerTheme: const DividerThemeData(color: AppColors.lineSoft, thickness: 1, space: 1),
    textTheme: base.textTheme.apply(bodyColor: AppColors.text, displayColor: AppColors.text, fontFamily: AppText.fBody),
    inputDecorationTheme: InputDecorationTheme(
      filled: true,
      fillColor: AppColors.field,
      isDense: true,
      contentPadding: const EdgeInsets.symmetric(horizontal: 12, vertical: 12),
      labelStyle: AppText.small(),
      hintStyle: AppText.small(AppColors.dim),
      border: border(AppColors.line),
      enabledBorder: border(AppColors.line),
      focusedBorder: border(AppColors.gold),
    ),
    elevatedButtonTheme: ElevatedButtonThemeData(
      style: ElevatedButton.styleFrom(
        backgroundColor: AppColors.gold,
        foregroundColor: AppColors.bg,
        textStyle: const TextStyle(fontFamily: AppText.fDisplay, fontWeight: FontWeight.w700, fontSize: 15, letterSpacing: 0.8),
        padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 14),
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
      ),
    ),
    outlinedButtonTheme: OutlinedButtonThemeData(
      style: OutlinedButton.styleFrom(
        foregroundColor: AppColors.text,
        side: const BorderSide(color: AppColors.line),
        textStyle: const TextStyle(fontFamily: AppText.fDisplay, fontWeight: FontWeight.w600, fontSize: 14, letterSpacing: 0.6),
        padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
      ),
    ),
    textButtonTheme: TextButtonThemeData(
      style: TextButton.styleFrom(
        foregroundColor: AppColors.gold2,
        textStyle: const TextStyle(fontFamily: AppText.fDisplay, fontWeight: FontWeight.w600, fontSize: 14, letterSpacing: 0.6),
      ),
    ),
    dialogTheme: DialogThemeData(
      backgroundColor: AppColors.panel,
      surfaceTintColor: Colors.transparent,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(14), side: const BorderSide(color: AppColors.line)),
    ),
    snackBarTheme: const SnackBarThemeData(
      backgroundColor: AppColors.panel2,
      contentTextStyle: TextStyle(color: AppColors.text, fontFamily: AppText.fBody),
      behavior: SnackBarBehavior.floating,
    ),
    tooltipTheme: TooltipThemeData(
      decoration: BoxDecoration(color: AppColors.panel2, borderRadius: BorderRadius.circular(6), border: Border.all(color: AppColors.line)),
      textStyle: AppText.small(AppColors.text),
    ),
    checkboxTheme: CheckboxThemeData(
      fillColor: WidgetStateProperty.resolveWith((s) => s.contains(WidgetState.selected) ? AppColors.green : Colors.transparent),
      checkColor: const WidgetStatePropertyAll(AppColors.bg),
      side: const BorderSide(color: AppColors.muted, width: 1.5),
    ),
    scrollbarTheme: ScrollbarThemeData(
      thumbColor: WidgetStatePropertyAll(AppColors.line.withValues(alpha: 0.9)),
      radius: const Radius.circular(8),
      thickness: const WidgetStatePropertyAll(8),
    ),
    popupMenuTheme: PopupMenuThemeData(
      color: AppColors.panel2,
      surfaceTintColor: Colors.transparent,
      textStyle: AppText.body(),
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10), side: const BorderSide(color: AppColors.line)),
    ),
    datePickerTheme: const DatePickerThemeData(
      backgroundColor: AppColors.panel,
      surfaceTintColor: Colors.transparent,
      headerBackgroundColor: AppColors.panel2,
      headerForegroundColor: AppColors.text,
      todayBorder: const BorderSide(color: AppColors.gold),
    ),
    progressIndicatorTheme: const ProgressIndicatorThemeData(color: AppColors.gold, linearTrackColor: AppColors.field),
  );
}
