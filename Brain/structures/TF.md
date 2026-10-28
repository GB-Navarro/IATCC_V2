---
aliases: ["Tracker Forward"]
composta_de: ["[[FWD]]", "[[EU]]"]
variante_de: []
flexivel: [strike]
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# Tracker Forward (TF)

![[Tracker Forward (TF)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| FWD | — | K1 | T1 | 1 | + | — |
| EU | put | K2 | T1 | 1 | + | — |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | compra de forward e compra de put (ou venda de forward e compra de call) | [ovml] |
| Strikes | a Bloomberg não fixa a relação entre a taxa do forward e o strike da opção | [ovml] |
| Flexível | strike, pela mesma razão | [ovml] |
| Vencimento | o mesmo nas duas pernas | [inferência: as duas pernas protegem o mesmo fluxo; texto da Bloomberg] |
| Notional | igual: o valor total do hedge | [inferência: o texto da Bloomberg fala em "protection rate for their full hedge amount" e em participar de "any favourable market movements"] |
| Composta de | FWD e EU | [ovml]; [inferência: convenção do _schema.md, combinações de vanillas usam opções europeias] |

## Restrições

- A versão com venda de forward e compra de call não é coberta pelas regras de short e espelho, porque o espelho não inverte o lado do forward [inferência: regras do _schema.md].

## Notas

- Fonte única para a definição: OVML. Nenhuma fonte de `fontes/` define esta estrutura [inferência: cobertura por estrutura em `fontes/README.md`].
