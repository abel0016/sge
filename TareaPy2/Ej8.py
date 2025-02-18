'''3.- Diseña un programa que llene una Lista de números enteros pedidos por teclado hasta que
se introduzca el número 0 y después muestre un listado con los números pares introducidos
y otro listado con los números impares.'''
def paresImpares():
    lista=[]
    pares=[]
    impares=[]
    print("Introduce numeros para añadir a la lista, 0 para salir")
    salida=""
    while salida!="Exit":
        num=int(input("Introduce un numero:\n"))
        if num==0:
            salida="Exit"
        else:
            lista.append(num)
    for i in lista:
        num=i
        if num%2==0:
            pares.append(num)
        else:
            impares.append(num)
    print(f"Numeros pares: {pares}")
    print(f"Numeros impares: {impares}")
paresImpares()


