# Validação do Claude — lote 1

Validador: agente independente · 2026-10-22 · cada página citada lida inteira (texto via PyMuPDF; Natenberg e figuras do Wystup pela imagem), OVML conferido no arquivo da Bloomberg, mais busca de evidência contrária em outras seções das fontes.

## Resumo
| ✅ | ◐ | ✗ | ⚖ | ? | total |
|---|---|---|---|---|---|
| 124 | 21 | 1 | 9 | 0 | 155 |

Nenhuma página está errada e nenhum marcador `exemplo` está trocado. Todas as citações literais conferem com a fonte. Os problemas são de escopo: citações que sustentam só parte da afirmação.

## Status das correções (aplicadas pelo Claude principal, 2026-10-22)

Os vereditos abaixo valem para as notas **antes** das correções.

| Status | Itens |
|---|---|
| ✎ aplicada | 1–4, 6–22, 23 (`variante_de: [[BF]]` no CR) |
| ✎ aplicada com ajuste | 5: a Fig. 1.5 (p. 22) foi para as Notas do BF, não para a linha Composição, porque mostra o formato do payoff e não a composição. 22: o espaçamento igual das pontas do CR ficou como inferência, porque o Natenberg o implica sem dizê-lo. |
| ⏸ decisão do usuário | 24 (`variante_de` do PF), 25 (aliases) |
| — não aplicada | a tensão entre a tabela de pernas e a restrição do DS fica registrada na própria restrição; resolvê-la depende da ampliação do schema (decisão aberta na Fase A) |

O ✗ do item 1 revelou um erro de padrão: a frase "Fonte única: OVML [ovml]" também aparecia em BFF, CASH, DACCR, EF, FP, KKF e TF. Essas notas foram corrigidas, e a citação passou a ser `[inferência: cobertura por estrutura em fontes/README.md]`. A convenção "combinações de vanillas usam opções europeias" foi registrada no `_schema.md` (itens 18–20).

## Correções propostas

**Prioridade 1**

1. **SDR · Notas:** `[ovml]` não sustenta "nenhuma fonte de `fontes/README.md` trata a estrutura". Trocar por `[inferência: busca por "ratio straddle" sem resultado em hull-2015, wystup-2006, haug-2007, reiswich-wystup-2009 e wystup-fxcol-2022; natenberg-1994 não pesquisável por texto]`, ou remover a linha, que não é divergência da Bloomberg.
2. **DS · Composição (2ª linha):** trocar `[inferência: segue o calendar spread, …]` por `[hull-2015, p. 272]`. O Problema 12.23 diz: "buying a call with strike price K2 and exercise date T2 and selling a call with strike price K1 and exercise date T1, where T2 > T1".
3. **DS · Restrição:** trocar `[inferência: hull-2015, p. 266 não fixa a ordem]` por `[hull-2015, p. 272]`. O mesmo problema pede os casos "(a) K2 > K1 and (b) K2 < K1".
4. **CR · Strikes (1ª linha):** o OVML só diz que o intervalo do strangle vendido é menor, não que ele fica dentro do comprado. Reescrever como "quatro; o intervalo do strangle vendido (K2–K3) é menor que o do comprado (K1–K4) [ovml]; os vendidos ficam entre os comprados [natenberg-1994, p. 158]", com base em "the two outside options are purchased and the two inside options sold".
5. **BF · Notas (Wystup):** a nota subestima o conflito. Além do exemplo da p. 37, o resto da p. 36 também descreve a posição oposta ("The holder has to pay a premium", "Maximum loss is the premium paid"), e o mesmo vale para a Fig. 1.15. Já a Fig. 1.5 da p. 22 mostra o butterfly com payoff em tenda, coerente com o OVML. Reescrever: "a definição (p. 36, 1ª frase) e a Fig. 1.5 (p. 22) coincidem com o OVML; o resto da seção (pp. 36–37) descreve a posição oposta". Acrescentar `[wystup-2006, p. 22]` à linha Composição.
6. **RR · Restrição de volatilidade:** trocar por "o RR de delta 0,25 (o mais cotado; outros deltas também são cotados)" e acrescentar `[wystup-2006, p. 22]` ("Other or additional implied volatilities for other deltas such as φ10 % and φ35 % are also quoted"). Na nota 1 da p. 12, o Reiswich diz que 0,25 é só um exemplo.
7. **SN · Restrição:** aplicar o mesmo ajuste: "o strangle de referência de delta 0,25 (o mais cotado)", com `[wystup-2006, p. 22]`.
8. **RR · Notas:** trocar `[wystup-2006, p. 151]` por `[wystup-2006, pp. 151–152]`, porque a composição (forward sintético + DNT) está na p. 152. O vínculo com o RF do OVML vem do texto da Bloomberg para o RF, não do Wystup. Atenção: o Wystup diz "range or bonus forward", e o OVML tem um BFW separado.
9. **DS · Notional:** trocar "igual no caso mais comum" por "igual em muitos casos (um para um)". O Natenberg diz "many diagonal spreads are executed one-to-one", não "the most common".

