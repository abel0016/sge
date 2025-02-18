import math


def menu_circulos():
    while True:
        print("""
---------------------------------------------------------------
                CÍRCULOS
---------------------------------------------------------------
    1   Calcular área
    2   Calcular perímetro
    3   Calcular radio a partir del área
    4   Calcular radio a partir del perímetro
    0   Salir programa
---------------------------------------------------------------
Seleccione una opción [0-4]: """)
        opcion = input()

        if opcion == "0":
            break
        elif opcion == "1":
            r = float(input("Ingrese el radio: "))
            area = math.pi * (r * r)
            print("Área redondeada:", round(area))
        elif opcion == "2":
            r = float(input("Ingrese el radio: "))
            perimetro = 2 * math.pi * r
            print("Perímetro redondeado:", round(perimetro))
        elif opcion == "3":
            area = float(input("Ingrese el área: "))
            radio = math.sqrt(area / math.pi)
            print("Radio redondeado:", round(radio))
        elif opcion == "4":
            perimetro = float(input("Ingrese el perímetro: "))
            radio = perimetro / (2 * math.pi)
            print("Radio redondeado:", round(radio))
        else:
            print("Opción no válida.")
menu_circulos()