from PIL import Image
import numpy as np

imag = Image.open("maki.jpg")

imagris = imag.convert("L")

m = np.array(imagris)

imagris.show()

filas = len(m)
columnas = len(m[0])

volteada = m.copy()

for f in range(filas):
    for i in range(columnas):
        j = columnas - 1 - i
        volteada[f][j] = m[f][i]

imavolteada = Image.array(volteada)

imavolteada.show()

