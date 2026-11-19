import 'package:flutter/material.dart';

import '../../core/bancas.dart';
import '../../core/catalog.dart';
import '../../core/dates.dart';
import '../../core/models.dart';
import '../../data/content.dart';
import '../../data/storage.dart';
import '../../state/app_state.dart';
import '../dialogs.dart';
import '../mindmap.dart';
import '../theme.dart';
import '../widgets.dart';

class MaterialsPage extends StatefulWidget {
  const MaterialsPage({super.key});

  @override
  State<MaterialsPage> createState() => _MaterialsPageState();
}

class _MaterialsPageState extends State<MaterialsPage> {
  MaterialInfo? open;

  /// Pasta (matéria) aberta; null = lista de pastas.
  String? folder;

  @override
  Widget build(BuildContext context) {
    final app = AppScope.of(context);
    if (app.pendingMaterialId != null) {
      final id = app.pendingMaterialId;
      app.pendingMaterialId = null;
      open = app.content.items.where((m) => m.id == id).firstOrNull ?? open;
      if (open != null) folder = open!.subjectId;
    }
    if (open != null) {
      return MaterialReader(key: ValueKey(open!.id), info: open!, onClose: () => setState(() => open = null));
    }
    final items = app.content.items;
    final opt = app.profile.optionId;
    final bySubject = <String, List<MaterialInfo>>{};
    for (final m in items) {
      bySubject.putIfAbsent(m.subjectId, () => []).add(m);
    }
    // Pastas: matérias do plano do aluno primeiro (por peso), depois as demais.
    final subjects = app.catalog.subjects.where((s) => bySubject.containsKey(s.id)).toList()
      ..sort((a, b) {
        final w = b.weightFor(opt).compareTo(a.weightFor(opt));
        return w != 0 ? w : a.name.compareTo(b.name);
      });
    if (folder != null && !bySubject.containsKey(folder)) folder = null;
    if (folder != null) return _folderView(app, app.catalog.subject(folder!), bySubject[folder]!);

    return ListView(padding: const EdgeInsets.only(bottom: 32), children: [
      PageHeader(
        title: 'Materiais',
        subtitle: 'Apostilas do Taticum separadas por matéria — e os seus próprios links e PDFs.',
        actions: [if (app.reviewer) const _ReviewerBadge()],
      ),
      Padding(
        padding: const EdgeInsets.symmetric(horizontal: 28),
        child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
          const SectionLabel('Conteúdos do Taticum'),
          Text('Cada assunto tem dois materiais: o APROFUNDADO, para o primeiro estudo (teoria completa + 20 questões), '
              'e o RESUMO, para as revisões (direto ao ponto + mapa mental + 10 questões).', style: AppText.small()),
          const SizedBox(height: 14),
          if (subjects.isEmpty)
            const _ComingSoon()
          else
            Wrap(spacing: 16, runSpacing: 16, children: [
              for (final s in subjects)
                _FolderCard(
                  subject: s,
                  materials: bySubject[s.id]!,
                  inPlan: s.weightFor(opt) > 0,
                  onOpen: () => setState(() => folder = s.id),
                ),
            ]),
          const SizedBox(height: 30),
          SectionLabel(
            'Meus materiais',
            trailing: OutlinedButton.icon(onPressed: () => _addMaterial(context), icon: const Icon(Icons.add_link, size: 18), label: const Text('ADICIONAR')),
          ),
          if (app.data.materials.isEmpty)
            Panel(
              child: Text(
                'Guarde aqui links de videoaulas, PDFs do seu computador e páginas úteis, ligados à matéria e ao assunto do edital.',
                style: AppText.small(),
              ),
            ),
          for (final m in app.data.materials) _UserMaterialRow(material: m),
        ]),
      ),
    ]);
  }

  Widget _folderView(AppController app, Subject sub, List<MaterialInfo> list) {
    // Agrupa por assunto, na ordem do catálogo; aprofundado antes do resumo.
    final byTopic = <String, List<MaterialInfo>>{};
    for (final m in list) {
      byTopic.putIfAbsent(m.topicIds.isEmpty ? '' : m.topicIds.first, () => []).add(m);
    }
    final topicIds = byTopic.keys.toList()
      ..sort((a, b) => (app.catalog.topic(a)?.index ?? 9999).compareTo(app.catalog.topic(b)?.index ?? 9999));
    final mine = app.data.materials.where((m) => m.subjectId == sub.id).toList();
    return ListView(padding: const EdgeInsets.only(bottom: 32), children: [
      Padding(
        padding: const EdgeInsets.fromLTRB(16, 18, 28, 6),
        child: Row(children: [
          IconButton(tooltip: 'Voltar para as pastas', onPressed: () => setState(() => folder = null), icon: const Icon(Icons.arrow_back)),
          const SizedBox(width: 6),
          Icon(Icons.folder_open, color: AppColors.hex(sub.colorHex), size: 28),
          const SizedBox(width: 10),
          Expanded(child: Text(sub.name.toUpperCase(), style: AppText.h1())),
          if (app.reviewer) const _ReviewerBadge(),
        ]),
      ),
      Padding(
        padding: const EdgeInsets.symmetric(horizontal: 28),
        child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
          Text('${byTopic.length} assunto(s) · ${list.length} material(is)', style: AppText.small()),
          const SizedBox(height: 14),
          for (final tid in topicIds) ...[
            Text(app.catalog.topic(tid)?.name.toUpperCase() ?? 'GERAL', style: AppText.label(AppColors.gold)),
            const SizedBox(height: 8),
            Wrap(spacing: 16, runSpacing: 16, children: [
              for (final m in [...byTopic[tid]!.where((m) => m.isDeep), ...byTopic[tid]!.where((m) => !m.isDeep)])
                _MaterialCard(info: m, onOpen: () => setState(() => open = m)),
            ]),
            const SizedBox(height: 22),
          ],
          if (mine.isNotEmpty) ...[
            const SectionLabel('Meus materiais desta matéria'),
            for (final m in mine) _UserMaterialRow(material: m),
          ],
        ]),
      ),
    ]);
  }

  Future<void> _addMaterial(BuildContext context) async {
    final app = AppScope.read(context);
    final title = TextEditingController();
    final loc = TextEditingController();
    var kind = 'video';
    String? subjectId;
    String? topicId;
    final opt = app.profile.optionId;
    final subjects = app.catalog.subjects.where((s) => s.weightFor(opt) > 0).toList();
    await showDialog<void>(
      context: context,
      builder: (ctx) => StatefulBuilder(builder: (ctx, setState) {
        final topics = subjectId == null ? <Topic>[] : app.catalog.topicsToPick(subjectId!, app.profile.careerCode, opt);
        final ok = title.text.trim().isNotEmpty && loc.text.trim().isNotEmpty;
        return AlertDialog(
          title: Text('ADICIONAR MATERIAL', style: AppText.h2()),
          content: SizedBox(
            width: 520,
            child: Column(mainAxisSize: MainAxisSize.min, crossAxisAlignment: CrossAxisAlignment.stretch, children: [
              Wrap(spacing: 8, children: [
                for (final k in const [('video', 'VIDEOAULA'), ('pdf', 'PDF / ARQUIVO'), ('link', 'SITE / LINK')])
                  ToggleChip(label: k.$2, selected: kind == k.$1, onTap: () => setState(() => kind = k.$1)),
              ]),
              const SizedBox(height: 14),
              TextField(controller: title, onChanged: (_) => setState(() {}), decoration: const InputDecoration(labelText: 'Título')),
              const SizedBox(height: 12),
              TextField(
                controller: loc,
                onChanged: (_) => setState(() {}),
                decoration: InputDecoration(
                  labelText: kind == 'pdf' ? 'Caminho do arquivo' : 'Link (https://…)',
                  hintText: kind == 'pdf' ? r'Ex.: C:\Users\voce\Documents\resumo.pdf' : 'Cole o endereço aqui',
                ),
              ),
              const SizedBox(height: 12),
              DropdownButtonFormField<String?>(
                initialValue: subjectId,
                isExpanded: true,
                dropdownColor: AppColors.panel2,
                decoration: const InputDecoration(labelText: 'Matéria (opcional)'),
                items: [
                  const DropdownMenuItem<String?>(value: null, child: Text('—')),
                  for (final s in subjects) DropdownMenuItem<String?>(value: s.id, child: Text(s.name)),
                ],
                onChanged: (v) => setState(() {
                  subjectId = v;
                  topicId = null;
                }),
              ),
              const SizedBox(height: 12),
              DropdownButtonFormField<String?>(
                key: ValueKey(subjectId),
                initialValue: topicId,
                isExpanded: true,
                dropdownColor: AppColors.panel2,
                decoration: const InputDecoration(labelText: 'Assunto do edital (opcional)'),
                items: [
                  const DropdownMenuItem<String?>(value: null, child: Text('—')),
                  for (final t in topics) DropdownMenuItem<String?>(value: t.id, child: Text(t.name, overflow: TextOverflow.ellipsis)),
                ],
                onChanged: subjectId == null ? null : (v) => setState(() => topicId = v),
              ),
            ]),
          ),
          actions: [
            TextButton(onPressed: () => Navigator.pop(ctx), child: const Text('CANCELAR')),
            ElevatedButton(
              onPressed: !ok
                  ? null
                  : () {
                      final l = loc.text.trim();
                      app.addUserMaterial(UserMaterial(
                        id: app.newId('m'),
                        title: title.text.trim(),
                        kind: kind,
                        location: kind == 'pdf' ? l.replaceAll('"', '') : normalizeUrl(l),
                        subjectId: subjectId,
                        topicId: topicId,
                      ));
                      Navigator.pop(ctx);
                    },
              child: const Text('SALVAR'),
            ),
          ],
        );
      }),
    );
  }
}

