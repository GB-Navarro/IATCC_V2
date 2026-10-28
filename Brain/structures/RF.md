---
aliases: ["Range Forward"]
composta_de: ["[[EU]]", "[[DNT]]"]
variante_de: []
flexivel: []
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# Range Forward (RF)

![[Range Forward (RF)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| EU | put | K1 | T1 | 1 | - | — |
| EU | call | K1 | T1 | 1 | + | — |
| DNT | — | — | T1 | r | + | — |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | forward sintético no strike do pior caso mais compra de um double-no-touch | [wystup-2006, pp. 152, 324] |
| Composição | forward sintético: compra de call e venda de put, mesmo strike e mesmo notional | [wystup-2006, p. 140] |
| Strikes | o mesmo nas duas opções: o pior caso | [wystup-2006, p. 152] |
| Vencimento | o mesmo em todas as pernas | [inferência: uma única data de vencimento, com o intervalo verificado "at expiry", wystup-2006, p. 151] |
| Notional | igual nas duas opções | [wystup-2006, p. 140] |
| Notional | o pagamento do DNT (r) cobre a diferença entre pior e melhor caso | [inferência: wystup-2006, p. 152] |
| Barreira | a tabela representa a versão com barreiras americanas (DNT); na versão básica, o intervalo só é verificado no vencimento, o que equivale a um DNT europeu | [wystup-2006, pp. 151–152, 324] |
| Composta de | DNT, mais um forward sintético | [wystup-2006, p. 152] |

## Restrições

- É montado a custo zero, como um forward outright [wystup-2006, p. 151].

## Notas

- O Hull usa *range forward* para o par de opções (RR do OVML): "This is a long position in a range forward contract and the payoff is shown in Figure 17.1b." [hull-2015, p. 371].
- O Wystup chama a estrutura também de *bonus forward* [wystup-2006, p. 151], nome que no OVML designa outra estrutura ([[BFW]]) [inferência: texto da Bloomberg do BFW + wystup-2006, p. 152].
