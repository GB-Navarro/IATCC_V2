---
aliases: ["Participating Fwd"]
composta_de: []
variante_de: ["[[RR]]"]
flexivel: [strike]
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# Participating Fwd (PF)

![[Participating Fwd (PF)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| EU | put | K1 | T1 | r | - | — |
| EU | call | K1 | T1 | 1 | + | — |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | compra de call, venda de put | [ovml]; [wystup-2006, p. 141] |
| Strikes | o mesmo nas duas pernas, na definição da Bloomberg | [ovml] |
| Vencimento | o mesmo nas duas pernas | [ovml] |
| Notional | diferente: o da put vendida é menor que o da call (baixo risco) ou maior (alto risco, ex.: o dobro) | [ovml]; [wystup-2006, p. 141] |
| Instrumento | opções europeias | [inferência: combinação de vanillas, que o Wystup define como opções europeias, wystup-2006, p. 39] |
| Flexível | strike: os strikes podem ser diferentes | [wystup-2006, p. 141]; [wystup-2006, p. 142, exemplo] |
| Variante de | RR, que o Wystup descreve como muito parecido | [wystup-2006, p. 141] |

## Restrições

- Costuma ser montado a custo baixo ou zero [ovml]; [wystup-2006, p. 141].

## Notas

- A Bloomberg exige o mesmo strike [ovml]. O Wystup admite strikes diferentes: "In a more general manner, the strikes can also be different." [wystup-2006, p. 141]
