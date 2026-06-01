M = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

suma = 0
mult = 1

contrasuma = 0
contramult = 1

for i in range(4):
    suma=suma + M[i][i]
    mult=mult * M[i][i]

    contrasuma=contrasuma + M[i][3-i]
    contramult=contramult * M[i][3-i]

print('Elementos de la matriz:')

for i in range(4):
    for j in range(4):
        print(M[i][j], end='')
    print()

print()
print('Suma diagonal :', suma)
print('Multiplicacion diagonal : ', mult)

print('Suma contra diagonal: ', contrasuma)
print('Multiplicacion contra diagonal: ', contramult)