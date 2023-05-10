import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("road.jpg")

#a)
lighterImg = img+150
lighterImg[lighterImg < 150] = 255
plt.imshow(lighterImg, cmap="gray")
plt.title("Light cesta")
plt.show()

#b)
quarterImg = img[:, int(img.shape[1]/4):int(img.shape[1]/2)]
plt.imshow(quarterImg, cmap="gray")
plt.title("Sliceana cesta")
plt.show()

#c)
rotated_img = np.rot90(img, k=-1)
plt.imshow(rotated_img)
plt.show()

#d)
mirrorImg = np.flip(img, axis=1)
plt.imshow(mirrorImg, cmap="gray")
plt.title("Zrcaljena cesta")
plt.show()
