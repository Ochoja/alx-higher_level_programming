#!/usr/bin/python3
with open("myText.txt", encoding="utf-8") as myFile:
    lineNum = 1

    while True:
        line = myFile.readline()

        if not line:
            break

        print("{} char:{}".format(line, len(line)), end="")
