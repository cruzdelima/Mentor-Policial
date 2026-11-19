/// Desktop: estes recursos só existem no navegador.
library;

class WebResponse {
  WebResponse(this.status, this.text);
  final int status;
  final String text;
}

Never _unsupported() => throw UnsupportedError('Disponível apenas na versão para navegador.');

String? webStorageGet(String key) => _unsupported();
void webStorageSet(String key, String value) => _unsupported();
void webStorageRemove(String key) => _unsupported();
List<String> webStorageKeys() => _unsupported();
Future<WebResponse> webFetch(String method, String url, Map<String, String> headers, String? body) => _unsupported();
void webOpen(String url) => _unsupported();
void webDownload(String fileName, String text) => _unsupported();
String webBaseUrl() => _unsupported();
Future<String?> webPickText(String accept) => _unsupported();
