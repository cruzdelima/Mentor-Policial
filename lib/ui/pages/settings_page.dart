import 'package:flutter/material.dart';

import '../../core/models.dart';
import '../../data/storage.dart';
import '../../state/app_state.dart';
import '../dialogs.dart';
import '../profile_editors.dart';
import '../theme.dart';
import '../widgets.dart';

class SettingsPage extends StatefulWidget {
  const SettingsPage({super.key});

  @override
  State<SettingsPage> createState() => _SettingsPageState();
}

class _SettingsPageState extends State<SettingsPage> {
  late Profile draft;
  final name = TextEditingController();
  final target = TextEditingController();
  bool _init = false;

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    if (!_init) {
      _init = true;
      _reset();
    }
  }

  void _reset() {
    final app = AppScope.read(context);
    draft = app.profile.copy();
    name.text = draft.name;
    target.text = draft.targetName;
  }

  @override
  void dispose() {
    name.dispose();
    target.dispose();
    super.dispose();
  }

  bool _dirty(AppController app) {
    final a = app.profile.toJson().toString();
    final b = (draft.copy()
          ..name = name.text.trim()
          ..targetName = target.text.trim())
        .toJson()
        .toString();
    return a != b;
  }

  void _save(AppController app) {
    final p = draft.copy()
      ..name = name.text.trim()
      ..targetName = target.text.trim();
    final replans = p.planSignature != app.profile.planSignature;
    app.updateProfile(p);
    toast(context, replans ? 'Salvo. Cronograma recalculado a partir de hoje.' : 'Alterações salvas.');
    setState(() {});
  }

  @override
  Widget build(BuildContext context) {
    final app = AppScope.of(context);
    final dirty = _dirty(app);
    final replans = (draft.copy()).planSignature != app.profile.planSignature;
    return Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
      PageHeader(
        title: 'Ajustes',
        subtitle: 'Perfil, concurso, rotina e seus dados. Mudanças na rotina recalculam o cronograma a partir de hoje — nada do que você já fez se perde.',
        actions: [
          if (dirty) ...[
            TextButton(
              onPressed: () => setState(_reset),
              child: const Text('DESCARTAR'),
            ),
            ElevatedButton.icon(onPressed: () => _save(app), icon: const Icon(Icons.save_outlined, size: 18), label: Text(replans ? 'SALVAR E REPLANEJAR' : 'SALVAR')),
          ],
        ],
      ),
      Expanded(
        child: ListView(padding: const EdgeInsets.fromLTRB(28, 0, 28, 40), children: [
          Panel(
            child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              const SectionLabel('Perfil e concurso'),
              Wrap(spacing: 16, runSpacing: 16, children: [
                SizedBox(width: 300, child: TextField(controller: name, onChanged: (_) => setState(() {}), decoration: const InputDecoration(labelText: 'Nome'))),
                SizedBox(
                  width: 300,
                  child: TextField(
                    controller: target,
                    onChanged: (_) => setState(() {}),
                    decoration: const InputDecoration(labelText: 'Concurso específico (opcional)', hintText: 'Ex.: PF 2027'),
                  ),
                ),
              ]),
              const SizedBox(height: 18),
              Row(children: [
                Pill(draft.esfera.toUpperCase(), color: AppColors.esfera(draft.esfera), filled: true),
                const SizedBox(width: 10),
                Expanded(
                  child: Text('${app.catalog.career(draft.careerCode).name} · ${app.catalog.cargo(draft.optionId).name}', style: AppText.strong()),
                ),
                OutlinedButton.icon(
                  onPressed: () => _changeTarget(context),
                  icon: const Icon(Icons.swap_horiz, size: 18),
                  label: const Text('TROCAR CONCURSO / CARGO'),
                ),
              ]),
            ]),
          ),
          const SizedBox(height: 16),
          Panel(
            child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              const SectionLabel('Rotina e nível'),
              RoutineEditor(catalog: app.catalog, profile: draft, today: app.today, onChanged: () => setState(() {})),
            ]),
          ),
          const SizedBox(height: 16),
          const _DataPanel(),
          const SizedBox(height: 16),
          const _AboutPanel(),
        ]),
      ),
    ]);
  }

  Future<void> _changeTarget(BuildContext context) async {
    final app = AppScope.read(context);
    final cat = app.catalog;
    var esfera = draft.esfera, career = draft.careerCode, option = draft.optionId;
    final ok = await showDialog<bool>(
      context: context,
      builder: (ctx) => StatefulBuilder(builder: (ctx, setState) {
        final careerObj = career.isEmpty ? null : cat.career(career);
        return AlertDialog(
          title: Text('TROCAR CONCURSO E CARGO', style: AppText.h2()),
          content: SizedBox(
            width: 1080,
            height: 620,
            child: SingleChildScrollView(
              child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                Text('ESFERA', style: AppText.label(AppColors.gold)),
                const SizedBox(height: 10),
                EsferaPicker(
                  catalog: cat,
                  value: esfera,
                  onChanged: (e) => setState(() {
                    if (e != esfera) {
                      career = '';
                      option = '';
                    }
                    esfera = e;
                  }),
                ),
                const SizedBox(height: 22),
                Text('CONCURSO', style: AppText.label(AppColors.gold)),
                const SizedBox(height: 10),
                CareerPicker(
                  catalog: cat,
                  esfera: esfera,
                  value: career.isEmpty ? null : career,
                  onChanged: (c) => setState(() {
                    if (c != career) option = '';
                    career = c;
                    final co = cat.career(c);
                    if (co.cargos.length == 1) option = co.cargos.first.id;
                  }),
                ),
                if (careerObj != null) ...[
                  const SizedBox(height: 22),
                  Text('CARGO', style: AppText.label(AppColors.gold)),
                  const SizedBox(height: 10),
                  CargoPicker(catalog: cat, career: careerObj, value: option.isEmpty ? null : option, onChanged: (o) => setState(() => option = o)),
                ],
              ]),
            ),
          ),
          actions: [
            TextButton(onPressed: () => Navigator.pop(ctx, false), child: const Text('CANCELAR')),
            ElevatedButton(onPressed: option.isEmpty ? null : () => Navigator.pop(ctx, true), child: const Text('USAR ESTE CARGO')),
          ],
        );
      }),
    );
    if (ok == true) {
      setState(() {
        draft.esfera = esfera;
        draft.careerCode = career;
        draft.optionId = option;
      });
    }
  }
}

