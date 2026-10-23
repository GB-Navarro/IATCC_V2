# Validação do Claude — lote 4

Validador: agente independente · 2026-10-22 · cada citação conferida na página inteira (texto do PyMuPDF; imagem da p. 173 do Wystup), cada `[ovml]` no arquivo da Bloomberg, e busca de evidência contrária no cap. 2 e na Tabela 5.1 do `wystup-2006` e no `wystup-fxcol-2026`. Obs.: a seção "Divergências" de `fontes/README.md` apareceu junto na leitura da cobertura; não foi usada como evidência.

## Resumo

| ✅ | ◐ | ✗ | ⚖ | ? | total |
|---|---|---|---|---|---|
| 77 | 20 | 2 | 16 | 0 | 115 |

## Status das correções (aplicadas pelo Claude principal, 2026-10-22)

Os vereditos abaixo valem para as notas **antes** das correções.

| Status | Itens |
|---|---|
| ✎ aplicada | 1, 3–7, 9, 11–17, 19–22, 24–26; 10 (só a citação dos strikes); 18 (só as citações diretas pp. 164 e 273) |
| ✎ aplicada com ajuste | 2: a tabela de 3 pernas segue o collar extra; sem `flexivel: strike`, que soltaria a igualdade dos strikes das knock-in; a ordem inversa do boomerang forward fica registrada em Restrições. 23: a p. 164 entrou na nota do auto-renewal |
| ✎ decidida pelo usuário | 8, 10, 18, 23, 27 (D36, D37) |

## Correções propostas

**Prioridade 1**

1. EC · "Strikes: a Bloomberg não fixa a relação" e `flexivel: [strike]` são contraditos pelo texto da Bloomberg ("lower risk alternative to the Risk Reversal", "flexibility between the best and worse case rates") e pela própria tabela de pernas, que já fixa put K1 < call K2. Com strikes iguais, a estrutura seria o FE. Correção: trocar a linha Strikes por "diferentes; put abaixo da call, como no RR | [inferência: texto da Bloomberg do EC, alternativa ao RR com 'best and worse case rates'; nota RR]"; apagar a linha Flexível; tirar `strike` de `flexivel`.

**Prioridade 2**

2. BFW · a estrutura está no Wystup. O *collar extra* (pp. 172–173) tem a mesma composição: "buys a EUR call with strike at the worst case, down-and-out", "sells a EUR put with strike at the improved case, down-and-in", "buys a EUR call with strike at the improved case, down-and-in", todas com barreira em 128.00. O *improved case* é igual ao forward outright (Tabela 2.21), como a "bonus rate, which can be equal to the current forward rate" da Bloomberg. O *boomerang forward* (p. 161) tem a mesma composição, com a ordem dos strikes invertida. Correções, a decidir com o usuário:
   - trocar a Restrição "os tipos não são informados" por uma tabela de 3 linhas [wystup-2006, p. 173]: `KO | call | K2 | T1 | 1 | +`, `KI | call | K1 | T1 | 1 | +`, `KI | put | K1 | T1 | 1 | -`, com `flexivel: [strike]`, porque a ordem dos strikes muda entre a p. 173 e a p. 161;
   - em Notas, registrar que o BFW do OVML corresponde ao *collar extra* do Wystup [wystup-2006, pp. 172–173];
   - na cobertura de `fontes/README.md`: BFW passa a wystup-2006 pp. 161, 172–173 ✓, e EC passa a "—". O collar extra não é o EC: depois do KI, o collar extra vira um forward; o EC vira um collar.
3. RF · o DNT da tabela é americano (a nota DNT fala em "não tocar"). Na versão básica do Wystup, porém, o intervalo só é verificado no vencimento (pp. 151–152, "at expiry"), o que dá um DNT europeu (p. 324: "EDNT(L, H) = digital(L) − digital(H)"). Correção: na linha Barreira, dizer que a tabela representa a versão com barreiras americanas e que a básica usa um DNT europeu [wystup-2006, pp. 152, 324].
4. RF · três trocas:
   - Notional "igual nas duas opções": trocar `[wystup-2006, p. 152, exemplo]` por `[wystup-2006, p. 140]` ("replicated by a long call and a short put with the same strike and same notional"). A Tabela 2.8 só dá um notional para a estrutura inteira.
   - Composição: acrescentar `[wystup-2006, p. 140]` para o parêntese "(compra de call e venda de put)".
   - Vencimento: trocar por `[inferência: uma única data de vencimento e o intervalo verificado "at expiry"; wystup-2006, p. 151]`.
