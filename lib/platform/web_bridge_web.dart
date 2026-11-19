/// Navegador: localStorage, fetch e abertura de abas, via dart:js_interop (sem pacotes externos).
library;

import 'dart:async';
import 'dart:js_interop';

class WebResponse {
  WebResponse(this.status, this.text);
  final int status;
  final String text;
}

extension type _Storage._(JSObject _) implements JSObject {
  external JSString? getItem(JSString key);
  external void setItem(JSString key, JSString value);
  external void removeItem(JSString key);
  external int get length;
  external JSString? key(int index);
}

@JS('localStorage')
external _Storage get _localStorage;

extension type _Response._(JSObject _) implements JSObject {
  external int get status;
  external JSPromise<JSString> text();
}

extension type _RequestInit._(JSObject _) implements JSObject {
  external factory _RequestInit({JSString method, JSAny? headers, JSString? body, JSString cache});
}

@JS('fetch')
external JSPromise<_Response> _fetch(JSString url, _RequestInit init);

@JS('open')
external JSAny? _open(JSString url, JSString target);

extension type _Location._(JSObject _) implements JSObject {
  external JSString get href;
}

@JS('document.baseURI')
external JSString get _baseUri;

@JS('location')
external _Location get _location;

extension type _Blob._(JSObject _) implements JSObject {
  external factory _Blob(JSArray<JSString> parts, _BlobOptions options);
}

extension type _BlobOptions._(JSObject _) implements JSObject {
  external factory _BlobOptions({JSString type});
}

@JS('URL.createObjectURL')
external JSString _createObjectUrl(_Blob blob);

@JS('URL.revokeObjectURL')
external void _revokeObjectUrl(JSString url);

extension type _Input._(JSObject _) implements JSObject {
  external set type(JSString v);
  external set accept(JSString v);
  external set onchange(JSFunction? f);
  external set oncancel(JSFunction? f);
  external _FileList? get files;
  external void click();
}

extension type _FileList._(JSObject _) implements JSObject {
  external int get length;
  external _File? item(int i);
}

extension type _File._(JSObject _) implements JSObject {
  external JSPromise<JSString> text();
}

extension type _Anchor._(JSObject _) implements JSObject {
  external set href(JSString v);
  external set download(JSString v);
  external void click();
}

@JS('document.createElement')
external _Anchor _createElement(JSString tag);

@JS('document.createElement')
external _Input _createInput(JSString tag);

String? webStorageGet(String key) => _localStorage.getItem(key.toJS)?.toDart;

void webStorageSet(String key, String value) => _localStorage.setItem(key.toJS, value.toJS);

void webStorageRemove(String key) => _localStorage.removeItem(key.toJS);

List<String> webStorageKeys() {
  final out = <String>[];
  final n = _localStorage.length;
  for (var i = 0; i < n; i++) {
    final k = _localStorage.key(i)?.toDart;
    if (k != null) out.add(k);
  }
  return out;
}

Future<WebResponse> webFetch(String method, String url, Map<String, String> headers, String? body) async {
  final res = await _fetch(
    url.toJS,
    _RequestInit(method: method.toJS, headers: headers.jsify(), body: body?.toJS, cache: 'no-store'.toJS),
  ).toDart;
  final text = (await res.text().toDart).toDart;
  return WebResponse(res.status, text);
}

void webOpen(String url) => _open(url.toJS, '_blank'.toJS);

/// Endereço base do app (para montar o link dos arquivos publicados junto com ele).
String webBaseUrl() {
  try {
    return _baseUri.toDart;
  } catch (_) {
    return _location.href.toDart;
  }
}

/// Baixa um arquivo de texto gerado pelo app (ex.: cópia de segurança).
void webDownload(String fileName, String text) {
  final blob = _Blob([text.toJS].toJS, _BlobOptions(type: 'application/json'.toJS));
  final url = _createObjectUrl(blob);
  final a = _createElement('a'.toJS)
    ..href = url
    ..download = fileName.toJS;
  a.click();
  _revokeObjectUrl(url);
}

/// Abre o seletor de arquivos e devolve o texto do arquivo escolhido (null se nada for escolhido).
Future<String?> webPickText(String accept) {
  final done = Completer<String?>();
  final input = _createInput('input'.toJS)
    ..type = 'file'.toJS
    ..accept = accept.toJS;
  input.onchange = ((JSAny _) {
    final files = input.files;
    final f = (files == null || files.length == 0) ? null : files.item(0);
    if (f == null) {
      done.complete(null);
      return;
    }
    f.text().toDart.then((t) => done.complete(t.toDart), onError: (Object e) => done.completeError(e));
  }).toJS;
  input.oncancel = ((JSAny _) {
    if (!done.isCompleted) done.complete(null);
  }).toJS;
  input.click();
  return done.future;
}
