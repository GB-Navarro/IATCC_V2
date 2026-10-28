# Validação D38 — taxonomia UPI
Validador: agente independente · 2026-10-23 · método: leitura integral do `dsb-2018` (20 pp.) e das abas Index, FISN, Version History e dos templates 054, 072–078, 097–103 e 110 do `dsb-2024`; das 66 notas e dos textos da Bloomberg; do `wystup-2006` (pp. 49–50, 156, 166–167); e contagens na amostra DTCC de 2026-10-21 (61.562 registros), com os scripts desta pasta.

## Resumo

| Decisão | Veredito | Em uma linha |
|---|---|---|
| 1 — regra de categoria pelo produto UPI | ✗ | O produto UPI não determina o payoff: o exemplo da DSB para Option.Non_Standard é Vanilla, e o NDO aceita Asian. Além disso, a lista termina em "etc.". A distribuição que resulta para as 66 notas está quase toda certa (só FLEX fica em aberto). |
| 1 — Vanilla_Option e NDO como "vanilla" | ◐ | Só vale se o método de avaliação do NDO for Vanilla, e o FISN do NDO não mostra esse método. |
| 1 — contagem de pernas e cobertura | ✅ | As 66 notas aparecem uma vez cada, e o nº de linhas da tabela de pernas bate com a pasta em todas as 57 que têm tabela. |
| 3 — forwards estruturados em `exotica` | ◐ | `exotica` se sustenta pelo payoff, não pelo UPI. Forward ou Option.Non_Standard não muda a pasta. FLEX conflita com o próprio `payoff: linear`. |
| 4 — toques e digitais com barreira | ◐ | Digital_Option está certo e a pasta não muda. Digital Barrier é o encaixe para DIKO, DIKI, DIDKO e DIDKI, mas não é único para OT, NT, DOT e DNT. |
| 5 — FX e CASH em `linear` | ◐ | Não têm produto UPI, e `linear` está certo. Mas "não aparecem no DTCC" está errado como dito: forwards de prazo ≤ 2 dias e campos "Other payment" aparecem. |

## Decisão 1 — regra de categoria

- **Veredito:** ✗ para o critério ("a categoria vem do produto UPI"). A pasta que ele dá para cada nota está quase toda certa (ver "Nota a nota").
- **A favor:**
  - A matriz ISDA da DSB separa "Vanilla Option", "Simple Exotic" (Barrier, Digital, Vol/Var) e "Exotic" (Target, Forward Vol Agreement) [dsb-2018, p. 6].
  - Barrier_Option tem método de avaliação fixo, "Barrier" ("Fixed value") [dsb-2024, aba 097 (Rec)]. Digital_Option só aceita [Digital (Binary), Digital Barrier] [dsb-2024, aba 098 (Req)]. Vanilla_Option tem método fixo "Vanilla" e subjacente fixo "Spot" [dsb-2024, aba 103 (Rec)]. Para esses três produtos, o produto já define a família.
  - Cobertura: as 66 notas estão no plano, sem repetição. O nº de linhas da tabela de pernas é igual ao N da pasta em todas as notas com tabela (método: `cobertura.py`).
- **Contra / contraexemplos:**
  1. **Non_Standard não implica exótica.** O exemplo da própria DSB para Option.Non_Standard tem método "Vanilla" e CFI HFTDVP [dsb-2024, aba 101 (Req) e (Rec)]. É o mesmo CFI do exemplo de Vanilla_Option [dsb-2024, aba 103 (Rec)].
     - Na amostra, 129 dos 179 registros `FX O Nstd` (72 %) são em CNY.
     - Os grupos com o mesmo horário são combinações de vanillas. Exemplos: call e put no mesmo strike e vencimento, CNY EUR, às 10:07:50 e às 05:54:43 (straddle); call e put em strikes diferentes, CNY USD, às 12:01:25 e às 20:29:25 (strangle/RR). Método: `onstd_grupos.py`.
     - Pela regra, esses grupos iriam para `exotica`, mas são SD e SN/RR.
     - O mesmo acontece com o FWD: 74 dos 298 `FX Fwd Nstd` são em CNY e 66 em metais (XAU, XAG, XPD, XPT).
  2. **NDO não implica vanilla.** O método de avaliação do NDO aceita [Vanilla; Asian; Lookback; etc.] [dsb-2024, aba 100 (Req)]. Um AVG ou ARC não entregável seria NDO (Asian) e, pela regra, iria para `vanilla`. A matriz de 2018 trata o NDO como produto-base próprio, separado de "Vanilla Option" [dsb-2018, p. 6].
  3. **A lista de exóticos termina em "etc.".**
     - 8 dos 17 produtos de FX ficam sem categoria: Vol_Var, Forward_Vol_Agreement, Contract_For_Difference, Rolling_Spot, Spreadbet, FX_Swap, Non_Deliverable_FX_Swap e TARF [dsb-2024, aba Index].
     - Na amostra aparecem também FISNs que não seguem nenhum formato da aba FISN: `Oth Oth Nstd` (33), `Ot Ot Oth` (13) e `FX Op Spt Eu* DgBr Cs` (14). Há ainda 846 FX swaps. Método: `contar_fisn2.py`.
  4. **O agente não consegue ver o método de avaliação.** Em 61.562 de 61.562 registros, as colunas Option Type, Option Style, Delivery Type e Product name estão vazias. Só o FISN identifica o produto, e o FISN do NDO e o do Non_Standard não trazem o método [dsb-2024, aba FISN].
  5. **Há notas com dois UPIs plausíveis que levam a pastas diferentes:**
     - FLEX: Forward → `linear`; Forward.Non_Standard → `exotica`;
     - AVG e ARC não entregáveis: NDO → `vanilla`;
     - toda combinação de vanillas em CNH (Non_Standard) → `exotica`.
