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

    choice_set = [-1, 1]
    kernel1 = []
    for _ in range(5):
        kernel1.append([random.choice(choice_set), random.choice(choice_set), random.choice(choice_set), random.choice(choice_set), random.choice(choice_set)])
    kernel2 = []
    for _ in range(5):
        kernel2.append([random.choice(choice_set), random.choice(choice_set), random.choice(choice_set), random.choice(choice_set), random.choice(choice_set)])
    kernel3 = []
    for _ in range(3):
        kernel3.append([random.choice(choice_set), random.choice(choice_set), random.choice(choice_set)])
    kernel4 = []
    for _ in range(3):
        kernel4.append([random.choice(choice_set), random.choice(choice_set), random.choice(choice_set)])
    kernel5 = []
    for _ in range(2):
        kernel5.append([random.choice(choice_set), random.choice(choice_set)])
    kernel6 = []
    for _ in range(2):
        kernel6.append([random.choice(choice_set), random.choice(choice_set)])

    weights1 = []
    for _ in range(24):
        weights1.append(np.random.uniform(size=16))
    bias1 = np.random.uniform(size=1)
    weights2 = []
    for _ in range(5):
        weights2.append(np.random.uniform(size=24))
    bias2 = np.random.uniform(size=1)

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
    pickle_out = open("kernel3.pickle", "wb")
    pickle.dump(kernel3, pickle_out)
    pickle_out.close()
    pickle_out = open("kernel4.pickle", "wb")
    pickle.dump(kernel4, pickle_out)
    pickle_out.close()
    pickle_out = open("kernel5.pickle", "wb")
    pickle.dump(kernel5, pickle_out)
    pickle_out.close()
    pickle_out = open("kernel6.pickle", "wb")
    pickle.dump(kernel6, pickle_out)
    pickle_out.close()
    pickle_out = open("weights1.pickle", "wb")
    pickle.dump(weights1, pickle_out)
    pickle_out.close()
    pickle_out = open("bias1.pickle", "wb")
    pickle.dump(bias1, pickle_out)
    pickle_out.close()
    pickle_out = open("weights2.pickle", "wb")
    pickle.dump(weights2, pickle_out)
    pickle_out.close()
    pickle_out = open("bias2.pickle", "wb")
    pickle.dump(bias2, pickle_out)
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

