def convertir_longitud(unidad_inicial, unidad_final, valor):
    conversiones = {
        ('m', 'ft'): valor * 3.28084,
        ('m', 'in'): valor * 39.3701,
        ('ft', 'm'): valor / 3.28084,
        ('ft', 'in'): valor * 12,
        ('in', 'm'): valor / 39.3701,
        ('in', 'ft'): valor / 12,
    }
    return conversiones.get((unidad_inicial, unidad_final))

def convertir_temperatura(unidad_inicial, unidad_final, valor):
    if unidad_inicial == 'C' and unidad_final == 'F':
        return (valor * 9/5) + 32
    elif unidad_inicial == 'F' and unidad_final == 'C':
        return (valor - 32) * 5/9

def convertir_peso(unidad_inicial, unidad_final, valor):
    if unidad_inicial == 'kg' and unidad_final == 'lb':
        return valor * 2.20462
    elif unidad_inicial == 'lb' and unidad_final == 'kg':
        return valor / 2.20462

def mostrar_menu():
    print("Conversor de unidades:")
    print("Menu:")
    print("----")
    print("1)- Convertir longitudes")
    print("2)- Convertir temperaturas")
    print("3)- Convertir pesos")
    print("4)- Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Fórmulas matemáticas")
            print("Conversión de longitudes:")
            print("\tMetros (m) a pies (ft): m2ft = valor en metros * 3.28084")
            # Continuar con el resto de las fórmulas

            unidad_inicial = input("Para convertir longitudes, diga la unidad de longitud inicial: ")
            unidad_final = input("Para convertir longitudes, diga la unidad de longitud final: ")
            valor = float(input("Para convertir longitudes, diga la longitud a convertir: "))

            resultado = convertir_longitud(unidad_inicial, unidad_final, valor)
            if resultado:
                print(f"Usted quiere convertir {valor} {unidad_inicial} a {unidad_final}.")
                print(f"{valor} {unidad_inicial} son {resultado} {unidad_final}.\n")
            else:
                print("Error: Unidades de longitud ingresadas no válidas.\n")

        elif opcion == "2":
            # Lógica similar para la conversión de temperaturas
            pass

        elif opcion == "3":
            # Lógica similar para la conversión de pesos
            pass

        elif opcion == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.\n")

if __name__ == "__main__":
    main()
