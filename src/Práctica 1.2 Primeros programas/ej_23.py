"""Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla 
otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es."""

correo = input("Introduce tu correo: ")
nombre_usuario = correo.split("@")[0]
New_email = nombre_usuario + "@ceu.es"
print(New_email)