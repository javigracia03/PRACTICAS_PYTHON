def calcularCapital(cantidad, interes, anos):



    interes = interes /100
    capital = cantidad * (interes + 1) ** anos
  

    print(f"El capital obtenido en {anos} años con un interes de {interes} es {capital}")


cantidad = float(input("Introduce la cantidad a invertir: "))
interes = float(input("Introduce el interés anual en %: "))
anos = int(input("Introduce el número de años: "))

calcularCapital(cantidad, interes, anos)