# Validação — lote 4

Marque cada item depois de conferir a afirmação na página indicada. Itens com ⚠ são inferências: confira as premissas.

## Pontos de atenção

- **FE:** o FE do OVML é o *forward plus* do Wystup (conflito de nome). A equivalência com o shark forward é inferência pela paridade KO + KI = vanilla.
- **RF:** coincide com o range forward do Wystup. O Hull usa o nome para o collar, e o Wystup também o chama de *bonus forward*, que no OVML é o BFW.
- **BFW e KKF:** têm tabela de uma linha só, porque a Bloomberg não informa os tipos das pernas. No KKF, a KIKO ser do tipo KOKI é inferência.
- **EC, TF e ARC:** vencimento, notional e (no ARC) strikes e moneyness são inferidos. EC e TF ficaram com `flexivel: strike`.
- **TF:** a versão com venda de forward e compra de call não é coberta pelas regras de short e espelho.
- **Só OVML:** KKF, TF, EF, BFF e ACCUKI.

## FE

- Origem · **Composição:** compra de call vanilla e venda de put reverse knock-in, no mesmo strike
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Composição:** equivale a um forward sintético mais um reverse knock-out, a composição do shark forward
  - [ ] `[inferência: call − put + RKO = call − RKI, pela paridade KO + KI = vanilla; wystup-2006, pp. 42, 145]` — wystup-2006: PDF 61, 164 ⚠ inferência
- Origem · **Strikes:** o mesmo nas duas pernas
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Vencimento:** o mesmo nas duas pernas
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Notional:** igual nas duas pernas
  - [ ] `[wystup-2006, p. 145, exemplo]` — wystup-2006: PDF 164
- Origem · **Barreira:** reverse knock-in na put: é tocada quando a put vai para dentro do dinheiro
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 42]` — wystup-2006: PDF 61
- Origem · **Composta de:** EU e KI
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Sinônimo:** Variance Forward
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Sinônimo:** shark forward, forward plus, enhanced forward
  - [ ] `[wystup-2006, p. 144]` — wystup-2006: PDF 163
- Notas · O FE do OVML corresponde ao que o Wystup chama de *forward plus*: "(shark) forward plus: the buyer benefits from a favorable spot movement.". O *forward extra* do Wystup é a variante oposta, em que o cliente ganha quando o spot anda contra …
  - [ ] `[wystup-2006, p. 145]` — wystup-2006: PDF 164
  - [ ] `[wystup-2006, p. 145]` — wystup-2006: PDF 164

## EC

- Origem · **Composição:** compra de call vanilla e venda de put knock-in com barreira dentro do dinheiro
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Barreira:** reverse knock-in: barreira dentro do dinheiro
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 42]` — wystup-2006: PDF 61
- Origem · **Strikes:** a Bloomberg não fixa a relação entre os strikes
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Flexível:** strike, pela mesma razão
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Vencimento:** o mesmo nas duas pernas
  - [ ] `[inferência: alternativa ao RR, que tem um só vencimento; texto da Bloomberg]` ⚠ inferência
- Origem · **Notional:** igual nas duas pernas
  - [ ] `[inferência: idem]` ⚠ inferência
- Origem · **Composta de:** EU e KI
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Variante de:** RR, numa versão de menor risco
  - [ ] `[ovml]` — texto Bloomberg na nota
