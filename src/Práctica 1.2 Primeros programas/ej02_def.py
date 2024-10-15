"""Este va a organizarte tus horas trabajadas:"""

def calcular_importe_trabajado():
    """Pedira los numeros"""

    horas = int(input("Ingresa las horas que has trabajado: "))
    coste = int(input("Ingrese el coste por horas: "))

    multi = horas * coste
    info = f"Horas de trabajo: {horas}\nCoste por hora: {coste}\nImporte total: {multi}"
    return info


if __name__ == "__main__":
    print("Escribe un programa para pedirle al usuario las horas de trabajo"
          "y el precio por hora y calcule el importe total del servicio.")

    print(calcular_importe_trabajado())
