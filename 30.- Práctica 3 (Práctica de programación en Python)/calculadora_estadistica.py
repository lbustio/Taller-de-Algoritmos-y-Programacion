def obtener_lista():
    while True:
        try:
            entrada = input("Ingrese una lista de números enteros separados por comas: ")
            numeros = [int(num) for num in entrada.split(',')]
            return numeros
        except ValueError:
            print("Error: Ingrese una lista válida de números enteros separados por comas.")

def cantidad_numeros(lista):
    cantidad = len(lista)
    print(f"La cantidad de números ingresados es: {cantidad}")

def numero_mas_grande(lista):
    maximo = max(lista)
    print(f"El número más grande de la lista es: {maximo}")

def numero_mas_pequeno(lista):
    minimo = min(lista)
    print(f"El número más pequeño de la lista es: {minimo}")

def promedio(lista):
    prom = sum(lista) / len(lista)
    print(f"El promedio de los números de la lista es: {prom}")

def suma_total(lista):
    suma = sum(lista)
    print(f"La suma total de los números de la lista es: {suma}")

def contiene_negativo(lista):
    contiene_neg = any(num < 0 for num in lista)
    if contiene_neg:
        print("La lista contiene números negativos.")
    else:
        print("La lista no contiene números negativos.")

def mostrar_menu():
    print("Calculadora de estadísticas")
    print("Menu:")
    print("-----")
    print("1)- Cantidad total de números ingresados")
    print("2)- Número más grande de la lista")
    print("3)- Número más pequeño de la lista")
    print("4)- El promedio de los números de la lista")
    print("5)- La suma total de los números de la lista")
    print("6)- Determinar si la lista contiene números negativos o no")
    print("7)- Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione la opción deseada: ")

        if opcion == "1":
            lista = obtener_lista()
            cantidad_numeros(lista)
        elif opcion == "2":
            lista = obtener_lista()
            numero_mas_grande(lista)
        elif opcion == "3":
            lista = obtener_lista()
            numero_mas_pequeno(lista)
        elif opcion == "4":
            lista = obtener_lista()
            promedio(lista)
        elif opcion == "5":
            lista = obtener_lista()
            suma_total(lista)
        elif opcion == "6":
            lista = obtener_lista()
            contiene_negativo(lista)
        elif opcion == "7":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 7.")

if __name__ == "__main__":
    main()
