
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división por cero"

def potencia(a, b):
    return a ** b

def division_entera(a, b):
    if b != 0:
        return a // b
    else:
        return "Error: división por cero"

# Pedimos datos al usuario
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
opcion = input("¿Qué operación quieres hacer? (division, potencia, division entera): ")

if opcion == "division":
    resultado = division(a, b)
    print("La división es:", resultado)
elif opcion == "potencia":
    resultado = potencia(a, b)
    print("La potencia es:", resultado)
elif opcion == "division_entera":
    resultado = division_entera(a, b)
    print("La división entera es:", resultado)
else:
    print("Opción no válida")
