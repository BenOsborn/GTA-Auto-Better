# GTA-Auto-Better
Created by Ben Osborn

A program which can automatically bet on horses featured in the GTA casino horse betting minigame. It selects the horse with the best chance of winning and max bets on it, and will repeat this cycle indefinitely. Created for educational purposes only.

To use the script you must first have a decent amount of chips within the casino. Since the bot relies on lucky, it's nice to have a high starting number, I would recommend starting with about 300k chips. Remember this script still relies on luck, so I am not responsible if you go broke within the game due to bad luck!

# Usage:
1. Load GTA at 1080p resolution on your main monitor
2. Goto the casino, load up the horse betting game, and load into the "single event" gamemode
3. Start the program "auto_better.py" and take your hands off of your mouse and keyboard, the program will run in the background by itself. If you move the mouse will the program is working, stop the program and restart it from the "single event" screen

NOTE:
No training data was ever made for numbers of 11 and 19, this could result in some errors when trying to compile the model for yourself. If you are trying to compile the model for yourself, create empty directories in the "training_data" section labelling them "11" and "19".
