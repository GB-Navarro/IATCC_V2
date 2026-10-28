# Validação D38 — dados do DTCC
Validador: agente independente · 2026-10-23 · Python 3.11 (`-I`) sobre `CFTC_CUMULATIVE_FOREX_2026_10_21.csv`. Grupos por união de registros consecutivos da mesma chave (plataforma, par). Para estimar junções por acaso, desloco o instante de cada opção em ±5, 15, 30 e 60 min (scripts nesta pasta).

## Resumo
| Decisão | Veredito | Em uma linha |
|---|---|---|
| 6 — delta hedge (< 90%) | ◐ | O limite cai num vale vazio (75–90%: 2 casos), mas nenhum dos 53 forwards ≥ 90% é perna: 41 são fluxo de NDF sem relação e 12 são hedge de digital. |
| 7 — janela 2 s + 60 s para pacotes | ◐ | 2 s é o ótimo medido. A extensão de 60 s cria mais junções por acaso (+107) do que ligações reais (+67) e deve sair. |
| 9 — não guardar amostra nem scripts | ◐ | Os arquivos antigos continuam disponíveis (testei até 2 anos, CRC idêntico ao local). Sem os scripts, porém, os números não se reproduzem. |

## Limpeza usada (base de todos os números)
- **Do bruto ao limpo:** 61.562 linhas → 53.723 negócios (49.379 forwards, 3.422 opções, 922 outros).
  - Ficam só NEWT/TRAD; saem COMP (821), NOVA (93) e EXER (1).
  - Saem 401 NEWT cancelados por EROR; em 1.144 NEWT, aplico a última CORR.
  - Saem 231 negócios executados fora de 21/10.
- **Correções de outros dias:** 177 CORR e 64 EROR apontam para originais que não estão no arquivo. As correções dos negócios de 21/10 também chegam nos arquivos dos dias seguintes.
- **`Delivery Type`:** vazio nas 61.562 linhas. Entregável ou não só se sabe pelo FISN (NDF/NDO).
- **Notional com "+":** 915 linhas. Há também valores-placeholder, como `99,999,999,999,999,999,999.99999` numa digital INR.
- **Duplicatas exatas de opção:** 108 conjuntos (223 registros) com mesma plataforma, instante, FISN, notional, strike e vencimento. Desses registros, 155 (70%) são PB=TRUE: espelhos de prime brokerage. Somar "pernas idênticas" dobra o notional.

## Decisão 6 — delta hedge
- **Veredito:** ◐
- **Base:** 523 forwards em 358 grupos com opção (W = 2 s); 34 têm "+" e 5 têm notional zero ou placeholder.
- **A favor:**
  - Razão fwd/maior opção do grupo (n = 485): <10%: 109 · 10–25: 128 · 25–50: 164 · 50–75: 29 · **75–90: 2** · 90–105: 16 · 105–150: 2 · >150: 35.
  - Razão fwd/soma das opções: 434 abaixo de 90% e 51 acima. Com as duas definições o vale fica entre 75% e 90%.
  - Forwards de pacote com vencimento igual ao de uma opção (±5 d), n = 215: 205 abaixo de 75% e nenhum entre 75% e 150%.
  - Forwards de prazo spot (≤ 5 d), n = 31: todos abaixo de 75%.
  - Exemplos de hedge bem classificado:
    - TPSE EUR USD 19:36:57: call 1,139 + put 1,1105 (venc. 19/11, ~30 M EUR) + Fwd 15,1 M EUR (venc. 23/11), razão 0,50.
    - BGCD BRL USD 15:38:37: straddle NDO 5,195 (5,0 M USD) + NDF 962 mil USD, razão 0,19.
  - Notionals com "+": usando o "+" como piso (forward) ou teto (opção), 32 dos 34 casos ficam decidíveis.
- **Contra / contraexemplos:**
  - Nenhum dos 53 forwards ≥ 90% (pela maior opção) é perna de TF ou COL. Não houve, neste dia, nenhum forward de pacote com o vencimento da opção e notional entre 90% e 110%. O lado "perna" da regra nunca acerta e gera 53 pernas falsas.
  - **41 dos 53 são fluxo de NDF sem relação:** não pacote, outro vencimento, quase todos BILT TWD/BRL/KRW. Exemplo: BILT TWD USD 01:55:22, NDF 1.000.000 USD (venc. 23/11, pac = F) num grupo com NDO put 34,6 de 1.011.560 USD (venc. 21/10/2027). A razão é 0,99, então pela D6 vira perna.
  - **12 dos 53 são hedge de digital** (11 com vencimento casado): o notional da digital é o payout, e o delta dela passa de 100% do payout. Exemplo: BILT BRL USD 12:41:43, O Dig Call 4,75 de 10 M USD (venc. 21/01/2027) + NDF 45,08 M USD (venc. 25/01/2027), ambos pacote, razão 4,5. Entre os 20 forwards casados com digitais, 13 dão ≥ 90%.
  - **Comparar com a soma de todas as opções do grupo não serve em grupos de carteira:** TPSE EUR USD 09:59:41 tem 23 opções e 23 forwards no mesmo segundo, e cada forward dá ≤ 3% da soma.
