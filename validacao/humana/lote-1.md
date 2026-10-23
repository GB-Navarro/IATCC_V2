# Validação — lote 1

Marque cada item depois de conferir a afirmação na página indicada. Itens com ⚠ são inferências: confira as premissas.

## Pontos de atenção

- **Inferências (⚠):** são conclusões minhas, não frases das fontes.
- **Decisões tiradas das fontes que mudam o matching:**
  - PF ganhou `flexivel: strike`, pelo Wystup (p. 141). A Bloomberg exige o mesmo strike.
  - DS ganhou `flexivel: notional`, pelo Natenberg (p. 157).
  - CP passou a exigir o mesmo vencimento, pelo Hull (p. 258). A Bloomberg não exige.
- **BF:** no Wystup, a definição (p. 36) e o exemplo (p. 37) descrevem posições opostas.
- **SDR:** a única fonte é o OVML.
- **Convenção EU:** "opções europeias" nas combinações de vanillas é uma convenção do `_schema.md`, citada como inferência.
- **Marcador `exemplo`:** a fonte só mostra a informação num exemplo numérico, não na definição.

## CP

- Origem · **Composição:** compra de uma call e venda de outra call
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[hull-2015, p. 258]` — hull-2015: PDF 281
  - [ ] `[wystup-2006, p. 30]` — wystup-2006: PDF 49
- Origem · **Strikes:** diferentes
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[hull-2015, p. 258]` — hull-2015: PDF 281
- Origem · **Strikes:** a call comprada tem o strike mais baixo
  - [ ] `[hull-2015, p. 258]` — hull-2015: PDF 281
- Origem · **Vencimento:** o mesmo nas duas pernas
  - [ ] `[hull-2015, p. 258]` — hull-2015: PDF 281
- Origem · **Notional:** igual: uma opção de cada lado
  - [ ] `[hull-2015, p. 258]` — hull-2015: PDF 281
  - [ ] `[wystup-2006, p. 31, exemplo]` — wystup-2006: PDF 50
- Origem · **Moneyness:** livre: as calls podem estar dentro ou fora do dinheiro
  - [ ] `[hull-2015, p. 259]` — hull-2015: PDF 282
- Origem · **Instrumento:** opções europeias
  - [ ] `[hull-2015, p. 258]` — hull-2015: PDF 281
- Restrições · Put spread e as versões bear são a mesma estrutura pelas regras de short e espelho
  - [ ] `[inferência: hull-2015, pp. 259–261 + regras de short e espelho do _schema.md]` — hull-2015: PDF 282–284 ⚠ inferência
- Notas · A Bloomberg não exige o mesmo vencimento. Foi adotada a definição do Hull: "Both options have the same expiration date."
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[hull-2015, p. 258]` — hull-2015: PDF 281

## RR

- Origem · **Composição:** compra de call, venda de put
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 31]` — wystup-2006: PDF 50
  - [ ] `[hull-2015, p. 371]` — hull-2015: PDF 394
- Origem · **Strikes:** diferentes; put abaixo da call
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[hull-2015, pp. 370–371]` — hull-2015: PDF 393–394
- Origem · **Vencimento:** o mesmo nas duas pernas
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Notional:** igual nas duas pernas
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 32, exemplo]` — wystup-2006: PDF 51
  - [ ] `[hull-2015, p. 370, exemplo]` — hull-2015: PDF 393
- Origem · **Moneyness:** as duas OTM
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Instrumento:** opções europeias
  - [ ] `[hull-2015, p. 370]` — hull-2015: PDF 393
- Origem · **Sinônimo:** collar
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 31]` — wystup-2006: PDF 50
- Restrições · Costuma ser montado a custo zero: o prêmio da put vendida paga o da call comprada
  - [ ] `[wystup-2006, p. 31]` — wystup-2006: PDF 50
  - [ ] `[hull-2015, p. 371]` — hull-2015: PDF 394
- Restrições · Em FX, o RR é cotado como a diferença entre a volatilidade da call e a da put com o mesmo delta em módulo; 0,25 é o caso usado como exemplo. O mercado cota o delta 0,25, e outros deltas, como 0,10 e 0,35, também são cotados
  - [ ] `[reiswich-wystup-2009, pp. 12–13]` — reiswich-wystup-2009: PDF 14–15
  - [ ] `[wystup-2006, p. 22]` — wystup-2006: PDF 41
- Notas · O nome Bloomberg desta estrutura é "Risk Reversal (Collar)". A versão com a posição protegida (fence) é outra nota, [[COL]]
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[natenberg-1994, p. 264]` — natenberg-1994: PDF 273
- Notas · O Hull chama esta estrutura de *range forward*: "This is a long position in a range forward contract and the payoff is shown in Figure 17.1b.". O RF do OVML é outra estrutura ([[RF]]): corresponde ao range forward do Wystup, um forward sint…
  - [ ] `[hull-2015, p. 371]` — hull-2015: PDF 394
  - [ ] `[wystup-2006, pp. 151–152]` — wystup-2006: PDF 170–171
  - [ ] `[inferência: texto da Bloomberg do RF]` ⚠ inferência

