# NumPy - Revisão da Biblioteca

## Introdução
NumPy é a biblioteca fundamental para computação científica em Python, fornecendo arrays multidimensionais eficientes e operações matemáticas otimizadas.

## 1. Criação de Arrays

### Arrays Básicos
```python
import numpy as np

# Criando array a partir de lista
arr = np.array([0,1,2,3,4])
my_list = [0,1,2,3,4]
arr = np.array(my_list)
```

### Funções de Geração
```python
# Sequências numéricas
np.arange(0,10)      # [0,1,2,3,4,5,6,7,8,9]
np.arange(0,10,2)    # [0,2,4,6,8] com step=2

# Espaçamento linear
np.linspace(0,10,6)  # 6 pontos igualmente espaçados entre 0 e 10
np.linspace(0,10,101) # 101 pontos para maior precisão
```

### Arrays Especiais
```python
# Matrizes de zeros e uns
np.zeros((5,5))      # Matriz 5x5 preenchida com zeros
np.ones((2,4))       # Matriz 2x4 preenchida com uns

# Números aleatórios
np.random.randint(0,10)        # Um inteiro aleatório entre 0-9
np.random.randint(0,10,(3,3))  # Matriz 3x3 com inteiros aleatórios
```

**Conceito-chave:** `np.random.seed(101)` garante reprodutibilidade dos números aleatórios.

## 2. Operações Estatísticas

### Funções Básicas
```python
arr = np.random.randint(0,100,10)

# Valores estatísticos
arr.max()   # Valor máximo
arr.min()   # Valor mínimo  
arr.mean()  # Média aritmética

# Índices de extremos
arr.argmin()  # Índice do valor mínimo
arr.argmax()  # Índice do valor máximo
```

**Diferença importante:** 
- `max()` retorna o **valor** máximo
- `argmax()` retorna o **índice** onde está o valor máximo

### Reshape - Modificando Dimensões
```python
arr.reshape(2,5)  # Transforma array 1D(10) em matriz 2D(2x5)
```

## 3. Indexação e Slicing

### Criando Matriz de Exemplo
```python
mat = np.arange(0,100).reshape(10,10)  # Matriz 10x10 com valores 0-99
```

### Acessando Elementos
```python
# Elemento específico
mat[row,col]    # Elemento na linha 'row', coluna 'col'

# Linhas e colunas completas
mat[:,col]      # Coluna inteira
mat[row,:]      # Linha inteira

# Submatrizes
mat[0:3,0:3]    # Submatriz 3x3 do canto superior esquerdo
```

## 4. Mascaramento (Boolean Indexing)

### Criando Máscaras Booleanas
```python
mask = mat > 50  # Cria array booleano: True onde mat > 50, False caso contrário
```

### Filtragem com Máscaras
```python
filtered = mat[mat>50]  # Retorna apenas elementos maiores que 50
```

**Conceito-chave:** O mascaramento permite filtrar dados baseado em condições lógicas, retornando um array 1D com os elementos que atendem à condição.

## Principais Vantagens do NumPy

1. **Performance:** Arrays NumPy são implementados em C, sendo muito mais rápidos que listas Python
2. **Operações Vetorizadas:** Aplica operações em arrays inteiros sem loops explícitos
3. **Broadcasting:** Permite operações entre arrays de diferentes dimensões
4. **Integração:** Base para outras bibliotecas científicas (Pandas, Matplotlib, Scikit-learn)

## Conceitos Fundamentais Aprendidos

- **Array vs Lista:** Arrays NumPy são homogêneos e otimizados
- **Indexação Multidimensional:** Sintaxe `[linha, coluna]` para matrizes
- **Reprodutibilidade:** Uso de `seed()` para resultados consistentes
- **Reshape:** Modificação de dimensões preservando os dados
- **Mascaramento:** Filtragem eficiente baseada em condições booleanas
