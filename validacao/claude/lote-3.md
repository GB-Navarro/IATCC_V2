# Validação do Claude — lote 3

Validador: agente independente (Claude) · 2026-10-22 · cada citação conferida na página impressa inteira (texto via PyMuPDF; Haug pp. 156, 169, 177–180 e Wystup p. 116 conferidos também pela imagem), OVML lido em `bloomberg_description/`, citações literais comparadas palavra por palavra.

## Resumo

| ✅ | ◐ | ✗ | ⚖ | ? | total |
|---|---|---|---|---|---|
| 131 | 20 | 2 | 11 | 0 | 164 |

## Status das correções (aplicadas pelo Claude principal, 2026-10-22)

Os vereditos abaixo valem para as notas **antes** das correções.

| Status | Itens |
|---|---|
| ✎ aplicada | 3–8, 10–13, 16–18, 21 (exceto o Wystup p. 86 do FP: lá, "deferred premium" aparece no contexto de forward start, não define o FP) |
| ✎ aplicada com ajuste | 1: a cobertura do DACCR continua "~", porque o corridor (p. 101) é a parte de acumulação; a Nota agora cita a p. 101 e diz que falta a condição no vencimento |
| — sem ação | 15 |
| ✎ decidida pelo usuário | 2, 9, 14, 19, 20, 22 (D36, D37) |

## Correções propostas

**Prioridade 1**

1. **DACCR** · Notas "Fonte única": a premissa citada contradiz a conclusão. A cobertura por estrutura em `fontes/README.md` marca DACCR como "~" com "wystup-2006 p. 101", e não como "—". · Trocar `[inferência: cobertura por estrutura em fontes/README.md]` por `[inferência: wystup-2006, p. 101 define só o corridor (ACCR), sem condição no vencimento; nenhuma outra fonte de fontes/ trata o digital accrual]` e alinhar a linha DACCR da cobertura ("~" → "—"). Se o usuário considerar o p. 101 uma cobertura parcial, a Nota cai.
2. **FP** · Payoff `vanilla` com `[ovml]`: o OVML diz só "An option payoff"; não fala em vanilla. Contra: wystup-2006, p. 118, "the pay-later effect can be extended beyond vanilla options to all kind of options". · Trocar `[ovml]` por `[inferência: o OVML diz só "an option payoff"; vanilla é a suposição padrão]` e confirmar com o usuário. A mesma suposição sustenta "a tabela mostra a call".

**Prioridade 2**

3. **OT** · Barreira: `[wystup-2006, p. 50]` não sustenta o rótulo ki. A página liga o OT ao knock-out ("the rebate portion of a knock-out barrier option"). · Trocar `[wystup-2006, p. 50]` por `[haug-2007, pp. 177–178]`: os itens 1–2 e 5–6 chamam o one-touch de "Down-and-in cash-(at-hit / at-expiration)-or-nothing".
4. **NT** · Barreira: mesmo problema; a p. 50 liga o NT ao rebate de um knock-in. · Trocar `[wystup-2006, p. 50]` por `[haug-2007, p. 178]`, itens 9–10 "Down-and-out cash-or-nothing".
5. **KOKI** · Restrição: a fórmula é dada para um exemplo (L = barreira KO inferior, U = barreira KI superior), e a nota não define L nem U. · Reescrever como "KIKO(L, U) = KO(L) − DKO(L, U), com L = barreira KO e U = barreira KI [wystup-2006, p. 116]". O livro tem um erro de digitação ("U be a knock-out barrier"); a frase seguinte mostra que U é a barreira KI. Opcional, para o caso geral: `[wystup-fxcol-2022, p. 2]` ("a KIKO can be decomposed into single knock-out (-KO) and double-knock-out barrier option (-DKO) options").
6. **KIKOSQ** · Sinônimo "first-then-barrier option": o termo é mais amplo e inclui as versões out (haug-2007, p. 170, "First-down-then-up-and-out call"). · Trocar por "o KIKI sequencial é uma first-then-in barrier option (ex.: first-down-then-up-and-in call)" [haug-2007, p. 169].
7. **DIKO, DIKI, DACCR** · Variante de: o texto da Bloomberg não cita a estrutura-base. A relação vem da comparação de dois textos, que nas notas DKO, DKI, DOT, DNT, DIDKO e DIDKI é citada como inferência. · Trocar `[ovml]` por `[inferência: comparação dos textos da Bloomberg do DIVA e do DIKO]` (DIKI e ACCR/DACCR, idem). Manter `[wystup-2006, p. 105]` em DIKO e DIKI.
8. **DKI** · Notas: a premissa "o DKO vale menos que o KO de uma barreira" ficou sem citação. · Incluir a premissa no colchete, por exemplo `[inferência: haug-2007, p. 156 (DKI = vanilla − DKO) + wystup-2006, p. 42 (KI = vanilla − KO) + o DKO é cancelado sempre que o KO com uma das suas barreiras é cancelado]`. Precisar também que se trata do "KI com uma das duas barreiras, mesmo strike e vencimento".
9. **DACCR** · Tabela de pernas: o strike `K1` não tem linha na tabela de origem e não combina com tipo `—`, porque "in-the-money" exige strike e direção. · Ou tipo `call` + "a tabela mostra a call" + linha Strikes `[ovml]` ("in-the-money at expiration"), ou strike `—`. Decisão do usuário.
10. **DISEQ** · Composição: `[ovml]` sustenta só "digital sequencial" ("Digital sequential option style."); "barreiras" não está no texto. · Reescrever como "digital sequencial [ovml]". Na Variante de, incluir no colchete a premissa do KIKOSQ, da qual "com barreiras sequenciais" depende.
11. **AVG** · Composição: a distinção average price × average strike está na Tabela 1.21, na p. 70. · Trocar `[wystup-2006, p. 69]` por `[wystup-2006, pp. 69–70]`.
12. **FA** · Composição: a p. 103 diz "options", e não "vanilla"; "definido no vencimento" está na p. 104. O Haug cobre só o fade-in com fixings dentro do intervalo. · Trocar `[wystup-2006, p. 103]` por `[wystup-2006, pp. 103–104]` e restringir o `[haug-2007, p. 122]` ao caso "dentro".
13. **CMP** · Strikes e Vencimento: `[ovml]` só nomeia o "C. Strike" e o "Comp Expiry"; o strike e o vencimento da vanilla ficam implícitos. · Opcional: `[hull-2015, pp. 602–603]`, já que o papel de K2 é descrito na p. 603.

