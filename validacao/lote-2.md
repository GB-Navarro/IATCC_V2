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

## FX

- Origem · **Composição:** contrato de troca de moedas na data spot
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[hull-2015, p. 6]` — hull-2015: PDF 29
- Origem · **Strikes:** a taxa do contrato (K1)
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Vencimento:** data spot: entrega quase imediata
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[hull-2015, p. 6]` — hull-2015: PDF 29
- Origem · **Payoff:** linear: o comprador ganha se a taxa do contrato for menor que a taxa do dia
  - [ ] `[ovml]` — texto Bloomberg na nota
- Restrições · O resultado descrito é o do comprador; o vendedor tem o resultado oposto
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[inferência: como no forward, hull-2015, p. 7]` — hull-2015: PDF 30 ⚠ inferência

## FWD

- Origem · **Composição:** contrato de troca de moedas numa data futura
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[hull-2015, p. 6]` — hull-2015: PDF 29
- Origem · **Strikes:** a taxa do contrato (K1), o preço de entrega
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[hull-2015, p. 7]` — hull-2015: PDF 30
- Origem · **Vencimento:** data de entrega futura
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[hull-2015, p. 6]` — hull-2015: PDF 29
- Origem · **Payoff:** linear: ST − K na posição comprada, K − ST na vendida
  - [ ] `[hull-2015, p. 7]` — hull-2015: PDF 30
- Restrições · Não custa nada para entrar
  - [ ] `[hull-2015, p. 7]` — hull-2015: PDF 30
- Restrições · O resultado descrito pela Bloomberg é o do comprador; a posição vendida tem o resultado oposto
  - [ ] `[ovml]` — texto Bloomberg na nota
  - [ ] `[hull-2015, p. 7]` — hull-2015: PDF 30

## CASH

- Origem · **Composição:** pagamento ou recebimento de um valor em dinheiro
  - [ ] `[ovml]` — texto Bloomberg na nota
- Origem · **Vencimento:** a data de entrega especificada
  - [ ] `[ovml]` — texto Bloomberg na nota
- Notas · Fonte única: OVML
  - [ ] `[ovml]` — texto Bloomberg na nota
