-- =====================================================================================
-- Taticum · 0001 · Contas, papéis e auditoria
-- Rode uma única vez no Supabase: SQL Editor › New query › colar › Run.
--
-- Princípios:
--   * Senhas ficam só no Supabase Auth (hash bcrypt). Este banco nunca vê senha.
--   * Row Level Security (RLS) em todas as tabelas: cada aluno só lê o próprio perfil;
--     administradores leem a lista; ninguém altera o próprio papel.
--   * Papel (aluno/admin/dono) só muda pela função set_role, que só o dono pode chamar,
--     e toda mudança fica registrada em audit_log.
--   * O papel de quem se cadastra é sempre 'student' (nunca vem do app).
-- =====================================================================================

create type public.app_role as enum ('student', 'admin', 'owner');

-- ------------------------------------------------------------------ perfis
create table public.profiles (
  id               uuid primary key references auth.users (id) on delete cascade,
  email            text not null,
  name             text not null default '' check (char_length(name) <= 120),
  phone            text not null default '' check (phone = '' or phone ~ '^\+55[1-9][0-9]9?[0-9]{8}$'),
  role             public.app_role not null default 'student',
  -- Assinatura (preenchida no futuro pelo servidor de pagamentos; o app só lê).
  plan             text not null default 'free',
  plan_expires_at  timestamptz,
  accepted_terms_at timestamptz,
  created_at       timestamptz not null default now()
);

-- Só pode existir um dono.
create unique index profiles_one_owner on public.profiles ((role)) where role = 'owner';

alter table public.profiles enable row level security;

-- Papel de quem está chamando. SECURITY DEFINER evita recursão nas políticas.
create or replace function public.my_role()
returns public.app_role
language sql stable security definer set search_path = ''
as $$
  select role from public.profiles where id = auth.uid()
$$;

create policy "aluno lê o próprio perfil" on public.profiles
  for select to authenticated using (id = (select auth.uid()));

create policy "administradores leem todos os perfis" on public.profiles
  for select to authenticated using ((select public.my_role()) in ('admin', 'owner'));

create policy "aluno edita o próprio perfil" on public.profiles
  for update to authenticated using (id = (select auth.uid())) with check (id = (select auth.uid()));

-- Permissões de tabela: anônimos não veem nada; o aluno só consegue alterar nome e telefone.
revoke all on public.profiles from anon, authenticated;
grant select on public.profiles to authenticated;
grant update (name, phone) on public.profiles to authenticated;

-- Cria o perfil quando alguém se cadastra. O papel é sempre 'student'.
create or replace function public.handle_new_user()
returns trigger
language plpgsql security definer set search_path = ''
as $$
begin
  insert into public.profiles (id, email, name, phone, accepted_terms_at)
  values (
    new.id,
    lower(new.email),
    left(coalesce(new.raw_user_meta_data ->> 'name', ''), 120),
    coalesce(new.raw_user_meta_data ->> 'phone', ''),
    case when (new.raw_user_meta_data ->> 'accepted_terms') = 'true' then now() end
  );
  return new;
end;
$$;

create trigger on_auth_user_created
  after insert on auth.users
  for each row execute function public.handle_new_user();

-- ------------------------------------------------------------------ auditoria
create table public.audit_log (
  id      bigint generated always as identity primary key,
  at      timestamptz not null default now(),
  actor   uuid,
  action  text not null,
  target  uuid,
  detail  text not null default ''
);

alter table public.audit_log enable row level security;

create policy "administradores leem a auditoria" on public.audit_log
  for select to authenticated using ((select public.my_role()) in ('admin', 'owner'));

revoke all on public.audit_log from anon, authenticated;
grant select on public.audit_log to authenticated;

-- Visão com e-mails, respeitando o RLS de quem consulta (security_invoker).
create view public.audit_log_view with (security_invoker = true) as
  select a.at, a.action, a.detail,
         coalesce(pa.email, a.actor::text, 'sistema') as actor_email,
         coalesce(pt.email, a.target::text, '')       as target_email
  from public.audit_log a
  left join public.profiles pa on pa.id = a.actor
  left join public.profiles pt on pt.id = a.target;

revoke all on public.audit_log_view from anon, authenticated;
grant select on public.audit_log_view to authenticated;

-- ------------------------------------------------------------------ funções chamadas pelo app

-- Conceder/remover administrador. Só o dono. Não cria outro dono nem altera o próprio papel.
create or replace function public.set_role(target uuid, new_role public.app_role)
returns void
language plpgsql security definer set search_path = ''
as $$
declare
  old_role public.app_role;
begin
  if public.my_role() is distinct from 'owner' then
    raise exception 'Apenas o dono pode alterar permissões.' using errcode = '42501';
  end if;
  if new_role = 'owner' then
    raise exception 'Não é possível criar outro dono pelo app.' using errcode = '22023';
  end if;
  if target = auth.uid() then
    raise exception 'O dono não pode alterar a própria permissão.' using errcode = '22023';
  end if;
  select role into old_role from public.profiles where id = target;
  if old_role is null then
    raise exception 'Conta não encontrada.' using errcode = 'P0002';
  end if;
  update public.profiles set role = new_role where id = target;
  insert into public.audit_log (actor, action, target, detail)
  values (auth.uid(), 'alterou permissão', target, old_role::text || ' › ' || new_role::text);
end;
$$;

-- Excluir a própria conta (direito do titular, LGPD art. 18). O dono não se exclui pelo app.
create or replace function public.delete_my_account()
returns void
language plpgsql security definer set search_path = ''
as $$
begin
  if auth.uid() is null then
    raise exception 'Não autenticado.' using errcode = '42501';
  end if;
  if public.my_role() = 'owner' then
    raise exception 'A conta do dono não pode ser excluída pelo app.' using errcode = '42501';
  end if;
  insert into public.audit_log (actor, action, target, detail) values (auth.uid(), 'excluiu a própria conta', null, '');
  delete from auth.users where id = auth.uid();
end;
$$;

revoke execute on function public.my_role()                              from public, anon;
revoke execute on function public.set_role(uuid, public.app_role)        from public, anon;
revoke execute on function public.delete_my_account()                    from public, anon;
revoke execute on function public.handle_new_user()                      from public, anon, authenticated;
grant  execute on function public.my_role()                              to authenticated;
grant  execute on function public.set_role(uuid, public.app_role)        to authenticated;
grant  execute on function public.delete_my_account()                    to authenticated;

-- =====================================================================================
-- DEPOIS de criar a SUA conta pelo app, rode (trocando o e-mail) para virar o dono:
--
--   update public.profiles set role = 'owner' where email = lower('seu-email@exemplo.com');
--
-- Isso só pode ser feito aqui, no painel do Supabase, nunca pelo app.
-- =====================================================================================
