# Probabilidad a priori de que una transacción sea fraudulenta o legítima
probabilidad_legitima = 0.98
probabilidad_fraudulenta = 0.02

# Función para predecir si una transacción es fraudulenta o legítima
def predecir_fraude(probabilidad):
    if probabilidad > 0.5:
        return "Fraude"
    else:
        return "Legítima"

# Ejemplo de probabilidad a priori en acción
probabilidad_transaccion = 0.05  # Probabilidad calculada por el modelo
prediccion = predecir_fraude(probabilidad_transaccion)

print(f"El modelo predice que la transacción es: {prediccion}")
