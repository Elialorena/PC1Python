# Definir la lista de muestra
lista = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']

# Eliminar los elementos en las posiciones 0, 4 y 5
posiciones_a_eliminar = [0, 4, 5]
for indice in sorted(posiciones_a_eliminar, reverse=True):
    del lista[indice]

# Imprimir la lista resultante
print("Resultado esperado:", lista)