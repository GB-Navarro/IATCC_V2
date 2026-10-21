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
- Em FX, o RR é cotado como a diferença entre a volatilidade da call de delta 0,25 e a da put de delta −0,25 [reiswich-wystup-2009, p. 13].

## Notas

- O Hull chama esta estrutura de *range forward*: "This is a long position in a range forward contract and the payoff is shown in Figure 17.1b." [hull-2015, p. 371]. O RF do OVML é outra estrutura ([[RF]]) [wystup-2006, p. 151].
