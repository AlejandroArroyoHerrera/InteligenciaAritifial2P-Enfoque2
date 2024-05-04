import numpy as np
import matplotlib.pyplot as plt

# Definimos la matriz de transición de probabilidades
matriz_transicion = np.array([[0.8, 0.2],  # Probabilidad de pasar de A a A y de A a B
                               [0.4, 0.6]]) # Probabilidad de pasar de B a A y de B a B

# Definimos los estados posibles
estados = ['A', 'B']

# Configuración inicial
estado_actual = 'A'
longitud = 100

# Generamos la secuencia de estados utilizando el proceso de Markov
secuencia_estados = [estado_actual]
for _ in range(longitud - 1):
    estado_siguiente = np.random.choice(estados, p=matriz_transicion[estados.index(estado_actual)])
    secuencia_estados.append(estado_siguiente)
    estado_actual = estado_siguiente

# Graficamos la secuencia de estados
plt.figure(figsize=(10, 4))
plt.plot(range(longitud), secuencia_estados, marker='o', linestyle='-', color='b')
plt.xlabel('Tiempo')
plt.ylabel('Estado')
plt.title('Proceso de Markov de Orden 1')
plt.yticks(range(len(estados)), estados)
plt.grid(True)
plt.show()
