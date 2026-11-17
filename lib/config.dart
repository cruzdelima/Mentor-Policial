/// Configuração do servidor de contas (Supabase).
///
/// Os valores entram na compilação por `--dart-define` (o workflow do GitHub lê as variáveis
/// SUPABASE_URL e SUPABASE_KEY do repositório). Sem eles, o app funciona sem contas, como nas
/// versões anteriores.
///
/// A chave usada aqui é a **publishable/anon key**: ela é pública por definição e só dá acesso ao
/// que as regras de segurança do banco (RLS) permitem. **Nunca** coloque no app a chave
/// `service_role`/`secret`: ela ignora todas as regras e daria acesso total ao banco.
library;

const kSupabaseUrl = String.fromEnvironment('SUPABASE_URL');
const kSupabaseKey = String.fromEnvironment('SUPABASE_KEY');

/// Página pública com os Termos de Uso e a Política de Privacidade.
const kTermsUrl = 'https://github.com/cruzdelima/Mentor-Policial/blob/main/docs/TERMOS_E_PRIVACIDADE.md';

bool get kAccountsEnabled => kSupabaseUrl.isNotEmpty && kSupabaseKey.isNotEmpty;
