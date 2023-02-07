
def sumaPositivos(entero):  
    suma = 0
    for i in range(1, entero + 1):
        suma += i
    print("La suma de los números enteros desde 1 hasta", entero, "es", suma)

entero = int(input("Dime un entero"))
sumaPositivos(entero)