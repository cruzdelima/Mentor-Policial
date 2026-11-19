/// Cliente mínimo do Supabase (Auth + banco via REST), sem dependências externas.
///
/// Segurança:
///  * A senha só trafega por HTTPS até o servidor, que guarda apenas o hash (bcrypt). O app nunca a grava.
///  * O app guarda localmente só o "refresh token" da sessão, na pasta de dados do usuário do sistema.
///  * Toda autorização é decidida no servidor (Row Level Security). O app apenas exibe o que o servidor libera.
library;

import 'dart:async';
import 'dart:convert';
import 'dart:io';

import '../state/cloud_sync.dart';
import 'package:flutter/foundation.dart' show kIsWeb;

import '../platform/fs.dart';
import '../platform/web_bridge.dart';
import 'catalog_store.dart';
import 'storage.dart';

enum Role { student, admin, owner }

Role roleFrom(String? s) => switch (s) {
      'owner' => Role.owner,
      'admin' => Role.admin,
      _ => Role.student,
    };

String roleLabel(Role r) => switch (r) {
      Role.owner => 'Dono',
      Role.admin => 'Administrador',
      Role.student => 'Aluno',
    };

/// Classificação do aluno (coluna profiles.plan). Beta e Gratuito são manuais (só o dono);
/// mensal e anual virão do pagamento, quando o app for pago.
enum Plan { none, beta, tester, monthly, annual }

Plan planFrom(String? s) => switch (s) {
      'beta' => Plan.beta,
      'tester' => Plan.tester,
      'monthly' => Plan.monthly,
      'annual' => Plan.annual,
      _ => Plan.none,
    };

String planLabel(Plan p) => switch (p) {
      Plan.none => 'Sem classificação',
      Plan.beta => 'Testador Beta',
      Plan.tester => 'Testador Gratuito',
      Plan.monthly => 'Assinante mensal',
      Plan.annual => 'Assinante anual',
    };

/// Classificações que o dono pode dar à mão.
const kManualPlans = [Plan.none, Plan.beta, Plan.tester];

class AccountProfile {
  AccountProfile({
    required this.id,
    required this.email,
    required this.name,
    required this.phone,
    required this.role,
    required this.plan,
    required this.createdAt,
    this.planExpiresAt,
    this.planNote = '',
    this.planSource = 'manual',
    this.planUpdatedAt,
  });

  factory AccountProfile.fromJson(Map<String, dynamic> j) => AccountProfile(
        id: j['id'] as String,
        email: j['email'] as String? ?? '',
        name: j['name'] as String? ?? '',
        phone: j['phone'] as String? ?? '',
        role: roleFrom(j['role'] as String?),
        plan: planFrom(j['plan'] as String?),
        createdAt: DateTime.tryParse(j['created_at'] as String? ?? '')?.toLocal() ?? DateTime.now(),
        planExpiresAt: DateTime.tryParse(j['plan_expires_at'] as String? ?? '')?.toLocal(),
        planNote: j['plan_note'] as String? ?? '',
        planSource: j['plan_source'] as String? ?? 'manual',
        planUpdatedAt: DateTime.tryParse(j['plan_updated_at'] as String? ?? '')?.toLocal(),
      );

  final String id;
  final String email;
  final String name;
  final String phone;
  final Role role;
  final Plan plan;
  final DateTime createdAt;
  final DateTime? planExpiresAt;
  final String planNote;
  final String planSource;
  final DateTime? planUpdatedAt;

  /// Assinatura paga ainda válida (o dono não pode mudar à mão).
  bool get hasActiveSubscription =>
      (plan == Plan.monthly || plan == Plan.annual) && (planExpiresAt == null || planExpiresAt!.isAfter(DateTime.now()));

  bool get isAdmin => role == Role.admin || role == Role.owner;
  bool get isOwner => role == Role.owner;
}

class AuditEntry {
  AuditEntry(this.at, this.actorEmail, this.action, this.targetEmail, this.detail);
  final DateTime at;
  final String actorEmail;
  final String action;
  final String targetEmail;
  final String detail;
}

class Session {
  Session({required this.accessToken, required this.refreshToken, required this.expiresAt, required this.userId, required this.email});

  factory Session.fromAuth(Map<String, dynamic> j) {
    final user = j['user'] as Map<String, dynamic>? ?? const {};
    final exp = (j['expires_at'] as num?)?.toInt();
    return Session(
      accessToken: j['access_token'] as String,
      refreshToken: j['refresh_token'] as String,
      expiresAt: exp != null
          ? DateTime.fromMillisecondsSinceEpoch(exp * 1000)
          : DateTime.now().add(Duration(seconds: (j['expires_in'] as num? ?? 3600).toInt())),
      userId: user['id'] as String? ?? '',
      email: user['email'] as String? ?? '',
    );
  }

