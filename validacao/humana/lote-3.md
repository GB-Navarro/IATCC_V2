# Validação — lote 3

Marque cada item depois de conferir a afirmação na página indicada. Itens com ⚠ são inferências: confira as premissas.

## Pontos de atenção

- **DKI:** a justificativa de prêmio da Bloomberg está invertida. A conclusão nas Notas é inferência a partir da paridade do Haug (p. 156).
- **KIKOSQ:** a Bloomberg reúne dois produtos (KIKO e KIKI sequenciais). A leitura da frase ambígua sobre o DownIn é inferência.
- **OT, NT, DOT e DNT:** o toque é codificado como `ki` (paga se tocar) ou `ko` (paga se não tocar); no OT e no NT, o Haug sustenta a codificação (pp. 177–178).
- **Só OVML para a definição:** DIDKO, DIDKI, DISEQ, DACCR e FP. As fontes tratam só componentes ou estruturas parecidas.
- **AVG:** a Bloomberg reúne dois produtos (average rate e average strike).
- **CMP:** a tabela mostra um strike e um vencimento; na prática são dois.

## KO

- Origem · **Composição:** opção vanilla que deixa de existir se o spot tocar a barreira; a tabela mostra a call
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[hull-2015, p. 604]` — hull-2015: PDF 627
  - [ ] `[wystup-2006, p. 40]` — wystup-2006: PDF 59
- Origem · **Barreira:** ko, uma barreira
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[hull-2015, p. 604]` — hull-2015: PDF 627
- Origem · **Payoff:** vanilla, se a barreira não for tocada
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 40]` — wystup-2006: PDF 59
- Restrições · A barreira pode ser americana (vale o tempo todo) ou europeia (só no vencimento). Por tradição, as barreiras são americanas
  - [ ] `[wystup-2006, pp. 40, 42]` — wystup-2006: PDF 59, 61
  - [ ] `[wystup-2006, p. 43]` — wystup-2006: PDF 62
- Restrições · Barreira regular fica fora do dinheiro; reverse, dentro do dinheiro
  - [ ] `[wystup-2006, p. 42]` — wystup-2006: PDF 61
- Restrições · O prêmio é menor que o da vanilla equivalente
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[hull-2015, p. 604]` — hull-2015: PDF 627

## KI

- Origem · **Composição:** opção vanilla que só passa a existir se o spot tocar a barreira; a tabela mostra a call
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[hull-2015, p. 604]` — hull-2015: PDF 627
  - [ ] `[wystup-2006, p. 42]` — wystup-2006: PDF 61
- Origem · **Barreira:** ki, uma barreira
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[hull-2015, p. 604]` — hull-2015: PDF 627
- Origem · **Payoff:** vanilla, se a barreira for tocada
  - [ ] `[ovml]` — texto Bloomberg na nota
- Restrições · Knock-out mais knock-in com os mesmos parâmetros equivalem à vanilla
  - [ ] `[wystup-2006, p. 42]` — wystup-2006: PDF 61
- Restrições · Barreira regular fica fora do dinheiro; reverse, dentro do dinheiro
  - [ ] `[wystup-2006, p. 42]` — wystup-2006: PDF 61
- Restrições · Por tradição, as barreiras são americanas
  - [ ] `[wystup-2006, p. 43]` — wystup-2006: PDF 62
- Restrições · O prêmio é menor que o da vanilla equivalente
  - [ ] `[ovml]` — texto Bloomberg na nota

## DKO

