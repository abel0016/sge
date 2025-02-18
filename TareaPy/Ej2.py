#2.- Diseña un programa que pida dos números enteros por teclado, los sume y muestre el resultado,
# entendemos que el usuario del programa sabe lo que es un entero y no tecleara caracteres.
def suma():
    num1=int(input("Introduce un numero:\n"))
    num2=int(input("Introduce otro numero:\n"))
    suma=num1+num2
    return print(f"La suma es: {suma}")
suma()