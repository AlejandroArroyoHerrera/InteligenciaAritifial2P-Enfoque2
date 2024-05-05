from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Ejemplo de documentos de texto
documents = [
    "Machine learning is the study of computer algorithms that improve automatically through experience.",
    "Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence.",
    "Information retrieval (IR) is the process of obtaining information from a collection of documents.",
    "Document retrieval is the task of finding documents that are relevant to an information need from a large collection."
]

# Consulta de búsqueda
query = "Machine learning and natural language processing"

# Vectorizamos los documentos y la consulta utilizando TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents + [query])

# Calculamos la similitud coseno entre la consulta y los documentos
similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])

# Ordenamos los documentos por similitud y mostramos los más relevantes
most_similar_doc_index = similarities.argsort()[0][::-1][0]
most_similar_doc = documents[most_similar_doc_index]
similarity_score = similarities[0][most_similar_doc_index]

print("Documento mas relevante:")
print(most_similar_doc)
print("Similitud:", similarity_score)