class _FolderCard extends StatelessWidget {
  const _FolderCard({required this.subject, required this.materials, required this.inPlan, required this.onOpen});
  final Subject subject;
  final List<MaterialInfo> materials;
  final bool inPlan;
  final VoidCallback onOpen;

  @override
  Widget build(BuildContext context) {
    final app = AppScope.of(context);
    final col = AppColors.hex(subject.colorHex);
    final topics = {for (final m in materials) ...m.topicIds}.length;
    final pending = app.reviewer ? materials.where((m) => !app.content.isApproved(m)).length : 0;
    return SizedBox(
      width: 280,
      child: Material(
        color: AppColors.panel,
        borderRadius: BorderRadius.circular(12),
        child: InkWell(
          onTap: onOpen,
          borderRadius: BorderRadius.circular(12),
          child: Container(
            decoration: BoxDecoration(borderRadius: BorderRadius.circular(12), border: Border.all(color: AppColors.lineSoft)),
            clipBehavior: Clip.antiAlias,
            child: IntrinsicHeight(
              child: Row(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
                Container(width: 4, color: col),
                Expanded(
                  child: Padding(
                    padding: const EdgeInsets.all(16),
                    child: Row(children: [
              Icon(Icons.folder, color: col, size: 36),
              const SizedBox(width: 14),
              Expanded(
                child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                  Text(subject.name.toUpperCase(), style: AppText.h3(), maxLines: 2, overflow: TextOverflow.ellipsis),
                  const SizedBox(height: 4),
                  Text('$topics assunto(s) · ${materials.length} material(is)', style: AppText.small()),
                  if (!inPlan || pending > 0) ...[
                    const SizedBox(height: 6),
                    Wrap(spacing: 6, runSpacing: 6, children: [
                      if (!inPlan) const Pill('FORA DO SEU PLANO', color: AppColors.dim),
                      if (pending > 0) Pill('$pending EM REVISÃO', color: AppColors.amber),
                    ]),
                  ],
                ]),
              ),
              const Icon(Icons.chevron_right, color: AppColors.dim),
                    ]),
                  ),
                ),
              ]),
            ),
          ),
        ),
      ),
    );
  }
}

