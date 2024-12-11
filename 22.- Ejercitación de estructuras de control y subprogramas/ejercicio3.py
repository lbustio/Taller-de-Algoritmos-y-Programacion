def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "No se puede dividir por cero"

def main():
    operaciones = {
        "suma": suma,
        "resta": resta,
        "multiplicacion": multiplicacion,
        "division": division
    }

    print("Operaciones disponibles: suma, resta, multiplicacion, division")
    operacion = input("Elige una operación: ").lower()

    try:
        if operacion in operaciones:
            numero1 = float(input("Ingresa el primer número: "))
            numero2 = float(input("Ingresa el segundo número: "))

            resultado = operaciones[operacion](numero1, numero2)
            print(f"El resultado de la {operacion} es: {resultado}")
        else:
            print("Operación no válida")
    except ValueError:
        print("Por favor, ingresa números válidos.")

if __name__ == "__main__":
    main()