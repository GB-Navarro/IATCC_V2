# Decisões

Status: **aceita** (em vigor) · **proposta** (recomendada, ainda não adotada) · **substituída** (indica a que a substitui).

---

### D01 · 2026-10-20 · aceita — Objetivo e fluxo
Agrupar as opções do DTCC por plataforma e timestamp em segundos. Para cada grupo, um agente consulta o `Brain/` para dizer que estruturas as pernas formam.

### D02 · 2026-10-20 · proposta — Refinamentos do agrupamento
- Incluir o subjacente (par de moedas) na chave do grupo.
- Usar o execution timestamp, não o de disseminação.
- Agrupar com janela de ±1–2 s.
- Tratar à parte os trades off-facility, que vêm sem plataforma.
- Remover cancelamentos e correções.
- Usar o `Package indicator` como gabarito da avaliação.
- **Motivo:** sem esses ajustes, o grupo mistura negócios que não têm relação entre si ou separa pernas da mesma estrutura.

### D03 · 2026-10-20 · aceita — O texto da Bloomberg é fonte imutável
As descrições do OVML ficam em `bloomberg_description/` exatamente como foram copiadas. Correções e divergências vão na seção **Notas** da nota canônica. Um hash registrado garante que o texto não muda.
- **Motivo:** manter a fonte original verificável e separada da nossa interpretação.

### D04 · 2026-10-20 · aceita — FE e Variance Forward são a mesma estrutura
Os dois são iguais no OVML. O arquivo duplicado foi removido, e "Variance Forward" virou alias do FE.

### D05 · 2026-10-20 · aceita — SDR e TF estão corretos
O usuário confirmou que os dois trechos apontados na auditoria ("date.Unlike" e "either here") são assim no original.

### D06 · 2026-10-20 · aceita — Descrições antes de facetas e relações
Primeiro cada estrutura ganha uma definição estruturada: pernas e restrições. As facetas e relações saem dela depois.
- **Motivo:** se as tags vierem de prosa livre, a classificação teria de ser refeita a cada ajuste.

### D07 · 2026-10-20 · aceita — Uma nota canônica por estrutura, nomeada pelo código
A nota fica em `structures/<COD>.md` e embute o texto da Bloomberg. Nome e sinônimos vão em `aliases`.
- **Motivo:** se a nota tivesse o mesmo nome do arquivo da Bloomberg, o wikilink ficaria ambíguo. Com o código, a coluna `instrumento` da tabela de pernas já funciona como link.
- **Substitui** a ideia inicial de colocar as tags no frontmatter dos próprios arquivos da Bloomberg.

### D08 · 2026-10-20 · aceita — Facetas em vez de árvore
Cada estrutura recebe tags aninhadas do Obsidian (`pernas/2`, `expiry/igual`…), e a busca é uma interseção de tags. Restrição que não é obrigatória vira `qualquer`, a partir do campo `flexivel`.
- **Motivo:** as dimensões são independentes. Uma árvore impõe uma ordem arbitrária e quebra quando falta um dado.

### D09 · 2026-10-20 · aceita — A tabela de pernas é a fonte da verdade
Tags, `instrumentos` e `ambigua_com` são gerados por script a partir da tabela. Ninguém edita esses campos à mão.
- **Motivo:** editar tags à mão em 65 notas gera inconsistência.

### D10 · 2026-10-20 · aceita — Sem lado no DTCC, o agente devolve hipóteses ranqueadas
O dado público não informa compra/venda. Estruturas que só diferem no lado (SN↔RR, SDR↔PF) recebem `ambigua_com`, calculado pelo script.

### D11 · 2026-10-20 · aceita — Variantes short e espelho são implícitas
- **Short**: inverter todos os lados.
- **Espelho**: trocar call↔put e inverter a ordem dos strikes.

Nenhuma das duas vira nota. Por isso `tipos/` só distingue `mesmo-tipo` de `call-put`.

### D12 · 2026-10-20 · aceita — Moneyness ranqueia, não filtra
ATM, OTM e ITM costumam ser só convenção e raramente são obrigatórios. Usados como filtro, eliminariam estruturas válidas.

