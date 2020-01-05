import pyautogui as gui
from PIL import ImageOps
from time import sleep
'''
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
'''
img = gui.screenshot(region=(175, 700, 100, 50))
img = ImageOps.grayscale(img)
img_pixels = np.array(img)
