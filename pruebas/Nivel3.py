#3.1. Crea una lista de nombres y muestra cada nombre de la lista.
nombres=["Paco","Manolo","Maria","Sara"]
for n in range(len(nombres)):
    print(f"{nombres[n]}")
#3.2. Escribe un programa que encuentre el número más grande en una lista creada por el usuario
numeros=[]
salida=""
while salida!="Exit":
    n=input("Introduce un numero para añadir a la lista, Exit para salir\n")
    if n=="Exit":
        salida="Exit"
    else:
        n=int(n)
        numeros.append(n)
print(f"El numero mas alto de la lista es: {max(numeros)}")

#3.3. Implementa un juego de adivinanza donde el usuario debe adivinar un número secreto entre 1 y 100.

num=int(input("Jugador 1. Introduce el numero a adivinar: "))
print("Jugador 2. Tienes 5 oportunidades")
for i in range(5):
    num2=int(input(f"Oportunidad {i+1}: "))
    if num==num2:
        print("Has acertado")
        break
    else:
        print("prueba otra vez")
        