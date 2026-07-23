from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open("maki.jpg").convert("L")
M = np.array(img, dtype=float)

K = np.array([[1, 2, 1],
              [2, 4, 2],
              [1, 2, 1]], dtype=float)

F = np.zeros(M.shape)

for i in range(1, M.shape[0]-1):
    for j in range(1, M.shape[1]-1):
        suma = 0

        for ki in range(3):
            for kj in range(3):
                suma = suma + M[i-1+ki, j-1+kj] * K[ki, kj]

        F[i, j] = suma / 16

plt.imshow(M, cmap="gray")
plt.title("Imagen original")
plt.axis("off")
plt.show()

plt.imshow(F, cmap="gray")
plt.title("Imagen filtrada")
plt.axis("off")
plt.show()

#el .axis nos va a sacar los ejes