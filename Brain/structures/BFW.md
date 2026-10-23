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
| KI | call | K1 | T1 | 1 | + | — |
| KI | put | K1 | T1 | 1 | - | — |
| KO | call | K2 | T1 | 1 | + | — |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | compra de uma knock-out e de uma knock-in e venda de uma reverse knock-in, todas com a mesma barreira | [ovml] |
| Composição | antes da barreira o cliente tem uma opção comprada; depois, um forward na taxa bônus (K1) | [ovml] |
| Composição | call knock-out comprada no pior caso; put knock-in (reverse) vendida e call knock-in comprada no caso melhorado; todas com a mesma barreira | [wystup-2006, p. 173] |
| Strikes | as duas knock-in no mesmo strike (o caso melhorado), a knock-out em outro (o pior caso) | [wystup-2006, p. 173] |
| Strikes | o caso melhorado pode ser igual ao forward outright | [ovml]; [wystup-2006, p. 173, exemplo] |
| Composta de | KO e KI | [ovml]; [wystup-2006, p. 173] |

## Restrições

- A tabela segue o collar extra, com o strike da knock-out acima do das knock-in [wystup-2006, p. 173, exemplo]. No boomerang forward, a mesma composição aparece com a ordem inversa [wystup-2006, p. 161].
- Pode ser montado a custo zero [ovml].

## Notas

- O Wystup usa *bonus forward* como sinônimo de range forward: "The range or bonus forward is another forward enhancement with guaranteed worst case." [wystup-2006, p. 151]. O BFW do OVML é outra estrutura [inferência: texto da Bloomberg do BFW + wystup-2006, p. 152].
- O BFW do OVML corresponde ao *collar extra* do Wystup, com a mesma composição e barreira comum [wystup-2006, pp. 172–173].
