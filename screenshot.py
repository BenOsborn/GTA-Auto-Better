import pyautogui as gui
from pynput.keyboard import Key, Listener
import os

CWD = os.getcwd()
TRAINDIR = os.path.join(CWD, "training_data")

i = [1]

try:

    numbers = []
    for files in os.walk(TRAINDIR):
        for file in files[2]:
            numbers.append(int(file[1:-4]))
    numbers.sort()

    i[0] = numbers[-1] + 1

except:

    i[0] = 1

def screenshot(key):

    if str(key)[1] == "c":

        for a in range(6):

            img = gui.screenshot(region=(180, 340 + 121*a, 56, 48))
            img.save(os.path.join(TRAINDIR, ("n" + str(i[0]) + ".jpg")))
            i[0] += 1

    else:

        pass

with Listener(on_press=screenshot) as listener:
    listener.join()
