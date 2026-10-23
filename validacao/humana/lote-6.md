# Validação — lote 6

Marque cada item depois de conferir a afirmação na página indicada. Itens com ⚠ são inferências: confira as premissas.

## Pontos de atenção

- **COL é uma estrutura fora do OVML:** não há texto da Bloomberg; tudo vem das fontes.
- **Escolha da forma:** nas fontes, "collar" tem três sentidos (par de opções = RR; posição + put + call = fence; collar de juros). A nota registra a forma com a posição protegida, a única que não duplica o RR.
- **Natenberg pp. 263–265:** o deslocamento nessas páginas é 9 (PDF 272–274), não 10.

## COL

- Origem · **Composição:** posição comprada no ativo, compra de uma put protetora e venda de uma call coberta
  - [ ] `[natenberg-1994, p. 264]` — natenberg-1994: PDF 273
- Origem · **Composição:** na versão vendida: posição vendida no ativo, compra de call e venda de put
  - [ ] `[natenberg-1994, p. 264]` — natenberg-1994: PDF 273
- Origem · **Strikes:** put abaixo do preço da posição, call acima
  - [ ] `[natenberg-1994, p. 263, exemplo]` — natenberg-1994: PDF 272
  - [ ] `[hull-2015, p. 370, exemplo]` — hull-2015: PDF 393
- Origem · **Vencimento:** o mesmo nas três pernas
  - [ ] `[inferência: as opções vencem na data do fluxo protegido, hull-2015, p. 370; a fence é uma split-price conversion, natenberg-1994, p. 264, e a conversion usa o mesmo vencimento, natenberg-1994, p. 218]` — hull-2015: PDF 393; natenberg-1994: PDF 273; natenberg-1994: PDF 227 ⚠ inferência
- Origem · **Notional:** igual nas três pernas: uma put e uma call para a posição
  - [ ] `[natenberg-1994, p. 263, exemplo]` — natenberg-1994: PDF 272
  - [ ] `[natenberg-1994, p. 264, exemplo]` — natenberg-1994: PDF 273
  - [ ] `[hull-2015, p. 370, exemplo]` — hull-2015: PDF 393
- Origem · **Moneyness:** put e call OTM
  - [ ] `[natenberg-1994, p. 263, exemplo]` — natenberg-1994: PDF 272
  - [ ] `[hull-2015, p. 370, exemplo]` — hull-2015: PDF 393
- Origem · **Instrumento:** a posição no ativo é representada por um FWD
  - [ ] `[inferência: em FX, a posição protegida é a compra ou venda futura da moeda, hull-2015, p. 370]` — hull-2015: PDF 393 ⚠ inferência
- Origem · **Instrumento:** opções europeias
  - [ ] `[hull-2015, p. 370]` — hull-2015: PDF 393
- Origem · **Composta de:** FWD (a posição) e RR na versão short (put comprada, call vendida)
  - [ ] `[inferência: natenberg-1994, p. 264 + tabela de pernas do RR]` — natenberg-1994: PDF 273 ⚠ inferência
- Origem · **Sinônimo:** fence
  - [ ] `[natenberg-1994, p. 264]` — natenberg-1994: PDF 273
- Origem · **Sinônimo:** collar
  - [ ] `[inferência: o collar de juros é "a fence done in the interest rate market", natenberg-1994, p. 265; a fence inclui a posição, natenberg-1994, p. 264]` — natenberg-1994: PDF 274; natenberg-1994: PDF 273 ⚠ inferência
- Restrições · O custo é zero quando a put e a call têm o mesmo preço; se a call vale mais, a estrutura gera crédito. Em geral, a proteção sai a custo baixo ou com crédito
  - [ ] `[natenberg-1994, p. 263, exemplo]` — natenberg-1994: PDF 272
  - [ ] `[natenberg-1994, p. 264]` — natenberg-1994: PDF 273
- Restrições · A versão comprada equivale a um bull spread montado de forma sintética
  - [ ] `[natenberg-1994, p. 264]` — natenberg-1994: PDF 273
- Restrições · Só casa quando a posição protegida (o FWD) está no mesmo grupo; se vierem só as duas opções, a receita que casa é a do [[RR]], na versão short
  - [ ] `[inferência: tabelas de pernas do COL e do RR]` ⚠ inferência
- Restrições · A versão vendida é a regra global de short. O espelho do `_schema.md` não se aplica, porque não inverte o lado da posição
  - [ ] `[inferência: regras de short e espelho do _schema.md]` ⚠ inferência
- Notas · No OVML, "collar" nomeia sempre o par de opções: o RR, "Risk Reversal (Collar)", e duas variantes dele, [[ARC]] e [[EC]]. O Wystup também chama o par de collar: "A popular liquid product in FX markets is the Risk Reversal or collar.". Nesta…
  - [ ] `[inferência: nomes e textos da Bloomberg do RR, do ARC e do EC]` ⚠ inferência
  - [ ] `[wystup-2006, p. 31]` — wystup-2006: PDF 50
- Notas · O Hull lista nomes para o range forward, que é só o par de opções: "Other names used for a range forward contract are zero-cost collar, flexible forward, cylinder option, option fence, min–max, and forward band.". O RF do OVML é outra estru…
  - [ ] `[hull-2015, p. 599]` — hull-2015: PDF 622
  - [ ] `[wystup-2006, pp. 151–152]` — wystup-2006: PDF 170–171
  - [ ] `[inferência: texto da Bloomberg do RF]` ⚠ inferência
- Notas · O Natenberg dá outros nomes à fence: "Fences go by a variety of names: range forwards, tunnels, cylinders; among floor traders they are sometimes known as split-price conversions and reversals.". Eles ficam fora de `aliases`: range forward …
  - [ ] `[natenberg-1994, p. 264]` — natenberg-1994: PDF 273
  - [ ] `[hull-2015, p. 599]` — hull-2015: PDF 622
  - [ ] `[natenberg-1994, p. 218]` — natenberg-1994: PDF 227
  - [ ] `[wystup-2006, p. 179]` — wystup-2006: PDF 198
- Notas · O collar de juros, cap comprado e floor vendido, é outro produto, fora do escopo da base. O Natenberg o descreve como "simply a fence done in the interest rate market."
  - [ ] `[hull-2015, p. 679]` — hull-2015: PDF 702
  - [ ] `[natenberg-1994, p. 265]` — natenberg-1994: PDF 274
- Notas · O collar extra series do Wystup é outra estrutura: em cada vencimento, uma call garante o pior caso e, se o knock-in ocorrer, fica travado um forward no caso melhorado. Corresponde ao [[BFW]] do OVML
  - [ ] `[wystup-2006, pp. 172–173]` — wystup-2006: PDF 191–192
