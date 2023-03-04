import os

path = "/Users/maxpaulino/Desktop/Java/LunarMile/fusilli/Python/bar_graph/numbered copy/"
files = os.listdir(path)

for i in range(len(files)):
    if files[i] != '.DS_Store':
        splitOnDot = files[i].split(".")
        splitted = splitOnDot[0].split("_")
        os.replace(path+files[i], str(i) + ".png")

print(f"After Renaming: {os.listdir(path)}")
