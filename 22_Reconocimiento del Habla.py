import numpy as np

# Definición de las palabras a reconocer y los fonemas que las componen
palabras = ['casa', 'perro', 'gato']
fonemas = {
    'casa': ['k', 'a', 's', 'a'],
    'perro': ['p', 'e', 'r', 'o'],
    'gato': ['g', 'a', 't', 'o']
}

# Definición de las probabilidades iniciales de las palabras
pi = {
    'casa': 1/3,
    'perro': 1/3,
    'gato': 1/3
}

# Matrices de transición entre fonemas
A = np.array([
    [0.7, 0.2, 0.1],
    [0.1, 0.7, 0.2],
    [0.2, 0.1, 0.7]
])

# Matrices de emisión de fonemas para cada palabra
B = {
    'casa': np.array([
        [0.1, 0.7, 0.2],
        [0.2, 0.1, 0.7],
        [0.2, 0.1, 0.7],
        [0.1, 0.7, 0.2]
    ]),
    'perro': np.array([
        [0.2, 0.1, 0.7],
        [0.2, 0.1, 0.7],
        [0.7, 0.2, 0.1],
        [0.1, 0.7, 0.2]
    ]),
    'gato': np.array([
        [0.2, 0.1, 0.7],
        [0.1, 0.7, 0.2],
        [0.1, 0.7, 0.2],
        [0.2, 0.1, 0.7]
    ])
}

# Función para calcular la probabilidad de una palabra dada una secuencia de fonemas
def probabilidad_palabra(secuencia_fonemas, palabra):
    probabilidad = pi[palabra]
    for i in range(len(secuencia_fonemas)):
        probabilidad *= B[palabra][i][fonemas[palabra].index(secuencia_fonemas[i])]
    return probabilidad

# Secuencia de fonemas de entrada
secuencia_entrada = ['k', 'a', 's', 'a']

# Reconocimiento de la palabra hablada
probabilidades = {palabra: probabilidad_palabra(secuencia_entrada, palabra) for palabra in palabras}
palabra_reconocida = max(probabilidades, key=probabilidades.get)

print("Secuencia de Fonemas de Entrada:", secuencia_entrada)
print("Palabra Reconocida:", palabra_reconocida)
print("Probabilidad:", probabilidades[palabra_reconocida])
