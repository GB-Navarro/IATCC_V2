---
aliases: ["Average Strike Forward"]
composta_de: []
variante_de: []
flexivel: []
payoff: media
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# Average Strike Forward (ASF)

![[Average Strike Forward (ASF)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| ASF | — | — | T1 | 1 | + | — |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | forward entre o spot no vencimento e um strike igual à média do spot num período | [ovml] |
| Strikes | não é fixo: é a média do período | [ovml] |
| Payoff | media | [ovml] |

## Restrições

- Forwards com strike flutuante na média harmônica aparecem no Wystup [wystup-2006, p. 132].
- Notional na moeda doméstica ou média geométrica exigem volatilidade no apreçamento [ovml].
