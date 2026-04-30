div=0
sobran=0
caram = int(input("Ingrese la cantidad de caramelos: "))
estudiantes = int(input("Ingrese la cantidad de estudiantes: "))

div = caram // estudiantes
sobran = caram % estudiantes


print("A cada estudiante le tocan:",div , "caramelos")
print("Sobran en la bolsa:", sobran, "caramelos")