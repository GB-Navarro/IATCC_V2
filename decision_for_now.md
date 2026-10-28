# Decisões pendentes do IATCC

Estado em 2026-10-28. Preparado pelo Claude a partir da sessão de 2026-10-23, para outro agente decidir. Cada decisão traz o contexto, as opções, a recomendação, a evidência e do que ela depende.

## Contexto mínimo

- **Projeto:** o `Brain/` é uma base Obsidian com 66 notas de estruturas de opções de FX (`Brain/structures/<COD>.md`): 65 do OVML da Bloomberg mais o COL. Ela serve a um agente de IA que classifica grupos de negócios públicos do DTCC em estruturas (TCC).
- **Estado:**
  - a base foi validada por agentes independentes (tag `base-v1-claude`, branch `validacao-claude`);
  - a validação humana, às cegas, fica para depois do MVP;
  - o histórico está em `docs/decisoes.md` (D01–D38) e `docs/evolucao.md`; o roteiro, em `docs/to-do.md`.
- **Regras fixas** (`CLAUDE.md`):
  - nunca editar `Brain/structures/bloomberg_description/`;
  - não editar à mão `tags`, `instrumentos` e `ambigua_com`, que são gerados por script;
  - arquivos só com o essencial, em português;
  - propor um plano antes de passos grandes;
  - toda decisão vai para `docs/decisoes.md` e toda mudança relevante para `docs/evolucao.md`;
  - toda afirmação das notas tem citação (`[chave, p. N]`, `[ovml]`, `[inferência: …]`);
  - commit só quando o usuário pedir; nunca dar push.
- **O que o dado do DTCC mostra e o que não mostra:**
  - o produto vem no `UPI FISN`: `O Van`, `O NDO`, `O Bar`, `O Dig`, `O DigBar`, `FX O Nstd`, `Fwd`, `Fwd NDF`, `FX Fwd Nstd`…;
  - NÃO há lado (compra/venda), tipo ou nível de barreira, nem método de avaliação;
  - o horário tem precisão de segundos.
  - Detalhes em `docs/dtcc.md` e `validacao/claude/d38-*.md`.

---

## Parte 1 — Organização da base (experimento de 2026-10-23)

Pergunta do usuário: como organizar as pastas das estruturas, se é que devem ser organizadas, para que um agente classifique melhor os grupos do DTCC.

### Resposta curta

As estruturas não precisam de pastas. No teste, organizar as notas em pastas por categoria e número de pernas não melhorou a classificação. O que fez diferença foi a informação chegar de fato ao agente:
- **Com o Opus (modelo forte):** todas as organizações acertaram 98–100% dos grupos. O arquivo único com todas as notas custou cerca de 2,5× menos.
- **Com o Haiku (modelo pequeno e barato):** nas variantes plana, com pastas, com índice e sem guia, ele nunca leu o guia nem o índice, porque a listagem da pasta foi cortada em 100 arquivos e escondeu os dois. Só leu o guia na variante de arquivo único, onde acertou mais (82%). Isso não está provado: a diferença para as pastas (76%) e para a plana (67%) não foi significativa.

**Recomendação:**
- manter `structures/` plana e não reorganizar em pastas;
- gerar a partir das notas um material compacto (catálogo ou índice) e o guia do DTCC, e **entregá-los no prompt do agente**, sem depender de ele encontrar os arquivos;
- o guia pode morar no Brain como fonte, mas o agente o recebe pronto.

### O que foi feito

1. **Pesquisa (agente independente):**
   - a literatura não favorece pastas hierárquicas nem busca semântica para uma base de 66 notas;
   - fontes de fornecedores (Anthropic, Vercel) dizem que um índice compacto sempre presente rende mais do que depender de o agente decidir buscar. O exemplo mais forte: 100% contra 53% numa avaliação da Vercel.
