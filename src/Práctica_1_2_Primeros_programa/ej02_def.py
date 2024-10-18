"""Este va a organizarte tus horas trabajadas:"""

def calcular_importe_trabajado(horas, coste):
    """Pedira los numeros"""
    print("Escribe un programa para pedirle al usuario las horas de trabajo"
          "y el precio por hora y calcule el importe total del servicio.")

    multi = horas * coste
    info = f"Horas de trabajo: {horas}\nCoste por hora: {coste}\nImporte total: {multi}"
    return info

def main():

    horas = int(input("Ingresa las horas que has trabajado: "))
    coste = int(input("Ingrese el coste por horas: "))
    results = calcular_importe_trabajado(horas, coste)

    print(results)
if __name__ == "__main__":
    main()
