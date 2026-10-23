# Validação do Claude — lote 6

Validador: agente independente · 2026-10-22 · método: leitura integral de cada página citada (Natenberg pela imagem, com o número impresso conferido; Hull e Wystup pelo texto do PyMuPDF), conferência dos textos da Bloomberg em `bloomberg_description/` e busca de evidência contrária em todas as fontes com texto ("collar", "fence", "cylinder", "tunnel", "range forward").

## Resumo

| ✅ | ◐ | ✗ | ⚖ | ? | total |
|---|---|---|---|---|---|
| 10 | 5 | 0 | 5 | 0 | 20 |

Itens adicionais do lote 1 (fora da contagem acima): 3 ✅, 2 ◐, 5 citações.

## Status das correções (aplicadas pelo Claude principal, 2026-10-22)

Os vereditos abaixo valem para as notas **antes** das correções.

| Status | Itens |
|---|---|
| ✎ aplicada | 1, 2, 4–8, 10, 11, 13, 14; o deslocamento do Natenberg passou a 9 a partir da p. 215 |
| ✎ decidida pelo usuário | 3, 9 (nome mantido: Collar), 12 (D36) |

## Correções propostas

**Prioridade 1**

1. COL · Notas, 1ª linha: "O OVML não tem uma estrutura 'collar' separada: o nome aparece no RR" é falso como escrito. O OVML tem também "Average Rate Collar (ARC)" ("Like a risk reversal but constructed with average rate put and calls") e "Enhanced Collar (EC)" ("a lower risk alternative to the Risk Reversal"). Correção: "No OVML, 'collar' sempre nomeia o par de opções: o RR, 'Risk Reversal (Collar)', e duas variantes dele, [[ARC]] e [[EC]]; não há collar com a posição [inferência: nomes e textos da Bloomberg do RR, ARC e EC]."
2. COL · tabela de origem, 2ª linha Sinônimo: "reversal" não é sinônimo da forma da tabela. A p. 264 diz "split-price conversions and reversals", e a p. 218 define reversal como "short underlying + long call + short put" (mesmo strike e vencimento), ou seja, o análogo da versão vendida. Correção: trocar "reversal" por "split-price reversal (versão vendida)", ou removê-lo.

**Prioridade 2**

3. COL · o alias "Collar" (nome da nota) não tem linha Sinônimo nem citação. Nas fontes de FX, "collar" é o par de opções: Wystup p. 31 ("Risk Reversal or collar"), Hull p. 599 ("zero-cost collar" é nome do range forward, que "consists of a long call and a short put or a short call and a long put") e OVML (RR, ARC, EC). O único apoio para a forma com a posição é o Natenberg p. 265, e no mercado de juros. Correção: acrescentar `| Sinônimo | collar | [inferência: natenberg-1994, p. 265, o collar é "a fence done in the interest rate market"; a fence inclui a posição, natenberg-1994, p. 264] |` e dizer nas Notas que, nas fontes de FX, collar é o par de opções. A escolha do nome está no item 9.
4. COL · a 2ª linha Sinônimo contradiz `aliases` e as Notas. Ela lista "range forward" e "cylinder", que as Notas excluem de `aliases`, e também "tunnel" e "split-price conversion", que não estão em `aliases`. Pelo `_schema.md`, a linha Sinônimo cobre os sinônimos de `aliases`. Correção: deixar na tabela de origem só os sinônimos que estão em `aliases` e levar os outros nomes da p. 264 para as Notas, como conflito de nome. Se forem aceitos como sinônimos, incluí-los em `aliases`.
5. COL · Composição, 1ª linha: a p. 263 só traz a definição genérica, "purchase of a protective option with the sale of a covered option", e a posição comprada aparece no exemplo. A definição com as três pernas está na p. 264: "long fence (long the underlying, short a covered call, long a protective put)". Trocar `[natenberg-1994, p. 263]` por `[natenberg-1994, p. 264]`.
6. COL · Restrições, 1ª linha (custo zero ou crédito): a p. 263 só diz isso no exemplo 45/55. Trocar por `[natenberg-1994, p. 263, exemplo]` e acrescentar `[natenberg-1994, p. 264]`, que diz em termos gerais: "known protection at a low cost, or even a credit".
7. COL · Notas, collar extra: "uma série de forwards com caso melhorado ativado por knock-in" deixa de fora o pior caso garantido e a participação quando não há knock-in. Trocar por: "uma série de collar extras: em cada vencimento, uma call garante o pior caso e, se o knock-in ocorrer, fica travado um forward no caso melhorado [wystup-2006, pp. 172–173]".
8. RR · Notas, 1ª linha: o `[ovml]` sustenta "collar" só pelo nome "Risk Reversal (Collar)"; o texto embutido não usa a palavra. A `[natenberg-1994, p. 263]` não diz que a fence inclui a posição; isso está na p. 264. Correção: escrever "O nome Bloomberg é 'Risk Reversal (Collar)' [ovml]" e trocar `[natenberg-1994, p. 263]` por `[natenberg-1994, p. 264]`. Também harmonizar com a COL, que cita o mesmo fato como inferência.

