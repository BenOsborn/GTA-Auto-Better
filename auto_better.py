import pyautogui as gui
from PIL import Image, ImageOps
from time import sleep
import numpy as np
from pynput.mouse import Button, Controller

mouse = Controller()

def auto_bet(x_dimension, y_dimension):
    mouse.position = (x_dimension, y_dimension)
    sleep(0.05)
    mouse.click(Button.left, 1)
    sleep(0.05)
    mouse.position = (1526, 513) #Bet amount position
    sleep(0.05)
    mouse.click(Button.left, 27)
    sleep(0.05)
    mouse.position = (1321, 787) #Place bet
    sleep(0.05)
    mouse.click(Button.left, 1)
    sleep(40)
    mouse.position = (950, 985) #Position of bet again
    sleep(0.05)
    mouse.click(Button.left, 1)
    sleep(0.05)
    mouse.position = (1430, 890) #Position of place bet
    sleep(0.05)
    mouse.click(Button.left, 1)
    sleep(0.05)

def main(weights1, bias1, weights2, bias2, weights3, bias3):

    images = []
    for h in range(6):
        img = gui.screenshot(region=(175, 340 + 120*h, 100, 50))
        img = ImageOps.grayscale(img)
        images.append(np.array(img))

    horse = {}
    for h in range(6):
        horse[h + 1] = round(classification(images[h], weights1, bias1, weights2, bias2, weights3, bias3), 0)

    horse_sorted = sorted(horse.items(), key = lambda t:t[1])

    value = list(horse_sorted)[0][0]

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

print(main(weight_set1, b1, weight_set2, b2, weight_set3, b3))
