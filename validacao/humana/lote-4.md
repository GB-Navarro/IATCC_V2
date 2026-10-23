# Validação — lote 4

Marque cada item depois de conferir a afirmação na página indicada. Itens com ⚠ são inferências: confira as premissas.

## Pontos de atenção

- **FE:** o FE do OVML é o *forward plus* do Wystup (conflito de nome). A equivalência com o shark forward é inferência pela paridade KO + KI = vanilla.
- **RF:** coincide com o range forward do Wystup. O Hull usa o nome para o collar, e o Wystup também o chama de *bonus forward*, que no OVML é o BFW.
- **BFW:** a tabela de três pernas vem do *collar extra* do Wystup (pp. 172–173), que tem a mesma composição do BFW do OVML.
- **KKF:** a tabela de duas pernas (KO call comprada, KIKO put vendida) é inferência, assim como a KIKO ser do tipo KOKI.
- **EC, TF e ARC:** vencimento, notional e (no ARC) strikes e moneyness são inferidos. No EC, a put fica abaixo da call, por inferência; o TF tem `flexivel: strike`.
- **TF:** a versão com venda de forward e compra de call não é coberta pelas regras de short e espelho.
- **Só OVML para a definição:** EC, KKF, TF, EF, BFF e ACCUKI.

## FE

- Origem · **Composição:** compra de call vanilla e venda de put reverse knock-in, no mesmo strike
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Composição:** equivale a um forward sintético mais um reverse knock-out, a composição do shark forward
  - [ ] `[wystup-2006, pp. 164, 273]` — wystup-2006: PDF 183, 292
  - [ ] `[inferência: call − put + RKO = call − RKI, pela paridade KO + KI = vanilla, wystup-2006, p. 42]` — wystup-2006: PDF 61 ⚠ inferência
- Origem · **Strikes:** o mesmo nas duas pernas
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Vencimento:** o mesmo nas duas pernas
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 145, exemplo]` — wystup-2006: PDF 164
- Origem · **Notional:** igual nas duas pernas
  - [ ] `[inferência: o double shark forward aumenta o notional do reverse knock-in "commonly by a factor of 2", logo no padrão são iguais, wystup-2006, p. 164]` — wystup-2006: PDF 183 ⚠ inferência
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
  - [ ] `[inferência: texto da Bloomberg do FE + wystup-2006, pp. 145, 164]` — wystup-2006: PDF 164, 183 ⚠ inferência
  - [ ] `[wystup-2006, p. 145]` — wystup-2006: PDF 164

## EC

- Origem · **Composição:** compra de call vanilla e venda de put knock-in com barreira dentro do dinheiro
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Barreira:** reverse knock-in: barreira dentro do dinheiro
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 42]` — wystup-2006: PDF 61
- Origem · **Strikes:** diferentes; put abaixo da call, como no RR
  - [ ] `[inferência: o texto da Bloomberg descreve uma alternativa ao RR, com "flexibility between the best and worse case rates"; com strikes iguais seria o FE]` ⚠ inferência
- Origem · **Vencimento:** o mesmo nas duas pernas
  - [ ] `[inferência: o texto da Bloomberg descreve uma alternativa ao RR, e o RR tem um só vencimento, ver nota RR]` ⚠ inferência
- Origem · **Notional:** igual nas duas pernas
  - [ ] `[inferência: idem; o RR tem notional igual nas duas pernas, ver nota RR]` ⚠ inferência
- Origem · **Composta de:** EU e KI
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Variante de:** RR, numa versão de menor risco
  - [ ] `[ovml]` — texto Bloomberg na nota