- Notas · O "Knock-In put with a barrier that is in-the-money" da Bloomberg é um reverse knock-in, o mesmo termo usado no FE e no BFW: "regular barriers are out of the money, reverse barriers are in the money"
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 42]` — wystup-2006: PDF 61

## BFW

- Origem · **Composição:** compra de uma knock-out e de uma knock-in e venda de uma reverse knock-in, todas com a mesma barreira
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Composição:** antes da barreira o cliente tem uma opção comprada; depois, um forward na taxa bônus (K1)
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Composta de:** KO e KI
  - [ ] `[ovml]` — texto Bloomberg na nota
- Restrições · Os tipos (call ou put) das pernas não são informados, por isso a tabela tem uma linha só
  - [ ] `[ovml]` — texto Bloomberg na nota
- Restrições · Pode ser montado a custo zero
  - [ ] `[ovml]` — texto Bloomberg na nota
- Notas · O Wystup usa *bonus forward* como sinônimo de range forward: "The range or bonus forward is another forward enhancement with guaranteed worst case.". O BFW do OVML é outra estrutura
  - [ ] `[wystup-2006, p. 151]` — wystup-2006: PDF 170
  - [ ] `[ovml]` — texto Bloomberg na nota

## KKF

- Origem · **Composição:** compra de uma knock-out e venda de uma KIKO
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Strikes:** o mesmo nas duas pernas: o cliente fica hedgeado no strike
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Composta de:** KO e KIKO
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Composta de:** a KIKO é do tipo KOKI: se o KO é tocado primeiro, o hedge se perde mesmo que o KI venha depois
  - [ ] `[inferência: texto da Bloomberg do KKF + wystup-2006, p. 115]` — wystup-2006: PDF 134 ⚠ inferência
- Restrições · Os tipos (call ou put) das pernas não são informados, por isso a tabela tem uma linha só
  - [ ] `[ovml]` — texto Bloomberg na nota
- Restrições · Pode ser montado a custo zero
  - [ ] `[ovml]` — texto Bloomberg na nota
- Notas · Fonte única: OVML
  - [ ] `[ovml]` — texto Bloomberg na nota

## TF

- Origem · **Composição:** compra de forward e compra de put (ou venda de forward e compra de call)
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Strikes:** a Bloomberg não fixa a relação entre a taxa do forward e o strike da opção
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Flexível:** strike, pela mesma razão
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Vencimento:** o mesmo nas duas pernas
  - [ ] `[inferência: as duas pernas protegem o mesmo fluxo; texto da Bloomberg]` ⚠ inferência
- Origem · **Notional:** igual: o valor total do hedge
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Composta de:** FWD e EU
  - [ ] `[ovml]` — texto Bloomberg na nota
- Restrições · A versão com venda de forward e compra de call não é coberta pelas regras de short e espelho, porque o espelho não inverte o lado do forward
  - [ ] `[inferência: regras do _schema.md]` ⚠ inferência
- Notas · Fonte única: OVML
  - [ ] `[ovml]` — texto Bloomberg na nota

## RF

- Origem · **Composição:** forward sintético no strike do pior caso (compra de call e venda de put) mais compra de um double-no-touch
  - [ ] `[wystup-2006, p. 152]` — wystup-2006: PDF 171
- Origem · **Strikes:** o mesmo nas duas opções: o pior caso
  - [ ] `[wystup-2006, p. 152]` — wystup-2006: PDF 171
- Origem · **Vencimento:** o mesmo em todas as pernas
  - [ ] `[wystup-2006, p. 151]` — wystup-2006: PDF 170
- Origem · **Notional:** igual nas duas opções
  - [ ] `[wystup-2006, p. 152, exemplo]` — wystup-2006: PDF 171
- Origem · **Notional:** o pagamento do DNT (r) cobre a diferença entre pior e melhor caso
  - [ ] `[inferência: wystup-2006, p. 152]` — wystup-2006: PDF 171 ⚠ inferência
- Origem · **Barreira:** as do DNT: na versão básica, o intervalo é verificado só no vencimento; também há versão com barreiras americanas
  - [ ] `[wystup-2006, pp. 151–152]` — wystup-2006: PDF 170–171
- Origem · **Composta de:** DNT, mais um forward sintético
  - [ ] `[wystup-2006, p. 152]` — wystup-2006: PDF 171
- Restrições · É montado a custo zero, como um forward outright
  - [ ] `[wystup-2006, p. 151]` — wystup-2006: PDF 170
- Notas · O Hull usa *range forward* para o collar (RR do OVML): "This is known as a short position in a range forward contract."
  - [ ] `[hull-2015, p. 370]` — hull-2015: PDF 393
- Notas · O Wystup chama a estrutura também de *bonus forward*, nome que no OVML designa outra estrutura ([[BFW]])
  - [ ] `[wystup-2006, p. 151]` — wystup-2006: PDF 170
  - [ ] `[ovml]` — texto Bloomberg na nota

## KOF

- Origem · **Composição:** compra de call e venda de put, as duas com knock-out
  - [ ] `[wystup-2006, p. 143]` — wystup-2006: PDF 162
- Origem · **Strikes:** o mesmo nas duas pernas
  - [ ] `[wystup-2006, p. 143]` — wystup-2006: PDF 162
- Origem · **Vencimento:** o mesmo nas duas pernas
  - [ ] `[wystup-2006, p. 143]` — wystup-2006: PDF 162
- Origem · **Notional:** igual nas duas pernas
  - [ ] `[wystup-2006, p. 143]` — wystup-2006: PDF 162
- Origem · **Barreira:** uma ou duas barreiras knock-out, as mesmas nas duas pernas
  - [ ] `[wystup-2006, p. 143]` — wystup-2006: PDF 162
- Origem · **Barreira:** dentro do dinheiro
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Composta de:** KO
  - [ ] `[wystup-2006, p. 143]` — wystup-2006: PDF 162
- Restrições · Se a barreira é tocada, o cliente fica sem hedge
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 144]` — wystup-2006: PDF 163
- Restrições · É montado a custo zero
  - [ ] `[wystup-2006, p. 144]` — wystup-2006: PDF 163

## EF

- Origem · **Composição:** forward, em geral com razão de notional, estendido por mais um período se o spot ficar além de uma barreira no vencimento
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Barreira:** uma, verificada no vencimento, que dispara a extensão
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Variante de:** FWD, ou PF quando há razão de notional
  - [ ] `[ovml]` — texto Bloomberg na nota
- Notas · Fonte única: OVML
  - [ ] `[ovml]` — texto Bloomberg na nota
