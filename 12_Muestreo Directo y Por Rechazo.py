import numpy as np

# Definimos la distribuci�n de probabilidad discreta
distribucion = {'A': 0.3, 'B': 0.5, 'C': 0.2}

# Funci�n para realizar muestreo directo
def muestreo_directo(distribucion):
    return np.random.choice(list(distribucion.keys()), p=list(distribucion.values()))

# Generamos 1000 muestras utilizando muestreo directo
muestras = [muestreo_directo(distribucion) for _ in range(1000)]

# Contamos la frecuencia de cada muestra
frecuencia = {muestra: muestras.count(muestra) for muestra in distribucion.keys()}

print("Frecuencia de cada muestra:")
for muestra, freq in frecuencia.items():
    print(f"{muestra}: {freq}")
