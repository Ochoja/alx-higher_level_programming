#!/usr/bin/python3

# print numbers from 0 - 99
for i in range(0, 100):
    if i == 99:
        print("{}".format(i))
    else:
        print(f"{i:02d}", end=", ")