**Prioridade 2: `[ovml]` preso a uma parte que o OVML não diz (dividir a citação)**

10. **CP · Strikes:** "diferentes [ovml]; a call comprada tem o strike mais baixo [hull-2015, p. 258]".
11. **SN · Strikes:** "diferentes [ovml]; call acima da put [hull-2015, p. 269]".
12. **CS · Sinônimo:** "horizontal spread [ovml]; time spread [natenberg-1994, p. 148]".
13. **CS · Moneyness:** tirar `[ovml]` ou restringi-lo a "a visão neutra é a usual". O OVML não fala do strike.
14. **PF · Notional:** "diferente [ovml]; o da put é menor (baixo risco) ou maior (alto risco, ex.: o dobro) [wystup-2006, p. 141]".
15. **BFC · Composição:** "compra de K1 e K3, venda de K2, só calls ou só puts [ovml]; duas opções em K2 [hull-2015, p. 264]".
16. **SG · Moneyness (put e call vendidas):** tirar `[ovml]` de "OTM", porque o OVML só diz "sale of a strangle". O OTM fica com `[wystup-2006, p. 35]`.
17. **SG · Restrição:** trocar "custo zero" por "custo baixo ou zero", como em PF. O OVML diz "low (or zero) cost position".

**Prioridade 3: consistência e decisões do usuário**

18. **SG, BF · Instrumento:** `[wystup-2006, pp. 29, 39]` é uma inferência, porque nenhuma das duas páginas diz que essas estruturas usam opções europeias. Usar o formato de SDR/PF/CR: `[inferência: estratégias com vanillas, wystup-2006, p. 29; vanilla = europeia, p. 39]`.
19. **SDR, PF, CR · Instrumento:** nessas inferências, a premissa "combinação de vanillas" não tem citação, o OVML não diz "europeia" e a Bloomberg tem AM. É aceitável como convenção, mas convém declarar a decisão.
20. **DS · Instrumento:** em `[hull-2015, pp. 265–266]`, o parágrafo sobre o diagonal não diz "European". A informação vem só do contexto do calendar spread (p. 265).
21. **SD · Moneyness:** `[reiswich-wystup-2009, p. 9]` define o ATM a partir do straddle, não diz que o straddle é ATM. Reforçar com uma inferência baseada no OVML do SDR: "Unlike a Straddle, the strike of the Ratio Straddle is usually Out-of-The-Money".
22. **CR · Strikes "consecutivos":** reescrever como "pontas igualmente espaçadas (K2 − K1 = K4 − K3)" `[natenberg-1994, p. 158]`. A fonte implica isso ao dizer que o condor "will be worthless whenever the underlying contract is outside the extreme exercise prices". "Consecutivos" é uma noção de strikes listados em bolsa.
23. **CR · frontmatter:** avaliar `variante_de: [[BF]]`, com base em "Another variation on a butterfly, known as a condor" (Natenberg, p. 158).
24. **PF · `variante_de`:** a primeira comparação do Wystup na p. 141 é com o forward sintético ("like a synthetic forward … except that the notionals are different"), que corresponde à forma do OVML com o mesmo strike. O RR exige strikes diferentes. Decisão do usuário.
25. **Aliases (opcional):** RR "Collar" como alias próprio (a tabela já tem Sinônimo); SN "Bottom Vertical Combination" (Hull, p. 269); PF "Leveraged Forward", só para o estilo de alto risco (Wystup, p. 142).

