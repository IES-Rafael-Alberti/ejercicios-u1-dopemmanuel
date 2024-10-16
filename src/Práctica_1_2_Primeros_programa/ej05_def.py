""" LA funcion"""
def importes():
    """Esto te pedira el importe con y sin IVA:"""

    sin_iva = float(input("Ingrese el importe sin IVA de su articulo: "))
    con_iva = int(input("Ingrese el porciento de IVA al aplicar: "))

    divi = sin_iva * (con_iva / 100)
    multi =  sin_iva + divi
    result = f"Su Importe es de {sin_iva}€ \nEl tipo de IVA a aplicar es de {con_iva}% \nEl precio fina del articulo es de {multi}€"


    return result

if __name__ == "__main__":
    print("Escribe un programa que pida el importe sin IVA de un artículo y el "
          "tipo de IVA a aplicar  y calcule e imprima por pantalla el precio final del artículo")

    print(importes())
