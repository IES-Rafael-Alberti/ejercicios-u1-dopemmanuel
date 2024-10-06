"""Escribe un programa que pida el nombre del usuario para luego darle la bienvenida."""
def ask_name(): #La funcion principal:

    nom = input("Escribe tu nombre: ")
    return nom #La variable con los datos se transforma en los datos de la funcion:

if __name__ == "__main__":
    print("Este programa va a preguntar por tu nombre ") #El titulo... tengo que recordar en colocarlo afuera del if name....


    name = ask_name() # Y es reutilizada fueda de la funcion.
    print(f"Hola {name}!!")