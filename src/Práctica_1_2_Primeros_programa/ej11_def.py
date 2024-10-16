"""La función principal:"""

def leer_numero(n):
    """Leer el entero positivo y calcular la suma de 1 a n."""

    suma = n * (n + 1) / 2
    result = f"La suma de los enteros de 1 a {n} es: {round(suma)}"
    return result

def main():
    n = int(input("Introduce un número: "))
    
    while n < 0:
        print("No es válido. Introduce un número positivo.")
        n = int(input("Introduce un número: "))
    

    result = leer_numero(n)
    print(result)

if __name__ == "__main__":
    print("Escribir un programa que lea un entero positivo, n, introducido por "
          "el usuario y después muestre en pantalla la suma de todos los enteros "
          "desde 1 hasta n. La suma de los n primeros enteros positivos "
          "puede ser calculada de la siguiente forma:")
    
    main()