## CP
| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: compra de uma call e venda de outra | `[ovml]` | ✅ | "buying and selling calls or puts with different strikes" |
| 〃 | `[hull-2015, p. 258]` | ✅ | "buying a European call option … and selling a European call option on the same stock with a higher strike price" |
| 〃 | `[wystup-2006, p. 30]` | ✅ | "A Call spread is a combination of a long and a short Call option." |
| Strikes: diferentes; a comprada tem o mais baixo | `[ovml]` | ◐ | Só "different strikes"; não diz qual perna tem o strike mais baixo |
| 〃 | `[hull-2015, p. 258]` | ✅ | "… selling a European call option … with a higher strike price" |
| Vencimento: o mesmo | `[hull-2015, p. 258]` | ✅ | "Both options have the same expiration date." |
| Notional: uma de cada lado | `[hull-2015, p. 258]` | ✅ | A definição compra "a European call" e vende "a European call" |
| 〃 | `[wystup-2006, p. 31, exemplo]` | ✅ | Tab. 1.11: "Notional of both the Call option EUR 1,000,000"; marcador correto |
| Moneyness: livre | `[hull-2015, p. 259]` | ✅ | Três tipos, de "Both calls are initially out of the money" a "Both calls are initially in the money" |
| Instrumento: europeias | `[hull-2015, p. 258]` | ✅ | "buying a European call option" |
| Restr.: put spread e bear = mesma estrutura | `[inferência: …]` | ⚖ | Válida: short do bull call = bear call (p. 261); espelho = bear put (p. 260); short do espelho = bull put (p. 259) |
| Notas: Bloomberg não exige mesmo vencimento | `[ovml]` | ✅ | O texto do OVML não menciona vencimento |
| Notas: citação do Hull | `[hull-2015, p. 258]` | ✅ | Citação literal idêntica |

**Verificações da nota:**
- Tabela de pernas ✅: +C K1 e −C K2, mesmo T1, 1:1, moneyness livre; confere com Hull, pp. 258–259.
- Frontmatter ✅: sem relações; coerente.
- Omissões/contradições ✅: nenhuma. O OVML não define o lado "long"; a nota usa o bull spread do Hull, coerente com a regra de short.

## RR
| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: compra de call, venda de put | `[ovml]` | ✅ | "purchasing an out-of-the-money call and selling an out-of-the-money put" |
| 〃 | `[wystup-2006, p. 31]` | ✅ | "A Risk Reversal is a combination of a long call and a short put." |
| 〃 | `[hull-2015, p. 371]` | ✅ | "sell a European put option with strike price K1 and buy a European call option with strike price K2" (o Hull chama de range forward) |
| Strikes: put abaixo da call | `[ovml]` | ✅ | Não diz isso de forma explícita, mas decorre de "different strikes" com as duas pernas OTM |
| 〃 | `[hull-2015, pp. 370–371]` | ✅ | "K1 < 1.5200 < K2", com a put em K1 e a call em K2 |
| Vencimento: o mesmo | `[ovml]` | ✅ | "for the same expiration date" |
| Notional: igual | `[ovml]` | ✅ | "same expiration date and notional amount" |
| 〃 | `[wystup-2006, p. 32, exemplo]` | ✅ | Tab. 1.12: um único notional, "EUR 1,000,000" |
| 〃 | `[hull-2015, p. 370, exemplo]` | ✅ | "In both cases, the options are on one million pounds." |
| Moneyness: as duas OTM | `[ovml]` | ✅ | "out-of-the-money call … out-of-the-money put" |
| Instrumento: europeias | `[hull-2015, p. 370]` | ✅ | "buy a European put option … and sell a European call option" |
| Sinônimo: collar | `[ovml]` | ✅ | Pelo nome do produto, "Risk Reversal (Collar)"; o corpo do texto não usa "collar" |
| 〃 | `[wystup-2006, p. 31]` | ✅ | "the Risk Reversal or collar" |
| Restr.: custo zero | `[wystup-2006, p. 31]` | ✅ | "the buyer can sell another option to finance the purchase of the call"; "Zero cost product" |
| 〃 | `[hull-2015, p. 371]` | ✅ | "set up so that the price of the put option equals the price of the call option" |
| Restr.: RR cotado com deltas 0,25 e −0,25 | `[reiswich-wystup-2009, p. 13]` | ◐ | A página define σ25−RR, mas a nota 1 (p. 12) diz: "We will take a delta of 0.25 as an example, although any choice is possible"; a afirmação generaliza o exemplo |
| Notas: o Hull chama de range forward (citação) | `[hull-2015, p. 371]` | ✅ | Citação literal idêntica |
| Notas: o RF do OVML é outra estrutura | `[wystup-2006, p. 151]` | ◐ | A p. 151 define o range forward pelo pior e melhor caso; a composição (forward sintético + DNT) está na p. 152; o vínculo com o RF do OVML não está no Wystup |

**Verificações da nota:**
- Tabela de pernas ✅: −P K1 OTM e +C K2 OTM, T1, 1:1.
- Frontmatter ◐: `aliases` não traz "Collar" como alias próprio, embora a tabela de origem tenha a linha Sinônimo (em CS, os sinônimos estão em `aliases`).
- Omissões/contradições ◐: o Wystup (p. 22) diz que volatilidades de delta 0,10 e 0,35 também são cotadas, o que relativiza a restrição de 25 delta.

