import nltk
from nltk.corpus import brown

# Descargamos el corpus 'brown' si no está presente
nltk.download('brown')

# Cargamos el corpus 'brown'
corpus = brown.words()

# Creamos un diccionario para almacenar las frecuencias de las palabras
word_freq = {}
total_words = 0

# Contamos la frecuencia de cada palabra en el corpus
for word in corpus:
    word_freq[word] = word_freq.get(word, 0) + 1
    total_words += 1

# Calculamos las probabilidades de ocurrencia de cada palabra
word_prob = {word: freq / total_words for word, freq in word_freq.items()}

# Imprimimos las probabilidades de ocurrencia de algunas palabras
print("Probabilidades de ocurrencia de palabras:")
for word in ['the', 'cat', 'dog', 'apple']:
    print(f"{word}: {word_prob.get(word, 0)}")
