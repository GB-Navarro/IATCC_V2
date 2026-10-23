---
aliases: ["Strangle", "Bottom Vertical Combination"]
composta_de: []
variante_de: []
flexivel: []
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# Strangle (SN)

![[Strangle (SN)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| EU | put | K1 | T1 | 1 | + | OTM |
| EU | call | K2 | T1 | 1 | + | OTM |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | compra de put e de call | [ovml]; [hull-2015, p. 269]; [wystup-2006, p. 35] |
| Strikes | diferentes | [ovml]; [hull-2015, p. 269] |
| Strikes | call acima da put | [hull-2015, p. 269] |
| Vencimento | o mesmo nas duas pernas | [ovml]; [hull-2015, p. 269] |
| Notional | igual nas duas pernas | [wystup-2006, p. 36, exemplo] |
| Moneyness | as duas OTM | [wystup-2006, p. 35] |
| Instrumento | opções europeias | [hull-2015, p. 269] |
| Sinônimo | bottom vertical combination | [hull-2015, p. 269] |

## Restrições

- O strangle de referência do mercado de FX (market strangle) usa call e put com o mesmo delta em módulo; 0,25 é o caso usado como exemplo [reiswich-wystup-2009, pp. 12, 15]. O mercado cota o delta 0,25, e outros deltas, como 0,10 e 0,35, também são cotados [wystup-2006, p. 22].
