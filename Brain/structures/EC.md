---
aliases: ["Enhanced Collar"]
composta_de: ["[[EU]]", "[[KI]]"]
variante_de: ["[[RR]]"]
flexivel: [strike]
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# Enhanced Collar (EC)

![[Enhanced Collar (EC)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| KI | put | K1 | T1 | 1 | - | — |
| EU | call | K2 | T1 | 1 | + | — |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | compra de call vanilla e venda de put knock-in com barreira dentro do dinheiro | [ovml] |
| Barreira | reverse knock-in: barreira dentro do dinheiro | [ovml]; [wystup-2006, p. 42] |
| Strikes | a Bloomberg não fixa a relação entre os strikes | [ovml] |
| Flexível | strike, pela mesma razão | [ovml] |
| Vencimento | o mesmo nas duas pernas | [inferência: alternativa ao RR, que tem um só vencimento; texto da Bloomberg] |
| Notional | igual nas duas pernas | [inferência: idem] |
| Composta de | EU e KI | [ovml] |
| Variante de | RR, numa versão de menor risco | [ovml] |

## Notas

- O "Knock-In put with a barrier that is in-the-money" da Bloomberg [ovml] é um reverse knock-in, o mesmo termo usado no FE e no BFW: "regular barriers are out of the money, reverse barriers are in the money" [wystup-2006, p. 42].
