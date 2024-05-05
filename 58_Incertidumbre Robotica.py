import numpy as np

# Funci�n para actualizar las part�culas utilizando el muestreo de part�culas
def muestreo_particulas(particulas_anteriores, medicion, movimiento, covarianza_medicion, covarianza_movimiento):
    # Predicci�n: Aplicar movimiento a las part�culas con ruido
    movimiento_simulado = np.random.normal(movimiento, np.sqrt(covarianza_movimiento), len(particulas_anteriores))
    particulas_predichas = particulas_anteriores + movimiento_simulado
    
    # Pesos: Calcular la probabilidad de cada part�cula dado la nueva medici�n
    pesos = np.exp(-0.5 * ((particulas_predichas - medicion) ** 2 / covarianza_medicion))
    pesos /= np.sum(pesos)
    
    # Resamplear: Seleccionar nuevas part�culas basadas en sus pesos
    indices = np.random.choice(len(particulas_anteriores), len(particulas_anteriores), p=pesos)
    nuevas_particulas = particulas_predichas[indices]
    
    return nuevas_particulas

# Par�metros del muestreo de part�culas
num_particulas = 1000
particulas_iniciales = np.random.uniform(0, 10, (num_particulas, 2))  # Part�culas iniciales distribuidas uniformemente
medicion_actual = np.array([3.0, 3.0])  # Medici�n actual de la posici�n del robot
movimiento_robot = np.array([0.1, 0.1])  # Movimiento del robot (simulado)
covarianza_medicion = 0.1  # Covarianza de la medici�n (ruido en la medici�n)
covarianza_movimiento = 0.1  # Covarianza del movimiento (incertidumbre en el movimiento del robot)

# Actualizar las part�culas utilizando el muestreo de part�culas
nuevas_particulas = muestreo_particulas(particulas_iniciales, medicion_actual, movimiento_robot, covarianza_medicion, covarianza_movimiento)

# Mostrar las nuevas part�culas
print("Nuevas particulas:")
print(nuevas_particulas)
