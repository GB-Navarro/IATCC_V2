---
aliases: ["Fader"]
composta_de: []
variante_de: []
flexivel: []
payoff: acumulativo
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# Fader (FA)

![[Fader (FA)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| FA | call | K1 | T1 | 1 | + | — |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | vanilla cujo notional é definido no vencimento pelos fixings dentro (ou fora) de um intervalo; a tabela mostra a call | [ovml]; [wystup-2006, pp. 103–104] |
| Composição | o fade-in com fixings dentro do intervalo | [haug-2007, p. 122] |
| Notional | proporcional ao número de fixings que cumprem a condição | [ovml]; [wystup-2006, pp. 103–104] |
| Payoff | acumulativo | [ovml] |

## Restrições

- No fade-in o notional começa em zero e cresce; no fade-out começa cheio e diminui [ovml]; [wystup-2006, p. 103].
