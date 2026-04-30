import random
numsecreto = random.randint(1, 21)
num=0
intentos=6

print('Adivina el número secreto entre 1 y 20')
print('Tienes', intentos, 'intentos')

for i in range(1, intentos+ 1):
    num=int(input('Ingresa un número: '))

    if num == numsecreto:
        print('¡Felicidades! Adivinaste el número')
    else:
        if (num < numsecreto):
            print('El número secreto es mayor')
        else:
            print('El número secreto es menor')

    if (intentos < 6):
        print("Se acabaron los intentos.")
        print("El número secreto era: ", numsecreto)