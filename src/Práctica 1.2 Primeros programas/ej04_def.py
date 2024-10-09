"""Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.
try:
    celcius = int(input("Ingresa los grados °C: "))

    
    Fahrenheit = celcius * 9 / 5 + 32
    print(celcius," °C son en °F ", Fahrenheit)
except ValueError:
    print("Solo caracter numerico para esto.")
"""
#La funcion principal:
def calculo_grados():
    celcius = float(input("Ingresa los grados °C: ")) # Te pide los grados para almacenarlos en la variable

    Fahrenheit = celcius * 9 / 5 + 32

    #La variable con los datos se transforma en los datos de la funcion:
    total = (f"{celcius:.2f}°C en Fahrenheit son °F {Fahrenheit:.2f}")
    return total

if __name__ == "__main__":
    print("Pedira la temperatura y lo pasara a grados:")

#Se sobreestituye las variables, osea que usaras otras variables que las representen fuera de la funcion:
print(calculo_grados())