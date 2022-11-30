#!/usr/bin/python3

# Print numbers from 1 to 100
# Replace multiples of 3 with Fizz and multiples of 5 with Buzz
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz ", end="")
        elif i % 3 == 0:
            print("Fizz ", end="")
        elif i % 5 == 0:
            print("Buzz ", end="")
        else:
            print(f"{i} ", end="")
