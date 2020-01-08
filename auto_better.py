import pyautogui as gui
from PIL import Image, ImageOps
from time import sleep
import numpy as np
from pynput.mouse import Button, Controller
import cv2

#image = cv2.imread(r"C:\Users\bengr\Documents\Programs\GTA-Auto-Better\training_data\n1.jpg")

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

def main():

    images = []
    for h in range(6):
        img = gui.screenshot(region=(175, 340 + 120*h, 60, 50))
        img = np.array(img)
        img = cv2.resize(img, (8, 8), interpolation=cv2.INTER_AREA)
        img = cv2.Canny(img, 100, 200)
        img = Image.fromarray(img)
        img = ImageOps.grayscale(img)
        img = np.array(img)
        new_img = []
        for row in img:
            for pixel in row:
                new_img.append(pixel / 255)
        images.append(new_img)

    horse = {}
    for h in range(6):
        horse[h + 1] = classification(images[h])

    horse_sorted = sorted(horse.items(), key = lambda t:t[1])

    value = list(horse_sorted)[0][0]

    if value == 1:
        print("1")
        #auto_bet(210, 340)
    elif value == 2:
        print("2")
        #auto_bet(210, 450)
    elif value == 3:
        print("3")
        #auto_bet(210, 570)
    elif value == 4:
        print("4")
        #auto_bet(210, 690)
    elif value == 5:
        print("5")
        #auto_bet(210, 800)
    elif value == 6:
        print("6")
        #auto_bet(210, 920)

main()
