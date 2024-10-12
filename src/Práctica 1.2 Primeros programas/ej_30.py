"""El incremento y el total deben ser mayores que cero. Si no es así, el programa debe finalizar con un error o obligar a que introduzcan
 un valor correcto para ambos (os lo dejo a vuestra elección, la primera opción es más fácil, aunque el mundo está lleno de valientes).
Por ejemplo, si introducen los valores 1, 1 y 10, el programa mostrará en consola exactamente lo siguiente: SERIE => 1-2..3..4..5..6..7..8..9-10
"""


# Solicitar el inicial, incremento y el total:
inicial = int(input("¿En que numero quieres comenzar? →"))
incremento = int(input("¿Por cuánto quieres incrementa? → "))
total = int(input("¿Hasta cuánto lo quieres incrementar? → "))

# Validar que los tres valores sean mayores que cero:
while incremento <= 0 or total <= 0 or inicial <= 0:
    print("EL VALOR NO PUEDE SER MENOR O IGUAL A 0")
    inicial = int(input("¿En que numero quieres comenzar? →"))
    incremento = int(input("Ingresa el número que quieres incrementar → "))
    total = int(input("¿Hasta cuánto lo quieres incrementar? → "))

serie = str(inicial)

# Al principio use una serie... pero tuve complicaciones y decidi usar el while:
while inicial < total:
    inicial = inicial + incremento
    if inicial <= total:
        serie = serie + "-" + str(inicial)
    else:
        serie = serie + ".." + str(total)
print(f"SERIE => {serie}")