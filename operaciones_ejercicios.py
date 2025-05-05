def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

# Pedimos datos al usuario
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
opcion = input("¿Qué operación quieres hacer? (suma, resta, multiplicacion): ")

if opcion == "suma":
    resultado = suma(a, b)
    print("La suma es:", resultado)
elif opcion == "resta":
    resultado = resta(a, b)
    print("La resta es:", resultado)
elif opcion == "multiplicacion":
    resultado = multiplicacion(a, b)
    print("La multiplicación es:", resultado)
else:
    print("Opción no válida")