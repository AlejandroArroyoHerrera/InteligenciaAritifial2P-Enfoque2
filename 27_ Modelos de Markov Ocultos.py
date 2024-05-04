from hmmlearn import hmm
import numpy as np

# Datos de entrenamiento (secuencias de observaciones)
secuencia_1 = np.array([[1.1], [0.9], [0.8], [1.0]])
secuencia_2 = np.array([[0.5], [0.7], [0.9], [1.1]])

# Definici�n del modelo HMM
modelo_hmm = hmm.GaussianHMM(n_components=2, covariance_type="full")

# Entrenamiento del modelo con m�ltiples secuencias
modelo_hmm.fit(np.concatenate([secuencia_1, secuencia_2]))

# Clasificaci�n de nuevas secuencias
etiqueta_secuencia_1 = modelo_hmm.predict(secuencia_1.reshape(1, -1))
etiqueta_secuencia_2 = modelo_hmm.predict(secuencia_2.reshape(1, -1))

print("Etiqueta de la secuencia 1:", etiqueta_secuencia_1)
print("Etiqueta de la secuencia 2:", etiqueta_secuencia_2)
