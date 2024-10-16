"""Escribe un programa para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total del servicio."""

# Pedira las horas y el coste:
horas = int(input("Ingresa las horas que has trabajado: "))
coste = int(input("Ingrese el coste por horas: "))

# Se multipican:
multi = horas * coste

# Inprimira el resultado:
print(f"Horas de trabajo: {horas}\nCoste por hora: {coste}\nImporte total: {multi}")
