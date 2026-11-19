import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../../core/bancas.dart';
import '../../core/catalog.dart';
import '../../core/dates.dart';
import '../../core/extras.dart';
import '../../data/auth.dart';
import '../../state/app_state.dart';
import '../dialogs.dart';
import '../theme.dart';
import '../widgets.dart';

/// Editor do catálogo (dono e administradores): áreas, cargos do ciclo básico, matérias e
/// concursos pós-edital. Tudo é montado num rascunho e só vale para os alunos ao PUBLICAR.
class CatalogEditor extends StatefulWidget {
  const CatalogEditor({super.key});

  @override
  State<CatalogEditor> createState() => _CatalogEditorState();
}

const _palette = [
  'FCA5A5', 'FDBA74', 'FDE047', 'BEF264', '86EFAC', '5EEAD4', '7DD3FC', '93C5FD',
  'A5B4FC', 'C4B5FD', 'F0ABFC', 'F9A8D4', 'E0BE94', 'CBD5E1',
];

class _CatalogEditorState extends State<CatalogEditor> {
  late Map<String, dynamic> draft;
  bool loading = true;
  bool saving = false;
  String? error;

  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addPostFrameCallback((_) => _reload());
  }

  Future<void> _reload() async {
    final app = AppScope.read(context);
    setState(() {
      loading = true;
      error = null;
    });
    await app.refreshCatalog();
    if (!mounted) return;
    setState(() {
      draft = cloneJson(normalizeExtras(app.extras));
      loading = false;
    });
  }

  bool _dirty(AppController app) => jsonEncode(normalizeExtras(app.extras)) != jsonEncode(normalizeExtras(draft));

  Catalog? _preview(AppController app) {
    try {
      return Catalog.fromJson(app.catalogBase, extras: draft);
    } catch (_) {
      return null;
    }
  }

  List<Map<String, dynamic>> _list(String k) => (draft[k] as List).cast<Map<String, dynamic>>();
  List<String> get _hidden => (draft['hidden'] as List).cast<String>();

  void _upsert(String k, Map<String, dynamic> item, String key) {
    setState(() {
      final l = _list(k);
      final i = l.indexWhere((x) => x[key] == item[key]);
      if (i >= 0) {
        l[i] = item;
      } else {
        l.add(item);
      }
      _hidden.remove(item[key]);
    });
  }

  /// Remove um item do rascunho; se for do catálogo embutido, ele fica oculto.
  void _remove(String k, String id, String key, {required bool builtin}) {
    setState(() {
      _list(k).removeWhere((x) => x[key] == id);
      if (builtin && !_hidden.contains(id)) _hidden.add(id);
    });
  }

  bool _isBuiltinOption(AppController app, String id) {
    final base = Catalog.fromJson(app.catalogBase);
    return base.hasOption(id);
  }

  Future<void> _publish(AppController app) async {
    final note = TextEditingController();
    final ok = await showDialog<bool>(
      context: context,
      builder: (ctx) => AlertDialog(
        title: Text('PUBLICAR PARA TODOS OS ALUNOS', style: AppText.h2()),
        content: SizedBox(
          width: 480,
          child: Column(mainAxisSize: MainAxisSize.min, crossAxisAlignment: CrossAxisAlignment.start, children: [
            Text('As mudanças chegam aos alunos na próxima vez que abrirem o app (com internet). '
                'Quem já estuda para um concurso removido volta automaticamente ao ciclo básico, sem perder nada.',
                style: AppText.body(AppColors.muted)),
            const SizedBox(height: 14),
            TextField(controller: note, maxLength: 150, decoration: const InputDecoration(labelText: 'O que mudou? (vai para a auditoria)')),
          ]),
        ),
        actions: [
          TextButton(onPressed: () => Navigator.pop(ctx, false), child: const Text('CANCELAR')),
          ElevatedButton(onPressed: () => Navigator.pop(ctx, true), child: const Text('PUBLICAR')),
        ],
      ),
    );
    if (ok != true || !mounted) return;
    setState(() => saving = true);
    try {
      await app.publishCatalog(normalizeExtras(draft), note.text.trim());
      if (mounted) {
        toast(context, 'Catálogo publicado (versão ${app.extrasVersion}).');
        setState(() => draft = cloneJson(normalizeExtras(app.extras)));
      }
    } on AuthError catch (e) {
      if (mounted) toast(context, e.message);
    } catch (e) {
      if (mounted) toast(context, 'Não foi possível publicar: $e');
    } finally {
      if (mounted) setState(() => saving = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    final app = AppScope.of(context);
    if (loading) return const Center(child: CircularProgressIndicator());
    final preview = _preview(app);
    final dirty = _dirty(app);
    if (preview == null) {
      return Padding(
        padding: const EdgeInsets.all(28),
        child: Panel(
          borderColor: AppColors.red,
          child: Row(children: [
            Expanded(child: Text('O rascunho tem um erro e não monta o catálogo. Descarte as alterações.', style: AppText.body(AppColors.red))),
            TextButton(onPressed: _reload, child: const Text('DESCARTAR')),
          ]),
        ),
      );
    }
    final base = Catalog.fromJson(app.catalogBase);
    return ListView(padding: const EdgeInsets.fromLTRB(28, 0, 28, 40), children: [
      Panel(
        accent: dirty ? AppColors.amber : AppColors.green,
        child: Row(children: [
          Icon(dirty ? Icons.edit_note : Icons.cloud_done_outlined, color: dirty ? AppColors.amber : AppColors.green),
          const SizedBox(width: 12),
          Expanded(
            child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              Text(dirty ? 'ALTERAÇÕES NÃO PUBLICADAS' : 'CATÁLOGO EM DIA', style: AppText.h3()),
              Text(
                app.remote == null
                    ? 'Servidor não configurado: as alterações não podem ser publicadas.'
                    : 'Versão publicada: ${app.extrasVersion == 0 ? 'nenhuma ainda' : app.extrasVersion}. '
                        'Edite à vontade: nada muda para os alunos até você publicar.',
                style: AppText.small(),
              ),
            ]),
          ),
          if (dirty) TextButton(onPressed: saving ? null : _reload, child: const Text('DESCARTAR')),
          const SizedBox(width: 8),
          ElevatedButton.icon(
            onPressed: !dirty || saving || app.remote == null ? null : () => _publish(app),
            icon: saving
                ? const SizedBox(width: 16, height: 16, child: CircularProgressIndicator(strokeWidth: 2))
                : const Icon(Icons.publish, size: 18),
            label: const Text('PUBLICAR PARA TODOS'),
          ),
        ]),
      ),
      const SizedBox(height: 16),

      // ------------------------------------------------ concursos
      _Section(
        title: 'Concursos pós-edital',
        help: 'Cada concurso tem as matérias, pesos, número de questões e assuntos do edital, na ordem do edital. '
            'Assuntos com o mesmo nome dos do ciclo básico aproveitam PDFs e o progresso do aluno.',
        action: ElevatedButton.icon(
          onPressed: () => _editContest(app, preview, null),
          icon: const Icon(Icons.add, size: 18),
          label: const Text('NOVO CONCURSO'),
        ),
        children: [
          if (preview.contests.isEmpty) Text('Nenhum concurso cadastrado.', style: AppText.small()),
          for (final c in preview.contests)
            _Row(
              title: c.name,
              subtitle: [
                preview.careerOfOption(c.id)?.name ?? '',
                if (c.contest!.banca.isNotEmpty) c.contest!.banca,
                if (c.contest!.examDate != null) 'prova ${fmtDate(c.contest!.examDate!)}',
                '${c.contest!.topicIds.length} assuntos',
              ].join(' · '),
              tag: base.hasOption(c.id) ? 'EMBUTIDO' : 'CRIADO NO EDITOR',
              onEdit: () => _editContest(app, preview, c.id),
              onRemove: () => _confirmRemove(c.name, () => _remove('contests', c.id, 'id', builtin: _isBuiltinOption(app, c.id))),
            ),
        ],
      ),
      const SizedBox(height: 16),

      // ------------------------------------------------ cargos do ciclo básico
      _Section(
        title: 'Cargos do ciclo básico (pré-edital)',
        help: 'Pesos de 0 a 3 por matéria. Peso 3 entra no 1º dia; 2 e 1 entram aos poucos; 0 fica fora do ciclo.',
        action: ElevatedButton.icon(
          onPressed: () => _editCargo(app, preview, null),
          icon: const Icon(Icons.add, size: 18),
          label: const Text('NOVO CARGO'),
        ),
        children: [
          for (final career in preview.careers)
            for (final o in career.cycleCargos)
              _Row(
                title: '${career.code} · ${o.name}',
                subtitle: preview.subjects.where((s) => s.weightFor(o.id) > 0).map((s) => '${s.name} ${s.weightFor(o.id)}').join(' · '),
                tag: base.hasOption(o.id) ? 'EMBUTIDO' : 'CRIADO NO EDITOR',
                onEdit: () => _editCargo(app, preview, o.id),
                onRemove: () => _confirmRemove(o.name, () => _remove('cargos', o.id, 'id', builtin: _isBuiltinOption(app, o.id))),
              ),
        ],
      ),
      const SizedBox(height: 16),

      // ------------------------------------------------ áreas
      _Section(
        title: 'Áreas (carreiras)',
        help: 'Ex.: Polícia Militar, Polícia Científica, Agente de Trânsito. Uma área só aparece para os alunos quando tem ao menos um cargo ou concurso.',
        action: ElevatedButton.icon(
          onPressed: () => _editArea(preview, null),
          icon: const Icon(Icons.add, size: 18),
          label: const Text('NOVA ÁREA'),
        ),
        children: [
          for (final c in preview.careers)
            _Row(
              title: '${c.code} · ${c.name}',
              subtitle: '${c.esfera} · ${c.cycleCargos.length} cargo(s) · ${c.contests.length} concurso(s)',
              tag: base.careerOrNull(c.code) != null ? 'EMBUTIDO' : 'CRIADO NO EDITOR',
              onEdit: () => _editArea(preview, c.code),
              onRemove: () => _confirmRemove(c.name, () => _remove('areas', c.code, 'code', builtin: base.careerOrNull(c.code) != null)),
            ),
        ],
      ),
      const SizedBox(height: 16),

      // ------------------------------------------------ matérias
      _Section(
        title: 'Matérias',
        help: 'Crie uma matéria quando o edital cobrar algo que ainda não existe (ex.: História de Pernambuco).',
        action: ElevatedButton.icon(
          onPressed: () => _editSubject(preview, null),
          icon: const Icon(Icons.add, size: 18),
          label: const Text('NOVA MATÉRIA'),
        ),
        children: [
          Wrap(spacing: 8, runSpacing: 8, children: [
            for (final s in preview.subjects)
              InkWell(
                onTap: () => _editSubject(preview, s.id),
                borderRadius: BorderRadius.circular(20),
                child: SubjectTag(s),
              ),
          ]),
        ],
      ),
      const SizedBox(height: 16),

      // ------------------------------------------------ ocultos e avançado
      if (_hidden.isNotEmpty) ...[
        _Section(
          title: 'Itens ocultos',
          help: 'Itens do catálogo embutido que você removeu. Restaure se precisar.',
          children: [
            Wrap(spacing: 8, runSpacing: 8, children: [
              for (final h in [..._hidden])
                InputChip(
                  label: Text(base.cargoOrNull(h)?.name ?? base.careerOrNull(h)?.name ?? h),
                  onDeleted: () => setState(() => _hidden.remove(h)),
                  deleteIcon: const Icon(Icons.restore, size: 18),
                ),
            ]),
          ],
        ),
        const SizedBox(height: 16),
      ],
      _Section(
        title: 'Avançado',
        help: 'Copie o rascunho em JSON para guardar uma cópia ou enviar a um programador (ele pode embutir no app).',
        children: [
          Wrap(spacing: 10, children: [
            OutlinedButton.icon(
              onPressed: () {
                Clipboard.setData(ClipboardData(text: const JsonEncoder.withIndent(' ').convert(draft)));
                toast(context, 'JSON copiado.');
              },
              icon: const Icon(Icons.copy, size: 18),
              label: const Text('COPIAR JSON'),
            ),
            OutlinedButton.icon(onPressed: _importJson, icon: const Icon(Icons.paste, size: 18), label: const Text('COLAR JSON')),
          ]),
        ],
      ),
    ]);
  }

  Future<void> _confirmRemove(String name, VoidCallback action) async {
    final ok = await confirm(context, 'REMOVER', 'Remover "$name" do catálogo? Só vale depois de publicar e pode ser desfeito antes disso.',
        ok: 'REMOVER', danger: true);
    if (ok) action();
  }

  Future<void> _importJson() async {
    final ctrl = TextEditingController();
    final ok = await showDialog<bool>(
      context: context,
      builder: (ctx) => AlertDialog(
        title: Text('COLAR JSON', style: AppText.h2()),
        content: SizedBox(width: 640, child: TextField(controller: ctrl, maxLines: 16, style: AppText.small(AppColors.text))),
        actions: [
          TextButton(onPressed: () => Navigator.pop(ctx, false), child: const Text('CANCELAR')),
          ElevatedButton(onPressed: () => Navigator.pop(ctx, true), child: const Text('USAR')),
        ],
      ),
    );
    if (ok != true || !mounted) return;
    try {
      final j = normalizeExtras(jsonDecode(ctrl.text));
      final app = AppScope.read(context);
      Catalog.fromJson(app.catalogBase, extras: j);
      setState(() => draft = j);
    } catch (_) {
      toast(context, 'JSON inválido.');
    }
  }

  // ---------------------------------------------------------------- área
  Future<void> _editArea(Catalog cat, String? code) async {
    final old = code == null ? null : cat.careerOrNull(code);
    final name = TextEditingController(text: old?.name ?? '');
    final sigla = TextEditingController(text: old?.code ?? '');
    final esc = TextEditingController(text: old?.escolaridade ?? 'Superior');
    final banca = TextEditingController(text: old?.banca ?? 'Varia por estado');
    final obs = TextEditingController(text: old?.observacao ?? '');
    final marca = TextEditingController(text: old?.marca ?? '');
    var esfera = old?.esfera ?? 'Estadual';
    var disc = old?.discursiva ?? true;
    final res = await showDialog<Map<String, dynamic>>(
      context: context,
      builder: (ctx) => StatefulBuilder(builder: (ctx, setState) {
        final codeOk = RegExp(r'^[A-Z0-9_]{2,10}$').hasMatch(sigla.text.trim()) &&
            (old != null || cat.careerOrNull(sigla.text.trim()) == null);
        final ok = name.text.trim().isNotEmpty && codeOk;
        return AlertDialog(
          title: Text(old == null ? 'NOVA ÁREA' : 'EDITAR ÁREA', style: AppText.h2()),
          content: SizedBox(
            width: 560,
            child: SingleChildScrollView(
              child: Column(mainAxisSize: MainAxisSize.min, crossAxisAlignment: CrossAxisAlignment.stretch, children: [
                Row(children: [
                  SizedBox(
                    width: 130,
                    child: TextField(
                      controller: sigla,
                      enabled: old == null,
                      textCapitalization: TextCapitalization.characters,
                      onChanged: (_) => setState(() {}),
                      decoration: const InputDecoration(labelText: 'Sigla', hintText: 'PCIENT'),
                    ),
                  ),
                  const SizedBox(width: 12),
                  Expanded(
                    child: TextField(
                      controller: name,
                      onChanged: (_) => setState(() {}),
                      decoration: const InputDecoration(labelText: 'Nome', hintText: 'Polícia Científica'),
                    ),
                  ),
                ]),
                if (old == null && sigla.text.isNotEmpty && !codeOk)
                  Padding(
                    padding: const EdgeInsets.only(top: 6),
                    child: Text('Sigla: 2 a 10 letras maiúsculas/números, sem repetir uma existente.', style: AppText.small(AppColors.red)),
                  ),
                const SizedBox(height: 14),
                Wrap(spacing: 8, children: [
                  for (final e in kEsferas) ToggleChip(label: e.toUpperCase(), selected: esfera == e, onTap: () => setState(() => esfera = e)),
                ]),
                const SizedBox(height: 14),
                TextField(controller: esc, decoration: const InputDecoration(labelText: 'Escolaridade')),
                const SizedBox(height: 12),
                StatefulBuilder(
                  builder: (context, set) => TextField(
                    controller: banca,
                    onChanged: (_) => set(() {}),
                    decoration: InputDecoration(labelText: 'Banca do último concurso', helperText: _bancaHint(banca.text), helperMaxLines: 2),
                  ),
                ),
                const SizedBox(height: 12),
                TextField(controller: obs, maxLines: 2, decoration: const InputDecoration(labelText: 'Observação (aparece na escolha da área)')),
                const SizedBox(height: 12),
                TextField(controller: marca, decoration: const InputDecoration(labelText: 'Matérias-marca', hintText: 'Ex.: Química · Biologia')),
                const SizedBox(height: 6),
                SwitchListTile(
                  contentPadding: EdgeInsets.zero,
                  value: disc,
                  onChanged: (v) => setState(() => disc = v),
                  title: Text('Tem prova discursiva/redação', style: AppText.body()),
                ),
              ]),
            ),
          ),
          actions: [
            TextButton(onPressed: () => Navigator.pop(ctx), child: const Text('CANCELAR')),
            ElevatedButton(
              onPressed: !ok
                  ? null
                  : () => Navigator.pop(ctx, {
                        'code': sigla.text.trim(),
                        'name': name.text.trim(),
                        'esfera': esfera,
                        'escolaridade': esc.text.trim(),
                        'banca': banca.text.trim(),
                        'discursiva': disc,
                        'observacao': obs.text.trim(),
                        'marca': marca.text.trim(),
                      }),
              child: const Text('GUARDAR NO RASCUNHO'),
            ),
          ],
        );
      }),
    );
    if (res != null) _upsert('areas', res, 'code');
  }

  // ---------------------------------------------------------------- matéria
  Future<void> _editSubject(Catalog cat, String? id) async {
    final old = id == null ? null : cat.subjectOrNull(id);
    final name = TextEditingController(text: old?.name ?? '');
    var color = old?.colorHex.toUpperCase() ?? _palette.first;
    final res = await showDialog<Map<String, dynamic>>(
      context: context,
      builder: (ctx) => StatefulBuilder(builder: (ctx, setState) {
        return AlertDialog(
          title: Text(old == null ? 'NOVA MATÉRIA' : 'EDITAR MATÉRIA', style: AppText.h2()),
          content: SizedBox(
            width: 460,
            child: Column(mainAxisSize: MainAxisSize.min, crossAxisAlignment: CrossAxisAlignment.stretch, children: [
              TextField(controller: name, onChanged: (_) => setState(() {}), decoration: const InputDecoration(labelText: 'Nome da matéria')),
              const SizedBox(height: 16),
              Wrap(spacing: 8, runSpacing: 8, children: [
                for (final c in _palette)
                  InkWell(
                    onTap: () => setState(() => color = c),
                    child: Container(
                      width: 30,
                      height: 30,
                      decoration: BoxDecoration(
                        color: AppColors.hex(c),
                        shape: BoxShape.circle,
                        border: Border.all(color: color == c ? AppColors.text : Colors.transparent, width: 2.5),
                      ),
                    ),
                  ),
              ]),
            ]),
          ),
          actions: [
            TextButton(onPressed: () => Navigator.pop(ctx), child: const Text('CANCELAR')),
            ElevatedButton(
              onPressed: name.text.trim().isEmpty
                  ? null
                  : () => Navigator.pop(ctx, {
                        'id': old?.id ?? makeId(name.text.trim(), cat.subjects.map((s) => s.id)),
                        'name': name.text.trim(),
                        'color': color,
                      }),
              child: const Text('GUARDAR NO RASCUNHO'),
            ),
          ],
        );
      }),
    );
    if (res != null) _upsert('subjects', res, 'id');
  }

  // ---------------------------------------------------------------- cargo do ciclo básico
  Future<void> _editCargo(AppController app, Catalog cat, String? id) async {
    final old = id == null ? null : cat.cargoOrNull(id);
    final name = TextEditingController(text: old?.name ?? '');
    var career = id == null ? (cat.careers.firstOrNull?.code ?? '') : cat.careerOfOption(id)!.code;
    final weights = {for (final s in cat.subjects) s.id: id == null ? 0 : s.weightFor(id)};
    final res = await showDialog<Map<String, dynamic>>(
      context: context,
      builder: (ctx) => StatefulBuilder(builder: (ctx, setState) {
        final ok = name.text.trim().isNotEmpty && career.isNotEmpty && weights.values.any((w) => w > 0);
        return AlertDialog(
          title: Text(old == null ? 'NOVO CARGO DO CICLO BÁSICO' : 'EDITAR CARGO', style: AppText.h2()),
          content: SizedBox(
            width: 720,
            height: 560,
            child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
              Row(children: [
                Expanded(
                  child: TextField(
                    controller: name,
                    onChanged: (_) => setState(() {}),
                    decoration: const InputDecoration(labelText: 'Nome do cargo', hintText: 'Ex.: Perito Criminal'),
                  ),
                ),
                const SizedBox(width: 12),
                SizedBox(
                  width: 260,
                  child: DropdownButtonFormField<String>(
                    initialValue: career.isEmpty ? null : career,
                    isExpanded: true,
                    dropdownColor: AppColors.panel2,
                    decoration: const InputDecoration(labelText: 'Área'),
                    items: [for (final c in cat.careers) DropdownMenuItem(value: c.code, child: Text('${c.code} · ${c.name}', overflow: TextOverflow.ellipsis))],
                    onChanged: old != null ? null : (v) => setState(() => career = v ?? career),
                  ),
                ),
              ]),
              const SizedBox(height: 14),
              Text('PESO DE CADA MATÉRIA (0 = fora do ciclo)', style: AppText.label(AppColors.gold)),
              const SizedBox(height: 8),
              Expanded(
                child: ListView(children: [
                  for (final s in cat.subjects)
                    Padding(
                      padding: const EdgeInsets.symmetric(vertical: 3),
                      child: Row(children: [
                        Container(width: 8, height: 8, decoration: BoxDecoration(color: AppColors.hex(s.colorHex), shape: BoxShape.circle)),
                        const SizedBox(width: 10),
                        Expanded(child: Text(s.name, style: AppText.body(weights[s.id]! > 0 ? AppColors.text : AppColors.dim))),
                        for (final w in const [0, 1, 2, 3])
                          Padding(
                            padding: const EdgeInsets.only(left: 6),
                            child: ToggleChip(label: '$w', minWidth: 40, selected: weights[s.id] == w, onTap: () => setState(() => weights[s.id] = w)),
                          ),
                      ]),
                    ),
                ]),
              ),
            ]),
          ),
          actions: [
            TextButton(onPressed: () => Navigator.pop(ctx), child: const Text('CANCELAR')),
            ElevatedButton(
              onPressed: !ok
                  ? null
                  : () => Navigator.pop(ctx, {
                        'id': id ?? makeId('${career}_${name.text.trim()}', cat.careers.expand((c) => c.cargos).map((c) => c.id)),
                        'career': career,
                        'name': name.text.trim(),
                        'weights': {for (final e in weights.entries) if (e.value > 0) e.key: e.value},
                      }),
              child: const Text('GUARDAR NO RASCUNHO'),
            ),
          ],
        );
      }),
    );
    if (res != null) _upsert('cargos', res, 'id');
  }

  // ---------------------------------------------------------------- concurso pós-edital
  Map<String, dynamic>? _contestJson(AppController app, String id) {
    for (final c in _list('contests')) {
      if (c['id'] == id) return cloneJson(c);
    }
    for (final c in (app.catalogBase['contests'] as List? ?? const []).cast<Map<String, dynamic>>()) {
      if (c['id'] == id) return cloneJson(c);
    }
    return null;
  }

  Future<void> _editContest(AppController app, Catalog cat, String? id) async {
    final j = id == null ? null : _contestJson(app, id);
    final res = await showDialog<Map<String, dynamic>>(
      context: context,
      builder: (ctx) => _ContestDialog(catalog: cat, data: j),
    );
    if (res != null) _upsert('contests', res, 'id');
  }
}