- Origem · **Composição:** opção vanilla que deixa de existir se o spot tocar qualquer uma de duas barreiras; a tabela mostra a call
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[haug-2007, p. 156]` — haug-2007: PDF 195
- Origem · **Barreira:** ko, duas barreiras (inferior e superior)
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[haug-2007, p. 156]` — haug-2007: PDF 195
- Origem · **Payoff:** vanilla, se nenhuma barreira for tocada
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[haug-2007, p. 156]` — haug-2007: PDF 195
- Origem · **Variante de:** KO, com duas barreiras
  - [ ] `[inferência: comparação dos textos da Bloomberg do KO e do DKO]` ⚠ inferência
  - [ ] `[wystup-2006, p. 40]` — wystup-2006: PDF 59

## DKI

- Origem · **Composição:** opção vanilla que só passa a existir se o spot tocar uma de duas barreiras; a tabela mostra a call
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[haug-2007, p. 156]` — haug-2007: PDF 195
- Origem · **Barreira:** ki, duas barreiras (inferior e superior)
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[haug-2007, p. 156]` — haug-2007: PDF 195
- Origem · **Payoff:** vanilla, se alguma barreira for tocada
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Variante de:** KI, com duas barreiras
  - [ ] `[inferência: comparação dos textos da Bloomberg do KI e do DKI]` ⚠ inferência
  - [ ] `[wystup-2006, p. 40]` — wystup-2006: PDF 59
- Restrições · Equivale a uma vanilla comprada mais um double knock-out vendido, com os mesmos strike e vencimento
  - [ ] `[haug-2007, p. 156]` — haug-2007: PDF 195
- Notas · A Bloomberg justifica o prêmio menor pelas duas chances de a opção nunca ser ativada, o que está invertido: com duas barreiras há duas formas de ativar. Pelo Haug, "a double knock-in put is equal to a long standard put and a short double kn…
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[haug-2007, p. 156]` — haug-2007: PDF 195
  - [ ] `[inferência: DKI = vanilla − DKO, haug-2007, p. 156; KI = vanilla − KO, wystup-2006, p. 42; o DKO é cancelado sempre que o KO com uma das suas barreiras é cancelado]` — haug-2007: PDF 195; wystup-2006: PDF 61 ⚠ inferência

## OT

- Origem · **Composição:** pagamento fixo se o spot tocar a barreira antes do vencimento
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 50]` — wystup-2006: PDF 69
- Origem · **Barreira:** ki (o toque ativa o pagamento), uma barreira
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[haug-2007, p. 177]` — haug-2007: PDF 216
- Origem · **Payoff:** toque
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Sinônimo:** hit option, one-touch digital
  - [ ] `[wystup-2006, p. 50]` — wystup-2006: PDF 69
- Restrições · Em FX, o pagamento padrão é na data de entrega, dois dias úteis após o vencimento; outra prática comum é dois dias úteis após o toque
  - [ ] `[wystup-2006, p. 49]` — wystup-2006: PDF 68

## NT

- Origem · **Composição:** pagamento fixo se o spot não tocar a barreira até o vencimento
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 50]` — wystup-2006: PDF 69
- Origem · **Barreira:** ko (o toque cancela o pagamento), uma barreira
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[haug-2007, p. 178]` — haug-2007: PDF 217
- Origem · **Payoff:** toque
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Variante de:** OT, com a condição invertida: one-touch mais no-touch pagam com certeza
  - [ ] `[wystup-2006, p. 50]` — wystup-2006: PDF 69

## DOT

- Origem · **Composição:** pagamento fixo se o spot tocar qualquer uma de duas barreiras
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 40]` — wystup-2006: PDF 59
  - [ ] `[haug-2007, p. 180]` — haug-2007: PDF 219
- Origem · **Barreira:** ki, duas barreiras
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[haug-2007, p. 180]` — haug-2007: PDF 219
- Origem · **Payoff:** toque
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Variante de:** OT, com duas barreiras
  - [ ] `[inferência: comparação dos textos da Bloomberg do OT e do DOT]` ⚠ inferência

## DNT

- Origem · **Composição:** pagamento fixo se o spot não tocar nenhuma de duas barreiras
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, pp. 55–56]` — wystup-2006: PDF 74–75
  - [ ] `[haug-2007, p. 180]` — haug-2007: PDF 219
- Origem · **Barreira:** ko, duas barreiras
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[haug-2007, p. 180]` — haug-2007: PDF 219
- Origem · **Payoff:** toque, pago no vencimento
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 56]` — wystup-2006: PDF 75
- Origem · **Variante de:** NT, com duas barreiras
  - [ ] `[inferência: comparação dos textos da Bloomberg do NT e do DNT]` ⚠ inferência

## DIVA

- Origem · **Composição:** pagamento fixo no vencimento se o spot estiver acima (call) ou abaixo (put) do strike; a tabela mostra a call
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[hull-2015, pp. 606–607]` — hull-2015: PDF 629–630
- Origem · **Payoff:** digital
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[hull-2015, pp. 606–607]` — hull-2015: PDF 629–630
- Origem · **Sinônimo:** cash-or-nothing
  - [ ] `[hull-2015, p. 606]` — hull-2015: PDF 629
- Origem · **Sinônimo:** binary option
  - [ ] `[haug-2007, p. 174]` — haug-2007: PDF 213

## DIKO

- Origem · **Composição:** digital que deixa de existir se o spot tocar a barreira; a tabela mostra a call
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 105]` — wystup-2006: PDF 124
  - [ ] `[haug-2007, p. 179]` — haug-2007: PDF 218
