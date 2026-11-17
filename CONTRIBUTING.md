# Como contribuir com o Mentor Policial

Guia para programadores convidados pelo dono do projeto.

## Acesso

| O quê | Como o dono concede | Permissão recomendada |
|---|---|---|
| Código | GitHub › *Settings › Collaborators* › *Add people* | **Write** (nunca *Admin*) |
| Banco de testes | Supabase › organização › *Team* › *Invite* | **Developer**, no projeto de **testes** |
| Banco de produção (dados reais) | Só se indispensável | **Read-only**, por tempo limitado |
| Administração dentro do app | Menu ADMIN › *Tornar admin* | Só para quem gerencia alunos. Programar **não** exige isso |

Ative a autenticação em dois fatores no GitHub e no Supabase antes de receber acesso.

## Preparar o ambiente

1. Instale o **Flutter 3.50** (canal stable) e o **Git**. No Windows, instale também o *Visual Studio 2022* com "Desenvolvimento para desktop com C++"; no Mac, o *Xcode*.
2. Clone e gere as pastas de plataforma (elas não ficam no repositório):
   ```bash
   git clone https://github.com/cruzdelima/Mentor-Policial.git
   cd Mentor-Policial
   flutter create --platforms=windows,macos --org br.com.mentorpolicial --project-name mentor_policial .
   rm test/widget_test.dart
   cp -R platform/windows/. windows/     # no Mac: cp -R platform/macos/. macos/
   flutter pub get
   flutter run -d windows                 # ou: -d macos
   ```
3. Para testar contas, use o **projeto de testes** do Supabase:
   `flutter run -d windows --dart-define=SUPABASE_URL=... --dart-define=SUPABASE_KEY=...`

Leia [`docs/ARQUITETURA.md`](docs/ARQUITETURA.md) e [`docs/SEGURANCA.md`](docs/SEGURANCA.md) antes de começar.

## Fluxo de trabalho

1. Crie um ramo a partir da `main`: `git checkout -b feature/descricao-curta` (ou `fix/...`, `content/...`).
2. Faça commits pequenos, com mensagem em português dizendo **o que** e **por quê**.
3. Antes de enviar:
   ```bash
   flutter analyze        # sem erros
   flutter test           # todos passando
   ```
4. Abra um **Pull Request** para a `main` explicando a mudança, como testou e, se mexeu em telas, com prints.
5. O GitHub roda análise, testes e build de Windows e macOS. O PR só entra com tudo verde e a aprovação de outra pessoa.
6. Não aumente o número da versão no seu PR: o dono decide quando publicar.

## Padrões de código

- Dart com `flutter analyze` limpo; formatação com `dart format --line-length 160`.
- Regras de negócio em `lib/core/` (sem importar Flutter) e testadas em `test/`.
- Textos da interface em português do Brasil, no tom do app (direto, sem jargão).
- Cores e fontes só pelo tema (`lib/ui/theme.dart`); componentes reutilizáveis em `lib/ui/widgets.dart`.
- Nada de pacotes novos sem discutir no PR (ver `docs/SEGURANCA.md`, regra 6).

## Banco de dados

- Mudança no banco = **novo** arquivo `supabase/migrations/000N_descricao.sql` (nunca altere um já aplicado).
- Toda tabela com RLS, `revoke` amplo e `grant` mínimo; funções `security definer` com `set search_path = ''`.
- Acrescente casos em `supabase/tests/tests.sql` e rode `bash supabase/tests/rodar.sh`.
- Aplique primeiro no projeto de **testes**. A aplicação em produção é feita pelo dono (SQL Editor).

## Conteúdos (apostilas e questões)

- Cada assunto: `tool/content/<assunto>_aprof.py` (estudo inicial, 20 questões) e `<assunto>_resumo.py` (revisão, mapa mental, 10 questões).
- Registre os módulos em `MODULES` (`tool/content/build_content.py`) e as pastas em `pubspec.yaml`.
- Gere com `python3 tool/content/build_content.py`. O gerador recusa gabarito incoerente, número errado de questões e caracteres que a fonte do PDF não tem.
- Texto próprio. Não copie trechos de livros, cursos ou provas; questões de banca, só com fonte (banca, órgão, ano).
- Todo material passa pela revisão do dono antes de ir para uma versão.