class _Section extends StatelessWidget {
  const _Section({required this.title, required this.help, required this.children, this.action});
  final String title;
  final String help;
  final List<Widget> children;
  final Widget? action;

  @override
  Widget build(BuildContext context) {
    return Panel(
      child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
        Row(children: [
          Expanded(child: SectionLabel(title)),
          if (action != null) action!,
        ]),
        Text(help, style: AppText.small()),
        const SizedBox(height: 12),
        ...children,
      ]),
    );
  }
}

class _Row extends StatelessWidget {
  const _Row({required this.title, required this.subtitle, required this.tag, required this.onEdit, required this.onRemove});
  final String title;
  final String subtitle;
  final String tag;
  final VoidCallback onEdit;
  final VoidCallback onRemove;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(vertical: 8),
      decoration: const BoxDecoration(border: Border(bottom: BorderSide(color: AppColors.lineSoft))),
      child: Row(children: [
        Expanded(
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Text(title, style: AppText.strong(), overflow: TextOverflow.ellipsis),
            Text(subtitle, style: AppText.small(), maxLines: 1, overflow: TextOverflow.ellipsis),
          ]),
        ),
        Pill(tag, color: tag == 'EMBUTIDO' ? AppColors.muted : AppColors.teal),
        const SizedBox(width: 8),
        TextButton.icon(onPressed: onEdit, icon: const Icon(Icons.edit_outlined, size: 16), label: const Text('EDITAR')),
        IconButton(onPressed: onRemove, tooltip: 'Remover', icon: const Icon(Icons.delete_outline, size: 19, color: AppColors.red)),
      ]),
    );
  }
}

