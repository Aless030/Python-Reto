def nombres_con_a(nombres):
    nombres_a = [nombre for nombre in nombres if nombre.startswith('A')]
    return nombres_a

nombres = ["Ana", "Carlos", "David", "Alberto", "Eva"]
nombres_a = nombres_con_a(nombres)
print("Nombres que comienzan con 'A':", nombres_a)
