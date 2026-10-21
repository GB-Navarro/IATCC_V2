# Fontes

Índice das fontes usadas nas notas de `Brain/structures/`. Os arquivos ficam nesta pasta, só na máquina local.

- **Nome do arquivo:** `<chave>_<título-curto>.<ext>`.
- **Citação nas notas:** `chave, p. N`, sempre com a página **impressa**.
- **Status:** **obtido** (arquivo na pasta) · **lido** (já usado nas notas) · **opcional** · **dispensado**

## Lista

| Chave | Referência | Edição / ISBN | Página impressa = PDF − | Status |
|---|---|---|---|---|
| `wystup-2006` | Wystup, U. *FX Options and Structured Products*. Wiley. | 1ª ed., 2006 · 978-0-470-01145-4 | 19 | obtido |
| `hull-2015` | Hull, J. C. *Options, Futures, and Other Derivatives*. Pearson. | 9ª ed., 2015 · 978-0-13-345631-8 | 23 | obtido |
| `haug-2007` | Haug, E. G. *The Complete Guide to Option Pricing Formulas*. McGraw-Hill. | 2ª ed., 2007 · 978-0-07-138997-6 | 39 | obtido |
| `reiswich-wystup-2009` | Reiswich, D.; Wystup, U. "FX Volatility Smile Construction". CPQF Working Paper 20, Frankfurt School. | versão 2 (2010) do working paper de 2009 · gratuito | 2 | obtido |
| `wystup-fxcol-2022` | Wystup, U. "KOAMKIEU and the Psychology of Derivatives in Private Banking". MathFinance FX Column. | 2022 · gratuito | 0 | lido |
| `wystup-fxcol-2025` | Wystup, U. "KIKO Double-Touch, Parisian Options and Triangular Relationships". MathFinance FX Column. | 2025 · gratuito | 0 | obtido |
| `wystup-fxcol-2026` | Wystup, U. "Sales Slide for the Shark Forward". MathFinance FX Column. | 2026 · gratuito (.docx) | — | obtido |
| `natenberg-1994` | Natenberg, S. *Option Volatility & Pricing: Advanced Trading Strategies and Techniques*. McGraw-Hill/Irwin. | ed. revisada, 1994 · 1-55738-486-X | 10 | obtido (escaneado) |
| `wystup-2017` | Wystup, U. *FX Options and Structured Products*, 2ª ed. | 2017 | — | dispensado |
| `clark-2011` | Clark, I. J. *Foreign Exchange Option Pricing*. | 2011 | — | dispensado |

- **Ano e ISBN do Haug:** vêm da editora, porque a página de copyright do PDF está em branco.
- **Wystup, 2ª ed.:** dispensada. A 1ª edição cobre todas as estruturas que buscávamos nela, exceto o condor. O calendar spread também falta na 1ª, mas está no Hull.
- **Clark:** dispensado. As convenções estão em `reiswich-wystup-2009` e em `wystup-2006` 1.2.6–1.2.7 e 1.3.5–1.3.6.
- **Natenberg:** é um escaneamento sem camada de texto. Não dá para buscar no arquivo; a leitura é por imagem, a partir das páginas abaixo.
- **Termos de uso do econstor:** o `reiswich-wystup-2009` só pode ser usado de forma pessoal e acadêmica. Não pode ser redistribuído.

### Seções relevantes (página impressa)

- **`wystup-2006`:**
  - 1.2.6, cotação: p. 8
  - 1.2.7, strike por delta: p. 10
  - 1.3.5–1.3.6, convenções de smile e ATM: pp. 25–26
  - 1.4, estratégias com vanillas: call/put spread p. 30, RR p. 31, straddle p. 33, strangle p. 35, butterfly p. 36, seagull p. 38
  - 1.5, exóticas de 1ª geração: barreiras p. 40; digitais e touch p. 49; compound p. 58; asiáticas p. 69
  - 1.6, exóticas de 2ª geração: corridors p. 101; faders p. 103; exotic barriers p. 105 (KIKO p. 115); pay-later p. 116; média harmônica p. 131
  - 2.1, forwards: outright p. 141, participating p. 142, fade-in p. 142, knock-out p. 143, shark p. 144, range p. 151, accumulative p. 156, auto-renewal p. 163, boosted p. 165, time option p. 166
  - 2.2.2, collar extra series: p. 172
  - 4.6, estudo de caso do forward plus: p. 272
  - 5.1.3, entrevista com a Bloomberg: p. 296
