#FUNCION PAR IMPAR
def par_impar(n):
    if n % 2 == 0:
        return("El numero es par")
    else:
        return("El numero es impar")

n = int(input("Introduce un numero:"))
print(par_impar(n))
