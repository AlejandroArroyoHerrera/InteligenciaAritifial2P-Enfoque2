import numpy as np

# Definición de parámetros del HMM
estados_ocultos = ['Soleado', 'Nublado', 'Lluvioso']
simbolos = ['Paseo', 'Gimnasio', 'Cine']
pi = np.array([0.6, 0.2, 0.2])  # Probabilidades iniciales de los estados ocultos
A = np.array([[0.7, 0.2, 0.1],   # Matriz de transición de estados ocultos
              [0.3, 0.5, 0.2],
              [0.2, 0.3, 0.5]])
B = np.array([[0.6, 0.2, 0.2],   # Matriz de emisión
              [0.1, 0.7, 0.2],
              [0.2, 0.3, 0.5]])

# Función para generar una secuencia de observaciones dado un HMM
def generar_secuencia_observaciones(longitud):
    secuencia_observaciones = []
    estado_actual = np.random.choice(estados_ocultos, p=pi)
    for _ in range(longitud):
        simbolo = np.random.choice(simbolos, p=B[estados_ocultos.index(estado_actual)])
        secuencia_observaciones.append(simbolo)
        estado_actual = np.random.choice(estados_ocultos, p=A[estados_ocultos.index(estado_actual)])
    return secuencia_observaciones

# Generación de una secuencia de observaciones de longitud 10
secuencia_generada = generar_secuencia_observaciones(10)
print("Secuencia de Observaciones Generada:", secuencia_generada)
