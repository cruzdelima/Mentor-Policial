import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import 'app.dart';
import 'state/app_state.dart';
import 'ui/theme.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  LicenseRegistry.addLicense(() async* {
    yield LicenseEntryWithLineBreaks(['Barlow', 'Barlow Condensed'], await rootBundle.loadString('assets/fonts/OFL.txt'));
  });
  try {
    final controller = await AppController.load();
    runApp(MentorApp(controller: controller));
  } catch (e, st) {
    debugPrint('Falha ao iniciar: $e\n$st');
    runApp(StartupError(error: '$e'));
  }
}

/// Tela exibida se algo impedir a abertura (ex.: arquivo de dados corrompido sem backup).
class StartupError extends StatelessWidget {
  const StartupError({super.key, required this.error});
  final String error;

  @override
  Widget build(BuildContext context) => MaterialApp(
        debugShowCheckedModeBanner: false,
        theme: buildTheme(),
        home: Scaffold(
          body: Center(
            child: ConstrainedBox(
              constraints: const BoxConstraints(maxWidth: 560),
              child: Column(mainAxisSize: MainAxisSize.min, children: [
                const Icon(Icons.report_gmailerrorred, size: 48, color: AppColors.red),
                const SizedBox(height: 12),
                Text('NÃO FOI POSSÍVEL ABRIR O MENTOR POLICIAL', style: AppText.h2(), textAlign: TextAlign.center),
                const SizedBox(height: 8),
                SelectableText(error, style: AppText.small(), textAlign: TextAlign.center),
              ]),
            ),
          ),
        ),
      );
}
