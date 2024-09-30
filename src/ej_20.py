"""Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, 
y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con 
este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión."""

while True:
    try:
        n = "+34-913724710-56"
        n.count("")
        prefijo = int(input("Coloca el prefijo: "))

        if prefijo != n[0:3]:
            print("Coloca un prefijo valido")
        else:
            print("OK")
    
        number = int(input("Ingrese el numero de telefono: "))