- Origem · **Barreira:** ko, uma barreira
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[haug-2007, p. 179]` — haug-2007: PDF 218
- Origem · **Payoff:** digital
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Variante de:** DIVA, com barreira knock-out
  - [ ] `[inferência: comparação dos textos da Bloomberg do DIVA e do DIKO]` ⚠ inferência
  - [ ] `[wystup-2006, p. 105]` — wystup-2006: PDF 124

## DIKI

- Origem · **Composição:** digital que só passa a existir se o spot tocar a barreira; a tabela mostra a call
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 105]` — wystup-2006: PDF 124
  - [ ] `[haug-2007, p. 178]` — haug-2007: PDF 217
- Origem · **Barreira:** ki, uma barreira
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[haug-2007, p. 178]` — haug-2007: PDF 217
- Origem · **Payoff:** digital
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Variante de:** DIVA, com barreira knock-in
  - [ ] `[inferência: comparação dos textos da Bloomberg do DIVA e do DIKI]` ⚠ inferência
  - [ ] `[wystup-2006, p. 105]` — wystup-2006: PDF 124

## DIDKO

- Origem · **Composição:** digital que deixa de existir se o spot tocar qualquer uma de duas barreiras; a tabela mostra a call
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Barreira:** ko, duas barreiras
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Payoff:** digital
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Variante de:** DIKO, com duas barreiras
  - [ ] `[inferência: comparação dos textos da Bloomberg do DIKO e do DIDKO]` ⚠ inferência
- Notas · Fonte única para a definição: OVML. As fontes tratam só componentes ou estruturas parecidas
  - [ ] `[inferência: páginas indicadas para esta estrutura na cobertura de `fontes/README.md`]` ⚠ inferência

## DIDKI

- Origem · **Composição:** digital que só passa a existir se o spot tocar uma de duas barreiras; a tabela mostra a call
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Barreira:** ki, duas barreiras
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Payoff:** digital
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Variante de:** DIKI, com duas barreiras
  - [ ] `[inferência: comparação dos textos da Bloomberg do DIKI e do DIDKI]` ⚠ inferência
- Notas · Fonte única para a definição: OVML. As fontes tratam só componentes ou estruturas parecidas
  - [ ] `[inferência: páginas indicadas para esta estrutura na cobertura de `fontes/README.md`]` ⚠ inferência

## DISEQ

- Origem · **Composição:** digital sequencial
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Barreira:** duas barreiras ativadas em sequência
  - [ ] `[inferência: mesmo uso de "sequential" no KIKOSQ; haug-2007, p. 169]` — haug-2007: PDF 208 ⚠ inferência
- Origem · **Payoff:** digital
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Variante de:** DIVA, com barreiras sequenciais
  - [ ] `[inferência: texto da Bloomberg do DISEQ; "sequential" indica barreiras em sequência, como no KIKOSQ, haug-2007, p. 169]` — haug-2007: PDF 208 ⚠ inferência
- Notas · A descrição da Bloomberg tem uma linha e não define tipo, strike nem barreiras
  - [ ] `[ovml]` — texto Bloomberg na nota
- Notas · Fonte única para a definição: OVML. As fontes tratam só componentes ou estruturas parecidas
  - [ ] `[inferência: páginas indicadas para esta estrutura na cobertura de `fontes/README.md`]` ⚠ inferência

## KOKI

- Origem · **Composição:** opção knock-in que pode ser cancelada pelo knock-out a qualquer momento; a tabela mostra a call
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 115]` — wystup-2006: PDF 134
- Origem · **Barreira:** kiko: uma barreira KI e uma KO; o KO vale antes e depois do KI
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, pp. 115–116]` — wystup-2006: PDF 134–135
- Origem · **Payoff:** vanilla
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Sinônimo:** KIKO do tipo 1, o padrão de mercado
  - [ ] `[wystup-2006, pp. 115–116]` — wystup-2006: PDF 134–135
- Restrições · É replicável com barreiras padrão: KIKO(L, U) = KO(L) − DKO(L, U), com L = barreira KO e U = barreira KI
  - [ ] `[wystup-2006, p. 116]` — wystup-2006: PDF 135
  - [ ] `[wystup-fxcol-2022, p. 2]` — wystup-fxcol-2022: PDF 2
- Notas · O alias "KIKO" segue o Wystup, para quem o tipo 1 é o padrão de mercado, mas o tipo deve ser sempre esclarecido: "The first one is the market standard, but when dealing one should always clarify which type of knock-in-knock-out is agreed up…
  - [ ] `[wystup-2006, p. 116]` — wystup-2006: PDF 135

## KIKOSQ

- Origem · **Composição:** opção knock-in cujo knock-out só vale depois do knock-in (KIKO sequencial); variante com dois knock-ins em sequência (KIKI sequencial); a tabela mostra a call
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Barreira:** kiko no KIKO sequencial; dois ki no KIKI sequencial; duas barreiras
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Payoff:** vanilla
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Sinônimo:** KIKO do tipo 2: o knock-out só pode ocorrer depois do knock-in
  - [ ] `[wystup-2006, pp. 115–116]` — wystup-2006: PDF 134–135
- Origem · **Sinônimo:** o KIKI sequencial é uma first-then-in barrier option (ex.: first-down-then-up-and-in call)
  - [ ] `[haug-2007, p. 169]` — haug-2007: PDF 208
- Notas · A Bloomberg reúne dois produtos na mesma descrição, o KIKO sequencial e o KIKI sequencial. O campo `barreira` registra só o primeiro
  - [ ] `[ovml]` — texto Bloomberg na nota
- Notas · A frase da Bloomberg sobre o DownIn "reached first" quer dizer que um toque no DownIn antes do UpIn não conta. O Haug descreve a mesma regra para a ordem inversa: "To be knocked in, the asset price has to hit the lower barrier at least once…
  - [ ] `[inferência: texto da Bloomberg + haug-2007, p. 169]` — haug-2007: PDF 208 ⚠ inferência
  - [ ] `[haug-2007, p. 169]` — haug-2007: PDF 208

## EAKO

- Origem · **Composição:** opção com knock-out americano e knock-in europeu, que só vale no vencimento; a tabela mostra a call
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-fxcol-2022, p. 1]` — wystup-fxcol-2022: PDF 1
- Origem · **Barreira:** kiko: KO americano fora do dinheiro, KI europeu dentro do dinheiro
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Payoff:** vanilla
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Variante de:** KOKI: é um caso especial de KIKO
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-fxcol-2022, p. 1]` — wystup-fxcol-2022: PDF 1
- Origem · **Sinônimo:** KOAMKIEU
  - [ ] `[wystup-fxcol-2022, p. 1]` — wystup-fxcol-2022: PDF 1
- Restrições · O cliente escolhe se o pagamento ocorre com o spot acima ou abaixo da barreira europeia no vencimento
  - [ ] `[ovml]` — texto Bloomberg na nota
- Notas · Não confundir com a transatlantic barrier option do Wystup, em que as duas barreiras (americana e europeia) são knock-out
  - [ ] `[wystup-2006, p. 108]` — wystup-2006: PDF 127

## CMP

- Origem · **Composição:** opção sobre uma vanilla: a compound call dá o direito de comprar a vanilla, a compound put o de vender; a tabela mostra a call
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 58]` — wystup-2006: PDF 77
  - [ ] `[hull-2015, p. 602]` — hull-2015: PDF 625
