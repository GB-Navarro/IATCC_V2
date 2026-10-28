---
aliases: ["Risk Reversal (Collar)"]
composta_de: []
variante_de: []
flexivel: []
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# Risk Reversal (Collar) (RR)

![[Risk Reversal (Collar) (RR)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| EU | put | K1 | T1 | 1 | - | OTM |
| EU | call | K2 | T1 | 1 | + | OTM |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | compra de call, venda de put | [ovml]; [wystup-2006, p. 31]; [hull-2015, p. 371] |
| Strikes | diferentes; put abaixo da call | [ovml]; [hull-2015, pp. 370–371] |
| Vencimento | o mesmo nas duas pernas | [ovml] |
| Notional | igual nas duas pernas | [ovml]; [wystup-2006, p. 32, exemplo]; [hull-2015, p. 370, exemplo] |
| Moneyness | as duas OTM | [ovml] |
| Instrumento | opções europeias | [hull-2015, p. 370] |
| Sinônimo | collar | [ovml]; [wystup-2006, p. 31] |

## Restrições

- Costuma ser montado a custo zero: o prêmio da put vendida paga o da call comprada [wystup-2006, p. 31]; [hull-2015, p. 371].
- Em FX, o RR é cotado como a diferença entre a volatilidade da call e a da put com o mesmo delta em módulo; 0,25 é o caso usado como exemplo [reiswich-wystup-2009, pp. 12–13]. O mercado cota o delta 0,25, e outros deltas, como 0,10 e 0,35, também são cotados [wystup-2006, p. 22].

## Notas

- O nome Bloomberg desta estrutura é "Risk Reversal (Collar)" [ovml]. A versão com a posição protegida (fence) é outra nota, [[COL]] [natenberg-1994, p. 264].
- O Hull chama esta estrutura de *range forward*: "This is a long position in a range forward contract and the payoff is shown in Figure 17.1b." [hull-2015, p. 371]. O RF do OVML é outra estrutura ([[RF]]): corresponde ao range forward do Wystup, um forward sintético mais um double-no-touch [wystup-2006, pp. 151–152]; [inferência: texto da Bloomberg do RF].
