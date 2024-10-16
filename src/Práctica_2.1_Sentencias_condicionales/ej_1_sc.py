"""Hola"""
def adult_swim():

    edad = int(input("Cual es tu edad? → "))

    while edad != int(edad):
        print("Solo se acepta valores de caracter numerico..")
        edad = int(input("Cual es tu edad? → "))

    if edad < 17:
        print("Eres menor de edad")
    else:
        print("eres mayor de edad")

if __name__ == "__main__":
    print("Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.\n")
    adult_swim()