  final String accessToken;
  final String refreshToken;
  final DateTime expiresAt;
  final String userId;
  final String email;

  bool get expiringSoon => DateTime.now().isAfter(expiresAt.subtract(const Duration(minutes: 2)));
}

/// Erro com mensagem pronta para o aluno.
class AuthError implements Exception {
  AuthError(this.message, {this.code = '', this.offline = false});
  final String message;
  final String code;
  final bool offline;
  @override
  String toString() => message;
}

String _friendly(String code, String raw, int status) {
  switch (code) {
    case 'invalid_credentials':
      return 'E-mail ou senha incorretos.';
    case 'email_not_confirmed':
      return 'Confirme seu e-mail antes de entrar. Procure a mensagem do Taticum (veja também o spam).';
    case 'user_already_exists':
    case 'email_exists':
      return 'Já existe uma conta com esse e-mail. Use "Entrar" ou "Esqueci minha senha".';
    case 'weak_password':
      return 'A senha não cumpre as regras de segurança.';
    case 'otp_expired':
      return 'Código inválido ou expirado. Peça um novo código.';
    case 'over_email_send_rate_limit':
      return 'Muitos e-mails enviados em pouco tempo. Aguarde alguns minutos e tente de novo.';
    case 'over_request_rate_limit':
      return 'Muitas tentativas. Aguarde alguns minutos e tente de novo.';
    case 'same_password':
      return 'A nova senha precisa ser diferente da atual.';
    case 'signup_disabled':
      return 'Os cadastros estão temporariamente fechados.';
    case 'refresh_token_not_found':
    case 'refresh_token_already_used':
    case 'session_not_found':
      return 'Sua sessão expirou. Entre novamente.';
    case 'PGRST202':
    case 'PGRST205':
    case '42P01':
      return 'O servidor ainda não tem a parte do catálogo. Rode o arquivo supabase/migrations/0002_catalogo.sql no SQL Editor do Supabase.';
  }
  if (status == 429) return 'Muitas tentativas. Aguarde alguns minutos e tente de novo.';
  if (status >= 500) return 'O servidor está indisponível no momento. Tente de novo em instantes.';
  if (raw.contains('Database error saving new user')) return 'Não foi possível criar a conta. Confira os dados (telefone com DDD).';
  return raw.isEmpty ? 'Não foi possível concluir a operação (erro $status).' : raw;
}

class AuthService implements CatalogRemote, StudyRemote {
  AuthService({required this.url, required this.apiKey, required this.storage});

  final String url;
  final String apiKey;

  /// Pasta onde a sessão fica salva (raiz dos dados do app).
  /// Pasta (no navegador: prefixo) onde a sessão fica salva.
  final String storage;

  Session? session;

  String get _sessionFile => Storage.join(storage, 'sessao.json');

  // ------------------------------------------------------------------ HTTP

  Future<dynamic> _send(String method, String path, {Object? body, bool auth = false, Map<String, String> extra = const {}}) async {
    final headers = <String, String>{'apikey': apiKey, 'Accept': 'application/json', 'Content-Type': 'application/json'};
    if (auth) {
      final s = await validSession();
      headers['Authorization'] = 'Bearer ${s.accessToken}';
    }
    headers.addAll(extra);
    final payload = body == null ? null : jsonEncode(body);
    final (status, text) = kIsWeb ? await _sendWeb(method, '$url$path', headers, payload) : await _sendIo(method, '$url$path', headers, payload);
    final data = text.isEmpty ? null : jsonDecode(text);
    if (status >= 200 && status < 300) return data;
    var code = '', msg = '';
    if (data is Map) {
      code = '${data['error_code'] ?? data['code'] ?? data['error'] ?? ''}';
      msg = '${data['msg'] ?? data['message'] ?? data['error_description'] ?? ''}';
    }
    throw AuthError(_friendly(code, msg, status), code: code);
  }

  Future<(int, String)> _sendWeb(String method, String url, Map<String, String> headers, String? body) async {
    try {
      final r = await webFetch(method, url, headers, body).timeout(const Duration(seconds: 25));
      return (r.status, r.text);
    } on TimeoutException {
      throw AuthError('O servidor demorou a responder. Verifique sua internet.', offline: true);
    } catch (_) {
      throw AuthError('Sem conexão com a internet.', offline: true);
    }
  }

