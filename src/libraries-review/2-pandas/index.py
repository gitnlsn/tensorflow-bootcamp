import pandas as pd

print("=== Lendo Dados ===")
df = pd.read_csv('src/libraries-review/resources/salaries.csv')
print("DataFrame original:")
print(df)

print("\n=== Seleção de Colunas ===")
print("df['Name']:")
print(df['Name'])

print("\ndf['Salary']:")
print(df['Salary'])

print("\nMúltiplas colunas df[['Name','Salary']]:")
print(df[['Name','Salary']])

print("\n=== Operações Estatísticas ===")
print("df['Age'].mean():", df['Age'].mean())
print("df['Salary'].max():", df['Salary'].max())
print("df['Salary'].min():", df['Salary'].min())
print("df['Age'].sum():", df['Age'].sum())

print("\n=== Info do DataFrame ===")
print("df.shape:", df.shape)
print("df.columns:", list(df.columns))
print("df.dtypes:")
print(df.dtypes)

print("\n=== Filtragem com Condições ===")
age_filter = df['Age'] > 30
print("df['Age'] > 30:")
print(age_filter)

print("\nPessoas com idade > 30:")
print(df[age_filter])

print("\nFiltro direto df[df['Age'] > 30]:")
print(df[df['Age'] > 30])

print("\nPessoas com salário >= 80000:")
print(df[df['Salary'] >= 80000])

print("\n=== Criando Novos DataFrames ===")
data = {
    'Produto': ['Notebook', 'Mouse', 'Teclado'],
    'Preco': [2500, 50, 150],
    'Categoria': ['Eletrônicos', 'Acessórios', 'Acessórios']
}
df_produtos = pd.DataFrame(data)
print("Novo DataFrame criado:")
print(df_produtos)

print("\n=== Operações com Grupos ===")
print("Média de preço por categoria:")
print(df_produtos.groupby('Categoria')['Preco'].mean())

print("\n=== Adicionando Colunas ===")
df_copy = df.copy()
df_copy['Bonus'] = df_copy['Salary'] * 0.1
print("DataFrame com coluna Bonus:")
print(df_copy)

print("\n=== Ordenação ===")
print("Ordenado por Salary (crescente):")
print(df.sort_values('Salary'))

print("\nOrdenado por Age (decrescente):")
print(df.sort_values('Age', ascending=False))
