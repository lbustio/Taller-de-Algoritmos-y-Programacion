import math

def area_circulo():
    try:
        radio = float(input("Ingrese el radio del círculo: "))
        area = math.pi * radio ** 2
        print(f"El área del círculo es: {area}")
    except ValueError:
        print("Error: Ingrese un número válido para el radio.")

def area_cuadrado():
    try:
        lado = float(input("Ingrese el lado del cuadrado: "))
        area = lado ** 2
        print(f"El área del cuadrado es: {area}")
    except ValueError:
        print("Error: Ingrese un número válido para el lado.")

def area_triangulo():
    try:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = (base * altura) / 2
        print(f"El área del triángulo es: {area}")
    except ValueError:
        print("Error: Ingrese números válidos para la base y la altura.")

def volumen_cilindro():
    try:
        radio = float(input("Ingrese el radio del cilindro: "))
        altura = float(input("Ingrese la altura del cilindro: "))
        area_base = math.pi * radio ** 2
        volumen = area_base * altura
        print(f"El volumen del cilindro es: {volumen}")
    except ValueError:
        print("Error: Ingrese números válidos para el radio y la altura.")

def volumen_cubo():
    try:
        lado = float(input("Ingrese el lado del cubo: "))
        volumen = lado ** 3
        print(f"El volumen del cubo es: {volumen}")
    except ValueError:
        print("Error: Ingrese un número válido para el lado.")

def volumen_piramide():
    try:
        base = float(input("Ingrese el área de la base de la pirámide: "))
        altura = float(input("Ingrese la altura de la pirámide: "))
        volumen = (1/3) * base * altura
        print(f"El volumen de la pirámide es: {volumen}")
    except ValueError:
        print("Error: Ingrese números válidos para el área de la base y la altura.")

def mostrar_menu():
    print("Calculadora de área y volumen")
    print("Menu:")
    print("-----")
    print("1)- Área del círculo")
    print("2)- Área del cuadrado")
    print("3)- Área del triángulo")
    print("4)- Volumen del cilindro")
    print("5)- Volumen del cubo")
    print("6)- Volumen de la pirámide")
    print("7)- Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione la opción deseada: ")

        if opcion == "1":
            area_circulo()
        elif opcion == "2":
            area_cuadrado()
        elif opcion == "3":
            area_triangulo()
        elif opcion == "4":
            volumen_cilindro()
        elif opcion == "5":
            volumen_cubo()
        elif opcion == "6":
            volumen_piramide()
        elif opcion == "7":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 7.")

if __name__ == "__main__":
    main()
