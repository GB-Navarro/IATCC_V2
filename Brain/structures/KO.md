---
aliases: ["Knockout"]
composta_de: []
variante_de: []
flexivel: []
barreira: ko
barreiras: 1
payoff: vanilla
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# Knockout (KO)

![[Knockout (KO)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| KO | call | K1 | T1 | 1 | + | — |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | opção vanilla que deixa de existir se o spot tocar a barreira; a tabela mostra a call | [ovml]; [hull-2015, p. 604]; [wystup-2006, p. 40] |
| Barreira | ko, uma barreira | [ovml]; [hull-2015, p. 604] |
| Payoff | vanilla, se a barreira não for tocada | [ovml]; [wystup-2006, p. 40] |

## Restrições

- A barreira pode ser americana (vale o tempo todo) ou europeia (só no vencimento) [wystup-2006, pp. 40, 42]. Por tradição, as barreiras são americanas [wystup-2006, p. 43].
- Barreira regular fica fora do dinheiro; reverse, dentro do dinheiro [wystup-2006, p. 42].
- O prêmio é menor que o da vanilla equivalente [ovml]; [hull-2015, p. 604].
