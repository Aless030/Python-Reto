#TODO pedir al usuario que ingrese una cantidad de días
dias = int(input("Ingresa una cantidad de días: "))

#TODO Calcular años semanas y días
años = dias // 365
semanas = (dias % 365) // 7
dias_restantes_semana = (dias % 365) % 7


print(f"{dias} días equivalen a {años} años, {semanas} semanas y {dias_restantes_semana} días restantes")
