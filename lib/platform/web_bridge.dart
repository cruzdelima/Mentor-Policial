/// Recursos do navegador (localStorage, fetch, abrir aba). No desktop, a versão "stub" nunca é chamada.
library;

export 'web_bridge_stub.dart' if (dart.library.js_interop) 'web_bridge_web.dart';
