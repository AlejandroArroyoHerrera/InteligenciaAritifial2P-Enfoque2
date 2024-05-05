import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.utils import to_categorical

# Cargar el conjunto de datos MNIST de dígitos escritos a mano
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Normalizar los valores de píxeles entre 0 y 1
X_train = X_train / 255.0
X_test = X_test / 255.0

# Codificar las etiquetas como vectores one-hot
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# Construir el modelo de red neuronal convolucional
modelo = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])

# Compilar y entrenar el modelo
modelo.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
modelo.fit(X_train.reshape(-1, 28, 28, 1), y_train, epochs=5, batch_size=32, validation_split=0.2)

# Evaluar el modelo con los datos de prueba
loss, accuracy = modelo.evaluate(X_test.reshape(-1, 28, 28, 1), y_test)
print(f'Precision en los datos de prueba: {accuracy}')