  Future<(int, String)> _sendIo(String method, String url, Map<String, String> headers, String? body) async {
    final client = HttpClient()
      ..connectionTimeout = const Duration(seconds: 10)
      ..userAgent = 'Taticum';
    try {
      final req = await client.openUrl(method, Uri.parse(url));
      headers.forEach(req.headers.set);
      if (body != null) req.add(utf8.encode(body));
      final res = await req.close().timeout(const Duration(seconds: 20));
      return (res.statusCode, await res.transform(utf8.decoder).join());
    } on SocketException {
      throw AuthError('Sem conexão com a internet.', offline: true);
    } on HandshakeException {
      throw AuthError('Não foi possível estabelecer uma conexão segura com o servidor.', offline: true);
    } on TimeoutException {
      throw AuthError('O servidor demorou a responder. Verifique sua internet.', offline: true);
    } on HttpException {
      throw AuthError('Falha de comunicação com o servidor.', offline: true);
    } finally {
      client.close();
    }
  }

  // ------------------------------------------------------------------ sessão

  Future<void> _saveSession(Session? s) async {
    session = s;
    if (s == null) {
      await Fs.instance.delete(_sessionFile);
      return;
    }
    // Guarda só o necessário para renovar a sessão. Nada de senha.
    await Fs.instance.write(_sessionFile, jsonEncode({'refresh_token': s.refreshToken, 'user_id': s.userId, 'email': s.email}));
    if (!kIsWeb && !Platform.isWindows) {
      // Somente o usuário do sistema pode ler o arquivo (no Windows, a pasta AppData já é privada do usuário).
      await Process.run('chmod', ['600', _sessionFile]);
    }
  }

  /// Dados da última sessão salva (para abrir offline): (userId, email) ou null.
  Future<(String, String)?> savedUser() async {
    final text = await Fs.instance.read(_sessionFile);
    if (text == null) return null;
    try {
      final j = jsonDecode(text) as Map<String, dynamic>;
      return (j['user_id'] as String, j['email'] as String? ?? '');
    } catch (_) {
      return null;
    }
  }

  /// Renova a sessão salva. Lança [AuthError] (offline = true se não houver internet).
  Future<Session> restore() async {
    final text = await Fs.instance.read(_sessionFile);
    if (text == null) throw AuthError('Sem sessão salva.');
    final j = jsonDecode(text) as Map<String, dynamic>;
    return _refresh(j['refresh_token'] as String);
  }

  Future<Session> _refresh(String refreshToken) async {
    try {
      final data = await _send('POST', '/auth/v1/token?grant_type=refresh_token', body: {'refresh_token': refreshToken});
      final s = Session.fromAuth(data as Map<String, dynamic>);
      await _saveSession(s);
      return s;
    } on AuthError catch (e) {
      if (!e.offline) await _saveSession(null);
      rethrow;
    }
  }

  Future<Session> validSession() async {
    final s = session;
    if (s == null) throw AuthError('Entre na sua conta.');
    if (s.expiringSoon) return _refresh(s.refreshToken);
    return s;
  }

  // ------------------------------------------------------------------ contas

  /// Cria a conta. Devolve a sessão se o servidor não exigir confirmação de e-mail; senão, null.
  Future<Session?> signUp({required String email, required String password, required String name, required String phone}) async {
    final data = await _send('POST', '/auth/v1/signup', body: {
      'email': email.trim().toLowerCase(),
      'password': password,
      'data': {'name': name.trim(), 'phone': phone, 'accepted_terms': true},
    }) as Map<String, dynamic>;
    if (data['access_token'] != null) {
      final s = Session.fromAuth(data);
      await _saveSession(s);
      return s;
    }
    return null;
  }

  Future<Session> signIn(String email, String password) async {
    final data = await _send('POST', '/auth/v1/token?grant_type=password', body: {'email': email.trim().toLowerCase(), 'password': password});
    final s = Session.fromAuth(data as Map<String, dynamic>);
    await _saveSession(s);
    return s;
  }

  /// Confirma o cadastro (type = 'signup') ou a recuperação de senha (type = 'recovery') com o código do e-mail.
  Future<Session> verifyCode(String email, String code, {required String type}) async {
    final data = await _send('POST', '/auth/v1/verify', body: {'email': email.trim().toLowerCase(), 'token': code.trim(), 'type': type});
    final s = Session.fromAuth(data as Map<String, dynamic>);
    await _saveSession(s);
    return s;
  }

  Future<void> resendSignupCode(String email) => _send('POST', '/auth/v1/resend', body: {'type': 'signup', 'email': email.trim().toLowerCase()});

  Future<void> sendRecoveryCode(String email) => _send('POST', '/auth/v1/recover', body: {'email': email.trim().toLowerCase()});

  Future<void> changePassword(String newPassword) => _send('PUT', '/auth/v1/user', body: {'password': newPassword}, auth: true);

  Future<void> signOut() async {
    try {
      if (session != null) await _send('POST', '/auth/v1/logout', auth: true);
    } catch (_) {
      // Sem internet: a sessão local é apagada mesmo assim.
    }
    await _saveSession(null);
  }

  // ------------------------------------------------------------------ perfil e administração

