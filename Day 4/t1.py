def suma_numeros_positivos(lista):
    suma = 0
    for numero in lista:
        if numero > 0:
            suma += numero
    return suma

print(suma_numeros_positivos([1, 2, 3, 5, 5]))