**Prioridade 3**

14. **DISEQ** · Frontmatter: `barreiras: 2` sem `barreira` contradiz o schema ("ausente = sem barreira"). A tabela usa `—` (ausência) para tipo e strike, que o OVML não define (desconhecido). · Decisão do usuário.
15. **DKO, DKI, DOT, DNT** · O `[ovml]` é parcial nas linhas Barreira (o rótulo ki/ko e o "inferior e superior" não estão no texto) e no Payoff do DNT ("pago no vencimento"). · Sem ação obrigatória: o Haug e o Wystup, na mesma linha, cobrem o restante.
16. **DIDKO, DIDKI, DISEQ** · Só têm o OVML como fonte, mas não têm a Nota "Fonte única", ao contrário de DACCR e FP. · Uniformizar.
17. **OT** · Restrição: "a alternativa" endurece "Another common practice". · Trocar por "outra prática comum".
18. **EAKO** · Omissão: o OVML diz "The user can select if they want the payout to happen if spot is either above or below the European barrier on expiration", e isso afeta a direção do KI. · Registrar em Restrições `[ovml]`.
19. **CMP** · O tipo `call` é o da compound; o tipo da vanilla subjacente não aparece, embora existam quatro tipos (hull-2015, p. 602; haug-2007, pp. 132–133). O estilo padrão é europeu (wystup-2006, p. 60). · Decisão do usuário.
20. **FA, ACCR, DACCR** · O OVML do FA chama os limites de "upper and lower barrier", e o Wystup (p. 102) chama L e H de barreiras do corridor; as notas não têm `barreira`. · Confirmar a decisão com o usuário.
21. **Evidência direta não aproveitada:**
    - DKO e DKI, Variante de: wystup-2006, p. 40, "knock in or out if the underlying hits a barrier (or one of two barriers)".
    - DIVA, sinônimo: haug-2007, p. 174, "Binary options, aka digital options" e 4.19.2.
    - KO e KI: wystup-2006, p. 43, "Traditionally barrier options are of American style".
    - FP: wystup-2006, p. 86, "deferred premium".
22. **KOKI** · O alias "KIKO" pode colidir com o KIKOSQ; o Wystup (p. 116) diz "one should always clarify which type of knock-in-knock-out is agreed upon". · Decisão do usuário.

## KO

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: vanilla que deixa de existir se tocar a barreira; call | `[ovml]` | ✅ | "unless the spot hits the specified barrier level … the option is knocked out and becomes worthless" |
| 〃 | `[hull-2015, p. 604]` | ✅ | "A knock-out option ceases to exist when the underlying asset price reaches a certain barrier" |
| 〃 | `[wystup-2006, p. 40]` | ✅ | "at a pre-determined rate called the strike K provided the exchange rate never hits or crosses a pre-determined barrier level B" |
| Barreira: ko, uma | `[ovml]` | ✅ | "the specified barrier level"; "knocked out" |
| 〃 | `[hull-2015, p. 604]` | ✅ | "reaches a certain barrier" |
| Payoff: vanilla se não tocar | `[ovml]` | ✅ | "option to buy (sell) … at the specified strike price unless the spot hits" |
| 〃 | `[wystup-2006, p. 40]` | ✅ | "exercise the option only if at expiration time the spot is above the strike and if the spot has failed to touch the barrier" |
| Restr.: barreira americana ou europeia | `[wystup-2006, pp. 40, 42]` | ✅ | p. 42: "American barrier: valid at all times • European barrier: valid only at expiration time" |
| Restr.: regular OTM, reverse ITM | `[wystup-2006, p. 42]` | ✅ | "Regular knock out: the barrier is out of the money. Reverse knock out: the barrier is in the money." |
| Restr.: prêmio menor que a vanilla | `[ovml]` | ✅ | "lower than the premium for a similar Vanilla option" |
| 〃 | `[hull-2015, p. 604]` | ✅ | "less expensive than the corresponding regular options" (dito das barreiras em geral) |

