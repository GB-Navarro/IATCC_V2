# Validação do Claude — lote 2

Validador: agente independente · 2026-10-22 · cada citação conferida na página impressa inteira (texto via PyMuPDF; hull-2015 p. 7 também por imagem) e no OVML, com busca de evidência contrária em hull-2015 e wystup-2006.

## Resumo

| ✅ | ◐ | ✗ | ⚖ | ? | total |
|---|---|---|---|---|---|
| 20 | 7 | 0 | 2 | 0 | 29 |

## Status das correções (aplicadas pelo Claude principal, 2026-10-22)

Os vereditos abaixo valem para as notas **antes** das correções.

| Status | Itens |
|---|---|
| ✎ aplicada | 1–10, 14 |
| ✎ decidida pelo usuário | 11–13 (D36, D37) |

## Correções propostas

Prioridade 1: nenhuma.

Prioridade 2

1. **FWD** · A restrição "Não custa nada para entrar" vale só para o forward a mercado. O próprio Hull diz que, na entrada, "the delivery price, K, is set equal to the forward price at that time and the value of the contract, f, is 0", com f = (F0 − K)e^(−rT) (hull-2015, pp. 112–113). O Wystup diz que o outright forward é "usually zero cost" e que o forward com taxa fora da forward de mercado gera prêmio (wystup-2006, p. 140). Já o OVML deixa a taxa do contrato livre. · Trocar a linha por: "Custo zero na entrada quando a taxa do contrato é a forward de mercado [hull-2015, pp. 112–113]; [wystup-2006, p. 140]; com outra taxa, há prêmio [wystup-2006, p. 140]."
2. **FWD** · Em "O resultado descrito pela Bloomberg é o do comprador [ovml]", o OVML diz só "the trade will make (lose) money" e não fala em comprador. · Trocar `[ovml]` por `[inferência: o OVML descreve lucro quando a taxa do contrato é menor que a taxa do dia [ovml]; esse é o payoff ST − K da posição comprada [hull-2015, p. 7]]`.
3. **FX** · Na origem, "Payoff: linear: o comprador ganha… [ovml]": o OVML dá só a condição de lucro; não diz "linear" nem "comprador". · Manter `[ovml]` e acrescentar `[inferência: o spot é o mesmo acordo de compra e venda do forward, só que com entrega quase imediata [hull-2015, p. 6]; o payoff do forward comprado é ST − K, linear [hull-2015, p. 7]]`.
4. **FX** · Em Restrições, a inferência `[inferência: como no forward, hull-2015, p. 7]` deixa sem citação a premissa de que o spot equivale a um forward (ela está em hull-2015, p. 6). Além disso, o `[ovml]` não identifica o comprador. · Trocar as duas citações por `[inferência: o OVML descreve lucro quando a taxa do contrato é menor que a taxa do dia [ovml]; spot e forward diferem só na data de entrega [hull-2015, p. 6]; no forward, esse é o payoff ST − K da posição comprada, e a vendida recebe K − ST [hull-2015, p. 7]]`.

Prioridade 3

