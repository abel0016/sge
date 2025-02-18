'''4.- Diseña un programa que pida un texto corto por teclado y a continuación imprima por
pantalla solo los caracteres pares del texto. Nota: Las cadenas de texto son como Listas inmutables.'''
def imprimir_pares():
    cadena=input("Introduce un texto corto:\n")
    print(cadena[::2])
imprimir_pares()