**Verificações da nota:**
- Tabela de pernas: ✅.
- Frontmatter: ✅ ko / 1 / vanilla.
- Omissões/contradições: ◐ menor. A nota não diz que o padrão é a barreira americana com monitoramento contínuo (wystup-2006, p. 43); o Wystup também define "Strike out" (p. 42).

## KI

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: vanilla que só passa a existir se tocar; call | `[ovml]` | ✅ | "provided that the spot hits the specified barrier level … the option is never knocked in and expires worthless" |
| 〃 | `[hull-2015, p. 604]` | ✅ | "a knock-in option comes into existence only when the underlying asset price reaches a barrier" |
| 〃 | `[wystup-2006, p. 42]` | ✅ | "knock-in options only become alive, if the spot ever trades at or beyond the barrier" |
| Barreira: ki, uma | `[ovml]` | ✅ | "the specified barrier level"; "knocked in" |
| 〃 | `[hull-2015, p. 604]` | ✅ | "reaches a barrier" |
| Payoff: vanilla se tocar | `[ovml]` | ✅ | "option to buy (sell) … at the specified strike price provided that the spot hits" |
| Restr.: KO + KI = vanilla | `[wystup-2006, p. 42]` | ✅ | "Naturally, knock-out + knock-in = vanilla." Vale sem rebate e com exercício europeu (haug-2007, p. 155: a paridade não vale em geral para opções americanas). |
| Restr.: regular OTM, reverse ITM | `[wystup-2006, p. 42]` | ✅ | Legenda da Fig. 1.19: "regular barriers are out of the money, reverse barriers are in the money"; o texto define só para knock-out, a legenda generaliza |
| Restr.: prêmio menor | `[ovml]` | ✅ | "lower than the premium for a similar Vanilla option as there is a possibility that the option does not knockin" |

**Verificações da nota:**
- Tabela de pernas: ✅.
- Frontmatter: ✅ ki / 1 / vanilla.
- Omissões/contradições: ✅. A ressalva sobre rebate (wystup-2006, p. 43) é opcional.

## DKO

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: vanilla que deixa de existir se tocar qualquer de duas barreiras; call | `[ovml]` | ✅ | "unless the spot hits one of the two specified barrier levels" |
| 〃 | `[haug-2007, p. 156]` | ✅ | "knocked either in or out if the underlying price touches the lower boundary L or the upper boundary U prior to expiration" |
| Barreira: ko, duas (inferior e superior) | `[ovml]` | ◐ | Sustenta ko e duas barreiras, mas não "inferior e superior" |
| 〃 | `[haug-2007, p. 156]` | ✅ | "lower boundary L or the upper boundary U" |
| Payoff: vanilla se nenhuma for tocada | `[ovml]` | ✅ | "option to buy (sell) … at the specified strike price unless the spot hits one of the two" |
| 〃 | `[haug-2007, p. 156]` | ✅ | "Payoff: c(S, U, L, T) = max(S − X; 0) if L < S < U before T else 0" |
| Variante de: KO com duas barreiras | `[inferência: textos KO e DKO]` | ⚖ | Os textos são idênticos, exceto "one of the two specified barrier levels"; a premissa é verdadeira. Fonte direta não usada: wystup-2006, p. 40, "(or one of two barriers)". |

**Verificações da nota:**
- Tabela de pernas: ✅.
- Frontmatter: ✅ ko / 2 / vanilla; `variante_de` KO.
- Omissões/contradições: ✅.

## DKI

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: vanilla que só existe se tocar uma de duas barreiras; call | `[ovml]` | ✅ | "provided that the spot hits one of the two specified barrier levels" |
| 〃 | `[haug-2007, p. 156]` | ✅ | "knocked either in or out if the underlying price touches the lower boundary L or the upper boundary U" |
| Barreira: ki, duas (inferior e superior) | `[ovml]` | ◐ | Não diz "inferior e superior" |
| 〃 | `[haug-2007, p. 156]` | ✅ | "lower boundary L or the upper boundary U" |
| Payoff: vanilla se alguma for tocada | `[ovml]` | ✅ | "option to buy (sell) … provided that the spot hits one of the two" |
| Variante de: KI com duas barreiras | `[inferência: textos KI e DKI]` | ⚖ | Textos paralelos; premissa verdadeira |
| Restr.: = vanilla comprada + DKO vendido | `[haug-2007, p. 156]` | ✅ | "a long standard call and a short double knock-out call, with identical strikes and time to expiration" |
| Notas: a Bloomberg justifica pelas duas chances de nunca ativar | `[ovml]` | ✅ | "as there are two possibilities of the option never being knocked in" |
| Notas: citação literal do Haug | `[haug-2007, p. 156]` | ✅ | O literal confere com a imagem da página |
| Notas: o DKI vale mais que o KI | `[inferência: haug 156 + wystup 42]` | ⚖ | A lógica está certa (DKI = V − DKO ≥ V − KO = KI), mas a premissa "o DKO vale menos que o KO" não tem citação, e a comparação exige que o KI use uma das duas barreiras do DKI |

