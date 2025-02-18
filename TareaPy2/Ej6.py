'''1.- Diseña un programa que llene un Lista de 5 elementos con números enteros pedidos por
teclado y a continuación los muestre por pantalla.'''

def lista():
    numeros=[]
    for i in range(5):
        num=int(input("Introduce un numero:\n"))
        numeros.append(num)

    for i in range(len(numeros)):
        print(numeros[i])
lista()