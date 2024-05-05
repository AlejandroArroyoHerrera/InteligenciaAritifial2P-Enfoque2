import numpy as np

# Función para actualizar las partículas utilizando el muestreo de partículas
def muestreo_particulas(particulas_anteriores, medicion, movimiento, covarianza_medicion, covarianza_movimiento):
    # Predicción: Aplicar movimiento a las partículas con ruido
    movimiento_simulado = np.random.normal(movimiento, np.sqrt(covarianza_movimiento), len(particulas_anteriores))
    particulas_predichas = particulas_anteriores + movimiento_simulado
    
    # Pesos: Calcular la probabilidad de cada partícula dado la nueva medición
    pesos = np.exp(-0.5 * ((particulas_predichas - medicion) ** 2 / covarianza_medicion))
    pesos /= np.sum(pesos)
    
    # Resamplear: Seleccionar nuevas partículas basadas en sus pesos
    indices = np.random.choice(len(particulas_anteriores), len(particulas_anteriores), p=pesos)
    nuevas_particulas = particulas_predichas[indices]
    
    return nuevas_particulas

# Parámetros del muestreo de partículas
num_particulas = 1000
particulas_iniciales = np.random.uniform(0, 10, (num_particulas, 2))  # Partículas iniciales distribuidas uniformemente
medicion_actual = np.array([3.0, 3.0])  # Medición actual de la posición del robot
movimiento_robot = np.array([0.1, 0.1])  # Movimiento del robot (simulado)
covarianza_medicion = 0.1  # Covarianza de la medición (ruido en la medición)
covarianza_movimiento = 0.1  # Covarianza del movimiento (incertidumbre en el movimiento del robot)

# Actualizar las partículas utilizando el muestreo de partículas
nuevas_particulas = muestreo_particulas(particulas_iniciales, medicion_actual, movimiento_robot, covarianza_medicion, covarianza_movimiento)

# Mostrar las nuevas partículas
print("Nuevas particulas:")
print(nuevas_particulas)
