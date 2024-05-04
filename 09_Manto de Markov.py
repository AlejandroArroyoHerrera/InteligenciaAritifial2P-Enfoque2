import numpy as np

# Definimos la matriz de transición del modelo de Markov
# Las filas representan el estado actual y las columnas representan el estado siguiente
matriz_transicion = np.array([[0.8, 0.15, 0.05],  # Soleado -> Soleado, Nublado, Lluvioso
                               [0.3, 0.6, 0.1],   # Nublado -> Soleado, Nublado, Lluvioso
                               [0.2, 0.3, 0.5]])  # Lluvioso -> Soleado, Nublado, Lluvioso

# Definimos los estados del tiempo
estados_tiempo = ['Soleado', 'Nublado', 'Lluvioso']

# Estado inicial (día 0)
estado_actual = np.random.choice(estados_tiempo, p=[0.6, 0.3, 0.1])
print("Dia 0:", estado_actual)

# Predicción del tiempo para los próximos 5 días
for dia in range(1, 6):
    estado_siguiente = np.random.choice(estados_tiempo, p=matriz_transicion[estados_tiempo.index(estado_actual)])
    print(f"Dia {dia}: {estado_siguiente}")
    estado_actual = estado_siguiente
