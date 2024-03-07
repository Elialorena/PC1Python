# Pedimos al usuario cuántos shows ha visto
numero_shows = int(input("¿Cuántos shows musicales has visto en el último año? "))

# Verificamos si el usuario ha visto más de 3 shows
ha_visto_mas_de_3_shows = numero_shows > 3

# Mostramos el resultado
print(f"Has visto más de 3 shows: {ha_visto_mas_de_3_shows}")