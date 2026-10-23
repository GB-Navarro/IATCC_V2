---
aliases: ["Forward Extra", "Variance Forward", "Shark Forward", "Forward Plus"]
composta_de: ["[[EU]]", "[[KI]]"]
variante_de: []
flexivel: []
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# Forward Extra (FE)

![[Forward Extra (FE)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| EU | call | K1 | T1 | 1 | + | — |
| KI | put | K1 | T1 | 1 | - | — |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | compra de call vanilla e venda de put reverse knock-in, no mesmo strike | [ovml] |
| Composição | equivale a um forward sintético mais um reverse knock-out, a composição do shark forward | [wystup-2006, pp. 164, 273]; [inferência: call − put + RKO = call − RKI, pela paridade KO + KI = vanilla, wystup-2006, p. 42] |
| Strikes | o mesmo nas duas pernas | [ovml] |
| Vencimento | o mesmo nas duas pernas | [ovml]; [wystup-2006, p. 145, exemplo] |
| Notional | igual nas duas pernas | [inferência: o double shark forward aumenta o notional do reverse knock-in "commonly by a factor of 2", logo no padrão são iguais, wystup-2006, p. 164] |
| Barreira | reverse knock-in na put: é tocada quando a put vai para dentro do dinheiro | [ovml]; [wystup-2006, p. 42] |
| Composta de | EU e KI | [ovml] |
| Sinônimo | Variance Forward | [ovml] |
| Sinônimo | shark forward, forward plus, enhanced forward | [wystup-2006, p. 144] |

## Notas

- O FE do OVML corresponde ao que o Wystup chama de *forward plus*: "(shark) forward plus: the buyer benefits from a favorable spot movement." [inferência: texto da Bloomberg do FE + wystup-2006, pp. 145, 164]. O *forward extra* do Wystup é a variante oposta, em que o cliente ganha quando o spot anda contra a sua posição [wystup-2006, p. 145].
