anyo  = int(input("Introduce el año"))
if (anyo % 4 == 0 and anyo % 100 != 0) or anyo % 400 == 0:
    print("Bisiesto")
else:
    print("No bisiesto")