  Future<AccountProfile> myProfile() async {
    final s = await validSession();
    final data = await _send('GET', '/rest/v1/profiles?id=eq.${s.userId}&select=*', auth: true) as List;
    if (data.isEmpty) throw AuthError('Perfil não encontrado. Fale com o suporte.');
    return AccountProfile.fromJson(data.first as Map<String, dynamic>);
  }

  Future<void> updateMyProfile({required String name, required String phone}) async {
    final s = await validSession();
    await _send('PATCH', '/rest/v1/profiles?id=eq.${s.userId}', body: {'name': name.trim(), 'phone': phone}, auth: true, extra: {'Prefer': 'return=minimal'});
  }

  /// Exclui a conta no servidor (direito do titular — LGPD, art. 18).
  Future<void> deleteMyAccount() async {
    await _send('POST', '/rest/v1/rpc/delete_my_account', body: const {}, auth: true);
    await _saveSession(null);
  }

  /// Lista de contas (o servidor só responde para administradores).
  Future<List<AccountProfile>> listProfiles() async {
    final data = await _send('GET', '/rest/v1/profiles?select=*&order=created_at.desc&limit=1000', auth: true) as List;
    return [for (final p in data) AccountProfile.fromJson(p as Map<String, dynamic>)];
  }

  /// Concede ou retira o papel de administrador (o servidor só aceita do dono).
  Future<void> setRole(String userId, Role role) =>
      _send('POST', '/rest/v1/rpc/set_role', body: {'target': userId, 'new_role': role.name}, auth: true);

  /// Classifica um aluno (o servidor só aceita do dono e só as classificações manuais).
  Future<void> setPlan(String userId, Plan plan, String note) =>
      _send('POST', '/rest/v1/rpc/set_plan', body: {'target': userId, 'new_plan': plan.name, 'note': note.trim()}, auth: true);

  Future<List<AuditEntry>> auditLog() async {
    final data = await _send('GET', '/rest/v1/audit_log_view?select=*&order=at.desc&limit=50', auth: true) as List;
    return [
      for (final r in data.cast<Map<String, dynamic>>())
        AuditEntry(
          DateTime.tryParse(r['at'] as String? ?? '')?.toLocal() ?? DateTime.now(),
          r['actor_email'] as String? ?? '',
          r['action'] as String? ?? '',
          r['target_email'] as String? ?? '',
          r['detail'] as String? ?? '',
        ),
    ];
  }

  // ------------------------------------------------------------------ progresso na nuvem

  @override
  Future<RemoteStudy?> fetchStudy({bool withData = true}) async {
    try {
      final s = await validSession();
      final cols = withData ? 'data,version,device,updated_at' : 'version,device,updated_at';
      final rows = await _send('GET', '/rest/v1/study_data?select=$cols&user_id=eq.${s.userId}', auth: true) as List;
      if (rows.isEmpty) return null;
      final r = rows.first as Map<String, dynamic>;
      return RemoteStudy(
        version: (r['version'] as num).toInt(),
        device: r['device'] as String? ?? '',
        updatedAt: DateTime.tryParse(r['updated_at'] as String? ?? '')?.toLocal() ?? DateTime.now(),
        data: withData ? (r['data'] as Map).cast<String, dynamic>() : null,
      );
    } on AuthError catch (e) {
      throw _studyError(e);
    }
  }

  @override
  Future<int> saveStudy(Map<String, dynamic> data, int baseVersion, String device) async {
    try {
      final v = await _send('POST', '/rest/v1/rpc/save_study',
          body: {'new_data': data, 'base_version': baseVersion, 'device_name': device}, auth: true);
      return (v as num).toInt();
    } on AuthError catch (e) {
      throw _studyError(e);
    }
  }

  Exception _studyError(AuthError e) {
    if (e.offline) return StudyOffline();
    if (e.code == 'TS409' || e.code == '23505') return StudyConflict();
    if (const {'PGRST202', 'PGRST205', '42P01', '42883'}.contains(e.code)) return StudyUnavailable();
    return e;
  }

  // ------------------------------------------------------------------ catálogo extra

  @override
  Future<({Map<String, dynamic> data, int version})?> fetchCatalog() async {
    final rows = await _send('GET', '/rest/v1/catalog_docs?select=data,version&key=eq.extras', auth: session != null) as List;
    if (rows.isEmpty) return null;
    final r = rows.first as Map<String, dynamic>;
    return (data: (r['data'] as Map).cast<String, dynamic>(), version: (r['version'] as num).toInt());
  }

  @override
  Future<int> saveCatalog(Map<String, dynamic> data, int baseVersion, String note) async {
    final v = await _send('POST', '/rest/v1/rpc/save_catalog',
        body: {'new_data': data, 'base_version': baseVersion, 'note': note}, auth: true);
    return (v as num).toInt();
  }
}
