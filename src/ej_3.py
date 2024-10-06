"""
Suponiendo que se han ejecutado las siguientes sentencias de asignación:

ancho = 17
alto = 12.0
para cada una de las expresiones siguientes, intenta adivinar el valor de la expresión y su tipo sin ejecutarlas en el intérprete:

1. ancho / 2 
2. ancho // 2
3. alto / 3
4. 1 + 2 * 5

"""

def sentencias():

    ancho = 17
    alto = 12.0

    choose = int(input("Seleciona una de estas operaciones(1-4): "))

    if choose == 1 :
        opcion1 = ancho / 2
        return opcion1, None, None, None


    elif choose == 2 :
        opcion2 = ancho // 2
        return None, opcion2, None, None 

    elif choose == 3:
        opcion3 = alto / 3
        return opcion3

    elif choose == 4:
        opcion4 = 1 + 2 * 5
        return opcion4
    else:
        print("() -_-)_Esa opcion no es valida_(-_-()")

    return opcion1, opcion2, opcion3, opcion4


if __name__ == "__main__":
    print("Averiguar cual es las sentencias de asignacion: ")

op1, op2, op3, op4 = sentencias()

if op1 is not None:
    print(op1, " es un float")




"""    
print(opcion4,"es un int")
print(opcion3," es un float")
print("La opcion ", opcion2, " es un int ")
"""