2. **Benchmark (outro agente, sem saber o que seria testado):**
   - 45 grupos com 123 registros: 31 sintéticos, gerados das tabelas de pernas com as imperfeições reais (hedge, duplicata de prime brokerage, `Nstd` em yuan, perna faltando), e 14 reais da amostra de 21/10/2026;
   - o gabarito lista o conjunto de estruturas que o dado não permite distinguir;
   - granularidade: só 24 dos 45 grupos têm uma única resposta aceitável. No catálogo inteiro, só 14 das 56 notas que geram registro ficam únicas com o que o dado mostra.
3. **Onze classificadores:** cinco organizações da base, cada uma com o Opus e com o Haiku, mais um classificador por script, em Python. As cinco organizações:
   - **A:** plana + guia;
   - **B:** pastas por categoria e número de pernas + guia;
   - **C:** plana + índice gerado + guia;
   - **D:** arquivo único (todas as notas concatenadas) + guia;
   - **E:** plana + índice, sem guia.
4. **Validador independente:** refez os números, revisou o gabarito, testou o script em 12 grupos novos e julgou as conclusões.

### Resultados

| Organização | Acerto, Opus | Acerto, Haiku | Custo relativo, Opus (lote) |
|---|---|---|---|
| A: plana + guia | 100% | 67% | ~2,7× |
| B: pastas por categoria/pernas + guia | 98% | 76% | ~2,8× |
| C: plana + índice + guia | 98% | 47% | ~2,5× |
| **D: arquivo único + guia** | 98% | **82%** | **1×** |
| E: plana + índice, sem guia | 98% | 60% | ~2,5× |
| Script determinístico | 98% (12/12 em grupos novos) | — | quase zero ao rodar |

Como os agentes navegaram:
- **Opus:** nas variantes A, B, C e E, abriu de 43 a 59 das 66 notas de qualquer jeito. As pastas não reduziram a leitura.
- **Haiku:** nas variantes B e C, quase não abriu notas: foi por buscas de texto, sem ler o guia nem o índice.

Os intervalos de 95% (Wilson) do acerto no Haiku se sobrepõem bastante:
- D: 69–91%;
- B: 61–86%;
- A: 52–79%;
- E: 45–73%;
- C: 33–61%.

### O que a validação ajustou

| Conclusão | Veredito | Ajuste |
|---|---|---|
| A organização não muda a acurácia do Opus | ◐ | Ficou no teto: o teste não tem poder para medir esse efeito. "Não se detectou diferença" é o enunciado honesto. |
| O arquivo único é mais barato | ◐ | Pelo preço com cache, é 2,5–2,8× mais barato, não 3,5×. Vale para 45 grupos numa sessão; um grupo por vez, sem cache, pode se inverter. |
| No Haiku, o problema é a descoberta | ◐ | O mecanismo se confirma: a listagem ordena por data, e o guia, gravado por último, ficou fora do corte. Mas foi uma rodada só: duas variantes com a mesma informação diferiram 29 pontos. |
| As pastas não trazem ganho | ✅ | Ressalva: o Haiku não chegou a navegar pelas pastas. |
| O script empata com o Opus | ◐ | Script, guia e gabarito usam as mesmas regras. O empate mede coerência com essas regras, não acerto contra a realidade. |
| Recomendação de entregar no prompt | ◐ | É hipótese: nenhuma variante testou o material entregue no prompt. |

**O problema mais grave é a circularidade.** O mesmo modelo fez o gabarito, o script e os classificadores fortes, então os 98% medem consistência, não verdade.

### Respostas às perguntas do usuário

- **As pastas devem ser organizadas?** Não para o agente. Para o humano no Obsidian, as tags geradas pelo script (`familia/`, `pernas/`) já dão a mesma navegação sem mover arquivos.
- **Faz sentido ter algo do DTCC no Brain?** Sim. O guia foi o arquivo que os agentes mais citaram como útil, mas só funciona se for entregue ao agente, não se ele precisar descobri-lo.
- **Como um agente classificaria melhor?**
  - com o guia e um catálogo compacto no prompt;
  - o script pode ajudar como pré-filtro: devolve as candidatas, e o agente decide os empates. A estrutura certa estava entre as candidatas dele em 44 de 45 grupos e em 12 de 12 grupos novos.

