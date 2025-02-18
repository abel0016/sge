'''3.- Diseña un programa que pida un número por teclado hasta que sea un número y determine
si este es un entero o un float.'''
def pedir_numero():
    while True:
        entrada = input("Introduce un número: ")
        try:
            numero = int(entrada)
            print(f"Has introducido el número entero: {numero}")
            break
        except ValueError:
            try:
                numero = float(entrada)
                print(f"Has introducido el número flotante: {numero}")
                break
            except ValueError:
                print("Error: No es un número válido. Inténtalo de nuevo.")

pedir_numero()