### D13 · 2026-10-20 · substituída (D31) — Matching determinístico, LLM depois
Python calcula a assinatura do grupo, testa as divisões possíveis e filtra as candidatas. O LLM só desempata e explica.
- **Motivo:** o resultado fica reprodutível e avaliável, e a combinatória de grupos grandes não fica nas mãos do LLM.

### D14 · 2026-10-20 · aceita — Fontes por família de estrutura
| Família | Fontes |
|---|---|
| Combinações de vanillas | Hull, *Options, Futures, and Other Derivatives* (cap. "Trading Strategies Involving Options"); Natenberg, *Option Volatility and Pricing* |
| Convenções de FX | Reiswich & Wystup, "A Guide to FX Options Quoting Conventions" (2010); Clark, *Foreign Exchange Option Pricing*; Castagna, *FX Options and Smile Risk* |
| Forwards estruturados | Wystup, *FX Options and Structured Products* |
| Exóticos | Haug, *The Complete Guide to Option Pricing Formulas*; Clark |
| Legal e reporte | ISDA 1998 FX and Currency Option Definitions e 2005 Barrier Supplement; FpML; CFTC Part 43; ANNA DSB (UPI) |
| Nomes próprios do OVML | ajuda do OVML e Help Desk da Bloomberg |

Texto escrito por IA conta como rascunho e cita a fonte no nível de capítulo.

### D15 · 2026-10-20 · aceita — Scripts fora do vault, idempotentes
O código fica em `scripts/`. Os scripts não sobrescrevem notas e não escrevem em `bloomberg_description/`. Os hashes ficam em `structures/.bloomberg_hashes.json`.

### D16 · 2026-10-20 · aceita — A geração inicial só preenche o mínimo mecânico
O script preenche só o que sai do nome do arquivo: código, alias, embed e `familia: generica` nas 2L–10L. Nenhuma tabela de pernas foi pré-preenchida, nem a dos exóticos de 1 perna.

### D17 · 2026-10-20 · aceita — Atualização contínua dos docs em três camadas
- **`CLAUDE.md`**: define o que é mudança relevante e qual doc atualizar.
- **Hook `Stop`**: ao fim de cada resposta, bloqueia o Claude se `Brain/`, `scripts/`, `CLAUDE.md` ou os hooks mudaram depois da última atualização de `docs/`.
- **Hook `SessionStart`**: na abertura da sessão, informa o que mudou fora do Claude Code.

O hook cobra uma vez por leva de mudanças (marcador em `docs/.ultima_verificacao`) e ignora `.obsidian/`. O Claude decide se a mudança é relevante e pergunta o motivo quando ela envolve uma decisão do usuário.
- **Motivo:** detectar mudanças dá para automatizar; interpretar, não. A regra sozinha depende de memória, e o hook sozinho não sabe o que é relevante.
- **Descartado por ora:** `git init`. Com git, o hook passaria a comparar pelo `git diff`.

### D18 · 2026-10-20 · aceita — Base de estruturas antes de qualquer trabalho com o DTCC
Primeiro a base de estruturas fica completa e validada; nada específico do DTCC por enquanto.
- **Risco aceito:** o mapeamento dos campos do DTCC para a coluna `instrumento`, e as decisões D02 e D13, ficam sem validação até lá. Se os dados contradisserem o schema, ele é revisado.

### D19 · 2026-10-20 · aceita — As notas são preenchidas a partir dos PDFs das fontes
As fontes ficam em `fontes/` e cada afirmação da nota cita `chave, p. N`. O rascunho feito de memória só serve de roteiro de leitura.
- **Fonte principal:** Wystup (2017), que tem a nomenclatura mais próxima do OVML. Hull, Haug e Clark complementam; os artigos gratuitos do Wystup cobrem estruturas específicas.
- **Quando só há o OVML:** estruturas com nome comercial (SDR, BFW, TF, FP, CASH) citam só o OVML, e a nota registra isso.
- **Motivo:** citações com página tornam a base verificável e eliminam a revisão de um rascunho escrito de memória.

