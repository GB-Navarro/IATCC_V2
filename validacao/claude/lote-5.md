# Validação do Claude — lote 5

Validador: agente independente · 2026-10-22 · cada citação `[ovml]` conferida no arquivo da Bloomberg; frontmatter e estrutura conferidos contra `Brain/_schema.md`.

## Resumo

| ✅ | ◐ | ✗ | ⚖ | ? | total |
|---|---|---|---|---|---|
| 9 | 0 | 0 | 0 | 0 | 9 |

## Correções propostas

Prioridades 1 e 2: nenhuma.

Prioridade 3

1. **2L–10L** · A tabela de origem fica sob o título `## Pernas`, herdado do template, mas o schema diz que as genéricas não têm tabela de pernas. · Decisão do usuário: manter assim (é só formatação) ou renomear o título nas genéricas.

## 2L

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: estratégia genérica de 2 pernas de opção, sem estrutura definida | `[ovml]` | ✅ | "Generic two leg option strategy." "Sem estrutura definida" parafraseia "generic". |

**Verificações da nota:**
- Tabela de pernas: ✅ não tem, como o schema manda para as genéricas; o número de pernas vem do código.
- Frontmatter: ✅ `familia: generica`; `aliases` traz o nome Bloomberg; não tem `barreira` nem `payoff`, porque não é nota de 1 perna. `flexivel` vazio não pesa, porque as facetas de strike, expiry e notional não valem para as genéricas.
- Omissões/contradições: ✅ nenhuma. O OVML é a única fonte, e `fontes/README.md` diz que 2L–10L não precisam de fonte.

## 3L

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: estratégia genérica de 3 pernas de opção, sem estrutura definida | `[ovml]` | ✅ | "Generic three leg option strategy." "Sem estrutura definida" parafraseia "generic". |

**Verificações da nota:**
- Tabela de pernas: ✅ igual a 2L.
- Frontmatter: ✅ igual a 2L.
- Omissões/contradições: ✅ igual a 2L.

## 4L

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: estratégia genérica de 4 pernas de opção, sem estrutura definida | `[ovml]` | ✅ | "Generic four leg option strategy." "Sem estrutura definida" parafraseia "generic". |

**Verificações da nota:**
- Tabela de pernas: ✅ igual a 2L.
- Frontmatter: ✅ igual a 2L.
- Omissões/contradições: ✅ igual a 2L.

## 5L

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: estratégia genérica de 5 pernas de opção, sem estrutura definida | `[ovml]` | ✅ | "Generic five leg option strategy." "Sem estrutura definida" parafraseia "generic". |

**Verificações da nota:**
- Tabela de pernas: ✅ igual a 2L.
- Frontmatter: ✅ igual a 2L.
- Omissões/contradições: ✅ igual a 2L.

## 6L

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: estratégia genérica de 6 pernas de opção, sem estrutura definida | `[ovml]` | ✅ | "Generic six leg option strategy." "Sem estrutura definida" parafraseia "generic". |

**Verificações da nota:**
- Tabela de pernas: ✅ igual a 2L.
- Frontmatter: ✅ igual a 2L.
- Omissões/contradições: ✅ igual a 2L.

## 7L

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: estratégia genérica de 7 pernas de opção, sem estrutura definida | `[ovml]` | ✅ | "Generic seven leg option strategy." "Sem estrutura definida" parafraseia "generic". |

**Verificações da nota:**
- Tabela de pernas: ✅ igual a 2L.
- Frontmatter: ✅ igual a 2L.
- Omissões/contradições: ✅ igual a 2L.

## 8L

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: estratégia genérica de 8 pernas de opção, sem estrutura definida | `[ovml]` | ✅ | "Generic eight leg option strategy." "Sem estrutura definida" parafraseia "generic". |

**Verificações da nota:**
- Tabela de pernas: ✅ igual a 2L.
- Frontmatter: ✅ igual a 2L.
- Omissões/contradições: ✅ igual a 2L.

## 9L

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: estratégia genérica de 9 pernas de opção, sem estrutura definida | `[ovml]` | ✅ | "Generic nine leg option strategy." "Sem estrutura definida" parafraseia "generic". |

**Verificações da nota:**
- Tabela de pernas: ✅ igual a 2L.
- Frontmatter: ✅ igual a 2L.
- Omissões/contradições: ✅ igual a 2L.

## 10L

| Afirmação | Citação | Veredito | Evidência / comentário |
|---|---|---|---|
| Composição: estratégia genérica de 10 pernas de opção, sem estrutura definida | `[ovml]` | ✅ | "Generic ten leg option strategy." "Sem estrutura definida" parafraseia "generic". |

**Verificações da nota:**
- Tabela de pernas: ✅ igual a 2L.
- Frontmatter: ✅ igual a 2L.
- Omissões/contradições: ✅ igual a 2L.
