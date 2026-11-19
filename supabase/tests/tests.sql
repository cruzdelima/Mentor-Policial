\set ON_ERROR_STOP off
\set VERBOSITY terse
-- três contas: dono, aluno A, aluno B
insert into auth.users (id, email, raw_user_meta_data) values
 ('00000000-0000-0000-0000-000000000001','DONO@x.com','{"name":"Dono","phone":"+5585999990001","accepted_terms":true,"role":"owner"}'),
 ('00000000-0000-0000-0000-00000000000a','a@x.com','{"name":"Aluno A","phone":"+5585999990002","accepted_terms":true}'),
 ('00000000-0000-0000-0000-00000000000b','b@x.com','{"name":"Aluno B","phone":"+5511988887777","accepted_terms":true}');
select 'T01 papel nunca vem do cadastro (deve ser student)' t, role from public.profiles where id='00000000-0000-0000-0000-000000000001';
update public.profiles set role='owner' where email = lower('dono@x.com');
select 'T02 e-mail normalizado' t, email from public.profiles where id='00000000-0000-0000-0000-000000000001';

-- ===== anônimo
set role anon;
select 'T03 anônimo lê perfis (deve dar erro)' t; select count(*) from public.profiles;
reset role;

-- ===== aluno A
set role authenticated; select set_config('request.jwt.claim.sub','00000000-0000-0000-0000-00000000000a',false);
select 'T04 aluno vê só o próprio perfil (1)' t, count(*) from public.profiles;
select 'T05 aluno muda o próprio papel (deve dar erro)' t; update public.profiles set role='admin' where id='00000000-0000-0000-0000-00000000000a';
select 'T06 aluno muda plano (deve dar erro)' t; update public.profiles set plan='premium' where id='00000000-0000-0000-0000-00000000000a';
select 'T07 aluno edita nome do outro (0 linhas)' t; update public.profiles set name='hack' where id='00000000-0000-0000-0000-00000000000b';
select 'T08 aluno edita o próprio nome' t; update public.profiles set name='Aluno A2', phone='+5585988887777' where id='00000000-0000-0000-0000-00000000000a';
select 'T09 telefone inválido (deve dar erro)' t; update public.profiles set phone='123' where id='00000000-0000-0000-0000-00000000000a';
select 'T10 aluno chama set_role (deve dar erro)' t; select public.set_role('00000000-0000-0000-0000-00000000000a','admin');
select 'T11 aluno lê auditoria (0)' t, count(*) from public.audit_log_view;
reset role;

-- ===== dono
set role authenticated; select set_config('request.jwt.claim.sub','00000000-0000-0000-0000-000000000001',false);
select 'T12 dono vê todos (3)' t, count(*) from public.profiles;
select 'T13 dono torna A admin' t; select public.set_role('00000000-0000-0000-0000-00000000000a','admin');
select 'T14 dono cria outro dono (deve dar erro)' t; select public.set_role('00000000-0000-0000-0000-00000000000b','owner');
select 'T15 dono altera a si mesmo (deve dar erro)' t; select public.set_role('00000000-0000-0000-0000-000000000001','admin');
select 'T16 dono exclui a própria conta (deve dar erro)' t; select public.delete_my_account();
reset role;

-- ===== A agora é admin
set role authenticated; select set_config('request.jwt.claim.sub','00000000-0000-0000-0000-00000000000a',false);
select 'T17 admin vê todos (3)' t, count(*) from public.profiles;
select 'T18 admin concede admin a B (deve dar erro: só o dono)' t; select public.set_role('00000000-0000-0000-0000-00000000000b','admin');
select 'T19 admin vê auditoria (1)' t, count(*) from public.audit_log_view;
select 'T20 admin altera papel direto na tabela (deve dar erro)' t; update public.profiles set role='owner' where id='00000000-0000-0000-0000-00000000000a';
select 'T21 admin apaga auditoria (deve dar erro)' t; delete from public.audit_log;
reset role;

-- ===== B exclui a própria conta
set role authenticated; select set_config('request.jwt.claim.sub','00000000-0000-0000-0000-00000000000b',false);
select 'T22 B exclui a própria conta' t; select public.delete_my_account();
reset role;
select 'T23 B sumiu de auth.users e profiles (0, 0)' t, (select count(*) from auth.users where email='b@x.com'), (select count(*) from public.profiles where email='b@x.com');
select 'T24 auditoria' t, action, detail, actor_email, target_email from public.audit_log_view order by at;

-- ===== catálogo editável (0002)
set role anon;
select 'T25 anônimo lê o catálogo (0)' t, count(*) from public.catalog_docs;
select 'T26 anônimo salva catálogo (deve dar erro)' t; select public.save_catalog('{"contests":[]}'::jsonb, 0, 'x');
select 'T27 anônimo grava direto na tabela (deve dar erro)' t; insert into public.catalog_docs (key, data) values ('extras', '{}');
reset role;
set role authenticated; select set_config('request.jwt.claim.sub','00000000-0000-0000-0000-000000000099',false);
select 'T28 usuário sem perfil salva catálogo (deve dar erro)' t; select public.save_catalog('{"contests":[]}'::jsonb, 0, 'x');
reset role;
insert into auth.users (id, email, raw_user_meta_data) values
 ('00000000-0000-0000-0000-00000000000c','c@x.com','{"name":"Aluno C","phone":"+5585999990003","accepted_terms":true}');
