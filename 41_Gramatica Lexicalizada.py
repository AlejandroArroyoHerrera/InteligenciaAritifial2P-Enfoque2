import nltk

# Definimos una gramática probabilística lexicalizada
grammar = nltk.PCFG.fromstring("""
    S -> NP VP [1.0]
    VP -> V NP [0.7] | V [0.3]
    NP -> Det N [0.6] | Det N PP [0.4]
    PP -> P NP [1.0]
    Det -> 'the' [0.8] | 'a' [0.2]
    N -> 'cat' [0.4] | 'dog' [0.4] | 'bird' [0.2]
    V -> 'chased' [0.5] | 'saw' [0.5]
    P -> 'in' [0.6] | 'on' [0.4]
""")

# Creamos un parser probabilístico lexicalizado
parser = nltk.ViterbiParser(grammar)

# Definimos una frase para analizar
sentence = "the cat chased the bird on the roof"

# Analizamos la frase y mostramos los árboles de análisis más probables
for tree in parser.parse(sentence.split()):
    print("Arbol de Analisis:")
    print(tree)
    print("Probabilidad:", parser.probability(tree))
