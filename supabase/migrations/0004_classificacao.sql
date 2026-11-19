-- =====================================================================================
-- Taticum · 0004 · Classificação dos alunos (plano de acesso)
--
-- Classificações (coluna profiles.plan):
--   none     Sem classificação
--   beta     Testador Beta      · manual (só o dono) · acesso gratuito · dá feedback com frequência
--   tester   Testador Gratuito  · manual (só o dono) · acesso gratuito · familiares e amigos
--   monthly  Assinante mensal   · automática (servidor de pagamentos, no futuro)
--   annual   Assinante anual    · automática (servidor de pagamentos, no futuro)
--
-- O aluno lê a própria classificação, mas não a altera (só tem permissão de editar nome e telefone).
-- O dono classifica pela função set_plan. Mensal e anual nunca são definidos pelo app: virão do pagamento,
-- com a service role, preenchendo plan, plan_expires_at e plan_source = 'pagamento'.
--
-- Rode no SQL Editor do Supabase depois das migrações 0001 a 0003.
-- =====================================================================================

alter table public.profiles add column if not exists plan_note text not null default '' check (char_length(plan_note) <= 200);
alter table public.profiles add column if not exists plan_source text not null default 'manual';
alter table public.profiles add column if not exists plan_updated_at timestamptz;

-- 'free' era o valor padrão provisório: passa a ser "sem classificação".
update public.profiles set plan = 'none' where plan is null or plan not in ('none', 'beta', 'tester', 'monthly', 'annual');
alter table public.profiles alter column plan set default 'none';
alter table public.profiles drop constraint if exists profiles_plan_check;
alter table public.profiles add constraint profiles_plan_check check (plan in ('none', 'beta', 'tester', 'monthly', 'annual'));
alter table public.profiles drop constraint if exists profiles_plan_source_check;
alter table public.profiles add constraint profiles_plan_source_check check (plan_source in ('manual', 'pagamento'));

-- Classificar um aluno. Só o dono, e só as classificações manuais.
create or replace function public.set_plan(target uuid, new_plan text, note text default '')
returns void
language plpgsql security definer set search_path = ''
as $$
declare
  cur record;
begin
  if public.my_role() is distinct from 'owner' then
    raise exception 'Apenas o dono pode classificar alunos.' using errcode = '42501';
  end if;
  if new_plan is null or new_plan not in ('none', 'beta', 'tester', 'monthly', 'annual') then
    raise exception 'Classificação desconhecida.' using errcode = '22023';
  end if;
  if new_plan in ('monthly', 'annual') then
    raise exception 'Assinante mensal e anual são definidos automaticamente pelo pagamento.' using errcode = '22023';
  end if;
  select role, plan, plan_expires_at into cur from public.profiles where id = target;
  if not found then
    raise exception 'Conta não encontrada.' using errcode = 'P0002';
  end if;
  if cur.role = 'owner' then
    raise exception 'A conta do dono não recebe classificação.' using errcode = '22023';
  end if;
  if cur.plan in ('monthly', 'annual') and (cur.plan_expires_at is null or cur.plan_expires_at > now()) then
    raise exception 'Esta conta tem assinatura ativa; a classificação é controlada pelo pagamento.' using errcode = '22023';
  end if;
  update public.profiles
     set plan = new_plan, plan_note = left(coalesce(note, ''), 200), plan_source = 'manual',
         plan_expires_at = null, plan_updated_at = now()
   where id = target;
  insert into public.audit_log (actor, action, target, detail)
  values (auth.uid(), 'alterou classificação', target, cur.plan || ' › ' || new_plan);
end;
$$;

-- Acesso ao app de quem está chamando (para quando ele for pago): dono, administradores, testadores e assinaturas em dia.
create or replace function public.has_access()
returns boolean
language sql stable security definer set search_path = ''
as $$
  select coalesce((
    select p.role in ('owner', 'admin')
        or p.plan in ('beta', 'tester')
        or (p.plan in ('monthly', 'annual') and p.plan_expires_at > now())
      from public.profiles p where p.id = auth.uid()
  ), false)
$$;

revoke execute on function public.set_plan(uuid, text, text) from public, anon;
revoke execute on function public.has_access()               from public, anon;
grant  execute on function public.set_plan(uuid, text, text) to authenticated;
grant  execute on function public.has_access()               to authenticated;
