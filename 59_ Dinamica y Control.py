import numpy as np
import matplotlib.pyplot as plt

# Funci�n para calcular la se�al de control utilizando un controlador PID
def control_pid(objetivo, actual, kp, ki, kd, dt, integral_previo, error_previo):
    # Calculamos el error actual
    error = objetivo - actual
    
    # Calculamos la integral del error
    integral = integral_previo + error * dt
    
    # Calculamos la derivada del error
    derivada = (error - error_previo) / dt
    
    # Calculamos la se�al de control PID
    se�al_control = kp * error + ki * integral + kd * derivada
    
    return se�al_control, integral, error

# Par�metros del controlador PID
kp = 1.0
ki = 0.1
kd = 0.1

# Par�metros de simulaci�n
posicion_objetivo = 90.0  # Posici�n deseada en grados
tiempo_simulacion = 10.0  # Tiempo de simulaci�n en segundos
dt = 0.01  # Paso de tiempo

# Inicializamos el controlador y el estado del brazo rob�tico
posicion_actual = 0.0  # Posici�n inicial del brazo
integral_previa = 0.0  # Integral previa del error
error_previo = 0.0  # Error previo
tiempo = np.arange(0, tiempo_simulacion, dt)
posiciones = []

# Simulamos el control de posici�n del brazo rob�tico utilizando el controlador PID
for t in tiempo:
    se�al_control, integral_previa, error_previo = control_pid(posicion_objetivo, posicion_actual, kp, ki, kd, dt, integral_previa, error_previo)
    posicion_actual += se�al_control * dt
    posiciones.append(posicion_actual)

# Visualizamos los resultados
plt.plot(tiempo, posiciones)
plt.xlabel('Tiempo (s)')
plt.ylabel('Posicion del Brazo (grados)')
plt.title('Control de Posicion con PID para un Brazo Robotico')
plt.grid(True)
plt.show()
