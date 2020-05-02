import cv2
import os
import numpy as np
import random
import tensorflow as tf
import keras

def highlight(image_array):
    for y in range(len(image_array)):
        for x in range(len(image_array[0])):
            if image_array[y][x] < 40:
                image_array[y][x] = 0
            else:
                image_array[y][x] = 1
    return image_array

if __name__ == "__main__":
    CWD = os.getcwd()
    DATADIR = os.path.join(CWD, "training_data")
    MODELPATH = os.path.join(CWD, "model")
    CATEGORIES = [str(i) for i in range(1, 31)]

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

    training_data_shuffled = sorted(training_data, key=lambda k: random.random())

    data = np.array([sets[0] for sets in training_data_shuffled])
    labels = np.array([sets[1] for sets in training_data_shuffled])

    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(48, 56)),
        keras.layers.Dense(128, activation=tf.nn.relu),
        keras.layers.Dense(31, activation=tf.nn.softmax)
    ])
    model.compile(optimizer="adam",
                loss="sparse_categorical_crossentropy",
                metrics=["accuracy"])
    model.fit(data, labels, epochs=10)

    model.save(os.path.join(MODELPATH, "model.h5"))
