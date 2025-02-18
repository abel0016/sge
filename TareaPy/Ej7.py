#3.- Diseñar un programa que pida un número por teclado e indique si este es par o impar y si la
# raíz da como resultado un número entero o decimal.
import math

def analizarNumero():
    numero = int(input("Introduce un número entero: "))

    paridad = "par" if numero % 2 == 0 else "impar"
    raiz_cuadrada = math.sqrt(numero)
    tipo_raiz = "entero" if raiz_cuadrada.is_integer() else "decimal"

    print(f"El número {numero} es {paridad} y su raíz cuadrada es {tipo_raiz}")

analizarNumero()
