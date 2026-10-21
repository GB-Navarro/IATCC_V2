# Ideias

Propostas ainda não aprovadas. Quando uma ideia for aceita, ela vira item do [`to-do.md`](to-do.md) e decisão em [`decisoes.md`](decisoes.md).

## 1. Algoritmos de busca para o matching (Fases B e C)

**Status:** aceita como a versão **Agente + algoritmos**, que será comparada com a versão **Agente** (LLM sozinha). Ver D31 e o `to-do.md`.

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
| Antes de tudo: formar o grupo | **Componentes conexas numa janela de tempo** | Ligar pernas com a mesma plataforma de execução e o mesmo par de moedas, separadas por menos de Δt segundos (D30), e usar o `Package indicator` quando existir. Isso ataca erros de agrupamento, que vêm antes de qualquer classificação. |

### Como isso muda o papel do LLM

Com essas peças, o matching deixa de só filtrar candidatas e passa a devolver **as k melhores partições completas**, cada uma com pontuação, lados inferidos e o motivo de cada restrição satisfeita ou violada. O LLM então:
- escolhe entre as k partições ou confirma a primeira;
- explica a escolha citando as notas;
- sinaliza quando nenhuma partição convence.

Isso reduz bastante o espaço de erro do modelo, e o rastro de cada decisão fica ainda mais completo.

O feedback também ganha um destino concreto: a pontuação da parte 4 pode virar um modelo pequeno e interpretável (regressão logística), treinado nas suas avaliações. É o "aprender com o feedback" discutido no RLHF (ideia 3), só que barato, transparente e sem tocar no LLM.

### Explicação intuitiva: a linha de montagem

Uma analogia do dia a dia e o mesmo exemplo pequeno do começo ao fim. Os nomes técnicos aparecem só no final de cada passo, entre parênteses.

#### A analogia: a lanchonete

Imagine que você recebe as notas de uma lanchonete. A nota lista **itens soltos** (hambúrguer, batata, refrigerante), mas **não diz qual combo** o cliente pediu. Você tem o **cardápio**, que diz de que itens cada combo é feito. O trabalho é descobrir quais combos foram pedidos.

| Lanchonete | Nosso problema |
|---|---|
| item da nota | perna (um registro do DTCC) |
| pedido de um cliente | grupo de pernas |
| cardápio | a base (as 65 notas) |
| combo | estrutura (BF, RR, SG…) |
| receita do combo | tabela de pernas da nota |

O processo é uma **linha de montagem com sete estações**. Cada estação responde a uma pergunta.

**Os registros do exemplo** (todos com vencimento em 3 meses e notional de 10M):

| Registro | Horário | Plataforma | Par | Tipo | Strike |
|---|---|---|---|---|---|
| P1 | 10:00:00,2 | SEF-A | EURUSD | put | 1,08 |
| C2 | 10:00:00,9 | SEF-A | EURUSD | call | 1,12 |
| P2 | 10:00:01,3 | SEF-A | EURUSD | put | 1,10 |
| C1 | 10:00:01,4 | SEF-A | EURUSD | call | 1,10 |
| J1 | 10:00:01,5 | SEF-A | USDJPY | call | 150,00 |
| P3 | 10:00:30,0 | SEF-A | EURUSD | put | 1,05 |

#### Estação 1 — Agrupamento: "quais itens são do mesmo pedido?"

**Intuição:** itens do mesmo pedido saem do **mesmo caixa** (plataforma), são do **mesmo cardápio** (par de moedas) e aparecem **quase juntos** (poucos segundos de diferença).

