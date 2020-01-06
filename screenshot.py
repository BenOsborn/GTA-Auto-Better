import pyautogui as gui
from pynput.keyboard import Key, Listener
import os

numbers = []
for files in os.walk(r"C:\Users\bengr\Documents\Programs\GTA-Auto-Better\training_data"):
    for file in files[2]:
        numbers.append(int(file[1:-4]))
numbers.sort()

i = [numbers[-1] + 1]

def screenshot(key):

    if str(key)[1] == "c":

        for a in range(6):

            img = gui.screenshot(region=(175, 340 + 120*a, 100, 50))
            img.save(r"C:\Users\bengr\Documents\Programs\GTA-Auto-Better\training_data\n" + str(i[0]) + ".jpg")
            i[0] += 1

    else:

        pass

with Listener(on_press=screenshot) as listener:
    listener.join()
