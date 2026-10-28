---
aliases: ["Euro-American KO", "KOAMKIEU"]
composta_de: []
variante_de: ["[[KOKI]]"]
flexivel: []
barreira: kiko
barreiras: 2
payoff: vanilla
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# Euro-American KO (EAKO)

![[Euro-American KO (EAKO)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| EAKO | call | K1 | T1 | 1 | + | — |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | opção com knock-out americano e knock-in europeu, que só vale no vencimento; a tabela mostra a call | [ovml]; [wystup-fxcol-2022, p. 1] |
| Barreira | kiko: KO americano fora do dinheiro, KI europeu dentro do dinheiro | [ovml] |
| Payoff | vanilla | [ovml] |
| Variante de | KOKI: é um caso especial de KIKO | [ovml]; [wystup-fxcol-2022, p. 1] |
| Sinônimo | KOAMKIEU | [wystup-fxcol-2022, p. 1] |

## Restrições

- O cliente escolhe se o pagamento ocorre com o spot acima ou abaixo da barreira europeia no vencimento [ovml].

## Notas

- Não confundir com a transatlantic barrier option do Wystup, em que as duas barreiras (americana e europeia) são knock-out [wystup-2006, p. 108].
