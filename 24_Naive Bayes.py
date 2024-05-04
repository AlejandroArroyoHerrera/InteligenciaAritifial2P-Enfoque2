from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Cargar los datos de dígitos escritos a mano
digits = load_digits()

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=42)

# Entrenar el clasificador Naive Bayes
clasificador = GaussianNB()
clasificador.fit(X_train, y_train)

# Predecir en el conjunto de prueba
predicciones = clasificador.predict(X_test)

# Calcular la precisión
precision = accuracy_score(y_test, predicciones)
print("Precision:", precision)
