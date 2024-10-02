"""n = str("+34-913724710-56")
print(n[13:15]




while True:
    try:
        pref = "+34"
        num = "913724710"
        ext = "56"
        
        #1
        a = input("Ingresa el prefijo: ")
        if len(a) != len(pref) or a != pref:
            print("La extension es incorrecta (￣へ￣()")
        else:
            continue
        #2
        b = input("Ingresa el numero del telefono: ")
        if len(b) != len(num):
            print("Faltan numeros (￣へ￣()")
        else:
            continue
        #3
        c = input("Ingresa la extension")
        if len(c) != len(ext):
            print("Error, esa extencion no vale (￣へ￣()")
        else:
            print(f"{a}-{b}-{c}")
    except ValueError:
        print("Carajo!! Solo se pude poner numero aqui (￣へ￣()")



"""

