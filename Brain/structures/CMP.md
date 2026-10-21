---
aliases: ["Compound"]
composta_de: []
variante_de: []
flexivel: []
payoff: composto
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# Compound (CMP)

![[Compound (CMP)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| CMP | call | K1 | T1 | 1 | + | — |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | opção sobre uma vanilla: a compound call dá o direito de comprar a vanilla, a compound put o de vender; a tabela mostra a call | [ovml]; [wystup-2006, p. 58]; [hull-2015, p. 602] |
| Strikes | dois: o da compound (o prêmio a pagar pela vanilla) e o da vanilla; a tabela mostra só K1 | [ovml]; [hull-2015, p. 602] |
| Vencimento | dois: o da compound e o da vanilla; a tabela mostra só T1 | [ovml]; [hull-2015, p. 602] |
| Payoff | composto | [ovml]; [haug-2007, p. 132] |

## Restrições

- Permite pagar o prêmio da vanilla em parcelas [wystup-2006, p. 58].
