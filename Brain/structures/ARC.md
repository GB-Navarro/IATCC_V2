---
aliases: ["Average Rate Collar"]
composta_de: ["[[AVG]]"]
variante_de: ["[[RR]]"]
flexivel: []
# gerado pelo script — não editar
tags: []
instrumentos: []
ambigua_com: []
---
# Average Rate Collar (ARC)

![[Average Rate Collar (ARC)]]

## Pernas

| instrumento | tipo | strike | vencimento | notional | lado | moneyness |
|---|---|---|---|---|---|---|
| AVG | put | K1 | T1 | 1 | - | OTM |
| AVG | call | K2 | T1 | 1 | + | OTM |

| Informação | Valor | Fonte |
|---|---|---|
| Composição | como um risk reversal, mas com put e call de taxa média | [ovml] |
| Strikes | como no RR: diferentes, put abaixo da call | [inferência: texto da Bloomberg do ARC + nota RR] |
| Vencimento | como no RR: o mesmo | [inferência: idem] |
| Notional | como no RR: igual | [inferência: idem] |
| Moneyness | como no RR: as duas OTM | [inferência: idem] |
| Composta de | AVG | [ovml] |
| Variante de | RR, com opções de média | [ovml] |
