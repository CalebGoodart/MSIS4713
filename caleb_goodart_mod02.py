#! python3

# Program by Caleb Goodart
# MSIS4713
# Mod02


import sys


def fuc(x):
    return (x**x) + x


while True:
    try:
        num = int(input("Please enter an integer between 1 and 10: "))
        if num < 1 or num > 10:
            print("Integer out of bounds.  Please try again.")
            continue
        else:
            print(str(fuc(num)) + "\n")
            if input("Press Q to exit, anything else to go again:  \n") == "Q":
                break
    except:
        print("That is not an integer.  Please try again.  \n")
