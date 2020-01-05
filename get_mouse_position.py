from pynput.mouse import Listener

def on_move(x, y):
    print(x, y)

with Listener(on_move=on_move) as listener:
    listener.join()
