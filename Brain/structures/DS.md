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
| Composição | vende a de vencimento curto e compra a de vencimento longo | [hull-2015, p. 272] |
| Strikes | diferentes | [hull-2015, p. 266]; [natenberg-1994, p. 157] |
| Vencimento | diferentes | [hull-2015, p. 266] |
| Notional | igual em muitos casos (uma opção de cada lado) | [natenberg-1994, p. 157] |
| Instrumento | opções europeias | [inferência: convenção do _schema.md, combinações de vanillas usam opções europeias; o Hull apresenta o diagonal como variação do calendar spread de calls europeias, hull-2015, pp. 265–266] |
| Flexível | notional: pode ter razão diferente de 1:1 | [natenberg-1994, p. 157] |
| Variante de | CS, com strikes diferentes | [natenberg-1994, p. 157] |

## Restrições

- A combinação entre strike e vencimento é livre: o strike do vencimento longo pode ser maior ou menor que o do curto [hull-2015, p. 272]. A tabela de pernas mostra só o primeiro caso.

## Notas

- A Bloomberg aceita "strikes and/or maturities" diferentes [ovml]. Foi adotado o Hull: "In a diagonal spread both the expiration date and the strike price of the calls are different." [hull-2015, p. 266]
