import numpy as np
import os
import cv2
import random
import pickle
import math

DATADIR = r"C:\Users\bengr\Documents\Programs\GTA-Auto-Better\training_data"
CATEGORIES = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"]

def create_training_data():

    training_data = []
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)
        class_num = format(int(category), "b")
        while len(class_num) < 5:
            class_num = "0" + class_num
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                training_data.append([img_array, class_num])
            except:
                pass

    training_data = sorted(training_data, key=lambda k: random.random())

    x = []
    y = []
    for sets in training_data:
        x.append(sets[0])
        bin_string = []
        for char in sets[1]:
            bin_string.append(float(char))
        y.append(bin_string)

    pickle_out = open("x.pickle", "wb")
    pickle.dump(x, pickle_out)
    pickle_out.close()
    pickle_out = open("y.pickle", "wb")
    pickle.dump(y, pickle_out)
    pickle_out.close()

    return [x, y]

def relu(x):
    return max(0.1*X, x)

def relud(x):
    if x <= 0:
        return float(0.1)
    else:
        return float(1)

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def sigmoidd(x):
    return (1 / (1 + math.exp(-x)))*(1 - (1 / (1 + math.exp(-x))))

def classify_training():