**Verificações da nota:**
- Tabela de pernas: ✅.
- Frontmatter: ✅ ki / 2 / vanilla.
- Omissões/contradições: ✅.

## OT

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: pagamento fixo se tocar antes do vencimento | `[ovml]` | ✅ | "a predetermined payoff if the spot hits the specified barrier level during the life of the option" |
| 〃 | `[wystup-2006, p. 50]` | ✅ | "pays a domestic cash amount R USD if a barrier B is hit any time before the expiration time" |
| Barreira: ki (o toque ativa), uma | `[ovml]` | ◐ | Sustenta uma barreira e que o toque ativa o pagamento; o rótulo ki é decisão de codificação |
| 〃 | `[wystup-2006, p. 50]` | ◐ | Sustenta uma barreira B e o pagamento no toque, mas não o ki; a página liga o OT ao knock-out: "the rebate portion of a knock-out barrier option" (também a p. 43). Usar haug-2007, p. 177, item 1, "Down-and-in cash-(at-hit)-or-nothing". |
| Payoff: toque | `[ovml]` | ✅ | "predetermined payoff if the spot hits" |
| Sinônimo: hit option, one-touch digital | `[wystup-2006, p. 50]` | ✅ | "In FX markets it is usually called a one-touch (option), one-touch-digital or hit option." |
| Restr.: pagamento na entrega (T+2); alternativa: toque + 2 | `[wystup-2006, p. 49]` | ✅ | "Another common practice is 2 business days after the touch event. In FX markets the former is the default." "A alternativa" endurece "another common practice". |

**Verificações da nota:**
- Tabela de pernas: ✅ (sem tipo e sem strike).
- Frontmatter: ⚖ ki / 1 / toque. O Haug (pp. 177–178) chama o one-touch de "down-and-in", o que sustenta a decisão; o Wystup, citado na nota, não sustenta.
- Omissões/contradições: ✅.

## NT

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: pagamento fixo se não tocar até o vencimento | `[ovml]` | ✅ | "if the spot does not hit the specified barrier level during the life of the option" |
| 〃 | `[wystup-2006, p. 50]` | ✅ | "a no-touch (option), R II{τB ≥ T} describes a rebate which is being paid if a knock-in-option has not knocked in by the time it expires" |
| Barreira: ko (o toque cancela), uma | `[ovml]` | ◐ | O rótulo ko é decisão de codificação |
| 〃 | `[wystup-2006, p. 50]` | ◐ | A página liga o NT ao rebate de um knock-in, sem sustentar o ko. Usar haug-2007, p. 178, itens 9–10, "Down-and-out cash-or-nothing". |
| Payoff: toque | `[ovml]` | ✅ | "predetermined payoff" |
| Variante de: OT invertido; OT + NT pagam com certeza | `[wystup-2006, p. 50]` | ✅ | (1.114): "R II{τB≤T} + R II{τB>T} = R" |

**Verificações da nota:**
- Tabela de pernas: ✅.
- Frontmatter: ⚖ ko / 1 / toque; como no OT.
- Omissões/contradições: ✅.

## DOT

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: pagamento fixo se tocar qualquer de duas barreiras | `[ovml]` | ✅ | "if the spot hits either of the specified barrier levels" |
| 〃 | `[wystup-2006, p. 40]` | ✅ | "Double one-touch and no-touch options work the same way but have two barriers." |
| 〃 | `[haug-2007, p. 180]` | ✅ | "A knock-in one-touch double-barrier pays off a cash amount K at maturity if the asset price touches the lower L or upper U barrier" |
| Barreira: ki, duas | `[ovml]` | ◐ | Duas barreiras, sim; o rótulo ki não está no texto |
| 〃 | `[haug-2007, p. 180]` | ✅ | "A knock-in one-touch double-barrier" |
| Payoff: toque | `[ovml]` | ✅ | "predetermined payoff if the spot hits" |
| Variante de: OT com duas barreiras | `[inferência: textos OT e DOT]` | ⚖ | Textos paralelos; premissa verdadeira |

**Verificações da nota:**
- Tabela de pernas: ✅.
- Frontmatter: ✅ ki / 2 / toque, sustentado pelo Haug.
- Omissões/contradições: ✅.

## DNT

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: pagamento fixo se não tocar nenhuma de duas barreiras | `[ovml]` | ✅ | "if the spot does not hit either of the specified barrier levels" |
| 〃 | `[wystup-2006, pp. 55–56]` | ✅ | (1.147) II{L ≤ min St < max St ≤ H}; "The lower barrier is denoted by L, the higher barrier by H" |
| 〃 | `[haug-2007, p. 180]` | ✅ | "a knock-out pays out a predefined cash amount K at maturity if the lower or upper barriers are not hit" |
| Barreira: ko, duas | `[ovml]` | ◐ | O rótulo ko não está no texto |
| 〃 | `[haug-2007, p. 180]` | ✅ | "If the asset price touches any of the barriers, the option vanishes." |
| Payoff: toque, pago no vencimento | `[ovml]` | ◐ | O OVML não diz quando paga |
| 〃 | `[wystup-2006, p. 56]` | ✅ | "is paid at maturity T" |
| Variante de: NT com duas barreiras | `[inferência: textos NT e DNT]` | ⚖ | Textos paralelos; premissa verdadeira |

