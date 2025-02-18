'''4.- Diseña un programa que pida un número entero por teclado y calcule y muestre su factorial,
 utiliza funciones creadas por ti para pedir el entero y otra para calcular el factorial.
•	El factorial se calcula multiplicando cada vez por un número menor. 5!=5*4*3*2*1
•	El factorial de 0 es 1.
•	El factorial de n.º negativos no existe.
'''
def pedir_entero():
    while True:
        try:
            numero = int(input("Introduce un número entero: "))
            if numero < 0:
                print("Error: El factorial de números negativos no existe. Inténtalo de nuevo")
            else:
                return numero
        except ValueError:
            print("Error: Debes ingresar un número entero válido")

def calcular_factorial(n):
    if n == 0 or n == 1:
        return 1
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial

numero = pedir_entero()
resultado = calcular_factorial(numero)
print(f"El factorial de {numero} es: {resultado}")
