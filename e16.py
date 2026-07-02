from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open("maki.jpg")
M = np.array(img)

plt.imshow(M)
plt.title("Imagen Original")
plt.show()

def gris(imagen):

    filas = imagen.shape[0]
    columnas = imagen.shape[1]

G = np.zeros((filas, columnas), dtype=int)

    for i in range(filas):
        for j in range(columnas):

            r = imagen[i][j][0]
            g = imagen[i][j][1]
            b = imagen[i][j][2]

            G[i][j] = 0.299*r + 0.587*g + 0.114*b

    return G

grisimg = gris(M)

plt.imshow(grisimg, cmap="gray")
plt.title("Escala de Grises")
plt.show()