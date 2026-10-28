# Validação D38 — literatura
Validador: agente independente · 2026-10-23 · método: tabelas de pernas das 66 notas + busca de texto (PyMuPDF) em Hull, Wystup, Haug, Reiswich-Wystup e DSB; Natenberg lido pela imagem; deltas ilustrativos calculados em `hedge.py` (σ 10%, 1 ano, forward delta).

## Resumo
| Decisão | Veredito | Em uma linha |
|---|---|---|
| 1 — categoria (vista pela literatura) e contagem de pernas | ◐ | Funciona como regra por componente (UPI), mas a literatura não confirma "vanilla" como família para pacotes, e o NDO não é necessariamente vanilla. A contagem de pernas está certa. |
| 2 — FP em `vanilla` | ✅ | O prêmio diferido sem condição muda o valor, não o payoff. O template Vanilla_Option nem tem campo de data do prêmio. |
| 6 — delta hedge (lado conceitual) | ◐ | O conceito está certo; o limite fixo de 90% não. O denominador é indefinido, há hedges de 95% ou mais na literatura, e falta o NDF. |

## Decisão 1 — categoria pela literatura e contagem de pernas
- **Veredito:** ◐
- **A favor:**
  - Vanilla = opção europeia ou americana de call/put [hull-2015, p. 598]. O Wystup separa "linear combinations of vanilla options" (CP, RR, SD, SN, BF, SG) das exóticas de 1ª e 2ª geração, que trata como "ingredients for FX structured products" [wystup-2006, pp. 1, 29, 39, 101]. Isso apoia `vanilla` para CP, RR, SD, SN, BF, BFC, SG, CR, CS e DS.
  - A taxonomia ISDA/DSB põe Barrier e Digital em "Simple Exotic" e Target em "Exotic" [dsb-2018, p. 6]. Isso apoia `exotica` para barreiras, toques e digitais.
  - **TF e COL em `vanilla` são coerentes.**
    - O Hull trata opção + ativo como estratégia de negociação, não como exótica. A protective put equivale a uma call longa mais caixa [hull-2015, pp. 254, 256, 258]. Logo, TF (FWD + put) tem payoff de call.
    - A fence, ou COL, "is simply a bull vertical spread done synthetically" [natenberg-1994, p. 264].
  - **Forwards estruturados em `exotica`** se apoiam nos componentes:
    - o accumulative forward "consists of fade-in calls and fade-in puts, possibly with extra knockout ranges" [wystup-2006, p. 157];
    - o RF é forward sintético + DNT [wystup-2006, p. 152];
    - o shark forward é forward + reverse knock-out [wystup-2006, p. 145];
    - forwards de média (ARF, ASF) estão entre as exóticas de 2ª geração (seção 1.6.9) [wystup-2006, p. viii].
  - **Regra de pernas:** o butterfly de puts 70×140×70 é "a three-sided spread", e "the options which comprise a spread position are sometimes referred to as the legs" [natenberg-1994, p. 181]. Portanto, as duas vendas do meio somam numa perna, e a butterfly de calls tem 3 pernas, não 4. O Hull é compatível: "three different strike prices… selling two European call options with a strike price K2" [hull-2015, pp. 262, 264].
- **Contra / contraexemplos:**
  - **Pacotes no Hull.** O Hull define "package" (calls, puts, forwards, caixa, ativo) como o 1º tipo de opção exótica. Ele cita entre os pacotes bull/bear spreads, butterflies, straddles e strangles, e conta os pacotes entre os "15 different types of exotic options" [hull-2015, pp. 598, 618]. A pasta `vanilla` não pode, portanto, ser justificada como "produto vanilla" pela literatura, só como "componentes vanilla".
  - **PF no Wystup.** O Wystup não chama os forward products de exóticos: classifica-os como "Structured Products". Isso inclui o PF, feito só de vanillas [wystup-2006, pp. 139, 141], e até o "outright or vanilla forward" [wystup-2006, p. 139]. É uma 4ª família, transversal às três pastas. Não há contradição com a regra por UPI, mas a "confirmação pela literatura" é parcial no PF (e no TF/COL).
  - **NDO.** O template NDO tem o atributo "Valuation Method or Trigger" = [Vanilla; Asian; Lookback; etc.] [dsb-2024, aba "100 (Req)", linha 14]. Um NDO não é necessariamente vanilla, e a regra "Vanilla_Option ou NDO → vanilla" classifica como vanilla um NDO asiático ou com barreira.
  - **Equivalentes sintéticos.** TF ≡ call [hull-2015, p. 258] e COL ≡ call spread [natenberg-1994, p. 264]. A mesma estrutura pode chegar ao DTCC com outro número de pernas. Isso não muda a categoria, mas afeta o matching.
