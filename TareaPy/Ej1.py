#1.- Diseña un programa que pida un nombre por teclado y muestre un mensaje de bienvenida
# en el que se incluya dicho nombre.

def saludo():
    nombre=input("¿Cómo te llamas?\n")
    return print(f"Hola {nombre}!")
saludo()