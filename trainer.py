from auto_better_framework import training
from PIL import Image, ImageOps
import os
import numpy as np

weight_set1 = []
for _ in range(8):
    weight_set1.append(np.random.uniform(size=625))
b1 = [np.random.uniform(size=1)]
weight_set2 = []
for _ in range(16):
    weight_set2.append(np.random.uniform(size=8))
b2 = [np.random.uniform(size=1)]
weight_set3 = np.random.uniform(size=16)
b3 = [np.random.uniform(size=1)]

image_files = []
for files in os.walk(r"C:\Users\bengr\Documents\Programs\GTA-Auto-Better\training_data"):
    for file in files[2]:
        image_files.append(file)

classified = [26, 20, 3, 12, 5, 7, 3, 6, 26, 12, 4, 24, 15, 12, 21, 29, 1, 1, 4, 1, 27, 12, 21, 9, 16, 5, 4, 9, 12, 23, 17, 4, 4, 14, 8, 26, 22, 9, 2, 4, 9, 25, 7, 7, 25, 4, 24, 1]

print("Old weights and biases:")
#print(weight_set1)
print(b1)
print(weight_set2)
print(b2)
print(weight_set3)
print(b3)

for i in range(len(image_files)):
    img = Image.open(r"C:\Users\bengr\Documents\Programs\GTA-Auto-Better\training_data\n" + str(i + 1) + ".jpg")
    img = ImageOps.grayscale(img)
    img = np.array(img)
    training(img, weight_set1, b1, weight_set2, b2, weight_set3, b3, 0.5, classified[i])

print("\nNew weights and biases:")
#print(weight_set1)
print(b1)
print(weight_set2)
print(b2)
print(weight_set3)
print(b3)
