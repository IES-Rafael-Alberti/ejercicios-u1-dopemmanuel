"""La funcion principal: """

def calculo_grados():
    """Pedira la temperatura y lo pasara a grados:"""
    celcius = float(input("Ingresa los grados °C: "))
    fahrenheit = celcius * 9 / 5 + 32
    total = f"{celcius:.2f}°C en Fahrenheit son °F {fahrenheit:.2f}"
    return total

if __name__ == "__main__":
    print("Escribe un programa que le pida al usuario una temperatura en grados Celsius,"
          "la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.")

print(calculo_grados())