/// Aviso de que o dono está vendo também o que ainda não foi liberado.
class _ReviewerBadge extends StatelessWidget {
  const _ReviewerBadge();
  @override
  Widget build(BuildContext context) => const Tooltip(
        message: 'Só você vê os materiais em revisão. Os alunos veem apenas os liberados.',
        child: Pill('VISÃO DO DONO', color: AppColors.gold, icon: Icons.visibility_outlined),
      );
}

/// Selo de revisão: aparece só para o dono.
class ReviewPill extends StatelessWidget {
  const ReviewPill(this.info, {super.key});
  final MaterialInfo info;
  @override
  Widget build(BuildContext context) {
    final app = AppScope.of(context);
    if (!app.reviewer) return const SizedBox.shrink();
    return app.content.isApproved(info)
        ? const Pill('LIBERADO AOS ALUNOS', color: AppColors.green, icon: Icons.verified_outlined)
        : const Pill('EM REVISÃO · SÓ VOCÊ VÊ', color: AppColors.amber, icon: Icons.rate_review_outlined);
  }
}

class _MaterialCard extends StatelessWidget {
  const _MaterialCard({required this.info, required this.onOpen});
  final MaterialInfo info;
  final VoidCallback onOpen;

  @override
  Widget build(BuildContext context) {
    final app = AppScope.of(context);
    final sub = app.catalog.subjectOrNull(info.subjectId);
    final col = sub == null ? AppColors.gold : AppColors.hex(sub.colorHex);
    final attempts = app.attemptsOf(info.id);
    final best = attempts.isEmpty ? null : attempts.map((a) => a.net).reduce((a, b) => a > b ? a : b);
    final topicNames = [for (final t in info.topicIds) app.catalog.topic(t)?.name ?? t];
    return SizedBox(
      width: 360,
      child: Material(
        color: AppColors.panel,
        borderRadius: BorderRadius.circular(12),
        child: InkWell(
          onTap: onOpen,
          borderRadius: BorderRadius.circular(12),
          child: Container(
            decoration: BoxDecoration(borderRadius: BorderRadius.circular(12), border: Border.all(color: AppColors.lineSoft)),
            clipBehavior: Clip.antiAlias,
            child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
              Container(
                constraints: const BoxConstraints(minHeight: 96),
                padding: const EdgeInsets.all(16),
                decoration: BoxDecoration(
                  gradient: LinearGradient(colors: [col.withValues(alpha: 0.35), AppColors.panel2], begin: Alignment.topLeft, end: Alignment.bottomRight),
                ),
                child: Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
                  Expanded(
                    child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                      Text(info.kindLabel, style: AppText.label(info.isDeep ? AppColors.gold2 : AppColors.amber)),
                      const SizedBox(height: 6),
                      Text(info.title.toUpperCase(), style: AppText.h2().copyWith(fontSize: 18), maxLines: 2, overflow: TextOverflow.ellipsis),
                    ]),
                  ),
                  Icon(info.isDeep ? Icons.auto_stories : Icons.bolt, color: col, size: 28),
                ]),
              ),
              Padding(
                padding: const EdgeInsets.all(16),
                child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                  Text('${sub?.name ?? info.subtitle} · ${topicNames.join(' · ')}', style: AppText.small(), maxLines: 2, overflow: TextOverflow.ellipsis),
                  const SizedBox(height: 10),
                  Wrap(spacing: 6, runSpacing: 6, children: [
                    Pill(info.isDeep ? 'TEORIA COMPLETA' : 'TEORIA RESUMIDA', color: AppColors.blue),
                    if (!info.isDeep) const Pill('MAPA MENTAL', color: AppColors.teal),
                    if (info.questions > 0) Pill('${info.questions} QUESTÕES', color: AppColors.gold),
                    const Pill('PDF', color: AppColors.muted),
                    Pill('~${minutesLabel(info.minutes)}', color: AppColors.muted),
                  ]),
                  const SizedBox(height: 12),
                  Row(children: [
                    ReviewPill(info),
                    const Spacer(),
                    Text(best == null ? 'v${info.version}' : 'melhor líquida: $best/${info.questions}', style: AppText.small(AppColors.dim)),
                  ]),
                ]),
              ),
            ]),
          ),
        ),
      ),
    );
  }
}

