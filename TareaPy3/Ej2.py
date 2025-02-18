'''2.- Diseña un programa que esté pidiendo un valor por teclado hasta que sea un número float.'''
def pedir_float():
    while True:
        try:
            numero = float(input("Introduce un número float: "))
            print(f"Has introducido el número: {numero}")
            break
        except ValueError:
            print("Error: No es un número float. Inténtalo de nuevo.")

pedir_float()