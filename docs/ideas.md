# Ideias

Propostas ainda não aprovadas. Quando uma ideia for aceita, ela vira item do [`to-do.md`](to-do.md) e decisão em [`decisoes.md`](decisoes.md).

## 1. Algoritmos de busca para o matching (Fases B e C)

O problema tem nome: é um problema de **cobertura exata com casamento de padrões sob restrições**. Escrito assim, existem algoritmos clássicos e exatos para cada parte, e o LLM fica só com o que sobra de genuinamente ambíguo.

### O problema, formalizado

Dado um grupo de pernas, encontrar uma **partição** delas em blocos em que:
1. cada bloco **casa com o modelo** de uma estrutura da base (tipos, relações entre K1 e K2, vencimentos, razões de notional);
2. o **lado** de cada perna, que o DTCC não informa, é uma variável a descobrir;
3. **toda perna é explicada exatamente uma vez.** Uma perna que não casa com nada vira uma vanilla avulsa;
4. entre as partições válidas, ganham as **mais plausíveis**.

### Os algoritmos, um para cada parte

| Parte | Classe de algoritmo | Na prática |
|---|---|---|
| 1. Um bloco casa com uma estrutura? | **Satisfação de restrições (CSP)** com unificação | Os símbolos da tabela de pernas (K1, K2, T1) viram variáveis, e "K1 < K2" ou "mesmo T1" viram restrições. Uma busca com retrocesso testa as associações perna ↔ linha do modelo. Com até ~10 pernas, é instantâneo. |
| 2. O lado desconhecido | **Variável latente enumerada** dentro do mesmo CSP | São 2ⁿ combinações de sinais, poucas para n pequeno. Quando mais de uma combinação satisfaz o modelo, a ambiguidade (SN↔RR) aparece naturalmente como várias soluções. |
| 3. Dividir o grupo em estruturas | **Cobertura exata**: Algorithm X do Knuth, ou **programação linear inteira** | Primeiro se listam todos os pares (subconjunto, estrutura) que casam. Depois se escolhe a combinação que cobre cada perna uma única vez. Bibliotecas como o OR-Tools (CP-SAT) ou o PuLP resolvem isso facilmente nesses tamanhos. |
| 4. Qual partição é a mais plausível | **Pontuação probabilística** (bayesiana ou regressão logística) com **navalha de Occam** | Somam pontos os sinais "típicos" já documentados nas notas: delta 25, ATM, asas simétricas, prêmio líquido perto de zero. Perdem pontos as partições com muitos blocos e com estruturas genéricas (2L…). As frequências observadas no DTCC entram como priors. |
| 5. Dados imperfeitos | **Restrições flexíveis** (MaxSAT ponderado) | Strike igual dentro de uma tolerância, razão de notional com arredondamento, notional com teto tratado como "≥ teto". Violar uma restrição flexível custa pontos em vez de eliminar a solução. |
| Antes de tudo: formar o grupo | **Componentes conexas numa janela de tempo** | Em vez de exigir o mesmo segundo, ligar pernas do mesmo subjacente separadas por menos de Δt, e usar o `Package indicator` quando existir. Isso ataca erros de agrupamento, que vêm antes de qualquer classificação. |

### Como isso muda o papel do LLM

Com essas peças, o matching deixa de só filtrar candidatas e passa a devolver **as k melhores partições completas**, cada uma com pontuação, lados inferidos e o motivo de cada restrição satisfeita ou violada. O LLM então:
- escolhe entre as k partições ou confirma a primeira;
- explica a escolha citando as notas;
- sinaliza quando nenhuma partição convence.

Isso reduz bastante o espaço de erro do modelo, e o rastro de cada decisão fica ainda mais completo.

O feedback também ganha um destino concreto: a pontuação da parte 4 pode virar um modelo pequeno e interpretável (regressão logística), treinado nas suas avaliações. É o "aprender com o feedback" discutido no RLHF (ideia 3), só que barato, transparente e sem tocar no LLM.

### Para o TCC

Formalizar o problema como cobertura exata com casamento de padrões já é uma contribuição metodológica. Também abre um experimento limpo de três braços:
- matching exato + pontuação;
- matching + LLM;
- só o LLM.

## 2. Usos do feedback humano, sem treinar o LLM (Fase D)

| Uso | Como |
|---|---|
| Corrigir a camada certa | Agrupar os erros pela `camada_do_erro` e corrigir a maior. |
| Exemplos tirados das revisões | Incluir no pedido ao modelo 2 ou 3 decisões já revisadas com a mesma assinatura, com a resposta certa. **Nunca usar casos do conjunto de teste.** |
| Calibrar a confiança | Comparar a confiança declarada com o acerto real, por faixa, e ajustar. |
| Comparar versões | Rodar cada versão (prompt, base, modelo) nos mesmos casos revisados e escolher a melhor. |
| Pontuação aprendida | Treinar a pontuação do matching (ideia 1, parte 4) como regressão logística sobre as avaliações. |

## 3. RLHF: fora do escopo, possível trabalho futuro

Não compensa no TCC:
- não dá para treinar o Claude pela API;
- faltam dados: seriam necessárias milhares de comparações;
- o conhecimento iria para dentro dos pesos e deixaria de ser citável e auditável;
- cada correção exigiria treinar de novo.

As ideias 1 e 2 tiram o mesmo valor do feedback de forma barata e transparente. RLHF, ou ajuste de um modelo aberto, só faria sentido se o sistema fosse para produção e acumulasse milhares de revisões.