class _ComingSoon extends StatelessWidget {
  const _ComingSoon();
  @override
  Widget build(BuildContext context) => SizedBox(
        width: 360,
        height: 236,
        child: Container(
          padding: const EdgeInsets.all(20),
          decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(12),
            border: Border.all(color: AppColors.line, style: BorderStyle.solid),
            color: AppColors.bg,
          ),
          child: Column(mainAxisAlignment: MainAxisAlignment.center, children: [
            const Icon(Icons.inventory_2_outlined, size: 34, color: AppColors.dim),
            const SizedBox(height: 10),
            Text('NOVOS CONTEÚDOS A CAMINHO', style: AppText.h3(AppColors.muted), textAlign: TextAlign.center),
            const SizedBox(height: 6),
            Text('Apostilas, mapas mentais, questões e videoaulas chegam nas próximas versões, matéria por matéria.',
                style: AppText.small(AppColors.dim), textAlign: TextAlign.center),
          ]),
        ),
      );
}

class _UserMaterialRow extends StatelessWidget {
  const _UserMaterialRow({required this.material});
  final UserMaterial material;

  @override
  Widget build(BuildContext context) {
    final app = AppScope.of(context);
    final m = material;
    final sub = m.subjectId == null ? null : app.catalog.subjectOrNull(m.subjectId!);
    final topic = m.topicId == null ? null : app.catalog.topic(m.topicId!);
    final icon = switch (m.kind) { 'video' => Icons.play_circle_outline, 'pdf' => Icons.picture_as_pdf_outlined, _ => Icons.link };
    return Container(
      margin: const EdgeInsets.only(bottom: 8),
      padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
      decoration: BoxDecoration(color: AppColors.panel, borderRadius: BorderRadius.circular(10), border: Border.all(color: AppColors.lineSoft)),
      child: Row(children: [
        Icon(icon, color: AppColors.gold),
        const SizedBox(width: 12),
        if (sub != null) ...[SubjectTag(sub), const SizedBox(width: 10)],
        Expanded(
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Text(m.title, style: AppText.strong()),
            Text(topic?.name ?? m.location, style: AppText.small(), maxLines: 1, overflow: TextOverflow.ellipsis),
          ]),
        ),
        TextButton.icon(
          onPressed: () async {
            final ok = await openExternal(m.location);
            if (!ok && context.mounted) toast(context, 'Não foi possível abrir: ${m.location}');
          },
          icon: const Icon(Icons.open_in_new, size: 16),
          label: const Text('ABRIR'),
        ),
        IconButton(
          tooltip: 'Remover',
          onPressed: () async {
            if (await confirm(context, 'Remover material', '“${m.title}” sai da sua lista. O arquivo ou link não é apagado.', ok: 'REMOVER')) {
              app.removeUserMaterial(m);
            }
          },
          icon: const Icon(Icons.delete_outline, size: 18, color: AppColors.muted),
        ),
      ]),
    );
  }
}

// ======================================================================== leitor

class MaterialReader extends StatefulWidget {
  const MaterialReader({super.key, required this.info, required this.onClose});
  final MaterialInfo info;
  final VoidCallback onClose;

  @override
  State<MaterialReader> createState() => _MaterialReaderState();
}

class _MaterialReaderState extends State<MaterialReader> {
  StudyMaterial? material;
  Object? error;
  int tab = 0;
  final scroll = ScrollController();

  @override
  void initState() {
    super.initState();
    _load();
  }

  void _load() {
    final app = AppScope.read(context);
    app.content.open(widget.info, app.bundle).then((m) {
      if (mounted) setState(() => material = m);
    }, onError: (Object e) {
      if (mounted) setState(() => error = e);
    });
  }

  /// Dono: troca a versão por banca para conferir (Cebraspe, AOCP, neutra).
  void _preview(String v) {
    final app = AppScope.read(context);
    app.content.preview = v == app.content.banca ? null : v;
    setState(() {
      material = null;
      error = null;
      tab = 0;
    });
    _load();
  }

  @override
  void dispose() {
    scroll.dispose();
    super.dispose();
  }

  Future<void> _openPdf() async {
    final app = AppScope.read(context);
    final m = material;
    if (m == null) return;
    try {
      final path = await app.pdfPathOf(m);
      if (path == null) return;
      final ok = await openExternal(path);
      if (!ok && mounted) toast(context, 'PDF salvo em: $path');
    } catch (e) {
      if (mounted) toast(context, 'Não foi possível abrir o PDF: $e');
    }
  }

