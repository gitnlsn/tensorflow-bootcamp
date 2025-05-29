# Types or Learning algorithms

Chapter: 3

Resumo:

- supervisionado
    - dados com labels pré-definidas
    - aprendizado do mapeamento
    - classificação e regressão
- não supervisionado
    - dados não rotulados
    - descoberta de padrões
    - agrupamento, associação e redução de dimensionalidade
- reforço
    - dados não rotulados
    - maximização de função
        - recompensa e penalidade

O Machine Learning (Aprendizado de Máquina) é uma área da Inteligência Artificial que permite que sistemas aprendam a partir de dados, identifiquem padrões e tomem decisões com o mínimo de intervenção humana. Existem três paradigmas principais no aprendizado de máquina: **Aprendizado Supervisionado**, **Aprendizado Não Supervisionado** e **Aprendizado por Reforço**.

### 1. Aprendizado Supervisionado (Supervised Learning)

**O que é:** O aprendizado supervisionado é o tipo mais comum de Machine Learning. Nele, o algoritmo é treinado com um conjunto de dados que já possui "rótulos" ou "saídas" conhecidas. É como ensinar uma criança com exemplos: "Este é um cachorro, este é um gato, este é um cachorro..." O modelo aprende a mapear as entradas (dados) para as saídas (rótulos) a partir desses exemplos rotulados. Uma vez treinado, o modelo pode prever as saídas para novos dados não vistos.

**Como funciona:**

- **Dados Rotulados:** Requer um conjunto de dados onde cada exemplo de entrada está associado a uma saída correta.
- **Aprendizado do Mapeamento:** O algoritmo busca aprender uma função que mapeie as entradas para as saídas.
- **Previsão:** Uma vez treinado, o modelo é capaz de prever as saídas para novas entradas.

**Tipos de problemas que resolve:**

- **Classificação:** Prever uma categoria discreta (ex: spam/não spam, doença/não doença).
- **Regressão:** Prever um valor contínuo (ex: preço de uma casa, temperatura).

**Exemplos:**

- **Detecção de Spam:** O sistema é treinado com e-mails rotulados como "spam" ou "não spam". Ele aprende a identificar características de spam (palavras-chave, remetente, etc.) e, em seguida, classifica novos e-mails.
- **Previsão de Preços de Imóveis:** Com base em dados históricos de casas (tamanho, número de quartos, localização, etc.) e seus respectivos preços, o modelo aprende a prever o preço de uma nova casa.
- **Diagnóstico Médico:** Prever a probabilidade de uma doença com base em sintomas, idade, resultados de exames de um paciente.
- **Reconhecimento de Imagens:** Treinar um modelo para identificar objetos específicos (carros, pessoas, etc.) em imagens, após serem mostradas inúmeras imagens com esses objetos rotulados.

### 2. Aprendizado Não Supervisionado (Unsupervised Learning)

**O que é:** No aprendizado não supervisionado, o algoritmo recebe dados **não rotulados**. O objetivo não é prever uma saída específica, mas sim encontrar padrões ocultos, estruturas ou relações dentro dos dados. É como dar a uma criança um monte de objetos e pedir para ela organizá-los sem dar nenhuma instrução prévia.

**Como funciona:**

- **Dados Não Rotulados:** Não há saídas pré-definidas ou rótulos nos dados de treinamento.
- **Descoberta de Padrões:** O algoritmo busca encontrar agrupamentos, associações ou reduzir a complexidade dos dados.
- **Nenhuma Orientação Externa:** O aprendizado acontece sem intervenção humana para corrigir ou validar as saídas.

**Tipos de problemas que resolve:**

- **Agrupamento (Clustering):** Agrupar pontos de dados semelhantes em "clusters" ou grupos.
- **Associação:** Descobrir regras que descrevem a relação entre diferentes variáveis nos dados.
- **Redução de Dimensionalidade:** Simplificar dados com muitas variáveis, encontrando representações mais compactas.

