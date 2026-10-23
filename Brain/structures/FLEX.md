---
aliases: ["Flexi Forward", "Time Option"]
composta_de: []
variante_de: []
flexivel: []
payoff: linear
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# Flexi Forward (FLEX)

![[Flexi Forward (FLEX)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| FLEX | — | K1 | T1 | 1 | + | — |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | forward em que o cliente escolhe a data de entrega dentro de um período | [ovml]; [wystup-2006, p. 166] |
| Payoff | linear | [inferência: é um forward, hull-2015, p. 7] |
| Sinônimo | time option | [ovml]; [wystup-2006, p. 166] |
| Sinônimo | forward de estilo americano | [wystup-2006, p. 166] |

## Notas

- A Bloomberg fala de uma única data de entrega [ovml]. O Wystup admite exercer partes do montante em datas diferentes: "The holder can choose times in this period to exercise parts of the total amount, where he or she shouts, which is why this type of contract is also called a shout forward." [wystup-2006, p. 167]
