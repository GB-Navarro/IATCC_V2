---
aliases: ["Average", "Asian Option"]
composta_de: []
variante_de: []
flexivel: []
payoff: media
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# Average (AVG)

![[Average (AVG)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| AVG | call | K1 | T1 | 1 | + | — |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | opção cujo payoff depende da média do spot: average rate (média contra o strike) ou average strike (a média é o strike); a tabela mostra a call | [ovml]; [hull-2015, pp. 609, 611]; [wystup-2006, p. 69] |
| Payoff | media | [ovml] |
| Sinônimo | opção asiática | [hull-2015, p. 609]; [wystup-2006, p. 69] |

## Restrições

- A média pode ser geométrica, aritmética ou harmônica [wystup-2006, p. 69].

## Notas

- A descrição da Bloomberg reúne dois produtos, average rate e average strike [ovml]; o Hull os trata como tipos distintos de opção asiática [hull-2015, p. 611].