## SD

- Origem · **Composição:** compra de call e de put
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[hull-2015, p. 267]` — hull-2015: PDF 290
  - [ ] `[wystup-2006, p. 33]` — wystup-2006: PDF 52
- Origem · **Strikes:** o mesmo nas duas pernas
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[hull-2015, p. 267]` — hull-2015: PDF 290
  - [ ] `[wystup-2006, p. 33]` — wystup-2006: PDF 52
- Origem · **Vencimento:** o mesmo nas duas pernas
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[hull-2015, p. 267]` — hull-2015: PDF 290
- Origem · **Notional:** igual nas duas pernas
  - [ ] `[wystup-2006, p. 35, exemplo]` — wystup-2006: PDF 54
- Origem · **Moneyness:** ATM
  - [ ] `[wystup-2006, p. 35, exemplo]` — wystup-2006: PDF 54
  - [ ] `[inferência: o texto da Bloomberg do SDR contrasta o straddle com o strike OTM do ratio straddle]` ⚠ inferência
- Origem · **Instrumento:** opções europeias
  - [ ] `[hull-2015, p. 267]` — hull-2015: PDF 290
- Origem · **Variante de:** SN, com os dois strikes iguais
  - [ ] `[inferência: hull-2015, pp. 267, 269]` — hull-2015: PDF 290, 292 ⚠ inferência
- Restrições · Em FX, o ATM padrão para opções curtas é o delta-neutro: o strike em que o straddle não tem exposição ao spot
  - [ ] `[reiswich-wystup-2009, p. 9]` — reiswich-wystup-2009: PDF 11

## SN

- Origem · **Composição:** compra de put e de call
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[hull-2015, p. 269]` — hull-2015: PDF 292
  - [ ] `[wystup-2006, p. 35]` — wystup-2006: PDF 54
- Origem · **Strikes:** diferentes
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[hull-2015, p. 269]` — hull-2015: PDF 292
- Origem · **Strikes:** call acima da put
  - [ ] `[hull-2015, p. 269]` — hull-2015: PDF 292
- Origem · **Vencimento:** o mesmo nas duas pernas
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[hull-2015, p. 269]` — hull-2015: PDF 292
- Origem · **Notional:** igual nas duas pernas
  - [ ] `[wystup-2006, p. 36, exemplo]` — wystup-2006: PDF 55
- Origem · **Moneyness:** as duas OTM
  - [ ] `[wystup-2006, p. 35]` — wystup-2006: PDF 54
- Origem · **Instrumento:** opções europeias
  - [ ] `[hull-2015, p. 269]` — hull-2015: PDF 292
- Origem · **Sinônimo:** bottom vertical combination
  - [ ] `[hull-2015, p. 269]` — hull-2015: PDF 292
- Restrições · O strangle de referência do mercado de FX (market strangle) usa call e put com o mesmo delta em módulo; 0,25 é o caso usado como exemplo. O mercado cota o delta 0,25, e outros deltas, como 0,10 e 0,35, também são cotados
  - [ ] `[reiswich-wystup-2009, pp. 12, 15]` — reiswich-wystup-2009: PDF 14, 17
  - [ ] `[wystup-2006, p. 22]` — wystup-2006: PDF 41

## SDR

- Origem · **Composição:** compra de call e de put
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Strikes:** o mesmo nas duas pernas
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Vencimento:** o mesmo nas duas pernas
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Notional:** diferente entre as pernas (razão r)
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Moneyness:** strike geralmente fora do dinheiro
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Instrumento:** opções europeias
  - [ ] `[inferência: convenção do _schema.md, combinações de vanillas usam opções europeias; vanilla = opção europeia, wystup-2006, p. 39]` — wystup-2006: PDF 58 ⚠ inferência
