
nombre = input("Introduce tu nombre: ")
sexo = input("Introduce tu sexo (H o M): ")

if (sexo == "M" and nombre < "M") or (sexo == "H" and nombre >= "N"):
    grupo = "A"
else:
    grupo = "B"


print(f"Perteneces al grupo {grupo}")