/// Uma matéria dentro do formulário do concurso.
class _SubjBlock {
  _SubjBlock({required this.subjectId, required this.weight, required int questions, required String topics})
      : questions = TextEditingController(text: questions == 0 ? '' : '$questions'),
        topics = TextEditingController(text: topics);
  String? subjectId;
  int weight;
  final TextEditingController questions;
  final TextEditingController topics;
}

class _ContestDialog extends StatefulWidget {
  const _ContestDialog({required this.catalog, this.data});
  final Catalog catalog;
  final Map<String, dynamic>? data;

  @override
  State<_ContestDialog> createState() => _ContestDialogState();
}

class _ContestDialogState extends State<_ContestDialog> {
  late final Map<String, dynamic> d = widget.data ?? {};
  late final name = TextEditingController(text: d['name'] as String? ?? '');
  late final orgao = TextEditingController(text: d['orgao'] as String? ?? '');
  late final uf = TextEditingController(text: d['uf'] as String? ?? '');
  late final banca = TextEditingController(text: d['banca'] as String? ?? '');
  late final vagas = TextEditingController(text: d['vagas'] as String? ?? '');
  late final url = TextEditingController(text: d['editalUrl'] as String? ?? '');
  late final notes = TextEditingController(text: d['notes'] as String? ?? '');
  late String career = d['career'] as String? ?? '';
  late String base = d['base'] as String? ?? '';
  late String status = kContestStatus.containsKey(d['status']) ? d['status'] as String : 'publicado';
  late DateTime? exam = DateTime.tryParse(d['examDate'] as String? ?? '');
  final blocks = <_SubjBlock>[];