- Notas · O "Knock-In put option with a barrier that is in-the-money" da Bloomberg é um reverse knock-in, o mesmo termo usado no FE e no BFW: "regular barriers are out of the money, reverse barriers are in the money"
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 42]` — wystup-2006: PDF 61
- Notas · Fonte única para a definição: OVML. Nenhuma fonte de `fontes/` define esta estrutura
  - [ ] `[inferência: cobertura por estrutura em `fontes/README.md`]` ⚠ inferência

## BFW

- Origem · **Composição:** compra de uma knock-out e de uma knock-in e venda de uma reverse knock-in, todas com a mesma barreira
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Composição:** antes da barreira o cliente tem uma opção comprada; depois, um forward na taxa bônus (K1)
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Composição:** call knock-out comprada no pior caso; put knock-in (reverse) vendida e call knock-in comprada no caso melhorado; todas com a mesma barreira
  - [ ] `[wystup-2006, p. 173]` — wystup-2006: PDF 192
- Origem · **Strikes:** as duas knock-in no mesmo strike (o caso melhorado), a knock-out em outro (o pior caso)
  - [ ] `[wystup-2006, p. 173]` — wystup-2006: PDF 192
- Origem · **Strikes:** o caso melhorado pode ser igual ao forward outright
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 173, exemplo]` — wystup-2006: PDF 192
- Origem · **Composta de:** KO e KI
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 173]` — wystup-2006: PDF 192
- Restrições · A tabela segue o collar extra, com o strike da knock-out acima do das knock-in. No boomerang forward, a mesma composição aparece com a ordem inversa
  - [ ] `[wystup-2006, p. 173, exemplo]` — wystup-2006: PDF 192
  - [ ] `[wystup-2006, p. 161]` — wystup-2006: PDF 180
- Restrições · Pode ser montado a custo zero
  - [ ] `[ovml]` — texto Bloomberg na nota
- Notas · O Wystup usa *bonus forward* como sinônimo de range forward: "The range or bonus forward is another forward enhancement with guaranteed worst case.". O BFW do OVML é outra estrutura
  - [ ] `[wystup-2006, p. 151]` — wystup-2006: PDF 170
  - [ ] `[inferência: texto da Bloomberg do BFW + wystup-2006, p. 152]` — wystup-2006: PDF 171 ⚠ inferência
- Notas · O BFW do OVML corresponde ao *collar extra* do Wystup, com a mesma composição e barreira comum
  - [ ] `[wystup-2006, pp. 172–173]` — wystup-2006: PDF 191–192

## KKF

- Origem · **Composição:** compra de uma knock-out e venda de uma KIKO
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Composição:** KO call comprada e KIKO put vendida
  - [ ] `[inferência: comprar uma opção e vender outra no mesmo strike, para ficar "hedged at the strike" como num forward, exige call comprada e put vendida, como no forward sintético, wystup-2006, p. 140]` — wystup-2006: PDF 159 ⚠ inferência
- Origem · **Strikes:** o mesmo nas duas pernas
  - [ ] `[inferência: o texto da Bloomberg diz que o cliente fica "hedged at the strike"]` ⚠ inferência
- Origem · **Composta de:** KO e KIKO
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Composta de:** a KIKO é do tipo KOKI: se o KO é tocado primeiro, o hedge se perde mesmo que o KI venha depois (exclui o tipo 2); se o KI vem primeiro e o KO depois, o hedge também se perde (exclui o tipo 3)
  - [ ] `[inferência: texto da Bloomberg do KKF + wystup-2006, p. 115]` — wystup-2006: PDF 134 ⚠ inferência
- Restrições · Pode ser montado a custo zero
  - [ ] `[ovml]` — texto Bloomberg na nota
- Notas · Fonte única para a definição: OVML. As fontes tratam só componentes ou estruturas parecidas
  - [ ] `[inferência: páginas indicadas para esta estrutura na cobertura de `fontes/README.md`]` ⚠ inferência

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
  - [ ] `[inferência: o texto da Bloomberg fala em "protection rate for their full hedge amount" e em participar de "any favourable market movements"]` ⚠ inferência
- Origem · **Composta de:** FWD e EU
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[inferência: convenção do _schema.md, combinações de vanillas usam opções europeias]` ⚠ inferência
- Restrições · A versão com venda de forward e compra de call não é coberta pelas regras de short e espelho, porque o espelho não inverte o lado do forward
  - [ ] `[inferência: regras do _schema.md]` ⚠ inferência
- Notas · Fonte única para a definição: OVML. Nenhuma fonte de `fontes/` define esta estrutura
  - [ ] `[inferência: cobertura por estrutura em `fontes/README.md`]` ⚠ inferência

## RF

- Origem · **Composição:** forward sintético no strike do pior caso mais compra de um double-no-touch
  - [ ] `[wystup-2006, pp. 152, 324]` — wystup-2006: PDF 171, 343
- Origem · **Composição:** forward sintético: compra de call e venda de put, mesmo strike e mesmo notional
  - [ ] `[wystup-2006, p. 140]` — wystup-2006: PDF 159
- Origem · **Strikes:** o mesmo nas duas opções: o pior caso
  - [ ] `[wystup-2006, p. 152]` — wystup-2006: PDF 171
- Origem · **Vencimento:** o mesmo em todas as pernas
  - [ ] `[inferência: uma única data de vencimento, com o intervalo verificado "at expiry", wystup-2006, p. 151]` — wystup-2006: PDF 170 ⚠ inferência
- Origem · **Notional:** igual nas duas opções
  - [ ] `[wystup-2006, p. 140]` — wystup-2006: PDF 159
- Origem · **Notional:** o pagamento do DNT (r) cobre a diferença entre pior e melhor caso
  - [ ] `[inferência: wystup-2006, p. 152]` — wystup-2006: PDF 171 ⚠ inferência
- Origem · **Barreira:** a tabela representa a versão com barreiras americanas (DNT); na versão básica, o intervalo só é verificado no vencimento, o que equivale a um DNT europeu
  - [ ] `[wystup-2006, pp. 151–152, 324]` — wystup-2006: PDF 170–171, 343
