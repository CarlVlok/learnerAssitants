import webbrowser
import os

base_dir = os.getcwd()
fp = os.path.join(base_dir, "data/studyGuides")
files = os.listdir(fp)
print(type(files[0]))
webbrowser.open(fp+"/"+files[0], 2)