import numpy as np
from tensorflow import keras
from tensorflow.keras import layers

# Generamos datos de entrada y salida para la regresión
x = np.random.rand(100, 1)  # Entradas (100 muestras de una dimensión)
y = 2 * x + 1 + np.random.randn(100, 1) * 0.1  # Salidas (linealmente relacionadas con x con ruido)

# Definimos la arquitectura de la red neuronal
modelo = keras.Sequential([
    layers.Dense(10, activation='relu', input_shape=(1,)),  # Capa oculta con 10 neuronas y activación ReLU
    layers.Dense(1)  # Capa de salida con una neurona (regresión lineal)
])

# Compilamos el modelo
modelo.compile(optimizer='adam', loss='mean_squared_error')

# Entrenamos el modelo
modelo.fit(x, y, epochs=50, verbose=0)

# Evaluamos el modelo
puntuacion = modelo.evaluate(x, y)
print("Error cuadratico medio:", puntuacion)