def classify(image_pixels, kernel1, kernel2, kernel3, kernel4, kernel5, kernel6, weights1, bias1, weights2, bias2):

    #Convolution layer 1
    reshaped_array1 = []
    weighted_pixel_net1_convolution1 = []
    weighted_pixel_relu1_convolution1 = [] #Main output layer
    weighted_pixel_net2_convolution1 = []
    weighted_pixel_relu2_convolution1 = []
    for y in range(7):
        square_row = []
        weighted_pixel_net_row1 = []
        weighted_pixel_relu_row1 = []
        weighted_pixel_net_row2 = []
        weighted_pixel_relu_row2 = []
        for x in range(10):
            square = [image_pixels[y][x:x+5], image_pixels[y+1][x:x+5], image_pixels[y+2][x:x+5], image_pixels[y+3][x:x+5], image_pixels[y+4][x:x+5]]

            weighted_pixel_net1 = (np.dot(square[0], kernel1[0]) + np.dot(square[1], kernel1[1]) + np.dot(square[2], kernel1[2]) + np.dot(square[3], kernel1[3]) + np.dot(square[4], kernel1[4]))/25
            weighted_pixel_relu1 = relu(weighted_pixel_net1)
            weighted_pixel_net2 = (np.dot(square[0], kernel2[0]) + np.dot(square[1], kernel2[1]) + np.dot(square[2], kernel2[2]) + np.dot(square[3], kernel2[3]) + np.dot(square[4], kernel2[4]))/25
            weighted_pixel_relu2 = relu(weighted_pixel_net2)

            square_row.append(square)
            weighted_pixel_net_row1.append(weighted_pixel_net1)
            weighted_pixel_relu_row1.append(weighted_pixel_relu1)
            weighted_pixel_net_row2.append(weighted_pixel_net2)
            weighted_pixel_relu_row2.append(weighted_pixel_relu2)

        reshaped_array1.append(square_row)
        weighted_pixel_net1_convolution1.append(weighted_pixel_net_row1)
        weighted_pixel_relu1_convolution1.append(weighted_pixel_relu_row1)
        weighted_pixel_net2_convolution1.append(weighted_pixel_net_row2)
        weighted_pixel_relu2_convolution1.append(weighted_pixel_relu_row2)

    #Pooling layer
    weighted_pixel_relu1_convolution1.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) #Added padding
    weighted_pixel_relu2_convolution1.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    pooled_array1 = []
    pooled_array2 = []
    for y in range(4):
        pooled_row1 = []
        pooled_row2 = []
        for x in range(5):
            square1 = [weighted_pixel_relu1_convolution1[y*2][2*x], weighted_pixel_relu1_convolution1[y*2][2*x+1], weighted_pixel_relu1_convolution1[y*2+1][2*x], weighted_pixel_relu1_convolution1[y*2+1][2*x+1]]
            pooled_row1.append(pool(square1)) #Somehow going to have to connect the corrected weight to its original matrice that created it while disregarding the others
            square2 = [weighted_pixel_relu2_convolution1[y*2][2*x], weighted_pixel_relu2_convolution1[y*2][2*x+1], weighted_pixel_relu2_convolution1[y*2+1][2*x], weighted_pixel_relu2_convolution1[y*2+1][2*x+1]]
            pooled_row2.append(pool(square2))
        pooled_array1.append(pooled_row1)
        pooled_array2.append(pooled_row2)

    #Convolutional layer 2
    reshaped_pool_array1 = []
    reshaped_pool_array2 = []
    weighted_pixel_net1_convolution2 = []
    weighted_pixel_relu1_convolution2 = []
    weighted_pixel_net2_convolution2 = []
    weighted_pixel_relu2_convolution2 = []
    weighted_pixel_net3_convolution2 = []
    weighted_pixel_relu3_convolution2 = []
    weighted_pixel_net4_convolution2 = []
    weighted_pixel_relu4_convolution2 = []
    for y in range(2):
        square_row1 = []
        square_row2 = []
        weighted_pixel_net_row1 = []
        weighted_pixel_relu_row1 = []
        weighted_pixel_net_row2 = []
        weighted_pixel_relu_row2 = []
        weighted_pixel_net_row3 = []
        weighted_pixel_relu_row3 = []
        weighted_pixel_net_row4 = []
        weighted_pixel_relu_row4 = []
        for x in range(3):
            square1 = [pooled_array1[y][x:x+3], pooled_array1[y+1][x:x+3], pooled_array1[y+2][x:x+3]]
            square2 = [pooled_array2[y][x:x+3], pooled_array2[y+1][x:x+3], pooled_array2[y+2][x:x+3]]
            weighted_pixel_net1 = (np.dot(square1[0], kernel3[0]) + np.dot(square1[1], kernel3[1]) + np.dot(square1[2], kernel3[2]))/9
            weighted_pixel_net2 = (np.dot(square1[0], kernel4[0]) + np.dot(square1[1], kernel4[1]) + np.dot(square1[2], kernel4[2]))/9
            weighted_pixel_net3 = (np.dot(square2[0], kernel3[0]) + np.dot(square2[1], kernel3[1]) + np.dot(square2[2], kernel3[2]))/9
            weighted_pixel_net4 = (np.dot(square2[0], kernel4[0]) + np.dot(square2[1], kernel4[1]) + np.dot(square2[2], kernel4[2]))/9
            weighted_pixel_relu1 = relu(weighted_pixel_net1)
            weighted_pixel_relu2 = relu(weighted_pixel_net2)
            weighted_pixel_relu3 = relu(weighted_pixel_net3)
            weighted_pixel_relu4 = relu(weighted_pixel_net4)

            square_row1.append(square1)
            square_row2.append(square2)
            weighted_pixel_net_row1.append(weighted_pixel_net1)
            weighted_pixel_relu_row1.append(weighted_pixel_relu1)
            weighted_pixel_net_row2.append(weighted_pixel_net2)
            weighted_pixel_relu_row2.append(weighted_pixel_relu2)
            weighted_pixel_net_row3.append(weighted_pixel_net3)
            weighted_pixel_relu_row3.append(weighted_pixel_relu3)
            weighted_pixel_net_row4.append(weighted_pixel_net4)
            weighted_pixel_relu_row4.append(weighted_pixel_relu4)

        reshaped_pool_array1.append(square_row1)
        reshaped_pool_array2.append(square_row2)
        weighted_pixel_net1_convolution2.append(weighted_pixel_net_row1)
        weighted_pixel_relu1_convolution2.append(weighted_pixel_relu_row1)
        weighted_pixel_net2_convolution2.append(weighted_pixel_net_row2)
        weighted_pixel_relu2_convolution2.append(weighted_pixel_relu_row2)
        weighted_pixel_net3_convolution2.append(weighted_pixel_net_row3)
        weighted_pixel_relu3_convolution2.append(weighted_pixel_relu_row3)
        weighted_pixel_net4_convolution2.append(weighted_pixel_net_row4)
        weighted_pixel_relu4_convolution2.append(weighted_pixel_relu_row4)

    #Convolutional layer 3 (Max output layer flatten) (Output of last = weighted_pixel_reluN_convolution2)
    flattened_net = []
    flattened_relu = []
    for x in range(2):
        square1 = [weighted_pixel_relu1_convolution2[0][x:x+2], weighted_pixel_relu1_convolution2[1][x:x+2]]
        square2 = [weighted_pixel_relu2_convolution2[0][x:x+2], weighted_pixel_relu2_convolution2[1][x:x+2]]
        square3 = [weighted_pixel_relu3_convolution2[0][x:x+2], weighted_pixel_relu3_convolution2[1][x:x+2]]
        square4 = [weighted_pixel_relu4_convolution2[0][x:x+2], weighted_pixel_relu4_convolution2[1][x:x+2]]

        weighted_pixel_net1 = (np.dot(square1[0], kernel5[0]) + np.dot(square1[1], kernel5[1]))/4
        weighted_pixel_net2 = (np.dot(square1[0], kernel6[0]) + np.dot(square1[1], kernel6[1]))/4
        weighted_pixel_net3 = (np.dot(square2[0], kernel5[0]) + np.dot(square2[1], kernel5[1]))/4
        weighted_pixel_net4 = (np.dot(square2[0], kernel6[0]) + np.dot(square2[1], kernel6[1]))/4
        weighted_pixel_net5 = (np.dot(square3[0], kernel5[0]) + np.dot(square3[1], kernel5[1]))/4
        weighted_pixel_net6 = (np.dot(square3[0], kernel6[0]) + np.dot(square3[1], kernel6[1]))/4
        weighted_pixel_net7 = (np.dot(square4[0], kernel5[0]) + np.dot(square4[1], kernel5[1]))/4
        weighted_pixel_net8 = (np.dot(square4[0], kernel6[0]) + np.dot(square4[1], kernel6[1]))/4
        flattened_net.append(weighted_pixel_net1)
        flattened_net.append(weighted_pixel_net2)
        flattened_net.append(weighted_pixel_net3)
        flattened_net.append(weighted_pixel_net4)
        flattened_net.append(weighted_pixel_net5)
        flattened_net.append(weighted_pixel_net6)
        flattened_net.append(weighted_pixel_net7)
        flattened_net.append(weighted_pixel_net8)

        weighted_pixel_sigmoid1 = sigmoid(weighted_pixel_net1)
        weighted_pixel_sigmoid2 = sigmoid(weighted_pixel_net2)
        weighted_pixel_sigmoid3 = sigmoid(weighted_pixel_net3)
        weighted_pixel_sigmoid4 = sigmoid(weighted_pixel_net4)
        weighted_pixel_sigmoid5 = sigmoid(weighted_pixel_net5)
        weighted_pixel_sigmoid6 = sigmoid(weighted_pixel_net6)
        weighted_pixel_sigmoid7 = sigmoid(weighted_pixel_net7)
        weighted_pixel_sigmoid8 = sigmoid(weighted_pixel_net8)
        flattened_relu.append(weighted_pixel_sigmoid1)
        flattened_relu.append(weighted_pixel_sigmoid2)
        flattened_relu.append(weighted_pixel_sigmoid3)
        flattened_relu.append(weighted_pixel_sigmoid4)
        flattened_relu.append(weighted_pixel_sigmoid5)
        flattened_relu.append(weighted_pixel_sigmoid6)
        flattened_relu.append(weighted_pixel_sigmoid7)
        flattened_relu.append(weighted_pixel_sigmoid8)

    hidden_layer_net = []
    hidden_layer_sigmoid = []
    for i in range(24):
        z = np.dot(flattened_relu, weights1[i]) + bias1[0]
        hidden_layer_net.append(z)
        hidden_layer_sigmoid.append(sigmoid(z))

    output_layer_net = []
    output_layer_sigmoid = []
    for i in range(5):
        z = np.dot(hidden_layer_sigmoid, weights2[i]) + bias2[0]
        output_layer_net.append(z)
        output_layer_sigmoid.append(sigmoid(z))

    return [flattened_relu, hidden_layer_net, hidden_layer_sigmoid, output_layer_net, output_layer_sigmoid]

