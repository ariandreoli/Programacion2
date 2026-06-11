from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

imagenpil = Image.open("maki.jpg")
imagen = np.array(imagenpil)


def convertgrises(img):
    R = img[:, :, 0]
    G = img[:, :, 1]
    B = img[:, :, 2]
    return R * 0.2989 + G * 0.5870 + B * 0.1140


imagengris = convertgrises(imagen)

plt.imshow(imagen)
plt.title("Imagen Original a color")
plt.show()

plt.imshow(imagengris, cmap="gray")
plt.title("Imagen a Gris")
plt.show()