  Catalog get cat => widget.catalog;

  @override
  void initState() {
    super.initState();
    for (final s in (d['subjects'] as List? ?? const []).cast<Map>()) {
      final lines = <String>[];
      for (final t in (s['topics'] as List? ?? const []).cast<Map>()) {
        final ref = t['ref'] as String?;
        if (ref != null) {
          final topic = cat.topic(ref);
          if (topic != null) lines.add(_line(topic.name, topic.size));
        } else {
          lines.add(_line('${t['name'] ?? ''}', '${t['size'] ?? 'M'}'));
        }
      }
      blocks.add(_SubjBlock(
        subjectId: s['id'] as String?,
        weight: ((s['weight'] as num?)?.toInt() ?? 2).clamp(1, 3),
        questions: (s['questions'] as num?)?.toInt() ?? 0,
        topics: lines.join('\n'),
      ));
    }
    if (blocks.isEmpty) blocks.add(_SubjBlock(subjectId: null, weight: 2, questions: 0, topics: ''));
  }

  @override
  void dispose() {
    for (final c in [name, orgao, uf, banca, vagas, url, notes]) {
      c.dispose();
    }
    for (final b in blocks) {
      b.questions.dispose();
      b.topics.dispose();
    }
    super.dispose();
  }

  static String _line(String name, String size) => size == 'M' ? name : '$name ($size)';

