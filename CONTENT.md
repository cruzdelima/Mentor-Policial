# Formato dos conteúdos

## `index.json` (lista de materiais)

```json
{
  "version": "2026.11.1",
  "materials": [
    {
      "id": "info-malware-01",
      "folder": "informatica_virus",
      "title": "Vírus e outros códigos maliciosos",
      "subtitle": "Informática · Segurança da informação",
      "subjectId": "INFO",
      "topicIds": ["INFO-12"],
      "kind": "resumo",
      "minutes": 50,
      "questions": 10,
      "version": "0.1.0",
      "status": "Em revisão pelo autor"
    }
  ]
}
```

`subjectId` e `topicIds` usam os códigos de `assets/catalog/catalog.json` (ex.: `INFO-12` = Malwares, ataques e golpes).
É assim que o material aparece no assunto certo do Edital e nas missões ("ESTUDAR NO APP").

## `material.json`

```json
{
  "sections": [
    { "id": "teoria", "title": "Teoria", "blocks": [ ... ] },
    { "id": "resumo", "title": "Resumo + mapa mental", "blocks": [ ... ] }
  ],
  "mindmap": { "root": "CÓDIGOS MALICIOSOS", "rootSub": "malware",
               "left":  [ { "label": "Vírus", "items": ["...", "..."] } ],
               "right": [ { "label": "Spyware", "items": ["..."] } ] },
  "quiz": { "style": "CE", "banca": "Estilo Cebraspe", "instructions": "...",
            "questions": [ { "id": "q1", "text": "...", "answer": "C", "comment": "**Certo.** ..." } ] },
  "videos": [ { "title": "Aula 1", "url": "https://..." } ],
  "pdf": "informatica_virus.pdf",
  "sources": ["..."]
}
```

### Blocos

| `t` | Campos | Uso |
|---|---|---|
| `h2`, `h3` | `text` | Títulos |
| `p` | `text` | Parágrafo (aceita `**negrito**`) |
| `bullets` | `items` | Lista |
| `callout` | `style` (`exam`, `key`, `trap`), `title`, `text` | Destaques: o que a banca cobra, ponto-chave, pegadinha |
| `table` | `head`, `rows`, `widths` | Tabela (larguras em fração, somando 1) |
| `note` | `text` | Observação pequena |
| `mindmap` | — | Insere o mapa mental definido em `mindmap` |

`kind` é `aprofundado` (estudo inicial: teoria completa + 20 questões em dois blocos, campo `group` em cada questão) ou `resumo` (revisão: teoria curta, quadro, mapa mental e 10 questões).

O gerador `tool/content/build_content.py` produz o `material.json` e o PDF de cada módulo-fonte e confere gabaritos e quantidade de questões antes de gerar.
