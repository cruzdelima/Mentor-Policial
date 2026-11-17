-- Taticum — convites pelo painel do Supabase.
--
-- Quem é convidado em Authentication › Users › Invite ganha um perfil vazio (sem nome,
-- celular e aceite dos termos). Quando essa pessoa cria a conta pelo app com o mesmo
-- e-mail, o Supabase só atualiza os dados do usuário; este gatilho copia nome, celular
-- e aceite dos termos para o perfil, sem nunca sobrescrever o que já estiver preenchido
-- e sem tocar no papel (role).
--
-- Rodar no SQL Editor do Supabase DEPOIS de 0002_catalogo.sql.

create or replace function public.handle_user_metadata()
returns trigger
language plpgsql security definer set search_path = ''
as $$
declare
  new_phone text := coalesce(new.raw_user_meta_data ->> 'phone', '');
begin
  update public.profiles p
     set name = case when p.name = '' then left(coalesce(new.raw_user_meta_data ->> 'name', ''), 120) else p.name end,
         phone = case when p.phone = '' and new_phone ~ '^\+55[1-9][0-9]9?[0-9]{8}$' then new_phone else p.phone end,
         accepted_terms_at = coalesce(p.accepted_terms_at,
           case when (new.raw_user_meta_data ->> 'accepted_terms') = 'true' then now() end)
   where p.id = new.id;
  return new;
end;
$$;

create trigger on_auth_user_metadata_updated
  after update of raw_user_meta_data on auth.users
  for each row execute function public.handle_user_metadata();

revoke execute on function public.handle_user_metadata() from public, anon, authenticated;
