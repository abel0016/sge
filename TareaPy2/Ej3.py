'''3.- Diseña un programa que lea dos número, el primero será la base y el segundo el exponente,
y tendrá que mostrar el resultado de realizar dicha potencia usando un bucle iterativo.'''


def calcular_potencia():
    base = int(input("Introduce la base: "))
    exponente = int(input("Introduce el exponente: "))

    resultado = 1

    for i in range(exponente):
        resultado *= base

    print(f"{base}^{exponente} = {resultado}")

calcular_potencia()
