'''2.- Diseñar un programa que imprima los múltiplos de 3 y de 5 que se encuentran entre dos número
 introducidos por teclado, el pseudocódigo deberá indicar si el número es
 múltiplo de 3 de 5 o de los dos a la vez.'''
def imprimir_multiplos():
    numinicio = int(input("Introduce el número de inicio: "))
    numfin = int(input("Introduce el número de fin: "))

    for num in range(numinicio, numfin + 1):
        if num % 3 == 0 and num % 5 == 0:
            print(f"{num} es múltiplo de 3 y 5")
        elif num % 3 == 0:
            print(f"{num} es múltiplo de 3")
        elif num % 5 == 0:
            print(f"{num} es múltiplo de 5")

imprimir_multiplos()
