
#TODO pedir al usuario que ingrese una cadena
cadena = input("Ingresa una cadena: ")

# TODO  verificar si una cadena es un palíndromo
def es_palindromo(cadena):
    cadena = cadena.lower()  # Convertir a minúsculas para ser insensible a mayúsculas
    cadena = cadena.replace(" ", "")  # Eliminar espacios en blanco
    return cadena == cadena[::-1]

# TODO es un palíndromo o no
if es_palindromo(cadena):
    print(f"{cadena} es un palíndromo.")
else:
    print(f"{cadena} no es un palíndromo.")