### D20 · 2026-10-20 · aceita — Haug e Clark ficam fora da lista principal
O usuário não conseguiu obter os dois livros.
- **Clark: dispensado.** Reiswich & Wystup (2009) e Wystup (2017) cobrem tudo o que ele traria.
- **Haug: em espera.** Decide-se depois de ler as seções 1.7.3, 1.7.4 e 1.8.4 do Wystup. Ele só seria necessário para digitais com barreira e barreiras sequenciais.
- **Revisa** a D19, que listava Haug e Clark como complementares.

### D21 · 2026-10-21 · aceita — Hull na 9ª edição; Haug volta à lista
- **Hull:** fica a 9ª ed. (2015), que é a obtida, e não a 11ª. Toda citação do Hull se refere à paginação da 9ª.
- **Haug:** a 2ª ed. foi obtida e cobre digitais com barreira, barreiras duplas e sequenciais. Revisa a D20 nesse ponto; o Clark continua dispensado.
- **Arquivos de fontes:** nomeados `<chave>_<título-curto>`. A citação usa a página impressa, e o deslocamento em relação ao PDF fica registrado em `fontes/README.md`.

### D22 · 2026-10-21 · aceita — Wystup na 1ª edição; fontes completas
- **Wystup:** a 1ª ed. (2006) substitui a 2ª. Ela cobre tudo o que buscávamos, exceto o condor; o calendar spread vem do Hull.
- **Natenberg:** opcional, só para o CR. Sem ele, o CR cita só o OVML.
- **A leitura resolveu quatro divergências** (detalhes em `fontes/README.md`):
  - RF do OVML = range forward do Wystup;
  - FE do OVML = forward *plus* do Wystup;
  - *bonus forward* do Wystup ≠ BFW do OVML;
  - KOKI e KIKOSQ = tipos 1 e 2 de KIKO do Wystup.

### D23 · 2026-10-21 · aceita — Natenberg (1994) entra como fonte
É a edição revisada de 1994, escaneada e sem camada de texto, por isso a leitura é por imagem, a partir das páginas do índice.
- **CR:** passa a ter fonte acadêmica (p. 158).
- **BF:** o Natenberg confirma a convenção de long/short (iron butterfly, p. 158).
- **CP, SD, SN, CS e DS:** ganham uma segunda fonte.
- **Revisa** a D22 na parte em que o Natenberg era opcional.

### D24 · 2026-10-21 · aceita — Citação em toda afirmação e validação por checklist
- **Formatos:** `[chave, p. N]` (página impressa), `[ovml]` e `[inferência: …]`. As regras completas estão em `Brain/_schema.md`.
- **Citação literal:** só nas **Notas** de divergência, com no máximo uma frase. Nos demais lugares vai só a página.
- **Nova seção Relações:** justifica `composta_de` e `variante_de`, para que todo campo manual tenha citação.
- **Validação por lote:** `scripts/checklist_citacoes.py` gera `validacao/lote-N.md`, com um item por citação e a página do PDF. O lote conta como validado quando todos os itens estiverem marcados.

### D25 · 2026-10-21 · aceita — Tabela de origem em cada nota
A linha `Fonte:` foi substituída por uma tabela de origem (`Informação | Valor | Fonte`) logo abaixo da tabela de pernas. Cada informação tem a sua fonte: as colunas da tabela de pernas e os campos manuais do frontmatter.
- **Seção Relações:** sai. O conteúdo dela vira as linhas Composta de e Variante de.
- **Marcador `, exemplo`:** separa o que a fonte define do que ela só ilustra num exemplo numérico.
- **Checklist:** cada afirmação aparece uma vez, com as fontes como sub-itens marcáveis.
- **Revisa** a D24.
- **Motivo:** o usuário precisa saber exatamente qual fonte sustenta cada informação para validá-la.

