import pyautogui as gui
from pynput.keyboard import Key, Listener

img = gui.screenshot(region=(175, 700, 100, 50))

i = [1]

def screenshot(key):

    if str(key)[1] == "c":

        img = gui.screenshot(region=(175, 340, 100, 50))
        img.save(r"C:\Users\bengr\Documents\Programs\GTA-Auto-Better\training_data\n" + str(i[0]) + ".jpg")
        i[0] += 1
        img = gui.screenshot(region=(175, 460, 100, 50))
        img.save(r"C:\Users\bengr\Documents\Programs\GTA-Auto-Better\training_data\n" + str(i[0])  + ".jpg")
        i[0] += 1
        img = gui.screenshot(region=(175, 580, 100, 50))
        img.save(r"C:\Users\bengr\Documents\Programs\GTA-Auto-Better\training_data\n" + str(i[0])  + ".jpg")
        i[0] += 1
        img = gui.screenshot(region=(175, 700, 100, 50))
        img.save(r"C:\Users\bengr\Documents\Programs\GTA-Auto-Better\training_data\n" + str(i[0])  + ".jpg")
        i[0] += 1
        img = gui.screenshot(region=(175, 820, 100, 50))
        img.save(r"C:\Users\bengr\Documents\Programs\GTA-Auto-Better\training_data\n" + str(i[0])  + ".jpg")
        i[0] += 1
        img = gui.screenshot(region=(175, 940, 100, 50))
        img.save(r"C:\Users\bengr\Documents\Programs\GTA-Auto-Better\training_data\n" + str(i[0])  + ".jpg")
        i[0] += 1

    else:
        pass

with Listener(on_press=screenshot) as listener:
    listener.join()