## SD
| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: compra de call e put | `[ovml]` | ✅ | "simultaneously purchasing a call and put option" |
| 〃 | `[hull-2015, p. 267]` | ✅ | "buying a European call and put with the same strike price and expiration date" |
| 〃 | `[wystup-2006, p. 33]` | ✅ | "a combination of a put and a call option with the same strike"; "Buying a straddle" |
| Strikes: o mesmo | `[ovml]` | ✅ | "with the same strike price" |
| 〃 | `[hull-2015, p. 267]` | ✅ | Idem |
| 〃 | `[wystup-2006, p. 33]` | ✅ | "with the same strike" |
| Vencimento: o mesmo | `[ovml]` | ✅ | "and expiry date" |
| 〃 | `[hull-2015, p. 267]` | ✅ | "and expiration date" |
| Notional: igual | `[wystup-2006, p. 35, exemplo]` | ✅ | Tab. 1.14: "Notional of both the options EUR 1,000,000" |
| Moneyness: ATM | `[wystup-2006, p. 35, exemplo]` | ✅ | Strike 1,1500 igual ao spot de referência 1,1500 |
| 〃 | `[reiswich-wystup-2009, p. 9]` | ◐ | A página define o ATM delta-neutro a partir do straddle ("a straddle with this strike has a zero spot exposure"); não diz que o straddle é ATM |
| Instrumento: europeias | `[hull-2015, p. 267]` | ✅ | "buying a European call and put" |
| Variante de SN | `[inferência: hull-2015, pp. 267, 269]` | ⚖ | Válida: as definições só diferem em strike igual vs. diferente; o próprio `_schema` usa SD → SN como exemplo |
| Restr.: ATM padrão é o delta-neutro | `[reiswich-wystup-2009, p. 9]` | ✅ | "This ATM convention is considered as the default ATM notion for short-dated FX options." |

**Verificações da nota:**
- Tabela de pernas ✅: +P K1 e +C K1, ATM, 1:1.
- Frontmatter ✅: `variante_de: [[SN]]`.
- Omissões/contradições ◐: nenhuma definição (OVML do SD, Hull p. 267, Wystup p. 33) exige ATM. O melhor apoio é o OVML do SDR ("Unlike a Straddle, the strike of the Ratio Straddle is usually Out-of-The-Money"), que não é citado. O Wystup (p. 22) usa outra convenção de ATM (strike = forward), o que não contradiz a restrição.

## SN
| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: compra de put e call | `[ovml]` | ✅ | "simultaneously purchasing a call and put option" |
| 〃 | `[hull-2015, p. 269]` | ✅ | "an investor buys a European put and a European call" |
| 〃 | `[wystup-2006, p. 35]` | ✅ | "a combination of an out-of-the-money put and call option"; "Buying a strangle" |
| Strikes: call acima da put | `[ovml]` | ◐ | Só "differing strike prices"; nem a ordem nem o OTM decorrem do texto |
| 〃 | `[hull-2015, p. 269]` | ✅ | "The call strike price, K2, is higher than the put strike price, K1." |
| Vencimento: o mesmo | `[ovml]` | ✅ | "but the same expiry date" |
| 〃 | `[hull-2015, p. 269]` | ✅ | "with the same expiration date" |
| Notional: igual | `[wystup-2006, p. 36, exemplo]` | ✅ | Tab. 1.15: "Notional of both the options EUR 1,000,000" |
| Moneyness: as duas OTM | `[wystup-2006, p. 35]` | ✅ | "an out-of-the-money put and call option" |
| Instrumento: europeias | `[hull-2015, p. 269]` | ✅ | "a European put and a European call" |
| Restr.: strangle de referência com deltas 0,25 e −0,25 | `[reiswich-wystup-2009, p. 15]` | ◐ | Sustenta o market strangle de 25 delta (deltas medidos com a vol σ25−S−M), mas 0,25 é só um exemplo (nota 1, p. 12) |

**Verificações da nota:**
- Tabela de pernas ✅: +P K1 OTM e +C K2 OTM, 1:1.
- Frontmatter ✅.
- Omissões/contradições ◐: o Hull (p. 269) dá o sinônimo "bottom vertical combination", ausente de `aliases`. O OTM vem só do Wystup; nem o OVML nem o Hull o exigem.