- Origem · **Variante de:** SD, com strike fora do dinheiro e notionals diferentes
  - [ ] `[ovml]` — texto Bloomberg na nota
- Restrições · Os notionals são escolhidos para que a estrutura tenha delta forward zero
  - [ ] `[ovml]` — texto Bloomberg na nota
- Notas · Fonte única: OVML. A busca por "ratio straddle" nas fontes com texto não teve resultado; o natenberg-1994, escaneado, não pôde ser pesquisado
  - [ ] `[inferência: busca de texto em `fontes/`]` ⚠ inferência

## PF

- Origem · **Composição:** compra de call, venda de put
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 141]` — wystup-2006: PDF 160
- Origem · **Strikes:** o mesmo nas duas pernas, na definição da Bloomberg
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Vencimento:** o mesmo nas duas pernas
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Notional:** diferente entre as pernas
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 141]` — wystup-2006: PDF 160
- Origem · **Notional:** o da put vendida é menor que o da call (baixo risco) ou maior (alto risco, ex.: o dobro)
  - [ ] `[wystup-2006, p. 141]` — wystup-2006: PDF 160
- Origem · **Instrumento:** opções europeias
  - [ ] `[inferência: convenção do _schema.md, combinações de vanillas usam opções europeias; vanilla = opção europeia, wystup-2006, p. 39]` — wystup-2006: PDF 58 ⚠ inferência
- Origem · **Flexível:** strike: os strikes podem ser diferentes
  - [ ] `[wystup-2006, p. 141]` — wystup-2006: PDF 160
  - [ ] `[wystup-2006, p. 142, exemplo]` — wystup-2006: PDF 161
- Origem · **Variante de:** FWD: generaliza o forward sintético (call comprada e put vendida, mesmo strike e mesmo notional) com notionals diferentes
  - [ ] `[wystup-2006, pp. 140–141]` — wystup-2006: PDF 159–160
- Origem · **Variante de:** RR, que o Wystup descreve como muito parecido
  - [ ] `[wystup-2006, p. 141]` — wystup-2006: PDF 160
- Restrições · Costuma ser montado a custo baixo ou zero
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 141]` — wystup-2006: PDF 160
- Notas · No estilo de alto risco, o Wystup também o chama de *leveraged forward*
  - [ ] `[wystup-2006, p. 142]` — wystup-2006: PDF 161
- Notas · A Bloomberg exige o mesmo strike. O Wystup admite strikes diferentes: "In a more general manner, the strikes can also be different."
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 141]` — wystup-2006: PDF 160

## CS

- Origem · **Composição:** venda da opção de vencimento curto e compra da de vencimento longo, do mesmo tipo
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[hull-2015, p. 265]` — hull-2015: PDF 288
  - [ ] `[natenberg-1994, p. 148]` — natenberg-1994: PDF 158
- Origem · **Strikes:** o mesmo nas duas pernas
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[hull-2015, p. 265]` — hull-2015: PDF 288
  - [ ] `[natenberg-1994, p. 148]` — natenberg-1994: PDF 158
- Origem · **Vencimento:** diferentes (T1 < T2)
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[hull-2015, p. 265]` — hull-2015: PDF 288
- Origem · **Notional:** igual: uma opção de cada lado
  - [ ] `[hull-2015, p. 265]` — hull-2015: PDF 288
  - [ ] `[natenberg-1994, p. 148]` — natenberg-1994: PDF 158
- Origem · **Moneyness:** livre: strike próximo do preço corrente na visão neutra, acima na altista, abaixo na baixista
  - [ ] `[hull-2015, p. 266]` — hull-2015: PDF 289
- Origem · **Instrumento:** opções europeias
  - [ ] `[hull-2015, p. 265]` — hull-2015: PDF 288
- Origem · **Sinônimo:** horizontal spread
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[natenberg-1994, p. 148]` — natenberg-1994: PDF 158
- Origem · **Sinônimo:** time spread
  - [ ] `[natenberg-1994, p. 148]` — natenberg-1994: PDF 158
- Restrições · É usado em geral com visão neutra de mercado
  - [ ] `[ovml]` — texto Bloomberg na nota

## DS

