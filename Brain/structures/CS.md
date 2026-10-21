---
aliases: ["Calendar Spread", "Horizontal Spread", "Time Spread"]
composta_de: []
variante_de: []
flexivel: []
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# Calendar Spread (CS)

![[Calendar Spread (CS)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| EU | call | K1 | T1 | 1 | - | — |
| EU | call | K1 | T2 | 1 | + | — |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | venda da opção de vencimento curto e compra da de vencimento longo, do mesmo tipo | [ovml]; [hull-2015, p. 265]; [natenberg-1994, p. 148] |
| Strikes | o mesmo nas duas pernas | [ovml]; [hull-2015, p. 265]; [natenberg-1994, p. 148] |
| Vencimento | diferentes (T1 < T2) | [ovml]; [hull-2015, p. 265] |
| Notional | igual: uma opção de cada lado | [hull-2015, p. 265]; [natenberg-1994, p. 148] |
| Moneyness | livre: strike próximo do preço corrente na visão neutra, acima na altista, abaixo na baixista | [hull-2015, p. 266]; [ovml] |
| Instrumento | opções europeias | [hull-2015, p. 265] |
| Sinônimo | horizontal spread; time spread | [ovml]; [natenberg-1994, p. 148] |
