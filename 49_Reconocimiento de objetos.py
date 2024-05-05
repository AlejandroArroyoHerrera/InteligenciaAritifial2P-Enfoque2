import cv2
import tensorflow as tf

# Cargar el modelo pre-entrenado de TensorFlow
modelo = tf.keras.applications.MobileNetV2(weights='imagenet')

# Cargar una imagen
imagen = cv2.imread('imagen.jpg')
imagen = cv2.resize(imagen, (224, 224))

# Preprocesar la imagen para que coincida con el formato del modelo
imagen = tf.keras.applications.mobilenet_v2.preprocess_input(imagen)

# Realizar la predicción de objetos en la imagen
predicciones = modelo.predict(tf.expand_dims(imagen, axis=0))

# Decodificar las predicciones para obtener las etiquetas de los objetos reconocidos
etiquetas = tf.keras.applications.mobilenet_v2.decode_predictions(predicciones)

# Mostrar las etiquetas de los objetos reconocidos
for etiqueta in etiquetas[0]:
    print(f'{etiqueta[1]}: {etiqueta[2]*100:.2f}%')

