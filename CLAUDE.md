# IATCC

Antes de propor mudanças, leia `docs/README.md` (estado e próximos passos) e `docs/decisoes.md`. As regras das notas ficam só em `Brain/_schema.md`.

## Regras fixas

- Nunca editar `Brain/structures/bloomberg_description/`.
- Não editar à mão os campos gerados pelo script (`tags`, `instrumentos`, `ambigua_com`).
- Arquivos do Brain e docs: só o essencial, em português. Seções vazias são omitidas.
- Antes de passos grandes, propor plano e esperar aprovação.

## Atualização dos docs

Após toda mudança relevante, atualizar os docs na mesma resposta:

| O que mudou | O que atualizar |
|---|---|
| decisão nova ou revista | `docs/decisoes.md`: próximo número, status, motivo |
| qualquer mudança relevante | `docs/evolucao.md`: entrada no topo, sob a data |
| estado de etapa, pastas ou próximos passos | `docs/README.md` |

- **Relevante:** `_schema.md` e `_template.md`, scripts, hooks, estrutura de pastas, decisões do usuário, etapas concluídas (ex.: "pernas de CP, RR e SN preenchidas").
- **Não relevante:** typo, formatação, ajuste pontual de um campo.
- Se a mudança veio do usuário (ex.: feita no Obsidian) e implica decisão, perguntar o motivo em vez de supor.

O hook `scripts/hooks/checar_docs.py` cobra isso ao fim de cada resposta e no início de cada sessão.
