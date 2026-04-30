def converaf(c):
    return c * 9/5 + 32

def fahrac(f):
    return (f - 32) * 5/9

temp = int(input('Ingresá la temperatura: '))
opcion = input('Convertir a (F)ahrenheit o (C)elsius: ')

if opcion == 'F' or opcion == 'f':
    print("Resultado:", converaf(temp))

if opcion == 'C' or opcion == 'c':
    print("Resultado:", fahrac(temp))

if opcion != 'F' and opcion != 'f' and opcion != 'C' and opcion != 'c':
    print('Opción inválida')