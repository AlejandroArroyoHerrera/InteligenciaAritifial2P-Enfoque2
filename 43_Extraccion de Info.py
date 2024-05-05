import nltk

# Ejemplo de texto
text = "Barack Obama was born in Hawaii. He served as the 44th President of the United States."

# Tokenizamos el texto en oraciones y palabras
sentences = nltk.sent_tokenize(text)
tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]

# Aplicamos NER utilizando un etiquetador probabilístico
tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
chunked_sentences = [nltk.ne_chunk(tagged_sentence) for tagged_sentence in tagged_sentences]

# Extraemos entidades nombradas del resultado del etiquetador
named_entities = []
for chunked_sentence in chunked_sentences:
    for subtree in chunked_sentence:
        if isinstance(subtree, nltk.Tree) and subtree.label() == 'PERSON':
            entity = " ".join([word for word, tag in subtree.leaves()])
            named_entities.append(entity)

print("Entidades Nombradas encontradas:")
print(named_entities)
