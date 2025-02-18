'''4.- Diseña un programa que solicite un divisor y un dividendo (ambos entero o float) y
controle mediante excepción que la división no se puede realizar.'''
def calcular_div():
    while True:
        try:
            dividendo = int(input("Introduce el dividendo:"))
            divisor = int(input("Introduce el divisor:"))
            div=dividendo/divisor
            print(div)
        except ValueError:
            print("Alguno de los valores introducidos no es un int")
            try:
                dividendo=float(input("Introduce el dividendo:"))
                divisor=float(input("Introduce el divisor:"))
                div=dividendo/divisor
                print(div)
            except ValueError:
                print("Alguno de los valores introducidos no es un float")
calcular_div()

