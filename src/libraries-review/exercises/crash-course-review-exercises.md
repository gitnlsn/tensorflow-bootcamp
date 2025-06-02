# Exercícios de Revisão do Crash Course

Este documento contém uma série de exercícios para revisar conceitos fundamentais de Python, NumPy, Pandas, Matplotlib e Scikit-learn.

## Objetivos
Praticar as bibliotecas essenciais para ciência de dados e machine learning através de exercícios práticos.

## Exercícios Propostos

### 1. Importação de Bibliotecas
**Tarefa:** Importe numpy, pandas, matplotlib e sklearn. Configure também as visualizações para serem mostradas inline no notebook.

**Bibliotecas necessárias:**
- numpy
- pandas 
- matplotlib.pyplot
- sklearn.preprocessing.MinMaxScaler

**Dica:** Use `%matplotlib inline` para visualizações inline.

### 2. Configuração de Seed
**Tarefa:** Configure o Random Seed do NumPy para 101.

**Objetivo:** Garantir reprodutibilidade dos resultados aleatórios.

### 3. Criação de Matriz NumPy
**Tarefa:** Crie uma matriz NumPy de 100 linhas por 5 colunas contendo números inteiros aleatórios de 1 a 100.

**Observações:**
- Lembre-se de que o limite superior pode ser exclusivo
- Use a função `np.random.randint()`

### 4. Visualização 2D com imshow
**Tarefa:** Crie uma visualização 2D usando `plt.imshow()` da matriz numpy com uma barra de cores. Adicione um título ao seu gráfico.

**Bonus:** Descubra como alterar o aspecto (`aspect`) do gráfico imshow().

**Dicas:**
- Use `plt.colorbar()` para adicionar a barra de cores
- Use `plt.title()` para adicionar o título
- Explore o parâmetro `aspect` do `plt.imshow()`

### 5. Conversão para DataFrame
**Tarefa:** Use `pd.DataFrame()` para converter a matriz numpy em um dataframe. Simplesmente passe a matriz numpy para a função para obter um dataframe. O Pandas irá automaticamente rotular as colunas de 0 a 4.

### 6. Gráfico de Dispersão
**Tarefa:** Crie um gráfico de dispersão (scatter plot) usando pandas da coluna 0 versus a coluna 1.

**Dica:** Use o método `.plot()` do pandas com `kind='scatter'`.

### 7. Normalização dos Dados
**Tarefa:** Normalize os dados para ter um valor mínimo de 0 e um valor máximo de 1 usando scikit-learn.

**Ferramenta:** Use `MinMaxScaler` do sklearn.preprocessing.

**Passos:**
1. Instancie o scaler
2. Use `fit_transform()` nos dados

### 8. Renomeação de Colunas e Train/Test Split
**Tarefa:** Usando o DataFrame criado anteriormente, use `df.columns = [...]` para renomear as colunas do pandas para ['f1','f2','f3','f4','label']. Em seguida, execute um train/test split com scikit-learn.

**Passos:**
1. Renomeie as colunas do DataFrame
2. Separe features (X) e target (y)
3. Use `train_test_split` do sklearn.model_selection

## Resultados Esperados

Ao completar todos os exercícios, você deve ter:

1. ✅ Bibliotecas importadas corretamente
2. ✅ Seed configurado para reprodutibilidade
3. ✅ Matriz 100x5 de números aleatórios criada
4. ✅ Visualização 2D com mapa de calor
5. ✅ DataFrame pandas criado
6. ✅ Gráfico de dispersão gerado
7. ✅ Dados normalizados entre 0 e 1
8. ✅ Colunas renomeadas e dados divididos em treino/teste

## Conceitos Praticados

- **NumPy:** Criação de arrays, números aleatórios, manipulação de dados
- **Pandas:** DataFrames, renomeação de colunas, plotting
- **Matplotlib:** Visualizações 2D, customização de gráficos
- **Scikit-learn:** Normalização de dados, divisão treino/teste
- **Jupyter:** Configuração de ambiente, visualizações inline

## Dicas Adicionais

- Sempre verifique a forma (shape) dos seus arrays e DataFrames
- Use `df.head()` e `df.info()` para explorar os dados
- Documente seu código com comentários explicativos
- Teste cada passo antes de prosseguir para o próximo

---

**Fonte:** Baseado nos exercícios do Crash Course Review do TensorFlow Bootcamp 