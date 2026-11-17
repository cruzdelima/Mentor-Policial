# Taticum · v0.3.0 (beta de testes)

## ⬇ Baixar

| Computador | Link (o download começa na hora) |
|---|---|
| **Windows** | [Taticum-Setup.exe](https://github.com/cruzdelima/Mentor-Policial/releases/latest/download/Taticum-Setup.exe) |
| **Mac** | [Taticum-macOS.dmg](https://github.com/cruzdelima/Mentor-Policial/releases/latest/download/Taticum-macOS.dmg) |

Os links sempre apontam para a versão mais nova. O app avisa quando houver atualização; basta instalar por cima, os dados continuam salvos.

---


Aplicativo para computador (Windows e macOS) que monta e acompanha o **ciclo básico de estudos** para carreiras policiais,
com o método de um aprovado em Agente da Polícia Federal 2025. Feito em Flutter, sem dependências externas.

## O que já tem nesta versão

| Tela | O que faz |
|---|---|
| **Primeiro acesso** | Nome → esfera (federal, estadual, municipal) → concurso → cargo → rotina (horas, dias, dia de revisão, nível, datas) → resumo do plano. |
| **QG** | Contagem regressiva, missões de hoje, números (questões, acerto, nota líquida, constância, edital), projeção da 1ª volta, gráfico semanal, alertas de reforço, ciclo por matéria. |
| **Missões** | Cronograma por dia, semana e trilha completa. Concluir uma missão já lança no diário. Revisão 24h, lei seca, revisão semanal, simulados, revisão de 30 dias e discursiva automáticas. Replanejamento a partir de hoje. |
| **Edital** | Edital verticalizado por cargo: teoria, questões, % de acerto, revisões e status (a estudar, em andamento, reforçar, consolidado). Pular assunto, mudar tamanho (P/M/G) e anotações. |
| **Diário** | Lançamentos automáticos e manuais, filtros, evolução semanal. |
| **Materiais** | Dois materiais por assunto: APROFUNDADO (estudo inicial, teoria completa + 20 questões) e RESUMO (revisão, mapa mental + 10 questões), ambos com PDF. Já incluídos: Ortografia, Vírus e malware, Contabilidade (conceitos) e Princípios fundamentais. Mais os links/PDFs do próprio aluno. |
| **Método** | Os números e as 10 lições do método do autor. |
| **Ajustes** | Perfil, troca de concurso/cargo, rotina, backup (exportar/importar), apagar dados. |

O motor de metas é o mesmo da planilha *Taticum — Ciclo Básico* (validado: PF Agente, 3h, iniciante → 296 missões, fim da 1ª volta em 02/11/2027).

## Como gerar o app para os testadores (sem instalar nada)

1. Crie um repositório **privado** no GitHub e envie esta pasta (com a pasta oculta `.github`).
2. O GitHub Actions roda sozinho: análise + testes automáticos + build de Windows e macOS (~15 min).
3. Baixe em **Actions › última execução › Artifacts**: `Taticum-windows-x64.zip` e `Taticum-macos.zip`.
4. Para publicar uma versão: suba o número em `pubspec.yaml` e em `kAppVersion` (`lib/state/app_state.dart`) e crie uma tag `vX.Y.Z` (vira um *Release* com os dois arquivos).

**Windows:** descompactar e abrir `Taticum.exe` (o SmartScreen pode avisar: *Mais informações › Executar assim mesmo*).
**macOS:** descompactar, clicar com o botão direito em *Taticum › Abrir* (o app ainda não tem assinatura da Apple).

## Como rodar no seu computador (opcional)

Instale o Flutter 3.50 e, na pasta do projeto:

```bash
flutter create --platforms=windows,macos --org br.com.taticum --project-name mentor_policial .
rm test/widget_test.dart                     # arquivo de exemplo criado pelo comando acima
cp -R platform/windows/. windows/            # ícone, título e tamanho mínimo da janela
cp -R platform/macos/. macos/
flutter run -d windows                       # ou: flutter run -d macos
```

## Documentação

| Documento | Para quem |
|---|---|
| [docs/CONTAS_SUPABASE.md](docs/CONTAS_SUPABASE.md) | Dono: ativar contas, e-mail e virar administrador principal |
| [docs/SEGURANCA.md](docs/SEGURANCA.md) | Todos: dados guardados, controles, regras obrigatórias, incidentes |
| [docs/ARQUITETURA.md](docs/ARQUITETURA.md) | Programadores: estrutura, fluxos, comandos, decisões |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Programadores: acesso, ambiente, fluxo de Pull Request, padrões |
| [docs/ASSINATURAS.md](docs/ASSINATURAS.md) | Dono e programadores: plano técnico de cobrança |
| [docs/TERMOS_E_PRIVACIDADE.md](docs/TERMOS_E_PRIVACIDADE.md) | Alunos: termos e política de privacidade (rascunho) |

## Onde ficam os dados do aluno

Tudo é local, em um arquivo JSON com cópia diária automática (15 dias):

* Windows: `%APPDATA%\Taticum\dados.json`
* macOS: `~/Library/Application Support/Taticum/dados.json`

## Estrutura

```
lib/
  core/        motor de metas (planner.dart), modelos, estatísticas, catálogo — Dart puro, testável
  data/        armazenamento local e formato dos conteúdos
  state/       controlador do app (ações, replanejamento, biblioteca de conteúdos)
  ui/          tema, componentes e telas (pages/)
assets/
  catalog/catalog.json             carreiras, cargos, matérias, pesos, 225 assuntos, lei seca e parâmetros do método
  content/index.json               lista de materiais
  content/<pasta do material>/     um material por pasta (material.json + PDF)
platform/      personalizações das pastas windows/ e macos/ (ícone, nome, janela)
tool/          gerador de ícones e verificação do motor
test/          testes automáticos (rodam no GitHub)
```

## Conteúdos

Cada material é uma pasta com `material.json` (blocos de texto, tabelas, destaques, mapa mental e questões) e o PDF.
O mesmo arquivo-fonte (`tool/content/<assunto>_aprof.py` e `<assunto>_resumo.py`) gera o PDF e a tela do app, então o texto revisado vale para os dois.
Para gerar tudo de novo: `python3 tool/content/build_content.py` (requer `reportlab`). Formato em `CONTENT.md`.

Nas missões de teoria o app abre o material aprofundado; nas revisões (24h, semanal e 30 dias), o resumo.

Atualizar conteúdo sem lançar versão nova: coloque a pasta do pacote em `<pasta de dados>/conteudos/<pacote>/`
com um `index.json` — o app carrega na próxima abertura. Videoaulas já têm campo próprio (`videos`).

## Próximos passos sugeridos

1. Rodada de testes com 5 a 10 alunos (anotar travamentos, telas confusas, metas irreais).
2. Conteúdos por prioridade de peso (Português, Informática, Contabilidade/Raciocínio).
3. Microsoft Store: gerar MSIX (pacote `msix`), conta de desenvolvedor individual e envio para certificação.
4. Assinatura Apple (Developer ID + notarização) para o macOS abrir sem aviso.
5. Atualização automática de conteúdo por download (servidor simples ou Releases do GitHub) e aviso de nova versão (`kUpdateManifestUrl`).
6. Monetização futura: conteúdos premium por pacote, mantendo o cronograma gratuito.

## Licenças

Fontes Barlow e Barlow Condensed — SIL Open Font License (`assets/fonts/OFL.txt`).
