# Arquitetura do Taticum

Visão para quem vai programar no app. Leia antes de abrir o primeiro Pull Request.

## Visão geral

```
┌──────────────── Computador do aluno (Windows / macOS) ────────────────┐
│  App Flutter                                                           │
│   ├─ core/      regras puras: catálogo, motor de metas, estatísticas   │
│   ├─ data/      armazenamento local, conteúdos, cliente do Supabase    │
│   ├─ state/     controladores (AppController, AccountController)       │
│   └─ ui/        telas e componentes                                    │
│  Pasta de dados: sessao.json · contas/<id>/dados.json · backups/       │
└───────────────┬────────────────────────────────────┬──────────────────┘
                │ HTTPS (contas)                     │ HTTPS (atualizações)
        ┌───────▼────────┐                   ┌───────▼────────────────┐
        │ Supabase       │                   │ GitHub Releases        │
        │ Auth + Postgres│                   │ instaladores e versões │
        │ RLS, auditoria │                   └────────────────────────┘
        └────────────────┘
```

- **Sem dependências de terceiros no app** além do Flutter (`flutter_localizations`). O cliente do Supabase usa a API REST diretamente (`lib/data/auth.dart`). Isso reduz a superfície de ataque e evita quebras por atualização de pacotes.
- **Estudos ficam no computador** (`dados.json`, gravação atômica + 15 backups diários). O servidor guarda só a conta.
- **Sem servidor configurado**, o app roda sem contas (`lib/config.dart`).

## Pastas do repositório

| Pasta | Conteúdo |
|---|---|
| `lib/core/` | Dart puro, sem Flutter: `catalog.dart` (carreiras, cargos, concursos, matérias, assuntos), `extras.dart` (catálogo extra do editor), `planner.dart` (motor de metas), `stats.dart`, `models.dart`, `validation.dart` (senha, e-mail, telefone) |
| `lib/data/` | `storage.dart` (arquivos locais), `content.dart` (formato dos materiais), `auth.dart` (Supabase), `catalog_store.dart` (cache do catálogo extra) |
| `lib/state/` | `app_state.dart` (estudos do aluno), `account.dart` (sessão, perfil, troca de conta) |
| `lib/ui/` | `theme.dart`, `widgets.dart`, telas em `pages/`, `onboarding.dart`, `auth_screen.dart`, `shell.dart` (menu lateral) |
| `assets/catalog/` | `catalog.json` — gerado por `tool/content/gen_catalog.py` (cargos em `catalog_data.py`/`gen_catalog.py`, concursos embutidos em `contests_data.py`) |
| `assets/content/` | Um material por pasta (`material.json` + PDF), listados em `index.json` |
| `tool/content/` | Fontes dos materiais (`<assunto>_aprof.py`, `<assunto>_resumo.py`) e o gerador `build_content.py` |
| `tool/tutorial/` | Gerador da imagem de instalação |
| `supabase/migrations/` | SQL do banco, em ordem. Nunca editar um arquivo já aplicado: criar o próximo |
| `supabase/tests/` | Testes das regras de segurança do banco |
| `platform/` | Personalizações das pastas `windows/` e `macos/` (ícone, janela, instalador) |
| `test/` | Testes automáticos do app (`flutter test`) |
| `.github/workflows/build.yml` | Análise, testes, build Windows/macOS e publicação de versões |

## Fluxos principais

**Abertura do app**
1. `main.dart`: se `kAccountsEnabled`, cria `AccountController` e tenta renovar a sessão salva.
2. Sem internet e com sessão salva: abre em **modo offline** com os dados locais.
3. Logado: carrega `AppController` com a pasta `contas/<id>/` e mostra o primeiro acesso (perfil de estudo) ou o QG.

**Motor de metas** (`core/planner.dart`)
- `Planner.buildTrail` monta a ordem do ciclo (fila justa ponderada por peso; matérias de peso 2 e 1 entram após 40 h e 100 h).
- `Schedule` distribui a trilha nos dias a partir da data-âncora; `dayPlan(data)` devolve missões e tarefas (revisão 24 h, lei seca, revisão semanal, simulados, revisão de 30 dias, discursiva).
- Validado contra a planilha original (`tool/check_planner.dart` e `test/app_test.dart`).

**Catálogo: embutido + extra** (`core/extras.dart`)
- O app traz `catalog.json` (carreiras, cargos do ciclo básico, matérias, assuntos e concursos pós-edital embutidos).
- O dono/administradores editam um **catálogo extra** na tela *Admin › Catálogo e concursos*. Ele é um JSON (`areas`, `subjects`, `cargos`, `contests`, `hidden`) salvo na tabela `catalog_docs` pela função `save_catalog()` (só admin/dono; versão com trava contra edição simultânea; histórico em `catalog_history`; registro na auditoria).
- Na abertura, o app aplica o cache local (`catalogo_extra.json`) e busca a versão publicada em segundo plano. `applyExtras` substitui itens de mesmo id e ignora itens mal formados.
- **Concurso pós-edital** = um "cargo" com `contest` (banca, data da prova, questões por matéria, assuntos na ordem do edital). Assuntos são `ref` a um assunto do ciclo básico (aproveita PDFs e progresso) ou exclusivos (`<concurso>:<slug>`). `Catalog.topicApplies` decide o que entra no plano.
- Se um concurso some do catálogo, o aluno volta ao cargo de referência (`Profile.baseOptionId`) sem perder nada.

**Conteúdos**
- Cada assunto tem dois materiais: `aprofundado` (estudo inicial, 20 questões) e `resumo` (revisão, mapa mental, 10 questões).
- O mesmo arquivo-fonte em `tool/content/` gera o PDF e o `material.json` exibido no app.
- Novas pastas de conteúdo precisam ser listadas em `pubspec.yaml` (seção `assets`).

## Comandos

```bash
flutter pub get
flutter analyze
flutter test
# rodar com contas (valores do seu projeto de TESTE no Supabase):
flutter run -d windows --dart-define=SUPABASE_URL=https://xxxx.supabase.co --dart-define=SUPABASE_KEY=sb_publishable_xxx
# gerar conteúdos (requer Python 3 + reportlab + fonttools):
python3 tool/content/build_content.py
# testar o banco (requer PostgreSQL local):
bash supabase/tests/rodar.sh
```

## Publicar uma versão

1. Aumente `version:` em `pubspec.yaml` e `kAppVersion` em `lib/state/app_state.dart` (mesmo número).
2. Faça o merge na `main`. O workflow testa, gera os instaladores e cria o Release `vX.Y.Z` sozinho.
3. Os apps instalados mostram a faixa de atualização.

## Decisões registradas

| Decisão | Motivo |
|---|---|
| Flutter desktop (Windows + macOS) | Um código só; foco no computador (celular distrai) |
| Supabase para contas | Auth pronto com hash bcrypt, regras de senha, RLS no Postgres, região São Paulo, plano gratuito para o beta |
| REST direto em vez do pacote `supabase_flutter` | Zero dependências; controle total do que é enviado |
| Estudos locais | Funciona offline; dados sensíveis de desempenho não saem do computador por padrão |
| Papéis no banco (`student`/`admin`/`owner`) | Autorização decidida no servidor, auditável |
| Catálogo extra em JSON único, aplicado sobre o embutido | O dono cadastra concursos sem nova versão do app; um documento só é simples de versionar, auditar e desfazer |
