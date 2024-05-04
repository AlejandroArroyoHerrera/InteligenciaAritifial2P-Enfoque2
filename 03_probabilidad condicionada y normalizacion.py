# Probabilidades sin normalizar
probabilidades = [0.2, 0.3, 0.5]

# Suma de todas las probabilidades sin normalizar
suma_probabilidades = sum(probabilidades)

# Normalizamos las probabilidades dividiendo cada una por la suma total
probabilidades_normalizadas = [prob / suma_probabilidades for prob in probabilidades]

print(f"Probabilidades normalizadas: {probabilidades_normalizadas}")
print(f"Suma de las probabilidades normalizadas: {sum(probabilidades_normalizadas)}")
