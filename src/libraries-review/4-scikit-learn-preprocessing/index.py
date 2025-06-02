import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

print("=== Criando Dataset de Exemplo ===")
np.random.seed(42)
X, y = make_classification(n_samples=100, n_features=3, n_redundant=0, n_informative=3, 
                          n_clusters_per_class=1, random_state=42)

data = pd.DataFrame(X, columns=['feature1', 'feature2', 'feature3'])
data['target'] = y

print("Dataset original:")
print(data.head())
print(f"Shape: {data.shape}")
print(f"Estatísticas:\n{data.describe()}")

print("\n=== Divisão Treino/Teste ===")
X = data[['feature1', 'feature2', 'feature3']]
y = data['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

print(f"X_train shape: {X_train.shape}")
print(f"X_test shape: {X_test.shape}")
print(f"y_train shape: {y_train.shape}")
print(f"y_test shape: {y_test.shape}")

print("\n=== MinMaxScaler - Normalização [0,1] ===")
minmax_scaler = MinMaxScaler()

X_train_minmax = minmax_scaler.fit_transform(X_train)
X_test_minmax = minmax_scaler.transform(X_test)

print("Dados originais (primeiras 5 amostras):")
print(X_train.head())
print("\nDados normalizados MinMax (primeiras 5 amostras):")
print(pd.DataFrame(X_train_minmax, columns=X.columns).head())

print(f"\nRange original - Min: {X_train.min().min():.2f}, Max: {X_train.max().max():.2f}")
print(f"Range MinMax - Min: {X_train_minmax.min():.2f}, Max: {X_train_minmax.max():.2f}")

print("\n=== StandardScaler - Padronização (Z-score) ===")
std_scaler = StandardScaler()

X_train_std = std_scaler.fit_transform(X_train)
X_test_std = std_scaler.transform(X_test)

print("Dados padronizados Standard (primeiras 5 amostras):")
print(pd.DataFrame(X_train_std, columns=X.columns).head())

print(f"\nMédia após StandardScaler: {X_train_std.mean(axis=0)}")
print(f"Desvio padrão após StandardScaler: {X_train_std.std(axis=0)}")

print("\n=== Comparação de Performance ===")
print("Sem preprocessamento:")
model_raw = LogisticRegression(random_state=42, max_iter=1000)
model_raw.fit(X_train, y_train)
y_pred_raw = model_raw.predict(X_test)
acc_raw = accuracy_score(y_test, y_pred_raw)
print(f"Acurácia: {acc_raw:.4f}")

print("\nCom MinMaxScaler:")
model_minmax = LogisticRegression(random_state=42, max_iter=1000)
model_minmax.fit(X_train_minmax, y_train)
y_pred_minmax = model_minmax.predict(X_test_minmax)
acc_minmax = accuracy_score(y_test, y_pred_minmax)
print(f"Acurácia: {acc_minmax:.4f}")

print("\nCom StandardScaler:")
model_std = LogisticRegression(random_state=42, max_iter=1000)
model_std.fit(X_train_std, y_train)
y_pred_std = model_std.predict(X_test_std)
acc_std = accuracy_score(y_test, y_pred_std)
print(f"Acurácia: {acc_std:.4f}")

print("\n=== Preprocessamento de Dados Categóricos ===")
categorias = pd.DataFrame({
    'cor': ['azul', 'verde', 'azul', 'vermelho', 'verde', 'azul'],
    'tamanho': ['P', 'M', 'G', 'P', 'G', 'M'],
    'preco': [100, 150, 200, 80, 180, 120]
})
print("Dataset categórico:")
print(categorias)

print("\n=== LabelEncoder - Codificação Ordinal ===")
label_encoder = LabelEncoder()

categorias_encoded = categorias.copy()
categorias_encoded['cor_encoded'] = label_encoder.fit_transform(categorias['cor'])

print("Mapeamento de cores:")
for i, cor in enumerate(label_encoder.classes_):
    print(f"{cor}: {i}")

print("\nDataset com LabelEncoder:")
print(categorias_encoded)

print("\n=== OneHotEncoder - Codificação Dummy ===")
onehot_encoder = OneHotEncoder(sparse_output=False, drop='first')

cor_onehot = onehot_encoder.fit_transform(categorias[['cor']])
feature_names = onehot_encoder.get_feature_names_out(['cor'])

onehot_df = pd.DataFrame(cor_onehot, columns=feature_names)
print("OneHotEncoder para 'cor':")
print(onehot_df)

print("\n=== Pipeline Completo ===")
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

dados_mistos = pd.DataFrame({
    'idade': [25, 30, 35, 28, 32],
    'salario': [50000, 60000, 70000, 55000, 65000],
    'departamento': ['TI', 'RH', 'TI', 'Vendas', 'RH'],
    'aprovado': [1, 0, 1, 0, 1]
})

print("Dataset com dados mistos:")
print(dados_mistos)

numeric_features = ['idade', 'salario']
categorical_features = ['departamento']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(drop='first'), categorical_features)
    ]
)

pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression(random_state=42))
])

X_mixed = dados_mistos[['idade', 'salario', 'departamento']]
y_mixed = dados_mistos['aprovado']

print("\nTreinando pipeline com dados mistos...")
pipeline.fit(X_mixed, y_mixed)

print("Pipeline treinado com sucesso!")
print("Componentes do pipeline:")
print("1. Preprocessor (StandardScaler + OneHotEncoder)")
print("2. Classifier (LogisticRegression)")
