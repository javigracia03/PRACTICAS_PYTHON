
edad = int(input("Introduce tu edad: "))

if edad > 30:
    precio = 0
elif edad >= 18 and edad <= 25:
    precio = 5
else: precio = 0


print(f"El precio de tu entrada es de {precio} €")
