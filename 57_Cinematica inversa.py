import numpy as np

# Funci�n para calcular la cinem�tica inversa de un robot m�vil diferencial
def cinematica_inversa_robot_diferencial(x_objetivo, y_objetivo, theta_objetivo, radio_rueda):
    # Distancia del centro del robot a las ruedas (mitad del ancho del robot)
    d = 0.5
    
    # Calcular la velocidad lineal y angular deseada
    v = np.sqrt(x_objetivo**2 + y_objetivo**2)
    w = np.arctan2(y_objetivo, x_objetivo) - theta_objetivo
    
    # Calcular las velocidades de las ruedas
    velocidad_izquierda = (v - d * w) / radio_rueda
    velocidad_derecha = (v + d * w) / radio_rueda
    
    return velocidad_izquierda, velocidad_derecha

# Par�metros del robot m�vil diferencial
posicion_objetivo_x = 2.0
posicion_objetivo_y = 1.0
orientacion_objetivo = np.radians(45)  # Orientaci�n objetivo en radianes
radio_rueda = 0.1

# Calcular las velocidades de las ruedas para alcanzar la posici�n y orientaci�n objetivo
v_izquierda, v_derecha = cinematica_inversa_robot_diferencial(posicion_objetivo_x, posicion_objetivo_y, orientacion_objetivo, radio_rueda)

# Mostrar las velocidades calculadas
print("Velocidad de la rueda izquierda:", v_izquierda)
print("Velocidad de la rueda derecha:", v_derecha)
