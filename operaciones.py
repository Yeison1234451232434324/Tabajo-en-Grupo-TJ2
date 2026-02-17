# version 1.0 yeison fabian
num1 = float(input("Escribe el primer número: "))
num2 = float(input("Escribe el segundo número: "))


multiplicacion = num1 * num2


print("-" * 20)
print(f"El resultado de multiplicar {num1} por {num2} es: {multiplicacion}")


if num2 != 0:
    division = num1 / num2
    print(f"El resultado de dividir {num1} entre {num2} es: {division}")
else:
    print("No puedo dividir entre cero, ¡el universo colapsaría!")
print("-" * 20)

# version 2.0 Angel Gutierrez
num1 = float(input("Escribe el primer número: "))
num2 = float(input("Escribe el segundo número: "))
print("-" * 20)
# SUMA
suma = num1 + num2
print(f"La suma de {num1} + {num2} es: {suma}")
# RESTA
resta = num1 - num2
print(f"La resta de {num1} - {num2} es: {resta}")
print("-" * 20)