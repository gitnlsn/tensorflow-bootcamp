# Medidas de avaliação de modelos

Chapter: 3

Em Machine Learning, especialmente em problemas de classificação, **accuracy (acurácia), recall (sensibilidade ou revocação) e precision (precisão)** são métricas cruciais para avaliar o desempenho de um modelo. Elas nos dão diferentes perspectivas sobre o quão bem o modelo está fazendo suas previsões.

Para entender essas métricas, é fundamental conhecer os quatro resultados possíveis de uma classificação:

- **Verdadeiro Positivo (VP):** O modelo previu corretamente a classe positiva. Ex: O modelo previu que a imagem era um cachorro, e de fato era um cachorro.
- **Verdadeiro Negativo (VN):** O modelo previu corretamente a classe negativa. Ex: O modelo previu que a imagem não era um cachorro, e de fato não era um cachorro.
- **Falso Positivo (FP):** O modelo previu a classe positiva incorretamente. Ex: O modelo previu que a imagem era um cachorro, mas na verdade era um gato. (Erro Tipo I)
- **Falso Negativo (FN):** O modelo previu a classe negativa incorretamente. Ex: O modelo previu que a imagem não era um cachorro, mas na verdade era um cachorro. (Erro Tipo II)

Esses termos são frequentemente organizados em uma **matriz de confusão**, que é uma tabela que resume o desempenho do modelo em relação aos resultados reais e previstos.

---

### Accuracy (Acurácia)

A **acurácia** mede a proporção de todas as previsões que foram corretas, tanto positivas quanto negativas, em relação ao total de previsões. É a métrica mais intuitiva e fácil de entender.

**Fórmula:**Accuracy=VP+VN+FP+FNVP+VN

**Interpretação:**
Uma acurácia de 90% significa que o modelo acertou 90 em cada 100 previsões.

**Quando usar:**
A acurácia é uma boa métrica quando o **conjunto de dados é balanceado**, ou seja, quando há um número aproximadamente igual de exemplos para cada classe.

**Limitações:**Em conjuntos de dados desbalanceados (onde uma classe é muito mais frequente que a outra), a acurácia pode ser enganosa. Por exemplo, se em um problema de detecção de fraude, 99% das transações são legítimas e 1% são fraudulentas, um modelo que simplesmente classifica todas as transações como "legítimas" teria 99% de acurácia, mas seria inútil para detectar fraudes.

---

### Recall (Sensibilidade ou Revocação)

O **recall**, também conhecido como **taxa de verdadeiros positivos (TVP)** ou **sensibilidade**, mede a proporção de todas as instâncias positivas *reais* que foram corretamente identificadas pelo modelo. Em outras palavras, ele responde à pergunta: "De todas as coisas que *realmente* eram positivas, quantas o modelo conseguiu capturar?"

**Fórmula:**Recall=VP+FNVP

**Interpretação:**
Um recall de 95% para a classe "fraude" significa que o modelo conseguiu identificar 95% de todas as transações fraudulentas reais.

**Quando usar:**
O recall é crucial quando o **custo de um falso negativo é alto**. Ou seja, quando é muito importante não perder nenhuma instância positiva real.

**Exemplos de uso:**

- **Diagnóstico médico (doenças graves):** É preferível ter alguns falsos positivos (pessoas saudáveis classificadas como doentes, que farão exames adicionais) do que falsos negativos (pessoas doentes classificadas como saudáveis, que não receberão tratamento).
- **Detecção de fraude:** Não queremos perder transações fraudulentas, mesmo que isso signifique investigar algumas transações legítimas.
- **Sistemas de segurança (detecção de intrusos):** É vital detectar todos os intrusos, mesmo que ocasionalmente soe um alarme falso.

---

### Precision (Precisão)

A **precision** mede a proporção de todas as previsões positivas do modelo que foram *realmente* positivas. Em outras palavras, ela responde à pergunta: "Das coisas que o modelo classificou como positivas, quantas estavam *corretas*?"

**Fórmula:**Precision=VP+FPVP

**Interpretação:**Uma precision de 80% para a classe "spam" significa que, de todos os e-mails que o modelo classificou como spam, 80% eram de fato spam.

**Quando usar:**A precision é importante quando o **custo de um falso positivo é alto**. Ou seja, quando é fundamental que as previsões positivas do modelo sejam muito confiáveis.

**Exemplos de uso:**

- **Filtro de spam em e-mails:** Não queremos que e-mails importantes (não-spam) sejam classificados como spam (falsos positivos), pois o usuário pode perdê-los. É preferível que alguns spams passem (falsos negativos) do que e-mails importantes sejam bloqueados.
- **Recomendações de produtos:** Se um sistema recomenda produtos que não interessam ao usuário (falsos positivos), isso pode levar à frustração e à perda de confiança no sistema.
- **Processos de fabricação (controle de qualidade):** Se o modelo classifica produtos bons como defeituosos (falsos positivos), isso gera desperdício.

---

### Trade-off entre Precision e Recall

É comum haver um **trade-off** entre precision e recall. Melhorar um geralmente significa piorar o outro. Por exemplo:

- Um modelo que é muito conservador e faz pouquíssimas previsões positivas terá alta precision (quase todas as previsões positivas serão corretas), mas pode ter baixo recall (perderá muitas instâncias positivas reais).
- Um modelo que é muito agressivo e tenta capturar todas as instâncias positivas possíveis terá alto recall, mas pode ter baixa precision (muitas de suas previsões positivas serão falsos positivos).

A escolha da métrica mais importante (ou a combinação delas, como o **F1-Score**, que é a média harmônica de precision e recall) depende do contexto do problema e das consequências de cada tipo de erro (falso positivo vs. falso negativo).

Ao avaliar um modelo de Machine Learning, é fundamental analisar essas métricas em conjunto com a matriz de confusão para ter uma compreensão completa do seu desempenho e decidir qual métrica otimizar com base nos objetivos do negócio.