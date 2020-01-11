import numpy as np
import os
import cv2
import random
import pickle
import math

DATADIR = r"C:\Users\bengr\Documents\Programs\GTA-Auto-Better\training_data"
CATEGORIES = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"]

def highlight(image_array):

    for y in range(len(image_array)):
        for x in range(len(image_array[0])):
            if image_array[y][x] < 40:
                image_array[y][x] = 0
            else:
                image_array[y][x] = 255

    return image_array

def create_training_data():

    training_data = []
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)
        class_num = format(int(category), "b")
        while len(class_num) < 5:
            class_num += "0"
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                #img_array = cv2.Canny(img_array, 100, 200)
                img_array = highlight(img_array)
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

    choice_set = [-1, 1]
    kernels = []
    for _ in range(4):
        kernel_set1 = []
        for _ in range(4):
            kernel_set1.append([random.choice(choice_set)/255, random.choice(choice_set)/255, random.choice(choice_set)/255, random.choice(choice_set)/255])
        kernels.append(kernel_set1)
    for _ in range(4):
        kernel_set2 = []
        for _ in range(4):
            kernel_set2.append([random.choice(choice_set), random.choice(choice_set), random.choice(choice_set), random.choice(choice_set)])
        kernels.append(kernel_set2)
    for _ in range(3):
        kernel_set3 = []
        for _ in range(3):
            kernel_set3.append([random.choice(choice_set), random.choice(choice_set), random.choice(choice_set)])
        kernels.append(kernel_set3)

    pickle_out = open("data.pickle", "wb")
    pickle.dump(data, pickle_out)
    pickle_out.close()
    pickle_out = open("label.pickle", "wb")
    pickle.dump(label, pickle_out)
    pickle_out.close()
    pickle_out = open("kernels.pickle", "wb")
    pickle.dump(kernels, pickle_out)
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

def classify(image, kernels):

    #Arrangement of first pixels
    arranged1 = []
    for y in range(45):
        square_row1 = []
        for x in range(53):
            pixel_row1 = [image[y][x:x+4], image[y+1][x:x+4], image[y+2][x:x+4], image[y+3][x:x+4]]
            square_row1.append(pixel_row1)
        arranged1.append(square_row1)
    arranged1 = np.array(arranged1)

    #print(arranged1[20][7])

    #Create kerneled image sets for first layer
    kerneled_images1 = []
    for a in range(4):
        kerneled1_pixels = []
        for y in range(45):
            kerneled_row1 = []
            for x in range(53):
                value = 0
                for i in range(4):
                    value += np.dot(arranged1[y][x][i], kernels[a][i])
                kerneled_row1.append(relu(value)/16)
            kerneled_row1.append(0)
            kerneled1_pixels.append(kerneled_row1)
        kerneled1_pixels.append(np.zeros(54))
        kerneled_images1.append(kerneled1_pixels)
    kerneled_images1 = np.array(kerneled_images1)

    #Pooling layer 1
    pooled_images1 = []
    for pic in kerneled_images1:
        pooled_image1 = []
        for y in range(23):
            pooled_row1 = []
            for x in range(27):
                pooled_pixel = pool([pic[y*2][x*2], pic[y*2][x*2+1], pic[y*2+1][x*2], pic[y*2+1][x*2+1]])
                pooled_row1.append(pooled_pixel)
            pooled_image1.append(pooled_row1)
        pooled_images1.append(pooled_image1)
    pooled_images1 = np.array(pooled_images1)

#create_training_data()
data = pickle.load(open("data.pickle", "rb"))
label = pickle.load(open("label.pickle", "rb"))
kernels = pickle.load(open("kernels.pickle", "rb"))

classify(data[3], kernels)
