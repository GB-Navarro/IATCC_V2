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
| Instrumento | opções europeias | [inferência: convenção do _schema.md, combinações de vanillas usam opções europeias; vanilla = opção europeia, wystup-2006, p. 39] |
| Variante de | SD, com strike fora do dinheiro e notionals diferentes | [ovml] |

## Restrições

- Os notionals são escolhidos para que a estrutura tenha delta forward zero [ovml].

## Notas

- Fonte única: OVML. A busca por "ratio straddle" nas fontes com texto não teve resultado; o natenberg-1994, escaneado, não pôde ser pesquisado [inferência: busca de texto em `fontes/`].
