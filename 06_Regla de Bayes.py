# Probabilidades a priori de pertenecer a cada categoría
prob_categoria_a = 0.4
prob_categoria_b = 0.6

# Probabilidades condicionales de que ciertas palabras aparezcan en cada categoría
prob_palabra_dado_a = {'interesante': 0.8, 'aburrido': 0.2}
prob_palabra_dado_b = {'interesante': 0.3, 'aburrido': 0.7}

# Función para calcular la probabilidad de pertenecer a una categoría dada una palabra
def prob_categoria_dado_palabra(palabra, prob_categoria, prob_palabra_dado_categoria):
    prob_no_palabra = 1 - prob_palabra_dado_categoria[palabra]
    prob_palabra = (prob_palabra_dado_categoria[palabra] * prob_categoria) + (prob_no_palabra * (1 - prob_categoria))
    return (prob_palabra_dado_categoria[palabra] * prob_categoria) / prob_palabra

# Calculamos la probabilidad de que el documento pertenezca a cada categoría dado ciertas palabras
prob_interesante_dado_a = prob_categoria_dado_palabra('interesante', prob_categoria_a, prob_palabra_dado_a)
prob_interesante_dado_b = prob_categoria_dado_palabra('interesante', prob_categoria_b, prob_palabra_dado_b)

print("La probabilidad de que el documento sea de la categoroa A dado que contiene la palabra 'interesante' es:", prob_interesante_dado_a)
print("La probabilidad de que el documento sea de la categoria B dado que contiene la palabra 'interesante' es:", prob_interesante_dado_b)