- Origem · **Composição:** uma opção comprada e outra vendida, do mesmo tipo
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[hull-2015, p. 266]` — hull-2015: PDF 289
- Origem · **Composição:** vende a de vencimento curto e compra a de vencimento longo
  - [ ] `[hull-2015, p. 272]` — hull-2015: PDF 295
- Origem · **Strikes:** diferentes
  - [ ] `[hull-2015, p. 266]` — hull-2015: PDF 289
  - [ ] `[natenberg-1994, p. 157]` — natenberg-1994: PDF 167
- Origem · **Vencimento:** diferentes
  - [ ] `[hull-2015, p. 266]` — hull-2015: PDF 289
- Origem · **Notional:** igual em muitos casos (uma opção de cada lado)
  - [ ] `[natenberg-1994, p. 157]` — natenberg-1994: PDF 167
- Origem · **Instrumento:** opções europeias
  - [ ] `[inferência: convenção do _schema.md, combinações de vanillas usam opções europeias; o Hull apresenta o diagonal como variação do calendar spread de calls europeias, hull-2015, pp. 265–266]` — hull-2015: PDF 288–289 ⚠ inferência
- Origem · **Flexível:** notional: pode ter razão diferente de 1:1
  - [ ] `[natenberg-1994, p. 157]` — natenberg-1994: PDF 167
- Origem · **Variante de:** CS, com strikes diferentes
  - [ ] `[natenberg-1994, p. 157]` — natenberg-1994: PDF 167
- Restrições · A combinação entre strike e vencimento é livre: o strike do vencimento longo pode ser maior ou menor que o do curto. A tabela de pernas mostra só o primeiro caso
  - [ ] `[hull-2015, p. 272]` — hull-2015: PDF 295
- Notas · A Bloomberg aceita "strikes and/or maturities" diferentes. Foi adotado o Hull: "In a diagonal spread both the expiration date and the strike price of the calls are different."
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[hull-2015, p. 266]` — hull-2015: PDF 289

## SG

- Origem · **Composição:** compra de uma call; venda de uma call e de uma put
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 38]` — wystup-2006: PDF 57
- Origem · **Strikes:** três diferentes: put abaixo da call comprada, call vendida acima
  - [ ] `[wystup-2006, p. 39, exemplo]` — wystup-2006: PDF 58
- Origem · **Vencimento:** o mesmo nas três pernas
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Notional:** igual nas três pernas
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 39, exemplo]` — wystup-2006: PDF 58
- Origem · **Moneyness:** call comprada ATM
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Moneyness:** put e call vendidas OTM, como num strangle
  - [ ] `[inferência: o OVML descreve a venda de um strangle, e o Wystup define o strangle com opções OTM, wystup-2006, p. 35]` — wystup-2006: PDF 54 ⚠ inferência
- Origem · **Instrumento:** opções europeias
  - [ ] `[inferência: seção de estratégias com vanillas, wystup-2006, p. 29; vanilla = opção europeia, wystup-2006, p. 39]` — wystup-2006: PDF 48; wystup-2006: PDF 58 ⚠ inferência
- Origem · **Flexível:** notional: igual é o usual, não uma exigência
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Composta de:** EU (a opção ATM comprada) e SN (o strangle vendido)
  - [ ] `[ovml]` — texto Bloomberg na nota
- Restrições · Costuma ser montado a custo baixo ou zero; o Wystup o apresenta como produto de custo zero
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 38]` — wystup-2006: PDF 57

## BF

- Origem · **Composição:** compra de um strangle e venda de um straddle
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 36]` — wystup-2006: PDF 55
- Origem · **Strikes:** três: o do straddle no meio do intervalo entre os do strangle
  - [ ] `[natenberg-1994, p. 158]` — natenberg-1994: PDF 168
  - [ ] `[wystup-2006, p. 38, exemplo]` — wystup-2006: PDF 57
- Origem · **Vencimento:** o mesmo em todas as pernas
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[natenberg-1994, p. 158]` — natenberg-1994: PDF 168
- Origem · **Notional:** igual em todas as pernas
  - [ ] `[wystup-2006, p. 38, exemplo]` — wystup-2006: PDF 57
- Origem · **Moneyness:** strangle OTM, straddle ATM
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Instrumento:** opções europeias
  - [ ] `[inferência: seção de estratégias com vanillas, wystup-2006, p. 29; vanilla = opção europeia, wystup-2006, p. 39]` — wystup-2006: PDF 48; wystup-2006: PDF 58 ⚠ inferência
- Origem · **Composta de:** SN (comprado) e SD (vendido)
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 36]` — wystup-2006: PDF 55
- Notas · O Natenberg chama esta posição de *short iron butterfly* e mostra que ela equivale a um butterfly comprado: "A short iron butterfly is therefore equivalent to a long butterfly.". O "long" do OVML está certo no resultado, mas o nome *long ir…
  - [ ] `[natenberg-1994, p. 158]` — natenberg-1994: PDF 168
