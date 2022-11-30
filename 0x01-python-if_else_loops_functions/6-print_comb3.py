#!/usr/bin/python3

count = 1
for i in range(0, 9):
    for j in range(count, 10):
        if i == 8:
            print("{}{}".format(i, j))
        else:
            print(f"{i}{j}", end=", ")
    count += 1