- **Ajuste proposto:**
  - Escrever no `_schema.md` que a categoria é por componente (UPI das pernas) e não pela família da literatura. Registrar a divergência com o Hull (packages = exóticas) e com o Wystup (forward products) nas notas do PF, TF e COL.
  - Contar o NDO como vanilla só se o método de valoração for Vanilla; com outro método, a nota vai para `exotica`.

## Decisão 2 — FP vai para `vanilla`
- **Veredito:** ✅
- **A favor:**
  - **Wystup.** O Wystup chama de "contingent or deferred payment options" a família da pay-later e diz: "We can also simply defer the payment of a vanilla without any conditions on the moneyness" [wystup-2006, p. 118]. Para o pagamento na data de entrega, em vez da data spot, ele só pergunta como mudam "the value formulae for say vanilla options" [wystup-2006, p. 135, exercício 1]. O payoff não muda.
  - **Hull.** No Hull, o prêmio diferido é A = c·e^{rT}, e o payoff é max(S_T − K, 0) − A [hull-2015, p. 599]. Isso é a vanilla mais um valor fixo, sem condição.
  - **Pay-later (Wystup e Haug).** A pay-later muda o payoff: [φ(S_T − K) − P]·1{φS_T ≥ φK}, isto é, vanilla − P·digital [wystup-2006, pp. 116, 118]. O Haug a trata como gap option [haug-2007, p. 174]. Ela é exótica justamente porque o prêmio é condicional, e o FP não tem essa condição.
  - **DSB.** O template Vanilla_Option só tem par de moedas, Option Type, Exercise Style e Delivery Type; não há atributo de data de pagamento do prêmio [dsb-2024, aba "103 (Req)"]. Um FP é reportado como Vanilla_Option.
- **Contra / contraexemplos:**
  - O Hull põe a deferred payment option na seção "Packages" do capítulo de exóticas. Com K = forward, ela recebe os nomes "break forward, Boston option, forward with optional exit, and cancelable forward" [hull-2015, p. 599]. Isso é nomenclatura de forward product, mas o produto continua sendo uma Vanilla_Option.
  - Consequência prática (não é contra a categoria): FP e EU têm o mesmo UPI. Pelo produto, o FP é indistinguível do EU [inferência: dsb-2024, aba "103 (Req)"].
- **Ajuste proposto:** nenhum na categoria. Opcional: incluir na nota do FP o sinônimo do Hull para K = forward (break forward/Boston option) e registrar a ambiguidade com o EU.

