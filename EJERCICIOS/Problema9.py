# Definir una función para invertir la lista
def invertir_lista(lista):
    return lista[::-1]

# Lista original
lista_original = ['Di', 'buen', 'día', 'a', 'papa']

# Invertir la lista
lista_invertida = invertir_lista(lista_original)

# Mostrar la lista invertida
print("Lista original:", lista_original)
print("Lista invertida:", lista_invertida)