**Prioridade 3**

9. COL · nome da nota (decisão do usuário). As fontes sustentam a forma da tabela, mas com o nome "fence": Natenberg p. 264 e Figura 13-5 ("A Long Fence"), e Hull pp. 370–371 na versão FX (exposição + put K1 comprada + call K2 vendida, Figura 17.2). As Notas excluem "range forward" e "cylinder" de `aliases` porque o Hull os usa para o par de opções. O mesmo critério atinge "Fence" ("option fence") e "Collar" ("zero-cost collar"), ambos do Hull p. 599. Há duas saídas: renomear a nota para Fence, ou manter Collar e registrar o conflito para todos os nomes. Além disso, no Wystup p. 179 "tunnel" é outro produto (tunnel deposit, ligado a double-no-touch).
10. COL · evidência direta em FX que a nota não usa: em Strikes e Moneyness, acrescentar `[hull-2015, p. 370, exemplo]` ("K1 < 1.5200 < K2", sendo 1.5200 a taxa forward de três meses). Em Notional, acrescentar `[hull-2015, p. 370, exemplo]` ("In both cases, the options are on one million pounds", o mesmo valor da exposição) e `[natenberg-1994, p. 264, exemplo]` ("45/55 fence = long underlying + long 45 put + short 55 call"). Em Instrumento EU, acrescentar `[hull-2015, p. 370]` ("buy a European put option … sell a European call option").
11. COL · Vencimento: a premissa "as opções protegem a mesma posição até a mesma data" está sem citação, e o mesmo prazo para as duas opções do Hull só se fecha nas pp. 370–371. Sugestão: `[inferência: as opções vencem na data do fluxo protegido, hull-2015, p. 370 ("buying put options on sterling that mature at that time"); a fence é uma split-price conversion, natenberg-1994, p. 264, e a conversion pressupõe o mesmo vencimento, natenberg-1994, p. 218]`.
12. COL · Instrumento FWD: registrar que no Hull o forward é uma alternativa ao par de opções, não uma perna dele ("An alternative is to buy a European put…", p. 370), e que o FWD representa a exposição só a menos de uma constante. Pela p. 264, a forma da tabela equivale a um bull spread de calls mais caixa. Em FX, a exposição protegida em geral não é um negócio reportado, e por isso um collar no DTCC tende a aparecer só com as duas opções, como um RR. É uma decisão do usuário.
13. COL · Restrições, espelho: a conclusão está certa. Vale acrescentar que a versão vendida da p. 264 é exatamente a regra global de short (inverter os três lados). A comparação com o TF não é exata: lá, a outra versão não é coberta por nenhuma das duas regras.
14. COL · Notas, 2ª linha: "o RF do OVML é outra estrutura ([[RF]])" está sem citação nesta nota. Reaproveitar as do RR: `[wystup-2006, pp. 151–152]; [inferência: texto da Bloomberg do RF]`.

