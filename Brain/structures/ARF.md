---
aliases: ["Average Rate Forward"]
composta_de: []
variante_de: []
flexivel: []
payoff: media
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# Average Rate Forward (ARF)

![[Average Rate Forward (ARF)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| ARF | — | K1 | T1 | 1 | + | — |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | forward cujo payoff é a diferença entre o strike e a média do spot num período | [ovml] |
| Payoff | media | [ovml] |

## Restrições

- Liquidado em moeda estrangeira, usa o inverso da média do spot [ovml], que é a média harmônica da taxa inversa 1/S [wystup-2006, p. 131].
- Média geométrica ou liquidação em moeda estrangeira exigem volatilidade no apreçamento [ovml].