- Origem · **Strikes:** dois: o da compound (o prêmio a pagar pela vanilla) e o da vanilla; a tabela mostra só K1
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[hull-2015, pp. 602–603]` — hull-2015: PDF 625–626
- Origem · **Vencimento:** dois: o da compound e o da vanilla; a tabela mostra só T1
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[hull-2015, pp. 602–603]` — hull-2015: PDF 625–626
- Origem · **Payoff:** composto
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[haug-2007, p. 132]` — haug-2007: PDF 171
- Restrições · Permite pagar o prêmio da vanilla em parcelas
  - [ ] `[wystup-2006, p. 58]` — wystup-2006: PDF 77
- Restrições · A compound pode ser call ou put sobre uma call ou uma put: são quatro tipos
  - [ ] `[hull-2015, p. 602]` — hull-2015: PDF 625

## AVG

- Origem · **Composição:** opção cujo payoff depende da média do spot: average rate (média contra o strike) ou average strike (a média é o strike); a tabela mostra a call
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[hull-2015, pp. 609, 611]` — hull-2015: PDF 632, 634
  - [ ] `[wystup-2006, pp. 69–70]` — wystup-2006: PDF 88–89
- Origem · **Payoff:** media
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Sinônimo:** opção asiática
  - [ ] `[hull-2015, p. 609]` — hull-2015: PDF 632
  - [ ] `[wystup-2006, p. 69]` — wystup-2006: PDF 88