**Verificações da nota:**
- Tabela de pernas: ✅.
- Frontmatter: ✅ ko / 2 / toque.
- Omissões/contradições: ✅.

## DIVA

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: pagamento fixo no vencimento acima (call) ou abaixo (put) do strike | `[ovml]` | ✅ | "provided the spot is greater (less) than the strike in the case of a call (put) option" |
| 〃 | `[hull-2015, pp. 606–607]` | ✅ | "pays off nothing if the asset price ends up below the strike price at time T and pays a fixed amount, Q, if it ends up above" |
| Payoff: digital | `[ovml]` | ✅ | "predetermined payoff on the expiry date" |
| 〃 | `[hull-2015, pp. 606–607]` | ✅ | "Binary options are options with discontinuous payoffs" (o Hull nunca usa "digital") |
| Sinônimo: cash-or-nothing | `[hull-2015, p. 606]` | ✅ | "A simple example of a binary option is a cash-or-nothing call"; a definição coincide com o OVML |

**Verificações da nota:**
- Tabela de pernas: ✅.
- Frontmatter: ✅ digital, sem barreira.
- Omissões/contradições: ✅. O haug-2007, p. 174 ("Binary options, aka digital options"; 4.19.2) não foi usado e é a fonte mais direta do par digital = cash-or-nothing.

## DIKO

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: digital que deixa de existir se tocar; call | `[ovml]` | ✅ | "and provided that the barrier has not been hit during the life of the option" |
| 〃 | `[wystup-2006, p. 105]` | ✅ | "digital calls and puts with additional American style knock-out or knock-in barriers" |
| 〃 | `[haug-2007, p. 179]` | ✅ | Itens 21–22 "Down-and-out cash-or-nothing call", "Up-and-out cash-or-nothing call" |
| Barreira: ko, uma | `[ovml]` | ✅ | "the barrier has not been hit" |
| 〃 | `[haug-2007, p. 179]` | ✅ | Uma barreira H nos itens 21–26 |
| Payoff: digital | `[ovml]` | ✅ | "predetermined payoff on the expiry date" |
| Variante de: DIVA com KO | `[ovml]` | ◐ | O texto não cita o DIVA; a relação vem da comparação de textos (ver item 7) |
| 〃 | `[wystup-2006, p. 105]` | ✅ | "Just like barrier options, which are calls or puts with knock-out or knock-in barriers, one can consider digital calls and puts with" barreiras |

**Verificações da nota:**
- Tabela de pernas: ✅.
- Frontmatter: ✅ ko / 1 / digital.
- Omissões/contradições: ✅.

## DIKI

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: digital que só existe se tocar; call | `[ovml]` | ✅ | "and provided that the barrier has been hit during the life of the option" |
| 〃 | `[wystup-2006, p. 105]` | ✅ | "digital calls and puts with additional American style knock-out or knock-in barriers" |
| 〃 | `[haug-2007, p. 178]` | ✅ | Itens 13–14 "Down-and-in cash-or-nothing call", "Up-and-in cash-or-nothing call" (as puts estão na p. 179) |
| Barreira: ki, uma | `[ovml]` | ✅ | "the barrier has been hit" |
| 〃 | `[haug-2007, p. 178]` | ✅ | Uma barreira H |
| Payoff: digital | `[ovml]` | ✅ | "predetermined payoff on the expiry date" |
| Variante de: DIVA com KI | `[ovml]` | ◐ | O texto não cita o DIVA; vem da comparação de textos |
| 〃 | `[wystup-2006, p. 105]` | ✅ | Idem DIKO |

**Verificações da nota:**
- Tabela de pernas: ✅.
- Frontmatter: ✅ ki / 1 / digital.
- Omissões/contradições: ✅.

## DIDKO

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: digital que deixa de existir se tocar qualquer de duas; call | `[ovml]` | ✅ | "provided that neither of the two specified barriers have been hit" |
| Barreira: ko, duas | `[ovml]` | ✅ | Idem |
| Payoff: digital | `[ovml]` | ✅ | "predetermined payoff on the expiry date provided that the spot is greater (less) than the strike" |
| Variante de: DIKO com duas barreiras | `[inferência: textos DIKO e DIDKO]` | ⚖ | Textos idênticos, exceto "the barrier" → "neither of the two specified barriers"; premissa verdadeira |

**Verificações da nota:**
- Tabela de pernas: ✅.
- Frontmatter: ✅ ko / 2 / digital.
- Omissões/contradições: ✅. O Haug 4.19.6 (pp. 180–181) trata só a barreira dupla sem strike, o que confirma que só o OVML define a estrutura. Falta a Nota "Fonte única" (item 16).

