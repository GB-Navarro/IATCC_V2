---
aliases: ["Knockin"]
composta_de: []
variante_de: []
flexivel: []
barreira: ki
barreiras: 1
payoff: vanilla
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# Knockin (KI)

![[Knockin (KI)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| KI | call | K1 | T1 | 1 | + | — |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | opção vanilla que só passa a existir se o spot tocar a barreira; a tabela mostra a call | [ovml]; [hull-2015, p. 604]; [wystup-2006, p. 42] |
| Barreira | ki, uma barreira | [ovml]; [hull-2015, p. 604] |
| Payoff | vanilla, se a barreira for tocada | [ovml] |

## Restrições

- Knock-out mais knock-in com os mesmos parâmetros equivalem à vanilla [wystup-2006, p. 42].
- Barreira regular fica fora do dinheiro; reverse, dentro do dinheiro [wystup-2006, p. 42].
- Por tradição, as barreiras são americanas [wystup-2006, p. 43].
- O prêmio é menor que o da vanilla equivalente [ovml].
