
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))


if num2 == 0:
    print("Error: no se puede dividir por cero")
else:
    
    resultado = num1 / num2
    print(f"{num1} / {num2} es {resultado}")
