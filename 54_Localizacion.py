import numpy as np

# Definir la función de movimiento del robot en 3D
def mover_robot_3d(posicion_anterior, distancia, angulo_x, angulo_y):
    x_prev, y_prev, z_prev = posicion_anterior
    x_nuevo = x_prev + distancia * np.cos(angulo_x) * np.cos(angulo_y)
    y_nuevo = y_prev + distancia * np.sin(angulo_x) * np.cos(angulo_y)
    z_nuevo = z_prev + distancia * np.sin(angulo_y)
    return x_nuevo, y_nuevo, z_nuevo

# Definir la función de observación en 3D (simulada)
def observar_3d(distancia_real, distancia_medida, desviacion):
    prob = 1.0 / (desviacion * np.sqrt(2 * np.pi)) * \
           np.exp(-0.5 * ((distancia_real - distancia_medida) / desviacion) ** 2)
    return prob

# Algoritmo de Monte Carlo para localización en 3D
def localizar_particulas_3d(num_particulas, num_pasos, distancia_medida, desviacion_observacion):
    # Generar partículas aleatorias en 3D
    particulas = np.random.rand(num_particulas, 3) * 10  # Espacio 3D de 10x10x10 unidades
    for _ in range(num_pasos):
        # Movimiento del robot (simulado) en 3D
        distancia_real = np.random.normal(1, 0.2)  # Distancia real con ruido
        angulo_x = np.random.uniform(0, 2*np.pi)  # Ángulo de giro aleatorio en x
        angulo_y = np.random.uniform(0, 2*np.pi)  # Ángulo de giro aleatorio en y
        for i in range(num_particulas):
            particulas[i] = mover_robot_3d(particulas[i], distancia_real, angulo_x, angulo_y)
        # Actualizar pesos basados en la observación en 3D
        for i in range(num_particulas):
            distancia_medida_simulada = np.linalg.norm(particulas[i] - [5, 5, 5])  # Distancia al punto central
            particulas[i, 3] = observar_3d(distancia_real, distancia_medida_simulada, desviacion_observacion)
        # Normalizar los pesos
        particulas[:, 3] /= np.sum(particulas[:, 3])
        # Resamplear partículas
        indices = np.random.choice(num_particulas, num_particulas, p=particulas[:, 3])
        particulas = particulas[indices]
    return particulas

# Parámetros
num_particulas = 1000
num_pasos = 10
distancia_medida = 4.5  # Distancia medida desde el punto central
desviacion_observacion = 0.1  # Desviación estándar de la observación (ruido)

# Localizar el robot en 3D
particulas_localizadas_3d = localizar_particulas_3d(num_particulas, num_pasos, distancia_medida, desviacion_observacion)

# Mostrar la ubicación estimada del robot en 3D
ubicacion_estimada_3d = np.mean(particulas_localizadas_3d[:, :3], axis=0)
print("Ubicacion estimada del robot en 3D:", ubicacion_estimada_3d)
