'''3.- Diseña un programa que pida una cadena de caracteres y nos indique si es o no palíndromo,
utiliza una función creada por ti que devuleva True o False  para saber si es palíndromo.'''

def es_palindromo(cadena):
    return cadena == cadena[::-1]
cadena = input("Introduce una cadena de caracteres: ")

if es_palindromo(cadena):
    print("La cadena es un palíndromo")
else:
    print("La cadena NO es un palíndromo")

es_palindromo("radar")

