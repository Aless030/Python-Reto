def numeros_pares(lista):
    pares = [x for x in lista if x % 2 == 0]
    return pares

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = numeros_pares(numeros)
print("Números pares:", pares)