  /// "Ordem social (P)" → ("Ordem social", "P").
  static (String, String) _parse(String line) {
    final m = RegExp(r'^(.*?)\s*\(([PMGpmg])\)\s*$').firstMatch(line);
    if (m == null) return (line.trim(), 'M');
    return (m.group(1)!.trim(), m.group(2)!.toUpperCase());
  }

  List<Map<String, dynamic>> _topicsOf(_SubjBlock b) {
    final byName = {for (final t in cat.topicsOf(b.subjectId!)) t.name.toLowerCase(): t};
    final out = <Map<String, dynamic>>[];
    for (final raw in b.topics.text.split('\n')) {
      if (raw.trim().isEmpty) continue;
      final (n, size) = _parse(raw);
      final existing = byName[n.toLowerCase()];
      out.add(existing != null ? {'ref': existing.id} : {'name': n, 'size': size});
    }
    return out;
  }

  int get _topicCount => blocks.where((b) => b.subjectId != null).fold(0, (a, b) => a + _topicsOf(b).length);

  bool get _valid =>
      name.text.trim().isNotEmpty &&
      career.isNotEmpty &&
      blocks.any((b) => b.subjectId != null && _topicsOf(b).isNotEmpty) &&
      blocks.map((b) => b.subjectId).whereType<String>().toSet().length == blocks.where((b) => b.subjectId != null).length;