  @override
  Widget build(BuildContext context) {
    final app = AppScope.of(context);
    final info = widget.info;
    final sub = app.catalog.subjectOrNull(info.subjectId);
    final m = material;
    final tabs = [
      if (m != null) ...m.sections.map((s) => s.title),
      if (m?.quiz != null) 'Questões (${m!.quiz!.questions.length})',
    ];
    return Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
      Container(
        padding: const EdgeInsets.fromLTRB(16, 14, 28, 0),
        decoration: const BoxDecoration(color: AppColors.panel, border: Border(bottom: BorderSide(color: AppColors.lineSoft))),
        child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
          Row(children: [
            IconButton(tooltip: 'Voltar para Materiais', onPressed: widget.onClose, icon: const Icon(Icons.arrow_back)),
            const SizedBox(width: 6),
            if (sub != null) ...[SubjectTag(sub, long: true), const SizedBox(width: 12)],
            Expanded(child: Text(info.title.toUpperCase(), style: AppText.h2(), overflow: TextOverflow.ellipsis)),
            Pill(info.kindLabel, color: info.isDeep ? AppColors.gold : AppColors.amber),
            const SizedBox(width: 10),
            if (app.reviewer) ...[_ReviewButton(info: info), const SizedBox(width: 10)],
            OutlinedButton.icon(onPressed: m?.pdf == null ? null : _openPdf, icon: const Icon(Icons.picture_as_pdf_outlined, size: 18), label: const Text('ABRIR PDF')),
          ]),
          if (app.reviewer && info.variants.isNotEmpty) ...[
            const SizedBox(height: 8),
            Row(children: [
              const SizedBox(width: 50),
              Text('VERSÃO POR BANCA', style: AppText.label()),
              const SizedBox(width: 10),
              for (final v in ['cebraspe', ...info.variants.where((x) => x != 'cebraspe')])
                Padding(
                  padding: const EdgeInsets.only(right: 6),
                  child: ChoiceChip(
                    label: Text(bancaVariantLabel(v) + (v == app.content.banca ? ' · do aluno' : '')),
                    selected: (m?.variant ?? app.content.variantFor(info)) == v,
                    onSelected: (_) => _preview(v),
                  ),
                ),
            ]),
          ],
          const SizedBox(height: 10),
          Row(children: [
            const SizedBox(width: 50),
            for (var i = 0; i < tabs.length; i++)
              _Tab(
                label: tabs[i],
                selected: tab == i,
                onTap: () {
                  setState(() => tab = i);
                  if (scroll.hasClients) scroll.jumpTo(0);
                  if (m != null && i < m.sections.length) app.setReadProgress(info.id, i);
                },
              ),
          ]),
        ]),
      ),
      Expanded(
        child: error != null
            ? EmptyState(icon: Icons.error_outline, title: 'Erro ao abrir', text: '$error')
            : m == null
                ? const Center(child: CircularProgressIndicator())
                : Scrollbar(
                    controller: scroll,
                    child: SingleChildScrollView(
                      controller: scroll,
                      padding: const EdgeInsets.fromLTRB(40, 28, 40, 60),
                      child: Center(
                        child: ConstrainedBox(
                          constraints: BoxConstraints(maxWidth: tab < m.sections.length && m.sections[tab].blocks.any((b) => b.type == 'mindmap') ? 1100 : 860),
                          child: tab < m.sections.length
                              ? _SectionView(section: m.sections[tab], material: m)
                              : QuizView(material: m),
                        ),
                      ),
                    ),
                  ),
      ),
    ]);
  }
}

/// Dono: libera o material para os alunos (ou recolhe para revisão), sem nova versão do app.
class _ReviewButton extends StatefulWidget {
  const _ReviewButton({required this.info});
  final MaterialInfo info;
  @override
  State<_ReviewButton> createState() => _ReviewButtonState();
}

class _ReviewButtonState extends State<_ReviewButton> {
  bool busy = false;

  Future<void> _toggle(AppController app, bool approve) async {
    final ok = await confirm(
      context,
      approve ? 'LIBERAR PARA OS ALUNOS' : 'RECOLHER PARA REVISÃO',
      approve
          ? 'Confirma que revisou "${widget.info.title}" (${widget.info.isDeep ? 'aprofundado' : 'resumo'})? '
              'Ele passa a aparecer para todos os alunos na próxima vez que abrirem o app.'
          : 'O material deixa de aparecer para os alunos até você liberar de novo.',
      ok: approve ? 'LIBERAR' : 'RECOLHER',
      danger: !approve,
    );
    if (!ok || !mounted) return;
    setState(() => busy = true);
    try {
      await app.setReviewed(widget.info, approve);
      if (mounted) toast(context, approve ? 'Material liberado para os alunos.' : 'Material recolhido para revisão.');
    } catch (e) {
      if (mounted) toast(context, 'Não foi possível salvar: $e');
    } finally {
      if (mounted) setState(() => busy = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    final app = AppScope.of(context);
    final approved = app.content.isApproved(widget.info);
    if (busy) return const SizedBox(width: 22, height: 22, child: CircularProgressIndicator(strokeWidth: 2));
    return approved
        ? TextButton.icon(
            onPressed: () => _toggle(app, false),
            icon: const Icon(Icons.undo, size: 18),
            label: const Text('RECOLHER PARA REVISÃO'),
          )
        : ElevatedButton.icon(
            style: ElevatedButton.styleFrom(backgroundColor: AppColors.green, foregroundColor: AppColors.bg),
            onPressed: () => _toggle(app, true),
            icon: const Icon(Icons.verified_outlined, size: 18),
            label: const Text('REVISEI · LIBERAR AOS ALUNOS'),
          );
  }
}

class _Tab extends StatelessWidget {
  const _Tab({required this.label, required this.selected, required this.onTap});
  final String label;
  final bool selected;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) => InkWell(
        onTap: onTap,
        child: Container(
          padding: const EdgeInsets.symmetric(horizontal: 18, vertical: 12),
          decoration: BoxDecoration(border: Border(bottom: BorderSide(color: selected ? AppColors.gold : Colors.transparent, width: 3))),
          child: Text(label.toUpperCase(), style: AppText.h3(selected ? AppColors.gold2 : AppColors.muted).copyWith(fontSize: 15)),
        ),
      );
}

class _SectionView extends StatelessWidget {
  const _SectionView({required this.section, required this.material});
  final ContentSection section;
  final StudyMaterial material;

  @override
  Widget build(BuildContext context) {
    return Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
      for (final b in section.blocks) BlockView(block: b, material: material),
      if (material.sources.isNotEmpty && section == material.sections.last) ...[
        const SizedBox(height: 28),
        Text('FONTES', style: AppText.label()),
        const SizedBox(height: 6),
        for (final s in material.sources) Text(s, style: AppText.small(AppColors.dim)),
      ],
    ]);
  }
}

/// Renderiza um bloco de conteúdo (formato JSON compartilhado com o gerador de PDF).
class BlockView extends StatelessWidget {
  const BlockView({super.key, required this.block, required this.material});
  final ContentBlock block;
  final StudyMaterial material;

