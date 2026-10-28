# Validação — lote 2

Marque cada item depois de conferir a afirmação na página indicada. Itens com ⚠ são inferências: confira as premissas.

## Pontos de atenção

- **FX e FWD:** a Bloomberg descreve o resultado só pela ótica do comprador. A nota registra que o vendedor tem o resultado oposto; no FX isso é inferência.
- **CASH:** a única fonte é o OVML.

## EU

- Origem · **Composição:** uma call ou uma put; a tabela mostra a call
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Instrumento:** opção europeia: exercício só no vencimento
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[hull-2015, p. 9]` — hull-2015: PDF 32
  - [ ] `[wystup-2006, p. 3]` — wystup-2006: PDF 22
- Restrições · Em FX, as vanillas são em geral europeias
  - [ ] `[wystup-2006, p. 3]` — wystup-2006: PDF 22
- Origem · **Payoff:** vanilla: exercida com lucro se o spot no vencimento estiver acima (call) ou abaixo (put) do strike
  - [ ] `[ovml]` — texto Bloomberg na nota

## AM

- Origem · **Composição:** uma call ou uma put; a tabela mostra a call
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Instrumento:** opção americana: exercício a qualquer momento até o vencimento
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[hull-2015, p. 9]` — hull-2015: PDF 32
- Origem · **Payoff:** vanilla
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Variante de:** EU, com exercício a qualquer momento até o vencimento
  - [ ] `[hull-2015, p. 213]` — hull-2015: PDF 236
- Restrições · Pouco usada em FX, exceto em time options
  - [ ] `[wystup-2006, pp. 3–4]` — wystup-2006: PDF 22–23

## FX

- Origem · **Composição:** contrato de troca de moedas na data spot
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[hull-2015, p. 6]` — hull-2015: PDF 29
- Origem · **Strikes:** a taxa do contrato (K1)
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Vencimento:** data spot
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Vencimento:** entrega quase imediata; por padrão, 2 dias úteis após a negociação
  - [ ] `[hull-2015, p. 6]` — hull-2015: PDF 29
  - [ ] `[wystup-2006, p. 135]` — wystup-2006: PDF 154
- Origem · **Payoff:** ganha-se se a taxa do contrato for menor que a taxa do dia
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Payoff:** linear; esse é o resultado do comprador da moeda do notional, e o vendedor tem o oposto
  - [ ] `[inferência: spot e forward diferem só na data de entrega, hull-2015, p. 6; no forward, a posição comprada recebe ST − K e a vendida K − ST, hull-2015, p. 7]` — hull-2015: PDF 29; hull-2015: PDF 30 ⚠ inferência

## FWD

- Origem · **Composição:** contrato de troca de moedas na data de entrega especificada
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[wystup-2006, p. 139]` — wystup-2006: PDF 158
- Origem · **Strikes:** a taxa do contrato (K1), o preço de entrega
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[hull-2015, p. 7]` — hull-2015: PDF 30
- Origem · **Vencimento:** data de entrega futura
  - [ ] `[hull-2015, p. 6]` — hull-2015: PDF 29
- Origem · **Payoff:** linear: ST − K na posição comprada, K − ST na vendida
  - [ ] `[hull-2015, p. 7]` — hull-2015: PDF 30
  - [ ] `[wystup-2006, p. 139]` — wystup-2006: PDF 158
- Origem · **Payoff:** o OVML descreve o resultado do comprador da moeda do notional
  - [ ] `[inferência: o texto da Bloomberg descreve lucro quando a taxa do contrato é menor que a taxa do dia; esse é o payoff ST − K da posição comprada, hull-2015, p. 7]` — hull-2015: PDF 30 ⚠ inferência
- Restrições · Custo zero na entrada quando a taxa do contrato é a forward de mercado;. Com outra taxa, há prêmio
  - [ ] `[hull-2015, pp. 112–113]` — hull-2015: PDF 135–136
  - [ ] `[wystup-2006, p. 140]` — wystup-2006: PDF 159
  - [ ] `[wystup-2006, p. 140]` — wystup-2006: PDF 159

## CASH

- Origem · **Composição:** pagamento ou recebimento de um valor em dinheiro; a tabela mostra o recebimento
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Vencimento:** a data de entrega especificada
  - [ ] `[ovml]` — texto Bloomberg na nota
- Notas · Fonte única para a definição: OVML. Nenhuma fonte de `fontes/` define esta estrutura
  - [ ] `[inferência: cobertura por estrutura em `fontes/README.md`]` ⚠ inferência
