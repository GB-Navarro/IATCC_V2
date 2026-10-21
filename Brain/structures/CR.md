---
aliases: ["Condor"]
composta_de: ["[[SN]]"]
variante_de: []
flexivel: []
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# Condor (CR)

![[Condor (CR)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| EU | put | K1 | T1 | 1 | + | — |
| EU | put | K2 | T1 | 1 | - | — |
| EU | call | K3 | T1 | 1 | - | — |
| EU | call | K4 | T1 | 1 | + | — |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | compra de um strangle largo e venda de um strangle mais estreito | [ovml] |
| Strikes | quatro; o strangle vendido (K2–K3) fica dentro do comprado (K1–K4) | [ovml] |
| Strikes | os quatro costumam ser consecutivos | [natenberg-1994, p. 158] |
| Vencimento | o mesmo nas quatro pernas | [natenberg-1994, p. 158] |
| Notional | igual: uma opção por perna | [natenberg-1994, p. 158] |
| Instrumento | opções europeias | [inferência: combinação de vanillas, que o Wystup define como opções europeias, wystup-2006, p. 39] |
| Composta de | SN comprado (K1–K4) e SN vendido (K2–K3) | [ovml] |

## Notas

- O Natenberg define o condor com um só tipo de opção: "As with a butterfly, all options must be of the same type (all calls or all puts) and expire at the same time." [natenberg-1994, p. 158]. A versão do OVML, com strangles, tem o mesmo resultado, e o "long" coincide [inferência: mesma equivalência do iron butterfly, natenberg-1994, p. 158].
