import cv2
import os
import numpy as np
import pickle
import random

DATADIR = r"C:\Users\bengr\Documents\Programs\GTA-Auto-Better\training_data"
CATEGORIES = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"]

def highlight(image_array):
    for y in range(len(image_array)):
        for x in range(len(image_array[0])):
            if image_array[y][x] < 40:
                image_array[y][x] = 0
            else:
                image_array[y][x] = 1 #255
    return image_array

training_data = []
for category in CATEGORIES:
    path = os.path.join(DATADIR, category)
    class_num = int(category) #format(int(category), "b")
    '''
    while len(class_num) < 5:
        class_num = "0" + class_num
    '''
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
    '''
    bin_string = []
    for char in sets[1]:
        bin_string.append(float(char))
    label.append(bin_string)
    '''
data = np.array(data)
label = np.array(label)
pickle.dump(data, open(r"C:\Users\bengr\Documents\Programs\GTA-Auto-Better\pickles\data.p", "wb"))
pickle.dump(label, open(r"C:\Users\bengr\Documents\Programs\GTA-Auto-Better\pickles\label.p", "wb"))