**Passo a passo** (com intervalo Δt = 2 s, ilustrativo):
1. Ordenar os registros por horário.
2. Ir de um em um. O registro entra no grupo do anterior se tiver a mesma plataforma, o mesmo par e uma diferença de horário menor que 2 s. Senão, abre um grupo novo.
   - **P1:** abre o grupo A.
   - **C2:** 0,7 s depois, SEF-A, EURUSD → grupo A.
   - **P2:** 0,4 s depois de C2 → grupo A.
   - **C1:** 0,1 s depois de P2 → grupo A.
   - **J1:** é USDJPY, outro par → abre o grupo B.
   - **P3:** EURUSD, mas 28,6 s depois → abre o grupo C.

**Resultado:** grupo A = {P1, C2, P2, C1}; grupo B = {J1}; grupo C = {P3}. Os grupos B e C têm uma perna só, então cada um é simplesmente uma vanilla. Daqui em diante, o exemplo segue só com o grupo A.

*(Nome técnico: componentes conexas numa janela de tempo.)*

#### Estação 2 — Casamento: "este conjunto de itens é o combo X?"

**Intuição:** a receita do combo tem **espaços em branco** com regras. A do butterfly diz, por exemplo: "duas puts e duas calls; a put de dentro e a call de dentro com o mesmo strike; strikes crescendo de fora para dentro". Casar é **tentar encaixar cada perna num espaço** e conferir as regras. Se uma regra quebra, você **desfaz o último encaixe e tenta outro**, como quem testa chaves numa fechadura.

**A receita do BF** (tirada da nota): espaço 1 = put com strike K1 · espaço 2 = put com strike K2 · espaço 3 = call com strike K2 · espaço 4 = call com strike K3. As letras são as regras: K1 < K2 < K3, e os dois "K2" têm de ser o mesmo número.

**Passo a passo:**
1. **Espaço 1 (put K1):** tento P1. Agora K1 vale 1,08.
2. **Espaço 2 (put K2):** a única put que sobra é P2. Agora K2 vale 1,10. Regra K2 > K1? 1,10 > 1,08 ✓.
3. **Espaço 3 (call K2):** K2 já vale 1,10, então só serve uma call de 1,10: C1 ✓.
4. **Espaço 4 (call K3):** sobra C2. Agora K3 vale 1,12. Regra K3 > K2? ✓. **Casou: é um BF.**

Se no passo 1 eu tivesse tentado P2 (K1 = 1,10), o passo 2 precisaria de uma put acima de 1,10. Não há, então eu desfaria e tentaria P1, que é o caminho acima.

**Um exemplo que não casa, o condor (CR).** A receita pede quatro strikes todos diferentes e crescentes. P2 e C1 têm o mesmo strike (1,10), então a regra "K2 < K3" vira "1,10 < 1,10", que é falso. O condor fica descartado.

**O ponto mais importante:** o algoritmo faz isso com **as 65 receitas, sempre do mesmo jeito**. Ele não sabe o que é um butterfly; só sabe ler uma receita e conferir as regras. Para incluir uma estrutura nova, basta escrever uma receita nova na base.

*(Nome técnico: satisfação de restrições com retrocesso e unificação.)*

#### Estação 3 — Variantes: "o mesmo combo, em outra versão"

**Intuição:** o cardápio lista o combo "com refrigerante", mas o cliente pode pedir "com suco". Em vez de escrever as duas versões no cardápio, o sistema **gera a outra versão sozinho**.

**O espelho** (a versão com suco) faz duas trocas em cada linha da receita:
1. troca call por put, e put por call;
2. inverte a ordem dos strikes: o mais baixo vira o mais alto, como num espelho.

**Exemplo:** a receita do call spread (CP) é "comprar call K1 · vender call K2". Espelhando, fica "comprar put K2 · vender put K1": compra a put de strike mais alto e vende a de strike mais baixo. É o put spread. O mercado dá outro nome, mas a estrutura é a mesma, sem nota nova na base.

**O short** (inverter compra e venda) é mais simples: o mesmo combo, do outro lado do balcão. Como o DTCC **não informa** quem comprou e quem vendeu, o short não muda nada no casamento. Ele só muda o nome da hipótese: "butterfly comprado" ou "butterfly vendido".

