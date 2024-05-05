import cv2
import numpy as np

# Cargar una imagen en escala de grises
imagen = cv2.imread('imagen.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar detección de bordes usando Canny
bordes = cv2.Canny(imagen, 50, 150)

# Encontrar contornos en la imagen
contornos, _ = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar los contornos en la imagen original
cv2.drawContours(imagen, contornos, -1, (0, 255, 0), 2)

# Mostrar la imagen con los contornos detectados
cv2.imshow('Contornos detectados', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