5. **FX, FWD** · Algumas linhas juntam `[ovml]` e `[hull-2015, p. 6]` numa afirmação composta. O OVML sustenta só "data spot" e "data de entrega especificada"; "quase imediata" e "futura" vêm do Hull. · Pôr cada citação junto da sua parte: FX Vencimento "data spot [ovml]: entrega quase imediata [hull-2015, p. 6]"; FWD Composição e Vencimento "numa data futura [hull-2015, p. 6], a data de entrega especificada [ovml]".
6. **FX, FWD** · Em FX, "comprador" é ambíguo, porque toda troca compra uma moeda e vende a outra. · Escrever "comprador da moeda do notional". O OVML fala em "exchange the specified notional amount of currency", e no Hull a posição comprada compra o ativo, a libra (hull-2015, p. 7).
7. **FX, FWD** · As restrições repetem a tabela de origem: o vendedor oposto já está no Payoff do FWD ("K − ST na vendida"), e o ponto de vista do comprador já está no Payoff do FX. O schema põe em Restrições só o que as tabelas não expressam. · Juntar tudo na linha Payoff e apagar a restrição repetida.
8. **EU, AM** · Há evidência direta de FX que não foi usada. Wystup diz que "Most commonly, vanilla options on foreign exchange are of European style, i.e. the holder can only exercise the option at time T" (wystup-2006, p. 3) e que as American style options "are not used very often except for time options" (wystup-2006, pp. 3–4). · Acrescentar `[wystup-2006, p. 3]` ao Instrumento do EU e `[wystup-2006, pp. 3–4]` ao do AM. Avaliar no AM a restrição "pouco usada em FX, exceto em time options [wystup-2006, pp. 3–4]", que ajuda a ranquear candidatas.
9. **FWD** · Evidência de FX não usada: o outright forward como "zero cost strategy to fix the exchange rate at a future date", com payoff ST − f (wystup-2006, p. 139). · Acrescentar `[wystup-2006, p. 139]` em Composição e Payoff.
10. **FX** · O Vencimento ficaria mais preciso com o prazo do spot: a "spot value date, which is by default two business days after the trade date" (wystup-2006, p. 135). · Acrescentar em Vencimento "por padrão, 2 dias úteis após a negociação [wystup-2006, p. 135]".
11. **CASH** · O OVML cobre pagar e receber, e não há versão "long". A tabela tem lado +, mas não diz qual dos dois mostra. · Decisão do usuário: em Composição, acrescentar "a tabela mostra o recebimento", como o EU faz com "a tabela mostra a call".
12. **CASH** · A linha "Fonte única…" está em Notas, mas o schema reserva Notas a divergências e conflitos de nome. O mesmo padrão aparece em BFF, DACCR, EF, FP, KKF e TF. · Decisão do usuário: ajustar o schema ou mudar a linha de seção.
13. **AM** · `variante_de` está vazio, embora o AM só difira do EU pelo estilo de exercício: "Options can be either American or European" (hull-2015, p. 213). · Decisão do usuário: `variante_de: [[EU]]` ou deixar como está.
14. **fontes/README.md** (fora do lote) · Na cobertura de FX e FWD, a "wystup-2006 p. 141" é o participating forward; o outright forward está nas pp. 139–140. A "hull-2015 p. 104" é só a abertura do cap. 5; a definição está nas pp. 6–7 e o valor na entrada, nas pp. 112–113. · Corrigir as páginas.

## EU

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: uma call ou uma put; a tabela mostra a call | `[ovml]` | ✅ | "A European Vanilla Call (Put) gives the right but not the obligation…". "A tabela mostra a call" é convenção da nota; a put é o espelho do schema. |
| Instrumento: opção europeia: exercício só no vencimento | `[ovml]` | ✅ | "…at the specified strike price on the expiry date." |
| 〃 | `[hull-2015, p. 9]` | ✅ | "European options can be exercised only on the expiration date itself." (PDF 32) |
| Payoff: vanilla: exercida com lucro se o spot no vencimento estiver acima (call) ou abaixo (put) do strike | `[ovml]` | ✅ | "if the spot rate on the expiry date is greater (less) than the strike, the option will be exercised at a profit" |

**Verificações da nota:**
- Tabela de pernas: ✅ EU · call · K1 · T1 · 1 · + · —. A versão long é a compra da call ("gives the right").
- Frontmatter: ✅ `payoff: vanilla`; sem barreira; relações vazias.
- Omissões/contradições: ◐ falta a evidência de FX de wystup-2006, p. 3: estilo europeu e payoff [φ(ST − K)]+. Sem contradição.

## AM

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: uma call ou uma put; a tabela mostra a call | `[ovml]` | ✅ | "An American Vanilla Call (Put) gives the right but not the obligation…" |
| Instrumento: opção americana: exercício a qualquer momento até o vencimento | `[ovml]` | ✅ | "…at any point during the lifetime of the option." |
| 〃 | `[hull-2015, p. 9]` | ✅ | "American options can be exercised at any time up to the expiration date." (PDF 32) |
| Payoff: vanilla | `[ovml]` | ✅ | "An American Vanilla Call (Put)…" |

**Verificações da nota:**
- Tabela de pernas: ✅ AM · call · K1 · T1 · 1 · + · —.
- Frontmatter: ✅ `payoff: vanilla`; sem barreira. `variante_de` vazio: ver item 13.
- Omissões/contradições: ◐ falta wystup-2006, pp. 3–4: o estilo americano é raro em FX, salvo em time options. Sem contradição.

## FX

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: contrato de troca de moedas na data spot | `[ovml]` | ✅ | "A contract to exchange the specified notional amount of currency on the specified spot delivery date." |
| 〃 | `[hull-2015, p. 6]` | ✅ | "a spot contract, which is an agreement to buy or sell an asset almost immediately"; o exemplo de GBP na mesma página traz o spot de moedas. |
| Strikes: a taxa do contrato (K1) | `[ovml]` | ✅ | "if the contract rate is lower (greater) than the FX rate for that day" |
| Vencimento: data spot: entrega quase imediata | `[ovml]` | ◐ | O OVML dá só "spot delivery date"; "quase imediata" não está nele. |
| 〃 | `[hull-2015, p. 6]` | ✅ | "in the spot market (i.e., for virtually immediate delivery)" |
| Payoff: linear: o comprador ganha se a taxa do contrato for menor que a taxa do dia | `[ovml]` | ◐ | "the trade will make (lose) money": não diz "linear" nem "comprador". |
| Restrição: o resultado descrito é o do comprador; o vendedor tem o resultado oposto | `[ovml]` | ◐ | O mesmo trecho não identifica o comprador nem fala do vendedor; serve só de premissa. |
| 〃 | `[inferência: como no forward, hull-2015, p. 7]` | ⚖ | A conclusão é correta (p. 7: long ST − K, short K − ST), mas falta citar a premissa "spot ≈ forward com entrega imediata" (hull-2015, p. 6), e as premissas não estão explícitas. |

