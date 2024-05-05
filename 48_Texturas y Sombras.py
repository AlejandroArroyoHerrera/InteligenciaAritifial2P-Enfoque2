import cv2
import numpy as np

# Cargar una imagen en escala de grises
imagen = cv2.imread('imagen.jpg', cv2.IMREAD_GRAYSCALE)

# Calcular la matriz de co-ocurrencia de Haralick
textura = cv2.Haralick(imagen).mean(axis=0)

# Mostrar las características de textura calculadas
print("Caracteristicas de textura:")
print(textura)
