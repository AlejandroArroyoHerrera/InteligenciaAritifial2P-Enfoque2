import numpy as np
import scipy.stats as stats

# Parámetros de la distribución normal
media = 0
desviacion_estandar = 1

# Generamos una muestra de la distribución normal
muestra = np.random.normal(loc=media, scale=desviacion_estandar, size=1000)

# Calculamos la probabilidad de que un valor esté dentro de cierto rango
rango_inicio = -1
rango_fin = 1
probabilidad_rango = stats.norm.cdf(rango_fin, loc=media, scale=desviacion_estandar) - stats.norm.cdf(rango_inicio, loc=media, scale=desviacion_estandar)

# Imprimimos el resultado
print(f'Probabilidad de que un valor esté entre {rango_inicio} y {rango_fin}: {probabilidad_rango}')

