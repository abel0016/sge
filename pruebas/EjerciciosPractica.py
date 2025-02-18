#1.2. Pide al usuario que ingrese su nombre y luego imprime un saludo personalizado.
nombre=input("¿Cómo te llamas?\n")
print(f"Hola {nombre}")
#1.3. Calcula la suma de dos números ingresados por el usuario y muestra el resultado.
num1=input("Ingrese un numero\n")
num2=input("Ingrese otro numero\n")
num1=int(num1)
num2=int(num2)
suma=num1+num2
print(f"La suma de los 2 numeros es: {suma}")
#2.1. Escribe un programa que determine si un número ingresado por el usuario es par o impar.
numero=input("Ingrese un numero\n")
numero=int(numero)
if numero%2==0:
    print("El numero es par")
elif numero%2!=0:
    print("El numero es impar")
#2.2. Crea un programa que verifique si un número es positivo, negativo o igual a cero.
if numero>0:
    print("El numero es positivo")
elif numero==0:
    print("El numero es 0")
elif numero<0:
    print("El numero es negativo")
#2.3. Escribe un programa que calcule el promedio de tres números ingresados por el usuario.
numeros=[]
for n in range(3):
    a=input("Ingrese un numero a la lista\n")
    a=int(a)
    numeros.insert(n,a)
print(f"La media de los numeros introducidos es: {sum(numeros)/3}")
