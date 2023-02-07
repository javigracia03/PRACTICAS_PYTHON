def calcularPeso():
    papa_pig = 112
    caillou = 75

    papa_pig_vendidos = int(input("Introduce el número de PapaPig vendidos: "))
    caillou_vendidos = int(input("Introduce el número de Caillou vendidos: "))

    peso_total = (papa_pig * papa_pig_vendidos) + (caillou * caillou_vendidos)

    print(f"El peso total del paquete es de {peso_total} g")

calcularPeso()