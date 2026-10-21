# IATCC — identificação de estruturas de opções

Agrupa as negociações de opções de FX disseminadas pelo DTCC e identifica que estruturas (Risk Reversal, Butterfly, Seagull…) cada grupo forma. Um agente de IA faz isso consultando uma base de conhecimento em Markdown: `Brain/`, um vault do Obsidian.

## Como funciona

```
DTCC (registros + insumos calculados)       Brain/ (base de conhecimento)
            │                                         │
  1. agrupar por plataforma              uma nota por estrutura:
     e timestamp (segundos)              pernas, facetas (tags), relações (wikilinks)
            │                                         │
  2. assinatura do grupo  ───────►  3. matching (Python)  ───────►  candidatas
                                                                        │
                                               4. agente (LLM): desempata, decompõe
                                                  grupos grandes e explica
```

- A assinatura do grupo e as tags das notas usam o mesmo vocabulário, definido em [`Brain/_schema.md`](../Brain/_schema.md).
- O matching é determinístico. O LLM entra só depois, sobre as candidatas.
- O dado público do DTCC não traz o lado (compra/venda). Por isso o agente devolve hipóteses ranqueadas, e as estruturas que só se distinguem pelo lado ficam marcadas em `ambigua_com`.

| Etapa | Estado |
|---|---|
| Base: schema, template e notas | 65 notas preenchidas, aguardando validação (`validacao/README.md`) |
| Gerador e validador de tags | a fazer |
| Agrupamento DTCC | a fazer |
| Matching | a fazer |
| Agente | a fazer |
| Avaliação | a fazer |

## Pastas

| Caminho | Conteúdo |
|---|---|
| `Brain/_schema.md` | regras das notas: campos, pernas, facetas, relações, matching, validação |
| `Brain/_template.md` | modelo de nota (excluir do grafo no Obsidian) |
| `Brain/structures/<COD>.md` | nota canônica de cada estrutura |
| `Brain/structures/bloomberg_description/` | texto original do OVML, nunca editado |
| `Brain/structures/.bloomberg_hashes.json` | hashes dos textos originais, para a validação |
| `scripts/` | código, fora do vault |
| `scripts/hooks/checar_docs.py` | detecta mudanças não registradas nos docs |
| `scripts/checklist_citacoes.py` | gera o checklist de validação de um lote |
| `validacao/` | checklists de validação das citações, um por lote |
| `docs/` | esta documentação |
| `fontes/` | PDFs das fontes (só local) e índice com chaves, edições e cobertura por estrutura |
| `CLAUDE.md` | regras do projeto e critérios de atualização dos docs, lidos pelo Claude Code em toda sessão |
| `.claude/settings.json` | hooks `Stop` e `SessionStart`, que rodam o `checar_docs.py` |

## Como trabalhar na base

1. Na nota, edite só os campos humanos e as seções do corpo, conforme o `_schema.md`.
2. Nunca edite `bloomberg_description/`. Correções e divergências vão na seção **Notas** da nota canônica.
3. Ao adicionar um texto da Bloomberg, rode `python scripts/gerar_notas.py`. O script só cria notas novas, nunca sobrescreve, e avisa se algum texto original mudou.
4. Registre toda decisão nova em [`decisoes.md`](decisoes.md) e toda mudança em [`evolucao.md`](evolucao.md). Ao fim de cada resposta e no início de cada sessão, o hook avisa o Claude se algo mudou sem registro, inclusive mudanças feitas por você no Obsidian.

## Próximos passos

0. Fontes completas ([`fontes/README.md`](../fontes/README.md)).
1. Validar os cinco lotes de uma vez (`validacao/README.md`, 472 citações) e corrigir o que for marcado com ❌.
2. Escrever o gerador e validador de tags (passo 4 do plano).
3. Agrupamento DTCC, matching, agente e avaliação.
4. A decidir depois: fontes como notas do Brain (proposta D26).

### Pendências conhecidas no texto da Bloomberg

Todas foram registradas nas **Notas** ou **Restrições** das estruturas afetadas: DKI, KIKOSQ, RF, EC, AVG, DISEQ, FX, FWD e FE.
