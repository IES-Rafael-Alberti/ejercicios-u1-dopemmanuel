"""Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de
todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:"""

while True:
    try:
        n = int(input("Ingrese el numero de veces: "))
        if n > 0:
            suma = n * (n + 1) / 2
            print(f"La suma de los enteros de 1 a {n} es: {suma}")
            break
        else:
            print("Ese no es un numero positivo")

    except ValueError:
        print("Solo de caracter numerico.")