  @override
  Widget build(BuildContext context) {
    final b = block;
    final body = AppText.body().copyWith(fontSize: 15.5, height: 1.6);
    switch (b.type) {
      case 'h2':
        return Padding(
          padding: const EdgeInsets.only(top: 22, bottom: 10),
          child: Row(children: [
            Container(width: 4, height: 22, color: AppColors.gold),
            const SizedBox(width: 12),
            Expanded(child: Text(b.text.toUpperCase(), style: AppText.h2().copyWith(fontSize: 22))),
          ]),
        );
      case 'h3':
        return Padding(padding: const EdgeInsets.only(top: 10, bottom: 6), child: Text(b.text.toUpperCase(), style: AppText.h3(AppColors.gold2)));
      case 'p':
        return Padding(padding: const EdgeInsets.only(bottom: 10), child: RichMd(b.text, style: body, boldColor: AppColors.gold2));
      case 'note':
        return Padding(padding: const EdgeInsets.only(bottom: 10), child: RichMd(b.text, style: AppText.small(AppColors.dim)));
      case 'bullets':
        return Padding(
          padding: const EdgeInsets.only(bottom: 10),
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            for (final it in b.items)
              Padding(
                padding: const EdgeInsets.only(bottom: 6),
                child: Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
                  Padding(padding: const EdgeInsets.only(top: 9, right: 12, left: 4), child: Container(width: 6, height: 6, color: AppColors.gold)),
                  Expanded(child: RichMd(it, style: body, boldColor: AppColors.gold2)),
                ]),
              ),
          ]),
        );
      case 'callout':
        final (bg, border, tcol) = switch (b.style) {
          'exam' => (AppColors.panel2, AppColors.gold, AppColors.gold2),
          'key' => (AppColors.gold.withValues(alpha: 0.10), AppColors.gold, AppColors.gold2),
          _ => (AppColors.red.withValues(alpha: 0.10), AppColors.red, AppColors.red),
        };
        final icon = switch (b.style) { 'exam' => Icons.gavel, 'key' => Icons.key, _ => Icons.warning_amber_rounded };
        return Container(
          margin: const EdgeInsets.only(top: 6, bottom: 14),
          decoration: BoxDecoration(color: bg, borderRadius: BorderRadius.circular(10), border: Border.all(color: border.withValues(alpha: 0.5))),
          padding: const EdgeInsets.fromLTRB(16, 14, 16, 14),
          child: Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Icon(icon, color: tcol, size: 20),
            const SizedBox(width: 12),
            Expanded(
              child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                Text(b.title.toUpperCase(), style: AppText.label(tcol).copyWith(fontSize: 13.5)),
                const SizedBox(height: 4),
                RichMd(b.text, style: body.copyWith(fontSize: 15), boldColor: AppColors.text),
              ]),
            ),
          ]),
        );
      case 'table':
        final widths = b.widths;
        final head = b.head;
        return Container(
          margin: const EdgeInsets.only(top: 4, bottom: 16),
          decoration: BoxDecoration(borderRadius: BorderRadius.circular(10), border: Border.all(color: AppColors.lineSoft)),
          clipBehavior: Clip.antiAlias,
          child: Table(
            columnWidths: {for (var i = 0; i < head.length; i++) i: FlexColumnWidth(i < widths.length ? widths[i] : 1)},
            defaultVerticalAlignment: TableCellVerticalAlignment.top,
            children: [
              TableRow(
                decoration: const BoxDecoration(color: AppColors.panel2, border: Border(bottom: BorderSide(color: AppColors.gold, width: 1.5))),
                children: [
                  for (final h in head) Padding(padding: const EdgeInsets.all(10), child: Text(h.toUpperCase(), style: AppText.label(AppColors.gold))),
                ],
              ),
              for (var r = 0; r < b.rows.length; r++)
                TableRow(
                  decoration: BoxDecoration(color: r.isOdd ? AppColors.panel : AppColors.bg),
                  children: [
                    for (var c = 0; c < b.rows[r].length; c++)
                      Padding(
                        padding: const EdgeInsets.all(10),
                        child: RichMd(
                          b.rows[r][c],
                          style: c == 0 ? AppText.strong(AppColors.text).copyWith(fontSize: 14) : AppText.body().copyWith(fontSize: 14),
                          boldColor: AppColors.gold2,
                        ),
                      ),
                  ],
                ),
            ],
          ),
        );
      case 'mindmap':
        final spec = material.mindmap;
        if (spec == null) return const SizedBox();
        return Padding(
          padding: const EdgeInsets.only(top: 22, bottom: 10),
          child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
            Row(children: [
              Container(width: 4, height: 22, color: AppColors.gold),
              const SizedBox(width: 12),
              Text('MAPA MENTAL', style: AppText.h2().copyWith(fontSize: 22)),
              const Spacer(),
              Text('role com o mouse para ampliar', style: AppText.small(AppColors.dim)),
            ]),
            const SizedBox(height: 12),
            MindMapView(spec: spec),
          ]),
        );
      default:
        return const SizedBox();
    }
  }
}

// ======================================================================== questões

class QuizView extends StatefulWidget {
  const QuizView({super.key, required this.material});
  final StudyMaterial material;

  @override
  State<QuizView> createState() => _QuizViewState();
}

class _QuizViewState extends State<QuizView> {
  final answers = <String, String?>{};
  QuizAttempt? result;
  final started = DateTime.now();

