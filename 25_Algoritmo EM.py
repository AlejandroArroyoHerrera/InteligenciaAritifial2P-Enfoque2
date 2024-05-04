from sklearn.datasets import make_blobs
from sklearn.mixture import GaussianMixture

# Generar datos sint�ticos
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Crear y ajustar modelo GMM
modelo_gmm = GaussianMixture(n_components=4)
modelo_gmm.fit(X)

# Etiquetar los puntos de datos seg�n el modelo ajustado
etiquetas = modelo_gmm.predict(X)

# Visualizaci�n de los clusters
plt.scatter(X[:, 0], X[:, 1], c=etiquetas, s=40, cmap='viridis');
plt.show()
