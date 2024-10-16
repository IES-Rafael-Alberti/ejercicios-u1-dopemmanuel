"""Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida."""

# Colocas los grados celcius:
celcius = int(input("Ingresa los grados °C: "))

# Se calcula con una operacion y te da el resludado:
Fahrenheit = celcius * 9 / 5 + 32
print(f"{celcius} °C son en °F {Fahrenheit}")