-- =====================================================================================
-- Taticum · 0005 · Progresso de estudo salvo na nuvem
--
-- Uma linha por aluno com os dados de estudo (o mesmo JSON que o app grava no computador): perfil de estudo,
-- missões concluídas, diário, questões respondidas, progresso de leitura.
--
-- Regras:
--   * Cada aluno lê apenas a própria linha. Nem administradores nem o dono leem o progresso dos alunos.
--   * A gravação é feita só pela função save_study, com controle de versão: se outro aparelho gravou antes,
--     a função recusa (código TS409) e o app pergunta ao aluno qual versão manter.
--   * Ao excluir a conta, o progresso é apagado junto (on delete cascade).
--
-- Rode no SQL Editor do Supabase depois das migrações 0001 a 0004.
-- =====================================================================================

create table if not exists public.study_data (
  user_id    uuid primary key references public.profiles (id) on delete cascade,
  data       jsonb not null,
  version    integer not null default 1,
  device     text not null default '' check (char_length(device) <= 80),
  updated_at timestamptz not null default now()
);

alter table public.study_data enable row level security;

drop policy if exists "aluno lê o próprio progresso" on public.study_data;
create policy "aluno lê o próprio progresso" on public.study_data
  for select to authenticated using (user_id = (select auth.uid()));

revoke all on public.study_data from anon, authenticated;
grant select on public.study_data to authenticated;

-- Grava o progresso do próprio aluno. base_version = versão que o aparelho recebeu da última vez (0 = nunca gravou).
create or replace function public.save_study(new_data jsonb, base_version integer, device_name text default '')
returns integer
language plpgsql security definer set search_path = ''
as $$
declare
  uid uuid := auth.uid();
  cur integer;
begin
  if uid is null then
    raise exception 'Não autenticado.' using errcode = '42501';
  end if;
  if not exists (select 1 from public.profiles where id = uid) then
    raise exception 'Perfil não encontrado.' using errcode = 'P0002';
  end if;
  if new_data is null or jsonb_typeof(new_data) <> 'object' then
    raise exception 'Dados de estudo inválidos.' using errcode = '22023';
  end if;
  if pg_column_size(new_data) > 5000000 then
    raise exception 'Dados de estudo grandes demais para salvar na nuvem.' using errcode = '22023';
  end if;

  select version into cur from public.study_data where user_id = uid for update;
  if cur is null then
    if coalesce(base_version, 0) <> 0 then
      raise exception 'Os dados de estudo mudaram em outro aparelho.' using errcode = 'TS409';
    end if;
    insert into public.study_data (user_id, data, version, device)
    values (uid, new_data, 1, left(coalesce(device_name, ''), 80));
    return 1;
  end if;

  if coalesce(base_version, -1) <> cur then
    raise exception 'Os dados de estudo mudaram em outro aparelho.' using errcode = 'TS409';
  end if;
  update public.study_data
     set data = new_data, version = cur + 1, device = left(coalesce(device_name, ''), 80), updated_at = now()
   where user_id = uid;
  return cur + 1;
end;
$$;

revoke execute on function public.save_study(jsonb, integer, text) from public, anon;
grant  execute on function public.save_study(jsonb, integer, text) to authenticated;