## COL

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: posição comprada, put protetora comprada, call coberta vendida | `[natenberg-1994, p. 263]` | ◐ | A p. 263 define só "the purchase of a protective option with the sale of a covered option"; a posição comprada aparece no exemplo. A definição com as três pernas está na p. 264. |
| Composição: versão vendida (posição vendida, call comprada, put vendida) | `[natenberg-1994, p. 264]` | ✅ | "A short fence consists of a short underlying position together with the purchase of a protective call and sale of a covered put." |
| Strikes: put abaixo do preço da posição, call acima | `[natenberg-1994, p. 263, exemplo]` | ✅ | "with an underlying contract at 50 … sell a 55 call and purchase a 45 put"; o marcador `exemplo` está correto. O Hull p. 370 dá a versão FX ("K1 < 1.5200 < K2"). |
| Vencimento: o mesmo nas três pernas | `[inferência: … hull-2015, p. 370, exemplo]` | ⚖ | A conclusão procede, mas a 1ª premissa está sem citação, e o exercício da call "in three months" só aparece na p. 371 (item 11). |
| Notional: igual nas três pernas | `[natenberg-1994, p. 263, exemplo]` | ✅ | No exemplo, uma put e uma call cobrem toda a posição: "insulated from any fall in price below 45" e "his underlying position will be called away". A p. 264 e o Hull p. 370 são mais explícitos. |
| Moneyness: put e call OTM | `[natenberg-1994, p. 263, exemplo]` | ✅ | Com o ativo a 50, a put 45 e a call 55 estão fora do dinheiro. |
| Instrumento: a posição é um FWD | `[inferência: … hull-2015, p. 370]` | ⚖ | A premissa confere ("a US company that knows it will receive one million pounds sterling in three months"). A conclusão é uma modelagem: no Hull o forward é uma alternativa às opções, não uma perna (item 12). |
| Instrumento: opções europeias | `[inferência: _schema.md; wystup-2006, p. 39]` | ⚖ | A p. 39 diz "vanilla (European style put and call) options"; a inferência é válida. Há evidência direta no Hull p. 370 ("European put … European call"). |
| Composta de: FWD e RR short | `[inferência: natenberg-1994, p. 263 + tabela do RR]` | ⚖ | Confere: o RR é put − e call +, e o short dá put + e call −, com a put abaixo da call. A premissa do Natenberg fica melhor na p. 264. |
| Sinônimo: fence | `[natenberg-1994, p. 263]` | ✅ | "A popular strategy, known as a *fence*". Contra: no Hull p. 599, "option fence" é o par de opções. |
| Sinônimo: range forward, tunnel, cylinder, split-price conversion, reversal | `[natenberg-1994, p. 264]` | ◐ | "range forwards, tunnels, cylinders; … split-price conversions and reversals". "Reversal" é a versão vendida (split-price reversal; p. 218). A linha também contradiz `aliases` e as Notas (itens 2 e 4). |
| Restrição: custo zero se a put e a call valem o mesmo; crédito se a call vale mais | `[natenberg-1994, p. 263]` | ◐ | Está dito só sobre o exemplo: "If they are the same, the cost of the hedge is zero … for a credit". Falta o marcador `exemplo`; o enunciado geral está na p. 264 (item 6). |
| Restrição: a versão comprada é um bull spread sintético | `[natenberg-1994, p. 264]` | ✅ | "a long fence … is simply a bull vertical spread done synthetically". |
| Restrição: o espelho não se aplica | `[inferência: regras de short e espelho, como no TF]` | ⚖ | Procede: o espelho dá +FWD, +call, −put, que não é uma fence. A versão vendida é a regra de short (item 13). |
| Notas: o OVML não tem estrutura "collar" separada; o nome aparece no RR | `[inferência: nome do RR no OVML]` | ◐ | A premissa está incompleta: o OVML tem "Average Rate Collar (ARC)" e "Enhanced Collar (EC)", ambas variantes do RR (item 1). |
| Notas: o Wystup chama o par de opções de collar | `[wystup-2006, p. 31]` | ✅ | A citação literal é idêntica: "A popular liquid product in FX markets is the Risk Reversal or collar." |
| Notas: o Hull lista nomes para o range forward, que é só o par de opções | `[hull-2015, p. 599]` | ✅ | A citação literal (nota de rodapé 1) é idêntica. A p. 599 diz que o range forward "consists of a long call and a short put or a short call and a long put". Contra: a lista inclui "zero-cost collar" e "option fence", que são os `aliases` da nota (item 9). |
| Notas: o collar de juros é um cap comprado com um floor vendido | `[hull-2015, p. 679]` | ✅ | "A collar is a combination of a long position in a cap and a short position in a floor." |
| 〃 (citação do Natenberg) | `[natenberg-1994, p. 265]` | ✅ | A citação literal é idêntica: "This is simply a fence done in the interest rate market." |
| Notas: o collar extra series é uma série de forwards com caso melhorado ativado por knock-in | `[wystup-2006, pp. 172–173]` | ◐ | É uma série de "collar extras", com o pior caso garantido por uma call; "If the knock-in event occurs, the client has locked in a forward with the improved case". Sem knock-in, o cliente participa da queda (item 7). |

