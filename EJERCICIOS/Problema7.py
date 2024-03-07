# Programa principal
try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    print("1. Mostrar suma de los dos números")
    print("2. Mostrar resta de los dos números (el primero menos el segundo)")
    print("3. Mostrar multiplicación de los dos números")
    opcion = input("Elija una opción: ")

    if opcion == '1':
        print("La suma de los dos números es:", num1 + num2)
    elif opcion == '2':
        print("La resta de los dos números es:", num1 - num2)
    elif opcion == '3':
        print("La multiplicación de los dos números es:", num1 * num2)
    else:
        print("Opción no válida.")

except ValueError:
    print("Por favor, ingrese números válidos.")