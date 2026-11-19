/// Estado da conta: sessão, perfil e o [AppController] do aluno logado.
library;

import 'dart:async';
import 'dart:io';

import 'package:flutter/foundation.dart' show kIsWeb;
import 'package:flutter/widgets.dart';

import '../config.dart';
import '../data/auth.dart';
import '../data/storage.dart';
import '../platform/fs.dart';
import 'app_state.dart';

enum AccountStatus { starting, signedOut, signedIn }

class AccountController extends ChangeNotifier {
  AccountController({AuthService? service})
      : service = service ?? AuthService(url: kSupabaseUrl, apiKey: kSupabaseKey, storage: Storage.defaultDir());

  final AuthService service;
  AccountStatus status = AccountStatus.starting;
  AccountProfile? profile;

  /// E-mail e id da conta (disponíveis mesmo offline).
  String email = '';
  String userId = '';

  /// Aberto sem internet com a última sessão salva.
  bool offline = false;

  /// Dados de estudo do aluno logado.
  AppController? app;
  String? startupError;

  bool get isAdmin => profile?.isAdmin ?? false;
  bool get isOwner => profile?.isOwner ?? false;

  /// Tenta retomar a sessão salva. Sem internet, abre com os dados locais (modo offline).
  Future<void> start() async {
    try {
      final s = await service.restore();
      await _enter(s.userId, s.email);
    } on AuthError catch (e) {
      final saved = await service.savedUser();
      if (e.offline && saved != null) {
        offline = true;
        await _enter(saved.$1, saved.$2, fetchProfile: false);
      } else {
        status = AccountStatus.signedOut;
        notifyListeners();
      }
    } catch (_) {
      status = AccountStatus.signedOut;
      notifyListeners();
    }
  }

  Future<void> _enter(String id, String mail, {bool fetchProfile = true}) async {
    userId = id;
    email = mail;
    if (fetchProfile) {
      try {
        profile = await service.myProfile();
        offline = false;
      } on AuthError catch (e) {
        if (!e.offline) rethrow;
        offline = true;
      }
    }
    final storage = await userStorage(id);
    app?.dispose();
    app = await AppController.load(storage: storage, remote: service);
    app!.reviewer = isOwner; // só o dono vê materiais em revisão
    status = AccountStatus.signedIn;
    notifyListeners();
    unawaited(app!.attachSync(service)); // progresso na nuvem (não atrasa a entrada)
  }

  Future<void> signIn(String email, String password) async {
    final s = await service.signIn(email, password);
    await _enter(s.userId, s.email);
  }

  /// Devolve true se já entrou; false se precisa confirmar o e-mail com o código.
  Future<bool> signUp({required String email, required String password, required String name, required String phone}) async {
    final s = await service.signUp(email: email, password: password, name: name, phone: phone);
    if (s == null) return false;
    await _enter(s.userId, s.email);
    return true;
  }

  Future<void> confirmSignup(String email, String code) async {
    final s = await service.verifyCode(email, code, type: 'signup');
    await _enter(s.userId, s.email);
  }

  Future<void> resetPassword(String email, String code, String newPassword) async {
    final s = await service.verifyCode(email, code, type: 'recovery');
    await service.changePassword(newPassword);
    await _enter(s.userId, s.email);
  }

  Future<void> refreshProfile() async {
    profile = await service.myProfile();
    offline = false;
    app?.reviewer = isOwner;
    notifyListeners();
  }

  Future<void> signOut() async {
    // Envia o que ainda não subiu para a nuvem antes de sair.
    try {
      final sy = app?.sync;
      if (sy != null && sy.dirty) await sy.push().timeout(const Duration(seconds: 8));
    } catch (_) {}
    await service.signOut();
    await _leave();
  }

  Future<void> deleteAccount() async {
    await service.deleteMyAccount();
    // Os dados de estudo deste computador também são apagados.
    final dir = (await userStorage(userId)).dir;
    await _leave();
    try {
      await Fs.instance.deleteTree(dir);
    } catch (_) {}
  }

  Future<void> _leave() async {
    app?.dispose();
    app = null;
    profile = null;
    userId = '';
    email = '';
    offline = false;
    status = AccountStatus.signedOut;
    notifyListeners();
  }

  @override
  void dispose() {
    app?.dispose();
    super.dispose();
  }

  /// Pasta de dados de cada conta. Na primeira conta que entrar neste computador, os dados da
  /// versão sem contas (dados.json na raiz) são trazidos para ela, para ninguém perder o progresso.
  static Future<Storage> userStorage(String userId) async {
    final root = Storage.defaultDir();
    final dir = Storage.join(Storage.join(root, 'contas'), userId);
    if (!kIsWeb && !await Directory(dir).exists()) {
      await Directory(dir).create(recursive: true);
      final legacy = File(Storage.join(root, 'dados.json'));
      if (await legacy.exists()) {
        await legacy.copy(Storage.join(dir, 'dados.json'));
        await legacy.rename(Storage.join(root, 'dados_antes_das_contas.json'));
      }
    }
    return Storage(dir);
  }
}

class AccountScope extends InheritedNotifier<AccountController> {
  const AccountScope({super.key, required AccountController controller, required super.child}) : super(notifier: controller);

  /// Null quando o app roda sem contas (servidor não configurado).
  static AccountController? maybeOf(BuildContext context) => context.dependOnInheritedWidgetOfExactType<AccountScope>()?.notifier;

  static AccountController? read(BuildContext context) => context.getInheritedWidgetOfExactType<AccountScope>()?.notifier;
}
