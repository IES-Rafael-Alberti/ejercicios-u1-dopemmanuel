"""La funcion principal:"""
def ask_name(nom):

    """La variable con los datos se transforma en los datos de la funcion:"""
    return nom

def main():
    """Funcion Main"""
    print("Este programa va a preguntar por tu nombre ")
    nom = input("Escribe tu nombre: ")
    print(f"Hola {ask_name(nom)}!!")


if __name__ == "__main__":
    main()
