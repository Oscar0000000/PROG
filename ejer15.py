anyio = int(input("Introduce un año:"))
if (anyio % 4 == 0 and anyio % 100 == 0) or (anyio % 400 == 0):
    print("El año", anyio, "Es bisiesto")

else:
    print("El año", anyio, "no es bisiesto")