- Origem · **Composta de:** DNT, mais um forward sintético
  - [ ] `[wystup-2006, p. 152]` — wystup-2006: PDF 171
- Restrições · É montado a custo zero, como um forward outright
  - [ ] `[wystup-2006, p. 151]` — wystup-2006: PDF 170
- Notas · O Hull usa *range forward* para o par de opções (RR do OVML): "This is a long position in a range forward contract and the payoff is shown in Figure 17.1b."
  - [ ] `[hull-2015, p. 371]` — hull-2015: PDF 394
- Notas · O Wystup chama a estrutura também de *bonus forward*, nome que no OVML designa outra estrutura ([[BFW]])
  - [ ] `[wystup-2006, p. 151]` — wystup-2006: PDF 170
  - [ ] `[inferência: texto da Bloomberg do BFW + wystup-2006, p. 152]` — wystup-2006: PDF 171 ⚠ inferência

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
- Restrições · Não tem pior caso garantido
  - [ ] `[wystup-2006, p. 144]` — wystup-2006: PDF 163

## EF

- Origem · **Composição:** forward, em geral com razão de notional, estendido por mais um período se o spot ficar além de uma barreira no vencimento
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Barreira:** uma, verificada no vencimento, que dispara a extensão
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Variante de:** FWD, ou PF quando há razão de notional
  - [ ] `[ovml]` — texto Bloomberg na nota
- Notas · Fonte única para a definição: OVML. As fontes tratam só componentes ou estruturas parecidas
  - [ ] `[inferência: páginas indicadas para esta estrutura na cobertura de `fontes/README.md`]` ⚠ inferência
- Notas · O auto-renewal forward do Wystup, uma série de forwards renovada automaticamente, é parecido mas não igual; a renovação dele também depende de uma barreira
  - [ ] `[wystup-2006, p. 163]` — wystup-2006: PDF 182
  - [ ] `[wystup-2006, p. 164]` — wystup-2006: PDF 183

## FLEX

- Origem · **Composição:** forward em que o cliente escolhe a data de entrega dentro de um período
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 166]` — wystup-2006: PDF 185
- Origem · **Payoff:** linear
  - [ ] `[inferência: é um forward, hull-2015, p. 7]` — hull-2015: PDF 30 ⚠ inferência
- Origem · **Sinônimo:** time option
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 166]` — wystup-2006: PDF 185
- Origem · **Sinônimo:** forward de estilo americano
  - [ ] `[wystup-2006, p. 166]` — wystup-2006: PDF 185
- Notas · A Bloomberg fala de uma única data de entrega. O Wystup admite exercer partes do montante em datas diferentes: "The holder can choose times in this period to exercise parts of the total amount, where he or she shouts, which is why this type…
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 167]` — wystup-2006: PDF 186

## BFF

- Origem · **Composição:** forward em que o notional acumula a cada dia com fixing acima ou abaixo da taxa de fade (a barreira)
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Composição:** um valor alavancado pode ser vendido num strike fora do dinheiro para melhorar a taxa
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Payoff:** acumulativo
  - [ ] `[ovml]` — texto Bloomberg na nota
- Notas · Fonte única para a definição: OVML. As fontes tratam só componentes ou estruturas parecidas
  - [ ] `[inferência: páginas indicadas para esta estrutura na cobertura de `fontes/README.md`]` ⚠ inferência
- Notas · É parecido com o fade-in forward, com o boosted spot/forward e com o accumulative forward do Wystup
  - [ ] `[wystup-2006, pp. 142, 156, 165]` — wystup-2006: PDF 161, 175, 184

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
- Restrições · Liquidado em moeda estrangeira, usa o inverso da média do spot, que é a média harmônica da taxa inversa 1/S
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
- Restrições · Notional na moeda doméstica ou média geométrica exigem volatilidade no apreçamento
  - [ ] `[ovml]` — texto Bloomberg na nota
- Notas · Forwards com strike flutuante na média harmônica aparecem no Wystup
  - [ ] `[wystup-2006, p. 132]` — wystup-2006: PDF 151

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
  - [ ] `[inferência: mesma definição do texto da Bloomberg e da wystup-2006, p. 156; o Wystup chama esses produtos de "accumulators", wystup-2006, p. 161]` — wystup-2006: PDF 175; wystup-2006: PDF 180 ⚠ inferência
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
  - [ ] `[wystup-2006, p. 156]` — wystup-2006: PDF 175
- Origem · **Payoff:** acumulativo
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Variante de:** ACCU, com knock-out
  - [ ] `[ovml]` — texto Bloomberg na nota
- Restrições · Por padrão, o fixing do dia conta para o acumulado se ocorrer antes do knock-out; isso deve ser combinado no contrato
  - [ ] `[wystup-2006, p. 157]` — wystup-2006: PDF 176
