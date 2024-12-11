def traducir_a_ingles(numero):
    match numero:
        case 1:
            return "one"
        case 2:
            return "two"
        case 3:
            return "three"
        case 4:
            return "four"
        case 5:
            return "five"
        case 6:
            return "six"
        case 7:
            return "seven"
        case 8:
            return "eight"
        case 9:
            return "nine"
        case 10:
            return "ten"
        case _:
            return "Número fuera de rango"

def traducir_a_espanol(numero):
    match numero:
        case 1:
            return "uno"
        case 2:
            return "dos"
        case 3:
            return "tres"
        case 4:
            return "cuatro"
        case 5:
            return "cinco"
        case 6:
            return "seis"
        case 7:
            return "siete"
        case 8:
            return "ocho"
        case 9:
            return "nueve"
        case 10:
            return "diez"
        case _:
            return "Número fuera de rango"

def main():
    idioma = input("Ingresa el idioma en el que deseas la traducción (ingles/espanol): ")

    if idioma.lower() == "ingles":
        numero = int(input("Ingresa un número del 1 al 10: "))
        palabra = traducir_a_ingles(numero)
        print(f"El número {numero} en inglés es: {palabra}")
    elif idioma.lower() == "espanol":
        numero = int(input("Ingresa un número del 1 al 10: "))
        palabra = traducir_a_espanol(numero)
        print(f"El número {numero} en español es: {palabra}")
    else:
        print("Idioma no compatible")

    main()