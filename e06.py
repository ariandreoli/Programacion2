bille1000=0
bille200=0
saldo=0
monto = int(input("Ingrese el monto que desea extraer: "))

bille1000 = monto // 1000
resto = monto % 1000

bille200 = resto // 200
saldo = resto % 200

print("Billetes de $1000:", bille1000)
print("Billetes de $200:", bille200)
print("Saldo no entregado:", saldo)