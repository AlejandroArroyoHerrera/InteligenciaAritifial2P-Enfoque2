import numpy as np
import matplotlib.pyplot as plt

# Definici�n del entorno y par�metros del robot
num_estados = 10
posicion_real = 7
num_particulas = 1000

# Generar part�culas inicialmente uniformemente distribuidas
particulas = np.random.choice(np.arange(num_estados), size=num_particulas)

# Funci�n de transici�n del estado del robot
def transicion_estado(posicion_actual):
    return np.random.choice([posicion_actual-1, posicion_actual, posicion_actual+1], p=[0.1, 0.8, 0.1])

# Funci�n de observaci�n del robot
def observacion(posicion):
    return np.random.normal(loc=posicion, scale=0.5)

# Actualizaci�n de las part�culas basada en la transici�n del estado
def actualizar_particulas():
    for i in range(num_particulas):
        particulas[i] = transicion_estado(particulas[i])

# Peso de cada part�cula basado en la observaci�n
def calcular_pesos(observacion_real):
    pesos = np.zeros(num_particulas)
    for i in range(num_particulas):
        observacion_predicha = observacion(particulas[i])
        probabilidad = np.exp(-0.5 * (observacion_predicha - observacion_real)**2)
        pesos[i] = probabilidad
    pesos /= np.sum(pesos)
    return pesos

# Remuestreo de part�culas basado en los pesos
def remuestreo(pesos):
    indices = np.random.choice(np.arange(num_particulas), size=num_particulas, p=pesos)
    return indices

# Filtrado de part�culas
num_iteraciones = 10
for _ in range(num_iteraciones):
    actualizar_particulas()
    observacion_real = observacion(posicion_real)
    pesos = calcular_pesos(observacion_real)
    indices_remuestreo = remuestreo(pesos)
    particulas = particulas[indices_remuestreo]

# Visualizaci�n de la distribuci�n final de part�culas
plt.hist(particulas, bins=np.arange(num_estados+1)-0.5, density=True, alpha=0.5, color='b')
plt.axvline(x=posicion_real, color='r', linestyle='--', label='Posicion Real')
plt.xlabel('Posicion del Robot')
plt.ylabel('Densidad de Particulas')
plt.title('Filtrado de Part�culas para Localizacion de un Robot')
plt.legend()
plt.grid(True)
plt.show()
