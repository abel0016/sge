'''4.- Diseña un programa que lea 5 números y encuentre el máximo, el mínimo y calcule
la media de esos número leídos.'''
print("Introduce 5 numeros")
def calcular_media():
    numeros=[]
    for i in range(5):
        num=int(input(f"Numero {i+1}: "))
        numeros.append(num)
    maximo=max(numeros)
    minimo=min(numeros)
    media=sum(numeros)/len(numeros)
    print(f"Maximo: {maximo}")
    print(f"Minimo: {minimo}")
    print(f"Media: {media}")

calcular_media()

