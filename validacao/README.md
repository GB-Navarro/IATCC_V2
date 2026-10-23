# Validação

Duas validações independentes da base (D32):

| Validação | Pasta | Quem | Quando | Estado |
|---|---|---|---|---|
| Claude | [`claude/`](claude/) | agente separado, sem o contexto da conversa que escreveu as notas | agora; o MVP usa a base validada por ela (tag `base-v1-claude`) | concluída: seis lotes validados e corrigidos, decisões do usuário aplicadas (D36, D37); tag `base-v1-claude` |
| Humana | [`humana/`](humana/) | o usuário | depois do MVP (tag `base-v2-humana`) | 0 de 553 |

**Separação:** os checklists humanos não mostram os vereditos do Claude, para que a validação humana seja feita às cegas. Ao final, as duas são comparadas.

**Correções:** quando a validação do Claude encontra um erro, a nota é corrigida, o item recebe o veredito ✎ em `claude/` e as seções afetadas de `humana/` são geradas de novo.

## Lotes

| Lote | Estruturas | Itens | Inferências (⚠) | Humana | Claude |
|---|---|---|---|---|---|
| 1 | combinações de vanillas (12) | 170 | 15 | [lote-1](humana/lote-1.md) | [lote-1](claude/lote-1.md): 124 ✅ · 21 ◐ · 1 ✗ · 9 ⚖ |
| 2 | vanillas e não-opções (5) | 34 | 3 | [lote-2](humana/lote-2.md) | [lote-2](claude/lote-2.md): 20 ✅ · 7 ◐ · 0 ✗ · 2 ⚖ |
| 3 | exóticos de 1 perna (23) | 178 | 18 | [lote-3](humana/lote-3.md) | [lote-3](claude/lote-3.md): 131 ✅ · 20 ◐ · 2 ✗ · 11 ⚖ |
| 4 | compostas e forwards estruturados (16) | 131 | 27 | [lote-4](humana/lote-4.md) | [lote-4](claude/lote-4.md): 77 ✅ · 20 ◐ · 2 ✗ · 16 ⚖ |
| 5 | genéricas 2L–10L (9) | 9 | 0 | [lote-5](humana/lote-5.md) | [lote-5](claude/lote-5.md): 9 ✅ |
| 6 | fora do OVML: COL (1) | 31 | 7 | [lote-6](humana/lote-6.md) | [lote-6](claude/lote-6.md): 10 ✅ · 5 ◐ · 0 ✗ · 5 ⚖ (+ 5 itens do lote 1) |
| | **total** | **553** | **70** | | |

Os números de itens e inferências mudam quando a validação do Claude divide ou corrige linhas. Os vereditos do Claude valem para as notas antes das correções; o status de cada correção está no topo de cada relatório.

## Validação humana: como fazer

1. Abra a fonte na página do PDF indicada no item. Os arquivos estão em `fontes/`.
2. Confira se a página sustenta a afirmação:
   - **`[chave, p. N]`:** a definição da fonte diz isso;
   - **`[chave, p. N, exemplo]`:** um exemplo numérico mostra isso;
   - **`[ovml]`:** o texto da Bloomberg, embutido no topo da nota, diz isso;
   - **⚠:** a conclusão é do Claude; confira as premissas.
3. Marque `[x]` se estiver certo. Se estiver errado, deixe desmarcado e escreva logo abaixo `- ❌ motivo`.

Comece pelos **Pontos de atenção** no topo de cada lote. Para não se ancorar, não leia `claude/` antes de terminar.

## Validação do Claude: vereditos

| Veredito | Significado |
|---|---|
| ✅ | sustentada: a página diz isso |
| ◐ | parcial: sustenta só parte, ou só por contexto |
| ✗ | não sustentada: a página não diz isso, ou diz outra coisa |
| ⚖ | julgamento: inferência ou decisão, avaliada pela lógica |
| ✎ | corrigida: estava errada e a nota foi corrigida |

## Histórico

- **2026-10-21, segunda passada (Claude, na conversa que escreveu as notas):** verificou só se os trechos estão nas páginas citadas (161 das fontes e 99 do OVML, todos encontrados). Corrigiu a citação do DOT (p. 55 → p. 40). Não substitui nenhuma das duas validações.
