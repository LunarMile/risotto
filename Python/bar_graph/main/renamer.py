import os
from datetime import datetime

path = "/Users/maxpaulino/Desktop/Java/LunarMile/fusilli/Python/bar_graph/finalphoto_copy copy/"
files = list(os.listdir(path))
files.sort()
for i in range(len(files)):
    if files[i] != '.DS_Store':
        os.replace(path+files[i], str(i) + ".png")

print(f"After Renaming: {os.listdir(path)}")

