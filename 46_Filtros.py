import cv2
import numpy as np

# Cargar una imagen
imagen = cv2.imread('imagen.jpg')

# Aplicar un filtro de media para suavizar la imagen
filtro_suavizado = cv2.blur(imagen, (5, 5))

# Mostrar la imagen original y la imagen suavizada
cv2.imshow('Imagen original', imagen)
cv2.imshow('Suavizado', filtro_suavizado)
cv2.waitKey(0)
cv2.destroyAllWindows()
