---
aliases: ["KIKO Forward"]
composta_de: ["[[KO]]", "[[KOKI]]"]
variante_de: []
flexivel: []
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# KIKO Forward (KKF)

![[KIKO Forward (KKF)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| KKF | — | K1 | T1 | 1 | + | — |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | compra de uma knock-out e venda de uma KIKO | [ovml] |
| Strikes | o mesmo nas duas pernas: o cliente fica hedgeado no strike | [ovml] |
| Composta de | KO e KIKO | [ovml] |
| Composta de | a KIKO é do tipo KOKI: se o KO é tocado primeiro, o hedge se perde mesmo que o KI venha depois | [inferência: texto da Bloomberg do KKF + wystup-2006, p. 115] |

## Restrições

- Os tipos (call ou put) das pernas não são informados, por isso a tabela tem uma linha só [ovml].
- Pode ser montado a custo zero [ovml].

## Notas

- Fonte única: OVML [ovml].