### D26 · 2026-10-21 · proposta — Fontes como notas do Brain
Criar uma nota por fonte (ex.: `[[hull-2015]]`) com a referência completa. As citações viram links clicáveis e as fontes aparecem no grafo ligadas às estruturas que sustentam.
- **Adiado:** o usuário quer retomar depois. Não muda a validação, só a navegação e o grafo.

### D27 · 2026-10-21 · aceita — Validação de todos os lotes de uma vez
Os cinco lotes foram preenchidos antes de começar a validação, que o usuário fará numa única passada (`validacao/README.md`).
- **Notas com pernas sem tipo informado (BFW, KKF):** a tabela tem uma linha só, com o próprio código como instrumento. A composição fica em `composta_de`, para não inventar os tipos.
- **Toques (OT, NT, DOT, DNT):** o campo `barreira` registra `ki` quando o toque ativa o pagamento e `ko` quando o cancela.
- **Risco aceito:** um erro de padrão encontrado na validação pode exigir corrigir várias notas de uma vez.

### D28 · 2026-10-21 · proposta — Arquitetura do agente, rastreamento e feedback
- **Arquitetura:** fluxo fixo antes de agente. O matching entrega as candidatas, e uma chamada ao Claude com structured output (códigos em lista fechada) decide. Agente com ferramentas só se a avaliação pedir.
- **Fora do escopo:** sem RAG nem fine-tuning; MCP é opcional.
- **Rastreamento:** cada decisão fica num SQLite com rastro completo e versões. A avaliação humana é feita por campo, com a camada do erro, e alimenta um ciclo de refinamento com um conjunto de teste em que nunca se ajusta nada.
- **Detalhes:** `docs/to-do.md`.

### D29 · 2026-10-21 · substituída (D30) — Agrupamento por intervalo de segundos e plataforma
Os registros do DTCC são agrupados por intervalo de segundos e mesma plataforma de execução.
- **Revisa** a D02: o subjacente não entra na chave do grupo. Por isso o matching precisa da regra genérica "todas as pernas de um bloco têm o mesmo subjacente".
- **Em aberto:** o tamanho do intervalo (Δt) e o tratamento dos trades off-facility, que vêm sem plataforma.

### D30 · 2026-10-21 · aceita — Chave de agrupamento: (intervalo de segundos, plataforma, par de moedas)
O grupo é definido pelo vetor (intervalo de segundos, plataforma de execução, par de moedas).
- **Revisa** a D29: o par de moedas volta à chave. A regra "mesmo subjacente" no matching deixa de ser necessária e vira só uma verificação de consistência.
- **Em aberto:** o tamanho do intervalo (Δt) e o tratamento dos trades off-facility, que vêm sem plataforma.

### D31 · 2026-10-21 · aceita — Duas versões para comparação: Agente e Agente + algoritmos
- **Agente:** o LLM classifica sozinho, com a base.
- **Agente + algoritmos:** as sete estações genéricas de `ideas.md` (ideia 1) resolvem o que é exato, e o LLM entra só nos casos ambíguos.
- **Piloto:** a versão Agente roda nos casos de teste antes de os algoritmos serem construídos (Fase A2).
- **Experimento final:** três braços (algoritmos sozinhos, Agente + algoritmos, Agente).
- **Revisa** a D13, que previa só o matching seguido do LLM.
- **Motivo:** a vantagem dos algoritmos é uma hipótese; o TCC precisa demonstrá-la medindo.

### D32 · 2026-10-22 · aceita — Duas validações separadas: Claude agora, humana depois do MVP
- **Validação do Claude:** feita agora por um agente separado, sem o contexto da conversa que escreveu as notas. O resultado fica em `validacao/claude/`, com veredito e evidência por item, e o MVP segue com a base validada por ela (tag `base-v1-claude`).
- **Validação humana:** feita pelo usuário depois do MVP, em `validacao/humana/`, às cegas (o checklist não mostra os vereditos do Claude). Depois das correções, a base recebe a tag `base-v2-humana` e os resultados do MVP são recalculados.
- **Correções:** a nota é corrigida, o item recebe o veredito ✎ e as seções do checklist humano são geradas de novo.
- **Revisa** a D27 na parte em que o usuário validaria tudo antes de seguir.
- **Motivo:** ganhar tempo sem abrir mão da validação humana. A comparação entre as duas também é um resultado para o TCC.

