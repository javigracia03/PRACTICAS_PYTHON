def calcularCapital(cantidad, interes, anos):




    capital = cantidad * (1 + interes) ** anos

    print(f"El capital obtenido en {anos} años con una inversión de {interes} es {capital}")


cantidad = float(input("Introduce la cantidad a invertir: "))
interes = float(input("Introduce el interés anual: "))
anos = int(input("Introduce el número de años: "))

calcularCapital(cantidad, interes, anos)