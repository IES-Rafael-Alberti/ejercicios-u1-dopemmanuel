"""Escribe un programa para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total del servicio."""

def calcular_importe_trabajado():

    horas = int(input("Ingresa las horas que has trabajado: "))
    coste = int(input("Ingrese el coste por horas: "))

    # El calculo ↓
    multi = horas * coste

    # Lo aplicara a la funcion, devolviendolo
    return horas, coste, multi #Olvide que eso es muy delicado, aqui el orden importa y deben coincidir ↓

if __name__ == "__main__":
    print("Este va a organizarte tus horas trabajadas:")

    #Se llaman las variables devolvidas fuera... bueno seria su resultado
    horas_trabajadas, coste_horas, calulo = calcular_importe_trabajado() # el orden debe de coincicir como el de arriba pero no con el mismo nombre,  ↑

    print(f"Horas de trabajo: {horas_trabajadas}\nCoste por hora: {coste_horas}\nImporte total: {calulo}")