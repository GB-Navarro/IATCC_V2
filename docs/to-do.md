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
- [ ] **Decisão aberta:** ampliar o schema para a versão Agente + algoritmos, antes do `validar_base.py`, porque muda o `base.json`:
  - atributos típicos em campo estruturado (ex.: `tipico: [custo_zero, delta_25]`), cada um medido por uma função genérica;
  - as Restrições que mudam o casamento (ex.: pareamento livre no DS) em campos, e não só em prosa.

## Fase A2 — Piloto da versão Agente (LLM sozinha)

Comparação definida na D31; argumentos em [`ideas.md`](ideas.md) (ideia 1, "Algoritmos + LLM × LLM sozinha").

- [ ] Montar a versão **Agente**. O LLM recebe o grupo de pernas, os insumos calculados e a base (`base.json`, em prompt caching) e classifica sozinho, sem algoritmos. A saída usa structured output (códigos em `enum`) e traz estrutura, decomposição, confiança, justificativa e citações.
- [ ] Rodar nos casos de teste e medir:
  - acerto no topo e no top-k;
  - consistência (a mesma resposta em 5 execuções);
  - custo por grupo;
  - acerto por tamanho do grupo e por dados limpos × imperfeitos.
- [ ] Com o resultado, decidir o escopo da Fase B. Se o Agente já acertar quase tudo, inclusive grupos grandes e dados imperfeitos, os algoritmos podem ficar mais simples.

## Fase B — Algoritmos da versão Agente + algoritmos

As estações estão explicadas em [`ideas.md`](ideas.md) (ideia 1, "Explicação intuitiva: a linha de montagem"). Todas são genéricas: o que muda de uma estrutura para outra fica nas receitas da base.

- [ ] Definir o formato neutro de perna: tipo, strike, vencimento, notional, instrumento; delta e prêmio opcionais.
- [ ] Estação 2, casamento: satisfação de restrições com retrocesso e unificação, lendo as tabelas de pernas.
- [ ] Estação 3, variantes: gerar o espelho e o short de todos os modelos.
- [ ] Estação 4, divisão: cobertura exata (Algorithm X ou programação linear inteira), com a vanilla avulsa como peça sempre disponível.
- [ ] Estação 5, pontuação: navalha de Occam, traços típicos e frequência; percentuais por divisão.
- [ ] Estação 6, tolerância: restrições flexíveis (tick de strike, arredondamento e teto de notional), com custo registrado.
- [ ] Estação 7, roteamento: decide sozinho quando há uma divisão claramente na frente; manda ao agente os empates e os casos em que nada casa.
- [ ] Registrar o rastro: cada peça aceita ou eliminada, com o motivo, e cada tolerância usada.
- [ ] Medir os **algoritmos sozinhos** nos casos de teste. É o primeiro dos três braços do experimento.

## Fase C — Dados do DTCC

- [ ] Inspecionar as colunas e mapear para a perna neutra: produto/UPI → instrumento, tipo, strike, vencimento, notional (com teto), prêmio, horário de execução, plataforma, `Package indicator`, cancelamentos. Revisar o schema se os dados o contradisserem (risco da D18).
- [ ] Agrupar pela chave (intervalo de segundos, plataforma de execução, par de moedas) (D30), removendo cancelamentos. **Decisão aberta:** o tamanho do intervalo (Δt) e o tratamento dos trades off-facility, que vêm sem plataforma.
- [ ] Análise exploratória: tamanho dos grupos, fração de pacotes, estruturas mais frequentes.
- [ ] Revisar uma amostra das saídas do matching no banco de avaliações, antes de existir o agente.

## Fase D — As duas versões e a comparação

- [ ] Versão **Agente + algoritmos**. Fluxo fixo:
  1. as estações 1 a 6 devolvem as k melhores divisões;
  2. só os casos roteados pela estação 7 vão ao Claude, com structured output (códigos em `enum`); a saída traz estrutura, decomposição, confiança, justificativa e citações;
  3. o resultado é gravado em `decisoes`.
- [ ] Versão **Agente**: a do piloto (Fase A2), ajustada com o que o piloto mostrou.
- [ ] Nas duas versões: prompt caching na parte fixa do prompt, Batch API para o histórico e resumo do raciocínio (`thinking.display: "summarized"`).
- [ ] **Decisão aberta:** modelo. Medir Opus 5.5, Sonnet 5.5 e Haiku 5.5 nos mesmos casos (acerto e custo).
- [ ] Só se a avaliação pedir: agente com ferramentas (`buscar_candidatas`, `ler_estrutura`, `calcular_payoff`), comparado com o fluxo fixo.
- [ ] Experimento com **três braços** nos casos de teste e numa amostra do DTCC rotulada:
  - braços: algoritmos sozinhos; **Agente + algoritmos**; **Agente**;
  - métricas: acerto no topo e no top-k, consistência em 5 execuções, custo por grupo, acerto por tamanho do grupo e por dados limpos × imperfeitos, tratamento das ambiguidades;
  - ablação: com base × sem base.
  - Expectativa a confirmar: a diferença aparece nos grupos grandes e nos dados imperfeitos, e quase some nos grupos simples. Qualquer resultado é válido para o TCC.

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
