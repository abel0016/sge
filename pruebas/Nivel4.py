#4.1. Crea una función que calcule el área de un triángulo dado su base y altura.
def calcularArea(base, altura):
    area=(base*altura)/2
    return print(f"El área del triangulo es: {area}")
calcularArea(2,4)
#4.2. Define una función que convierta grados Celsius a grados Fahrenheit.
def conversion(celsius):
    farenheit=(celsius*9/5)+32
    return print(f"{celsius}ºC equivalen a: {farenheit}ºF")
conversion(0)
#4.3. Escribe una función que determine si una palabra es un palíndromo (simétrica).
def esPalindromo(palabra):
    if palabra == palabra[::-1]:
        return print(f"{palabra} es un palíndromo")
    else:
        return print(f"{palabra} no es un palíndromo")
esPalindromo("aerea")