5. RF e BFW · "o BFW do OVML é outra estrutura" está com `[ovml]`. No RF, o texto embutido nem fala do BFW. Nas duas notas, trocar por `[inferência: texto da Bloomberg do BFW + wystup-2006, p. 152]`.
6. FE · Notas: "O FE do OVML corresponde ao *forward plus*" é leitura conjunta. Trocar a primeira `[wystup-2006, p. 145]` por `[inferência: texto da Bloomberg do FE + wystup-2006, pp. 145, 164]`. Na p. 164, o shark forward de um comprador de USD "buys a EUR put with strike equal to the worst case and sells a reverse knock-in EUR call".
7. FE · Notional: o exemplo da p. 145 dá um único notional para o forward mais o RKO, não para a call e a put RKI. Trocar por `[inferência: o double shark forward aumenta o notional do reverse knock-in "commonly by a factor of 2", logo no padrão são iguais; wystup-2006, p. 164]`. Vencimento: acrescentar `[wystup-2006, p. 145, exemplo]` ("3 months maturity").
8. TF · tabela de pernas: os símbolos K1 (forward) < K2 (put) afirmam uma ordem que a nota diz não existir. Pelo "market rate adjusted by fixed spread", o natural seria strike da put ≤ taxa do forward. Decidir com o usuário: trocar para FWD K2 / put K1, ou registrar que, com `flexivel: strike`, a ordem dos símbolos é arbitrária.
9. TF · duas citações:
   - Composta de: o texto da Bloomberg só diz "put"/"call". Trocar `[ovml]` por `[ovml]; [inferência: convenção do _schema.md, vanillas em combinações usam EU]`.
   - Notional: trocar `[ovml]` por `[inferência: texto da Bloomberg, "protection rate for their full hedge amount" e "any favourable market movements"]`.
10. KKF · duas mudanças:
   - Strikes: a Bloomberg diz "hedged at the strike", não que as pernas têm o mesmo strike. Trocar por `[inferência: texto da Bloomberg, "hedged at the strike"]`.
   - Tipos: pela mesma leitura, KO comprada mais KIKO vendida no mesmo strike formam um forward, então uma perna é call e a outra put. Decisão do usuário: usar a tabela `KO | call | K1 | T1 | 1 | +` / `KOKI | put | K1 | T1 | 1 | -`, ou manter uma linha e reescrever a Restrição como decisão, não como falta de informação.
11. BFF · "um valor alavancado é vendido" → "pode ser vendido" (no texto da Bloomberg: "can be sold").
12. FLEX · dividir a linha Sinônimo em "time option | [ovml]; [wystup-2006, p. 166]" e "forward de estilo americano | [wystup-2006, p. 166]". A Bloomberg só diz "time-option forward contract".
13. ACCU · Sinônimo "accumulative forward": a p. 156 não usa "accumulator". Trocar por `[inferência: mesma definição do texto da Bloomberg e da wystup-2006, p. 156; o Wystup chama esses produtos de "accumulators" na p. 161]`.
14. ACCUKO · duas trocas:
   - Barreira: a p. 157 não diz "uma barreira" nem "contínua". Trocar `[wystup-2006, p. 157]` por `[wystup-2006, p. 156]` ("If the non-resurrecting knock out level of 1.2000 is ever traded").
   - Restrição: escrever "Por padrão, o fixing do dia conta…". A fonte diz "The standard is that it does" e pede que isso seja combinado no contrato.
15. ARF · "o inverso da média, ou seja, a média harmônica" é ambíguo: o inverso da média do spot é a média harmônica da taxa inversa R = 1/S (eq. 1.423), não a do spot. Trocar por "a média harmônica da taxa inversa 1/S".
16. EC · Notas: a citação literal está incompleta. O texto é "Knock-In put option with a barrier that is in-the-money".

**Prioridade 3**

