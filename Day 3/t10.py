def suma_digitos(numero):
    suma = 0
    while numero > 0:
        suma += numero % 10
        numero //= 10
    return suma

numero = int(input("Ingresa un número: "))
resultado = suma_digitos(numero)
print("La suma de dígitos de", numero, "es", resultado)