- **`hull-2015`:**
  - cap. 5, forwards: p. 104
  - cap. 10, opções: p. 213
  - 12.3, spreads: bull p. 258, bear p. 260, butterfly ~p. 263, calendar p. 265, diagonal p. 266
  - 12.4, combinações: straddle p. 267, strips/straps p. 268, strangle p. 269
  - 17.2, opções de moeda: p. 369; range forwards p. 370
  - 20.2, smile em FX: p. 433
  - cap. 26, exóticas: compound p. 602, barrier p. 604, binary p. 606, Asian p. 609
- **`haug-2007`:**
  - 4.7, fade-in: p. 122
  - 4.13, options on options: p. 132
  - 4.14, extendible: p. 138
  - 4.17, barreiras: padrão p. 152, dupla p. 156
  - 4.18.1, first-then-barrier: p. 169
  - 4.19, binárias: cash-or-nothing p. 174; binary barrier p. 176; double-barrier binary p. 180
  - 4.20, asiáticas: p. 182
- **`natenberg-1994`:**
  - cap. 8, volatility spreads: straddle p. 141, strangle p. 143, butterfly p. 145, time (calendar) spread p. 148, diagonal p. 157
  - p. 157, Christmas tree
  - p. 158, iron butterfly e condor
  - cap. 10, bull/bear e vertical spreads: pp. 199–202
  - cap. 11, sintéticos, conversões/reversões e boxes: pp. 213–228
- **`reiswich-wystup-2009`:** tipos de delta (premium-adjusted ou não) p. 4; definições de ATM p. 8; conversão delta–strike p. 9; risk reversal pp. 12–14; butterfly e *market strangle* pp. 15–24.

## Cobertura por estrutura

✓ cobertura direta · ~ parcial ou a confirmar na leitura · — só o OVML

| Estruturas | Fontes (página impressa) | |
|---|---|---|
| CP | hull-2015 p. 258; wystup-2006 p. 30; natenberg-1994 p. 202 | ✓ |
| RR | wystup-2006 p. 31; reiswich-wystup-2009 pp. 12–14; hull-2015 p. 370 (com o nome "range forward") | ✓ |
| SD, SN | hull-2015 pp. 267, 269; wystup-2006 pp. 33, 35; natenberg-1994 pp. 141, 143 | ✓ |
| BF | wystup-2006 p. 36; natenberg-1994 pp. 145, 158; reiswich-wystup-2009 pp. 15–24 | ✓ |
| BFC | hull-2015 ~p. 263 | ✓ |
| SG | wystup-2006 p. 38 | ✓ |
| CS, DS | hull-2015 pp. 265–266; natenberg-1994 pp. 148, 157 | ✓ |
| PF | wystup-2006 p. 142 | ✓ |
| CR | natenberg-1994 p. 158 | ✓ |
| SDR, CASH, FP, BFW, TF | — | — |
| EU, AM | hull-2015 cap. 10 e p. 369 | ✓ |
| FX, FWD | hull-2015 p. 104; wystup-2006 p. 141 | ✓ |
| KO, KI | wystup-2006 p. 40; hull-2015 p. 604; haug-2007 p. 152 | ✓ |
| DKO, DKI | haug-2007 p. 156; wystup-2006 p. 40 | ✓ |
| OT, NT, DOT, DNT | wystup-2006 p. 49; haug-2007 pp. 176, 180 | ✓ |
| DIVA | wystup-2006 p. 49; hull-2015 p. 606; haug-2007 p. 174 | ✓ |
| DIKO, DIKI | haug-2007 p. 176; wystup-2006 p. 49 | ✓ |
| DIDKO, DIDKI | haug-2007 pp. 180–181 | ~ |
| KOKI, KIKOSQ | wystup-2006 p. 115; haug-2007 p. 169; wystup-fxcol-2025 | ✓ |
| DISEQ | haug-2007 p. 169 | ~ |
| EAKO | wystup-fxcol-2022; wystup-2006 p. 115 | ✓ |
| CMP | wystup-2006 p. 58; hull-2015 p. 602; haug-2007 p. 132 | ✓ |
| AVG | wystup-2006 p. 69; hull-2015 p. 609; haug-2007 p. 182 | ✓ |
| ARF, ASF | wystup-2006 p. 131; haug-2007 p. 182 | ~ |
| ARC | wystup-2006 pp. 69 + 31 | ~ |
| FA | wystup-2006 p. 103; haug-2007 p. 122 | ✓ |
| ACCR | wystup-2006 p. 101 | ✓ |
| DACCR | wystup-2006 p. 101 | ~ |
| ACCU | wystup-2006 p. 156 | ✓ |
| ACCUKI, ACCUKO | wystup-2006 p. 156 | ~ |
| FE | wystup-2006 pp. 144–145, 272; wystup-fxcol-2026 | ✓ |
| KOF | wystup-2006 p. 143 | ✓ |
| RF | wystup-2006 p. 151 | ✓ |
| FLEX | wystup-2006 p. 166 (time option) | ✓ |
| BFF | wystup-2006 pp. 142 + 165 | ~ |
| EF | wystup-2006 p. 163 (auto-renewal) | ~ |
| EC | wystup-2006 p. 172 (collar extra) | ~ |
| KKF | wystup-2006 p. 115 (KIKO) | ~ |
| 2L–10L | não precisam de fonte | |

