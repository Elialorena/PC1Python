# Solicitar al usuario que ingrese la hora en formato HH:MM
time = input("Ingrese la hora (formato HH:MM): ")
hours, minutes = time.split(":")
hour_decimal = float(hours) + float(minutes) / 60

# Verificar si la hora ingresada corresponde a la hora de desayuno, almuerzo o cena
if 7.0 <= hour_decimal <= 8.0:
    print("Es hora de desayunar.")
elif 12.0 <= hour_decimal <= 13.0:
    print("Es hora de almorzar.")
elif 18.0 <= hour_decimal <= 19.0:
    print("Es hora de cenar.")