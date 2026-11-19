import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../config.dart';
import '../core/validation.dart';
import '../data/auth.dart';
import '../data/storage.dart';
import '../state/account.dart';
import 'theme.dart';
import 'widgets.dart';

enum _Mode { login, signup, confirm, forgot, reset }

/// Entrar, criar conta, confirmar e-mail e recuperar senha.
class AuthScreen extends StatefulWidget {
  const AuthScreen({super.key});

  @override
  State<AuthScreen> createState() => _AuthScreenState();
}

class _AuthScreenState extends State<AuthScreen> {
  _Mode mode = _Mode.login;
  final name = TextEditingController();
  final email = TextEditingController();
  final phone = TextEditingController();
  final pass = TextEditingController();
  final pass2 = TextEditingController();
  final code = TextEditingController();
  bool showPass = false;
  bool terms = false;
  bool busy = false;
  String? error;
  String? info;

  @override
  void dispose() {
    for (final c in [name, email, phone, pass, pass2, code]) {
      c.dispose();
    }
    super.dispose();
  }

  void _go(_Mode m) => setState(() {
        mode = m;
        error = null;
        info = null;
        code.clear();
        if (m != _Mode.signup) pass2.clear();
      });

  Future<void> _run(Future<void> Function() action) async {
    if (busy) return;
    setState(() {
      busy = true;
      error = null;
      info = null;
    });
    try {
      await action();
    } on AuthError catch (e) {
      if (mounted) setState(() => error = e.message);
    } catch (e) {
      if (mounted) setState(() => error = 'Erro inesperado: $e');
    } finally {
      if (mounted) setState(() => busy = false);
    }
  }

  AccountController get acc => AccountScope.read(context)!;

  // ------------------------------------------------------------------ validação

  String? get signupProblem {
    if (name.text.trim().length < 2) return 'Informe seu nome.';
    if (!isValidEmail(email.text)) return 'Informe um e-mail válido.';
    if (normalizePhone(phone.text) == null) return 'Informe um celular válido com DDD.';
    final p = passwordProblem(pass.text);
    if (p != null) return p;
    if (pass.text != pass2.text) return 'As senhas não conferem.';
    if (!terms) return 'Aceite os Termos de Uso e a Política de Privacidade.';
    return null;
  }

  Future<void> _login() => _run(() async {
        if (!isValidEmail(email.text) || pass.text.isEmpty) throw AuthError('Informe e-mail e senha.');
        try {
          await acc.signIn(email.text, pass.text);
        } on AuthError catch (e) {
          if (e.code == 'email_not_confirmed') {
            setState(() => mode = _Mode.confirm);
          }
          rethrow;
        }
      });

  Future<void> _signup() => _run(() async {
        final p = signupProblem;
        if (p != null) throw AuthError(p);
        final entered = await acc.signUp(email: email.text, password: pass.text, name: name.text, phone: normalizePhone(phone.text)!);
        if (!entered && mounted) {
          setState(() {
            mode = _Mode.confirm;
            info = 'Enviamos um código para ${email.text.trim()}. Confira também a caixa de spam.';
          });
        }
      });

  Future<void> _confirm() => _run(() async {
        if (code.text.trim().length < 6) throw AuthError('Digite o código que chegou no seu e-mail.');
        await acc.confirmSignup(email.text, code.text);
      });

  Future<void> _sendRecovery() => _run(() async {
        if (!isValidEmail(email.text)) throw AuthError('Informe o e-mail da sua conta.');
        await acc.service.sendRecoveryCode(email.text);
        if (mounted) {
          setState(() {
            mode = _Mode.reset;
            info = 'Se houver uma conta com esse e-mail, enviamos um código para ele.';
          });
        }
      });

  Future<void> _reset() => _run(() async {
        if (code.text.trim().length < 6) throw AuthError('Digite o código que chegou no seu e-mail.');
        final p = passwordProblem(pass.text);
        if (p != null) throw AuthError(p);
        if (pass.text != pass2.text) throw AuthError('As senhas não conferem.');
        await acc.resetPassword(email.text, code.text, pass.text);
      });

  // ------------------------------------------------------------------ interface

