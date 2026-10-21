---
aliases: ["FX Spot"]
composta_de: []
variante_de: []
flexivel: []
payoff: linear
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# FX Spot (FX)

![[FX Spot (FX)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| FX | — | K1 | T1 | 1 | + | — |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | contrato de troca de moedas na data spot | [ovml]; [hull-2015, p. 6] |
| Strikes | a taxa do contrato (K1) | [ovml] |
| Vencimento | data spot: entrega quase imediata | [ovml]; [hull-2015, p. 6] |
| Payoff | linear: o comprador ganha se a taxa do contrato for menor que a taxa do dia | [ovml] |

## Restrições

- O resultado descrito é o do comprador; o vendedor tem o resultado oposto [ovml]; [inferência: como no forward, hull-2015, p. 7].
