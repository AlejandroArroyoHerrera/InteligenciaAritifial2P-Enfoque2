from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Definimos la estructura de la red bayesiana
modelo_tiempo = BayesianNetwork([('Humedad', 'Tiempo'), ('Viento', 'Tiempo')])

# Definimos las probabilidades condicionales
cpd_humedad = TabularCPD(variable='Humedad', variable_card=2, values=[[0.7], [0.3]])
cpd_viento = TabularCPD(variable='Viento', variable_card=2, values=[[0.8], [0.2]])
cpd_tiempo = TabularCPD(variable='Tiempo', variable_card=3, 
                        values=[[0.4, 0.6, 0.3, 0.1],  # Humedad: Baja, Viento: Bajo
                                [0.3, 0.3, 0.4, 0.2],  # Humedad: Baja, Viento: Alto
                                [0.3, 0.1, 0.3, 0.7]],  # Humedad: Alta, Viento: Bajo
                        evidence=['Humedad', 'Viento'], evidence_card=[2, 2])

# Asociamos las probabilidades condicionales con el modelo
modelo_tiempo.add_cpds(cpd_humedad, cpd_viento, cpd_tiempo)

# Verificamos la validez del modelo
print("¿Es valido el modelo de predicción del tiempo?:", modelo_tiempo.check_model())

# Realizamos inferencia utilizando Variable Elimination
inference_tiempo = VariableElimination(modelo_tiempo)

# Calculamos la probabilidad de cada tipo de tiempo dado ciertos valores de humedad y viento
resultado_tiempo = inference_tiempo.query(variables=['Tiempo'], evidence={'Humedad': 1, 'Viento': 0})['Tiempo']
print("Probabilidad de cada tipo de tiempo dado ciertos valores de humedad y viento:", resultado_tiempo.values)
