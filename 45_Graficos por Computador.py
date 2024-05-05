import cv2
import numpy as np

# Cargar una imagen
imagen = cv2.imread('imagen.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar el operador de Sobel en x
sobelx = cv2.Sobel(imagen, cv2.CV_64F, 1, 0, ksize=5)

# Aplicar el operador de Sobel en y
sobely = cv2.Sobel(imagen, cv2.CV_64F, 0, 1, ksize=5)

# Calcular la magnitud de los gradientes
magnitud = np.sqrt(sobelx**2 + sobely**2)

# Mostrar la imagen original y la imagen con los bordes detectados
cv2.imshow('Imagen original', imagen)
cv2.imshow('Bordes', magnitud)
cv2.waitKey(0)
cv2.destroyAllWindows()