- **Ajuste proposto:**
  - Definir a categoria pelo payoff de cada perna, usando o método de avaliação do CFI [dsb-2018, p. 5]:
    - V → `vanilla`;
    - A, D, B, G, L, P, M → `exotica`;
    - forward de payoff linear → `linear`.
  - O campo `upi` lista todos os produtos plausíveis de cada perna. Exemplo, para EU: `Vanilla_Option | NDO | Option.Non_Standard`.
  - Mapear os 17 produtos sem "etc.". Instruir o agente a não restringir a busca a uma pasta quando o grupo tiver `Nstd`, `NDO` ou um FISN fora da aba FISN.
  - A distribuição proposta pode ficar como está. Só FLEX precisa de uma decisão explícita.
- **Vanilla_Option e NDO juntos:** ◐. O agrupamento vale para NDO com método Vanilla, que é o exemplo de 2018 [dsb-2018, p. 8]. Não vale para NDO Asian ou Lookback [dsb-2024, aba 100 (Req)], e o DTCC não permite distinguir os dois casos (contra 4).
- **Fonte:** a planilha citada como `dsb-2024` está na versão 9, de 2026-08-07, e não na versão 6. O template TARF (110) entrou na versão 8, de 2026-06-26 [dsb-2024, aba Version History; datas seriais do Excel convertidas].

## Decisão 3 — forwards estruturados

- **Veredito:** ◐
- **Forward.Non_Standard × Option.Non_Standard:**
  - **Forward (075):**
    - subjacente [Spot; Forward; Options; Futures];
    - gatilho [Spreadbets; CFD; Forward price; Rolling spot];
    - entrega [CASH; PHYS];
    - não tem tipo, estilo nem método de avaliação; CFI JFTXFP [dsb-2024, aba 075 (Req) e (Rec)].
  - **Opção (101):**
    - subjacente [Forwards; Futures; Spot; Volatility; Other];
    - tipo e estilo condicionais;
    - método de avaliação obrigatório [Vanilla; Asian; Barrier; etc.];
    - entrega [CASH; PHYS; OPTL] [dsb-2024, aba 101 (Req)].
  - **Diferença:** nenhum dos dois tem definição em prosa; o que os separa é o tipo de instrumento (J × H).
  - **Onde cai cada um:**
    - Pelo texto da Bloomberg ("is a forward"), os 8 caem em Forward.Non_Standard.
    - Só o template de opção tem atributo para média e barreira. Por isso, Option.Non_Standard também é plausível para ARF, ASF, ACCUKI e ACCUKO.
    - A marca ⚖ está correta.
- **A escolha muda a pasta?** Entre os dois Non_Standard, não: os dois vão para `exotica` pela regra. Entre Non_Standard e o Forward simples, muda, e isso afeta FLEX.
- **A favor de `exotica`:**
  - A matriz ISDA da DSB põe o Vol_Var em "Simple Exotic", e ele é um instrumento forward (CFI JFRXFC) [dsb-2018, pp. 6, 13]. Há, portanto, precedente para um forward exótico.
  - O accumulative forward é "a (usually) zero cost forward enhancement without a guaranteed worst case", com acumulação por fixing e knock-out [wystup-2006, p. 156]: o payoff não é linear.
