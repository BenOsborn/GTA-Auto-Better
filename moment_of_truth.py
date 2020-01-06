from auto_better_framework import classification
from weights_and_biases import *
from PIL import Image, ImageOps
import numpy as np

img = Image.open(r"C:\Users\bengr\Documents\Programs\GTA-Auto-Better\training_data\n44.jpg")
img1 = ImageOps.grayscale(img)
img_pixels = np.array(img1)

print(classification(img_pixels, weight_set1, b1, weight_set2, b2, weight_set3, b3))
