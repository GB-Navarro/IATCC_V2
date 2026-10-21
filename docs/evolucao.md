# Evolução

Mudanças no sistema, da mais recente para a mais antiga. As decisões estão em [`decisoes.md`](decisoes.md).

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
