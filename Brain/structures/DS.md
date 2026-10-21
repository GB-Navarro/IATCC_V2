---
aliases: ["Diagonal Spread"]
composta_de: []
variante_de: ["[[CS]]"]
flexivel: [notional]
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# Diagonal Spread (DS)

![[Diagonal Spread (DS)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| EU | call | K1 | T1 | 1 | - | — |
| EU | call | K2 | T2 | 1 | + | — |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | uma opção comprada e outra vendida, do mesmo tipo | [ovml]; [hull-2015, p. 266] |
| Composição | vende a de vencimento curto e compra a de vencimento longo | [inferência: segue o calendar spread, hull-2015, p. 265; natenberg-1994, pp. 148, 157] |
| Strikes | diferentes | [hull-2015, p. 266]; [natenberg-1994, p. 157] |
| Vencimento | diferentes | [hull-2015, p. 266] |
| Notional | igual no caso mais comum (uma opção de cada lado) | [natenberg-1994, p. 157] |
| Instrumento | opções europeias | [hull-2015, pp. 265–266] |
| Flexível | notional: pode ter razão diferente de 1:1 | [natenberg-1994, p. 157] |
| Variante de | CS, com strikes diferentes | [natenberg-1994, p. 157] |

## Restrições

- A combinação entre strike e vencimento é livre: K1 pode estar no vencimento curto ou no longo [inferência: hull-2015, p. 266 não fixa a ordem].

## Notas

- A Bloomberg aceita "strikes and/or maturities" diferentes [ovml]. Foi adotado o Hull: "In a diagonal spread both the expiration date and the strike price of the calls are different." [hull-2015, p. 266]