As estruturas marcadas com "—" têm nome comercial, sem definição acadêmica. A nota de cada uma registra "fonte única: OVML".

## Divergências

**Confirmadas pela leitura:**
- **DS:** o `hull-2015` (p. 266) exige strike **e** vencimento diferentes. A Bloomberg diz "and/or".
- **RF:** o RF do OVML é o *range forward* do `wystup-2006` (p. 151): forward sintético + double-no-touch. O `hull-2015` (p. 370) usa o nome *range forward* para o collar, que no OVML é o RR.
- **FE:** o FE do OVML corresponde ao *forward plus* do `wystup-2006` (p. 145), em que o cliente ganha quando o spot anda a seu favor. O *forward extra* do Wystup é a variante oposta. O `wystup-fxcol-2026` confirma a distinção.
- **BF:** o "long Butterfly" do OVML (compra o strangle, vende o straddle) é o *short iron butterfly* do `natenberg-1994` (p. 158). O Natenberg mostra que ele equivale a um butterfly comprado, então o "long" do OVML está certo no resultado. O mesmo nome com "long" na frente (*long iron butterfly*) designa a posição oposta.
- **CR:** o `natenberg-1994` (p. 158) define o condor com um só tipo de opção, comprando as duas pontas e vendendo os dois strikes internos. O CR do OVML monta a mesma coisa com strangles. Pela mesma equivalência do iron butterfly, os dois têm o mesmo resultado, e o "long" coincide.
- **BFW:** o `wystup-2006` (p. 151) usa *bonus forward* como sinônimo de range forward. O BFW do OVML é outra estrutura (KO + KI − reverse KI).
- **KOKI e KIKOSQ:** o `wystup-2006` (p. 115) separa três tipos de KIKO. O KOKI é o tipo em que o KO pode ocorrer a qualquer momento; o KIKOSQ é o tipo em que o KO só ocorre depois do KI.

**A conferir na leitura:**
- **EF:** comparar com o auto-renewal forward (`wystup-2006` p. 163). Não confundir com as "options with extendible maturities" (`haug-2007` p. 138).
- **EC:** comparar com a collar extra series (`wystup-2006` p. 172).
- **EAKO:** conferir a convenção ITM/OTM das barreiras.
- **DIDKO, DIDKI:** conferir se o Haug cobre a condição de strike além das duas barreiras.
