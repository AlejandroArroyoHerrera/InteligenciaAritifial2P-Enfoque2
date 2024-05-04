import numpy as np

# Datos observados
datos = np.array([1, 1, 0, 1, 0, 1, 1, 0, 1, 0])

# Función para calcular la verosimilitud de un parámetro dado los datos
def verosimilitud(parametro):
    probabilidad_exitos = parametro ** sum(datos) * (1 - parametro) ** (len(datos) - sum(datos))
    return probabilidad_exitos

# Definimos una lista de posibles valores del parámetro
valores_parametro = np.linspace(0, 1, 100)

# Calculamos la verosimilitud para cada valor del parámetro
verosimilitudes = [verosimilitud(parametro) for parametro in valores_parametro]

# Normalizamos las verosimilitudes para obtener una distribución de probabilidad
verosimilitudes_normalizadas = verosimilitudes / np.sum(verosimilitudes)

# Graficamos la distribución de verosimilitud
import matplotlib.pyplot as plt
plt.plot(valores_parametro, verosimilitudes_normalizadas)
plt.xlabel('Parametro')
plt.ylabel('Densidad de Verosimilitud')
plt.title('Ponderacion de Verosimilitud para una Distribucion de Bernoulli')
plt.show()
