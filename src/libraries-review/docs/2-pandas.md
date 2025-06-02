# Pandas - Revisão da Biblioteca

## Introdução
Pandas é a biblioteca essencial para manipulação e análise de dados em Python, fornecendo estruturas de dados flexíveis como DataFrame e Series, ideais para trabalhar com dados tabulares.

## 1. Lendo e Criando DataFrames

### Lendo Dados de Arquivo
```python
import pandas as pd

# Carregando dados de CSV
df = pd.read_csv('salaries.csv')
```

### Criando DataFrames Manualmente
```python
data = {
    'Produto': ['Notebook', 'Mouse', 'Teclado'],
    'Preco': [2500, 50, 150],
    'Categoria': ['Eletrônicos', 'Acessórios', 'Acessórios']
}
df_produtos = pd.DataFrame(data)
```

**Conceito-chave:** DataFrame é uma estrutura de dados 2D com rótulos nas linhas e colunas, similar a uma planilha Excel.

## 2. Seleção de Dados

### Selecionando Colunas
```python
# Uma coluna (retorna Series)
df['Name']

# Múltiplas colunas (retorna DataFrame)
df[['Name','Salary']]
```

### Informações do DataFrame
```python
df.shape       # Dimensões (linhas, colunas)
df.columns     # Nomes das colunas
df.dtypes      # Tipos de dados de cada coluna
```

**Diferença importante:**
- `df['coluna']` retorna uma **Series** (1D)
- `df[['coluna']]` retorna um **DataFrame** (2D)

## 3. Operações Estatísticas

### Funções Agregadas
```python
# Estatísticas básicas
df['Age'].mean()    # Média
df['Salary'].max()  # Valor máximo
df['Salary'].min()  # Valor mínimo
df['Age'].sum()     # Soma total
```

### Agrupamento de Dados
```python
# Operações por grupo
df.groupby('Categoria')['Preco'].mean()  # Média de preço por categoria
```

**Conceito-chave:** `groupby()` permite agrupar dados por uma ou mais colunas e aplicar funções agregadas.

## 4. Filtragem de Dados

### Criando Filtros Booleanos
```python
age_filter = df['Age'] > 30  # Cria Series booleana
```

### Aplicando Filtros
```python
# Usando variável de filtro
df[age_filter]

# Filtro direto
df[df['Age'] > 30]
df[df['Salary'] >= 80000]
```

**Conceito-chave:** A filtragem em pandas usa indexação booleana similar ao NumPy, mas trabalha com DataFrames estruturados.

## 5. Manipulação de DataFrames

### Adicionando Colunas
```python
df_copy = df.copy()
df_copy['Bonus'] = df_copy['Salary'] * 0.1  # Nova coluna baseada em cálculo
```

### Ordenação
```python
# Ordenação crescente
df.sort_values('Salary')

# Ordenação decrescente
df.sort_values('Age', ascending=False)
```

**Conceito-chave:** `copy()` cria uma cópia independente do DataFrame, evitando modificações no original.

## 6. Estruturas de Dados Pandas

### DataFrame vs Series
- **DataFrame:** Estrutura 2D (tabela) com linhas e colunas rotuladas
- **Series:** Estrutura 1D (vetor) com índices rotulados

### Relação com NumPy
```python
# Pandas é construído sobre NumPy
df.values  # Retorna array NumPy subjacente
```

## Principais Vantagens do Pandas

1. **Manipulação Intuitiva:** Interface similar a SQL e Excel para dados tabulares
2. **Leitura de Arquivos:** Suporte nativo para CSV, Excel, JSON, SQL, etc.
3. **Dados Heterogêneos:** Colunas podem ter tipos diferentes (strings, números, datas)
4. **Indexação Flexível:** Índices personalizados e hierárquicos
5. **Tratamento de Dados Ausentes:** Funcionalidades para lidar com valores NaN

## Conceitos Fundamentais Aprendidos

- **DataFrame vs Series:** Estruturas 2D vs 1D para dados tabulares
- **Seleção de Dados:** Diferença entre `[]` e `[[]]` para colunas
- **Filtragem Booleana:** Uso de condições lógicas para filtrar linhas
- **Agrupamento:** `groupby()` para análises por categorias
- **Imutabilidade:** Uso de `copy()` para modificações seguras
- **Integração:** Pandas + NumPy para análise completa de dados

## Workflow Típico com Pandas

1. **Carregar:** `pd.read_csv()` ou `pd.DataFrame()`
2. **Explorar:** `.shape`, `.dtypes`, `.head()`
3. **Filtrar:** `df[condição]`
4. **Agrupar:** `.groupby().agg()`
5. **Transformar:** Criar novas colunas
6. **Analisar:** Estatísticas e visualizações
