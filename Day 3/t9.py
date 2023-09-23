def contar_palabras_largas(palabras):
    contador = 0
    for palabra in palabras:
        if len(palabra) > 5:
            contador += 1
    return contador

palabras = ["manzana", "banana", "uva", "sandía", "kiwi"]
contador = contar_palabras_largas(palabras)
print("Cantidad de palabras con más de cinco caracteres:", contador)
