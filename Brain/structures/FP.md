---
aliases: ["Forward Premium"]
composta_de: []
variante_de: []
flexivel: []
payoff: vanilla
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# Forward Premium (FP)

![[Forward Premium (FP)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| FP | call | K1 | T1 | 1 | + | — |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | opção cujo prêmio é pago no futuro, em geral na data de liquidação da opção; a tabela mostra a call | [ovml] |
| Payoff | vanilla: o caso mais comum; a Bloomberg não especifica o tipo de opção | [inferência: o texto da Bloomberg diz só "an option payoff"] |

## Notas

- Fonte única para a definição: OVML. Nenhuma fonte de `fontes/` define esta estrutura [inferência: cobertura por estrutura em `fontes/README.md`].
- Não confundir com a pay-later option, em que o prêmio só é pago se a opção for exercida [wystup-2006, p. 116].
