def es_palindromo(cadena):
    cadena = cadena.lower()  # Convertirmos a minúsculas
    return cadena == cadena[::-1]

print(es_palindromo("Ana"))