def determinar_ganador(jugador, computadora):
    if jugador == computadora:
        return "Empate"
    elif (jugador == "piedra" and computadora == "tijeras") or (jugador == "papel" and computadora == "piedra") or (jugador == "tijeras" and computadora == "papel"):
        return "¡Ganaste!"
    else:
        return "¡La computadora gana!"

def main():
    import random

    opciones = ["piedra", "papel", "tijeras"]

    print("Bienvenido al juego de Piedra, Papel o Tijeras")
    print("Opciones disponibles: piedra, papel, tijeras")

    jugador = input("Elige tu jugada: ").lower()

    if jugador in opciones:
        computadora = random.choice(opciones)
        print(f"La computadora eligió: {computadora}")

        resultado = determinar_ganador(jugador, computadora)
        print(resultado)
    else:
        print("Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()