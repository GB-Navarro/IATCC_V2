---
aliases: ["Non-Sequential KIKO", "KIKO"]
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
# Non-Sequential KIKO (KOKI)

![[Non-Sequential KIKO (KOKI)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| KOKI | call | K1 | T1 | 1 | + | — |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | opção knock-in que pode ser cancelada pelo knock-out a qualquer momento; a tabela mostra a call | [ovml]; [wystup-2006, p. 115] |
| Barreira | kiko: uma barreira KI e uma KO; o KO vale antes e depois do KI | [ovml]; [wystup-2006, pp. 115–116] |
| Payoff | vanilla | [ovml] |
| Sinônimo | KIKO do tipo 1, o padrão de mercado | [wystup-2006, pp. 115–116] |

## Restrições

- É replicável com barreiras padrão: KIKO(L, U) = KO(L) − DKO(L, U) [wystup-2006, p. 116].
