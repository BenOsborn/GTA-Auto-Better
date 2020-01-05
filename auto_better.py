import pyautogui as gui
from PIL import Image, ImageOps
from time import sleep
import numpy as np
#from pynput import mouse

weight_set1 = []
for _ in range(8):
    weight_set1.append(np.random.uniform(size=625))
b1 = [np.random.uniform(size=1)]
weight_set2 = []
for _ in range(16):
    weight_set2.append(np.random.uniform(size=8))
b2 = [np.random.uniform(size=1)]
weight_set3 = np.random.uniform(size=16)
b3 = [np.random.uniform(size=1)]

def bet_algorithm():

    images = []
    for h in range(6):
        img = gui.screenshot(region=(175, 340 + 120*h, 100, 50))
        img = ImageOps.grayscale(img)
        images.append(img)
