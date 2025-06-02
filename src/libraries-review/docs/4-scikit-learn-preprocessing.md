# Scikit-Learn Preprocessing - Revisão da Biblioteca

## Introdução
Scikit-learn é a principal biblioteca de machine learning em Python, oferecendo ferramentas completas para preprocessamento de dados, modelagem e avaliação de modelos.

## 1. Divisão de Dados (Train/Test Split)

### Separação Treino/Teste
```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)
```

**Conceito-chave:** A divisão treino/teste é fundamental para avaliar o desempenho real do modelo. O `test_size=0.3` significa 30% dos dados para teste.

**Parâmetros importantes:**
- `test_size`: Proporção dos dados para teste (0.2 = 20%, 0.3 = 30%)
- `random_state`: Garante reprodutibilidade da divisão
- `stratify`: Mantém proporção das classes em problemas de classificação

## 2. Normalização e Padronização

### MinMaxScaler - Normalização [0,1]
```python
from sklearn.preprocessing import MinMaxScaler

minmax_scaler = MinMaxScaler()
X_train_scaled = minmax_scaler.fit_transform(X_train)
X_test_scaled = minmax_scaler.transform(X_test)
```

**Fórmula:** `(x - min) / (max - min)`

**Quando usar:**
- Quando você conhece os valores mínimo e máximo
- Para algoritmos sensíveis à escala (SVM, KNN, Redes Neurais)
- Quando quer preservar a distribuição original

### StandardScaler - Padronização (Z-score)
```python
from sklearn.preprocessing import StandardScaler

std_scaler = StandardScaler()
X_train_std = std_scaler.fit_transform(X_train)
X_test_std = std_scaler.transform(X_test)
```

**Fórmula:** `(x - média) / desvio_padrão`

**Características:**
- Resultado tem média = 0 e desvio padrão = 1
- Não limita valores a um range específico
- Melhor para dados com distribuição normal

**Conceito crítico:** Sempre use `fit()` apenas nos dados de treino, depois `transform()` no teste para evitar data leakage.

## 3. Preprocessamento de Dados Categóricos

### LabelEncoder - Codificação Ordinal
```python
from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
categorias_encoded = label_encoder.fit_transform(categorias['cor'])

# Mapeamento: azul=0, verde=1, vermelho=2
```

**Quando usar:**
- Variáveis categóricas **ordinais** (Pequeno < Médio < Grande)
- Como etapa intermediária para OneHotEncoder
- Quando há relação de ordem entre as categorias

**Cuidado:** Não use para variáveis nominais pois cria ordem artificial.

### OneHotEncoder - Codificação Dummy
```python
from sklearn.preprocessing import OneHotEncoder

onehot_encoder = OneHotEncoder(sparse_output=False, drop='first')
encoded_features = onehot_encoder.fit_transform(data[['categoria']])
```

**Funcionamento:**
- Cada categoria vira uma coluna binária (0 ou 1)
- `drop='first'` remove uma coluna para evitar multicolinearidade
- Ideal para variáveis categóricas **nominais**

**Exemplo:**
```
Cor Original  →  cor_verde  cor_vermelho
azul          →      0           0
verde         →      1           0  
vermelho      →      0           1
```

## 4. Pipeline - Automatização do Preprocessamento

### Pipeline Simples
```python
from sklearn.pipeline import Pipeline

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression())
])

pipeline.fit(X_train, y_train)
predictions = pipeline.predict(X_test)
```

**Vantagens:**
- Automatiza sequência de transformações
- Evita data leakage
- Facilita validação cruzada
- Código mais limpo e reproduzível

### ColumnTransformer - Dados Mistos
```python
from sklearn.compose import ColumnTransformer

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), ['idade', 'salario']),
        ('cat', OneHotEncoder(drop='first'), ['departamento'])
    ]
)

pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression())
])
```

**Conceito-chave:** ColumnTransformer permite aplicar diferentes transformações a diferentes colunas simultaneamente.

## 5. Fluxo de Trabalho Completo

### Ordem Recomendada
1. **Divisão dos dados** (train_test_split)
2. **Fit no treino** (`scaler.fit(X_train)`)
3. **Transform em ambos** (`scaler.transform(X_train)` e `scaler.transform(X_test)`)
4. **Treinamento do modelo**
5. **Avaliação no teste**

### Exemplo Completo
```python
# 1. Divisão
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 2. Preprocessamento
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 3. Modelo
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# 4. Predição e avaliação
predictions = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, predictions)
```

## 6. Comparação de Impacto

### Performance com Diferentes Scalers
```python
# Sem preprocessing: accuracy = 0.8500
# Com MinMaxScaler: accuracy = 0.9000  
# Com StandardScaler: accuracy = 0.9100
```

**Observação:** O impacto varia por algoritmo:
- **Alta sensibilidade:** SVM, KNN, Regressão Logística, Redes Neurais
- **Baixa sensibilidade:** Árvores de Decisão, Random Forest

## Principais Conceitos Aprendidos

### Data Leakage Prevention
- **Correto:** `fit()` apenas no treino, `transform()` em ambos
- **Incorreto:** `fit_transform()` em todo o dataset

### Escolha do Scaler
- **MinMaxScaler:** Quando conhece o range dos dados
- **StandardScaler:** Para dados com distribuição normal
- **RobustScaler:** Para dados com outliers

### Dados Categóricos
- **LabelEncoder:** Para variáveis ordinais
- **OneHotEncoder:** Para variáveis nominais
- **drop='first':** Evita multicolinearidade

### Pipeline Benefits
- **Reprodutibilidade:** Mesmo fluxo sempre
- **Simplicidade:** Menos código, menos erros
- **Eficiência:** Otimização automática de transformações

## Erros Comuns a Evitar

1. **Fit nos dados de teste** → Data leakage
2. **Usar LabelEncoder em variáveis nominais** → Ordem artificial
3. **Esquecer de transformar dados novos** → Escalas diferentes
4. **Não usar random_state** → Resultados não reproduzíveis
5. **Aplicar scaling em variáveis categóricas** → Perde significado

**Lembrete:** O preprocessamento é tão importante quanto o modelo - dados bem preparados podem fazer a diferença entre um modelo medíocre e um excelente.