**Verificações da nota:**
- Tabela de pernas: ✅ as fontes sustentam a forma (posição + put comprada + call vendida). É a "long fence" do Natenberg (p. 264 e Figura 13-5, com "long an underlying position", "buy a protective put", "sell a covered call") e o hedge do Hull pp. 370–371 (exposição comprada em libra + put K1 + call K2 vendida). Os lados da versão long conferem. A ordem K1 < K2 < K3 vale com o FWD à taxa forward corrente (Hull: "K1 < 1.5200 < K2"); se o FWD for uma posição antiga a outra taxa, K2 pode ficar fora do intervalo, e a tabela não cobre esse caso. Notional 1 e T1 em todas as pernas conferem.
- Frontmatter: ◐ `composta_de` ([[FWD]], [[RR]]) está consistente com a tabela de origem. `flexivel: []` e a ausência de `barreira` e `payoff` estão corretas, porque a nota tem 3 pernas. Já `aliases` traz "Collar" sem citação, e "Fence" conflita com o Hull p. 599 (itens 3, 4 e 9).
- Omissões/contradições: ◐
  - a nota omite ARC e EC do OVML;
  - a linha Sinônimo contradiz `aliases` e as Notas;
  - o conflito de nomes corre nos dois sentidos: o Natenberg p. 264 usa "range forwards" e "cylinders" para a fence com a posição, e o Hull usa esses nomes para o par de opções;
  - o Natenberg (p. 265) trata o collar de juros como a mesma estratégia em outro mercado, e por isso "outro produto" só se justifica pelo ativo (juros). A nota diz isso de forma aceitável.

## Itens adicionais (lote 1)

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| RR · Notas: o OVML também chama esta estrutura de collar | `[ovml]` | ◐ | O texto embutido do RR não contém "collar"; só o nome Bloomberg, "Risk Reversal (Collar)", sustenta a afirmação. Os textos do ARC ("Like a risk reversal") e do EC reforçam que, no OVML, collar = par de opções (item 8). |
| RR · Notas: a versão com a posição protegida (fence) é a [[COL]] | `[natenberg-1994, p. 263]` | ◐ | Na p. 263, a fence aparece como "protective option" + "covered option"; a inclusão da posição está explícita na p. 264 ("long the underlying, short a covered call, long a protective put"). |
| PF · Variante de FWD: generaliza o forward sintético com notionals diferentes | `[wystup-2006, pp. 140–141]` | ✅ | p. 140: "a long forward can be replicated by a long call and a short put with the same strike and same notional"; p. 141: "like a synthetic forward … except that the notionals are different". A própria p. 141 remete à seção 2.1.1, então não se trata de uma leitura conjunta indevida. |
| PF · Notas: no estilo de alto risco, também se chama *leveraged forward* | `[wystup-2006, p. 142]` | ✅ | "This high risk style product is also sometimes called leveraged forward." A frase começa na p. 141, mas o nome está na p. 142. |
| SN · Sinônimo e alias: bottom vertical combination | `[hull-2015, p. 269]` | ✅ | "In a strangle, sometimes called a bottom vertical combination". Opcional: a mesma página chama a venda de strangle de "top vertical combination". |
