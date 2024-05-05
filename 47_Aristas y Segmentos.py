import cv2

# Cargar una imagen
imagen = cv2.imread('imagen.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar el detector de bordes de Canny
bordes = cv2.Canny(imagen, 100, 200)

# Mostrar la imagen original y la imagen con los bordes detectados
cv2.imshow('Imagen original', imagen)
cv2.imshow('Bordes detectados', bordes)
cv2.waitKey(0)
cv2.destroyAllWindows()