**Exemplos:**

- **Segmentação de Clientes:** Agrupar clientes de uma empresa com base em seu comportamento de compra, dados demográficos ou histórico de navegação, para que a empresa possa criar campanhas de marketing mais direcionadas.
- **Sistemas de Recomendação:** Em plataformas como Netflix ou Amazon, o sistema pode agrupar usuários com gostos semelhantes ou produtos frequentemente comprados juntos para recomendar itens relevantes (ex: "quem comprou X também comprou Y").
- **Detecção de Anomalias:** Identificar comportamentos incomuns em um conjunto de dados, como transações financeiras fraudulentas ou falhas em equipamentos industriais, onde os dados anormais se destacam dos padrões normais.
- **Organização de Documentos:** Agrupar documentos de texto com temas semelhantes, mesmo que não haja categorias pré-definidas.

### 3. Aprendizado por Reforço (Reinforcement Learning)

**O que é:** O aprendizado por reforço é um tipo de aprendizado onde um "agente" aprende a tomar decisões sequenciais em um "ambiente" para maximizar uma "recompensa". Ele aprende por tentativa e erro, recebendo feedback na forma de recompensas (por ações boas) ou penalidades (por ações ruins). Não há um conjunto de dados rotulados pré-definido; o agente aprende através da interação com o ambiente.

**Como funciona:**

- **Agente:** O tomador de decisões (ex: um robô, um algoritmo de jogo).
- **Ambiente:** O contexto onde o agente atua (ex: um jogo, o mundo real).
- **Estado:** A situação atual do ambiente.
- **Ação:** O que o agente faz no ambiente.
- **Recompensa:** Feedback positivo ou negativo que o agente recebe após uma ação.
- **Política:** A estratégia que o agente desenvolve para escolher ações em diferentes estados.

**Exemplos:**

- **Jogos (AlphaGo, xadrez):** Um agente de IA aprende a jogar xadrez ou Go. Ele experimenta diferentes movimentos e recebe uma recompensa se ganhar o jogo e uma penalidade se perder. Com milhões de simulações, ele otimiza sua estratégia para maximizar as vitórias.
- **Carros Autônomos:** Um carro autônomo aprende a dirigir navegando em um ambiente (real ou simulado). Ele recebe recompensas por chegar ao destino com segurança e no tempo certo, e penalidades por colisões ou desvios de rota.
- **Robótica:** Um robô aprende a andar, manipular objetos ou completar tarefas em um ambiente físico. Ele recebe recompensas por realizar a tarefa corretamente e penalidades por erros.
- **Otimização de Processos Industriais:** Um sistema de IA pode aprender a otimizar a operação de uma fábrica, ajustando parâmetros para maximizar a produção e minimizar o consumo de energia, recebendo recompensas por bons resultados.

### Tabela Comparativa

| Característica | Aprendizado Supervisionado | Aprendizado Não Supervisionado | Aprendizado por Reforço |
| --- | --- | --- | --- |
| **Dados** | Rotulados (entrada-saída conhecida) | Não Rotulados (apenas entradas) | Não Rotulados (apenas interações e recompensas) |
| **Objetivo** | Prever saídas para novos dados | Encontrar padrões, estruturas ou relações ocultas | Aprender a tomar decisões para maximizar recompensas |
| **Feedback** | Direto (rótulos corretos fornecidos) | Indireto (nenhum rótulo; o algoritmo se auto-organiza) | Baseado em recompensas/penalidades de ações sequenciais |
| **Intervenção Humana** | Alta (para rotular os dados) | Baixa (para interpretar os padrões descobertos) | Variável (para definir as recompensas e o ambiente) |
| **Exemplos de Tarefas** | Classificação, Regressão | Agrupamento, Redução de Dimensionalidade, Regras de Associação | Jogos, Robótica, Carros Autônomos |