class _DataPanel extends StatelessWidget {
  const _DataPanel();

  @override
  Widget build(BuildContext context) {
    final app = AppScope.of(context);
    return Panel(
      child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
        const SectionLabel('Seus dados'),
        Text('Tudo fica salvo neste computador. Uma cópia de segurança diária é feita automaticamente (últimos 15 dias).', style: AppText.small()),
        const SizedBox(height: 8),
        SelectableText(app.storage.dir.path, style: AppText.small(AppColors.dim)),
        const SizedBox(height: 14),
        Wrap(spacing: 10, runSpacing: 10, children: [
          OutlinedButton.icon(
            onPressed: () => openExternal(app.storage.dir.path),
            icon: const Icon(Icons.folder_open_outlined, size: 18),
            label: const Text('ABRIR PASTA DE DADOS'),
          ),
          OutlinedButton.icon(
            onPressed: () async {
              try {
                final path = await app.exportBackup();
                if (context.mounted) toast(context, 'Backup salvo em: $path');
              } catch (e) {
                if (context.mounted) toast(context, 'Falha ao exportar: $e');
              }
            },
            icon: const Icon(Icons.download_outlined, size: 18),
            label: const Text('EXPORTAR BACKUP'),
          ),
          OutlinedButton.icon(
            onPressed: () => _import(context),
            icon: const Icon(Icons.upload_outlined, size: 18),
            label: const Text('IMPORTAR BACKUP'),
          ),
          OutlinedButton.icon(
            style: OutlinedButton.styleFrom(foregroundColor: AppColors.red, side: const BorderSide(color: AppColors.red)),
            onPressed: () async {
              final ok = await confirm(
                context,
                'Apagar tudo',
                'Perfil, diário, missões concluídas e anotações serão apagados deste computador. Exporte um backup antes se quiser guardar.',
                ok: 'APAGAR TUDO',
                danger: true,
              );
              if (ok) app.resetAll();
            },
            icon: const Icon(Icons.delete_forever_outlined, size: 18),
            label: const Text('APAGAR TUDO'),
          ),
        ]),
      ]),
    );
  }

  Future<void> _import(BuildContext context) async {
    final app = AppScope.read(context);
    final c = TextEditingController();
    final path = await showDialog<String>(
      context: context,
      builder: (ctx) => AlertDialog(
        title: Text('IMPORTAR BACKUP', style: AppText.h2()),
        content: SizedBox(
          width: 520,
          child: Column(mainAxisSize: MainAxisSize.min, crossAxisAlignment: CrossAxisAlignment.stretch, children: [
            Text('Cole o caminho do arquivo .json exportado (no Windows: clique com o botão direito no arquivo › "Copiar como caminho").',
                style: AppText.small()),
            const SizedBox(height: 12),
            TextField(controller: c, autofocus: true, decoration: const InputDecoration(labelText: 'Caminho do backup')),
            const SizedBox(height: 8),
            Text('Os dados atuais serão substituídos.', style: AppText.small(AppColors.amber)),
          ]),
        ),
        actions: [
          TextButton(onPressed: () => Navigator.pop(ctx), child: const Text('CANCELAR')),
          ElevatedButton(onPressed: () => Navigator.pop(ctx, c.text), child: const Text('IMPORTAR')),
        ],
      ),
    );
    if (path == null || path.trim().isEmpty) return;
    try {
      await app.importBackup(path);
      if (context.mounted) toast(context, 'Backup importado.');
    } catch (e) {
      if (context.mounted) toast(context, 'Não foi possível importar: $e');
    }
  }
}

class _AboutPanel extends StatelessWidget {
  const _AboutPanel();

  @override
  Widget build(BuildContext context) {
    final app = AppScope.of(context);
    return Panel(
      child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
        const SectionLabel('Sobre'),
        Row(children: [
          const BadgeLogo(size: 44),
          const SizedBox(width: 14),
          Expanded(
            child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              Text('MENTOR POLICIAL · v$kAppVersion', style: AppText.h3()),
              Text('$kAppChannel · catálogo ${app.catalog.version} · ${app.content.items.length} material(is) de conteúdo', style: AppText.small()),
            ]),
          ),
        ]),
        const SizedBox(height: 12),
        Text(
          'Versão de testes: anote o que travou, o que ficou confuso e o que faria você usar todos os dias — e envie ao autor. '
          'Os pesos e assuntos seguem o núcleo comum dos últimos editais; confira sempre o edital do seu concurso.',
          style: AppText.small(),
        ),
        const SizedBox(height: 8),
        Text('Fontes tipográficas: Barlow e Barlow Condensed (SIL Open Font License).', style: AppText.small(AppColors.dim)),
      ]),
    );
  }
}