## SDR
| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: compra de call e put | `[ovml]` | ✅ | "simultaneously purchasing a call and put" |
| Strikes: o mesmo | `[ovml]` | ✅ | "with the same strike price" |
| Vencimento: o mesmo | `[ovml]` | ✅ | "and expiry date" |
| Notional: razão r | `[ovml]` | ✅ | "the notional on each leg is not the same" |
| Moneyness: geralmente OTM | `[ovml]` | ✅ | "the strike of the Ratio Straddle is usually Out-of-The-Money (OTM)" |
| Instrumento: europeias | `[inferência: … wystup-2006, p. 39]` | ⚖ | Fraca: a premissa do Wystup confere ("vanilla (European style put and call) options"), mas "combinação de vanillas" não tem citação, o OVML não diz "europeia" e a Bloomberg tem AM; é uma convenção, não uma conclusão |
| Variante de SD | `[ovml]` | ✅ | "Unlike a Straddle, the strike … is usually … OTM and the notional on each leg is not the same" |
| Restr.: delta forward zero | `[ovml]` | ✅ | "to create the OTM structure with a zero forward delta exposure" |
| Notas: nenhuma outra fonte trata a estrutura | `[ovml]` | ✗ | O OVML não diz nada sobre outras fontes. A afirmação é verdadeira por busca de texto (nenhuma ocorrência de "ratio straddle"), menos no Natenberg, escaneado |

**Verificações da nota:**
- Tabela de pernas ✅: mesmo K1, +P r e +C 1. A moneyness "—" está correta: com um único strike, uma perna fica ITM e a outra OTM.
- Frontmatter ✅: `variante_de: [[SD]]`.
- Omissões/contradições ✅: nenhuma.

## PF
| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: compra de call, venda de put | `[ovml]` | ✅ | "purchasing a call (put) option and selling a put (call)" |
| 〃 | `[wystup-2006, p. 141]` | ✅ | "at a pre-determined rate (long strike) … below the strike of the short put" |
| Strikes: o mesmo (Bloomberg) | `[ovml]` | ✅ | "for the same expiration date and strike" |
| Vencimento: o mesmo | `[ovml]` | ✅ | Idem |
| Notional: put menor ou maior (ex.: o dobro) | `[ovml]` | ◐ | Só "with differing notional amounts" |
| 〃 | `[wystup-2006, p. 141]` | ✅ | "In the low risk style, the notional of the sold put is smaller … say by a factor of 2" |
| Instrumento: europeias | `[inferência: … wystup-2006, p. 39]` | ⚖ | Fraca, pelo mesmo motivo do SDR |
| Flexível: strike | `[wystup-2006, p. 141]` | ✅ | "In a more general manner, the strikes can also be different." |
| 〃 | `[wystup-2006, p. 142, exemplo]` | ✅ | Tab. 2.1: call em 1,2000 e put em 1,1475 |
| Variante de RR | `[wystup-2006, p. 141]` | ✅ | "It is also very similar to a risk reversal." (ver verificação do frontmatter) |
| Restr.: custo baixo ou zero | `[ovml]` | ✅ | "a low (or zero) cost position" |
| 〃 | `[wystup-2006, p. 141]` | ✅ | "Zero cost product" |
| Notas: a Bloomberg exige o mesmo strike | `[ovml]` | ✅ | "same expiration date and strike" |
| Notas: citação do Wystup | `[wystup-2006, p. 141]` | ✅ | Citação literal idêntica |

**Verificações da nota:**
- Tabela de pernas ✅: mesmo K1, −P r e +C 1, como no OVML.
- Frontmatter ⚖: `flexivel: [strike]` está sustentado. `variante_de: [[RR]]` é defensável, mas a primeira comparação da p. 141 é com o forward sintético ("like a synthetic forward … except that the notionals are different"), que corresponde à forma do OVML com o mesmo strike.
- Omissões/contradições ◐: o Wystup (p. 142) dá o sinônimo "leveraged forward" para o estilo de alto risco.

