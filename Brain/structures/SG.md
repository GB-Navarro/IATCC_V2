---
aliases: ["Seagull"]
composta_de: ["[[EU]]", "[[SN]]"]
variante_de: []
flexivel: [notional]
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# Seagull (SG)

![[Seagull (SG)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| EU | put | K1 | T1 | 1 | - | OTM |
| EU | call | K2 | T1 | 1 | + | ATM |
| EU | call | K3 | T1 | 1 | - | OTM |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | compra de uma call; venda de uma call e de uma put | [ovml]; [wystup-2006, p. 38] |
| Strikes | três diferentes: put abaixo da call comprada, call vendida acima | [wystup-2006, p. 39, exemplo] |
| Vencimento | o mesmo nas três pernas | [ovml] |
| Notional | igual nas três pernas | [ovml]; [wystup-2006, p. 39, exemplo] |
| Moneyness | call comprada ATM | [ovml] |
| Moneyness | put e call vendidas OTM (formam um strangle) | [ovml]; [wystup-2006, p. 35] |
| Instrumento | opções europeias | [wystup-2006, pp. 29, 39] |
| Flexível | notional: igual é o usual, não uma exigência | [ovml] |
| Composta de | EU (a opção ATM comprada) e SN (o strangle vendido) | [ovml] |

## Restrições

- Costuma ser montado a custo zero [wystup-2006, p. 38]; [ovml].