#### Estação 4 — Divisão: "como dividir o pedido em combos?"

**Intuição:** um pedido de 4 itens pode ser **um combo grande**, **dois combos pequenos** ou **4 itens avulsos**. É um quebra-cabeça: montar o pedido inteiro **sem sobrar item e sem usar o mesmo item duas vezes**.

**Passo A — Juntar as peças.** A estação 2 roda em todos os subconjuntos do grupo, e cada um que casa vira uma peça:
- **BF:** {P1, P2, C1, C2};
- **SD:** {P2, C1}, mesmo strike;
- **SN ou RR:** {P1, C2}, {P1, C1} e {P2, C2};
- **CP espelhado (put spread):** {P1, P2};
- **CP:** {C1, C2};
- **vanilla avulsa:** cada perna sozinha.

A vanilla avulsa garante que sempre existe pelo menos uma resposta, nem que seja "4 itens soltos".

**Passo B — Montar.** O algoritmo pega uma perna e testa cada peça que a contém. Para cada escolha, tira da mesa as peças que usariam pernas já usadas e continua com o que sobra:

```
perna P1 — quais peças a contêm?
├── BF {P1,P2,C1,C2} → cobre tudo                      ✓ divisão 1: BF
├── SN/RR {P1,C2}  → sobram P2, C1
│   ├── SD {P2,C1}                                      ✓ divisão 2: SN/RR + SD
│   └── P2 avulsa + C1 avulsa                           ✓ divisão 3
├── put spread {P1,P2} → sobram C1, C2
│   ├── call spread {C1,C2}                             ✓ divisão 4: dois CPs
│   └── C1 avulsa + C2 avulsa                           ✓ divisão 5
├── SN/RR {P1,C1} → sobram P2, C2 → SN/RR {P2,C2}…      ✓ mais divisões
└── P1 avulsa → continua com P2, C1, C2…                ✓ mais divisões
```

**Resultado:** uma lista com **todas** as formas válidas de explicar o pedido, umas 10 neste exemplo. Esta estação **não escolhe** a melhor; isso é com a próxima.

*(Nome técnico: cobertura exata, Algorithm X ou programação linear inteira.)*

#### Estação 5 — Pontuação: "qual divisão é a mais provável?"

**Intuição:** é um detetive pesando pistas, com três critérios:
- **Preferir a explicação mais simples.** Quatro pernas no mesmo segundo formando exatamente um butterfly é mais provável do que dois clientes que, por coincidência, pediram dois combos que se encaixam perfeitamente. Cada combo a mais custa pontos.
- **Conferir os traços típicos.** As notas dizem como cada estrutura costuma aparecer: no BF, o strike do meio fica exatamente entre os outros dois; no RR, os prêmios se cancelam (custo zero); no SD, o strike é ATM. Cada traço confirmado nas pernas soma pontos.
- **Considerar a frequência.** Estruturas comuns no DTCC começam com uma pequena vantagem.

**Passo a passo** (pontos ilustrativos):

| Divisão | Começa | Por bloco (−1 cada) | Traços típicos | Total |
|---|---|---|---|---|
| BF | 0 | −1 | strike do meio exatamente no meio (1,10 entre 1,08 e 1,12): +2 | **+1** |
| SD + SN | 0 | −2 | SD com strike ATM: +1 | −1 |
| dois CPs | 0 | −2 | nenhum | −2 |
| 4 avulsas | 0 | −4 | nenhum | −4 |

Os totais viram percentuais: **BF ≈ 80%**, SD + SN ≈ 15%, o resto ≈ 5%.

*(Nome técnico: pontuação probabilística com navalha de Occam.)*

#### Estação 6 — Tolerância: "e se a nota tiver pequenos erros?"

**Intuição:** em vez de um juiz que reprova por qualquer detalhe, um professor que **desconta pontos** por erros pequenos. Dados reais têm imprecisões, e regras rígidas jogariam fora a resposta certa.

