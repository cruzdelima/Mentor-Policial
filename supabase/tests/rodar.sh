#!/usr/bin/env bash
# Testa as regras de segurança do banco num PostgreSQL local que imita o Supabase.
# Requer PostgreSQL 15+ (psql) rodando localmente com o usuário postgres.
# uso: bash supabase/tests/rodar.sh
set -euo pipefail
cd "$(dirname "$0")"
psql -U postgres -q -f supabase_mock.sql
for f in ../migrations/*.sql; do psql -U postgres -q -d mentor_test -v ON_ERROR_STOP=1 -f "$f"; done
psql -U postgres -d mentor_test -A -t -f tests.sql 2>&1 | grep -v "^$\|^SET$\|^UPDATE\|^INSERT\|^0000\|^RESET"
echo "Confira: cada linha 'deve dar erro' precisa vir seguida de ERROR; as contagens entre parênteses precisam bater."
