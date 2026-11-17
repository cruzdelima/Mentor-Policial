# Assinaturas — plano técnico

Como cobrar assinatura sem enfraquecer a segurança. Nada disto está ativo; o banco já tem as colunas `plan` e `plan_expires_at`, que **o app só lê**.

## Fluxo recomendado (pagamento fora do app)

```
Aluno clica "Assinar" no app
   └─> abre no navegador a página de pagamento do gateway (Pix Automático, cartão, boleto)
          └─> gateway confirma o pagamento
                 └─> webhook (HTTPS) para uma Edge Function do Supabase
                        ├─ confere a assinatura digital do webhook
                        ├─ atualiza profiles.plan / plan_expires_at (com a chave secreta, só no servidor)
                        └─ grava em audit_log
App (ao abrir ou a cada 6 h) lê o próprio perfil › libera os recursos do plano
```

- **Nenhum dado de cartão passa pelo app nem pelo nosso banco.** O gateway é que cuida disso (e da certificação PCI).
- A chave secreta do gateway e a do Supabase ficam só nas *Secrets* da Edge Function.
- Cancelamento e reembolso: pelo painel do gateway; o webhook de cancelamento rebaixa o plano.

## O que fica pago e como proteger

| Hoje | Problema | Para cobrar |
|---|---|---|
| Os materiais vêm **dentro** do instalador | Qualquer pessoa pode extrair os arquivos do instalador; não dá para restringir | Materiais pagos ficam no **Supabase Storage** (bucket privado). O app baixa com URL assinada de curta duração, e o RLS só libera para `plan` ativo |
| O cronograma é calculado no computador | Não precisa de proteção forte | Pode continuar gratuito (atrai alunos) |

Sugestão de produto: **cronograma, diário e edital gratuitos**; **materiais aprofundados, resumos, questões comentadas e simulados** na assinatura.

## Regras no app

- Assinatura vencida: os recursos pagos ficam bloqueados, mas o aluno **nunca perde** o diário e o cronograma.
- Sem internet: vale o último plano conhecido por até **7 dias** (carência), depois pede conexão.
- Mostrar sempre preço, renovação automática, como cancelar e o direito de arrependimento de 7 dias (CDC, art. 49) antes do pagamento.

## Trabalho estimado

1. Conta no gateway + página de checkout com plano mensal e anual.
2. Migração `0002_assinaturas.sql`: tabela `payments` (RLS), bucket privado `materiais-pagos` e políticas.
3. Edge Function `webhook-pagamento` (validação de assinatura, idempotência por id do evento).
4. App: tela "Assinatura", download de materiais pagos, carência offline.
5. Termos de Uso com cláusulas de cobrança, revisados por advogado; emissão de nota fiscal (MEI/ME).
