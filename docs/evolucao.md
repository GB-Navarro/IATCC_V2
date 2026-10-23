# Evolução

Mudanças no sistema, da mais recente para a mais antiga. As decisões estão em [`decisoes.md`](decisoes.md).

## 2026-10-23

- Aplicada a 2ª rodada de decisões (CASH, FP, DACCR, DISEQ, KKF e duas regras no `_schema.md`). Validação do Claude concluída; commit e tag `base-v1-claude` (D37).
- Aplicadas 9 decisões do usuário (COL, AM, CMP, KOKI, FE e regra de barreira no schema). Corrigidas duplicações em 5 notas causadas por uma nova execução do script. Checklists humanos gerados de novo (D36).

## 2026-10-22

- Validação do Claude concluída nos seis lotes. Aplicadas as correções verificadas dos lotes 2 a 6 em 39 notas; o BFW passou a ter 3 pernas, pelo collar extra do Wystup. Checklists humanos: 553 itens. 15 decisões do usuário pendentes (D35).
- Criada a nota `COL` (Collar, fora do OVML), após varredura das fontes; ela tem o seu checklist próprio (lote 6), e o RR passou a apontar para ela. PF e SN ajustados. `checklist_citacoes.py` passou a aceitar faixas de deslocamento, por causa do Natenberg. Validação do Claude: lotes 2 e 5 concluídos, sem ✗ (D34).
- Validação do Claude do lote 1 concluída por um agente independente: 124 ✅, 21 ◐, 1 ✗ e 9 ⚖ em 155 citações. Aplicadas 21 de 25 correções em 12 notas, mais o padrão "Fonte única" em 8 notas e a convenção EU no `_schema.md` (D33). Os checklists humanos 1 a 4 foram gerados de novo (482 itens, 45 inferências).
- Validação dividida em `validacao/humana/` e `validacao/claude/` (D32). Os checklists humanos foram movidos, sem os avisos 🔎, e `checklist_citacoes.py` passou a gravar em `humana/`. A validação do lote 1 por um agente separado está em andamento.

## 2026-10-21

- Segunda passada nas citações (Claude), antes da validação do usuário: 161 trechos das fontes e 99 do OVML conferidos, todos encontrados. Corrigida a citação do DOT (p. 55 → p. 40); 10 avisos 🔎 nos checklists. Resumo em `validacao/README.md`.
- `ideas.md` ganhou a explicação intuitiva das sete estações e a comparação algoritmos + LLM × LLM sozinha. `to-do.md` ganhou a Fase A2 (piloto da versão Agente), a Fase B como versão Agente + algoritmos e a Fase D com as duas versões e o experimento de três braços (D31).
- Definida a chave de agrupamento: (intervalo de segundos, plataforma de execução, par de moedas) (D29, revisada pela D30). `to-do.md` e `ideas.md` foram ajustados.
- Criado `docs/ideas.md`, com propostas ainda não aprovadas: algoritmos para o matching (CSP, cobertura exata, pontuação, restrições flexíveis), agrupamento por janela de tempo, usos do feedback humano e RLHF como trabalho futuro.
- Criado `docs/to-do.md`, com o roteiro por fase (A–D), o rastreamento e o feedback das decisões. O README passa a apontar para ele (D28).
- Lotes 2 a 5 preenchidos (53 notas). Gerados `validacao/lote-2.md` a `lote-5.md` e o índice `validacao/README.md`: 472 citações no total, aguardando validação (D27).
- Tabela de origem implantada (D25): schema e template atualizados; as 12 notas do lote 1 foram reescritas e as outras 53, migradas. O `validacao/lote-1.md` foi refeito com 155 citações e pontos de atenção. Registrada a proposta D26 (fontes como notas).
- Lote 1 preenchido com citações: CP, RR, SD, SN, SDR, PF, CS, DS, SG, BF, BFC e CR. Gerado o checklist `validacao/lote-1.md`, com 80 itens, aguardando validação (D24).
- `_schema.md` e `_template.md` ganharam as regras de citação e a seção Relações; a seção Fontes saiu. As 65 notas foram migradas. Criado `scripts/checklist_citacoes.py` (D24).
- Obtido o `natenberg-1994` (escaneado), renomeado e indexado. O CR deixou de depender só do OVML (D23).
- Obtidos `wystup-2006` (1ª ed.) e `reiswich-wystup-2009`, já renomeados. O índice foi refeito com páginas impressas para todas as estruturas e quatro divergências resolvidas (D22).
- Obtidos `hull-2015` (9ª ed.) e `haug-2007`. Fontes renomeadas para `<chave>_<título-curto>`. O índice ganhou paginação, seções relevantes e duas divergências confirmadas pelo Hull: DS e RF (D21).

## 2026-10-20

- Baixados `wystup-fxcol-2025` (PDF) e `wystup-fxcol-2026` (.docx). O `reiswich-wystup-2009` fica pendente porque o econstor bloqueia download automático. Haug e Clark não foram obtidos (D20).
- Criada `fontes/`, com índice de 8 fontes, cobertura por estrutura e divergências a conferir. O PDF do `wystup-fxcol-2022` já está na pasta (D19).
- Criados `CLAUDE.md`, `scripts/hooks/checar_docs.py` e `.claude/settings.json`, com hooks `Stop` e `SessionStart` para a atualização contínua dos docs (D17).
- Criado `docs/`, com README, decisões e evolução.
- Criado `scripts/gerar_notas.py`. Ele gerou 65 notas canônicas em `Brain/structures/` e registrou os hashes dos textos originais (D07, D15, D16).
- Criados `Brain/_schema.md` e `Brain/_template.md` (D07–D12).
- Removido `Variance Forward (FE).md`, duplicata do Forward Extra (D04).
- Auditadas as descrições da Bloomberg. O `Accumulator (ACCU).md`, que tinha o texto do Accrual, foi corrigido pelo usuário. As demais pendências estão no [README](README.md#pendências-conhecidas-no-texto-da-bloomberg).
- Coletadas 66 descrições de estruturas do OVML em `Brain/structures/bloomberg_description/`.
