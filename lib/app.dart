import 'package:flutter/material.dart';
import 'package:flutter_localizations/flutter_localizations.dart';

import 'state/account.dart';
import 'state/app_state.dart';
import 'ui/auth_screen.dart';
import 'ui/onboarding.dart';
import 'ui/shell.dart';
import 'ui/theme.dart';
import 'ui/widgets.dart';

/// Raiz do app.
///  * Sem contas (servidor não configurado ou testes): recebe [controller] pronto.
///  * Com contas: recebe [account]; o controlador de estudos é criado após o login.
class MentorApp extends StatelessWidget {
  const MentorApp({super.key, this.controller, this.account}) : assert(controller != null || account != null);
  final AppController? controller;
  final AccountController? account;

  @override
  Widget build(BuildContext context) {
    if (account == null) return _material();
    // Reconstrói o MaterialApp quando a conta muda (login, logout), trocando o controlador de estudos.
    return AccountScope(controller: account!, child: ListenableBuilder(listenable: account!, builder: (_, _) => _material()));
  }

  Widget _material() {
    return MaterialApp(
      title: 'Taticum',
      debugShowCheckedModeBanner: false,
      theme: buildTheme(),
      locale: const Locale('pt', 'BR'),
      supportedLocales: const [Locale('pt', 'BR')],
      localizationsDelegates: const [
        GlobalMaterialLocalizations.delegate,
        GlobalWidgetsLocalizations.delegate,
        GlobalCupertinoLocalizations.delegate,
      ],
      // O AppScope fica acima do Navigator para que diálogos também enxerguem o controlador.
      builder: (context, child) {
        final c = controller ?? account?.app;
        return c == null ? child! : AppScope(controller: c, child: child!);
      },
      home: account == null ? const _Gate() : const _AccountGate(),
    );
  }
}

class _AccountGate extends StatelessWidget {
  const _AccountGate();

  @override
  Widget build(BuildContext context) {
    final acc = AccountScope.maybeOf(context)!;
    switch (acc.status) {
      case AccountStatus.starting:
        return const Scaffold(
          body: Center(child: Column(mainAxisSize: MainAxisSize.min, children: [BadgeLogo(size: 64), SizedBox(height: 24), CircularProgressIndicator()])),
        );
      case AccountStatus.signedOut:
        return const AuthScreen(key: ValueKey('auth'));
      case AccountStatus.signedIn:
        return KeyedSubtree(key: ValueKey('user-${acc.userId}'), child: const _Gate());
    }
  }
}

class _Gate extends StatelessWidget {
  const _Gate();

  @override
  Widget build(BuildContext context) {
    final app = AppScope.of(context);
    // Troca direta (sem animação): a tela antiga não pode ser reconstruída sem perfil.
    return app.onboarded ? const Shell(key: ValueKey('shell')) : const Onboarding(key: ValueKey('onboarding'));
  }
}
