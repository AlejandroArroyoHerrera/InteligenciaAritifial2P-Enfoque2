import numpy as np

# Par�metros del HMM
estados_ocultos = ['A', 'B', 'C']  # Estados ocultos
observaciones = [1, 0, 1, 0, 1]  # Secuencia de observaciones

# Matriz de transici�n de estados ocultos
A = np.array([[0.6, 0.3, 0.1],
              [0.2, 0.7, 0.1],
              [0.3, 0.2, 0.5]])

# Matriz de emisi�n
B = np.array([[0.8, 0.2],
              [0.2, 0.8],
              [0.5, 0.5]])

# Probabilidades iniciales de los estados ocultos
pi = np.array([0.5, 0.3, 0.2])

# Funci�n para calcular la probabilidad de una secuencia de observaciones dada una secuencia de estados ocultos
def probabilidad_observaciones(secuencia_estados):
    probabilidad = pi[estados_ocultos.index(secuencia_estados[0])]
    for i in range(1, len(secuencia_estados)):
        probabilidad *= A[estados_ocultos.index(secuencia_estados[i-1])][estados_ocultos.index(secuencia_estados[i])]
    return probabilidad

# Funci�n de Hacia Delante
def hacia_delante(observaciones):
    alfa = np.zeros((len(observaciones), len(estados_ocultos)))
    alfa[0] = pi * B[:, observaciones[0]]
    for t in range(1, len(observaciones)):
        for j in range(len(estados_ocultos)):
            alfa[t][j] = B[j, observaciones[t]] * sum(alfa[t-1] * A[:, j])
    return alfa

# Funci�n de Hacia Atr�s
def hacia_atras(observaciones):
    beta = np.ones((len(observaciones), len(estados_ocultos)))
    for t in range(len(observaciones)-2, -1, -1):
        for i in range(len(estados_ocultos)):
            beta[t][i] = sum(beta[t+1] * A[i] * B[:, observaciones[t+1]])
    return beta

# Calculamos la probabilidad de estar en cada estado en cada paso de tiempo
alfa = hacia_delante(observaciones)
beta = hacia_atras(observaciones)

# Calculamos la probabilidad marginal de estar en cada estado en cada paso de tiempo
prob_estado_tiempo = alfa * beta / np.sum(alfa * beta, axis=1, keepdims=True)

# Imprimimos las probabilidades marginales de estar en cada estado en cada paso de tiempo
for t, prob in enumerate(prob_estado_tiempo):
    print(f"Paso de tiempo {t}: {dict(zip(estados_ocultos, prob))}")
