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

### D13 · 2026-10-20 · proposta — Matching determinístico, LLM depois
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