### D33 · 2026-10-22 · aceita — Correções da validação do Claude no lote 1
- **Correções:** 21 das 25 propostas pelo agente independente foram aplicadas em 12 notas. As principais: o DS ganhou apoio direto (Hull, p. 272); o CR ganhou `variante_de: [[BF]]` e espaçamento igual das pontas; o 25 delta deixou de ser regra no RR e no SN (é exemplo; outros deltas são cotados, Wystup, p. 22); as citações `[ovml]` compostas foram divididas.
- **Padrão corrigido em 8 notas:** "Fonte única: OVML" deixou de citar `[ovml]` (SDR, BFF, CASH, DACCR, EF, FP, KKF, TF).
- **Convenção no `_schema.md`:** combinações de vanillas usam `EU`; a `AM` só aparece como estrutura de uma perna.
- **Pendentes de decisão do usuário:** o `variante_de` do PF (RR ou forward sintético) e os aliases opcionais.

### D34 · 2026-10-22 · aceita — Collar registrado como estrutura fora do OVML; PF e SN ajustados
- **COL:** nas fontes, "collar" tem três sentidos: o par de opções (= RR no OVML, Wystup p. 31 e Hull p. 599), a posição protegida + put comprada + call vendida (*fence*, Natenberg pp. 263–265) e o collar de juros (fora do escopo). Foi registrada como `COL` a forma com a posição, a única que não duplica a receita do RR. É a primeira estrutura fora do OVML: não tem embed nem `[ovml]` (regra no `_schema.md`). O RR aponta para ela, e o COL é validado no lote 6.
- **PF:** `variante_de` passa a ser FWD e RR, cada um com a sua citação (Wystup pp. 140–141). *Leveraged forward* entra nas Notas, não como alias, porque vale só para o estilo de alto risco.
- **SN:** alias "Bottom Vertical Combination" (Hull, p. 269).
- **Deslocamento do Natenberg:** é 10 até a p. 158 e 9 a partir da p. 263. O `checklist_citacoes.py` passou a aceitar faixas de deslocamento.
- **Escolha do usuário:** "Collar" não virou alias do RR, porque o usuário quis o collar como estrutura própria.

### D35 · 2026-10-22 · aceita — Correções das validações do Claude, lotes 2 a 6
- **Resultado:** a validação independente dos lotes 2 a 6 encontrou 4 ✗ (DACCR, FP e duas no EC) e dezenas de citações parciais.
- **Aplicadas** as correções verificadas, em 39 notas. As principais:
  - o BFW ganhou tabela de 3 pernas, pelo *collar extra* do Wystup (pp. 172–173), que tem a mesma composição;
  - o EC perdeu `flexivel: strike`;
  - FX e FWD separaram o que diz o OVML do que vem do Hull e do Wystup;
  - a codificação ki/ko de OT e NT passou a citar o Haug (pp. 177–178);
  - o COL e o RR foram corrigidos.
- **Padrão "Fonte única":** nas estruturas com cobertura parcial, a nota passou a dizer que as fontes tratam só componentes ou estruturas parecidas.
- **Índice de fontes:** cobertura corrigida (FX, FWD, EU, AM, FE, BFW, EC). O deslocamento do Natenberg é 9 a partir da p. 215.
- **Checklists humanos** gerados de novo: 553 itens.
- **Pendentes:** 15 decisões do usuário, listadas no topo de cada relatório em `validacao/claude/`.