### O que falta para decidir com segurança

O validador listou o mínimo:
1. **Corrigir o instrumento de medida.**
   - A tolerância de notional difere entre o guia (10%) e o gabarito (20%).
   - A avaliação compara os registros excluídos pelo ID e deveria comparar pelo conteúdo. Com essa correção, o Opus e o script vão a 100%.
   - Três grupos do gabarito precisam de revisão (G24, G31 e G35). No G24, o PF deveria ser aceito. O G31 é uma variante de FE fora do catálogo, com razão 1:3, e a convenção do prompt para esse caso é ambígua. G13 e G35 são inconsistentes entre si.
2. **Teste de produção.**
   - Guia + índice contra guia + catálogo, entregues no prompt;
   - um grupo por sessão, 3 rodadas, no modelo que será usado;
   - custo por grupo, com o preço de cache.
3. **Uns 30 grupos reais sorteados, rotulados às cegas pelo usuário.** É o único jeito de quebrar a circularidade.

### Decisões

- **O1. Abandonar o plano de pastas da D38 e manter `structures/` plana?**
  - Recomendação: **sim**.
  - Consequências:
    - não se cria o `organizar_pastas.py`;
    - `gerar_notas.py` e `checklist_citacoes.py` não mudam;
    - o checklist humano do lote 7 (pastas) deixa de existir.
- **O2. Rodar o teste de produção do item 2 acima?**
  - Depende das regras do guia (Parte 2) e da correção do instrumento (item 1).
  - Recomendação: sim, depois da Parte 2.
- **O3. O usuário rotula ~30 grupos reais às cegas, num checklist como os de `validacao/humana/`?**
  - Recomendação: sim. Depende da disponibilidade do usuário.
- **O4. Guardar no projeto um resumo do experimento e dos três relatórios** (pesquisa, benchmark e validação), por exemplo em `validacao/claude/organizacao.md`?
  - Hoje eles só existem no scratchpad, que é temporário.
  - Recomendação: sim, só o resumo, sem dados nem scripts, como na D38, item 9.

### Onde está a evidência (scratchpad temporário da sessão)

