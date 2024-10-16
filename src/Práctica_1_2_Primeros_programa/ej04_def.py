"""La funcion principal: """

def calculo_grados(celcius):
    """Pedira la temperatura y lo pasara a grados:"""
    print("Escribe un programa que le pida al usuario una temperatura en grados Celsius,"
          "la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.")
    fahrenheit = celcius * 9 / 5 + 32
    total = f"{celcius:.2f}°C en Fahrenheit son °F {fahrenheit:.2f}"
    return total

def main():
    
    celcius = float(input("Ingresa los grados °C: "))
    result = calculo_grados(celcius)

    print(result)


if __name__ == "__main__":
    main()
