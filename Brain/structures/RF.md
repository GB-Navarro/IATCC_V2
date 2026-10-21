---
aliases: ["Range Forward"]
composta_de: ["[[DNT]]"]
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
| Composição | forward sintético no strike do pior caso (compra de call e venda de put) mais compra de um double-no-touch | [wystup-2006, p. 152] |
| Strikes | o mesmo nas duas opções: o pior caso | [wystup-2006, p. 152] |
| Vencimento | o mesmo em todas as pernas | [wystup-2006, p. 151] |
| Notional | igual nas duas opções | [wystup-2006, p. 152, exemplo] |
| Notional | o pagamento do DNT (r) cobre a diferença entre pior e melhor caso | [inferência: wystup-2006, p. 152] |
| Barreira | as do DNT: na versão básica, o intervalo é verificado só no vencimento; também há versão com barreiras americanas | [wystup-2006, pp. 151–152] |
| Composta de | DNT, mais um forward sintético | [wystup-2006, p. 152] |

## Restrições

- É montado a custo zero, como um forward outright [wystup-2006, p. 151].

## Notas

- O Hull usa *range forward* para o collar (RR do OVML): "This is known as a short position in a range forward contract." [hull-2015, p. 370].
- O Wystup chama a estrutura também de *bonus forward* [wystup-2006, p. 151], nome que no OVML designa outra estrutura ([[BFW]]) [ovml].