  @override
  Widget build(BuildContext context) {
    final width = MediaQuery.sizeOf(context).width;
    return Scaffold(
      body: Row(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
        // Em telas estreitas (tablet em pé) o painel de apresentação some; em telas baixas (tablet deitado
        // com o teclado aberto) ele rola em vez de estourar.
        if (width >= 820)
          Container(
            width: width < 1100 ? 320 : 380,
            color: AppColors.sidebar,
            child: LayoutBuilder(
              builder: (context, box) => SingleChildScrollView(
                child: ConstrainedBox(
                  constraints: BoxConstraints(minHeight: box.maxHeight),
                  child: IntrinsicHeight(child: _intro()),
                ),
              ),
            ),
          ),
        Expanded(
          child: Center(
            child: SingleChildScrollView(
              padding: const EdgeInsets.symmetric(vertical: 32, horizontal: 24),
              child: ConstrainedBox(
                constraints: const BoxConstraints(maxWidth: 460),
                child: AutofillGroup(child: _form()),
              ),
            ),
          ),
        ),
      ]),
    );
  }

  Widget _intro() => Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
            const TapeBand(height: 22),
            Padding(
              padding: const EdgeInsets.fromLTRB(32, 40, 32, 0),
              child: Row(children: [
                const BadgeLogo(size: 54),
                const SizedBox(width: 16),
                Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                  Text('TATICUM', style: AppText.h1(AppColors.gold2).copyWith(fontSize: 34, letterSpacing: 3, height: 1.0)),
                  Text('MENTOR POLICIAL', style: AppText.label(AppColors.muted).copyWith(fontSize: 14.3, letterSpacing: 2.2)),
                ]),
              ]),
            ),
            const SizedBox(height: 40),
            for (final (icon, title, text) in const [
              (Icons.flag_outlined, 'Metas diárias', 'O cronograma do ciclo básico, calculado pelo seu tempo e pelo seu nível.'),
              (Icons.menu_book_outlined, 'Materiais e questões', 'Apostilas aprofundadas, resumos para revisão e questões comentadas.'),
              (Icons.lock_outline, 'Seus dados protegidos', 'Senha forte e acesso individual. Seu progresso fica com você e numa cópia protegida na nuvem.'),
            ])
              Padding(
                padding: const EdgeInsets.fromLTRB(32, 0, 32, 22),
                child: Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
                  Icon(icon, color: AppColors.gold, size: 22),
                  const SizedBox(width: 14),
                  Expanded(
                    child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                      Text(title.toUpperCase(), style: AppText.h3()),
                      const SizedBox(height: 2),
                      Text(text, style: AppText.small()),
                    ]),
                  ),
                ]),
              ),
            const Spacer(),
            Padding(
              padding: const EdgeInsets.all(32),
              child: Text('Ciclo básico, edital verticalizado e revisões para carreiras policiais.', style: AppText.small(AppColors.dim)),
            ),
          ]);

  Widget _form() {
    final children = <Widget>[];
    void title(String kicker, String t, [String? sub]) {
      children.add(Text(kicker.toUpperCase(), style: AppText.label(AppColors.gold)));
      children.add(const SizedBox(height: 6));
      children.add(Text(t.toUpperCase(), style: AppText.h1().copyWith(fontSize: 32)));
      if (sub != null) {
        children.add(const SizedBox(height: 8));
        children.add(Text(sub, style: AppText.body(AppColors.muted)));
      }
      children.add(const SizedBox(height: 24));
    }

    switch (mode) {
      case _Mode.login:
        title('Bem-vindo de volta', 'Entrar');
        children.addAll([
          _emailField(),
          const SizedBox(height: 14),
          _passField(pass, 'Senha', onSubmitted: _login, hints: const [AutofillHints.password]),
          Align(
            alignment: Alignment.centerRight,
            child: TextButton(onPressed: () => _go(_Mode.forgot), child: const Text('ESQUECI MINHA SENHA')),
          ),
          ..._messages(),
          const SizedBox(height: 8),
          _primary('ENTRAR', _login),
          const SizedBox(height: 24),
          _switchLine('Ainda não tem conta?', 'CRIAR CONTA', () => _go(_Mode.signup)),
        ]);
      case _Mode.signup:
        title('Gratuito durante os testes', 'Criar conta');
        children.addAll([
          TextField(
            controller: name,
            textCapitalization: TextCapitalization.words,
            autofillHints: const [AutofillHints.name],
            decoration: const InputDecoration(labelText: 'Nome completo', prefixIcon: Icon(Icons.person_outline)),
            onChanged: (_) => setState(() {}),
          ),
          const SizedBox(height: 14),
          _emailField(),
          const SizedBox(height: 14),
          TextField(
            controller: phone,
            keyboardType: TextInputType.phone,
            autofillHints: const [AutofillHints.telephoneNumber],
            inputFormatters: [FilteringTextInputFormatter.allow(RegExp(r'[0-9()+\- ]')), LengthLimitingTextInputFormatter(20)],
            decoration: InputDecoration(
              labelText: 'Celular com DDD',
              hintText: '(85) 99999-1234',
              prefixIcon: const Icon(Icons.phone_iphone),
              suffixIcon: phone.text.isEmpty
                  ? null
                  : Icon(normalizePhone(phone.text) == null ? Icons.close : Icons.check, color: normalizePhone(phone.text) == null ? AppColors.red : AppColors.green),
            ),
            onChanged: (_) => setState(() {}),
          ),
          const SizedBox(height: 14),
          _passField(pass, 'Senha', hints: const [AutofillHints.newPassword]),
          const SizedBox(height: 10),
          PasswordChecklist(password: pass.text),
          const SizedBox(height: 14),
          _passField(pass2, 'Repita a senha', onSubmitted: _signup, hints: const [AutofillHints.newPassword]),
          if (pass2.text.isNotEmpty && pass2.text != pass.text)
            Padding(padding: const EdgeInsets.only(top: 6), child: Text('As senhas não conferem.', style: AppText.small(AppColors.red))),
          const SizedBox(height: 12),
          Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Checkbox(value: terms, onChanged: (v) => setState(() => terms = v ?? false)),
            Expanded(
              child: Padding(
                padding: const EdgeInsets.only(top: 10),
                child: Wrap(children: [
                  Text('Li e aceito os ', style: AppText.small(AppColors.text)),
                  InkWell(
                    onTap: () => openExternal(kTermsUrl),
                    child: Text('Termos de Uso e a Política de Privacidade',
                        style: AppText.small(AppColors.gold2).copyWith(decoration: TextDecoration.underline, decorationColor: AppColors.gold2)),
                  ),
                  Text('.', style: AppText.small(AppColors.text)),
                ]),
              ),
            ),
          ]),
          ..._messages(),
          const SizedBox(height: 8),
          _primary('CRIAR CONTA', _signup, enabled: signupProblem == null),
          const SizedBox(height: 24),
          _switchLine('Já tem conta?', 'ENTRAR', () => _go(_Mode.login)),
        ]);
      case _Mode.confirm:
        title('Último passo', 'Confirme seu e-mail', 'Digite o código enviado para ${email.text.trim()}. Se preferir, clique no link do e-mail e depois em ENTRAR.');
        children.addAll([
          _codeField(onSubmitted: _confirm),
          ..._messages(),
          const SizedBox(height: 16),
          _primary('CONFIRMAR', _confirm),
          const SizedBox(height: 12),
          Wrap(spacing: 8, children: [
            TextButton(
              onPressed: busy
                  ? null
                  : () => _run(() async {
                        await acc.service.resendSignupCode(email.text);
                        if (mounted) setState(() => info = 'Código reenviado. Confira também o spam.');
                      }),
              child: const Text('REENVIAR CÓDIGO'),
            ),
            TextButton(onPressed: () => _go(_Mode.login), child: const Text('JÁ CONFIRMEI PELO LINK: ENTRAR')),
          ]),
        ]);
      case _Mode.forgot:
        title('Recuperar acesso', 'Esqueci minha senha', 'Informe o e-mail da conta. Enviaremos um código para você criar uma nova senha.');
        children.addAll([
          _emailField(onSubmitted: _sendRecovery),
          ..._messages(),
          const SizedBox(height: 16),
          _primary('ENVIAR CÓDIGO', _sendRecovery),
          const SizedBox(height: 16),
          _switchLine('Lembrou a senha?', 'ENTRAR', () => _go(_Mode.login)),
        ]);
      case _Mode.reset:
        title('Recuperar acesso', 'Nova senha', 'Digite o código enviado para ${email.text.trim()} e escolha uma nova senha.');
        children.addAll([
          _codeField(),
          const SizedBox(height: 14),
          _passField(pass, 'Nova senha', hints: const [AutofillHints.newPassword]),
          const SizedBox(height: 10),
          PasswordChecklist(password: pass.text),
          const SizedBox(height: 14),
          _passField(pass2, 'Repita a nova senha', onSubmitted: _reset, hints: const [AutofillHints.newPassword]),
          ..._messages(),
          const SizedBox(height: 16),
          _primary('SALVAR NOVA SENHA', _reset),
          const SizedBox(height: 12),
          TextButton(onPressed: () => _go(_Mode.forgot), child: const Text('REENVIAR CÓDIGO')),
        ]);
    }
    return Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: children);
  }

  Widget _emailField({VoidCallback? onSubmitted}) => TextField(
        controller: email,
        keyboardType: TextInputType.emailAddress,
        autofillHints: const [AutofillHints.email],
        autocorrect: false,
        decoration: const InputDecoration(labelText: 'E-mail', prefixIcon: Icon(Icons.alternate_email)),
        onChanged: (_) => setState(() {}),
        onSubmitted: (_) => onSubmitted?.call(),
      );

  Widget _passField(TextEditingController c, String label, {VoidCallback? onSubmitted, List<String> hints = const []}) => TextField(
        controller: c,
        obscureText: !showPass,
        autocorrect: false,
        enableSuggestions: false,
        autofillHints: hints,
        decoration: InputDecoration(
          labelText: label,
          prefixIcon: const Icon(Icons.lock_outline),
          suffixIcon: IconButton(
            tooltip: showPass ? 'Ocultar senha' : 'Mostrar senha',
            icon: Icon(showPass ? Icons.visibility_off_outlined : Icons.visibility_outlined, size: 20),
            onPressed: () => setState(() => showPass = !showPass),
          ),
        ),
        onChanged: (_) => setState(() {}),
        onSubmitted: (_) => onSubmitted?.call(),
      );

  Widget _codeField({VoidCallback? onSubmitted}) => TextField(
        controller: code,
        keyboardType: TextInputType.number,
        inputFormatters: [FilteringTextInputFormatter.digitsOnly, LengthLimitingTextInputFormatter(10)],
        style: AppText.h2().copyWith(letterSpacing: 8),
        decoration: const InputDecoration(labelText: 'Código do e-mail', prefixIcon: Icon(Icons.pin_outlined)),
        onSubmitted: (_) => onSubmitted?.call(),
      );

  List<Widget> _messages() => [
        if (info != null)
          Padding(
            padding: const EdgeInsets.only(top: 12),
            child: _Note(text: info!, color: AppColors.teal, icon: Icons.mark_email_read_outlined),
          ),
        if (error != null)
          Padding(
            padding: const EdgeInsets.only(top: 12),
            child: _Note(text: error!, color: AppColors.red, icon: Icons.error_outline),
          ),
      ];

  Widget _primary(String label, VoidCallback onTap, {bool enabled = true}) => SizedBox(
        height: 50,
        child: ElevatedButton(
          onPressed: busy || !enabled ? null : onTap,
          child: busy ? const SizedBox(width: 22, height: 22, child: CircularProgressIndicator(strokeWidth: 2.5, color: AppColors.bg)) : Text(label),
        ),
      );

  Widget _switchLine(String text, String action, VoidCallback onTap) => Row(mainAxisAlignment: MainAxisAlignment.center, children: [
        Text(text, style: AppText.small()),
        TextButton(onPressed: onTap, child: Text(action)),
      ]);
}

