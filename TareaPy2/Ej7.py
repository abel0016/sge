'''2.- Diseña un programa que pida la longitud de una lista y los números enteros para llenarla,
 y con esto muestre el mínimo, el máximo y la media de los valores introducidos en la lista.'''
def calcular_media():
    lista=[]
    longitud=int(input("Introduce el tamaño de la lista:"))
    for i in range(longitud):
        num=int(input("Introduce un numero:"))
        lista.append(num)
    print(f"Maximo: {max(lista)}")
    print(f"Minimo: {min(lista)}")
    print(f"Media: {sum(lista)/len(lista)}")
calcular_media()