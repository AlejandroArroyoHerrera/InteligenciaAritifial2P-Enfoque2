import numpy as np
import matplotlib.pyplot as plt

# Generamos datos de ejemplo
datos = np.random.rand(100, 2)

# Creamos y entrenamos el mapa autoorganizado de Kohonen
mapa_kohonen = KohonenMap(input_dim=2, map_dim=(5, 5))
mapa_kohonen.train(datos, learning_rate=0.01, epochs=100)

# Visualizamos el mapa y los datos
plt.figure(figsize=(8, 8))
for i in range(mapa_kohonen.map_dim[0]):
    for j in range(mapa_kohonen.map_dim[1]):
        plt.scatter(i, j, color='b', marker='o', s=100, alpha=0.5)
        for punto in datos:
            bmu_idx = np.argmin(np.linalg.norm(mapa_kohonen.weights - punto, axis=(2, 1)))
            if (bmu_idx[0] == i) and (bmu_idx[1] == j):
                plt.scatter(i, j, color='r', marker='x', s=200)
plt.title('Mapa Autoorganizado de Kohonen')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
