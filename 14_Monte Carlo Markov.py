import numpy as np

# Definimos la distribución de probabilidad discreta objetivo
distribucion_objetivo = {0: 0.2, 1: 0.4, 2: 0.3, 3: 0.1}

# Función para calcular la probabilidad de aceptación según el algoritmo Metropolis-Hastings
def probabilidad_aceptacion(actual, propuesto):
    return min(1, distribucion_objetivo[propuesto] / distribucion_objetivo[actual])

# Función para realizar un paso del algoritmo Metropolis-Hastings
def paso_metropolis_hastings(actual):
    propuesto = np.random.choice(list(distribucion_objetivo.keys()))
    if np.random.rand() < probabilidad_aceptacion(actual, propuesto):
        return propuesto
    else:
        return actual

# Configuración inicial
estado_actual = np.random.choice(list(distribucion_objetivo.keys()))

# Realizamos 1000 pasos del algoritmo Metropolis-Hastings
muestras = [estado_actual]
for _ in range(1000):
    estado_actual = paso_metropolis_hastings(estado_actual)
    muestras.append(estado_actual)

# Contamos la frecuencia de cada muestra
frecuencia = {estado: muestras.count(estado) for estado in distribucion_objetivo.keys()}

print("Frecuencia de cada muestra:")
for estado, freq in frecuencia.items():
    print(f"{estado}: {freq}")
