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
                img_array = cv2.resize(img_array, (14, 12), interpolation=cv2.INTER_AREA)
                training_data.append([img_array, class_num])
            except:
                pass

    training_data = sorted(training_data, key=lambda k: random.random())

    data = []
    label = []
    for sets in training_data:
        data.append(sets[0])
        bin_string = []
        for char in sets[1]:
            bin_string.append(float(char))
        label.append(bin_string)

    kernel1 = []
    for _ in range(5):
        kernel1.append([random.randrange(-1, 2), random.randrange(-1, 2), random.randrange(-1, 2), random.randrange(-1, 2), random.randrange(-1, 2)])
    kernel2 = []
    for _ in range(3):
        kernel2.append([random.randrange(-1, 2), random.randrange(-1, 2), random.randrange(-1, 2)])

    pickle_out = open("data.pickle", "wb")
    pickle.dump(data, pickle_out)
    pickle_out.close()
    pickle_out = open("label.pickle", "wb")
    pickle.dump(label, pickle_out)
    pickle_out.close()
    pickle_out = open("kernel1.pickle", "wb")
    pickle.dump(kernel1, pickle_out)
    pickle_out.close()
    pickle_out = open("kernel2.pickle", "wb")
    pickle.dump(kernel2, pickle_out)
    pickle_out.close()

def relu(x):
    return max(0,x)

def relud(x):
    if x <= 0:
        return float(0)
    else:
        return float(1)

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def sigmoidd(x):
    return (1 / (1 + math.exp(-x)))*(1 - (1 / (1 + math.exp(-x))))

def pool(square):
    sorted = np.sort(square, kind="quicksort")
    return sorted[-1]

#create_training_data()

data = pickle.load(open("data.pickle", "rb"))
label = pickle.load(open("label.pickle", "rb"))
kernel1 = pickle.load(open("kernel1.pickle", "rb"))
kernel2 = pickle.load(open("kernel2.pickle", "rb"))

def classify(image_pixels, kernel1, kernel2):

    #Convolution layer 1
    reshaped_array1 = []
    weighted_pixel_net_array1 = []
    weighted_pixel_relu_array1 = [] #Main output layer
    for y in range(7):
        square_row = []
        weighted_pixel_net_row1 = []
        weighted_pixel_relu_row1 = []
        for x in range(10):
            square = [image_pixels[y][x:x+5], image_pixels[y+1][x:x+5], image_pixels[y+2][x:x+5], image_pixels[y+3][x:x+5], image_pixels[y+4][x:x+5]]
            weighted_pixel_net1 = (np.dot(square[0], kernel1[0]) + np.dot(square[1], kernel1[1]) + np.dot(square[2], kernel1[2]) + np.dot(square[3], kernel1[3]) + np.dot(square[4], kernel1[4]))/25
            weighted_pixel_relu1 = relu(weighted_pixel_net1)
            square_row.append(square)
            weighted_pixel_net_row1.append(weighted_pixel_net1)
            weighted_pixel_relu_row1.append(weighted_pixel_relu1)
        reshaped_array1.append(square_row)
        weighted_pixel_net_array1.append(weighted_pixel_net_row1)
        weighted_pixel_relu_array1.append(weighted_pixel_relu_row1)

    #Pooling layer
    weighted_pixel_relu_array1.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) #Adding padding layer
    pooled_array = []
    for y in range(4):
        pooled_row = []
        for x in range(5):
            square = [weighted_pixel_relu_array1[y*2][2*x], weighted_pixel_relu_array1[y*2][2*x+1], weighted_pixel_relu_array1[y*2+1][2*x], weighted_pixel_relu_array1[y*2+1][2*x+1]]
            pooled_row.append(pool(square)) #Somehow going to have to connect the corrected weight to its original matrice that created it while disregarding the others
        pooled_array.append(pooled_row)

    #Convolutional layer 2
    reshaped_array2 = []
    weighted_pixel_net_array2 = []
    weighted_pixel_relu_array2 = []
    flattened_layer = []
    for y in range(2):
        square_row = []
        weighted_pixel_net_row2 = []
        weighted_pixel_relu_row2 = []
        for x in range(3):
            square = [pooled_array[y][x:x+3], pooled_array[y+1][x:x+3], pooled_array[y+2][x:x+3]]
            weighted_pixel_net2 = (np.dot(square[0], kernel2[0]) + np.dot(square[1], kernel2[1]) + np.dot(square[2], kernel2[2]))/9
            weighted_pixel_relu2 = relu(weighted_pixel_net2)
            square_row.append(square)
            weighted_pixel_net_row2.append(weighted_pixel_net2)
            weighted_pixel_relu_row2.append(weighted_pixel_relu2)
            flattened_layer.append(weighted_pixel_relu2)
        reshaped_array2.append(square_row)
        weighted_pixel_net_array2.append(weighted_pixel_net_row2)
        weighted_pixel_relu_array2.append(weighted_pixel_relu_row2)

    print(flattened_layer)

classify(data[0], kernel1, kernel2)
