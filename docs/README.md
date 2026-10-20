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
| Base: schema, template e notas | em andamento: 65 notas criadas, tabelas de pernas vazias |
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
| `docs/` | esta documentação |

## Como trabalhar na base

1. Na nota, edite só os campos humanos e as seções do corpo, conforme o `_schema.md`.
2. Nunca edite `bloomberg_description/`. Correções e divergências vão na seção **Notas** da nota canônica.
3. Ao adicionar um texto da Bloomberg, rode `python scripts/gerar_notas.py`. O script só cria notas novas, nunca sobrescreve, e avisa se algum texto original mudou.
4. Registre toda decisão nova em [`decisoes.md`](decisoes.md) e toda mudança em [`evolucao.md`](evolucao.md).

## Próximos passos

1. Preencher as notas canônicas, nesta ordem:
   - combinações de vanillas: CP, RR, SD, SN, SDR, PF, CS, DS, SG, BF, BFC, CR;
   - compostas e forwards estruturados;
   - exóticos de 1 perna.
2. Registrar as pendências abaixo na seção **Notas** de cada estrutura.
3. Escrever o gerador e validador de tags (passo 4 do plano).
4. Agrupamento DTCC, matching, agente e avaliação.

### Pendências conhecidas no texto da Bloomberg

| Nota | Problema |
|---|---|
| DKI | A justificativa do prêmio está invertida: duas barreiras dão duas formas de ativar. |
| KIKOSQ | A redação sobre a ordem das barreiras é ambígua. |
| DS, CP, CS | O "and/or" do DS engloba CP e CS, e o CP não exige o mesmo vencimento. |
| BFC | Não cita a razão de notional 1:2:1. |
| CR | Não diz se vencimento e notional são iguais. |
| RF | Na Bloomberg é uma estrutura com barreira; na literatura, "range forward" é o collar (RR). |
| EC | "KI com barreira ITM" é o mesmo que o Reverse KI citado em FE e BFW. |
| AVG | Uma nota descreve dois produtos (average rate e average strike). |
| DISEQ | A descrição não tem conteúdo; falta buscar uma fonte. |
| RR, BF, FWD, FX, FE | O lado ou a perspectiva (comprador/hedger) fica implícito. |