def train(image_pixels, label, learning_rate, kernel1, kernel2, kernel3, kernel4, kernel5, kernel6, weights1, bias1, weights2, bias2):

    out = classify(image_pixels, kernel1, kernel2, kernel3, kernel4, kernel5, kernel6, weights1, bias1, weights2, bias2)

    weights1old = weights1
    bias1old = bias1
    weights2old = weights2
    bias2old = bias2

    #Adjusting second layer of weights
    for a in range(5):
        for b in range(24):
            weights2[a][b] = weights2old[a][b] - -learning_rate*(label[a] - out[4][a])*sigmoidd(out[3][a])*out[2][b]
    bias2[0] = bias2old[0] - -learning_rate*(label[0] - out[4][0])*sigmoidd(out[3][0])

    #Find error for hidden layer
    hidden_layer_error = []
    for b in range(24):
        error = 0
        for a in range(5):
            error += -(label[a] - out[4][a])*sigmoidd(out[3][a])*weights2old[a][b]
        hidden_layer_error.append(error)

    #Adjusting first layer of weights
    for a in range(24):
        for b in range(16):
            weights1[a][b] = weights1old[a][b] - -learning_rate*hidden_layer_error[a]*sigmoidd(out[1][a])*out[0][b]
    bias1[0] = bias1old[0] - -learning_rate*hidden_layer_error[0]*sigmoid(out[1][0])

    pickle_out = open("weights2.pickle", "wb")
    pickle.dump(weights2, pickle_out)
    pickle_out.close()
    pickle_out = open("bias2.pickle", "wb")
    pickle.dump(bias2, pickle_out)
    pickle_out.close()
    pickle_out = open("weights1.pickle", "wb")
    pickle.dump(weights1, pickle_out)
    pickle_out.close()
    pickle_out = open("bias1.pickle", "wb")
    pickle.dump(bias1, pickle_out)
    pickle_out.close()

#create_training_data()
data = pickle.load(open("data.pickle", "rb"))
label = pickle.load(open("label.pickle", "rb"))
kernel1 = pickle.load(open("kernel1.pickle", "rb"))
kernel2 = pickle.load(open("kernel2.pickle", "rb"))
kernel3 = pickle.load(open("kernel3.pickle", "rb"))
kernel4 = pickle.load(open("kernel4.pickle", "rb"))
kernel5 = pickle.load(open("kernel5.pickle", "rb"))
kernel6 = pickle.load(open("kernel6.pickle", "rb"))
weights1 = pickle.load(open("weights1.pickle", "rb"))
bias1 = pickle.load(open("bias1.pickle", "rb"))
weights2 = pickle.load(open("weights2.pickle", "rb"))
bias2 = pickle.load(open("bias2.pickle", "rb"))

for i in range(len(data)):
    train(data[i], label[i], 0.5, kernel1, kernel2, kernel3, kernel4, kernel5, kernel6, weights1, bias1, weights2, bias2)