- **Contra / contraexemplos:**
  - **O rótulo "forward" da DSB não prevê como o negócio é reportado.** O TARF tem template Forward [dsb-2024, aba 110 (Req)]. Mesmo assim, os 33 TARFs da amostra aparecem como Target_Option (`O Targ`), e nenhum como `Fwd TARF` (contagem do FISN).
  - **Na amostra, `FX Fwd Nstd` é quase sempre um forward simples:**
    - 167 dos 298 têm prazo ≤ 2 dias;
    - 66 são em metais e 74 em CNY;
    - só 3 têm strike;
    - 9 têm `Embedded Option type` = OTHR: uma tira mensal em MXN, talvez um forward de janela.

    Método: `nstd_detalhe.py` e `spot_cash.py`. O UPI Non_Standard, portanto, não justifica `exotica`; quem justifica é o payoff.
  - **FLEX:** a nota tem `payoff: linear` [hull-2015, p. 7], mas a pasta proposta é `exotica`.
    - O Wystup define a time option como "American style forward contract" e diz que ela é "just like an American style call, except that the entire amount must be exercised" [wystup-2006, pp. 166–167]: há opção sobre a data.
    - Reportada como Forward com a data final, ela cairia em `linear`.
- **Ajuste proposto:**
  - Manter ACCU, ACCUKI, ACCUKO, ARF, ASF, EF e BFF em `exotica`, com a justificativa no payoff. O campo `upi` deles fica `Forward.Non_Standard | Option.Non_Standard`.
  - FLEX: resolver o conflito entre `payoff: linear` e a pasta `exotica`. Minha preferência é `linear` com UPI `Forward | Forward.Non_Standard`. Se ficar em `exotica`, a justificativa deve ser a opção de data [wystup-2006, p. 167].

## Decisão 4 — toques e digitais com barreira

- **Veredito:** ◐
- **O que a definição diz:**
  - A DSB não define os termos em prosa. Há só os rótulos do CFI: "D Digital (Binary)", "B Barrier" e "G Digital Barrier" [dsb-2018, p. 5].
  - O Digital_Option enumera "[Digital (Binary), Digital Barrier]" [dsb-2024, aba 098 (Req)].
  - Portanto, dizer que um toque "cabe em Digital Barrier" é uma inferência, não algo que se possa citar.
- **A favor:**
  - Barrier_Option fica excluído porque o método dele é fixo, "Barrier" [dsb-2024, aba 097 (Rec)].
  - Para DIKO, DIKI, DIDKO e DIDKI (pagamento fixo, strike e barreira), o encaixe direto é Digital_Option com o método Digital Barrier.
  - Na amostra, o método aparece em `O DigBar Put/Call/O` (32 registros) e em `FX Op Spt Eu* DgBr Cs` (14). Dos 28 `DigBar Put`, 21 têm o 1º exercício antes do vencimento, comportamento de produto americano (método: `nstd_detalhe.py`).
- **Contra / contraexemplos:**
  - **Toques.** O Wystup chama o one-touch de "(American style) binary or digital options" e diz que ele pode ser visto "either … as the rebate portion of a knock-out barrier option or as an American cash-or-nothing digital option" [wystup-2006, pp. 49–50]. Digital (Binary) com exercício americano é, então, tão plausível quanto Digital Barrier.
  - Na amostra, `O Dig O` (Digital (Binary), tipo OPTL) tem 16 registros. Desses, 7 têm strike 0 e 7 têm o 1º exercício antes do vencimento: perfil de toque.
  - O Option.Non_Standard também aceita o método Barrier [dsb-2024, aba 101 (Req)]. É uma alternativa para DISEQ, DIDKO e DIDKI.
  - **DISEQ:** a descrição da Bloomberg tem uma linha, e o UPI não pode ser determinado.
- **Ajuste proposto:**
  - OT, NT, DOT, DNT: `upi` = `Digital_Option (Digital Barrier | Digital (Binary), AMER, OPTL)`. O matching não deve depender do método.
  - DISEQ: `upi` = `Digital_Option | Option.Non_Standard`.
  - A pasta fica `exotica` em todas as alternativas.

## Decisão 5 — FX spot e CASH

- **Veredito:** ◐
- **A favor:**
  - Não há produto UPI para spot nem para pagamento em dinheiro. Os 17 produtos de FX são swaps, forwards e opções [dsb-2024, aba Index].
  - O Rolling_Spot não é spot: é um forward com vencimento em 9999-12-31 e liquidação CASH [dsb-2018, p. 16].
  - O payoff do FX é linear, então `linear` é coerente.