17. KKF, EF e BFF · a nota "Fonte única: OVML" cita como premissa a cobertura de `fontes/README.md`, mas lá essas estruturas têm "~" (parcial), não "—". Reescrever como "nenhuma fonte define esta estrutura", citando as páginas lidas. Já o ACCUKI é só OVML (o Wystup não tem accumulator com knock-in) e não tem essa nota.
18. FE · `aliases` não tem "Forward Plus" nem "Enhanced Forward", que a tabela de origem lista como sinônimos. A inferência da Composição pode virar citação direta:
   - `[wystup-2006, p. 164]`;
   - `[wystup-2006, p. 273]`: "long EUR call and short EUR put" mais "a long EUR put with a reverse knock-out barrier", com "the strike of all options is equal";
   - `wystup-fxcol-2026`: traz "EUR put – EUR Call RKI" e diz que o forward plus é "labelled Forward Extra (American) in ICE Data Services".

   O double shark forward (pp. 164–165, com o notional do RKI multiplicado por 2) é uma variante não registrada.
19. EC · as inferências de Vencimento e Notional não citam a premissa (o RR). A de Notional é fraca: o PF também é variante do RR e tem notionals diferentes.
20. KKF · a inferência do KOKI está certa, mas a justificativa está incompleta. "KO primeiro → perde o hedge" só exclui o tipo 2 da p. 115; quem exclui o tipo 3 é "KI primeiro, KO depois → perde o hedge". Citar as duas frases.
21. RF · três pontos:
   - `composta_de` só tem `[[DNT]]`, mas a tabela tem duas pernas EU, e FE, EC e TF incluem EU;
   - a Tabela 5.1 (p. 324, "bonus forward | forward + DNT") é citação direta da composição;
   - a citação do Hull é a da posição *short* (p. 370), e a nota RR usa a da *long* (p. 371), que é a que corresponde ao RR do OVML. Harmonizar.
22. KOF · faltou a desvantagem "No worst case scenario" [wystup-2006, p. 144].
23. EF · é nota de 1 perna com linha Barreira, mas não tem `barreira`/`barreiras`/`payoff` (o FLEX, também um forward, tem `payoff: linear`). Além disso, a renovação do auto-renewal forward depende de uma barreira: "if at the end of the first year, the exchange rate is above 120.00, then the strategy is automatically renewed" (p. 164). Acrescentar a p. 164.
24. FLEX · divergência não registrada: o Wystup admite exercer partes do montante em datas diferentes e dá o sinônimo *shout forward* (p. 167); a Bloomberg fala de uma única data de entrega.
25. BFF · o accumulative forward (p. 156, com acumulação por fixing e "Leverage") também é parecido e não foi citado.
26. ASF · a 1ª Restrição ("aparecem no Wystup") não é restrição: mover para Notas ou cortar.
27. BFW, KKF · são notas de 1 linha sem `payoff`/`barreira`, enquanto o ACCU tem `payoff`. Decidir se esses campos se aplicam a compostas representadas numa linha só.

## FE

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: compra de call vanilla e venda de put reverse knock-in, no mesmo strike | `[ovml]` | ✅ | "purchasing a vanilla call (put) option and simultaneously selling a Reverse Knock-In put (call) at the same strike" |
| Composição: equivale a forward sintético + reverse knock-out (shark forward) | `[inferência: …; wystup-2006, pp. 42, 145]` | ⚖ | Premissas corretas ("knock-out + knock-in = vanilla", p. 42; "a forward contract … and a reverse knock-out", p. 145) e conta certa; há evidência direta nas pp. 164 e 273 (item 18). |
| Strikes: o mesmo nas duas pernas | `[ovml]` | ✅ | "at the same strike" |
| Vencimento: o mesmo nas duas pernas | `[ovml]` | ◐ | Só por contexto ("At expiration", no singular); "simultaneously" se refere à contratação. |
| Notional: igual nas duas pernas | `[wystup-2006, p. 145, exemplo]` | ◐ | O exemplo dá 1 MIO USD para forward + RKO, não para call e put RKI; só vale via paridade (item 7). |
| Barreira: reverse KI na put, tocada quando a put vai para dentro do dinheiro | `[ovml]` | ✅ | "the barrier is hit when the option is moving into-the-money" |
| 〃 | `[wystup-2006, p. 42]` | ✅ | "regular barriers are out of the money, reverse barriers are in the money" |
| Composta de: EU e KI | `[ovml]` | ✅ | "vanilla call" + "Reverse Knock-In put" |
| Sinônimo: Variance Forward | `[ovml]` | ✅ | "Forward Extra (aka Variance Forward)" |
| Sinônimo: shark forward, forward plus, enhanced forward | `[wystup-2006, p. 144]` | ✅ | "also called forward plus or forward extra or enhanced forward"; a lista inclui "forward extra", que a p. 145 depois separa. |
| Notas: o FE do OVML é o *forward plus* do Wystup (com citação literal) | `[wystup-2006, p. 145]` | ◐ | A citação literal confere; a correspondência (correta: min(S, K) até o gatilho) é leitura conjunta com o texto da Bloomberg (item 6). |
| Notas: o *forward extra* é a variante oposta | `[wystup-2006, p. 145]` | ✅ | "the buyer benefits from a spot movement against his position" |

