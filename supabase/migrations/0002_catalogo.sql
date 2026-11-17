-- Taticum — catálogo editável pelo dono e pelos administradores.
--
-- O app já traz um catálogo embutido (carreiras, cargos, matérias, assuntos).
-- Esta tabela guarda as ALTERAÇÕES feitas no editor do app (novas áreas, cargos,
-- matérias e concursos pós-edital). Todos os alunos leem; só dono/administradores
-- gravam, e sempre pela função save_catalog(), que valida, guarda o histórico
-- e registra a mudança na auditoria.
--
-- Rodar no SQL Editor do Supabase DEPOIS de 0001_contas.sql.

create table public.catalog_docs (
  key         text primary key check (key in ('extras')),
  data        jsonb not null check (jsonb_typeof(data) = 'object' and pg_column_size(data) < 2000000),
  version     integer not null default 1,
  updated_at  timestamptz not null default now(),
  updated_by  uuid references auth.users (id) on delete set null
);

create table public.catalog_history (
  id          bigint generated always as identity primary key,
  key         text not null,
  version     integer not null,
  data        jsonb not null,
  at          timestamptz not null default now(),
  by          uuid references auth.users (id) on delete set null,
  note        text not null default '' check (char_length(note) <= 200)
);

alter table public.catalog_docs    enable row level security;
alter table public.catalog_history enable row level security;

-- Qualquer pessoa com o app (mesmo antes do login) pode LER o catálogo: não há dado pessoal nele.
create policy "todos leem o catálogo" on public.catalog_docs
  for select to anon, authenticated using (true);

create policy "administradores leem o histórico" on public.catalog_history
  for select to authenticated using ((select public.my_role()) in ('admin', 'owner'));

revoke all on public.catalog_docs    from anon, authenticated;
revoke all on public.catalog_history from anon, authenticated;
grant select on public.catalog_docs    to anon, authenticated;
grant select on public.catalog_history to authenticated;

-- Gravação: só pela função abaixo (ninguém tem insert/update direto na tabela).
create or replace function public.save_catalog(new_data jsonb, base_version integer, note text default '')
returns integer
language plpgsql
security definer
set search_path = ''
as $$
declare
  current_version integer;
  next_version integer;
begin
  if coalesce((select public.my_role())::text, '') not in ('admin', 'owner') then
    raise exception 'apenas o dono ou administradores podem alterar o catálogo';
  end if;
  if new_data is null or jsonb_typeof(new_data) <> 'object' then
    raise exception 'catálogo inválido';
  end if;
  if pg_column_size(new_data) >= 2000000 then
    raise exception 'catálogo grande demais';
  end if;

  select version into current_version from public.catalog_docs where key = 'extras' for update;

  -- Evita que duas pessoas editando ao mesmo tempo apaguem o trabalho uma da outra.
  if coalesce(current_version, 0) <> coalesce(base_version, 0) then
    raise exception 'o catálogo foi alterado por outra pessoa; recarregue antes de salvar';
  end if;

  next_version := coalesce(current_version, 0) + 1;

  insert into public.catalog_docs (key, data, version, updated_at, updated_by)
  values ('extras', new_data, next_version, now(), auth.uid())
  on conflict (key) do update
    set data = excluded.data, version = excluded.version,
        updated_at = excluded.updated_at, updated_by = excluded.updated_by;

  insert into public.catalog_history (key, version, data, by, note)
  values ('extras', next_version, new_data, auth.uid(), left(coalesce(note, ''), 200));

  insert into public.audit_log (actor, action, target, detail)
  values (auth.uid(), 'alterou o catálogo', null, 'versão ' || next_version || coalesce(': ' || nullif(left(note, 150), ''), ''));

  return next_version;
end;
$$;

revoke execute on function public.save_catalog(jsonb, integer, text) from public, anon;
grant  execute on function public.save_catalog(jsonb, integer, text) to authenticated;
