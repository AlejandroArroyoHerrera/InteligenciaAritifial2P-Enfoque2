# Importamos las bibliotecas necesarias
import tensorflow as tf
from tensorflow.keras import layers, models

# Definimos la arquitectura de la red neuronal convolutiva (CNN)
modelo = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)), # Capa convolucional con 32 filtros de 3x3
    layers.MaxPooling2D((2, 2)),  # Capa de agrupación máxima
    layers.Conv2D(64, (3, 3), activation='relu'), # Segunda capa convolucional con 64 filtros de 3x3
    layers.MaxPooling2D((2, 2)),  # Segunda capa de agrupación máxima
    layers.Conv2D(64, (3, 3), activation='relu'), # Tercera capa convolucional con 64 filtros de 3x3
    layers.Flatten(),  # Capa de aplanamiento
    layers.Dense(64, activation='relu'),  # Capa completamente conectada con 64 neuronas y activación ReLU
    layers.Dense(10, activation='softmax') # Capa de salida con 10 neuronas (una para cada clase) y activación softmax
])

# Compilamos el modelo
modelo.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Cargamos y preprocesamos los datos de MNIST
(x_entrenamiento, y_entrenamiento), (x_prueba, y_prueba) = tf.keras.datasets.mnist.load_data()
x_entrenamiento = x_entrenamiento.reshape((x_entrenamiento.shape[0], 28, 28, 1))
x_entrenamiento = x_entrenamiento.astype('float32') / 255

x_prueba = x_prueba.reshape((x_prueba.shape[0], 28, 28, 1))
x_prueba = x_prueba.astype('float32') / 255

# Entrenamos el modelo
modelo.fit(x_entrenamiento, y_entrenamiento, epochs=5)

# Evaluamos el modelo
puntuacion = modelo.evaluate(x_prueba, y_prueba)
print("Precision en prueba:", puntuacion[1])
