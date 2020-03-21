import pyautogui as gui
from PIL import ImageOps
from time import sleep
import numpy as np
import pynput.mouse as mouse
import cv2
import pickle
import tensorflow as tf
from tensorflow import keras

CWD = os.getcwd()
PICKLEPATH = os.path.join(CWD, "pickles")

data = pickle.load(open(os.path.join(PICKLEPATH, "data.p"), "rb"))
label = pickle.load(open(os.path.join(PICKLEPATH, "label.p"), "rb"))

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(48, 56)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(30, activation=tf.nn.softmax)
])

model.compile(optimizer="adam",
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])

model.fit(data, label, epochs=10)

def highlight(image_array):
    for y in range(len(image_array)):
        for x in range(len(image_array[0])):
            if image_array[y][x] < 40:
                image_array[y][x] = 0
            else:
                image_array[y][x] = 1 #255
    return image_array

def auto_bet(x, y):
    mouse.Controller().position = (x, y)
    mouse.Controller().press(mouse.Button.left)
    sleep(0.1)
    mouse.Controller().release(mouse.Button.left)
    mouse.Controller().position = (1526, 513)
    for _ in range(28):
            mouse.Controller().press(mouse.Button.left)
            sleep(0.05)
            mouse.Controller().release(mouse.Button.left)
            sleep(0.05)
    mouse.Controller().position = (1321, 787)
    mouse.Controller().press(mouse.Button.left)
    sleep(0.1)
    mouse.Controller().release(mouse.Button.left)
    sleep(39)
    mouse.Controller().position = (950, 985)
    sleep(0.1)
    mouse.Controller().press(mouse.Button.left)
    sleep(0.1)
    mouse.Controller().release(mouse.Button.left)
    mouse.Controller().position = (1430, 890)
    sleep(0.1)
    mouse.Controller().press(mouse.Button.left)
    sleep(0.1)
    mouse.Controller().release(mouse.Button.left)
    sleep(0.1)

def main_auto():

    images = []
    for h in range(6):
        img = gui.screenshot(region=(180, 340 + 121*h, 56, 48))
        img = ImageOps.grayscale(img)
        img = highlight(np.array(img))
        images.append(np.array(img))
    images = np.array(images)

    predictions = model.predict(images)

    min_values = []
    for prediction in predictions:
        indexed_predictions = {}
        for i in range(len(prediction)):
            indexed_predictions[i + 1] = prediction[i]
        prediction_sorted = sorted(indexed_predictions.items(), key = lambda t:t[1])
        min_values.append(list(prediction_sorted)[-1][0])

    min_values_sorted = {}
    for i in range(6):
        min_values_sorted[i + 1] = min_values[i]
    values_sorted = sorted(min_values_sorted.items(), key = lambda t:t[1])
    value = list(values_sorted)[0][0]

    if value == 1:
        auto_bet(210, 340)
    elif value == 2:
        auto_bet(210, 450)
    elif value == 3:
        auto_bet(210, 570)
    elif value == 4:
        auto_bet(210, 690)
    elif value == 5:
        auto_bet(210, 800)
    elif value == 6:
        auto_bet(210, 920)
    else:
        pass
    
sleep(3)
while True:
    main_auto()