## DIDKI

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: digital que só existe se tocar uma de duas; call | `[ovml]` | ✅ | "provided that one of the two specified barriers have been hit" |
| Barreira: ki, duas | `[ovml]` | ✅ | Idem |
| Payoff: digital | `[ovml]` | ✅ | "predetermined payoff on the expiry date" |
| Variante de: DIKI com duas barreiras | `[inferência: textos DIKI e DIDKI]` | ⚖ | Textos paralelos; premissa verdadeira |

**Verificações da nota:**
- Tabela de pernas: ✅.
- Frontmatter: ✅ ki / 2 / digital.
- Omissões/contradições: como no DIDKO.

## DISEQ

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: digital com barreiras sequenciais | `[ovml]` | ◐ | O texto é só "Digital sequential option style."; "barreiras" não está nele |
| Barreira: duas, ativadas em sequência | `[inferência: KIKOSQ; haug-2007, p. 169]` | ⚖ | As premissas são verdadeiras (o KIKOSQ usa "Sequential" para barreiras em ordem; o Haug, p. 169, descreve barreiras em sequência), mas a conclusão é só plausível: o OVML do DISEQ não menciona barreira, e o número 2 vem da analogia |
| Payoff: digital | `[ovml]` | ✅ | "Digital" |
| Variante de: DIVA com barreiras sequenciais | `[inferência: texto da Bloomberg do DISEQ]` | ⚖ | "Digital" sustenta DIVA; "com barreiras sequenciais" depende da inferência anterior, sem premissa citada neste colchete |
| Notas: descrição de uma linha, sem tipo, strike nem barreiras | `[ovml]` | ✅ | Confere |

**Verificações da nota:**
- Tabela de pernas: ◐. O `—` em tipo e strike afirma ausência, mas o OVML só não define esses campos; um digital tem strike (DIVA).
- Frontmatter: ✗ de consistência: `barreiras: 2` sem `barreira` contradiz o schema ("ausente = sem barreira").
- Omissões/contradições: falta a Nota "Fonte única" (item 16).

## KOKI

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: knock-in cancelável pelo KO a qualquer momento; call | `[ovml]` | ✅ | "KOKIs (Non Sequentials) are knockin options that can knockout at any time." |
| 〃 | `[wystup-2006, p. 115]` | ✅ | "1. the knock-out can happen any time" |
| Barreira: kiko; o KO vale antes e depois do KI | `[ovml]` | ✅ | "A KOKI can knock out at any time before or after the KI trigger is reached" |
| 〃 | `[wystup-2006, pp. 115–116]` | ✅ | "barriers with both a knock-out and a knock-in barrier"; tipo 1 "can happen any time" |
| Payoff: vanilla | `[ovml]` | ✅ | Implícito em "knockin options" |
| Sinônimo: KIKO tipo 1, padrão de mercado | `[wystup-2006, pp. 115–116]` | ✅ | "The first one is the market standard" |
| Restr.: KIKO(L, U) = KO(L) − DKO(L, U) | `[wystup-2006, p. 116]` | ◐ | Dada para o exemplo "let the lower barrier L be a knock-out barrier and the upper barrier U be a knock-out [sic] barrier"; a nota não define L e U |

**Verificações da nota:**
- Tabela de pernas: ✅.
- Frontmatter: ✅ kiko / 2 / vanilla.
- Omissões/contradições: ✅. O alias "KIKO" é ambíguo (item 22).

## KIKOSQ

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: KIKO sequencial; KIKI sequencial; call | `[ovml]` | ✅ | "can knockout only once the knock-in barrier has traded"; "can be activated by another Knock-In barrier" |
| Barreira: kiko / dois ki; duas | `[ovml]` | ✅ | Confere |
| Payoff: vanilla | `[ovml]` | ✅ | "then the option becomes a vanilla" |
| Sinônimo: KIKO tipo 2 | `[wystup-2006, pp. 115–116]` | ✅ | "2. the knock-out can happen only after the knock-in"; "Knock-out events in the structure are only active after the structure knocks in" |
| Sinônimo: o KIKI sequencial é uma first-then-barrier | `[haug-2007, p. 169]` | ◐ | O exemplo do Haug ("first-down-then-up-and-in call") é o caso DownIn&UpIn, mas "first-then-barrier" inclui as versões out (p. 170); o termo exato é first-then-in |
| Notas: a Bloomberg reúne dois produtos | `[ovml]` | ✅ | "KIKO Sequential: …" e "KIKI Sequential: …" |
| Notas: "reached first" = o toque no DownIn antes do UpIn não conta | `[inferência: Bloomberg + haug 169]` | ⚖ | Leitura correta: consistente com "If thereafter, the DownIn is reached" e com o parágrafo do KIKO ("It is irrelevant if spot trades at the knock-out barrier first") |
| Notas: citação literal do Haug | `[haug-2007, p. 169]` | ✅ | O literal confere com a imagem. O caso do Haug (primeiro a de baixo, depois a de cima) é o parágrafo DownIn&UpIn do OVML |

