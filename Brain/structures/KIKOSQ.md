---
aliases: ["Sequential KIKO&KIKI"]
composta_de: []
variante_de: []
flexivel: []
barreira: kiko
barreiras: 2
payoff: vanilla
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# Sequential KIKO&KIKI (KIKOSQ)

![[Sequential KIKO&KIKI (KIKOSQ)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| KIKOSQ | call | K1 | T1 | 1 | + | — |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | opção knock-in cujo knock-out só vale depois do knock-in (KIKO sequencial); variante com dois knock-ins em sequência (KIKI sequencial); a tabela mostra a call | [ovml] |
| Barreira | kiko no KIKO sequencial; dois ki no KIKI sequencial; duas barreiras | [ovml] |
| Payoff | vanilla | [ovml] |
| Sinônimo | KIKO do tipo 2: o knock-out só pode ocorrer depois do knock-in | [wystup-2006, pp. 115–116] |
| Sinônimo | o KIKI sequencial é uma first-then-barrier option | [haug-2007, p. 169] |

## Notas

- A Bloomberg reúne dois produtos na mesma descrição, o KIKO sequencial e o KIKI sequencial [ovml]. O campo `barreira` registra só o primeiro.
- A frase da Bloomberg sobre o DownIn "reached first" quer dizer que um toque no DownIn antes do UpIn não conta [inferência: texto da Bloomberg + haug-2007, p. 169]. O Haug descreve a mesma regra para a ordem inversa: "To be knocked in, the asset price has to hit the lower barrier at least once before an upper barrier hit has any effect." [haug-2007, p. 169]
