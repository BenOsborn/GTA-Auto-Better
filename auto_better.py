import pyautogui as gui
from PIL import ImageOps
from time import sleep
import numpy as np
import pynput.mouse as mouse
import cv2
import tensorflow as tf
from keras.models import load_model
from keras.utils import get_custom_objects
import os

def highlight(image_array):
    for y in range(len(image_array)):
        for x in range(len(image_array[0])):
            if image_array[y][x] < 40:
                image_array[y][x] = 0
            else:
                image_array[y][x] = 1 #255
    return image_array

def auto_bet(x, y):
    mCTRL = mouse.Controller()
    mCTRL.position = (x, y)
    mCTRL.press(mouse.Button.left)
    sleep(0.1)
    mCTRL.release(mouse.Button.left)
    mCTRL.position = (1526, 513)
    for _ in range(28):
            mCTRL.press(mouse.Button.left)
            sleep(0.05)
            mCTRL.release(mouse.Button.left)
            sleep(0.05)
    mCTRL.position = (1321, 787)
    mCTRL.press(mouse.Button.left)
    sleep(0.1)
    mCTRL.release(mouse.Button.left)
    sleep(39)
    mCTRL.position = (950, 985)
    sleep(0.1)
    mCTRL.press(mouse.Button.left)
    sleep(0.1)
    mCTRL.release(mouse.Button.left)
    mCTRL.position = (1430, 890)
    sleep(0.1)
    mCTRL.press(mouse.Button.left)
    sleep(0.1)
    mCTRL.release(mouse.Button.left)
    sleep(0.1)

def main_auto(model):

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

if __name__ == "__main__":
    print("Welcome to Ben Osborn's auto bet bot!")
 
    CWD = os.getcwd()
    MODELPATH = os.path.join(CWD, "model")
    get_custom_objects().update({"softmax_v2": tf.nn.softmax})
    model = load_model(os.path.join(MODELPATH, "model.h5"))

    for i in range(3):
        print(f"Commencing in {3-i}...")
        sleep(1)

    while True:
        main_auto(model)
