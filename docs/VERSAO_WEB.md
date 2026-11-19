# Versão para navegador (site)

O mesmo código do app gera o site. A cada envio para `main` que passa nos testes, o GitHub Actions
compila a versão web (`flutter build web`) e publica no GitHub Pages.

## Ativar (uma vez só)

1. GitHub › repositório › **Settings › Pages** › *Build and deployment* › **Source: GitHub Actions**.
2. Rode de novo o último build (Actions › execução › *Re-run all jobs*) ou envie qualquer alteração.
3. O site fica em `https://cruzdelima.github.io/Mentor-Policial/`.

## Domínio próprio (app.taticum.com.br)

1. No painel do domínio (onde está o DNS de taticum.com.br), crie um registro **CNAME**:
   nome `app`, valor `cruzdelima.github.io`.
2. GitHub › Settings › **Secrets and variables › Actions › Variables** › nova variável
   `WEB_DOMAIN` = `app.taticum.com.br` (o site passa a ser compilado para a raiz do domínio).
3. GitHub › Settings › Pages › **Custom domain** = `app.taticum.com.br` › Save. Quando o certificado
   ficar pronto (minutos a algumas horas), marque **Enforce HTTPS**.
4. Envie qualquer alteração (ou *Re-run*) para recompilar.

## Como funciona

- **Dados**: ficam no `localStorage` do navegador (prefixo `taticum:`) e na cópia da nuvem da conta
  (`study_data`). Entrar com a mesma conta no computador e no navegador mantém tudo igual.
- **Sessão**: só o *refresh token* fica salvo no navegador (como no app, nunca a senha).
- **PDFs**: publicados junto com o site e abertos numa aba nova.
- **Sem**: pasta de dados, cópia diária em arquivo, pacotes de conteúdo locais, aviso de
  atualização (o site já abre sempre na versão nova) e materiais "PDF do computador" (só links).
- **Backup**: EXPORTAR baixa um `.json`; IMPORTAR abre o seletor de arquivos.
- **Tablet**: funciona na horizontal (testado de 960×600 a 1366×1024). Em pé ainda não é o foco.
- **Código**: `lib/platform/` — `fs.dart` (arquivos no computador, `localStorage` no navegador) e
  `web_bridge*.dart` (fetch, abrir abas, baixar e escolher arquivos via `dart:js_interop`).

## Antes de cobrar assinatura

Hoje os PDFs e o conteúdo ficam públicos no site (assim como no repositório). Antes do lançamento
pago, mover os materiais para armazenamento protegido (ex.: Supabase Storage com acesso por plano).
