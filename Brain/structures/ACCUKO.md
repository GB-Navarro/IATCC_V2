---
aliases: ["Accumulator KO"]
composta_de: []
variante_de: ["[[ACCU]]"]
flexivel: []
barreira: ko
barreiras: 1
payoff: acumulativo
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# Accumulator KO (ACCUKO)

![[Accumulator KO (ACCUKO)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| ACCUKO | — | K1 | T1 | 1 | + | — |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | accumulator cujos fixings restantes são cancelados se o spot tocar uma barreira knock-out americana; o acumulado até ali vale | [ovml] |
| Barreira | ko, uma barreira, contínua em FX | [ovml]; [wystup-2006, p. 157] |
| Payoff | acumulativo | [ovml] |
| Variante de | ACCU, com knock-out | [ovml] |

## Restrições

- O fixing do dia conta para o acumulado se ocorrer antes do knock-out [wystup-2006, p. 157].
