'''5.- Diseña un programa que pida un numero y muestre la tabla de multiplicar de dicho número.'''
def tabla():
    num=int(input("Introduce un numero:\n"))
    for i in range(11):
        print(f"{num}*{i}={num*i}")
tabla()