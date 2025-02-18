'''2.- Diseña un programa que pida dos números (float o entero) por teclado, los multiplique
y muestre el resultado, utiliza funciones creadas por ti, una para pedir los números
(hasta que sea número) y otra para hacer la multiplicación.'''
def pedir_numero(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            return float(entrada)
        except ValueError:
            print("Error: Debes ingresar un número válido.")

def multiplicar(num1, num2):
    return num1 * num2

numero1 = pedir_numero("Introduce el primer número: ")
numero2 = pedir_numero("Introduce el segundo número: ")

resultado = multiplicar(numero1, numero2)

print(f"El resultado de multiplicar {numero1} por {numero2} es: {resultado}")


