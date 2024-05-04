# Probabilidad a priori de que una transacci�n sea fraudulenta o leg�tima
probabilidad_legitima = 0.98
probabilidad_fraudulenta = 0.02

# Funci�n para predecir si una transacci�n es fraudulenta o leg�tima
def predecir_fraude(probabilidad):
    if probabilidad > 0.5:
        return "Fraude"
    else:
        return "Leg�tima"

# Ejemplo de probabilidad a priori en acci�n
probabilidad_transaccion = 0.05  # Probabilidad calculada por el modelo
prediccion = predecir_fraude(probabilidad_transaccion)

print(f"El modelo predice que la transacci�n es: {prediccion}")
