# Evolução

Mudanças no sistema, da mais recente para a mais antiga. As decisões estão em [`decisoes.md`](decisoes.md).

## 2026-10-21

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
