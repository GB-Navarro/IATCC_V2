---
aliases: ["Digital Accrual"]
composta_de: []
variante_de: ["[[ACCR]]"]
flexivel: []
payoff: acumulativo
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# Digital Accrual (DACCR)

![[Digital Accrual (DACCR)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| DACCR | call | K1 | T1 | 1 | + | — |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | pagamento que acumula com os fixings e só é pago se a opção estiver no dinheiro no vencimento; a tabela mostra a call | [ovml] |
| Strikes | um strike, que define se a opção termina no dinheiro | [ovml] |
| Payoff | acumulativo, com condição digital no vencimento | [ovml] |
| Variante de | ACCR, com a condição de estar no dinheiro no vencimento | [inferência: comparação dos textos da Bloomberg do ACCR e do DACCR] |

## Notas

- Fonte única para a definição: OVML. O Wystup define o corridor, que corresponde só à parte de acumulação, sem a condição no vencimento [wystup-2006, p. 101].