## CS
| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: vende a curta, compra a longa, mesmo tipo | `[ovml]` | ✅ | "selling a short-term option and buying a long-term option of the same type" |
| 〃 | `[hull-2015, p. 265]` | ✅ | "selling a European call option … and buying a longer-maturity European call option with the same strike price" |
| 〃 | `[natenberg-1994, p. 148]` | ◐ | O lado está definido ("When the long-term option is purchased and the short-term option is sold, a trader is long the time spread"), mas o mesmo tipo aparece só como "the most common type" |
| Strikes: o mesmo | `[ovml]` | ✅ | "with the same strike prices" |
| 〃 | `[hull-2015, p. 265]` | ✅ | "with the same strike price" |
| 〃 | `[natenberg-1994, p. 148]` | ◐ | "The most common type of time spread … where both options have the same exercise price": é o caso mais comum, não uma exigência |
| Vencimento: T1 < T2 | `[ovml]` | ✅ | "short-term option … long-term option" |
| 〃 | `[hull-2015, p. 265]` | ✅ | "longer-maturity" |
| Notional: uma de cada lado | `[hull-2015, p. 265]` | ✅ | Uma call vendida e uma call comprada |
| 〃 | `[natenberg-1994, p. 148]` | ✅ | "opposing positions in two options" |
| Moneyness: livre conforme a visão | `[hull-2015, p. 266]` | ✅ | "A bullish calendar spread involves a higher strike price, whereas a bearish … a lower strike price." |
| 〃 | `[ovml]` | ◐ | Só "usually used with a neutral market outlook"; nada sobre o strike |
| Instrumento: europeias | `[hull-2015, p. 265]` | ✅ | "selling a European call option" |
| Sinônimo: horizontal; time spread | `[ovml]` | ◐ | Só "also known as a Horizontal Spread" |
| 〃 | `[natenberg-1994, p. 148]` | ✅ | "TIME SPREAD (also referred to as a calendar spread or horizontal spread)" |

**Verificações da nota:**
- Tabela de pernas ✅: −C K1 T1 e +C K1 T2.
- Frontmatter ✅.
- Omissões/contradições ✅: o "reverse calendar spread" (Hull, p. 266) é o short, coberto pela regra de short.

## DS
| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: uma comprada, outra vendida, mesmo tipo | `[ovml]` | ✅ | "going long and short an option of the same type" |
| 〃 | `[hull-2015, p. 266]` | ✅ | "a long position in one call and a short position in another call … both the expiration date and the strike price of the calls are different" |
| Composição: vende a curta, compra a longa | `[inferência: …]` | ⚖ | A conclusão é correta e tem apoio direto não citado: Hull, p. 272 (Probl. 12.23), "selling a call with strike price K1 and exercise date T1, where T2 > T1" |
| Strikes: diferentes | `[hull-2015, p. 266]` | ✅ | "the strike price of the calls are different" |
| 〃 | `[natenberg-1994, p. 157]` | ✅ | "except that the options have different exercise prices" |
| Vencimento: diferentes | `[hull-2015, p. 266]` | ✅ | "both the expiration date and the strike price … are different" |
| Notional: igual no caso mais comum | `[natenberg-1994, p. 157]` | ◐ | "many diagonal spreads are executed one-to-one": diz "muitos", não "o caso mais comum" |
| Instrumento: europeias | `[hull-2015, pp. 265–266]` | ◐ | O parágrafo sobre o diagonal (p. 266) não diz "European"; a informação vem só do contexto do calendar spread (p. 265) |
| Flexível: notional | `[natenberg-1994, p. 157]` | ✅ | "diagonal spreads can also be ratioed, with unequal numbers of long and short market contracts" |
| Variante de CS | `[natenberg-1994, p. 157]` | ✅ | "A diagonal spread is similar to a time spread, except that the options have different exercise prices." |
| Restr.: par strike-vencimento livre | `[inferência: hull-2015, p. 266 …]` | ⚖ | Válida (a p. 266 não fixa o par) e com apoio direto em Hull, p. 272: "(a) K2 > K1 and (b) K2 < K1" |
| Notas: Bloomberg "strikes and/or maturities" | `[ovml]` | ✅ | Citação literal idêntica |
| Notas: citação do Hull | `[hull-2015, p. 266]` | ✅ | Citação literal idêntica |

**Verificações da nota:**
- Tabela de pernas ◐: as linhas põem K1 no vencimento curto e K2 no longo, enquanto a Restrição diz que esse par é livre. É aceitável, porque as facetas ignoram o par, mas há tensão entre a tabela e a restrição.
- Frontmatter ✅: `variante_de: [[CS]]` e `flexivel: [notional]` estão sustentados pelo Natenberg (p. 157).
- Omissões/contradições ◐: há evidência contrária fraca a "mesmo tipo". O Natenberg (p. 157) trata "both options are of the same type" como condição de um caso particular, e o resumo do Hull (p. 270) também não exige o mesmo tipo.

