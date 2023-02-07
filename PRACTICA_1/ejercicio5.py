

def calcularPaga(coste,horas):
    print("La paga que le corresponde es de", coste*horas, "€")


horas = float(input("¿Cuantas horas has trabajado?"))

coste = float(input("¿Cuánto cuesta cada hora?"))
calcularPaga(coste,horas)