from auto_better_framework import training, classification, classification_for_training
from PIL import Image, ImageOps
import numpy as np
import os
import logging

logging.basicConfig(filename="weights_and_biases.py", level=logging.DEBUG, format="%(message)s")

weight_set1 = [np.random.uniform(size=625)]
b1 = np.random.uniform(size=1)
weight_set2 = []
for _ in range(16):
    weight_set2.append(np.random.uniform(size=8))
b2 = np.random.uniform(size=1)
weight_set3 = [np.random.uniform(size=16)]
b3 = np.random.uniform(size=1)

image_files = []
for files in os.walk(r"C:\Users\bengr\Documents\Programs\GTA-Auto-Better\training_data"):
    for file in files[2]:
        image_files.append(file)

classified = [0.26, 0.20, 0.3, 0.12, 0.5, 0.7, 0.3, 0.6, 0.26, 0.12, 0.4, 0.24, 0.15, 0.12, 0.21, 0.29, 0.1, 0.1, 0.4, 0.1, 0.27, 0.12, 0.21, 0.9, 0.16, 0.5, 0.4, 0.9, 0.12, 0.23, 0.17, 0.4, 0.4, 0.14, 0.8, 0.26, 0.22, 0.9, 0.2, 0.4, 0.9, 0.25, 0.7, 0.7, 0.25, 0.4, 0.24, 0.1]

for _ in range(100):
    for i in range(len(image_files)):
        img = Image.open(r"C:\Users\bengr\Documents\Programs\GTA-Auto-Better\training_data\n" + str(i + 1) + ".jpg")
        img = ImageOps.grayscale(img)
        img = np.array(img)
        training(img, weight_set1[0], b1, weight_set2, b2, weight_set3[0], b3, 0.5, classified[i])
        with open("weights_and_biases.py", "r+") as file:
            file.seek(0)
            file.truncate(0)

            logging.info("import numpy as np")
            logging.info(weight_set1)
            logging.info(b1)
            logging.info(weight_set2)
            logging.info(b2)
            logging.info(weight_set3)
            logging.info(b3)
