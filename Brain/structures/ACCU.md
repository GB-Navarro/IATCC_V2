---
aliases: ["Accumulator", "Accumulative Forward"]
composta_de: ["[[FA]]"]
variante_de: []
flexivel: []
payoff: acumulativo
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# Accumulator (ACCU)

![[Accumulator (ACCU)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| ACCU | — | K1 | T1 | 1 | + | — |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | forward cujo valor de face é definido pelo spot em vários fixings; cresce a cada fixing que cumpre a condição | [ovml]; [wystup-2006, p. 156] |
| Notional | o exibido é o máximo; cada fixing acrescenta o notional dividido pelo número de fixings | [ovml] |
| Payoff | acumulativo | [ovml] |
| Composta de | faders (fade-in calls e puts), possivelmente com faixas de knock-out | [wystup-2006, p. 157] |
| Sinônimo | accumulative forward | [wystup-2006, p. 156] |

## Restrições

- Costuma ter custo zero e não tem pior caso garantido [wystup-2006, pp. 156–157].
