# Lista para almacenar los nombres de los productos
productos = []

# Diccionario para almacenar los detalles de los productos (nombre y cantidad)
inventario = {}

# Función para agregar un nuevo producto al inventario
def agregar_producto(nombre, cantidad):
    # Agrega el nombre del producto a la lista de productos
    productos.append(nombre)
    # Almacena el nombre y la cantidad del producto en el diccionario de inventario
    inventario[nombre] = cantidad
    # Imprime un mensaje confirmando la adición del producto
    print(f"¡Se ha agregado {cantidad} unidades del producto {nombre} al inventario!")

# Función para actualizar la cantidad de un producto existente
def actualizar_inventario(nombre, cantidad):
    # Verifica si el producto existe en el inventario
    if nombre in inventario:
        # Actualiza la cantidad del producto en el inventario
        inventario[nombre] += cantidad
        # Imprime un mensaje confirmando la actualización del inventario del producto
        print(f"¡Se ha actualizado el inventario del producto {nombre} a {inventario[nombre]} unidades!")
    else:
        # Imprime un mensaje si el producto no existe en el inventario
        print("El producto no existe en el inventario.")

# Función para mostrar todo el inventario
def mostrar_inventario():
    # Imprime el encabezado del inventario
    print("Inventario Actual:")
    # Itera a través de la lista de productos
    for producto in productos:
        # Muestra el nombre del producto y su cantidad del diccionario de inventario
        print(f"{producto}: {inventario[producto]} unidades")

# Función principal para la interacción con el usuario
def menu():
    while True:
        # Menú de opciones para el usuario
        print("\n1. Agregar Producto")
        print("2. Actualizar Existencias")
        print("3. Mostrar Inventario")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del nuevo producto: ")
            cantidad = int(input("Ingrese la cantidad inicial: "))
            agregar_producto(nombre, cantidad)
        elif opcion == '2':
            nombre = input("Ingrese el nombre del producto a actualizar: ")
            cantidad = int(input("Ingrese la cantidad a agregar (-X si es una reducción): "))
            actualizar_inventario(nombre, cantidad)
        elif opcion == '3':
            mostrar_inventario()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecutar el programa
menu()
