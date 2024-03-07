# Definimos el peso de cada juguete
peso_payaso = 112  # gramos
peso_muneca = 75  # gramos

# Pedimos el número de payasos y muñecas vendidos
numero_payasos = int(input("¿Cuántos payasos se vendieron? "))
numero_munecas = int(input("¿Cuántas muñecas se vendieron? "))

# Calculamos el peso total del paquete
peso_total = (numero_payasos * peso_payaso) + (numero_munecas * peso_muneca)

# Mostramos el peso total del paquete
print(f"El peso total del paquete es de: {peso_total} gramos")