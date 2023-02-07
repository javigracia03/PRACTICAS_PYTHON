
def division(n,m):
    c = n // m
    r = n % m

    print(f"{n} entre {m} da un cociente {c} y un resto {r}")

n = int(input("Introduce el primer número entero: "))
m = int(input("Introduce el segundo número entero: "))

division(n, m)