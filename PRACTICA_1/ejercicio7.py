

def imc(peso, estatura):
    imc = peso / (estatura ** 2)
    imc = round(imc, 2)

    print("Tu índice de masa corporal es", imc)

peso = float(input("Introduce tu peso en kg: "))
estatura = float(input("Introduce tu estatura en metros: "))

imc(peso, estatura)