## SG
| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: compra de call; venda de call e put | `[ovml]` | ✅ | "purchase of an at-the-money option and the sale of a strangle"; "at-the-money call (put)" |
| 〃 | `[wystup-2006, p. 38]` | ✅ | "a combination of a long call, a short call and a short put" |
| Strikes: put < call comprada < call vendida | `[wystup-2006, p. 39, exemplo]` | ✅ | Tab. 1.17: 1,0775 < 1,1400 < 1,1900 |
| Vencimento: o mesmo | `[ovml]` | ✅ | "have the same expiration date" |
| Notional: igual | `[ovml]` | ✅ | "usually also have the same notional amount" |
| 〃 | `[wystup-2006, p. 39, exemplo]` | ✅ | Notional único, "USD 1,000,000" |
| Moneyness: call comprada ATM | `[ovml]` | ✅ | "purchase of an at-the-money option" (no exemplo do Wystup, a call comprada está em 1,1400 com spot em 1,1500) |
| Moneyness: vendidas OTM (strangle) | `[ovml]` | ◐ | Só "sale of a strangle"; o OTM não está no OVML, nem no OVML do SN |
| 〃 | `[wystup-2006, p. 35]` | ✅ | "an out-of-the-money put and call option" |
| Instrumento: europeias | `[wystup-2006, pp. 29, 39]` | ◐ | Só pela leitura conjunta: a seção é de "BASIC STRATEGIES CONTAINING VANILLA OPTIONS" (p. 29) e vanilla = "European style" (p. 39); é uma inferência formatada como citação direta |
| Flexível: notional | `[ovml]` | ✅ | "usually also have the same notional amount" |
| Composta de EU e SN | `[ovml]` | ✅ | "purchase of an at-the-money option and the sale of a strangle" |
| Restr.: custo zero | `[wystup-2006, p. 38]` | ✅ | "Zero cost product" |
| 〃 | `[ovml]` | ◐ | O OVML diz "low (or zero) cost position"; a afirmação é mais estreita |

**Verificações da nota:**
- Tabela de pernas ✅: −P K1 OTM, +C K2 ATM e −C K3 OTM, 1:1:1.
- Frontmatter ✅: `composta_de` EU e SN; `flexivel: [notional]`.
- Omissões/contradições ◐: o Wystup não exige a call comprada ATM; o ATM vem só do OVML. O Wystup (p. 38) diz "It is similar to a Risk Reversal", o que permitiria um `variante_de: [[RR]]` opcional.

## BF
| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: compra de strangle, venda de straddle | `[ovml]` | ✅ | "long an out-of-the-money Strangle and being short an at-the-money Straddle" |
| 〃 | `[wystup-2006, p. 36]` | ◐ | A 1ª frase diz isso, mas o resto da mesma página descreve a posição oposta ("The holder has to pay a premium", "Maximum loss is the premium paid") |
| Strikes: straddle no meio | `[natenberg-1994, p. 158]` | ✅ | "the straddle is executed at an exercise price midway between the strangle's exercise prices" |
| 〃 | `[wystup-2006, p. 38, exemplo]` | ✅ | Tab. 1.16: 1,1400 / 1,1500 / 1,1600 |
| Vencimento: o mesmo | `[ovml]` | ✅ | "the same expiration date across all the options" |
| 〃 | `[natenberg-1994, p. 158]` | ✅ | "All options must expire at the same time." |
| Notional: igual | `[wystup-2006, p. 38, exemplo]` | ✅ | Notional único, "EUR 1,000,000" |
| Moneyness: strangle OTM, straddle ATM | `[ovml]` | ✅ | "out-of-the-money Strangle … at-the-money Straddle" |
| Instrumento: europeias | `[wystup-2006, pp. 29, 39]` | ◐ | Só pela leitura conjunta, como no SG |
| Composta de SN e SD | `[ovml]` | ✅ | Idem à composição |
| 〃 | `[wystup-2006, p. 36]` | ◐ | Mesma ressalva da composição |
| Notas: short iron butterfly = long butterfly | `[natenberg-1994, p. 158]` | ✅ | Citação literal idêntica; "If the straddle is sold and the strangle is purchased … (a short iron butterfly)" confirma o nome |
| Notas: a definição do Wystup coincide com o OVML | `[wystup-2006, p. 36]` | ✅ | A 1ª frase coincide, mas a nota é incompleta: a posição oposta já aparece na própria p. 36 |
| Notas: o exemplo descreve a posição oposta | `[wystup-2006, p. 37]` | ✅ | Citação literal idêntica; a Fig. 1.15 (lucro em V, mínimo em K2) confirma |

**Verificações da nota:**
- Tabela de pernas ✅: +P K1 OTM, −P K2 ATM, −C K2 ATM e +C K3 OTM.
- Frontmatter ✅: `composta_de` SN e SD.
- Omissões/contradições ◐: a Fig. 1.5 do Wystup (p. 22) mostra o butterfly com payoff em tenda, coerente com o OVML, e serve de apoio melhor que a p. 36. O Problema 12.26 do Hull (p. 272) monta "a long strangle and a short straddle", com o straddle "halfway".

