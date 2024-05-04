import numpy as np
import matplotlib.pyplot as plt

# Generamos una muestra de una distribución normal
muestra = np.random.normal(loc=0, scale=1, size=1000)

# Trazamos el histograma para visualizar la distribución de probabilidad
plt.hist(muestra, bins=30, density=True, alpha=0.6, color='g')

# Añadimos una línea para mostrar la función de densidad de probabilidad (PDF) teórica
x = np.linspace(-4, 4, 100)
pdf = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)
plt.plot(x, pdf, color='r', linestyle='--', linewidth=2)

plt.xlabel('Valor')
plt.ylabel('Densidad de Probabilidad')
plt.title('Distribucion Normal')
plt.grid(True)
plt.show()
