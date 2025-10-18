n = int(input("Introduce el número al que le quieres calcular el factorial: "))
fact = 1
for i in range(1,n+1):
    fact = fact*i
print(f"El factorial de {n} es {fact}")
