#PROMEDIO DE NUMEROS INTRODUCIDOS
suma_total = 0
contar_numeros = 0
while True:
    n = input("Introduce un numero, Tecla Enter para terminar:")
    
    if n == "":
        break

    n =float(n)
suma_total += 1
contar_numeros += 1

if contar_numeros > 0:
    promedio = suma_total / contar_numeros
print(f"El promedio total es {promedio}")