**Verificações da nota:**
- Tabela de pernas: ✅.
- Frontmatter: ⚖ kiko / 2 / vanilla. Só cobre o KIKO sequencial, o que está declarado nas Notas.
- Omissões/contradições: ✅.

## EAKO

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: KO americano e KI europeu (só no vencimento); call | `[ovml]` | ✅ | "The first barrier is a knockout American barrier … The second barrier is a knock-in and is European meaning it is only live on expiry" |
| 〃 | `[wystup-fxcol-2022, p. 1]` | ✅ | "with an American knock-out (KOAM) barrier and a European knock-in barrier (KIEU)" ("only observed at maturity" está explícito só na p. 2) |
| Barreira: kiko; KO americano OTM, KI europeu ITM | `[ovml]` | ✅ | "This barrier is positioned out-the-money … and is positioned in-the-money" |
| Payoff: vanilla | `[ovml]` | ✅ | "An option to buy (sell) the notional amount … at the specified strike price" |
| Variante de: KOKI, caso especial de KIKO | `[ovml]` | ✅ | "A variation to a KIKO (Non sequential)" |
| 〃 | `[wystup-fxcol-2022, p. 1]` | ✅ | "It is a special case of a KIKO (knock-in-knock-out) option." (não diz o tipo) |
| Sinônimo: KOAMKIEU | `[wystup-fxcol-2022, p. 1]` | ✅ | A definição coincide com o OVML |
| Notas: transatlantic tem as duas barreiras KO | `[wystup-2006, p. 108]` | ✅ | "a call with strike K, a European style up-and-out H > K and an American style down-and-out at L ≤ K" |

**Verificações da nota:**
- Tabela de pernas: ✅.
- Frontmatter: ✅ kiko / 2 / vanilla; `variante_de` KOKI.
- Omissões/contradições: ◐. Falta a escolha do lado do pagamento em relação à barreira europeia (item 18).

## CMP

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: compound call/put = direito de comprar/vender a vanilla; call | `[ovml]` | ✅ | "A compound call (put) gives the right but not the obligation to buy (sell) a Vanilla option" |
| 〃 | `[wystup-2006, p. 58]` | ✅ | "A Compound call(put) option is the right to buy(sell) a vanilla option." |
| 〃 | `[hull-2015, p. 602]` | ✅ | "Compound options are options on options"; o Hull lista quatro tipos |
| Strikes: dois (o da compound = prêmio; o da vanilla) | `[ovml]` | ◐ | Só nomeia o "C. Strike" ("the Premium you would pay for the other option"); o strike da vanilla fica implícito |
| 〃 | `[hull-2015, p. 602]` | ✅ | "Compound options have two strike prices and two exercise dates"; o K2 é descrito na p. 603 |
| Vencimento: dois | `[ovml]` | ◐ | Só o "Comp Expiry" |
| 〃 | `[hull-2015, p. 602]` | ✅ | "two exercise dates" |
| Payoff: composto | `[ovml]` | ✅ | Opção sobre opção |
| 〃 | `[haug-2007, p. 132]` | ✅ | "4.13 Options on Options"; "Payoff: max[cBSM(S, X1, T2) − X2; 0]" |
| Restr.: prêmio em parcelas | `[wystup-2006, p. 58]` | ✅ | "allows the holder to pay the premium of the call option spread over time" |

**Verificações da nota:**
- Tabela de pernas: ◐. O K1 e o T1 não dizem se são os da compound ou os da vanilla; o tipo `call` é o da compound, e o da vanilla não aparece (item 19).
- Frontmatter: ✅ composto.
- Omissões/contradições: ◐ menor. O padrão é europeu (wystup-2006, p. 60), e a compound é mais cara que a vanilla (p. 59).

## AVG

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: average rate ou average strike; call | `[ovml]` | ✅ | "the payoff is the difference between the strike and the average spot price"; "the strike is the average spot price" |
| 〃 | `[hull-2015, pp. 609, 611]` | ✅ | p. 609: "average price call is max(0, Save − K)"; p. 611: "An average strike call pays off max(0, ST − Save)" |
| 〃 | `[wystup-2006, p. 69]` | ◐ | A p. 69 diz "options on the average"; os dois tipos estão na Tabela 1.21, p. 70 |
| Payoff: media | `[ovml]` | ✅ | "average spot price" |
| Sinônimo: opção asiática | `[hull-2015, p. 609]` | ✅ | "Asian options are options where the payoff depends on the arithmetic average" |
| 〃 | `[wystup-2006, p. 69]` | ✅ | "Asian Options are options on the average … Average options belong to the class of path dependent options." |
| Restr.: média geométrica, aritmética ou harmônica | `[wystup-2006, p. 69]` | ✅ | "We find geometric, arithmetic or harmonic average of prices." |
| Notas: a Bloomberg reúne dois produtos | `[ovml]` | ✅ | Dois parágrafos, um para cada |
| 〃 | `[hull-2015, p. 611]` | ✅ | "Another type of Asian option is an average strike option." |

**Verificações da nota:**
- Tabela de pernas: ◐ menor. O K1 só existe no average rate.
- Frontmatter: ✅ media.
- Omissões/contradições: ✅.