**Exemplos:**
- **Strikes quase iguais:** P2 = 1,10000 e C1 = 1,10002. Pela regra rígida, "mesmo strike" falha. Com tolerância, a diferença está dentro de 1 tick: aceita, sem desconto.
- **Notional com teto:** C2 aparece como "100M+" (o DTCC esconde o valor exato de operações grandes). Com tolerância, "pode ser igual aos outros": aceita, com um desconto pequeno pela incerteza.
- **Notional quase igual:** 9,8M contra 10M. Com tolerância, 2% de diferença: aceita, com um desconto um pouco maior.

O BF continua vencendo, só que com nota menor. O rastro registra quais tolerâncias foram usadas e quanto custaram.

#### Estação 7 — Roteamento: "preciso chamar o agente?"

**Intuição:** quando o detetive tem certeza, encerra o caso. Quando há duas explicações empatadas, chama um especialista.

1. **Uma divisão claramente na frente** (o BF com 80%): o algoritmo decide sozinho, sem chamar o LLM.
2. **Empate:** um grupo com só put 1,08 e call 1,12 casa com **SN** e com **RR**, que diferem apenas em quem comprou e quem vendeu. O DTCC não informa isso, então a pontuação empata. O caso vai para o agente com as duas candidatas, os deltas, os prêmios e as notas. Ele decide e explica, ou marca como ambiguidade legítima.

#### Resumo da linha de montagem

| Estação | Pergunta | Saída no exemplo |
|---|---|---|
| 1. Agrupamento | quais itens são do mesmo pedido? | {P1, C2, P2, C1} |
| 2. Casamento | este conjunto é o combo X? | BF casa; CR não |
| 3. Variantes | e as outras versões do combo? | o put spread também vira peça |
| 4. Divisão | como dividir o pedido em combos? | umas 10 divisões válidas |
| 5. Pontuação | qual é a mais provável? | BF com 80% |
| 6. Tolerância | e os pequenos erros nos dados? | BF continua, com desconto |
| 7. Roteamento | precisa do agente? | não; o grupo SN/RR, sim |

Todas as estações são **genéricas**. O que muda de uma estrutura para outra está nas **receitas da base**, não no código.

### Algoritmos + LLM × LLM sozinha

Não dá para garantir de antemão que a combinação é melhor. É uma **hipótese com bons motivos**, e o TCC deve prová-la medindo. Há razões concretas para esperar que algoritmos + LLM seja melhor do que a LLM sozinha na maior parte dos casos, e também há casos em que a LLM sozinha pode empatar ou até ganhar.

#### Por que se espera que seja melhor

**1. A LLM não garante ver todas as divisões possíveis.** Pense num grupo de 6 pernas, todas com o mesmo vencimento e o mesmo notional:

| Perna | P4 | P1 | P2 | C1 | C2 | C4 |
|---|---|---|---|---|---|---|
| Tipo e strike | put 1,06 | put 1,08 | put 1,10 | call 1,10 | call 1,12 | call 1,14 |

Há pelo menos duas leituras igualmente simples, com 2 estruturas cada:
- **BF** (P1, P2, C1, C2) + **SN ou RR** (P4, C4);
- **CR** (P4, P1, C2, C4) + **SD** (P2, C1).

A LLM tende a enxergar a primeira leitura plausível ("tem um butterfly aqui") e parar. A estação 4 **lista as duas por construção**, e a escolha vira uma comparação explícita. Com 8 a 10 pernas, o número de divisões cresce rápido, e esse risco aumenta.

**2. Conferências numéricas exatas.** Para casar, é preciso conferir dezenas de relações: strike igual dentro de 1 tick, ordem dos strikes, razão de notional 1:2:1, notional com teto. Para uma LLM, comparar 1,10000 com 1,10002 ou 9,8M com 10M é exatamente o tipo de tarefa em que ela erra de vez em quando, e de forma diferente a cada execução. Para o código, é trivial e sempre igual.

