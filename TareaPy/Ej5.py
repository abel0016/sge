#1.- Diseña un programa que pida un número entero por teclado y nos indique si es mayor,
# igual o menor que 100.

def comparar_con_100():
    numero = int(input("Introduce un número entero: "))

    if numero > 100:
        print(f"El número {numero} es mayor que 100")
    elif numero < 100:
        print(f"El número {numero} es menor que 100")
    else:
        print(f"El número {numero} es igual a 100")

comparar_con_100()
