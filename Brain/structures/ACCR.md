---
aliases: ["Accrual", "Corridor"]
composta_de: []
variante_de: []
flexivel: []
payoff: acumulativo
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# Accrual (ACCR)

![[Accrual (ACCR)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| ACCR | — | — | T1 | 1 | + | — |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | pagamento em dinheiro que cresce a cada fixing dentro do intervalo | [ovml]; [wystup-2006, p. 101] |
| Notional | cada fixing dentro do intervalo acrescenta o pagamento máximo dividido pelo número de fixings | [ovml]; [wystup-2006, p. 101] |
| Payoff | acumulativo | [ovml] |
| Sinônimo | corridor | [wystup-2006, p. 101] |

## Restrições

- Na versão europeia contam todos os fixings dentro do intervalo; na americana, a acumulação para quando o spot sai do intervalo [wystup-2006, p. 102].
