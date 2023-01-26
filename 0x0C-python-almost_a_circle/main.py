#!/usr/bin/python3
""" 15-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(13, 7, 2, 8)
    r2 = Rectangle(5, 4)
    Rectangle.save_to_file([r1, r2])
