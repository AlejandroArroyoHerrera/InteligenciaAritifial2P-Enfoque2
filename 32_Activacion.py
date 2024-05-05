# Importamos las bibliotecas necesarias
import numpy as np

# Definimos la función de activación sigmoide
def sigmoide(x):
    return 1 / (1 + np.exp(-x))

# Creamos una red neuronal de retroalimentación (feedback) con una sola neurona
def red_neuronal_retroalimentacion(x, peso, sesgo):
    # Calculamos la salida de la neurona
    salida = sigmoide(np.dot(x, peso) + sesgo)
    return salida

# Entrada de ejemplo
entrada = np.array([0.7, 0.2])

# Pesos y sesgo de la neurona
peso = np.array([0.5, 0.3])
sesgo = np.array([0.1])

# Obtenemos la salida de la red neuronal
salida_red = red_neuronal_retroalimentacion(entrada, peso, sesgo)
print("Salida de la red neuronal de retroalimentacion:", salida_red)
