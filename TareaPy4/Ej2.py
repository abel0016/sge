from math import sqrt


def calcular_hipotenusa():
    a = float(input("Ingrese el valor del cateto a: "))
    b = float(input("Ingrese el valor del cateto b: "))
    h = sqrt(a * a + b * b)
    print("La hipotenusa es:", h)
calcular_hipotenusa()