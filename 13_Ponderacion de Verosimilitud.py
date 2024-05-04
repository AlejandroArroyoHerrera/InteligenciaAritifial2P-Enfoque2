import numpy as np

# Datos observados
datos = np.array([1, 1, 0, 1, 0, 1, 1, 0, 1, 0])

# Funci�n para calcular la verosimilitud de un par�metro dado los datos
def verosimilitud(parametro):
    probabilidad_exitos = parametro ** sum(datos) * (1 - parametro) ** (len(datos) - sum(datos))
    return probabilidad_exitos

# Definimos una lista de posibles valores del par�metro
valores_parametro = np.linspace(0, 1, 100)

# Calculamos la verosimilitud para cada valor del par�metro
verosimilitudes = [verosimilitud(parametro) for parametro in valores_parametro]

# Normalizamos las verosimilitudes para obtener una distribuci�n de probabilidad
verosimilitudes_normalizadas = verosimilitudes / np.sum(verosimilitudes)

# Graficamos la distribuci�n de verosimilitud
import matplotlib.pyplot as plt
plt.plot(valores_parametro, verosimilitudes_normalizadas)
plt.xlabel('Parametro')
plt.ylabel('Densidad de Verosimilitud')
plt.title('Ponderacion de Verosimilitud para una Distribucion de Bernoulli')
plt.show()
