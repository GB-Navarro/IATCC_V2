---
aliases: ["KIKO Forward"]
composta_de: ["[[KO]]", "[[KOKI]]"]
variante_de: []
flexivel: []
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# KIKO Forward (KKF)

![[KIKO Forward (KKF)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| KO | call | K1 | T1 | 1 | + | — |
| KOKI | put | K1 | T1 | 1 | - | — |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | compra de uma knock-out e venda de uma KIKO | [ovml] |
| Composição | KO call comprada e KIKO put vendida | [inferência: comprar uma opção e vender outra no mesmo strike, para ficar "hedged at the strike" como num forward, exige call comprada e put vendida, como no forward sintético, wystup-2006, p. 140] |
| Strikes | o mesmo nas duas pernas | [inferência: o texto da Bloomberg diz que o cliente fica "hedged at the strike"] |
| Composta de | KO e KIKO | [ovml] |
| Composta de | a KIKO é do tipo KOKI: se o KO é tocado primeiro, o hedge se perde mesmo que o KI venha depois (exclui o tipo 2); se o KI vem primeiro e o KO depois, o hedge também se perde (exclui o tipo 3) | [inferência: texto da Bloomberg do KKF + wystup-2006, p. 115] |

## Restrições

- Pode ser montado a custo zero [ovml].

## Notas

- Fonte única para a definição: OVML. As fontes tratam só componentes ou estruturas parecidas [inferência: páginas indicadas para esta estrutura na cobertura de `fontes/README.md`].
