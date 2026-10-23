---
aliases: ["Collar", "Fence"]
composta_de: ["[[FWD]]", "[[RR]]"]
variante_de: []
flexivel: []
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# Collar (COL)

Estrutura fora do OVML: não há texto da Bloomberg.

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| EU | put | K1 | T1 | 1 | + | OTM |
| FWD | — | K2 | T1 | 1 | + | — |
| EU | call | K3 | T1 | 1 | - | OTM |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | posição comprada no ativo, compra de uma put protetora e venda de uma call coberta | [natenberg-1994, p. 264] |
| Composição | na versão vendida: posição vendida no ativo, compra de call e venda de put | [natenberg-1994, p. 264] |
| Strikes | put abaixo do preço da posição, call acima | [natenberg-1994, p. 263, exemplo]; [hull-2015, p. 370, exemplo] |
| Vencimento | o mesmo nas três pernas | [inferência: as opções vencem na data do fluxo protegido, hull-2015, p. 370; a fence é uma split-price conversion, natenberg-1994, p. 264, e a conversion usa o mesmo vencimento, natenberg-1994, p. 218] |
| Notional | igual nas três pernas: uma put e uma call para a posição | [natenberg-1994, p. 263, exemplo]; [natenberg-1994, p. 264, exemplo]; [hull-2015, p. 370, exemplo] |
| Moneyness | put e call OTM | [natenberg-1994, p. 263, exemplo]; [hull-2015, p. 370, exemplo] |
| Instrumento | a posição no ativo é representada por um FWD | [inferência: em FX, a posição protegida é a compra ou venda futura da moeda, hull-2015, p. 370] |
| Instrumento | opções europeias | [hull-2015, p. 370] |
| Composta de | FWD (a posição) e RR na versão short (put comprada, call vendida) | [inferência: natenberg-1994, p. 264 + tabela de pernas do RR] |
| Sinônimo | fence | [natenberg-1994, p. 264] |
| Sinônimo | collar | [inferência: o collar de juros é "a fence done in the interest rate market", natenberg-1994, p. 265; a fence inclui a posição, natenberg-1994, p. 264] |

## Restrições

- O custo é zero quando a put e a call têm o mesmo preço; se a call vale mais, a estrutura gera crédito [natenberg-1994, p. 263, exemplo]. Em geral, a proteção sai a custo baixo ou com crédito [natenberg-1994, p. 264].
- A versão comprada equivale a um bull spread montado de forma sintética [natenberg-1994, p. 264].
- Só casa quando a posição protegida (o FWD) está no mesmo grupo; se vierem só as duas opções, a receita que casa é a do [[RR]], na versão short [inferência: tabelas de pernas do COL e do RR].
- A versão vendida é a regra global de short. O espelho do `_schema.md` não se aplica, porque não inverte o lado da posição [inferência: regras de short e espelho do _schema.md].

## Notas

- No OVML, "collar" nomeia sempre o par de opções: o RR, "Risk Reversal (Collar)", e duas variantes dele, [[ARC]] e [[EC]] [inferência: nomes e textos da Bloomberg do RR, do ARC e do EC]. O Wystup também chama o par de collar: "A popular liquid product in FX markets is the Risk Reversal or collar." [wystup-2006, p. 31]. Nesta base, a versão só com opções é o [[RR]], e a versão com a posição protegida é esta nota.
- O Hull lista nomes para o range forward, que é só o par de opções: "Other names used for a range forward contract are zero-cost collar, flexible forward, cylinder option, option fence, min–max, and forward band." [hull-2015, p. 599]. O RF do OVML é outra estrutura ([[RF]]) [wystup-2006, pp. 151–152]; [inferência: texto da Bloomberg do RF].
- O Natenberg dá outros nomes à fence: "Fences go by a variety of names: range forwards, tunnels, cylinders; among floor traders they are sometimes known as split-price conversions and reversals." [natenberg-1994, p. 264]. Eles ficam fora de `aliases`: range forward e cylinder designam o par de opções no Hull [hull-2015, p. 599], o reversal é a versão vendida [natenberg-1994, p. 218], e no Wystup o tunnel é outro produto [wystup-2006, p. 179].
- O collar de juros, cap comprado e floor vendido, é outro produto, fora do escopo da base [hull-2015, p. 679]. O Natenberg o descreve como "simply a fence done in the interest rate market." [natenberg-1994, p. 265]
- O collar extra series do Wystup é outra estrutura: em cada vencimento, uma call garante o pior caso e, se o knock-in ocorrer, fica travado um forward no caso melhorado. Corresponde ao [[BFW]] do OVML [wystup-2006, pp. 172–173].