**Verificações da nota:**
- Tabela de pernas: ✅ call EU K1 + / put KI K1 −; confere com o texto da Bloomberg e com a p. 164 (versão espelho).
- Frontmatter: ◐ `composta_de` certo; `aliases` sem os sinônimos da tabela de origem (item 18).
- Omissões/contradições: ◐ double shark forward (pp. 164–165) não registrado; o `wystup-fxcol-2026` confirma o conflito de nome.

## EC

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: compra de call vanilla e venda de put KI com barreira dentro do dinheiro | `[ovml]` | ✅ | "selling a Knock-In put option with a barrier that is in-the-money" |
| Barreira: reverse knock-in, dentro do dinheiro | `[ovml]` | ✅ | Idem; o termo "reverse" vem da p. 42. |
| 〃 | `[wystup-2006, p. 42]` | ✅ | "reverse barriers are in the money" |
| Strikes: a Bloomberg não fixa a relação | `[ovml]` | ✗ | O texto implica put abaixo da call ("flexibility between the best and worse case rates", alternativa ao RR); com strikes iguais seria o FE; a tabela já fixa K1 < K2. |
| Flexível: strike, pela mesma razão | `[ovml]` | ✗ | Cai com a linha anterior. |
| Vencimento: o mesmo | `[inferência: alternativa ao RR…]` | ⚖ | Conclusão razoável; a premissa "o RR tem um só vencimento" ficou sem citação. |
| Notional: igual | `[inferência: idem]` | ⚖ | Fraca: ser alternativa ao RR não implica notional igual (o PF também é variante do RR, com razão). |
| Composta de: EU e KI | `[ovml]` | ✅ | "vanilla call" + "Knock-In put" |
| Variante de: RR, de menor risco | `[ovml]` | ✅ | "a lower risk alternative to the Risk Reversal strategy" |
| Notas: o termo da Bloomberg é um reverse knock-in | `[ovml]` | ◐ | Conteúdo certo, mas a citação literal está inexata: falta "option" (item 16). |
| 〃 | `[wystup-2006, p. 42]` | ✅ | Legenda da Fig. 1.19, idêntica. |

**Verificações da nota:**
- Tabela de pernas: ✅ KI put K1 − / EU call K2 +; a ordem K1 < K2 está certa e contradiz a linha Strikes.
- Frontmatter: ✗ `flexivel: [strike]` (item 1); o resto ✅.
- Omissões/contradições: ✅ nenhuma fonte define o EC. O collar extra (p. 172), que a cobertura associa ao EC, é o BFW (item 2).