class _Note extends StatelessWidget {
  const _Note({required this.text, required this.color, required this.icon});
  final String text;
  final Color color;
  final IconData icon;

  @override
  Widget build(BuildContext context) => Container(
        padding: const EdgeInsets.all(12),
        decoration: BoxDecoration(
          color: color.withValues(alpha: 0.10),
          borderRadius: BorderRadius.circular(8),
          border: Border.all(color: color.withValues(alpha: 0.5)),
        ),
        child: Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Icon(icon, color: color, size: 20),
          const SizedBox(width: 10),
          Expanded(child: Text(text, style: AppText.small(AppColors.text))),
        ]),
      );
}

/// Lista das regras de senha, marcadas em tempo real.
class PasswordChecklist extends StatelessWidget {
  const PasswordChecklist({super.key, required this.password});
  final String password;

  @override
  Widget build(BuildContext context) {
    return Wrap(spacing: 14, runSpacing: 6, children: [
      for (final r in kPasswordRules)
        Row(mainAxisSize: MainAxisSize.min, children: [
          Icon(r.test(password) ? Icons.check_circle : Icons.radio_button_unchecked, size: 16, color: r.test(password) ? AppColors.green : AppColors.dim),
          const SizedBox(width: 6),
          Text(r.label, style: AppText.small(r.test(password) ? AppColors.text : AppColors.muted).copyWith(fontSize: 12.5)),
        ]),
    ]);
  }
}
