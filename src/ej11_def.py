"""
Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de
todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:
def leer_NUMERO():


    while True:
        try:
            n = int(input("Ingrese los numeros: "))
            if n > 0:
                suma = n * (n + 1) / 2
                return n, suma
            else:
                print("Ese no es un numero positivo")
        except ValueError:
            print("Solo de caracter numerico.")


    num, summ = leer_NUMERO()
    print(print(f"La suma de los enteros de 1 a {num} es: {summ}"))
"""

def leer_NUMEROV2():
    n = int(input("Introduce un numero: "))

    while n < 0:
        print ("No es valido")
        n = int(input("Introduce un numero: "))
    suma = n * (n + 1) / 2
    return n, suma

if __name__ == "__main__":
    print("Leer el entero positivo: ")

num, summ = leer_NUMEROV2()
print(f"La suma de los enteros de 1 a {num} es: {round(summ)}")