## Decisão 6 — delta hedge, lado conceitual
- **Veredito:** ◐
- **A favor:**
  - **O hedge não é perna.**
    - O delta é "the percentage of the foreign notional one must buy when selling the option to hold a hedged position"; o forward delta corresponde ao hedge no mercado a termo [reiswich-wystup-2009, p. 4].
    - No Natenberg, o hedge é uma "opposing market position" tomada junto com a opção, por exemplo "Sell five underlying contracts" para 10 calls de delta 50 [natenberg-1994, p. 137]. As pernas são as opções [natenberg-1994, p. 181, nota 2].
  - **Hedge no ato.** O hedge sai no momento do negócio: "the immediate hedge executed is generally the spot-hedge, because it has to be done instantaneously with the option trade" [reiswich-wystup-2009, p. 7]. O mercado cota a vol por delta (ATM, RR 25Δ, strangle) [reiswich-wystup-2009, pp. 12–13; wystup-2006, p. 25]. O ATM delta-neutral garante um straddle com "zero spot exposure" [reiswich-wystup-2009, p. 9].
  - **Nas estruturas de vol interbancárias, o hedge fica longe de 90%** (`hedge.py`, em % do notional de uma perna):
    - ATM 50%;
    - RR 25Δ 50%, ou 25% da soma das pernas;
    - RR 10Δ 20%;
    - CP ATM/25Δ 25%;
    - SG 50%;
    - SD, SN, BF, BFC, CR e SDR perto de 0 (no SDR, "zero forward delta" é parte da definição [ovml]).
  - **Estruturas da base com FWD.** Só TF e COL têm FWD, ambas em razão 1 [tabelas de pernas], de acordo com o Natenberg (1:1:1) [natenberg-1994, p. 264]. A regra não descarta nenhuma estrutura da base na razão nominal.
- **Contra / contraexemplos:**
  - **"Delta exchange".** O termo não aparece nas fontes, nem a troca do hedge com a mesma contraparte. As fontes dizem que o hedge imediato é **spot** [reiswich-wystup-2009, p. 7; wystup-2006, p. 10]. O spot não aparece no DTCC (decisão 5). O hedge a termo aparece:
    - em pares emergentes, onde o forward delta é o padrão;
    - em prazos acima de 1 ano;
    - em "delta-one-similar products" [reiswich-wystup-2009, pp. 7–8];
    - depois do negócio, via FX swap, provavelmente fora da janela de 2 s [reiswich-wystup-2009, p. 7].
  - **Hedge de 90% ou mais.**
    - **Forward products.** Na fader forward extra, o hedge é "the bank buys EUR 3,768,784" sobre USD 4.800.000 a 1,2165, ou seja, **95,5%** do notional [wystup-2006, p. 149]. Há outros casos parecidos:
      - PF com razão 1 (forward sintético): 100%;
      - PF alavancado (r = 2): 150% do notional da call;
      - FE, KOF, KKF, RF e BFW: replicam forwards [wystup-2006, pp. 140, 143, 145, 152], logo o delta fica perto de 100% [inferência].
    - **Opções ITM.** Uma call de 75Δ ou 90Δ tem hedge de 75% ou 90%; "a 25-delta call must have the same volatility as a 75-delta put" [reiswich-wystup-2009, p. 5].
    - **Delta premium-adjusted.** O delta premium-adjusted de put é (K/f)·N(−d₂) [reiswich-wystup-2009, p. 7, eq. 12–13]; com K/f = 1,2, dá **116%**. Esse é o padrão em USDJPY, EURJPY, USDCHF, USDBRL e USDMXN [reiswich-wystup-2009, p. 8, Tabela 2].
    - **Reverse barriers.** Perto da barreira, o delta é muito grande ("Sell lots of EUR… Sell even more EUR") [wystup-2006, pp. 47–48].
  - **Denominador indefinido.** "O notional das opções" é a soma ou o de uma perna? Para um RR 25Δ, o hedge é 50% de uma perna ou 25% da soma. Para um PF com r = 2, é 150% da call ou 50% da soma.
  - **Forward legítimo em razão ≠ 1, fora da base.**
    - PF de mesmo strike = r·FWD + (1 − r)·call, pela paridade [wystup-2006, pp. 140–141]. Se for reportado assim, com r = 0,3 o forward fica em 43% da call e seria descartado por engano.
    - Boosted forward: forward de USD 1 M com put de EUR 750 mil [wystup-2006, pp. 165–166].
    - Fader forward plus de 50% [wystup-2006, p. 148].
    - ACCU negociado "along with outright forward" [wystup-2006, p. 157].
  - **Faltam o NDF e a moeda.** Para NDO e pares emergentes, o hedge é NDF [inferência: reiswich-wystup-2009, pp. 7–8]. O delta é medido em moeda estrangeira [reiswich-wystup-2009, p. 4], então a comparação precisa usar a mesma moeda nos dois registros.
  - **Conversion.** A conversion (FWD + call vendida + put comprada, mesmo strike) tem forward de 100% contra as opções [natenberg-1994, p. 218]. Um put muito ITM com hedge perto de 100% vira o TF.
