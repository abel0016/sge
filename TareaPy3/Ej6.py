'''1.- Diseña un programa que pida dos números enteros por teclado, los sume y muestre el resultado,
 utiliza funciones creadas por ti para la solicitud de número entero (hasta que sea entero) y
 otra para realizar la suma.'''
def pedir_numero():
    while True:
        try:
            num1=int(input("Introduce un numero:\n"))
            return num1
        except ValueError:
            print("Debes introducir los numeros como int")
def suma():
    sum=pedir_numero()+pedir_numero()
    print(f"La suma es: {sum}")
suma()