## FA

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: vanilla com notional definido no vencimento por fixings dentro (ou fora) | `[ovml]` | ✅ | "a Vanilla option, but its notional is determined at expiry … inside (outside) the upper and lower barrier" |
| 〃 | `[wystup-2006, p. 103]` | ◐ | "Faders are options, whose nominal is directly proportional to the number of fixings the spot stays inside or outside a pre-defined range"; não diz vanilla, e o "no vencimento" está na p. 104 |
| 〃 | `[haug-2007, p. 122]` | ◐ | Só o fade-in, com fixings dentro: "weighted by how many fixings the asset price were inside a predefined range (L, U)" |
| Notional: proporcional aos fixings que cumprem a condição | `[ovml]` | ✅ | "notional is accrued each time spot is inside (outside)" |
| 〃 | `[wystup-2006, pp. 103–104]` | ✅ | (1.290): "number of fixings inside the range / M" |
| Payoff: acumulativo | `[ovml]` | ✅ | "notional is accrued" |
| Restr.: fade-in começa em zero e cresce; fade-out começa cheio e diminui | `[ovml]` | ✅ | "A Fade In (Out) option's notional begins at zero (the amount entered into the Notional field) and increases (decreases)" |
| 〃 | `[wystup-2006, p. 103]` | ✅ | "progressive activation of the nominal … progressive deactivation" |

**Verificações da nota:**
- Tabela de pernas: ✅.
- Frontmatter: ⚖ acumulativo, sem `barreira`, embora o OVML fale em "barrier" (item 20).
- Omissões/contradições: ◐ menor. Os faders têm muitas vezes um intervalo de knock-out adicional (wystup-2006, p. 105).

## ACCR

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: pagamento em dinheiro que cresce a cada fixing dentro do intervalo | `[ovml]` | ✅ | "At each fixing, if spot is within the specified range, the payment grows by the accrual amount." |
| 〃 | `[wystup-2006, p. 101]` | ✅ | "proportional to the number of fixings inside a lower range and an upper range" |
| Notional: pagamento máximo / nº de fixings | `[ovml]` | ✅ | "The accrual amount is the maximum Payoff divided by the number of fixings." |
| 〃 | `[wystup-2006, p. 101]` | ✅ | "the holder receives n/N · notional" |
| Payoff: acumulativo | `[ovml]` | ✅ | "the payment grows" |
| Sinônimo: corridor | `[wystup-2006, p. 101]` | ✅ | A definição do European corridor coincide com o OVML |
| Restr.: europeia conta todos os fixings; americana para ao sair | `[wystup-2006, p. 102]` | ✅ | "all fixings inside the range count … even if some of the fixings are outside"; "only fixings count … that occurs before the first time the exchange rate leaves the range" |

**Verificações da nota:**
- Tabela de pernas: ✅.
- Frontmatter: ✅ acumulativo.
- Omissões/contradições: ✅. Na versão americana, o titular mantém o que acumulou (p. 102); há também outras variantes, opcionais.

## DACCR

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: acumula com os fixings; só paga se ITM no vencimento | `[ovml]` | ✅ | "the size of the payment depends on the value of spot at multiple fixings … makes the payment … if it is in-the-money at expiration" ("acumula" vem do nome) |
| Payoff: acumulativo, com condição digital | `[ovml]` | ✅ | Idem |
| Variante de: ACCR com condição ITM | `[ovml]` | ◐ | O texto não cita o ACCR; a 1ª frase é idêntica à do ACCR, então a relação vem da comparação |
| Notas: fonte única OVML | `[inferência: cobertura no README]` | ✗ | A premissa é falsa: a cobertura marca DACCR como "~ wystup-2006 p. 101", e não "—" |

**Verificações da nota:**
- Tabela de pernas: ✗. O strike K1 não tem citação e não combina com tipo `—` (item 9).
- Frontmatter: ✅ acumulativo; `variante_de` ACCR.
- Omissões/contradições: ✅.

## FP

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: prêmio pago no futuro, em geral na liquidação | `[ovml]` | ✅ | "premium is paid in the future, typically on the settlement date of the option, rather than spot settlement" |
| Payoff: vanilla | `[ovml]` | ✗ | Diz só "An option payoff"; contra: wystup-2006, p. 118, o pagamento diferido "can be extended beyond vanilla options to all kind of options" |
| Notas: fonte única OVML | `[inferência: cobertura no README]` | ⚖ | Premissa verdadeira (FP marcado "—"). Ressalva: o Wystup menciona "deferred premium" como variação (p. 86) e o usa em exemplos (pp. 176–183), sem definir a estrutura |
| Notas: não confundir com pay-later | `[wystup-2006, p. 116]` | ✅ | "A pay-later option is a vanilla option, whose premium is only paid if the option is exercised" |

**Verificações da nota:**
- Tabela de pernas: ◐. Call e K1 vêm da mesma suposição de vanilla (item 2).
- Frontmatter: ✗ `payoff: vanilla` sem fonte (item 2).
- Omissões/contradições: ✅.