## BFW

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: compra de KO e KI, venda de RKI, mesma barreira | `[ovml]` | ✅ | "The barriers of all three options are set to the same level." |
| Composição: opção comprada antes da barreira; depois, forward na taxa bônus (K1) | `[ovml]` | ✅ | "reverts to a conventional forward at a bonus rate" |
| Composta de: KO e KI | `[ovml]` | ✅ | "a Knock-Out option and a Knock-In option, and the sale of a Reverse Knock-In option" |
| Restrição: os tipos não são informados → uma linha | `[ovml]` | ◐ | Certo quanto ao texto da Bloomberg, mas os tipos são deduzíveis (KI e RKI que viram forward = call e put) e o Wystup os dá (p. 173, p. 161). |
| Restrição: custo zero possível | `[ovml]` | ✅ | "can be made zero-cost by using the OVML 'Solve For' functionality" |
| Notas: no Wystup, *bonus forward* é sinônimo de range forward | `[wystup-2006, p. 151]` | ✅ | Citação literal idêntica. |
| Notas: o BFW do OVML é outra estrutura | `[ovml]` | ◐ | Correto (KO + KI − RKI ≠ forward + DNT), mas é comparação com a p. 152: inferência (item 5). |

**Verificações da nota:**
- Tabela de pernas: ◐ uma linha só, embora a composição com tipos esteja no Wystup (item 2).
- Frontmatter: ✅ `composta_de`.
- Omissões/contradições: ✗ omite a correspondência com o collar extra (pp. 172–173) e com o boomerang forward (p. 161).

## KKF

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: compra de KO e venda de KIKO | `[ovml]` | ✅ | "the purchase of a Knock-Out option and the sale of a KIKO option" |
| Strikes: o mesmo nas duas pernas | `[ovml]` | ◐ | Só por leitura de "the holder is hedged at the strike"; o texto não fala dos strikes das pernas. |
| Composta de: KO e KIKO | `[ovml]` | ✅ | Idem. |
| A KIKO é do tipo KOKI | `[inferência: … + wystup-2006, p. 115]` | ⚖ | Conclusão certa: o texto exclui o tipo 2 (KO primeiro) e o tipo 3 ("If the Knock-Out barrier is reached thereafter, the holder is loses his hedging position"); a nota só usa o 1º caso (item 20). |
| Restrição: os tipos não são informados → uma linha | `[ovml]` | ◐ | Certo quanto ao texto, mas "hedged at the strike" com KO comprada e KIKO vendida = forward, ou seja, uma call e uma put (item 10). |
| Restrição: custo zero possível | `[ovml]` | ✅ | "can be made zero cost by using the OVML 'Solve For' functionality" |
| Notas: fonte única OVML | `[inferência: cobertura…]` | ⚖ | Conclusão certa (a p. 115 só define a KIKO), mas na cobertura o KKF tem "~", não "—" (item 17). |

**Verificações da nota:**
- Tabela de pernas: ◐ uma linha; os tipos são deduzíveis (item 10).
- Frontmatter: ✅ `composta_de: [[KO]], [[KOKI]]`, coerente com a inferência.
- Omissões/contradições: ✅.

## TF

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: compra de forward e de put (ou venda de forward e compra de call) | `[ovml]` | ✅ | "either here buying a forward and buying a put or selling a forward and buying a call" |
| Strikes: a Bloomberg não fixa a relação | `[ovml]` | ✅ | "adjusted by fixed spread" não dá o sinal do spread. |
| Flexível: strike | `[ovml]` | ✅ | Decisão coerente com a linha anterior. |
| Vencimento: o mesmo | `[inferência: mesmo fluxo…]` | ⚖ | Razoável. |
| Notional: igual, o valor total do hedge | `[ovml]` | ◐ | "protection rate for their full hedge amount" fala da proteção; o notional igual da put é só por contexto (item 9). |
| Composta de: FWD e EU | `[ovml]` | ◐ | O texto só diz "put"/"call"; EU vem da convenção do schema (item 9). |
| Restrição: a versão com forward vendido + call não é coberta | `[inferência: _schema.md]` | ⚖ | Correta: o short dá −FWD −put e o espelho dá +FWD +call; nenhuma regra chega a −FWD +call. |
| Notas: fonte única OVML | `[inferência: cobertura…]` | ⚖ | Correta: na cobertura o TF tem "—". |

**Verificações da nota:**
- Tabela de pernas: ◐ K1 (forward) < K2 (put) afirma uma ordem que a nota nega (item 8).
- Frontmatter: ✅.
- Omissões/contradições: ✅.