  Map<String, dynamic> _result() {
    final id = d['id'] as String? ??
        makeId(name.text.trim(), cat.careers.expand((c) => c.cargos).map((c) => c.id));
    final cycle = cat.careerOrNull(career)?.cycleCargos ?? const <Cargo>[];
    return {
      'id': id,
      'career': career,
      'base': cycle.any((c) => c.id == base) ? base : (cycle.firstOrNull?.id ?? ''),
      'name': name.text.trim(),
      'orgao': orgao.text.trim(),
      'uf': uf.text.trim().toUpperCase(),
      'banca': banca.text.trim(),
      'examDate': exam == null ? '' : isoDate(exam!),
      'editalUrl': url.text.trim(),
      'vagas': vagas.text.trim(),
      'status': status,
      'notes': notes.text.trim(),
      'subjects': [
        for (final b in blocks)
          if (b.subjectId != null && _topicsOf(b).isNotEmpty)
            {
              'id': b.subjectId,
              'weight': b.weight,
              'questions': int.tryParse(b.questions.text.trim()) ?? 0,
              'topics': _topicsOf(b),
            },
      ],
    };
  }

  @override
  Widget build(BuildContext context) {
    final cycle = cat.careerOrNull(career)?.cycleCargos ?? const <Cargo>[];
    return AlertDialog(
      title: Text(widget.data == null ? 'NOVO CONCURSO PÓS-EDITAL' : 'EDITAR CONCURSO', style: AppText.h2()),
      content: SizedBox(
        width: 1000,
        height: 660,
        child: ListView(children: [
          Row(children: [
            Expanded(
              flex: 3,
              child: TextField(
                controller: name,
                onChanged: (_) => setState(() {}),
                decoration: const InputDecoration(labelText: 'Nome do concurso', hintText: 'Ex.: CFO PMPE 2026 — 2º Tenente'),
              ),
            ),
            const SizedBox(width: 12),
            Expanded(
              flex: 2,
              child: DropdownButtonFormField<String>(
                initialValue: career.isEmpty ? null : career,
                isExpanded: true,
                dropdownColor: AppColors.panel2,
                decoration: const InputDecoration(labelText: 'Área'),
                items: [for (final c in cat.careers) DropdownMenuItem(value: c.code, child: Text('${c.code} · ${c.name}', overflow: TextOverflow.ellipsis))],
                onChanged: (v) => setState(() {
                  career = v ?? career;
                  base = '';
                }),
              ),
            ),
            const SizedBox(width: 12),
            Expanded(
              flex: 2,
              child: DropdownButtonFormField<String>(
                key: ValueKey('base-$career'),
                initialValue: cycle.any((c) => c.id == base) ? base : null,
                isExpanded: true,
                dropdownColor: AppColors.panel2,
                decoration: const InputDecoration(labelText: 'Cargo de referência (ciclo básico)'),
                items: [for (final c in cycle) DropdownMenuItem(value: c.id, child: Text(c.name, overflow: TextOverflow.ellipsis))],
                onChanged: (v) => setState(() => base = v ?? ''),
              ),
            ),
          ]),
          const SizedBox(height: 12),
          Row(children: [
            Expanded(flex: 3, child: TextField(controller: orgao, decoration: const InputDecoration(labelText: 'Órgão', hintText: 'Polícia Militar de Pernambuco'))),
            const SizedBox(width: 12),
            SizedBox(width: 70, child: TextField(controller: uf, maxLength: 2, decoration: const InputDecoration(labelText: 'UF', counterText: ''))),
            const SizedBox(width: 12),
            Expanded(
              flex: 2,
              child: TextField(
                controller: banca,
                onChanged: (_) => setState(() {}),
                decoration: InputDecoration(labelText: 'Banca', helperText: _bancaHint(banca.text), helperMaxLines: 2),
              ),
            ),
            const SizedBox(width: 12),
            SizedBox(width: 90, child: TextField(controller: vagas, decoration: const InputDecoration(labelText: 'Vagas'))),
          ]),
          const SizedBox(height: 12),
          Row(children: [
            OutlinedButton.icon(
              onPressed: () async {
                final now = DateTime.now();
                final p = await showDatePicker(
                  context: context,
                  initialDate: exam ?? now.add(const Duration(days: 90)),
                  firstDate: DateTime(now.year - 1),
                  lastDate: DateTime(now.year + 4),
                );
                if (p != null) setState(() => exam = p);
              },
              icon: const Icon(Icons.event, size: 18),
              label: Text(exam == null ? 'DATA DA PROVA' : 'PROVA: ${fmtDate(exam!)}'),
            ),
            if (exam != null) IconButton(onPressed: () => setState(() => exam = null), icon: const Icon(Icons.close, size: 18), tooltip: 'Sem data'),
            const SizedBox(width: 12),
            Wrap(spacing: 6, children: [
              for (final e in kContestStatus.entries)
                ToggleChip(label: e.value.toUpperCase(), selected: status == e.key, onTap: () => setState(() => status = e.key)),
            ]),
          ]),
          const SizedBox(height: 12),
          TextField(controller: url, decoration: const InputDecoration(labelText: 'Link do edital (página da banca)', hintText: 'https://')),
          const SizedBox(height: 12),
          TextField(controller: notes, maxLines: 3, decoration: const InputDecoration(labelText: 'Observações (estrutura da prova, requisitos, notas mínimas)')),
          const SizedBox(height: 20),
          Row(children: [
            Expanded(child: Text('MATÉRIAS E ASSUNTOS DO EDITAL · $_topicCount assuntos', style: AppText.label(AppColors.gold))),
            TextButton.icon(
              onPressed: () => setState(() => blocks.add(_SubjBlock(subjectId: null, weight: 2, questions: 0, topics: ''))),
              icon: const Icon(Icons.add, size: 18),
              label: const Text('ADICIONAR MATÉRIA'),
            ),
          ]),
          Text(
            'Um assunto por linha, na ordem do edital. Tamanho: acrescente (P) pequeno ou (G) grande — sem nada é médio. '
            'Se o nome for igual ao de um assunto do ciclo básico, o app reaproveita PDFs e o progresso do aluno.',
            style: AppText.small(),
          ),
          const SizedBox(height: 10),
          for (var i = 0; i < blocks.length; i++) _block(i),
        ]),
      ),
      actions: [
        TextButton(onPressed: () => Navigator.pop(context), child: const Text('CANCELAR')),
        ElevatedButton(onPressed: _valid ? () => Navigator.pop(context, _result()) : null, child: const Text('GUARDAR NO RASCUNHO')),
      ],
    );
  }

