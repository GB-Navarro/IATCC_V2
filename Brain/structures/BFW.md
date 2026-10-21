---
aliases: ["Bonus Forward"]
composta_de: ["[[KO]]", "[[KI]]"]
variante_de: []
flexivel: []
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# Bonus Forward (BFW)

![[Bonus Forward (BFW)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| BFW | — | K1 | T1 | 1 | + | — |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | compra de uma knock-out e de uma knock-in e venda de uma reverse knock-in, todas com a mesma barreira | [ovml] |
| Composição | antes da barreira o cliente tem uma opção comprada; depois, um forward na taxa bônus (K1) | [ovml] |
| Composta de | KO e KI | [ovml] |

## Restrições

- Os tipos (call ou put) das pernas não são informados, por isso a tabela tem uma linha só [ovml].
- Pode ser montado a custo zero [ovml].

## Notas

- O Wystup usa *bonus forward* como sinônimo de range forward: "The range or bonus forward is another forward enhancement with guaranteed worst case." [wystup-2006, p. 151]. O BFW do OVML é outra estrutura [ovml].
