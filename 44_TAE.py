import nltk
from nltk.translate import IBMModel1

# Oraciones de ejemplo en inglés y sus traducciones en español
english_sentences = ["machine learning is fascinating", "natural language processing is challenging"]
spanish_sentences = ["el aprendizaje automatico es fascinante", "el procesamiento del lenguaje natural es desafiante"]

# Tokenizamos las oraciones
english_tokens = [nltk.word_tokenize(sentence.lower()) for sentence in english_sentences]
spanish_tokens = [nltk.word_tokenize(sentence.lower()) for sentence in spanish_sentences]

# Entrenamos el modelo IBM Model 1
ibm_model = IBMModel1(list(zip(english_tokens, spanish_tokens)), 5)

# Traducimos una nueva oración de inglés a español
new_english_sentence = "text classification is important"
new_english_tokens = nltk.word_tokenize(new_english_sentence.lower())
new_spanish_tokens = ibm_model.align(new_english_tokens)

# Convertimos los tokens traducidos en una oración
new_spanish_sentence = " ".join(new_spanish_tokens)
print("Traduccion de la nueva oracion:", new_spanish_sentence)
