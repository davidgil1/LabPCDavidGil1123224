import turtle
import textwrap
def pedir_nombre():
    while True:
        nombre = input("Por favor, ingresa tu nombre: ")
        if nombre.strip():  # Verifica que el nombre no esté vacío
            return nombre
        else:
            print("El nombre no puede estar vacío. Por favor, inténtalo de nuevo.")
