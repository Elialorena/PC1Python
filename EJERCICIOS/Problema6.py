# Solicitar al usuario que ingrese la edad del cliente
edad = int(input("Ingrese la edad del cliente: "))

# Calcular el precio de la entrada según la edad del cliente
if edad < 4:
    precio_entrada = 0
elif edad <= 18:
    precio_entrada = 5
else:
    precio_entrada = 10

# Mostrar el precio de la entrada al usuario
print("El precio de la entrada es: $" + str(precio_entrada))
