# Dados do DTCC

Achados sobre os dados públicos de opções de FX, a partir de uma amostra real. Base para as decisões D38 em diante.

## Fonte e formato

- **Arquivo:** relatório cumulativo diário da CFTC no DTCC (PPD): `https://pddata.dtcc.com/ppd/api/report/cumulative/cftc/CFTC_CUMULATIVE_FOREX_<AAAA_MM_DD>.zip`. É um CSV com 110 colunas.
- **Amostra analisada:** 21/10/2026, com 61.562 registros, dos quais 54.355 negócios novos (`Action type = NEWT`, `Event type = TRAD`).
- **Conteúdo:** opções, forwards, NDFs e swaps vêm no mesmo arquivo.
- **Horário de execução:** precisão de segundos (`2026-10-21T20:47:51Z`).

## Como o produto aparece

- `Option Type`, `Option Style` e `Product name` vêm **vazios**.
- O produto está no **`UPI FISN`**, o nome curto do UPI ([`dsb-2024`], aba FISN):

| FISN | Produto UPI | Registros na amostra |
|---|---|---|
| `O Van Call/Put` | Vanilla_Option | 3.467 |
| `O NDO Call/Put` | NDO | 947 |
| `O Bar Call/Put` | Barrier_Option | 189 |
| `O Dig Call/Put` | Digital_Option (digital) | 172 |
| `O DigBar Call/Put` | Digital_Option (digital barrier) | 30 |
| `O Targ Call/Put` | Target_Option | 32 |
| `FX O Nstd` | Option Non_Standard (sem call/put) | 179 |
| `Fwd`, `Fwd NDF`, `FX Fwd Nstd`, `Fwd TARF`, `Fwd VolVar` | produtos de forward | 55.000+ |
| `Swaps`, `Swaps NDS` | swaps | 846 |

**O que não há nos dados:**
- **Barreira:** nenhuma coluna informa nível, tipo (KI ou KO) ou número de barreiras. O template Barrier_Option do UPI também não tem esses atributos.
- **Lado:** nenhuma coluna informa se a perna foi comprada ou vendida.
- **Detalhe das não padronizadas:** o FISN não mostra se uma `FX O Nstd` é asiática, de barreira etc.

**O que há:**
- **Para opções:** strike, vencimento, primeira data de exercício, notional, prêmio, `Package indicator`, plataforma e par de moedas (`UPI Underlier Name`).
- **Notional com teto:** marcado com "+".

## Agrupamento: chave (intervalo de segundos, plataforma, par) — D30

| Janela | Grupos com opção | Isolados | Grupos com 11+ registros |
|---|---|---|---|
| 0 s | 2.220 | 1.204 | 7 |
| 1 s | 2.079 | 957 | 6 |
| 2 s | 2.065 | 921 | 7 |
| 5 s | 2.037 | 858 | 20 |

- **Janela:** de 1 a 2 segundos. Acima disso, negócios sem relação começam a se juntar.
- **Pacotes partidos:** 320 pernas marcadas como pacote ficam isoladas.
  - Em 88 casos, as outras pernas chegam entre 2 e 60 segundos depois, na mesma plataforma e no mesmo par.
  - Em 207 casos, não há nenhuma outra perna de pacote por perto. Provavelmente estão fora deste arquivo: outro repositório ou hedge em spot.
- **Delta hedge:** 324 grupos misturam opções vanilla e forwards. O notional do forward fica em torno de 25% do notional das opções (10% dos casos abaixo de 6%, 90% abaixo de 101%). É o padrão de um delta hedge, não de uma perna de estrutura.

## Padrões das opções vanilla (janela de 1 s, após somar pernas idênticas)

| Padrão | Grupos | Estruturas candidatas |
|---|---|---|
| 1 perna | 809 | EU, AM |
| call + put, mesmo strike e vencimento | 248 | SD, SDR, PF |
| call + put, strikes diferentes | ~75 | RR, SN |
| mesmo tipo, strikes diferentes, mesmo vencimento | ~80 | CP |
| mesmo tipo, vencimentos diferentes | ~30 | CS, DS |

- **Pernas repetidas:** em 68 grupos, a mesma perna veio em mais de um registro.
- **Razões de notional:** vêm com ruído (1,01, 1,02, 1,08), o que exige tolerância.

## Opções exóticas em grupo

| Combinação | Grupos | Estruturas candidatas |
|---|---|---|
| `O Bar` + `O Van` | 9 | FE, EC |
| `O Bar` + `O Bar` | 7 | KOF |
| `O Dig` + `O Dig` | 8 | — |

## Lacunas da base

- **TARF:** os dados têm `Target_Option` (32) e `Fwd TARF`, e a base não tem nenhuma nota para eles.
