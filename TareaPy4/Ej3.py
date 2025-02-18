import statistics
import math
import random


def lanzar_dado():
    return random.randint(1, 6)

def main():
    try:
        n = int(input("Ingrese el número de lanzamientos del dado: "))
        if n <= 0:
            print("El número de lanzamientos debe ser mayor que 0.")
            return

        resultados = []
        for i in range(n):
            resultado = lanzar_dado()
            resultados.append(resultado)
            print(f"Lanzamiento {i + 1}: {resultado}")

        print("\nEstadísticas de los lanzamientos:")
        print(f"Promedio: {statistics.mean(resultados)}")
        print(f"Mediana: {statistics.median(resultados)}")
        print(f"Moda: {statistics.mode(resultados)}")
        print(f"Desviación estándar: {statistics.stdev(resultados)}")
    except ValueError:
        print("Ingrese un número válido.")
main()