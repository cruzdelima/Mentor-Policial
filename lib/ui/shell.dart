import 'package:flutter/material.dart';

import '../core/dates.dart';
import '../data/storage.dart';
import '../state/app_state.dart';
import '../state/account.dart';
import 'pages/admin_page.dart';
import 'pages/contests_page.dart';
import 'pages/diary_page.dart';
import 'pages/edital_page.dart';
import 'pages/materials_page.dart';
import 'pages/method_page.dart';
import 'pages/missions_page.dart';
import 'pages/qg_page.dart';
import 'pages/settings_page.dart';
import 'theme.dart';
import 'widgets.dart';

class _NavItem {
  const _NavItem(this.page, this.label, this.icon, this.hint);
  final AppPage page;
  final String label;
  final IconData icon;
  final String hint;
}

const _nav = [
  _NavItem(AppPage.qg, 'QG', Icons.space_dashboard_outlined, 'Central de comando'),
  _NavItem(AppPage.missions, 'Missões', Icons.flag_outlined, 'Cronograma diário'),
  _NavItem(AppPage.edital, 'Edital', Icons.checklist_rtl, 'Edital verticalizado'),
  _NavItem(AppPage.diary, 'Diário', Icons.edit_note, 'Lançamentos de estudo'),
  _NavItem(AppPage.materials, 'Materiais', Icons.menu_book_outlined, 'Apostilas e questões'),
  _NavItem(AppPage.contests, 'Pós-edital', Icons.campaign_outlined, 'Concursos com edital publicado'),
  _NavItem(AppPage.method, 'Método', Icons.military_tech_outlined, 'Como o autor foi aprovado'),
  _NavItem(AppPage.settings, 'Ajustes', Icons.tune, 'Perfil, rotina e dados'),
];

class Shell extends StatelessWidget {
  const Shell({super.key});

  @override
  Widget build(BuildContext context) {
    final app = AppScope.of(context);
    final page = switch (app.page) {
      AppPage.qg => const QgPage(),
      AppPage.missions => const MissionsPage(),
      AppPage.edital => const EditalPage(),
      AppPage.diary => const DiaryPage(),
      AppPage.materials => const MaterialsPage(),
      AppPage.contests => const ContestsPage(),
      AppPage.method => const MethodPage(),
      AppPage.settings => const SettingsPage(),
      AppPage.admin => const AdminPage(),
    };
    return Scaffold(
      body: LayoutBuilder(builder: (context, c) {
        final compact = c.maxWidth < 1280;
        return Row(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            _Sidebar(compact: compact),
            Expanded(
              child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
                if (app.update != null && !app.updateDismissed) _UpdateBanner(version: app.update!.version, url: app.update!.url),
                Expanded(
                  child: AnimatedSwitcher(
                    duration: const Duration(milliseconds: 180),
                    child: KeyedSubtree(key: ValueKey(app.page), child: page),
                  ),
                ),
              ]),
            ),
          ],
        );
      }),
    );
  }
}

class _Sidebar extends StatelessWidget {
  const _Sidebar({required this.compact});
  final bool compact;