## RF

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: forward sintético no pior caso (call − put) + compra de DNT | `[wystup-2006, p. 152]` | ◐ | "buys a synthetic forward (see Section 2.1.1) with strike at the worst case and buys a double-no-touch"; a decomposição em call e put está na p. 140. |
| Strikes: o mesmo nas duas opções, o pior caso | `[wystup-2006, p. 152]` | ✅ | "with strike at the worst case" |
| Vencimento: o mesmo em todas as pernas | `[wystup-2006, p. 151]` | ◐ | Só por contexto: uma "specified date (expiry)" e o intervalo verificado "at expiry". |
| Notional: igual nas duas opções | `[wystup-2006, p. 152, exemplo]` | ◐ | A Tabela 2.8 dá um único notional para a estrutura; a igualdade vem da definição da p. 140 (item 4). |
| Notional: o pagamento do DNT (r) cobre pior − melhor caso | `[inferência: p. 152]` | ⚖ | Correta: compra em W pelo sintético e recebe W − B dentro do intervalo, o que dá a taxa B. |
| Barreira: na versão básica, verificada só no vencimento; há versão americana | `[wystup-2006, pp. 151–152]` | ✅ | "within a predefined range at expiry"; "The barriers can be American style barriers." |
| Composta de: DNT + forward sintético | `[wystup-2006, p. 152]` | ✅ | Idem. |
| Restrição: custo zero, como um outright | `[wystup-2006, p. 151]` | ✅ | "a zero cost strategy like an outright forward" |
| Notas: o Hull usa *range forward* para o collar | `[hull-2015, p. 370]` | ✅ | Citação literal idêntica. |
| Notas: o Wystup também o chama de *bonus forward* | `[wystup-2006, p. 151]` | ✅ | "The range or bonus forward" |
| 〃, nome que no OVML é o BFW | `[ovml]` | ◐ | O texto embutido é o do RF; o do BFW está em outra nota (item 5). |

**Verificações da nota:**
- Tabela de pernas: ◐ instrumentos e lados conferem com a p. 152; DNT americano vs. versão básica europeia (item 3).
- Frontmatter: ◐ `composta_de` sem `[[EU]]` (item 21).
- Omissões/contradições: ◐ a Tabela 5.1 (p. 324) não foi usada.

## KOF

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: compra de call e venda de put, as duas com KO | `[wystup-2006, p. 143]` | ✅ | "buying a long call and selling a short put with the same strike, notional and maturity we attach one or two knock-out barriers for both" |
| Strikes: o mesmo | `[wystup-2006, p. 143]` | ✅ | "same strike" |
| Vencimento: o mesmo | `[wystup-2006, p. 143]` | ✅ | "same … maturity" |
| Notional: igual | `[wystup-2006, p. 143]` | ✅ | "same … notional" |
| Barreira: uma ou duas, as mesmas nas duas pernas | `[wystup-2006, p. 143]` | ✅ | "one or two knock-out barriers for both" |
| Barreira: dentro do dinheiro | `[ovml]` | ✅ | "a knock-out barrier positioned in-the-money" |
| Composta de: KO | `[wystup-2006, p. 143]` | ✅ | Idem. |
| Restrição: tocada a barreira, o cliente fica sem hedge | `[ovml]` | ✅ | "If this triggers you are left unhedged." |
| 〃 | `[wystup-2006, p. 144]` | ✅ | "Hedge is lost in case of knock-out" |
| Restrição: custo zero | `[wystup-2006, p. 144]` | ✅ | "Zero cost product"; a definição na p. 143 também diz "at zero cost". |

**Verificações da nota:**
- Tabela de pernas: ✅.
- Frontmatter: ✅.
- Omissões/contradições: ◐ falta "No worst case scenario" (item 22).

## EF

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: forward, em geral com razão, estendido se o spot passar a barreira no vencimento | `[ovml]` | ✅ | "typically ratioed … extended for a further period if spot resets above or below a pre-specified barrier at expiry" |
| Barreira: uma, verificada no vencimento | `[ovml]` | ✅ | "a pre-specified barrier at expiry" |
| Variante de: FWD, ou PF com razão | `[ovml]` | ✅ | "(participating forward if this is the case)" |
| Notas: fonte única OVML | `[inferência: cobertura…]` | ⚖ | Defensável (o auto-renewal não é igual), mas na cobertura o EF tem "~" (item 17). |
| Notas: o auto-renewal forward é parecido, não igual | `[wystup-2006, p. 163]` | ✅ | "a series of forward contracts, which is automatically renewed"; a renovação condicionada à barreira está na p. 164 (item 23). |

