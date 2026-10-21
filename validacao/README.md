# Validação

Um checklist por lote. Cada afirmação das notas aparece uma vez, com as fontes como sub-itens marcáveis.

| Lote | Estruturas | Itens | Inferências (⚠) |
|---|---|---|---|
| [1](lote-1.md) | combinações de vanillas (12) | 155 | 9 |
| [2](lote-2.md) | vanillas e não-opções (5) | 29 | 1 |
| [3](lote-3.md) | exóticos de 1 perna (23) | 164 | 10 |
| [4](lote-4.md) | compostas e forwards estruturados (16) | 115 | 12 |
| [5](lote-5.md) | genéricas 2L–10L (9) | 9 | 0 |
| | **total** | **472** | **32** |

## Segunda passada (Claude, 2026-10-21)

Feita antes da sua validação, sem marcar nenhum `[x]`.

- **Fontes:** 161 trechos procurados nas 73 páginas com texto. Todos estão nas páginas citadas; 2 só apareceram depois de desfazer a hifenização da quebra de linha. As 3 páginas do Natenberg (escaneado) foram conferidas pela imagem.
- **OVML:** 99 trechos procurados nos textos da Bloomberg das 65 estruturas; todos encontrados.
- **Correção:** no DOT, a citação `wystup-2006, p. 55` passou a `p. 40`, onde está a definição. A nota e o checklist foram corrigidos.
- **10 avisos 🔎** logo abaixo dos sub-itens que merecem atenção:
  - 7 em que a fonte sustenta só parte da afirmação da linha; a outra parte vem de outra fonte da mesma linha (CP, RR, SN, PF, CS, SG, BFC);
  - 2 de apoio indireto (DS e FE);
  - 1 de correção (DOT).

A passada não substitui a sua conferência: sou eu revisando o meu próprio trabalho. Ela verifica se o trecho está na página, não se a interpretação está certa.

## Como validar

1. Abra a fonte na página do PDF indicada no item. Os arquivos estão em `fontes/`.
2. Confira se a página sustenta a afirmação:
   - **`[chave, p. N]`:** a definição da fonte diz isso;
   - **`[chave, p. N, exemplo]`:** um exemplo numérico mostra isso;
   - **`[ovml]`:** o texto da Bloomberg, embutido no topo da nota, diz isso;
   - **⚠:** a conclusão é minha; confira as premissas.
3. Marque `[x]` se estiver certo. Se estiver errado, deixe desmarcado e escreva logo abaixo `- ❌ motivo`.

Comece pelos **Pontos de atenção** no topo de cada lote.
