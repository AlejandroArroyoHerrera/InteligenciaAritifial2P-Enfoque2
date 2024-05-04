import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_blobs
from sklearn.mixture import GaussianMixture

# Generar datos sintéticos
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Aplicar el modelo de mezcla gaussiana (GMM)
gmm = GaussianMixture(n_components=4)
gmm.fit(X)

# Obtener las etiquetas de los clusters
etiquetas = gmm.predict(X)

# Visualizar los clusters
plt.scatter(X[:, 0], X[:, 1], c=etiquetas, s=50, cmap='viridis')

# Visualizar las elipses de covarianza
for componente in range(gmm.n_components):
    covarianza = gmm.covariances_[componente][:2, :2]
    media = gmm.means_[componente][:2]
    v, w = np.linalg.eigh(covarianza)
    v = 2.0 * np.sqrt(2.0) * np.sqrt(v)
    u = w[0] / np.linalg.norm(w[0])
    if u[0] == 0:
        angulo = np.arctan(u[1] / u[0])
    else:
        angulo = np.arctan(u[1] / u[0])
    angulo = 180 * angulo / np.pi
    ellipsoide = mpl.patches.Ellipse(media, v[0], v[1], 180 + angulo, color='k')
    ellipsoide.set_clip_box(ax.bbox)
    ellipsoide.set_alpha(0.5)
    ax.add_artist(ellipsoide)

plt.show()