  @override
  Widget build(BuildContext context) {
    final app = AppScope.of(context);
    final p = app.profile;
    final exam = p.examDate;
    final daysLeft = exam == null ? null : daysBetween(app.today, exam);
    final overdue = app.schedule?.overdue.length ?? 0;
    return Container(
      width: compact ? 76 : 236,
      color: AppColors.sidebar,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          const TapeBand(height: 18),
          Padding(
            padding: EdgeInsets.fromLTRB(compact ? 16 : 20, 20, 16, 22),
            child: Row(children: [
              const BadgeLogo(size: 38),
              if (!compact) ...[
                const SizedBox(width: 12),
                Expanded(
                  child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                    Text('TATICUM', style: AppText.h2(AppColors.gold2).copyWith(fontSize: 24, letterSpacing: 3, height: 1.0)),
                    Text('MENTOR POLICIAL', style: AppText.label(AppColors.muted).copyWith(fontSize: 10.1, letterSpacing: 2.2)),
                  ]),
                ),
              ],
            ]),
          ),
          Expanded(
            child: ListView(padding: EdgeInsets.zero, children: [
              for (final n in [
                ..._nav,
                if (AccountScope.maybeOf(context)?.isAdmin ?? false)
                  const _NavItem(AppPage.admin, 'Admin', Icons.admin_panel_settings_outlined, 'Contas, permissões e catálogo'),
              ])
                _NavButton(
                  item: n,
                  compact: compact,
                  selected: app.page == n.page,
                  badge: n.page == AppPage.missions && overdue > 0
                      ? '$overdue'
                      : (n.page == AppPage.contests && app.cargo.isContest ? 'ON' : null),
                  onTap: () => app.goTo(n.page),
                ),
            ]),
          ),
          if (!compact)
            Container(
              margin: const EdgeInsets.fromLTRB(14, 0, 14, 12),
              padding: const EdgeInsets.all(14),
              decoration: BoxDecoration(
                color: AppColors.panel,
                borderRadius: BorderRadius.circular(10),
                border: Border.all(color: AppColors.lineSoft),
              ),
              child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                Text(p.name.isEmpty ? 'ALUNO' : p.name.toUpperCase(), style: AppText.h3(), maxLines: 1, overflow: TextOverflow.ellipsis),
                const SizedBox(height: 2),
                Text(app.cargo.name, style: AppText.small(), maxLines: 2, overflow: TextOverflow.ellipsis),
                const SizedBox(height: 8),
                Wrap(spacing: 6, runSpacing: 6, children: [
                  if (AccountScope.maybeOf(context)?.offline ?? false) const Pill('OFFLINE', color: AppColors.amber),
                  Pill(p.esfera.toUpperCase(), color: AppColors.esfera(p.esfera), filled: true),
                  if (daysLeft != null && daysLeft >= 0) Pill('PROVA EM $daysLeft D', color: AppColors.gold),
                ]),
              ]),
            ),
          Padding(
            padding: const EdgeInsets.fromLTRB(16, 0, 16, 14),
            child: Text(compact ? 'β $kAppVersion' : '$kAppChannel · v$kAppVersion',
                style: AppText.small(AppColors.dim).copyWith(fontSize: 11), textAlign: compact ? TextAlign.center : TextAlign.left),
          ),
        ],
      ),
    );
  }
}

class _NavButton extends StatelessWidget {
  const _NavButton({required this.item, required this.compact, required this.selected, required this.onTap, this.badge});
  final _NavItem item;
  final bool compact;
  final bool selected;
  final VoidCallback onTap;
  final String? badge;

  @override
  Widget build(BuildContext context) {
    final color = selected ? AppColors.gold2 : AppColors.muted;
    final body = Container(
      height: 46,
      margin: const EdgeInsets.symmetric(horizontal: 10, vertical: 2),
      decoration: BoxDecoration(
        color: selected ? AppColors.panel2 : Colors.transparent,
        borderRadius: BorderRadius.circular(8),
        border: Border(left: BorderSide(color: selected ? AppColors.gold : Colors.transparent, width: 3)),
      ),
      padding: EdgeInsets.symmetric(horizontal: compact ? 0 : 12),
      child: Row(
        mainAxisAlignment: compact ? MainAxisAlignment.center : MainAxisAlignment.start,
        children: [
          Icon(item.icon, size: 21, color: color),
          if (!compact) ...[
            const SizedBox(width: 12),
            Expanded(child: Text(item.label.toUpperCase(), style: AppText.h3(selected ? AppColors.text : AppColors.muted).copyWith(fontSize: 15))),
            if (badge != null) Pill(badge!, color: item.page == AppPage.missions ? AppColors.red : AppColors.gold, filled: true),
          ],
        ],
      ),
    );
    return Tooltip(
      message: compact ? '${item.label} · ${item.hint}' : item.hint,
      waitDuration: const Duration(milliseconds: 600),
      child: Material(color: Colors.transparent, child: InkWell(onTap: onTap, borderRadius: BorderRadius.circular(8), child: body)),
    );
  }
}

class _UpdateBanner extends StatelessWidget {
  const _UpdateBanner({required this.version, required this.url});
  final String version;
  final String url;

  @override
  Widget build(BuildContext context) {
    final app = AppScope.read(context);
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 10),
      color: AppColors.gold,
      child: Row(children: [
        const Icon(Icons.system_update_alt, color: AppColors.bg),
        const SizedBox(width: 12),
        Expanded(
          child: Text(
            'Nova versão $version disponível. Baixe e instale por cima: seus dados continuam salvos.',
            style: AppText.strong(AppColors.bg),
          ),
        ),
        TextButton(
          onPressed: app.dismissUpdate,
          style: TextButton.styleFrom(foregroundColor: AppColors.bg),
          child: const Text('DEPOIS'),
        ),
        const SizedBox(width: 6),
        ElevatedButton.icon(
          style: ElevatedButton.styleFrom(backgroundColor: AppColors.bg, foregroundColor: AppColors.gold2),
          onPressed: () => openExternal(url),
          icon: const Icon(Icons.download, size: 18),
          label: const Text('BAIXAR ATUALIZAÇÃO'),
        ),
      ]),
    );
  }
}
