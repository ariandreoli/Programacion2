def factorial(num):
    resultado = 1
    for i in range(1, num + 1):
        resultado *= i
    return resultado


num = int(input('Ingresa un número entero positivo: '))

while num < 0:
    print('Error, debe ser positivo')
    n = int(input('Ingresa un número entero positivo: '))

print('Factorial: ', factorial(num))