import math
def areacirculo(radio):
    return math.pi * radio ** 2

def volumencilin(radio, altura):
    area = areacirculo(radio)  
    return area * altura

r = int(input("Ingresa el radio: "))
h = int(input("Ingresa la altura: "))

volumen = volumencilin(r, h)

print("El volumen del cilindro es:", volumen)