### D36 · 2026-10-23 · aceita — Decisões do usuário sobre a validação do Claude (1ª rodada)
- **COL:** mantém o nome Collar. Ganhou a restrição de que só casa quando a posição protegida está no mesmo grupo; sem ela, casa o RR.
- **AM:** passa a ser variante do EU (Hull, p. 213).
- **CMP:** registra os quatro tipos de compound (Hull, p. 602).
- **KOKI:** mantém o alias "KIKO", com nota sobre a ambiguidade (Wystup, p. 116).
- **FE:** ganha o alias "Forward Plus".
- **`_schema.md`:** intervalos de contagem de fixings (FA, ACCR, DACCR) não são barreira.
- **Sem alteração:** `payoff` e `barreira` ficam vazios em notas de uma linha que representam estruturas (EF, KKF).
- **Em discussão:** CASH, "Fonte única" em Notas, FP, DACCR, DISEQ, TF, KKF.
- **Erro corrigido:** cinco notas (AM, EAKO, DIVA, KO, DISEQ) tinham texto duplicado por uma nova execução do script de correções. Foram corrigidas, e uma varredura nas 66 notas não encontrou mais repetições.

### D37 · 2026-10-23 · aceita — Decisões do usuário sobre a validação do Claude (2ª rodada)
- **CASH:** a tabela mostra o recebimento.
- **FP:** `payoff: vanilla` fica como suposição do caso mais comum, citada como inferência; a Bloomberg diz só "an option payoff".
- **DACCR:** tipo `call` ("a tabela mostra a call") e linha de origem para o strike.
- **DISEQ:** sai `barreiras: 2`; a dedução das duas barreiras fica só no texto, como inferência.
- **KKF:** tabela de duas pernas (KO call comprada e KIKO put vendida, mesmo strike), deduzida como no forward sintético e marcada como inferência.
- **`_schema.md`:**
  - Notas aceitam a linha "Fonte única para a definição: OVML";
  - um item em `flexivel` desliga as relações da tabela de pernas naquela coluna (igualdade e ordem dos símbolos; no notional, a razão).
- **Encerramento:** com isso, a validação do Claude está concluída e a base recebe a tag `base-v1-claude`.

### D38 · 2026-10-23 · aceita, sujeita à validação independente — Reorganização da base em pastas por categoria e número de pernas
- **Estrutura:** `vanilla/`, `exotica/`, `linear/` e `generica/`, cada uma com `pernas/N/`. Plano e achados em `docs/dtcc.md`.
- **Decisões do usuário, que seguem as recomendações:**
  1. a categoria vem do produto UPI de cada perna, com a literatura como confirmação;
  2. o FP vai para `vanilla`;
  3. os forwards estruturados (ACCU, ACCUKI, ACCUKO, ARF, ASF, EF, BFF, FLEX) vão para `exotica`, com UPI Non_Standard;
  4. os toques e as digitais com barreira recebem o UPI Digital_Option (Digital Barrier);
  5. FX e CASH ficam em `linear`, com nota de que não aparecem no DTCC;
  6. o schema ganha a regra do delta hedge;
  7. a janela de agrupamento é de 2 s, estendida até 60 s entre registros marcados como pacote.
- **TARF:** fica só registrado como lacuna da base (D8 do plano); nenhuma nota por enquanto.
- **Amostra e scripts:** a amostra do DTCC e os scripts de análise não ficam no projeto; quando necessário, baixa-se o arquivo de novo.
- **Validação independente** (três agentes; relatórios em `validacao/claude/d38-*.md`):
  - ✅ a decisão 2 (FP);
  - ◐ as decisões 3 a 7 e 9;
  - ✗ o critério da decisão 1: o produto UPI não define o payoff. O `Non_Standard` inclui vanillas em CNY, e o NDO aceita Asian.
  - As pastas resultantes ficam certas, exceto a FLEX.
- **Revisões do usuário após a validação:**
  - item 7: janela só de 2 s, sem a extensão para pacotes. Os vizinhos a 60 s são, em maioria, o mesmo negócio feito de novo, e a extensão fundiria grupos completos;
  - item 9: `docs/dtcc.md` guarda URL, CRC32, tamanho e regras de limpeza, sem dados nem scripts. Os números dependem da limpeza.
- **Pendentes:** critério da categoria, FLEX, delta hedge, duplicatas de prime brokerage, grupos com mais de 5 registros e ajustes menores.