- **Outros sinais (hedge com vencimento casado × fluxo sem relação):**

  | Sinal | Hedge | Fluxo sem relação |
  |---|---|---|
  | Mesmo segundo da opção | 88–100% | 25% |
  | Mesmo indicador PB | 93–100% | 55% |
  | Mesma moeda na perna 1 | 73–100% | 51% |
  | Mais forwards que opções | 0–13% | 71% |

- **Ajuste proposto:**
  1. Primeiro, tirar do grupo o forward que não é pacote **e** não tem prazo spot nem o vencimento (±5 d) de alguma opção: é fluxo sem relação (140 dos 484).
  2. Calcular a razão contra a maior opção **de vencimento casado**, não contra a soma do grupo.
  3. Hedge quando a razão < 90%, ou quando a opção casada é digital, qualquer que seja a razão.
  4. Perna quando a razão fica entre 90% e 110%, com vencimento casado.
  5. O resto vai para revisão.
  6. Notional com "+": usar como limite (piso ou teto).
  - Neste dia, a regra dá 326 hedges, 140 fora do grupo e 18 para revisão (11 digitais + 7 de pacote com outro vencimento).

## Decisão 7 — janela de agrupamento
- **Veredito:** ◐ (2 s ✅; extensão de 60 s para pacotes ✗)
- **A favor (W = 2):**

  | W | grupos c/ opção | opções isoladas | grupos >5 / >10 | pacote c/ outro pacote | grupos mistos pac/não | acaso¹ | obs − acaso² |
  |---|---|---|---|---|---|---|---|
  | 0 | 2.136 | 1.158 | 27 / 7 | 77,8% | 43 | 1,1% | 2.135 |
  | 1 | 2.001 | 917 | 35 / 6 | 84,9% | 57 | 2,7% | 2.314 |
  | **2** | 1.988 | 882 | 42 / 7 | 85,2% | 65 | 3,9% | 2.309 |
  | 5 | 1.961 | 820 | 68 / 19 | 85,9% | 91 | 6,8% | 2.267 |
  | 10 | 1.921 | 766 | 117 / 43 | 86,3% | 119 | 9,7% | 2.219 |
  | 2 + pac. 30 s | 1.925 | 839 | 58 / 8 | 87,6% | 66 | | |
  | 2 + pac. 60 s | 1.878 | 812 | 74 / 10 | 89,0% | 67 | | |
  | 2 + pac. 120 s | 1.836 | 791 | 87 / 16 | 90,3% | 68 | | |

  ¹ Opções em plataforma com outro registro da mesma chave a ≤ W s do instante deslocado.
  ² Opções com vizinho observado menos o esperado por acaso.

  - O ganho líquido máximo está em W = 1–2.
  - W = 0 perde 233 opções cujo vizinho está a exatamente 1 s (o arredondamento para segundos corta as pernas).
  - De 2 para 10 s, a contaminação por NDF sem relação sobe de 74 para 153 grupos, e os grupos encadeados (duração > W) sobem de 23 para 102.
- **Contra a extensão de 60 s:**
  - **Opção de pacote → outro pacote, em plataforma:** o observado sobe de 83,5% para 87,4% (+67 registros), mas o acaso sobe de 0,4% para 6,6% (+107). O ganho líquido cai de 1.428 para 1.388 (com 30 s: 1.411).
  - **Pernas isoladas recuperadas (70):** só 8 são plausíveis (mesmo vencimento e mesmo notional de outra perna); 10 são ambíguas; 28 repetem uma perna já existente (mesmo C/P, strike e vencimento); 24 têm outro vencimento. Com 30 s: 43 (6 plausíveis). Com 120 s: 91 (8 plausíveis).
  - **Fusões de dois ou mais grupos já completos (46):** 30 são réplicas da mesma estrutura, 7 têm vencimentos disjuntos e 9 são outras. Com 30 s: 22 (13 + 2). Com 120 s: 64 (41 + 12). Exemplos:
    - TPSE EUR USD: straddle 1,1245 de 49,8 M EUR às 13:27:07 e o mesmo straddle de 37,35 M às 13:27:47 viram um grupo de 4 pernas.
    - TPSE CAD USD: calls 1,40/1,4025 + 2 fwds (30 M) às 12:25:14 e a mesma estrutura de 50 M às 12:25:23.
    - BGCD BRL USD: straddle 5,195 venc. 20/04/2027 + NDF às 15:38:37 e straddle 5,3535 venc. 21/10/2027 + NDF às 15:39:21.
  - **Único exemplo plausível:** XXXX EUR USD, puts 1,105 e 1,095, 10 M EUR cada, venc. 16/06/2027, às 09:53:39 e 09:54:21.
