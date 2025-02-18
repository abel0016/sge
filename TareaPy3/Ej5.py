'''5.- Diseña un programa que haya dos jugadores, uno que introduce un número entero del
1 al 100 (controla que entre un entero y entre 1 y 100) y otro jugador tiene que adivinarlo,
con un máximo de 5 intentos (Cualquier intento será contado aunque introduzca un float o texto).
Pero cuidado piensa como comparas la entrada del jugador 1 con la del jugador 2 (input() siempre
almacena como string).'''


def obtener_numero_jugador1():
    while True:
        try:
            numero = int(input("Jugador 1, introduce un número entre 1 y 100: "))
            if 1 <= numero <= 100:
                return numero
            else:
                print("Error: El número debe estar entre 1 y 100")
        except ValueError:
            print("Error: Debes ingresar un número entero válido")


def adivinar_numero(numero_secreto):
    intentos = 5
    print("\nJugador 2, intenta adivinar el número en 5 intentos.")

    for intento in range(1, intentos + 1):
        entrada = input(f"Intento {intento}: Ingresa un número: ")

        try:
            numero_adivinado = int(entrada)
        except ValueError:
            print("Entrada no válida. Se cuenta como un intento fallido.")

        if numero_adivinado == numero_secreto:
            print(f"¡Felicidades! Has adivinado el número {numero_secreto} en {intento} intentos")
            return
        elif numero_adivinado < numero_secreto:
            print("El número es mayor")
        else:
            print("El número es menor")

    print(f"\n¡Has perdido! El número era {numero_secreto}")


numero_secreto = obtener_numero_jugador1()
adivinar_numero(numero_secreto)
