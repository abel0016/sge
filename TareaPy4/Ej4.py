import random


def generar_password():
    while True:
        print("""
        ---------------------------------------------------------------
                        CONTRASEÑAS
        ---------------------------------------------------------------
            1   Aleatorias letras abecedario
            2   Aleatorias letras abecedario y numeros
            3   Aleatorias combinacion 5 caracteres
            0   Salir programa
        ---------------------------------------------------------------
        Seleccione una opción [0-3]: """)

        opcion= input()
        if opcion=="0":
            break
        elif opcion=="1":
            longitud=int(input("¿Que longitud quieres?"))
            abc="abcdefghijklmnopqrstuvwxyz"
            password = ""
            for i in range(longitud):
                password=password+(abc[random.randint(0,len(abc))])
            print(password)
        elif opcion=="2":
            longitud = int(input("¿Que longitud quieres?"))
            abc = "abcdefghijklmnopqrstuvwxyz"
            password=""
            for i in range(longitud):
                num=str(random.randint(1,9))
                password=password+(abc[random.randint(0,len(abc))])
                password=password+num
            print(password)

generar_password()


