"""La funcion principal:"""

def leer_numero():

    """ Leer el entero positivo:"""

    n = int(input("Introduce un numero: "))

    while n < 0:
        print ("No es valido")
        n = int(input("Introduce un numero: "))
    suma = n * (n + 1) / 2
    return n, suma

if __name__ == "__main__":
    print("Escribir un programa que lea un entero positivo, n, introducido por "
            "el usuario y después muestre en pantalla la suma de todos los enteros"
            "desde 1 hasta n. La suma de los n primeros enteros positivos"
            "puede ser calculada de la siguiente forma:")

num, summ = leer_numero()
print(f"La suma de los enteros de 1 a {num} es: {round(summ)}")
