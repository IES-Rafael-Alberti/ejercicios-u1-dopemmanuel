"""La funcion principal:"""
def ask_name():

    """La variable con los datos se transforma en los datos de la funcion:"""
    nom = input("Escribe tu nombre: ")
    return nom

if __name__ == "__main__":
    print("Este programa va a preguntar por tu nombre ")

    name = ask_name()
    print(f"Hola {name}!!")