  Widget _block(int i) {
    final b = blocks[i];
    final usedElsewhere = {for (final x in blocks) if (x != b && x.subjectId != null) x.subjectId};
    final reused = b.subjectId == null ? 0 : _topicsOf(b).where((t) => t.containsKey('ref')).length;
    return Container(
      margin: const EdgeInsets.only(bottom: 12),
      padding: const EdgeInsets.all(12),
      decoration: BoxDecoration(color: AppColors.panel2, borderRadius: BorderRadius.circular(10)),
      child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
        Row(children: [
          Expanded(
            child: DropdownButtonFormField<String>(
              initialValue: b.subjectId,
              isExpanded: true,
              dropdownColor: AppColors.panel2,
              decoration: const InputDecoration(labelText: 'Matéria'),
              items: [
                for (final s in cat.subjects)
                  if (!usedElsewhere.contains(s.id)) DropdownMenuItem(value: s.id, child: Text(s.name, overflow: TextOverflow.ellipsis)),
              ],
              onChanged: (v) => setState(() => b.subjectId = v),
            ),
          ),
          const SizedBox(width: 12),
          Text('PESO', style: AppText.label()),
          for (final w in const [1, 2, 3])
            Padding(
              padding: const EdgeInsets.only(left: 6),
              child: ToggleChip(label: '$w', minWidth: 40, selected: b.weight == w, onTap: () => setState(() => b.weight = w)),
            ),
          const SizedBox(width: 12),
          SizedBox(
            width: 110,
            child: TextField(
              controller: b.questions,
              keyboardType: TextInputType.number,
              inputFormatters: [FilteringTextInputFormatter.digitsOnly],
              decoration: const InputDecoration(labelText: 'Questões'),
            ),
          ),
          IconButton(
            tooltip: 'Remover matéria',
            onPressed: blocks.length == 1 ? null : () => setState(() => blocks.removeAt(i)),
            icon: const Icon(Icons.delete_outline, color: AppColors.red),
          ),
        ]),
        const SizedBox(height: 10),
        TextField(
          controller: b.topics,
          minLines: 3,
          maxLines: 10,
          onChanged: (_) => setState(() {}),
          style: AppText.body(),
          decoration: const InputDecoration(labelText: 'Assuntos (um por linha)', alignLabelWithHint: true),
        ),
        const SizedBox(height: 6),
        Row(children: [
          Expanded(
            child: Text(
              b.subjectId == null ? 'Escolha a matéria.' : '${_topicsOf(b).length} assuntos · $reused aproveitados do ciclo básico',
              style: AppText.small(AppColors.dim),
            ),
          ),
          if (b.subjectId != null)
            TextButton(
              onPressed: () => setState(() {
                final names = cat.topicsOf(b.subjectId!).map((t) => _line(t.name, t.size)).join('\n');
                b.topics.text = b.topics.text.trim().isEmpty ? names : '${b.topics.text.trim()}\n$names';
              }),
              child: const Text('INSERIR ASSUNTOS DO CICLO BÁSICO'),
            ),
        ]),
      ]),
    );
  }
}

/// Mostra ao dono qual versão dos materiais os alunos vão receber com essa banca.
String _bancaHint(String banca) {
  final v = bancaProfileOf(banca);
  return switch (v) {
    'cebraspe' => 'Materiais na versão Cebraspe (certo/errado).',
    'aocp' => 'Materiais na versão Instituto AOCP (Bloco B em múltipla escolha).',
    _ => 'Materiais na versão neutra. Para ter a versão desta banca, peça a nova versão dos materiais.',
  };
}