**3. Mesma entrada, mesma resposta.** O algoritmo dá sempre o mesmo resultado para o mesmo grupo. A LLM pode classificar o mesmo grupo de formas diferentes em duas execuções. Para o TCC, a reprodutibilidade conta; para o ciclo de feedback, também: se a resposta varia sozinha, você não sabe se a correção que fez funcionou.

**4. Ela só responde com o que a base sustenta.** A LLM sozinha pode responder "iron condor" ou "ratio spread", que não existem na base. Uma lista fechada de códigos (`enum`) evita o nome inventado, mas não evita **forçar** um encaixe errado. O algoritmo só devolve encaixes que respeitam uma receita da base, ou diz explicitamente "nada casa".

**5. A explicação é o próprio cálculo.** O rastro do algoritmo **é** o motivo: "CR eliminado porque 1,10 < 1,10 é falso". A explicação da LLM é ela descrevendo o que acha que fez, sem garantia de que foi isso. Na revisão, isso faz diferença: com o algoritmo, você sabe exatamente qual regra corrigir.

**6. Custo e volume.** O DTCC tem milhares de grupos por dia, e a maioria é trivial (uma ou duas pernas). O algoritmo resolve cada um em milissegundos e sem custo. A LLM sozinha cobra por todos, inclusive pelos óbvios. No modelo híbrido, ela só é chamada para os casos ambíguos.

**7. Corrigir a base corrige o comportamento.** Se você corrige uma nota (ex.: a restrição do DS), o algoritmo passa a obedecer na hora, de forma previsível. A LLM sozinha lê a nota em prosa e pode ou não aplicar a correção do jeito esperado.

#### Onde a LLM sozinha pode empatar ou ganhar

- **Grupos simples** (2 pernas óbvias): ela provavelmente acerta tanto quanto o algoritmo; só custa mais.
- **O que está fora da base:** diante de algo que nenhuma receita cobre, o algoritmo responde "genérica de N pernas". A LLM pode reconhecer o padrão ("parece um ratio spread") e sugerir uma estrutura nova.
- **Juntar sinais fracos e contexto:** se a pontuação do algoritmo for mal calibrada, ele escolhe errado com confiança. A LLM pode pesar melhor o que não foi codificado.
- **Custo de construção:** a LLM sozinha fica pronta em dias; os algoritmos levam semanas.

Por isso a proposta é **híbrida, e não "algoritmo no lugar da LLM"**: cada um faz aquilo em que é melhor.

#### Como provar de verdade

**1. Piloto antes de construir os algoritmos.** Assim que os casos de teste existirem, rodar a LLM sozinha neles. É barato e responde à pergunta com dados:
- se ela já acertar quase tudo, inclusive os grupos grandes e os dados imperfeitos, os algoritmos podem ficar mais simples do que o planejado;
- se errar nos tipos de caso acima, você terá a demonstração do porquê, com exemplos reais para o TCC.

**2. Experimento completo com três braços:** algoritmos sozinhos, algoritmos + LLM e só a LLM. Para cada braço, medir:
- acerto no topo e no top-k;
- **consistência**: a mesma resposta em 5 execuções?
- custo por grupo;
- acerto separado por tamanho do grupo e por dados limpos × imperfeitos.

A expectativa é que a diferença apareça **nos grupos grandes e nos dados imperfeitos**, e quase desapareça nos grupos simples. Se não for assim, também é um resultado válido para o TCC.

### Para o TCC

Formalizar o problema como cobertura exata com casamento de padrões já é uma contribuição metodológica. Também abre o experimento de três braços descrito acima:
- algoritmos sozinhos (matching exato + pontuação);
- **Agente + algoritmos** (matching + LLM);
- **Agente** (só o LLM).

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
