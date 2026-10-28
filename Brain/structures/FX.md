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
| Vencimento | data spot | [ovml] |
| Vencimento | entrega quase imediata; por padrão, 2 dias úteis após a negociação | [hull-2015, p. 6]; [wystup-2006, p. 135] |
| Payoff | ganha-se se a taxa do contrato for menor que a taxa do dia | [ovml] |
| Payoff | linear; esse é o resultado do comprador da moeda do notional, e o vendedor tem o oposto | [inferência: spot e forward diferem só na data de entrega, hull-2015, p. 6; no forward, a posição comprada recebe ST − K e a vendida K − ST, hull-2015, p. 7] |