Raiz: `C:\Users\gsilv\AppData\Local\Temp\claude\c--Users-gsilv-Brain-V2-IATCC\6947135f-b0c8-4da0-9fd5-961e07c2cc80\scratchpad\exp\`

| Arquivo | Conteúdo |
|---|---|
| `pesquisa\relatorio.md` | pesquisa bibliográfica, com fontes e URLs |
| `bench\grupos.json`, `gabarito\gabarito.json`, `gabarito\notas.md` | benchmark e gabarito |
| `variantes\A…E\` | as cinco organizações testadas |
| `insumos\_dtcc.md` | o guia usado no teste |
| `insumos\montar_variantes.py` | monta as variantes e gera o índice |
| `resultados\*.json`, `resultados_avaliacao.md`, `custos.md` | saídas dos classificadores e avaliação |
| `script\classificar.py` | classificador determinístico |
| `validacao\relatorio.md`, `validacao\novos\` | validação independente e os 12 grupos novos |

---

## Parte 2 — Pendências da D38: regras do guia e do índice

A D38 previa pastas. Se O1 for aceita, os itens P1 e P2 passam a valer só para a tag `familia/` e para a coluna "produtos possíveis" do índice; P3 a P5 vão para o guia.

**Já decidido pelo usuário:**
- janela de agrupamento só de 2 s, sem a extensão de 60 s para pacotes;
- `docs/dtcc.md` guarda URL, CRC32, tamanho e regras de limpeza, sem dados nem scripts. **Ainda não executado.**

**Validação independente da D38:** `validacao/claude/d38-taxonomia.md`, `d38-literatura.md` e `d38-dados.md`.

### P1. Critério da categoria: produto UPI ou payoff

- **Problema.** A regra aprovada ("categoria pelo produto UPI de cada perna") mistura o que a estrutura é (o payoff) com como ela aparece no DTCC (o produto UPI). A mesma estrutura pode vir com UPIs diferentes:
  - **`Non_Standard` contém vanillas.** O exemplo que a própria DSB dá para esse produto (`dsb-2024`, aba 101) é uma put europeia com método "Vanilla", em CNY, liquidada em Hong Kong. Na amostra, 129 dos 179 registros `FX O Nstd` são em CNY, vários deles straddles e strangles.
  - **NDO aceita payoff asiático:** "Valuation Method: [Vanilla; Asian; Lookback; etc.]" (aba 100). E o FISN não mostra o método.
  - **Literatura:** o Hull trata as combinações de vanillas ("packages") no capítulo de exóticas [hull-2015, pp. 598, 618].
- **Opções:**
  - (a) manter o UPI;
  - (b) categoria pelo payoff das pernas, com o campo `upi` como lista dos produtos plausíveis.
- **Recomendação: (b).**
  - Só as notas de 1 perna recebem `upi`. Exemplos: EU = `[Vanilla_Option, NDO, Non_Standard]`; KO = `[Barrier_Option, Non_Standard]`; AVG = `[Non_Standard, NDO]`.
  - A categoria de 1 perna sai de campos existentes: `payoff: vanilla` sem barreira → `vanilla`; `payoff: linear` → `linear`; o resto → `exotica`.
  - As notas de várias pernas herdam pela coluna instrumento: alguma perna exótica → `exotica`; senão, alguma vanilla → `vanilla`; senão → `linear`.
  - Tudo é gerado por script.
  - Também é preciso: corrigir a regra da faceta `familia/` do `_schema.md`, que hoje usa o código do instrumento (põe o FP como exótico e TF/COL como compostas), e dar `payoff` a EF e CASH, com citação.

### P2. FLEX: `linear` ou `exotica`

- **O produto:** "A time option or American style forward contract entitles and requires the holder to buy/sell a pre-determined amount of a currency at a pre-determined strike K within a given time period" [wystup-2006, p. 166]; "just like an American style call, except that the entire amount must be exercised" [wystup-2006, p. 167]. A troca é obrigatória; só a data é escolhida.
- **Problema:** a nota tem `payoff: linear`, mas o plano a punha em `exotica`.
- **Recomendação: `linear`.** O payoff é linear, e no DTCC ela provavelmente aparece como forward, ao lado da FWD. Sai automaticamente de P1(b).

### P3. Regra do delta hedge

- **Regra aprovada:** um forward abaixo de 90% do notional das opções é hedge; acima disso, é perna.
- **Problema.** Na amostra, os 53 forwards acima de 90% não eram pernas:
  - 41 eram negócios de outros clientes no mesmo segundo. Exemplo: NDF de TWD de 1 M USD, vencendo em 1 mês, ao lado de uma put de TWD de 1 M USD, vencendo em 1 ano, sem pacote;
  - 12 eram hedge de digital. Exemplo: digital de BRL que paga 10 M USD, com NDF de 45 M USD;
  - nenhum TF ou COL apareceu no dia.

  A literatura também mostra hedges ≥ 90%: 95,5% [wystup-2006, p. 149]; o delta premium-adjusted passa de 100% [reiswich-wystup-2009, p. 7]. E "notional das opções" não estava definido: soma ou uma perna?
- **Recomendação:** inverter o padrão. O forward é hedge ou ruído até prova em contrário.
  1. Forward sem pacote, que não é spot e cujo vencimento difere do de todas as opções (±5 dias): sai do grupo.
  2. Perna só se o grupo casa TF ou COL com razão entre 90% e 110% e o mesmo vencimento.
  3. O resto é hedge, inclusive NDF e forward de digital, de qualquer tamanho.
  4. Se as duas leituras casarem, as duas vão para o ranking.
  5. A razão é calculada contra a maior opção de mesmo vencimento, na mesma moeda.

  Na amostra: 326 hedges, 140 forwards fora do grupo e 18 casos para revisão.

### P4. Duplicatas de prime brokerage

- **Problema:** o mesmo negócio é reportado duas vezes (dealer com PB e PB com cliente). Na amostra, há 119 conjuntos (245 registros) de opções idênticas em plataforma, segundo, produto, notional, strike e vencimento; 158 desses registros estão marcados como PB. O schema manda somar pernas idênticas, o que dobraria o notional.
- **Recomendação:** tirar as duplicatas marcadas como PB antes de somar.

### P5. Grupos com mais de 5 registros

- **Problema:** há 42 grupos assim, e 28 deles cabem inteiros em 1 s, de modo que nenhuma janela os separa. Exemplo: BILT SAR/USD, com 111 registros e 37 vencimentos × (barreira, vanilla, digital). É uma carteira, não uma estrutura do catálogo.
- **Recomendação:** mandar para revisão em vez de passar pelo matching.

### P6. Ajustes menores

1. **`upi` dos forwards estruturados** (ACCU, ACCUKI, ACCUKO, ARF, ASF, EF, BFF): `Forward Non_Standard | Option Non_Standard`.
   - Só o template de opção tem atributo de barreira e de média. Um accumulator com knock-out pode ir para qualquer um dos dois.
   - A pasta ou categoria continua `exotica`, pelo payoff: "The accumulative forward consists of fade-in calls and fade-in puts, possibly with extra knock-out ranges" [wystup-2006, p. 157].
2. **`upi` dos toques** (OT, NT, DOT, DNT): `Digital_Option`, com os dois métodos, Digital e Digital Barrier.
   - O FISN distingue `O Dig` de `O DigBar`. O Wystup descreve o one-touch das duas formas [wystup-2006, pp. 49–50].
   - DISEQ: `Digital_Option | Non_Standard`.
3. **Frase para FX e CASH:** "Sem produto UPI próprio. Se reportado, o FX aparece como forward de prazo até 2 dias; o CASH, só como campo 'Other payment' de outro registro."
   - Na amostra, há 1.236 forwards de prazo até 2 dias e 230 negócios com "Other payment".
4. **Atualizar `docs/dtcc.md`:**
   - escrever as regras de limpeza, o manifesto (URL, CRC32, tamanho) e os números refeitos com elas;
   - tirar a afirmação dos 60 s.

   As regras de limpeza do validador: só NEWT/TRAD; saem os negócios cancelados por EROR; aplica-se a última CORR; filtra-se pela data de execução. O meu "2.065 grupos com opção a 2 s" vira 1.988 com elas.
5. **Renomear a fonte `dsb-2024` para `dsb-2026`:** a planilha é a versão 9, de 2026-08-07.
   - Hoje só `fontes/README.md` e `docs/dtcc.md` usam a chave.
   - Os relatórios de validação ficam como estão, por serem histórico.
6. **Novo, do benchmark: o rótulo Call/Put do FISN nem sempre é confiável.** O tipo deve vir de `Call currency`/`Put currency`.
   - Na amostra, o rótulo discorda das colunas de moeda em ~12% dos registros da BILT (284 de 2.296), em 53 de 168 dos XXXX e em 11 de 15 dos XOFF.
   - O guia do teste já foi corrigido; o schema e o `docs/dtcc.md`, não.

---

## Parte 3 — Outras decisões abertas no projeto

| # | Decisão | Onde | Situação e recomendação |
|---|---|---|---|
| Q1 | Modelo de produção (Opus, Sonnet ou Haiku) | `docs/to-do.md`, Fase C | O experimento dá um primeiro dado: o Opus fica no teto; o Haiku cai muito quando precisa navegar. O Sonnet não foi testado. Recomendação: decidir com o teste O2, incluindo o Sonnet. |
| Q2 | Formato dos casos de teste (`casos/_schema.md`) | `docs/to-do.md`, Fase A1 | O benchmark do experimento (`grupos.json` + `gabarito.json`, com o conjunto de respostas aceitas e os registros que não são pernas) é um candidato pronto. Recomendação: adotá-lo como ponto de partida e corrigir G24, G31 e G35. |
| Q3 | Ampliar o schema para a versão Agente + algoritmos (campo `tipico`; Restrições que mudam o casamento em campos estruturados) | `docs/to-do.md`, Fase A1 | O classificador determinístico do experimento já funciona só com as tabelas de pernas. Recomendação: esperar o resultado de O2 antes de ampliar. |
| Q4 | Arquitetura do agente (D28, proposta): fluxo fixo antes de agente; matching entrega candidatas; uma chamada com structured output decide; SQLite com rastro | `docs/decisoes.md` | O experimento apoia "entregar no prompt" e o script como pré-filtro, que é o que a D28 propõe. Recomendação: aceitar a D28 depois de O2. |
| Q5 | Fechar a D02 (proposta) e os "em aberto" da D29, D30 e do `to-do.md` (tamanho do intervalo Δt e trades off-facility) | `docs/decisoes.md`, `docs/to-do.md` | Já respondidos: Δt = 2 s (D38, item 7); fora de plataforma, os negócios vêm como `XXXX` ou `XOFF`, que ficam como chaves separadas, e plataforma vazia só aparece em EROR e TERM (`validacao/claude/d38-dados.md`); cancelamentos e correções saem pelas regras de limpeza (P6.4). Recomendação: registrar como decisão nova e marcar D02 como substituída. |
| Q6 | Fontes como notas do Brain (D26, proposta adiada) | `docs/decisoes.md` | Opcional; muda só a navegação e o grafo. Recomendação: continuar adiada. |
| Q7 | Gerar os campos do script (`tags`, `instrumentos`, `ambigua_com`), hoje vazios nas 66 notas | `scripts/gerar_notas.py`, `_schema.md` (Facetas, Relações) | Os classificadores sentiram falta de `ambigua_com` (RR↔SN, SDR↔PF). O índice e a tag `familia/` dependem de P1. Recomendação: implementar junto com o índice, depois de P1 e P2. |
| Q8 | Git | branch `validacao-claude` | Há mudanças sem commit em `docs/decisoes.md`, `docs/evolucao.md`, `fontes/README.md` e `validacao/README.md`, e três relatórios novos (`validacao/claude/d38-*.md`). A branch não foi enviada ao GitHub. Commit só se o usuário pedir; nunca push. |

---

## Ordem sugerida

1. **O1:** se aceita, o resto da Parte 2 vale para as tags e o índice, não para pastas.
2. **P1 a P6**, as regras do guia e do índice, e **Q5**.
3. **Implementar:**
   - campos `upi` e `payoff` faltantes;
   - geração de `tags`, `instrumentos`, `ambigua_com` e do índice (Q7);
   - guia `Brain/_dtcc.md`;
   - `docs/dtcc.md` (P6.4).

   Antes, propor o plano ao usuário.
4. **Corrigir o instrumento de medida e rodar O2**, decidindo Q1, Q3 e Q4 com o resultado.
5. **O3:** rotulagem humana de grupos reais.
6. **O4 e Q8**, quando o usuário quiser.

Toda decisão tomada deve ser registrada em `docs/decisoes.md` (próximo número: D39), com motivo, e em `docs/evolucao.md`.
