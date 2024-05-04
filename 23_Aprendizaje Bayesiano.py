import numpy as np
import pymc3 as pm

# Datos de entrada
x = np.random.uniform(0, 10, size=100)
pendiente_verdadera = 2
intercepto_verdadero = 3
y = pendiente_verdadera * x + intercepto_verdadero + np.random.normal(0, 1, size=100)

# Definición del modelo bayesiano
with pm.Model() as modelo:
    # Parámetros
    pendiente = pm.Normal('pendiente', mu=0, sigma=10)
    intercepto = pm.Normal('intercepto', mu=0, sigma=10)
    sigma = pm.HalfNormal('sigma', sigma=1)
    
    # Modelo lineal
    mu = pendiente * x + intercepto
    
    # Likelihood
    observaciones = pm.Normal('observaciones', mu=mu, sigma=sigma, observed=y)
    
    # Inferencia
    traza = pm.sample(1000, tune=1000)

# Resultados
pm.summary(traza)
pm.traceplot(traza)
