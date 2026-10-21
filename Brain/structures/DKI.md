---
aliases: ["Double KI"]
composta_de: []
variante_de: ["[[KI]]"]
flexivel: []
barreira: ki
barreiras: 2
payoff: vanilla
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# Double KI (DKI)

![[Double KI (DKI)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| DKI | call | K1 | T1 | 1 | + | — |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | opção vanilla que só passa a existir se o spot tocar uma de duas barreiras; a tabela mostra a call | [ovml]; [haug-2007, p. 156] |
| Barreira | ki, duas barreiras (inferior e superior) | [ovml]; [haug-2007, p. 156] |
| Payoff | vanilla, se alguma barreira for tocada | [ovml] |
| Variante de | KI, com duas barreiras | [inferência: comparação dos textos da Bloomberg do KI e do DKI] |

## Restrições

- Equivale a uma vanilla comprada mais um double knock-out vendido, com os mesmos strike e vencimento [haug-2007, p. 156].

## Notas

- A Bloomberg justifica o prêmio menor pelas duas chances de a opção nunca ser ativada [ovml], o que está invertido: com duas barreiras há duas formas de ativar. Pelo Haug, "a double knock-in put is equal to a long standard put and a short double knock-out put." [haug-2007, p. 156]. Como o DKO vale menos que o KO de uma barreira, o DKI vale mais que o KI de uma barreira [inferência: haug-2007, p. 156 + wystup-2006, p. 42].
