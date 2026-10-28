---
aliases: ["Double KO"]
composta_de: []
variante_de: ["[[KO]]"]
flexivel: []
barreira: ko
barreiras: 2
payoff: vanilla
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# Double KO (DKO)

![[Double KO (DKO)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| DKO | call | K1 | T1 | 1 | + | — |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | opção vanilla que deixa de existir se o spot tocar qualquer uma de duas barreiras; a tabela mostra a call | [ovml]; [haug-2007, p. 156] |
| Barreira | ko, duas barreiras (inferior e superior) | [ovml]; [haug-2007, p. 156] |
| Payoff | vanilla, se nenhuma barreira for tocada | [ovml]; [haug-2007, p. 156] |
| Variante de | KO, com duas barreiras | [inferência: comparação dos textos da Bloomberg do KO e do DKO]; [wystup-2006, p. 40] |