## BFC
| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: compra de K1 e K3, venda de 2×K2, um só tipo | `[ovml]` | ◐ | "long the in-the-money and out-the-money strikes and short at-the-money strike … entirely of either puts or calls"; não diz "duas" |
| 〃 | `[hull-2015, pp. 262, 264]` | ✅ | "selling two European call options with a strike price K2"; versão com puts na p. 264 |
| Strikes: K3 − K2 = K2 − K1 | `[hull-2015, pp. 264, 270]` | ✅ | "halfway between K1 and K3" (p. 264); "K3 − K2 = K2 − K1" (p. 270) |
| Vencimento: o mesmo | `[hull-2015, p. 265]` | ✅ | "Up to now we have assumed that the options used to create a spread all expire at the same time." |
| Notional: 1:2:1 | `[hull-2015, p. 264]` | ✅ | "selling two European call options" |
| Moneyness: K1 ITM, K2 ATM, K3 OTM | `[ovml]` | ✅ | Para calls; nas puts a ordem se inverte, o que o espelho cobre |
| Moneyness: K2 perto do preço corrente | `[hull-2015, p. 264]` | ✅ | "Generally, K2 is close to the current stock price." |
| Instrumento: europeias | `[hull-2015, pp. 262, 264]` | ✅ | "buying a European call option" |
| Composta de CP comprado e CP vendido | `[inferência: …]` | ⚖ | Válida: (+C K1 −C K2) é o bull spread (p. 258); (−C K2 +C K3) é o bear spread de calls (p. 261), o short do CP; a soma dá 1:−2:1 |
| Variante de BF | `[ovml]` | ✅ | "Unlike the other butterflies constructed with straddles and strangles this is constructed entirely of either puts or calls." |
| Notas: citação do Hull | `[hull-2015, p. 264]` | ✅ | Citação literal idêntica |

**Verificações da nota:**
- Tabela de pernas ✅: +C K1 ITM, −C K2 ATM (2) e +C K3 OTM.
- Frontmatter ✅: `composta_de: [[CP]]` e `variante_de: [[BF]]`.
- Omissões/contradições ✅: nenhuma. O short ("reverse strategy", Hull p. 265) é coberto pela regra de short.

## CR
| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: compra de strangle largo, venda de estreito | `[ovml]` | ✅ | "being long a Strangle and being short another Strangle … smaller than the interval … of the larger strangle" |
| Strikes: o vendido fica dentro do comprado | `[ovml]` | ◐ | O OVML só exige um intervalo menor, não diz que o vendido fica dentro do comprado |
| Strikes: costumam ser consecutivos | `[natenberg-1994, p. 158]` | ✅ | "four options at consecutive exercise prices"; na fonte é parte da definição, não um hábito, e está dada para o condor de um só tipo |
| Vencimento: o mesmo | `[natenberg-1994, p. 158]` | ✅ | "all options must … expire at the same time" (o OVML do CR não fala de vencimento) |
| Notional: uma por perna | `[natenberg-1994, p. 158]` | ✅ | "the two outside options are purchased and the two inside options sold" |
| Instrumento: europeias | `[inferência: … wystup-2006, p. 39]` | ⚖ | Fraca, pelo mesmo motivo do SDR |
| Composta de SN comprado e vendido | `[ovml]` | ✅ | "long a Strangle and being short another Strangle" |
| Notas: citação do Natenberg | `[natenberg-1994, p. 158]` | ✅ | Citação literal idêntica |
| Notas: a versão com strangles equivale, e o "long" coincide | `[inferência: …]` | ⚖ | Válida: pela paridade put-call, (+P K1 −P K2) = (+C K1 −C K2) + constante, logo o condor do OVML equivale ao condor de calls mais caixa; o OVML confirma o lado ("long a Condor if … stable") |

**Verificações da nota:**
- Tabela de pernas ✅: +P K1, −P K2, −C K3 e +C K4, coerente com o OVML se os strikes forem aninhados.
- Frontmatter ◐: falta `variante_de: [[BF]]`, sustentado por "Another variation on a butterfly, known as a condor" (Natenberg, p. 158).
- Omissões/contradições ◐: o Natenberg implica pontas igualmente espaçadas (K2 − K1 = K4 − K3), porque o condor "will be worthless whenever the underlying contract is outside the extreme exercise prices". A nota não registra isso.