set role authenticated; select set_config('request.jwt.claim.sub','00000000-0000-0000-0000-00000000000c',false);
select 'T29 aluno salva catálogo (deve dar erro)' t; select public.save_catalog('{"contests":[]}'::jsonb, 0, 'x');
select 'T30 aluno grava direto (deve dar erro)' t; update public.catalog_docs set data='{}';
select 'T31 aluno lê histórico (0)' t, count(*) from public.catalog_history;
reset role;
set role authenticated; select set_config('request.jwt.claim.sub','00000000-0000-0000-0000-00000000000a',false);
select 'T32 admin salva catálogo (versão 1)' t, public.save_catalog('{"contests":[{"id":"X"}]}'::jsonb, 0, 'primeiro');
select 'T33 admin salva com versão velha (deve dar erro)' t; select public.save_catalog('{"contests":[]}'::jsonb, 0, 'conflito');
select 'T34 admin salva versão 2' t, public.save_catalog('{"contests":[]}'::jsonb, 1, 'segundo');
select 'T35 catálogo não-objeto (deve dar erro)' t; select public.save_catalog('[1,2]'::jsonb, 2, 'lista');
select 'T36 admin lê histórico (2)' t, count(*) from public.catalog_history;
select 'T37 admin apaga histórico (deve dar erro)' t; delete from public.catalog_history;
reset role;
set role authenticated; select set_config('request.jwt.claim.sub','00000000-0000-0000-0000-00000000000c',false);
select 'T38 aluno lê catálogo atual (versão 2)' t, version, data from public.catalog_docs;
reset role;
select 'T39 auditoria do catálogo (2)' t, count(*) from public.audit_log where action = 'alterou o catálogo';

-- ===== convite pelo painel (0003)
insert into auth.users (id, email, raw_user_meta_data) values ('00000000-0000-0000-0000-0000000000d1','convidado@x.com','{}');
select 'T40 convidado nasce sem nome' t, name, phone, accepted_terms_at is null as sem_aceite from public.profiles where email='convidado@x.com';
update auth.users set raw_user_meta_data = '{"name":"Convidado","phone":"+5581999990009","accepted_terms":true,"role":"owner"}' where email='convidado@x.com';
select 'T41 cadastro pelo app completa o perfil (Convidado, telefone, aceite, student)' t, name, phone, accepted_terms_at is not null as aceite, role from public.profiles where email='convidado@x.com';
update auth.users set raw_user_meta_data = '{"name":"Outro","phone":"123"}' where email='convidado@x.com';
select 'T42 não sobrescreve o que já existe (Convidado)' t, name, phone from public.profiles where email='convidado@x.com';

-- ===== classificação dos alunos (0004)
select 'T43 convidado nasce sem classificação (none)' t, plan from public.profiles where email='convidado@x.com';
set role authenticated; select set_config('request.jwt.claim.sub',(select id::text from public.profiles where email='convidado@x.com'),false);
select 'T44 aluno se classifica beta (deve dar erro)' t; select public.set_plan((select id from public.profiles where email='convidado@x.com'),'beta','');
select 'T45 aluno muda plano direto (deve dar erro)' t; update public.profiles set plan='beta' where email='convidado@x.com';
select 'T46 aluno sem classificação tem acesso? (false)' t, public.has_access();
reset role;
set role authenticated; select set_config('request.jwt.claim.sub','00000000-0000-0000-0000-00000000000a',false);
select 'T47 admin classifica (deve dar erro: só o dono)' t; select public.set_plan((select id from public.profiles where email='convidado@x.com'),'beta','');
reset role;
set role authenticated; select set_config('request.jwt.claim.sub','00000000-0000-0000-0000-000000000001',false);
select 'T48 dono classifica como Testador Beta' t; select public.set_plan((select id from public.profiles where email='convidado@x.com'),'beta','grupo de agosto');
select 'T49 dono define assinante mensal (deve dar erro)' t; select public.set_plan((select id from public.profiles where email='convidado@x.com'),'monthly','');
select 'T50 dono classifica a si mesmo (deve dar erro)' t; select public.set_plan('00000000-0000-0000-0000-000000000001','tester','');
select 'T51 classificação desconhecida (deve dar erro)' t; select public.set_plan((select id from public.profiles where email='convidado@x.com'),'vip','');
select 'T52 registro (beta, grupo de agosto, manual)' t, plan, plan_note, plan_source from public.profiles where email='convidado@x.com';
reset role;
set role authenticated; select set_config('request.jwt.claim.sub',(select id::text from public.profiles where email='convidado@x.com'),false);
select 'T53 beta tem acesso (true)' t, public.has_access();
reset role;
update public.profiles set plan='annual', plan_source='pagamento', plan_expires_at=now() + interval '300 days' where email='convidado@x.com';
set role authenticated; select set_config('request.jwt.claim.sub','00000000-0000-0000-0000-000000000001',false);
select 'T54 dono rebaixa assinatura ativa (deve dar erro)' t; select public.set_plan((select id from public.profiles where email='convidado@x.com'),'tester','');
select 'T55 auditoria da classificação' t, action, detail from public.audit_log_view where action = 'alterou classificação';
reset role;
