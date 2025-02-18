'''4.- Crear un programa que muestre un menú por pantalla de la siguiente forma:
Menú:
N – Nuevo
G – Guardar
B – Borrar
Y dependiendo de la tecla pulsada, N, G o B nos de un mensaje de la opción que hemos elegido,
si elegimos una opción no contemplada el programa informara de dicha situación.

'''
def mostrar_menu():
    print("Menú:\nN – Nuevo\nG – Guardar\nB – Borrar")
    opcion = input("Elige una opción: ")

    if opcion == "N":
        print("Has elegido la opción: Nuevo")
    elif opcion == "G":
        print("Has elegido la opción: Guardar")
    elif opcion == "B":
        print("Has elegido la opción: Borrar")
    else:
        print("Opcion no valida")

mostrar_menu()