- **Contra / contraexemplos:** a nota "não aparecem no DTCC" está errada como dita.
  - Há registros de forward com prazo (vencimento − execução) ≤ 2 dias corridos: 41 `Fwd`, 167 `FX Fwd Nstd` e 1.052 `Fwd NDF`. Um FX à vista, se reportado, viria assim, sem como distingui-lo do FWD.
  - Pagamentos em dinheiro aparecem como atributo "Other payment" de outro registro, nunca como registro próprio. São 359 registros: `PEXH;PEXH` 320, `UFRO` 37 e `UWIN` 2; 357 deles em swaps e 2 em vanillas.
  - Método: `spot_cash.py`.
- **Ajuste proposto:** trocar a nota por "sem produto UPI próprio; se reportado, o FX aparece como Forward/NDF de prazo ≤ 2 dias, e o CASH como campo Other payment de outro registro".

## Nota a nota

Em todas as notas com Vanilla_Option ou Forward, a variante em CNH seria Option.Non_Standard ou Forward.Non_Standard, que a regra manda para `exotica` (Decisão 1, contra 1). Isso não se repete por linha.

| COD | Pasta proposta | UPI por perna (seu) | Concorda? | Comentário |
|---|---|---|---|---|
| EU | vanilla/1 | Vanilla_Option (EURO); NDO se não entregável | Sim | |
| AM | vanilla/1 | Vanilla_Option (AMER) | Sim | |
| FP | vanilla/1 | Vanilla_Option | Sim | O template não tem atributo de prêmio [dsb-2024, aba 103 (Req)]. Que o payoff é vanilla, a nota infere. |
| CP | vanilla/2 | Vanilla_Option ×2 | Sim | |
| RR | vanilla/2 | Vanilla_Option ×2 | Sim | Na amostra, pares CNY USD em `O Nstd` com strikes diferentes. |
| SD | vanilla/2 | Vanilla_Option ×2 | Sim | Na amostra, straddles CNY EUR como `O Nstd` ×2, que a regra mandaria para `exotica`. |
| SN | vanilla/2 | Vanilla_Option ×2 | Sim | |
| SDR | vanilla/2 | Vanilla_Option ×2 | Sim | |
| PF | vanilla/2 | Vanilla_Option ×2 | Sim | |
| CS | vanilla/2 | Vanilla_Option ×2 | Sim | |
| DS | vanilla/2 | Vanilla_Option ×2 | Sim | |
| TF | vanilla/2 | Forward ou NDF + Vanilla_Option | Sim | |
| SG | vanilla/3 | Vanilla_Option ×3 | Sim | |
| BFC | vanilla/3 | Vanilla_Option ×3 | Sim | |
| COL | vanilla/3 | Vanilla_Option + Forward ou NDF + Vanilla_Option | Sim | |
| BF | vanilla/4 | Vanilla_Option ×4 | Sim | |
| CR | vanilla/4 | Vanilla_Option ×4 | Sim | |
| KO | exotica/1 | Barrier_Option | Sim | |
| KI | exotica/1 | Barrier_Option | Sim | |
| DKO | exotica/1 | Barrier_Option | Sim | |
| DKI | exotica/1 | Barrier_Option | Sim | |
| KOKI | exotica/1 | Barrier_Option, ou Option.Non_Standard (Barrier) | Sim | A pasta é a mesma nas duas. |
| KIKOSQ | exotica/1 | Barrier_Option, ou Option.Non_Standard (Barrier) | Sim | A pasta é a mesma nas duas. |
| EAKO | exotica/1 | Barrier_Option, ou Option.Non_Standard (Barrier) | Sim | A pasta é a mesma nas duas. |
| DIVA | exotica/1 | Digital_Option (Digital (Binary)) | Sim | |
| DIKO | exotica/1 | Digital_Option (Digital Barrier) | Sim | |
| DIKI | exotica/1 | Digital_Option (Digital Barrier) | Sim | |
| DIDKO | exotica/1 | Digital_Option (Digital Barrier), ou Option.Non_Standard | Sim | |
| DIDKI | exotica/1 | Digital_Option (Digital Barrier), ou Option.Non_Standard | Sim | |
| OT | exotica/1 | Digital_Option (Digital Barrier ou Digital (Binary) AMER, OPTL) | Sim | Na pasta, sim; o método é ambíguo [wystup-2006, pp. 49–50] (`O Dig O` na amostra). |
| NT | exotica/1 | Digital_Option (Digital Barrier ou Digital (Binary) AMER, OPTL) | Sim | Mesma ambiguidade de método do OT. |
| DOT | exotica/1 | Digital_Option (Digital Barrier ou Digital (Binary) AMER, OPTL) | Sim | Mesma ambiguidade de método do OT. |
| DNT | exotica/1 | Digital_Option (Digital Barrier ou Digital (Binary) AMER, OPTL) | Sim | Mesma ambiguidade de método do OT. |
| DISEQ | exotica/1 | Digital_Option ou Option.Non_Standard | Sim | O UPI não pode ser determinado: a descrição tem uma linha. |
| CMP | exotica/1 | Option.Non_Standard (subjacente Other) | Sim | A Vanilla_Option tem subjacente fixo Spot [dsb-2024, aba 103 (Rec)]. |
| AVG | exotica/1 | Option.Non_Standard (Asian); NDO (Asian) se não entregável | ⚖ | Pela regra, o NDO vai para `vanilla`; pelo payoff, `exotica` (Decisão 1, contra 2). |
| FA | exotica/1 | Option.Non_Standard | Sim | |
| ACCR | exotica/1 | Option.Non_Standard ou Digital_Option | Sim | A pasta é a mesma nos dois. |
| DACCR | exotica/1 | Option.Non_Standard ou Digital_Option | Sim | A pasta é a mesma nos dois. |
| ACCU | exotica/1 | Forward.Non_Standard ou Option.Non_Standard | Sim | |
| ACCUKI | exotica/1 | Forward.Non_Standard ou Option.Non_Standard (Barrier) | Sim | |
| ACCUKO | exotica/1 | Forward.Non_Standard ou Option.Non_Standard (Barrier) | Sim | |
| ARF | exotica/1 | Forward.Non_Standard ou Option.Non_Standard (Asian) | Sim | |
| ASF | exotica/1 | Forward.Non_Standard ou Option.Non_Standard (Asian) | Sim | |
| EF | exotica/1 | Forward.Non_Standard | Sim | |
| BFF | exotica/1 | Forward.Non_Standard ou Option.Non_Standard | Sim | |
| FLEX | exotica/1 | Forward (com a data final) ou Forward.Non_Standard | ⚖ | Como Forward, iria para `linear`. A nota tem `payoff: linear`, e a pasta contradiz isso (Decisão 3). |
| FE | exotica/2 | Vanilla_Option + Barrier_Option | Sim | |
| EC | exotica/2 | Vanilla_Option + Barrier_Option | Sim | |
| KOF | exotica/2 | Barrier_Option ×2 | Sim | |
| KKF | exotica/2 | Barrier_Option ×2 | Sim | |
| ARC | exotica/2 | Option.Non_Standard (Asian) ×2; NDO (Asian) ×2 se não entregável | ⚖ | Pela regra, o NDO vai para `vanilla`; pelo payoff, `exotica`. |
| BFW | exotica/3 | Barrier_Option ×3 | Sim | |
| RF | exotica/3 | Vanilla_Option ×2 + Digital_Option | Sim | O método do DNT tem a mesma ambiguidade da Decisão 4. |
| FX | linear/1 | sem produto; se reportado, Forward ou NDF de prazo ≤ 2 dias | Sim | A nota "não aparecem no DTCC" precisa ser reescrita (Decisão 5). |
| FWD | linear/1 | Forward; NDF; Forward.Non_Standard (CNH, metais) | Sim | Como Forward.Non_Standard, iria para `exotica` pela regra. |
| CASH | linear/1 | sem produto; aparece só como campo Other payment | Sim | A nota precisa ser reescrita (Decisão 5). |
| 2L | generica | indefinido | Sim | |
| 3L | generica | indefinido | Sim | |
| 4L | generica | indefinido | Sim | |
| 5L | generica | indefinido | Sim | |
| 6L | generica | indefinido | Sim | |
| 7L | generica | indefinido | Sim | |
| 8L | generica | indefinido | Sim | |
| 9L | generica | indefinido | Sim | |
| 10L | generica | indefinido | Sim | |

## Não verificado

- **Definições em prosa dos produtos e dos métodos de avaliação:** a planilha remete a um "Product Definition document" que não está em `fontes/`, e o texto da ISO 10962 também não está disponível. ?
- **Método de avaliação dos registros NDO e Non_Standard da amostra:** o CFI não é público. ?
- **Que os registros `Oth Oth Nstd` (prêmio zero, notional pequeno, package) e a tira em MXN com OTHR sejam accumulators e forwards de janela:** é só um indício. ?
- **Como cada dealer registra os forwards de melhoria (PF, TF, FE, KOF, RF, BFW):** se decomposto ou num único registro. Isso mudaria o nº de pernas, não a pasta. ?
