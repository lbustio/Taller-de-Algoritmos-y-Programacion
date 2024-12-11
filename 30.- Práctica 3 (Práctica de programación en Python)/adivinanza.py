import random

def jugar():
    numero_a_adivinar = random.randint(1, 10)

    while True:
        try:
            numero_ingresado = int(input("Ingresa un número entre 1 y 10 para adivinar: "))

            if numero_ingresado < 1 or numero_ingresado > 10:
                print("Error: Ingresa un número válido entre 1 y 10.")
                continue

            if numero_ingresado < numero_a_adivinar:
                print("El número a adivinar es mayor.")
            elif numero_ingresado > numero_a_adivinar:
                print("El número a adivinar es menor.")
            else:
                print("¡Felicidades! Has adivinado el número.")
                seguir_jugando = input("¿Quieres jugar otra vez? (s/n): ").lower()
                if seguir_jugando == 's':
                    numero_a_adivinar = random.randint(1, 10)
                    continue
                else:
                    print("¡Gracias por jugar! ¡Hasta luego!")
                    break
        except ValueError:
            print("Error: Ingresa un número válido.")

if __name__ == "__main__":
    jugar()