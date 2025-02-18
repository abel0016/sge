'''1.- Diseña un programa que esté pidiendo un valor por teclado hasta que sea un entero.'''
def pedir_entero():
    while True:
        try:
            numero = int(input("Introduce un número entero: "))
            print(f"Has introducido el número: {numero}")
            break
        except ValueError:
            print("Error: No es un número entero. Inténtalo de nuevo.")

pedir_entero()
