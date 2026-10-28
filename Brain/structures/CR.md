---
aliases: ["Condor"]
composta_de: ["[[SN]]"]
variante_de: ["[[BF]]"]
flexivel: []
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# Condor (CR)

![[Condor (CR)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| EU | put | K1 | T1 | 1 | + | — |
| EU | put | K2 | T1 | 1 | - | — |
| EU | call | K3 | T1 | 1 | - | — |
| EU | call | K4 | T1 | 1 | + | — |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | compra de um strangle largo e venda de um strangle mais estreito | [ovml] |
| Strikes | quatro; o intervalo do strangle vendido (K2–K3) é menor que o do comprado (K1–K4) | [ovml] |
| Strikes | as duas opções vendidas ficam entre as duas compradas | [natenberg-1994, p. 158] |
| Strikes | as pontas têm o mesmo espaçamento: K2 − K1 = K4 − K3 | [inferência: o condor vale zero fora dos strikes extremos, natenberg-1994, p. 158] |
| Vencimento | o mesmo nas quatro pernas | [natenberg-1994, p. 158] |
| Notional | igual: uma opção por perna | [natenberg-1994, p. 158] |
| Instrumento | opções europeias | [inferência: convenção do _schema.md, combinações de vanillas usam opções europeias; vanilla = opção europeia, wystup-2006, p. 39] |
| Composta de | SN comprado (K1–K4) e SN vendido (K2–K3) | [ovml] |
| Variante de | BF, com o strike central dividido em dois | [natenberg-1994, p. 158] |

## Notas

- O Natenberg define o condor com um só tipo de opção: "As with a butterfly, all options must be of the same type (all calls or all puts) and expire at the same time." [natenberg-1994, p. 158]. A versão do OVML, com strangles, tem o mesmo resultado, e o "long" coincide [inferência: mesma equivalência do iron butterfly, natenberg-1994, p. 158].
