'''3.- Diseña un programa que pidiendo por teclado la marca de un vehículo, el consumo de combustible
 a los 100km y los litros de combustible que le he puesto en el depósito, me calcule los kilómetros
 que puedo recorrer. La salida tendrá el siguiente formato:

***********************************
El vehículo marca que consume consumo litros a los 100km
Me permite circular una distancia de kmrecorridos km con litros litros
***********************************
'''
def kmDisponibles():
    marca=input("¿Cúal es la marca del vehiculo?\n")
    consumo=int(input("¿Cuanto consume a los 100km?\n"))
    litros=int(input("¿Cuantos litros tiene el deposito?\n"))
    kmrecorridos=(litros*100)/consumo
    return print(f"El vehiculo {marca} que consume {consumo} litros a los 100km me permite circular una distancia de {kmrecorridos} km con {litros} litros")
kmDisponibles()