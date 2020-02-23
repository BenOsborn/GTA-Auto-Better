import cv2
import os
import numpy as np
import pickle
import random

DATADIR = os.getcwd()
CATEGORIES = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"]

def highlight(image_array):
    for y in range(len(image_array)):
        for x in range(len(image_array[0])):
            if image_array[y][x] < 40:
                image_array[y][x] = 0
            else:
                image_array[y][x] = 1
    return image_array

training_data = []
for category in CATEGORIES:
    path = os.path.join(DATADIR, category)
    class_num = int(category)
    for img in os.listdir(path):
        try:
            img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
            img_array = highlight(img_array)
            training_data.append([img_array, class_num])
        except:
            pass
training_data = sorted(training_data, key=lambda k: random.random())
data = []
label = []
for sets in training_data:
    data.append(sets[0])
    label.append(sets[1] - 1)

data = np.array(data)
label = np.array(label)
PICKLEPATH = os.path.join(DATADIR, "pickles")
pickle.dump(data, open(os.path.join(PICKLEPATH, "data.p"), "wb"))
pickle.dump(label, open(open(os.path.join(PICKLEPATH, "label.p"), "wb"))
