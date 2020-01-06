from auto_better_framework import classification
from weights_and_biases import *
from PIL import Image, ImageOps
import numpy as np

img = Image.open(r"C:\Users\bengr\Documents\Programs\GTA-Auto-Better\training_data\n20.jpg")
img1 = ImageOps.grayscale(img)
img1_pixels = np.array(img1)

img = Image.open(r"C:\Users\bengr\Documents\Programs\GTA-Auto-Better\training_data\n21.jpg")
img2 = ImageOps.grayscale(img)
img2_pixels = np.array(img2)

img_difference = np.subtract(img2_pixels, img1_pixels)
img_difference = Image.fromarray(img_difference)

print(classification(img1_pixels, weight_set1, b1, weight_set2, b2, weight_set3, b3))
