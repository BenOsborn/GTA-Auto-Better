import pyautogui as gui
from PIL import Image, ImageOps
from time import sleep
import numpy as np
import pynput.mouse as mouse
import pynput.keyboard as keyboard
import cv2

#image = cv2.imread(r"C:\Users\bengr\Documents\Programs\GTA-Auto-Better\training_data\n1.jpg")

mousecontroller = mouse.Controller()

def auto_bet(x, y):
    mousecontroller.position = (x, y)
    mousecontroller.press(mouse.Button.left)
    sleep(0.1)
    mousecontroller.release(mouse.Button.left)
    mousecontroller.position = (1526, 513) #Bet amount position
    for _ in range(28):
            mousecontroller.press(mouse.Button.left)
            sleep(0.05)
            mousecontroller.release(mouse.Button.left)
            sleep(0.05)
    mousecontroller.position = (1321, 787) #Place bet
    mousecontroller.press(mouse.Button.left)
    sleep(0.1)
    mousecontroller.release(mouse.Button.left)
    sleep(39)
    mousecontroller.position = (950, 985) #Position of bet again
    sleep(0.1)
    mousecontroller.press(mouse.Button.left)
    sleep(0.1)
    mousecontroller.release(mouse.Button.left)
    mousecontroller.position = (1430, 890) #Position of place bet
    sleep(0.1)
    mousecontroller.press(mouse.Button.left)
    sleep(0.1)
    mousecontroller.release(mouse.Button.left)
    sleep(0.1)

def main_auto():

    images = []
    for h in range(6):
        img = gui.screenshot(region=(175, 340 + 120*h, 60, 50))
        img = np.array(img)
        img = cv2.resize(img, (14, 12), interpolation=cv2.INTER_AREA) #Why is this 8*8 lol?
        img = ImageOps.grayscale(img)
        img = np.array(img)
        images.append(img)

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

def on_press(key):

    key_pressed = str(key)[1:-1]

    if key_pressed == "1":
        auto_bet(210, 340)
    elif key_pressed == "2":
        auto_bet(210, 450)
    elif key_pressed == "3":
        auto_bet(210, 570)
    elif key_pressed == "4":
        auto_bet(210, 690)
    elif key_pressed == "5":
        auto_bet(210, 800)
    elif key_pressed == "6":
        auto_bet(210, 920)
    if key_pressed == "g":
        exit()
    else:
        pass

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
