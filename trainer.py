from auto_better_framework import *
import os


image_files = []
for files in os.walk(r"C:\Users\bengr\Documents\Programs\GTA-Auto-Better\training_data"):
    for file in files[2]:
        image_files.append(file)

print(image_files)

for i in range(len(image_files)):
    
