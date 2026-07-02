from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open("maki.jpg")

M = np.array(img)

def rotar(imagen, op):

    if op == 1:      
        R = np.rot90(imagen)

    elif op == 2:    
        R = np.rot90(imagen, -1)

    elif op == 3:    
        R = np.rot90(imagen, 2)

    return R

print("1 - 90° izquierda")
print("2 - 90° derecha")
print("3 - 180°")

op = int(input("Elija una opción: "))

result= rotar(M, op)

plt.imshow(M)
plt.title("Imagen original")
plt.show()

plt.imshow(result)
plt.title("Imagen rotada")
plt.show()