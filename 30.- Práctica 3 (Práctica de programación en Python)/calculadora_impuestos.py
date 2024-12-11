def calcular_impuesto(precio_venta, categoria):
    if categoria == 'A':
        impuesto = precio_venta * 0.20
    elif categoria == 'B':
        impuesto = precio_venta * 0.15
    elif categoria == 'C':
        impuesto = precio_venta * 0.10
    else:
        impuesto = 0  # Si la categoría no es válida, el impuesto será cero
    return impuesto

def validar_precio(precio):
    try:
        precio = float(precio)
        if precio < 0:
            return False, precio
        else:
            return True, precio
    except ValueError:
        return False, precio

def validar_categoria(categoria):
    return categoria.upper() in ['A', 'B', 'C']

def main():
    while True:
        precio_valido = False
        categoria_valida = False

        while not precio_valido:
            precio_venta = input("Ingrese el precio de venta: ")
            precio_valido, precio_venta = validar_precio(precio_venta)
            if not precio_valido:
                print("Error: Ingrese un precio válido (número positivo).")

        while not categoria_valida:
            categoria = input("Ingrese la categoría del producto (A, B o C): ")
            categoria_valida = validar_categoria(categoria)
            if not categoria_valida:
                print("Error: Ingrese una categoría válida (A, B o C).")

        impuesto = calcular_impuesto(precio_venta, categoria.upper())
        print(f"El impuesto a pagar es: {impuesto}\n")

        continuar = input("¿Desea realizar otra transacción? (Sí o No): ")
        if continuar.lower() != 's':
            print("¡Hasta luego!")
            break

if __name__ == "__main__":
    main()
