# Schema das estruturas

Contrato entre as notas de `structures/`, o script gerador e o agente.

## Arquivos

- Uma nota por estrutura: `structures/<COD>.md` (ex.: `BF.md`), criada a partir de `_template.md`.
- `structures/bloomberg_description/` é a fonte original: nunca é editada, só embutida.
- Nome completo e sinônimos ficam em `aliases`.
- Seções vazias são omitidas. **Restrições**: só o que a tabela não expressa. **Notas**: só divergências da Bloomberg ou conflitos de nome. **Fontes**: `Autor, *Título*, cap.`

## Frontmatter

| Campo | Preenchido por | Valores |
|---|---|---|
| `aliases` | humano | nome Bloomberg, sinônimos |
| `composta_de` | humano | `[[COD]]` das subestruturas |
| `variante_de` | humano | `[[COD]]` da estrutura-base |
| `flexivel` | humano | `strike`, `vencimento`, `notional` |
| `barreira` | humano | `ki`, `ko`, `kiko` (ausente = sem barreira) |
| `barreiras` | humano | `1`, `2` |
| `payoff` | humano | `vanilla`, `digital`, `toque`, `acumulativo`, `media`, `composto`, `linear` |
| `familia` | humano, só em genéricas | `generica` |
| `tags` | script | ver Facetas |
| `instrumentos` | script | `[[COD]]` da coluna instrumento |
| `ambigua_com` | script | `[[COD]]` |

`barreira`, `barreiras` e `payoff` só existem em notas de 1 perna.

## Pernas

| Coluna | Valores |
|---|---|
| instrumento | código de uma nota existente |
| tipo | `call`, `put`, `—` |
| strike | `K1`, `K2`, …, `—` |
| vencimento | `T1`, `T2`, … |
| notional | inteiro relativo, ou `r` (razão livre ≠ 1) |
| lado | `+` compra, `-` venda |
| moneyness | `ATM`, `OTM`, `ITM`, `—` |

- Mesmo símbolo = mesmo valor. Índices crescentes: `K1 < K2 < …`, `T1 < T2`.
- Uma linha por (instrumento, tipo, strike, vencimento, lado); repetições somam o notional.
- A tabela descreve uma única forma: a versão long da Bloomberg. Variantes implícitas, que não viram notas:
  - **short**: inverter todos os lados;
  - **espelho**: trocar call ↔ put e inverter a ordem dos strikes.
- Nota de 1 perna usa o próprio código como instrumento.
- Genéricas (2L–10L) não têm tabela; o nº de pernas vem do código.

## Facetas

Tags aninhadas do Obsidian, geradas a partir da tabela e de `flexivel`.

| Faceta | Valores | Regra | Aplica-se a |
|---|---|---|---|
| `familia/` | `vanilla`, `vanilla-combo`, `exotico`, `composta`, `nao-opcao`, `generica` | abaixo | todas |
| `pernas/` | `1`–`10` | nº de linhas | todas |
| `tipos/` | `mesmo-tipo`, `call-put` | linhas com call/put; omitida se < 2 | combo, composta |
| `strikes/` | inteiro, `qualquer` | nº de K distintos | combo, composta |
| `expiry/` | `igual`, `diferente`, `qualquer` | 1 T → igual; > 1 → diferente | combo, composta |
| `notional/` | `igual`, `razao`, `qualquer` | todos iguais → igual | combo, composta |
| `barreira/`, `barreiras/`, `payoff/` | como no frontmatter | copiados | 1 perna |

- `qualquer` quando o campo está em `flexivel`.
- `familia/`:
  - `nao-opcao`: só FX, FWD, CASH;
  - `vanilla`: 1 linha, EU ou AM;
  - `exotico`: 1 linha, outro instrumento;
  - `vanilla-combo`: ≥ 2 linhas, só EU/AM;
  - `composta`: ≥ 2 linhas, ao menos uma fora de EU/AM;
  - `generica`: declarada.

## Relações

| Campo | Significado | Origem |
|---|---|---|
| `composta_de` | é formada por essas subestruturas | humano |
| `variante_de` | é variação dessa estrutura (DKO → KO, SD → SN) | humano |
| `instrumentos` | instrumentos usados nas pernas | script |
| `ambigua_com` | tabelas iguais ignorando a coluna lado (a menos de espelho) | script, simétrica |

## Matching (grupo DTCC → estrutura)

1. Somar os registros do grupo com mesmo instrumento, tipo, strike e vencimento.
2. Calcular as facetas do grupo com as regras acima.
3. Candidatas: notas cujas tags casam com as do grupo; `qualquer` casa com tudo.
4. Moneyness e Restrições ranqueiam as candidatas; não filtram.

## Validação

1. Campos do script não são editados à mão.
2. Todo valor de faceta pertence a este vocabulário.
3. Todo wikilink e todo instrumento resolvem para uma nota existente.
4. `ambigua_com` é recíproca.
5. Os arquivos de `bloomberg_description/` mantêm o hash registrado.
