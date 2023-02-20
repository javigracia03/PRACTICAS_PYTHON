
precio = input("Dime el precio con 2 decimales ")

posicion = precio.find(".")


euros = precio[:posicion]
centimos = precio[posicion+1:]

print("El precio es de", euros, "euros y", centimos, "céntimos.")
