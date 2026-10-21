---
aliases: ["Butterfly"]
composta_de: ["[[SN]]", "[[SD]]"]
variante_de: []
flexivel: []
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# Butterfly (BF)

![[Butterfly (BF)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| EU | put | K1 | T1 | 1 | + | OTM |
| EU | put | K2 | T1 | 1 | - | ATM |
| EU | call | K2 | T1 | 1 | - | ATM |
| EU | call | K3 | T1 | 1 | + | OTM |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | compra de um strangle e venda de um straddle | [ovml]; [wystup-2006, p. 36] |
| Strikes | três: o do straddle no meio do intervalo entre os do strangle | [natenberg-1994, p. 158]; [wystup-2006, p. 38, exemplo] |
| Vencimento | o mesmo em todas as pernas | [ovml]; [natenberg-1994, p. 158] |
| Notional | igual em todas as pernas | [wystup-2006, p. 38, exemplo] |
| Moneyness | strangle OTM, straddle ATM | [ovml] |
| Instrumento | opções europeias | [wystup-2006, pp. 29, 39] |
| Composta de | SN (comprado) e SD (vendido) | [ovml]; [wystup-2006, p. 36] |

## Notas

- O Natenberg chama esta posição de *short iron butterfly* e mostra que ela equivale a um butterfly comprado: "A short iron butterfly is therefore equivalent to a long butterfly." [natenberg-1994, p. 158]. O "long" do OVML está certo no resultado, mas o nome *long iron butterfly* designa a posição oposta.
- No Wystup, a definição coincide com a do OVML [wystup-2006, p. 36], mas o exemplo descreve a posição oposta (straddle comprado, strangle vendido): "If K1 < ST < K2, it would sell 1 Mio EUR at strike K2." [wystup-2006, p. 37]