- Notas · No Wystup, a primeira frase da definição coincide com o OVML, e a Fig. 1.5 mostra o butterfly com o pico no strike do meio, como o BF do OVML. O resto da seção descreve a posição oposta (straddle comprado, strangle vendido, com prêmio pago)…
  - [ ] `[wystup-2006, p. 36]` — wystup-2006: PDF 55
  - [ ] `[wystup-2006, p. 22]` — wystup-2006: PDF 41
  - [ ] `[wystup-2006, pp. 36–37]` — wystup-2006: PDF 55–56

## BFC

- Origem · **Composição:** compra das calls K1 e K3, venda da call K2; só calls ou só puts
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[hull-2015, pp. 262, 264]` — hull-2015: PDF 285, 287
- Origem · **Composição:** duas opções vendidas em K2
  - [ ] `[hull-2015, p. 264]` — hull-2015: PDF 287
- Origem · **Strikes:** três; K2 no meio: K3 − K2 = K2 − K1
  - [ ] `[hull-2015, pp. 264, 270]` — hull-2015: PDF 287, 293
- Origem · **Vencimento:** o mesmo nas três pernas
  - [ ] `[hull-2015, p. 265]` — hull-2015: PDF 288
- Origem · **Notional:** 1:2:1
  - [ ] `[hull-2015, p. 264]` — hull-2015: PDF 287
- Origem · **Moneyness:** K1 ITM, K2 ATM, K3 OTM
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Moneyness:** K2 costuma ficar próximo do preço corrente
  - [ ] `[hull-2015, p. 264]` — hull-2015: PDF 287
- Origem · **Instrumento:** opções europeias
  - [ ] `[hull-2015, pp. 262, 264]` — hull-2015: PDF 285, 287
- Origem · **Composta de:** CP comprado (K1–K2) e CP vendido (K2–K3)
  - [ ] `[inferência: hull-2015, pp. 258, 261, 264]` — hull-2015: PDF 281, 284, 287 ⚠ inferência
- Origem · **Variante de:** BF, montado só com calls ou só com puts
  - [ ] `[ovml]` — texto Bloomberg na nota
- Notas · A Bloomberg não cita a razão 1:2:1. O Hull vende duas opções no strike central: "selling two European call options with a strike price K2 that is halfway between K1 and K3"
  - [ ] `[hull-2015, p. 264]` — hull-2015: PDF 287

## CR

- Origem · **Composição:** compra de um strangle largo e venda de um strangle mais estreito
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Strikes:** quatro; o intervalo do strangle vendido (K2–K3) é menor que o do comprado (K1–K4)
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Strikes:** as duas opções vendidas ficam entre as duas compradas
  - [ ] `[natenberg-1994, p. 158]` — natenberg-1994: PDF 168
- Origem · **Strikes:** as pontas têm o mesmo espaçamento: K2 − K1 = K4 − K3
  - [ ] `[inferência: o condor vale zero fora dos strikes extremos, natenberg-1994, p. 158]` — natenberg-1994: PDF 168 ⚠ inferência
- Origem · **Vencimento:** o mesmo nas quatro pernas
  - [ ] `[natenberg-1994, p. 158]` — natenberg-1994: PDF 168
- Origem · **Notional:** igual: uma opção por perna
  - [ ] `[natenberg-1994, p. 158]` — natenberg-1994: PDF 168
- Origem · **Instrumento:** opções europeias
  - [ ] `[inferência: convenção do _schema.md, combinações de vanillas usam opções europeias; vanilla = opção europeia, wystup-2006, p. 39]` — wystup-2006: PDF 58 ⚠ inferência
- Origem · **Composta de:** SN comprado (K1–K4) e SN vendido (K2–K3)
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Variante de:** BF, com o strike central dividido em dois
  - [ ] `[natenberg-1994, p. 158]` — natenberg-1994: PDF 168
- Notas · O Natenberg define o condor com um só tipo de opção: "As with a butterfly, all options must be of the same type (all calls or all puts) and expire at the same time.". A versão do OVML, com strangles, tem o mesmo resultado, e o "long" coinci…
  - [ ] `[natenberg-1994, p. 158]` — natenberg-1994: PDF 168
  - [ ] `[inferência: mesma equivalência do iron butterfly, natenberg-1994, p. 158]` — natenberg-1994: PDF 168 ⚠ inferência
