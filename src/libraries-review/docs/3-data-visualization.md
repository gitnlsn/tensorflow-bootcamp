# Matplotlib - Revisão da Biblioteca de Visualização

## Introdução
Matplotlib é a biblioteca principal para criação de gráficos e visualizações em Python, oferecendo controle total sobre todos os aspectos de um gráfico e suportando diversos formatos de saída.

## 1. Configuração Básica

### Importação e Setup
```python
import numpy as np
import matplotlib.pyplot as plt

# Para Jupyter Notebooks (exibe gráficos inline)
%matplotlib inline
```

### Primeiro Gráfico
```python
x = np.arange(0, 10)
y = x**2

plt.plot(x, y)
plt.title("Basic Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()  # Necessário em scripts Python
```

**Conceito-chave:** `plt.show()` é obrigatório em scripts Python para exibir o gráfico, mas opcional em Jupyter Notebooks.

## 2. Tipos de Gráficos Básicos

### Gráficos de Linha
```python
# Múltiplas linhas
plt.plot(x, y, 'r-', label='x²')        # Linha vermelha sólida
plt.plot(x, x*2, 'b--', label='2x')     # Linha azul tracejada
plt.legend()  # Mostra a legenda
```

### Gráficos de Dispersão (Scatter)
```python
plt.scatter(x, y, alpha=0.6, c='purple')
plt.title("Scatter Plot")
```

### Gráficos de Barras
```python
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 32]

bars = plt.bar(categories, values, color=['red', 'blue', 'green'])
plt.title("Bar Chart Example")
```

## 3. Estilos e Personalização

### Marcadores e Estilos de Linha
```python
# Diferentes estilos de linha
'r-'    # Linha vermelha sólida
'b--'   # Linha azul tracejada  
'go'    # Pontos verdes
'k:'    # Linha preta pontilhada
```

### Customização Avançada
```python
plt.plot(x_data, y1, 'r-', linewidth=2, label='sin(x)')
plt.title("Trigonometric Functions", fontsize=16)
plt.xlabel("X (radians)", fontsize=12)
plt.grid(True, alpha=0.3)  # Grade com transparência
```

## 4. Subplots - Múltiplos Gráficos

### Layout em Grade
```python
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)  # 1 linha, 2 colunas, posição 1
plt.plot(x, y, 'r-')
plt.title("First Plot")

plt.subplot(1, 2, 2)  # 1 linha, 2 colunas, posição 2
plt.plot(x, y, 'go')
plt.title("Second Plot")

plt.tight_layout()  # Ajusta espaçamento automático
```

### Método Orientado a Objetos
```python
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))

ax1.plot(x, y)
ax1.set_title("Line Plot")
ax1.grid(True)

ax2.scatter(x, y)
ax2.set_title("Scatter Plot")
```

## 5. Tipos de Gráficos Especializados

### Histogramas
```python
data = np.random.normal(100, 15, 1000)  # Distribuição normal

plt.hist(data, bins=30, edgecolor='black', alpha=0.7)
plt.axvline(data.mean(), color='red', linestyle='--', label=f'Mean: {data.mean():.2f}')
```

### Gráficos de Pizza
```python
sizes = [30, 25, 20, 25]
labels = ['A', 'B', 'C', 'D']
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
```

### Mapas de Calor (Heatmaps)
```python
data_matrix = np.random.randint(0, 100, (10, 10))
im = plt.imshow(data_matrix, cmap='viridis')
plt.colorbar(im)  # Adiciona barra de cores
```

## 6. Mapas de Cores (Colormaps)

### Colormaps Populares
```python
# Sequenciais
'viridis', 'plasma', 'coolwarm', 'hot'

# Divergentes  
'RdYlBu', 'seismic'

# Uso
plt.imshow(data, cmap='plasma')
```

## 7. Gráficos Avançados

### Gráficos de Contorno
```python
X, Y = np.meshgrid(x_data, y_data)
Z = np.sin(np.sqrt(X**2 + Y**2))

contour = plt.contourf(X, Y, Z, levels=20, cmap='plasma')
plt.colorbar(contour)
```

### Preenchimento de Área
```python
x = np.linspace(0, 4*np.pi, 200)
y = np.exp(-x/8) * np.sin(x)

plt.plot(x, y, linewidth=3)
plt.fill_between(x, y, alpha=0.3)  # Preenche área sob a curva
```

## 8. Anotações e Texto

### Adicionando Texto aos Gráficos
```python
# Texto em posição específica
plt.text(x_pos, y_pos, 'Texto', fontsize=12)

# Anotação com seta
plt.annotate('Ponto máximo', xy=(x_max, y_max), xytext=(x_text, y_text),
             arrowprops=dict(arrowstyle='->'))

# Texto nas barras
for bar, value in zip(bars, values):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
             str(value), ha='center', va='bottom')
```

## 9. Configurações de Figura

### Tamanho e Resolução
```python
plt.figure(figsize=(10, 6))  # Largura x Altura em polegadas
plt.figure(dpi=150)          # Resolução (dots per inch)
```

### Salvando Gráficos
```python
plt.savefig('grafico.png', dpi=300, bbox_inches='tight')
plt.savefig('grafico.pdf')  # Formato vetorial
```

## 10. Boas Práticas e Dicas

### Clareza e Legibilidade
- **Use títulos descritivos** e rótulos nos eixos
- **Adicione legendas** quando há múltiplas séries
- **Configure a grade** para facilitar leitura: `plt.grid(True, alpha=0.3)`
- **Ajuste o tamanho da fonte** para melhor visualização

### Performance
- **Use `plt.tight_layout()`** para ajustar espaçamento automaticamente
- **Configure `figsize`** adequadamente para sua aplicação
- **Use transparência (`alpha`)** para sobrepor dados sem perder informação

### Reprodutibilidade
```python
np.random.seed(42)  # Garante resultados consistentes com dados aleatórios
```

## Principais Vantagens do Matplotlib

1. **Controle Total:** Personalização completa de todos os elementos visuais
2. **Formatos Múltiplos:** Saída para PNG, PDF, SVG, EPS e outros formatos
3. **Integração:** Funciona perfeitamente com NumPy e Pandas
4. **Flexibilidade:** Interface simples (`pyplot`) e orientada a objetos disponíveis
5. **Extensibilidade:** Base para outras bibliotecas como Seaborn

## Conceitos Fundamentais Aprendidos

- **Interface Pyplot:** Simplifica criação de gráficos com estilo MATLAB
- **Figure e Axes:** Estrutura hierárquica dos elementos gráficos
- **Subplots:** Organização de múltiplos gráficos em layouts estruturados
- **Colormaps:** Mapeamento de dados para cores em visualizações 2D
- **Personalização:** Controle fino sobre aparência e estilo dos gráficos
- **Formatos de Saída:** Versatilidade para diferentes meios de publicação
