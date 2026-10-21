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
| Composição | contrato de troca de moedas numa data futura | [ovml]; [hull-2015, p. 6] |
| Strikes | a taxa do contrato (K1), o preço de entrega | [ovml]; [hull-2015, p. 7] |
| Vencimento | data de entrega futura | [ovml]; [hull-2015, p. 6] |
| Payoff | linear: ST − K na posição comprada, K − ST na vendida | [hull-2015, p. 7] |

## Restrições

- Não custa nada para entrar [hull-2015, p. 7].
- O resultado descrito pela Bloomberg é o do comprador [ovml]; a posição vendida tem o resultado oposto [hull-2015, p. 7].
