import nltk
from nltk import PCFG
from nltk.parse.generate import generate

# Definimos una gramática probabilística
grammar = PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> Det N [0.6] | Det N PP [0.4]
    VP -> V [0.7] | V NP [0.3]
    PP -> P NP [1.0]
    Det -> 'the' [0.8] | 'a' [0.2]
    N -> 'cat' [0.4] | 'dog' [0.4] | 'bird' [0.2]
    V -> 'chased' [0.5] | 'saw' [0.5]
    P -> 'in' [0.6] | 'on' [0.4]
""")

# Generamos frases probabilísticamente
for sentence in generate(grammar, n=5, depth=5):
    print(' '.join(sentence))
