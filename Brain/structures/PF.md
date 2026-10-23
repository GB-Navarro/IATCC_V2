---
aliases: ["Participating Fwd"]
composta_de: []
variante_de: ["[[FWD]]", "[[RR]]"]
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
| Notional | diferente entre as pernas | [ovml]; [wystup-2006, p. 141] |
| Notional | o da put vendida é menor que o da call (baixo risco) ou maior (alto risco, ex.: o dobro) | [wystup-2006, p. 141] |
| Instrumento | opções europeias | [inferência: convenção do _schema.md, combinações de vanillas usam opções europeias; vanilla = opção europeia, wystup-2006, p. 39] |
| Flexível | strike: os strikes podem ser diferentes | [wystup-2006, p. 141]; [wystup-2006, p. 142, exemplo] |
| Variante de | FWD: generaliza o forward sintético (call comprada e put vendida, mesmo strike e mesmo notional) com notionals diferentes | [wystup-2006, pp. 140–141] |
| Variante de | RR, que o Wystup descreve como muito parecido | [wystup-2006, p. 141] |

## Restrições

- Costuma ser montado a custo baixo ou zero [ovml]; [wystup-2006, p. 141].

## Notas

- No estilo de alto risco, o Wystup também o chama de *leveraged forward* [wystup-2006, p. 142].
- A Bloomberg exige o mesmo strike [ovml]. O Wystup admite strikes diferentes: "In a more general manner, the strikes can also be different." [wystup-2006, p. 141]