- Restrições · A média pode ser geométrica, aritmética ou harmônica
  - [ ] `[wystup-2006, p. 69]` — wystup-2006: PDF 88
- Notas · A descrição da Bloomberg reúne dois produtos, average rate e average strike; o Hull os trata como tipos distintos de opção asiática
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[hull-2015, p. 611]` — hull-2015: PDF 634

## FA

- Origem · **Composição:** vanilla cujo notional é definido no vencimento pelos fixings dentro (ou fora) de um intervalo; a tabela mostra a call
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, pp. 103–104]` — wystup-2006: PDF 122–123
- Origem · **Composição:** o fade-in com fixings dentro do intervalo
  - [ ] `[haug-2007, p. 122]` — haug-2007: PDF 161
- Origem · **Notional:** proporcional ao número de fixings que cumprem a condição
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, pp. 103–104]` — wystup-2006: PDF 122–123
- Origem · **Payoff:** acumulativo
  - [ ] `[ovml]` — texto Bloomberg na nota
- Restrições · No fade-in o notional começa em zero e cresce; no fade-out começa cheio e diminui
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 103]` — wystup-2006: PDF 122

## ACCR

- Origem · **Composição:** pagamento em dinheiro que cresce a cada fixing dentro do intervalo
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 101]` — wystup-2006: PDF 120
- Origem · **Notional:** cada fixing dentro do intervalo acrescenta o pagamento máximo dividido pelo número de fixings
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 101]` — wystup-2006: PDF 120
- Origem · **Payoff:** acumulativo
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Sinônimo:** corridor
  - [ ] `[wystup-2006, p. 101]` — wystup-2006: PDF 120
- Restrições · Na versão europeia contam todos os fixings dentro do intervalo; na americana, a acumulação para quando o spot sai do intervalo
  - [ ] `[wystup-2006, p. 102]` — wystup-2006: PDF 121

## DACCR

- Origem · **Composição:** pagamento que acumula com os fixings e só é pago se a opção estiver no dinheiro no vencimento; a tabela mostra a call
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Strikes:** um strike, que define se a opção termina no dinheiro
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Payoff:** acumulativo, com condição digital no vencimento
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Variante de:** ACCR, com a condição de estar no dinheiro no vencimento
  - [ ] `[inferência: comparação dos textos da Bloomberg do ACCR e do DACCR]` ⚠ inferência
- Notas · Fonte única para a definição: OVML. O Wystup define o corridor, que corresponde só à parte de acumulação, sem a condição no vencimento
  - [ ] `[wystup-2006, p. 101]` — wystup-2006: PDF 120

## FP

- Origem · **Composição:** opção cujo prêmio é pago no futuro, em geral na data de liquidação da opção; a tabela mostra a call
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Payoff:** vanilla: o caso mais comum; a Bloomberg não especifica o tipo de opção
  - [ ] `[inferência: o texto da Bloomberg diz só "an option payoff"]` ⚠ inferência
- Notas · Fonte única para a definição: OVML. Nenhuma fonte de `fontes/` define esta estrutura
  - [ ] `[inferência: cobertura por estrutura em `fontes/README.md`]` ⚠ inferência
- Notas · Não confundir com a pay-later option, em que o prêmio só é pago se a opção for exercida
  - [ ] `[wystup-2006, p. 116]` — wystup-2006: PDF 135
