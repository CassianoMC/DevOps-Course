# Importar Bibliotecas e carregar os dados
import tensorflow as tf
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Carregar conjunto de dados Iris
iris = load_iris()
X = iris.data
y = iris.target

#Dividir o conjunto de dados em treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizar os dados
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Construir o Modelo
modelo =tf.keras.models.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(4,)),
    tf.keras.layers.Dense(3, activation='softmax')
])

# Compilar o modelo
modelo.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Treinar o modelo
print("\nA iniciar o treino do modelo...")
modelo.fit(X_train, y_train, epochs=50, batch_size=5)

# Avaliar o modelo --> avaliar a precisão do modelo usando os dados dos testes.
print("\nAvaliação do Modelo: ")
loss, accuracy = modelo.evaluate(X_test, y_test)
print(f"Precisão do Modelo nos dados de teste: {accuracy * 100:.2f}%")

# Fazer previsões
print("\nRealizando Previsões: ")
previsoes = modelo.predict(X_test)
print("Previsões para as 5 primeiras amostras de teste (probabilidade de cada espécie): ")
print(previsoes[:5])