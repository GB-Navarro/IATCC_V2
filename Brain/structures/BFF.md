---
aliases: ["Boosted Fade Forward"]
composta_de: []
variante_de: []
flexivel: []
payoff: acumulativo
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# Boosted Fade Forward (BFF)

![[Boosted Fade Forward (BFF)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| BFF | — | K1 | T1 | 1 | + | — |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | forward em que o notional acumula a cada dia com fixing acima ou abaixo da taxa de fade (a barreira) | [ovml] |
| Composição | um valor alavancado é vendido num strike fora do dinheiro para melhorar a taxa | [ovml] |
| Payoff | acumulativo | [ovml] |

## Notas

- Fonte única: OVML [ovml].
- É parecido com o fade-in forward e com o boosted spot/forward do Wystup [wystup-2006, pp. 142, 165].
