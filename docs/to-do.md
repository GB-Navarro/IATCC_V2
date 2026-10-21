# To-do

`[ ]` pendente · `[x]` feito. **Decisão aberta** marca o item que precisa da escolha do usuário antes de começar. As propostas ainda não aprovadas ficam em [`ideas.md`](ideas.md).

## Fase A — Fechar a base

- [ ] Validar os cinco lotes (`validacao/README.md`, 472 citações) e corrigir os itens marcados com ❌.
- [ ] Registrar os lotes como validados; fazer commit e tag `base-v1` no git.
- [ ] Escrever `scripts/validar_base.py`:
  - gerar `tags`, `instrumentos` e `ambigua_com` a partir das tabelas de pernas;
  - rodar as 6 validações do `_schema.md`;
  - exportar `base.json`, que é o que o agente e o matching leem.
- [ ] Revisar o grafo no Obsidian: os filtros de facetas e as ambiguidades esperadas (SN↔RR, SDR↔PF).
- [ ] **Decisão aberta:** formato dos casos de teste (`casos/_schema.md`).
- [ ] Gerar `casos/` fora do `Brain/`: canônicos (das fontes e do OVML), variantes, quase-iguais, ambíguos (sem o lado), com ruído e compostos.
- [ ] Opcional: fontes como notas do Brain (D26).

## Fase B — Matching determinístico

- [ ] **Decisão aberta:** D13 (matching determinístico, LLM depois).
- [ ] Definir o formato neutro de perna: tipo, strike, vencimento, notional, instrumento; delta e prêmio opcionais.
- [ ] Implementar o matching, nesta ordem:
  1. normalizar o grupo (somar pernas idênticas);
  2. calcular a assinatura;
  3. filtrar pelas facetas (`qualquer` casa com tudo);
  4. conferir as relações da tabela de pernas;
  5. ranquear por moneyness e delta;
  6. decompor grupos grandes via `composta_de`, com limite de combinações.
- [ ] Registrar o rastro do matching: cada candidata aceita ou eliminada, com o motivo.
- [ ] Medir nos casos de teste. Esse é o baseline.

## Fase C — Dados do DTCC

- [ ] Inspecionar as colunas e mapear para a perna neutra: produto/UPI → instrumento, tipo, strike, vencimento, notional (com teto), prêmio, horário de execução, plataforma, `Package indicator`, cancelamentos. Revisar o schema se os dados o contradisserem (risco da D18).
- [ ] **Decisão aberta:** D02 (refinamentos do agrupamento). Depois, agrupar por plataforma, segundo e subjacente, com janela de tolerância, tratando off-facility e removendo cancelamentos.
- [ ] Análise exploratória: tamanho dos grupos, fração de pacotes, estruturas mais frequentes.
- [ ] Revisar uma amostra das saídas do matching no banco de avaliações, antes de existir o agente.

## Fase D — Agente

- [ ] Fluxo fixo:
  1. o matching devolve as candidatas;
  2. uma chamada ao Claude com structured output, em que os códigos de estrutura são uma lista fechada (`enum`) e a saída traz estrutura, decomposição, confiança, justificativa e citações;
  3. o resultado é gravado em `decisoes`.
- [ ] Usar prompt caching na parte fixa do prompt, a Batch API para o histórico e pedir o resumo do raciocínio (`thinking.display: "summarized"`).
- [ ] **Decisão aberta:** modelo. Medir Opus 5.5, Sonnet 5.5 e Haiku 5.5 nos mesmos casos (acerto e custo).
- [ ] Só se a avaliação pedir: agente com ferramentas (`buscar_candidatas`, `ler_estrutura`, `calcular_payoff`), comparado com o fluxo fixo.
- [ ] Avaliar nos casos de teste e numa amostra do DTCC rotulada:
  - agente contra baseline;
  - com base contra sem base;
  - acerto no topo e no top-k;
  - tratamento das ambiguidades.

## Rastreamento e feedback (Fases B a D)

- [ ] Banco SQLite local, fora do git.
- [ ] Tabela `decisoes`, imutável. Registra:
  - registros de entrada, pernas normalizadas, candidatas e motivos de eliminação;
  - saída do modelo e resumo do raciocínio;
  - versões (base, matching, prompt, modelo, esforço);
  - tokens e custo.
- [ ] Tabela `avaliacoes`. Colunas:
  - identificação: `decisao_id`, revisor, data;
  - por campo da saída: `estrutura_ok` e `estrutura_correta`, `decomposicao_ok` e `decomposicao_correta`, `lados_ok`, `confianca_ok`, `justificativa_ok`;
  - `camada_do_erro`, com os valores dados, agrupamento, matching, base, modelo ou ambiguidade legítima;
  - comentário livre.
- [ ] Relatório por decisão, com links para as notas, fora do `Brain/`, para navegar da decisão até a fonte e de volta.
- [ ] Ciclo de refinamento:
  1. revisar uma amostra, parte aleatória e parte dirigida (baixa confiança, estruturas raras);
  2. agrupar os erros por camada e corrigir a maior;
  3. rodar de novo todas as decisões já revisadas;
  4. manter um conjunto de teste em que nunca se ajusta nada.
- [ ] Depois: página local de revisão.

## Fora do escopo (recomendado)

- **RAG:** o matching já faz a busca, por facetas exatas.
- **Fine-tuning:** não há dados rotulados suficientes, e o conhecimento deixaria de ser citável.
- **MCP:** só se for útil para consulta interativa durante a análise; o pipeline não precisa.
