import os

def makefile(path,content=""):
    with open(path, "w") as file:
        file.write(content)

if os.path.exists("folder"):
    makefile("folder\\file.txt")
else:
    os.mkdir("folder")
    makefile("folder\\file.txt")