  @override
  Widget build(BuildContext context) {
    final app = AppScope.of(context);
    final quiz = widget.material.quiz!;
    final attempts = app.attemptsOf(widget.material.info.id);
    final r = result;
    final answered = answers.values.where((v) => v != null).length;
    return Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
      Row(children: [
        Expanded(
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Text(quiz.banca.toUpperCase(), style: AppText.label(AppColors.gold)),
            const SizedBox(height: 4),
            Text(quiz.instructions, style: AppText.body(AppColors.muted)),
          ]),
        ),
        if (attempts.isNotEmpty)
          Pill('${attempts.length} tentativa(s) · melhor ${quiz.penalty ? 'líquida' : 'nota'} ${attempts.map((a) => a.net).reduce((a, b) => a > b ? a : b)}', color: AppColors.muted),
      ]),
      const SizedBox(height: 18),
      if (r != null) _ResultBanner(result: r, total: quiz.questions.length, penalty: quiz.penalty, onRetry: () => setState(() {
            result = null;
            answers.clear();
          })),
      for (var i = 0; i < quiz.questions.length; i++) ...[
        if (quiz.questions[i].group.isNotEmpty && (i == 0 || quiz.questions[i - 1].group != quiz.questions[i].group))
          Padding(
            padding: const EdgeInsets.only(top: 6, bottom: 10),
            child: Text(quiz.questions[i].group.toUpperCase(), style: AppText.h3(AppColors.gold2)),
          ),
        if (quiz.questions[i].context.isNotEmpty)
          Container(
            margin: const EdgeInsets.only(bottom: 12),
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(
              color: AppColors.gold.withValues(alpha: 0.08),
              borderRadius: BorderRadius.circular(10),
              border: Border.all(color: AppColors.gold.withValues(alpha: 0.5)),
            ),
            child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              Text('TEXTO PARA OS PRÓXIMOS ITENS', style: AppText.label(AppColors.gold2)),
              const SizedBox(height: 6),
              RichMd(quiz.questions[i].context, style: AppText.body().copyWith(fontSize: 15, height: 1.55)),
            ]),
          ),
        _QuestionCard(
        index: i + 1,
        q: quiz.questions[i],
        penalty: quiz.penalty,
        answer: (r?.answers ?? answers)[quiz.questions[i].id],
        reveal: r != null,
        onAnswer: r != null ? null : (v) => setState(() => answers[quiz.questions[i].id] = answers[quiz.questions[i].id] == v ? null : v),
      ),
      ],
      const SizedBox(height: 10),
      if (r == null)
        Row(children: [
          Text('$answered de ${quiz.questions.length} respondidas · ${quiz.questions.length - answered} em branco', style: AppText.small()),
          const Spacer(),
          ElevatedButton.icon(
            onPressed: () {
              final minutes = DateTime.now().difference(started).inMinutes;
              final a = app.submitQuiz(widget.material, Map.of(answers), minutes: minutes.clamp(1, 240));
              setState(() => result = a);
              toast(context, 'Resultado lançado no diário: ${a.correct} certas, ${a.wrong} erradas.');
            },
            icon: const Icon(Icons.fact_check, size: 18),
            label: const Text('CORRIGIR E LANÇAR NO DIÁRIO'),
          ),
        ]),
    ]);
  }
}

class _ResultBanner extends StatelessWidget {
  const _ResultBanner({required this.result, required this.total, required this.onRetry, required this.penalty});
  final QuizAttempt result;
  final int total;
  final bool penalty;
  final VoidCallback onRetry;

  @override
  Widget build(BuildContext context) {
    final r = result;
    final answered = r.correct + r.wrong;
    final color = r.net >= total * 0.6 ? AppColors.green : (r.net <= 0 ? AppColors.red : AppColors.gold2);
    return Container(
      margin: const EdgeInsets.only(bottom: 18),
      padding: const EdgeInsets.all(18),
      decoration: BoxDecoration(color: AppColors.panel2, borderRadius: BorderRadius.circular(12), border: Border.all(color: color)),
      child: Row(children: [
        Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Text(penalty ? 'NOTA LÍQUIDA' : 'ACERTOS', style: AppText.label()),
          Text('${r.net}', style: AppText.kpi(color).copyWith(fontSize: 44)),
        ]),
        const SizedBox(width: 28),
        Expanded(
          child: Wrap(spacing: 22, runSpacing: 8, children: [
            _num('CERTAS', r.correct, AppColors.green),
            _num('ERRADAS', r.wrong, AppColors.red),
            _num('EM BRANCO', r.blank, AppColors.muted),
            _numText('ACERTO', answered == 0 ? '—' : pct(r.correct / answered), AppColors.text),
          ]),
        ),
        OutlinedButton.icon(onPressed: onRetry, icon: const Icon(Icons.replay, size: 18), label: const Text('REFAZER')),
      ]),
    );
  }

  Widget _num(String l, int v, Color c) => _numText(l, '$v', c);
  Widget _numText(String l, String v, Color c) => Column(crossAxisAlignment: CrossAxisAlignment.start, mainAxisSize: MainAxisSize.min, children: [
        Text(l, style: AppText.label()),
        Text(v, style: AppText.h1(c)),
      ]);
}

class _QuestionCard extends StatelessWidget {
  const _QuestionCard({required this.index, required this.q, required this.answer, required this.reveal, required this.onAnswer, required this.penalty});
  final int index;
  final QuizQuestion q;
  final bool penalty;
  final String? answer;
  final bool reveal;
  final ValueChanged<String>? onAnswer;

