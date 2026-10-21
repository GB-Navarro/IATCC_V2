---
aliases: ["Ratio Straddle"]
composta_de: []
variante_de: ["[[SD]]"]
flexivel: []
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# Ratio Straddle (SDR)

![[Ratio Straddle (SDR)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| EU | put | K1 | T1 | r | + | — |
| EU | call | K1 | T1 | 1 | + | — |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | compra de call e de put | [ovml] |
| Strikes | o mesmo nas duas pernas | [ovml] |
| Vencimento | o mesmo nas duas pernas | [ovml] |
| Notional | diferente entre as pernas (razão r) | [ovml] |
| Moneyness | strike geralmente fora do dinheiro | [ovml] |
| Instrumento | opções europeias | [inferência: combinação de vanillas, que o Wystup define como opções europeias, wystup-2006, p. 39] |
| Variante de | SD, com strike fora do dinheiro e notionals diferentes | [ovml] |

## Restrições

- Os notionals são escolhidos para que a estrutura tenha delta forward zero [ovml].

## Notas

- Fonte única: OVML. Nenhuma fonte de `fontes/README.md` trata a estrutura [ovml].