**Verificações da nota:**
- Tabela de pernas: ✅.
- Frontmatter: ◐ sem `barreira`/`barreiras`/`payoff` (item 23).
- Omissões/contradições: ◐ a p. 164 não foi usada.

## FLEX

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: o cliente escolhe a data de entrega num período | `[ovml]` | ✅ | "The client must decide the delivery date" |
| 〃 | `[wystup-2006, p. 166]` | ✅ | "entitles and requires the holder to buy/sell … within a given time period" |
| Payoff: linear | `[inferência: é um forward, hull-2015, p. 7]` | ⚖ | Correta: na data escolhida, o resultado é φ(S − K), como no forward ("ST − K", p. 7). |
| Sinônimo: time option, forward de estilo americano | `[ovml]` | ◐ | Só "time-option forward contract" (item 12). |
| 〃 | `[wystup-2006, p. 166]` | ✅ | "A time option or American style forward contract" |

**Verificações da nota:**
- Tabela de pernas: ✅.
- Frontmatter: ✅.
- Omissões/contradições: ◐ exercício parcial e *shout forward* na p. 167 (item 24).

## BFF

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: o notional acumula por fixing acima/abaixo da taxa de fade | `[ovml]` | ✅ | "the amount of notional is accrued each day the fixing is above/ below the pre-defined fade rate (barrier)" |
| Composição: um valor alavancado é vendido fora do dinheiro | `[ovml]` | ◐ | É opcional: "A leveraged amount can be sold" (item 11). |
| Payoff: acumulativo | `[ovml]` | ✅ | "an accrual based forward" |
| Notas: fonte única OVML | `[inferência: cobertura…]` | ⚖ | Defensável, mas na cobertura o BFF tem "~" (item 17). |
| Notas: parecido com o fade-in forward e o boosted spot/forward | `[wystup-2006, pp. 142, 165]` | ✅ | Fade-in na p. 142; boosted: "financed by selling an option, usually an out-of-the money vanilla" (p. 165). |

**Verificações da nota:**
- Tabela de pernas: ✅.
- Frontmatter: ✅.
- Omissões/contradições: ◐ o accumulative forward (p. 156) não foi citado (item 25).

## ARC

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: como um RR, com put e call de taxa média | `[ovml]` | ✅ | "Like a risk reversal but constructed with average rate put and calls" |
| Strikes: como no RR, put abaixo da call | `[inferência: … + nota RR]` | ⚖ | Premissa confere com a nota RR (put K1 < call K2). |
| Vencimento: como no RR | `[inferência: idem]` | ⚖ | Idem. |
| Notional: como no RR | `[inferência: idem]` | ⚖ | Idem. |
| Moneyness: como no RR, as duas OTM | `[inferência: idem]` | ⚖ | Idem. |
| Composta de: AVG | `[ovml]` | ✅ | "average rate put and calls" |
| Variante de: RR | `[ovml]` | ✅ | "Like a risk reversal" |

**Verificações da nota:**
- Tabela de pernas: ✅ espelha o RR.
- Frontmatter: ✅.
- Omissões/contradições: ✅.

## ARF

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: forward com payoff igual a strike − média | `[ovml]` | ✅ | Caso "settled in the domestic currency". |
| Payoff: media | `[ovml]` | ✅ | "the average rate of the spot over an averaging period" |
| Restrição: em moeda estrangeira, usa o inverso da média, ou seja, a média harmônica | `[ovml]` | ✅ | "the inverse of the average rate of the spot and the inverse strike" |
| 〃 | `[wystup-2006, p. 131]` | ◐ | A média harmônica da eq. 1.423 é a da taxa inversa R = 1/S; sem isso, o texto sugere a média harmônica do spot (item 15). |
| Restrição: média geométrica ou moeda estrangeira exigem volatilidade | `[ovml]` | ✅ | "volatility is involved…"; "If the averaging method is Geometric, volatility is always required." |

