#TRIANGULO
a = float(input("Introduce un primer lado"))
b = float(input("Introduce un segundo lado"))
c = float(input("Introduce un tercer lado"))
if a + b > c and a + c > b and b + c > a:
    print("Se puede formar un triangulo")

if a == b == c:
     triangulo = "equilátero"

elif a == b != c or a != b == c or a == c != b:
     triangulo = "isosceles"

elif a != b != c :
    triangulo= "escaleno"

else:
    print("No se puede formar un triangulo")
print("El triangulo es", triangulo)

     