- **Outros problemas da W = 2:**
  - **Grupos grandes:** 42 grupos com > 5 registros, dos quais 28 têm duração ≤ 1 s, e nenhuma janela os separa. Exemplos:
    - BILT SAR USD: 111 registros, 37 vencimentos × (Bar, Van, Dig).
    - TPSE EUR USD: 23 pares opção + hedge no mesmo segundo.
  - **Pacotes sem par:** 307 opções de pacote (14,8%) ficam sem outro pacote no grupo. Para 244 delas não há nenhum pacote a ≤ 2 s em todo o arquivo: o par está fora deste relatório. Por isso a coerência com o pacote não passa de ~85%.
- **Fora de plataforma:**
  - Plataforma vazia só aparece em 101 linhas brutas (89 EROR e 12 TERM); nenhum negócio válido fica com ela. Os negócios fora de plataforma vêm como XXXX (6.138) ou XOFF (2.106), e entre eles há 185 opções.
  - Com W = 2 e chave XXXX ou XOFF, os 51 grupos com opção e mais de um registro parecem coerentes: 45 têm duração 0 s.
  - Acaso a ≤ 2 s: 0,3% com XXXX e XOFF separados, 1,0% com os dois juntos e 6,2% ignorando a plataforma. O observado fica em 57,3%, 57,3% e 59,5%, ou seja, juntar não ganha nada.
  - A 60 s, o acaso fora de plataforma sobe para 11,6%.
- **Ajuste proposto:**
  - W = 2 s para todos, **sem** a extensão de 60 s.
  - XXXX e XOFF como chaves separadas; plataforma vazia, se aparecer, como chave própria só com W = 0.
  - Marcar para revisão, em vez de casar, os grupos com mais de 5 registros.
  - Antes de somar pernas idênticas, tirar as duplicatas exatas de PB.

## Decisão 9 — amostra e scripts fora do projeto
- **Veredito:** ◐
- **A favor:**
  - GET com resposta `200 application/octet-stream` e bytes iniciais `PK\x03\x04` para 21/10/2026, 22/10/2026, 23/09/2026, 24/07/2026, 23/04/2026, 23/10/2025 e 23/10/2024. Domingo (25/10/2026) dá 404.
  - O cabeçalho do zip guarda a data de geração original: 2024-10-23 20:03, 2025-10-23 20:02, 2026-07-24 20:15 etc. Os arquivos antigos não são regerados.
  - O zip de 21/10/2026 servido hoje tem CRC32 `0x8b3ddf4a` e 33.761.383 bytes, idênticos ao CSV local.
- **Contra:**
  - **HEAD não funciona:** responde 503 para todas as datas. Quem checar a disponibilidade com HEAD conclui errado.
  - **Range ignorado:** o servidor ignora o `Range` e responde 200 com o arquivo inteiro. No primeiro teste baixei o zip todo (2,5 MB) e apaguei em seguida. Depois disso, só li os 128 primeiros bytes, por pipe.
  - **Retenção:** não verifiquei nenhuma política escrita; não há garantia de que os arquivos sigam disponíveis.
  - **Scripts (o problema maior):** os números de D6 e D7 dependem de escolhas de limpeza que não estão em nenhum outro lugar, como EROR, CORR, NEWT/TRAD, filtro de data, "+" e placeholders. Ao reimplementar, tive de decidir cada uma.
- **Ajuste proposto:**
  - Manter o novo download, mas guardar no projeto um manifesto mínimo: URL, data, CRC32 e tamanho (lidos dos 30 primeiros bytes do zip), contagem de linhas e as regras de limpeza.
  - Guardar os scripts de análise, que são poucos KB.
  - Checar a disponibilidade com GET, nunca com HEAD.
