---
aliases: ["Straddle"]
composta_de: []
variante_de: ["[[SN]]"]
flexivel: []
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# Straddle (SD)

![[Straddle (SD)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| EU | put | K1 | T1 | 1 | + | ATM |
| EU | call | K1 | T1 | 1 | + | ATM |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | compra de call e de put | [ovml]; [hull-2015, p. 267]; [wystup-2006, p. 33] |
| Strikes | o mesmo nas duas pernas | [ovml]; [hull-2015, p. 267]; [wystup-2006, p. 33] |
| Vencimento | o mesmo nas duas pernas | [ovml]; [hull-2015, p. 267] |
| Notional | igual nas duas pernas | [wystup-2006, p. 35, exemplo] |
| Moneyness | ATM | [wystup-2006, p. 35, exemplo]; [inferência: o texto da Bloomberg do SDR contrasta o straddle com o strike OTM do ratio straddle] |
| Instrumento | opções europeias | [hull-2015, p. 267] |
| Variante de | SN, com os dois strikes iguais | [inferência: hull-2015, pp. 267, 269] |

## Restrições

- Em FX, o ATM padrão para opções curtas é o delta-neutro: o strike em que o straddle não tem exposição ao spot [reiswich-wystup-2009, p. 9].
