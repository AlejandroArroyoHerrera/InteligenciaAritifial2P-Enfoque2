import numpy as np
import matplotlib.pyplot as plt

# Parámetros del proceso
media = 0
desviacion_estandar = 1
longitud = 1000

# Generación del proceso estacionario gaussiano
tiempo = np.arange(longitud)
proceso = np.random.normal(loc=media, scale=desviacion_estandar, size=longitud)

# Graficamos el proceso estacionario
plt.plot(tiempo, proceso)
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.title('Proceso Estacionario Gaussiano')
plt.grid(True)
plt.show()
