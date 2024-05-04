import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# Generar datos sintéticos
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Entrenar el modelo k-Medias
k = 4
modelo_kmeans = KMeans(n_clusters=k)
modelo_kmeans.fit(X)

# Obtener las etiquetas de los clusters
etiquetas = modelo_kmeans.labels_

# Visualizar los clusters y los centroides
plt.scatter(X[:, 0], X[:, 1], c=etiquetas, s=50, cmap='viridis')
plt.scatter(modelo_kmeans.cluster_centers_[:, 0], modelo_kmeans.cluster_centers_[:, 1], marker='*', s=200, color='red')
plt.show()
