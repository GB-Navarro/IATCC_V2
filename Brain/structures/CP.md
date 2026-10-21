---
aliases: ["Call-Put Spread"]
composta_de: []
variante_de: []
flexivel: []
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# Call-Put Spread (CP)

![[Call-Put Spread (CP)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| EU | call | K1 | T1 | 1 | + | — |
| EU | call | K2 | T1 | 1 | - | — |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | compra de uma call e venda de outra call | [ovml]; [hull-2015, p. 258]; [wystup-2006, p. 30] |
| Strikes | diferentes; a call comprada tem o strike mais baixo | [ovml]; [hull-2015, p. 258] |
| Vencimento | o mesmo nas duas pernas | [hull-2015, p. 258] |
| Notional | igual: uma opção de cada lado | [hull-2015, p. 258]; [wystup-2006, p. 31, exemplo] |
| Moneyness | livre: as calls podem estar dentro ou fora do dinheiro | [hull-2015, p. 259] |
| Instrumento | opções europeias | [hull-2015, p. 258] |

## Restrições

- Put spread e as versões bear são a mesma estrutura pelas regras de short e espelho [inferência: hull-2015, pp. 259–261 + regras de short e espelho do _schema.md].

## Notas

- A Bloomberg não exige o mesmo vencimento [ovml]. Foi adotada a definição do Hull: "Both options have the same expiration date." [hull-2015, p. 258]
