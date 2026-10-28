---
aliases: ["Butterfly (Calls-Puts)"]
composta_de: ["[[CP]]"]
variante_de: ["[[BF]]"]
flexivel: []
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# Butterfly (Calls-Puts) (BFC)

![[Butterfly (Calls-Puts) (BFC)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| EU | call | K1 | T1 | 1 | + | ITM |
| EU | call | K2 | T1 | 2 | - | ATM |
| EU | call | K3 | T1 | 1 | + | OTM |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | compra das calls K1 e K3, venda da call K2; só calls ou só puts | [ovml]; [hull-2015, pp. 262, 264] |
| Composição | duas opções vendidas em K2 | [hull-2015, p. 264] |
| Strikes | três; K2 no meio: K3 − K2 = K2 − K1 | [hull-2015, pp. 264, 270] |
| Vencimento | o mesmo nas três pernas | [hull-2015, p. 265] |
| Notional | 1:2:1 | [hull-2015, p. 264] |
| Moneyness | K1 ITM, K2 ATM, K3 OTM | [ovml] |
| Moneyness | K2 costuma ficar próximo do preço corrente | [hull-2015, p. 264] |
| Instrumento | opções europeias | [hull-2015, pp. 262, 264] |
| Composta de | CP comprado (K1–K2) e CP vendido (K2–K3) | [inferência: hull-2015, pp. 258, 261, 264] |
| Variante de | BF, montado só com calls ou só com puts | [ovml] |

## Notas

- A Bloomberg não cita a razão 1:2:1. O Hull vende duas opções no strike central: "selling two European call options with a strike price K2 that is halfway between K1 and K3" [hull-2015, p. 264].
