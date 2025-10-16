#CALCULADORA
# Programa: Calculadora básica en Python
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

# El usuario elige la operación
opcion = input("Elige una opción (1-4): ")

# Pide los dos números
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

# Realiza la operación según la opción
if opcion == "1":
    resultado = num1 + num2
    print("La suma es:", resultado)
elif opcion == "2":
    resultado = num1 - num2
    print("La resta es:", resultado)

elif opcion == "3":
    resultado = num1 * num2
    print("La multiplicacion es:", resultado)

else:
    resultado = num1 / num2
    print("La division es", resultado)