- Notas · O auto-renewal forward do Wystup, uma série de forwards renovada automaticamente, é parecido mas não igual
  - [ ] `[wystup-2006, p. 163]` — wystup-2006: PDF 182

## FLEX

- Origem · **Composição:** forward em que o cliente escolhe a data de entrega dentro de um período
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 166]` — wystup-2006: PDF 185
- Origem · **Payoff:** linear
  - [ ] `[inferência: é um forward, hull-2015, p. 7]` — hull-2015: PDF 30 ⚠ inferência
- Origem · **Sinônimo:** time option, forward de estilo americano
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 166]` — wystup-2006: PDF 185

## BFF

- Origem · **Composição:** forward em que o notional acumula a cada dia com fixing acima ou abaixo da taxa de fade (a barreira)
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Composição:** um valor alavancado é vendido num strike fora do dinheiro para melhorar a taxa
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Payoff:** acumulativo
  - [ ] `[ovml]` — texto Bloomberg na nota
- Notas · Fonte única: OVML
  - [ ] `[ovml]` — texto Bloomberg na nota
- Notas · É parecido com o fade-in forward e com o boosted spot/forward do Wystup
  - [ ] `[wystup-2006, pp. 142, 165]` — wystup-2006: PDF 161, 184

## ARC

- Origem · **Composição:** como um risk reversal, mas com put e call de taxa média
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Strikes:** como no RR: diferentes, put abaixo da call
  - [ ] `[inferência: texto da Bloomberg do ARC + nota RR]` ⚠ inferência
- Origem · **Vencimento:** como no RR: o mesmo
  - [ ] `[inferência: idem]` ⚠ inferência
- Origem · **Notional:** como no RR: igual
  - [ ] `[inferência: idem]` ⚠ inferência
- Origem · **Moneyness:** como no RR: as duas OTM
  - [ ] `[inferência: idem]` ⚠ inferência
- Origem · **Composta de:** AVG
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Variante de:** RR, com opções de média
  - [ ] `[ovml]` — texto Bloomberg na nota

## ARF

- Origem · **Composição:** forward cujo payoff é a diferença entre o strike e a média do spot num período
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Payoff:** media
  - [ ] `[ovml]` — texto Bloomberg na nota
- Restrições · Liquidado em moeda estrangeira, usa o inverso da média, ou seja, a média harmônica
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 131]` — wystup-2006: PDF 150
- Restrições · Média geométrica ou liquidação em moeda estrangeira exigem volatilidade no apreçamento
  - [ ] `[ovml]` — texto Bloomberg na nota

## ASF

- Origem · **Composição:** forward entre o spot no vencimento e um strike igual à média do spot num período
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Strikes:** não é fixo: é a média do período
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Payoff:** media
  - [ ] `[ovml]` — texto Bloomberg na nota
- Restrições · Forwards com strike flutuante na média harmônica aparecem no Wystup
  - [ ] `[wystup-2006, p. 132]` — wystup-2006: PDF 151
- Restrições · Notional na moeda doméstica ou média geométrica exigem volatilidade no apreçamento
  - [ ] `[ovml]` — texto Bloomberg na nota

## ACCU

- Origem · **Composição:** forward cujo valor de face é definido pelo spot em vários fixings; cresce a cada fixing que cumpre a condição
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 156]` — wystup-2006: PDF 175
- Origem · **Notional:** o exibido é o máximo; cada fixing acrescenta o notional dividido pelo número de fixings
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Payoff:** acumulativo
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Composta de:** faders (fade-in calls e puts), possivelmente com faixas de knock-out
  - [ ] `[wystup-2006, p. 157]` — wystup-2006: PDF 176
- Origem · **Sinônimo:** accumulative forward
  - [ ] `[wystup-2006, p. 156]` — wystup-2006: PDF 175
- Restrições · Costuma ter custo zero e não tem pior caso garantido
  - [ ] `[wystup-2006, pp. 156–157]` — wystup-2006: PDF 175–176

## ACCUKI

- Origem · **Composição:** accumulator que só começa a acumular depois que o spot toca uma barreira knock-in americana
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Barreira:** ki, uma barreira, contínua em FX
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Payoff:** acumulativo
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Variante de:** ACCU, com knock-in
  - [ ] `[ovml]` — texto Bloomberg na nota

## ACCUKO

- Origem · **Composição:** accumulator cujos fixings restantes são cancelados se o spot tocar uma barreira knock-out americana; o acumulado até ali vale
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Barreira:** ko, uma barreira, contínua em FX
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 157]` — wystup-2006: PDF 176
- Origem · **Payoff:** acumulativo
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Variante de:** ACCU, com knock-out
  - [ ] `[ovml]` — texto Bloomberg na nota
- Restrições · O fixing do dia conta para o acumulado se ocorrer antes do knock-out
  - [ ] `[wystup-2006, p. 157]` — wystup-2006: PDF 176
