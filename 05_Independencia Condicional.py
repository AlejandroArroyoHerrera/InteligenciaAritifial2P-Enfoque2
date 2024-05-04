import numpy as np

# Simulamos el lanzamiento de dos dados
num_experimentos = 10000
dado_1 = np.random.randint(1, 7, size=num_experimentos)
dado_2 = np.random.randint(1, 7, size=num_experimentos)

# Contamos la cantidad de veces que la suma es 7 y el primer dado muestra un 4
suma_siete = np.sum((dado_1 + dado_2) == 7)
primer_dado_cuatro = np.sum(dado_1 == 4)

# Calculamos las probabilidades de cada evento
prob_suma_siete = suma_siete / num_experimentos
prob_primer_dado_cuatro = primer_dado_cuatro / num_experimentos

# Calculamos la probabilidad de que ambos eventos ocurran
ambos_eventos = np.sum((dado_1 == 4) & ((dado_1 + dado_2) == 7)) / num_experimentos

# Verificamos si los eventos son independientes
independencia_condicional = ambos_eventos == prob_suma_siete * prob_primer_dado_cuatro

print("Probabilidad de que la suma de los dados sea 7:", prob_suma_siete)
print("Probabilidad de que el primer dado muestre un 4:", prob_primer_dado_cuatro)
print("Probabilidad de que ambos eventos ocurran:", ambos_eventos)
print("Los eventos son independientes?:", independencia_condicional)
