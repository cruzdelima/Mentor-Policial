# Segurança e proteção de dados

Este documento define **o que o Taticum guarda, onde guarda e quem pode ver**, e as regras que todo programador deve seguir. Qualquer mudança que contrarie estas regras precisa de aprovação do dono.

## 1. Mapa dos dados

| Dado | Onde fica | Quem acessa |
|---|---|---|
| E-mail, nome, celular, papel, plano | Supabase (Postgres, região São Paulo) | O próprio aluno; administradores (somente leitura) |
| Senha | Supabase Auth, **apenas o hash bcrypt** | Ninguém (nem o dono, nem o Supabase consegue ler a senha) |
| Sessão (refresh token) | Computador do aluno: `…/Taticum/sessao.json` | O usuário do sistema operacional |
| Cronograma, diário, questões, anotações | Computador do aluno: `…/Taticum/contas/<id>/dados.json` + backups diários | O usuário do sistema operacional |
| Registro de auditoria (quem alterou permissões, exclusões de conta) | Supabase | Administradores (somente leitura); ninguém altera ou apaga pelo app |

**Princípio da minimização (LGPD, art. 6º, III):** o app coleta só o necessário. Não coletar CPF, endereço, data de nascimento ou documentos sem necessidade clara e sem atualizar a Política de Privacidade.

## 2. Controles já implementados

**Contas e senhas**
- Senha com no mínimo 8 caracteres, maiúscula, minúscula, número e caractere especial. A regra é validada no app **e** no servidor, e o app recusa senhas comuns demais.
- Confirmação do e-mail por código antes do primeiro acesso.
- Recuperação de senha por código enviado ao e-mail, sem revelar se o e-mail existe.
- Limites de tentativas do Supabase contra força bruta.
- O app nunca grava a senha; guarda só o token de sessão, renovado automaticamente.

**Autorização (no servidor, não no app)**
- **Row Level Security** em todas as tabelas. O aluno lê apenas o próprio perfil; administradores leem a lista de contas.
- O aluno só pode alterar **nome e celular**. Papel e plano são bloqueados por permissão de coluna.
- O papel de quem se cadastra é sempre *aluno*, mesmo que alguém altere o app.
- Só o **dono** concede ou remove administradores, pela função `set_role`, e toda alteração vai para a auditoria.
- Existe apenas **um dono**, e ele não pode ser rebaixado nem excluído pelo app.
- Essas regras têm testes automatizados: `supabase/tests/rodar.sh`.

**Transporte e distribuição**
- Toda comunicação com o servidor usa HTTPS (TLS). O app recusa conexões com certificado inválido.
- O instalador é gerado pelo GitHub Actions a partir do código do repositório. Ninguém compila "na própria máquina" para distribuir.

**Direitos do titular (LGPD, art. 18)**
- O aluno pode **editar** os dados e **excluir a conta** pelo app (Ajustes › Minha conta). A exclusão apaga a conta do servidor e os estudos daquele computador.

## 3. Regras para programadores

1. **Nunca** coloque no código, no GitHub ou em mensagens a chave `secret`/`service_role` do Supabase, senhas de banco, senhas de SMTP ou tokens de pagamento. Use as *Variables/Secrets* do GitHub e as variáveis de ambiente do Supabase.
2. **Toda tabela nova nasce com RLS ligado** (`alter table … enable row level security`) e com `revoke all … from anon, authenticated` seguido apenas dos `grant` necessários.
3. **Toda decisão de permissão é do servidor.** Esconder um botão no app não é segurança; o banco precisa recusar.
4. Funções `security definer` sempre com `set search_path = ''` e nomes qualificados (`public.tabela`).
5. Mudança no banco = novo arquivo em `supabase/migrations/` (nunca editar um já aplicado) + teste em `supabase/tests/`.
6. Dependências novas (`pubspec.yaml`) só de fontes conhecidas, com versão fixa, e mencionadas no Pull Request.
7. Não registrar dados pessoais em logs (`print`/`debugPrint`) — e-mail, telefone, tokens.
8. Pull Requests passam pelos testes automáticos e pela revisão de outra pessoa antes de entrar na `main`.

## 4. Configurações obrigatórias do dono

- Autenticação em dois fatores no **GitHub**, no **Supabase** e no e-mail usado nesses serviços.
- No GitHub: **Settings › Branches › Add branch ruleset** para `main` — exigir Pull Request, 1 aprovação e os testes passando; bloquear *force push*.
- Supabase com *Confirm email* ligado, regras de senha conforme `CONTAS_SUPABASE.md` e SMTP próprio.
- Antes de cobrar assinaturas: plano **Pro** do Supabase (backups diários e sem pausa) e *Leaked password protection* ligado.

## 5. Limitações conhecidas (próximos passos)

| Limitação | Risco | Solução planejada |
|---|---|---|
| Token de sessão em arquivo comum (protegido pelas permissões do usuário do sistema) | Malware no computador do aluno poderia copiá-lo | Usar o cofre do sistema (Windows Credential Manager / Keychain do macOS) via `flutter_secure_storage` |
| Estudos guardados só no computador | Perda se o computador quebrar (há backups locais e exportação manual) | Sincronização opcional com o servidor, criptografada, com tabela própria e RLS |
| Instalador sem certificado digital | Avisos do Windows/macOS; usuário não consegue verificar o editor | Publicar na Microsoft Store (assina gratuitamente) e obter Developer ID da Apple |
| Sem verificação de celular por SMS | Telefone informado pode estar errado | Avaliar verificação por SMS (custo por mensagem) quando houver cobrança |
| Sem autenticação em dois fatores para administradores no app | Senha vazada de admin expõe a lista de alunos | Ativar MFA (TOTP) do Supabase e exigir para administradores |

## 6. Incidente de segurança

Se houver suspeita de vazamento ou acesso indevido:
1. **Conter:** trocar imediatamente a chave `secret` e a senha do banco no Supabase (*Project Settings*), revogar sessões (*Authentication › Users*) e remover administradores suspeitos.
2. **Registrar:** o que aconteceu, quando, quais dados e quantos titulares.
3. **Comunicar:** a LGPD (art. 48) exige comunicar à **ANPD** e aos titulares incidentes que possam causar risco ou dano relevante. Procure orientação jurídica.
4. **Corrigir** a causa e documentar neste arquivo.
