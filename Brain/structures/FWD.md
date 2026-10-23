---
aliases: ["FX Forward"]
composta_de: []
variante_de: []
flexivel: []
payoff: linear
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# FX Forward (FWD)

![[FX Forward (FWD)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| FWD | — | K1 | T1 | 1 | + | — |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | contrato de troca de moedas na data de entrega especificada | [ovml]; [wystup-2006, p. 139] |
| Strikes | a taxa do contrato (K1), o preço de entrega | [ovml]; [hull-2015, p. 7] |
| Vencimento | data de entrega futura | [hull-2015, p. 6] |
| Payoff | linear: ST − K na posição comprada, K − ST na vendida | [hull-2015, p. 7]; [wystup-2006, p. 139] |
| Payoff | o OVML descreve o resultado do comprador da moeda do notional | [inferência: o texto da Bloomberg descreve lucro quando a taxa do contrato é menor que a taxa do dia; esse é o payoff ST − K da posição comprada, hull-2015, p. 7] |

## Restrições

- Custo zero na entrada quando a taxa do contrato é a forward de mercado [hull-2015, pp. 112–113]; [wystup-2006, p. 140]. Com outra taxa, há prêmio [wystup-2006, p. 140].