  @override
  Widget build(BuildContext context) {
    final right = answer != null && answer == q.answer;
    final wrong = answer != null && answer != q.answer;
    final border = !reveal ? AppColors.lineSoft : (right ? AppColors.green : (wrong ? AppColors.red : AppColors.line));
    return Container(
      margin: const EdgeInsets.only(bottom: 12),
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(color: AppColors.panel, borderRadius: BorderRadius.circular(12), border: Border.all(color: border, width: reveal ? 1.4 : 1)),
      child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
        Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Container(
            width: 34,
            height: 30,
            alignment: Alignment.center,
            decoration: BoxDecoration(color: AppColors.bg, borderRadius: BorderRadius.circular(6), border: Border.all(color: AppColors.gold)),
            child: Text(index.toString().padLeft(2, '0'), style: AppText.h3(AppColors.gold2)),
          ),
          const SizedBox(width: 14),
          Expanded(child: RichMd(q.text, style: AppText.body().copyWith(fontSize: 15.5, height: 1.55))),
          if (!q.isChoice) ...[
            const SizedBox(width: 14),
            for (final opt in const ['C', 'E'])
              Padding(
                padding: const EdgeInsets.only(left: 6),
                child: _OptButton(
                  label: opt,
                  selected: answer == opt,
                  correct: reveal && q.answer == opt,
                  onTap: onAnswer == null ? null : () => onAnswer!(opt),
                ),
              ),
          ],
        ]),
        if (q.isChoice)
          Padding(
            padding: const EdgeInsets.only(left: 48, top: 10),
            child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
              for (var k = 0; k < q.options.length; k++)
                _ChoiceRow(
                  letter: q.letters[k],
                  text: q.options[k],
                  selected: answer == q.letters[k],
                  correct: reveal && q.answer == q.letters[k],
                  onTap: onAnswer == null ? null : () => onAnswer!(q.letters[k]),
                ),
            ]),
          ),
        if (reveal) ...[
          const SizedBox(height: 12),
          Container(
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: AppColors.bg, borderRadius: BorderRadius.circular(8)),
            child: Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
              Icon(right ? Icons.check_circle : (wrong ? Icons.cancel : Icons.remove_circle_outline),
                  color: right ? AppColors.green : (wrong ? AppColors.red : AppColors.muted), size: 20),
              const SizedBox(width: 10),
              Expanded(
                child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                  Text(
                    'GABARITO: ${q.isChoice ? 'LETRA ${q.answer}' : (q.answer == 'C' ? 'CERTO' : 'ERRADO')}'
                    '${answer == null ? ' · em branco' : (right ? ' · você acertou' : (penalty && !q.isChoice ? ' · você errou (anula um acerto)' : ' · você errou'))}',
                    style: AppText.label(right ? AppColors.green : (wrong ? AppColors.red : AppColors.muted)),
                  ),
                  const SizedBox(height: 4),
                  RichMd(q.comment, style: AppText.body(AppColors.muted).copyWith(fontSize: 14.5), boldColor: AppColors.text),
                ]),
              ),
            ]),
          ),
        ],
      ]),
    );
  }
}

class _ChoiceRow extends StatelessWidget {
  const _ChoiceRow({required this.letter, required this.text, required this.selected, required this.correct, required this.onTap});
  final String letter;
  final String text;
  final bool selected;
  final bool correct;
  final VoidCallback? onTap;

  @override
  Widget build(BuildContext context) {
    final Color border = correct ? AppColors.green : (selected ? AppColors.gold : AppColors.lineSoft);
    return Padding(
      padding: const EdgeInsets.only(bottom: 6),
      child: Material(
        color: selected ? AppColors.gold.withValues(alpha: 0.12) : AppColors.field,
        borderRadius: BorderRadius.circular(8),
        child: InkWell(
          onTap: onTap,
          borderRadius: BorderRadius.circular(8),
          child: Container(
            padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 9),
            decoration: BoxDecoration(borderRadius: BorderRadius.circular(8), border: Border.all(color: border, width: correct ? 1.6 : 1)),
            child: Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
              Container(
                width: 26,
                height: 26,
                alignment: Alignment.center,
                decoration: BoxDecoration(
                  color: selected ? AppColors.gold : AppColors.bg,
                  borderRadius: BorderRadius.circular(13),
                  border: Border.all(color: correct ? AppColors.green : AppColors.line),
                ),
                child: Text(letter, style: AppText.label(selected ? AppColors.bg : AppColors.text)),
              ),
              const SizedBox(width: 10),
              Expanded(child: RichMd(text, style: AppText.body().copyWith(fontSize: 15, height: 1.5))),
            ]),
          ),
        ),
      ),
    );
  }
}

class _OptButton extends StatelessWidget {
  const _OptButton({required this.label, required this.selected, required this.correct, required this.onTap});
  final String label;
  final bool selected;
  final bool correct;
  final VoidCallback? onTap;

  @override
  Widget build(BuildContext context) {
    final Color bg = selected ? AppColors.gold : AppColors.field;
    final Color border = correct ? AppColors.green : (selected ? AppColors.gold : AppColors.line);
    return Tooltip(
      message: label == 'C' ? 'Certo' : 'Errado',
      child: Material(
        color: bg,
        borderRadius: BorderRadius.circular(8),
        child: InkWell(
          onTap: onTap,
          borderRadius: BorderRadius.circular(8),
          child: Container(
            width: 42,
            height: 38,
            alignment: Alignment.center,
            decoration: BoxDecoration(borderRadius: BorderRadius.circular(8), border: Border.all(color: border, width: correct ? 2 : 1)),
            child: Text(label, style: AppText.h2(selected ? AppColors.bg : AppColors.text).copyWith(fontSize: 18)),
          ),
        ),
      ),
    );
  }
}

String fmtAttempt(QuizAttempt a) => '${fmtDate(a.date)} · ${a.correct}C ${a.wrong}E ${a.blank}B';