**Verificações da nota:**
- Tabela de pernas: ✅.
- Frontmatter: ✅.
- Omissões/contradições: ✅.

## ASF

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: spot no vencimento contra strike igual à média | `[ovml]` | ✅ | "the strike which is calculated based on the average rate of the spot price" |
| Strikes: não fixo, é a média | `[ovml]` | ✅ | Idem. |
| Payoff: media | `[ovml]` | ✅ | Idem. |
| Restrição: forwards de strike flutuante na média harmônica aparecem no Wystup | `[wystup-2006, p. 132]` | ✅ | "there can be forwards and options on the harmonic average, both with fixed and floating strike"; é só uma menção, não uma restrição (item 26). |
| Restrição: notional em moeda doméstica ou média geométrica exigem volatilidade | `[ovml]` | ✅ | "If the notional is specified in the domestic currency, then volatility is required" |

**Verificações da nota:**
- Tabela de pernas: ✅ strike "—".
- Frontmatter: ✅.
- Omissões/contradições: ✅.

## ACCU

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: valor de face definido em vários fixings; cresce a cada fixing que cumpre a condição | `[ovml]` | ✅ | "the forward grows by the notional divided by the number of fixings" |
| 〃 | `[wystup-2006, p. 156]` | ✅ | "with each fixing inside such a range a pre-determined notional amount … accumulates" |
| Notional: o exibido é o máximo; notional / nº de fixings | `[ovml]` | ✅ | "The notional displayed is the maximum face value of the forward" |
| Payoff: acumulativo | `[ovml]` | ✅ | Idem. |
| Composta de: faders, possivelmente com faixas de KO | `[wystup-2006, p. 157]` | ✅ | "consists of fade-in calls and fade-in puts, possibly with extra knock-out ranges" |
| Sinônimo: accumulative forward | `[wystup-2006, p. 156]` | ◐ | A página não usa "accumulator"; a equivalência é leitura conjunta (item 13). |
| Restrição: em geral custo zero, sem pior caso garantido | `[wystup-2006, pp. 156–157]` | ✅ | "a (usually) zero cost forward enhancement without a guaranteed worst case" |

**Verificações da nota:**
- Tabela de pernas: ✅.
- Frontmatter: ✅ `composta_de: [[FA]]`.
- Omissões/contradições: ◐ a alavancagem não foi registrada ("common leverage factors are 1 and 2", p. 156).

## ACCUKI

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: só acumula depois do toque numa barreira KI americana | `[ovml]` | ✅ | "Accumulation starts only after the knockin barrier is hit" |
| Barreira: ki, uma, contínua em FX | `[ovml]` | ✅ | "the American barrier is continuous for FX" |
| Payoff: acumulativo | `[ovml]` | ✅ | "a regular accumulator" |
| Variante de: ACCU, com knock-in | `[ovml]` | ✅ | "a regular accumulator with an American knockin barrier" |

**Verificações da nota:**
- Tabela de pernas: ✅.
- Frontmatter: ✅.
- Omissões/contradições: ◐ é só OVML e não tem a nota de fonte única (item 17).

## ACCUKO

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: os fixings restantes caem no KO; o acumulado vale | `[ovml]` | ✅ | "any notional accumulated up to the knockout date is valid" |
| Barreira: ko, uma, contínua em FX | `[ovml]` | ✅ | "the American barrier is continuous for FX" |
| 〃 | `[wystup-2006, p. 157]` | ◐ | A p. 157 só implica um evento de KO intradiário; não diz "uma" nem "contínua" (item 14). |
| Payoff: acumulativo | `[ovml]` | ✅ | Idem. |
| Variante de: ACCU, com knock-out | `[ovml]` | ✅ | "a regular accumulator with an American knockout barrier" |
| Restrição: o fixing do dia conta se vier antes do KO | `[wystup-2006, p. 157]` | ◐ | É o padrão, não regra: "The standard is that it does if the fixing is before the knock-out event" (item 14). |

**Verificações da nota:**
- Tabela de pernas: ✅.
- Frontmatter: ✅.
- Omissões/contradições: ◐ o Wystup trata "keep all" e "keep nothing" como produtos diferentes (p. 156); o ACCUKO da Bloomberg é o "keep all".
