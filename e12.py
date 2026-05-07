import random

estudiantes = ["Xavier", "Solange", "Mia", "Exequiel", "Morena"]
orden = []

for i in range(len(estudiantes)):
    alumnos = estudiantes.pop(random.randint(0, len(estudiantes) - 1))
    orden.append(alumnos)

print('Orden de exposición: ')
for i in range(len(orden)):
    print(orden[i])