---
aliases: ["Enhanced Collar"]
composta_de: ["[[EU]]", "[[KI]]"]
variante_de: ["[[RR]]"]
flexivel: []
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
| Strikes | diferentes; put abaixo da call, como no RR | [inferência: o texto da Bloomberg descreve uma alternativa ao RR, com "flexibility between the best and worse case rates"; com strikes iguais seria o FE] |
| Vencimento | o mesmo nas duas pernas | [inferência: o texto da Bloomberg descreve uma alternativa ao RR, e o RR tem um só vencimento, ver nota RR] |
| Notional | igual nas duas pernas | [inferência: idem; o RR tem notional igual nas duas pernas, ver nota RR] |
| Composta de | EU e KI | [ovml] |
| Variante de | RR, numa versão de menor risco | [ovml] |

## Notas

- O "Knock-In put option with a barrier that is in-the-money" da Bloomberg [ovml] é um reverse knock-in, o mesmo termo usado no FE e no BFW: "regular barriers are out of the money, reverse barriers are in the money" [wystup-2006, p. 42].
- Fonte única para a definição: OVML. Nenhuma fonte de `fontes/` define esta estrutura [inferência: cobertura por estrutura em `fontes/README.md`].