- **Ajuste proposto (critério melhor):**
  1. **Denominador:** o notional da maior perna de opção, depois de somadas as idênticas, na mesma moeda (a moeda do notional da opção).
  2. **Matching primeiro, sem limite fixo.** O FWD ou NDF é perna só se o grupo com ele casa uma nota que tem FWD (hoje TF e COL), com razão ≈ 1 (tolerância de ±5%). Caso contrário, é candidato a hedge até cerca de 1,5× (cobre ITM, premium-adjusted e delta-one). Remove-se o FWD e faz-se o matching do resto.
  3. **Empate.** Se as duas leituras casam (ex.: put ITM + FWD de 95–100% → TF ou EU com hedge), manter as duas candidatas e ranquear (passo 4 do Matching). Não descartar.
  4. **Sinal.** Se o lado estiver disponível, o hedge tem sinal oposto ao delta líquido das opções. Um forward no mesmo sentido nunca é hedge.
  5. **Grupos sem forward.** Registrar no schema que a falta de hedge é o caso normal, porque o hedge imediato é spot.

## Contagem de pernas
| COD | Pernas propostas | Suas | Comentário |
|---|---|---|---|
| CP | 2 | 2 | — |
| RR | 2 | 2 | — |
| SD | 2 | 2 | Call e put no mesmo strike são tipos diferentes; não se somam. |
| SN | 2 | 2 | — |
| SDR | 2 | 2 | Como o spread 1 do Natenberg (10 calls × 8 puts, delta neutro) [natenberg-1994, p. 175]. |
| PF | 2 | 2 | Notionals diferentes [wystup-2006, p. 142, exemplo]. Equivale a r·FWD + (1 − r)·call (ver D6). |
| CS | 2 | 2 | — |
| DS | 2 | 2 | — |
| TF | 2 | 2 | Pode chegar como 1 call sintética [hull-2015, p. 258]. |
| SG | 3 | 3 | [wystup-2006, p. 38] |
| BFC | 3 | 3 | "Three-sided" depois de somar as vendas do meio [natenberg-1994, p. 181]. |
| COL | 3 | 3 | Natenberg: posição + put + call [natenberg-1994, p. 264]. Sinteticamente, é um call spread (2). |
| BF | 4 | 4 | Put K2 e call K2 têm tipos diferentes; não se somam [wystup-2006, p. 36]. |
| CR | 4 | 4 | Quatro strikes distintos. |
| FE | 2 | 2 | O Wystup compõe com FWD + reverse KO [wystup-2006, p. 145]: mesma contagem, outros instrumentos. |
| EC | 2 | 2 | — |
| KOF | 2 | 2 | [wystup-2006, p. 143] |
| KKF | 2 | 2 | — |
| ARC | 2 | 2 | — |
| BFW | 3 | 3 | [wystup-2006, pp. 161, 173] |
| RF | 3 | 3 | Se o forward sintético vier como FWD outright, são 2 pernas (FWD + DNT) [wystup-2006, p. 152]. |

Nenhuma contagem diverge. A regra de somar pernas idênticas só faz diferença na BFC.

## Não verificado
- **Lado (compra/venda) nos dados públicos.** Não verifiquei se os dados públicos do DTCC trazem o lado. Isso decide se o teste de sinal do critério de hedge é viável. O motivo: não há fonte em `fontes/`, e a amostra estava fora do escopo.
- **Método de valoração do NDO nos dados públicos.** Não verifiquei se ele é visível; pelo mesmo motivo, isso fica para a validação empírica.
- **Hedges reais do DTCC.** Não medi a razão dos hedges observados no DTCC. Os percentuais acima são ilustrativos (`hedge.py`) ou vêm de exemplos dos livros.
