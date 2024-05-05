import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Funci�n para calcular las posiciones posibles del brazo en funci�n de los �ngulos de las articulaciones
def calcular_posiciones(angulo_1, angulo_2):
    # Longitudes de los segmentos del brazo
    l1 = 1
    l2 = 1.5
    # Calcular las posiciones en funci�n de los �ngulos
    x = l1 * np.cos(angulo_1) + l2 * np.cos(angulo_1 + angulo_2)
    y = l1 * np.sin(angulo_1) + l2 * np.sin(angulo_1 + angulo_2)
    return x, y

# �ngulos de las articulaciones para explorar el espacio de configuraci�n
angulos_1 = np.linspace(0, 2*np.pi, 50)
angulos_2 = np.linspace(0, 2*np.pi, 50)

# Crear un gr�fico 3D para mostrar las posiciones en el espacio de configuraci�n
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
for angulo_1 in angulos_1:
    for angulo_2 in angulos_2:
        x, y = calcular_posiciones(angulo_1, angulo_2)
        ax.scatter(x, y, angulo_1 + angulo_2, c='b')
ax.set_title('Espacio de Configuracion para un Brazo Robotico de 2 Grados de Libertad')
ax.set_xlabel('Posici�n en X')
ax.set_ylabel('Posici�n en Y')
ax.set_zlabel('�ngulo 1 + �ngulo 2')
plt.show()
