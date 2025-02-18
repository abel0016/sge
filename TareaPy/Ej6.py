'''2.- Una tienda desea un programa que calcule un porcentaje de descuento sobre el importe de la
compra de sus clientes, pero el porcentaje de descuento solo se aplicará si esta por encima de un
gasto de la compra, por lo tanto el programa pedirá el importe de la compra, el porcentaje de descuento y la
cantidad a partir de la cual se hará el descuento, pero en caso de que se haga el descuento, el total de la
compra nunca podrá ser menor al importe a partir del cual se hace el descuento. Mostrara por pantalla el
descuento que se le va ha hacer al cliente y el total que tiene que pagar el cliente.'''
def calcular_descuento():
    importe_compra = float(input("Introduce el importe de la compra: "))
    porcentaje_descuento = float(input("Introduce el porcentaje de descuento: "))
    umbral_descuento = float(input("Introduce la cantidad mínima para aplicar el descuento: "))

    if importe_compra >= umbral_descuento:
        descuento = (importe_compra * porcentaje_descuento) / 100
        total_pagar = max(importe_compra - descuento, umbral_descuento)
    else:
        descuento = 0
        total_pagar = importe_compra

    print(f"Descuento aplicado: {descuento}€\nTotal a pagar: {total_pagar}€")

calcular_descuento()