**Verificações da nota:**
- Tabela de pernas: ✅ FX · — · K1 · T1 · 1 · + · —. O lado + é o comprador da moeda do notional, coerente com o lucro quando a taxa do contrato é menor que a do dia.
- Frontmatter: ◐ `payoff: linear` bate com a origem, mas "linear" está sem fonte (item 3).
- Omissões/contradições: ◐ falta precisão no prazo do spot, de 2 dias úteis (wystup-2006, p. 135). Sem contradição.

## FWD

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: contrato de troca de moedas numa data futura | `[ovml]` | ◐ | "…exchange the specified notional amount of currency on the specified delivery date": não diz "futura", que vem do Hull. |
| 〃 | `[hull-2015, p. 6]` | ✅ | "an agreement to buy or sell an asset at a certain future time for a certain price"; "Forward contracts on foreign exchange are very popular." |
| Strikes: a taxa do contrato (K1), o preço de entrega | `[ovml]` | ✅ | "contract rate" |
| 〃 | `[hull-2015, p. 7]` | ✅ | "where K is the delivery price" |
| Vencimento: data de entrega futura | `[ovml]` | ◐ | "specified delivery date", sem "futura". |
| 〃 | `[hull-2015, p. 6]` | ✅ | "on a certain specified future date" |
| Payoff: linear: ST − K na posição comprada, K − ST na vendida | `[hull-2015, p. 7]` | ✅ | "the payoff from a long position … is ST − K" e "from a short position … is K − ST"; a Figura 1.2 mostra retas (conferido na imagem). |
| Restrição: não custa nada para entrar | `[hull-2015, p. 7]` | ◐ | A página diz "it costs nothing to enter into a forward contract", mas o próprio Hull só dá valor zero quando K é a forward de mercado (pp. 112–113), e o OVML deixa a taxa livre. Escopo mais amplo que a fonte (item 1). |
| Restrição: o resultado descrito pela Bloomberg é o do comprador; a posição vendida tem o resultado oposto | `[ovml]` (parte do comprador) | ◐ | O OVML diz "the trade will make (lose) money"; "comprador" é leitura via Hull, não está no texto. |
| 〃 | `[hull-2015, p. 7]` (parte da vendida) | ✅ | "the payoff from a short position in a forward contract on one unit of an asset is K − ST" |

**Verificações da nota:**
- Tabela de pernas: ✅ FWD · — · K1 · T1 · 1 · + · —.
- Frontmatter: ✅ `payoff: linear` (hull-2015, p. 7, Figura 1.2).
- Omissões/contradições: ◐ o "não custa nada" é contradito em escopo por hull-2015, pp. 112–113 e wystup-2006, p. 140 (item 1). Falta wystup-2006, p. 139. A restrição repete o Payoff (item 7).

## CASH

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: pagamento ou recebimento de um valor em dinheiro | `[ovml]` | ✅ | "A contract to either pay another party cash or receive cash from another party…" |
| Vencimento: a data de entrega especificada | `[ovml]` | ✅ | "…on the specified delivery date." |
| Notas: fonte única para a definição é o OVML; nenhuma fonte de `fontes/` define a estrutura | `[inferência: cobertura por estrutura em fontes/README.md]` | ⚖ | A premissa é verdadeira: a linha "SDR, CASH, FP, BFW, TF" está marcada "—". Uma busca contrária no índice e no glossário do Hull e no Wystup só achou "cash settlement" e cash-or-nothing, que são outra coisa. A conclusão se sustenta. |

**Verificações da nota:**
- Tabela de pernas: ◐ CASH · — · — · T1 · 1 · + · —. O lado + não diz se a tabela mostra o pagamento ou o recebimento (item 11).
- Frontmatter: ✅ sem `payoff`: nenhum valor do vocabulário serve a um fluxo fixo. Sem barreira.
- Omissões/contradições: ◐ a linha "Fonte única" está em Notas, fora do uso que o schema dá a Notas (item 12).
