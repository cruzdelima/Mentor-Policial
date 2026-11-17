-- Imita o essencial do Supabase: papéis anon/authenticated, schema auth, auth.users e auth.uid().
drop database if exists mentor_test;
create database mentor_test;
\c mentor_test
create role anon nologin;
create role authenticated nologin;
grant usage on schema public to anon, authenticated;
-- Supabase concede tudo por padrão nas tabelas novas do public (a migração precisa revogar):
alter default privileges in schema public grant all on tables to anon, authenticated;
alter default privileges in schema public grant all on functions to anon, authenticated;
create schema auth;
grant usage on schema auth to anon, authenticated;
create table auth.users (id uuid primary key default gen_random_uuid(), email text, raw_user_meta_data jsonb default '{}');
create function auth.uid() returns uuid language sql stable as $$ select nullif(current_setting('request.jwt.claim.sub', true), '')::uuid $$;
grant execute on function auth.uid() to anon, authenticated;
