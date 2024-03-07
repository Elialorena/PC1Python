# Pedimos el consumo al usuario
consumo = float(input("¿Cuánto fue su consumo en el restaurante? "))

# Pedimos el porcentaje de propina al usuario
porcentaje_propina = float(input("¿Qué porcentaje de propina desea dejar al mesero? "))

# Calculamos la cantidad de propina
propina = consumo * (porcentaje_propina / 100)

# Mostramos la cantidad de propina
print(f"La cantidad de propina a dejar es de: {propina:.2f}")